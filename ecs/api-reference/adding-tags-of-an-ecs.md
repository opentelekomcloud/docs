# Adding Tags of an ECS<a name="EN-US_TOPIC_0065820823"></a>

This API is used to add tags to an ECS.

You are required to use the HTTP header  **X-OpenStack-Nova-API-Version: 2.26**  to specify the microversion on the client.

## URI<a name="en-us_topic_0057972838_section58912114"></a>

PUT /v2.1/\{project\_id\}/servers/\{server\_id\}/tags

[Table 1](#en-us_topic_0057972838_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972838_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057972838_row44937496"><th class="cellrowborder" valign="top" width="16.79%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.73%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.48%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972838_row1664874"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972838_p637140"><a name="en-us_topic_0057972838_p637140"></a><a name="en-us_topic_0057972838_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972838_p51608407"><a name="en-us_topic_0057972838_p51608407"></a><a name="en-us_topic_0057972838_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.48%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972838_row41565035"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972838_p11324657"><a name="en-us_topic_0057972838_p11324657"></a><a name="en-us_topic_0057972838_p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972838_p44882061"><a name="en-us_topic_0057972838_p44882061"></a><a name="en-us_topic_0057972838_p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.48%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972838_p11568292"><a name="en-us_topic_0057972838_p11568292"></a><a name="en-us_topic_0057972838_p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972838_section60446980"></a>

[Table 2](#en-us_topic_0057972838_table28387752)  describes the request parameters.

**Table  2**  Request parameters

<a name="en-us_topic_0057972838_table28387752"></a>
<table><thead align="left"><tr id="en-us_topic_0057972838_row66802302"><th class="cellrowborder" valign="top" width="16.79%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057972838_p42277343"><a name="en-us_topic_0057972838_p42277343"></a><a name="en-us_topic_0057972838_p42277343"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.75%" id="mcps1.2.5.1.2"><p id="p1045515223348"><a name="p1045515223348"></a><a name="p1045515223348"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.44%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057972838_p1912753"><a name="en-us_topic_0057972838_p1912753"></a><a name="en-us_topic_0057972838_p1912753"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.019999999999996%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057972838_p217030"><a name="en-us_topic_0057972838_p217030"></a><a name="en-us_topic_0057972838_p217030"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972838_row17579482"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972838_p14651901"><a name="en-us_topic_0057972838_p14651901"></a><a name="en-us_topic_0057972838_p14651901"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="17.75%" headers="mcps1.2.5.1.2 "><p id="p54556226341"><a name="p54556226341"></a><a name="p54556226341"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.44%" headers="mcps1.2.5.1.3 "><p id="p136741937121318"><a name="p136741937121318"></a><a name="p136741937121318"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="52.019999999999996%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972838_p47045852"><a name="en-us_topic_0057972838_p47045852"></a><a name="en-us_topic_0057972838_p47045852"></a>Specifies ECS tags.</p>
<p id="p61431611133610"><a name="p61431611133610"></a><a name="p61431611133610"></a>A maximum of 50 tags can be configured, and each tag can contain up to 80 characters.</p>
<p id="p1036152112366"><a name="p1036152112366"></a><a name="p1036152112366"></a>Can only consist of digits, letters, hyphens (-), and underscores (_).</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section10456114218587"></a>

**Table  3**  Response parameters

<a name="table1481741123815"></a>
<table><thead align="left"><tr id="row1818614389"><th class="cellrowborder" valign="top" width="16.6%" id="mcps1.2.5.1.1"><p id="p281816120382"><a name="p281816120382"></a><a name="p281816120382"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.12%" id="mcps1.2.5.1.2"><p id="p108181610386"><a name="p108181610386"></a><a name="p108181610386"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.26%" id="mcps1.2.5.1.3"><p id="p4818161113816"><a name="p4818161113816"></a><a name="p4818161113816"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.019999999999996%" id="mcps1.2.5.1.4"><p id="p1281812119386"><a name="p1281812119386"></a><a name="p1281812119386"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row08181516386"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.5.1.1 "><p id="p181818163815"><a name="p181818163815"></a><a name="p181818163815"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="18.12%" headers="mcps1.2.5.1.2 "><p id="p1818171133818"><a name="p1818171133818"></a><a name="p1818171133818"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.26%" headers="mcps1.2.5.1.3 "><p id="p28181710388"><a name="p28181710388"></a><a name="p28181710388"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="52.019999999999996%" headers="mcps1.2.5.1.4 "><p id="p198186118384"><a name="p198186118384"></a><a name="p198186118384"></a>Specifies ECS tags.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Reserved tag parameters

<a name="table5668174110389"></a>
<table><thead align="left"><tr id="row96682418384"><th class="cellrowborder" valign="top" width="23.810000000000002%" id="mcps1.2.3.1.1"><p id="p13668541113820"><a name="p13668541113820"></a><a name="p13668541113820"></a>Tag Name</p>
</th>
<th class="cellrowborder" valign="top" width="76.19%" id="mcps1.2.3.1.2"><p id="p966844143815"><a name="p966844143815"></a><a name="p966844143815"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row66689417387"><td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.3.1.1 "><p id="p26695418384"><a name="p26695418384"></a><a name="p26695418384"></a>__type_baremetal</p>
</td>
<td class="cellrowborder" valign="top" width="76.19%" headers="mcps1.2.3.1.2 "><p id="p1566917415389"><a name="p1566917415389"></a><a name="p1566917415389"></a>Specifies that the server is a BMS.</p>
</td>
</tr>
<tr id="row7669541123815"><td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.3.1.1 "><p id="p466910416389"><a name="p466910416389"></a><a name="p466910416389"></a>__type_virtual</p>
</td>
<td class="cellrowborder" valign="top" width="76.19%" headers="mcps1.2.3.1.2 "><p id="p7669114113387"><a name="p7669114113387"></a><a name="p7669114113387"></a>Specifies that the server is an ECS.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section114961544142619"></a>

```
PUT https://{endpoint}/v2.1/{project_id}/servers/{server_id}/tags
```

```
{ 
   "tags": ["baz", "foo", "qux"]
}
```

## Example Response<a name="section1356113511582"></a>

```
{ 
   "tags": ["baz", "foo", "qux"]
}
```

## Returned Values<a name="en-us_topic_0057972838_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

