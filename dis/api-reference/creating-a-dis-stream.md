# Creating a DIS Stream<a name="dis_02_0016_01"></a>

## Function<a name="section65332931172946"></a>

This API is used to create a stream.

-   When creating a channel, you need to specify the stream type \(common or advanced\), number of partitions, and source data type.
-   A maximum of 10 advanced stream partitions and 50 common stream partitions can be created for a domain by default. You can submit a service ticket to increase the quota.

## URI<a name="section47522773172946"></a>

-   URI format

    POST /v2/\{project\_id\}/streams

-   Parameter description

    None


## Request<a name="section16390157172946"></a>

-   Example request
    -   Create a stream whose source data type is BLOB.

        ```
        POST https://{endpoint}/v2/{project_id}/streams                
        {  
        	"stream_name": "dis-DLpR",
        	"partition_count": 1,
        	"stream_type": "COMMON",
        	"data_type": "BLOB",
        	"data_duration": 24
        } 
        ```

    -   Create a stream whose source data type is JSON or CSV.

        ```
        POST https://{endpoint}/v2/{project_id}/streams       
        {  
        	"stream_name": "dis-DLpR",
        	"partition_count": 1,
        	"stream_type": "COMMON",
                "data_type": "JSON",
        	"data_duration": 24,
                "data_schema":"{\"type\":\"record\",\"name\":\"RecordName\",\"fields\":[{\"name\":\"id\",\"type\":\"string\",\"doc\":\"Type inferred from '\\\"2017/10/11 11:11:11\\\"'\"},{\"name\":\"info\",\"type\":{\"type\":\"array\",\"items\":{\"type\":\"record\",\"name\":\"info\",\"fields\":[{\"name\":\"date\",\"type\":\"string\",\"doc\":\"Type inferred from '\\\"2018/10/11 11:11:11\\\"'\"}]}},\"doc\":\"Type inferred from '[{\\\"date\\\":\\\"2018/10/11 11:11:11\\\"}]'\"}]}"}
        }
        ```


-   Parameter description

**Table  1**  Parameter description

