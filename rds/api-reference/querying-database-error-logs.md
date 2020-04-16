# Querying Database Error Logs<a name="en-us_topic_0037147510"></a>

## Function<a name="section61759636"></a>

This API is used to query database error logs.

## URI<a name="section18965813"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/instances/\{instanceId\}/errorlog

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table58427690"></a>
    <table><thead align="left"><tr id="row1482002"><th class="cellrowborder" valign="top" width="20.93%" id="mcps1.2.4.1.1"><p id="p52933326"><a name="p52933326"></a><a name="p52933326"></a><strong id="b842352706102328_1"><a name="b842352706102328_1"></a><a name="b842352706102328_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.449999999999996%" id="mcps1.2.4.1.2"><p id="p59740974"><a name="p59740974"></a><a name="p59740974"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.62%" id="mcps1.2.4.1.3"><p id="p7180698"><a name="p7180698"></a><a name="p7180698"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44765691"><td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.1 "><p id="p2142393"><a name="p2142393"></a><a name="p2142393"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.449999999999996%" headers="mcps1.2.4.1.2 "><p id="p39316155"><a name="p39316155"></a><a name="p39316155"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.62%" headers="mcps1.2.4.1.3 "><p id="p30492010"><a name="p30492010"></a><a name="p30492010"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row5992637"><td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.1 "><p id="p15641626"><a name="p15641626"></a><a name="p15641626"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.449999999999996%" headers="mcps1.2.4.1.2 "><p id="p59012183"><a name="p59012183"></a><a name="p59012183"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.62%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Specifies the primary node ID of the DB instance.</p>
    <div class="note" id="note18250133224019"><a name="note18250133224019"></a><a name="note18250133224019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p142501332164011"><a name="p142501332164011"></a><a name="p142501332164011"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section36474591"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table22478116"></a>
    <table><thead align="left"><tr id="row12299945"><th class="cellrowborder" valign="top" width="21.490000000000002%" id="mcps1.2.4.1.1"><p id="p56771492"><a name="p56771492"></a><a name="p56771492"></a><strong id="b842352706102328_3"><a name="b842352706102328_3"></a><a name="b842352706102328_3"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.08%" id="mcps1.2.4.1.2"><p id="p35088115"><a name="p35088115"></a><a name="p35088115"></a><strong id="b842352706102346_5"><a name="b842352706102346_5"></a><a name="b842352706102346_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.43%" id="mcps1.2.4.1.3"><p id="p23565055"><a name="p23565055"></a><a name="p23565055"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35621668174547"><td class="cellrowborder" valign="top" width="21.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p24007821174547"><a name="p24007821174547"></a><a name="p24007821174547"></a>startDate</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.08%" headers="mcps1.2.4.1.2 "><p id="p65585369174547"><a name="p65585369174547"></a><a name="p65585369174547"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="p10814706174547"><a name="p10814706174547"></a><a name="p10814706174547"></a>Specifies the start time following a specified time translation rule. For example, time "2016-08-29+06:35" is translated into "2016-08-29+06%3A35", where "%3A" is translated from ":" and other digits and characters remain unchanged.</p>
    </td>
    </tr>
    <tr id="row56153746174547"><td class="cellrowborder" valign="top" width="21.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p32183997174547"><a name="p32183997174547"></a><a name="p32183997174547"></a>endDate</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.08%" headers="mcps1.2.4.1.2 "><p id="p56766964174547"><a name="p56766964174547"></a><a name="p56766964174547"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="p185070539196"><a name="p185070539196"></a><a name="p185070539196"></a>Specifies the end time following a specified time translation rule. For example, time "2016-08-29+06:35" is translated into "2016-08-29+06%3A35", where "%3A" is translated from ":" and other digits and characters remain unchanged.</p>
    <p id="p34721363174547"><a name="p34721363174547"></a><a name="p34721363174547"></a>You can only query error logs generated within a month.</p>
    </td>
    </tr>
    <tr id="row50978547174547"><td class="cellrowborder" valign="top" width="21.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p11832481174547"><a name="p11832481174547"></a><a name="p11832481174547"></a>curPage</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.08%" headers="mcps1.2.4.1.2 "><p id="p18906893174547"><a name="p18906893174547"></a><a name="p18906893174547"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="p55063325174547"><a name="p55063325174547"></a><a name="p55063325174547"></a>Specifies the current page number, such as 1, 2, 3, or 4. The parameter value is <strong id="b842352706164811"><a name="b842352706164811"></a><a name="b842352706164811"></a>1</strong> by default if it is not specified.</p>
    </td>
    </tr>
    <tr id="row28033904174547"><td class="cellrowborder" valign="top" width="21.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p10063368174547"><a name="p10063368174547"></a><a name="p10063368174547"></a>perPage</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.08%" headers="mcps1.2.4.1.2 "><p id="p9826466174547"><a name="p9826466174547"></a><a name="p9826466174547"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.43%" headers="mcps1.2.4.1.3 "><p id="p57746301174547"><a name="p57746301174547"></a><a name="p57746301174547"></a>Specifies the number of records on a page. Its value range is from 1 to 100. The parameter value is <strong id="b842352706164925"><a name="b842352706164925"></a><a name="b842352706164925"></a>10</strong> by default if it is not specified.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    ```
    /rds/v1/68e3010955d748099f62a0df726fe09b/instances/02cf1fd7-24ae-4fec-a621-329ec732e4f6/errorlog?startDate=2016-08-29+06%3A35&endDate=2016-09-05+06%3A35&curPage=1&perPage=10
    ```


