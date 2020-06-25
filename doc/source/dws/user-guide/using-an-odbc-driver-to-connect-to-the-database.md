# Using an ODBC Driver to Connect to the Database<a name="en-us_topic_0056218063"></a>

In DWS, you can use an ODBC driver to connect to database either through an ECS in the public cloud or over the Internet.

For details about how to use the ODBC interface, see the official document. 

## Prerequisites<a name="section17871125219214"></a>

-   You have downloaded ODBC driver packages  **dws\_odbc\_driver\_for\_linux.tar.gz**  \(for Linux\) and  **dws\_odbc\_driver\_for\_windows.tar.gz**  \(for Windows\). For details, see  [Downloading the JDBC or ODBC Driver](downloading-the-jdbc-or-odbc-driver.md).

    DWS also supports open-source ODBC driver: PostgreSQL ODBC 09.01.0200 or later.

-   You have downloaded the open source unixODBC code file 2.3.0 from  **http://sourceforge.net/projects/unixodbc/files/unixODBC/2.3.0/unixODBC-2.3.0.tar.gz/download**.
-   You have downloaded the SSL certificate file. For details, see section  [Downloading the SSL Certificate File](downloading-the-ssl-certificate-file.md).

## Using an ODBC Driver to Connect to a Database \(Linux\)<a name="section42307202184151"></a>

1.  Upload the ODBC package and code file to the Linux environment and decompress them to the specified directory.
2.  Log in to the Linux environment as user  **root**.
3.  Prepare  **unixODBC**.
    1.  Decompress the  **unixODBC**  code file.

        **tar -xvf unixODBC-2.3.0.tar.gz**

    2.  Modify the configuration.

        **cd unixODBC-2.3.0**

        **vi configure**

        Change the value of  **LIB\_VERSION**  to the following. Save the change and exit.

        ```
        LIB_VERSION="1:0:0"
        ```

    3.  Compile the code file and install the driver.

        **./configure --enable-gui=no**

        **make**

        **make install**

4.  Replace the driver file.
    1.  Decompress  **dws\_odbc\_driver\_for\_linux.tar.gz**.

        **tar -xvf dws\_odbc\_driver\_for\_linux.tar.gz**

    2.  Copy all files in the  **lib**  directory to  **/usr/local/lib**. If there are files with the same name, overwrite them.
    3.  Copy  **psqlodbcw.la**  and  **psqlodbcw.so**  in the  **odbc/lib**  directory to  **/usr/local/lib**.

5.  Run the following command to modify the configuration of the driver file:

    **vi /usr/local/etc/odbcinst.ini**

    Copy the following content to the file:

    ```
    [DWS] 
    Driver64=/usr/local/lib/psqlodbcw.so
    ```

    The parameters are as follows:

    -   **\[DWS\]**: indicates the driver name. You can customize the name.
    -   **Driver64**  or  **Driver**: indicates the path where the dynamic library of the driver resides. For a 64-bit OS, search for  **Driver64**  first. If  **Driver64**  is not configured, search for  **Driver**.

