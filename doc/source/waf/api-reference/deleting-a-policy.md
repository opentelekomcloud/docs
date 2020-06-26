# Deleting a Policy<a name="EN-US_TOPIC_0193631118"></a>

## Function Description<a name="section18356467"></a>

This API is used to delete a policy.

## URI<a name="section30990477"></a>

-   URI format

    DELETE  /v1/\{project\_id\}/waf/policy/\{policy\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table11432709"></a>
    <table><thead align="left"><tr id="row47112728"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p58034622"><a name="p58034622"></a><a name="p58034622"></a><strong id="b166193443118"><a name="b166193443118"></a><a name="b166193443118"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p3183912"><a name="p3183912"></a><a name="p3183912"></a><strong id="b223810359311"><a name="b223810359311"></a><a name="b223810359311"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p56570302"><a name="p56570302"></a><a name="p56570302"></a><strong id="b20989143618317"><a name="b20989143618317"></a><a name="b20989143618317"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p18791786"><a name="p18791786"></a><a name="p18791786"></a><strong id="b1370843783110"><a name="b1370843783110"></a><a name="b1370843783110"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45739665"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p13925405"><a name="p13925405"></a><a name="p13925405"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p54216054"><a name="p54216054"></a><a name="p54216054"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p29424259"><a name="p29424259"></a><a name="p29424259"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p34554797"><a name="p34554797"></a><a name="p34554797"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row42557720"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p24623287"><a name="p24623287"></a><a name="p24623287"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p48329255"><a name="p48329255"></a><a name="p48329255"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p22355600"><a name="p22355600"></a><a name="p22355600"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p65973145"><a name="p65973145"></a><a name="p65973145"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section10478839"></a>

Request parameters

None

## Response<a name="section27200690"></a>

Response parameters

None

## Status Code<a name="section43479624"></a>

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

