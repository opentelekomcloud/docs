# Deleting a BMS \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158713"></a>

## Function<a name="section4329148591032"></a>

This interface is used to delete a BMS.

## URI<a name="section1832690791032"></a>

DELETE /v2.1/\{project\_id\}/servers/\{server\_id\}

[Table 1](#table11676151834514)  lists the parameters.

**Table  1**  Parameter description

<a name="table11676151834514"></a>
<table><thead align="left"><tr id="row20676618184519"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p5203048591032"><a name="p5203048591032"></a><a name="p5203048591032"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p5371975591032"><a name="p5371975591032"></a><a name="p5371975591032"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p5633286991032"><a name="p5633286991032"></a><a name="p5633286991032"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1467691854512"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p3144131991032"><a name="p3144131991032"></a><a name="p3144131991032"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6371887891032"><a name="p6371887891032"></a><a name="p6371887891032"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6095551491032"><a name="p6095551491032"></a><a name="p6095551491032"></a>Specifies the project ID.</p>
<p id="p13397185821014"><a name="p13397185821014"></a><a name="p13397185821014"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row667611824519"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p255895491134"><a name="p255895491134"></a><a name="p255895491134"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p594874291134"><a name="p594874291134"></a><a name="p594874291134"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1208612791134"><a name="p1208612791134"></a><a name="p1208612791134"></a>Specifies the BMS ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section1172872291032"></a>

-   Request parameters

    None

-   Example request

    ```
    DELETE https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/9ab74d89-61e7-4259-8546-465fdebe4944
    ```


## Response Message<a name="section6619360391225"></a>

N/A

## Returned Values<a name="section3477250491225"></a>

Normal values

<a name="table753804619176"></a>
<table><thead align="left"><tr id="row10735134615172"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p19735204616177"><a name="p19735204616177"></a><a name="p19735204616177"></a>Returned Values</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p207355465176"><a name="p207355465176"></a><a name="p207355465176"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1473514621713"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p13735144611178"><a name="p13735144611178"></a><a name="p13735144611178"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p81516575011"><a name="p81516575011"></a><a name="p81516575011"></a>The server has processed the request but did not return any content.</p>
</td>
</tr>
</tbody>
</table>

For details about other returned values, see  [Status Codes](status-codes.md).

## Error Codes<a name="section14752650154917"></a>

See  [Error Codes](error-codes.md).

