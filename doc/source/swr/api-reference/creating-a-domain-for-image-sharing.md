# Creating a Domain for Image Sharing<a name="EN-US_TOPIC_0198655148"></a>

## Function<a name="se03aae4436e64394a95dc13b6f233898"></a>

Create a domain for image sharing. You can share your  private images  with other users and grant access permissions to them.

## URI<a name="s476df674307e4b04b9545f9575dde042"></a>

POST /v2/manage/namespaces/\{_namespace_\}/repos/\{_repository_\}/access-domains

For details about parameters, see  [Table 1](#table11843162810214).

**Table  1**  Parameter description

<a name="table11843162810214"></a>
<table><thead align="left"><tr id="row20843172818213"><th class="cellrowborder" valign="top" width="17.26%" id="mcps1.2.5.1.1"><p id="p3843528621"><a name="p3843528621"></a><a name="p3843528621"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.950000000000001%" id="mcps1.2.5.1.2"><p id="p15022419437"><a name="p15022419437"></a><a name="p15022419437"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="19.53%" id="mcps1.2.5.1.3"><p id="p1450315424313"><a name="p1450315424313"></a><a name="p1450315424313"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="49.26%" id="mcps1.2.5.1.4"><p id="p1584342811211"><a name="p1584342811211"></a><a name="p1584342811211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1084316281925"><td class="cellrowborder" valign="top" width="17.26%" headers="mcps1.2.5.1.1 "><p id="p6843228526"><a name="p6843228526"></a><a name="p6843228526"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.2.5.1.2 "><p id="p158951353104613"><a name="p158951353104613"></a><a name="p158951353104613"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.53%" headers="mcps1.2.5.1.3 "><p id="p13895185318469"><a name="p13895185318469"></a><a name="p13895185318469"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.26%" headers="mcps1.2.5.1.4 "><p id="p85037015469"><a name="p85037015469"></a><a name="p85037015469"></a>Organization name</p>
</td>
</tr>
<tr id="row1319321944420"><td class="cellrowborder" valign="top" width="17.26%" headers="mcps1.2.5.1.1 "><p id="p919315194441"><a name="p919315194441"></a><a name="p919315194441"></a>repository</p>
</td>
<td class="cellrowborder" valign="top" width="13.950000000000001%" headers="mcps1.2.5.1.2 "><p id="p1089613531464"><a name="p1089613531464"></a><a name="p1089613531464"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.53%" headers="mcps1.2.5.1.3 "><p id="p17899145312462"><a name="p17899145312462"></a><a name="p17899145312462"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.26%" headers="mcps1.2.5.1.4 "><p id="p13193201924411"><a name="p13193201924411"></a><a name="p13193201924411"></a>Image repository name</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="s8246d3afdd6f44dc817ce0c3f2ac7d53"></a>

**Request parameters**

**Table  2**  Request body parameter description

<a name="table129941514855"></a>
<table><thead align="left"><tr id="row1111415559"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p162815458"><a name="p162815458"></a><a name="p162815458"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.010000000000002%" id="mcps1.2.5.1.2"><p id="p179515064715"><a name="p179515064715"></a><a name="p179515064715"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="22.55%" id="mcps1.2.5.1.3"><p id="p117979034718"><a name="p117979034718"></a><a name="p117979034718"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="45.440000000000005%" id="mcps1.2.5.1.4"><p id="p7612153511"><a name="p7612153511"></a><a name="p7612153511"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11816151559"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p17916150515"><a name="p17916150515"></a><a name="p17916150515"></a>access_domain</p>
</td>
<td class="cellrowborder" valign="top" width="15.010000000000002%" headers="mcps1.2.5.1.2 "><p id="p151114158513"><a name="p151114158513"></a><a name="p151114158513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="22.55%" headers="mcps1.2.5.1.3 "><p id="p14131315257"><a name="p14131315257"></a><a name="p14131315257"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="p2152015954"><a name="p2152015954"></a><a name="p2152015954"></a>Name of the domain for image sharing.</p>
</td>
</tr>
<tr id="row14116102041010"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p151171720181020"><a name="p151171720181020"></a><a name="p151171720181020"></a>permit</p>
</td>
<td class="cellrowborder" valign="top" width="15.010000000000002%" headers="mcps1.2.5.1.2 "><p id="p15117420191012"><a name="p15117420191012"></a><a name="p15117420191012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="22.55%" headers="mcps1.2.5.1.3 "><p id="p8117320111011"><a name="p8117320111011"></a><a name="p8117320111011"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="p31177205103"><a name="p31177205103"></a><a name="p31177205103"></a>Currently, only the <strong id="b669912336504"><a name="b669912336504"></a><a name="b669912336504"></a>read</strong> permission is supported.</p>
</td>
</tr>
<tr id="row10426185741019"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p74261957121020"><a name="p74261957121020"></a><a name="p74261957121020"></a>deadline</p>
</td>
<td class="cellrowborder" valign="top" width="15.010000000000002%" headers="mcps1.2.5.1.2 "><p id="p34261757141016"><a name="p34261757141016"></a><a name="p34261757141016"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="22.55%" headers="mcps1.2.5.1.3 "><p id="p106651856111"><a name="p106651856111"></a><a name="p106651856111"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="p11427155712106"><a name="p11427155712106"></a><a name="p11427155712106"></a>End date of image sharing (UTC). When the value is set to <strong id="b827515280467"><a name="b827515280467"></a><a name="b827515280467"></a>forever</strong>, the image will be permanently available for the domain. The validity period is calculated by day. The shared images expire at 00:00:00 on the day after the end date.</p>
</td>
</tr>
<tr id="row1930349121111"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p1630417961115"><a name="p1630417961115"></a><a name="p1630417961115"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="15.010000000000002%" headers="mcps1.2.5.1.2 "><p id="p130415920113"><a name="p130415920113"></a><a name="p130415920113"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="22.55%" headers="mcps1.2.5.1.3 "><p id="p930413917115"><a name="p930413917115"></a><a name="p930413917115"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.440000000000005%" headers="mcps1.2.5.1.4 "><p id="p1230420914115"><a name="p1230420914115"></a><a name="p1230420914115"></a>Description.</p>
</td>
</tr>
</tbody>
</table>

**Request example**

```
{
    "access_domain":"otc",
    "permit":"read",
    "deadline":"2018-10-01T16:00:00.000Z",
    "description":"description"
}
```

## Response<a name="sab9be5ce850743859bb238e072f8d1f2"></a>

N/A

## Status Code<a name="s336c1dbc7af446a1b3cc077ea3f82fc9"></a>

For details about status code, see  [Table 3](#t33d02fa79e8443868a71c99f411610a5).

**Table  3**  Status code

<a name="t33d02fa79e8443868a71c99f411610a5"></a>
<table><thead align="left"><tr id="r9eb80d64e8f34d0db940daa95fc929dd"><th class="cellrowborder" valign="top" width="16.439999999999998%" id="mcps1.2.3.1.1"><p id="a7e51ed73a71e4dc29d0dd4aae3016632"><a name="a7e51ed73a71e4dc29d0dd4aae3016632"></a><a name="a7e51ed73a71e4dc29d0dd4aae3016632"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83.56%" id="mcps1.2.3.1.2"><p id="aa802d02e21c944f1863435a0d11c7ec1"><a name="aa802d02e21c944f1863435a0d11c7ec1"></a><a name="aa802d02e21c944f1863435a0d11c7ec1"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r1cc0192c651444db882dde750b14be23"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="a6a3639a3cb154e17b95c5076c8036471"><a name="a6a3639a3cb154e17b95c5076c8036471"></a><a name="a6a3639a3cb154e17b95c5076c8036471"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="p14504142233912"><a name="p14504142233912"></a><a name="p14504142233912"></a>Created successfully.</p>
</td>
</tr>
<tr id="r0bd68000afe546dd9c7a8d3a05991a04"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="ad46ccdc6b7e04df3b6b5679f7606f434"><a name="ad46ccdc6b7e04df3b6b5679f7606f434"></a><a name="ad46ccdc6b7e04df3b6b5679f7606f434"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="a1f2e8d58145d461781428d28f07a5351"><a name="a1f2e8d58145d461781428d28f07a5351"></a><a name="a1f2e8d58145d461781428d28f07a5351"></a>Request error.</p>
</td>
</tr>
<tr id="row059261364320"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="p059261310438"><a name="p059261310438"></a><a name="p059261310438"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="p759261314433"><a name="p759261314433"></a><a name="p759261314433"></a>Authentication failed.</p>
</td>
</tr>
<tr id="row20511419122"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="p195119191228"><a name="p195119191228"></a><a name="p195119191228"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="p11516196218"><a name="p11516196218"></a><a name="p11516196218"></a>The image has already been shared to this domain.</p>
</td>
</tr>
<tr id="r19bdef782c164c93917f897241e521f8"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="a7da68e311c0f4267bacf3cbdb71d1ead"><a name="a7da68e311c0f4267bacf3cbdb71d1ead"></a><a name="a7da68e311c0f4267bacf3cbdb71d1ead"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="aa6fd12cedd8841e29eeeca27c1bdea1a"><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a>Internal error.</p>
</td>
</tr>
</tbody>
</table>

