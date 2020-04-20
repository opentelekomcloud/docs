# Obtaining a DB Instance List<a name="en-us_topic_0032348280"></a>

## Function<a name="section6603527917262"></a>

This API is used to obtain a DB instance list.

## URI<a name="section2266321117262"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/instances

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table6510197817262"></a>
    <table><thead align="left"><tr id="row1990636917262"><th class="cellrowborder" valign="top" width="21.27%" id="mcps1.2.4.1.1"><p id="p180318617262"><a name="p180318617262"></a><a name="p180318617262"></a><strong id="b842352706102328"><a name="b842352706102328"></a><a name="b842352706102328"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.93%" id="mcps1.2.4.1.2"><p id="p1184034317262"><a name="p1184034317262"></a><a name="p1184034317262"></a><strong id="b842352706102346"><a name="b842352706102346"></a><a name="b842352706102346"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.8%" id="mcps1.2.4.1.3"><p id="p1954370417262"><a name="p1954370417262"></a><a name="p1954370417262"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3953622317262"><td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.2.4.1.1 "><p id="p4831745717262"><a name="p4831745717262"></a><a name="p4831745717262"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.93%" headers="mcps1.2.4.1.2 "><p id="p2139996017262"><a name="p2139996017262"></a><a name="p2139996017262"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.8%" headers="mcps1.2.4.1.3 "><p id="p56722555163647"><a name="p56722555163647"></a><a name="p56722555163647"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section807511017262"></a>

None

