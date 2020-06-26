# Querying the Specified Network of an ECS<a name="EN-US_TOPIC_0031169059"></a>

## Function<a name="section53922917165259"></a>

This API is used to query the specified network of an ECS.

## Constraints<a name="section64211377173223"></a>

None

## URI<a name="section51121191165259"></a>

GET /v2/\{project\_id\}/servers/\{server\_id\}/ips/\{networkName\}

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/ips/\{networkName\}

[Table 1](#table60562285165259)  describes the parameters in the URI.

**Table  1**  Path parameters

<a name="table60562285165259"></a>
<table><thead align="left"><tr id="row4861884165259"><th class="cellrowborder" valign="top" width="18.48%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="64.17%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row63809876165259"><td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.2.4.1.1 "><p id="p1217433165259"><a name="p1217433165259"></a><a name="p1217433165259"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p31503226165259"><a name="p31503226165259"></a><a name="p31503226165259"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="64.17%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Request parameters

<a name="table1051945864112"></a>
<table><thead align="left"><tr id="row13519135844110"><th class="cellrowborder" valign="top" width="18.459999999999997%" id="mcps1.2.5.1.1"><p id="p1494123091511"><a name="p1494123091511"></a><a name="p1494123091511"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.22%" id="mcps1.2.5.1.2"><p id="p9494630131514"><a name="p9494630131514"></a><a name="p9494630131514"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.120000000000001%" id="mcps1.2.5.1.3"><p id="p19764237111514"><a name="p19764237111514"></a><a name="p19764237111514"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.2%" id="mcps1.2.5.1.4"><p id="p6494030121520"><a name="p6494030121520"></a><a name="p6494030121520"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6533658174112"><td class="cellrowborder" valign="top" width="18.459999999999997%" headers="mcps1.2.5.1.1 "><p id="p11533958134116"><a name="p11533958134116"></a><a name="p11533958134116"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.22%" headers="mcps1.2.5.1.2 "><p id="p19533958124119"><a name="p19533958124119"></a><a name="p19533958124119"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.120000000000001%" headers="mcps1.2.5.1.3 "><p id="p9764153718155"><a name="p9764153718155"></a><a name="p9764153718155"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.2%" headers="mcps1.2.5.1.4 "><p id="p12533558154116"><a name="p12533558154116"></a><a name="p12533558154116"></a>Specifies the ECS ID.</p>
</td>
</tr>
<tr id="row85331158174111"><td class="cellrowborder" valign="top" width="18.459999999999997%" headers="mcps1.2.5.1.1 "><p id="p1153315585416"><a name="p1153315585416"></a><a name="p1153315585416"></a>networkName</p>
</td>
<td class="cellrowborder" valign="top" width="17.22%" headers="mcps1.2.5.1.2 "><p id="p195337587419"><a name="p195337587419"></a><a name="p195337587419"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.120000000000001%" headers="mcps1.2.5.1.3 "><p id="p87642037171514"><a name="p87642037171514"></a><a name="p87642037171514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.2%" headers="mcps1.2.5.1.4 "><p id="p15339586411"><a name="p15339586411"></a><a name="p15339586411"></a>Specifies the ECS network name.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section169561520543"></a>

None

## Response<a name="section58140617165259"></a>

[Table 3](#table56891490143956)  describes the response parameters.

**Table  3**  Response parameters

<a name="table56891490143956"></a>
<table><thead align="left"><tr id="row33903869143956"><th class="cellrowborder" valign="top" width="18.73%" id="mcps1.2.4.1.1"><p id="p61858896143956"><a name="p61858896143956"></a><a name="p61858896143956"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.649999999999999%" id="mcps1.2.4.1.2"><p id="p44514659143956"><a name="p44514659143956"></a><a name="p44514659143956"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.62%" id="mcps1.2.4.1.3"><p id="p2902506143956"><a name="p2902506143956"></a><a name="p2902506143956"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row33776430143956"><td class="cellrowborder" valign="top" width="18.73%" headers="mcps1.2.4.1.1 "><p id="p51536339143956"><a name="p51536339143956"></a><a name="p51536339143956"></a>Name of the network where the ECS accesses</p>
</td>
<td class="cellrowborder" valign="top" width="14.649999999999999%" headers="mcps1.2.4.1.2 "><p id="p13693953143956"><a name="p13693953143956"></a><a name="p13693953143956"></a>List(Dict)</p>
</td>
<td class="cellrowborder" valign="top" width="66.62%" headers="mcps1.2.4.1.3 "><p id="p54366741143956"><a name="p54366741143956"></a><a name="p54366741143956"></a>Specifies the network where the ECS accesses. For details about the network, see <a href="#table22651992144025">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  ECS network parameter structure description

<a name="table22651992144025"></a>
<table><thead align="left"><tr id="row15576094144025"><th class="cellrowborder" valign="top" width="14.84851514848515%" id="mcps1.2.7.1.1"><p id="p53704088144025"><a name="p53704088144025"></a><a name="p53704088144025"></a>Attribute</p>
</th>
<th class="cellrowborder" valign="top" width="9.959004099590041%" id="mcps1.2.7.1.2"><p id="p55063891144025"><a name="p55063891144025"></a><a name="p55063891144025"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="11.0988901109889%" id="mcps1.2.7.1.3"><p id="p30990199144025"><a name="p30990199144025"></a><a name="p30990199144025"></a>CRUD</p>
</th>
<th class="cellrowborder" valign="top" width="12.028797120287972%" id="mcps1.2.7.1.4"><p id="p27178154144025"><a name="p27178154144025"></a><a name="p27178154144025"></a>Default Value</p>
</th>
<th class="cellrowborder" valign="top" width="16.928307169283073%" id="mcps1.2.7.1.5"><p id="p53946903144025"><a name="p53946903144025"></a><a name="p53946903144025"></a>Constraint</p>
</th>
<th class="cellrowborder" valign="top" width="35.136486351364866%" id="mcps1.2.7.1.6"><p id="p7623012144025"><a name="p7623012144025"></a><a name="p7623012144025"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row1498246144025"><td class="cellrowborder" valign="top" width="14.84851514848515%" headers="mcps1.2.7.1.1 "><p id="p54249095144025"><a name="p54249095144025"></a><a name="p54249095144025"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="9.959004099590041%" headers="mcps1.2.7.1.2 "><p id="p32100540144025"><a name="p32100540144025"></a><a name="p32100540144025"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="11.0988901109889%" headers="mcps1.2.7.1.3 "><p id="p50006925144025"><a name="p50006925144025"></a><a name="p50006925144025"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="12.028797120287972%" headers="mcps1.2.7.1.4 "><p id="p24029156144025"><a name="p24029156144025"></a><a name="p24029156144025"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="16.928307169283073%" headers="mcps1.2.7.1.5 "><p id="p204582144025"><a name="p204582144025"></a><a name="p204582144025"></a>4 or 6</p>
</td>
<td class="cellrowborder" valign="top" width="35.136486351364866%" headers="mcps1.2.7.1.6 "><p id="p16571197144025"><a name="p16571197144025"></a><a name="p16571197144025"></a>Specifies the IP address version. The value of this parameter can be <strong id="b49505674143946"><a name="b49505674143946"></a><a name="b49505674143946"></a>4</strong> or <strong id="b32947804143949"><a name="b32947804143949"></a><a name="b32947804143949"></a>6</strong>.</p>
</td>
</tr>
<tr id="row14923052144025"><td class="cellrowborder" valign="top" width="14.84851514848515%" headers="mcps1.2.7.1.1 "><p id="p807709144025"><a name="p807709144025"></a><a name="p807709144025"></a>addr</p>
</td>
<td class="cellrowborder" valign="top" width="9.959004099590041%" headers="mcps1.2.7.1.2 "><p id="p65424470144025"><a name="p65424470144025"></a><a name="p65424470144025"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="11.0988901109889%" headers="mcps1.2.7.1.3 "><p id="p64890752144025"><a name="p64890752144025"></a><a name="p64890752144025"></a>R</p>
</td>
<td class="cellrowborder" valign="top" width="12.028797120287972%" headers="mcps1.2.7.1.4 "><p id="p21659587144025"><a name="p21659587144025"></a><a name="p21659587144025"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="16.928307169283073%" headers="mcps1.2.7.1.5 "><p id="p9596102144025"><a name="p9596102144025"></a><a name="p9596102144025"></a>IP address format</p>
</td>
<td class="cellrowborder" valign="top" width="35.136486351364866%" headers="mcps1.2.7.1.6 "><p id="p39086769144025"><a name="p39086769144025"></a><a name="p39086769144025"></a>Specifies the IP address.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section970712100142"></a>

```
GET https://{endpoint}/v2/{project_id}/servers/{server_id}/ips/{networkName}
GET https://{endpoint}/v2.1/{project_id}/servers/{server_id}/ips/{networkName}
```

## Example Response<a name="section14612172044110"></a>

```
{
    "demo_net": [
        {
            "version": 4,
            "addr": "10.0.0.4"
        },
        {
            "version": 4,
            "addr": "192.150.73.132"
        }
    ]
}
```

## Returned Values<a name="section38817202165259"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

