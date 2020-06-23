# Querying DB Instances<a name="dds_api_0023"></a>

## Function<a name="section6603527917262"></a>

This API is used to query DB instances based on specified conditions.

## URI<a name="section2266321117262"></a>

-   URI format

    GET /v3/\{project\_id\}/instances?id=\{id\}&name=\{name\}&mode=\{mode\}&datastore\_type=\{datastore\_type\}&vpc\_id=\{vpc\_id\}&subnet\_id=\{subnet\_id\}&offset=\{offset\}&limit=\{limit\}

-   Parameter description

    **Table  1**  Parameter description

    <a name="table126251026172611"></a>
    <table><thead align="left"><tr id="row1567132719261"><th class="cellrowborder" valign="top" width="17.41%" id="mcps1.2.5.1.1"><p id="p1167122711267"><a name="p1167122711267"></a><a name="p1167122711267"></a><strong id="b842352706102328_1"><a name="b842352706102328_1"></a><a name="b842352706102328_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="10.12%" id="mcps1.2.5.1.2"><p id="p9671727172610"><a name="p9671727172610"></a><a name="p9671727172610"></a><strong id="b17220193216479"><a name="b17220193216479"></a><a name="b17220193216479"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.18%" id="mcps1.2.5.1.3"><p id="p14434135218914"><a name="p14434135218914"></a><a name="p14434135218914"></a><strong id="b179712342471"><a name="b179712342471"></a><a name="b179712342471"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="59.29%" id="mcps1.2.5.1.4"><p id="p2775334615440"><a name="p2775334615440"></a><a name="p2775334615440"></a><strong id="b27543594911"><a name="b27543594911"></a><a name="b27543594911"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16678272266"><td class="cellrowborder" valign="top" width="17.41%" headers="mcps1.2.5.1.1 "><p id="p146718273268"><a name="p146718273268"></a><a name="p146718273268"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.12%" headers="mcps1.2.5.1.2 "><p id="p1167202762618"><a name="p1167202762618"></a><a name="p1167202762618"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.18%" headers="mcps1.2.5.1.3 "><p id="p746045218919"><a name="p746045218919"></a><a name="p746045218919"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.29%" headers="mcps1.2.5.1.4 "><p id="p567827152614"><a name="p567827152614"></a><a name="p567827152614"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row36702720266"><td class="cellrowborder" valign="top" width="17.41%" headers="mcps1.2.5.1.1 "><p id="p86772719262"><a name="p86772719262"></a><a name="p86772719262"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.12%" headers="mcps1.2.5.1.2 "><p id="p17692270260"><a name="p17692270260"></a><a name="p17692270260"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.18%" headers="mcps1.2.5.1.3 "><p id="p3470652997"><a name="p3470652997"></a><a name="p3470652997"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.29%" headers="mcps1.2.5.1.4 "><p id="p156917276261"><a name="p156917276261"></a><a name="p156917276261"></a>Specifies the DB instance ID.</p>
    </td>
    </tr>
    <tr id="row1869102722612"><td class="cellrowborder" valign="top" width="17.41%" headers="mcps1.2.5.1.1 "><p id="p1869927112614"><a name="p1869927112614"></a><a name="p1869927112614"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.12%" headers="mcps1.2.5.1.2 "><p id="p96952719266"><a name="p96952719266"></a><a name="p96952719266"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.18%" headers="mcps1.2.5.1.3 "><p id="p83091759796"><a name="p83091759796"></a><a name="p83091759796"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.29%" headers="mcps1.2.5.1.4 "><p id="p1269227192619"><a name="p1269227192619"></a><a name="p1269227192619"></a>Specifies the DB instance name.</p>
    <p id="p1069142722615"><a name="p1069142722615"></a><a name="p1069142722615"></a>If you use asterisk (*) at the beginning of the name, fuzzy search results are returned. Otherwise, the exact results are returned.</p>
    <div class="note" id="note28771940133312"><a name="note28771940133312"></a><a name="note28771940133312"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p158802040153320"><a name="p158802040153320"></a><a name="p158802040153320"></a>The asterisk (*) is a reserved character in the system and cannot be used alone.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row8691527142613"><td class="cellrowborder" valign="top" width="17.41%" headers="mcps1.2.5.1.1 "><p id="p1269162762611"><a name="p1269162762611"></a><a name="p1269162762611"></a>mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.12%" headers="mcps1.2.5.1.2 "><p id="p1969162711264"><a name="p1969162711264"></a><a name="p1969162711264"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.18%" headers="mcps1.2.5.1.3 "><p id="p1131710596914"><a name="p1131710596914"></a><a name="p1131710596914"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.29%" headers="mcps1.2.5.1.4 "><p id="p13346172812125"><a name="p13346172812125"></a><a name="p13346172812125"></a>Specifies the instance type.</p>
    <a name="ul985874012144"></a><a name="ul985874012144"></a><ul id="ul985874012144"><li><strong id="b1759118594118"><a name="b1759118594118"></a><a name="b1759118594118"></a>Sharding</strong> indicates the cluster instance.</li><li><strong id="b920512312214"><a name="b920512312214"></a><a name="b920512312214"></a>ReplicaSet</strong> indicate the replica set instance.</li></ul>
    </td>
    </tr>
    <tr id="row36972732618"><td class="cellrowborder" valign="top" width="17.41%" headers="mcps1.2.5.1.1 "><p id="p169827152616"><a name="p169827152616"></a><a name="p169827152616"></a>datastore_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.12%" headers="mcps1.2.5.1.2 "><p id="p1069127122616"><a name="p1069127122616"></a><a name="p1069127122616"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.18%" headers="mcps1.2.5.1.3 "><p id="p1032616597916"><a name="p1032616597916"></a><a name="p1032616597916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.29%" headers="mcps1.2.5.1.4 "><p id="p87911162456"><a name="p87911162456"></a><a name="p87911162456"></a>Specifies the database type. The value is <strong id="b13671219172619"><a name="b13671219172619"></a><a name="b13671219172619"></a>DDS-Community</strong>.</p>
    </td>
    </tr>
    <tr id="row36942716264"><td class="cellrowborder" valign="top" width="17.41%" headers="mcps1.2.5.1.1 "><p id="p10691627152613"><a name="p10691627152613"></a><a name="p10691627152613"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.12%" headers="mcps1.2.5.1.2 "><p id="p16697276266"><a name="p16697276266"></a><a name="p16697276266"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.18%" headers="mcps1.2.5.1.3 "><p id="p201521856105"><a name="p201521856105"></a><a name="p201521856105"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.29%" headers="mcps1.2.5.1.4 "><p id="p1169727192611"><a name="p1169727192611"></a><a name="p1169727192611"></a>Specifies the VPC ID. You can log in to the VPC console and obtain the ID of the VPC where the DDS instance is located.</p>
    </td>
    </tr>
    <tr id="row186918275261"><td class="cellrowborder" valign="top" width="17.41%" headers="mcps1.2.5.1.1 "><p id="p16992710268"><a name="p16992710268"></a><a name="p16992710268"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.12%" headers="mcps1.2.5.1.2 "><p id="p269142782612"><a name="p269142782612"></a><a name="p269142782612"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.18%" headers="mcps1.2.5.1.3 "><p id="p171621557103"><a name="p171621557103"></a><a name="p171621557103"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.29%" headers="mcps1.2.5.1.4 "><p id="p136912273263"><a name="p136912273263"></a><a name="p136912273263"></a>Specifies the network ID of the subnet. You can log in to the VPC console and obtain the network ID of the subnet in the VPC where the DDS instance is located.</p>
    </td>
    </tr>
    <tr id="row6691627162611"><td class="cellrowborder" valign="top" width="17.41%" headers="mcps1.2.5.1.1 "><p id="p196902716268"><a name="p196902716268"></a><a name="p196902716268"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.12%" headers="mcps1.2.5.1.2 "><p id="p2691227122610"><a name="p2691227122610"></a><a name="p2691227122610"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.18%" headers="mcps1.2.5.1.3 "><p id="p161771450106"><a name="p161771450106"></a><a name="p161771450106"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.29%" headers="mcps1.2.5.1.4 "><p id="p68771249161712"><a name="p68771249161712"></a><a name="p68771249161712"></a>Specifies the index position. The query starts from the next instance creation time indexed by this parameter under a specified project. If offset is set to N, the resource query starts from the N+1 piece of data </p>
    <p id="p164514316252"><a name="p164514316252"></a><a name="p164514316252"></a>The value must be greater than or equal to <strong id="b17830103613368"><a name="b17830103613368"></a><a name="b17830103613368"></a>0</strong>. If this parameter is not transferred, offset is set to <strong id="b14603291356"><a name="b14603291356"></a><a name="b14603291356"></a>0</strong> by default, indicating that the query starts from the latest created DB instance.</p>
    </td>
    </tr>
    <tr id="row15691927142620"><td class="cellrowborder" valign="top" width="17.41%" headers="mcps1.2.5.1.1 "><p id="p1269827152619"><a name="p1269827152619"></a><a name="p1269827152619"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.12%" headers="mcps1.2.5.1.2 "><p id="p14697274268"><a name="p14697274268"></a><a name="p14697274268"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.18%" headers="mcps1.2.5.1.3 "><p id="p1189155111018"><a name="p1189155111018"></a><a name="p1189155111018"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.29%" headers="mcps1.2.5.1.4 "><p id="p16281630205219"><a name="p16281630205219"></a><a name="p16281630205219"></a>Specifies the maximum allowed number of DB instances.</p>
    <p id="p15258114142818"><a name="p15258114142818"></a><a name="p15258114142818"></a>The value ranges from 1 to 100. If this parameter is not transferred, the first 100 DB instances are queried by default.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="section807511017262"></a>

