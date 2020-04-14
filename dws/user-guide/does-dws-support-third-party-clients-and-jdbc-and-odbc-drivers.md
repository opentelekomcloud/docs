# Does DWS Support Third-party Clients and JDBC and ODBC Drivers?<a name="dws_03_0017"></a>

DWS client and drivers are recommended. Compared with open source PostgreSQL clients and drivers, DWS client and drivers has two main advantages:

-   **Security hardening**: PostgreSQL drivers only support MD5 authentication, but DWS drivers support SHA256 and MD5.
-   **Data type enhancement**: DWS drivers support new data types smalldatetime and tinyint.

DWS supports open source PostgreSQL clients and JDBC and ODBC drivers.

The compatible client and driver versions are:

-   PostgreSQL psql 9.2.4 or later
-   PostgreSQL JDBC Driver 9.3-1103 or later
-   PSQL ODBC 09.01.0200 or later

