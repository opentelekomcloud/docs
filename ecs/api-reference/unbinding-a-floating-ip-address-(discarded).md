# Unbinding a Floating IP Address \(Discarded\)<a name="EN-US_TOPIC_0065817719"></a>

## Function<a name="en-us_topic_0057973008_section9177509"></a>

This API is used to unbind a floating IP address from an ECS.

## Constraints<a name="en-us_topic_0057973008_section5180770"></a>

-   This API will become invalid from microversion 2.44. Since this version, the system will return error 404 when you call this API. You are advised to use the VPC API "Updating a Floating IP Address".

## URI<a name="en-us_topic_0057973008_section15488722"></a>

POST /v2/\{project\_id\}/servers/\{server\_id\}/action

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/action

[Table 1](#en-us_topic_0057973008_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973008_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057973008_row44937496"><th class="cellrowborder" valign="top" width="22.24%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.87%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="55.88999999999999%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973008_row1664874"><td class="cellrowborder" valign="top" width="22.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973008_p637140"><a name="en-us_topic_0057973008_p637140"></a><a name="en-us_topic_0057973008_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973008_p51608407"><a name="en-us_topic_0057973008_p51608407"></a><a name="en-us_topic_0057973008_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="55.88999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973008_row41565035"><td class="cellrowborder" valign="top" width="22.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973008_p11324657"><a name="en-us_topic_0057973008_p11324657"></a><a name="en-us_topic_0057973008_p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973008_p44882061"><a name="en-us_topic_0057973008_p44882061"></a><a name="en-us_topic_0057973008_p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="55.88999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973008_p11568292"><a name="en-us_topic_0057973008_p11568292"></a><a name="en-us_topic_0057973008_p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973008_section16989244"></a>

[Table 2](#en-us_topic_0057973008_table20592177)  describes the request parameters.

**Table  2**  Request parameter

<a name="en-us_topic_0057973008_table20592177"></a>
<table><thead align="left"><tr id="en-us_topic_0057973008_row40662280"><th class="cellrowborder" valign="top" width="17.27%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057973008_p5310363"><a name="en-us_topic_0057973008_p5310363"></a><a name="en-us_topic_0057973008_p5310363"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.83%" id="mcps1.2.5.1.2"><p id="p17106184382112"><a name="p17106184382112"></a><a name="p17106184382112"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="27.24%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057973008_p27486230"><a name="en-us_topic_0057973008_p27486230"></a><a name="en-us_topic_0057973008_p27486230"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="36.66%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057973008_p15641062"><a name="en-us_topic_0057973008_p15641062"></a><a name="en-us_topic_0057973008_p15641062"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973008_row58966539"><td class="cellrowborder" valign="top" width="17.27%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973008_p11560377"><a name="en-us_topic_0057973008_p11560377"></a><a name="en-us_topic_0057973008_p11560377"></a>removeFloatingIp</p>
</td>
<td class="cellrowborder" valign="top" width="18.83%" headers="mcps1.2.5.1.2 "><p id="p1710614437211"><a name="p1710614437211"></a><a name="p1710614437211"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="27.24%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973008_p63975319"><a name="en-us_topic_0057973008_p63975319"></a><a name="en-us_topic_0057973008_p63975319"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="36.66%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973008_p43233028"><a name="en-us_topic_0057973008_p43233028"></a><a name="en-us_topic_0057973008_p43233028"></a>Unbinds a floating IP address from an ECS.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **removeFloatingIp**  parameter information

<a name="en-us_topic_0057973008_table12214371"></a>
<table><thead align="left"><tr id="en-us_topic_0057973008_row11201709"><th class="cellrowborder" valign="top" width="17.03%" id="mcps1.2.5.1.1"><p id="p61001030132313"><a name="p61001030132313"></a><a name="p61001030132313"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.07%" id="mcps1.2.5.1.2"><p id="p10534105692116"><a name="p10534105692116"></a><a name="p10534105692116"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="27.24%" id="mcps1.2.5.1.3"><p id="p4100163062315"><a name="p4100163062315"></a><a name="p4100163062315"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="36.66%" id="mcps1.2.5.1.4"><p id="p71001930132315"><a name="p71001930132315"></a><a name="p71001930132315"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973008_row48978777"><td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973008_p7857996"><a name="en-us_topic_0057973008_p7857996"></a><a name="en-us_topic_0057973008_p7857996"></a>address</p>
</td>
<td class="cellrowborder" valign="top" width="19.07%" headers="mcps1.2.5.1.2 "><p id="p5534156112113"><a name="p5534156112113"></a><a name="p5534156112113"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="27.24%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973008_p32517948"><a name="en-us_topic_0057973008_p32517948"></a><a name="en-us_topic_0057973008_p32517948"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.66%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973008_p11179825"><a name="en-us_topic_0057973008_p11179825"></a><a name="en-us_topic_0057973008_p11179825"></a>Specifies the floating IP address.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0057973008_section18685471"></a>

None

## Example Request<a name="en-us_topic_0057973008_section33951514"></a>

```
POST https://{endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/servers/47e9be4e-a7b9-471f-92d9-ffc83814e07a/action
POST https://{endpoint}/v2.1/9c53a566cb3443ab910cf0daebca90c4/servers/47e9be4e-a7b9-471f-92d9-ffc83814e07a/action
```

```
{
   "removeFloatingIp" : {
        "address" : "10.144.2.1"
    }
}
```

## Example Response<a name="section1497194212473"></a>

None

## Returned Values<a name="en-us_topic_0057973008_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

