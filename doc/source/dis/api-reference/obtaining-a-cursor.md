# Obtaining a Cursor<a name="dis_02_0020"></a>

## Function<a name="section46191521"></a>

This API is used to obtain a data cursor.

There are five cursor types available:

-   AT\_SEQUENCE\_NUMBER
-   AFTER\_SEQUENCE\_NUMBER
-   TRIM\_HORIZON
-   LATEST
-   AT\_TIMESTAMP

To download streaming data, you need to determine the position where the data is obtained from the partition, that is, to obtain the cursor. After the start position is determined, the data is obtained cyclically.

## URI<a name="section13070512"></a>

-   URI format

    GET /v2/\{project\_id\}/cursors\{?stream-name,stream-id,partition-id,cursor-type,starting-sequence-number\}

-   Parameter description

    None


## Request<a name="section50525752"></a>

-   Example request

    ```
    GET https://{endpoint}/v2/{project_id}/cursors?stream-name=lzc08&stream-id=i9eOJp4sTYRApsWwJDS&partition-id=0&cursor-type=AT_SEQUENCE_NUMBER&starting-sequence-number=l1        
    ```

-   Parameter description

    **Table  1**  Parameter description

    <a name="table47841633"></a>
    <table><thead align="left"><tr id="row37599894"><th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.1"><p id="p25692540"><a name="p25692540"></a><a name="p25692540"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.308469153084694%" id="mcps1.2.5.1.2"><p id="p720995"><a name="p720995"></a><a name="p720995"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p58400626"><a name="p58400626"></a><a name="p58400626"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.93530646935306%" id="mcps1.2.5.1.4"><p id="p32830290"><a name="p32830290"></a><a name="p32830290"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42007851"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p66260603113816"><a name="p66260603113816"></a><a name="p66260603113816"></a>stream-name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p64515557"><a name="p64515557"></a><a name="p64515557"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p58377623"><a name="p58377623"></a><a name="p58377623"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p30967009"><a name="p30967009"></a><a name="p30967009"></a><span id="text19604279144639"><a name="text19604279144639"></a><a name="text19604279144639"></a>Name of the stream created on the management console.</span></p>
    <p id="p977965794531"><a name="p977965794531"></a><a name="p977965794531"></a>Value range: Only letters, digits, hyphens (-), and underscores (_) are allowed.</p>
    <p id="p417910414053"><a name="p417910414053"></a><a name="p417910414053"></a>The value must be 1 to 64 characters long.</p>
    </td>
    </tr>
    <tr id="row62696124210"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p32701120216"><a name="p32701120216"></a><a name="p32701120216"></a>stream_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p427021215216"><a name="p427021215216"></a><a name="p427021215216"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p827012122219"><a name="p827012122219"></a><a name="p827012122219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p152704121629"><a name="p152704121629"></a><a name="p152704121629"></a>Unique ID of the stream.</p>
    <p id="p891773618311"><a name="p891773618311"></a><a name="p891773618311"></a>If no stream is found based on stream_name and stream_id is not empty, stream_id is used to search for the stream.</p>
    </td>
    </tr>
    <tr id="row10267631"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p33186307113823"><a name="p33186307113823"></a><a name="p33186307113823"></a>partition-id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p55740512"><a name="p55740512"></a><a name="p55740512"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p18687619"><a name="p18687619"></a><a name="p18687619"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p37302179"><a name="p37302179"></a><a name="p37302179"></a>Partition ID of a stream.</p>
    <p id="p3991828135610"><a name="p3991828135610"></a><a name="p3991828135610"></a>Two partition ID formats are available:</p>
    <a name="ul715543195618"></a><a name="ul715543195618"></a><ul id="ul715543195618"><li>shardId-0000000000</li><li>0</li></ul>
    </td>
    </tr>
    <tr id="row175293"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p44744140113841"><a name="p44744140113841"></a><a name="p44744140113841"></a>cursor-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p9248440"><a name="p9248440"></a><a name="p9248440"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p10926182"><a name="p10926182"></a><a name="p10926182"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p12605589"><a name="p12605589"></a><a name="p12605589"></a>Cursor type.</p>
    <a name="ul27841096142711"></a><a name="ul27841096142711"></a><ul id="ul27841096142711"><li>AT_SEQUENCE_NUMBER: Data is read from the position denoted by a specific sequence number (that is defined by <strong id="b957523716178"><a name="b957523716178"></a><a name="b957523716178"></a>starting-sequence-number</strong>). This is the default cursor type.</li><li>AFTER_SEQUENCE_NUMBER: Data is read right after the position denoted by a specific sequence number (that is defined by <strong id="b1808917171710"><a name="b1808917171710"></a><a name="b1808917171710"></a>starting-sequence-number</strong>).</li><li>TRIM_HORIZON: Data is read from the earliest valid records that are stored in the partition.<p id="p66465473710"><a name="p66465473710"></a><a name="p66465473710"></a>For example, a tenant uses a DIS stream to upload three pieces of data A1, A2, and A3. N days later, A1 has expired and A2 and A3 are still in the validity period. In this case, if the tenant uses TRIM_HORIZON to download the data, only A2 and A3 are downloadable.</p>
    </li><li>LATEST: Data is read just after the most recent record in the partition. This setting ensures that you always read the most recent data in the partition.</li><li id="li1853861617205"><a name="li1853861617205"></a><a name="li1853861617205"></a>AT_TIMESTAMP: Data is read from the position denoted by a specific timestamp (that is defined by <strong id="b4547427121712"><a name="b4547427121712"></a><a name="b4547427121712"></a>timestamp</strong>).</li></ul>
    </td>
    </tr>
    <tr id="row46341445"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p33065814113913"><a name="p33065814113913"></a><a name="p33065814113913"></a>starting-sequence-number</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p43066942"><a name="p43066942"></a><a name="p43066942"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p65870306"><a name="p65870306"></a><a name="p65870306"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p33894570"><a name="p33894570"></a><a name="p33894570"></a><span id="text2201432144311"><a name="text2201432144311"></a><a name="text2201432144311"></a>Sequence number of an individual data record. Each data record has a sequence number that is unique within its partition. The sequence number is assigned by DIS when a data producer calls PutRecords to add data to a DIS stream. Sequence numbers for the same partition key generally increase over time; the longer the time period between write requests (PutRecords requests), the larger the sequence numbers become.</span></p>
    <p id="p16816213192118"><a name="p16816213192118"></a><a name="p16816213192118"></a>The sequence number is closely related to cursor types <strong id="b7841192611554"><a name="b7841192611554"></a><a name="b7841192611554"></a>AT_SEQUENCE_NUMBER</strong> and <strong id="b83738312553"><a name="b83738312553"></a><a name="b83738312553"></a>AFTER_SEQUENCE_NUMBER</strong>. The two parameters determine the location of the data to be accessed.</p>
    <p id="p51849298142548"><a name="p51849298142548"></a><a name="p51849298142548"></a>Value range: 0 to 9223372036854775807</p>
    </td>
    </tr>
    <tr id="row15103517114"><td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.1 "><p id="p994917192456"><a name="p994917192456"></a><a name="p994917192456"></a>timestamp</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="p594961916459"><a name="p594961916459"></a><a name="p594961916459"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p12949181954511"><a name="p12949181954511"></a><a name="p12949181954511"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.93530646935306%" headers="mcps1.2.5.1.4 "><p id="p995041919450"><a name="p995041919450"></a><a name="p995041919450"></a>Timestamp when the data record starts to be accessed. It is closely related to cursor type <a href="#li1853861617205">AT_TIMESTAMP</a>. The two parameters determine the location of the data to be accessed.</p>
    <div class="note" id="note64013584172539"><a name="note64013584172539"></a><a name="note64013584172539"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p5256102617255"><a name="p5256102617255"></a><a name="p5256102617255"></a>This timestamp is accurate to milliseconds.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


