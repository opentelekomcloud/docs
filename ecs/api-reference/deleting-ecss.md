# Deleting ECSs<a name="EN-US_TOPIC_0020212679"></a>

## Function<a name="section61511739"></a>

This API is used to delete ECSs based on a specified ECS ID list.

You can delete a single ECS or multiple ECSs in a batch. A maximum of 1000 ECSs can be deleted in a batch.

## URI<a name="section16734741"></a>

POST /v1/\{project\_id\}/cloudservers/delete

[Table 1](#table52652517)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table52652517"></a>
<table><thead align="left"><tr id="row61945077"><th class="cellrowborder" valign="top" width="16.42%" id="mcps1.2.4.1.1"><p id="p51495331"><a name="p51495331"></a><a name="p51495331"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.4.1.2"><p id="p10372286"><a name="p10372286"></a><a name="p10372286"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.22%" id="mcps1.2.4.1.3"><p id="p34848813"><a name="p34848813"></a><a name="p34848813"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4181593"><td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.1 "><p id="p3164713"><a name="p3164713"></a><a name="p3164713"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p55015173"><a name="p55015173"></a><a name="p55015173"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.22%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section16394943"></a>

[Table 2](#table8361976)  describes the request parameters.

**Table  2**  Request parameters

<a name="table8361976"></a>
<table><thead align="left"><tr id="row2187155"><th class="cellrowborder" valign="top" width="16.348365163483656%" id="mcps1.2.5.1.1"><p id="p42941906"><a name="p42941906"></a><a name="p42941906"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.548245175482453%" id="mcps1.2.5.1.2"><p id="p55742394"><a name="p55742394"></a><a name="p55742394"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.748525147485253%" id="mcps1.2.5.1.3"><p id="p18840050"><a name="p18840050"></a><a name="p18840050"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.35486451354865%" id="mcps1.2.5.1.4"><p id="p49649058"><a name="p49649058"></a><a name="p49649058"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row62150771"><td class="cellrowborder" valign="top" width="16.348365163483656%" headers="mcps1.2.5.1.1 "><p id="p1047692"><a name="p1047692"></a><a name="p1047692"></a>servers</p>
</td>
<td class="cellrowborder" valign="top" width="17.548245175482453%" headers="mcps1.2.5.1.2 "><p id="p17754262"><a name="p17754262"></a><a name="p17754262"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.748525147485253%" headers="mcps1.2.5.1.3 "><p id="p28809145"><a name="p28809145"></a><a name="p28809145"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="51.35486451354865%" headers="mcps1.2.5.1.4 "><p id="p63901309"><a name="p63901309"></a><a name="p63901309"></a>Specifies the ECSs to be deleted. For details, see <a href="#table32603030">Table 3</a>.</p>
</td>
</tr>
<tr id="row38240871"><td class="cellrowborder" valign="top" width="16.348365163483656%" headers="mcps1.2.5.1.1 "><p id="p10502851"><a name="p10502851"></a><a name="p10502851"></a>delete_publicip</p>
</td>
<td class="cellrowborder" valign="top" width="17.548245175482453%" headers="mcps1.2.5.1.2 "><p id="p45424599"><a name="p45424599"></a><a name="p45424599"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.748525147485253%" headers="mcps1.2.5.1.3 "><p id="p55513932"><a name="p55513932"></a><a name="p55513932"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="51.35486451354865%" headers="mcps1.2.5.1.4 "><p id="p334666"><a name="p334666"></a><a name="p334666"></a>Specifies whether to delete the EIP bound to the ECS when deleting the ECS. If you do not want to delete the EIP, the system only unbinds the EIP from the ECS and reserves the IP address.</p>
<p id="p3011995"><a name="p3011995"></a><a name="p3011995"></a>The value can be <strong id="b842352706184734"><a name="b842352706184734"></a><a name="b842352706184734"></a>true</strong> or <strong id="b842352706184738"><a name="b842352706184738"></a><a name="b842352706184738"></a>false</strong>. The default value is <strong id="b842352706184742"><a name="b842352706184742"></a><a name="b842352706184742"></a>false</strong>.</p>
<a name="ul11598244152333"></a><a name="ul11598244152333"></a><ul id="ul11598244152333"><li><strong id="b842352706172054"><a name="b842352706172054"></a><a name="b842352706172054"></a>true</strong>: indicates to delete the EIP bound to the ECS when deleting the ECS.</li><li><strong id="b842352706172110"><a name="b842352706172110"></a><a name="b842352706172110"></a>false</strong>: indicates only to unbind the EIP bound to the ECS when deleting the ECS.</li></ul>
</td>
</tr>
<tr id="row27107960"><td class="cellrowborder" valign="top" width="16.348365163483656%" headers="mcps1.2.5.1.1 "><p id="p48261118"><a name="p48261118"></a><a name="p48261118"></a>delete_volume</p>
</td>
<td class="cellrowborder" valign="top" width="17.548245175482453%" headers="mcps1.2.5.1.2 "><p id="p16836485"><a name="p16836485"></a><a name="p16836485"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.748525147485253%" headers="mcps1.2.5.1.3 "><p id="p21578036"><a name="p21578036"></a><a name="p21578036"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="51.35486451354865%" headers="mcps1.2.5.1.4 "><p id="p2990516"><a name="p2990516"></a><a name="p2990516"></a>Specifies whether to delete the data disks of the ECS. If you do not want to delete the data disks, the system only detaches the disks from the ECS and reserves the disks.</p>
<p id="p26914650"><a name="p26914650"></a><a name="p26914650"></a>The value can be <strong id="b285584762"><a name="b285584762"></a><a name="b285584762"></a>true</strong> or <strong id="b1700441549"><a name="b1700441549"></a><a name="b1700441549"></a>false</strong>. The default value is <strong id="b1703516327"><a name="b1703516327"></a><a name="b1703516327"></a>false</strong>.</p>
<a name="ul48071530152411"></a><a name="ul48071530152411"></a><ul id="ul48071530152411"><li><strong id="b842352706161021"><a name="b842352706161021"></a><a name="b842352706161021"></a>true</strong>: indicates to delete the data disks attached to the ECS when deleting the ECS.</li><li><strong id="b505974657161155"><a name="b505974657161155"></a><a name="b505974657161155"></a>false</strong>: indicates only to detach the data disks attached to the ECS when deleting the ECS.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  3** **servers**  field description

<a name="table32603030"></a>
<table><thead align="left"><tr id="row25141347"><th class="cellrowborder" valign="top" width="16.35%" id="mcps1.2.5.1.1"><p id="p3065418507"><a name="p3065418507"></a><a name="p3065418507"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.48%" id="mcps1.2.5.1.2"><p id="p100135425018"><a name="p100135425018"></a><a name="p100135425018"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.85%" id="mcps1.2.5.1.3"><p id="p170854105015"><a name="p170854105015"></a><a name="p170854105015"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.32%" id="mcps1.2.5.1.4"><p id="p816115445017"><a name="p816115445017"></a><a name="p816115445017"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53999455"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.5.1.1 "><p id="p11879716"><a name="p11879716"></a><a name="p11879716"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.2 "><p id="p22732954"><a name="p22732954"></a><a name="p22732954"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.2.5.1.3 "><p id="p29429992"><a name="p29429992"></a><a name="p29429992"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.32%" headers="mcps1.2.5.1.4 "><p id="p35019191"><a name="p35019191"></a><a name="p35019191"></a>Specifies the ID of the ECS to be deleted.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section112357236514"></a>

See  [Responses \(Task\)](responses-(task).md).

## Example Request<a name="section159261353165117"></a>

Example request

```
POST https://{endpoint}/v1/{project_id}/cloudservers/delete
```

```
{
    "servers": [
        {
            "id": "616fb98f-46ca-475e-917e-2563e5a8cd19"
        }
    ], 
    "delete_publicip": false, 
    "delete_volume": false
   }
```

## Example Response<a name="section5373174623216"></a>

```
{
    "job_id": "70a599e0-31e7-49b7-b260-868f441e862b"
}
```

Or

```
{
    "error": {
        "message": "request body is illegal.",
        "code": "Ecs.0005"
    }
}
```

## Returned Values<a name="section12571834"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).

