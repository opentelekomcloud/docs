# Querying the Total Number of Requests per Second<a name="EN-US_TOPIC_0193631168"></a>

## Function Description<a name="section24663769"></a>

This API is used to query the total number of requests per second.

## URI<a name="section51608295"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/event/request/peak?from=\{from\}&to=\{to\}&hosts=\{hostids\}

    >![](/images/icon-note.gif) **NOTE:**   
    >An example of a URI is as follows:  
    >GET  /v1/3ac26c59e15a4a11bb680a103a29ddb6/waf/event/attack/type?from=1543976973635&to=1563976973635&hosts=3211757cafa3437aae24d760022e79ba&hosts=93029844064b43739b51ca63036fbc4b&hosts=34fe5f5c60ef4e43a9975296765d1217  

-   Parameter description

    **Table  1**  Path parameters

    <a name="table7676484"></a>
    <table><thead align="left"><tr id="row53791928"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p62178935"><a name="p62178935"></a><a name="p62178935"></a><strong id="b47578335273"><a name="b47578335273"></a><a name="b47578335273"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p3328970"><a name="p3328970"></a><a name="p3328970"></a><strong id="b1288643514271"><a name="b1288643514271"></a><a name="b1288643514271"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p1211162"><a name="p1211162"></a><a name="p1211162"></a><strong id="b11479370279"><a name="b11479370279"></a><a name="b11479370279"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p30995278"><a name="p30995278"></a><a name="p30995278"></a><strong id="b557993862713"><a name="b557993862713"></a><a name="b557993862713"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row27589583"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p20163716"><a name="p20163716"></a><a name="p20163716"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p22648277"><a name="p22648277"></a><a name="p22648277"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p22571180"><a name="p22571180"></a><a name="p22571180"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p16326254"><a name="p16326254"></a><a name="p16326254"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row12718564"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p23570740"><a name="p23570740"></a><a name="p23570740"></a>from</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p30181797"><a name="p30181797"></a><a name="p30181797"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p629819401359"><a name="p629819401359"></a><a name="p629819401359"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p18857034"><a name="p18857034"></a><a name="p18857034"></a>Specifies the start time (UTC) in milliseconds. For example, <strong id="b755774118549"><a name="b755774118549"></a><a name="b755774118549"></a>1548172800000</strong>.</p>
    </td>
    </tr>
    <tr id="row22044242519"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p1820412246510"><a name="p1820412246510"></a><a name="p1820412246510"></a>to</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p74981428751"><a name="p74981428751"></a><a name="p74981428751"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p918445753"><a name="p918445753"></a><a name="p918445753"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p1020414242511"><a name="p1020414242511"></a><a name="p1020414242511"></a>Specifies the end time (UTC) in milliseconds. For example, <strong id="b949424855410"><a name="b949424855410"></a><a name="b949424855410"></a>1548431999000</strong>.</p>
    </td>
    </tr>
    <tr id="row61969231"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p53451813"><a name="p53451813"></a><a name="p53451813"></a>hosts</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p34629567"><a name="p34629567"></a><a name="p34629567"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p53531525"><a name="p53531525"></a><a name="p53531525"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p41086305"><a name="p41086305"></a><a name="p41086305"></a>Specifies the domain IDs.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section61821472"></a>

Request parameters

None

## Response<a name="section19522341"></a>

Response parameters

**Table  2**  Parameter description

<a name="table595532713613"></a>
<table><thead align="left"><tr id="row095519271617"><th class="cellrowborder" valign="top" width="20.142014201420142%" id="mcps1.2.4.1.1"><p id="p17955827167"><a name="p17955827167"></a><a name="p17955827167"></a><strong id="b174431848103910"><a name="b174431848103910"></a><a name="b174431848103910"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.761676167616763%" id="mcps1.2.4.1.2"><p id="p99551271569"><a name="p99551271569"></a><a name="p99551271569"></a><strong id="b82804507394"><a name="b82804507394"></a><a name="b82804507394"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="63.0963096309631%" id="mcps1.2.4.1.3"><p id="p995522713617"><a name="p995522713617"></a><a name="p995522713617"></a><strong id="b131611852133910"><a name="b131611852133910"></a><a name="b131611852133910"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2955927862"><td class="cellrowborder" valign="top" width="20.142014201420142%" headers="mcps1.2.4.1.1 "><p id="p9955427764"><a name="p9955427764"></a><a name="p9955427764"></a>qps</p>
</td>
<td class="cellrowborder" valign="top" width="16.761676167616763%" headers="mcps1.2.4.1.2 "><p id="p29557271764"><a name="p29557271764"></a><a name="p29557271764"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="63.0963096309631%" headers="mcps1.2.4.1.3 "><p id="p1095518271362"><a name="p1095518271362"></a><a name="p1095518271362"></a>Specifies the total number of requests per second.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section65815403158"></a>

Response example

```
{
"qps": 800
}
```

## Status Code<a name="section41483341"></a>

[Table 3](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  3**  Status code

<a name="en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0"></a>
<table><thead align="left"><tr id="en-us_topic_0193631139_r3d6e2f205c444705bdbb9daaac74e575"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"><a name="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"></a><a name="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="19.41%" id="mcps1.2.4.1.2"><p id="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"><a name="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"></a><a name="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"></a>Meaning</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0193631139_rc7b2adc390904a1ba79e303017797786"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"><a name="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"></a><a name="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="19.41%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"></a>The request has succeeded.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

