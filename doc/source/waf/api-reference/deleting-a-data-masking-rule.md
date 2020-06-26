# Deleting a Data Masking Rule<a name="EN-US_TOPIC_0193631130"></a>

## Function Description<a name="section42072185"></a>

This API is used to delete a data masking rule.

## URI<a name="section43105347"></a>

-   URI format

    DELETE  /v1/\{project\_id\}/waf/policy/\{policy\_id\}/privacy/\{privacy\_rule\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table63108286"></a>
    <table><thead align="left"><tr id="row45128200"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p31505563"><a name="p31505563"></a><a name="p31505563"></a><strong id="b14350181691614"><a name="b14350181691614"></a><a name="b14350181691614"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p1813782"><a name="p1813782"></a><a name="p1813782"></a><strong id="b34653181168"><a name="b34653181168"></a><a name="b34653181168"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p12698658"><a name="p12698658"></a><a name="p12698658"></a><strong id="b69313213161"><a name="b69313213161"></a><a name="b69313213161"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p21958374"><a name="p21958374"></a><a name="p21958374"></a><strong id="b7633623191613"><a name="b7633623191613"></a><a name="b7633623191613"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33797899"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p53275321"><a name="p53275321"></a><a name="p53275321"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p20333719"><a name="p20333719"></a><a name="p20333719"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p36418509"><a name="p36418509"></a><a name="p36418509"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p64218116"><a name="p64218116"></a><a name="p64218116"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row41092135"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p40128642"><a name="p40128642"></a><a name="p40128642"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p29194545"><a name="p29194545"></a><a name="p29194545"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p15947933"><a name="p15947933"></a><a name="p15947933"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p16714157"><a name="p16714157"></a><a name="p16714157"></a>Specifies the policy ID.</p>
    </td>
    </tr>
    <tr id="row16209686"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p37916184"><a name="p37916184"></a><a name="p37916184"></a>privacy_rule_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p51312050"><a name="p51312050"></a><a name="p51312050"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p62635405"><a name="p62635405"></a><a name="p62635405"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p40303057"><a name="p40303057"></a><a name="p40303057"></a>Specifies the ID of a data masking rule.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section52403806"></a>

Request parameters

None

## Response<a name="section1872212"></a>

Response parameters

None

## Status Code<a name="section16849908"></a>

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