-   Request header

    Query all DB instances.

    ```
    GET https://DDS endpoint/v3/0483b6b16e954cb88930a360d2c4e663/instances
    ```

    Query DB instances based on specified conditions.

    ```
    GET https://DDS endpoint/v3/0483b6b16e954cb88930a360d2c4e663/instances?offset=0&limit=10&id=ed7cc6166ec24360a5ed5c5c9c2ed726in02&name=hy&mode=ReplicaSet&datastore_type=DDS-Community&vpc_id=19e5d45d-70fd-4a91-87e9-b27e71c9891f&subnet_id=bd51fb45-2dcb-4296-8783-8623bfe89bb7
    ```


-   Request body

    N/A


## Responses<a name="section4828447917262"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table54571314103317"></a>
    <table><thead align="left"><tr id="row3459121463318"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p91816414334"><a name="p91816414334"></a><a name="p91816414334"></a><strong id="b842352706102328_3"><a name="b842352706102328_3"></a><a name="b842352706102328_3"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p123216414335"><a name="p123216414335"></a><a name="p123216414335"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p114801652119"><a name="p114801652119"></a><a name="p114801652119"></a><strong id="b492015414308"><a name="b492015414308"></a><a name="b492015414308"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16459161403314"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p12459414153315"><a name="p12459414153315"></a><a name="p12459414153315"></a>instances</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1573120282446"><a name="p1573120282446"></a><a name="p1573120282446"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10459614163315"><a name="p10459614163315"></a><a name="p10459614163315"></a>Indicates the DB instance information. For more information, see <a href="#table4062895917262">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row1729824910274"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1553519588278"><a name="p1553519588278"></a><a name="p1553519588278"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p153595819277"><a name="p153595819277"></a><a name="p153595819277"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14535165814272"><a name="p14535165814272"></a><a name="p14535165814272"></a>Indicates the total number of queried records.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  instances field data structure description

    <a name="table4062895917262"></a>
    <table><thead align="left"><tr id="row2045312717262"><th class="cellrowborder" valign="top" width="22.11%" id="mcps1.2.4.1.1"><p id="p4609059717262"><a name="p4609059717262"></a><a name="p4609059717262"></a><strong id="b84235270691445_3"><a name="b84235270691445_3"></a><a name="b84235270691445_3"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.76%" id="mcps1.2.4.1.2"><p id="p4235091617262"><a name="p4235091617262"></a><a name="p4235091617262"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.129999999999995%" id="mcps1.2.4.1.3"><p id="p1597516542118"><a name="p1597516542118"></a><a name="p1597516542118"></a><strong id="b1872244233012"><a name="b1872244233012"></a><a name="b1872244233012"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3366877217262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p4281598817262"><a name="p4281598817262"></a><a name="p4281598817262"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p4554301317262"><a name="p4554301317262"></a><a name="p4554301317262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p6510543817262"><a name="p6510543817262"></a><a name="p6510543817262"></a>Indicates the DB instance ID.</p>
    </td>
    </tr>
    <tr id="row1586864310283"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p1658895710287"><a name="p1658895710287"></a><a name="p1658895710287"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p1658815722818"><a name="p1658815722818"></a><a name="p1658815722818"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p1658813578282"><a name="p1658813578282"></a><a name="p1658813578282"></a>Indicates the DB instance name.</p>
    </td>
    </tr>
    <tr id="row4973938517262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p235838917262"><a name="p235838917262"></a><a name="p235838917262"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p5681181717262"><a name="p5681181717262"></a><a name="p5681181717262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p2682840893927"><a name="p2682840893927"></a><a name="p2682840893927"></a>Indicates the DB instance status.</p>
    <p id="p3835449417262"><a name="p3835449417262"></a><a name="p3835449417262"></a>Valid value:</p>
    <a name="ul19906938143616"></a><a name="ul19906938143616"></a><ul id="ul19906938143616"><li><strong id="b842352706165621"><a name="b842352706165621"></a><a name="b842352706165621"></a>normal</strong>: indicates that the instance is running properly.</li><li><strong id="b842352706165427"><a name="b842352706165427"></a><a name="b842352706165427"></a>abnormal</strong>: indicates that the instance is abnormal.</li><li><strong id="b1574116135617"><a name="b1574116135617"></a><a name="b1574116135617"></a>creating</strong>: indicates that the instance is being created.</li><li><strong id="b71864349563"><a name="b71864349563"></a><a name="b71864349563"></a>data_disk_full</strong>: indicates that the instance disk is full.</li><li><strong id="b1045718506561"><a name="b1045718506561"></a><a name="b1045718506561"></a>createfail</strong>: indicates that the instance failed to be created.</li><li><strong id="b1796311319577"><a name="b1796311319577"></a><a name="b1796311319577"></a>enlargefail</strong>: indicates that nodes failed to be added to the instance.</li></ul>
    </td>
    </tr>
    <tr id="row1542344713010"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p7306854153018"><a name="p7306854153018"></a><a name="p7306854153018"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p530665414307"><a name="p530665414307"></a><a name="p530665414307"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p18306155453011"><a name="p18306155453011"></a><a name="p18306155453011"></a>Indicates the database port number. The port range is 2100 to 9500.</p>
    </td>
    </tr>
    <tr id="row547219133119"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p12349101213314"><a name="p12349101213314"></a><a name="p12349101213314"></a>mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p1349191216316"><a name="p1349191216316"></a><a name="p1349191216316"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p41801225203113"><a name="p41801225203113"></a><a name="p41801225203113"></a>Indicates the instance type, which is the same as the request parameter.</p>
    </td>
    </tr>
    <tr id="row161256327317"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p12846184013119"><a name="p12846184013119"></a><a name="p12846184013119"></a>region</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p11846194063118"><a name="p11846194063118"></a><a name="p11846194063118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p208461540163116"><a name="p208461540163116"></a><a name="p208461540163116"></a>Indicates the region where the DB instance is deployed.</p>
    </td>
    </tr>
    <tr id="row143345492318"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p1916717590310"><a name="p1916717590310"></a><a name="p1916717590310"></a>datastore</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p175443254512"><a name="p175443254512"></a><a name="p175443254512"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p17167195923116"><a name="p17167195923116"></a><a name="p17167195923116"></a>Indicates the database information. For more information, see <a href="#table5636104310403">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row373410289323"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p1585623418326"><a name="p1585623418326"></a><a name="p1585623418326"></a>engine</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p7856123410326"><a name="p7856123410326"></a><a name="p7856123410326"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p2856934113215"><a name="p2856934113215"></a><a name="p2856934113215"></a>Indicates the storage engine. The value is <strong id="b4533143018420"><a name="b4533143018420"></a><a name="b4533143018420"></a>wiredTiger</strong>.</p>
    </td>
    </tr>
    <tr id="row1199640717262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p3218490217262"><a name="p3218490217262"></a><a name="p3218490217262"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p5684029417262"><a name="p5684029417262"></a><a name="p5684029417262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p64320678"><a name="p64320678"></a><a name="p64320678"></a>Indicates the DB instance creation time.</p>
    </td>
    </tr>
    <tr id="row10346151318330"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p2305123816371"><a name="p2305123816371"></a><a name="p2305123816371"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p1531123818378"><a name="p1531123818378"></a><a name="p1531123818378"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p831613813378"><a name="p831613813378"></a><a name="p831613813378"></a>Indicates the time when a DB instance is updated.</p>
    </td>
    </tr>
    <tr id="row19202155803713"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p18811780381"><a name="p18811780381"></a><a name="p18811780381"></a>db_user_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p13881188103818"><a name="p13881188103818"></a><a name="p13881188103818"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p138819883816"><a name="p138819883816"></a><a name="p138819883816"></a>Indicates the default username. The value is <strong id="b55161546547"><a name="b55161546547"></a><a name="b55161546547"></a>rwuser</strong>.</p>
    </td>
    </tr>
    <tr id="row521631217262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p16168720183816"><a name="p16168720183816"></a><a name="p16168720183816"></a>ssl</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p11168162012385"><a name="p11168162012385"></a><a name="p11168162012385"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p1486912373620"><a name="p1486912373620"></a><a name="p1486912373620"></a>Indicates that SSL is enabled or not.</p>
    <a name="ul1390275817429"></a><a name="ul1390275817429"></a><ul id="ul1390275817429"><li><strong id="b842352706203930"><a name="b842352706203930"></a><a name="b842352706203930"></a>1</strong>: indicate that SSL is enabled.</li><li><strong id="b79641341135815"><a name="b79641341135815"></a><a name="b79641341135815"></a>0</strong>: indicate that SSL is disabled.</li></ul>
    </td>
    </tr>
    <tr id="row6076080317262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p6101242203816"><a name="p6101242203816"></a><a name="p6101242203816"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p17101134219381"><a name="p17101134219381"></a><a name="p17101134219381"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p21019429383"><a name="p21019429383"></a><a name="p21019429383"></a>Indicates the VPC ID.</p>
    </td>
    </tr>
    <tr id="row6085477618055"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p010104233819"><a name="p010104233819"></a><a name="p010104233819"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p5101142163813"><a name="p5101142163813"></a><a name="p5101142163813"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p01011942123813"><a name="p01011942123813"></a><a name="p01011942123813"></a>Indicates the subnet ID.</p>
    </td>
    </tr>
    <tr id="row2423602017262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p1101242163812"><a name="p1101242163812"></a><a name="p1101242163812"></a>security_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p110134218384"><a name="p110134218384"></a><a name="p110134218384"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p10101342103816"><a name="p10101342103816"></a><a name="p10101342103816"></a>Indicates the security group ID.</p>
    </td>
    </tr>
    <tr id="row3836683017262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p169221846193912"><a name="p169221846193912"></a><a name="p169221846193912"></a>backup_strategy</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p615761254510"><a name="p615761254510"></a><a name="p615761254510"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p992212464390"><a name="p992212464390"></a><a name="p992212464390"></a>Indicates the backup policy. For more information, see <a href="#table50876711173859">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row5158348917262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p9180186194016"><a name="p9180186194016"></a><a name="p9180186194016"></a>pay_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p31801262406"><a name="p31801262406"></a><a name="p31801262406"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p135518404115"><a name="p135518404115"></a><a name="p135518404115"></a>Indicates the billing mode. <strong id="b59581846105812"><a name="b59581846105812"></a><a name="b59581846105812"></a>0</strong>: indicates the pay-per-use billing mode.</p>
    </td>
    </tr>
    <tr id="row26042558155946"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p31813615407"><a name="p31813615407"></a><a name="p31813615407"></a>maintenance_window</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p0181106124014"><a name="p0181106124014"></a><a name="p0181106124014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p18181116184018"><a name="p18181116184018"></a><a name="p18181116184018"></a>Indicates the maintenance time window.</p>
    </td>
    </tr>
    <tr id="row58201947133019"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p17820747153013"><a name="p17820747153013"></a><a name="p17820747153013"></a>groups</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p18968617194620"><a name="p18968617194620"></a><a name="p18968617194620"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p158202479305"><a name="p158202479305"></a><a name="p158202479305"></a>Indicates group information. For more information, see <a href="#table0581104824211">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row6543147717262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p17181186164013"><a name="p17181186164013"></a><a name="p17181186164013"></a>disk_encryption_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p318115674014"><a name="p318115674014"></a><a name="p318115674014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p1218176164019"><a name="p1218176164019"></a><a name="p1218176164019"></a>Indicates the disk encryption key ID.</p>
    </td>
    </tr>
    <tr id="row2350798811137"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p418111674018"><a name="p418111674018"></a><a name="p418111674018"></a>time_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p1318126154014"><a name="p1318126154014"></a><a name="p1318126154014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p1427217032614"><a name="p1427217032614"></a><a name="p1427217032614"></a>Indicates the time zone.</p>
    </td>
    </tr>
    <tr id="row20543634133116"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p1654373473114"><a name="p1654373473114"></a><a name="p1654373473114"></a>actions</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p1788575916475"><a name="p1788575916475"></a><a name="p1788575916475"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p16629413187"><a name="p16629413187"></a><a name="p16629413187"></a>Indicates the operation that is executed on the DB instance.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  datastore field data structure description

    <a name="table5636104310403"></a>
    <table><thead align="left"><tr id="row1165216437409"><th class="cellrowborder" valign="top" width="23.93%" id="mcps1.2.4.1.1"><p id="p12657343144015"><a name="p12657343144015"></a><a name="p12657343144015"></a><strong id="b199564518493"><a name="b199564518493"></a><a name="b199564518493"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.62%" id="mcps1.2.4.1.2"><p id="p16621743124010"><a name="p16621743124010"></a><a name="p16621743124010"></a><strong id="b842352706164541_1_1"><a name="b842352706164541_1_1"></a><a name="b842352706164541_1_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.449999999999996%" id="mcps1.2.4.1.3"><p id="p62502217220"><a name="p62502217220"></a><a name="p62502217220"></a><strong id="b18480154319307"><a name="b18480154319307"></a><a name="b18480154319307"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1267084317404"><td class="cellrowborder" valign="top" width="23.93%" headers="mcps1.2.4.1.1 "><p id="p1667834315404"><a name="p1667834315404"></a><a name="p1667834315404"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.2.4.1.2 "><p id="p1568254314012"><a name="p1568254314012"></a><a name="p1568254314012"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.449999999999996%" headers="mcps1.2.4.1.3 "><p id="p2029419174111"><a name="p2029419174111"></a><a name="p2029419174111"></a>Indicates the DB engine.</p>
    </td>
    </tr>
    <tr id="row868810436406"><td class="cellrowborder" valign="top" width="23.93%" headers="mcps1.2.4.1.1 "><p id="p969244314404"><a name="p969244314404"></a><a name="p969244314404"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.2.4.1.2 "><p id="p1769664320400"><a name="p1769664320400"></a><a name="p1769664320400"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.449999999999996%" headers="mcps1.2.4.1.3 "><p id="p1129418914416"><a name="p1129418914416"></a><a name="p1129418914416"></a>Indicates the database version.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  backup\_strategy field data structure description

    <a name="table50876711173859"></a>
    <table><thead align="left"><tr id="row26941115173859"><th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.1"><p id="p44284799173859"><a name="p44284799173859"></a><a name="p44284799173859"></a><strong id="b84235270691445_15"><a name="b84235270691445_15"></a><a name="b84235270691445_15"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.589999999999996%" id="mcps1.2.4.1.2"><p id="p30298928173859"><a name="p30298928173859"></a><a name="p30298928173859"></a><strong id="b842352706164541_15"><a name="b842352706164541_15"></a><a name="b842352706164541_15"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.19%" id="mcps1.2.4.1.3"><p id="p01931951822"><a name="p01931951822"></a><a name="p01931951822"></a><strong id="b12218104443012"><a name="b12218104443012"></a><a name="b12218104443012"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9102564173859"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p1835143820417"><a name="p1835143820417"></a><a name="p1835143820417"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.4.1.2 "><p id="p98352388418"><a name="p98352388418"></a><a name="p98352388418"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.19%" headers="mcps1.2.4.1.3 "><p id="p883563844112"><a name="p883563844112"></a><a name="p883563844112"></a>Indicates the backup time window. Automated backups will be triggered during the backup time window. The current time is the UTC time.</p>
    </td>
    </tr>
    <tr id="row7902174173859"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p783518382416"><a name="p783518382416"></a><a name="p783518382416"></a>keep_days</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.4.1.2 "><p id="p16835163817415"><a name="p16835163817415"></a><a name="p16835163817415"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.19%" headers="mcps1.2.4.1.3 "><p id="p6835143816415"><a name="p6835143816415"></a><a name="p6835143816415"></a>Indicates the number of days to retain the generated backup files. The value range is from 0 to 732.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  groups field data structure description

    <a name="table0581104824211"></a>
    <table><thead align="left"><tr id="row1159824894215"><th class="cellrowborder" valign="top" width="23.369999999999997%" id="mcps1.2.4.1.1"><p id="p560414811427"><a name="p560414811427"></a><a name="p560414811427"></a><strong id="b7613539135413"><a name="b7613539135413"></a><a name="b7613539135413"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.99%" id="mcps1.2.4.1.2"><p id="p1609114834210"><a name="p1609114834210"></a><a name="p1609114834210"></a><strong id="b842352706164541_1_2"><a name="b842352706164541_1_2"></a><a name="b842352706164541_1_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.64%" id="mcps1.2.4.1.3"><p id="p38731481622"><a name="p38731481622"></a><a name="p38731481622"></a><strong id="b8973174417307"><a name="b8973174417307"></a><a name="b8973174417307"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15255328225"><td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.1 "><p id="p85262032112214"><a name="p85262032112214"></a><a name="p85262032112214"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.2 "><p id="p352643217225"><a name="p352643217225"></a><a name="p352643217225"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.64%" headers="mcps1.2.4.1.3 "><p id="p1081219472322"><a name="p1081219472322"></a><a name="p1081219472322"></a>Indicates the node type.</p>
    <p id="p102012214343"><a name="p102012214343"></a><a name="p102012214343"></a>Valid value:</p>
    <a name="ul64965214345"></a><a name="ul64965214345"></a><ul id="ul64965214345"><li>shard</li><li>config</li><li>mongos</li><li>replica</li></ul>
    </td>
    </tr>
    <tr id="row156194486423"><td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.1 "><p id="p194661421134312"><a name="p194661421134312"></a><a name="p194661421134312"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.2 "><p id="p16466162110439"><a name="p16466162110439"></a><a name="p16466162110439"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.64%" headers="mcps1.2.4.1.3 "><p id="p94661321194313"><a name="p94661321194313"></a><a name="p94661321194313"></a>Indicates the group ID. This parameter is valid only when the node type is shard or config.</p>
    </td>
    </tr>
    <tr id="row26331548174214"><td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.1 "><p id="p3466152115439"><a name="p3466152115439"></a><a name="p3466152115439"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.2 "><p id="p346672174311"><a name="p346672174311"></a><a name="p346672174311"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.64%" headers="mcps1.2.4.1.3 "><p id="p17466102112437"><a name="p17466102112437"></a><a name="p17466102112437"></a>Indicates the group name. This parameter is valid only when the node type is shard or config.</p>
    </td>
    </tr>
    <tr id="row1521173962210"><td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.1 "><p id="p5211039112214"><a name="p5211039112214"></a><a name="p5211039112214"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.2 "><p id="p4211173915228"><a name="p4211173915228"></a><a name="p4211173915228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.64%" headers="mcps1.2.4.1.3 "><p id="p20211163952216"><a name="p20211163952216"></a><a name="p20211163952216"></a>Indicates the group status. This parameter is valid only when the node type is shard or config.</p>
    </td>
    </tr>
    <tr id="row1170116144310"><td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.1 "><p id="p94661721134320"><a name="p94661721134320"></a><a name="p94661721134320"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.2 "><p id="p65461844134916"><a name="p65461844134916"></a><a name="p65461844134916"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.64%" headers="mcps1.2.4.1.3 "><p id="p66811129104611"><a name="p66811129104611"></a><a name="p66811129104611"></a>Indicates the volume information. For more information, see <a href="#table1149918231246">Table 7</a>. This parameter is valid only when the node type is shard, config, or replica. </p>
    </td>
    </tr>
    <tr id="row86761748134216"><td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.1 "><p id="p1446652144315"><a name="p1446652144315"></a><a name="p1446652144315"></a>nodes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.2 "><p id="p68087345011"><a name="p68087345011"></a><a name="p68087345011"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.64%" headers="mcps1.2.4.1.3 "><p id="p1246642104310"><a name="p1246642104310"></a><a name="p1246642104310"></a>Indicates node information. For more information, see <a href="#table3426155424213">Table 8</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7**  volume field data structure description

    <a name="table1149918231246"></a>
    <table><thead align="left"><tr id="row25301823182412"><th class="cellrowborder" valign="top" width="23.369999999999997%" id="mcps1.2.4.1.1"><p id="p3537102382413"><a name="p3537102382413"></a><a name="p3537102382413"></a><strong id="b84235270691445_11"><a name="b84235270691445_11"></a><a name="b84235270691445_11"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.99%" id="mcps1.2.4.1.2"><p id="p1454202332412"><a name="p1454202332412"></a><a name="p1454202332412"></a><strong id="b842352706164541_1_3"><a name="b842352706164541_1_3"></a><a name="b842352706164541_1_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.64%" id="mcps1.2.4.1.3"><p id="p1789113926"><a name="p1789113926"></a><a name="p1789113926"></a><strong id="b364615457303"><a name="b364615457303"></a><a name="b364615457303"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8581132319246"><td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.1 "><p id="p1958916239247"><a name="p1958916239247"></a><a name="p1958916239247"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.2 "><p id="p1594523132414"><a name="p1594523132414"></a><a name="p1594523132414"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.64%" headers="mcps1.2.4.1.3 "><p id="p13604122313246"><a name="p13604122313246"></a><a name="p13604122313246"></a>Indicates the disk size. Unit: GB</p>
    </td>
    </tr>
    <tr id="row1692220263912"><td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.1 "><p id="p118283923919"><a name="p118283923919"></a><a name="p118283923919"></a>used</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.2 "><p id="p082820953918"><a name="p082820953918"></a><a name="p082820953918"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.64%" headers="mcps1.2.4.1.3 "><p id="p8828195392"><a name="p8828195392"></a><a name="p8828195392"></a>Indicates the disk usage. Unit: GB</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8**  nodes field data structure description

    <a name="table3426155424213"></a>
    <table><thead align="left"><tr id="row104391354174216"><th class="cellrowborder" valign="top" width="23.369999999999997%" id="mcps1.2.4.1.1"><p id="p94421654184220"><a name="p94421654184220"></a><a name="p94421654184220"></a><strong id="b16580175410213"><a name="b16580175410213"></a><a name="b16580175410213"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.84%" id="mcps1.2.4.1.2"><p id="p94461854124211"><a name="p94461854124211"></a><a name="p94461854124211"></a><strong id="b842352706164541_1_5"><a name="b842352706164541_1_5"></a><a name="b842352706164541_1_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.790000000000006%" id="mcps1.2.4.1.3"><p id="p376812197219"><a name="p376812197219"></a><a name="p376812197219"></a><strong id="b9327144723017"><a name="b9327144723017"></a><a name="b9327144723017"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row739024810443"><td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.1 "><p id="p439094844410"><a name="p439094844410"></a><a name="p439094844410"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.84%" headers="mcps1.2.4.1.2 "><p id="p1139074834418"><a name="p1139074834418"></a><a name="p1139074834418"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.790000000000006%" headers="mcps1.2.4.1.3 "><p id="p10390204854416"><a name="p10390204854416"></a><a name="p10390204854416"></a>Indicates the node ID.</p>
    </td>
    </tr>
    <tr id="row1545510547425"><td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.1 "><p id="p388312397433"><a name="p388312397433"></a><a name="p388312397433"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.84%" headers="mcps1.2.4.1.2 "><p id="p17883139124313"><a name="p17883139124313"></a><a name="p17883139124313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.790000000000006%" headers="mcps1.2.4.1.3 "><p id="p14883839134318"><a name="p14883839134318"></a><a name="p14883839134318"></a>Indicates the node name.</p>
    </td>
    </tr>
    <tr id="row4180183094418"><td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.1 "><p id="p18583183954410"><a name="p18583183954410"></a><a name="p18583183954410"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.84%" headers="mcps1.2.4.1.2 "><p id="p1159113954419"><a name="p1159113954419"></a><a name="p1159113954419"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.790000000000006%" headers="mcps1.2.4.1.3 "><p id="p2060110393442"><a name="p2060110393442"></a><a name="p2060110393442"></a>Indicates the node status.</p>
    </td>
    </tr>
    <tr id="row247211545421"><td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.1 "><p id="p148831139144319"><a name="p148831139144319"></a><a name="p148831139144319"></a>role</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.84%" headers="mcps1.2.4.1.2 "><p id="p19883133914314"><a name="p19883133914314"></a><a name="p19883133914314"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.790000000000006%" headers="mcps1.2.4.1.3 "><p id="p1188323934310"><a name="p1188323934310"></a><a name="p1188323934310"></a>Indicates the node role.</p>
    <div class="p" id="p616216422484"><a name="p616216422484"></a><a name="p616216422484"></a>Valid value:<a name="ul152383354911"></a><a name="ul152383354911"></a><ul id="ul152383354911"><li><strong id="b46031534194617"><a name="b46031534194617"></a><a name="b46031534194617"></a>master</strong>: This value is returned for the mongos node.</li><li><strong id="b2076482110475"><a name="b2076482110475"></a><a name="b2076482110475"></a>Primary</strong>: This value is returned for the primary node of shards, primary node of configs, and primary node of a replica set.</li><li><strong id="b1896018125484"><a name="b1896018125484"></a><a name="b1896018125484"></a>Secondary</strong>: This value is returned for the secondary node of shards, secondary node of configs, and secondary node of a replica set.</li><li><strong id="b755213512488"><a name="b755213512488"></a><a name="b755213512488"></a>Hidden</strong>: This value is returned for the hidden node of shards, hidden node of configs, and hidden node of a replica set.</li><li><strong id="b183862049135419"><a name="b183862049135419"></a><a name="b183862049135419"></a>unknown</strong>. This value is returned when the node is abnormal.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row1250385474215"><td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.1 "><p id="p18834391436"><a name="p18834391436"></a><a name="p18834391436"></a>private_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.84%" headers="mcps1.2.4.1.2 "><p id="p788343916437"><a name="p788343916437"></a><a name="p788343916437"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.790000000000006%" headers="mcps1.2.4.1.3 "><p id="p20883113984310"><a name="p20883113984310"></a><a name="p20883113984310"></a>Indicates the private IP address of a node. This parameter is valid only for mongos nodes and replica set instances. The value exists after the ECS is created successfully. Otherwise, the value is <strong id="b183091849153512"><a name="b183091849153512"></a><a name="b183091849153512"></a>""</strong>.</p>
    </td>
    </tr>
    <tr id="row529663511457"><td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.1 "><p id="p1129643517459"><a name="p1129643517459"></a><a name="p1129643517459"></a>public_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.84%" headers="mcps1.2.4.1.2 "><p id="p229603514454"><a name="p229603514454"></a><a name="p229603514454"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.790000000000006%" headers="mcps1.2.4.1.3 "><p id="p8296143594510"><a name="p8296143594510"></a><a name="p8296143594510"></a>Indicates the EIP that has been bound. This parameter is valid only for mongos nodes of cluster instances and the primary and secondary nodes of replica set instances.</p>
    </td>
    </tr>
    <tr id="row155181554114214"><td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.1 "><p id="p398277124510"><a name="p398277124510"></a><a name="p398277124510"></a>spec_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.84%" headers="mcps1.2.4.1.2 "><p id="p148837395436"><a name="p148837395436"></a><a name="p148837395436"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.790000000000006%" headers="mcps1.2.4.1.3 "><p id="p12589718155110"><a name="p12589718155110"></a><a name="p12589718155110"></a>Indicates the resource specifications code. For details about the instance specifications, see the value of the <strong id="b385636151116"><a name="b385636151116"></a><a name="b385636151116"></a>flavors.spec_code</strong> parameter in <a href="querying-all-db-instance-specifications.md">Querying All DB Instance Specifications</a>.</p>
    </td>
    </tr>
    <tr id="row20724925103610"><td class="cellrowborder" valign="top" width="23.369999999999997%" headers="mcps1.2.4.1.1 "><p id="p572532514362"><a name="p572532514362"></a><a name="p572532514362"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.84%" headers="mcps1.2.4.1.2 "><p id="p19725112563616"><a name="p19725112563616"></a><a name="p19725112563616"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.790000000000006%" headers="mcps1.2.4.1.3 "><p id="p1472532514361"><a name="p1472532514361"></a><a name="p1472532514361"></a>Indicates the AZ.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:**   
    >The values of  **region**  and  **availability\_zone**  are used as examples.  