6.  Run the following command to modify the data source file:

    **vi /usr/local/etc/odbc.ini**

    Copy the following content to the configuration file, save the modification, and exit.

    ```
    [DWSODBC]
    Driver=DWS
    Servername=10.10.0.13
    Database=postgres
    Username=dbadmin
    Password=Abcd@123
    Port=8000
    Sslmode=allow
    ```

    <a name="table698016191057"></a>
    <table><thead align="left"><tr id="row43688892191057"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="p49139350191057"><a name="p49139350191057"></a><a name="p49139350191057"></a><strong id="b4331210191910"><a name="b4331210191910"></a><a name="b4331210191910"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40%" id="mcps1.1.4.1.2"><p id="p53562174191057"><a name="p53562174191057"></a><a name="p53562174191057"></a><strong id="b1861928191910"><a name="b1861928191910"></a><a name="b1861928191910"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40%" id="mcps1.1.4.1.3"><p id="p56575432191057"><a name="p56575432191057"></a><a name="p56575432191057"></a><strong id="b3176675391910"><a name="b3176675391910"></a><a name="b3176675391910"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row38648128191057"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p43490644191057"><a name="p43490644191057"></a><a name="p43490644191057"></a>[DSN]</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.4.1.2 "><p id="p33081269191057"><a name="p33081269191057"></a><a name="p33081269191057"></a>Data source name</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.4.1.3 "><p id="p62337098191057"><a name="p62337098191057"></a><a name="p62337098191057"></a>[DWSODBC]</p>
    </td>
    </tr>
    <tr id="row24162971191057"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p11043674191057"><a name="p11043674191057"></a><a name="p11043674191057"></a>Driver</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.4.1.2 "><p id="p22122434191057"><a name="p22122434191057"></a><a name="p22122434191057"></a>Driver name, corresponding to <strong id="b84235270615421"><a name="b84235270615421"></a><a name="b84235270615421"></a>DriverName</strong> in <span class="filepath" id="filepath107056302415438"><a name="filepath107056302415438"></a><a name="filepath107056302415438"></a><b>odbcinst.ini</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.4.1.3 "><p id="p47086714191057"><a name="p47086714191057"></a><a name="p47086714191057"></a>Driver=DWS</p>
    </td>
    </tr>
    <tr id="row21127243191057"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p33585151191057"><a name="p33585151191057"></a><a name="p33585151191057"></a>Servername</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.4.1.2 "><p id="p36042711191057"><a name="p36042711191057"></a><a name="p36042711191057"></a>Server IP address</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.4.1.3 "><p id="p33778492191057"><a name="p33778492191057"></a><a name="p33778492191057"></a>Servername=10.10.0.13</p>
    </td>
    </tr>
    <tr id="row35570974191057"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p62676673191057"><a name="p62676673191057"></a><a name="p62676673191057"></a>Database</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.4.1.2 "><p id="p43645732191057"><a name="p43645732191057"></a><a name="p43645732191057"></a>Name of the database to be connected to</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.4.1.3 "><p id="p45643375191057"><a name="p45643375191057"></a><a name="p45643375191057"></a>Database=postgres</p>
    </td>
    </tr>
    <tr id="row8137195191057"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p55133095191057"><a name="p55133095191057"></a><a name="p55133095191057"></a>Username</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.4.1.2 "><p id="p36595678191057"><a name="p36595678191057"></a><a name="p36595678191057"></a>Database username</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.4.1.3 "><p id="p11459962191057"><a name="p11459962191057"></a><a name="p11459962191057"></a>Username=dbadmin</p>
    </td>
    </tr>
    <tr id="row36030802191057"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p32813824191057"><a name="p32813824191057"></a><a name="p32813824191057"></a>Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.4.1.2 "><p id="p40674054191057"><a name="p40674054191057"></a><a name="p40674054191057"></a>Database user password</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.4.1.3 "><p id="p6264077191057"><a name="p6264077191057"></a><a name="p6264077191057"></a>Password=Abcd@123</p>
    </td>
    </tr>
    <tr id="row56376696191057"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p3109667191057"><a name="p3109667191057"></a><a name="p3109667191057"></a>Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.4.1.2 "><p id="p50556450191057"><a name="p50556450191057"></a><a name="p50556450191057"></a>Port number of the server</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.4.1.3 "><p id="p1431774191057"><a name="p1431774191057"></a><a name="p1431774191057"></a>Port=8000</p>
    </td>
    </tr>
    <tr id="row12885966191057"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p37130287191057"><a name="p37130287191057"></a><a name="p37130287191057"></a>Sslmode</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.4.1.2 "><p id="p54763265191057"><a name="p54763265191057"></a><a name="p54763265191057"></a>SSL certification mode. This parameter is enabled for the cluster by default.</p>
    <p id="p1442353513431"><a name="p1442353513431"></a><a name="p1442353513431"></a>Values and meanings:</p>
    <a name="ul1438325020436"></a><a name="ul1438325020436"></a><ul id="ul1438325020436"><li><strong id="dws_01_0038_b84235270616196"><a name="dws_01_0038_b84235270616196"></a><a name="dws_01_0038_b84235270616196"></a>disable</strong>: only tries to establish a non-SSL connection.</li><li><strong id="dws_01_0038_b842352706161935"><a name="dws_01_0038_b842352706161935"></a><a name="dws_01_0038_b842352706161935"></a>allow</strong>: tries to establish a non-SSL connection first, and then an SSL connection if the first attempt fails.</li><li><strong id="dws_01_0038_b842352706162016"><a name="dws_01_0038_b842352706162016"></a><a name="dws_01_0038_b842352706162016"></a>prefer</strong>: tries to establish an SSL connection first, and then a non-SSL connection if the first attempt fails.</li><li><strong id="dws_01_0038_b842352706162047"><a name="dws_01_0038_b842352706162047"></a><a name="dws_01_0038_b842352706162047"></a>require</strong>: only tries to establish an SSL connection. If there is a CA file, perform the verification according to the scenario in which the parameter is set to <strong id="dws_01_0038_b842352706162118"><a name="dws_01_0038_b842352706162118"></a><a name="dws_01_0038_b842352706162118"></a>verify-ca</strong>.</li><li><strong id="dws_01_0038_b842352706162135"><a name="dws_01_0038_b842352706162135"></a><a name="dws_01_0038_b842352706162135"></a>verify-ca</strong>: tries to establish an SSL connection and check whether the server certificate is issued by a trusted CA.</li><li><strong id="dws_01_0038_b922295117459"><a name="dws_01_0038_b922295117459"></a><a name="dws_01_0038_b922295117459"></a>verify-full</strong>: DWS does not support this mode.</li></ul>
    <div class="note" id="note94497271018"><a name="note94497271018"></a><a name="note94497271018"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p444916277012"><a name="p444916277012"></a><a name="p444916277012"></a>The SSL connection mode delivers higher security than the common mode. You are advised to use SSL connection when using ODBC to connect to the cluster.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.4.1.3 "><p id="p6639467191057"><a name="p6639467191057"></a><a name="p6639467191057"></a>Sslmode=allow</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:**   
    >You can view the values of  **Servername**  and  **Port**  on the DWS management console. Log in to the DWS management console and click  **Connection Management**. In the  **Data Warehouse Connection String**  area, select the target cluster and obtain  **Private Network Address**  or  **Public Network Address**. For details, see  [Obtaining the Cluster Connection Address](obtaining-the-cluster-connection-address.md).  

