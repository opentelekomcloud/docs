# Deleting Specified BMS Metadata \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158683"></a>

## Function<a name="section5520708185439"></a>

This API is used to delete specified BMS metadata.

## Constraints<a name="section5072450814374"></a>

The BMS  **OS-EXT-STS:vm\_state**  attribute \(BMS status\) must be  **active**,  **stopped**,  **paused**, or  **suspended**.

## URI<a name="section65173692185439"></a>

DELETE /v2.1/\{project\_id\}/servers/\{server\_id\}/metadata/\{key\}

[Table 1](#table12474435113619)  lists the parameters.

**Table  1**  Parameter description

<a name="table12474435113619"></a>
<table><thead align="left"><tr id="row1947413503615"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p54886041185439"><a name="p54886041185439"></a><a name="p54886041185439"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p16584368185439"><a name="p16584368185439"></a><a name="p16584368185439"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p1156530185439"><a name="p1156530185439"></a><a name="p1156530185439"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16474735103610"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4696221185439"><a name="p4696221185439"></a><a name="p4696221185439"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p44849621185439"><a name="p44849621185439"></a><a name="p44849621185439"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p8940698185439"><a name="p8940698185439"></a><a name="p8940698185439"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row12474113573619"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8209263185439"><a name="p8209263185439"></a><a name="p8209263185439"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p60970546185439"><a name="p60970546185439"></a><a name="p60970546185439"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p39667165185439"><a name="p39667165185439"></a><a name="p39667165185439"></a>Specifies the <span id="text10391121222112"><a name="text10391121222112"></a><a name="text10391121222112"></a>BMS</span><span id="text439171216215"><a name="text439171216215"></a><a name="text439171216215"></a></span> ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
<tr id="row16474835173611"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p48209085185622"><a name="p48209085185622"></a><a name="p48209085185622"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p12621798185622"><a name="p12621798185622"></a><a name="p12621798185622"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15732716185622"><a name="p15732716185622"></a><a name="p15732716185622"></a>Specifies the <span id="text18734141311421"><a name="text18734141311421"></a><a name="text18734141311421"></a>BMS</span><span id="text1573681354217"><a name="text1573681354217"></a><a name="text1573681354217"></a></span> metadata key value to be deleted.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section21460169185439"></a>

-   Request parameters

    None

-   Example request

    ```
    DELETE https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/metadata/{key}
    ```


## Response Message<a name="section31286738185439"></a>

N/A

## Returned Values<a name="section27037160"></a>

Normal values

<a name="en-us_topic_0053158659_table753804619176"></a>
<table><thead align="left"><tr id="en-us_topic_0053158659_row10735134615172"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="en-us_topic_0053158659_p19735204616177"><a name="en-us_topic_0053158659_p19735204616177"></a><a name="en-us_topic_0053158659_p19735204616177"></a>Returned Values</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="en-us_topic_0053158659_p207355465176"><a name="en-us_topic_0053158659_p207355465176"></a><a name="en-us_topic_0053158659_p207355465176"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0053158659_row1473514621713"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0053158659_p13735144611178"><a name="en-us_topic_0053158659_p13735144611178"></a><a name="en-us_topic_0053158659_p13735144611178"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0053158659_p81516575011"><a name="en-us_topic_0053158659_p81516575011"></a><a name="en-us_topic_0053158659_p81516575011"></a>The server has processed the request but did not return any content.</p>
</td>
</tr>
</tbody>
</table>

For details about other returned values, see  [Status Codes](status-codes.md).

## Error Codes<a name="section14752650154917"></a>

See  [Error Codes](error-codes.md).

