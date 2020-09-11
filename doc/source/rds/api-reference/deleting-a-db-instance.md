# Deleting a DB Instance<a name="en-us_topic_0032347781"></a>

## Function<a name="section29874939"></a>

This API is used to delete a DB instance.

## URI<a name="section439002"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/instances/\{instanceId\}

    Method: DELETE

-   Parameter description

    **Table  1**  Parameter description

    <a name="table4508766"></a>
    <table><thead align="left"><tr id="row21306406"><th class="cellrowborder" valign="top" width="22.05%" id="mcps1.2.4.1.1"><p id="p48097351"><a name="p48097351"></a><a name="p48097351"></a><strong id="b842352706102328_1"><a name="b842352706102328_1"></a><a name="b842352706102328_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.07%" id="mcps1.2.4.1.2"><p id="p3571397"><a name="p3571397"></a><a name="p3571397"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.88%" id="mcps1.2.4.1.3"><p id="p20847751"><a name="p20847751"></a><a name="p20847751"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10946294"><td class="cellrowborder" valign="top" width="22.05%" headers="mcps1.2.4.1.1 "><p id="p14234617"><a name="p14234617"></a><a name="p14234617"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.2 "><p id="p12153337"><a name="p12153337"></a><a name="p12153337"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.88%" headers="mcps1.2.4.1.3 "><p id="p19338596163746"><a name="p19338596163746"></a><a name="p19338596163746"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row1412808"><td class="cellrowborder" valign="top" width="22.05%" headers="mcps1.2.4.1.1 "><p id="p47328638"><a name="p47328638"></a><a name="p47328638"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.07%" headers="mcps1.2.4.1.2 "><p id="p8414476"><a name="p8414476"></a><a name="p8414476"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.88%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Specifies the primary node ID of the DB instance.</p>
    <div class="note" id="note18250133224019"><a name="note18250133224019"></a><a name="note18250133224019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p142501332164011"><a name="p142501332164011"></a><a name="p142501332164011"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


-   Restrictions

    Standby DB instances cannot be deleted.


## Request<a name="section3951024"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table2131788218919"></a>
    <table><thead align="left"><tr id="row4584518218919"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="p2247228518919"><a name="p2247228518919"></a><a name="p2247228518919"></a><strong id="b842352706102328_3"><a name="b842352706102328_3"></a><a name="b842352706102328_3"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.74427442744275%" id="mcps1.2.4.1.2"><p id="p831579218919"><a name="p831579218919"></a><a name="p831579218919"></a><strong id="b842352706102346_5"><a name="b842352706102346_5"></a><a name="b842352706102346_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.01330133013302%" id="mcps1.2.4.1.3"><p id="p249056018919"><a name="p249056018919"></a><a name="p249056018919"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row40878818919"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p3311186118919"><a name="p3311186118919"></a><a name="p3311186118919"></a>keepLastManualBackup</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.74427442744275%" headers="mcps1.2.4.1.2 "><p id="p6481505018919"><a name="p6481505018919"></a><a name="p6481505018919"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.01330133013302%" headers="mcps1.2.4.1.3 "><p id="p22237723165518"><a name="p22237723165518"></a><a name="p22237723165518"></a>This parameter is obsolete. Its value can be left empty or set to an integer and has no impact on calling the API.</p>
    <p id="p30519341165019"><a name="p30519341165019"></a><a name="p30519341165019"></a>All automated backups will be deleted and all manual backups will be retained.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    ```
    {
    "keepLastManualBackup": "0"
    }
    ```


## Normal Response<a name="section35559222"></a>

