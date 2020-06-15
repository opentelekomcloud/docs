# Binding a Floating IP Address \(Discarded\)<a name="EN-US_TOPIC_0065817718"></a>

## Function<a name="en-us_topic_0057972997_section32822464"></a>

This API is used to bind a floating IP address to an ECS.

## Constraints<a name="en-us_topic_0057972997_section41373960"></a>

-   This API will become invalid from microversion 2.44. Since this version, the system will return error 404 when you call this API. You are advised to use the VPC API "Updating a Floating IP Address".

## URI<a name="en-us_topic_0057972997_section26966728"></a>

POST /v2/\{project\_id\}/servers/\{server\_id\}/action

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/action

[Table 1](#en-us_topic_0057972997_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972997_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057972997_row44937496"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="61.61616161616161%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972997_row1664874"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972997_p637140"><a name="en-us_topic_0057972997_p637140"></a><a name="en-us_topic_0057972997_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972997_p51608407"><a name="en-us_topic_0057972997_p51608407"></a><a name="en-us_topic_0057972997_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972997_row41565035"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972997_p11324657"><a name="en-us_topic_0057972997_p11324657"></a><a name="en-us_topic_0057972997_p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972997_p44882061"><a name="en-us_topic_0057972997_p44882061"></a><a name="en-us_topic_0057972997_p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972997_p11568292"><a name="en-us_topic_0057972997_p11568292"></a><a name="en-us_topic_0057972997_p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972997_section62956448"></a>

[Table 2](#en-us_topic_0057972997_table49322741)  describes the request parameters.

**Table  2**  Request parameter

<a name="en-us_topic_0057972997_table49322741"></a>
<table><thead align="left"><tr id="en-us_topic_0057972997_row35749488"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057972997_p10027379"><a name="en-us_topic_0057972997_p10027379"></a><a name="en-us_topic_0057972997_p10027379"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.2"><p id="p1579692179"><a name="p1579692179"></a><a name="p1579692179"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057972997_p6911408"><a name="en-us_topic_0057972997_p6911408"></a><a name="en-us_topic_0057972997_p6911408"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057972997_p47267058"><a name="en-us_topic_0057972997_p47267058"></a><a name="en-us_topic_0057972997_p47267058"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972997_row3426504"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972997_p9111414"><a name="en-us_topic_0057972997_p9111414"></a><a name="en-us_topic_0057972997_p9111414"></a>addFloatingIp</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p2057918910178"><a name="p2057918910178"></a><a name="p2057918910178"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972997_p66935973"><a name="en-us_topic_0057972997_p66935973"></a><a name="en-us_topic_0057972997_p66935973"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972997_p6518693"><a name="en-us_topic_0057972997_p6518693"></a><a name="en-us_topic_0057972997_p6518693"></a>Specifies the floating IP address to be bound to an ECS.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **addFloatingIp**  parameter information

<a name="en-us_topic_0057972997_table58252101"></a>
<table><thead align="left"><tr id="en-us_topic_0057972997_row45148248"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p863285611197"><a name="p863285611197"></a><a name="p863285611197"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.2"><p id="p8861511151711"><a name="p8861511151711"></a><a name="p8861511151711"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p86328569191"><a name="p86328569191"></a><a name="p86328569191"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.5.1.4"><p id="p863217564195"><a name="p863217564195"></a><a name="p863217564195"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972997_row23607505"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972997_p33159773"><a name="en-us_topic_0057972997_p33159773"></a><a name="en-us_topic_0057972997_p33159773"></a>address</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p88619112175"><a name="p88619112175"></a><a name="p88619112175"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972997_p1587126"><a name="en-us_topic_0057972997_p1587126"></a><a name="en-us_topic_0057972997_p1587126"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972997_p11263469"><a name="en-us_topic_0057972997_p11263469"></a><a name="en-us_topic_0057972997_p11263469"></a>Specifies the floating IP address.</p>
</td>
</tr>
<tr id="en-us_topic_0057972997_row34262360"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972997_p23787767"><a name="en-us_topic_0057972997_p23787767"></a><a name="en-us_topic_0057972997_p23787767"></a>fixed_address</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p3861211201716"><a name="p3861211201716"></a><a name="p3861211201716"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972997_p47760999"><a name="en-us_topic_0057972997_p47760999"></a><a name="en-us_topic_0057972997_p47760999"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972997_p28633049"><a name="en-us_topic_0057972997_p28633049"></a><a name="en-us_topic_0057972997_p28633049"></a>Specifies the fixed IP address with which the floating IP address associates.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0057972997_section29737121"></a>

None

## Example Request<a name="en-us_topic_0057972997_section66307504"></a>

```
POST https://{endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/servers/47e9be4e-a7b9-471f-92d9-ffc83814e07a/action
POST https://{endpoint}/v2.1/9c53a566cb3443ab910cf0daebca90c4/servers/47e9be4e-a7b9-471f-92d9-ffc83814e07a/action
```

```
{
   "addFloatingIp" : {
       "address" : "10.144.2.1",
       "fixed_address" : "192.168.1.3"
    }
}
```

## Example Response<a name="section462213664713"></a>

None

## Returned Values<a name="en-us_topic_0057972997_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

