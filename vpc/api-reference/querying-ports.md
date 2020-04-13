# Querying Ports<a name="vpc_port02_0001"></a>

## Function<a name="en-us_topic_0062207386_section66569185"></a>

Queries all networks accessible to the tenant submitting the request. 

## URI<a name="en-us_topic_0062207386_section62251757"></a>

GET /v2.0/ports

Example:

```
GET https://{Endpoint}/v2.0/ports?id={port_id}&name={port_name}&admin_state_up={is_admin_status_up}&network_id={network_id}&mac_address={port_mac}&device_id={port_device_id}&device_owner={device_owner}&tenant_id={tenant_id}&status={port_status}&fixed_ips=ip_address={ip_address}&fixed_ips=subnet_id={subnet_id}
```

Example of querying ports by page

```
GET https://{Endpoint}/v2.0/ports?limit=2&marker=791870bd-36a7-4d9b-b015-a78e9b06af08&page_reverse=False
```

[Table 1](#table534412611487)  describes the parameters.

**Table  1**  Parameter description

<a name="table534412611487"></a>
<table><thead align="left"><tr id="row448492674817"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.5.1.1"><p id="p24841926154819"><a name="p24841926154819"></a><a name="p24841926154819"></a><strong id="b692610714300"><a name="b692610714300"></a><a name="b692610714300"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.2"><p id="p1648432615489"><a name="p1648432615489"></a><a name="p1648432615489"></a><strong id="b933103112306"><a name="b933103112306"></a><a name="b933103112306"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.3"><p id="p144841026144810"><a name="p144841026144810"></a><a name="p144841026144810"></a><strong id="b187643113011"><a name="b187643113011"></a><a name="b187643113011"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.2.5.1.4"><p id="p2484112664814"><a name="p2484112664814"></a><a name="p2484112664814"></a><strong id="b27092032133011"><a name="b27092032133011"></a><a name="b27092032133011"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row948482644816"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p18484826154812"><a name="p18484826154812"></a><a name="p18484826154812"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p1848410267488"><a name="p1848410267488"></a><a name="p1848410267488"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p104842262481"><a name="p104842262481"></a><a name="p104842262481"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p94841626104816"><a name="p94841626104816"></a><a name="p94841626104816"></a>Specifies that the port ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row8484226114819"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p7484202694817"><a name="p7484202694817"></a><a name="p7484202694817"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p9484162664814"><a name="p9484162664814"></a><a name="p9484162664814"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p1548412269482"><a name="p1548412269482"></a><a name="p1548412269482"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p8485172674817"><a name="p8485172674817"></a><a name="p8485172674817"></a>Specifies that the port name is used as the filtering condition.</p>
</td>
</tr>
<tr id="row1448518262483"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p124851326114815"><a name="p124851326114815"></a><a name="p124851326114815"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p18485112614488"><a name="p18485112614488"></a><a name="p18485112614488"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p13485162694818"><a name="p13485162694818"></a><a name="p13485162694818"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p132122181612"><a name="p132122181612"></a><a name="p132122181612"></a>Specifies that the admin state is used as the filtering condition.</p>
<p id="p9485122611486"><a name="p9485122611486"></a><a name="p9485122611486"></a>The value can be <strong id="b4957120185718"><a name="b4957120185718"></a><a name="b4957120185718"></a>true</strong> or <strong id="b18958122012572"><a name="b18958122012572"></a><a name="b18958122012572"></a>false</strong>.</p>
</td>
</tr>
<tr id="row848522612484"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p1448516264489"><a name="p1448516264489"></a><a name="p1448516264489"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p154852026124815"><a name="p154852026124815"></a><a name="p154852026124815"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p1048592684818"><a name="p1048592684818"></a><a name="p1048592684818"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p10485132664815"><a name="p10485132664815"></a><a name="p10485132664815"></a>Specifies that the network ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row1948562624813"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p154851626134817"><a name="p154851626134817"></a><a name="p154851626134817"></a>mac_address</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p5485726104812"><a name="p5485726104812"></a><a name="p5485726104812"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p11485132644813"><a name="p11485132644813"></a><a name="p11485132644813"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p114851326144819"><a name="p114851326144819"></a><a name="p114851326144819"></a>Specifies that the MAC address is used as the filtering condition.</p>
</td>
</tr>
<tr id="row1348552617486"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p4485926194812"><a name="p4485926194812"></a><a name="p4485926194812"></a>device_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p448522624814"><a name="p448522624814"></a><a name="p448522624814"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p648511262487"><a name="p648511262487"></a><a name="p648511262487"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p1548518263489"><a name="p1548518263489"></a><a name="p1548518263489"></a>Specifies that the device ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row16485122614487"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p13485192616487"><a name="p13485192616487"></a><a name="p13485192616487"></a>device_owner</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p3485152619489"><a name="p3485152619489"></a><a name="p3485152619489"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p8485102620484"><a name="p8485102620484"></a><a name="p8485102620484"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p64851126204810"><a name="p64851126204810"></a><a name="p64851126204810"></a>Specifies that the device owner is used as the filtering condition.</p>
</td>
</tr>
<tr id="row0485142618484"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p15485172619482"><a name="p15485172619482"></a><a name="p15485172619482"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p5485172612482"><a name="p5485172612482"></a><a name="p5485172612482"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p2048519261484"><a name="p2048519261484"></a><a name="p2048519261484"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p47831820460"><a name="p47831820460"></a><a name="p47831820460"></a>Specifies that the port status is used as the filtering condition.</p>
<p id="p348516264489"><a name="p348516264489"></a><a name="p348516264489"></a>The value can be <strong id="b1868813530222922"><a name="b1868813530222922"></a><a name="b1868813530222922"></a>ACTIVE</strong>, <strong id="b1414577617222922"><a name="b1414577617222922"></a><a name="b1414577617222922"></a>BUILD</strong>, or <strong id="b92255202222922"><a name="b92255202222922"></a><a name="b92255202222922"></a>DOWN</strong>.</p>
</td>
</tr>
<tr id="row154851626164815"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p10485926164819"><a name="p10485926164819"></a><a name="p10485926164819"></a>fixed_ips</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p15485826194811"><a name="p15485826194811"></a><a name="p15485826194811"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p11485026164810"><a name="p11485026164810"></a><a name="p11485026164810"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p9486526174813"><a name="p9486526174813"></a><a name="p9486526174813"></a>Specifies that the IP address is used as the filtering condition. The value can be <strong id="b91107595448"><a name="b91107595448"></a><a name="b91107595448"></a>fixed_ips=ip_address</strong> or <strong id="b431763164513"><a name="b431763164513"></a><a name="b431763164513"></a>fixed_ips=subnet_id</strong>.</p>
</td>
</tr>
<tr id="row84861626204816"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p1448672614484"><a name="p1448672614484"></a><a name="p1448672614484"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p13486626114819"><a name="p13486626114819"></a><a name="p13486626114819"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p194861626124817"><a name="p194861626124817"></a><a name="p194861626124817"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p114861226174812"><a name="p114861226174812"></a><a name="p114861226174812"></a>Specifies that the project ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row748682684814"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p1148672694815"><a name="p1148672694815"></a><a name="p1148672694815"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p154862263482"><a name="p154862263482"></a><a name="p154862263482"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p11486926134819"><a name="p11486926134819"></a><a name="p11486926134819"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p948692684817"><a name="p948692684817"></a><a name="p948692684817"></a>Specifies the start resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
</td>
</tr>
<tr id="row1048632694819"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p164861626154814"><a name="p164861626154814"></a><a name="p164861626154814"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.2 "><p id="p1948619268488"><a name="p1948619268488"></a><a name="p1948619268488"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="p2486142612485"><a name="p2486142612485"></a><a name="p2486142612485"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p01471215164915"><a name="p01471215164915"></a><a name="p01471215164915"></a>Specifies the number of records on each page.</p>
<p id="p24869261488"><a name="p24869261488"></a><a name="p24869261488"></a>The value ranges from 0 to intmax.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0062207386_section15938858"></a>

None

## Response Parameter<a name="en-us_topic_0062207386_section9232000"></a>

**Table  2**  Response parameter

<a name="en-us_topic_0062207386_table48620262"></a>
<table><thead align="left"><tr id="en-us_topic_0062207386_row18332862"><th class="cellrowborder" valign="top" width="22.32%" id="mcps1.2.4.1.1"><p id="en-us_topic_0062207386_p8566882"><a name="en-us_topic_0062207386_p8566882"></a><a name="en-us_topic_0062207386_p8566882"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.67%" id="mcps1.2.4.1.2"><p id="en-us_topic_0062207386_p22828842"><a name="en-us_topic_0062207386_p22828842"></a><a name="en-us_topic_0062207386_p22828842"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.010000000000005%" id="mcps1.2.4.1.3"><p id="en-us_topic_0062207386_p60161096"><a name="en-us_topic_0062207386_p60161096"></a><a name="en-us_topic_0062207386_p60161096"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0062207386_row41210606"><td class="cellrowborder" valign="top" width="22.32%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0062207386_p49724760"><a name="en-us_topic_0062207386_p49724760"></a><a name="en-us_topic_0062207386_p49724760"></a>ports</p>
</td>
<td class="cellrowborder" valign="top" width="24.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0062207386_p1173742"><a name="en-us_topic_0062207386_p1173742"></a><a name="en-us_topic_0062207386_p1173742"></a>Array of <a href="#table15919752145624">port</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="53.010000000000005%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0062207386_p50516929"><a name="en-us_topic_0062207386_p50516929"></a><a name="en-us_topic_0062207386_p50516929"></a>Specifies the port object list. For details, see <a href="#table15919752145624">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **port**  objects

<a name="table15919752145624"></a>
<table><thead align="left"><tr id="row28529169145624"><th class="cellrowborder" valign="top" width="28.499999999999996%" id="mcps1.2.4.1.1"><p id="p42540009145658"><a name="p42540009145658"></a><a name="p42540009145658"></a><strong id="b1349964116577"><a name="b1349964116577"></a><a name="b1349964116577"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.749999999999996%" id="mcps1.2.4.1.2"><p id="p23188741145658"><a name="p23188741145658"></a><a name="p23188741145658"></a><strong id="b84561642125718"><a name="b84561642125718"></a><a name="b84561642125718"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.75%" id="mcps1.2.4.1.3"><p id="p13444574145658"><a name="p13444574145658"></a><a name="p13444574145658"></a><strong id="b205421843125714"><a name="b205421843125714"></a><a name="b205421843125714"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row13166425145624"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p28807446145658"><a name="p28807446145658"></a><a name="p28807446145658"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p51701793145658"><a name="p51701793145658"></a><a name="p51701793145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p5183528145658"><a name="p5183528145658"></a><a name="p5183528145658"></a>Specifies the port ID. A maximum of 255 characters are allowed.</p>
<p id="p189962619371"><a name="p189962619371"></a><a name="p189962619371"></a>This parameter is not mandatory when you query ports.</p>
</td>
</tr>
<tr id="row1387566145624"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p20696121145658"><a name="p20696121145658"></a><a name="p20696121145658"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p65773124145658"><a name="p65773124145658"></a><a name="p65773124145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p10771861145658"><a name="p10771861145658"></a><a name="p10771861145658"></a>Specifies the port name.</p>
</td>
</tr>
<tr id="row36437767145624"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p949776145658"><a name="p949776145658"></a><a name="p949776145658"></a>network_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p9822997145658"><a name="p9822997145658"></a><a name="p9822997145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p36061910145658"><a name="p36061910145658"></a><a name="p36061910145658"></a>Specifies the ID of the network to which the port belongs.</p>
</td>
</tr>
<tr id="row41410455145624"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p49567182145658"><a name="p49567182145658"></a><a name="p49567182145658"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p55518807145658"><a name="p55518807145658"></a><a name="p55518807145658"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p26909682145658"><a name="p26909682145658"></a><a name="p26909682145658"></a>Specifies the administrative status.</p>
<p id="p40860550145658"><a name="p40860550145658"></a><a name="p40860550145658"></a>The value can only be <strong id="b37202937615141"><a name="b37202937615141"></a><a name="b37202937615141"></a>true</strong>.</p>
</td>
</tr>
<tr id="row11261085145624"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p58114882145658"><a name="p58114882145658"></a><a name="p58114882145658"></a>mac_address</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p9685031145658"><a name="p9685031145658"></a><a name="p9685031145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p8831008145658"><a name="p8831008145658"></a><a name="p8831008145658"></a>Specifies the port MAC address. For example, <strong id="b84235270685915"><a name="b84235270685915"></a><a name="b84235270685915"></a>"mac_address": "fa:16:3e:9e:ff:55"</strong>.</p>
<p id="p12370211145658"><a name="p12370211145658"></a><a name="p12370211145658"></a>This value can only be dynamically assigned by the system.</p>
</td>
</tr>
<tr id="row59425565145624"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p25296431145658"><a name="p25296431145658"></a><a name="p25296431145658"></a>fixed_ips</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p35745048145658"><a name="p35745048145658"></a><a name="p35745048145658"></a>Array of <a href="#table4290920914597">fixed_ip</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p48560910145658"><a name="p48560910145658"></a><a name="p48560910145658"></a>Specifies the port IP address. For details, see <a href="#table4290920914597">Table 4</a>. For example, the value is <strong id="b1148612467126"><a name="b1148612467126"></a><a name="b1148612467126"></a>"fixed_ips": [{"subnet_id": "4dc70db6-cb7f-4200-9790-a6a910776bba", "ip_address": "192.169.25.79"}]</strong>.</p>
</td>
</tr>
<tr id="row52336547145624"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p42357933145658"><a name="p42357933145658"></a><a name="p42357933145658"></a>device_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p8440512145658"><a name="p8440512145658"></a><a name="p8440512145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p23990357145658"><a name="p23990357145658"></a><a name="p23990357145658"></a>Specifies the device ID.</p>
<p id="p14586626145658"><a name="p14586626145658"></a><a name="p14586626145658"></a>This value is automatically maintained by the system and cannot be set or updated manually. The port with this field specified cannot be deleted.</p>
</td>
</tr>
<tr id="row8304195145630"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p30450002145658"><a name="p30450002145658"></a><a name="p30450002145658"></a>device_owner</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p50531130145658"><a name="p50531130145658"></a><a name="p50531130145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p60282892145658"><a name="p60282892145658"></a><a name="p60282892145658"></a>Specifies the DHCP, router or Nova to which a device belongs.</p>
<p id="p2837225125711"><a name="p2837225125711"></a><a name="p2837225125711"></a>This parameter value cannot be updated. You can only set <strong id="b842352706202734"><a name="b842352706202734"></a><a name="b842352706202734"></a>device_owner</strong> to <strong id="b842352706202743"><a name="b842352706202743"></a><a name="b842352706202743"></a>neutron:VIP_PORT</strong> for a virtual IP address port during port creation. If this parameter of a port is not left blank, the port can only be deleted when this parameter value is <strong id="b842352706203622"><a name="b842352706203622"></a><a name="b842352706203622"></a>neutron:VIP_PORT</strong>.</p>
<p id="p1458812975819"><a name="p1458812975819"></a><a name="p1458812975819"></a>The port with this field specified cannot be deleted.</p>
</td>
</tr>
<tr id="row47218120145630"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p43524921145658"><a name="p43524921145658"></a><a name="p43524921145658"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p35857692145658"><a name="p35857692145658"></a><a name="p35857692145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row925022145630"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p12676379145658"><a name="p12676379145658"></a><a name="p12676379145658"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p20153784145658"><a name="p20153784145658"></a><a name="p20153784145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p12312282145658"><a name="p12312282145658"></a><a name="p12312282145658"></a>Specifies the port status. The value can be <strong id="b842352706112837"><a name="b842352706112837"></a><a name="b842352706112837"></a>ACTIVE</strong>, <strong id="b842352706112844"><a name="b842352706112844"></a><a name="b842352706112844"></a>BUILD</strong>, or <strong id="b842352706112853"><a name="b842352706112853"></a><a name="b842352706112853"></a>DOWN</strong>.</p>
<p id="p43701677145658"><a name="p43701677145658"></a><a name="p43701677145658"></a>The status of a HANA SR-IOV VM port is always <strong id="b842352706112928"><a name="b842352706112928"></a><a name="b842352706112928"></a>DOWN</strong>.</p>
</td>
</tr>
<tr id="row36940776145630"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p48921078145658"><a name="p48921078145658"></a><a name="p48921078145658"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p646712486358"><a name="p646712486358"></a><a name="p646712486358"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p4527282145658"><a name="p4527282145658"></a><a name="p4527282145658"></a>Specifies the UUID of the security group, for example, <strong id="b842352706113011"><a name="b842352706113011"></a><a name="b842352706113011"></a>"security_groups": ["a0608cbf-d047-4f54-8b28-cd7b59853fff"]</strong>. This is an extended attribute.</p>
<p id="p103001912487"><a name="p103001912487"></a><a name="p103001912487"></a>This parameter cannot be left blank.</p>
</td>
</tr>
<tr id="row17626705145630"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p41382197145658"><a name="p41382197145658"></a><a name="p41382197145658"></a>allowed_address_pairs</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p13529152643712"><a name="p13529152643712"></a><a name="p13529152643712"></a>Array of <a href="#en-us_topic_0062207355_table57914257">allow_address_pair</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p30975735145658"><a name="p30975735145658"></a><a name="p30975735145658"></a>Specifies the IP address and MAC address pair. This is an extended attribute. For details, see <a href="#en-us_topic_0062207355_table57914257">Table 5</a>. </p>
<p id="p7136530194312"><a name="p7136530194312"></a><a name="p7136530194312"></a>Instructions:</p>
<a name="ul18386852174311"></a><a name="ul18386852174311"></a><ul id="ul18386852174311"><li>The IP address cannot be <strong id="b13938102310270"><a name="b13938102310270"></a><a name="b13938102310270"></a>0.0.0.0</strong>.</li><li>Configure an independent security group for the port if a large CIDR block (subnet mask less than 24) is configured for parameter <strong id="b842352706135639"><a name="b842352706135639"></a><a name="b842352706135639"></a>allowed_address_pairs</strong>.</li><li>In the hardware SDN networking plan, the <strong id="b84235270611336"><a name="b84235270611336"></a><a name="b84235270611336"></a>ip_address</strong> attribute value cannot be in CIDR format.</li><li>To assign a virtual IP address to an ECS, the IP address configured in <strong id="b842352706212447"><a name="b842352706212447"></a><a name="b842352706212447"></a>allowed_address_pairs</strong> must be an existing ECS NIC IP address. Otherwise, the virtual IP address cannot be used for communication.</li></ul>
</td>
</tr>
<tr id="row938573145630"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p34089655145658"><a name="p34089655145658"></a><a name="p34089655145658"></a>extra_dhcp_opts</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p440115378365"><a name="p440115378365"></a><a name="p440115378365"></a>Array of <a href="#table5056075615524">extra_dhcp_opt</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p45787521145658"><a name="p45787521145658"></a><a name="p45787521145658"></a>Specifies the extended DHCP option. This is an extended attribute. For details, see <a href="#table5056075615524">Table 6</a>.</p>
</td>
</tr>
<tr id="row46629855145636"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p62371645145658"><a name="p62371645145658"></a><a name="p62371645145658"></a>binding:vif_details</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p18938488145658"><a name="p18938488145658"></a><a name="p18938488145658"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p62312767145658"><a name="p62312767145658"></a><a name="p62312767145658"></a>Specifies the VIF details. Parameter <strong id="b842352706173430"><a name="b842352706173430"></a><a name="b842352706173430"></a>ovs_hybrid_plug</strong> specifies whether the OVS/bridge hybrid mode is used.</p>
</td>
</tr>
<tr id="row35771758145636"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p7522524145658"><a name="p7522524145658"></a><a name="p7522524145658"></a>binding:profile</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p5344685145658"><a name="p5344685145658"></a><a name="p5344685145658"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p4278449145658"><a name="p4278449145658"></a><a name="p4278449145658"></a>Specifies the user-defined settings. This is an extended attribute.</p>
<p id="p38506045145658"><a name="p38506045145658"></a><a name="p38506045145658"></a>Instructions:</p>
<a name="ul11010089145658"></a><a name="ul11010089145658"></a><ul id="ul11010089145658"><li>The <strong id="b842352706153317_1"><a name="b842352706153317_1"></a><a name="b842352706153317_1"></a>internal_elb</strong> field is in boolean type and is available to common tenants. Set the value of this parameter to <strong id="b842352706105631"><a name="b842352706105631"></a><a name="b842352706105631"></a>true</strong> only when you assign a virtual IP address to an internal network load balancer. Common tenants do not have the permission to change the value of this field, which is maintained by the system.<p id="p041674418210"><a name="p041674418210"></a><a name="p041674418210"></a>Example:</p>
<p id="p1774284092111"><a name="p1774284092111"></a><a name="p1774284092111"></a>{"internal_elb": true}</p>
</li><li>The <strong id="b842352706153317_3"><a name="b842352706153317_3"></a><a name="b842352706153317_3"></a>disable_security_groups</strong> field is in boolean type and is available to common tenants. The default value is <strong id="b842352706115044"><a name="b842352706115044"></a><a name="b842352706115044"></a>false</strong>. In high-performance communication scenarios, you can set the parameter value to <strong id="b842352706115112"><a name="b842352706115112"></a><a name="b842352706115112"></a>true</strong>, which makes this parameter to be available to common tenants. You can specify this parameter when creating a port. Currently, the value of this parameter can only be set to <strong id="b842352706154853"><a name="b842352706154853"></a><a name="b842352706154853"></a>true</strong>.<p id="p19402030145658"><a name="p19402030145658"></a><a name="p19402030145658"></a>Example:</p>
<p id="p40400544145658"><a name="p40400544145658"></a><a name="p40400544145658"></a>{"disable_security_groups": true },</p>
<p id="p28060583145658"><a name="p28060583145658"></a><a name="p28060583145658"></a>Currently, the value can only be set to <strong id="b842352706204236"><a name="b842352706204236"></a><a name="b842352706204236"></a>true</strong>. When the value is set to <strong id="b1283192462204259"><a name="b1283192462204259"></a><a name="b1283192462204259"></a>true</strong>, the FWaaS function does not take effect.</p>
</li></ul>
<a name="ul51218659145658"></a><a name="ul51218659145658"></a>
</td>
</tr>
<tr id="row63233200145636"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p4700493145658"><a name="p4700493145658"></a><a name="p4700493145658"></a>binding:vnic_type</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p45195649145658"><a name="p45195649145658"></a><a name="p45195649145658"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p42146344145658"><a name="p42146344145658"></a><a name="p42146344145658"></a>Specifies the type of the bound vNIC.</p>
<p id="p43772780145658"><a name="p43772780145658"></a><a name="p43772780145658"></a><strong id="b84235270616736"><a name="b84235270616736"></a><a name="b84235270616736"></a>normal</strong>: Softswitch</p>
</td>
</tr>
<tr id="row8784124710810"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p759775317217"><a name="p759775317217"></a><a name="p759775317217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p1675142052312"><a name="p1675142052312"></a><a name="p1675142052312"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row19797526919"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p1953114119914"><a name="p1953114119914"></a><a name="p1953114119914"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p595318416919"><a name="p595318416919"></a><a name="p595318416919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p89991542406"><a name="p89991542406"></a><a name="p89991542406"></a>Specifies the time (UTC) when the port is created.</p>
<p id="p1395374115919"><a name="p1395374115919"></a><a name="p1395374115919"></a>Format: <em id="i0407177174015"><a name="i0407177174015"></a><a name="i0407177174015"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row124097610917"><td class="cellrowborder" valign="top" width="28.499999999999996%" headers="mcps1.2.4.1.1 "><p id="p139719548912"><a name="p139719548912"></a><a name="p139719548912"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="28.749999999999996%" headers="mcps1.2.4.1.2 "><p id="p53971154594"><a name="p53971154594"></a><a name="p53971154594"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.75%" headers="mcps1.2.4.1.3 "><p id="p1339713549918"><a name="p1339713549918"></a><a name="p1339713549918"></a>Specifies the time (UTC) when the port is updated.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i73302053144017"><a name="i73302053144017"></a><a name="i73302053144017"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
</tbody>
</table>

**Table  4** **fixed\_ip**  objects

<a name="table4290920914597"></a>
<table><thead align="left"><tr id="row3523499914597"><th class="cellrowborder" valign="top" width="25.95259525952595%" id="mcps1.2.4.1.1"><p id="p6174509115118"><a name="p6174509115118"></a><a name="p6174509115118"></a><strong id="b192911759144013"><a name="b192911759144013"></a><a name="b192911759144013"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.95259525952595%" id="mcps1.2.4.1.2"><p id="p3529643715118"><a name="p3529643715118"></a><a name="p3529643715118"></a><strong id="b5321184903910"><a name="b5321184903910"></a><a name="b5321184903910"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.09480948094809%" id="mcps1.2.4.1.3"><p id="p2048854115118"><a name="p2048854115118"></a><a name="p2048854115118"></a><strong id="b880419491445"><a name="b880419491445"></a><a name="b880419491445"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2319879914597"><td class="cellrowborder" valign="top" width="25.95259525952595%" headers="mcps1.2.4.1.1 "><p id="p626497215118"><a name="p626497215118"></a><a name="p626497215118"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.95259525952595%" headers="mcps1.2.4.1.2 "><p id="p3770069415118"><a name="p3770069415118"></a><a name="p3770069415118"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.09480948094809%" headers="mcps1.2.4.1.3 "><p id="p2612244315118"><a name="p2612244315118"></a><a name="p2612244315118"></a>Specifies the ID of the subnet to which the port belongs.</p>
<p id="p3377540315118"><a name="p3377540315118"></a><a name="p3377540315118"></a>This parameter cannot be updated.</p>
</td>
</tr>
<tr id="row636738414597"><td class="cellrowborder" valign="top" width="25.95259525952595%" headers="mcps1.2.4.1.1 "><p id="p6042468915118"><a name="p6042468915118"></a><a name="p6042468915118"></a>ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="25.95259525952595%" headers="mcps1.2.4.1.2 "><p id="p6256165915118"><a name="p6256165915118"></a><a name="p6256165915118"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.09480948094809%" headers="mcps1.2.4.1.3 "><p id="p1336175915118"><a name="p1336175915118"></a><a name="p1336175915118"></a>Specifies the port IP address.</p>
<p id="p5314696715118"><a name="p5314696715118"></a><a name="p5314696715118"></a>This parameter cannot be updated.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **allow\_address\_pair**  objects

<a name="en-us_topic_0062207355_table57914257"></a>
<table><thead align="left"><tr id="en-us_topic_0062207355_row41852331"><th class="cellrowborder" valign="top" width="25.89%" id="mcps1.2.4.1.1"><p id="en-us_topic_0062207355_p34595685"><a name="en-us_topic_0062207355_p34595685"></a><a name="en-us_topic_0062207355_p34595685"></a><strong id="b171900156456"><a name="b171900156456"></a><a name="b171900156456"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.16%" id="mcps1.2.4.1.2"><p id="en-us_topic_0062207355_p50787128"><a name="en-us_topic_0062207355_p50787128"></a><a name="en-us_topic_0062207355_p50787128"></a><strong id="b14804121615459"><a name="b14804121615459"></a><a name="b14804121615459"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="47.949999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0062207355_p52626454"><a name="en-us_topic_0062207355_p52626454"></a><a name="en-us_topic_0062207355_p52626454"></a><strong id="b75883186454"><a name="b75883186454"></a><a name="b75883186454"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0062207355_row34884411"><td class="cellrowborder" valign="top" width="25.89%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0062207355_p7065065"><a name="en-us_topic_0062207355_p7065065"></a><a name="en-us_topic_0062207355_p7065065"></a>ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="26.16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0062207355_p35399367"><a name="en-us_topic_0062207355_p35399367"></a><a name="en-us_topic_0062207355_p35399367"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.949999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0062207355_p64721603"><a name="en-us_topic_0062207355_p64721603"></a><a name="en-us_topic_0062207355_p64721603"></a>Specifies the IP address.</p>
<p id="en-us_topic_0062207355_p45623521"><a name="en-us_topic_0062207355_p45623521"></a><a name="en-us_topic_0062207355_p45623521"></a>This parameter cannot be <strong id="b372029376162853"><a name="b372029376162853"></a><a name="b372029376162853"></a>0.0.0.0</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0062207355_row7958508"><td class="cellrowborder" valign="top" width="25.89%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0062207355_p40659381"><a name="en-us_topic_0062207355_p40659381"></a><a name="en-us_topic_0062207355_p40659381"></a>mac_address</p>
</td>
<td class="cellrowborder" valign="top" width="26.16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0062207355_p5075526"><a name="en-us_topic_0062207355_p5075526"></a><a name="en-us_topic_0062207355_p5075526"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.949999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0062207355_p51982593"><a name="en-us_topic_0062207355_p51982593"></a><a name="en-us_topic_0062207355_p51982593"></a>Specifies the MAC address.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **extra\_dhcp\_opt**  objects

<a name="table5056075615524"></a>
<table><thead align="left"><tr id="row739480215524"><th class="cellrowborder" valign="top" width="25.722572257225725%" id="mcps1.2.4.1.1"><p id="p3368663215532"><a name="p3368663215532"></a><a name="p3368663215532"></a><strong id="b19992137184615"><a name="b19992137184615"></a><a name="b19992137184615"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.422642264226422%" id="mcps1.2.4.1.2"><p id="p4426268215532"><a name="p4426268215532"></a><a name="p4426268215532"></a><strong id="b1025023910466"><a name="b1025023910466"></a><a name="b1025023910466"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="47.85478547854785%" id="mcps1.2.4.1.3"><p id="p3407518415532"><a name="p3407518415532"></a><a name="p3407518415532"></a><strong id="b143071940164613"><a name="b143071940164613"></a><a name="b143071940164613"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2636755215524"><td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.4.1.1 "><p id="p2765891815532"><a name="p2765891815532"></a><a name="p2765891815532"></a>opt_name</p>
</td>
<td class="cellrowborder" valign="top" width="26.422642264226422%" headers="mcps1.2.4.1.2 "><p id="p2577986315532"><a name="p2577986315532"></a><a name="p2577986315532"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.85478547854785%" headers="mcps1.2.4.1.3 "><p id="p5884162715532"><a name="p5884162715532"></a><a name="p5884162715532"></a>Specifies the option name.</p>
</td>
</tr>
<tr id="row3942590315524"><td class="cellrowborder" valign="top" width="25.722572257225725%" headers="mcps1.2.4.1.1 "><p id="p1298235215532"><a name="p1298235215532"></a><a name="p1298235215532"></a>opt_value</p>
</td>
<td class="cellrowborder" valign="top" width="26.422642264226422%" headers="mcps1.2.4.1.2 "><p id="p4493762615532"><a name="p4493762615532"></a><a name="p4493762615532"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.85478547854785%" headers="mcps1.2.4.1.3 "><p id="p5057146315532"><a name="p5057146315532"></a><a name="p5057146315532"></a>Specifies the option value.</p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="en-us_topic_0062207386_section15979144"></a>

\[Example 1\]

-   Example request

    ```
    GET https://{Endpoint}/v2.0/ports?limit=1
    ```

-   Example response

    ```
    {
     "ports": [{
           "id": "791870bd-36a7-4d9b-b015-a78e9b06af08",
           "name": "port-test",
           "status": "DOWN",
           "admin_state_up": true,
           "fixed_ips": [],
           "mac_address": "fa:16:3e:01:e0:b2",
           "network_id": "00ae08c5-f727-49ab-ad4b-b069398aa171",
           "tenant_id": "db82c9e1415a464ea68048baa8acc6b8",
           "project_id": "db82c9e1415a464ea68048baa8acc6b8",
           "device_id": "",
           "device_owner": "",
           "security_groups": ["d0d58aa9-cda9-414c-9c52-6c3daf8534e6"],
           "extra_dhcp_opts": [],
           "allowed_address_pairs": [],
           "binding: vnic_type": "normal",
           "binding: vif_details": {},
           "binding: profile": {},
           "port_security_enabled": true,
           "created_at": "2018-09-13T01: 43: 41",
           "updated_at": "2018-09-13T01: 43: 41"
     }]
    }
    ```


\[Example 2\]

-   Example request

    ```
    GET https://{Endpoint}/v2.0/ports?mac_address=fa:16:3e:f1:0b:09
    ```


-   Example response

    ```
    {
        "ports": [
            {
                "admin_state_up": true,
                "allowed_address_pairs": [],
                "binding:vnic_type": "normal",
                "device_id": "e6c05704-c907-4cc1-8106-69b0996c43b9",
                "device_owner": "compute:az3.dc1",
                "extra_dhcp_opts": [],
                "fixed_ips": [
                    {
                        "ip_address": "172.16.0.37",
                        "subnet_id": "b3ac1347-63f2-4e82-b853-3d86416a0db5"
                    }
                ],
                "id": "7bb64706-6e46-4f94-a28a-4bc7caaab87d",
                "mac_address": "fa:16:3e:f1:0b:09",
                "name": "port_vm_50_3",
                "network_id": "a54e1b19-ce78-4b7e-b28b-d2d716cdc161",
                "security_groups": [
                    "ef69bc60-2f4b-4f97-b95b-e3b68df0c0b2"
                ],
                "status": "ACTIVE",
                "tenant_id": "6c9298ec8c874f7f99688489ab65f90e",
                "project_id": "6c9298ec8c874f7f99688489ab65f90e", 
                "created_at": "2018-09-13T01: 43: 41",
                "updated_at": "2018-09-13T01: 43: 41"
            }
        ]
    }
    ```


\[Example 3\]

-   Example request

    ```
    GET https://{Endpoint}/v2.0/ports?admin_state_up=False
    ```


-   Example response

    ```
    {
        "ports": [
    
            {
                "admin_state_up": false, 
                "allowed_address_pairs": [], 
                "binding:vnic_type": "normal", 
                "device_id": "", 
                "device_owner": "", 
                "extra_dhcp_opts": [], 
                "fixed_ips": [
                    {
                        "ip_address": "10.100.100.62", 
                        "subnet_id": "9b28f20c-0234-419f-a0b4-4a84f182f64b"
                    }
                ], 
                "id": "ffc0bdee-8413-4fa2-bd82-fa8efe5b3a87", 
                "mac_address": "fa:16:3e:2b:bc:57", 
                "name": "small_net_port", 
                "network_id": "b299b151-7a66-4c6f-a313-cdd3b5724296", 
                "security_groups": [
                    "ef69bc60-2f4b-4f97-b95b-e3b68df0c0b2"
                ], 
                "status": "DOWN", 
                "tenant_id": "6c9298ec8c874f7f99688489ab65f90e",
                "project_id": "6c9298ec8c874f7f99688489ab65f90e", 
                "created_at": "2018-09-13T01: 43: 41",
                "updated_at": "2018-09-13T01: 43: 41"
            }
        ]
    }
    ```


\[Example 4\]

-   Example request

    ```
    GET https://{Endpoint}/v2.0/ports?device_id=e6c05704-c907-4cc1-8106-69b0996c43b9
    ```


-   Example response

    ```
    {
        "ports": [
            {
                "admin_state_up": true, 
                "allowed_address_pairs": [], 
                "binding:vnic_type": "normal", 
                "device_id": "e6c05704-c907-4cc1-8106-69b0996c43b9", 
                "device_owner": "compute:az3.dc1", 
                "extra_dhcp_opts": [], 
                "fixed_ips": [
                    {
                        "ip_address": "10.1.0.37", 
                        "subnet_id": "b3ac1347-63f2-4e82-b853-3d86416a0db5"
                    }
                ], 
                "id": "7bb64706-6e46-4f94-a28a-4bc7caaab87d", 
                "mac_address": "fa:16:3e:f1:0b:09", 
                "name": "port_vm_50_3", 
                "network_id": "a54e1b19-ce78-4b7e-b28b-d2d716cdc161", 
                "security_groups": [
                    "ef69bc60-2f4b-4f97-b95b-e3b68df0c0b2"
                ], 
                "status": "ACTIVE", 
                "tenant_id": "6c9298ec8c874f7f99688489ab65f90e",
                "project_id": "6c9298ec8c874f7f99688489ab65f90e" ,
                "created_at": "2018-09-13T01: 43: 41",
                "updated_at": "2018-09-13T01: 43: 41"
            }
        ]
    }
    ```


\[Example 5\]

-   Example request

    ```
    GET https://{Endpoint}/v2.0/ports?tenant_id=6c9298ec8c874f7f99688489ab65f90e&name=port_vm_50_3
    ```


-   Example response

    ```
    {
        "ports": [
            {
                "admin_state_up": true, 
                "allowed_address_pairs": [], 
                "binding:vnic_type": "normal", 
                "device_id": "e6c05704-c907-4cc1-8106-69b0996c43b9", 
                "device_owner": "compute:az3.dc1", 
                "extra_dhcp_opts": [], 
                "fixed_ips": [
                    {
                        "ip_address": "10.1.0.37", 
                        "subnet_id": "b3ac1347-63f2-4e82-b853-3d86416a0db5"
                    }
                ], 
                "id": "7bb64706-6e46-4f94-a28a-4bc7caaab87d", 
                "mac_address": "fa:16:3e:f1:0b:09", 
                "name": "port_vm_50_3", 
                "network_id": "a54e1b19-ce78-4b7e-b28b-d2d716cdc161", 
                "security_groups": [
                    "ef69bc60-2f4b-4f97-b95b-e3b68df0c0b2"
                ], 
                "status": "ACTIVE", 
                "tenant_id": "6c9298ec8c874f7f99688489ab65f90e",
                "project_id": "6c9298ec8c874f7f99688489ab65f90e" ,
                "created_at": "2018-09-13T01: 43: 41",
                "updated_at": "2018-09-13T01: 43: 41"
            }
        ]
    }
    ```


\[Example 6\]

-   Example request

    ```
    GET https://{Endpoint}/v2.0/ports?name=port_vm_50_3
    ```


-   Example response

    ```
    {
        "ports": [
            {
                "status": "DOWN",
                "allowed_address_pairs": [],
                "extra_dhcp_opts": [],
                "device_owner": "",
                "fixed_ips": [
                    {
                        "subnet_id": "391c74f7-e3b1-405c-8473-2f71a0aec7dc",
                        "ip_address": "10.1.0.33"
                    }
                ],
                "id": "0f405555-739f-4a19-abb7-ec11d005b3a9",
                "security_groups": [
                    "043548bc-1020-4be0-885a-caac8530e8f6"
                ],
                "device_id": "",
                "port_security_enabled":true,
                "name": "port_vm_50_3",
                "admin_state_up": true,
                "network_id": "9898a82d-7795-4ad5-bf2c-0ed8b822be4f",
                "tenant_id": "3e4a1816927f405cacbc3dca1e05111e",
                "project_id": "3e4a1816927f405cacbc3dca1e05111e",
                "created_at": "2018-09-13T01: 43: 41",
                "updated_at": "2018-09-13T01: 43: 41",
                "binding:vnic_type": "normal",
                "mac_address": "fa:16:3e:b0:d9:cf"
            },
            {
                "status": "ACTIVE",
                "allowed_address_pairs": [],
                "extra_dhcp_opts": [],
                "device_owner": "compute:az3.dc1",
                "fixed_ips": [
                    {
                        "subnet_id": "b3ac1347-63f2-4e82-b853-3d86416a0db5",
                        "ip_address": "10.1.0.37"
                    }
                ],
                "id": "7bb64706-6e46-4f94-a28a-4bc7caaab87d",
                "security_groups": [
                    "ef69bc60-2f4b-4f97-b95b-e3b68df0c0b2"
                ],
                "device_id": "e6c05704-c907-4cc1-8106-69b0996c43b9",
                "name": "port_vm_50_3",
                "admin_state_up": true,
                "network_id": "a54e1b19-ce78-4b7e-b28b-d2d716cdc161",
                "tenant_id": "6c9298ec8c874f7f99688489ab65f90e",
                "project_id": "3e4a1816927f405cacbc3dca1e05111e",
                "created_at": "2018-09-13T01: 43: 41",
                "updated_at": "2018-09-13T01: 43: 41",
                 "binding:vnic_type": "normal", 
                "binding:vnic_type": "normal",
                "mac_address": "fa:16:3e:f1:0b:09"
            }
        ]
    }
    ```


## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

