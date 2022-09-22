from pyflink.table import (TableEnvironment, EnvironmentSettings, 
                           DataTypes,  CsvTableSource)

def main():

    #defined the environment settings and passed this object to TableEnvironment.create() method to generate the table environment I am going to use to import data
    env_settings = EnvironmentSettings.new_instance()\
                                      .build()

    tbl_env = TableEnvironment.create(env_settings)

    #stored both column_names and column_types (using DataTypes to define the dataset schema) as lists
    column_names = ['Username', 'Identifier', 'First_name', 'Last_name']
    
    column_types = [DataTypes.STRING(), DataTypes.INT(), DataTypes.STRING(), DataTypes.STRING()]

    #used the CsvTableSource() class - together with the local path to the file - to create a data source
    source = CsvTableSource(
        './myfile.csv',
        column_names,
        column_types,
        ignore_first_line=True
    )

    #registered the CSV source under test name and created an actual table tbl, by passing the source name to the from_path() method
    tbl_env.register_table_source('test', source)
    
    tbl = tbl_env.from_path('test')
    
    #visualisation
    print('\nRegistered Tables List')
    print(tbl_env.list_tables())

    print('\nTest Schema')
    tbl.print_schema()

    print('\nTest Data')
    print(tbl.to_pandas()) 
    
    print('\nTest execution')
    tbl.limit(10).execute().print()
    
if __name__ == '__main__':
    main()