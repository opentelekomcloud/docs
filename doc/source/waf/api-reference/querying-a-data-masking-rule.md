# Querying a Data Masking Rule<a name="EN-US_TOPIC_0193631190"></a>

## Function Description<a name="section7310871"></a>

This API is used to query details about a data masking rule.

## URI<a name="section65797845"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/privacy/\{privacy\_rule\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table31166170"></a>
    <table><thead align="left"><tr id="row55464205"><th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.5.1.1"><p id="p63415654"><a name="p63415654"></a><a name="p63415654"></a><strong id="b135931292014"><a name="b135931292014"></a><a name="b135931292014"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.2"><p id="p36394355"><a name="p36394355"></a><a name="p36394355"></a><strong id="b156162492011"><a name="b156162492011"></a><a name="b156162492011"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.2.5.1.3"><p id="p62261661"><a name="p62261661"></a><a name="p62261661"></a><strong id="b23477619201"><a name="b23477619201"></a><a name="b23477619201"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p10029771"><a name="p10029771"></a><a name="p10029771"></a><strong id="b14331513162019"><a name="b14331513162019"></a><a name="b14331513162019"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7105126"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p38644309"><a name="p38644309"></a><a name="p38644309"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p43181313"><a name="p43181313"></a><a name="p43181313"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p8025425"><a name="p8025425"></a><a name="p8025425"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p46079661"><a name="p46079661"></a><a name="p46079661"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row12063772"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p37641462"><a name="p37641462"></a><a name="p37641462"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p29059601"><a name="p29059601"></a><a name="p29059601"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p5017493"><a name="p5017493"></a><a name="p5017493"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p3763752"><a name="p3763752"></a><a name="p3763752"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row33873776"><td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.1 "><p id="p59421344"><a name="p59421344"></a><a name="p59421344"></a>privacy_rule_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.2 "><p id="p48399540"><a name="p48399540"></a><a name="p48399540"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.2.5.1.3 "><p id="p28048661"><a name="p28048661"></a><a name="p28048661"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p57349034"><a name="p57349034"></a><a name="p57349034"></a>Specifies the ID of a data masking rule.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section55309694"></a>

Request parameters

None

## Response<a name="section28025205"></a>

Response parameters

**Table  2**  Parameter description

<a name="table3291956"></a>
<table><thead align="left"><tr id="row19779383"><th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.4.1.1"><p id="p58626204"><a name="p58626204"></a><a name="p58626204"></a><strong id="b38981333192118"><a name="b38981333192118"></a><a name="b38981333192118"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.4.1.2"><p id="p51102069"><a name="p51102069"></a><a name="p51102069"></a><strong id="b82268375219"><a name="b82268375219"></a><a name="b82268375219"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p45626923"><a name="p45626923"></a><a name="p45626923"></a><strong id="b565453917219"><a name="b565453917219"></a><a name="b565453917219"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row7989124"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p43139279"><a name="p43139279"></a><a name="p43139279"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p4620715"><a name="p4620715"></a><a name="p4620715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p38733631"><a name="p38733631"></a><a name="p38733631"></a>Specifies the ID of a data masking rule.</p>
</td>
</tr>
<tr id="row13058366"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p51094746"><a name="p51094746"></a><a name="p51094746"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p45033795"><a name="p45033795"></a><a name="p45033795"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p23858784"><a name="p23858784"></a><a name="p23858784"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row13402470"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p11858285"><a name="p11858285"></a><a name="p11858285"></a>path</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p20997020"><a name="p20997020"></a><a name="p20997020"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p23037084"><a name="p23037084"></a><a name="p23037084"></a>Specifies the URL to which the data masking rule applies (exact match by default).</p>
</td>
</tr>
<tr id="row6007170"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p16818750"><a name="p16818750"></a><a name="p16818750"></a>category</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p20141470"><a name="p20141470"></a><a name="p20141470"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p20846346"><a name="p20846346"></a><a name="p20846346"></a>Specifies the masked field. The options are <strong id="b1195911193315"><a name="b1195911193315"></a><a name="b1195911193315"></a>params</strong> and <strong id="b15958113334"><a name="b15958113334"></a><a name="b15958113334"></a>header</strong>.</p>
</td>
</tr>
<tr id="row53399393"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p30383563"><a name="p30383563"></a><a name="p30383563"></a>index</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p45149558"><a name="p45149558"></a><a name="p45149558"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p33235594"><a name="p33235594"></a><a name="p33235594"></a>Specifies the masked subfield.</p>
</td>
</tr>
<tr id="row30684890"><td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.4.1.1 "><p id="p2448157"><a name="p2448157"></a><a name="p2448157"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p64083037"><a name="p64083037"></a><a name="p64083037"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p12128762"><a name="p12128762"></a><a name="p12128762"></a>Specifies the time when a data masking rule is added.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section23831157906"></a>

Rule ID  **e1c0e55865544d1f8c95cf71df108c6b**  is used as an example.

Response example

```
{
  "id": "e1c0e55865544d1f8c95cf71df108c6b",
  "policy_id": "yuc0e55865544d1f8c95cf71df108c6b",
  "path": "/login",
  "category": "params",
  "index": "password",
  "timestamp": 12324435345
}
```

## Status Code<a name="section50900258"></a>

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

