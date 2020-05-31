# Querying All API Versions<a name="EN-US_TOPIC_0198655134"></a>

## Function<a name="se03aae4436e64394a95dc13b6f233898"></a>

Query all available API versions of SWR.

## URI<a name="s476df674307e4b04b9545f9575dde042"></a>

GET /

## Request<a name="s8246d3afdd6f44dc817ce0c3f2ac7d53"></a>

N/A

## Response<a name="sab9be5ce850743859bb238e072f8d1f2"></a>

**Response parameters**

**Table  1**  Response body parameter description

<a name="table1585555623716"></a>
<table><thead align="left"><tr id="row18561356203713"><th class="cellrowborder" valign="top" width="21.52215221522152%" id="mcps1.2.4.1.1"><p id="p20856135619375"><a name="p20856135619375"></a><a name="p20856135619375"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.65196519651965%" id="mcps1.2.4.1.2"><p id="p3856105610372"><a name="p3856105610372"></a><a name="p3856105610372"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.825882588258814%" id="mcps1.2.4.1.3"><p id="p6856956203719"><a name="p6856956203719"></a><a name="p6856956203719"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18561356173718"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p1985685653718"><a name="p1985685653718"></a><a name="p1985685653718"></a>versions</p>
</td>
<td class="cellrowborder" valign="top" width="19.65196519651965%" headers="mcps1.2.4.1.2 "><p id="p585645612379"><a name="p585645612379"></a><a name="p585645612379"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="58.825882588258814%" headers="mcps1.2.4.1.3 "><p id="p28568564370"><a name="p28568564370"></a><a name="p28568564370"></a>A list of objects related to the version. For details, see <a href="#table45446245174724">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  versions parameter description

<a name="table45446245174724"></a>
<table><thead align="left"><tr id="row1412623174724"><th class="cellrowborder" valign="top" width="21.52215221522152%" id="mcps1.2.4.1.1"><p id="p47313663174724"><a name="p47313663174724"></a><a name="p47313663174724"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.65196519651965%" id="mcps1.2.4.1.2"><p id="p7201512174724"><a name="p7201512174724"></a><a name="p7201512174724"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.825882588258814%" id="mcps1.2.4.1.3"><p id="p4480706174724"><a name="p4480706174724"></a><a name="p4480706174724"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row98876365819"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p1440645517302"><a name="p1440645517302"></a><a name="p1440645517302"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="19.65196519651965%" headers="mcps1.2.4.1.2 "><p id="p540675519302"><a name="p540675519302"></a><a name="p540675519302"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.825882588258814%" headers="mcps1.2.4.1.3 "><p id="p15406115518308"><a name="p15406115518308"></a><a name="p15406115518308"></a>Version ID (version number), for example, v2.</p>
</td>
</tr>
<tr id="row3367184810392"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p14406755103013"><a name="p14406755103013"></a><a name="p14406755103013"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="19.65196519651965%" headers="mcps1.2.4.1.2 "><p id="p17406855153012"><a name="p17406855153012"></a><a name="p17406855153012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.825882588258814%" headers="mcps1.2.4.1.3 "><p id="p13406195533010"><a name="p13406195533010"></a><a name="p13406195533010"></a>API URL.</p>
</td>
</tr>
<tr id="row626682835815"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p1891845543117"><a name="p1891845543117"></a><a name="p1891845543117"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="19.65196519651965%" headers="mcps1.2.4.1.2 "><p id="p1491805516316"><a name="p1491805516316"></a><a name="p1491805516316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.825882588258814%" headers="mcps1.2.4.1.3 "><p id="p59181855123117"><a name="p59181855123117"></a><a name="p59181855123117"></a>If the APIs of this version support microversions, set this parameter to the supported maximum microversion. If the microversion is not supported, leave this parameter blank.</p>
</td>
</tr>
<tr id="row1272510338318"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p69181655183119"><a name="p69181655183119"></a><a name="p69181655183119"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="19.65196519651965%" headers="mcps1.2.4.1.2 "><p id="p191855553110"><a name="p191855553110"></a><a name="p191855553110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.825882588258814%" headers="mcps1.2.4.1.3 "><p id="p791815513111"><a name="p791815513111"></a><a name="p791815513111"></a>Version status. The options are as follows:</p>
<p id="p14919135517310"><a name="p14919135517310"></a><a name="p14919135517310"></a><strong id="b1842114154125"><a name="b1842114154125"></a><a name="b1842114154125"></a>CURRENT</strong>: The version is the primary version.</p>
<p id="p169191555103116"><a name="p169191555103116"></a><a name="p169191555103116"></a><strong id="b1691692111128"><a name="b1691692111128"></a><a name="b1691692111128"></a>SUPPORTED</strong>: The version is an earlier version, but it is still supported.</p>
<p id="p149191355173117"><a name="p149191355173117"></a><a name="p149191355173117"></a><strong id="b13548842151216"><a name="b13548842151216"></a><a name="b13548842151216"></a>DEPRECATED</strong>: The version is a deprecated version, which may be deleted later.</p>
</td>
</tr>
<tr id="row11746173743119"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p15919145533117"><a name="p15919145533117"></a><a name="p15919145533117"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="19.65196519651965%" headers="mcps1.2.4.1.2 "><p id="p791917552312"><a name="p791917552312"></a><a name="p791917552312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.825882588258814%" headers="mcps1.2.4.1.3 "><p id="p7919195503119"><a name="p7919195503119"></a><a name="p7919195503119"></a>Version release time, in Coordinated Universal time (UTC). For example, the release time of v1 is 2014-06-28T12:20:21Z.</p>
</td>
</tr>
<tr id="row14580164713313"><td class="cellrowborder" valign="top" width="21.52215221522152%" headers="mcps1.2.4.1.1 "><p id="p791995515312"><a name="p791995515312"></a><a name="p791995515312"></a>min_version</p>
</td>
<td class="cellrowborder" valign="top" width="19.65196519651965%" headers="mcps1.2.4.1.2 "><p id="p18919155511315"><a name="p18919155511315"></a><a name="p18919155511315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.825882588258814%" headers="mcps1.2.4.1.3 "><p id="p6919195518313"><a name="p6919195518313"></a><a name="p6919195518313"></a>If APIs of this version support microversions, set this parameter to the supported minimum microversion. If the microversion is not supported, leave this parameter empty.</p>
</td>
</tr>
</tbody>
</table>