## Response<a name="section52078584"></a>

-   Example response

    ```
    {
     "partition_cursor": "eyJnZXRJdGVyYXRvclBhcmFtIjp7InN0cmVhbS1uYW1lIjoianpjIiwicGFydGl0aW9uLWlkIjoiMCIsImN1cnNvci10eXBlIjoiQVRfU0VRVUVOQ0VfTlVNQkVSIiwic3RhcnRpbmctc2VxdWVuY2UtbnVtYmVyIjoiMTAifSwiZ2VuZXJhdGVUaW1lc3RhbXAiOjE1MDYxNTk1NjM0MDV9"
    }
    ```

-   Parameter description

    **Table  2**  Response parameter description

    <a name="table43390320165757"></a>
    <table><thead align="left"><tr id="row61194080"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p57773428"><a name="p57773428"></a><a name="p57773428"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p49136085"><a name="p49136085"></a><a name="p49136085"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p20599914"><a name="p20599914"></a><a name="p20599914"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57980315"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p20796043114118"><a name="p20796043114118"></a><a name="p20796043114118"></a>partition_cursor</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p35811316"><a name="p35811316"></a><a name="p35811316"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15035499"><a name="p15035499"></a><a name="p15035499"></a>Cursor of the partition used to specify the position in the partition from which to start reading data records sequentially.</p>
    <p id="p33919450142819"><a name="p33919450142819"></a><a name="p33919450142819"></a>Value: 1 to 512 characters</p>
    <div class="note" id="note2086939164321"><a name="note2086939164321"></a><a name="note2086939164321"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p18782458164321"><a name="p18782458164321"></a><a name="p18782458164321"></a>The validity period of a cursor is 5 minutes.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


## Status Code<a name="section65302542113017"></a>

-   Normal

    200 OK

-   Failed

    For more information, see  [Error Codes](error-codes.md).


