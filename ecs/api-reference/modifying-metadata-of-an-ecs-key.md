# Modifying Metadata of an ECS Key<a name="EN-US_TOPIC_0025567413"></a>

## Function<a name="section19950704192629"></a>

This API is used to modify the metadata of an ECS key.

-   If the metadata does not contain the target field, the field is automatically added.
-   If the metadata contains the target field, the field value is automatically updated.

## Constraints<a name="section178513519245"></a>

An ECS must be in active, stopped, paused, or suspended state, which is specified by  **OS-EXT-STS:vm\_state**.

## URI<a name="section48549151192629"></a>

PUT /v2/\{project\_id\}/servers/\{server\_id\}/metadata/\{key\}

PUT /v2.1/\{project\_id\}/servers/\{server\_id\}/metadata/\{key\}

[Table 1](#table258804192629)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table258804192629"></a>
<table><thead align="left"><tr id="row33277594192629"><th class="cellrowborder" valign="top" width="16.42%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.16%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.42%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row56232837192629"><td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.1 "><p id="p58565959192629"><a name="p58565959192629"></a><a name="p58565959192629"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p46222262192629"><a name="p46222262192629"></a><a name="p46222262192629"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.42%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row7379590192629"><td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.1 "><p id="p60875907192629"><a name="p60875907192629"></a><a name="p60875907192629"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p32001416192629"><a name="p32001416192629"></a><a name="p32001416192629"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.42%" headers="mcps1.2.4.1.3 "><p id="p41977918192629"><a name="p41977918192629"></a><a name="p41977918192629"></a>Specifies the ECS ID.</p>
</td>
</tr>
<tr id="row1185148119279"><td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.1 "><p id="p2044590819279"><a name="p2044590819279"></a><a name="p2044590819279"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p4550582719279"><a name="p4550582719279"></a><a name="p4550582719279"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.42%" headers="mcps1.2.4.1.3 "><p id="p6209335919279"><a name="p6209335919279"></a><a name="p6209335919279"></a>Specifies the ECS metadata key to be modified.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section42256947192629"></a>

[Table 2](#table21113531192629)  describes the request parameters.

**Table  2**  Request parameters

<a name="table21113531192629"></a>
<table><thead align="left"><tr id="row12974012192629"><th class="cellrowborder" valign="top" width="16.36%" id="mcps1.2.5.1.1"><p id="p44262053192629"><a name="p44262053192629"></a><a name="p44262053192629"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.09%" id="mcps1.2.5.1.2"><p id="p28456575192629"><a name="p28456575192629"></a><a name="p28456575192629"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="11.469999999999999%" id="mcps1.2.5.1.3"><p id="p23281266192629"><a name="p23281266192629"></a><a name="p23281266192629"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.08%" id="mcps1.2.5.1.4"><p id="p6734373192629"><a name="p6734373192629"></a><a name="p6734373192629"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8613312192629"><td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.2.5.1.1 "><p id="p26589676192629"><a name="p26589676192629"></a><a name="p26589676192629"></a>meta</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.2.5.1.2 "><p id="p6280144192629"><a name="p6280144192629"></a><a name="p6280144192629"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.2.5.1.3 "><p id="p38929685192629"><a name="p38929685192629"></a><a name="p38929685192629"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="55.08%" headers="mcps1.2.5.1.4 "><p id="p59800316192629"><a name="p59800316192629"></a><a name="p59800316192629"></a>Specifies the user-defined metadata key pair.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **meta**  field description

<a name="table40778039192629"></a>
<table><thead align="left"><tr id="row63796811192629"><th class="cellrowborder" valign="top" width="16.36%" id="mcps1.2.5.1.1"><p id="p339195083012"><a name="p339195083012"></a><a name="p339195083012"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.09%" id="mcps1.2.5.1.2"><p id="p1339118502309"><a name="p1339118502309"></a><a name="p1339118502309"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="11.469999999999999%" id="mcps1.2.5.1.3"><p id="p939120502303"><a name="p939120502303"></a><a name="p939120502303"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.08%" id="mcps1.2.5.1.4"><p id="p183911350183017"><a name="p183911350183017"></a><a name="p183911350183017"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row861719548144"><td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.2.5.1.1 "><p id="p1089262011454"><a name="p1089262011454"></a><a name="p1089262011454"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.2.5.1.2 "><p id="p18894122014512"><a name="p18894122014512"></a><a name="p18894122014512"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.2.5.1.3 "><p id="p220493014454"><a name="p220493014454"></a><a name="p220493014454"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.08%" headers="mcps1.2.5.1.4 "><p id="p19894192011457"><a name="p19894192011457"></a><a name="p19894192011457"></a>Specifies the tag key.</p>
<p id="p146113814453"><a name="p146113814453"></a><a name="p146113814453"></a>It contains a maximum of 255 Unicode characters and cannot be blank. The value can contain uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), hyphens (-), underscores (_), colons (:), and periods (.).</p>
</td>
</tr>
<tr id="row30326018192629"><td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.2.5.1.1 "><p id="p40878540185333"><a name="p40878540185333"></a><a name="p40878540185333"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.2.5.1.2 "><p id="p22827413185333"><a name="p22827413185333"></a><a name="p22827413185333"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.469999999999999%" headers="mcps1.2.5.1.3 "><p id="p37081126185333"><a name="p37081126185333"></a><a name="p37081126185333"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.08%" headers="mcps1.2.5.1.4 "><p id="p999582373317"><a name="p999582373317"></a><a name="p999582373317"></a>Specifies the tag value.</p>
<p id="p58906615396"><a name="p58906615396"></a><a name="p58906615396"></a>It contains a maximum of 255 Unicode characters.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section12391939192629"></a>

[Table 4](#table34681280192629)  describes the response parameters.

**Table  4**  Response parameters

<a name="table34681280192629"></a>
<table><thead align="left"><tr id="row7754416192629"><th class="cellrowborder" valign="top" width="16.48%" id="mcps1.2.4.1.1"><p id="p24127969192629"><a name="p24127969192629"></a><a name="p24127969192629"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.2.4.1.2"><p id="p8208474192629"><a name="p8208474192629"></a><a name="p8208474192629"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.05%" id="mcps1.2.4.1.3"><p id="p60906692192629"><a name="p60906692192629"></a><a name="p60906692192629"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row34495047192629"><td class="cellrowborder" valign="top" width="16.48%" headers="mcps1.2.4.1.1 "><p id="p42635402192629"><a name="p42635402192629"></a><a name="p42635402192629"></a>meta</p>
</td>
<td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.2 "><p id="p30915509192629"><a name="p30915509192629"></a><a name="p30915509192629"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="67.05%" headers="mcps1.2.4.1.3 "><p id="p55937021192629"><a name="p55937021192629"></a><a name="p55937021192629"></a>Specifies the user-defined metadata key-value pair.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section1854919457276"></a>

```
PUT https://{endpoint}/v2/{project_id}/servers/{server_id}/metadata/{key}
PUT https://{endpoint}/v2.1/{project_id}/servers/{server_id}/metadata/{key}
```

```
{
    "meta":{
        "key":"value"
    }
} 
```

## Example Response<a name="section06122457441"></a>

```
{
    "meta":{
        "key":"value"
    }
} 
```

## Returned Values<a name="section38207615192629"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

