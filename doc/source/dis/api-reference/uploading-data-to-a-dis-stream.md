# Uploading Data to a DIS Stream<a name="dis_02_0018"></a>

## Function<a name="section10750772"></a>

This API is used to upload data to a DIS stream.

-   Before uploading data, you need to create a stream by referring to  [Creating a DIS Stream](creating-a-dis-stream.md).
-   When uploading data, you need to specify the partition ID of the stream. The partition ID can be obtained from  [Viewing Details of a DIS Stream](viewing-details-of-a-dis-stream.md).

## URI<a name="section29648085"></a>

-   URI format

    POST /v2/\{project\_id\}/records

-   Parameter description

    None


## Request<a name="d0e1325"></a>

-   Example request

    ```
    POST https://{endpoint}/v2/{project_id}/records  
    
    {
     "stream_name": "stream_test",
      "records": [
        {
          "data":
    "MTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTE=",
          "explicit_hash_key": null,
          "partition_key": "0"
     ]
    }
    ```

-   Parameter description

    **Table  1**  Parameter description

    <a name="table11766267"></a>
    <table><thead align="left"><tr id="row54764719"><th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.1"><p id="p6757235"><a name="p6757235"></a><a name="p6757235"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.308469153084694%" id="mcps1.2.5.1.2"><p id="p10465156"><a name="p10465156"></a><a name="p10465156"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p42371273"><a name="p42371273"></a><a name="p42371273"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.93530646935306%" id="mcps1.2.5.1.4"><p id="p9521066"><a name="p9521066"></a><a name="p9521066"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33008913"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p24700768113116"><a name="p24700768113116"></a><a name="p24700768113116"></a>stream_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p11174282"><a name="p11174282"></a><a name="p11174282"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p32701678"><a name="p32701678"></a><a name="p32701678"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p31590262"><a name="p31590262"></a><a name="p31590262"></a>Name of the stream created on the management console.</p>
    <p id="p55276975145527"><a name="p55276975145527"></a><a name="p55276975145527"></a>A stream name is 1 to 64 characters long. Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
    </td>
    </tr>
    <tr id="row48661450105513"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p8867175065512"><a name="p8867175065512"></a><a name="p8867175065512"></a>stream_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p28671450155513"><a name="p28671450155513"></a><a name="p28671450155513"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p18867205017555"><a name="p18867205017555"></a><a name="p18867205017555"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p18674509558"><a name="p18674509558"></a><a name="p18674509558"></a>Unique ID of the stream.</p>
    <p id="p5732142911251"><a name="p5732142911251"></a><a name="p5732142911251"></a>If no stream is found based on stream_name and stream_id is not empty, stream_id is used to search for the stream.</p>
    <div class="note" id="note1462724818314"><a name="note1462724818314"></a><a name="note1462724818314"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1362824873113"><a name="p1362824873113"></a><a name="p1362824873113"></a>This parameter is mandatory when you upload data to a stream that has been authorized.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row15876907"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p10961125"><a name="p10961125"></a><a name="p10961125"></a>records</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p15435960"><a name="p15435960"></a><a name="p15435960"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p42353227"><a name="p42353227"></a><a name="p42353227"></a>List&lt;PutRecordsRequestEntry&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p8059334"><a name="p8059334"></a><a name="p8059334"></a>Information of data records.</p>
    <p id="p48826322"><a name="p48826322"></a><a name="p48826322"></a>For more information, see <a href="#table2811077317374">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **records**  parameter description

    <a name="table2811077317374"></a>
    <table><thead align="left"><tr id="row5020285"><th class="cellrowborder" valign="top" width="22.447755224477554%" id="mcps1.2.5.1.1"><p id="p3989940"><a name="p3989940"></a><a name="p3989940"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.308469153084694%" id="mcps1.2.5.1.2"><p id="p54749715"><a name="p54749715"></a><a name="p54749715"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.308469153084694%" id="mcps1.2.5.1.3"><p id="p5541955"><a name="p5541955"></a><a name="p5541955"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.93530646935306%" id="mcps1.2.5.1.4"><p id="p46245228"><a name="p46245228"></a><a name="p46245228"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54875957"><td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.1 "><p id="p15767494"><a name="p15767494"></a><a name="p15767494"></a>data</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p2098632"><a name="p2098632"></a><a name="p2098632"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="p35771490"><a name="p35771490"></a><a name="p35771490"></a>Base64-encoded binary data object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p43012933112354"><a name="p43012933112354"></a><a name="p43012933112354"></a>Data to be put into the chosen DIS stream.</p>
    <p id="p37054767112350"><a name="p37054767112350"></a><a name="p37054767112350"></a>The uploaded data must be serialized into binary Base64-encoded data.</p>
    </td>
    </tr>
    <tr id="row39177514"><td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.1 "><p id="p30630178113229"><a name="p30630178113229"></a><a name="p30630178113229"></a>explicit_hash_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p16725372"><a name="p16725372"></a><a name="p16725372"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="p12577900"><a name="p12577900"></a><a name="p12577900"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p12176960"><a name="p12176960"></a><a name="p12176960"></a>Hash value used to explicitly determine the partition into which an individual data record will be put. The hash value overrides the partition key hash.</p>
    <p id="p6519654125120"><a name="p6519654125120"></a><a name="p6519654125120"></a>Value range: 0 to long.max</p>
    </td>
    </tr>
    <tr id="row12367794162335"><td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.1 "><p id="p62267224162335"><a name="p62267224162335"></a><a name="p62267224162335"></a>partition_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p10480383162335"><a name="p10480383162335"></a><a name="p10480383162335"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="p43604686162335"><a name="p43604686162335"></a><a name="p43604686162335"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p4248540417243"><a name="p4248540417243"></a><a name="p4248540417243"></a>Unique identifier of the partition.</p>
    </td>
    </tr>
    <tr id="row42483779"><td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.1 "><p id="p10714600113254"><a name="p10714600113254"></a><a name="p10714600113254"></a>partition_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p32966247"><a name="p32966247"></a><a name="p32966247"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.3 "><p id="p53020390"><a name="p53020390"></a><a name="p53020390"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p66793230"><a name="p66793230"></a><a name="p66793230"></a>Partition key of the partition into which an individual data record will be put.</p>
    <div class="note" id="note64013584172539"><a name="note64013584172539"></a><a name="note64013584172539"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p4570972117262"><a name="p4570972117262"></a><a name="p4570972117262"></a>The <strong id="b4142386317281"><a name="b4142386317281"></a><a name="b4142386317281"></a>partition_id</strong> parameter takes precedence over the <strong id="b3727045317281"><a name="b3727045317281"></a><a name="b3727045317281"></a>partition_key</strong> parameter. If the <strong id="b515447700111950"><a name="b515447700111950"></a><a name="b515447700111950"></a>partition_id</strong> parameter is not passed in, then the <strong id="b2138982840111950"><a name="b2138982840111950"></a><a name="b2138982840111950"></a>partition_key</strong> parameter is selected for use.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