-   Response example

    Query all DB instances.

    ```
    { 
        "instances": [
            {
                "id": "8436a91546294036b75931e879882200in02",
                "name": "dds-efa6",
                "status": "normal",
                "port": "8635",
                "mode": "ReplicaSet",
                "region": "aaa",
                "datastore": {
                    "type": "DDS-Community",
                    "version": "3.2"
                },
                "engine": "wiredTiger",
                "created": "2019-01-17T07:05:52",
                "updated": "2019-01-17T07:05:47",
                "db_user_name": "rwuser",
                "ssl": "1",
                "vpc_id": "674e9b42-cd8d-4d25-a2e6-5abcc565b961",
                "subnet_id": "f1df08c5-71d1-406a-aff0-de435a51007b",
                "security_group_id": "7aa51dbf-5b63-40db-9724-dad3c4828b58",
                "backup_strategy": {
                    "start_time": "16:00-17:00",
                    "keep_days": 7
                },
                "pay_mode": "0",
                "maintenance_window": "02:00-06:00",
                "groups": [
                    {
                        "type": "replica",
                        "volume": {
                            "size": "10",
                            "used": "0.33"
                        },
                        "nodes": [
                            {
                                "id": "233eaac9c6f245c0bb9c2d21eea12d1bno02",
                                "name": "dds-efa6_replica_node_2",
                                "status": "normal",
                                "role": "Primary",
                                "private_ip": "192.168.0.174",
                                "public_ip": "",
                                "spec_code": "dds.mongodb.s2.medium.4.repset",
                                "availability_zone": "bbb"
                            },
                            {
                                "id": "d57d76d6320a4a7b86db82c317550c4ano02",
                                "name": "dds-efa6_replica_node_1",
                                "status": "normal",
                                "role": "Hidden",
                                "private_ip": "192.168.0.39",
                                "public_ip": "",
                                "spec_code": "dds.mongodb.s2.medium.4.repset",
                                "availability_zone": "bbb"
                            },
                            {
                                "id": "f46b0a1cf4d9400e9fd7af17f8742d37no02",
                                "name": "dds-efa6_replica_node_3",
                                "status": "normal",
                                "role": "Secondary",
                                "private_ip": "192.168.0.176",
                                "public_ip": "",
                                "spec_code": "dds.mongodb.s2.medium.4.repset",
                                "availability_zone": "bbb"
                            }
                        ]
                    }
                ],
                "time_zone": "",
                "actions": [
                  "CREATE"
                 ]
            },
            {
                "id": "9136fd2a9fcd405ea4674276ce36dae8in02",
                "name": "dds-32f4",
                "status": "normal",
                "port": "8635",
                "mode": "Sharding",
                "region": "aaa",
                "datastore": {
                    "type": "DDS-Community",
                    "version": "3.2"
                },
                "engine": "wiredTiger",
                "created": "2019-01-17T07:04:37",
                "updated": "2019-01-17T07:04:31",
                "db_user_name": "rwuser",
                "ssl": "1",
                "vpc_id": "674e9b42-cd8d-4d25-a2e6-5abcc565b961",
                "subnet_id": "f1df08c5-71d1-406a-aff0-de435a51007b",
                "security_group_id": "7aa51dbf-5b63-40db-9724-dad3c4828b58",
                "backup_strategy": {
                    "start_time": "19:00-20:00",
                    "keep_days": 7
                },
                "pay_mode": "0",
                "maintenance_window": "02:00-06:00",
                "groups": [
                    {
                        "type": "mongos",
                        "nodes": [
                            {
                                "id": "a742c13a284949adad177672e8a0f01cno02",
                                "name": "dds-32f4_mongos_node_1",
                                "status": "normal",
                                "role": "master",
                                "private_ip": "192.168.0.56",
                                "public_ip": "",
                                "spec_code": "dds.mongodb.s2.medium.4.mongos",
                                "availability_zone": "bbb"
                            },
                            {
                                "id": "d4f66666b1d64ab28719da0526341c7eno02",
                                "name": "dds-32f4_mongos_node_2",
                                "status": "normal",
                                "role": "master",
                                "private_ip": "192.168.0.185",
                                "public_ip": "",
                                "spec_code": "dds.mongodb.s2.medium.4.mongos",
                                "availability_zone": "bbb"
                            }
                        ]
                    },
                    {
                        "type": "shard",
                        "id": "d1b92d2cbd544e85ac7ce6a7f33ba205gr02",
                        "name": "shard_2",
                        "status": "normal",
                        "volume": {
                            "size": "10",
                            "used": "0.33"
                        },
                        "nodes": [
                            {
                                "id": "0e9abaebe5974b63a5b221de6ee34cfeno02",
                                "name": "dds-32f4_shard_2_node_3",
                                "status": "normal",
                                "role": "Primary",
                                "spec_code": "dds.mongodb.s2.medium.4.shard",
                                "availability_zone": "bbb"
                            },
                            {
                                "id": "1d7f4c5476c04cc187f920925c2b601fno02",
                                "name": "dds-32f4_shard_2_node_2",
                                "status": "normal",
                                "role": "Hidden",
                                "spec_code": "dds.mongodb.s2.medium.4.shard",
                                "availability_zone": "bbb"
                            },
                            {
                                "id": "3dd2cce03da54fc08f10651cbfea778dno02",
                                "name": "dds-32f4_shard_2_node_1",
                                "status": "normal",
                                "role": "Secondary",
                                "spec_code": "dds.mongodb.s2.medium.4.shard",
                                "availability_zone": "bbb"
                            }
                        ]
                    },
                    {
                        "type": "shard",
                        "id": "06439baa35c146d3a8965af59d370908gr02",
                        "name": "shard_1",
                        "status": "normal",
                        "volume": {
                            "size": "10",
                            "used": "0.33"
                        },
                        "nodes": [
                            {
                                "id": "0f6744d7e29f42ff80fc1a36cc145042no02",
                                "name": "dds-32f4_shard_1_node_1",
                                "status": "normal",
                                "role": "Primary",
                                "spec_code": "dds.mongodb.s2.medium.4.shard",
                                "availability_zone": "bbb"
                            },
                            {
                                "id": "3abcb399113b4512bd5a906da54e8753no02",
                                "name": "dds-32f4_shard_1_node_3",
                                "status": "normal",
                                "role": "Hidden",
                                "spec_code": "dds.mongodb.s2.medium.4.shard",
                                "availability_zone": "bbb"
                            },
                            {
                                "id": "c149f70563494501b5706cad225a8ebdno02",
                                "name": "dds-32f4_shard_1_node_2",
                                "status": "normal",
                                "role": "Secondary",
                                "spec_code": "dds.mongodb.s2.medium.4.shard",
                                "availability_zone": "bbb"
                            }
                        ]
                    },
                    {
                        "type": "config",
                        "id": "84e7c96b82aa4fedb3b00f98edd71ba4gr02",
                        "name": "config",
                        "status": "normal",
                        "volume": {
                            "size": "20",
                            "used": "0.33"
                        },
                        "nodes": [
                            {
                                "id": "7422f7331b714ac39aa647a1ec968d33no02",
                                "name": "dds-32f4_config_node_2",
                                "status": "normal",
                                "role": "Primary",
                                "spec_code": "dds.mongodb.s2.large.2.config",
                                "availability_zone": "bbb"
                            },
                            {
                                "id": "9e3b343151044eda91ddb8a42ae5cbefno02",
                                "name": "dds-32f4_config_node_3",
                                "status": "normal",
                                "role": "Hidden",
                                "spec_code": "dds.mongodb.s2.large.2.config",
                                "availability_zone": "bbb"
                            },
                            {
                                "id": "c0053ca460ac4889841ffb14a886ec54no02",
                                "name": "dds-32f4_config_node_1",
                                "status": "normal",
                                "role": "Secondary",
                                "spec_code": "dds.mongodb.s2.large.2.config",
                                "availability_zone": "bbb"
                            }
                        ]
                    }
                ],
                "time_zone": "",
                "actions": [
                  "CREATE"
                 ]
            }
        ],
        "total_count": 2
    }
    ```


## **Status Code**<a name="section5382712154838"></a>

For more information, see  [Status Code](status-code.md).

## Error Code<a name="section6522193710339"></a>

For more information, see  [Error Code](error-code.md).

