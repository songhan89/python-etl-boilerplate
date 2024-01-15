import argparse 
from config.config import PIPELINE_CONFIG
from utils.logger import setup_logger
from db.connect import connect_to_db
from etl.etl import parse_data

# Get logger
log = setup_logger()


def main():

    # Create an ArgumentParser object
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument('--dry-run', type=bool, default=False,
                        dest='is_dry_run',
                        help='Run the ETL pipeline without writing to the database.')

    # Parse the arguments
    args = parser.parse_args()
    log.debug(args)

    # Get config
    log.debug(PIPELINE_CONFIG)

    # Start pipeline
    log.info('Starting the pipeline.')
    engine = connect_to_db()
    
    import pandas as pd

    for var, cfg in PIPELINE_CONFIG.items():
        df = parse_data(var, cfg)
        log.debug(f'Parsed data for {var}.')

        # Check if the data is already in the database
        min_date = df['datetime'].min()
        db_max_date = pd.read_sql(
            f"""SELECT MAX(datetime) as datetime
            FROM silver.{cfg['table']}
            WHERE datetime >= '{min_date}'
            """, engine)
        if db_max_date.datetime.values != None:
            date_filter = pd.to_datetime(db_max_date['datetime'], utc=True)
            # Filter out data that is already in the database
            df = df[df.datetime.values > date_filter.values].reset_index()

        if args.is_dry_run:
            log.info(f'Dry run. Not updating database for {var}.')
        else:
            log.info(f'Writing data to the database for {var}.')
            df.to_sql(name=cfg['table'], con=engine,
                      schema=cfg['schema'], index=False,
                      if_exists='append', method='multi')
            log.info(f'Data updated in the database for {var}.')
        





if __name__ == '__main__':
    main()

    