## Normal Response<a name="section4828447917262"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table54571314103317"></a>
    <table><thead align="left"><tr id="row3459121463318"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p91816414334"><a name="p91816414334"></a><a name="p91816414334"></a><strong id="b530410137"><a name="b530410137"></a><a name="b530410137"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p123216414335"><a name="p123216414335"></a><a name="p123216414335"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p440144113310"><a name="p440144113310"></a><a name="p440144113310"></a><strong id="b1787690539"><a name="b1787690539"></a><a name="b1787690539"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16459161403314"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p12459414153315"><a name="p12459414153315"></a><a name="p12459414153315"></a>instances</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p945941483315"><a name="p945941483315"></a><a name="p945941483315"></a>List data structure. For details, see <a href="#table4062895917262">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10459614163315"><a name="p10459614163315"></a><a name="p10459614163315"></a>Indicates the DB instance information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  instances field data structure description

    <a name="table4062895917262"></a>
    <table><thead align="left"><tr id="row2045312717262"><th class="cellrowborder" valign="top" width="22.11%" id="mcps1.2.4.1.1"><p id="p4609059717262"><a name="p4609059717262"></a><a name="p4609059717262"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.76%" id="mcps1.2.4.1.2"><p id="p4235091617262"><a name="p4235091617262"></a><a name="p4235091617262"></a><strong id="b229398771"><a name="b229398771"></a><a name="b229398771"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.129999999999995%" id="mcps1.2.4.1.3"><p id="p787220417262"><a name="p787220417262"></a><a name="p787220417262"></a><strong id="b1692183722"><a name="b1692183722"></a><a name="b1692183722"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3366877217262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p4281598817262"><a name="p4281598817262"></a><a name="p4281598817262"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p4554301317262"><a name="p4554301317262"></a><a name="p4554301317262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Indicates the primary node ID of the DB instance.</p>
    <div class="note" id="note18250133224019"><a name="note18250133224019"></a><a name="note18250133224019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p142501332164011"><a name="p142501332164011"></a><a name="p142501332164011"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row4973938517262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p235838917262"><a name="p235838917262"></a><a name="p235838917262"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p5681181717262"><a name="p5681181717262"></a><a name="p5681181717262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p2682840893927"><a name="p2682840893927"></a><a name="p2682840893927"></a>Indicates the DB instance status.</p>
    <div class="p" id="p3835449417262"><a name="p3835449417262"></a><a name="p3835449417262"></a>Value:<a name="ul3066104695748"></a><a name="ul3066104695748"></a><ul id="ul3066104695748"><li>If the value is <strong id="b84235270616547"><a name="b84235270616547"></a><a name="b84235270616547"></a>BUILD</strong>, the instance is being created.</li><li>If the value is <strong id="b842352706165415"><a name="b842352706165415"></a><a name="b842352706165415"></a>ACTIVE</strong>, the instance is normal.</li><li>If the value is <strong id="b842352706165427"><a name="b842352706165427"></a><a name="b842352706165427"></a>FAILED</strong>, the instance is abnormal.</li><li>If the value is <strong id="b1064442472"><a name="b1064442472"></a><a name="b1064442472"></a>MODIFYING</strong>, the instance is being scaled up.</li><li>If the value is <strong id="b1932177384"><a name="b1932177384"></a><a name="b1932177384"></a>REBOOTING</strong>, the instance is being rebooted.</li><li>If the value is <strong id="b1202485224"><a name="b1202485224"></a><a name="b1202485224"></a>RESTORING</strong>, the instance is being restored.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row964613217262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p4313926117262"><a name="p4313926117262"></a><a name="p4313926117262"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p461925817262"><a name="p461925817262"></a><a name="p461925817262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p3861563617262"><a name="p3861563617262"></a><a name="p3861563617262"></a>Indicates the created DB instance name.</p>
    </td>
    </tr>
    <tr id="row1199640717262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p3218490217262"><a name="p3218490217262"></a><a name="p3218490217262"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p5684029417262"><a name="p5684029417262"></a><a name="p5684029417262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p64320678"><a name="p64320678"></a><a name="p64320678"></a>Indicates the creation time in the "yyyy-mm-ddThh:mm:ssZ" format.</p>
    <p id="p6642150175824"><a name="p6642150175824"></a><a name="p6642150175824"></a><strong id="b842352706151812"><a name="b842352706151812"></a><a name="b842352706151812"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b842352706153833"><a name="b842352706153833"></a><a name="b842352706153833"></a>Z</strong> indicates the time zone offset.</p>
    <div class="note" id="note5126817175844"><a name="note5126817175844"></a><a name="note5126817175844"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p46141354175844"><a name="p46141354175844"></a><a name="p46141354175844"></a>The value is empty when the DB instance is being created. After the DB instance is created, the value is not empty.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row521631217262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p1986808917262"><a name="p1986808917262"></a><a name="p1986808917262"></a>hostname</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p6581137117262"><a name="p6581137117262"></a><a name="p6581137117262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p2912082117262"><a name="p2912082117262"></a><a name="p2912082117262"></a>Indicates the DB instance connection address. It is a blank string until an ECS is created.</p>
    </td>
    </tr>
    <tr id="row6076080317262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p2267802117262"><a name="p2267802117262"></a><a name="p2267802117262"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p2498043617262"><a name="p2498043617262"></a><a name="p2498043617262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p1014943117262"><a name="p1014943117262"></a><a name="p1014943117262"></a>Indicates the DB instance type, which can be <strong id="b84235270617352"><a name="b84235270617352"></a><a name="b84235270617352"></a>master</strong>, <strong id="b99726394894912"><a name="b99726394894912"></a><a name="b99726394894912"></a>slave</strong>, or <strong id="b84235270617355"><a name="b84235270617355"></a><a name="b84235270617355"></a>readreplica</strong>.</p>
    </td>
    </tr>
    <tr id="row6085477618055"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p1502529718057"><a name="p1502529718057"></a><a name="p1502529718057"></a>region</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p908955818057"><a name="p908955818057"></a><a name="p908955818057"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p6516558318057"><a name="p6516558318057"></a><a name="p6516558318057"></a>Indicates the region where the DB instance is deployed.</p>
    </td>
    </tr>
    <tr id="row2423602017262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p1696059317262"><a name="p1696059317262"></a><a name="p1696059317262"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p3163077417262"><a name="p3163077417262"></a><a name="p3163077417262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p53428882"><a name="p53428882"></a><a name="p53428882"></a>Indicates the updated time, which is the same as <strong id="b842352706164129"><a name="b842352706164129"></a><a name="b842352706164129"></a>created</strong> in the format.</p>
    <div class="note" id="note542057061864"><a name="note542057061864"></a><a name="note542057061864"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p180893121864"><a name="p180893121864"></a><a name="p180893121864"></a>The value is empty when the DB instance is being created. After the DB instance is created, the value is not empty.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row4049438517262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p5881973017262"><a name="p5881973017262"></a><a name="p5881973017262"></a>availabilityZone</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p6677772117262"><a name="p6677772117262"></a><a name="p6677772117262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p4028628317262"><a name="p4028628317262"></a><a name="p4028628317262"></a>Indicates the AZ ID.</p>
    </td>
    </tr>
    <tr id="row2703223317262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p714310104515"><a name="p714310104515"></a><a name="p714310104515"></a>vpc</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p38963172104515"><a name="p38963172104515"></a><a name="p38963172104515"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p65300105104515"><a name="p65300105104515"></a><a name="p65300105104515"></a>Indicates the VPC ID.</p>
    </td>
    </tr>
    <tr id="row32278200104511"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p41014036104516"><a name="p41014036104516"></a><a name="p41014036104516"></a>nics</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p33802645104516"><a name="p33802645104516"></a><a name="p33802645104516"></a>Dictionary data structure. For details, see <a href="#table37920950175250">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p53659763104516"><a name="p53659763104516"></a><a name="p53659763104516"></a>Indicates the nics information.</p>
    </td>
    </tr>
    <tr id="row4722801917262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p26431617262"><a name="p26431617262"></a><a name="p26431617262"></a>securityGroup</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p2140963417262"><a name="p2140963417262"></a><a name="p2140963417262"></a>Dictionary data structure. For details, see <a href="#table3309421917534">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p5645876417262"><a name="p5645876417262"></a><a name="p5645876417262"></a>Indicates the security group information.</p>
    </td>
    </tr>
    <tr id="row3836683017262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p2070553017262"><a name="p2070553017262"></a><a name="p2070553017262"></a>flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p6653523017262"><a name="p6653523017262"></a><a name="p6653523017262"></a>Dictionary data structure. For details, see <a href="#table6373831917584">Table 6</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p2064457917262"><a name="p2064457917262"></a><a name="p2064457917262"></a>Indicates the specification information.</p>
    </td>
    </tr>
    <tr id="row5158348917262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p1751311417262"><a name="p1751311417262"></a><a name="p1751311417262"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p927613517262"><a name="p927613517262"></a><a name="p927613517262"></a>Dictionary data structure. For details, see <a href="#table35005463173456">Table 7</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p1316948917262"><a name="p1316948917262"></a><a name="p1316948917262"></a>Indicates the volume information.</p>
    </td>
    </tr>
    <tr id="row26042558155946"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p29072469155946"><a name="p29072469155946"></a><a name="p29072469155946"></a>dataStoreInfo</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p6059817155946"><a name="p6059817155946"></a><a name="p6059817155946"></a>Dictionary data structure. For details, see <a href="#table16797672173620">Table 8</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p21083169155946"><a name="p21083169155946"></a><a name="p21083169155946"></a>Indicates the database information.</p>
    </td>
    </tr>
    <tr id="row3104228817747"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p156965461780"><a name="p156965461780"></a><a name="p156965461780"></a>dbPort</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p634606801780"><a name="p634606801780"></a><a name="p634606801780"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p400414551780"><a name="p400414551780"></a><a name="p400414551780"></a>Indicates the database port number.</p>
    </td>
    </tr>
    <tr id="row6543147717262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p6545824517262"><a name="p6545824517262"></a><a name="p6545824517262"></a>backupStrategy</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p51760117262"><a name="p51760117262"></a><a name="p51760117262"></a>Dictionary data structure. For details, see <a href="#table50876711173859">Table 9</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p4192574617262"><a name="p4192574617262"></a><a name="p4192574617262"></a>Indicates the advanced backup policy.</p>
    </td>
    </tr>
    <tr id="row4178740217262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p18816388111317"><a name="p18816388111317"></a><a name="p18816388111317"></a>slaveId</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p47732488111317"><a name="p47732488111317"></a><a name="p47732488111317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p41126320111317"><a name="p41126320111317"></a><a name="p41126320111317"></a>Returned only when you create primary/standby DB instances.</p>
    </td>
    </tr>
    <tr id="row2350798811137"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p27149812111313"><a name="p27149812111313"></a><a name="p27149812111313"></a>ha</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p51651186111313"><a name="p51651186111313"></a><a name="p51651186111313"></a>Dictionary data structure. For details, see <a href="#table497888411810">Table 10</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p391079579319"><a name="p391079579319"></a><a name="p391079579319"></a>Indicates the primary/standby DB instance information. Returned only when you obtain a primary/standby DB instance list.</p>
    </td>
    </tr>
    <tr id="row525514017262"><td class="cellrowborder" valign="top" width="22.11%" headers="mcps1.2.4.1.1 "><p id="p2301320417262"><a name="p2301320417262"></a><a name="p2301320417262"></a>replicaOf</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.76%" headers="mcps1.2.4.1.2 "><p id="p5213021617262"><a name="p5213021617262"></a><a name="p5213021617262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.129999999999995%" headers="mcps1.2.4.1.3 "><p id="p6179796117262"><a name="p6179796117262"></a><a name="p6179796117262"></a>Returned only when you obtain the read replica information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  nics field data structure description

    <a name="table37920950175250"></a>
    <table><thead align="left"><tr id="row23321270175250"><th class="cellrowborder" valign="top" width="21.95%" id="mcps1.2.4.1.1"><p id="p9974708175250"><a name="p9974708175250"></a><a name="p9974708175250"></a><strong id="b64780299"><a name="b64780299"></a><a name="b64780299"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.96%" id="mcps1.2.4.1.2"><p id="p2645023175250"><a name="p2645023175250"></a><a name="p2645023175250"></a><strong id="b2016037747"><a name="b2016037747"></a><a name="b2016037747"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.09%" id="mcps1.2.4.1.3"><p id="p12920286175250"><a name="p12920286175250"></a><a name="p12920286175250"></a><strong id="b1912224743"><a name="b1912224743"></a><a name="b1912224743"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39910234175250"><td class="cellrowborder" valign="top" width="21.95%" headers="mcps1.2.4.1.1 "><p id="p11503482175250"><a name="p11503482175250"></a><a name="p11503482175250"></a>subnetId</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.96%" headers="mcps1.2.4.1.2 "><p id="p59366822175250"><a name="p59366822175250"></a><a name="p59366822175250"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.09%" headers="mcps1.2.4.1.3 "><p id="p43983303175250"><a name="p43983303175250"></a><a name="p43983303175250"></a>Indicates the network ID of the subnet.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  securityGroup field data structure description

    <a name="table3309421917534"></a>
    <table><thead align="left"><tr id="row238163517534"><th class="cellrowborder" valign="top" width="22.23222322232223%" id="mcps1.2.4.1.1"><p id="p5869477217534"><a name="p5869477217534"></a><a name="p5869477217534"></a><strong id="b743078136"><a name="b743078136"></a><a name="b743078136"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.962796279627966%" id="mcps1.2.4.1.2"><p id="p5665613017534"><a name="p5665613017534"></a><a name="p5665613017534"></a><strong id="b1378226222"><a name="b1378226222"></a><a name="b1378226222"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.80498049804981%" id="mcps1.2.4.1.3"><p id="p2574382817534"><a name="p2574382817534"></a><a name="p2574382817534"></a><strong id="b1192193370"><a name="b1192193370"></a><a name="b1192193370"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row487534717534"><td class="cellrowborder" valign="top" width="22.23222322232223%" headers="mcps1.2.4.1.1 "><p id="p5935882217534"><a name="p5935882217534"></a><a name="p5935882217534"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.962796279627966%" headers="mcps1.2.4.1.2 "><p id="p4333528617534"><a name="p4333528617534"></a><a name="p4333528617534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.80498049804981%" headers="mcps1.2.4.1.3 "><p id="p2049725817534"><a name="p2049725817534"></a><a name="p2049725817534"></a>Indicates the security group ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  flavor field data structure description

    <a name="table6373831917584"></a>
    <table><thead align="left"><tr id="row2420947817584"><th class="cellrowborder" valign="top" width="22.38%" id="mcps1.2.4.1.1"><p id="p1481073317584"><a name="p1481073317584"></a><a name="p1481073317584"></a><strong id="b1502281678"><a name="b1502281678"></a><a name="b1502281678"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.68%" id="mcps1.2.4.1.2"><p id="p5881868717584"><a name="p5881868717584"></a><a name="p5881868717584"></a><strong id="b264259810"><a name="b264259810"></a><a name="b264259810"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.94%" id="mcps1.2.4.1.3"><p id="p6669322217584"><a name="p6669322217584"></a><a name="p6669322217584"></a><strong id="b1533742120"><a name="b1533742120"></a><a name="b1533742120"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3344193017584"><td class="cellrowborder" valign="top" width="22.38%" headers="mcps1.2.4.1.1 "><p id="p2444181017584"><a name="p2444181017584"></a><a name="p2444181017584"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.68%" headers="mcps1.2.4.1.2 "><p id="p3362960717584"><a name="p3362960717584"></a><a name="p3362960717584"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.94%" headers="mcps1.2.4.1.3 "><p id="p3964363217584"><a name="p3964363217584"></a><a name="p3964363217584"></a>Indicates the specification ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7**  volume field data structure description

    <a name="table35005463173456"></a>
    <table><thead align="left"><tr id="row9318556173456"><th class="cellrowborder" valign="top" width="22.24%" id="mcps1.2.4.1.1"><p id="p15232744173456"><a name="p15232744173456"></a><a name="p15232744173456"></a><strong id="b823678472"><a name="b823678472"></a><a name="b823678472"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.82%" id="mcps1.2.4.1.2"><p id="p25892781173456"><a name="p25892781173456"></a><a name="p25892781173456"></a><strong id="b594127791"><a name="b594127791"></a><a name="b594127791"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.94%" id="mcps1.2.4.1.3"><p id="p16940539173456"><a name="p16940539173456"></a><a name="p16940539173456"></a><strong id="b1394703569"><a name="b1394703569"></a><a name="b1394703569"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18247124173456"><td class="cellrowborder" valign="top" width="22.24%" headers="mcps1.2.4.1.1 "><p id="p1622081173456"><a name="p1622081173456"></a><a name="p1622081173456"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.4.1.2 "><p id="p64279755173456"><a name="p64279755173456"></a><a name="p64279755173456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.94%" headers="mcps1.2.4.1.3 "><p id="p39277657173456"><a name="p39277657173456"></a><a name="p39277657173456"></a>Indicates the volume type.</p>
    </td>
    </tr>
    <tr id="row17954597173456"><td class="cellrowborder" valign="top" width="22.24%" headers="mcps1.2.4.1.1 "><p id="p45036277173456"><a name="p45036277173456"></a><a name="p45036277173456"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.4.1.2 "><p id="p24059838173456"><a name="p24059838173456"></a><a name="p24059838173456"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.94%" headers="mcps1.2.4.1.3 "><p id="p2689831173456"><a name="p2689831173456"></a><a name="p2689831173456"></a>Indicates the volume size.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8**  dataStoreInfo field data structure description

    <a name="table16797672173620"></a>
    <table><thead align="left"><tr id="row16288138173620"><th class="cellrowborder" valign="top" width="22.37%" id="mcps1.2.4.1.1"><p id="p62892653173620"><a name="p62892653173620"></a><a name="p62892653173620"></a><strong id="b360903052"><a name="b360903052"></a><a name="b360903052"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.310000000000002%" id="mcps1.2.4.1.2"><p id="p61140119173620"><a name="p61140119173620"></a><a name="p61140119173620"></a><strong id="b1770949673"><a name="b1770949673"></a><a name="b1770949673"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.32%" id="mcps1.2.4.1.3"><p id="p53402626173620"><a name="p53402626173620"></a><a name="p53402626173620"></a><strong id="b293424311"><a name="b293424311"></a><a name="b293424311"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10861591173620"><td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.2.4.1.1 "><p id="p7373702173620"><a name="p7373702173620"></a><a name="p7373702173620"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.310000000000002%" headers="mcps1.2.4.1.2 "><p id="p60398985173620"><a name="p60398985173620"></a><a name="p60398985173620"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.32%" headers="mcps1.2.4.1.3 "><p id="p60479625173620"><a name="p60479625173620"></a><a name="p60479625173620"></a>Indicates the DB engine.</p>
    </td>
    </tr>
    <tr id="row7445715173620"><td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.2.4.1.1 "><p id="p66232024173620"><a name="p66232024173620"></a><a name="p66232024173620"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.310000000000002%" headers="mcps1.2.4.1.2 "><p id="p63193742173620"><a name="p63193742173620"></a><a name="p63193742173620"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.32%" headers="mcps1.2.4.1.3 "><p id="p18419484173620"><a name="p18419484173620"></a><a name="p18419484173620"></a>Indicates the database version.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  9**  backupStrategy field data structure description

    <a name="table50876711173859"></a>
    <table><thead align="left"><tr id="row26941115173859"><th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.1"><p id="p44284799173859"><a name="p44284799173859"></a><a name="p44284799173859"></a><strong id="b2026700682"><a name="b2026700682"></a><a name="b2026700682"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.589999999999996%" id="mcps1.2.4.1.2"><p id="p30298928173859"><a name="p30298928173859"></a><a name="p30298928173859"></a><strong id="b999848861"><a name="b999848861"></a><a name="b999848861"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.19%" id="mcps1.2.4.1.3"><p id="p38294098173859"><a name="p38294098173859"></a><a name="p38294098173859"></a><strong id="b2126548616"><a name="b2126548616"></a><a name="b2126548616"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9102564173859"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p66219122173859"><a name="p66219122173859"></a><a name="p66219122173859"></a>startTime</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.4.1.2 "><p id="p62148676173859"><a name="p62148676173859"></a><a name="p62148676173859"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.19%" headers="mcps1.2.4.1.3 "><p id="p55315500174811"><a name="p55315500174811"></a><a name="p55315500174811"></a>Indicates the backup start time that has been set. The backup task will be triggered within one hour after the backup start time.</p>
    <p id="p1583127716151"><a name="p1583127716151"></a><a name="p1583127716151"></a>The time is in the UTC format.</p>
    </td>
    </tr>
    <tr id="row7902174173859"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p36096395173859"><a name="p36096395173859"></a><a name="p36096395173859"></a>keepDays</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.4.1.2 "><p id="p38126872173859"><a name="p38126872173859"></a><a name="p38126872173859"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.19%" headers="mcps1.2.4.1.3 "><p id="p59681602174811"><a name="p59681602174811"></a><a name="p59681602174811"></a>Indicates the number of days to retain the generated backup files.</p>
    <p id="p263511174811"><a name="p263511174811"></a><a name="p263511174811"></a>The value range is from 0 to 732. If this parameter is <strong id="b842352706112422"><a name="b842352706112422"></a><a name="b842352706112422"></a>0</strong>, the automated backup policy is not set. To extend the retention period, contact customer service. Automated backups can be retained for up to 2562 days.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  10**  ha field data structure description

    <a name="table497888411810"></a>
    <table><thead align="left"><tr id="row145013461810"><th class="cellrowborder" valign="top" width="22.52%" id="mcps1.2.4.1.1"><p id="p337583601810"><a name="p337583601810"></a><a name="p337583601810"></a><strong id="b1431977547"><a name="b1431977547"></a><a name="b1431977547"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.400000000000002%" id="mcps1.2.4.1.2"><p id="p500726761810"><a name="p500726761810"></a><a name="p500726761810"></a><strong id="b977653462"><a name="b977653462"></a><a name="b977653462"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.080000000000005%" id="mcps1.2.4.1.3"><p id="p293549231810"><a name="p293549231810"></a><a name="p293549231810"></a><strong id="b1793121218"><a name="b1793121218"></a><a name="b1793121218"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row289385831810"><td class="cellrowborder" valign="top" width="22.52%" headers="mcps1.2.4.1.1 "><p id="p623239201810"><a name="p623239201810"></a><a name="p623239201810"></a>replicationMode</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.400000000000002%" headers="mcps1.2.4.1.2 "><p id="p150727651810"><a name="p150727651810"></a><a name="p150727651810"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.4.1.3 "><p id="p129344711810"><a name="p129344711810"></a><a name="p129344711810"></a>Indicates the replication mode for the standby DB instance.</p>
    <p id="p3394570181655"><a name="p3394570181655"></a><a name="p3394570181655"></a>The value cannot be empty.</p>
    <a name="ul30551132181655"></a><a name="ul30551132181655"></a><ul id="ul30551132181655"><li>For MySQL, the value is <strong id="b842352706165650"><a name="b842352706165650"></a><a name="b842352706165650"></a>async</strong> or <strong id="b842352706165654"><a name="b842352706165654"></a><a name="b842352706165654"></a>semisync</strong>.</li><li>For PostgreSQL, the value is <strong id="b424906094"><a name="b424906094"></a><a name="b424906094"></a>async</strong> or <strong id="b389714787"><a name="b389714787"></a><a name="b389714787"></a>sync</strong>.</li><li>For Microsoft SQL Server, the value is <strong id="b1084866521183314"><a name="b1084866521183314"></a><a name="b1084866521183314"></a>sync</strong>.</li></ul>
    <div class="note" id="note58913671181655"><a name="note58913671181655"></a><a name="note58913671181655"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul60460995181655"></a><a name="ul60460995181655"></a><ul id="ul60460995181655"><li><strong id="b842352706105954"><a name="b842352706105954"></a><a name="b842352706105954"></a>async</strong> indicates the asynchronous replication mode.</li><li><strong id="b842352706164020"><a name="b842352706164020"></a><a name="b842352706164020"></a>semisync</strong> indicates the semi-synchronous replication mode.</li><li><strong id="b13384211081105"><a name="b13384211081105"></a><a name="b13384211081105"></a>sync</strong> indicates the synchronous replication mode.</li></ul>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    Single DB instance:

    ```
    {
        "instances": [
          {
            "id": "252f11f1-2912-4c06-be55-1999bde659c5",
            "status": "BUILD",
            "name": "trove-instance-rep3",
            "created": "2016-06-18T21:21:50+0200",
            "hostname": "192.168.0.132",
            "type": "master",
            "region": "eu-de",
            "updated": "2016-06-18T21:21:50+0200",
            "availabilityZone": "eu-de-01",
            "vpc": "490a4a08-ef4b-44c5-94be-3051ef9e4fce",
            "nics": {
              "subnetId": "0e2eda62-1d42-4d64-a9d1-4e9aa9cd994f"
            },
            "securityGroup": {
                "id": "2a1f7fc8-3307-42a7-aa6f-42c8b9b8f8c5"
            },
            "flavor": {
                "id": "bf07a6d4-844a-4023-a776-fc5c5fb71fb4"
            },
            "volume": {
                "type": "ULTRAHIGH",
                "size": 100
            },
            "dataStoreInfo": {
                "type": "MySQL",
                "version": "5.7"
            },
            "dbPort": 3306,
            "backupStrategy": {
                "startTime": "01:00:00",
                "keepDays": 3
            }
        }
     ]
    }
    ```

    Primary/standby DB instances:

    ```
    {
        "instances": [
          {
            "id": "252f11f1-2912-4c06-be55-1999bde659c5",
            "status": "BUILD",
            "name": "trove-instance-rep3",
            "created": "2016-06-18T21:21:50+0200",
            "hostname": "192.168.0.132",
            "type": "master",
            "region": "eu-de",
            "updated": "2016-06-18T21:21:50+0200",
            "availabilityZone": "eu-de-01",
            "vpc": "490a4a08-ef4b-44c5-94be-3051ef9e4fce",
            "nics": {
              "subnetId": "0e2eda62-1d42-4d64-a9d1-4e9aa9cd994f"
            },
            "securityGroup": {
                "id": "2a1f7fc8-3307-42a7-aa6f-42c8b9b8f8c5"
            },
            "flavor": {
                "id": "bf07a6d4-844a-4023-a776-fc5c5fb71fb4"
            },
            "volume": {
                "type": "ULTRAHIGH",
                "size": 100
            },
            "dataStoreInfo": {
                "type": "MySQL",
                "version": "5.7"
            },
            "dbPort": 3306,
            "backupStrategy": {
                "startTime": "01:00:00",
                "keepDays": 3
            },
            "slaveId": "9405d8b8-a87d-4531-bd3a-e504c8434281",
            "ha": {
                "replicationMode": "async"
            }
        }
      ]
    }
    ```

    Read replica:

    ```
    {
        "instances": [
          {
            "id": "252f11f1-2912-4c06-be55-1999bde659c5",
            "status": "BUILD",
            "name": "trove-instance-rep3",
            "created": "2016-06-18T21:21:50+0200",
            "hostname": "192.168.0.132",
            "type": "readreplica",
            "region": "eu-de",
            "updated": "2016-06-18T21:21:50+0200",
            "availabilityZone": "eu-de-01",
            "vpc": "490a4a08-ef4b-44c5-94be-3051ef9e4fce",
            "nics": {
              "subnetId": "0e2eda62-1d42-4d64-a9d1-4e9aa9cd994f"
            },
            "securityGroup": {
                "id": "2a1f7fc8-3307-42a7-aa6f-42c8b9b8f8c5"
            },
            "flavor": {
                "id": "bf07a6d4-844a-4023-a776-fc5c5fb71fb4"
            },
            "volume": {
                "type": "ULTRAHIGH",
                "size": 100
            },
            "dataStoreInfo": {
                "type": "MySQL",
                "version": "5.7"
            },
            "dbPort": 3306,
            "replicaOf": "252f11f1-2912-4c06-be55-1999bde659c5"
        }
      ]
    }
    ```


## Abnormal Response<a name="section55968780172618"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

