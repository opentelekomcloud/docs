# Querying Image Permissions<a name="EN-US_TOPIC_0215229640"></a>

## Function<a name="se03aae4436e64394a95dc13b6f233898"></a>

Query image permissions.

## URI<a name="s476df674307e4b04b9545f9575dde042"></a>

GET /v2/manage/namespaces/\{_namespace_\}/repos/\{_repository_\}/access

**Table  1**  Parameter description

<a name="table4985135363111"></a>
<table><thead align="left"><tr id="row17986653133115"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p1698625393113"><a name="p1698625393113"></a><a name="p1698625393113"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p8962134733214"><a name="p8962134733214"></a><a name="p8962134733214"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23.599999999999998%" id="mcps1.2.5.1.3"><p id="p1096264715327"><a name="p1096264715327"></a><a name="p1096264715327"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="46.400000000000006%" id="mcps1.2.5.1.4"><p id="p1398605373115"><a name="p1398605373115"></a><a name="p1398605373115"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row49861453133111"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p14986453193115"><a name="p14986453193115"></a><a name="p14986453193115"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p1198635333114"><a name="p1198635333114"></a><a name="p1198635333114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="23.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p7986853153114"><a name="p7986853153114"></a><a name="p7986853153114"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46.400000000000006%" headers="mcps1.2.5.1.4 "><p id="p199861531314"><a name="p199861531314"></a><a name="p199861531314"></a>Organization name.</p>
</td>
</tr>
<tr id="row1316181182114"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p1816115113217"><a name="p1816115113217"></a><a name="p1816115113217"></a>repository</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p21611111202111"><a name="p21611111202111"></a><a name="p21611111202111"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="23.599999999999998%" headers="mcps1.2.5.1.3 "><p id="p7161111192116"><a name="p7161111192116"></a><a name="p7161111192116"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46.400000000000006%" headers="mcps1.2.5.1.4 "><p id="p31611811102113"><a name="p31611811102113"></a><a name="p31611811102113"></a>Image name.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="s8246d3afdd6f44dc817ce0c3f2ac7d53"></a>

**Request example**

```
N/A
```

## Response Message<a name="sab9be5ce850743859bb238e072f8d1f2"></a>

**Response parameters**

**Table  2**  Response body parameter description

