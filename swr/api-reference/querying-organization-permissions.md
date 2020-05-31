# Querying Organization Permissions<a name="EN-US_TOPIC_0215229636"></a>

## Function<a name="se03aae4436e64394a95dc13b6f233898"></a>

Query organization permissions.

## URI<a name="s476df674307e4b04b9545f9575dde042"></a>

GET /v2/manage/namespaces/\{_namespace_\}/access

**Table  1**  Parameter description

<a name="table73271639103420"></a>
<table><thead align="left"><tr id="row53291539153419"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p6331539113416"><a name="p6331539113416"></a><a name="p6331539113416"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p14332539113414"><a name="p14332539113414"></a><a name="p14332539113414"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23.35%" id="mcps1.2.5.1.3"><p id="p153331239183410"><a name="p153331239183410"></a><a name="p153331239183410"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="46.650000000000006%" id="mcps1.2.5.1.4"><p id="p43347399345"><a name="p43347399345"></a><a name="p43347399345"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row7335939103416"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p6843228526"><a name="p6843228526"></a><a name="p6843228526"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p284310281826"><a name="p284310281826"></a><a name="p284310281826"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="23.35%" headers="mcps1.2.5.1.3 "><p id="p1884432818210"><a name="p1884432818210"></a><a name="p1884432818210"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46.650000000000006%" headers="mcps1.2.5.1.4 "><p id="p776511203467"><a name="p776511203467"></a><a name="p776511203467"></a>Organization name.</p>
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

<a name="t4b8ef5821d984e5bb98d60fbcaae2f10"></a>
<table><thead align="left"><tr id="rb0bcfb9829c841cc8324bb05c4bf5f12"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="a76c4d4c3eb1543ce8c40c0448b44ccea"><a name="a76c4d4c3eb1543ce8c40c0448b44ccea"></a><a name="a76c4d4c3eb1543ce8c40c0448b44ccea"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.29%" id="mcps1.2.4.1.2"><p id="a29df7d0e56754d91959c13c7abe6af3f"><a name="a29df7d0e56754d91959c13c7abe6af3f"></a><a name="a29df7d0e56754d91959c13c7abe6af3f"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.71%" id="mcps1.2.4.1.3"><p id="a0101343364754edd8fc84cf355ffef77"><a name="a0101343364754edd8fc84cf355ffef77"></a><a name="a0101343364754edd8fc84cf355ffef77"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rd2e8de514d8441b98053e2d715a61142"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1012113524165"><a name="p1012113524165"></a><a name="p1012113524165"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="24.29%" headers="mcps1.2.4.1.2 "><p id="p1512025251619"><a name="p1512025251619"></a><a name="p1512025251619"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54.71%" headers="mcps1.2.4.1.3 "><p id="p4119752181610"><a name="p4119752181610"></a><a name="p4119752181610"></a>id</p>
</td>
</tr>
<tr id="row674422085119"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p3118652111610"><a name="p3118652111610"></a><a name="p3118652111610"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="24.29%" headers="mcps1.2.4.1.2 "><p id="p4323171581519"><a name="p4323171581519"></a><a name="p4323171581519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.71%" headers="mcps1.2.4.1.3 "><p id="p9116752151615"><a name="p9116752151615"></a><a name="p9116752151615"></a>Organization name.</p>
</td>
</tr>
<tr id="row195241733121314"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p2524153314134"><a name="p2524153314134"></a><a name="p2524153314134"></a>creator_name</p>
</td>
<td class="cellrowborder" valign="top" width="24.29%" headers="mcps1.2.4.1.2 "><p id="p13326515191512"><a name="p13326515191512"></a><a name="p13326515191512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.71%" headers="mcps1.2.4.1.3 "><p id="p16524133181312"><a name="p16524133181312"></a><a name="p16524133181312"></a>Organization creator.</p>
</td>
</tr>
<tr id="row19282975146"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p128214721413"><a name="p128214721413"></a><a name="p128214721413"></a>self_auth</p>
</td>
<td class="cellrowborder" valign="top" width="24.29%" headers="mcps1.2.4.1.2 "><p id="p1628218791415"><a name="p1628218791415"></a><a name="p1628218791415"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="54.71%" headers="mcps1.2.4.1.3 "><p id="p16502201811340"><a name="p16502201811340"></a><a name="p16502201811340"></a>For details, see <a href="creating-organization-permissions.md#table6912142367">Table 2</a>.</p>
<pre class="screen" id="screen117045433146"><a name="screen117045433146"></a><a name="screen117045433146"></a>{
        "user_id": "xxx",
        "user_name": "xxx",
        "auth": x
}</pre>
</td>
</tr>
<tr id="row118081529141415"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p6808102917143"><a name="p6808102917143"></a><a name="p6808102917143"></a>others_auths</p>
</td>
<td class="cellrowborder" valign="top" width="24.29%" headers="mcps1.2.4.1.2 "><p id="p4809172913147"><a name="p4809172913147"></a><a name="p4809172913147"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="54.71%" headers="mcps1.2.4.1.3 "><pre class="screen" id="screen1452313021517"><a name="screen1452313021517"></a><a name="screen1452313021517"></a>[
        {
            "user_id": "xxx",
            "user_name": "xxx",
            "auth": x
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
    "creator_name": "user01",
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

