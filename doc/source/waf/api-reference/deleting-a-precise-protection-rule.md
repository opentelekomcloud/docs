# Deleting a Precise Protection Rule<a name="EN-US_TOPIC_0193631165"></a>

## Function Description<a name="section31889035"></a>

This API is used to delete a precise protection rule.

## URI<a name="section18565866"></a>

-   URI format

    DELETE  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/custom/\{custom\_rule\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table33937262"></a>
    <table><thead align="left"><tr id="row33875949"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p59597335"><a name="p59597335"></a><a name="p59597335"></a><strong id="b1168148194210"><a name="b1168148194210"></a><a name="b1168148194210"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p62654850"><a name="p62654850"></a><a name="p62654850"></a><strong id="b17391135119427"><a name="b17391135119427"></a><a name="b17391135119427"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p41878102"><a name="p41878102"></a><a name="p41878102"></a><strong id="b168591554134215"><a name="b168591554134215"></a><a name="b168591554134215"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p36683065"><a name="p36683065"></a><a name="p36683065"></a><strong id="b7290341544"><a name="b7290341544"></a><a name="b7290341544"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18538326"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p25209427"><a name="p25209427"></a><a name="p25209427"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p28697688"><a name="p28697688"></a><a name="p28697688"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p42811406"><a name="p42811406"></a><a name="p42811406"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p45171868"><a name="p45171868"></a><a name="p45171868"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row3893636"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p46949131"><a name="p46949131"></a><a name="p46949131"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p44783229"><a name="p44783229"></a><a name="p44783229"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p3562948"><a name="p3562948"></a><a name="p3562948"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p20163400"><a name="p20163400"></a><a name="p20163400"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row47252876"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p2277749"><a name="p2277749"></a><a name="p2277749"></a>custom_rule_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p50280015"><a name="p50280015"></a><a name="p50280015"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p46149442"><a name="p46149442"></a><a name="p46149442"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p47117301"><a name="p47117301"></a><a name="p47117301"></a>Specifies the ID of a precise protection rule.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section32875072"></a>

Request parameters

None

## Response<a name="section27440198"></a>

Response parameters

None

## Status Code<a name="section45635198"></a>

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