-   Parameter description

    **Table  3**  Parameter description

    <a name="table29807226151454"></a>
    <table><thead align="left"><tr id="row3223123151454"><th class="cellrowborder" valign="top" width="24.122412241224122%" id="mcps1.2.4.1.1"><p id="p59746450151454"><a name="p59746450151454"></a><a name="p59746450151454"></a><strong id="b842352706102328_5"><a name="b842352706102328_5"></a><a name="b842352706102328_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.544254425442546%" id="mcps1.2.4.1.2"><p id="p7624314151454"><a name="p7624314151454"></a><a name="p7624314151454"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p13589682151454"><a name="p13589682151454"></a><a name="p13589682151454"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row27022434151454"><td class="cellrowborder" valign="top" width="24.122412241224122%" headers="mcps1.2.4.1.1 "><p id="p41333555151454"><a name="p41333555151454"></a><a name="p41333555151454"></a>extendparam</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.544254425442546%" headers="mcps1.2.4.1.2 "><p id="p59683660151454"><a name="p59683660151454"></a><a name="p59683660151454"></a>Dictionary data structure. For details, see <a href="#table32267243">Table 4</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p22844941151454"><a name="p22844941151454"></a><a name="p22844941151454"></a>Indicates the returned <strong id="b842352706113519"><a name="b842352706113519"></a><a name="b842352706113519"></a>extendparam</strong> key-value pair.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  extendparam field data structure description

    <a name="table32267243"></a>
    <table><thead align="left"><tr id="row9230088"><th class="cellrowborder" valign="top" width="24.69%" id="mcps1.2.4.1.1"><p id="p11190634151741"><a name="p11190634151741"></a><a name="p11190634151741"></a><strong id="b84235270691445_3"><a name="b84235270691445_3"></a><a name="b84235270691445_3"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.16%" id="mcps1.2.4.1.2"><p id="p16816714151741"><a name="p16816714151741"></a><a name="p16816714151741"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.15%" id="mcps1.2.4.1.3"><p id="p22858126151741"><a name="p22858126151741"></a><a name="p22858126151741"></a><strong id="b842352706163417_9"><a name="b842352706163417_9"></a><a name="b842352706163417_9"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15736877"><td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.2.4.1.1 "><p id="p25628649151741"><a name="p25628649151741"></a><a name="p25628649151741"></a>jobs</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.16%" headers="mcps1.2.4.1.2 "><p id="p1615789151741"><a name="p1615789151741"></a><a name="p1615789151741"></a>List data structure. For details, see <a href="#table57556452151811">Table 5</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.15%" headers="mcps1.2.4.1.3 "><p id="p41083402151741"><a name="p41083402151741"></a><a name="p41083402151741"></a>Indicates the returned <strong id="b842352706113940"><a name="b842352706113940"></a><a name="b842352706113940"></a>jobs</strong> parameter information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  jobs field data structure description

    <a name="table57556452151811"></a>
    <table><thead align="left"><tr id="row53658718151811"><th class="cellrowborder" valign="top" width="24.69%" id="mcps1.2.4.1.1"><p id="p36464991151811"><a name="p36464991151811"></a><a name="p36464991151811"></a><strong id="b84235270691445_5"><a name="b84235270691445_5"></a><a name="b84235270691445_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="41.980000000000004%" id="mcps1.2.4.1.2"><p id="p41158197151811"><a name="p41158197151811"></a><a name="p41158197151811"></a><strong id="b842352706164541_5"><a name="b842352706164541_5"></a><a name="b842352706164541_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p31836063151811"><a name="p31836063151811"></a><a name="p31836063151811"></a><strong id="b842352706163417_11"><a name="b842352706163417_11"></a><a name="b842352706163417_11"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2444491151811"><td class="cellrowborder" valign="top" width="24.69%" headers="mcps1.2.4.1.1 "><p id="p3112662151811"><a name="p3112662151811"></a><a name="p3112662151811"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.980000000000004%" headers="mcps1.2.4.1.2 "><p id="p10765391151811"><a name="p10765391151811"></a><a name="p10765391151811"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p29880500151811"><a name="p29880500151811"></a><a name="p29880500151811"></a>Indicates the task ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
       "extendparam": {
          "jobs": [ 
             {
                 "id":"ff8080815a88d52c015a8a0db2250003"
             } 
          ]
       }
    }
    ```


## Abnormal Response<a name="section51597550"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

