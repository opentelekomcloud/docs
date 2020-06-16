# Querying a Quota<a name="EN-US_TOPIC_0090543963"></a>

## Function<a name="section63927665153611"></a>

This interface is used to query quota information.

>![](/images/icon-note.gif) **NOTE:**   
>SFS supports querying quotas of only tenants.  

## Command<a name="section29716671153611"></a>

-   Usage

    ```
    manila quota-show [--tenant <tenant-id>] [--user <user-id>]
    ```

-   Parameter description

    <a name="table62930403153611"></a>
    <table><thead align="left"><tr id="row44000776153611"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.5.1.1"><p id="p7293140153611"><a name="p7293140153611"></a><a name="p7293140153611"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.1.5.1.2"><p id="p53873435153611"><a name="p53873435153611"></a><a name="p53873435153611"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.1.5.1.3"><p id="p1672135153611"><a name="p1672135153611"></a><a name="p1672135153611"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.494949494949495%" id="mcps1.1.5.1.4"><p id="p1225280153611"><a name="p1225280153611"></a><a name="p1225280153611"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row32138861153611"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p53110967153611"><a name="p53110967153611"></a><a name="p53110967153611"></a>tenant-id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p7021061153611"><a name="p7021061153611"></a><a name="p7021061153611"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p31835072153611"><a name="p31835072153611"></a><a name="p31835072153611"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p28504015153611"><a name="p28504015153611"></a><a name="p28504015153611"></a>Specifies the UUID of the tenant whose quota is to be queried. This parameter is used by Administrator to query quotas of other tenants. For a common tenant, this parameter is unnecessary because only the tenant's own quota can be queried by default.</p>
    </td>
    </tr>
    <tr id="row55209546153611"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p42788211153611"><a name="p42788211153611"></a><a name="p42788211153611"></a>user-id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p43293028153611"><a name="p43293028153611"></a><a name="p43293028153611"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p17074374153611"><a name="p17074374153611"></a><a name="p17074374153611"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p40847040153611"><a name="p40847040153611"></a><a name="p40847040153611"></a>User ID</p>
    <div class="note" id="note14445102082520"><a name="note14445102082520"></a><a name="note14445102082520"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p184461820142518"><a name="p184461820142518"></a><a name="p184461820142518"></a>SFS supports querying quotas of only tenants. Therefore, setting this parameter for user quota query is meaningless.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   Example command

    ```
    manila quota-show
    ```


## Response<a name="section51404336153611"></a>

