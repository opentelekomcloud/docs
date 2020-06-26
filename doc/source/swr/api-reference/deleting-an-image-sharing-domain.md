# Deleting an Image Sharing Domain<a name="EN-US_TOPIC_0198655159"></a>

## Function<a name="se03aae4436e64394a95dc13b6f233898"></a>

Delete an image sharing domain.

## URI<a name="s476df674307e4b04b9545f9575dde042"></a>

DELETE /v2/manage/namespaces/\{_namespace_\}/repos/\{_repository_\}/access-domains/\{_access\_domain_\}

For details about parameters, see  [Table 1](#table11843162810214).

**Table  1**  Parameter description

<a name="table11843162810214"></a>
<table><thead align="left"><tr id="row20843172818213"><th class="cellrowborder" valign="top" width="17.61%" id="mcps1.2.5.1.1"><p id="p3843528621"><a name="p3843528621"></a><a name="p3843528621"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.13%" id="mcps1.2.5.1.2"><p id="p15022419437"><a name="p15022419437"></a><a name="p15022419437"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="23.27%" id="mcps1.2.5.1.3"><p id="p1450315424313"><a name="p1450315424313"></a><a name="p1450315424313"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42.99%" id="mcps1.2.5.1.4"><p id="p1584342811211"><a name="p1584342811211"></a><a name="p1584342811211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1084316281925"><td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.5.1.1 "><p id="p6843228526"><a name="p6843228526"></a><a name="p6843228526"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="16.13%" headers="mcps1.2.5.1.2 "><p id="p1588511134719"><a name="p1588511134719"></a><a name="p1588511134719"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.2.5.1.3 "><p id="p39019111471"><a name="p39019111471"></a><a name="p39019111471"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.99%" headers="mcps1.2.5.1.4 "><p id="p85037015469"><a name="p85037015469"></a><a name="p85037015469"></a>Organization name</p>
</td>
</tr>
<tr id="row1319321944420"><td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.5.1.1 "><p id="p919315194441"><a name="p919315194441"></a><a name="p919315194441"></a>repository</p>
</td>
<td class="cellrowborder" valign="top" width="16.13%" headers="mcps1.2.5.1.2 "><p id="p26577123471"><a name="p26577123471"></a><a name="p26577123471"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.2.5.1.3 "><p id="p20658112104717"><a name="p20658112104717"></a><a name="p20658112104717"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.99%" headers="mcps1.2.5.1.4 "><p id="p13193201924411"><a name="p13193201924411"></a><a name="p13193201924411"></a>Image repository name</p>
</td>
</tr>
<tr id="row169349264113"><td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.5.1.1 "><p id="p11934726191114"><a name="p11934726191114"></a><a name="p11934726191114"></a>access_domain</p>
</td>
<td class="cellrowborder" valign="top" width="16.13%" headers="mcps1.2.5.1.2 "><p id="p192815146472"><a name="p192815146472"></a><a name="p192815146472"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.2.5.1.3 "><p id="p1728241420476"><a name="p1728241420476"></a><a name="p1728241420476"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.99%" headers="mcps1.2.5.1.4 "><p id="p17934626131118"><a name="p17934626131118"></a><a name="p17934626131118"></a>Image sharing domain name</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="s8246d3afdd6f44dc817ce0c3f2ac7d53"></a>

N/A

## Response Message<a name="sab9be5ce850743859bb238e072f8d1f2"></a>

N/A

## Status Code<a name="s336c1dbc7af446a1b3cc077ea3f82fc9"></a>

For details about status code, see  [Table 2](#t33d02fa79e8443868a71c99f411610a5).

**Table  2**  Status code

<a name="t33d02fa79e8443868a71c99f411610a5"></a>
<table><thead align="left"><tr id="r9eb80d64e8f34d0db940daa95fc929dd"><th class="cellrowborder" valign="top" width="16.439999999999998%" id="mcps1.2.3.1.1"><p id="a7e51ed73a71e4dc29d0dd4aae3016632"><a name="a7e51ed73a71e4dc29d0dd4aae3016632"></a><a name="a7e51ed73a71e4dc29d0dd4aae3016632"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83.56%" id="mcps1.2.3.1.2"><p id="aa802d02e21c944f1863435a0d11c7ec1"><a name="aa802d02e21c944f1863435a0d11c7ec1"></a><a name="aa802d02e21c944f1863435a0d11c7ec1"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r1cc0192c651444db882dde750b14be23"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="a6a3639a3cb154e17b95c5076c8036471"><a name="a6a3639a3cb154e17b95c5076c8036471"></a><a name="a6a3639a3cb154e17b95c5076c8036471"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="p14504142233912"><a name="p14504142233912"></a><a name="p14504142233912"></a>Deleted successfully.</p>
</td>
</tr>
<tr id="r0bd68000afe546dd9c7a8d3a05991a04"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="ad46ccdc6b7e04df3b6b5679f7606f434"><a name="ad46ccdc6b7e04df3b6b5679f7606f434"></a><a name="ad46ccdc6b7e04df3b6b5679f7606f434"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="a1f2e8d58145d461781428d28f07a5351"><a name="a1f2e8d58145d461781428d28f07a5351"></a><a name="a1f2e8d58145d461781428d28f07a5351"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row059261364320"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="p059261310438"><a name="p059261310438"></a><a name="p059261310438"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="p759261314433"><a name="p759261314433"></a><a name="p759261314433"></a>Authentication failed.</p>
</td>
</tr>
<tr id="r19bdef782c164c93917f897241e521f8"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="a7da68e311c0f4267bacf3cbdb71d1ead"><a name="a7da68e311c0f4267bacf3cbdb71d1ead"></a><a name="a7da68e311c0f4267bacf3cbdb71d1ead"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="aa6fd12cedd8841e29eeeca27c1bdea1a"><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

