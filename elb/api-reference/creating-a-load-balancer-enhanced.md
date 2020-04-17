# Creating a Load Balancer<a name="EN-US_TOPIC_0141008273"></a>

## Function<a name="en-us_topic_0096561535_en-us_topic_0049139634_section19714419"></a>

This API is used to create a private network load balancer. After the load balancer is created, its information is returned such as load balancer ID, IP address, and subnet ID.

To create a public network load balancer, you also need to call the API for assigning a floating IP address and associate this IP address to the port bound to the IP address of the private network load balancer.

## URI<a name="en-us_topic_0096561535_en-us_topic_0049139634_section43212049"></a>

POST /v2.0/lbaas/loadbalancers

## Request<a name="en-us_topic_0096561535_section196085184393"></a>

**Table  1**  Request parameters

<a name="en-us_topic_0096561535_table55596238165"></a>
<table><thead align="left"><tr id="en-us_topic_0096561535_row1356016236168"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="en-us_topic_0096561535_p185600235163"><a name="en-us_topic_0096561535_p185600235163"></a><a name="en-us_topic_0096561535_p185600235163"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.2"><p id="p146831131814"><a name="p146831131814"></a><a name="p146831131814"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="en-us_topic_0096561535_p1756052313165"><a name="en-us_topic_0096561535_p1756052313165"></a><a name="en-us_topic_0096561535_p1756052313165"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.5.1.4"><p id="en-us_topic_0096561535_p1856019234166"><a name="en-us_topic_0096561535_p1856019234166"></a><a name="en-us_topic_0096561535_p1856019234166"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561535_row155611323101620"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096561535_p1556182321620"><a name="en-us_topic_0096561535_p1556182321620"></a><a name="en-us_topic_0096561535_p1556182321620"></a>loadbalancer</p>
</td>
<td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.2 "><p id="p52614174114"><a name="p52614174114"></a><a name="p52614174114"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096561535_p656218233167"><a name="en-us_topic_0096561535_p656218233167"></a><a name="en-us_topic_0096561535_p656218233167"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096561535_p17562023141619"><a name="en-us_topic_0096561535_p17562023141619"></a><a name="en-us_topic_0096561535_p17562023141619"></a>Specifies the load balancer. For details, see <a href="#en-us_topic_0096561535_table1673416344910">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **loadbalancer**  parameter description

