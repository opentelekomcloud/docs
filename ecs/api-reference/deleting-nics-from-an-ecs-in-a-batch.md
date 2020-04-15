# Deleting NICs from an ECS in a Batch<a name="EN-US_TOPIC_0020212665"></a>

## Function<a name="section4187856"></a>

This API is used to uninstall and delete one or multiple NICs from an ECS.

## Constraints<a name="section16704417311"></a>

The primary NIC of an ECS has routing rules configured and cannot be deleted.

## URI<a name="section37690705"></a>

POST /v1/\{project\_id\}/cloudservers/\{server\_id\}/nics/delete

[Table 1](#table42885739)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table42885739"></a>
<table><thead align="left"><tr id="row63231703"><th class="cellrowborder" valign="top" width="16.41%" id="mcps1.2.4.1.1"><p id="p21494305"><a name="p21494305"></a><a name="p21494305"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p63317164"><a name="p63317164"></a><a name="p63317164"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.42%" id="mcps1.2.4.1.3"><p id="p28416672"><a name="p28416672"></a><a name="p28416672"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20049059"><td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.4.1.1 "><p id="p13361120"><a name="p13361120"></a><a name="p13361120"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p8508925"><a name="p8508925"></a><a name="p8508925"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.42%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row3613092117015"><td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.4.1.1 "><p id="p1181501417024"><a name="p1181501417024"></a><a name="p1181501417024"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p1749204017024"><a name="p1749204017024"></a><a name="p1749204017024"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.42%" headers="mcps1.2.4.1.3 "><p id="p756915117024"><a name="p756915117024"></a><a name="p756915117024"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section3672032"></a>

[Table 2](#table35856517)  describes the request parameters.

**Table  2**  Request parameters

<a name="table35856517"></a>
<table><thead align="left"><tr id="row15151670"><th class="cellrowborder" valign="top" width="16.36%" id="mcps1.2.5.1.1"><p id="p19325759"><a name="p19325759"></a><a name="p19325759"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.19%" id="mcps1.2.5.1.2"><p id="p21882681"><a name="p21882681"></a><a name="p21882681"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.13%" id="mcps1.2.5.1.3"><p id="p27666764"><a name="p27666764"></a><a name="p27666764"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.32%" id="mcps1.2.5.1.4"><p id="p26415391"><a name="p26415391"></a><a name="p26415391"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row59271898"><td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.2.5.1.1 "><p id="p36294438"><a name="p36294438"></a><a name="p36294438"></a>nics</p>
</td>
<td class="cellrowborder" valign="top" width="17.19%" headers="mcps1.2.5.1.2 "><p id="p54168362"><a name="p54168362"></a><a name="p54168362"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.13%" headers="mcps1.2.5.1.3 "><p id="p25561231"><a name="p25561231"></a><a name="p25561231"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="52.32%" headers="mcps1.2.5.1.4 "><p id="p44982630"><a name="p44982630"></a><a name="p44982630"></a>Specifies the NICs to be deleted. For details, see <a href="#table43212049">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **nics**  field description

<a name="table43212049"></a>
<table><thead align="left"><tr id="row13772373"><th class="cellrowborder" valign="top" width="16.35%" id="mcps1.2.5.1.1"><p id="p1687315211520"><a name="p1687315211520"></a><a name="p1687315211520"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.2"><p id="p9873021657"><a name="p9873021657"></a><a name="p9873021657"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.919999999999998%" id="mcps1.2.5.1.3"><p id="p9873721157"><a name="p9873721157"></a><a name="p9873721157"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.44%" id="mcps1.2.5.1.4"><p id="p7873102111513"><a name="p7873102111513"></a><a name="p7873102111513"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row38764716"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.5.1.1 "><p id="p52934302"><a name="p52934302"></a><a name="p52934302"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p59820093"><a name="p59820093"></a><a name="p59820093"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.919999999999998%" headers="mcps1.2.5.1.3 "><p id="p13589360"><a name="p13589360"></a><a name="p13589360"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.44%" headers="mcps1.2.5.1.4 "><p id="p41640866"><a name="p41640866"></a><a name="p41640866"></a>Specifies the port ID of the NIC.</p>
<div class="note" id="note49262081714"><a name="note49262081714"></a><a name="note49262081714"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p443358761714"><a name="p443358761714"></a><a name="p443358761714"></a>When the ID is the same as the ECS primary NIC ID, the system will return error code 403.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## Response<a name="section33048293"></a>

See  [Responses \(Task\)](responses-(task).md).

## Example Request<a name="section12428547539"></a>

```
POST https://{endpoint}/v1/{project_id}/cloudservers/{server_id}/nics/delete
```

```
{
    "nics": [
         {
            "id": "d32019d3-bc6e-4319-9c1d-6722fc136a23"
        }
    ]
}
```

## Example Response<a name="section185132219719"></a>

None

## Returned Values<a name="en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section23611955"></a>

See  [Error Code Description](error-code-description.md).

