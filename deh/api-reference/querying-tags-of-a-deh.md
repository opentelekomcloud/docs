# Querying Tags of a DeH<a name="EN-US_TOPIC_0134153398"></a>

## Function<a name="section54478915181842"></a>

-   This API is used to query tags of a DeH.

-   Tag Management Service \(TMS\) uses this API to query all tags of a DeH.

## URI<a name="en-us_topic_0057972838_section58912114"></a>

GET /v1.0/\{project\_id\}/dedicated-host-tags/\{dedicated\_host\_id\}/tags

[Table 1](#table291625114015)  describes the parameters.

**Table  1**  Parameters description

<a name="table291625114015"></a>
<table><thead align="left"><tr id="row291610574011"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p64521444164912"><a name="p64521444164912"></a><a name="p64521444164912"></a><strong id="b11812174710154"><a name="b11812174710154"></a><a name="b11812174710154"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p16452114494915"><a name="p16452114494915"></a><a name="p16452114494915"></a><strong id="b618354941512"><a name="b618354941512"></a><a name="b618354941512"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p69548610432"><a name="p69548610432"></a><a name="p69548610432"></a><strong id="b11103250201516"><a name="b11103250201516"></a><a name="b11103250201516"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p94521344104916"><a name="p94521344104916"></a><a name="p94521344104916"></a><strong id="b1259175131515"><a name="b1259175131515"></a><a name="b1259175131515"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row69161956409"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p14452174415495"><a name="p14452174415495"></a><a name="p14452174415495"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p134521443499"><a name="p134521443499"></a><a name="p134521443499"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p59527664313"><a name="p59527664313"></a><a name="p59527664313"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p10452244104914"><a name="p10452244104914"></a><a name="p10452244104914"></a>Specifies the project ID.</p>
<p id="p7376194915119"><a name="p7376194915119"></a><a name="p7376194915119"></a>For details about how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row129169504014"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p3452144416495"><a name="p3452144416495"></a><a name="p3452144416495"></a>dedicated_host_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p6452124416491"><a name="p6452124416491"></a><a name="p6452124416491"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p095086134310"><a name="p095086134310"></a><a name="p095086134310"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1945284419497"><a name="p1945284419497"></a><a name="p1945284419497"></a>Specifies the DeH ID.</p>
<p id="p858154817367"><a name="p858154817367"></a><a name="p858154817367"></a>You can obtain the DeH ID from the DeH console or using the <a href="querying-dehs.md">Querying DeHs</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972838_section60446980"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{Endpoint}/v1.0/9c53a566cb3443ab910cf0daebca90c4/dedicated-host-tags/74259164-e63a-4ad9-9c77-a1bd2c9aa187/tags
    ```


## Response<a name="section40529449"></a>

-   Response parameters

    <a name="table19269134632211"></a>
    <table><thead align="left"><tr id="row627217461225"><th class="cellrowborder" valign="top" width="22.67%" id="mcps1.1.4.1.1"><p id="p16273546132213"><a name="p16273546132213"></a><a name="p16273546132213"></a><strong id="b172826101614"><a name="b172826101614"></a><a name="b172826101614"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.43%" id="mcps1.1.4.1.2"><p id="p627604632212"><a name="p627604632212"></a><a name="p627604632212"></a><strong id="b771127141611"><a name="b771127141611"></a><a name="b771127141611"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.900000000000006%" id="mcps1.1.4.1.3"><p id="p1027674613222"><a name="p1027674613222"></a><a name="p1027674613222"></a><strong id="b1865285162"><a name="b1865285162"></a><a name="b1865285162"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row132775466226"><td class="cellrowborder" valign="top" width="22.67%" headers="mcps1.1.4.1.1 "><p id="p22791746162215"><a name="p22791746162215"></a><a name="p22791746162215"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.43%" headers="mcps1.1.4.1.2 "><p id="p528064612220"><a name="p528064612220"></a><a name="p528064612220"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.900000000000006%" headers="mcps1.1.4.1.3 "><p id="p1528117465221"><a name="p1528117465221"></a><a name="p1528117465221"></a>Specifies the tag list.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **resource\_tag**  field description

    <a name="table354841117456"></a>
    <table><thead align="left"><tr id="row11550211164514"><th class="cellrowborder" valign="top" width="22.68%" id="mcps1.1.4.1.1"><p id="p6993140202415"><a name="p6993140202415"></a><a name="p6993140202415"></a><strong id="b5443230166"><a name="b5443230166"></a><a name="b5443230166"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.42%" id="mcps1.1.4.1.2"><p id="p179969011243"><a name="p179969011243"></a><a name="p179969011243"></a><strong id="b9116181713164"><a name="b9116181713164"></a><a name="b9116181713164"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.900000000000006%" id="mcps1.1.4.1.3"><p id="p1299770122412"><a name="p1299770122412"></a><a name="p1299770122412"></a><strong id="b8334174712917"><a name="b8334174712917"></a><a name="b8334174712917"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19550611164513"><td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.1.4.1.1 "><p id="p1505192415"><a name="p1505192415"></a><a name="p1505192415"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.42%" headers="mcps1.1.4.1.2 "><p id="p12431102414"><a name="p12431102414"></a><a name="p12431102414"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.900000000000006%" headers="mcps1.1.4.1.3 "><p id="p1651311249"><a name="p1651311249"></a><a name="p1651311249"></a>Specifies the tag key.</p>
    </td>
    </tr>
    <tr id="row1455017119455"><td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.1.4.1.1 "><p id="p37191182412"><a name="p37191182412"></a><a name="p37191182412"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.42%" headers="mcps1.1.4.1.2 "><p id="p6116115249"><a name="p6116115249"></a><a name="p6116115249"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.900000000000006%" headers="mcps1.1.4.1.3 "><p id="p911191112415"><a name="p911191112415"></a><a name="p911191112415"></a>Specifies the tag value.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "tags": [
            {
                "key": "key1", 
                "value": "value1"
            },
            {
                "key": "key2", 
                "value": "value2"
            }
        ]
    }
    ```


## Status Code<a name="section9992350"></a>

See  [Status Codes](status-codes.md).