<a name="en-us_topic_0096561535_table1673416344910"></a>
<table><thead align="left"><tr id="en-us_topic_0096561535_row49121038493"><th class="cellrowborder" valign="top" width="22.36%" id="mcps1.2.5.1.1"><p id="en-us_topic_0096561535_p7913332497"><a name="en-us_topic_0096561535_p7913332497"></a><a name="en-us_topic_0096561535_p7913332497"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="10.74%" id="mcps1.2.5.1.2"><p id="en-us_topic_0096561535_p191314384918"><a name="en-us_topic_0096561535_p191314384918"></a><a name="en-us_topic_0096561535_p191314384918"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.3%" id="mcps1.2.5.1.3"><p id="en-us_topic_0096561535_p99131033494"><a name="en-us_topic_0096561535_p99131033494"></a><a name="en-us_topic_0096561535_p99131033494"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.6%" id="mcps1.2.5.1.4"><p id="en-us_topic_0096561535_p159131317492"><a name="en-us_topic_0096561535_p159131317492"></a><a name="en-us_topic_0096561535_p159131317492"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561535_row159131033490"><td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096561535_p69131434493"><a name="en-us_topic_0096561535_p69131434493"></a><a name="en-us_topic_0096561535_p69131434493"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="10.74%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096561535_p1091317364912"><a name="en-us_topic_0096561535_p1091317364912"></a><a name="en-us_topic_0096561535_p1091317364912"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096561535_p119131138496"><a name="en-us_topic_0096561535_p119131138496"></a><a name="en-us_topic_0096561535_p119131138496"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.6%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096561535_p12913113114915"><a name="en-us_topic_0096561535_p12913113114915"></a><a name="en-us_topic_0096561535_p12913113114915"></a>Specifies the load balancer name.</p>
<p id="p17232144005213"><a name="p17232144005213"></a><a name="p17232144005213"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561535_row8913335494"><td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096561535_p189132374911"><a name="en-us_topic_0096561535_p189132374911"></a><a name="en-us_topic_0096561535_p189132374911"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="10.74%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096561535_p1291310313496"><a name="en-us_topic_0096561535_p1291310313496"></a><a name="en-us_topic_0096561535_p1291310313496"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096561535_p12913113104913"><a name="en-us_topic_0096561535_p12913113104913"></a><a name="en-us_topic_0096561535_p12913113104913"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.6%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0096561535_p179136317491"><a name="en-us_topic_0096561535_p179136317491"></a><a name="en-us_topic_0096561535_p179136317491"></a>Provides supplementary information about the load balancer.</p>
<p id="p1090416424528"><a name="p1090416424528"></a><a name="p1090416424528"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561535_row991310311495"><td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096561535_p20913630492"><a name="en-us_topic_0096561535_p20913630492"></a><a name="en-us_topic_0096561535_p20913630492"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.74%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096561535_p119131831490"><a name="en-us_topic_0096561535_p119131831490"></a><a name="en-us_topic_0096561535_p119131831490"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096561535_p491323104910"><a name="en-us_topic_0096561535_p491323104910"></a><a name="en-us_topic_0096561535_p491323104910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.6%" headers="mcps1.2.5.1.4 "><p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a>Specifies the ID of the project where the load balancer is used. </p>
<p id="p5446154655214"><a name="p5446154655214"></a><a name="p5446154655214"></a>The value contains a maximum of 255 characters.</p>
<p id="p145223511764"><a name="p145223511764"></a><a name="p145223511764"></a>The value must be the same as the value of <strong id="b116321851795"><a name="b116321851795"></a><a name="b116321851795"></a>project_id</strong> in the token.</p>
</td>
</tr>
<tr id="en-us_topic_0096561535_row119132334911"><td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096561535_p13913193114915"><a name="en-us_topic_0096561535_p13913193114915"></a><a name="en-us_topic_0096561535_p13913193114915"></a>vip_subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.74%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096561535_p891303184910"><a name="en-us_topic_0096561535_p891303184910"></a><a name="en-us_topic_0096561535_p891303184910"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096561535_p791363114916"><a name="en-us_topic_0096561535_p791363114916"></a><a name="en-us_topic_0096561535_p791363114916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.6%" headers="mcps1.2.5.1.4 "><p id="p153041351121318"><a name="p153041351121318"></a><a name="p153041351121318"></a>Specifies the ID of the subnet where the load balancer works. You can obtain the value by calling the API for querying subnets {VPC endpoint}/v2.0/subnets} using the GET method.</p>
<p id="p1898095613614"><a name="p1898095613614"></a><a name="p1898095613614"></a>The private IP address of the load balancer is in this subnet.</p>
<p id="p137488581464"><a name="p137488581464"></a><a name="p137488581464"></a>Only IPv4 subnets are supported.</p>
</td>
</tr>
<tr id="en-us_topic_0096561535_row191493134915"><td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096561535_p291463114917"><a name="en-us_topic_0096561535_p291463114917"></a><a name="en-us_topic_0096561535_p291463114917"></a>provider</p>
</td>
<td class="cellrowborder" valign="top" width="10.74%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096561535_p89543183618"><a name="en-us_topic_0096561535_p89543183618"></a><a name="en-us_topic_0096561535_p89543183618"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096561535_p209149319494"><a name="en-us_topic_0096561535_p209149319494"></a><a name="en-us_topic_0096561535_p209149319494"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.6%" headers="mcps1.2.5.1.4 "><p id="p533933310712"><a name="p533933310712"></a><a name="p533933310712"></a>Specifies the provider of the load balancer.</p>
<p id="p152810351271"><a name="p152810351271"></a><a name="p152810351271"></a>The value can only be <strong id="b842352706164927"><a name="b842352706164927"></a><a name="b842352706164927"></a>vlb</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561535_row149144312495"><td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096561535_p1091411394915"><a name="en-us_topic_0096561535_p1091411394915"></a><a name="en-us_topic_0096561535_p1091411394915"></a>vip_address</p>
</td>
<td class="cellrowborder" valign="top" width="10.74%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096561535_p2091423174912"><a name="en-us_topic_0096561535_p2091423174912"></a><a name="en-us_topic_0096561535_p2091423174912"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096561535_p139147311492"><a name="en-us_topic_0096561535_p139147311492"></a><a name="en-us_topic_0096561535_p139147311492"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.6%" headers="mcps1.2.5.1.4 "><p id="p076173714711"><a name="p076173714711"></a><a name="p076173714711"></a>Specifies the private IP address of the load balancer.</p>
<p id="p1386043115916"><a name="p1386043115916"></a><a name="p1386043115916"></a>This IP address must be the one in the subnet specified by <strong id="b842352706165031"><a name="b842352706165031"></a><a name="b842352706165031"></a>vip_subnet_id</strong>. If this parameter is not specified, an IP address is automatically assigned to the load balancer from the subnet specified by <strong id="b842352706165352"><a name="b842352706165352"></a><a name="b842352706165352"></a>vip_subnet_id</strong>.</p>
<p id="p1829311695315"><a name="p1829311695315"></a><a name="p1829311695315"></a>The value contains a maximum of 64 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561535_row159141239494"><td class="cellrowborder" valign="top" width="22.36%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0096561535_p89147319494"><a name="en-us_topic_0096561535_p89147319494"></a><a name="en-us_topic_0096561535_p89147319494"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="10.74%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0096561535_p6295202120618"><a name="en-us_topic_0096561535_p6295202120618"></a><a name="en-us_topic_0096561535_p6295202120618"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096561535_p2091483104914"><a name="en-us_topic_0096561535_p2091483104914"></a><a name="en-us_topic_0096561535_p2091483104914"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="50.6%" headers="mcps1.2.5.1.4 "><p id="p10692193313917"><a name="p10692193313917"></a><a name="p10692193313917"></a>Specifies the administrative status of the load balancer.</p>
<p id="p18576435690"><a name="p18576435690"></a><a name="p18576435690"></a>This parameter is reserved. The default value is <strong id="b182023172152"><a name="b182023172152"></a><a name="b182023172152"></a>true</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0096561535_section14610958143910"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0096561535_table10636133131611"></a>
<table><thead align="left"><tr id="en-us_topic_0096561535_row6637113381614"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561535_p763763315165"><a name="en-us_topic_0096561535_p763763315165"></a><a name="en-us_topic_0096561535_p763763315165"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.61%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561535_p363733310161"><a name="en-us_topic_0096561535_p363733310161"></a><a name="en-us_topic_0096561535_p363733310161"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561535_p1637733201614"><a name="en-us_topic_0096561535_p1637733201614"></a><a name="en-us_topic_0096561535_p1637733201614"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561535_row26373338166"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561535_p166371933191614"><a name="en-us_topic_0096561535_p166371933191614"></a><a name="en-us_topic_0096561535_p166371933191614"></a>loadbalancer</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561535_p563833361611"><a name="en-us_topic_0096561535_p563833361611"></a><a name="en-us_topic_0096561535_p563833361611"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561535_p3638153321619"><a name="en-us_topic_0096561535_p3638153321619"></a><a name="en-us_topic_0096561535_p3638153321619"></a>Specifies the load balancer. For details, see <a href="#en-us_topic_0096561535_table1857116262516">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **loadbalancer**  parameter description

