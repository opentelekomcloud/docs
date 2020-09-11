# Viewing Details of a DIS Stream<a name="dis_02_0025"></a>

## Function<a name="section57323557113017"></a>

This API is used to query details about a specified stream.

-   You need to specify the name of the stream to be queried.
-   You need to specify the partition from which the partition list is returned and the maximum number of partitions returned in a single request.

## URI<a name="section47160318113017"></a>

-   URI format

    GET /v2/\{project\_id\}/streams/\{stream\_name\}

-   Parameter description

    None


## Request<a name="section27598700113017"></a>

-   Example request

    ```
    GET https://{endpoint}/v2/{project_id}/streams/stream_test?start_partitionId=shardId-0000000000&limit_partitions=100
    ```

-   Parameter description

    **Table  1**  Parameter description

    <a name="table36088163113017"></a>
    <table><thead align="left"><tr id="row37049485113017"><th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.1"><p id="p48218333113017"><a name="p48218333113017"></a><a name="p48218333113017"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.308469153084694%" id="mcps1.2.5.1.2"><p id="p13370918113017"><a name="p13370918113017"></a><a name="p13370918113017"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p9302543113017"><a name="p9302543113017"></a><a name="p9302543113017"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.93530646935306%" id="mcps1.2.5.1.4"><p id="p15308480113017"><a name="p15308480113017"></a><a name="p15308480113017"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row32027362113017"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p44079516113017"><a name="p44079516113017"></a><a name="p44079516113017"></a>stream_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p13671063113017"><a name="p13671063113017"></a><a name="p13671063113017"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p33614331113017"><a name="p33614331113017"></a><a name="p33614331113017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p38406254113017"><a name="p38406254113017"></a><a name="p38406254113017"></a>Name of the DIS stream to be queried.</p>
    </td>
    </tr>
    <tr id="row10111974113017"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p13763574113017"><a name="p13763574113017"></a><a name="p13763574113017"></a>start_partitionId</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p41107690113017"><a name="p41107690113017"></a><a name="p41107690113017"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p41388587113017"><a name="p41388587113017"></a><a name="p41388587113017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p64141216113017"><a name="p64141216113017"></a><a name="p64141216113017"></a>ID of the partition to start the partition list with. The returned partition list does not contain this partition ID.</p>
    </td>
    </tr>
    <tr id="row40400033113017"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p51177280113017"><a name="p51177280113017"></a><a name="p51177280113017"></a>limit_partitions</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p51719048113017"><a name="p51719048113017"></a><a name="p51719048113017"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p28493344113017"><a name="p28493344113017"></a><a name="p28493344113017"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p5303700612318"><a name="p5303700612318"></a><a name="p5303700612318"></a>Maximum number of partitions to list in a single API call.</p>
    <p id="p57564350123115"><a name="p57564350123115"></a><a name="p57564350123115"></a>Value range: 1–1000</p>
    <p id="p42742397123138"><a name="p42742397123138"></a><a name="p42742397123138"></a>Default value: 100</p>
    </td>
    </tr>
    </tbody>
    </table>


## Response<a name="section35008949113017"></a>

-   Example response

    ```
    {
      "stream_name": "stream_test",
      "stream_id": "U7v0U582F8ccXyErJKC",
      "create_time": 1504679587519,
      "last_modified_time": 1504679587519,
      "retention_period": 24,
      "status": "RUNNING",
      "stream_type": "COMMON",
      "data_type": "JSON",
      "writable_partition_count": 3,
      "readable_partition_count": 5,
      "partitions": [
        {
         "status": "ACTIVE",
         "partition_id": "shardId-0000000000",
          "hash_range": "[0 : 9223372036854775807]",
           "sequence_number_range": "[0 : 200]"
        }
     ],
     "data_schema":{
    	"type": "record",
    	"name": "RecordName",
    	"fields": [{
    		"name": "id",
    		"type": "string",
    		"doc": "Type inferred from '\"1\"'"
                    }, {
    		"name": "detail",
    		"type": {
    			"type": "record",
    			"name": "detail",
    			"fields": [{
    				"name": "detID",
    				"type": "string",
    				"doc": "Type inferred from '\"05790110000000000103\"'"
    			}, {
    				"name": "endTime",
    				"type": "string",
    				"doc": "Type inferred from '\"2018/10/07 13:26:35\"'"
    			}]
    		},
    		"doc": "Type inferred from '{\"detID\":\"05790110000000000103\",\"endTime\":\"2018/10/07 13:26:35\"}'"
    	}]
       },
      "has_more_partitions": false,
       "tags": []
    }
    ```

