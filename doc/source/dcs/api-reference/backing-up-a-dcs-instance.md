# Backing Up a DCS Instance<a name="EN-US_TOPIC_0237964369"></a>

## Function<a name="section9292835"></a>

This API is used to back up a specified DCS instance.

## URI<a name="section16526653"></a>

-   URI format:

    POST /v1.0/\{project\_id\}/instances/\{instance\_id\}/backups

-   Parameter description:

    [Table 1](#d0e5762)  describes the parameters of this API.


**Table  1**  Parameter description

<a name="d0e5762"></a>
<table><thead align="left"><tr id="row6320796"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p42222440"><a name="p42222440"></a><a name="p42222440"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p64574505"><a name="p64574505"></a><a name="p64574505"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p63152455"><a name="p63152455"></a><a name="p63152455"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p15075241"><a name="p15075241"></a><a name="p15075241"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13135032"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p57304667"><a name="p57304667"></a><a name="p57304667"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p11166459"><a name="p11166459"></a><a name="p11166459"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p32067967"><a name="p32067967"></a><a name="p32067967"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p47368528"><a name="p47368528"></a><a name="p47368528"></a>Project ID.</p>
</td>
</tr>
<tr id="row23663568"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p37700862"><a name="p37700862"></a><a name="p37700862"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p33871021"><a name="p33871021"></a><a name="p33871021"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p59198213"><a name="p59198213"></a><a name="p59198213"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p30325933"><a name="p30325933"></a><a name="p30325933"></a>DCS instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section14522153"></a>

-   Request parameter:

    [Table 2](#d0e5822)  describes request parameters.


**Table  2**  Parameter description

<a name="d0e5822"></a>
<table><thead align="left"><tr id="row50335026"><th class="cellrowborder" valign="top" width="20.2020202020202%" id="mcps1.2.5.1.1"><p id="p50605310"><a name="p50605310"></a><a name="p50605310"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.2"><p id="p5389442"><a name="p5389442"></a><a name="p5389442"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.3"><p id="p33891687"><a name="p33891687"></a><a name="p33891687"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="45.45454545454545%" id="mcps1.2.5.1.4"><p id="p60872149"><a name="p60872149"></a><a name="p60872149"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row31697011"><td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.2.5.1.1 "><p id="p17321065"><a name="p17321065"></a><a name="p17321065"></a>remark</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p60829024"><a name="p60829024"></a><a name="p60829024"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="p28203903"><a name="p28203903"></a><a name="p28203903"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454545%" headers="mcps1.2.5.1.4 "><p id="p2814831"><a name="p2814831"></a><a name="p2814831"></a>Description of DCS instance backup.</p>
</td>
</tr>
</tbody>
</table>

-   Example request:

    ```
    { 
     "remark": "Backup instances" 
    }
    ```


## Response<a name="section63590521"></a>

-   Status code:

    If status code "200 OK" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    [Table 3](#table2807163920546)  describes the response parameter.


**Table  3**  Parameter description

<a name="table2807163920546"></a>
<table><thead align="left"><tr id="row10412728"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p38124620"><a name="p38124620"></a><a name="p38124620"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p1086509"><a name="p1086509"></a><a name="p1086509"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p20898370"><a name="p20898370"></a><a name="p20898370"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15046387"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p10797866"><a name="p10797866"></a><a name="p10797866"></a>backup_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p2211916"><a name="p2211916"></a><a name="p2211916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p44947523"><a name="p44947523"></a><a name="p44947523"></a>ID of the backup record.</p>
</td>
</tr>
</tbody>
</table>

-   Example response:

    ```
    { 
     "backup_id": "548ceeff-2cbb-47ab-9a1c-7b085a8c08d7" 
    }
    ```


