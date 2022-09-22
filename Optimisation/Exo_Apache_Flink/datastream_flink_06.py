from pyflink.table import (TableEnvironment, EnvironmentSettings, 
                           DataTypes,  CsvTableSource)


env_settings = EnvironmentSettings.new_instance()\
                                .build()

tbl_env = TableEnvironment.create(env_settings)

source_path = './fin_trxs.csv'

source_ddl = f"""
            create table financial_trxs_2 (
            trx_id BIGINT,
            trx_date DATE,
            src_curr VARCHAR,
            amnt_src_curr FLOAT,
            amnt_gbp FLOAT,
            user_id BIGINT,
            user_type VARCHAR,
            user_country VARCHAR
            ) 
            with (
            'connector' = 'filesystem',
            'format' = 'csv',
            'path' = '{source_path}'
        )
        """

tbl_env.execute_sql(source_ddl) 

tbl = tbl_env.from_path("financial_trxs_2")

print(tbl.to_pandas()) ### or 
tbl.limit(10).execute().print()  