## Normal Response<a name="section59835867"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table29752153"></a>
    <table><thead align="left"><tr id="row62070345"><th class="cellrowborder" valign="top" width="22.05%" id="mcps1.2.4.1.1"><p id="p61642077"><a name="p61642077"></a><a name="p61642077"></a><strong id="b842352706102328_5"><a name="b842352706102328_5"></a><a name="b842352706102328_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.889999999999997%" id="mcps1.2.4.1.2"><p id="p26952341"><a name="p26952341"></a><a name="p26952341"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.06%" id="mcps1.2.4.1.3"><p id="p35656026"><a name="p35656026"></a><a name="p35656026"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49943891183823"><td class="cellrowborder" valign="top" width="22.05%" headers="mcps1.2.4.1.1 "><p id="p17747976183823"><a name="p17747976183823"></a><a name="p17747976183823"></a>errorLogList</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.2 "><p id="p28299952183823"><a name="p28299952183823"></a><a name="p28299952183823"></a>List data structure. For details, see <a href="#table66531170">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.06%" headers="mcps1.2.4.1.3 "><p id="p10594789183823"><a name="p10594789183823"></a><a name="p10594789183823"></a>Indicates detailed information.</p>
    </td>
    </tr>
    <tr id="row29657875143522"><td class="cellrowborder" valign="top" width="22.05%" headers="mcps1.2.4.1.1 "><p id="p56278588143531"><a name="p56278588143531"></a><a name="p56278588143531"></a>totalRecord</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.889999999999997%" headers="mcps1.2.4.1.2 "><p id="p62271785143531"><a name="p62271785143531"></a><a name="p62271785143531"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.06%" headers="mcps1.2.4.1.3 "><p id="p10849843143531"><a name="p10849843143531"></a><a name="p10849843143531"></a>Indicates the total number of records.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  errorLogList field data structure description

    <a name="table66531170"></a>
    <table><thead align="left"><tr id="row12984378"><th class="cellrowborder" valign="top" width="22.05%" id="mcps1.2.4.1.1"><p id="p45101667"><a name="p45101667"></a><a name="p45101667"></a><strong id="b842352706102328_7"><a name="b842352706102328_7"></a><a name="b842352706102328_7"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.2"><p id="p29356372"><a name="p29356372"></a><a name="p29356372"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.88%" id="mcps1.2.4.1.3"><p id="p29055926"><a name="p29055926"></a><a name="p29055926"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4719792"><td class="cellrowborder" valign="top" width="22.05%" headers="mcps1.2.4.1.1 "><p id="p46758891"><a name="p46758891"></a><a name="p46758891"></a>datetime</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.2 "><p id="p29373839"><a name="p29373839"></a><a name="p29373839"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.88%" headers="mcps1.2.4.1.3 "><p id="p30470722"><a name="p30470722"></a><a name="p30470722"></a>Indicates the date and time.</p>
    </td>
    </tr>
    <tr id="row5801050"><td class="cellrowborder" valign="top" width="22.05%" headers="mcps1.2.4.1.1 "><p id="p123050"><a name="p123050"></a><a name="p123050"></a>content</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.2 "><p id="p9967070"><a name="p9967070"></a><a name="p9967070"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.88%" headers="mcps1.2.4.1.3 "><p id="p2026335"><a name="p2026335"></a><a name="p2026335"></a>Indicates the log content.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
        "errorLogList": [
            {
                "datetime": "2016-08-30 09:55:39",
                "content": "[Warning] 'proxies_priv' entry '@ root@rds-bf83' ignored in --skip-name-resolve mode."
            }
        ],
        "totalRecord":1
    }
    ```


## Abnormal Response<a name="section1651899"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

