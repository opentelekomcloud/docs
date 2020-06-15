# Configuring ECS Metadata<a name="EN-US_TOPIC_0077847902"></a>

## Function<a name="en-us_topic_0057973166_section2604713"></a>

This API is used to configure ECS metadata.

When you call this API, all the metadata of this ECS will be deleted, and the ECS uses the value configured in the request.

## Constraints<a name="en-us_topic_0057973166_section9655225"></a>

An ECS must be in active, stopped, paused, or suspended state, which is specified by  **OS-EXT-STS:vm\_state**.

## URI<a name="en-us_topic_0057973166_section23442424"></a>

PUT /v2/\{project\_id\}/servers/\{server\_id\}/metadata

PUT /v2.1/\{project\_id\}/servers/\{server\_id\}/metadata

[Table 1](#en-us_topic_0057973166_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973166_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057973166_row44937496"><th class="cellrowborder" valign="top" width="16.41164116411641%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.92179217921792%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.66656665666567%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973166_row1664874"><td class="cellrowborder" valign="top" width="16.41164116411641%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973166_p637140"><a name="en-us_topic_0057973166_p637140"></a><a name="en-us_topic_0057973166_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.92179217921792%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973166_p51608407"><a name="en-us_topic_0057973166_p51608407"></a><a name="en-us_topic_0057973166_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66656665666567%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973166_row41565035"><td class="cellrowborder" valign="top" width="16.41164116411641%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973166_p11324657"><a name="en-us_topic_0057973166_p11324657"></a><a name="en-us_topic_0057973166_p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.92179217921792%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973166_p44882061"><a name="en-us_topic_0057973166_p44882061"></a><a name="en-us_topic_0057973166_p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66656665666567%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973166_p11568292"><a name="en-us_topic_0057973166_p11568292"></a><a name="en-us_topic_0057973166_p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973166_section43875778"></a>

[Table 2](#en-us_topic_0057973166_table58874912)  describes the request parameters.

**Table  2**  Request

<a name="en-us_topic_0057973166_table58874912"></a>
<table><thead align="left"><tr id="en-us_topic_0057973166_row60391117"><th class="cellrowborder" valign="top" width="16.168383161683835%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057973166_p59842305"><a name="en-us_topic_0057973166_p59842305"></a><a name="en-us_topic_0057973166_p59842305"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.448655134486554%" id="mcps1.2.5.1.2"><p id="en-us_topic_0057973166_p15388566"><a name="en-us_topic_0057973166_p15388566"></a><a name="en-us_topic_0057973166_p15388566"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.418258174182583%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057973166_p38514356"><a name="en-us_topic_0057973166_p38514356"></a><a name="en-us_topic_0057973166_p38514356"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="52.964703529647025%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057973166_p32655106"><a name="en-us_topic_0057973166_p32655106"></a><a name="en-us_topic_0057973166_p32655106"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973166_row27817896"><td class="cellrowborder" valign="top" width="16.168383161683835%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973166_p38657103"><a name="en-us_topic_0057973166_p38657103"></a><a name="en-us_topic_0057973166_p38657103"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="13.448655134486554%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973166_p44217630"><a name="en-us_topic_0057973166_p44217630"></a><a name="en-us_topic_0057973166_p44217630"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="17.418258174182583%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973166_p24858302"><a name="en-us_topic_0057973166_p24858302"></a><a name="en-us_topic_0057973166_p24858302"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="52.964703529647025%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973166_p26317995185333"><a name="en-us_topic_0057973166_p26317995185333"></a><a name="en-us_topic_0057973166_p26317995185333"></a>Specifies the user-defined metadata key-value pair.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Data structure description of the  **metadata**  field

<a name="en-us_topic_0057973166_table59792218185333"></a>
<table><thead align="left"><tr id="en-us_topic_0057973166_row39910345185333"><th class="cellrowborder" valign="top" width="16.17%" id="mcps1.2.5.1.1"><p id="p18972171961811"><a name="p18972171961811"></a><a name="p18972171961811"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.530000000000001%" id="mcps1.2.5.1.2"><p id="p2972191901817"><a name="p2972191901817"></a><a name="p2972191901817"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.299999999999997%" id="mcps1.2.5.1.3"><p id="p1197281911187"><a name="p1197281911187"></a><a name="p1197281911187"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.2.5.1.4"><p id="p13972519121820"><a name="p13972519121820"></a><a name="p13972519121820"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973166_row15890112034514"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973166_p1089262011454"><a name="en-us_topic_0057973166_p1089262011454"></a><a name="en-us_topic_0057973166_p1089262011454"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973166_p18894122014512"><a name="en-us_topic_0057973166_p18894122014512"></a><a name="en-us_topic_0057973166_p18894122014512"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973166_p220493014454"><a name="en-us_topic_0057973166_p220493014454"></a><a name="en-us_topic_0057973166_p220493014454"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973166_p19894192011457"><a name="en-us_topic_0057973166_p19894192011457"></a><a name="en-us_topic_0057973166_p19894192011457"></a>Specifies the key name.</p>
<p id="en-us_topic_0057973166_p146113814453"><a name="en-us_topic_0057973166_p146113814453"></a><a name="en-us_topic_0057973166_p146113814453"></a>The value contains a maximum of 255 Unicode characters and cannot be empty. It can contain letters in upper or lower cases, digits, hyphens (-), underscores (_), colons (:), and periods (.).</p>
</td>
</tr>
<tr id="en-us_topic_0057973166_row17903267185333"><td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973166_p40878540185333"><a name="en-us_topic_0057973166_p40878540185333"></a><a name="en-us_topic_0057973166_p40878540185333"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973166_p22827413185333"><a name="en-us_topic_0057973166_p22827413185333"></a><a name="en-us_topic_0057973166_p22827413185333"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973166_p37081126185333"><a name="en-us_topic_0057973166_p37081126185333"></a><a name="en-us_topic_0057973166_p37081126185333"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973166_p999582373317"><a name="en-us_topic_0057973166_p999582373317"></a><a name="en-us_topic_0057973166_p999582373317"></a>Specifies the key value.</p>
<p id="en-us_topic_0057973166_p58906615396"><a name="en-us_topic_0057973166_p58906615396"></a><a name="en-us_topic_0057973166_p58906615396"></a>The value can contain a maximum of 255 Unicode characters.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0057973166_section59337683"></a>

[Table 4](#en-us_topic_0057973166_table52843024)  describes the response parameters.

**Table  4**  Response parameters

<a name="en-us_topic_0057973166_table52843024"></a>
<table><thead align="left"><tr id="en-us_topic_0057973166_row1967448"><th class="cellrowborder" valign="top" width="16.13%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057973166_p25145612"><a name="en-us_topic_0057973166_p25145612"></a><a name="en-us_topic_0057973166_p25145612"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.68%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057973166_p23528655"><a name="en-us_topic_0057973166_p23528655"></a><a name="en-us_topic_0057973166_p23528655"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="70.19%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057973166_p21124521"><a name="en-us_topic_0057973166_p21124521"></a><a name="en-us_topic_0057973166_p21124521"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973166_row33364622"><td class="cellrowborder" valign="top" width="16.13%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973166_p951875545516"><a name="en-us_topic_0057973166_p951875545516"></a><a name="en-us_topic_0057973166_p951875545516"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="13.68%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973166_p63283858"><a name="en-us_topic_0057973166_p63283858"></a><a name="en-us_topic_0057973166_p63283858"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="70.19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973166_p1434720105613"><a name="en-us_topic_0057973166_p1434720105613"></a><a name="en-us_topic_0057973166_p1434720105613"></a>Specifies the user-defined metadata key-value pair.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973166_section64277099"></a>

```
PUT https://{endpoint}/v2/{project_id}/servers/{server_id}/metadata
PUT https://{endpoint}/v2.1/{project_id}/servers/{server_id}/metadata
```

```
{
    "metadata": {
            "key1": "value1",
            "key2": "value2"
    }
}
```

## Example Response<a name="section22101537134219"></a>

```
{
    "metadata": {
            "key1": "value1",
            "key2": "value2"
    }
}
```

## Returned Values<a name="en-us_topic_0057973166_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

