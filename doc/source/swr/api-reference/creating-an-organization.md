# Creating an Organization<a name="EN-US_TOPIC_0198655145"></a>

## Function<a name="se03aae4436e64394a95dc13b6f233898"></a>

Create an organization.

## URI<a name="s476df674307e4b04b9545f9575dde042"></a>

POST /v2/manage/namespaces

## Request<a name="s8246d3afdd6f44dc817ce0c3f2ac7d53"></a>

**Request parameters**

**Table  1**  Request body parameter description

<a name="table129941514855"></a>
<table><thead align="left"><tr id="row1111415559"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p162815458"><a name="p162815458"></a><a name="p162815458"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p63228569414"><a name="p63228569414"></a><a name="p63228569414"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.98%" id="mcps1.2.5.1.3"><p id="p83241756144115"><a name="p83241756144115"></a><a name="p83241756144115"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="52.019999999999996%" id="mcps1.2.5.1.4"><p id="p7612153511"><a name="p7612153511"></a><a name="p7612153511"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11816151559"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p17916150515"><a name="p17916150515"></a><a name="p17916150515"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p6326856114114"><a name="p6326856114114"></a><a name="p6326856114114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.98%" headers="mcps1.2.5.1.3 "><p id="p193261756154118"><a name="p193261756154118"></a><a name="p193261756154118"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="52.019999999999996%" headers="mcps1.2.5.1.4 "><p id="p5222017131216"><a name="p5222017131216"></a><a name="p5222017131216"></a>Organization name, which must be globally unique. Enter 1 to 64 characters, starting with a lowercase letter and ending with a lowercase letter or digit. Only lowercase letters, digits, periods (.), underscores (_), and hyphens (-) are allowed. Periods, underscores, and hyphens cannot be placed next to each other. A maximum of two consecutive underscores are allowed.</p>
</td>
</tr>
</tbody>
</table>

**Request example**

Create an organization named  **otc**.

```
{
    "namespace": "otc"
}
```

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
<tbody><tr id="r1cc0192c651444db882dde750b14be23"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="a6a3639a3cb154e17b95c5076c8036471"><a name="a6a3639a3cb154e17b95c5076c8036471"></a><a name="a6a3639a3cb154e17b95c5076c8036471"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="p14504142233912"><a name="p14504142233912"></a><a name="p14504142233912"></a>Created successfully.</p>
</td>
</tr>
<tr id="r0bd68000afe546dd9c7a8d3a05991a04"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="ad46ccdc6b7e04df3b6b5679f7606f434"><a name="ad46ccdc6b7e04df3b6b5679f7606f434"></a><a name="ad46ccdc6b7e04df3b6b5679f7606f434"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="a1f2e8d58145d461781428d28f07a5351"><a name="a1f2e8d58145d461781428d28f07a5351"></a><a name="a1f2e8d58145d461781428d28f07a5351"></a>Request error or the maximum number of organizations has been reached.</p>
</td>
</tr>
<tr id="row059261364320"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="p059261310438"><a name="p059261310438"></a><a name="p059261310438"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="p759261314433"><a name="p759261314433"></a><a name="p759261314433"></a>Authentication failed.</p>
</td>
</tr>
<tr id="row9547111612437"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="p19547131615432"><a name="p19547131615432"></a><a name="p19547131615432"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="p16547416114315"><a name="p16547416114315"></a><a name="p16547416114315"></a>The resource already exists.</p>
</td>
</tr>
<tr id="r19bdef782c164c93917f897241e521f8"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="a7da68e311c0f4267bacf3cbdb71d1ead"><a name="a7da68e311c0f4267bacf3cbdb71d1ead"></a><a name="a7da68e311c0f4267bacf3cbdb71d1ead"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="aa6fd12cedd8841e29eeeca27c1bdea1a"><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a>Internal error.</p>
</td>
</tr>
</tbody>
</table>

