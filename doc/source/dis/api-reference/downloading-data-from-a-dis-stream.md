# Downloading Data from a DIS Stream<a name="dis_02_0019"></a>

## Function<a name="section43216271"></a>

This API is used to download data from a DIS stream.

When downloading data, you need to specify a data cursor. For details about how to obtain a cursor, see  [Obtaining a Cursor](obtaining-a-cursor.md).

## URI<a name="section53402119"></a>

-   URI format

    GET /v2/\{project\_id\}/records?\{partition-cursor\}

-   Parameter description

    None


## Request<a name="section10857028"></a>

-   Example request

    ```
    GET https://{endpoint}/v2/{project_id}/records?partition-cursor= eyJpdGVyR2VuVGltZSI6MTQ5MDk0ODk5OTM5NywiU3RyZWFtTmFtZSI6IjY2MCIsIlNoYXJkSWQiOiIwIiwiU2hhcmRJdGVyYXRvclR5cGUiOiJBVF9TRVFVRU5DRV9OVU1CRVIiLCJTdGFydGluZ1NlcXVlbmNlTnVtYmVyIjoiMCIsIlRpbWVTdGFtcCI6MH0=
    ```

-   Parameter description

    **Table  1**  Parameter description

    <a name="table22312206"></a>
    <table><thead align="left"><tr id="row16654654"><th class="cellrowborder" valign="top" width="27.552755275527556%" id="mcps1.2.5.1.1"><p id="p6849756"><a name="p6849756"></a><a name="p6849756"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.241224122412241%" id="mcps1.2.5.1.2"><p id="p17959338"><a name="p17959338"></a><a name="p17959338"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.241224122412241%" id="mcps1.2.5.1.3"><p id="p45420240"><a name="p45420240"></a><a name="p45420240"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.964796479647966%" id="mcps1.2.5.1.4"><p id="p55160823"><a name="p55160823"></a><a name="p55160823"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row38841670"><td class="cellrowborder" valign="top" width="27.552755275527556%" headers="mcps1.2.5.1.1 "><p id="p13070301114249"><a name="p13070301114249"></a><a name="p13070301114249"></a>partition-cursor</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.241224122412241%" headers="mcps1.2.5.1.2 "><p id="p27845503"><a name="p27845503"></a><a name="p27845503"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.241224122412241%" headers="mcps1.2.5.1.3 "><p id="p40893240"><a name="p40893240"></a><a name="p40893240"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.964796479647966%" headers="mcps1.2.5.1.4 "><p id="p24018105"><a name="p24018105"></a><a name="p24018105"></a>Cursor of the partition used to specify the position in the partition from which to start reading data records sequentially.</p>
    <p id="p19400719161322"><a name="p19400719161322"></a><a name="p19400719161322"></a>Value: 1 to 512 characters</p>
    <div class="note" id="note167967165130"><a name="note167967165130"></a><a name="note167967165130"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a3aeefbda996f4cc48beb82a8889aa907"><a name="a3aeefbda996f4cc48beb82a8889aa907"></a><a name="a3aeefbda996f4cc48beb82a8889aa907"></a>The validity period of a cursor is 5 minutes.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


## Response<a name="section30604389"></a>

-   Example response

    ```
    {
      "records": [
        {
          "partition_key": "0",
          "sequence_number": "21",
           "data": "MTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTEx",
          "timestamp": 1527577402541, 
          "timestamp_type": "CreateTime"
        }
      ],
      "next_partition_cursor":   "eyJpdGVyR2VuVGltZSI6MTQ5MDk1MDE1Nzc0NywiU3RyZWFtTmFtZSI6IjY2MCIsIlNoYXJkSWQiOiIwIiwiU2hhcmRJdGVyYXRvclR5cGUiOiJBVF9TRVFVRU5DRV9OVU1CRVIiLCJTdGFydGluZ1NlcXVlbmNlTnVtYmVyIjoiMjIiLCJUaW1lU3RhbXAiOjB9",
     }
    ```

