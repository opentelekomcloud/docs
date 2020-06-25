# Deleting an Endpoint Group<a name="en-dc_topic_0055025338"></a>

## Function<a name="en-us_topic_0070658809_section43031324205035"></a>

This API is used to delete a Direct Connect endpoint group.

## URI<a name="en-us_topic_0070658809_section29996404205035"></a>

DELETE /v2.0/dcaas/dc-endpoint-groups/\{endpoint\_group\_id\}

**Table  1**  Parameter description

<a name="table1297211334365"></a>
<table><thead align="left"><tr id="row6972123313361"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p7972133143612"><a name="p7972133143612"></a><a name="p7972133143612"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.2"><p id="p997213303616"><a name="p997213303616"></a><a name="p997213303616"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p597215330365"><a name="p597215330365"></a><a name="p597215330365"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.5.1.4"><p id="p69722339368"><a name="p69722339368"></a><a name="p69722339368"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14972143317361"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p0972633143618"><a name="p0972633143618"></a><a name="p0972633143618"></a>endpoint_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.2 "><p id="p5972633193614"><a name="p5972633193614"></a><a name="p5972633193614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p7972193343618"><a name="p7972193343618"></a><a name="p7972193343618"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="p59808335369"><a name="p59808335369"></a><a name="p59808335369"></a>Indicates the ID of the Direct Connect endpoint group.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0070658809_section54655929205035"></a>

[Table 2](#en-us_topic_0070658809_table2198437322244)  lists the request parameter.

**Table  2**  Request parameter

<a name="en-us_topic_0070658809_table2198437322244"></a>
<table><thead align="left"><tr id="en-us_topic_0070658809_row4304807922244"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="en-us_topic_0070658809_p6505580022244"><a name="en-us_topic_0070658809_p6505580022244"></a><a name="en-us_topic_0070658809_p6505580022244"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.2"><p id="en-us_topic_0070658809_p329696222244"><a name="en-us_topic_0070658809_p329696222244"></a><a name="en-us_topic_0070658809_p329696222244"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="en-us_topic_0070658809_p3257067222244"><a name="en-us_topic_0070658809_p3257067222244"></a><a name="en-us_topic_0070658809_p3257067222244"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.5.1.4"><p id="en-us_topic_0070658809_p5470821922244"><a name="en-us_topic_0070658809_p5470821922244"></a><a name="en-us_topic_0070658809_p5470821922244"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0070658809_row5451891922244"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0070658809_p3187982384832"><a name="en-us_topic_0070658809_p3187982384832"></a><a name="en-us_topic_0070658809_p3187982384832"></a>endpoint_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0070658809_p757920222316"><a name="en-us_topic_0070658809_p757920222316"></a><a name="en-us_topic_0070658809_p757920222316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0070658809_p4706384922316"><a name="en-us_topic_0070658809_p4706384922316"></a><a name="en-us_topic_0070658809_p4706384922316"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0070658809_p970883222316"><a name="en-us_topic_0070658809_p970883222316"></a><a name="en-us_topic_0070658809_p970883222316"></a>Indicates the ID of the Direct Connect endpoint group.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0070658809_section48616095205035"></a>

None

## Examples<a name="en-us_topic_0070658809_section7653394205035"></a>

-   Example request

```
DELETE /v2.0/dcaas/dc-endpoint-groups/{endpoint_group_id}
```

-   Response example

    None


## Returned Value<a name="section12113171955820"></a>

For details, see section  [Common Returned Values](common-returned-values.md).

