# Updating Image Permissions<a name="EN-US_TOPIC_0215229639"></a>

## Function<a name="se03aae4436e64394a95dc13b6f233898"></a>

Update image permissions.

## URI<a name="s476df674307e4b04b9545f9575dde042"></a>

**URI format**

PATCH /v2/manage/namespaces/\{_namespace_\}/repos/\{_repository_\}/access

**Table  1**  Parameter description

<a name="table73271639103420"></a>
<table><thead align="left"><tr id="row53291539153419"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p6331539113416"><a name="p6331539113416"></a><a name="p6331539113416"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p8962134733214"><a name="p8962134733214"></a><a name="p8962134733214"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="21.11%" id="mcps1.2.5.1.3"><p id="p1096264715327"><a name="p1096264715327"></a><a name="p1096264715327"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="48.89%" id="mcps1.2.5.1.4"><p id="p43347399345"><a name="p43347399345"></a><a name="p43347399345"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row7335939103416"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p6843228526"><a name="p6843228526"></a><a name="p6843228526"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p284310281826"><a name="p284310281826"></a><a name="p284310281826"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.5.1.3 "><p id="p1884432818210"><a name="p1884432818210"></a><a name="p1884432818210"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="48.89%" headers="mcps1.2.5.1.4 "><p id="p776511203467"><a name="p776511203467"></a><a name="p776511203467"></a>Organization name.</p>
</td>
</tr>
<tr id="row1316181182114"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p1816115113217"><a name="p1816115113217"></a><a name="p1816115113217"></a>repository</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p21611111202111"><a name="p21611111202111"></a><a name="p21611111202111"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.5.1.3 "><p id="p7161111192116"><a name="p7161111192116"></a><a name="p7161111192116"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="48.89%" headers="mcps1.2.5.1.4 "><p id="p31611811102113"><a name="p31611811102113"></a><a name="p31611811102113"></a>Image name.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="s8246d3afdd6f44dc817ce0c3f2ac7d53"></a>

**Request parameters**

**Table  2**  Request body parameter description

<a name="table1656715468307"></a>
<table><thead align="left"><tr id="row1156754619306"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p1156774683014"><a name="p1156774683014"></a><a name="p1156774683014"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p25683461309"><a name="p25683461309"></a><a name="p25683461309"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="20.79%" id="mcps1.2.5.1.3"><p id="p20568164617302"><a name="p20568164617302"></a><a name="p20568164617302"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="49.21%" id="mcps1.2.5.1.4"><p id="p956844693017"><a name="p956844693017"></a><a name="p956844693017"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19568104693019"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p1110011416365"><a name="p1110011416365"></a><a name="p1110011416365"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p1910111473610"><a name="p1910111473610"></a><a name="p1910111473610"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.79%" headers="mcps1.2.5.1.3 "><p id="p7102121411366"><a name="p7102121411366"></a><a name="p7102121411366"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.21%" headers="mcps1.2.5.1.4 "><p id="p19103151463617"><a name="p19103151463617"></a><a name="p19103151463617"></a>User ID, which needs to be obtained from the IAM service.</p>
</td>
</tr>
<tr id="row14568164611303"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p3107314193615"><a name="p3107314193615"></a><a name="p3107314193615"></a>user_name</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p2108514163620"><a name="p2108514163620"></a><a name="p2108514163620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.79%" headers="mcps1.2.5.1.3 "><p id="p31101214113617"><a name="p31101214113617"></a><a name="p31101214113617"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.21%" headers="mcps1.2.5.1.4 "><p id="p168731436184619"><a name="p168731436184619"></a><a name="p168731436184619"></a>Username, which needs to be obtained from the IAM service.</p>
</td>
</tr>
<tr id="row181901609314"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p35101132143714"><a name="p35101132143714"></a><a name="p35101132143714"></a>auth</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p151033215376"><a name="p151033215376"></a><a name="p151033215376"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="20.79%" headers="mcps1.2.5.1.3 "><p id="p1651014326371"><a name="p1651014326371"></a><a name="p1651014326371"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.21%" headers="mcps1.2.5.1.4 "><p id="p1751033214375"><a name="p1751033214375"></a><a name="p1751033214375"></a>User permission that is configured. The value can be 1, 3, or 7. <strong id="b7199814115011"><a name="b7199814115011"></a><a name="b7199814115011"></a>7</strong>: manage <strong id="b7696624104213"><a name="b7696624104213"></a><a name="b7696624104213"></a>3</strong>: write <strong id="b126501438134218"><a name="b126501438134218"></a><a name="b126501438134218"></a>1</strong>: read</p>
</td>
</tr>
</tbody>
</table>

**Request example**

```
[
    {
        "user_id": "fb3f175c1fd146ab8cdae3272be6107b",
        "user_name": "user01",
        "auth": 7
    }
]
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
<tbody><tr id="r1cc0192c651444db882dde750b14be23"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.1.3.1.1 "><p id="a6a3639a3cb154e17b95c5076c8036471"><a name="a6a3639a3cb154e17b95c5076c8036471"></a><a name="a6a3639a3cb154e17b95c5076c8036471"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.1.3.1.2 "><p id="ad54ae639e7f94380a87bfc10cc91a4f0"><a name="ad54ae639e7f94380a87bfc10cc91a4f0"></a><a name="ad54ae639e7f94380a87bfc10cc91a4f0"></a>Updated successfully.</p>
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
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.1.3.1.2 "><p id="p16547416114315"><a name="p16547416114315"></a><a name="p16547416114315"></a>The image or the image permission does not exist.</p>
</td>
</tr>
<tr id="r19bdef782c164c93917f897241e521f8"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.1.3.1.1 "><p id="a7da68e311c0f4267bacf3cbdb71d1ead"><a name="a7da68e311c0f4267bacf3cbdb71d1ead"></a><a name="a7da68e311c0f4267bacf3cbdb71d1ead"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.1.3.1.2 "><p id="aa6fd12cedd8841e29eeeca27c1bdea1a"><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a>Internal error.</p>
</td>
</tr>
</tbody>
</table>