-   Parameter description

    **Table  2**  Response parameter description

    <a name="table24638553113017"></a>
    <table><thead align="left"><tr id="row58127106113017"><th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.1"><p id="p10675170113017"><a name="p10675170113017"></a><a name="p10675170113017"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.2"><p id="p59382459113017"><a name="p59382459113017"></a><a name="p59382459113017"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.599999999999994%" id="mcps1.2.4.1.3"><p id="p45249844113017"><a name="p45249844113017"></a><a name="p45249844113017"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41358709113017"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p61721127113017"><a name="p61721127113017"></a><a name="p61721127113017"></a>stream_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p33355377113017"><a name="p33355377113017"></a><a name="p33355377113017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p17431036113017"><a name="p17431036113017"></a><a name="p17431036113017"></a>Name of the DIS stream.</p>
    </td>
    </tr>
    <tr id="row55300209111415"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p50131978111415"><a name="p50131978111415"></a><a name="p50131978111415"></a>stream_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p34158423111415"><a name="p34158423111415"></a><a name="p34158423111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p15368897111415"><a name="p15368897111415"></a><a name="p15368897111415"></a>Unique ID of each stream.</p>
    </td>
    </tr>
    <tr id="row22661601113017"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p23650416113017"><a name="p23650416113017"></a><a name="p23650416113017"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p36635539113017"><a name="p36635539113017"></a><a name="p36635539113017"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p14688691113017"><a name="p14688691113017"></a><a name="p14688691113017"></a>Timestamp at which the DIS stream was created.</p>
    </td>
    </tr>
    <tr id="row65089357113017"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p37746546113017"><a name="p37746546113017"></a><a name="p37746546113017"></a>last_modified_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p37571400113017"><a name="p37571400113017"></a><a name="p37571400113017"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p23384566113017"><a name="p23384566113017"></a><a name="p23384566113017"></a>Timestamp at which the DIS stream was most recently modified.</p>
    </td>
    </tr>
    <tr id="row9134510113017"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p1697877113017"><a name="p1697877113017"></a><a name="p1697877113017"></a>retention_period</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p3310311113017"><a name="p3310311113017"></a><a name="p3310311113017"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p66808654113017"><a name="p66808654113017"></a><a name="p66808654113017"></a>Period for storing data in units of hours.</p>
    </td>
    </tr>
    <tr id="row64406981113017"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p49582982113017"><a name="p49582982113017"></a><a name="p49582982113017"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p56798607113017"><a name="p56798607113017"></a><a name="p56798607113017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p37284489113017"><a name="p37284489113017"></a><a name="p37284489113017"></a>The stream status is one of the following:</p>
    <a name="ul16088113017"></a><a name="ul16088113017"></a><ul id="ul16088113017"><li>CREATING</li><li>RUNNING</li><li>TERMINATING</li><li>TERMINATED</li></ul>
    </td>
    </tr>
    <tr id="row2759165911561"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p2033194311561"><a name="p2033194311561"></a><a name="p2033194311561"></a>stream_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p3627465411561"><a name="p3627465411561"></a><a name="p3627465411561"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p5256588211561"><a name="p5256588211561"></a><a name="p5256588211561"></a>Partition type.</p>
    </td>
    </tr>
    <tr id="row1246175210420"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p375811364316"><a name="p375811364316"></a><a name="p375811364316"></a>data_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p975871364317"><a name="p975871364317"></a><a name="p975871364317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p147581313194310"><a name="p147581313194310"></a><a name="p147581313194310"></a>Type of the source data.</p>
    </td>
    </tr>
    <tr id="row5112153311720"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p192255731718"><a name="p192255731718"></a><a name="p192255731718"></a>data_schema</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p3244164616172"><a name="p3244164616172"></a><a name="p3244164616172"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p740411183810"><a name="p740411183810"></a><a name="p740411183810"></a>Source data structure that defines JSON and CSV formats. It is described in the syntax of the Avro schema. For details about Avro, see <a href="http://avro.apache.org/docs/current/#schemas" target="_blank" rel="noopener noreferrer">http://avro.apache.org/docs/current/#schemas</a>.</p>
    </td>
    </tr>
    <tr id="row19180195794217"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p475851314438"><a name="p475851314438"></a><a name="p475851314438"></a>writable_partition_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p1975811317435"><a name="p1975811317435"></a><a name="p1975811317435"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p8758131311432"><a name="p8758131311432"></a><a name="p8758131311432"></a>Total number of writable partitions (including partitions in ACTIVE state only).</p>
    </td>
    </tr>
    <tr id="row1278920547422"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p0758101314310"><a name="p0758101314310"></a><a name="p0758101314310"></a>readable_partition_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p675841317432"><a name="p675841317432"></a><a name="p675841317432"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p1758131315431"><a name="p1758131315431"></a><a name="p1758131315431"></a>Total number of readable partitions (including partitions in ACTIVE and DELETED state).</p>
    </td>
    </tr>
    <tr id="row214681611351"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p15240193115359"><a name="p15240193115359"></a><a name="p15240193115359"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p152401031143519"><a name="p152401031143519"></a><a name="p152401031143519"></a>List&lt;Tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p924011318358"><a name="p924011318358"></a><a name="p924011318358"></a>Label of the stream.</p>
    </td>
    </tr>
    <tr id="row38447592113017"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p27247230113017"><a name="p27247230113017"></a><a name="p27247230113017"></a>partitions</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p59542058113017"><a name="p59542058113017"></a><a name="p59542058113017"></a>List&lt;PartitionResult&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p58177361113017"><a name="p58177361113017"></a><a name="p58177361113017"></a>A list of partitions that comprise the DIS stream. For more information, see <a href="#table10248152113017">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row53834207113017"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p65603533113017"><a name="p65603533113017"></a><a name="p65603533113017"></a>has_more_partitions</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.2 "><p id="p12285931113017"><a name="p12285931113017"></a><a name="p12285931113017"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.599999999999994%" headers="mcps1.2.4.1.3 "><p id="p55636321113017"><a name="p55636321113017"></a><a name="p55636321113017"></a>Specify whether there are more matching partitions of the DIS stream to list.</p>
    <a name="ul28735404161846"></a><a name="ul28735404161846"></a><ul id="ul28735404161846"><li><strong id="b1672871235516"><a name="b1672871235516"></a><a name="b1672871235516"></a>true</strong>: There are more partitions.</li><li><strong id="b69731233185519"><a name="b69731233185519"></a><a name="b69731233185519"></a>false</strong>: There are no more partitions.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **partitions**  parameter description

    <a name="table10248152113017"></a>
    <table><thead align="left"><tr id="row12499921113017"><th class="cellrowborder" valign="top" width="26.26%" id="mcps1.2.4.1.1"><p id="p5860641113017"><a name="p5860641113017"></a><a name="p5860641113017"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.15%" id="mcps1.2.4.1.2"><p id="p4949885113017"><a name="p4949885113017"></a><a name="p4949885113017"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.2.4.1.3"><p id="p65396430113017"><a name="p65396430113017"></a><a name="p65396430113017"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62619516113017"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.4.1.1 "><p id="p39016046113017"><a name="p39016046113017"></a><a name="p39016046113017"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.4.1.2 "><p id="p6183181113017"><a name="p6183181113017"></a><a name="p6183181113017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p31075648113017"><a name="p31075648113017"></a><a name="p31075648113017"></a>Current status of each partition.</p>
    <a name="ul11245381113017"></a><a name="ul11245381113017"></a><ul id="ul11245381113017"><li>CREATING</li><li>ACTIVE</li><li>DELETED</li><li>EXPIRED</li></ul>
    </td>
    </tr>
    <tr id="row53423589113017"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.4.1.1 "><p id="p32343418113017"><a name="p32343418113017"></a><a name="p32343418113017"></a>partition_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.4.1.2 "><p id="p2571179113017"><a name="p2571179113017"></a><a name="p2571179113017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p6938978113017"><a name="p6938978113017"></a><a name="p6938978113017"></a>Unique identifier of the partition.</p>
    </td>
    </tr>
    <tr id="row62450802113017"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.4.1.1 "><p id="p25350186113017"><a name="p25350186113017"></a><a name="p25350186113017"></a>hash_range</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.4.1.2 "><p id="p40099162113017"><a name="p40099162113017"></a><a name="p40099162113017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p26806699113017"><a name="p26806699113017"></a><a name="p26806699113017"></a>Possible value range of the hash key used by each partition.</p>
    </td>
    </tr>
    <tr id="row41814228113017"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.4.1.1 "><p id="p31509279113017"><a name="p31509279113017"></a><a name="p31509279113017"></a>sequence_number_range</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.4.1.2 "><p id="p2114811113017"><a name="p2114811113017"></a><a name="p2114811113017"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="p37081999113017"><a name="p37081999113017"></a><a name="p37081999113017"></a>Sequence number range of each partition.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **tags**  parameter description

    <a name="table18918185943518"></a>
    <table><thead align="left"><tr id="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_row2597110112415"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p20597120152420"><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p20597120152420"></a><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p20597120152420"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p359718019240"><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p359718019240"></a><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p359718019240"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p35978012418"><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p35978012418"></a><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p35978012418"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.99999999999999%" id="mcps1.2.5.1.4"><p id="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p3597160132417"><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p3597160132417"></a><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p3597160132417"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_row75973022419"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p105973017245"><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p105973017245"></a><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p105973017245"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p15982012410"><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p15982012410"></a><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p15982012410"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p1598110182416"><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p1598110182416"></a><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p1598110182416"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p13598140102410"><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p13598140102410"></a><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p13598140102410"></a>Key. A tag key cannot contain special characters such as =*&lt;&gt;\,|/ or start or end with a space.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_row145981052413"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p1559880132414"><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p1559880132414"></a><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p1559880132414"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p25981800247"><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p25981800247"></a><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p25981800247"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p125981607243"><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p125981607243"></a><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p125981607243"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p55984072416"><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p55984072416"></a><a name="en-us_topic_0111418644_en-us_topic_0112442485_en-us_topic_0110707061_p55984072416"></a>Value. A tag value cannot contain special characters such as =*&lt;&gt;\,|/ or start or end with a space.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Status Code<a name="section65302542113017"></a>

-   Normal

    200 OK

-   Failed

    For more information, see  [Error Codes](error-codes.md).


