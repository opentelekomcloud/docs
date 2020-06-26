# Step 4: Connect to a DB Instance Through psql<a name="rds_02_0051"></a>

You can use the PostgreSQL client psql to connect to a DB instance through a common connection or an  SSL connection. The SSL connection is encrypted and therefore more secure.

## **Preparations**<a name="en-us_topic_0192953574_section48118919135236"></a>

1.  To connect to a DB instance through an EIP, you must:
    1.  Bind the EIP to the DB instance. For details, see section  [Step 3: Bind an EIP](step-3-bind-an-eip-(PostgreSQL).md).
    2.  Ensure that the local device can access the EIP that has been bound to the DB instance.

2.  Install the PostgreSQL client on the prepared ECS or device that can access RDS.

    For details, see section  [How Can I Install the PostgreSQL Client?](how-can-i-install-the-postgresql-client.md)


## Common Connection<a name="en-us_topic_0192953574_section50158178113022"></a>

1.  Log in to the ECS or device that can access RDS.
2.  Run the following command to connect to an RDS DB instance:

    **psql --no-readline -U**  <_user_\>  **-h**  <_host_\>  **-p**  <_port_\>  **-d**  <_datastore_\>  **-W**

    **Table  1**  Parameter description

    <a name="table18330639097"></a>
    <table><thead align="left"><tr id="row23312390914"><th class="cellrowborder" valign="top" width="29.38%" id="mcps1.2.3.1.1"><p id="p19331439391"><a name="p19331439391"></a><a name="p19331439391"></a><strong id="b187791162569"><a name="b187791162569"></a><a name="b187791162569"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="70.62%" id="mcps1.2.3.1.2"><p id="p1333133911911"><a name="p1333133911911"></a><a name="p1333133911911"></a><strong id="b36885755613"><a name="b36885755613"></a><a name="b36885755613"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1433119391690"><td class="cellrowborder" valign="top" width="29.38%" headers="mcps1.2.3.1.1 "><p id="p83311739193"><a name="p83311739193"></a><a name="p83311739193"></a>&lt;<em id="i10357182714102"><a name="i10357182714102"></a><a name="i10357182714102"></a>user</em>&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="70.62%" headers="mcps1.2.3.1.2 "><p id="p03311439593"><a name="p03311439593"></a><a name="p03311439593"></a>Indicates the username of the RDS database account. The default administrator is <strong id="b427215120566"><a name="b427215120566"></a><a name="b427215120566"></a>root</strong>.</p>
    </td>
    </tr>
    <tr id="row2331133912911"><td class="cellrowborder" valign="top" width="29.38%" headers="mcps1.2.3.1.1 "><p id="p1331339598"><a name="p1331339598"></a><a name="p1331339598"></a>&lt;<em id="i1463194141011"><a name="i1463194141011"></a><a name="i1463194141011"></a>host</em>&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="70.62%" headers="mcps1.2.3.1.2 "><p id="p6331123917911"><a name="p6331123917911"></a><a name="p6331123917911"></a>Indicates the IP address of the primary DB instance. To obtain this parameter, go to the <span class="uicontrol" id="uicontrol191626423452"><a name="uicontrol191626423452"></a><a name="uicontrol191626423452"></a><b>Basic Information</b></span> page of the DB instance. If the DB instance is accessed through an EIP, the IP address can be found on the <strong id="b199844613454"><a name="b199844613454"></a><a name="b199844613454"></a>EIPs</strong> page.</p>
    </td>
    </tr>
    <tr id="row1333115398920"><td class="cellrowborder" valign="top" width="29.38%" headers="mcps1.2.3.1.1 "><p id="p9331143910914"><a name="p9331143910914"></a><a name="p9331143910914"></a>&lt;<em id="i13981145351015"><a name="i13981145351015"></a><a name="i13981145351015"></a>port</em>&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="70.62%" headers="mcps1.2.3.1.2 "><p id="p1533111391295"><a name="p1533111391295"></a><a name="p1533111391295"></a>Indicates the database port in use. The default value is <strong id="b265814824516"><a name="b265814824516"></a><a name="b265814824516"></a>5432</strong>. To obtain this parameter, go to the <span class="uicontrol" id="uicontrol8659548144517"><a name="uicontrol8659548144517"></a><a name="uicontrol8659548144517"></a><b>Basic Information</b></span> page of the DB instance. The port number can be found in the <span class="uicontrol" id="uicontrol36591848104517"><a name="uicontrol36591848104517"></a><a name="uicontrol36591848104517"></a><b>Database Port</b></span> field in the <span class="uicontrol" id="uicontrol14660174834513"><a name="uicontrol14660174834513"></a><a name="uicontrol14660174834513"></a><b>Connection Information</b></span> area.</p>
    </td>
    </tr>
    <tr id="row1933283919915"><td class="cellrowborder" valign="top" width="29.38%" headers="mcps1.2.3.1.1 "><p id="p143321139694"><a name="p143321139694"></a><a name="p143321139694"></a>&lt;<em id="i520061671117"><a name="i520061671117"></a><a name="i520061671117"></a>datastore</em>&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="70.62%" headers="mcps1.2.3.1.2 "><p id="p203329395920"><a name="p203329395920"></a><a name="p203329395920"></a>Indicates the name of the database (the default database name is <strong id="b19416456134518"><a name="b19416456134518"></a><a name="b19416456134518"></a>postgres</strong>).</p>
    </td>
    </tr>
    </tbody>
    </table>

    The parameter  **-W**  indicates that a password must be entered for the connection. After running this command, you will be prompted to enter a password.

    Example:

    Run the following command as user  **root**  to connect to a DB instance:

    **psql --no-readline -U root -h 192.168.0.44 -p 5432 -d postgres -W**