<a name="table861363224"></a>
<table><thead align="left"><tr id="row1610612213"><th class="cellrowborder" valign="top" width="21.29%" id="mcps1.2.4.1.1"><p id="p15483169172220"><a name="p15483169172220"></a><a name="p15483169172220"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.68%" id="mcps1.2.4.1.2"><p id="p161860229"><a name="p161860229"></a><a name="p161860229"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.03%" id="mcps1.2.4.1.3"><p id="p14611642210"><a name="p14611642210"></a><a name="p14611642210"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row661186162213"><td class="cellrowborder" valign="top" width="21.29%" headers="mcps1.2.4.1.1 "><p id="p2061960226"><a name="p2061960226"></a><a name="p2061960226"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.2 "><p id="p11613672211"><a name="p11613672211"></a><a name="p11613672211"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="57.03%" headers="mcps1.2.4.1.3 "><p id="p72841350182214"><a name="p72841350182214"></a><a name="p72841350182214"></a>Permission ID.</p>
</td>
</tr>
<tr id="row362362226"><td class="cellrowborder" valign="top" width="21.29%" headers="mcps1.2.4.1.1 "><p id="p2628618226"><a name="p2628618226"></a><a name="p2628618226"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.2 "><p id="p56236162212"><a name="p56236162212"></a><a name="p56236162212"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.03%" headers="mcps1.2.4.1.3 "><p id="p126212617227"><a name="p126212617227"></a><a name="p126212617227"></a>Image name.</p>
</td>
</tr>
<tr id="row46226172217"><td class="cellrowborder" valign="top" width="21.29%" headers="mcps1.2.4.1.1 "><p id="p1262462228"><a name="p1262462228"></a><a name="p1262462228"></a>creator_name</p>
</td>
<td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.2 "><p id="p9621967225"><a name="p9621967225"></a><a name="p9621967225"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.03%" headers="mcps1.2.4.1.3 "><p id="p1362146162212"><a name="p1362146162212"></a><a name="p1362146162212"></a>Creator.</p>
</td>
</tr>
<tr id="row1190415802318"><td class="cellrowborder" valign="top" width="21.29%" headers="mcps1.2.4.1.1 "><p id="p7904458152320"><a name="p7904458152320"></a><a name="p7904458152320"></a>self_auth</p>
</td>
<td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.2 "><p id="p1628218791415"><a name="p1628218791415"></a><a name="p1628218791415"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="57.03%" headers="mcps1.2.4.1.3 "><p id="p4381755113616"><a name="p4381755113616"></a><a name="p4381755113616"></a>For details, see <a href="creating-image-permissions.md#table6912142367">Table 2</a>.</p>
<pre class="screen" id="screen126971423171111"><a name="screen126971423171111"></a><a name="screen126971423171111"></a>{
        "user_id": "3059e6b5562241fda3fa441cca6f228b",
        "user_name": "user",
        "auth": 7
}</pre>
</td>
</tr>
<tr id="row1672110181276"><td class="cellrowborder" valign="top" width="21.29%" headers="mcps1.2.4.1.1 "><p id="p11722718172711"><a name="p11722718172711"></a><a name="p11722718172711"></a>others_auth</p>
</td>
<td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.2 "><p id="p4809172913147"><a name="p4809172913147"></a><a name="p4809172913147"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="57.03%" headers="mcps1.2.4.1.3 "><pre class="screen" id="screen17578185816104"><a name="screen17578185816104"></a><a name="screen17578185816104"></a>[
        {
            "user_id": "fb3f175c1fd146ab8cdae3272be6107b",
            "user_name": "user01",
            "auth": 7
        }
]</pre>
</td>
</tr>
</tbody>
</table>

**Response example**

```
{
    "id": 1422,
    "name": "test",
    "creator_name": "user",
    "self_auth": {
        "user_id": "3059e6b5562241fda3fa441cca6f228b",
        "user_name": "user",
        "auth": 7
    },
    "others_auths": [
        {
            "user_id": "fb3f175c1fd146ab8cdae3272be6107b",
            "user_name": "user01",
            "auth": 7
        }
    ]
}
```

## Status Code<a name="s336c1dbc7af446a1b3cc077ea3f82fc9"></a>

<a name="t33d02fa79e8443868a71c99f411610a5"></a>
<table><thead align="left"><tr id="r9eb80d64e8f34d0db940daa95fc929dd"><th class="cellrowborder" valign="top" width="16.439999999999998%" id="mcps1.1.3.1.1"><p id="a7e51ed73a71e4dc29d0dd4aae3016632"><a name="a7e51ed73a71e4dc29d0dd4aae3016632"></a><a name="a7e51ed73a71e4dc29d0dd4aae3016632"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83.56%" id="mcps1.1.3.1.2"><p id="aa802d02e21c944f1863435a0d11c7ec1"><a name="aa802d02e21c944f1863435a0d11c7ec1"></a><a name="aa802d02e21c944f1863435a0d11c7ec1"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r1cc0192c651444db882dde750b14be23"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.1.3.1.1 "><p id="a6a3639a3cb154e17b95c5076c8036471"><a name="a6a3639a3cb154e17b95c5076c8036471"></a><a name="a6a3639a3cb154e17b95c5076c8036471"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.1.3.1.2 "><p id="ad54ae639e7f94380a87bfc10cc91a4f0"><a name="ad54ae639e7f94380a87bfc10cc91a4f0"></a><a name="ad54ae639e7f94380a87bfc10cc91a4f0"></a>Operation succeeded.</p>
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

