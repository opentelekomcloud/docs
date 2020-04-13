# Viewing Quotas<a name="EN-US_TOPIC_0128036933"></a>

## Function<a name="section58427690"></a>

This API is used to view the quota of the current project.

## URI<a name="section56087165"></a>

GET /v1.0/\{project\_id\}/quotas/dms

[Table 1](#d0e1978)  describes the parameters of this API.

**Table  1**  Parameters

<a name="d0e1978"></a>
<table><thead align="left"><tr id="row5992637"><th class="cellrowborder" valign="top" width="23.30766923307669%" id="mcps1.2.5.1.1"><p id="p15641626"><a name="p15641626"></a><a name="p15641626"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p59012183"><a name="p59012183"></a><a name="p59012183"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.3"><p id="p647213801718"><a name="p647213801718"></a><a name="p647213801718"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="40.97590240975902%" id="mcps1.2.5.1.4"><p id="p15257500"><a name="p15257500"></a><a name="p15257500"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row27898002"><td class="cellrowborder" valign="top" width="23.30766923307669%" headers="mcps1.2.5.1.1 "><p id="p45145696"><a name="p45145696"></a><a name="p45145696"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p32922799"><a name="p32922799"></a><a name="p32922799"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.3 "><p id="p391918691718"><a name="p391918691718"></a><a name="p391918691718"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.97590240975902%" headers="mcps1.2.5.1.4 "><p id="p49501095"><a name="p49501095"></a><a name="p49501095"></a>Indicates the ID of a project.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section35022440"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section46766508"></a>

**Response parameters**

[Table 2](#d0e2089),  [Table 3](#table6131701015544), and  [Table 4](#table1007748144816)  describe the response parameters.

**Table  2**  Response parameters

<a name="d0e2089"></a>
<table><thead align="left"><tr id="row37189853"><th class="cellrowborder" valign="top" width="24.12%" id="mcps1.2.4.1.1"><p id="p59588135"><a name="p59588135"></a><a name="p59588135"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.12%" id="mcps1.2.4.1.2"><p id="p61909621"><a name="p61909621"></a><a name="p61909621"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.76%" id="mcps1.2.4.1.3"><p id="p48623408"><a name="p48623408"></a><a name="p48623408"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row46181951"><td class="cellrowborder" valign="top" width="24.12%" headers="mcps1.2.4.1.1 "><p id="p46504938144020"><a name="p46504938144020"></a><a name="p46504938144020"></a>quotas</p>
</td>
<td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.2.4.1.2 "><p id="p3261819"><a name="p3261819"></a><a name="p3261819"></a>JSON</p>
</td>
<td class="cellrowborder" valign="top" width="54.76%" headers="mcps1.2.4.1.3 "><p id="p62880759"><a name="p62880759"></a><a name="p62880759"></a>Indicates the quotas of a tenant.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  quotas parameter description

<a name="table6131701015544"></a>
<table><thead align="left"><tr id="row1414270515544"><th class="cellrowborder" valign="top" width="23.93%" id="mcps1.2.4.1.1"><p id="p470844315544"><a name="p470844315544"></a><a name="p470844315544"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.310000000000002%" id="mcps1.2.4.1.2"><p id="p4583962215544"><a name="p4583962215544"></a><a name="p4583962215544"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.76%" id="mcps1.2.4.1.3"><p id="p2202191415544"><a name="p2202191415544"></a><a name="p2202191415544"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4419434315544"><td class="cellrowborder" valign="top" width="23.93%" headers="mcps1.2.4.1.1 "><p id="p2297201515544"><a name="p2297201515544"></a><a name="p2297201515544"></a>resources</p>
</td>
<td class="cellrowborder" valign="top" width="21.310000000000002%" headers="mcps1.2.4.1.2 "><p id="p4879390315544"><a name="p4879390315544"></a><a name="p4879390315544"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="54.76%" headers="mcps1.2.4.1.3 "><p id="p5999208015544"><a name="p5999208015544"></a><a name="p5999208015544"></a>Indicates the list of quotas.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  resources parameter description

<a name="table1007748144816"></a>
<table><thead align="left"><tr id="row2348298144816"><th class="cellrowborder" valign="top" width="24.5%" id="mcps1.2.4.1.1"><p id="p55994482144816"><a name="p55994482144816"></a><a name="p55994482144816"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.74%" id="mcps1.2.4.1.2"><p id="p39259178144816"><a name="p39259178144816"></a><a name="p39259178144816"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.76%" id="mcps1.2.4.1.3"><p id="p25876826144816"><a name="p25876826144816"></a><a name="p25876826144816"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15648171144816"><td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.1 "><p id="p59542340144816"><a name="p59542340144816"></a><a name="p59542340144816"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="20.74%" headers="mcps1.2.4.1.2 "><p id="p58200270144816"><a name="p58200270144816"></a><a name="p58200270144816"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.76%" headers="mcps1.2.4.1.3 "><p id="p16601457144816"><a name="p16601457144816"></a><a name="p16601457144816"></a>Indicates the name of a quota.</p>
</td>
</tr>
<tr id="row7560584144822"><td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.1 "><p id="p936396144822"><a name="p936396144822"></a><a name="p936396144822"></a>quota</p>
</td>
<td class="cellrowborder" valign="top" width="20.74%" headers="mcps1.2.4.1.2 "><p id="p8739288144822"><a name="p8739288144822"></a><a name="p8739288144822"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54.76%" headers="mcps1.2.4.1.3 "><p id="p36793695144822"><a name="p36793695144822"></a><a name="p36793695144822"></a>Indicates the total quota.</p>
</td>
</tr>
<tr id="row645914516564"><td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.1 "><p id="p11459145125615"><a name="p11459145125615"></a><a name="p11459145125615"></a>used</p>
</td>
<td class="cellrowborder" valign="top" width="20.74%" headers="mcps1.2.4.1.2 "><p id="p19459124535615"><a name="p19459124535615"></a><a name="p19459124535615"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54.76%" headers="mcps1.2.4.1.3 "><p id="p194608452569"><a name="p194608452569"></a><a name="p194608452569"></a>Indicates the used quota.</p>
</td>
</tr>
<tr id="row3896171151714"><td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.1 "><p id="p17873113301719"><a name="p17873113301719"></a><a name="p17873113301719"></a>min</p>
</td>
<td class="cellrowborder" valign="top" width="20.74%" headers="mcps1.2.4.1.2 "><p id="p18984119175"><a name="p18984119175"></a><a name="p18984119175"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54.76%" headers="mcps1.2.4.1.3 "><p id="p289811121715"><a name="p289811121715"></a><a name="p289811121715"></a>Indicates the minimum value that a quota must reach.</p>
</td>
</tr>
<tr id="row777520152173"><td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.1 "><p id="p1091113541716"><a name="p1091113541716"></a><a name="p1091113541716"></a>max</p>
</td>
<td class="cellrowborder" valign="top" width="20.74%" headers="mcps1.2.4.1.2 "><p id="p577511514176"><a name="p577511514176"></a><a name="p577511514176"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54.76%" headers="mcps1.2.4.1.3 "><p id="p13775101510176"><a name="p13775101510176"></a><a name="p13775101510176"></a>Indicates the maximum value that a quota cannot exceed.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
  "quotas" : {
    "resources" : [{
        "type" : "queue",
        "quota" : 30,
        "used" : 5,
        "min" : 0,
        "max" : 500
      } 
    ]
  }
}
```

## Status Code<a name="section18245395"></a>

[Table 5](#d0e2143)  lists the status code indicating that the operation is successful. For details about the status codes indicating that the operation fails, see  [Status Code](status-code.md).

**Table  5**  Status code

<a name="d0e2143"></a>
<table><thead align="left"><tr id="row46146710"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.3.1.1"><p id="p46896054"><a name="p46896054"></a><a name="p46896054"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="77.25999999999999%" id="mcps1.2.3.1.2"><p id="p40484047"><a name="p40484047"></a><a name="p40484047"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row57982344"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.3.1.1 "><p id="p66058249"><a name="p66058249"></a><a name="p66058249"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="77.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p49117947"><a name="p49117947"></a><a name="p49117947"></a>The information is obtained successfully.</p>
</td>
</tr>
</tbody>
</table>