>![](/images/icon-note.gif) **NOTE:**   
>-   The user's raw data may contain invisible characters. Therefore, the raw data must be encoded using Base64 encoding before invoking the API.  
>-   If a user uploads data using SDK provided by DIS, the SDK will automatically encode the raw data using Base64 encoding.  

## Response<a name="section52684690"></a>

-   Example response

    ```
    {
       "failed_record_count": 0, 
       "records": [ 
          { 
    
    
             "sequence_number": "195",
             "partition_id": "shardId-0000000000"
          }
       ]
    }
    ```

-   Parameter description

    **Table  3**  Response parameter description

    <a name="table40372317"></a>
    <table><thead align="left"><tr id="row25717600"><th class="cellrowborder" valign="top" width="22.45%" id="mcps1.2.4.1.1"><p id="p2750866"><a name="p2750866"></a><a name="p2750866"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.37%" id="mcps1.2.4.1.2"><p id="p21493617"><a name="p21493617"></a><a name="p21493617"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.18%" id="mcps1.2.4.1.3"><p id="p63261412"><a name="p63261412"></a><a name="p63261412"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6151694"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p38789413113422"><a name="p38789413113422"></a><a name="p38789413113422"></a>failed_record_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p208141609576"><a name="p208141609576"></a><a name="p208141609576"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.18%" headers="mcps1.2.4.1.3 "><p id="p286286439576"><a name="p286286439576"></a><a name="p286286439576"></a>The number of data records that failed to be put into the selected DIS stream.</p>
    </td>
    </tr>
    <tr id="row4531290295651"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p198613595653"><a name="p198613595653"></a><a name="p198613595653"></a>records</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.2 "><p id="p2665924295653"><a name="p2665924295653"></a><a name="p2665924295653"></a>List&lt;PutRecordResult&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.18%" headers="mcps1.2.4.1.3 "><p id="p1191500295653"><a name="p1191500295653"></a><a name="p1191500295653"></a>Processing result of each data record.</p>
    <p id="p4012615695653"><a name="p4012615695653"></a><a name="p4012615695653"></a>For more information, see <a href="#table9600654145646">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **PutRecordResult**  parameter description

    <a name="table9600654145646"></a>
    <table><thead align="left"><tr id="row44539515"><th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.1"><p id="p50930930"><a name="p50930930"></a><a name="p50930930"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.310000000000002%" id="mcps1.2.4.1.2"><p id="p31764686"><a name="p31764686"></a><a name="p31764686"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.160000000000004%" id="mcps1.2.4.1.3"><p id="p22802807"><a name="p22802807"></a><a name="p22802807"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row30799715113618"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p17268771113624"><a name="p17268771113624"></a><a name="p17268771113624"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.2.4.1.2 "><p id="p56593178113624"><a name="p56593178113624"></a><a name="p56593178113624"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p20644726113624"><a name="p20644726113624"></a><a name="p20644726113624"></a>Error code for an individual record result.</p>
    </td>
    </tr>
    <tr id="row57095544113615"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p17620380113624"><a name="p17620380113624"></a><a name="p17620380113624"></a>error_message</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.2.4.1.2 "><p id="p17964642113624"><a name="p17964642113624"></a><a name="p17964642113624"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p45849897113624"><a name="p45849897113624"></a><a name="p45849897113624"></a>Error message for an individual record result.</p>
    </td>
    </tr>
    <tr id="row35088084"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p2601223211363"><a name="p2601223211363"></a><a name="p2601223211363"></a>partition_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.2.4.1.2 "><p id="p5133722810059"><a name="p5133722810059"></a><a name="p5133722810059"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p4792019510059"><a name="p4792019510059"></a><a name="p4792019510059"></a>Partition ID for an individual record result.</p>
    </td>
    </tr>
    <tr id="row14913854"><td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p3724278211369"><a name="p3724278211369"></a><a name="p3724278211369"></a>sequence_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.2.4.1.2 "><p id="p5077725"><a name="p5077725"></a><a name="p5077725"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p23562633144229"><a name="p23562633144229"></a><a name="p23562633144229"></a><span id="text5094682124159"><a name="text5094682124159"></a><a name="text5094682124159"></a>Sequence number of an individual data record. Each data record has a sequence number that is unique within its partition. The sequence number is assigned by DIS when a data producer calls PutRecords to add data to a DIS stream. Sequence numbers for the same partition key generally increase over time; the longer the time period between write requests (PutRecords requests), the larger the sequence numbers become.</span></p>
    </td>
    </tr>
    </tbody>
    </table>


## Status Code<a name="section65302542113017"></a>

-   Normal

    200 OK

-   Failed

    For more information, see  [Error Codes](error-codes.md).


