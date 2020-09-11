# Querying All Tags<a name="dis_02_0419"></a>

## Function<a name="en-us_topic_0112442489_en-us_topic_0110707085_section1471126172111"></a>

This API is used to query all tag sets of a specified region.

## URI<a name="en-us_topic_0112442489_en-us_topic_0110707085_section315415176217"></a>

GET /v2/\{project\_id\}/stream/tags

**Table  1**  URI parameter description

<a name="en-us_topic_0112442489_en-us_topic_0110707085_table2882182815226"></a>
<table><thead align="left"><tr id="en-us_topic_0112442489_en-us_topic_0110707085_row12884528142211"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112442489_en-us_topic_0110707085_p7884228122214"><a name="en-us_topic_0112442489_en-us_topic_0110707085_p7884228122214"></a><a name="en-us_topic_0112442489_en-us_topic_0110707085_p7884228122214"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112442489_en-us_topic_0110707085_p388412816227"><a name="en-us_topic_0112442489_en-us_topic_0110707085_p388412816227"></a><a name="en-us_topic_0112442489_en-us_topic_0110707085_p388412816227"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112442489_en-us_topic_0110707085_p19884182820220"><a name="en-us_topic_0112442489_en-us_topic_0110707085_p19884182820220"></a><a name="en-us_topic_0112442489_en-us_topic_0110707085_p19884182820220"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112442489_en-us_topic_0110707085_row78841828112220"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112442489_en-us_topic_0110707085_p18884132810221"><a name="en-us_topic_0112442489_en-us_topic_0110707085_p18884132810221"></a><a name="en-us_topic_0112442489_en-us_topic_0110707085_p18884132810221"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112442489_en-us_topic_0110707085_p29494508194812"><a name="en-us_topic_0112442489_en-us_topic_0110707085_p29494508194812"></a><a name="en-us_topic_0112442489_en-us_topic_0110707085_p29494508194812"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112442489_en-us_topic_0110707085_p40820562194812"><a name="en-us_topic_0112442489_en-us_topic_0110707085_p40820562194812"></a><a name="en-us_topic_0112442489_en-us_topic_0110707085_p40820562194812"></a>Project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0112442489_en-us_topic_0110707085_section158621312122315"></a>

**Request parameters**

None

## Response<a name="en-us_topic_0112442489_en-us_topic_0110707085_section1726123842419"></a>

**Response parameter**