-   Parameter description

    **Table  2**  Response parameter description

    <a name="table40372317"></a>
    <table><thead align="left"><tr id="row25717600"><th class="cellrowborder" valign="top" width="22.45%" id="mcps1.2.4.1.1"><p id="p2750866"><a name="p2750866"></a><a name="p2750866"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.37%" id="mcps1.2.4.1.2"><p id="p21493617"><a name="p21493617"></a><a name="p21493617"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.18%" id="mcps1.2.4.1.3"><p id="p63261412"><a name="p63261412"></a><a name="p63261412"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23900756"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p56913064"><a name="p56913064"></a><a name="p56913064"></a>records</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p46555465"><a name="p46555465"></a><a name="p46555465"></a>List&lt;PullRecord&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.18%" headers="mcps1.2.4.1.3 "><p id="p12896286"><a name="p12896286"></a><a name="p12896286"></a>Information of data records.</p>
    <p id="p48957711"><a name="p48957711"></a><a name="p48957711"></a>For more information, see <a href="#table9600654145646">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row6151694"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p7336512114338"><a name="p7336512114338"></a><a name="p7336512114338"></a>next_partition_cursor</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p28842926"><a name="p28842926"></a><a name="p28842926"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.18%" headers="mcps1.2.4.1.3 "><p id="p54575646"><a name="p54575646"></a><a name="p54575646"></a>Next cursor, which specifies the next position in the partition from which to start reading data records sequentially.</p>
    <div class="note" id="note15044838165524"><a name="note15044838165524"></a><a name="note15044838165524"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0058207017_p18782458164321"><a name="en-us_topic_0058207017_p18782458164321"></a><a name="en-us_topic_0058207017_p18782458164321"></a>The validity period of a cursor is 5 minutes.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **PullRecord**  parameter description

    <a name="table9600654145646"></a>
    <table><thead align="left"><tr id="row44539515"><th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.1"><p id="p50930930"><a name="p50930930"></a><a name="p50930930"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.310000000000002%" id="mcps1.2.4.1.2"><p id="p31764686"><a name="p31764686"></a><a name="p31764686"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.160000000000004%" id="mcps1.2.4.1.3"><p id="p22802807"><a name="p22802807"></a><a name="p22802807"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35088084"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p23562574"><a name="p23562574"></a><a name="p23562574"></a>data</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.2.4.1.2 "><p id="p29520332"><a name="p29520332"></a><a name="p29520332"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p42336695"><a name="p42336695"></a><a name="p42336695"></a>Data pulled from the DIS stream.</p>
    </td>
    </tr>
    <tr id="row45485936"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p41870578114447"><a name="p41870578114447"></a><a name="p41870578114447"></a>partition_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.2.4.1.2 "><p id="p112514"><a name="p112514"></a><a name="p112514"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p9113635"><a name="p9113635"></a><a name="p9113635"></a>Partition key set when data is being uploaded.</p>
    <div class="note" id="note2541622142514"><a name="note2541622142514"></a><a name="note2541622142514"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p15432252513"><a name="p15432252513"></a><a name="p15432252513"></a>If the <strong id="b107186491323"><a name="b107186491323"></a><a name="b107186491323"></a>partition_key</strong> parameter is transferred when data is uploaded, this parameter is returned when data is downloaded. If the <strong id="b14728024631"><a name="b14728024631"></a><a name="b14728024631"></a>partition_key</strong> parameter is not transferred but the <strong id="b181373314"><a name="b181373314"></a><a name="b181373314"></a>partition_id</strong> parameter is transferred when data is uploaded, no partition_key is returned.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row14913854"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p39768478114520"><a name="p39768478114520"></a><a name="p39768478114520"></a>sequence_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.2.4.1.2 "><p id="p5077725"><a name="p5077725"></a><a name="p5077725"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p54107956"><a name="p54107956"></a><a name="p54107956"></a><span id="text18338445144725"><a name="text18338445144725"></a><a name="text18338445144725"></a>Sequence number of an individual data record. Each data record has a sequence number that is unique within its partition. The sequence number is assigned by DIS when a data producer calls PutRecords to add data to a DIS stream. Sequence numbers for the same partition key generally increase over time; the longer the time period between write requests (PutRecords requests), the larger the sequence numbers become.</span></p>
    </td>
    </tr>
    <tr id="row1864513458019"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p3923107264"><a name="p3923107264"></a><a name="p3923107264"></a>timestamp</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.2.4.1.2 "><p id="p792427661"><a name="p792427661"></a><a name="p792427661"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p1292467863"><a name="p1292467863"></a><a name="p1292467863"></a>Timestamp when the record is written to DIS.</p>
    </td>
    </tr>
    <tr id="row765215511902"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p446212121464"><a name="p446212121464"></a><a name="p446212121464"></a>timestamp_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.2.4.1.2 "><p id="p54629128612"><a name="p54629128612"></a><a name="p54629128612"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p846210126610"><a name="p846210126610"></a><a name="p846210126610"></a>Type of the timestamp.</p>
    <p id="p365191221416"><a name="p365191221416"></a><a name="p365191221416"></a>The value is <strong id="b3121125310132"><a name="b3121125310132"></a><a name="b3121125310132"></a>CreateTime</strong>, specifying the creation time.</p>
    </td>
    </tr>
    </tbody>
    </table>


>![](/images/icon-note.gif) **NOTE:**   
>-   The data obtained through this API is the data encoded from the raw data using Base64 encoding.  
>-   If a user downloads data using SDK provided by DIS, the SDK will automatically decode the data using Base64 decoding, and the user will obtain the raw data.  

## Status Code<a name="section65302542113017"></a>

-   Normal

    200 OK

-   Failed

    For more information, see  [Error Codes](error-codes.md).