<a name="en-us_topic_0096561535_table1857116262516"></a>
<table><thead align="left"><tr id="en-us_topic_0141008271_en-us_topic_0096561532_row6659133533816"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.1"><p id="en-us_topic_0141008271_en-us_topic_0096561532_p96591835173819"><a name="en-us_topic_0141008271_en-us_topic_0096561532_p96591835173819"></a><a name="en-us_topic_0141008271_en-us_topic_0096561532_p96591835173819"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="en-us_topic_0141008271_en-us_topic_0096561532_p17660123513386"><a name="en-us_topic_0141008271_en-us_topic_0096561532_p17660123513386"></a><a name="en-us_topic_0141008271_en-us_topic_0096561532_p17660123513386"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.2.4.1.3"><p id="en-us_topic_0141008271_en-us_topic_0096561532_p4660183515387"><a name="en-us_topic_0141008271_en-us_topic_0096561532_p4660183515387"></a><a name="en-us_topic_0141008271_en-us_topic_0096561532_p4660183515387"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0141008271_en-us_topic_0096561532_row156601235133818"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p10415829113311"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p10415829113311"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p10415829113311"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_p155784252919"><a name="en-us_topic_0141008271_p155784252919"></a><a name="en-us_topic_0141008271_p155784252919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1941513297339"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1941513297339"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1941513297339"></a>Specifies the load balancer ID.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_row1758616126181"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p20415229113312"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p20415229113312"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p20415229113312"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p741592933318"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p741592933318"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p741592933318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1341519295331"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1341519295331"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1341519295331"></a>Specifies the ID of the project where the load balancer is used.</p>
<p id="en-us_topic_0141008271_p77281547155311"><a name="en-us_topic_0141008271_p77281547155311"></a><a name="en-us_topic_0141008271_p77281547155311"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row76601535193815"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1041552912332"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1041552912332"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1041552912332"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p241692918331"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p241692918331"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p241692918331"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p17416152919332"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p17416152919332"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p17416152919332"></a>Specifies the load balancer name.</p>
<p id="en-us_topic_0141008271_p076212535532"><a name="en-us_topic_0141008271_p076212535532"></a><a name="en-us_topic_0141008271_p076212535532"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row66605355385"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p4416102918335"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p4416102918335"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p4416102918335"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p24161129143314"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p24161129143314"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p24161129143314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p5416142912334"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p5416142912334"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p5416142912334"></a>Provides supplementary information about the load balancer.</p>
<p id="en-us_topic_0141008271_p157105551532"><a name="en-us_topic_0141008271_p157105551532"></a><a name="en-us_topic_0141008271_p157105551532"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row1166020352385"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1541618299335"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1541618299335"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1541618299335"></a>vip_subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_p135272044182910"><a name="en-us_topic_0141008271_p135272044182910"></a><a name="en-us_topic_0141008271_p135272044182910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_p4335125124117"><a name="en-us_topic_0141008271_p4335125124117"></a><a name="en-us_topic_0141008271_p4335125124117"></a>Specifies the ID of the subnet where the load balancer works.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row36601435103818"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1041622923320"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1041622923320"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1041622923320"></a>vip_port_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_p19102164614291"><a name="en-us_topic_0141008271_p19102164614291"></a><a name="en-us_topic_0141008271_p19102164614291"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_p173334177415"><a name="en-us_topic_0141008271_p173334177415"></a><a name="en-us_topic_0141008271_p173334177415"></a>Specifies the ID of the port bound to the private IP address of the load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row1866173519389"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p174164295334"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p174164295334"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p174164295334"></a>provider</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p541611290339"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p541611290339"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p541611290339"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_p43391417194120"><a name="en-us_topic_0141008271_p43391417194120"></a><a name="en-us_topic_0141008271_p43391417194120"></a>Specifies the provider of the load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row6661203510387"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1416829143318"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1416829143318"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1416829143318"></a>vip_address</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p341672912338"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p341672912338"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p341672912338"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p64178297334"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p64178297334"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p64178297334"></a>Specifies the private IP address of the load balancer.</p>
<p id="en-us_topic_0141008271_p832917316544"><a name="en-us_topic_0141008271_p832917316544"></a><a name="en-us_topic_0141008271_p832917316544"></a>The value contains a maximum of 64 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row16611235163814"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1841715293336"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1841715293336"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1841715293336"></a>listeners</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_p10662124818106"><a name="en-us_topic_0141008271_p10662124818106"></a><a name="en-us_topic_0141008271_p10662124818106"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p7417112963311"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p7417112963311"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p7417112963311"></a>Lists the IDs of listeners added to the load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row8661143513384"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1441712910330"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1441712910330"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1441712910330"></a>pools</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_p563318509102"><a name="en-us_topic_0141008271_p563318509102"></a><a name="en-us_topic_0141008271_p563318509102"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p104171229123313"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p104171229123313"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p104171229123313"></a>Lists the IDs of backend server groups associated with the load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row566114352387"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_p727217358477"><a name="en-us_topic_0141008271_p727217358477"></a><a name="en-us_topic_0141008271_p727217358477"></a>operating_status</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_p82761735124717"><a name="en-us_topic_0141008271_p82761735124717"></a><a name="en-us_topic_0141008271_p82761735124717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_p9800291619"><a name="en-us_topic_0141008271_p9800291619"></a><a name="en-us_topic_0141008271_p9800291619"></a>Specifies the operating status of the load balancer.</p>
<p id="en-us_topic_0141008271_p75131031164"><a name="en-us_topic_0141008271_p75131031164"></a><a name="en-us_topic_0141008271_p75131031164"></a>The value can be <strong id="en-us_topic_0141008271_b842352706165847"><a name="en-us_topic_0141008271_b842352706165847"></a><a name="en-us_topic_0141008271_b842352706165847"></a>ONLINE</strong>, <strong id="en-us_topic_0141008271_b842352706165850"><a name="en-us_topic_0141008271_b842352706165850"></a><a name="en-us_topic_0141008271_b842352706165850"></a>OFFLINE</strong>, <strong id="en-us_topic_0141008271_b842352706165852"><a name="en-us_topic_0141008271_b842352706165852"></a><a name="en-us_topic_0141008271_b842352706165852"></a>DEGRADED</strong>, <strong id="en-us_topic_0141008271_b842352706165855"><a name="en-us_topic_0141008271_b842352706165855"></a><a name="en-us_topic_0141008271_b842352706165855"></a>DISABLED</strong>, or <strong id="en-us_topic_0141008271_b842352706165859"><a name="en-us_topic_0141008271_b842352706165859"></a><a name="en-us_topic_0141008271_b842352706165859"></a>NO_MONITOR</strong>.</p>
<p id="en-us_topic_0141008271_p58611733561"><a name="en-us_topic_0141008271_p58611733561"></a><a name="en-us_topic_0141008271_p58611733561"></a>This parameter is reserved. The default value is <strong id="en-us_topic_0141008271_b842352706145855"><a name="en-us_topic_0141008271_b842352706145855"></a><a name="en-us_topic_0141008271_b842352706145855"></a>ONLINE</strong>.</p>
<p id="en-us_topic_0141008271_p71718156545"><a name="en-us_topic_0141008271_p71718156545"></a><a name="en-us_topic_0141008271_p71718156545"></a>The value contains a maximum of 16 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row2661123514384"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_p930113351475"><a name="en-us_topic_0141008271_p930113351475"></a><a name="en-us_topic_0141008271_p930113351475"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_p7305153534717"><a name="en-us_topic_0141008271_p7305153534717"></a><a name="en-us_topic_0141008271_p7305153534717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_p4255836060"><a name="en-us_topic_0141008271_p4255836060"></a><a name="en-us_topic_0141008271_p4255836060"></a>Specifies the provisioning status of the load balancer.</p>
<p id="en-us_topic_0141008271_p9469138261"><a name="en-us_topic_0141008271_p9469138261"></a><a name="en-us_topic_0141008271_p9469138261"></a>The value can be <strong id="en-us_topic_0141008271_b842352706165943"><a name="en-us_topic_0141008271_b842352706165943"></a><a name="en-us_topic_0141008271_b842352706165943"></a>ACTIVE</strong>, <strong id="en-us_topic_0141008271_b842352706165947"><a name="en-us_topic_0141008271_b842352706165947"></a><a name="en-us_topic_0141008271_b842352706165947"></a>PENDING_CREATE</strong>, or <strong id="en-us_topic_0141008271_b842352706165951"><a name="en-us_topic_0141008271_b842352706165951"></a><a name="en-us_topic_0141008271_b842352706165951"></a>ERROR</strong>.</p>
<p id="en-us_topic_0141008271_p15614144018617"><a name="en-us_topic_0141008271_p15614144018617"></a><a name="en-us_topic_0141008271_p15614144018617"></a>This parameter is reserved. The default value is <strong id="en-us_topic_0141008271_b1402670288"><a name="en-us_topic_0141008271_b1402670288"></a><a name="en-us_topic_0141008271_b1402670288"></a>ACTIVE</strong>.</p>
<p id="en-us_topic_0141008271_p18722348205910"><a name="en-us_topic_0141008271_p18722348205910"></a><a name="en-us_topic_0141008271_p18722348205910"></a>The value contains a maximum of 16 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row16662935103816"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p114181329133314"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p114181329133314"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p114181329133314"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p10418172913319"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p10418172913319"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p10418172913319"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_p14847443611"><a name="en-us_topic_0141008271_p14847443611"></a><a name="en-us_topic_0141008271_p14847443611"></a>Specifies the administrative status of the load balancer.</p>
<p id="en-us_topic_0141008271_p114911046864"><a name="en-us_topic_0141008271_p114911046864"></a><a name="en-us_topic_0141008271_p114911046864"></a>This parameter is reserved. The default value is <strong id="en-us_topic_0141008271_b1291373994"><a name="en-us_topic_0141008271_b1291373994"></a><a name="en-us_topic_0141008271_b1291373994"></a>true</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row866215358384"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p74181229133310"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p74181229133310"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p74181229133310"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_p71551954161018"><a name="en-us_topic_0141008271_p71551954161018"></a><a name="en-us_topic_0141008271_p71551954161018"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p4418112919333"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p4418112919333"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p4418112919333"></a>Lists load balancer tags.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row13900164817511"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p18781627124910"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p18781627124910"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p18781627124910"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p18781627204916"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p18781627204916"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p18781627204916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p578162719490"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p578162719490"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p578162719490"></a>Specifies the time when the load balancer was created.</p>
<p id="en-us_topic_0141008271_p3462240292"><a name="en-us_topic_0141008271_p3462240292"></a><a name="en-us_topic_0141008271_p3462240292"></a>The UTC time is in <em id="en-us_topic_0141008271_i155506367247"><a name="en-us_topic_0141008271_i155506367247"></a><a name="en-us_topic_0141008271_i155506367247"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
<p id="en-us_topic_0141008271_p415795413546"><a name="en-us_topic_0141008271_p415795413546"></a><a name="en-us_topic_0141008271_p415795413546"></a>The value contains a maximum of 19 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0141008271_en-us_topic_0096561532_row4521952195114"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1541843114495"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1541843114495"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1541843114495"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p1810172112506"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1810172112506"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p1810172112506"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0141008271_en-us_topic_0096561531_p341843144919"><a name="en-us_topic_0141008271_en-us_topic_0096561531_p341843144919"></a><a name="en-us_topic_0141008271_en-us_topic_0096561531_p341843144919"></a>Specifies the time when the load balancer was updated.</p>
<p id="en-us_topic_0141008271_p52901417154816"><a name="en-us_topic_0141008271_p52901417154816"></a><a name="en-us_topic_0141008271_p52901417154816"></a>The UTC time is in <em id="en-us_topic_0141008271_i185028407247"><a name="en-us_topic_0141008271_i185028407247"></a><a name="en-us_topic_0141008271_i185028407247"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
<p id="en-us_topic_0141008271_p3844185817544"><a name="en-us_topic_0141008271_p3844185817544"></a><a name="en-us_topic_0141008271_p3844185817544"></a>The value contains a maximum of 19 characters.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section9687843171917"></a>

