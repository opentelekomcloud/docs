# Querying ECS Metadata<a name="EN-US_TOPIC_0065817713"></a>

## Function<a name="en-us_topic_0057973165_section15255933"></a>

This API is used to query ECS metadata.

## URI<a name="en-us_topic_0057973165_section3085673"></a>

GET /v2/\{project\_id\}/servers/\{server\_id\}/metadata

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/metadata

[Table 1](#en-us_topic_0057973165_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973165_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057973165_row44937496"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.549999999999997%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.47%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973165_row1664874"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973165_p637140"><a name="en-us_topic_0057973165_p637140"></a><a name="en-us_topic_0057973165_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973165_p51608407"><a name="en-us_topic_0057973165_p51608407"></a><a name="en-us_topic_0057973165_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.47%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973165_row41565035"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973165_p11324657"><a name="en-us_topic_0057973165_p11324657"></a><a name="en-us_topic_0057973165_p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973165_p44882061"><a name="en-us_topic_0057973165_p44882061"></a><a name="en-us_topic_0057973165_p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.47%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973165_p11568292"><a name="en-us_topic_0057973165_p11568292"></a><a name="en-us_topic_0057973165_p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Pagination query is not supported.  

## Request<a name="en-us_topic_0057973165_section34863789"></a>

None

## Response<a name="en-us_topic_0057973165_section45338652"></a>

[Table 2](#en-us_topic_0057973165_table48538422)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057973165_table48538422"></a>
<table><thead align="left"><tr id="en-us_topic_0057973165_row25630477"><th class="cellrowborder" valign="top" width="20.06%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057973165_p62802766"><a name="en-us_topic_0057973165_p62802766"></a><a name="en-us_topic_0057973165_p62802766"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.5.1.2"><p id="p1018311433156"><a name="p1018311433156"></a><a name="p1018311433156"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.719999999999999%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057973165_p53859287"><a name="en-us_topic_0057973165_p53859287"></a><a name="en-us_topic_0057973165_p53859287"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.870000000000005%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057973165_p42619108"><a name="en-us_topic_0057973165_p42619108"></a><a name="en-us_topic_0057973165_p42619108"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973165_row29595703"><td class="cellrowborder" valign="top" width="20.06%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973165_p48441714"><a name="en-us_topic_0057973165_p48441714"></a><a name="en-us_topic_0057973165_p48441714"></a>User-defined</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.5.1.2 "><p id="p91831743181514"><a name="p91831743181514"></a><a name="p91831743181514"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.719999999999999%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973165_p31464766"><a name="en-us_topic_0057973165_p31464766"></a><a name="en-us_topic_0057973165_p31464766"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.870000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973165_p13467047"><a name="en-us_topic_0057973165_p13467047"></a><a name="en-us_topic_0057973165_p13467047"></a>Specifies the metadata key-value pair.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973165_section5394690"></a>

```
GET https://{endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/servers/998af54b-5762-4041-abc1-f98a2c27b3a2/metadata
GET https://{endpoint}/v2.1/9c53a566cb3443ab910cf0daebca90c4/servers/998af54b-5762-4041-abc1-f98a2c27b3a2/metadata
```

## Example Response<a name="section12127142810430"></a>

```
{
    "metadata": {
        "wj": "True"
    }
}
```

## Returned Values<a name="en-us_topic_0057973165_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

