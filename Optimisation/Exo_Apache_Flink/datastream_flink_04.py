from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment
from pyflink.table import (TableEnvironment, EnvironmentSettings, 
                           DataTypes,  CsvTableSource)

env_settings = EnvironmentSettings.new_instance()\
                                .build()

tbl_env = TableEnvironment.create(env_settings)

source_path = './transactions_bigdata.csv'

def create_source(input_path, env):

    
    my_source_ddl = """
        create table source (
            agency_id BIGINT,
            account_sender_name VARCHAR,
            country_sender VARCHAR,
            account_receiver_name VARCHAR,
            country_receiver VARCHAR,
            amount BIGINT,
            payment_type VARCHAR,
            datetime_timestamp BIGINT
        ) with (
            'connector' = 'filesystem',
            'csv.ignore-parse-errors' = 'true',
            'format' = 'csv',
            'path' = '{}'
        )
    """.format(source_path)

    tbl_env.execute_sql(my_source_ddl)
  

create_source(source_path, tbl_env)

# get the result
result = tbl_env.execute_sql("SELECT * FROM source")

#result.print()

with result.collect() as res:
    for r in res:
        print(list(r))