-   Parameter description

    <a name="table41810086153611"></a>
    <table><thead align="left"><tr id="row54498648153611"><th class="cellrowborder" valign="top" width="25.942594259425945%" id="mcps1.1.5.1.1"><p id="p52314340153611"><a name="p52314340153611"></a><a name="p52314340153611"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.431343134313432%" id="mcps1.1.5.1.2"><p id="p9603173153611"><a name="p9603173153611"></a><a name="p9603173153611"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.441544154415443%" id="mcps1.1.5.1.3"><p id="p39659587153611"><a name="p39659587153611"></a><a name="p39659587153611"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.18451845184518%" id="mcps1.1.5.1.4"><p id="p58309989153611"><a name="p58309989153611"></a><a name="p58309989153611"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row25488692153611"><td class="cellrowborder" valign="top" width="25.942594259425945%" headers="mcps1.1.5.1.1 "><p id="p51318167153611"><a name="p51318167153611"></a><a name="p51318167153611"></a>gigabytes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.431343134313432%" headers="mcps1.1.5.1.2 "><p id="p63130871153611"><a name="p63130871153611"></a><a name="p63130871153611"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.441544154415443%" headers="mcps1.1.5.1.3 "><p id="p44053564141022"><a name="p44053564141022"></a><a name="p44053564141022"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.18451845184518%" headers="mcps1.1.5.1.4 "><p id="p47753777141039"><a name="p47753777141039"></a><a name="p47753777141039"></a>Specifies the capacity in gigabytes allowed for each tenant. If the value is <strong id="b14817324343"><a name="b14817324343"></a><a name="b14817324343"></a>-1</strong>, there is no quota limit.</p>
    </td>
    </tr>
    <tr id="row63928818153611"><td class="cellrowborder" valign="top" width="25.942594259425945%" headers="mcps1.1.5.1.1 "><p id="p10851801153611"><a name="p10851801153611"></a><a name="p10851801153611"></a>snapshot_gigabytes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.431343134313432%" headers="mcps1.1.5.1.2 "><p id="p6580651153611"><a name="p6580651153611"></a><a name="p6580651153611"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.441544154415443%" headers="mcps1.1.5.1.3 "><p id="p63270738153611"><a name="p63270738153611"></a><a name="p63270738153611"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.18451845184518%" headers="mcps1.1.5.1.4 "><p id="p1441139141336"><a name="p1441139141336"></a><a name="p1441139141336"></a>Specifies the snapshot capacity in gigabytes allowed for each tenant. If the value is <strong id="b532119171"><a name="b532119171"></a><a name="b532119171"></a>-1</strong>, there is no quota limit.</p>
    <div class="notice" id="note197181343122910"><a name="note197181343122910"></a><a name="note197181343122910"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p14718164311291"><a name="p14718164311291"></a><a name="p14718164311291"></a>Currently, snapshot is not supported. This parameter is reserved and the default value is <strong id="b1389319112361"><a name="b1389319112361"></a><a name="b1389319112361"></a>-1</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row20579050153611"><td class="cellrowborder" valign="top" width="25.942594259425945%" headers="mcps1.1.5.1.1 "><p id="p56290355153611"><a name="p56290355153611"></a><a name="p56290355153611"></a>snapshots</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.431343134313432%" headers="mcps1.1.5.1.2 "><p id="p63224941153611"><a name="p63224941153611"></a><a name="p63224941153611"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.441544154415443%" headers="mcps1.1.5.1.3 "><p id="p20946624153611"><a name="p20946624153611"></a><a name="p20946624153611"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.18451845184518%" headers="mcps1.1.5.1.4 "><p id="p48840770141254"><a name="p48840770141254"></a><a name="p48840770141254"></a>Specifies the number of snapshots allowed for each tenant. If the value is <strong id="b0418141614368"><a name="b0418141614368"></a><a name="b0418141614368"></a>-1</strong>, there is no quota limit.</p>
    <div class="notice" id="note158671348161917"><a name="note158671348161917"></a><a name="note158671348161917"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p27129783102229"><a name="p27129783102229"></a><a name="p27129783102229"></a>Currently, snapshot is not supported. This parameter is reserved and the default value is <strong id="b1456811903620"><a name="b1456811903620"></a><a name="b1456811903620"></a>-1</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row36376940153611"><td class="cellrowborder" valign="top" width="25.942594259425945%" headers="mcps1.1.5.1.1 "><p id="p60851010153611"><a name="p60851010153611"></a><a name="p60851010153611"></a>shares</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.431343134313432%" headers="mcps1.1.5.1.2 "><p id="p29984814153611"><a name="p29984814153611"></a><a name="p29984814153611"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.441544154415443%" headers="mcps1.1.5.1.3 "><p id="p12850837153611"><a name="p12850837153611"></a><a name="p12850837153611"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.18451845184518%" headers="mcps1.1.5.1.4 "><p id="p201648414136"><a name="p201648414136"></a><a name="p201648414136"></a>Specifies the number of shared file systems allowed for each tenant. If the value is <strong id="b1014212118427"><a name="b1014212118427"></a><a name="b1014212118427"></a>-1</strong>, there is no quota limit.</p>
    </td>
    </tr>
    <tr id="row19857148511"><td class="cellrowborder" valign="top" width="25.942594259425945%" headers="mcps1.1.5.1.1 "><p id="p138591348215"><a name="p138591348215"></a><a name="p138591348215"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.431343134313432%" headers="mcps1.1.5.1.2 "><p id="p3859154819113"><a name="p3859154819113"></a><a name="p3859154819113"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.441544154415443%" headers="mcps1.1.5.1.3 "><p id="p3859164814113"><a name="p3859164814113"></a><a name="p3859164814113"></a>sting</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.18451845184518%" headers="mcps1.1.5.1.4 "><p id="p1185911481811"><a name="p1185911481811"></a><a name="p1185911481811"></a>Specifies the ID of the tenant whose quota is to be queried.</p>
    <div class="notice" id="note1548313412211"><a name="note1548313412211"></a><a name="note1548313412211"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p164853411218"><a name="p164853411218"></a><a name="p164853411218"></a>The ID of the tenant to be queried is displayed only when the version of python-manilaclient is 1.12.0 or later.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row40128625153611"><td class="cellrowborder" valign="top" width="25.942594259425945%" headers="mcps1.1.5.1.1 "><p id="p29193167153611"><a name="p29193167153611"></a><a name="p29193167153611"></a>share_networks</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.431343134313432%" headers="mcps1.1.5.1.2 "><p id="p15836293153611"><a name="p15836293153611"></a><a name="p15836293153611"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.441544154415443%" headers="mcps1.1.5.1.3 "><p id="p7671356153611"><a name="p7671356153611"></a><a name="p7671356153611"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.18451845184518%" headers="mcps1.1.5.1.4 "><p id="p21308240141321"><a name="p21308240141321"></a><a name="p21308240141321"></a>Specifies the number of share networks for each tenant. If the value is <strong id="b20472289420"><a name="b20472289420"></a><a name="b20472289420"></a>-1</strong>, there is no quota limit.</p>
    <div class="notice" id="note186291919112618"><a name="note186291919112618"></a><a name="note186291919112618"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p1763071952616"><a name="p1763071952616"></a><a name="p1763071952616"></a>Currently, share networks cannot be configured. This parameter is reserved and the default value is <strong id="b123961524315"><a name="b123961524315"></a><a name="b123961524315"></a>10</strong>.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    +--------------------+----------------------------------+
    | Property           | Value                            |
    +--------------------+----------------------------------+
    | gigabytes          | 31200                            |
    | snapshots          | -1                               |
    | snapshot_gigabytes | -1                               |
    | shares             | 3                                | 
    | id                 | 703fdd5a62c84cbfb1385c212881f695 |
    | share_networks     | 10                               |
    +--------------------+----------------------------------+
    ```

    >![](/images/icon-notice.gif) **NOTICE:**   
    >The ID is displayed only when the version of python-manilaclient is 1.12.0 or later.  


