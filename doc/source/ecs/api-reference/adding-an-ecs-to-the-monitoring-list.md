# Adding an ECS to the Monitoring List<a name="EN-US_TOPIC_0081529857"></a>

## Function<a name="section3492751018840"></a>

This API is used to add an ECS to the monitoring list.

Ceilometer periodically collects monitoring data on the ECSs added to the monitoring list and reports the data to Cloud Eye. The data includes the platform version, CPU, memory, NICs, disks, and hardware version. For example, the plug-in of an SAP ECS periodically obtains monitoring data from Cloud Eye and reports the data to SAP in reports.

## URI<a name="section3752955218923"></a>

POST /v1.0/servers/\{server\_id\}/action

[Table 1](#table3713317418952)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table3713317418952"></a>
<table><thead align="left"><tr id="row5865996918952"><th class="cellrowborder" valign="top" width="20.43%" id="mcps1.2.4.1.1"><p id="p5383705918952"><a name="p5383705918952"></a><a name="p5383705918952"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.49%" id="mcps1.2.4.1.2"><p id="p6583454618952"><a name="p6583454618952"></a><a name="p6583454618952"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="62.08%" id="mcps1.2.4.1.3"><p id="p3099800518952"><a name="p3099800518952"></a><a name="p3099800518952"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2781048518952"><td class="cellrowborder" valign="top" width="20.43%" headers="mcps1.2.4.1.1 "><p id="p3805679318952"><a name="p3805679318952"></a><a name="p3805679318952"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.4.1.2 "><p id="p6270138618952"><a name="p6270138618952"></a><a name="p6270138618952"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.08%" headers="mcps1.2.4.1.3 "><p id="p4564747118952"><a name="p4564747118952"></a><a name="p4564747118952"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section61456643181021"></a>

[Table 2](#table20892986181041)  describes the request parameters.

**Table  2**  Request parameters

<a name="table20892986181041"></a>
<table><thead align="left"><tr id="row38729067181041"><th class="cellrowborder" valign="top" width="20.44%" id="mcps1.2.5.1.1"><p id="p50046718181041"><a name="p50046718181041"></a><a name="p50046718181041"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.2"><p id="p27252366181041"><a name="p27252366181041"></a><a name="p27252366181041"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="11.66%" id="mcps1.2.5.1.3"><p id="p59958018181041"><a name="p59958018181041"></a><a name="p59958018181041"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.61%" id="mcps1.2.5.1.4"><p id="p24761283181041"><a name="p24761283181041"></a><a name="p24761283181041"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row59506872181041"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.2.5.1.1 "><p id="p55327305181041"><a name="p55327305181041"></a><a name="p55327305181041"></a>monitorMetrics</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p52326752181041"><a name="p52326752181041"></a><a name="p52326752181041"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.66%" headers="mcps1.2.5.1.3 "><p id="p10608482181041"><a name="p10608482181041"></a><a name="p10608482181041"></a>Null</p>
</td>
<td class="cellrowborder" valign="top" width="50.61%" headers="mcps1.2.5.1.4 "><p id="p53980729181041"><a name="p53980729181041"></a><a name="p53980729181041"></a>Adds an ECS to the monitoring list.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section7035651181135"></a>

None

## Example Request<a name="section65518423453"></a>

```
POST https://{endpoint}/v1.0/servers/{server_id}/action
```

```
{  
   "monitorMetrics" : null 
}
```

## Example Response<a name="section733344563613"></a>

None

## Returned Values<a name="section4901036318129"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).

