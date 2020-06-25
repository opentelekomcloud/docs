# Adding a Tag to a Specified Stream<a name="dis_02_0415"></a>

## Function<a name="en-us_topic_0112442485_en-us_topic_0110707061_section1471126172111"></a>

This API is used to add a tag to a specified stream.

A stream has a maximum of 10 tags. This API is idempotent. If a tag to be created has the same key as an existing tag, the tag will overwrite the existing one.

## URI<a name="en-us_topic_0112442485_en-us_topic_0110707061_section315415176217"></a>

POST /v2/\{project\_id\}/stream/\{stream\_id\}/tags

The following table describes URI parameters.

**Table  1**  URI parameter description

<a name="en-us_topic_0112442485_en-us_topic_0110707061_table2882182815226"></a>
<table><thead align="left"><tr id="en-us_topic_0112442485_en-us_topic_0110707061_row12884528142211"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112442485_en-us_topic_0110707061_p7884228122214"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p7884228122214"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p7884228122214"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112442485_en-us_topic_0110707061_p388412816227"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p388412816227"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p388412816227"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112442485_en-us_topic_0110707061_p19884182820220"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p19884182820220"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p19884182820220"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112442485_en-us_topic_0110707061_row78841828112220"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p18884132810221"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p18884132810221"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p18884132810221"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p29494508194812"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p29494508194812"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p29494508194812"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p40820562194812"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p40820562194812"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p40820562194812"></a>Project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0112442485_en-us_topic_0110707061_row488402818223"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p288462815221"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p288462815221"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p288462815221"></a>stream_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p138841728132213"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p138841728132213"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p138841728132213"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p78845285227"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p78845285227"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p78845285227"></a>Stream ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0112442485_en-us_topic_0110707061_section158621312122315"></a>

**Request parameters**

**Table  2**  Request parameters

<a name="en-us_topic_0112442485_en-us_topic_0110707061_table1759719014243"></a>
<table><thead align="left"><tr id="en-us_topic_0112442485_en-us_topic_0110707061_row2597110112415"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112442485_en-us_topic_0110707061_p20597120152420"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p20597120152420"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p20597120152420"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112442485_en-us_topic_0110707061_p359718019240"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p359718019240"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p359718019240"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112442485_en-us_topic_0110707061_p35978012418"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p35978012418"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p35978012418"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112442485_en-us_topic_0110707061_p3597160132417"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p3597160132417"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p3597160132417"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112442485_en-us_topic_0110707061_row75973022419"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p105973017245"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p105973017245"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p105973017245"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p15982012410"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p15982012410"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p15982012410"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p1598110182416"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p1598110182416"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p1598110182416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p86921582248"><a name="p86921582248"></a><a name="p86921582248"></a>Key. </p>
<p id="en-us_topic_0112442485_en-us_topic_0110707061_p13598140102410"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p13598140102410"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p13598140102410"></a>A tag key consists of a maximum of 36 characters, including A-Z, a-z, 0-9, hyphens (-), and underscores (_).</p>
</td>
</tr>
<tr id="en-us_topic_0112442485_en-us_topic_0110707061_row145981052413"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p1559880132414"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p1559880132414"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p1559880132414"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p25981800247"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p25981800247"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p25981800247"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p125981607243"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p125981607243"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p125981607243"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="p1963212513257"><a name="p1963212513257"></a><a name="p1963212513257"></a>Value.</p>
<p id="en-us_topic_0112442485_en-us_topic_0110707061_p55984072416"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p55984072416"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p55984072416"></a>The value consists of a maximum of 43 characters, including A-Z, a-z, 0-9, periods (.), hyphens (-), and underscores (_), and can be an empty string.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0112442485_en-us_topic_0110707061_section1726123842419"></a>

**Response parameter**

None

## Example<a name="en-us_topic_0112442485_en-us_topic_0110707061_section7518458264"></a>

-   Request example

```
{ 
    "tag": 
        { 
            "key":"DEV", 
            "value":"DEV1" 
        } 
} 
```

-   Response example

    None


## Status Code<a name="en-us_topic_0112442485_en-us_topic_0110707061_section236812132267"></a>

[Table 3](#en-us_topic_0112442485_en-us_topic_0110707061_table5043525610328)  lists the status code of this API.

**Table  3**  Status code

<a name="en-us_topic_0112442485_en-us_topic_0110707061_table5043525610328"></a>
<table><thead align="left"><tr id="en-us_topic_0112442485_en-us_topic_0110707061_row1549446910328"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="en-us_topic_0112442485_en-us_topic_0110707061_p4709251510328"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p4709251510328"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p4709251510328"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="en-us_topic_0112442485_en-us_topic_0110707061_p5639738110328"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p5639738110328"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p5639738110328"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112442485_en-us_topic_0110707061_row478517210328"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p5205464710328"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p5205464710328"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p5205464710328"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p39771881331"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p39771881331"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p39771881331"></a>No Content</p>
</td>
</tr>
</tbody>
</table>

