# Obtaining a VNC-based Remote Login Address \(Microversion 2.6 or Later\)<a name="EN-US_TOPIC_0142763126"></a>

## Function<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section16588975"></a>

This API is used to obtain the address for remotely logging in to an ECS using VNC.

## URI<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section15083054"></a>

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/remote-consoles

[Table 1](#en-us_topic_0092803065_table55945983)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0092803065_table55945983"></a>
<table><thead align="left"><tr id="en-us_topic_0092803065_row11302482"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0092803065_row49888896"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0092803065_p14468758"><a name="en-us_topic_0092803065_p14468758"></a><a name="en-us_topic_0092803065_p14468758"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0092803065_p31118786"><a name="en-us_topic_0092803065_p31118786"></a><a name="en-us_topic_0092803065_p31118786"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0092803065_row613736410235"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0092803065_p2736446410235"><a name="en-us_topic_0092803065_p2736446410235"></a><a name="en-us_topic_0092803065_p2736446410235"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0092803065_p192907210235"><a name="en-us_topic_0092803065_p192907210235"></a><a name="en-us_topic_0092803065_p192907210235"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0092803065_p2203711610235"><a name="en-us_topic_0092803065_p2203711610235"></a><a name="en-us_topic_0092803065_p2203711610235"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="en-us_topic_0092803065_section56676316111458"></a>

-   When using this API, ensure that the microversion is 2.6 or later.

    Add a microversion using the HTTP request header X-OpenStack-Nova-API-Version or OpenStack-API-Version.

    For example, X-OpenStack-Nova-API-Version: 2.6 or OpenStack-API-Version: compute 2.6

-   An obtained login address is valid for 10 minutes. Obtain a new one after expiration.

## Request<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section56802184"></a>

**Table  2**  Request parameters

<a name="table2421133916364"></a>
<table><thead align="left"><tr id="row15425153973610"><th class="cellrowborder" valign="top" width="17.23%" id="mcps1.2.5.1.1"><p id="p1542663953616"><a name="p1542663953616"></a><a name="p1542663953616"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.06%" id="mcps1.2.5.1.2"><p id="p16512193593516"><a name="p16512193593516"></a><a name="p16512193593516"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.88%" id="mcps1.2.5.1.3"><p id="p11427173918366"><a name="p11427173918366"></a><a name="p11427173918366"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.83%" id="mcps1.2.5.1.4"><p id="p1842973903611"><a name="p1842973903611"></a><a name="p1842973903611"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16430153914363"><td class="cellrowborder" valign="top" width="17.23%" headers="mcps1.2.5.1.1 "><p id="p498319273719"><a name="p498319273719"></a><a name="p498319273719"></a>remote_console</p>
</td>
<td class="cellrowborder" valign="top" width="17.06%" headers="mcps1.2.5.1.2 "><p id="p105121035103517"><a name="p105121035103517"></a><a name="p105121035103517"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.88%" headers="mcps1.2.5.1.3 "><p id="p898215212374"><a name="p898215212374"></a><a name="p898215212374"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.83%" headers="mcps1.2.5.1.4 "><p id="p9978132133714"><a name="p9978132133714"></a><a name="p9978132133714"></a>Obtains the address for remotely logging in to an ECS using VNC.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  remote\_console parameters

<a name="table19959184318164"></a>
<table><thead align="left"><tr id="row129653435167"><th class="cellrowborder" valign="top" width="17.05%" id="mcps1.2.5.1.1"><p id="p1296704318169"><a name="p1296704318169"></a><a name="p1296704318169"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.119999999999997%" id="mcps1.2.5.1.2"><p id="p1149238163514"><a name="p1149238163514"></a><a name="p1149238163514"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.04%" id="mcps1.2.5.1.3"><p id="p109701443181618"><a name="p109701443181618"></a><a name="p109701443181618"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.790000000000006%" id="mcps1.2.5.1.4"><p id="p597624311615"><a name="p597624311615"></a><a name="p597624311615"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row39781443181610"><td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.2.5.1.1 "><p id="p10980144310164"><a name="p10980144310164"></a><a name="p10980144310164"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p6149203820355"><a name="p6149203820355"></a><a name="p6149203820355"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.04%" headers="mcps1.2.5.1.3 "><p id="p189829437166"><a name="p189829437166"></a><a name="p189829437166"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.790000000000006%" headers="mcps1.2.5.1.4 "><p id="p1498612438166"><a name="p1498612438166"></a><a name="p1498612438166"></a>Specifies a remote login mode. Set it to <strong id="b84235270615195"><a name="b84235270615195"></a><a name="b84235270615195"></a>novnc</strong>.</p>
</td>
</tr>
<tr id="row11987144391610"><td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.2.5.1.1 "><p id="p2098904311617"><a name="p2098904311617"></a><a name="p2098904311617"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.5.1.2 "><p id="p614923863516"><a name="p614923863516"></a><a name="p614923863516"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.04%" headers="mcps1.2.5.1.3 "><p id="p599184312166"><a name="p599184312166"></a><a name="p599184312166"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.790000000000006%" headers="mcps1.2.5.1.4 "><p id="p599510433169"><a name="p599510433169"></a><a name="p599510433169"></a>Specifies a remote login protocol. Set it to <strong id="b842352706151929"><a name="b842352706151929"></a><a name="b842352706151929"></a>vnc</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section41457614"></a>

[Table 4](#table8420447171011)  describes the response parameters.

**Table  4**  Response parameters

<a name="table8420447171011"></a>
<table><thead align="left"><tr id="row19425134710106"><th class="cellrowborder" valign="top" width="21.15%" id="mcps1.2.4.1.1"><p id="p1542644714106"><a name="p1542644714106"></a><a name="p1542644714106"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.18%" id="mcps1.2.4.1.2"><p id="p2426104761014"><a name="p2426104761014"></a><a name="p2426104761014"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.67%" id="mcps1.2.4.1.3"><p id="p204289475101"><a name="p204289475101"></a><a name="p204289475101"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20429447201017"><td class="cellrowborder" valign="top" width="21.15%" headers="mcps1.2.4.1.1 "><p id="p743019477102"><a name="p743019477102"></a><a name="p743019477102"></a>remote_console</p>
</td>
<td class="cellrowborder" valign="top" width="13.18%" headers="mcps1.2.4.1.2 "><p id="p343116478104"><a name="p343116478104"></a><a name="p343116478104"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="65.67%" headers="mcps1.2.4.1.3 "><p id="p44331647131017"><a name="p44331647131017"></a><a name="p44331647131017"></a>Obtains the address for remotely logging in to an ECS.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **type**  parameters

<a name="table12434194718104"></a>
<table><thead align="left"><tr id="row11437194781018"><th class="cellrowborder" valign="top" width="21.34%" id="mcps1.2.4.1.1"><p id="p10438104701020"><a name="p10438104701020"></a><a name="p10438104701020"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.18%" id="mcps1.2.4.1.2"><p id="p644124714100"><a name="p644124714100"></a><a name="p644124714100"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.48%" id="mcps1.2.4.1.3"><p id="p1044224771012"><a name="p1044224771012"></a><a name="p1044224771012"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row44421547151015"><td class="cellrowborder" valign="top" width="21.34%" headers="mcps1.2.4.1.1 "><p id="p16443114712101"><a name="p16443114712101"></a><a name="p16443114712101"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="13.18%" headers="mcps1.2.4.1.2 "><p id="p154442475107"><a name="p154442475107"></a><a name="p154442475107"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.48%" headers="mcps1.2.4.1.3 "><p id="p13445747131013"><a name="p13445747131013"></a><a name="p13445747131013"></a>Specifies a remote login mode.</p>
</td>
</tr>
<tr id="row194475479107"><td class="cellrowborder" valign="top" width="21.34%" headers="mcps1.2.4.1.1 "><p id="p1044764712103"><a name="p1044764712103"></a><a name="p1044764712103"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="13.18%" headers="mcps1.2.4.1.2 "><p id="p20448447111014"><a name="p20448447111014"></a><a name="p20448447111014"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.48%" headers="mcps1.2.4.1.3 "><p id="p64491447131016"><a name="p64491447131016"></a><a name="p64491447131016"></a>Specifies a remote login protocol.</p>
</td>
</tr>
<tr id="row112741544151614"><td class="cellrowborder" valign="top" width="21.34%" headers="mcps1.2.4.1.1 "><p id="p627404410168"><a name="p627404410168"></a><a name="p627404410168"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="13.18%" headers="mcps1.2.4.1.2 "><p id="p92741044141612"><a name="p92741044141612"></a><a name="p92741044141612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.48%" headers="mcps1.2.4.1.3 "><p id="p10274544151617"><a name="p10274544151617"></a><a name="p10274544151617"></a>Specifies a remote login URL.</p>
<p id="p18426544113918"><a name="p18426544113918"></a><a name="p18426544113918"></a>The URL is valid for 10 minutes. Obtain a new one after expiration.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section37574207"></a>

```
POST https://{endpoint}/v2.1/13c67a214ced4afb88d911ae4bd5721a/servers/47bc79ae-df61-4ade-9197-283a74e5d70e/remote-consoles
```

```
{
   "remote_console" : {
        "type" : "novnc",
        "protocol": "vnc"
    }
}
```

## Example Response<a name="section1713910142558"></a>

```
{
	"remote_console": {
		"url": "https://nova-novncproxy.az21.dc1.domainname.com:8002/vnc.auto.html?token=80fa7c8d-37fe-451e-8b08-bfbd9fb6a4df&lang=EN",
		"type": "novnc",
		"protocol": "vnc"
	}
}
```

## Returned Values<a name="en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section23611955"></a>

See  [Error Code Description](error-code-description.md).

