# Deleting an NIC from an ECS<a name="EN-US_TOPIC_0020212666"></a>

## Function<a name="section12502218"></a>

This API is used to delete a single NIC from the ECS based on the specified port ID.

## Constraints<a name="section1198904415453"></a>

The primary NIC of an ECS has routing rules configured and cannot be deleted.

When an ECS NIC is detached, all NICs attached to the ECS through the OpenStack Nova API will be deleted.

## URI<a name="section45411103"></a>

DELETE /v2/\{project\_id\}/servers/\{server\_id\}/os-interface/\{id\}\{?reserve\_port\}

DELETE /v2.1/\{project\_id\}/servers/\{server\_id\}/os-interface/\{id\}\{?reserve\_port\}

[Table 1](#table34333880)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table34333880"></a>
<table><thead align="left"><tr id="row1561146"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.37%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.64999999999999%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row34896348"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p8031928"><a name="p8031928"></a><a name="p8031928"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.4.1.2 "><p id="p46606392"><a name="p46606392"></a><a name="p46606392"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.64999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row4716221165950"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p42445993165950"><a name="p42445993165950"></a><a name="p42445993165950"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.4.1.2 "><p id="p15573376165950"><a name="p15573376165950"></a><a name="p15573376165950"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.64999999999999%" headers="mcps1.2.4.1.3 "><p id="p53483964165950"><a name="p53483964165950"></a><a name="p53483964165950"></a>Specifies the ECS ID.</p>
</td>
</tr>
<tr id="row18974699"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p60555637"><a name="p60555637"></a><a name="p60555637"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.4.1.2 "><p id="p6059584"><a name="p6059584"></a><a name="p6059584"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.64999999999999%" headers="mcps1.2.4.1.3 "><p id="p21064308"><a name="p21064308"></a><a name="p21064308"></a>Specifies the port ID of the NIC.</p>
<div class="note" id="note2787378017659"><a name="note2787378017659"></a><a name="note2787378017659"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p4953742817659"><a name="p4953742817659"></a><a name="p4953742817659"></a>When the ID is the same as the ECS primary NIC ID, the system will return error code 403.</p>
</div></div>
</td>
</tr>
<tr id="row16385916495"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p1738149194916"><a name="p1738149194916"></a><a name="p1738149194916"></a>reserve_port</p>
</td>
<td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.4.1.2 "><p id="p11382919491"><a name="p11382919491"></a><a name="p11382919491"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="65.64999999999999%" headers="mcps1.2.4.1.3 "><p id="p1138179154913"><a name="p1138179154913"></a><a name="p1138179154913"></a>Indicates whether to retain the NIC port after the NIC is unbound.</p>
<p id="p15127134211502"><a name="p15127134211502"></a><a name="p15127134211502"></a><strong id="b842352706151144"><a name="b842352706151144"></a><a name="b842352706151144"></a>True</strong>: indicates that the port is reserved.</p>
<p id="p1983020535501"><a name="p1983020535501"></a><a name="p1983020535501"></a><strong id="b842352706151226"><a name="b842352706151226"></a><a name="b842352706151226"></a>False</strong>: indicates that the port is deleted. This is the default value.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section6046746"></a>

None

## Response<a name="section54420716"></a>

None

## Example Request<a name="section05727183616"></a>

```
DELETE https://{endpoint}/v2/{project_id}/servers/{server_id}/os-interface/{id}
DELETE https://{endpoint}/v2.1/{project_id}/servers/{server_id}/os-interface/{id}
```

## Example Response<a name="section712919176361"></a>

None

## Returned Values<a name="section20024398"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

