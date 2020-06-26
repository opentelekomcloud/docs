# Tablespaces Management<a name="en-us_topic_0077893063"></a>

## **Scenarios**<a name="section21161918185247"></a>

RDS provides the  PostgreSQL tablespace  management solution based on user  **root**.

## Creating a Tablespace<a name="section3787577116487"></a>

1.  Connect to the database as user  **root**  and create a tablespace.

    **\# psql --host=**_<RDS\_ADDRESS\>_** --port=**<_DB\_PORT_\>  **--dbname=**_<DB\_NAME\>_** --username=root -c **"**select control\_tablespace **\(**'create'**, '_<TABLESPACE\_NAME\>_'\);"

    **Table  1**  Parameter description

    <a name="table59901821142611"></a>
    <table><thead align="left"><tr id="row8990221112611"><th class="cellrowborder" valign="top" width="35.29%" id="mcps1.2.3.1.1"><p id="p4991142142610"><a name="p4991142142610"></a><a name="p4991142142610"></a><strong id="b1426018816537"><a name="b1426018816537"></a><a name="b1426018816537"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="64.71000000000001%" id="mcps1.2.3.1.2"><p id="p1799192112260"><a name="p1799192112260"></a><a name="p1799192112260"></a><strong id="b4529892531"><a name="b4529892531"></a><a name="b4529892531"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19911521112611"><td class="cellrowborder" valign="top" width="35.29%" headers="mcps1.2.3.1.1 "><p id="p59918217264"><a name="p59918217264"></a><a name="p59918217264"></a><em id="i2099182192611"><a name="i2099182192611"></a><a name="i2099182192611"></a>RDS_ADDRESS</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="64.71000000000001%" headers="mcps1.2.3.1.2 "><p id="p11991202114262"><a name="p11991202114262"></a><a name="p11991202114262"></a>Indicates the IP address of the RDS DB instance.</p>
    </td>
    </tr>
    <tr id="row12991172110266"><td class="cellrowborder" valign="top" width="35.29%" headers="mcps1.2.3.1.1 "><p id="p149912217263"><a name="p149912217263"></a><a name="p149912217263"></a><em id="i999132162610"><a name="i999132162610"></a><a name="i999132162610"></a>DB_PORT</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="64.71000000000001%" headers="mcps1.2.3.1.2 "><p id="p2099172111268"><a name="p2099172111268"></a><a name="p2099172111268"></a>Indicates the port of the RDS DB instance.</p>
    </td>
    </tr>
    <tr id="row4991142102618"><td class="cellrowborder" valign="top" width="35.29%" headers="mcps1.2.3.1.1 "><p id="p799111216264"><a name="p799111216264"></a><a name="p799111216264"></a><em id="i39917214263"><a name="i39917214263"></a><a name="i39917214263"></a>DB_NAME</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="64.71000000000001%" headers="mcps1.2.3.1.2 "><p id="p1399111218262"><a name="p1399111218262"></a><a name="p1399111218262"></a>Indicates the database name.</p>
    </td>
    </tr>
    <tr id="row299132162620"><td class="cellrowborder" valign="top" width="35.29%" headers="mcps1.2.3.1.1 "><p id="p59915217267"><a name="p59915217267"></a><a name="p59915217267"></a><em id="i1299152132611"><a name="i1299152132611"></a><a name="i1299152132611"></a>TABLESPACE_NAME</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="64.71000000000001%" headers="mcps1.2.3.1.2 "><p id="p11991162102616"><a name="p11991162102616"></a><a name="p11991162102616"></a>Indicates the tablespace name.</p>
    </td>
    </tr>
    </tbody>
    </table>

2.  Enter the password of user  **root**  as prompted.

    Log in to the  **my\_db**  database and create the  **tbspc1**  tablespace. Example:

    **\# psql --host=192.168.6.141 --port=****5432****  --dbname=my\_db --username=root -c "select control\_tablespace\('create', 'tbspc1'\);"**

    ```
    Password for user root:
              control_tablespace          
    ------------------------------    
    create tablespace tbspc1 successfully.   
    (1 row)
    ```

    If the creation fails, view error logs of the DB instance.

    >![](/images/icon-note.gif) **NOTE:**   
    >To ensure performance, a maximum of 20 tablespaces can be created.  


