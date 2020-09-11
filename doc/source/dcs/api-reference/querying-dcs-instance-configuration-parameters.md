# Querying DCS Instance Configuration Parameters<a name="dcs-api-0312015"></a>

## Function<a name="section166920407553"></a>

This API is used to query the configuration parameters of a DCS instance.

## URI<a name="section149423025817"></a>

GET /v1.0/\{project\_id\}/instances/\{instance\_id\}/configs

[Table 1](#table133085233516)  describes the parameters.

**Table  1**  Parameter description

<a name="table133085233516"></a>
<table><thead align="left"><tr id="row11301852163514"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p18301052133516"><a name="p18301052133516"></a><a name="p18301052133516"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p113095220352"><a name="p113095220352"></a><a name="p113095220352"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p18301352173511"><a name="p18301352173511"></a><a name="p18301352173511"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p1230185218351"><a name="p1230185218351"></a><a name="p1230185218351"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1030252113519"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p83095213515"><a name="p83095213515"></a><a name="p83095213515"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p430125213358"><a name="p430125213358"></a><a name="p430125213358"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1330195212357"><a name="p1330195212357"></a><a name="p1330195212357"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1830952123516"><a name="p1830952123516"></a><a name="p1830952123516"></a>Project ID</p>
</td>
</tr>
<tr id="row103012521355"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p8301652183514"><a name="p8301652183514"></a><a name="p8301652183514"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p143016523351"><a name="p143016523351"></a><a name="p143016523351"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p11304527356"><a name="p11304527356"></a><a name="p11304527356"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p930152153516"><a name="p930152153516"></a><a name="p930152153516"></a>ID of the instance to be queried</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section19842205591"></a>

**Request parameters**

None.

**Example request**

```
GET https://{dcs_endpoint}/v1.0/{project_id}/instances/{instance_id}/configs
```

## Response<a name="section171184818599"></a>

**Response parameters**

[Table 2](#table1831432163611)  describes the response parameters.

**Table  2**  Parameter description

<a name="table1831432163611"></a>
<table><thead align="left"><tr id="row14314192143612"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="p19313172113614"><a name="p19313172113614"></a><a name="p19313172113614"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.4.1.2"><p id="p2313202143617"><a name="p2313202143617"></a><a name="p2313202143617"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.565656565656575%" id="mcps1.2.4.1.3"><p id="p83133215366"><a name="p83133215366"></a><a name="p83133215366"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18314172163611"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p6314172173620"><a name="p6314172173620"></a><a name="p6314172173620"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p18314825362"><a name="p18314825362"></a><a name="p18314825362"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.565656565656575%" headers="mcps1.2.4.1.3 "><p id="p1231412203618"><a name="p1231412203618"></a><a name="p1231412203618"></a>Current status of a DCS instance.</p>
</td>
</tr>
<tr id="row131419211367"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p123145253611"><a name="p123145253611"></a><a name="p123145253611"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p331419218363"><a name="p331419218363"></a><a name="p331419218363"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.565656565656575%" headers="mcps1.2.4.1.3 "><p id="p531412213612"><a name="p531412213612"></a><a name="p531412213612"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row68141143112110"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p664813762218"><a name="p664813762218"></a><a name="p664813762218"></a>redis_config</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p146481937132219"><a name="p146481937132219"></a><a name="p146481937132219"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="56.565656565656575%" headers="mcps1.2.4.1.3 "><p id="p5648183715227"><a name="p5648183715227"></a><a name="p5648183715227"></a>Array of configuration items of the DCS instance. For details, see <a href="#table4967184515317">Table 3</a>.</p>
</td>
</tr>
<tr id="row1031418220363"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p4314621368"><a name="p4314621368"></a><a name="p4314621368"></a>config_status</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p031412219361"><a name="p031412219361"></a><a name="p031412219361"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.565656565656575%" headers="mcps1.2.4.1.3 "><p id="p931420214369"><a name="p931420214369"></a><a name="p931420214369"></a>DCS instance status that is being modified or has been modified. Options:</p>
<a name="ul2971182894312"></a><a name="ul2971182894312"></a><ul id="ul2971182894312"><li><strong id="b3716621114114"><a name="b3716621114114"></a><a name="b3716621114114"></a>UPDATING</strong></li><li><strong id="b515492614412"><a name="b515492614412"></a><a name="b515492614412"></a>FAILURE</strong></li><li><strong id="b8357730124110"><a name="b8357730124110"></a><a name="b8357730124110"></a>SUCCESS</strong></li></ul>
</td>
</tr>
<tr id="row13314725361"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p1231452123615"><a name="p1231452123615"></a><a name="p1231452123615"></a>config_time</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p9314327362"><a name="p9314327362"></a><a name="p9314327362"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.565656565656575%" headers="mcps1.2.4.1.3 "><p id="p19314192183611"><a name="p19314192183611"></a><a name="p19314192183611"></a>Time at which the DCS instance is operated on. For example, 2017-03-31<strong id="b1429681720163"><a name="b1429681720163"></a><a name="b1429681720163"></a>T</strong>12:24:46.297<strong id="b129681791617"><a name="b129681791617"></a><a name="b129681791617"></a>Z</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  redis\_config parameter description

<a name="table4967184515317"></a>
<table><thead align="left"><tr id="row7967134518533"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p18967104518537"><a name="p18967104518537"></a><a name="p18967104518537"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p1696714512534"><a name="p1696714512534"></a><a name="p1696714512534"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.4.1.3"><p id="p4967145115317"><a name="p4967145115317"></a><a name="p4967145115317"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3103173862316"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p870864732310"><a name="p870864732310"></a><a name="p870864732310"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p1570912475234"><a name="p1570912475234"></a><a name="p1570912475234"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p197091947112319"><a name="p197091947112319"></a><a name="p197091947112319"></a>Configuration item description.</p>
</td>
</tr>
<tr id="row1096714515536"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p9967104505312"><a name="p9967104505312"></a><a name="p9967104505312"></a>param_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p096714510532"><a name="p096714510532"></a><a name="p096714510532"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p19967245175316"><a name="p19967245175316"></a><a name="p19967245175316"></a>Configuration parameter ID. For the possible values, see the <strong id="b22801194177"><a name="b22801194177"></a><a name="b22801194177"></a>Parameter ID</strong> column in <a href="#table1439111281351">Table 4</a>.</p>
</td>
</tr>
<tr id="row996712453534"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p29671245185310"><a name="p29671245185310"></a><a name="p29671245185310"></a>param_name</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p1996744518538"><a name="p1996744518538"></a><a name="p1996744518538"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p149681457534"><a name="p149681457534"></a><a name="p149681457534"></a>Configuration parameter name. For the possible values, see the <strong id="b1632210338173"><a name="b1632210338173"></a><a name="b1632210338173"></a>Parameter Name</strong> column in <a href="#table1439111281351">Table 4</a>.</p>
</td>
</tr>
<tr id="row1896844513533"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p11968174517535"><a name="p11968174517535"></a><a name="p11968174517535"></a>param_value</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p14968164505312"><a name="p14968164505312"></a><a name="p14968164505312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p3968114517538"><a name="p3968114517538"></a><a name="p3968114517538"></a>Configuration parameter value.</p>
</td>
</tr>
<tr id="row39681745175317"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p4968194545312"><a name="p4968194545312"></a><a name="p4968194545312"></a>default_value</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p8968245125317"><a name="p8968245125317"></a><a name="p8968245125317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p8968174518539"><a name="p8968174518539"></a><a name="p8968174518539"></a>Default value of the configuration parameter. For the possible values, see the <strong id="b4102644161719"><a name="b4102644161719"></a><a name="b4102644161719"></a>Default Value</strong> column in <a href="#table1439111281351">Table 4</a>.</p>
</td>
</tr>
<tr id="row2968114565318"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p169682045105320"><a name="p169682045105320"></a><a name="p169682045105320"></a>value_type</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p69681745185319"><a name="p69681745185319"></a><a name="p69681745185319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p14968124595312"><a name="p14968124595312"></a><a name="p14968124595312"></a>Type of the configuration parameter value. For the possible values, see the <strong id="b1753057201714"><a name="b1753057201714"></a><a name="b1753057201714"></a>Value Type</strong> column in <a href="#table1439111281351">Table 4</a>.</p>
</td>
</tr>
<tr id="row199681245175314"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p696814515531"><a name="p696814515531"></a><a name="p696814515531"></a>value_range</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p4968144519534"><a name="p4968144519534"></a><a name="p4968144519534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p296811453533"><a name="p296811453533"></a><a name="p296811453533"></a>Range of the configuration parameter value. For the possible values, see the <strong id="b8102139171812"><a name="b8102139171812"></a><a name="b8102139171812"></a>Value Range</strong> column in <a href="#table1439111281351">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

[Table 4](#table1439111281351)  describes the configuration parameters of a DCS instance.

**Table  4**  Configuration parameters of a DCS instance

<a name="table1439111281351"></a>
<table><thead align="left"><tr id="row341117287513"><th class="cellrowborder" valign="top" width="10.000000000000002%" id="mcps1.2.7.1.1"><p id="p641592815516"><a name="p641592815516"></a><a name="p641592815516"></a>Parameter ID</p>
</th>
<th class="cellrowborder" valign="top" width="13.000000000000004%" id="mcps1.2.7.1.2"><p id="p142012815513"><a name="p142012815513"></a><a name="p142012815513"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="12.000000000000002%" id="mcps1.2.7.1.3"><p id="p1342932816511"><a name="p1342932816511"></a><a name="p1342932816511"></a>Value Type</p>
</th>
<th class="cellrowborder" valign="top" width="34.00000000000001%" id="mcps1.2.7.1.4"><p id="p74341628951"><a name="p74341628951"></a><a name="p74341628951"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="22.000000000000004%" id="mcps1.2.7.1.5"><p id="p1438162811513"><a name="p1438162811513"></a><a name="p1438162811513"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="9.000000000000002%" id="mcps1.2.7.1.6"><p id="p14442202817520"><a name="p14442202817520"></a><a name="p14442202817520"></a>Default Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row114457282052"><td class="cellrowborder" valign="top" width="10.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p19449142814519"><a name="p19449142814519"></a><a name="p19449142814519"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13.000000000000004%" headers="mcps1.2.7.1.2 "><p id="p1453112820520"><a name="p1453112820520"></a><a name="p1453112820520"></a>timeout</p>
</td>
<td class="cellrowborder" valign="top" width="12.000000000000002%" headers="mcps1.2.7.1.3 "><p id="p94631928151"><a name="p94631928151"></a><a name="p94631928151"></a>Interger</p>
</td>
<td class="cellrowborder" valign="top" width="34.00000000000001%" headers="mcps1.2.7.1.4 "><p id="p194671128257"><a name="p194671128257"></a><a name="p194671128257"></a>Connection between the client and server (DCS instance) will be closed if the client is idle for the timeout period (measured in seconds). A timeout period of 0 seconds indicates that the timeout function is disabled.</p>
</td>
<td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.2.7.1.5 "><p id="p1447132818515"><a name="p1447132818515"></a><a name="p1447132818515"></a>0 to 7200. Unit: second.</p>
</td>
<td class="cellrowborder" valign="top" width="9.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p847413281518"><a name="p847413281518"></a><a name="p847413281518"></a>0</p>
</td>
</tr>
<tr id="row9476172811519"><td class="cellrowborder" valign="top" width="10.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p6480132816513"><a name="p6480132816513"></a><a name="p6480132816513"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="13.000000000000004%" headers="mcps1.2.7.1.2 "><p id="p348382819517"><a name="p348382819517"></a><a name="p348382819517"></a>maxmemory-policy</p>
</td>
<td class="cellrowborder" valign="top" width="12.000000000000002%" headers="mcps1.2.7.1.3 "><p id="p104911928155"><a name="p104911928155"></a><a name="p104911928155"></a>Enum</p>
</td>
<td class="cellrowborder" valign="top" width="34.00000000000001%" headers="mcps1.2.7.1.4 "><p id="p44951028258"><a name="p44951028258"></a><a name="p44951028258"></a>How Redis will select what to remove when maxmemory is reached.</p>
<p id="p1949719289515"><a name="p1949719289515"></a><a name="p1949719289515"></a>For more information about this parameter, see <a href="https://redis.io/topics/lru-cache" target="_blank" rel="noopener noreferrer">https://redis.io/topics/lru-cache</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.2.7.1.5 "><p id="p145021281255"><a name="p145021281255"></a><a name="p145021281255"></a>volatile-lru</p>
<p id="p1850452810519"><a name="p1850452810519"></a><a name="p1850452810519"></a>allkeys-lru</p>
<p id="p150642815518"><a name="p150642815518"></a><a name="p150642815518"></a>volatile-random</p>
<p id="p5507192813518"><a name="p5507192813518"></a><a name="p5507192813518"></a>allkeys-random</p>
<p id="p125102287515"><a name="p125102287515"></a><a name="p125102287515"></a>volatile-ttl</p>
<p id="p251215281956"><a name="p251215281956"></a><a name="p251215281956"></a>noeviction</p>
</td>
<td class="cellrowborder" valign="top" width="9.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p1051512812518"><a name="p1051512812518"></a><a name="p1051512812518"></a>noeviction</p>
</td>
</tr>
<tr id="row12517122812512"><td class="cellrowborder" valign="top" width="10.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p65211728552"><a name="p65211728552"></a><a name="p65211728552"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="13.000000000000004%" headers="mcps1.2.7.1.2 "><p id="p195255282057"><a name="p195255282057"></a><a name="p195255282057"></a>hash-max-ziplist-entries</p>
</td>
<td class="cellrowborder" valign="top" width="12.000000000000002%" headers="mcps1.2.7.1.3 "><p id="p65341281150"><a name="p65341281150"></a><a name="p65341281150"></a>Interger</p>
</td>
<td class="cellrowborder" valign="top" width="34.00000000000001%" headers="mcps1.2.7.1.4 "><p id="p05388284518"><a name="p05388284518"></a><a name="p05388284518"></a>When the number of entries in hashes is less than the value of this parameter, hashes are encoded using ziplist to save memory.</p>
</td>
<td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.2.7.1.5 "><p id="p85411228155"><a name="p85411228155"></a><a name="p85411228155"></a>1 to 10000</p>
</td>
<td class="cellrowborder" valign="top" width="9.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p1554592817516"><a name="p1554592817516"></a><a name="p1554592817516"></a>512</p>
</td>
</tr>
<tr id="row054702814515"><td class="cellrowborder" valign="top" width="10.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p955182813513"><a name="p955182813513"></a><a name="p955182813513"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="13.000000000000004%" headers="mcps1.2.7.1.2 "><p id="p115550281250"><a name="p115550281250"></a><a name="p115550281250"></a>hash-max-ziplist-value</p>
</td>
<td class="cellrowborder" valign="top" width="12.000000000000002%" headers="mcps1.2.7.1.3 "><p id="p256519283514"><a name="p256519283514"></a><a name="p256519283514"></a>Interger</p>
</td>
<td class="cellrowborder" valign="top" width="34.00000000000001%" headers="mcps1.2.7.1.4 "><p id="p65692028552"><a name="p65692028552"></a><a name="p65692028552"></a>When the biggest entry in hashes does not exceed the length threshold indicated by this parameter, hashes are encoded using ziplist to save memory.</p>
</td>
<td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.2.7.1.5 "><p id="p55779281756"><a name="p55779281756"></a><a name="p55779281756"></a>1 to 10000</p>
</td>
<td class="cellrowborder" valign="top" width="9.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p4581192813515"><a name="p4581192813515"></a><a name="p4581192813515"></a>64</p>
</td>
</tr>
<tr id="row7584112813516"><td class="cellrowborder" valign="top" width="10.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p1458792815516"><a name="p1458792815516"></a><a name="p1458792815516"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="13.000000000000004%" headers="mcps1.2.7.1.2 "><p id="p859214281551"><a name="p859214281551"></a><a name="p859214281551"></a>list-max-ziplist-entries</p>
</td>
<td class="cellrowborder" valign="top" width="12.000000000000002%" headers="mcps1.2.7.1.3 "><p id="p46000281259"><a name="p46000281259"></a><a name="p46000281259"></a>Interger</p>
</td>
<td class="cellrowborder" valign="top" width="34.00000000000001%" headers="mcps1.2.7.1.4 "><p id="p1260492814520"><a name="p1260492814520"></a><a name="p1260492814520"></a>When the number of entries in lists is less than the value of this parameter, lists are encoded using ziplist to save memory.</p>
</td>
<td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.2.7.1.5 "><p id="p2607192815518"><a name="p2607192815518"></a><a name="p2607192815518"></a>1 to 10000</p>
</td>
<td class="cellrowborder" valign="top" width="9.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p861142817511"><a name="p861142817511"></a><a name="p861142817511"></a>512</p>
</td>
</tr>
<tr id="row156128281354"><td class="cellrowborder" valign="top" width="10.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p14615192814511"><a name="p14615192814511"></a><a name="p14615192814511"></a>6</p>
</td>
<td class="cellrowborder" valign="top" width="13.000000000000004%" headers="mcps1.2.7.1.2 "><p id="p86209284517"><a name="p86209284517"></a><a name="p86209284517"></a>list-max-ziplist-value</p>
</td>
<td class="cellrowborder" valign="top" width="12.000000000000002%" headers="mcps1.2.7.1.3 "><p id="p1362916280513"><a name="p1362916280513"></a><a name="p1362916280513"></a>Interger</p>
</td>
<td class="cellrowborder" valign="top" width="34.00000000000001%" headers="mcps1.2.7.1.4 "><p id="p46325281851"><a name="p46325281851"></a><a name="p46325281851"></a>When the biggest entry in lists does not exceed the length threshold indicated by this parameter, lists are encoded using ziplist to save memory.</p>
</td>
<td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.2.7.1.5 "><p id="p663762810517"><a name="p663762810517"></a><a name="p663762810517"></a>1 to 10000</p>
</td>
<td class="cellrowborder" valign="top" width="9.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p9644172819515"><a name="p9644172819515"></a><a name="p9644172819515"></a>64</p>
</td>
</tr>
<tr id="row764572817514"><td class="cellrowborder" valign="top" width="10.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p1064913281059"><a name="p1064913281059"></a><a name="p1064913281059"></a>7</p>
</td>
<td class="cellrowborder" valign="top" width="13.000000000000004%" headers="mcps1.2.7.1.2 "><p id="p1665562811515"><a name="p1665562811515"></a><a name="p1665562811515"></a>set-max-intset-entries</p>
</td>
<td class="cellrowborder" valign="top" width="12.000000000000002%" headers="mcps1.2.7.1.3 "><p id="p86631028253"><a name="p86631028253"></a><a name="p86631028253"></a>Interger</p>
</td>
<td class="cellrowborder" valign="top" width="34.00000000000001%" headers="mcps1.2.7.1.4 "><p id="p16676286511"><a name="p16676286511"></a><a name="p16676286511"></a>When a set is composed entirely of strings and the number of integers does not exceed the length threshold indicated by this parameter, the set is encoded using intset to save memory.</p>
</td>
<td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.2.7.1.5 "><p id="p4672172817519"><a name="p4672172817519"></a><a name="p4672172817519"></a>1 to 10000</p>
</td>
<td class="cellrowborder" valign="top" width="9.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p12675628558"><a name="p12675628558"></a><a name="p12675628558"></a>512</p>
</td>
</tr>
<tr id="row46773281259"><td class="cellrowborder" valign="top" width="10.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p1568113281058"><a name="p1568113281058"></a><a name="p1568113281058"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="13.000000000000004%" headers="mcps1.2.7.1.2 "><p id="p186861028951"><a name="p186861028951"></a><a name="p186861028951"></a>zset-max-ziplist-entries</p>
</td>
<td class="cellrowborder" valign="top" width="12.000000000000002%" headers="mcps1.2.7.1.3 "><p id="p126930282514"><a name="p126930282514"></a><a name="p126930282514"></a>Interger</p>
</td>
<td class="cellrowborder" valign="top" width="34.00000000000001%" headers="mcps1.2.7.1.4 "><p id="p270118281055"><a name="p270118281055"></a><a name="p270118281055"></a>When the number of entries in sorted sets is less than the value of this parameter, sorted sets are encoded using a memory efficient data structure.</p>
</td>
<td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.2.7.1.5 "><p id="p670552818514"><a name="p670552818514"></a><a name="p670552818514"></a>1~10000</p>
</td>
<td class="cellrowborder" valign="top" width="9.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p4708192815514"><a name="p4708192815514"></a><a name="p4708192815514"></a>128</p>
</td>
</tr>
<tr id="row87105285519"><td class="cellrowborder" valign="top" width="10.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p137158281153"><a name="p137158281153"></a><a name="p137158281153"></a>9</p>
</td>
<td class="cellrowborder" valign="top" width="13.000000000000004%" headers="mcps1.2.7.1.2 "><p id="p1072010281359"><a name="p1072010281359"></a><a name="p1072010281359"></a>zset-max-ziplist-value</p>
</td>
<td class="cellrowborder" valign="top" width="12.000000000000002%" headers="mcps1.2.7.1.3 "><p id="p1372920281553"><a name="p1372920281553"></a><a name="p1372920281553"></a>Interger</p>
</td>
<td class="cellrowborder" valign="top" width="34.00000000000001%" headers="mcps1.2.7.1.4 "><p id="p15734102814511"><a name="p15734102814511"></a><a name="p15734102814511"></a>When the biggest entry in sorted sets does not exceed the length threshold indicated by this parameter, sorted sets are encoded using ziplist to save memory.</p>
</td>
<td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.2.7.1.5 "><p id="p12739142813513"><a name="p12739142813513"></a><a name="p12739142813513"></a>1 to 10000</p>
</td>
<td class="cellrowborder" valign="top" width="9.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p19742172811510"><a name="p19742172811510"></a><a name="p19742172811510"></a>64</p>
</td>
</tr>
<tr id="row974410281753"><td class="cellrowborder" valign="top" width="10.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p774913281759"><a name="p774913281759"></a><a name="p774913281759"></a>10</p>
</td>
<td class="cellrowborder" valign="top" width="13.000000000000004%" headers="mcps1.2.7.1.2 "><p id="p1475382818517"><a name="p1475382818517"></a><a name="p1475382818517"></a>latency-monitor-threshold</p>
</td>
<td class="cellrowborder" valign="top" width="12.000000000000002%" headers="mcps1.2.7.1.3 "><p id="p47641928453"><a name="p47641928453"></a><a name="p47641928453"></a>Interger</p>
</td>
<td class="cellrowborder" valign="top" width="34.00000000000001%" headers="mcps1.2.7.1.4 "><p id="p177681285519"><a name="p177681285519"></a><a name="p177681285519"></a>Threshold time in latency monitoring.</p>
<p id="p147705281752"><a name="p147705281752"></a><a name="p147705281752"></a>If this parameter is set to <strong id="b1164113012160"><a name="b1164113012160"></a><a name="b1164113012160"></a>0</strong>, latency monitoring is disabled. If this parameter is set to a value greater than 0, all events blocking the server for a time greater than the configured value will be logged.</p>
<p id="p47721428251"><a name="p47721428251"></a><a name="p47721428251"></a>By running the LATENCY command, you can perform operations related to latency monitoring, such as obtaining statistical data, and configuring and enabling latency monitoring. For more information about the latency-monitor-threshold, visit <a href="https://redis.io/topics/latency-monitor" target="_blank" rel="noopener noreferrer">https://redis.io/topics/latency-monitor</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.2.7.1.5 "><p id="p57762281152"><a name="p57762281152"></a><a name="p57762281152"></a>0 to 86400000 Unit: ms</p>
</td>
<td class="cellrowborder" valign="top" width="9.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p107821628859"><a name="p107821628859"></a><a name="p107821628859"></a>0</p>
</td>
</tr>
<tr id="row1378412812513"><td class="cellrowborder" valign="top" width="10.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p778915288513"><a name="p778915288513"></a><a name="p778915288513"></a>12</p>
</td>
<td class="cellrowborder" valign="top" width="13.000000000000004%" headers="mcps1.2.7.1.2 "><p id="p17796142818515"><a name="p17796142818515"></a><a name="p17796142818515"></a>reserved-memory</p>
</td>
<td class="cellrowborder" valign="top" width="12.000000000000002%" headers="mcps1.2.7.1.3 "><p id="p1880314281459"><a name="p1880314281459"></a><a name="p1880314281459"></a>Interger</p>
</td>
<td class="cellrowborder" valign="top" width="34.00000000000001%" headers="mcps1.2.7.1.4 "><p id="p7307339173312"><a name="p7307339173312"></a><a name="p7307339173312"></a>Reserved memory, which is the number of megabytes reserved for the backend to perform internal processing such as persistence and master/standby replication.</p>
<p id="p38851334333"><a name="p38851334333"></a><a name="p38851334333"></a>This parameter is available only for master/standby instances.</p>
<p id="p16812628551"><a name="p16812628551"></a><a name="p16812628551"></a>The size of the reserved memory can be adjusted, but must be in the value range described in the next column. For more information about maximum available memory of each instance type, see <em id="i6666133115511"><a name="i6666133115511"></a><a name="i6666133115511"></a>Distributed Cache Service User Guide</em>.</p>
</td>
<td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.2.7.1.5 "><p id="p9817828555"><a name="p9817828555"></a><a name="p9817828555"></a>0% to 50% of maximum memory space initially available to the instance and below the current free memory space. Unit: MB.</p>
</td>
<td class="cellrowborder" valign="top" width="9.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p78221281956"><a name="p78221281956"></a><a name="p78221281956"></a>0</p>
</td>
</tr>
<tr id="row0827122812513"><td class="cellrowborder" valign="top" width="10.000000000000002%" headers="mcps1.2.7.1.1 "><p id="p1283219281154"><a name="p1283219281154"></a><a name="p1283219281154"></a>13</p>
</td>
<td class="cellrowborder" valign="top" width="13.000000000000004%" headers="mcps1.2.7.1.2 "><p id="p128389281352"><a name="p128389281352"></a><a name="p128389281352"></a>notify-keyspace-events</p>
</td>
<td class="cellrowborder" valign="top" width="12.000000000000002%" headers="mcps1.2.7.1.3 "><p id="p9849102814520"><a name="p9849102814520"></a><a name="p9849102814520"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="34.00000000000001%" headers="mcps1.2.7.1.4 "><p id="p485418285514"><a name="p485418285514"></a><a name="p485418285514"></a>Keyspace event notification. If this parameter is configured, the Redis Sub/Pub feature will allow clients to receive an event when a Redis data set is modified.</p>
</td>
<td class="cellrowborder" valign="top" width="22.000000000000004%" headers="mcps1.2.7.1.5 "><p id="p98601128754"><a name="p98601128754"></a><a name="p98601128754"></a>If the parameter value is a string of multiple characters, keyspace event notification is enabled and each character identifies a class of keyspace events for which Redis will send notifications.</p>
<p id="p78838286510"><a name="p78838286510"></a><a name="p78838286510"></a>K: Keyspace events, published with the __keyspace@__ prefix</p>
<p id="p888422812513"><a name="p888422812513"></a><a name="p888422812513"></a>E: Keyevent events, published with the __keyevent@__ prefix</p>
<p id="p1888872818513"><a name="p1888872818513"></a><a name="p1888872818513"></a>g: Generic commands (non-type specific) such as DEL, EXPIRE, and RENAME</p>
<p id="p1289017281558"><a name="p1289017281558"></a><a name="p1289017281558"></a>$: String commands</p>
<p id="p18914281854"><a name="p18914281854"></a><a name="p18914281854"></a>l: List commands</p>
<p id="p289392815513"><a name="p289392815513"></a><a name="p289392815513"></a>s: Set commands</p>
<p id="p289519285512"><a name="p289519285512"></a><a name="p289519285512"></a>h: Hash commands</p>
<p id="p78961528456"><a name="p78961528456"></a><a name="p78961528456"></a>z: Sorted set commands</p>
<p id="p148982028355"><a name="p148982028355"></a><a name="p148982028355"></a>x: Expired events (events generated every time a key expires)</p>
<p id="p17900182816519"><a name="p17900182816519"></a><a name="p17900182816519"></a>e: Evicted events (events generated when a key is evicted for maxmemory)</p>
<p id="p14970177195518"><a name="p14970177195518"></a><a name="p14970177195518"></a>For more information, see the following note.</p>
</td>
<td class="cellrowborder" valign="top" width="9.000000000000002%" headers="mcps1.2.7.1.6 "><p id="p18452173419149"><a name="p18452173419149"></a><a name="p18452173419149"></a>Ex</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:** 
>More about the  **notify-keyspace-events**  parameter:
>-   Allowed characters are K, E, KE, A, g, l, s, h, z, x, e, and $. The parameter value must contain either  **K**  or  **E**.
>-   **A**  is an alias for  **g$lshzxe**  and cannot be used together with any of the characters in g$lshzxe.
>-   For example, the value  **Kl**  means that Redis will notify Pub/Sub clients about keyspace events and list commands. The value  **AKE**  means Redis will notify Pub/Sub clients about all events.

**Example response**

```
{
    "status": "RUNNING",
    "instance_id": "c08fdc6e-5c25-4185-ab57-c0a5529b727f",
    "redis_config": [
        {
            "description": "How Redis will select what to remove when maxmemory is reached, You can select among five behaviors: volatile-lru : remove the key with an expire set using an LRU algorithm allkeys-lru : remove any key according to the LRU algorithm volatile-random: remove a random key with an expire set allkeys-random: remove a random key, any key volatile-ttl : remove the key with the nearest expire time (minor TTL) noeviction : don't expire at all, just return an error on write operations",
            "param_id": 2,
            "param_name": "maxmemory-policy",
            "param_value": "noeviction",
            "default_value": "noeviction",
            "value_type": "Enum",
            "value_range": "volatile-lru,allkeys-lru,volatile-random,allkeys-random,volatile-ttl,noeviction"
        },
        {
            "description": "Hashes are encoded using a memory efficient data structure when they have a small number of entries",
            "param_id": 3,
            "param_name": "hash-max-ziplist-entries",
            "param_value": "512",
            "default_value": "512",
            "value_type": "Interger",
            "value_range": "1-10000"
        },
        {
            "description": "Hashes are encoded using a memory efficient data structure when the biggest entry does not exceed a given threshold",
            "param_id": 4,
            "param_name": "hash-max-ziplist-value",
            "param_value": "64",
            "default_value": "64",
            "value_type": "Interger",
            "value_range": "1-10000"
        },
        {
            "description": "Lists are encoded using a memory efficient data structure when they have a small number of entries",
            "param_id": 5,
            "param_name": "list-max-ziplist-entries",
            "param_value": "512",
            "default_value": "512",
            "value_type": "Interger",
            "value_range": "1-10000"
        },
        {
            "description": "Lists are encoded using a memory efficient data structure when the biggest entry does not exceed a given threshold",
            "param_id": 6,
            "param_name": "list-max-ziplist-value",
            "param_value": "64",
            "default_value": "64",
            "value_type": "Interger",
            "value_range": "1-10000"
        },
        {
            "description": "When a set is composed of just strings that happen to be integers in radix 10 in the range of 64 bit signed integers.",
            "param_id": 7,
            "param_name": "set-max-intset-entries",
            "param_value": "512",
            "default_value": "512",
            "value_type": "Interger",
            "value_range": "1-10000"
        },
        {
            "description": "Sorted sets are encoded using a memory efficient data structure when they have a small number of entries",
            "param_id": 8,
            "param_name": "zset-max-ziplist-entries",
            "param_value": "128",
            "default_value": "128",
            "value_type": "Interger",
            "value_range": "1-10000"
        },
        {
            "description": "Sorted sets are encoded using a memory efficient data structure when the biggest entry does not exceed a given threshold",
            "param_id": 9,
            "param_name": "zset-max-ziplist-value",
            "param_value": "64",
            "default_value": "64",
            "value_type": "Interger",
            "value_range": "1-10000"
        },
        {
            "description": "Close the connection after a client is idle for N seconds (0 to disable)",
            "param_id": 1,
            "param_name": "timeout",
            "param_value": "0",
            "default_value": "0",
            "value_type": "Interger",
            "value_range": "0-7200"
        },
        {
            "description": "Only events that run in more time than the configured latency-monitor-threshold will be logged as latency spikes. If latency-monitor-threshold is set to 0, latency monitoring is disabled. If latency-monitor-threshold is set to a value greater than 0, all events blocking the server for a time equal to or greater than the configured latency-monitor-threshold will be logged.",
            "param_id": 10,
            "param_name": "latency-monitor-threshold",
            "param_value": "0",
            "default_value": "0",
            "value_type": "Interger",
            "value_range": "0-86400000"
        },
        {
            "description": "The total memory, in bytes, reserved for non-data usage.",
            "param_id": 12,
            "param_name": "reserved-memory",
            "param_value": "0",
            "default_value": "0",
            "value_type": "Interger",
            "value_range": "0-6553"
        },
        {
            "description": "Redis can notify Pub or Sub clients about events happening in the key space",
            "param_id": 13,
            "param_name": "notify-keyspace-events",
            "param_value": null,
            "default_value": null,
            "value_type": "regular",
            "value_range": "([KE]+([A]|[g$lshzxe]+)){0,11}"
        }
    ],
    "config_status": "SUCCESS",
    "config_time": ""
}
```

## Status Code<a name="section1144939111219"></a>

[Table 5](#table1644239141218)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  5**  Status code

<a name="table1644239141218"></a>
<table><thead align="left"><tr id="row8454396123"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p134513920126"><a name="p134513920126"></a><a name="p134513920126"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p1045193915122"><a name="p1045193915122"></a><a name="p1045193915122"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row74583915129"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p1045143931210"><a name="p1045143931210"></a><a name="p1045143931210"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p64543901210"><a name="p64543901210"></a><a name="p64543901210"></a>Instance configurations queried successfully.</p>
</td>
</tr>
</tbody>
</table>

