# Obtaining an Automated Backup Policy<a name="en-us_topic_0037139085"></a>

## Function<a name="section4850156117316"></a>

This API is used to obtain an automated backup policy information.

## URI<a name="section28961517113719"></a>

-   URI format

    PATH: /rds/v1/\{project\_id\}/instances/\{instanceId\}/backups/policy

    Method: GET

-   Parameter description

    **Table  1**  Parameter description

    <a name="table58427690"></a>
    <table><thead align="left"><tr id="row1482002"><th class="cellrowborder" valign="top" width="21.3%" id="mcps1.2.4.1.1"><p id="p52933326"><a name="p52933326"></a><a name="p52933326"></a><strong id="b842352706102328_1"><a name="b842352706102328_1"></a><a name="b842352706102328_1"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.060000000000002%" id="mcps1.2.4.1.2"><p id="p59740974"><a name="p59740974"></a><a name="p59740974"></a><strong id="b842352706102346_1"><a name="b842352706102346_1"></a><a name="b842352706102346_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.63999999999999%" id="mcps1.2.4.1.3"><p id="p7180698"><a name="p7180698"></a><a name="p7180698"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44765691"><td class="cellrowborder" valign="top" width="21.3%" headers="mcps1.2.4.1.1 "><p id="p2142393"><a name="p2142393"></a><a name="p2142393"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p39316155"><a name="p39316155"></a><a name="p39316155"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p18331498163153"><a name="p18331498163153"></a><a name="p18331498163153"></a>Specifies the project ID of a tenant in a region.</p>
    </td>
    </tr>
    <tr id="row32947160154149"><td class="cellrowborder" valign="top" width="21.3%" headers="mcps1.2.4.1.1 "><p id="p28088991154149"><a name="p28088991154149"></a><a name="p28088991154149"></a>instanceId</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.060000000000002%" headers="mcps1.2.4.1.2 "><p id="p60615762154149"><a name="p60615762154149"></a><a name="p60615762154149"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p7417132564016"><a name="p7417132564016"></a><a name="p7417132564016"></a>Specifies the primary node ID of the DB instance.</p>
    <div class="note" id="note18250133224019"><a name="note18250133224019"></a><a name="note18250133224019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p142501332164011"><a name="p142501332164011"></a><a name="p142501332164011"></a>This field is not the DB instance ID. You are advised to use API v3 and the DB instance ID to perform related operations.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section3074340117316"></a>

None

## Normal Response<a name="section28521534113742"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table11236435"></a>
    <table><thead align="left"><tr id="row61525259"><th class="cellrowborder" valign="top" width="32.58%" id="mcps1.2.4.1.1"><p id="p17490046"><a name="p17490046"></a><a name="p17490046"></a><strong id="b842352706102328_3"><a name="b842352706102328_3"></a><a name="b842352706102328_3"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.089999999999996%" id="mcps1.2.4.1.2"><p id="p63149496"><a name="p63149496"></a><a name="p63149496"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p14835533"><a name="p14835533"></a><a name="p14835533"></a><strong id="b842352706163417_5"><a name="b842352706163417_5"></a><a name="b842352706163417_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60827539"><td class="cellrowborder" valign="top" width="32.58%" headers="mcps1.2.4.1.1 "><p id="p28083633"><a name="p28083633"></a><a name="p28083633"></a>policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.089999999999996%" headers="mcps1.2.4.1.2 "><p id="p42890904"><a name="p42890904"></a><a name="p42890904"></a>Dictionary data structure. For details, see <a href="#table35260043174853">Table 3</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p49586916144357"><a name="p49586916144357"></a><a name="p49586916144357"></a>Indicates the backup policy objects, including the backup retention period (days) and backup start time.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  policy field data structure description

    <a name="table35260043174853"></a>
    <table><thead align="left"><tr id="row29173707174853"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p14260042174853"><a name="p14260042174853"></a><a name="p14260042174853"></a><strong id="b842352706102328_5"><a name="b842352706102328_5"></a><a name="b842352706102328_5"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p10381414174853"><a name="p10381414174853"></a><a name="p10381414174853"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p35588178174853"><a name="p35588178174853"></a><a name="p35588178174853"></a><strong id="b842352706163417_7"><a name="b842352706163417_7"></a><a name="b842352706163417_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64070195174853"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p22303345174853"><a name="p22303345174853"></a><a name="p22303345174853"></a>keepday</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p34927138174853"><a name="p34927138174853"></a><a name="p34927138174853"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p30482871191015"><a name="p30482871191015"></a><a name="p30482871191015"></a>Indicates the number of days to retain the generated backup files.</p>
    <p id="p5563313"><a name="p5563313"></a><a name="p5563313"></a>The value range is from 0 to 732. If this parameter is <strong id="b842352706112422"><a name="b842352706112422"></a><a name="b842352706112422"></a>0</strong>, the automated backup policy is not set. To extend the retention period, contact customer service. Automated backups can be retained for up to 2562 days.</p>
    </td>
    </tr>
    <tr id="row43181693175641"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8056259175641"><a name="p8056259175641"></a><a name="p8056259175641"></a>starttime</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p42443136175641"><a name="p42443136175641"></a><a name="p42443136175641"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p40942168155958"><a name="p40942168155958"></a><a name="p40942168155958"></a>Indicates the backup start time that has been set. The backup task will be triggered within one hour after the backup start time.</p>
    <p id="p57223682"><a name="p57223682"></a><a name="p57223682"></a>Valid value:</p>
    <p id="p23592952151615"><a name="p23592952151615"></a><a name="p23592952151615"></a>The value cannot be empty. The format can be hh:mm:ss or hh:mm and must be valid. The time is in the UTC format.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Response example

    ```
    {
      "policy": {
      "keepday": 7,
      "starttime": "00:00:00"
     }
    }
    ```


## Abnormal Response<a name="section51597550"></a>

For details, see  [Abnormal Request Results](abnormal-request-results.md).