7.  Configure environment variables.

    **vi \~/.bashrc**

    Add the following information to the configuration file:

    ```
    export LD_LIBRARY_PATH=/usr/local/lib/:$LD_LIBRARY_PATH 
    export ODBCSYSINI=/usr/local/etc 
    export ODBCINI=/usr/local/etc/odbc.ini
    ```

8.  Import environment variables.

    **source \~/.bashrc**

9.  Run the following commands to connect to the database:

    **/usr/local/bin/isql -v DWSODBC**

    If the following information is displayed, the connection is successful:

    ```
    +---------------------------------------+ 
    | Connected!                            | 
    |                                       | 
    | sql-statement                         | 
    | help [tablename]                      | 
    | quit                                  | 
    |                                       | 
    +---------------------------------------+ 
    SQL> 
    ```


## Using an ODBC Driver to Connect to a Database \(Windows\)<a name="section31086112145338"></a>

1.  Decompress ODBC driver package  **dws\_odbc\_driver\_for\_windows.tar.gz**  \(for Windows\) and install  **psqlodbc.msi**.
2.  Decompress the SSL certificate package to obtain the certificate file.

    You can choose to automatically or manually deploy the certificate based on your needs.

    Automatic deployment:

    Double-click the  **sslcert\_env.bat**  file. The certificate is automatically deployed to a default location.

    >![](/images/icon-note.gif) **NOTE:**   
    >The  **sslcert\_env.bat**  file ensures the purity of the certificate environment. When the  **%APPDATA%\\postgresql**  directory exists, a message will be prompted asking you whether you want to remove related directories. If you want to remove related directories, back up files in the directory.  

    Manual deployment:

    1.  Create a new folder named  **postgresql**  in the  **%APPDATA%\\**  directory.
    2.  Copy files  **client.crt**,  **client.key**,  **client.key.cipher**, and  **client.key.rand**  to the  **%APPDATA%\\postgresql**  directory and change  **client**  in the file name to  **postgres**. For example, change the name of  **client.key**  to  **postgres.key**.
    3.  Copy  **cacert.pem**  to  **%APPDATA%\\postgresql**  and change the name of  **cacert.pem**  to  **root.crt**.