-   Example request 1: Creating a private network load balancer

    ```
    POST https://{Endpoint}/v2.0/lbaas/loadbalancers 
    
    { 
        "loadbalancer": { 
            "name": "loadbalancer1", 
            "description": "simple lb", 
            "tenant_id": "1867112d054b427e808cc6096d8193a1", 
            "vip_subnet_id": "58077bdb-d470-424b-8c45-2e3c65060a5b", 
            "vip_address": "192.168.0.100", 
            "admin_state_up": true 
        } 
    }
    ```


-   <a name="li170912435191"></a>Example response 1

    ```
    {
        "loadbalancer": {
            "description": "simple lb",
            "provisioning_status": "ACTIVE",
            "tenant_id": "1867112d054b427e808cc6096d8193a1",
            "created_at": "2019-01-19T05:32:56",
            "admin_state_up": true,
            "updated_at": "2019-01-19T05:32:57",
            "id": "ea2843da-4026-49ec-8338-8fa015b067fc",
            "pools": [],
            "listeners": [],
            "vip_port_id": "a7ecbdb5-5a63-41dd-a830-e16c0a7e04a7",
            "operating_status": "ONLINE",
            "vip_address": "192.168.0.100",
            "vip_subnet_id": "58077bdb-d470-424b-8c45-2e3c65060a5b",
            "provider": "vlb",
            "tags": [],
            "name": "loadbalancer1"
        }
    }
    ```

