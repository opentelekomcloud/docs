# Querying the Number of Attack Source IP Addresses<a name="EN-US_TOPIC_0193631164"></a>

## Function Description<a name="section16144219"></a>

This API is used to query the number of attack source IP addresses.

## URI<a name="section32613372"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/event/attack/source/num?from=\{from\}&to=\{to\}&hosts=\{hostids\}

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >An example of a URI is as follows:  
    >GET  /v1/3ac26c59e15a4a11bb680a103a29ddb6/waf/event/attack/type?from=1543976973635&to=1563976973635&hosts=3211757cafa3437aae24d760022e79ba&hosts=93029844064b43739b51ca63036fbc4b&hosts=34fe5f5c60ef4e43a9975296765d1217  

-   Parameter description

    **Table  1**  Path parameters

    <a name="table9130325"></a>
    <table><thead align="left"><tr id="row45600051"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p2616641"><a name="p2616641"></a><a name="p2616641"></a><strong id="b1691123262310"><a name="b1691123262310"></a><a name="b1691123262310"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p10621372"><a name="p10621372"></a><a name="p10621372"></a><strong id="b6820173452315"><a name="b6820173452315"></a><a name="b6820173452315"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p55024779"><a name="p55024779"></a><a name="p55024779"></a><strong id="b112581364234"><a name="b112581364234"></a><a name="b112581364234"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p27822103"><a name="p27822103"></a><a name="p27822103"></a><strong id="b6933103714232"><a name="b6933103714232"></a><a name="b6933103714232"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row38997831"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p4707715"><a name="p4707715"></a><a name="p4707715"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p45780660"><a name="p45780660"></a><a name="p45780660"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p17246018"><a name="p17246018"></a><a name="p17246018"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p54750228"><a name="p54750228"></a><a name="p54750228"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row22990011"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p50251566"><a name="p50251566"></a><a name="p50251566"></a>from</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p43845083"><a name="p43845083"></a><a name="p43845083"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p1276012911412"><a name="p1276012911412"></a><a name="p1276012911412"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p18857034"><a name="p18857034"></a><a name="p18857034"></a>Specifies the start time (UTC) in milliseconds. For example, <strong id="b10317144410533"><a name="b10317144410533"></a><a name="b10317144410533"></a>1548172800000</strong>.</p>
    </td>
    </tr>
    <tr id="row13491151514416"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p3492715246"><a name="p3492715246"></a><a name="p3492715246"></a>to</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p1839312220411"><a name="p1839312220411"></a><a name="p1839312220411"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p1149251513416"><a name="p1149251513416"></a><a name="p1149251513416"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p94921715348"><a name="p94921715348"></a><a name="p94921715348"></a>Specifies the end time (UTC) in milliseconds. For example, <strong id="b136124716534"><a name="b136124716534"></a><a name="b136124716534"></a>1548431999000</strong>.</p>
    </td>
    </tr>
    <tr id="row15463147"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p44555360"><a name="p44555360"></a><a name="p44555360"></a>hosts</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p52214385"><a name="p52214385"></a><a name="p52214385"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p1506824"><a name="p1506824"></a><a name="p1506824"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p54943882"><a name="p54943882"></a><a name="p54943882"></a>Specifies the domain IDs.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section25084896"></a>

Request parameters

None

## Response<a name="section24437477"></a>

Response parameters

**Table  2**  Parameter description

<a name="table17379311124"></a>
<table><thead align="left"><tr id="row123773119126"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p62178935"><a name="p62178935"></a><a name="p62178935"></a><strong id="b25931823512"><a name="b25931823512"></a><a name="b25931823512"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p3371131171212"><a name="p3371131171212"></a><a name="p3371131171212"></a><strong id="b13227111113517"><a name="b13227111113517"></a><a name="b13227111113517"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p33710314125"><a name="p33710314125"></a><a name="p33710314125"></a><strong id="b13812912123512"><a name="b13812912123512"></a><a name="b13812912123512"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row11374310121"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p237731191211"><a name="p237731191211"></a><a name="p237731191211"></a>sip</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p437193151210"><a name="p437193151210"></a><a name="p437193151210"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p737331201219"><a name="p737331201219"></a><a name="p737331201219"></a>Specifies the number of attack source IP addresses.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1880600111519"></a>

Response example

```
{
  "sip":  50
}
```

## Status Code<a name="section18610709"></a>

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

