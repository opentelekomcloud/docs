# Deleting an Organization<a name="EN-US_TOPIC_0198655146"></a>

## Function<a name="se03aae4436e64394a95dc13b6f233898"></a>

Delete an organization.

## URI<a name="s476df674307e4b04b9545f9575dde042"></a>

DELETE /v2/manage/namespaces/\{_namespace_\}

For details about parameters, see  [Table 1](#tae82a09e27434bef9a38b734d798ae6c).

**Table  1**  Parameter description

<a name="tae82a09e27434bef9a38b734d798ae6c"></a>
<table><thead align="left"><tr id="r2c22eba22439445680961f8c447f8756"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="a4276374f4f884a1a8ff6eabdab4da030"><a name="a4276374f4f884a1a8ff6eabdab4da030"></a><a name="a4276374f4f884a1a8ff6eabdab4da030"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p2011016570315"><a name="p2011016570315"></a><a name="p2011016570315"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="21.83%" id="mcps1.2.5.1.3"><p id="p537522204217"><a name="p537522204217"></a><a name="p537522204217"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="48.17%" id="mcps1.2.5.1.4"><p id="en-us_topic_0060210625_p192541611508"><a name="en-us_topic_0060210625_p192541611508"></a><a name="en-us_topic_0060210625_p192541611508"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4140165617213"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p520212400161"><a name="p520212400161"></a><a name="p520212400161"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p15117857734"><a name="p15117857734"></a><a name="p15117857734"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="21.83%" headers="mcps1.2.5.1.3 "><p id="p20379152154213"><a name="p20379152154213"></a><a name="p20379152154213"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="48.17%" headers="mcps1.2.5.1.4 "><p id="p219804051612"><a name="p219804051612"></a><a name="p219804051612"></a>Organization name</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="s8246d3afdd6f44dc817ce0c3f2ac7d53"></a>

N/A

## Response<a name="sab9be5ce850743859bb238e072f8d1f2"></a>

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
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="ad54ae639e7f94380a87bfc10cc91a4f0"><a name="ad54ae639e7f94380a87bfc10cc91a4f0"></a><a name="ad54ae639e7f94380a87bfc10cc91a4f0"></a>Deleted successfully.</p>
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
<tr id="row121541746162419"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="p2155846172416"><a name="p2155846172416"></a><a name="p2155846172416"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="p151551946202416"><a name="p151551946202416"></a><a name="p151551946202416"></a>The organization does not exist.</p>
</td>
</tr>
<tr id="r19bdef782c164c93917f897241e521f8"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="a7da68e311c0f4267bacf3cbdb71d1ead"><a name="a7da68e311c0f4267bacf3cbdb71d1ead"></a><a name="a7da68e311c0f4267bacf3cbdb71d1ead"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="aa6fd12cedd8841e29eeeca27c1bdea1a"><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a>Internal error.</p>
</td>
</tr>
</tbody>
</table>

