# Querying Database Slow Logs<a name="en-us_topic_0037147511"></a>

## Function<a name="section61759636"></a>

This API is used to query database slow logs.

## URI<a name="section18965813"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/instances/\{instanceId\}/slowlog

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table58427690"></a>
    <table><thead align="left"><tr id="row1482002"><th class="cellrowborder" valign="top" width="21.11%" id="mcps1.2.4.1.1"><p id="p52933326"><a name="p52933326"></a><a name="p52933326"></a><strong id="b842352706102328_1"><a name="b842352706102328_1"></a><a name="b842352706102328_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.88%" id="mcps1.2.4.1.2"><p id="p59740974"><a name="p59740974"></a><a name="p59740974"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.01%" id="mcps1.2.4.1.3"><p id="p7180698"><a name="p7180698"></a><a name="p7180698"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44765691"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="p2142393"><a name="p2142393"></a><a name="p2142393"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.88%" headers="mcps1.2.4.1.2 "><p id="p39316155"><a name="p39316155"></a><a name="p39316155"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.2.4.1.3 "><p id="p30492010"><a name="p30492010"></a><a name="p30492010"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row5992637"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="p15641626"><a name="p15641626"></a><a name="p15641626"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.88%" headers="mcps1.2.4.1.2 "><p id="p59012183"><a name="p59012183"></a><a name="p59012183"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Specifies the primary node ID of the DB instance.</p>
    <div class="note" id="note18250133224019"><a name="note18250133224019"></a><a name="note18250133224019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p142501332164011"><a name="p142501332164011"></a><a name="p142501332164011"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions

    Only MySQL DB instances are supported.


## Request<a name="section36474591"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table22478116"></a>
    <table><thead align="left"><tr id="row12299945"><th class="cellrowborder" valign="top" width="21.11%" id="mcps1.2.4.1.1"><p id="p56771492"><a name="p56771492"></a><a name="p56771492"></a><strong id="b842352706102328_5"><a name="b842352706102328_5"></a><a name="b842352706102328_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.64%" id="mcps1.2.4.1.2"><p id="p35088115"><a name="p35088115"></a><a name="p35088115"></a><strong id="b842352706102346_5"><a name="b842352706102346_5"></a><a name="b842352706102346_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.24999999999999%" id="mcps1.2.4.1.3"><p id="p23565055"><a name="p23565055"></a><a name="p23565055"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row53630064175338"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="p50260708175338"><a name="p50260708175338"></a><a name="p50260708175338"></a>sftype</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.64%" headers="mcps1.2.4.1.2 "><p id="p44585518175338"><a name="p44585518175338"></a><a name="p44585518175338"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.24999999999999%" headers="mcps1.2.4.1.3 "><p id="p54657188175338"><a name="p54657188175338"></a><a name="p54657188175338"></a>Specifies the statement type. Its value can be empty, <strong id="b842352706906"><a name="b842352706906"></a><a name="b842352706906"></a>INSERT</strong>, <strong id="b8423527069010"><a name="b8423527069010"></a><a name="b8423527069010"></a>UPDATE</strong>, <strong id="b8423527069013"><a name="b8423527069013"></a><a name="b8423527069013"></a>SELECT</strong>, <strong id="b8423527069016"><a name="b8423527069016"></a><a name="b8423527069016"></a>DELETE</strong>, or <strong id="b8423527069020"><a name="b8423527069020"></a><a name="b8423527069020"></a>CREATE</strong>. If the value is empty, all statement types exist.</p>
    </td>
    </tr>
    <tr id="row50698138175338"><td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.1 "><p id="p49534384175338"><a name="p49534384175338"></a><a name="p49534384175338"></a>top</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.64%" headers="mcps1.2.4.1.2 "><p id="p52862197175338"><a name="p52862197175338"></a><a name="p52862197175338"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.24999999999999%" headers="mcps1.2.4.1.3 "><p id="p3481240119126"><a name="p3481240119126"></a><a name="p3481240119126"></a>Specifies how many records are returned.</p>
    <a name="ul5678002519211"></a><a name="ul5678002519211"></a><ul id="ul5678002519211"><li>If this parameter is specified, the value range is from 1 to 50.</li><li>If this parameter is not specified, the first 10 records are returned.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    ```
    /rds/v1/68e3010955d748099f62a0df726fe09b/instances/02e47383-9222-4d29-bf5b-54b3013b0f71/slowlog?sftype=&top=10
    ```