3.  Open Driver Manager.

    Currently, because DWS only provides a 32-bit ODBC driver, it only supports 32-bit application development. Use the 32-bit Driver Manager when you configure the data source. \(Assume the Windows system drive is drive C. If another disk drive is used, modify the path accordingly.\)

    -   In a 64-bit Windows OS, open  **C:\\Windows\\SysWOW64\\odbcad32.exe**.

        Do not open Driver Manager by choosing  **Control Panel**  \>  **System and Security**  \>  **Administrative Tools**  \>  **Data Sources \(ODBC\)**.

        >![](/images/icon-note.gif) **NOTE:**   
        >WOW64 is the acronym for Windows 32-bit on Windows 64-bit.  **C:\\Windows\\SysWOW64\\**  stores the 32-bit environment on a 64-bit system.  **C:\\Windows\\System32\\**  stores the environment consistent with the current OS. For technical details, see the Windows technical documents.  

    -   In a 32-bit Windows OS, open  **C:\\Windows\\System32\\odbcad32.exe**.

        You can also open Driver Manager by choosing  **Control Panel**  \>  **System and Security**  \>  **Administrative Tools**  \>  **Data Sources \(ODBC\)**.

4.  Configure a data source to be connected to.
    1.  On the  **User DSN**  tab, click  **Add**, and choose  **PostgreSQL Unicode**  for setup.

        **Figure  1**  Configuring a data source to be connected to<a name="fig46625912141933"></a>  
        ![](figures/configuring-a-data-source-to-be-connected-to.png "configuring-a-data-source-to-be-connected-to")

        You can view the values of  **Server**  and  **Port**  on the DWS management console. Log in to the DWS management console and click  **Connection Management**. In the  **Data Warehouse Connection String**  area, select the target cluster and obtain  **Private Network Address**  or  **Public Network Address**. For details, see  [Obtaining the Cluster Connection Address](obtaining-the-cluster-connection-address.md).

    2.  Click  **Test**  to verify that the connection is correct. If  **Connection successful**  is displayed, the connection is correct.

