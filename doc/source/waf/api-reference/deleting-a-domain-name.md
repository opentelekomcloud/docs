# Deleting a Domain Name<a name="EN-US_TOPIC_0193631187"></a>

## Function Description<a name="section12424902"></a>

This API is used to delete a domain name.

>![](/images/icon-notice.gif) **NOTICE:**   
>Deleting a domain name relies on some components, such as DNS. These components may cause deletion failed.  

## URI<a name="section44715260"></a>

-   URI format

    DELETE  /v1/\{project\_id\}/waf/instance/\{instance\_id\}?keepPolicy=\{keepPolicy\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table39367534"></a>
    <table><thead align="left"><tr id="row49918595"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p16874366"><a name="p16874366"></a><a name="p16874366"></a><strong id="b8423192211398"><a name="b8423192211398"></a><a name="b8423192211398"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p24646410"><a name="p24646410"></a><a name="p24646410"></a><strong id="b16189237395"><a name="b16189237395"></a><a name="b16189237395"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p50202190"><a name="p50202190"></a><a name="p50202190"></a><strong id="b1269720245393"><a name="b1269720245393"></a><a name="b1269720245393"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p39845619"><a name="p39845619"></a><a name="p39845619"></a><strong id="b1847822510391"><a name="b1847822510391"></a><a name="b1847822510391"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6269729"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p38086015"><a name="p38086015"></a><a name="p38086015"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p65068341"><a name="p65068341"></a><a name="p65068341"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p36044268"><a name="p36044268"></a><a name="p36044268"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p33904587"><a name="p33904587"></a><a name="p33904587"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row36705834"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p20382553"><a name="p20382553"></a><a name="p20382553"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p40374085"><a name="p40374085"></a><a name="p40374085"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p49075413"><a name="p49075413"></a><a name="p49075413"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p15685489"><a name="p15685489"></a><a name="p15685489"></a>Specifies the instance ID or domain ID.</p>
    </td>
    </tr>
    <tr id="row6951680"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p26215194"><a name="p26215194"></a><a name="p26215194"></a>keepPolicy</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p43055989"><a name="p43055989"></a><a name="p43055989"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p64983097"><a name="p64983097"></a><a name="p64983097"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p672111566452"><a name="p672111566452"></a><a name="p672111566452"></a>Specifies whether to retain the policy when deleting a domain name.</p>
    <a name="ul1933512313463"></a><a name="ul1933512313463"></a><ul id="ul1933512313463"><li><strong id="b17569128921"><a name="b17569128921"></a><a name="b17569128921"></a>true</strong>: The policy is retained.</li><li><strong id="b17744181816213"><a name="b17744181816213"></a><a name="b17744181816213"></a>false</strong>: The policy is deleted.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section66893020"></a>

Request parameters

None

## Response<a name="section65166273"></a>

Response parameters

None

## Status Code<a name="section49625546"></a>

[Table 2](#en-us_topic_0148832986_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  2**  Status code

<a name="en-us_topic_0148832986_t82c3440f3efb42a38b9d4dc4011a33d0"></a>
<table><thead align="left"><tr id="en-us_topic_0148832986_r3d6e2f205c444705bdbb9daaac74e575"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0148832986_af3c4073076f24eca88d94e3fa1effdc6"><a name="en-us_topic_0148832986_af3c4073076f24eca88d94e3fa1effdc6"></a><a name="en-us_topic_0148832986_af3c4073076f24eca88d94e3fa1effdc6"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="19.41%" id="mcps1.2.4.1.2"><p id="en-us_topic_0148832986_en-us_topic_0144911667_p4531342288"><a name="en-us_topic_0148832986_en-us_topic_0144911667_p4531342288"></a><a name="en-us_topic_0148832986_en-us_topic_0144911667_p4531342288"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0148832986_ada185614bba24140995b8123b3e9faa8"><a name="en-us_topic_0148832986_ada185614bba24140995b8123b3e9faa8"></a><a name="en-us_topic_0148832986_ada185614bba24140995b8123b3e9faa8"></a>Meaning</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0148832986_rc7b2adc390904a1ba79e303017797786"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0148832986_a93f3895d44bb4226934cc626ac50e37b"><a name="en-us_topic_0148832986_a93f3895d44bb4226934cc626ac50e37b"></a><a name="en-us_topic_0148832986_a93f3895d44bb4226934cc626ac50e37b"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="19.41%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0148832986_en-us_topic_0144911667_p7538425819"><a name="en-us_topic_0148832986_en-us_topic_0144911667_p7538425819"></a><a name="en-us_topic_0148832986_en-us_topic_0144911667_p7538425819"></a>No Content</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0148832986_en-us_topic_0144911667_p369874114414"><a name="en-us_topic_0148832986_en-us_topic_0144911667_p369874114414"></a><a name="en-us_topic_0148832986_en-us_topic_0144911667_p369874114414"></a>The server successfully processed the request and is not returning any content.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

