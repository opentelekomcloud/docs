# Obtaining the Cluster Connection Address<a name="dws_01_0033"></a>

## Scenario<a name="section26616723151647"></a>

You can access data warehouse clusters using different methods and the connection address of each connection method varies. This section describes how to view and obtain the private network address in the public cloud, public network address on the Internet, and JDBC connection strings.

To obtain the cluster connection address, use either of the following methods:

-   [Obtaining the Cluster Connection Address on the Connection Management Page](#section5539467151713)
-   [Obtaining the Cluster Access Addresses on the Basic Information Page](#section149501253104810)

## Obtaining the Cluster Connection Address on the Connection Management Page<a name="section5539467151713"></a>

1.  Log in to the DWS management console.
2.  In the navigation tree on the left, click  **Connection Management**.
3.  In the  **Data Warehouse Connection Information**  area, select an available cluster.

    You can only select clusters in the  **Available**  state.

    **Figure  1**  Connection information<a name="fig14123111115591"></a>  
    ![](figures/connection-information.png "connection-information")

4.  View and obtain the cluster connection information.

    -   **Private Network Address**
    -   **Public Network Address**
    -   **JDBC URL \(Private Network\)**
    -   **JDBC URL \(Public Network\)**
    -   **ODBC URL**

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   If no EIP is automatically assigned during cluster creation and  **Public Network Address**  is empty, click  **Bind EIP**  to bind an EIP to the cluster.   
    >-   If an EIP is bound during cluster creation, click  **Unbind EIP**  to unbind the EIP.   


## Obtaining the Cluster Access Addresses on the Basic Information Page<a name="section149501253104810"></a>

1.  Log in to the management console at  [https://console.otc.t-systems.com/dws/](https://console.otc.t-systems.com/dws/).
2.  In the navigation tree on the left, click  **Cluster Management**.
3.  In the cluster list, click the name of the cluster that you want to view. The  **Basic Information**  page is displayed.
4.  In the  **Database Attribute**  area, view and obtain the cluster's access address information, including the private network address and public network address.

    **Figure  2**  Access addresses<a name="fig114601558858"></a>  
    ![](figures/access-addresses.png "access-addresses")

    **Table  1**  Database attribute parameters

    <a name="table878289143910"></a>
    <table><thead align="left"><tr id="row107835915393"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.3.1.1"><p id="p77831797399"><a name="p77831797399"></a><a name="p77831797399"></a><strong id="b84235270692541"><a name="b84235270692541"></a><a name="b84235270692541"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="76%" id="mcps1.2.3.1.2"><p id="p137830993917"><a name="p137830993917"></a><a name="p137830993917"></a><strong id="b842352706181449"><a name="b842352706181449"></a><a name="b842352706181449"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11404121572"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p830515405276"><a name="p830515405276"></a><a name="p830515405276"></a>Default Database</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p10308184022711"><a name="p10308184022711"></a><a name="p10308184022711"></a>Database that is automatically created during cluster creation. When you connect to the cluster for the first time, you need to connect to the default database.</p>
    </td>
    </tr>
    <tr id="row1913311541965"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p1955610197325"><a name="p1955610197325"></a><a name="p1955610197325"></a>Initial Administrator</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p1355601903215"><a name="p1355601903215"></a><a name="p1355601903215"></a>Administrator user specified during cluster creation. When you connect to the cluster for the first time, you need to use the initial administrator and password to connect to the default database.</p>
    </td>
    </tr>
    <tr id="row1083211501964"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p193208401279"><a name="p193208401279"></a><a name="p193208401279"></a>Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p203223409278"><a name="p203223409278"></a><a name="p203223409278"></a>Port for accessing the cluster database over the public network or private network. Database port specified during cluster creation. It is used to listen to client connections.</p>
    </td>
    </tr>
    <tr id="row129517471462"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p1945102733413"><a name="p1945102733413"></a><a name="p1945102733413"></a>JDBC URL (Private Network)</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p17451127133410"><a name="p17451127133410"></a><a name="p17451127133410"></a>In the private network environment, you can use the JDBC URL (private network) to connect to the cluster when developing applications.</p>
    </td>
    </tr>
    <tr id="row58581742162"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p5340194014273"><a name="p5340194014273"></a><a name="p5340194014273"></a>JDBC URL (Public Network)</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p21271330356"><a name="p21271330356"></a><a name="p21271330356"></a>In the public network environment, you can use the JDBC URL (public network) to connect to the cluster when developing applications.</p>
    </td>
    </tr>
    <tr id="row1278775864518"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p17422209466"><a name="p17422209466"></a><a name="p17422209466"></a>Private Network Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p124255014619"><a name="p124255014619"></a><a name="p124255014619"></a>Name of the domain for accessing the database in the cluster through the private network. The private network domain address is automatically generated when you create a cluster. The default naming rule is as follows: cluster name.dws.otc-tsi.de</p>
    <div class="note" id="note144260547564"><a name="note144260547564"></a><a name="note144260547564"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p244575418567"><a name="p244575418567"></a><a name="p244575418567"></a>If the cluster name does not comply with the domain name standards, the prefix of the default access domain name will be adjusted accordingly.</p>
    </div></div>
    <p id="p342513044618"><a name="p342513044618"></a><a name="p342513044618"></a>Click <strong id="b84235270620162"><a name="b84235270620162"></a><a name="b84235270620162"></a>Modify</strong> to change the private network access domain name. The access domain name contains 4 to 63 characters, which consist of letters, digits, and hyphens (-), and must start with a letter.</p>
    <p id="p1389192415716"><a name="p1389192415716"></a><a name="p1389192415716"></a>For more information, see section <a href="managing-access-domain-names.md">Managing Access Domain Names</a>.</p>
    </td>
    </tr>
    <tr id="row197835916390"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p177837983914"><a name="p177837983914"></a><a name="p177837983914"></a>Private Network IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p137832943917"><a name="p137832943917"></a><a name="p137832943917"></a>IP address for accessing the database in the cluster through the private network. The private network address is automatically generated when you create a cluster.</p>
    </td>
    </tr>
    <tr id="row16870618204610"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p677962610462"><a name="p677962610462"></a><a name="p677962610462"></a>Public Network Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p107841026134612"><a name="p107841026134612"></a><a name="p107841026134612"></a>Name of the domain for accessing the database in the cluster through the public network. </p>
    <div class="note" id="note8787132634615"><a name="note8787132634615"></a><a name="note8787132634615"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul4787192618461"></a><a name="ul4787192618461"></a><ul id="ul4787192618461"><li>If you have not bound an EIP to the cluster, <span class="parmname" id="parmname769647905114214"><a name="parmname769647905114214"></a><a name="parmname769647905114214"></a><b>Public Network IP Address</b></span>, <span class="parmname" id="parmname769647905114221"><a name="parmname769647905114221"></a><a name="parmname769647905114221"></a><b>Public Network Port</b></span>, and <span class="parmname" id="parmname769647905114236"><a name="parmname769647905114236"></a><a name="parmname769647905114236"></a><b>Public Network Domain Name</b></span> are left blank.</li><li>If you bind an EIP during cluster creation, the public network domain name is automatically generated. The default naming rule is as follows: cluster name.dws.t-systems.com</li><li>Bind an EIP to the cluster before binding the public network domain name to the cluster. Click <span class="uicontrol" id="uicontrol299876375201943"><a name="uicontrol299876375201943"></a><a name="uicontrol299876375201943"></a><b>Create</b></span> to bind the public network domain name to the cluster.</li><li>You can click <span class="uicontrol" id="uicontrol56641847592555"><a name="uicontrol56641847592555"></a><a name="uicontrol56641847592555"></a><b>Modify</b></span> to modify the public network domain name bound to the cluster. The domain name contains 4 to 63 characters, which consist of letters, digits, and hyphens (-), and must start with a letter.</li><li>You can click <span class="uicontrol" id="uicontrol127106090692650"><a name="uicontrol127106090692650"></a><a name="uicontrol127106090692650"></a><b>Release</b></span> to release the public network domain name bound to the cluster.</li></ul>
    </div></div>
    <p id="p1017894116564"><a name="p1017894116564"></a><a name="p1017894116564"></a>For more information, see section <a href="managing-access-domain-names.md">Managing Access Domain Names</a>.</p>
    </td>
    </tr>
    <tr id="row16299125111411"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p15299135164118"><a name="p15299135164118"></a><a name="p15299135164118"></a>Public Network IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p8299951174119"><a name="p8299951174119"></a><a name="p8299951174119"></a>IP address for accessing the database in the cluster through the public network. </p>
    <div class="note" id="note68025695012"><a name="note68025695012"></a><a name="note68025695012"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul198032619509"></a><a name="ul198032619509"></a><ul id="ul198032619509"><li>If no EIP is assigned during cluster creation and <span class="parmname" id="parmname1997655969756_3"><a name="parmname1997655969756_3"></a><a name="parmname1997655969756_3"></a><b>Public Network IP Address</b></span> is empty, click <span class="parmname" id="parmname12531424949947_3"><a name="parmname12531424949947_3"></a><a name="parmname12531424949947_3"></a><b>Bind EIP</b></span> to bind an EIP to the cluster. </li><li>If an EIP is bound during cluster creation, click <span class="parmname" id="parmname13806863502"><a name="parmname13806863502"></a><a name="parmname13806863502"></a><b>Unbind EIP</b></span> to unbind the EIP. </li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row1816181020814"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p13171110988"><a name="p13171110988"></a><a name="p13171110988"></a>ODBC URL</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p18199101889"><a name="p18199101889"></a><a name="p18199101889"></a>In DWS, you can use an ODBC driver to connect to the database. The drivers can connect to the database through the ECS in the public cloud or over the Internet.</p>
    </td>
    </tr>
    </tbody>
    </table>