**Response example**

```
{ 
   "versions": [
        {
            "id": "v2",
            "links": [
                {
                    "href": "https://xxxx.otc.t-systems.com/v2/",
                    "rel": "self"
                }
            ],
            "min_version": "2.0",
            "status": "CURRENT",
            "updated": "2017-12-09T00:00:00Z",
            "version": "2.26",
        }
    ]

}
```

## Status Code<a name="s336c1dbc7af446a1b3cc077ea3f82fc9"></a>

For details, see  [Table 3](#t33d02fa79e8443868a71c99f411610a5).

**Table  3**  Status Code

<a name="t33d02fa79e8443868a71c99f411610a5"></a>
<table><thead align="left"><tr id="r9eb80d64e8f34d0db940daa95fc929dd"><th class="cellrowborder" valign="top" width="16.439999999999998%" id="mcps1.2.3.1.1"><p id="a7e51ed73a71e4dc29d0dd4aae3016632"><a name="a7e51ed73a71e4dc29d0dd4aae3016632"></a><a name="a7e51ed73a71e4dc29d0dd4aae3016632"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83.56%" id="mcps1.2.3.1.2"><p id="aa802d02e21c944f1863435a0d11c7ec1"><a name="aa802d02e21c944f1863435a0d11c7ec1"></a><a name="aa802d02e21c944f1863435a0d11c7ec1"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r1cc0192c651444db882dde750b14be23"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="a6a3639a3cb154e17b95c5076c8036471"><a name="a6a3639a3cb154e17b95c5076c8036471"></a><a name="a6a3639a3cb154e17b95c5076c8036471"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="p14504142233912"><a name="p14504142233912"></a><a name="p14504142233912"></a>Request successful.</p>
</td>
</tr>
<tr id="r19bdef782c164c93917f897241e521f8"><td class="cellrowborder" valign="top" width="16.439999999999998%" headers="mcps1.2.3.1.1 "><p id="a7da68e311c0f4267bacf3cbdb71d1ead"><a name="a7da68e311c0f4267bacf3cbdb71d1ead"></a><a name="a7da68e311c0f4267bacf3cbdb71d1ead"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="83.56%" headers="mcps1.2.3.1.2 "><p id="aa6fd12cedd8841e29eeeca27c1bdea1a"><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a><a name="aa6fd12cedd8841e29eeeca27c1bdea1a"></a>Internal error.</p>
</td>
</tr>
</tbody>
</table>

