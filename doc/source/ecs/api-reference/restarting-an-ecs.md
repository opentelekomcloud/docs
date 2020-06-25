# Restarting an ECS<a name="EN-US_TOPIC_0020212650"></a>

## Function<a name="section6488958"></a>

This API is used to restart a single ECS.

## URI<a name="section58400626"></a>

POST /v2/\{project\_id\}/servers/\{server\_id\}/action

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/action

[Table 1](#table62669527)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table62669527"></a>
<table><thead align="left"><tr id="row33894570"><th class="cellrowborder" valign="top" width="16.61%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.54%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.85%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8419032"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.4.1.1 "><p id="p10852974"><a name="p10852974"></a><a name="p10852974"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.54%" headers="mcps1.2.4.1.2 "><p id="p6675738"><a name="p6675738"></a><a name="p6675738"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.85%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row34774863"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.4.1.1 "><p id="p65300541"><a name="p65300541"></a><a name="p65300541"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.54%" headers="mcps1.2.4.1.2 "><p id="p54852443"><a name="p54852443"></a><a name="p54852443"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.85%" headers="mcps1.2.4.1.3 "><p id="p13862865"><a name="p13862865"></a><a name="p13862865"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section55843593"></a>

[Table 2](#table37818817)  describes the request parameters.

**Table  2**  Request parameters

<a name="table37818817"></a>
<table><thead align="left"><tr id="row57787318"><th class="cellrowborder" valign="top" width="16.55%" id="mcps1.2.5.1.1"><p id="p50261201"><a name="p50261201"></a><a name="p50261201"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.669999999999998%" id="mcps1.2.5.1.2"><p id="p44625493"><a name="p44625493"></a><a name="p44625493"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.16%" id="mcps1.2.5.1.3"><p id="p57895144"><a name="p57895144"></a><a name="p57895144"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.62%" id="mcps1.2.5.1.4"><p id="p58995125"><a name="p58995125"></a><a name="p58995125"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13875810"><td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.5.1.1 "><p id="p50198807"><a name="p50198807"></a><a name="p50198807"></a>reboot</p>
</td>
<td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.2 "><p id="p39571581"><a name="p39571581"></a><a name="p39571581"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.3 "><p id="p51181499"><a name="p51181499"></a><a name="p51181499"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="49.62%" headers="mcps1.2.5.1.4 "><p id="p65893970"><a name="p65893970"></a><a name="p65893970"></a>Specifies the operation to restart the ECS. For details, see <a href="#table10346346162744">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **reboot**  field description

<a name="table10346346162744"></a>
<table><thead align="left"><tr id="row45993853162744"><th class="cellrowborder" valign="top" width="16.54%" id="mcps1.2.5.1.1"><p id="p8544354193715"><a name="p8544354193715"></a><a name="p8544354193715"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.669999999999998%" id="mcps1.2.5.1.2"><p id="p13544195423710"><a name="p13544195423710"></a><a name="p13544195423710"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.16%" id="mcps1.2.5.1.3"><p id="p154465415374"><a name="p154465415374"></a><a name="p154465415374"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.63%" id="mcps1.2.5.1.4"><p id="p1554412541371"><a name="p1554412541371"></a><a name="p1554412541371"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row41908639162744"><td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.5.1.1 "><p id="p39156593162744"><a name="p39156593162744"></a><a name="p39156593162744"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.2.5.1.2 "><p id="p17567451162744"><a name="p17567451162744"></a><a name="p17567451162744"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.3 "><p id="p13677446162744"><a name="p13677446162744"></a><a name="p13677446162744"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.2.5.1.4 "><p id="p34131354162744"><a name="p34131354162744"></a><a name="p34131354162744"></a>Specifies the type of the restart operation.</p>
<a name="ul1169415154044"></a><a name="ul1169415154044"></a><ul id="ul1169415154044"><li><strong>SOFT</strong>: soft restart</li><li><strong id="b6265247414476"><a name="b6265247414476"></a><a name="b6265247414476"></a>HARD</strong>: forcible restart (hard restart)</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section32830290"></a>

None

## Example Request<a name="section7158465403"></a>

```
POST https://{endpoint}/v2.1/{project_id}/servers/{server_id}/action
```

```
{
    "reboot": {
        "type": "SOFT"
    }
}
```

## Example Response<a name="section271812171439"></a>

None

## Returned Values<a name="section27037160"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