## Deleting a Tablespace<a name="section61601016487"></a>

1.  Connect to the database as user  **root**  and delete a tablespace.

    **\# psql --host=**_<RDS\_ADDRESS\>_** --port=**<_DB\_PORT_\>  **--username=root** **--dbname=**_<DB\_NAME\>_** -c **"**select control\_tablespace**\(**'drop', **'_<TABLESPACE \_NAME\>_'\);"

    **Table  2**  Parameter description

    <a name="table555513459246"></a>
    <table><thead align="left"><tr id="row10555104514241"><th class="cellrowborder" valign="top" width="35.29%" id="mcps1.2.3.1.1"><p id="p95561345142413"><a name="p95561345142413"></a><a name="p95561345142413"></a><strong id="b1593974864"><a name="b1593974864"></a><a name="b1593974864"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="64.71000000000001%" id="mcps1.2.3.1.2"><p id="p8556145162414"><a name="p8556145162414"></a><a name="p8556145162414"></a><strong id="b1683377161"><a name="b1683377161"></a><a name="b1683377161"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55561845102416"><td class="cellrowborder" valign="top" width="35.29%" headers="mcps1.2.3.1.1 "><p id="p2556945182413"><a name="p2556945182413"></a><a name="p2556945182413"></a><em id="i8833447132520"><a name="i8833447132520"></a><a name="i8833447132520"></a>RDS_ADDRESS</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="64.71000000000001%" headers="mcps1.2.3.1.2 "><p id="p05561345142419"><a name="p05561345142419"></a><a name="p05561345142419"></a>Indicates the IP address of the RDS DB instance.</p>
    </td>
    </tr>
    <tr id="row55561445192411"><td class="cellrowborder" valign="top" width="35.29%" headers="mcps1.2.3.1.1 "><p id="p2556174510240"><a name="p2556174510240"></a><a name="p2556174510240"></a><em id="i15835147152510"><a name="i15835147152510"></a><a name="i15835147152510"></a>DB_PORT</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="64.71000000000001%" headers="mcps1.2.3.1.2 "><p id="p20556174592415"><a name="p20556174592415"></a><a name="p20556174592415"></a>Indicates the port of the RDS DB instance.</p>
    </td>
    </tr>
    <tr id="row25561845132412"><td class="cellrowborder" valign="top" width="35.29%" headers="mcps1.2.3.1.1 "><p id="p125562453240"><a name="p125562453240"></a><a name="p125562453240"></a><em id="i6835154717256"><a name="i6835154717256"></a><a name="i6835154717256"></a>DB_NAME</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="64.71000000000001%" headers="mcps1.2.3.1.2 "><p id="p13556154510248"><a name="p13556154510248"></a><a name="p13556154510248"></a>Indicates the database name.</p>
    </td>
    </tr>
    <tr id="row1455684572418"><td class="cellrowborder" valign="top" width="35.29%" headers="mcps1.2.3.1.1 "><p id="p855644517243"><a name="p855644517243"></a><a name="p855644517243"></a><em id="i118361847182517"><a name="i118361847182517"></a><a name="i118361847182517"></a>TABLESPACE_NAME</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="64.71000000000001%" headers="mcps1.2.3.1.2 "><p id="p555618456248"><a name="p555618456248"></a><a name="p555618456248"></a>Indicates the tablespace name.</p>
    </td>
    </tr>
    </tbody>
    </table>

2.  Enter the password of user  **root**  as prompted.

    Example:

    **\# psql --host=192.168.6.141 --port=8635 --dbname=my\_db --username=root -c "select control\_tablespace\('drop', 'tbspc1'\);"**

    ```
    Password for user root:
             control_tablespace         
    ----------------------------    
    drop tablespace tbspc1 successfully.   
    (1 row)
    ```

    Before deleting the tablespace, ensure that it is empty. If the deletion fails, view error logs of the DB instance.