-   Example request 2: Creating a public network load balancer

    \(Bind an EIP to the port that has been bound to the load balancer's private IP address.For details about the parameters, see  [Table 5](#table98531817181218).\)

    **Table  5**  Request parameters

    <a name="table98531817181218"></a>
    <table><thead align="left"><tr id="row1685771713127"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.1"><p id="p15988448151043"><a name="p15988448151043"></a><a name="p15988448151043"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="p19995902151043"><a name="p19995902151043"></a><a name="p19995902151043"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p9055369151043"><a name="p9055369151043"></a><a name="p9055369151043"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51%" id="mcps1.2.5.1.4"><p id="p62396264151043"><a name="p62396264151043"></a><a name="p62396264151043"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2858141715122"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p17819972151043"><a name="p17819972151043"></a><a name="p17819972151043"></a>publicip</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p34131600151043"><a name="p34131600151043"></a><a name="p34131600151043"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p13196241151043"><a name="p13196241151043"></a><a name="p13196241151043"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><p id="p23492844151043"><a name="p23492844151043"></a><a name="p23492844151043"></a>Specifies the EIP objects. For details, see <a href="#table8139247714">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row185144527123"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p24675975151050"><a name="p24675975151050"></a><a name="p24675975151050"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p52596998151050"><a name="p52596998151050"></a><a name="p52596998151050"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p12429959151120"><a name="p12429959151120"></a><a name="p12429959151120"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><p id="p1744019151120"><a name="p1744019151120"></a><a name="p1744019151120"></a>Specifies the bandwidth objects. For details, see <a href="#table4629141212214">Table 7</a>.</p>
    </td>
    </tr>
    <tr id="row271555171214"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p19564181313543"><a name="p19564181313543"></a><a name="p19564181313543"></a>enterprise_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p13564413185412"><a name="p13564413185412"></a><a name="p13564413185412"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p95641133547"><a name="p95641133547"></a><a name="p95641133547"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><a name="ul16411048123"></a><a name="ul16411048123"></a><ul id="ul16411048123"><li>Specifies the enterprise project ID. The value can contain a maximum of 36 characters. It is string <strong id="b1815319813395"><a name="b1815319813395"></a><a name="b1815319813395"></a>"0"</strong> or in UUID format with hyphens (-).</li><li>When assigning an EIP, you need to bind an enterprise project ID to the EIP.</li><li>If this parameter is not specified, the default value is <strong id="b77601111203917"><a name="b77601111203917"></a><a name="b77601111203917"></a>0</strong>.</li></ul>
    <div class="note" id="note16336122416016"><a name="note16336122416016"></a><a name="note16336122416016"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p89770612438"><a name="p89770612438"></a><a name="p89770612438"></a>For more information about enterprise projects and how to obtain enterprise project IDs, see <em id="i19933320203912"><a name="i19933320203912"></a><a name="i19933320203912"></a>Enterprise Management User Guide</em>.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **publicip**  parameter description

    <a name="table8139247714"></a>
    <table><thead align="left"><tr id="row18132240714"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="p101201250870"><a name="p101201250870"></a><a name="p101201250870"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p18557165561911"><a name="p18557165561911"></a><a name="p18557165561911"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p161211850674"><a name="p161211850674"></a><a name="p161211850674"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51%" id="mcps1.2.5.1.4"><p id="p41217502719"><a name="p41217502719"></a><a name="p41217502719"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2014192410713"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p30749271"><a name="p30749271"></a><a name="p30749271"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p7663035"><a name="p7663035"></a><a name="p7663035"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p70444218129"><a name="p70444218129"></a><a name="p70444218129"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><a name="ul29589093174724"></a><a name="ul29589093174724"></a><ul id="ul29589093174724"><li>Specifies the EIP type.</li><li>Note:<a name="ul9738153015499"></a><a name="ul9738153015499"></a><ul id="ul9738153015499"><li>The configured value must be supported by the system.</li><li><strong id="b659893819404"><a name="b659893819404"></a><a name="b659893819404"></a>publicip_id</strong> is an IPv4 port. If <strong id="b859863854013"><a name="b859863854013"></a><a name="b859863854013"></a>publicip_type</strong> is not specified, the default value is <strong id="b1859983864020"><a name="b1859983864020"></a><a name="b1859983864020"></a>5_bgp</strong>.</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row4141241070"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p1661484872917"><a name="p1661484872917"></a><a name="p1661484872917"></a>ip_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p1861404882912"><a name="p1861404882912"></a><a name="p1861404882912"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p111532059555"><a name="p111532059555"></a><a name="p111532059555"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><a name="ul1842191914615"></a><a name="ul1842191914615"></a><ul id="ul1842191914615"><li>Specifies the EIP version.</li><li>The value can be <strong id="b10731154213401"><a name="b10731154213401"></a><a name="b10731154213401"></a>4</strong> and <strong id="b17732242184012"><a name="b17732242184012"></a><a name="b17732242184012"></a>6</strong>. <strong id="b776019154111"><a name="b776019154111"></a><a name="b776019154111"></a>4</strong> indicates IPv4 addresses, and <strong id="b13781931911"><a name="b13781931911"></a><a name="b13781931911"></a>6</strong> indicates IPv6 addresses.</li><li>Note:<a name="ul1190139775"></a><a name="ul1190139775"></a><ul id="ul1190139775"><li>The configured value must be supported by the system.</li><li>If this parameter is left blank or is an empty string, IPv4 address is assigned by default.</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row614132416712"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p0818123182013"><a name="p0818123182013"></a><a name="p0818123182013"></a>ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p481853132016"><a name="p481853132016"></a><a name="p481853132016"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p1781813117205"><a name="p1781813117205"></a><a name="p1781813117205"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><a name="ul178181631102013"></a><a name="ul178181631102013"></a><ul id="ul178181631102013"><li>Specifies the EIP to be assigned. The system automatically assigns an EIP if you do not specify it.</li><li>The value must be a valid IPv4 address in the available IP address range.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **bandwidth**  parameter description

    <a name="table4629141212214"></a>
    <table><thead align="left"><tr id="row963021219220"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="p17630912102219"><a name="p17630912102219"></a><a name="p17630912102219"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p1630612182220"><a name="p1630612182220"></a><a name="p1630612182220"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p5630141282212"><a name="p5630141282212"></a><a name="p5630141282212"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="p10630121232212"><a name="p10630121232212"></a><a name="p10630121232212"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10630101292211"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p7414170"><a name="p7414170"></a><a name="p7414170"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p63676932"><a name="p63676932"></a><a name="p63676932"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p4516535118155"><a name="p4516535118155"></a><a name="p4516535118155"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><a name="ul518119181073"></a><a name="ul518119181073"></a><ul id="ul518119181073"><li>Specifies the bandwidth name.</li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li><li>This parameter is mandatory when <strong id="b276165742195527"><a name="b276165742195527"></a><a name="b276165742195527"></a>share_type</strong> is set to <strong id="b1379441107195527"><a name="b1379441107195527"></a><a name="b1379441107195527"></a>PER</strong>. This parameter will be ignored when <strong id="b1701699234195527"><a name="b1701699234195527"></a><a name="b1701699234195527"></a>share_type</strong> is set to <strong id="b1218397550195527"><a name="b1218397550195527"></a><a name="b1218397550195527"></a>WHOLE</strong> with an ID specified.</li></ul>
    </td>
    </tr>
    <tr id="row1063341212214"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p2537905"><a name="p2537905"></a><a name="p2537905"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p4243749"><a name="p4243749"></a><a name="p4243749"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p3451484018155"><a name="p3451484018155"></a><a name="p3451484018155"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><a name="ul194366475712"></a><a name="ul194366475712"></a><ul id="ul194366475712"><li>Specifies the bandwidth (Mbit/s).</li><li>The value ranges from <strong id="b115343238316"><a name="b115343238316"></a><a name="b115343238316"></a>1</strong> to <strong id="b851042619315"><a name="b851042619315"></a><a name="b851042619315"></a>1000</strong> by default. (The range may vary depending on the configuration in each region. You can see the bandwidth range of each region on the management console.)</li><li>This parameter is mandatory when <strong id="b783895606"><a name="b783895606"></a><a name="b783895606"></a>share_type</strong> is set to <strong id="b224405373"><a name="b224405373"></a><a name="b224405373"></a>PER</strong>. This parameter will be ignored when <strong id="b1262772117"><a name="b1262772117"></a><a name="b1262772117"></a>share_type</strong> is set to <strong id="b1782763574"><a name="b1782763574"></a><a name="b1782763574"></a>WHOLE</strong> with an ID specified.</li><li>The minimum unit for bandwidth adjustment varies depending on the bandwidth range. The details are as follows:<a name="ul9790510185"></a><a name="ul9790510185"></a><ul id="ul9790510185"><li>The minimum increment is 1 Mbit/s if the allowed bandwidth ranges from 0 to 300 Mbit/s (with 300 Mbit/s included).</li><li>The minimum increment is 50 Mbit/s if the allowed bandwidth ranges 300 Mbit/s to 1000 Mbit/s (with 1000 Mbit/s included).</li><li>The minimum increment is 500 Mbit/s if the allowed bandwidth is greater than 1000 Mbit/s.</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row1063512126226"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p61660876"><a name="p61660876"></a><a name="p61660876"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p28475059"><a name="p28475059"></a><a name="p28475059"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p4423869418155"><a name="p4423869418155"></a><a name="p4423869418155"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><a name="ul569842518819"></a><a name="ul569842518819"></a><ul id="ul569842518819"><li>Specifies the bandwidth ID. You can specify an existing shared bandwidth when assigning an EIP.</li><li>The value can be the ID of the shared bandwidth whose type is set to <strong id="b174150368419"><a name="b174150368419"></a><a name="b174150368419"></a>WHOLE</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row9850204292213"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p40656116"><a name="p40656116"></a><a name="p40656116"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p4811061"><a name="p4811061"></a><a name="p4811061"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p2656447218155"><a name="p2656447218155"></a><a name="p2656447218155"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><a name="ul2255712095"></a><a name="ul2255712095"></a><ul id="ul2255712095"><li>Specifies the bandwidth type.</li><li>The value is <strong id="b25288513165924"><a name="b25288513165924"></a><a name="b25288513165924"></a>PER</strong>, indicating that the bandwidth is dedicated.</li></ul>
    </td>
    </tr>
    <tr id="row143946112220"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p27426113172319"><a name="p27426113172319"></a><a name="p27426113172319"></a>charge_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p55776100172330"><a name="p55776100172330"></a><a name="p55776100172330"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p23864764172319"><a name="p23864764172319"></a><a name="p23864764172319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><a name="ul152417331215"></a><a name="ul152417331215"></a><ul id="ul152417331215"><li>If the value is <strong id="b842352706173820"><a name="b842352706173820"></a><a name="b842352706173820"></a>traffic</strong>, the bandwidth is billed by traffic.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    -   Step1: Apply for an EIP.

        ```
        POST https://{VPCEndpoint}/v1/8b7e35ad379141fc9df3e178bd64f55c/publicips
        
        {
            "publicip": {
                "type": "5_bgp",
                "ip_version": 4
            },
            "bandwidth": {
                "name": "bandwidth123",
                "size": 10,
                "share_type": "PER"
            }
        }
        ```

    -   <a name="li11904132299"></a>Example response

        ```
        {
            "publicip": {
                "id": "f588ccfa-8750-4d7c-bf5d-2ede24414706",
                "status": "PENDING_CREATE",
                "type": "5_bgp",
                "public_ip_address": "139.9.204.183",
                "tenant_id": "8b7e35ad379141fc9df3e178bd64f55c",
                "ip_version": 4,
                "create_time": "2019-06-29 06:45:32",
                "bandwidth_size": 1
                
            }
        }
        ```

    -   Step 2: Bind the EIP. \(The value of  **public\_id**  is the same as that in the  [▪ Example response](#li11904132299), and the value of  **port\_id**  is the same as that of  **vip\_port\_id**  in  [Example response 1](#li170912435191).\)

        ```
        PUT /v1/8b7e35ad379141fc9df3e178bd64f55c/publicips/f588ccfa-8750-4d7c-bf5d-2ede24414706
        
        {
            "publicip": {
                "port_id": "a7ecbdb5-5a63-41dd-a830-e16c0a7e04a7"
            }
        }
        ```

    -   Example response

        ```
        {
          "publicip": {
            "id": "f588ccfa-8750-4d7c-bf5d-2ede24414706",
            "status": "ACTIVE",
            "type": "5_bgp",
            "port_id": "a7ecbdb5-5a63-41dd-a830-e16c0a7e04a7",
            "public_ip_address": "139.9.204.183",
            "private_ip_address": "192.168.1.131",
            "tenant_id": "8b7e35ad379141fc9df3e178bd64f55c",
            "create_time": "2019-06-29 07:33:18",
            "bandwidth_size": 1,
            "ip_version": 4
          }
        }
        ```

    -   After the preceding steps are complete, the load balancer has the capability of accessing the public network. You can access the load balancer using 139.9.204.183, the value of parameter  **floating\_ip\_address**.


## Status Code<a name="en-us_topic_0096561535_en-us_topic_0049139632_section15511864"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

