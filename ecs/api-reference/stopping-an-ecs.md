# Stopping an ECS<a name="EN-US_TOPIC_0020212652"></a>

## Function<a name="section32841145"></a>

This API is used to stop a single ECS.

## URI<a name="section27134857"></a>

POST /v2/\{project\_id\}/servers/\{server\_id\}/action

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/action

[Table 1](#table52155720)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table52155720"></a>
<table><thead align="left"><tr id="row49639248"><th class="cellrowborder" valign="top" width="16.61%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.22%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row45123001"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.4.1.1 "><p id="p31084503"><a name="p31084503"></a><a name="p31084503"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p34816825"><a name="p34816825"></a><a name="p34816825"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.22%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row14315403"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.4.1.1 "><p id="p18697032"><a name="p18697032"></a><a name="p18697032"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p38064613"><a name="p38064613"></a><a name="p38064613"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.22%" headers="mcps1.2.4.1.3 "><p id="p63334794"><a name="p63334794"></a><a name="p63334794"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section42887128"></a>

[Table 2](#table54550461)  describes the request parameters.

**Table  2**  Request parameters

<a name="table54550461"></a>
<table><thead align="left"><tr id="row11842506"><th class="cellrowborder" valign="top" width="17.11%" id="mcps1.2.5.1.1"><p id="p19718930"><a name="p19718930"></a><a name="p19718930"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.299999999999997%" id="mcps1.2.5.1.2"><p id="p53729511"><a name="p53729511"></a><a name="p53729511"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.16%" id="mcps1.2.5.1.3"><p id="p57123120"><a name="p57123120"></a><a name="p57123120"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.43%" id="mcps1.2.5.1.4"><p id="p63570006"><a name="p63570006"></a><a name="p63570006"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row48896832"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.5.1.1 "><p id="p1220438"><a name="p1220438"></a><a name="p1220438"></a>os-stop</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.2.5.1.2 "><p id="p31746690"><a name="p31746690"></a><a name="p31746690"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.3 "><p id="p21345065"><a name="p21345065"></a><a name="p21345065"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49.43%" headers="mcps1.2.5.1.4 "><p id="p58405349"><a name="p58405349"></a><a name="p58405349"></a>Specifies the operation to stop the ECS. For details, see <a href="#table10346346162744">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **os-stop**  field description

<a name="table10346346162744"></a>
<table><thead align="left"><tr id="row45993853162744"><th class="cellrowborder" valign="top" width="17.1%" id="mcps1.2.5.1.1"><p id="p5888173944215"><a name="p5888173944215"></a><a name="p5888173944215"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.299999999999997%" id="mcps1.2.5.1.2"><p id="p1588833954215"><a name="p1588833954215"></a><a name="p1588833954215"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.16%" id="mcps1.2.5.1.3"><p id="p16888143911424"><a name="p16888143911424"></a><a name="p16888143911424"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.44%" id="mcps1.2.5.1.4"><p id="p10888639134216"><a name="p10888639134216"></a><a name="p10888639134216"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row41908639162744"><td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.2.5.1.1 "><p id="p39156593162744"><a name="p39156593162744"></a><a name="p39156593162744"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.2.5.1.2 "><p id="p17567451162744"><a name="p17567451162744"></a><a name="p17567451162744"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.3 "><p id="p13677446162744"><a name="p13677446162744"></a><a name="p13677446162744"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.44%" headers="mcps1.2.5.1.4 "><p id="p34131354162744"><a name="p34131354162744"></a><a name="p34131354162744"></a>Specifies an ECS stop type. The default value is <strong id="b84235270612825"><a name="b84235270612825"></a><a name="b84235270612825"></a>SOFT</strong>.</p>
<a name="ul1169415154044"></a><a name="ul1169415154044"></a><ul id="ul1169415154044"><li><strong id="b504423009171038"><a name="b504423009171038"></a><a name="b504423009171038"></a>SOFT</strong>: normal ECS stop</li><li><strong id="b8423527061788"><a name="b8423527061788"></a><a name="b8423527061788"></a>HARD</strong>: forcible ECS stop</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section50439840"></a>

None

## Example Request<a name="section38609473427"></a>

```
POST https://{endpoint}/v2.1/{project_id}/servers/{server_id}/action
```

```
{
    "os-stop": {}
}
```

## Example Response<a name="section108329486315"></a>

None

## Returned Values<a name="section51305376"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

