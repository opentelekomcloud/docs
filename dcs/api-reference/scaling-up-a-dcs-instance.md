# Scaling Up a DCS Instance<a name="EN-US_TOPIC_0237964359"></a>

## Function<a name="section2794612"></a>

This API is used to scale up a DCS instance.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Only single-node DCS instances and master/standby DCS instances support specification scale-ups, while DCS instances in the cluster mode do not.  

## URI<a name="section25151514"></a>

-   URI format:

    POST /v1.0/\{project\_id\}/instances/\{instance\_id\}/extend

-   Parameter description:

    [Table 1](#d0e3342)  describes the parameters of this API.


**Table  1**  Parameter description

<a name="d0e3342"></a>
<table><thead align="left"><tr id="row11137969"><th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.5.1.1"><p id="p29760277"><a name="p29760277"></a><a name="p29760277"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.2"><p id="p61772230"><a name="p61772230"></a><a name="p61772230"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.2.5.1.3"><p id="p37494699"><a name="p37494699"></a><a name="p37494699"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="39.39393939393939%" id="mcps1.2.5.1.4"><p id="p17171756"><a name="p17171756"></a><a name="p17171756"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row48735027"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.1 "><p id="p55223077"><a name="p55223077"></a><a name="p55223077"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p43884268"><a name="p43884268"></a><a name="p43884268"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.3 "><p id="p64964848"><a name="p64964848"></a><a name="p64964848"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="p27661336"><a name="p27661336"></a><a name="p27661336"></a>Project ID.</p>
</td>
</tr>
<tr id="row47625437"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.1 "><p id="p32455223"><a name="p32455223"></a><a name="p32455223"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p11627434"><a name="p11627434"></a><a name="p11627434"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.3 "><p id="p2298077"><a name="p2298077"></a><a name="p2298077"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="p51926520"><a name="p51926520"></a><a name="p51926520"></a>DCS instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section25037038"></a>

-   Request parameter:

[Table 2](#d0e3402)  describes request parameters.

**Table  2**  Parameter description

<a name="d0e3402"></a>
<table><thead align="left"><tr id="row56907078"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="p46070597"><a name="p46070597"></a><a name="p46070597"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p40730901"><a name="p40730901"></a><a name="p40730901"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p10868702"><a name="p10868702"></a><a name="p10868702"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.2.5.1.4"><p id="p7949639"><a name="p7949639"></a><a name="p7949639"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row39940984"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p13994266"><a name="p13994266"></a><a name="p13994266"></a>new_capacity</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p59793748"><a name="p59793748"></a><a name="p59793748"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p11455439"><a name="p11455439"></a><a name="p11455439"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p55475379"><a name="p55475379"></a><a name="p55475379"></a>New specifications (memory space) of the DCS instance. The new specification value to which the DCS instance will be scaled up must be greater than the current specification value.</p>
<p id="p29516363"><a name="p29516363"></a><a name="p29516363"></a>Unit: GB.</p>
</td>
</tr>
</tbody>
</table>

Example request:

```
{ 
```

```
 "new_capacity": 4 
```

```
}
```

## Response<a name="section24006753"></a>

-   Status code:

    If status code "204 No content" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    None.

-   Example response:

    None.


