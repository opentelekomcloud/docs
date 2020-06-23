# Restoring a DCS Instance<a name="EN-US_TOPIC_0237964370"></a>

## Function<a name="section25670449"></a>

This API is used to restore a specified DCS instance.

## URI<a name="section29707457"></a>

-   URI format:

    POST /v1.0/\{project\_id\}/instances/\{instance\_id\}/restores

-   Parameter description:

    [Table 1](#d0e5974)  describes the parameters of this API.


**Table  1**  Parameter description

<a name="d0e5974"></a>
<table><thead align="left"><tr id="row11549419"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p63087769"><a name="p63087769"></a><a name="p63087769"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p9835639"><a name="p9835639"></a><a name="p9835639"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p58489261"><a name="p58489261"></a><a name="p58489261"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p40009700"><a name="p40009700"></a><a name="p40009700"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19560259"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p40877171"><a name="p40877171"></a><a name="p40877171"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p22716572"><a name="p22716572"></a><a name="p22716572"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p28103013"><a name="p28103013"></a><a name="p28103013"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p61751542"><a name="p61751542"></a><a name="p61751542"></a>Project ID.</p>
</td>
</tr>
<tr id="row18892969"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p53935546"><a name="p53935546"></a><a name="p53935546"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p6703144"><a name="p6703144"></a><a name="p6703144"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p6083802"><a name="p6083802"></a><a name="p6083802"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p23025977"><a name="p23025977"></a><a name="p23025977"></a>DCS instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section66040521"></a>

-   Request parameter:

    [Table 2](#d0e6034)  describes request parameters.


**Table  2**  Parameter description

<a name="d0e6034"></a>
<table><thead align="left"><tr id="row7912910"><th class="cellrowborder" valign="top" width="20.2020202020202%" id="mcps1.2.5.1.1"><p id="p36965936"><a name="p36965936"></a><a name="p36965936"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.2"><p id="p41450855"><a name="p41450855"></a><a name="p41450855"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.3"><p id="p2076123"><a name="p2076123"></a><a name="p2076123"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="45.45454545454545%" id="mcps1.2.5.1.4"><p id="p33948275"><a name="p33948275"></a><a name="p33948275"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row65455768"><td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.2.5.1.1 "><p id="p316977"><a name="p316977"></a><a name="p316977"></a>remark</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p25675175"><a name="p25675175"></a><a name="p25675175"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="p66423265"><a name="p66423265"></a><a name="p66423265"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454545%" headers="mcps1.2.5.1.4 "><p id="p11575367"><a name="p11575367"></a><a name="p11575367"></a>Description of DCS instance restoration.</p>
</td>
</tr>
<tr id="row37069447"><td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.2.5.1.1 "><p id="p49835227"><a name="p49835227"></a><a name="p49835227"></a>backup_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p10121616"><a name="p10121616"></a><a name="p10121616"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="p14544590"><a name="p14544590"></a><a name="p14544590"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454545%" headers="mcps1.2.5.1.4 "><p id="p37261116"><a name="p37261116"></a><a name="p37261116"></a>ID of the backup record.</p>
</td>
</tr>
</tbody>
</table>

-   Example request:

    ```
    { 
     "remark":"restore instance", 
     "backup_id":"8ba256cb-e5ac-44f6-a3da-c03d8f0e5029" 
    }
    ```


## Response<a name="section57493779"></a>

-   Status code:

    If status code "200 OK" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    [Table 3](#d0e6104)  describes the response parameter.


**Table  3**  Parameter description

<a name="d0e6104"></a>
<table><thead align="left"><tr id="row51554213"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p15141735"><a name="p15141735"></a><a name="p15141735"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p18521046"><a name="p18521046"></a><a name="p18521046"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p23809753"><a name="p23809753"></a><a name="p23809753"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row49541849"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p53466813"><a name="p53466813"></a><a name="p53466813"></a>restore_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p35844590"><a name="p35844590"></a><a name="p35844590"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p17730643"><a name="p17730643"></a><a name="p17730643"></a>ID of the restoration record.</p>
</td>
</tr>
</tbody>
</table>

-   Example response:

    ```
    { 
     "restore_id": "a6155972-800c-4170-a479-3231e907d2f6" 
    }
    ```


