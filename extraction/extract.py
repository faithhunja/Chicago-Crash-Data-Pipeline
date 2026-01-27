# Import modules
import certifi
import json
import pandas as pd
import sqlite3
import urllib3
import logging

# Define top level module logger
logger = logging.getLogger(__name__)

# Extract data from csv file
def source_data_from_csv(csv_file_name):
    try:
        df_csv = pd.read_csv(csv_file_name)
        logger.info(f'{csv_file_name}: extracted {df_csv.shape[0]} records from the csv file')
    except Exception as e:
        logger.exception(f'{csv_file_name}: - exception {e} encountered while extracting the csv file')
        df_csv = pd.DataFrame()
    return df_csv

# Extract data from parquet file
def source_data_from_parquet(parquet_file_name):
    try:
        df_parquet = pd.read_parquet(parquet_file_name)
        logger.info(f'{parquet_file_name}: extracted {df_parquet.shape[0]} records from the parquet file')
    except Exception as e:
        logger.exception(f'{parquet_file_name} : - exception {e} encountered while extracting the parquet file')
        df_parquet = pd.DataFrame()
    return df_parquet

# Extract data from an api
def source_data_from_api(api_endpoint):
    try:
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        api_response = http.request('GET', api_endpoint)
        apt_status = api_response.status
        if apt_status == 200:
            logger.info(f'{apt_status} - ok: while invoking the API {api_endpoint}')
            data = json.loads(api_response.data.decode('utf-8'))
            df_api = pd.json_normalize(data)
            logger.info(f'{apt_status} - extracted {df_api.shape[0]} records from the API')
        else:
            logger.error(f'{apt_status} - error: while invoking the api {api_endpoint}')
            df_api = pd.DataFrame()
    except Exception as e:
        logger.exception(f'{apt_status} - exception {e} encountered while reading data from the API')
        df_api = pd.DataFrame()
    return df_api

# Extract data from a database table
def source_data_from_db(db_name, table_name):
    try:
        with sqlite3.connect(db_name) as conn:
            df_table = pd.read_sql(f"SELECT * FROM {table_name}", conn)
            logger.info(f'{db_name}- read {df_table.shape[0]} records from the table: {table_name}')
    except Exception as e:
        logger.exception(f'{db_name} : - exception {e} encountered while reading data from the table: {table_name}')
        df_table = pd.DataFrame()
    return df_table

# Extract data from all the data sources
def extracted_data():
    csv_file_name = "h9gi-nx95.csv"
    parquet_file_name = "yellow_tripdata_2022-01.parquet"
    api_endpoint = 'https://data.cityofnewyork.us/resource/h9gi-nx95.json?$limit=500'
    db_name = "movies.sqlite"
    table_name = "movies"

    df_csv, df_parquet, df_api, df_db = (source_data_from_csv(csv_file_name),
                                         source_data_from_parquet(parquet_file_name),
                                         source_data_from_api(api_endpoint),
                                         source_data_from_db(db_name, table_name))
    return df_csv, df_parquet, df_api, df_db