5.  Compile an ODBC sample program to connect to the data source.

    The sample code is as follows:

    ```
    // This example shows how to obtain DWS data through the ODBC driver.
    // DBtest.c (compile with: libodbc.so)   
    #include <stdlib.h> 
    #include <stdio.h> 
    #include <sqlext.h>
    #ifdef WIN32
    #include <windows.h>
    #endif 
    SQLHENV       V_OD_Env;        // Handle ODBC environment 
    SQLHSTMT      V_OD_hstmt;      // Handle statement 
    SQLHDBC       V_OD_hdbc;       // Handle connection     
    char          typename[100];
    SQLINTEGER    value = 100;
    SQLINTEGER    V_OD_erg,V_OD_buffer,V_OD_err,V_OD_id;
    int main(int argc,char *argv[]) 
    {         
          // 1. Allocate environment handles.
          V_OD_erg = SQLAllocHandle(SQL_HANDLE_ENV,SQL_NULL_HANDLE,&V_OD_Env);     
          if ((V_OD_erg != SQL_SUCCESS) && (V_OD_erg != SQL_SUCCESS_WITH_INFO))        
          {           
               printf("Error AllocHandle\n");           
               exit(0);        
          } 
          // 2. Set environment attributes (version information).
          SQLSetEnvAttr(V_OD_Env, SQL_ATTR_ODBC_VERSION, (void*)SQL_OV_ODBC3, 0);      
          // 3. Allocate connection handles.
          V_OD_erg = SQLAllocHandle(SQL_HANDLE_DBC, V_OD_Env, &V_OD_hdbc);     
          if ((V_OD_erg != SQL_SUCCESS) && (V_OD_erg != SQL_SUCCESS_WITH_INFO))      
          {                     
               SQLFreeHandle(SQL_HANDLE_ENV, V_OD_Env);          
               exit(0);       
          }
          // 4. Set connection attributes.
          SQLSetConnectAttr(V_OD_hdbc, SQL_ATTR_AUTOCOMMIT, SQL_AUTOCOMMIT_ON, 0);          
          // 5. Connect to a data source. You do not need to enter the username and password if you have configured them in the odbc.ini file. If you have not configured them, specify the name and password of the user who wants to connect to the database in the SQLConnect function.
          V_OD_erg = SQLConnect(V_OD_hdbc, (SQLCHAR*) "gaussdb", SQL_NTS,  
                               (SQLCHAR*) "", SQL_NTS,  (SQLCHAR*) "", SQL_NTS);        
          if ((V_OD_erg != SQL_SUCCESS) && (V_OD_erg != SQL_SUCCESS_WITH_INFO))      
          {           
              printf("Error SQLConnect %d\n",V_OD_erg);            
              SQLFreeHandle(SQL_HANDLE_ENV, V_OD_Env);       
              exit(0);        
          }     
          printf("Connected !\n"); 
          // 6. Set statement attributes.
          SQLSetStmtAttr(V_OD_hstmt,SQL_ATTR_QUERY_TIMEOUT,(SQLPOINTER *)3,0);
          // 7. Allocate statement handles.
          SQLAllocHandle(SQL_HANDLE_STMT, V_OD_hdbc, &V_OD_hstmt);       
          // 8. Execute SQL statements.
          SQLExecDirect(V_OD_hstmt,"drop table IF EXISTS testtable",SQL_NTS);
          SQLExecDirect(V_OD_hstmt,"create table testtable(id int)",SQL_NTS);
          SQLExecDirect(V_OD_hstmt,"insert into testtable values(25)",SQL_NTS);
          // 9. Prepare for execution.
          SQLPrepare(V_OD_hstmt,"insert into testtable values(?)",SQL_NTS); 
          // 10. Bind parameters.
          SQLBindParameter(V_OD_hstmt,1,SQL_PARAM_INPUT,SQL_C_SLONG,SQL_INTEGER,0,0,
                           &value,0,NULL);
          // 11. Execute prepared statements.
          SQLExecute(V_OD_hstmt);
          SQLExecDirect(V_OD_hstmt,"select id from testtable",SQL_NTS);
          // 12. Obtain attributes of a specific column in the result set.
          SQLColAttribute(V_OD_hstmt,1,SQL_DESC_TYPE,typename,100,NULL,NULL);                 
          printf("SQLColAtrribute %s\n",typename);
          // 13. Bind the result set.
          SQLBindCol(V_OD_hstmt,1,SQL_C_SLONG, (SQLPOINTER)&V_OD_buffer,150,
                    (SQLLEN *)&V_OD_err);
          // 14. Obtain data in the result set by executing SQLFetch.
          V_OD_erg=SQLFetch(V_OD_hstmt);
          // 15. Obtain and return data by executing SQLGetData.
          while(V_OD_erg != SQL_NO_DATA)
          {
              SQLGetData(V_OD_hstmt,1,SQL_C_SLONG,(SQLPOINTER)&V_OD_id,0,NULL);
              printf("SQLGetData ----ID = %d\n",V_OD_id);
              V_OD_erg=SQLFetch(V_OD_hstmt);
          };
          printf("Done !\n");pgadmin
          // 16. Disconnect data source connections and release handle resources.
          SQLFreeHandle(SQL_HANDLE_STMT,V_OD_hstmt);    
          SQLDisconnect(V_OD_hdbc);         
          SQLFreeHandle(SQL_HANDLE_DBC,V_OD_hdbc);       
          SQLFreeHandle(SQL_HANDLE_ENV, V_OD_Env);  
          return(0);
     }
    
    ```


