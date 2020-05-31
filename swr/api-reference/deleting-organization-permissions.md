# Deleting Organization Permissions<a name="EN-US_TOPIC_0215229634"></a>

## Function<a name="se03aae4436e64394a95dc13b6f233898"></a>

Delete organization permissions.

## URI<a name="s476df674307e4b04b9545f9575dde042"></a>

DELETE /v2/manage/namespaces/\{_namespace_\}/access

**Table  1**  Parameter description

<a name="table73271639103420"></a>
<table><thead align="left"><tr id="row53291539153419"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p6331539113416"><a name="p6331539113416"></a><a name="p6331539113416"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.01%" id="mcps1.2.5.1.2"><p id="p14332539113414"><a name="p14332539113414"></a><a name="p14332539113414"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="21.3%" id="mcps1.2.5.1.3"><p id="p153331239183410"><a name="p153331239183410"></a><a name="p153331239183410"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="44.690000000000005%" id="mcps1.2.5.1.4"><p id="p43347399345"><a name="p43347399345"></a><a name="p43347399345"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row7335939103416"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p6843228526"><a name="p6843228526"></a><a name="p6843228526"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="17.01%" headers="mcps1.2.5.1.2 "><p id="p738985891415"><a name="p738985891415"></a><a name="p738985891415"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="21.3%" headers="mcps1.2.5.1.3 "><p id="p1884432818210"><a name="p1884432818210"></a><a name="p1884432818210"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44.690000000000005%" headers="mcps1.2.5.1.4 "><p id="p776511203467"><a name="p776511203467"></a><a name="p776511203467"></a>Organization name.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="s8246d3afdd6f44dc817ce0c3f2ac7d53"></a>

**Request parameters**

**Table  2**  Request body parameter description

<a name="table1410410571231"></a>
<table><thead align="left"><tr id="row5107125716318"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p810811571237"><a name="p810811571237"></a><a name="p810811571237"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.5%" id="mcps1.2.5.1.2"><p id="p2011016570315"><a name="p2011016570315"></a><a name="p2011016570315"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="21.91%" id="mcps1.2.5.1.3"><p id="p1311119571031"><a name="p1311119571031"></a><a name="p1311119571031"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="43.59%" id="mcps1.2.5.1.4"><p id="p19113185715315"><a name="p19113185715315"></a><a name="p19113185715315"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10114145712314"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p1110011416365"><a name="p1110011416365"></a><a name="p1110011416365"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.5%" headers="mcps1.2.5.1.2 "><p id="p69014461148"><a name="p69014461148"></a><a name="p69014461148"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="21.91%" headers="mcps1.2.5.1.3 "><p id="p7102121411366"><a name="p7102121411366"></a><a name="p7102121411366"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43.59%" headers="mcps1.2.5.1.4 "><p id="p19103151463617"><a name="p19103151463617"></a><a name="p19103151463617"></a>User ID, which needs to be obtained from the IAM service.</p>
</td>
</tr>
</tbody>
</table>

**Request example**

```
["fb3f175c1fd146ab8cdae3272be6107b"]
```

## Response Message<a name="sab9be5ce850743859bb238e072f8d1f2"></a>

**Response example**

```
N/A
```

## Status Code<a name="s336c1dbc7af446a1b3cc077ea3f82fc9"></a>

<a name="t33d02fa79e8443868a71c99f411610a5"></a>
<table><thead align="left"><tr id="r9eb80d64e8f34d0db940daa95fc929dd"><th class="cellrowborder" valign="top" width="16.439999999999998%" id="mcps1.1.3.1.1"><p id="a7e51ed73a71e4dc29d0dd4aae3016632"><a name="a7e51ed73a71e4dc29d0dd4aae3016632"></a><a name="a7e51ed73a71e4dc29d0dd4aae3016632"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83.56%" id="mcps1.1.3.1.2"><p id="aa802d02e21c944f1863435a0d11c7ec1"><a name="aa802d02e21c944f1863435a0d11c7ec1"></a><a name="aa802d02e21c944f1863435a0d11c7ec1"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r1cc0192c651444db882dde750b14be23"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.1.3.1.1 "><p id="a6a3639a3cb154e17b95c5076c8036471"><a name="a6a3639a3cb154e17b95c5076c8036471"></a><a name="a6a3639a3cb154e17b95c5076c8036471"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.1.3.1.2 "><p id="ad54ae639e7f94380a87bfc10cc91a4f0"><a name="ad54ae639e7f94380a87bfc10cc91a4f0"></a><a name="ad54ae639e7f94380a87bfc10cc91a4f0"></a>Deleted successfully.</p>
</td>
</tr>
<tr id="r0bd68000afe546dd9c7a8d3a05991a04"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.1.3.1.1 "><p id="ad46ccdc6b7e04df3b6b5679f7606f434"><a name="ad46ccdc6b7e04df3b6b5679f7606f434"></a><a name="ad46ccdc6b7e04df3b6b5679f7606f434"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.1.3.1.2 "><p id="a1f2e8d58145d461781428d28f07a5351"><a name="a1f2e8d58145d461781428d28f07a5351"></a><a name="a1f2e8d58145d461781428d28f07a5351"></a>Request error.</p>
</td>
</tr>
<tr id="row059261364320"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.1.3.1.1 "><p id="p059261310438"><a name="p059261310438"></a><a name="p059261310438"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.1.3.1.2 "><p id="p759261314433"><a name="p759261314433"></a><a name="p759261314433"></a>Authentication failed.</p>
</td>
</tr>
<tr id="row9547111612437"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.1.3.1.1 "><p id="p19547131615432"><a name="p19547131615432"></a><a name="p19547131615432"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.1.3.1.2 "><p id="p16547416114315"><a name="p16547416114315"></a><a name="p16547416114315"></a>The organization or the organization permission does not exist.</p>
</td>
</tr>
<tr id="r19bdef782c164c93917f897241e521f8"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.1.3.1.1 "><p id="a7da68e311c0f4267bacf3cbdb71d1ead"><a name="a7da68e311c0f4267bacf3cbdb71d1ead"></a><a name="a7da68e311c0f4267bacf3cbdb71d1ead"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.1.3.1.2 "><p id="aa6fd12cedd8841e29eeeca27c1bdea1a"><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a>Internal error.</p>
</td>
</tr>
</tbody>
</table>

