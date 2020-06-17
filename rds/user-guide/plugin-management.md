# Plugin Management<a name="en-us_topic_0077893062"></a>

RDS provides the PostgreSQL plugin management solution for user  **root**. The auto\_explain is automatically created by the system and other plugins need to be manually created.

## Creating a Plugin<a name="section3157625911310"></a>

1.  Connect to the database  **postgres**  as user  **root**  and use  **template1**  to create a database that can support the plugin.

    **\# psql --host=**_<RDS\_ADDRESS\>_** --port=**<_DB\_PORT_\>  **--dbname=postgres --username=root -c **"**create database **_<DB\_NAME\> _**template template1**;"

    -   _**RDS\_ADDRESS**_  indicates the IP address of the RDS DB instance.
    -   _**DB\_PORT**_  indicates the RDS DB instance port.
    -   _**DB\_NAME**_  indicates the name of the database to be created.

    Enter the password of user  **root**  as prompted.

    Create a database named  **_my\_extension\_db_**  that can support the plugin. Example:

    **\# psql --host=192.168.6.141 --port=****5432****  --dbname=postgres --username=root -c "create database my\_extension\_db template template1;"**

    ```
    Password for user root:
    CREATE DATABASE
    ```

    Note: If you are creating a database as a common user, log in to the created database as the common user and run the following command to grant all rights to user  **root**:

    **GRANT ALL ON DATABASE db1 TO root;**

2.  Connect to the created database as user  **root**  and create a plugin.

    **\# psql --host=**_<RDS\_ADDRESS\>_** --port=**<_DB\_PORT_\>  **--dbname=**_<DB\_NAME\>_** --username=root -c **"**select control\_extension**\('**create**','_<EXTENSION\_NAME\>_'\);"

    -   _**RDS\_ADDRESS**_  indicates the IP address of the RDS DB instance.
    -   _**DB\_PORT**_  indicates the RDS DB instance port.
    -   _**DB\_NAME**_  indicates the name of the database to be created.
    -   _**EXTENSION\_NAME**_  indicates the plugin name and has the following possible values:
        -   postgis: When  **postgis**  is created, the following plugins are created at the same time:

            postgis

            postgis\_topology

            fuzzystrmatch

            postgis\_tiger\_geocoder

            address\_standardizer

            address\_standardizer\_data\_us

        -   btree\_gin
        -   btree\_gist
        -   hstore
        -   pg\_trgm
        -   tablefunc
        -   unaccent
        -   uuid-ossp
        -   cube
        -   dict\_int
        -   dict\_xsyn
        -   earthdistance

            >![](/images/icon-notice.gif) **NOTICE:**   
            >To install the  **earthdistance**  plugin, you must install the  **cube**  plugin first.  

        -   intagg
        -   intarray
        -   ltree
        -   pgcrypto
        -   timescaledb

            >![](/images/icon-notice.gif) **NOTICE:**   
            >-   The timescaledb plugin supports PostgreSQL 9.6 and later versions.  
            >-   The timescaledb plugin does not support the TSL protocol.  

        -   hll
        -   zhparser, which provides the default dictionary only and does not support user-defined dictionaries. The default values are as follows:

            zhparser.punctuation\_ignore = off

            zhparser.multi\_short = off

            zhparser.multi\_duality = off

            zhparser.multi\_zmain = off

            zhparser.multi\_zall = off

            zhparser.dict\_in\_memory = off

        -   pg\_pathman

            >![](/images/icon-notice.gif) **NOTICE:**   
            >The pg\_pathman plugin supports only the following versions: PostgreSQL 11.5, PostgreSQL 10, PostgreSQL 9.6, and PostgreSQL9.5.  

        -   pg\_stat\_statements
        -   pg\_hint\_plan

    Enter the password of user  **root**  as prompted.

    Create plugin  **postgis**  in the database  **_my\_extension\_db_**. Example:

    **\# psql --host=192.168.6.141 --port=****5432****  --dbname=my\_extension\_db --username=root -c "select control\_extension\('create','postgis'\);"**

    ```
    Password for user root: 
          control_extension       
    ------------------------------
     create postgis successfully.
    (1 row)
    ```


## Deleting a Plugin<a name="section2637708311349"></a>

Connect to the database with a plugin created as user  **root**  and delete the plugin.

**\# psql --host=**_<RDS\_ADDRESS\>_** --port=**<_DB\_PORT_\>  **--username=root** **--dbname=**_<DB\_NAME\>_** -c **"**select control\_extension **\('**drop**','_<EXTENSION\_NAME\>_'\);"

-   _**RDS\_ADDRESS**_  indicates the IP address of the RDS DB instance.
-   _**DB\_PORT**_  indicates the RDS DB instance port.
-   _**DB\_NAME**_  indicates the name of the database to be created.
-   _**EXTENSION\_NAME**_  indicates the plugin name and has the following values:
    -   postgis
    -   btree\_gin
    -   btree\_gist
    -   hstore
    -   pg\_trgm
    -   tablefunc
    -   unaccent
    -   uuid-ossp
    -   cube

        >![](/images/icon-notice.gif) **NOTICE:**   
        >If the  **earthdistance**  plugin has been installed, deleting the  **cube**  plugin will cause the  **earthdistance**  plugin to be unavailable.  

    -   dict\_int
    -   dict\_xsyn
    -   earthdistance
    -   intagg
    -   intarray
    -   ltree
    -   pgcrypto
    -   timescaledb
    -   hll
    -   zhparser


Enter the password of user  **root**  as prompted.

Example:

**\# psql --host=192.168.6.141 --port=****5432****  --dbname=my\_extension\_db --username=root -c "select control\_extension\('drop','postgis'\);"**

```
Password for user root: 
     control_extension      
----------------------------
 drop postgis successfully.
(1 row)
```

