# Updating ECS Metadata<a name="EN-US_TOPIC_0025560298"></a>

## Function<a name="section61558535185333"></a>

This API is used to update ECS metadata.

-   If the metadata does not contain the target field, the field is automatically added.
-   If the metadata contains the target field, the field value is automatically updated.
-   If the field in the metadata is not requested, the field value remains unchanged.

## Constraints<a name="section39865556127"></a>

An ECS must be in active, stopped, paused, or suspended state, which is specified by  **OS-EXT-STS:vm\_state**.

## URI<a name="section47451206185333"></a>

POST /v2/\{project\_id\}/servers/\{server\_id\}/metadata

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/metadata

[Table 1](#table18618337185333)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table18618337185333"></a>
<table><thead align="left"><tr id="row17183202185333"><th class="cellrowborder" valign="top" width="16.79%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.03999999999999%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row30151070185333"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="p26317623185333"><a name="p26317623185333"></a><a name="p26317623185333"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p51352688185333"><a name="p51352688185333"></a><a name="p51352688185333"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.03999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row56472316185333"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="p10854909185333"><a name="p10854909185333"></a><a name="p10854909185333"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p6832475185333"><a name="p6832475185333"></a><a name="p6832475185333"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.03999999999999%" headers="mcps1.2.4.1.3 "><p id="p16559613185333"><a name="p16559613185333"></a><a name="p16559613185333"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section14818796185333"></a>

[Table 2](#table52485804185333)  describes the request parameters.

**Table  2**  Request parameters

<a name="table52485804185333"></a>
<table><thead align="left"><tr id="row22430249185333"><th class="cellrowborder" valign="top" width="16.73%" id="mcps1.2.5.1.1"><p id="p4910858185333"><a name="p4910858185333"></a><a name="p4910858185333"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.2"><p id="p62235249185333"><a name="p62235249185333"></a><a name="p62235249185333"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="11.84%" id="mcps1.2.5.1.3"><p id="p7890371185333"><a name="p7890371185333"></a><a name="p7890371185333"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.14%" id="mcps1.2.5.1.4"><p id="p35140330185333"><a name="p35140330185333"></a><a name="p35140330185333"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row27794510185333"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.1 "><p id="p36762838185333"><a name="p36762838185333"></a><a name="p36762838185333"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p24999915185333"><a name="p24999915185333"></a><a name="p24999915185333"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.84%" headers="mcps1.2.5.1.3 "><p id="p11727220185333"><a name="p11727220185333"></a><a name="p11727220185333"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="54.14%" headers="mcps1.2.5.1.4 "><p id="p26317995185333"><a name="p26317995185333"></a><a name="p26317995185333"></a>Specifies the user-defined metadata key-value pair.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **metadata**  field description

<a name="table59792218185333"></a>
<table><thead align="left"><tr id="row39910345185333"><th class="cellrowborder" valign="top" width="16.73%" id="mcps1.2.5.1.1"><p id="p11512487185333"><a name="p11512487185333"></a><a name="p11512487185333"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.2"><p id="p60096221185333"><a name="p60096221185333"></a><a name="p60096221185333"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="11.84%" id="mcps1.2.5.1.3"><p id="p35955732185333"><a name="p35955732185333"></a><a name="p35955732185333"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.14%" id="mcps1.2.5.1.4"><p id="p26733171185333"><a name="p26733171185333"></a><a name="p26733171185333"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15890112034514"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.1 "><p id="p1089262011454"><a name="p1089262011454"></a><a name="p1089262011454"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p18894122014512"><a name="p18894122014512"></a><a name="p18894122014512"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.84%" headers="mcps1.2.5.1.3 "><p id="p220493014454"><a name="p220493014454"></a><a name="p220493014454"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.14%" headers="mcps1.2.5.1.4 "><p id="p19894192011457"><a name="p19894192011457"></a><a name="p19894192011457"></a>Specifies the tag key.</p>
<p id="p146113814453"><a name="p146113814453"></a><a name="p146113814453"></a>It contains a maximum of 255 Unicode characters and cannot be blank. The value can contain uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), hyphens (-), underscores (_), colons (:), and periods (.).</p>
</td>
</tr>
<tr id="row17903267185333"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.1 "><p id="p40878540185333"><a name="p40878540185333"></a><a name="p40878540185333"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p22827413185333"><a name="p22827413185333"></a><a name="p22827413185333"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.84%" headers="mcps1.2.5.1.3 "><p id="p37081126185333"><a name="p37081126185333"></a><a name="p37081126185333"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.14%" headers="mcps1.2.5.1.4 "><p id="p999582373317"><a name="p999582373317"></a><a name="p999582373317"></a>Specifies the tag value.</p>
<p id="p58906615396"><a name="p58906615396"></a><a name="p58906615396"></a>It contains a maximum of 255 Unicode characters.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section22254218185333"></a>

[Table 4](#table48150236185333)  describes the response parameters.

**Table  4**  Response parameters

<a name="table48150236185333"></a>
<table><thead align="left"><tr id="row64499137185333"><th class="cellrowborder" valign="top" width="16.74%" id="mcps1.2.4.1.1"><p id="p57047574185333"><a name="p57047574185333"></a><a name="p57047574185333"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.43%" id="mcps1.2.4.1.2"><p id="p57450759185333"><a name="p57450759185333"></a><a name="p57450759185333"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.83%" id="mcps1.2.4.1.3"><p id="p22999934185333"><a name="p22999934185333"></a><a name="p22999934185333"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row51055328185333"><td class="cellrowborder" valign="top" width="16.74%" headers="mcps1.2.4.1.1 "><p id="p41840919185333"><a name="p41840919185333"></a><a name="p41840919185333"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="15.43%" headers="mcps1.2.4.1.2 "><p id="p33671307185333"><a name="p33671307185333"></a><a name="p33671307185333"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="67.83%" headers="mcps1.2.4.1.3 "><p id="p51647808185333"><a name="p51647808185333"></a><a name="p51647808185333"></a>Specifies the user-defined metadata key-value pair.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section1124134931510"></a>

```
POST https://{endpoint}/v2/{project_id}/servers/{server_id}/metadata
POST https://{endpoint}/v2.1/{project_id}/servers/{server_id}/metadata
```

```
{
    "metadata": {
        "key": "value"
    }
}
```

## Example Response<a name="section111751241184111"></a>

```
{
    "metadata":{
        "key":"value"
    }
} 
```

## Returned Values<a name="section46706088185333"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

