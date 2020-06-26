# Deleting a Web Tamper Protection Rule<a name="EN-US_TOPIC_0193631152"></a>

## Function Description<a name="section17488634"></a>

This API is used to delete a web tamper protection rule.

## URI<a name="section23179978"></a>

-   URI format

    DELETE  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/antitamper/\{antitamper\_rule\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table29468588"></a>
    <table><thead align="left"><tr id="row5786662"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p66066498"><a name="p66066498"></a><a name="p66066498"></a><strong id="b260234213536"><a name="b260234213536"></a><a name="b260234213536"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p49786155"><a name="p49786155"></a><a name="p49786155"></a><strong id="b13409134555316"><a name="b13409134555316"></a><a name="b13409134555316"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p6146760"><a name="p6146760"></a><a name="p6146760"></a><strong id="b39631463531"><a name="b39631463531"></a><a name="b39631463531"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p28125570"><a name="p28125570"></a><a name="p28125570"></a><strong id="b7799348145313"><a name="b7799348145313"></a><a name="b7799348145313"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63578688"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p49600107"><a name="p49600107"></a><a name="p49600107"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p58185706"><a name="p58185706"></a><a name="p58185706"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p15421734"><a name="p15421734"></a><a name="p15421734"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p41200902"><a name="p41200902"></a><a name="p41200902"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row35263799"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p37795465"><a name="p37795465"></a><a name="p37795465"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p41533811"><a name="p41533811"></a><a name="p41533811"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p8795550"><a name="p8795550"></a><a name="p8795550"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p41350962"><a name="p41350962"></a><a name="p41350962"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row36614338"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p12971397"><a name="p12971397"></a><a name="p12971397"></a>antitamper_rule_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p44050245"><a name="p44050245"></a><a name="p44050245"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p11300073"><a name="p11300073"></a><a name="p11300073"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p42890714"><a name="p42890714"></a><a name="p42890714"></a>Specifies the ID of a web tamper protection rule.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section7293212"></a>

Request parameters

None

## Response<a name="section65638914"></a>

Response parameters

None

## Status Code<a name="section53879315"></a>

[Table 2](#en-us_topic_0193631187_en-us_topic_0148832986_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  2**  Status code

<a name="en-us_topic_0193631187_en-us_topic_0148832986_t82c3440f3efb42a38b9d4dc4011a33d0"></a>
<table><thead align="left"><tr id="en-us_topic_0193631187_en-us_topic_0148832986_r3d6e2f205c444705bdbb9daaac74e575"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0193631187_en-us_topic_0148832986_af3c4073076f24eca88d94e3fa1effdc6"><a name="en-us_topic_0193631187_en-us_topic_0148832986_af3c4073076f24eca88d94e3fa1effdc6"></a><a name="en-us_topic_0193631187_en-us_topic_0148832986_af3c4073076f24eca88d94e3fa1effdc6"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="19.41%" id="mcps1.2.4.1.2"><p id="en-us_topic_0193631187_en-us_topic_0148832986_en-us_topic_0144911667_p4531342288"><a name="en-us_topic_0193631187_en-us_topic_0148832986_en-us_topic_0144911667_p4531342288"></a><a name="en-us_topic_0193631187_en-us_topic_0148832986_en-us_topic_0144911667_p4531342288"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0193631187_en-us_topic_0148832986_ada185614bba24140995b8123b3e9faa8"><a name="en-us_topic_0193631187_en-us_topic_0148832986_ada185614bba24140995b8123b3e9faa8"></a><a name="en-us_topic_0193631187_en-us_topic_0148832986_ada185614bba24140995b8123b3e9faa8"></a>Meaning</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0193631187_en-us_topic_0148832986_rc7b2adc390904a1ba79e303017797786"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0193631187_en-us_topic_0148832986_a93f3895d44bb4226934cc626ac50e37b"><a name="en-us_topic_0193631187_en-us_topic_0148832986_a93f3895d44bb4226934cc626ac50e37b"></a><a name="en-us_topic_0193631187_en-us_topic_0148832986_a93f3895d44bb4226934cc626ac50e37b"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="19.41%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0193631187_en-us_topic_0148832986_en-us_topic_0144911667_p7538425819"><a name="en-us_topic_0193631187_en-us_topic_0148832986_en-us_topic_0144911667_p7538425819"></a><a name="en-us_topic_0193631187_en-us_topic_0148832986_en-us_topic_0144911667_p7538425819"></a>No Content</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0193631187_en-us_topic_0148832986_en-us_topic_0144911667_p369874114414"><a name="en-us_topic_0193631187_en-us_topic_0148832986_en-us_topic_0144911667_p369874114414"></a><a name="en-us_topic_0193631187_en-us_topic_0148832986_en-us_topic_0144911667_p369874114414"></a>The server successfully processed the request and is not returning any content.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

