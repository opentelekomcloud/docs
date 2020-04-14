# Deleting a CC Attack Protection Rule<a name="EN-US_TOPIC_0193631188"></a>

## Function Description<a name="section37231090"></a>

This API is used to delete a CC attack protection rule.

## URI<a name="section66644355"></a>

-   URI format

    DELETE  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/cc/\{ccrule\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table18987003"></a>
    <table><thead align="left"><tr id="row50238956"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p42823667"><a name="p42823667"></a><a name="p42823667"></a><strong id="b42121947182717"><a name="b42121947182717"></a><a name="b42121947182717"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p46164965"><a name="p46164965"></a><a name="p46164965"></a><strong id="b83254481273"><a name="b83254481273"></a><a name="b83254481273"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p48374700"><a name="p48374700"></a><a name="p48374700"></a><strong id="b07976493275"><a name="b07976493275"></a><a name="b07976493275"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p26036656"><a name="p26036656"></a><a name="p26036656"></a><strong id="b738045118271"><a name="b738045118271"></a><a name="b738045118271"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row28594392"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p34444429"><a name="p34444429"></a><a name="p34444429"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p38535350"><a name="p38535350"></a><a name="p38535350"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p34355644"><a name="p34355644"></a><a name="p34355644"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p31343750"><a name="p31343750"></a><a name="p31343750"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row13658296"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p32580196"><a name="p32580196"></a><a name="p32580196"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p21750216"><a name="p21750216"></a><a name="p21750216"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p16937101"><a name="p16937101"></a><a name="p16937101"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p29727963"><a name="p29727963"></a><a name="p29727963"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row66225076"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p62630945"><a name="p62630945"></a><a name="p62630945"></a>ccrule_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p39941803"><a name="p39941803"></a><a name="p39941803"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p14060601"><a name="p14060601"></a><a name="p14060601"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p65166900"><a name="p65166900"></a><a name="p65166900"></a>Specifies the ID of a CC attack protection rule.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section62928286"></a>

Request parameters

None

## Response<a name="section29483669"></a>

Response parameters

None

## Status Code<a name="section64026431"></a>

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

