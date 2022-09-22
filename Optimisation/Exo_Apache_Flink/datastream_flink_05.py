from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import *
from pyflink.table.expressions import col

# environment configuration
env_settings  = EnvironmentSettings\
                .new_instance()\
                .in_streaming_mode()\
                .build()

tbl_env = TableEnvironment.create(env_settings)

# register Orders table and Result table sink in table environment
source_data_path = "C:/Users/yohan/OneDrive/Bureau/Formations/Projets/house_clean.csv"
result_data_path = "C:/Users/yohan/OneDrive/Bureau/Formations/Cours/Optimisation"

def create_source(path, env):
    source_ddl = f"""
            create table Source(
                nb_room INT,
                price FLOAT
            ) with (
                'connector' = 'filesystem',
                'format' = 'csv',
                'csv.ignore-parse-errors' = 'true',
                'path' = '{source_data_path}'
            )
            """
    tbl_env.execute_sql(source_ddl)

def create_sink(env):
    sink_ddl = f"""
        create table `Result`(
            avg_room FLOAT,
            avg_price FLOAT
        ) with (
            'connector' = 'filesystem',
            'format' = 'csv',
            'path' = '{result_data_path}'
        )
        """
    tbl_env.execute_sql(sink_ddl)


create_source(source_data_path, tbl_env)
create_sink(tbl_env)

print(tbl_env.list_tables())

#orders.group_by(col("account_sender_name")).select(col("account_sender_name"), col("amount").count.alias('cnt')).execute_insert("Result").wait()

tbl_env.execute_sql("INSERT INTO Result SELECT AVG(nb_room), AVG(price) FROM Source").wait()