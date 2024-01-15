# Boilerplate for Python ETL Pipeline

This is a boilerplate Python repository is a Python ETL (Extract, Transform, Load) pipeline for ingesting data. The pipeline reads in a .csv file, melts the columns except date and time, and writes them to different PostgreSQL tables.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need Python 3.6 or later to run this project. You will also need PostgreSQL installed on your machine.

### Getting Started

1. Set up your PostgreSQL credentials in a `.env` file in the root directory of the project. The file should have the following format:

```
POSTGRES_USER=yourusername
POSTGRES_PASSWORD=yourpassword
```

2. Set up your PostgreSQL configuration in the `config.json` file. The file should have the following format:

```json
{
  "database": "analytics_db",
  "host": "localhost",
  "port": 5432,
  "data": { // The data object contains the configuration for each data source.
    "dry_bulb": {
      "vector": false, // Set to true if the data source contains vector data.
      "source": "./input/test.csv", // The path to the data source.
      "columns": ["date", "time", "station_id", "dry_bulb"], // The columns of data source.
      "unit": "[deg C]", // The unit of the data source. This is removed from the column name.
      "table": "aws_drybulb_1_min" // The name of the PostgreSQL table to write to.
    }
  }
}



```

## Usage

To run the project, navigate to the `src` directory and run the `main.py` script:

```
python ./src/main.py
```

To run the script without writing to the database, use the `--dry-run` flag:
```
python ./src/main.py --dry-run True
```

```bash
usage: main.py [-h] [--dry-run IS_DRY_RUN]

optional arguments:
  -h, --help            show this help message and exit
  --dry-run IS_DRY_RUN  Run the ETL pipeline without writing to the database.
```



## Project Structure

- `src/main.py`: Main script that runs the ETL pipeline.
- `src/etl.py`: Contains the ETL pipeline functions.
- `src/config.py`: Reads the configuration from `config.json` and the PostgreSQL credentials from the `.env` file.
- `src/logger.py`: Sets up the logging configuration.
- `config/config.json`: Stores the configuration for the PostgreSQL database.
- `.env`: Stores the PostgreSQL username and password.

## Author

Wong Songhan