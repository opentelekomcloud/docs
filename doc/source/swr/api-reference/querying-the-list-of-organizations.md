# Querying the List of Organizations<a name="EN-US_TOPIC_0198655152"></a>

## Function<a name="se03aae4436e64394a95dc13b6f233898"></a>

Query the list of organizations.

## URI<a name="s476df674307e4b04b9545f9575dde042"></a>

GET /v2/manage/namespaces?namespace=\{namespace\}

For details about parameters, see  [Table 1](#tae82a09e27434bef9a38b734d798ae6c).

**Table  1**  Parameter description

<a name="tae82a09e27434bef9a38b734d798ae6c"></a>
<table><thead align="left"><tr id="r2c22eba22439445680961f8c447f8756"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="a4276374f4f884a1a8ff6eabdab4da030"><a name="a4276374f4f884a1a8ff6eabdab4da030"></a><a name="a4276374f4f884a1a8ff6eabdab4da030"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p1781316754219"><a name="p1781316754219"></a><a name="p1781316754219"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="22.07%" id="mcps1.2.5.1.3"><p id="p1351382513427"><a name="p1351382513427"></a><a name="p1351382513427"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="47.93%" id="mcps1.2.5.1.4"><p id="en-us_topic_0060210625_p192541611508"><a name="en-us_topic_0060210625_p192541611508"></a><a name="en-us_topic_0060210625_p192541611508"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4140165617213"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p6843228526"><a name="p6843228526"></a><a name="p6843228526"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p681437134216"><a name="p681437134216"></a><a name="p681437134216"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="22.07%" headers="mcps1.2.5.1.3 "><p id="p9516625134212"><a name="p9516625134212"></a><a name="p9516625134212"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="47.93%" headers="mcps1.2.5.1.4 "><p id="p776511203467"><a name="p776511203467"></a><a name="p776511203467"></a>Organization name</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="s8246d3afdd6f44dc817ce0c3f2ac7d53"></a>

N/A

## Response<a name="sab9be5ce850743859bb238e072f8d1f2"></a>

**Response parameters**

**Table  2**  Response body parameter description

<a name="table34001413863"></a>
<table><thead align="left"><tr id="row17400171319612"><th class="cellrowborder" valign="top" width="20.89%" id="mcps1.2.4.1.1"><p id="p1840015139619"><a name="p1840015139619"></a><a name="p1840015139619"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.11%" id="mcps1.2.4.1.2"><p id="p24002135620"><a name="p24002135620"></a><a name="p24002135620"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="p174008131163"><a name="p174008131163"></a><a name="p174008131163"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11400113668"><td class="cellrowborder" valign="top" width="20.89%" headers="mcps1.2.4.1.1 "><p id="p14008131464"><a name="p14008131464"></a><a name="p14008131464"></a>namespaces</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.2.4.1.2 "><p id="p9400151314615"><a name="p9400151314615"></a><a name="p9400151314615"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p1840110136612"><a name="p1840110136612"></a><a name="p1840110136612"></a>Organization list. For details, see <a href="#table1787854911167">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  namespaces parameter description

<a name="table1787854911167"></a>
<table><thead align="left"><tr id="row1588184916165"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p158847496166"><a name="p158847496166"></a><a name="p158847496166"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p2088624911169"><a name="p2088624911169"></a><a name="p2088624911169"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="p128875496169"><a name="p128875496169"></a><a name="p128875496169"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row888994917169"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1889144915167"><a name="p1889144915167"></a><a name="p1889144915167"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p189324913167"><a name="p189324913167"></a><a name="p189324913167"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p14894149141612"><a name="p14894149141612"></a><a name="p14894149141612"></a>ID</p>
</td>
</tr>
<tr id="row19895649171616"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p589616491166"><a name="p589616491166"></a><a name="p589616491166"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p990115495162"><a name="p990115495162"></a><a name="p990115495162"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p2904184981613"><a name="p2904184981613"></a><a name="p2904184981613"></a>Organization name</p>
</td>
</tr>
<tr id="row1576047252"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p3578164162517"><a name="p3578164162517"></a><a name="p3578164162517"></a>creator_name</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p8578134122515"><a name="p8578134122515"></a><a name="p8578134122515"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p1557814492513"><a name="p1557814492513"></a><a name="p1557814492513"></a>Username</p>
</td>
</tr>
<tr id="row670815227263"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p270822232620"><a name="p270822232620"></a><a name="p270822232620"></a>auth</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p11708622162613"><a name="p11708622162613"></a><a name="p11708622162613"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p3709822102615"><a name="p3709822102615"></a><a name="p3709822102615"></a>User permission. The value can be 1, 3, or 7. <strong id="b7199814115011"><a name="b7199814115011"></a><a name="b7199814115011"></a>7</strong>: manage <strong id="b7696624104213"><a name="b7696624104213"></a><a name="b7696624104213"></a>3</strong>: write <strong id="b126501438134218"><a name="b126501438134218"></a><a name="b126501438134218"></a>1</strong>: read</p>
</td>
</tr>
</tbody>
</table>

**Response example**

```
{
    "namespaces": [
        {
            "id": 1422,
            "name": "otc",
            "creator_name": "username",
            "auth": 7
        }
    ]
}
```

## Status Code<a name="s336c1dbc7af446a1b3cc077ea3f82fc9"></a>

For details about status code, see  [Table 4](#t33d02fa79e8443868a71c99f411610a5).

**Table  4**  Status code

<a name="t33d02fa79e8443868a71c99f411610a5"></a>
<table><thead align="left"><tr id="r9eb80d64e8f34d0db940daa95fc929dd"><th class="cellrowborder" valign="top" width="16.48%" id="mcps1.2.3.1.1"><p id="a7e51ed73a71e4dc29d0dd4aae3016632"><a name="a7e51ed73a71e4dc29d0dd4aae3016632"></a><a name="a7e51ed73a71e4dc29d0dd4aae3016632"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83.52000000000001%" id="mcps1.2.3.1.2"><p id="aa802d02e21c944f1863435a0d11c7ec1"><a name="aa802d02e21c944f1863435a0d11c7ec1"></a><a name="aa802d02e21c944f1863435a0d11c7ec1"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r1cc0192c651444db882dde750b14be23"><td class="cellrowborder" valign="top" width="16.48%" headers="mcps1.2.3.1.1 "><p id="a6a3639a3cb154e17b95c5076c8036471"><a name="a6a3639a3cb154e17b95c5076c8036471"></a><a name="a6a3639a3cb154e17b95c5076c8036471"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="83.52000000000001%" headers="mcps1.2.3.1.2 "><p id="ad54ae639e7f94380a87bfc10cc91a4f0"><a name="ad54ae639e7f94380a87bfc10cc91a4f0"></a><a name="ad54ae639e7f94380a87bfc10cc91a4f0"></a>Operation successful.</p>
</td>
</tr>
<tr id="r0bd68000afe546dd9c7a8d3a05991a04"><td class="cellrowborder" valign="top" width="16.48%" headers="mcps1.2.3.1.1 "><p id="ad46ccdc6b7e04df3b6b5679f7606f434"><a name="ad46ccdc6b7e04df3b6b5679f7606f434"></a><a name="ad46ccdc6b7e04df3b6b5679f7606f434"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="83.52000000000001%" headers="mcps1.2.3.1.2 "><p id="a1f2e8d58145d461781428d28f07a5351"><a name="a1f2e8d58145d461781428d28f07a5351"></a><a name="a1f2e8d58145d461781428d28f07a5351"></a>Request error.</p>
</td>
</tr>
<tr id="row059261364320"><td class="cellrowborder" valign="top" width="16.48%" headers="mcps1.2.3.1.1 "><p id="p059261310438"><a name="p059261310438"></a><a name="p059261310438"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="83.52000000000001%" headers="mcps1.2.3.1.2 "><p id="p759261314433"><a name="p759261314433"></a><a name="p759261314433"></a>Authentication failed.</p>
</td>
</tr>
<tr id="row9547111612437"><td class="cellrowborder" valign="top" width="16.48%" headers="mcps1.2.3.1.1 "><p id="p19547131615432"><a name="p19547131615432"></a><a name="p19547131615432"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="83.52000000000001%" headers="mcps1.2.3.1.2 "><p id="p16547416114315"><a name="p16547416114315"></a><a name="p16547416114315"></a>The organization does not exist.</p>
</td>
</tr>
<tr id="r19bdef782c164c93917f897241e521f8"><td class="cellrowborder" valign="top" width="16.48%" headers="mcps1.2.3.1.1 "><p id="a7da68e311c0f4267bacf3cbdb71d1ead"><a name="a7da68e311c0f4267bacf3cbdb71d1ead"></a><a name="a7da68e311c0f4267bacf3cbdb71d1ead"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="83.52000000000001%" headers="mcps1.2.3.1.2 "><p id="aa6fd12cedd8841e29eeeca27c1bdea1a"><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a>Internal error.</p>
</td>
</tr>
</tbody>
</table>

