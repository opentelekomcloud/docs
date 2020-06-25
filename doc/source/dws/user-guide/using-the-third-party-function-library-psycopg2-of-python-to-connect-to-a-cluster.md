# Using the Third-Party Function Library psycopg2 of Python to Connect to a Cluster<a name="dws_01_0120"></a>

After creating a data warehouse cluster and using the third-party function library psycopg2 to connect to the cluster, you can use Python to access DWS and perform various operations on data tables.

## Preparations Before Connecting to a Cluster<a name="section5781841515252"></a>

-   An EIP has been bound to the data warehouse cluster.
-   You have obtained the administrator username and password for logging in to the database in the data warehouse cluster.
-   You have obtained the public network address, including the IP address and port number in the data warehouse cluster. For details, see section  [Obtaining the Cluster Connection Address](obtaining-the-cluster-connection-address.md).
-   You have installed the third-party function library psycopg2. Download link:  [https://pypi.org/project/psycopg2/](https://pypi.org/project/psycopg2/)

## Using the Third-Party Function Library psycopg2 to Connect to a Cluster \(Linux\)<a name="section2825650154610"></a>

1.  Log in to the Linux environment as user  **root**.
2.  Run the following command to create the  **python\_dws.py**  file and copy the following content to the file:

    **vi python\_dws.py**

    ```
    #!/usr/bin/python
    # -*- coding: UTF-8 -*-
    
    import psycopg2
    def CreateTable(connection):
        print "Begin to create table"
        try:
            cursor = connection.cursor()
            cursor.execute('''drop table if exists test;create table test(id int, name text);''')
            #print "Table created successfully"
            connection.commit()
        except psycopg2.ProgrammingError,e:
            print e
        else:
            print "Table created successfully"
            cursor.close()
    
    
    def InsertData(connection):
        print "Begin to insert data"
        try:
            cursor = connection.cursor()
            cursor.execute("insert into test values(1,'number1');")
            cursor.execute("insert into test values(2,'number2');")
            cursor.execute("insert into test values(3,'number3');")
            connection.commit()
        except psycopg2.ProgrammingError,e:
            print e
        else:
            print "Insert data successfully"
            cursor.close()
    
    
    def UpdateData(connection):
        print "Begin to update data"
        try:
            cursor = connection.cursor()
            cursor.execute("update test set name = 'numberupdated' where id=1;")
            connection.commit()
            print "Total number of rows updated :", cursor.rowcount
            cursor.execute("select * from test;")
            rows=cursor.fetchall()
            for row in rows:
                print "id = ", row[0]
                print "name = ", row[1], "\n"
        except psycopg2.ProgrammingError,e:
            print e
        else:
            print "After Update, Operation done successfully";
    
    
    def DeleteData(connection):
        print "Begin to delete data"
        try:
            cursor = connection.cursor()
            cursor.execute("delete from test where id=3;")
            connection.commit()
            print "Total number of rows deleted :", cursor.rowcount
            cursor.execute("select * from test;")
            rows=cursor.fetchall()
            for row in rows:
                print "id = ", row[0]
                print "name = ", row[1], "\n"
        except psycopg2.ProgrammingError,e:
            print e
        else:
            print "After Delete,Operation done successfully";
    
    
    def SelectData(connection):
        print "Begin to select data"
        try:
            cursor = connection.cursor()
            cursor.execute("select * from test;")
            rows=cursor.fetchall()
            for row in rows:
                print "id = ", row[0]
                print "name = ", row[1], "\n"
        except psycopg2.ProgrammingError,e:
            print e
            print "select failed"
        else:
            print "Operation done successfully";
            cursor.close()
    
    if __name__ == '__main__':
        try:
            connection = psycopg2.connect(host='10.154.70.231', port='8000', database='postgres', user='dbadmin', password='Bigdata_2013')
        except psycopg2.DatabaseError, e:
            print e
            print "Connect database failed"
        else:
            print "Opened database successfully"
            CreateTable(connection)
            InsertData(connection)
            SelectData(connection)
            UpdateData(connection)
            DeleteData(connection)
            connection.close()
    ```

3.  Change the public network address, cluster port number, database name, database username, and database password in the  **python\_dws.py**  file based on the actual cluster information.

    ```
    connection = psycopg2.connect(host='10.154.70.231', port='8000', database='postgres', user='dbadmin', password='Bigdata_2013')
    ```

4.  Run the following command to connect to the cluster using the third-party function library psycopg:

    **python python\_dws.py**


## Using the Third-Party Function Library psycopg2 to Connect to a Cluster \(Windows\)<a name="section79862501183"></a>

1.  In the Windows OS, click the  **Start**  button, enter  **cmd**  in the search box, and click  **cmd.exe**  in the result list to open the CLI.
2.  On the CLI, run the following command to create the  **python\_dws.py**  file and copy the following content to the file:

    ****type nul\>**  python\_dws.py**

    ```
    #!/usr/bin/python
    # -*- coding: UTF-8 -*-
    
    import psycopg2
    def CreateTable(connection):
        print "Begin to create table"
        try:
            cursor = connection.cursor()
            cursor.execute('''drop table if exists test;create table test(id int, name text);''')
            #print "Table created successfully"
            connection.commit()
        except psycopg2.ProgrammingError,e:
            print e
        else:
            print "Table created successfully"
            cursor.close()
    
    
    def InsertData(connection):
        print "Begin to insert data"
        try:
            cursor = connection.cursor()
            cursor.execute("insert into test values(1,'number1');")
            cursor.execute("insert into test values(2,'number2');")
            cursor.execute("insert into test values(3,'number3');")
            connection.commit()
        except psycopg2.ProgrammingError,e:
            print e
        else:
            print "Insert data successfully"
            cursor.close()
    
    
    def UpdateData(connection):
        print "Begin to update data"
        try:
            cursor = connection.cursor()
            cursor.execute("update test set name = 'numberupdated' where id=1;")
            connection.commit()
            print "Total number of rows updated :", cursor.rowcount
            cursor.execute("select * from test;")
            rows=cursor.fetchall()
            for row in rows:
                print "id = ", row[0]
                print "name = ", row[1], "\n"
        except psycopg2.ProgrammingError,e:
            print e
        else:
            print "After Update, Operation done successfully";
    
    
    def DeleteData(connection):
        print "Begin to delete data"
        try:
            cursor = connection.cursor()
            cursor.execute("delete from test where id=3;")
            connection.commit()
            print "Total number of rows deleted :", cursor.rowcount
            cursor.execute("select * from test;")
            rows=cursor.fetchall()
            for row in rows:
                print "id = ", row[0]
                print "name = ", row[1], "\n"
        except psycopg2.ProgrammingError,e:
            print e
        else:
            print "After Delete,Operation done successfully";
    
    
    def SelectData(connection):
        print "Begin to select data"
        try:
            cursor = connection.cursor()
            cursor.execute("select * from test;")
            rows=cursor.fetchall()
            for row in rows:
                print "id = ", row[0]
                print "name = ", row[1], "\n"
        except psycopg2.ProgrammingError,e:
            print e
            print "select failed"
        else:
            print "Operation done successfully";
            cursor.close()
    
    if __name__ == '__main__':
        try:
            connection = psycopg2.connect(host='10.154.70.231', port='8000', database='postgres', user='dbadmin', password='Bigdata_2013')
        except psycopg2.DatabaseError, e:
            print e
            print "Connect database failed"
        else:
            print "Opened database successfully"
            CreateTable(connection)
            InsertData(connection)
            SelectData(connection)
            UpdateData(connection)
            DeleteData(connection)
            connection.close()
    ```

3.  Change the public network address, cluster port number, database name, database username, and database password in the  **python\_dws.py**  file based on the actual cluster information.

    ```
    connection = psycopg2.connect(host='10.154.70.231', port='8000', database='postgres', user='dbadmin', password='Bigdata_2013')
    ```

4.  In the CLI, run the following command to use psycopg to connect to the cluster:

    **python python\_dws.py**