The following table describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0112442489_table45211674182"></a>
<table><thead align="left"><tr id="dis_02_0417_en-us_topic_0112442487_row6447741616"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="dis_02_0417_en-us_topic_0112442487_p144437171619"><a name="dis_02_0417_en-us_topic_0112442487_p144437171619"></a><a name="dis_02_0417_en-us_topic_0112442487_p144437171619"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="dis_02_0417_en-us_topic_0112442487_p34517171618"><a name="dis_02_0417_en-us_topic_0112442487_p34517171618"></a><a name="dis_02_0417_en-us_topic_0112442487_p34517171618"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="dis_02_0417_en-us_topic_0112442487_p847075161"><a name="dis_02_0417_en-us_topic_0112442487_p847075161"></a><a name="dis_02_0417_en-us_topic_0112442487_p847075161"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="dis_02_0417_en-us_topic_0112442487_p1548378165"><a name="dis_02_0417_en-us_topic_0112442487_p1548378165"></a><a name="dis_02_0417_en-us_topic_0112442487_p1548378165"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="dis_02_0417_row1046244151010"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="dis_02_0417_p1462341151019"><a name="dis_02_0417_p1462341151019"></a><a name="dis_02_0417_p1462341151019"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="dis_02_0417_en-us_topic_0112442490_p7758165732819"><a name="dis_02_0417_en-us_topic_0112442490_p7758165732819"></a><a name="dis_02_0417_en-us_topic_0112442490_p7758165732819"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="dis_02_0417_en-us_topic_0112442490_p275835732812"><a name="dis_02_0417_en-us_topic_0112442490_p275835732812"></a><a name="dis_02_0417_en-us_topic_0112442490_p275835732812"></a>List&lt;tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="dis_02_0417_p184625412107"><a name="dis_02_0417_p184625412107"></a><a name="dis_02_0417_p184625412107"></a>Tag list.</p>
</td>
</tr>
<tr id="dis_02_0417_en-us_topic_0112442487_row124947121617"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="dis_02_0417_en-us_topic_0112442487_p18491073163"><a name="dis_02_0417_en-us_topic_0112442487_p18491073163"></a><a name="dis_02_0417_en-us_topic_0112442487_p18491073163"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="dis_02_0417_en-us_topic_0112442487_p54997171618"><a name="dis_02_0417_en-us_topic_0112442487_p54997171618"></a><a name="dis_02_0417_en-us_topic_0112442487_p54997171618"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="dis_02_0417_en-us_topic_0112442487_p0492712166"><a name="dis_02_0417_en-us_topic_0112442487_p0492712166"></a><a name="dis_02_0417_en-us_topic_0112442487_p0492712166"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="dis_02_0417_p1569712166264"><a name="dis_02_0417_p1569712166264"></a><a name="dis_02_0417_p1569712166264"></a>Key. </p>
<p id="dis_02_0417_en-us_topic_0112442487_p164907111612"><a name="dis_02_0417_en-us_topic_0112442487_p164907111612"></a><a name="dis_02_0417_en-us_topic_0112442487_p164907111612"></a>A tag key consists of a maximum of 36 characters, including A-Z, a-z, 0-9, hyphens (-), and underscores (_).</p>
</td>
</tr>
<tr id="dis_02_0417_en-us_topic_0112442487_row17501761611"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="dis_02_0417_en-us_topic_0112442487_p115087181618"><a name="dis_02_0417_en-us_topic_0112442487_p115087181618"></a><a name="dis_02_0417_en-us_topic_0112442487_p115087181618"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="dis_02_0417_en-us_topic_0112442487_p6506710168"><a name="dis_02_0417_en-us_topic_0112442487_p6506710168"></a><a name="dis_02_0417_en-us_topic_0112442487_p6506710168"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="dis_02_0417_en-us_topic_0112442487_p35027201610"><a name="dis_02_0417_en-us_topic_0112442487_p35027201610"></a><a name="dis_02_0417_en-us_topic_0112442487_p35027201610"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="dis_02_0417_p2528152382618"><a name="dis_02_0417_p2528152382618"></a><a name="dis_02_0417_p2528152382618"></a>Value.</p>
<p id="dis_02_0417_en-us_topic_0112442487_p35027151611"><a name="dis_02_0417_en-us_topic_0112442487_p35027151611"></a><a name="dis_02_0417_en-us_topic_0112442487_p35027151611"></a>The value consists of a maximum of 43 characters, including A-Z, a-z, 0-9, periods (.), hyphens (-), and underscores (_), and can be an empty string.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="en-us_topic_0112442489_en-us_topic_0110707085_section7518458264"></a>

-   Request example

None

-   Response example

```
{ 
    "tags": [ 
    { 
        "key": "key1", 
        "values": [ 
            "value1", 
            "value2" 
        ] 
        }, 
        { 
        "key": "key2", 
        "values": [ 
            "value1", 
            "value2" 
        ] 
        } 
    ] 
} 

```

## Status Code<a name="en-us_topic_0112442489_en-us_topic_0110707085_section236812132267"></a>

[Table 3](#en-us_topic_0112442489_en-us_topic_0110707085_table5043525610328)  lists the status code of this API.

**Table  3**  Status code

<a name="en-us_topic_0112442489_en-us_topic_0110707085_table5043525610328"></a>
<table><thead align="left"><tr id="en-us_topic_0112442489_en-us_topic_0110707085_row1549446910328"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="en-us_topic_0112442489_en-us_topic_0110707085_p4709251510328"><a name="en-us_topic_0112442489_en-us_topic_0110707085_p4709251510328"></a><a name="en-us_topic_0112442489_en-us_topic_0110707085_p4709251510328"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="en-us_topic_0112442489_en-us_topic_0110707085_p5639738110328"><a name="en-us_topic_0112442489_en-us_topic_0110707085_p5639738110328"></a><a name="en-us_topic_0112442489_en-us_topic_0110707085_p5639738110328"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112442489_en-us_topic_0110707085_row478517210328"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0112442489_en-us_topic_0110707085_p5205464710328"><a name="en-us_topic_0112442489_en-us_topic_0110707085_p5205464710328"></a><a name="en-us_topic_0112442489_en-us_topic_0110707085_p5205464710328"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0112442489_en-us_topic_0110707085_p39771881331"><a name="en-us_topic_0112442489_en-us_topic_0110707085_p39771881331"></a><a name="en-us_topic_0112442489_en-us_topic_0110707085_p39771881331"></a>OK</p>
</td>
</tr>
</tbody>
</table>