<a name="table6914317172946"></a>
<table><thead align="left"><tr id="row64574973172946"><th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.2.5.1.1"><p id="p63190347172946"><a name="p63190347172946"></a><a name="p63190347172946"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.13%" id="mcps1.2.5.1.2"><p id="p18144457172946"><a name="p18144457172946"></a><a name="p18144457172946"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.14%" id="mcps1.2.5.1.3"><p id="p60414879172946"><a name="p60414879172946"></a><a name="p60414879172946"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.53%" id="mcps1.2.5.1.4"><p id="p61767030172946"><a name="p61767030172946"></a><a name="p61767030172946"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row37073525172946"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.5.1.1 "><p id="p40068043111945"><a name="p40068043111945"></a><a name="p40068043111945"></a>stream_name</p>
</td>
<td class="cellrowborder" valign="top" width="13.13%" headers="mcps1.2.5.1.2 "><p id="p36879630172946"><a name="p36879630172946"></a><a name="p36879630172946"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.5.1.3 "><p id="p34460023172946"><a name="p34460023172946"></a><a name="p34460023172946"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.53%" headers="mcps1.2.5.1.4 "><p id="p39798440172946"><a name="p39798440172946"></a><a name="p39798440172946"></a>Name of the DIS stream.</p>
<p id="p22641643172946"><a name="p22641643172946"></a><a name="p22641643172946"></a>Each DIS stream has a unique name. A stream name is 1 to 64 characters in length. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
</td>
</tr>
<tr id="row1307269102511"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.5.1.1 "><p id="p12179892102524"><a name="p12179892102524"></a><a name="p12179892102524"></a>stream_type</p>
</td>
<td class="cellrowborder" valign="top" width="13.13%" headers="mcps1.2.5.1.2 "><p id="p47047171102524"><a name="p47047171102524"></a><a name="p47047171102524"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.5.1.3 "><p id="p52724495102524"><a name="p52724495102524"></a><a name="p52724495102524"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.53%" headers="mcps1.2.5.1.4 "><p id="p42825663102524"><a name="p42825663102524"></a><a name="p42825663102524"></a>Stream type. Possible values:</p>
<a name="ul46326651102524"></a><a name="ul46326651102524"></a><ul id="ul46326651102524"><li><strong id="b163104310403"><a name="b163104310403"></a><a name="b163104310403"></a>Common</strong>: a common stream. The bandwidth is 1 MB/s.</li><li><strong id="b125394018439"><a name="b125394018439"></a><a name="b125394018439"></a>ADVANCED</strong>: an advanced stream. The bandwidth is 5 MB/s.</li></ul>
<p id="p50948623102524"><a name="p50948623102524"></a><a name="p50948623102524"></a>Default value: COMMON</p>
</td>
</tr>
<tr id="row2448202172946"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.5.1.1 "><p id="p4538411011203"><a name="p4538411011203"></a><a name="p4538411011203"></a>partition_count</p>
</td>
<td class="cellrowborder" valign="top" width="13.13%" headers="mcps1.2.5.1.2 "><p id="p23636991172946"><a name="p23636991172946"></a><a name="p23636991172946"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.5.1.3 "><p id="p35548131172946"><a name="p35548131172946"></a><a name="p35548131172946"></a>Int</p>
</td>
<td class="cellrowborder" valign="top" width="52.53%" headers="mcps1.2.5.1.4 "><p id="p60826326172946"><a name="p60826326172946"></a><a name="p60826326172946"></a>Quantity of the partitions into which data records in the newly created DIS stream will be distributed.</p>
<p id="p22032301194636"><a name="p22032301194636"></a><a name="p22032301194636"></a>Partitions are the base throughput unit of a DIS stream.</p>
<p id="p38960612102828"><a name="p38960612102828"></a><a name="p38960612102828"></a>The value range varies depending on the value of <strong id="b4348325911350"><a name="b4348325911350"></a><a name="b4348325911350"></a>stream_type</strong>.</p>
<a name="ul33980650104610"></a><a name="ul33980650104610"></a><ul id="ul33980650104610"><li>If <strong id="b179473989710643"><a name="b179473989710643"></a><a name="b179473989710643"></a>stream_type</strong> is not specified or set to <strong id="b202544670110643"><a name="b202544670110643"></a><a name="b202544670110643"></a>COMMON</strong>, the value of <strong id="b178088510810643"><a name="b178088510810643"></a><a name="b178088510810643"></a>partition_count</strong> is an integer from 1 to 50. If the tenant has created <span class="parmvalue" id="parmvalue1061416132615"><a name="parmvalue1061416132615"></a><a name="parmvalue1061416132615"></a><b>N</b></span> common partitions, the maximum value of <strong id="b173276612210639"><a name="b173276612210639"></a><a name="b173276612210639"></a>partition_count </strong>is <span class="parmvalue" id="parmvalue48711829102617"><a name="parmvalue48711829102617"></a><a name="parmvalue48711829102617"></a><b>50-N</b></span>.</li><li>If <strong id="b82980614910635"><a name="b82980614910635"></a><a name="b82980614910635"></a>stream_type</strong> is set to <strong id="b188426244310635"><a name="b188426244310635"></a><a name="b188426244310635"></a>ADVANCED</strong>, the value of <strong id="b90569017510635"><a name="b90569017510635"></a><a name="b90569017510635"></a>partition_count</strong> is an integer from 1 to 10. If the tenant has created <span class="parmvalue" id="parmvalue202487120273"><a name="parmvalue202487120273"></a><a name="parmvalue202487120273"></a><b>N</b></span> advanced partitions, the maximum value of <strong id="b159321414810626"><a name="b159321414810626"></a><a name="b159321414810626"></a>partition_count</strong> is <span class="parmvalue" id="parmvalue15884222162715"><a name="parmvalue15884222162715"></a><a name="parmvalue15884222162715"></a><b>10-N</b></span>. </li></ul>
</td>
</tr>
<tr id="row333095551285"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.5.1.1 "><p id="p1407596812815"><a name="p1407596812815"></a><a name="p1407596812815"></a>data_duration</p>
</td>
<td class="cellrowborder" valign="top" width="13.13%" headers="mcps1.2.5.1.2 "><p id="p6641159512815"><a name="p6641159512815"></a><a name="p6641159512815"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.5.1.3 "><p id="p1063011912815"><a name="p1063011912815"></a><a name="p1063011912815"></a>Int</p>
</td>
<td class="cellrowborder" valign="top" width="52.53%" headers="mcps1.2.5.1.4 "><p id="p5573330712815"><a name="p5573330712815"></a><a name="p5573330712815"></a>Period of time for which data is retained in the DIS stream.</p>
<p id="p497023212840"><a name="p497023212840"></a><a name="p497023212840"></a>Value range: 24 to 72</p>
<p id="p1748320012910"><a name="p1748320012910"></a><a name="p1748320012910"></a>Unit: hour</p>
<p id="p990727512916"><a name="p990727512916"></a><a name="p990727512916"></a>Default value: 24</p>
<p id="p872929817555"><a name="p872929817555"></a><a name="p872929817555"></a>If this parameter is left unspecified, the default value will be used.</p>
</td>
</tr>
<tr id="row102205721711"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.5.1.1 "><p id="p192255731718"><a name="p192255731718"></a><a name="p192255731718"></a>data_schema</p>
</td>
<td class="cellrowborder" valign="top" width="13.13%" headers="mcps1.2.5.1.2 "><p id="p1622185751715"><a name="p1622185751715"></a><a name="p1622185751715"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.5.1.3 "><p id="p112225718177"><a name="p112225718177"></a><a name="p112225718177"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.53%" headers="mcps1.2.5.1.4 "><p id="p740411183810"><a name="p740411183810"></a><a name="p740411183810"></a>Source data structure that defines JOSN and CSV formats. It is described in the syntax of Avro. For details about Avro, see <a href="http://avro.apache.org/docs/current/#schemas" target="_blank" rel="noopener noreferrer">http://avro.apache.org/docs/current/#schemas</a>.</p>
<div class="note" id="note2764222193813"><a name="note2764222193813"></a><a name="note2764222193813"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p187645225387"><a name="p187645225387"></a><a name="p187645225387"></a>This parameter is mandatory when <strong id="b13288174616447"><a name="b13288174616447"></a><a name="b13288174616447"></a>Dump File Format</strong> is <strong id="b81179499443"><a name="b81179499443"></a><a name="b81179499443"></a>Parquet</strong> or <strong id="b12679135116443"><a name="b12679135116443"></a><a name="b12679135116443"></a>CarbonData</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row16339173214299"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.5.1.1 "><p id="p7356153219294"><a name="p7356153219294"></a><a name="p7356153219294"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="13.13%" headers="mcps1.2.5.1.2 "><p id="p2356232112912"><a name="p2356232112912"></a><a name="p2356232112912"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.5.1.3 "><p id="p6356153262917"><a name="p6356153262917"></a><a name="p6356153262917"></a>List&lt;Tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="52.53%" headers="mcps1.2.5.1.4 "><p id="p5356123292916"><a name="p5356123292916"></a><a name="p5356123292916"></a>Label of the stream.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **Tag**  parameter description

<a name="table75941414193216"></a>
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
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p13598140102410"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p13598140102410"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p13598140102410"></a>Key. A tag key cannot contain special characters such as =*&lt;&gt;\,|/ or start or end with a space.</p>
</td>
</tr>
<tr id="en-us_topic_0112442485_en-us_topic_0110707061_row145981052413"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p1559880132414"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p1559880132414"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p1559880132414"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p25981800247"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p25981800247"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p25981800247"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p125981607243"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p125981607243"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p125981607243"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112442485_en-us_topic_0110707061_p55984072416"><a name="en-us_topic_0112442485_en-us_topic_0110707061_p55984072416"></a><a name="en-us_topic_0112442485_en-us_topic_0110707061_p55984072416"></a>Value. A tag value cannot contain special characters such as =*&lt;&gt;\,|/ or start or end with a space.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section6576977617376"></a>

-   If the DIS stream was successfully created, a 201 response with an empty response body is returned.
-   If the DIS stream failed to be created, identify the failure cause according to the response body and the instructions in  [Error Codes](error-codes.md).

## Status Code<a name="section2384767417376"></a>

-   Normal

    201 Created

-   Failed

    For more information, see  [Error Codes](error-codes.md).


