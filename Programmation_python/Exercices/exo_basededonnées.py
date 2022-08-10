import sqlite3
from sqlite3 import Error

#Creating a New Database

def create_connection0(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


#if __name__ == '__main__':
    #create_connection0(r"C:\Users\yohan\OneDrive\Bureau\Formations\Cours\Programmation_python\pythonsqlite.db")

#Creating Tables

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

#Main fonction pour créer les tables, insérer les données 
def main():
    database = r"pythonsqlite.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")

    with conn:
        # create a new project
        project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
        project_id = create_project(conn, project)

        # tasks
        task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

        # create tasks
        create_task(conn, task_1)
        create_task(conn, task_2)
        
#Insertion des données
def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

#Vérifier les tables
def get_tables():
    database = r"pythonsqlite.db"
    con = sqlite3.connect(database)
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())

#Vérifier l'insertion des données
def select_all_tasks():
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    database = r"pythonsqlite.db"
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute("SELECT * FROM tasks")
        

    rows = cur.fetchall()

    for row in rows:
        print(row)
    print(f"Nombre de lignes: {len(rows)}")

# Supprimer une seule ligne
def deleteRecord(id):
    try:
        sqliteConnection = sqlite3.connect('pythonsqlite.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_delete_query = """DELETE from tasks where id = ?"""
        cursor.execute(sql_delete_query, (id,))
        sqliteConnection.commit()
        print("Record deleted successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete record from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

# Supprimer plusieurs lignes
def deleteMultipleRecords(idList):
    try:
        sqliteConnection = sqlite3.connect('pythonsqlite.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_update_query = """DELETE from tasks where id = ?"""

        cursor.executemany(sqlite_update_query, idList)
        sqliteConnection.commit()
        print("Total", cursor.rowcount, "Records deleted successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete multiple records from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

if __name__ == '__main__':
    main()
    get_tables()
    select_all_tasks()
    #deleteRecord(23)
    id_to_delete=[(23,),(24,),(25,),(26,),(27,),(28,)]
    #deleteMultipleRecords(id_to_delete)
