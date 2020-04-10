# Detaching an EVS Disk from a BMS \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158611"></a>

## Function<a name="section53922917165259"></a>

This API is used to detach an EVS disk from a BMS.

## Constraints<a name="section64211377173223"></a>

If a BMS is stopped, disks can be detached from it without any limitation on the OS. If a BMS is in running state, the constraints are as follows:

-   Before detaching an EVS disk from a Linux BMS, log in to the BMS, run the  **unmount**  command to disassociate the disk to be detached from the file system, and ensure that no program is reading data from or writing data to the disk. Otherwise, the disk will fail to be detached.
-   Before detaching an EVS disk from a running Windows BMS, ensure that no program is reading data from or writing data to the disk. Otherwise, data will be lost.

## URI<a name="section51121191165259"></a>

DELETE /v2.1/\{project\_id\}/servers/\{server\_id\}/os-volume\_attachments/\{volume\_id\}

[Table 1](#table88181828105313)  lists the parameters.

**Table  1**  Parameter description

<a name="table88181828105313"></a>
<table><thead align="left"><tr id="row15819112816535"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p58268319165259"><a name="p58268319165259"></a><a name="p58268319165259"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p22113407165259"><a name="p22113407165259"></a><a name="p22113407165259"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p46355523165259"><a name="p46355523165259"></a><a name="p46355523165259"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18819132875319"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1217433165259"><a name="p1217433165259"></a><a name="p1217433165259"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p31503226165259"><a name="p31503226165259"></a><a name="p31503226165259"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1624545165259"><a name="p1624545165259"></a><a name="p1624545165259"></a>Specifies the project ID.</p>
<p id="p13397185821014"><a name="p13397185821014"></a><a name="p13397185821014"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row15819152825317"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p28142050151519"><a name="p28142050151519"></a><a name="p28142050151519"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p64913614151519"><a name="p64913614151519"></a><a name="p64913614151519"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p23511349151519"><a name="p23511349151519"></a><a name="p23511349151519"></a>Specifies the BMS ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
<tr id="row16819182805319"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p44090003175857"><a name="p44090003175857"></a><a name="p44090003175857"></a>volume_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p14520484175857"><a name="p14520484175857"></a><a name="p14520484175857"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p35308521175857"><a name="p35308521175857"></a><a name="p35308521175857"></a>Specifies the EVS disk ID.</p>
<p id="p102916285214"><a name="p102916285214"></a><a name="p102916285214"></a>You can query attached EVS disks attached to a <span id="en-us_topic_0053158665_text1798918157392"><a name="en-us_topic_0053158665_text1798918157392"></a><a name="en-us_topic_0053158665_text1798918157392"></a>BMS</span><span id="en-us_topic_0053158665_text10990131533919"><a name="en-us_topic_0053158665_text10990131533919"></a><a name="en-us_topic_0053158665_text10990131533919"></a></span> using the <a href="querying-information-about-the-disks-attached-to-a-bms-(native-openstack-api).md">Querying Information About the Disks Attached to a BMS (Native OpenStack API)</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section8194118165259"></a>

-   Request parameters

    None

-   Example request

    ```
    DELETE https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/os-volume_attachments/b53f23bd-ee8f-49ec-9420-d1acfeaf91d6
    ```


## Response Message<a name="section58140617165259"></a>

N/A

## Returned Values<a name="section7610951"></a>

Normal values

<a name="en-us_topic_0106040941_table753804619176"></a>
<table><thead align="left"><tr id="en-us_topic_0106040941_row10735134615172"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="en-us_topic_0106040941_p19735204616177"><a name="en-us_topic_0106040941_p19735204616177"></a><a name="en-us_topic_0106040941_p19735204616177"></a>Returned Values</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="en-us_topic_0106040941_p207355465176"><a name="en-us_topic_0106040941_p207355465176"></a><a name="en-us_topic_0106040941_p207355465176"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0106040941_row1473514621713"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0106040941_p13735144611178"><a name="en-us_topic_0106040941_p13735144611178"></a><a name="en-us_topic_0106040941_p13735144611178"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0106040941_p207351246161711"><a name="en-us_topic_0106040941_p207351246161711"></a><a name="en-us_topic_0106040941_p207351246161711"></a>The server has successfully processed the request.</p>
</td>
</tr>
</tbody>
</table>

For details about other returned values, see  [Status Codes](status-codes.md).

## Error Codes<a name="section14752650154917"></a>

See  [Error Codes](error-codes.md).