## **SSL Connection**<a name="en-us_topic_0192953574_section836277162054"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  In the  **DB Information**  area on the  **Basic Information**  page, click  ![](figures/down.png)  in the  **SSL**  field to download the root certificate or certificate bundle.
5.  Upload the root certificate to the ECS or save it to the device to be connected to the DB instance.

    Import the root certificate to the Linux OS on the ECS. For details, see  [How Can I Import the Root Certificate to the Windows or Linux OS?](how-can-i-import-the-root-certificate-to-the-windows-or-linux-os.md)

6.  Run the following command to connect to an RDS DB instance. The Linux OS is used as an example.

    **psql --no-readline -h **_<host\>_ **-p** _<port\>_ **"dbname=**_<database\>_ **user=**_<user\> _**sslmode=verify-ca sslrootcert=**_<ca-file-directory\>_**"**

    **Table  2**  Parameter description

    <a name="table518415566128"></a>
    <table><thead align="left"><tr id="row151851356191216"><th class="cellrowborder" valign="top" width="20.44%" id="mcps1.2.3.1.1"><p id="p0185456141212"><a name="p0185456141212"></a><a name="p0185456141212"></a><strong id="b155923258558"><a name="b155923258558"></a><a name="b155923258558"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="79.56%" id="mcps1.2.3.1.2"><p id="p8185175611216"><a name="p8185175611216"></a><a name="p8185175611216"></a><strong id="b1344817261559"><a name="b1344817261559"></a><a name="b1344817261559"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11185195613125"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.3.1.1 "><p id="p1918545617124"><a name="p1918545617124"></a><a name="p1918545617124"></a><em id="i14948141810139"><a name="i14948141810139"></a><a name="i14948141810139"></a>&lt;host&gt;</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="79.56%" headers="mcps1.2.3.1.2 "><p id="p19362123813218"><a name="p19362123813218"></a><a name="p19362123813218"></a>Indicates the IP address of the primary DB instance. To obtain this parameter, go to the <span class="uicontrol" id="uicontrol1594616278555"><a name="uicontrol1594616278555"></a><a name="uicontrol1594616278555"></a><b>Basic Information</b></span> page of the DB instance. If the DB instance is accessed through an EIP, the IP address can be found on the <strong id="b83916351554"><a name="b83916351554"></a><a name="b83916351554"></a>EIPs</strong> page.</p>
    </td>
    </tr>
    <tr id="row17185135615123"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.3.1.1 "><p id="p318516569128"><a name="p318516569128"></a><a name="p318516569128"></a><em id="i1837210367132"><a name="i1837210367132"></a><a name="i1837210367132"></a>&lt;port&gt;</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="79.56%" headers="mcps1.2.3.1.2 "><p id="p18185115611217"><a name="p18185115611217"></a><a name="p18185115611217"></a>Indicates the database port in use. The default value is <strong id="b1284293775511"><a name="b1284293775511"></a><a name="b1284293775511"></a>5432</strong>. To obtain this parameter, go to the <span class="uicontrol" id="uicontrol1284353745512"><a name="uicontrol1284353745512"></a><a name="uicontrol1284353745512"></a><b>Basic Information</b></span> page of the DB instance. The port number can be found in the <span class="uicontrol" id="uicontrol484313795510"><a name="uicontrol484313795510"></a><a name="uicontrol484313795510"></a><b>Database Port</b></span> field in the <span class="uicontrol" id="uicontrol6844113715556"><a name="uicontrol6844113715556"></a><a name="uicontrol6844113715556"></a><b>Connection Information</b></span> area.</p>
    </td>
    </tr>
    <tr id="row15185155621219"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.3.1.1 "><p id="p1418511561126"><a name="p1418511561126"></a><a name="p1418511561126"></a><em id="i166765404131"><a name="i166765404131"></a><a name="i166765404131"></a>&lt;database&gt;</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="79.56%" headers="mcps1.2.3.1.2 "><p id="p1018525621219"><a name="p1018525621219"></a><a name="p1018525621219"></a>Indicates the name of the database (the default database name is <strong id="b17860154145520"><a name="b17860154145520"></a><a name="b17860154145520"></a>postgres</strong>).</p>
    </td>
    </tr>
    <tr id="row61851256161215"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.3.1.1 "><p id="p1318519561123"><a name="p1318519561123"></a><a name="p1318519561123"></a><em id="i1661204612137"><a name="i1661204612137"></a><a name="i1661204612137"></a>&lt;user&gt;</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="79.56%" headers="mcps1.2.3.1.2 "><p id="p141859566124"><a name="p141859566124"></a><a name="p141859566124"></a>Indicates the username of the RDS database account. The default administrator is <strong id="b1816174416556"><a name="b1816174416556"></a><a name="b1816174416556"></a>root</strong>.</p>
    </td>
    </tr>
    <tr id="row9185175614121"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.3.1.1 "><p id="p2185356161210"><a name="p2185356161210"></a><a name="p2185356161210"></a><em id="i15739185012137"><a name="i15739185012137"></a><a name="i15739185012137"></a>&lt;ca-file-directory&gt;</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="79.56%" headers="mcps1.2.3.1.2 "><p id="p518535681210"><a name="p518535681210"></a><a name="p518535681210"></a>Indicates the directory of the CA certificate for the SSL connection. The certificate should be stored in the directory where the command is executed.</p>
    </td>
    </tr>
    <tr id="row753931512459"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.3.1.1 "><p id="p15401315164514"><a name="p15401315164514"></a><a name="p15401315164514"></a><strong id="b653882511523"><a name="b653882511523"></a><a name="b653882511523"></a>sslmode</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="79.56%" headers="mcps1.2.3.1.2 "><p id="p2540151594512"><a name="p2540151594512"></a><a name="p2540151594512"></a>Indicates the SSL connection mode. Set it to <strong id="b18802144914552"><a name="b18802144914552"></a><a name="b18802144914552"></a>verify-ca</strong> to use a CA to check whether the service is trusted.</p>
    </td>
    </tr>
    </tbody>
    </table>

    Enter the password of the database account if the following information is displayed:

    Password:

    For example, to connect to a DB instance through an SSL connection as user  **root**, run the following command:

    **psql --no-readline -h 192.168.0.44 -p 5432 "dbname=postgres user=root  sslmode=verify-ca sslrootcert=/root/ca.pem"**

    **Password:**

7.  The SSL connection is established if information similar to the following is displayed after you log in to the database:

    ```
    SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
    ```


