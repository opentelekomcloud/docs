# Querying the Details of an Image Sharing Domain<a name="EN-US_TOPIC_0198655135"></a>

## Function<a name="se03aae4436e64394a95dc13b6f233898"></a>

Query the details of an image sharing domain.

## URI<a name="s476df674307e4b04b9545f9575dde042"></a>

GET /v2/manage/namespaces/\{_namespace_\}/repos/\{_repository_\}/access-domains/\{_access\_domain_\}

For details about parameters, see  [Table 1](#table11843162810214).

**Table  1**  Parameter description

<a name="table11843162810214"></a>
<table><thead align="left"><tr id="row20843172818213"><th class="cellrowborder" valign="top" width="23.71%" id="mcps1.2.5.1.1"><p id="p3843528621"><a name="p3843528621"></a><a name="p3843528621"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.879999999999999%" id="mcps1.2.5.1.2"><p id="p3467112312474"><a name="p3467112312474"></a><a name="p3467112312474"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="26.650000000000002%" id="mcps1.2.5.1.3"><p id="p12469202344715"><a name="p12469202344715"></a><a name="p12469202344715"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="34.760000000000005%" id="mcps1.2.5.1.4"><p id="p1584342811211"><a name="p1584342811211"></a><a name="p1584342811211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1084316281925"><td class="cellrowborder" valign="top" width="23.71%" headers="mcps1.2.5.1.1 "><p id="p6843228526"><a name="p6843228526"></a><a name="p6843228526"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="14.879999999999999%" headers="mcps1.2.5.1.2 "><p id="p289883118229"><a name="p289883118229"></a><a name="p289883118229"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="26.650000000000002%" headers="mcps1.2.5.1.3 "><p id="p69291145134715"><a name="p69291145134715"></a><a name="p69291145134715"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="34.760000000000005%" headers="mcps1.2.5.1.4 "><p id="p85037015469"><a name="p85037015469"></a><a name="p85037015469"></a>Organization name</p>
</td>
</tr>
<tr id="row1319321944420"><td class="cellrowborder" valign="top" width="23.71%" headers="mcps1.2.5.1.1 "><p id="p919315194441"><a name="p919315194441"></a><a name="p919315194441"></a>repository</p>
</td>
<td class="cellrowborder" valign="top" width="14.879999999999999%" headers="mcps1.2.5.1.2 "><p id="p1189833112228"><a name="p1189833112228"></a><a name="p1189833112228"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="26.650000000000002%" headers="mcps1.2.5.1.3 "><p id="p1840713471471"><a name="p1840713471471"></a><a name="p1840713471471"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="34.760000000000005%" headers="mcps1.2.5.1.4 "><p id="p13193201924411"><a name="p13193201924411"></a><a name="p13193201924411"></a>Image repository name</p>
</td>
</tr>
<tr id="row177081913132710"><td class="cellrowborder" valign="top" width="23.71%" headers="mcps1.2.5.1.1 "><p id="p167081513102715"><a name="p167081513102715"></a><a name="p167081513102715"></a>access_domain</p>
</td>
<td class="cellrowborder" valign="top" width="14.879999999999999%" headers="mcps1.2.5.1.2 "><p id="p46813432228"><a name="p46813432228"></a><a name="p46813432228"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="26.650000000000002%" headers="mcps1.2.5.1.3 "><p id="p878984854713"><a name="p878984854713"></a><a name="p878984854713"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="34.760000000000005%" headers="mcps1.2.5.1.4 "><p id="p13708313122716"><a name="p13708313122716"></a><a name="p13708313122716"></a>Image sharing domain name</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="s8246d3afdd6f44dc817ce0c3f2ac7d53"></a>

N/A

## Response<a name="sab9be5ce850743859bb238e072f8d1f2"></a>

**Table  2**  Response body parameter description

<a name="table444617282446"></a>
<table><thead align="left"><tr id="row1245012815447"><th class="cellrowborder" valign="top" width="24.63%" id="mcps1.2.4.1.1"><p id="p1545182804417"><a name="p1545182804417"></a><a name="p1545182804417"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.240000000000002%" id="mcps1.2.4.1.2"><p id="p4336150134811"><a name="p4336150134811"></a><a name="p4336150134811"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.13%" id="mcps1.2.4.1.3"><p id="p1845516288440"><a name="p1845516288440"></a><a name="p1845516288440"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row645652824413"><td class="cellrowborder" valign="top" width="24.63%" headers="mcps1.2.4.1.1 "><p id="p2458132854413"><a name="p2458132854413"></a><a name="p2458132854413"></a>exist</p>
</td>
<td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p12459528154411"><a name="p12459528154411"></a><a name="p12459528154411"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.4.1.3 "><p id="p1846115289446"><a name="p1846115289446"></a><a name="p1846115289446"></a><strong id="b82311326204114"><a name="b82311326204114"></a><a name="b82311326204114"></a>true</strong>: exist <strong id="b1891163414113"><a name="b1891163414113"></a><a name="b1891163414113"></a>false</strong>: not exist</p>
</td>
</tr>
<tr id="row799919581432"><td class="cellrowborder" valign="top" width="24.63%" headers="mcps1.2.4.1.1 "><p id="p43401630141910"><a name="p43401630141910"></a><a name="p43401630141910"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p2041912381137"><a name="p2041912381137"></a><a name="p2041912381137"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.4.1.3 "><p id="p20340730191918"><a name="p20340730191918"></a><a name="p20340730191918"></a>Organization.</p>
</td>
</tr>
<tr id="row1998165811311"><td class="cellrowborder" valign="top" width="24.63%" headers="mcps1.2.4.1.1 "><p id="p10980112717192"><a name="p10980112717192"></a><a name="p10980112717192"></a>repository</p>
</td>
<td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p14191338171310"><a name="p14191338171310"></a><a name="p14191338171310"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.4.1.3 "><p id="p14980192714197"><a name="p14980192714197"></a><a name="p14980192714197"></a>Image repository.</p>
</td>
</tr>
<tr id="row139972581836"><td class="cellrowborder" valign="top" width="24.63%" headers="mcps1.2.4.1.1 "><p id="p4111525165410"><a name="p4111525165410"></a><a name="p4111525165410"></a>access_domain</p>
</td>
<td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p7419103815132"><a name="p7419103815132"></a><a name="p7419103815132"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.4.1.3 "><p id="p206025311878"><a name="p206025311878"></a><a name="p206025311878"></a>Name of the domain for image sharing.</p>
</td>
</tr>
<tr id="row899716583314"><td class="cellrowborder" valign="top" width="24.63%" headers="mcps1.2.4.1.1 "><p id="p1568212212204"><a name="p1568212212204"></a><a name="p1568212212204"></a>permit</p>
</td>
<td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p10419538141320"><a name="p10419538141320"></a><a name="p10419538141320"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.4.1.3 "><p id="p1968202192013"><a name="p1968202192013"></a><a name="p1968202192013"></a>Permission.</p>
</td>
</tr>
<tr id="row199616580319"><td class="cellrowborder" valign="top" width="24.63%" headers="mcps1.2.4.1.1 "><p id="p820345065419"><a name="p820345065419"></a><a name="p820345065419"></a>deadline</p>
</td>
<td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1441933861312"><a name="p1441933861312"></a><a name="p1441933861312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.4.1.3 "><p id="p33651491427"><a name="p33651491427"></a><a name="p33651491427"></a>End date.</p>
</td>
</tr>
<tr id="row59959580315"><td class="cellrowborder" valign="top" width="24.63%" headers="mcps1.2.4.1.1 "><p id="p9463481556"><a name="p9463481556"></a><a name="p9463481556"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1241963813133"><a name="p1241963813133"></a><a name="p1241963813133"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.4.1.3 "><p id="p05141147434"><a name="p05141147434"></a><a name="p05141147434"></a>Description.</p>
</td>
</tr>
<tr id="row19955581135"><td class="cellrowborder" valign="top" width="24.63%" headers="mcps1.2.4.1.1 "><p id="p18944193920576"><a name="p18944193920576"></a><a name="p18944193920576"></a>creator_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p4392134851314"><a name="p4392134851314"></a><a name="p4392134851314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.4.1.3 "><p id="p368285415720"><a name="p368285415720"></a><a name="p368285415720"></a>Creator ID.</p>
</td>
</tr>
<tr id="row99941658636"><td class="cellrowborder" valign="top" width="24.63%" headers="mcps1.2.4.1.1 "><p id="p15603531879"><a name="p15603531879"></a><a name="p15603531879"></a>creator_name</p>
</td>
<td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1939244881314"><a name="p1939244881314"></a><a name="p1939244881314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.4.1.3 "><p id="p136038314714"><a name="p136038314714"></a><a name="p136038314714"></a>Name of the creator.</p>
</td>
</tr>
<tr id="row13993175812318"><td class="cellrowborder" valign="top" width="24.63%" headers="mcps1.2.4.1.1 "><p id="p13603531378"><a name="p13603531378"></a><a name="p13603531378"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p239224819132"><a name="p239224819132"></a><a name="p239224819132"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.4.1.3 "><p id="p760315313710"><a name="p760315313710"></a><a name="p760315313710"></a>Time when an image is created, in Coordinated Universal time (UTC). Users need to calculate the offset based on local time. For example, GMT+8 is 8 hours ahead of UTC.</p>
</td>
</tr>
<tr id="row39927581133"><td class="cellrowborder" valign="top" width="24.63%" headers="mcps1.2.4.1.1 "><p id="p14603631778"><a name="p14603631778"></a><a name="p14603631778"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p53927483135"><a name="p53927483135"></a><a name="p53927483135"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.4.1.3 "><p id="p1360316317716"><a name="p1360316317716"></a><a name="p1360316317716"></a>Time when an image is updated, in Coordinated Universal time (UTC). Users need to calculate the offset based on local time. For example, GMT+8 is 8 hours ahead of UTC.</p>
</td>
</tr>
<tr id="row14991458430"><td class="cellrowborder" valign="top" width="24.63%" headers="mcps1.2.4.1.1 "><p id="p427119188502"><a name="p427119188502"></a><a name="p427119188502"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p9392348171312"><a name="p9392348171312"></a><a name="p9392348171312"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="57.13%" headers="mcps1.2.4.1.3 "><p id="p11674184218407"><a name="p11674184218407"></a><a name="p11674184218407"></a>Status. <strong id="b12883187101410"><a name="b12883187101410"></a><a name="b12883187101410"></a>true</strong>: valid <strong id="b18988741412"><a name="b18988741412"></a><a name="b18988741412"></a>false</strong>: expired</p>
</td>
</tr>
</tbody>
</table>

**Response example**

```
{
    "exist": true,
    "namespace": "testns",
    "repository": "test_create1",
    "access_domain": "op_test_swr",
    "permit": "read",
    "deadline": "2019-12-24T16:00:00Z",
    "description": "",
    "creator_id": "3c349daf345649838e99675913000a3f",
    "creator_name": "user01",
    "created": "2019-12-25T08:16:19.550711Z",
    "updated": "2019-12-25T08:16:19.550715Z",
    "status": true
}
```

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
<tbody><tr id="r1cc0192c651444db882dde750b14be23"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="a6a3639a3cb154e17b95c5076c8036471"><a name="a6a3639a3cb154e17b95c5076c8036471"></a><a name="a6a3639a3cb154e17b95c5076c8036471"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="p14504142233912"><a name="p14504142233912"></a><a name="p14504142233912"></a>Query successful.</p>
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
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="aa6fd12cedd8841e29eeeca27c1bdea1a"><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a>Internal error.</p>
</td>
</tr>
</tbody>
</table>