## Normal Response<a name="section59835867"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table29752153"></a>
    <table><thead align="left"><tr id="row62070345"><th class="cellrowborder" valign="top" width="20.919999999999998%" id="mcps1.2.4.1.1"><p id="p61642077"><a name="p61642077"></a><a name="p61642077"></a><strong id="b842352706102328_7"><a name="b842352706102328_7"></a><a name="b842352706102328_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.21%" id="mcps1.2.4.1.2"><p id="p26952341"><a name="p26952341"></a><a name="p26952341"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.87%" id="mcps1.2.4.1.3"><p id="p35656026"><a name="p35656026"></a><a name="p35656026"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49943891183823"><td class="cellrowborder" valign="top" width="20.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p17747976183823"><a name="p17747976183823"></a><a name="p17747976183823"></a>slowLogList</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.21%" headers="mcps1.2.4.1.2 "><p id="p28299952183823"><a name="p28299952183823"></a><a name="p28299952183823"></a>List data structure. For details, see <a href="#table66531170">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.87%" headers="mcps1.2.4.1.3 "><p id="p10594789183823"><a name="p10594789183823"></a><a name="p10594789183823"></a>Indicates detailed information.</p>
    </td>
    </tr>
    <tr id="row6331999514368"><td class="cellrowborder" valign="top" width="20.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p27570747143630"><a name="p27570747143630"></a><a name="p27570747143630"></a>totalRecord</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.21%" headers="mcps1.2.4.1.2 "><p id="p18638029143630"><a name="p18638029143630"></a><a name="p18638029143630"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.87%" headers="mcps1.2.4.1.3 "><p id="p33285367143630"><a name="p33285367143630"></a><a name="p33285367143630"></a>Indicates the total number of records.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  slowLogList field data structure description

    <a name="table66531170"></a>
    <table><thead align="left"><tr id="row12984378"><th class="cellrowborder" valign="top" width="20.73%" id="mcps1.2.4.1.1"><p id="p45101667"><a name="p45101667"></a><a name="p45101667"></a><strong id="b842352706102328_9"><a name="b842352706102328_9"></a><a name="b842352706102328_9"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.759999999999998%" id="mcps1.2.4.1.2"><p id="p29356372"><a name="p29356372"></a><a name="p29356372"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.51%" id="mcps1.2.4.1.3"><p id="p29055926"><a name="p29055926"></a><a name="p29055926"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4719792"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p46758891"><a name="p46758891"></a><a name="p46758891"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.759999999999998%" headers="mcps1.2.4.1.2 "><p id="p29373839"><a name="p29373839"></a><a name="p29373839"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.51%" headers="mcps1.2.4.1.3 "><p id="p30470722"><a name="p30470722"></a><a name="p30470722"></a>Indicates the number of executions.</p>
    </td>
    </tr>
    <tr id="row5801050"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p123050"><a name="p123050"></a><a name="p123050"></a>time</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.759999999999998%" headers="mcps1.2.4.1.2 "><p id="p9967070"><a name="p9967070"></a><a name="p9967070"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.51%" headers="mcps1.2.4.1.3 "><p id="p2026335"><a name="p2026335"></a><a name="p2026335"></a>Indicates the average execution duration.</p>
    </td>
    </tr>
    <tr id="row1562610185558"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p27564685185558"><a name="p27564685185558"></a><a name="p27564685185558"></a>lockTime</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.759999999999998%" headers="mcps1.2.4.1.2 "><p id="p18147022185558"><a name="p18147022185558"></a><a name="p18147022185558"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.51%" headers="mcps1.2.4.1.3 "><p id="p60622679185558"><a name="p60622679185558"></a><a name="p60622679185558"></a>Indicates the average waiting time before locking.</p>
    </td>
    </tr>
    <tr id="row46227617185624"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p61882053185624"><a name="p61882053185624"></a><a name="p61882053185624"></a>rowsSent</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.759999999999998%" headers="mcps1.2.4.1.2 "><p id="p46390393185624"><a name="p46390393185624"></a><a name="p46390393185624"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.51%" headers="mcps1.2.4.1.3 "><p id="p66634382185624"><a name="p66634382185624"></a><a name="p66634382185624"></a>Indicates the average number of rows contained in a result.</p>
    </td>
    </tr>
    <tr id="row26041859185714"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p62791567185714"><a name="p62791567185714"></a><a name="p62791567185714"></a>rowsExamined</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.759999999999998%" headers="mcps1.2.4.1.2 "><p id="p52952143185714"><a name="p52952143185714"></a><a name="p52952143185714"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.51%" headers="mcps1.2.4.1.3 "><p id="p61265200185714"><a name="p61265200185714"></a><a name="p61265200185714"></a>Indicates the average number of scanned rows.</p>
    </td>
    </tr>
    <tr id="row8051277185753"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p65936923185753"><a name="p65936923185753"></a><a name="p65936923185753"></a>database</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.759999999999998%" headers="mcps1.2.4.1.2 "><p id="p39290538185753"><a name="p39290538185753"></a><a name="p39290538185753"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.51%" headers="mcps1.2.4.1.3 "><p id="p28417034185753"><a name="p28417034185753"></a><a name="p28417034185753"></a>Indicates the database which the slow log belongs to.</p>
    </td>
    </tr>
    <tr id="row62737284185755"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p65776751185755"><a name="p65776751185755"></a><a name="p65776751185755"></a>users</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.759999999999998%" headers="mcps1.2.4.1.2 "><p id="p26316620185755"><a name="p26316620185755"></a><a name="p26316620185755"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.51%" headers="mcps1.2.4.1.3 "><p id="p51271494185755"><a name="p51271494185755"></a><a name="p51271494185755"></a>Indicates the account.</p>
    </td>
    </tr>
    <tr id="row24608043185759"><td class="cellrowborder" valign="top" width="20.73%" headers="mcps1.2.4.1.1 "><p id="p60502836185759"><a name="p60502836185759"></a><a name="p60502836185759"></a>querySample</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.759999999999998%" headers="mcps1.2.4.1.2 "><p id="p1782674185759"><a name="p1782674185759"></a><a name="p1782674185759"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.51%" headers="mcps1.2.4.1.3 "><p id="p10178909185759"><a name="p10178909185759"></a><a name="p10178909185759"></a>Indicates the execution syntax.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {    "slowLogList": [
            {
                "count": " 409  (99.76%)",
                "time": "1.29",
                "lockTime": " 0 ",
                "rowsSent": " 0 ",
                "rowsExamined": " 0 ",
                "database": " ",
                "users": " \trdsBackup@localhost  : 100.00% (409) of query, 99.76% (409) of all users",
                "querySample": "flush logs;"
            },
            {
                "count": " 1  (0.24%)",
                "time": "5.0",
                "lockTime": " 0 ",
                "rowsSent": " 1 ",
                "rowsExamined": " 0 ",
                "database": " ",
                "users": " \trdsAdmin@localhost  : 100.00% (1) of query, 0.24% (1) of all users",
                "querySample": "select sleep(5);"
            }
        ],
        "totalRecord": 2
    }
    ```


## Abnormal Response<a name="section1651899"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

