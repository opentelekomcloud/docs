# Common Request Parameters<a name="css_03_0015"></a>

[Table 1](#table181671338175614)  describes the common request parameters.

**Table  1**  Common request headers

<a name="table181671338175614"></a>
<table><thead align="left"><tr id="row101671738165610"><th class="cellrowborder" valign="top" width="21.63%" id="mcps1.2.4.1.1"><p id="p71671738165620"><a name="p71671738165620"></a><a name="p71671738165620"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="30.36%" id="mcps1.2.4.1.2"><p id="p14168193875620"><a name="p14168193875620"></a><a name="p14168193875620"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="48.010000000000005%" id="mcps1.2.4.1.3"><p id="p18168113813566"><a name="p18168113813566"></a><a name="p18168113813566"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1116873818569"><td class="cellrowborder" valign="top" width="21.63%" headers="mcps1.2.4.1.1 "><p id="p1168338205612"><a name="p1168338205612"></a><a name="p1168338205612"></a>X-Sdk-Date</p>
</td>
<td class="cellrowborder" valign="top" width="30.36%" headers="mcps1.2.4.1.2 "><p id="p31687389562"><a name="p31687389562"></a><a name="p31687389562"></a>This parameter is mandatory for authentication using AK/SK.</p>
</td>
<td class="cellrowborder" valign="top" width="48.010000000000005%" headers="mcps1.2.4.1.3 "><p id="p15168173818564"><a name="p15168173818564"></a><a name="p15168173818564"></a>Time when the request is sent. The time is in the <strong id="b1592113843110"><a name="b1592113843110"></a><a name="b1592113843110"></a>YYYYMMDD'T'HHMMSS'Z'</strong> format.</p>
<p id="p816853811560"><a name="p816853811560"></a><a name="p816853811560"></a>The value is the current GMT time of the system.</p>
</td>
</tr>
<tr id="row21686380566"><td class="cellrowborder" valign="top" width="21.63%" headers="mcps1.2.4.1.1 "><p id="p1168338115620"><a name="p1168338115620"></a><a name="p1168338115620"></a>Authorization</p>
</td>
<td class="cellrowborder" valign="top" width="30.36%" headers="mcps1.2.4.1.2 "><p id="p2016933816564"><a name="p2016933816564"></a><a name="p2016933816564"></a>This parameter is mandatory for authentication using AK/SK.</p>
</td>
<td class="cellrowborder" valign="top" width="48.010000000000005%" headers="mcps1.2.4.1.3 "><p id="p3168173815567"><a name="p3168173815567"></a><a name="p3168173815567"></a>Signature authentication information. The value can be obtained from the request signing result.</p>
<p id="p16168113835612"><a name="p16168113835612"></a><a name="p16168113835612"></a>See <a href="obtaining-request-authentication.md">Obtaining Request Authentication</a>.</p>
</td>
</tr>
<tr id="row131691938145610"><td class="cellrowborder" valign="top" width="21.63%" headers="mcps1.2.4.1.1 "><p id="p316953818564"><a name="p316953818564"></a><a name="p316953818564"></a>Host</p>
</td>
<td class="cellrowborder" valign="top" width="30.36%" headers="mcps1.2.4.1.2 "><p id="p01697385565"><a name="p01697385565"></a><a name="p01697385565"></a>This parameter is mandatory for authentication using AK/SK.</p>
</td>
<td class="cellrowborder" valign="top" width="48.010000000000005%" headers="mcps1.2.4.1.3 "><p id="p1169113855617"><a name="p1169113855617"></a><a name="p1169113855617"></a>Server domain name and port number of the resource being requested. The value can be obtained from the URL of the service API. The value is <em id="i6871028321"><a name="i6871028321"></a><a name="i6871028321"></a>hostname[:port]</em>. If the port number is not specified, the default port is used. The default port number for <strong id="b2273357321"><a name="b2273357321"></a><a name="b2273357321"></a>https</strong> is <strong id="b52731855329"><a name="b52731855329"></a><a name="b52731855329"></a>443</strong>.</p>
</td>
</tr>
<tr id="row10169143817564"><td class="cellrowborder" valign="top" width="21.63%" headers="mcps1.2.4.1.1 "><p id="p316953815568"><a name="p316953815568"></a><a name="p316953815568"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="30.36%" headers="mcps1.2.4.1.2 "><p id="p13169113816568"><a name="p13169113816568"></a><a name="p13169113816568"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="48.010000000000005%" headers="mcps1.2.4.1.3 "><p id="p316983816565"><a name="p316983816565"></a><a name="p316983816565"></a>MIME type of the request body.</p>
</td>
</tr>
<tr id="row15169538145616"><td class="cellrowborder" valign="top" width="21.63%" headers="mcps1.2.4.1.1 "><p id="p116993805613"><a name="p116993805613"></a><a name="p116993805613"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="30.36%" headers="mcps1.2.4.1.2 "><p id="p31694386566"><a name="p31694386566"></a><a name="p31694386566"></a>This parameter is mandatory for POST and PUT requests, but must be left blank for GET requests.</p>
</td>
<td class="cellrowborder" valign="top" width="48.010000000000005%" headers="mcps1.2.4.1.3 "><p id="p2169638175614"><a name="p2169638175614"></a><a name="p2169638175614"></a>Length of the request body. The unit is byte.</p>
</td>
</tr>
<tr id="row1217083825612"><td class="cellrowborder" valign="top" width="21.63%" headers="mcps1.2.4.1.1 "><p id="p1817073815612"><a name="p1817073815612"></a><a name="p1817073815612"></a>X-Project-Id</p>
</td>
<td class="cellrowborder" valign="top" width="30.36%" headers="mcps1.2.4.1.2 "><p id="p19170143817567"><a name="p19170143817567"></a><a name="p19170143817567"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="48.010000000000005%" headers="mcps1.2.4.1.3 "><p id="p117033820564"><a name="p117033820564"></a><a name="p117033820564"></a>Project ID. This parameter is used to obtain the token for each project.</p>
</td>
</tr>
<tr id="row21707382565"><td class="cellrowborder" valign="top" width="21.63%" headers="mcps1.2.4.1.1 "><p id="p5170638155610"><a name="p5170638155610"></a><a name="p5170638155610"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="30.36%" headers="mcps1.2.4.1.2 "><p id="p5170238175610"><a name="p5170238175610"></a><a name="p5170238175610"></a>No (This parameter is mandatory for authentication using tokens.)</p>
</td>
<td class="cellrowborder" valign="top" width="48.010000000000005%" headers="mcps1.2.4.1.3 "><p id="p1170338125614"><a name="p1170338125614"></a><a name="p1170338125614"></a>User token.</p>
</td>
</tr>
<tr id="row3170123820569"><td class="cellrowborder" valign="top" width="21.63%" headers="mcps1.2.4.1.1 "><p id="p61701381568"><a name="p61701381568"></a><a name="p61701381568"></a>X-Language</p>
</td>
<td class="cellrowborder" valign="top" width="30.36%" headers="mcps1.2.4.1.2 "><p id="p181708389569"><a name="p181708389569"></a><a name="p181708389569"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="48.010000000000005%" headers="mcps1.2.4.1.3 "><p id="p8170138145611"><a name="p8170138145611"></a><a name="p8170138145611"></a>Request language. The value is <strong id="b13743646164514"><a name="b13743646164514"></a><a name="b13743646164514"></a>en-us</strong>.</p>
</td>
</tr>
<tr id="row118151751165914"><td class="cellrowborder" valign="top" width="21.63%" headers="mcps1.2.4.1.1 "><p id="p68621055165911"><a name="p68621055165911"></a><a name="p68621055165911"></a>Accept</p>
</td>
<td class="cellrowborder" valign="top" width="30.36%" headers="mcps1.2.4.1.2 "><p id="p1286210558598"><a name="p1286210558598"></a><a name="p1286210558598"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="48.010000000000005%" headers="mcps1.2.4.1.3 "><p id="p78621455145910"><a name="p78621455145910"></a><a name="p78621455145910"></a>Type of content that can be received by a client.</p>
</td>
</tr>
</tbody>
</table>

