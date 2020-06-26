# Querying Summary of a Specified Service<a name="EN-US_TOPIC_0220024736"></a>

## Function<a name="en-us_topic_0125376218_section1693516137279"></a>

This API is used to query summary of a specified service in a cluster.

## URI<a name="en-us_topic_0125376218_s09ba7354a86545728a5453aab70db875"></a>

-   Format

GET /web/v1/cluster/\{cluster\_id\}/services/\{service\_name\}

-   URI parameter description

<a name="en-us_topic_0125376218_en-us_topic_0110839921_table62265016"></a>
<table><thead align="left"><tr id="en-us_topic_0125376218_en-us_topic_0110839921_row65147869"><th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.1"><p id="en-us_topic_0125376218_en-us_topic_0110839921_p42486052"><a name="en-us_topic_0125376218_en-us_topic_0110839921_p42486052"></a><a name="en-us_topic_0125376218_en-us_topic_0110839921_p42486052"></a><strong id="en-us_topic_0125376218_b162774213314533_1"><a name="en-us_topic_0125376218_b162774213314533_1"></a><a name="en-us_topic_0125376218_b162774213314533_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.2"><p id="en-us_topic_0125376218_en-us_topic_0110839921_p18818216"><a name="en-us_topic_0125376218_en-us_topic_0110839921_p18818216"></a><a name="en-us_topic_0125376218_en-us_topic_0110839921_p18818216"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="49.08%" id="mcps1.1.4.1.3"><p id="en-us_topic_0125376218_en-us_topic_0110839921_p8067764"><a name="en-us_topic_0125376218_en-us_topic_0110839921_p8067764"></a><a name="en-us_topic_0125376218_en-us_topic_0110839921_p8067764"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376218_en-us_topic_0110839921_row49509118"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376218_en-us_topic_0110839921_p50815604"><a name="en-us_topic_0125376218_en-us_topic_0110839921_p50815604"></a><a name="en-us_topic_0125376218_en-us_topic_0110839921_p50815604"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376218_en-us_topic_0110839921_p22423296"><a name="en-us_topic_0125376218_en-us_topic_0110839921_p22423296"></a><a name="en-us_topic_0125376218_en-us_topic_0110839921_p22423296"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376218_en-us_topic_0110839921_p31441817"><a name="en-us_topic_0125376218_en-us_topic_0110839921_p31441817"></a><a name="en-us_topic_0125376218_en-us_topic_0110839921_p31441817"></a>Cluster ID that is displayed on MRS Manager. The default cluster ID is <strong id="en-us_topic_0125376218_b842352706152828"><a name="en-us_topic_0125376218_b842352706152828"></a><a name="en-us_topic_0125376218_b842352706152828"></a>1</strong>, because MRS Manager supports management of only one cluster currently.</p>
</td>
</tr>
<tr id="en-us_topic_0125376218_en-us_topic_0110839921_row14540903"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376218_en-us_topic_0110839921_p36962494"><a name="en-us_topic_0125376218_en-us_topic_0110839921_p36962494"></a><a name="en-us_topic_0125376218_en-us_topic_0110839921_p36962494"></a>service_name</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376218_en-us_topic_0110839921_p41172029"><a name="en-us_topic_0125376218_en-us_topic_0110839921_p41172029"></a><a name="en-us_topic_0125376218_en-us_topic_0110839921_p41172029"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376218_p42313610163"><a name="en-us_topic_0125376218_p42313610163"></a><a name="en-us_topic_0125376218_p42313610163"></a>Name of the service to be queried.</p>
<p id="en-us_topic_0125376218_p8148103217165"><a name="en-us_topic_0125376218_p8148103217165"></a><a name="en-us_topic_0125376218_p8148103217165"></a>For example, the service name is HBase, HDFS, or Spark.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0125376218_s4ef085a1c7a74029bfce22258f6077a6"></a>

-   Example:

    ```
    GET /web/v1/cluster/{cluster_id}/services/{service_name} HTTP/1.1
    Host: example.com
    Content-Type: application/json
    Accept:application/json
    ```

-   Parameter description

    None


## Response<a name="en-us_topic_0125376218_section1560865371016"></a>

-   Example:

    ```
    HTTP/1.1 200 OK  
    Data:Wed,02 May 2018 10:10:01 GMT  
    Server: example-server  
    Content-Type: application/json  {
      "id": 0,
      "state": "NEW",
      "error_code": 0,
      "error_description": "string",
      "total_progress": 0,
      "res_obj": {
        "key_property": [
          {
            "name": "string",
            "value": {},
            "type": "TEXT"
          }
        ]
      }
    }
    ```


-   Parameter description

    **Table  1**  Response parameter description

    <a name="en-us_topic_0125376218_table080914831515"></a>
    <table><thead align="left"><tr id="en-us_topic_0125376218_row16990164820154"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376218_p9990104813151"><a name="en-us_topic_0125376218_p9990104813151"></a><a name="en-us_topic_0125376218_p9990104813151"></a><strong id="en-us_topic_0125376218_b162774213314533_1_1"><a name="en-us_topic_0125376218_b162774213314533_1_1"></a><a name="en-us_topic_0125376218_b162774213314533_1_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376218_p5990154810159"><a name="en-us_topic_0125376218_p5990154810159"></a><a name="en-us_topic_0125376218_p5990154810159"></a>Mandatory or Not</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376218_p14990104816150"><a name="en-us_topic_0125376218_p14990104816150"></a><a name="en-us_topic_0125376218_p14990104816150"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.39393939393939%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376218_p14990184841510"><a name="en-us_topic_0125376218_p14990184841510"></a><a name="en-us_topic_0125376218_p14990184841510"></a><strong id="en-us_topic_0125376218_b842352706134712"><a name="en-us_topic_0125376218_b842352706134712"></a><a name="en-us_topic_0125376218_b842352706134712"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0125376218_row89901048141515"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376218_p4990164891515"><a name="en-us_topic_0125376218_p4990164891515"></a><a name="en-us_topic_0125376218_p4990164891515"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376218_p59901148141513"><a name="en-us_topic_0125376218_p59901148141513"></a><a name="en-us_topic_0125376218_p59901148141513"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376218_p6990048171511"><a name="en-us_topic_0125376218_p6990048171511"></a><a name="en-us_topic_0125376218_p6990048171511"></a>LONG</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376218_p109901748181518"><a name="en-us_topic_0125376218_p109901748181518"></a><a name="en-us_topic_0125376218_p109901748181518"></a>Asynchronous task ID (meaningless in other scenarios). The default value is <strong id="en-us_topic_0125376218_b842352706191850"><a name="en-us_topic_0125376218_b842352706191850"></a><a name="en-us_topic_0125376218_b842352706191850"></a>-1</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0125376218_row20992184810159"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376218_p599218481159"><a name="en-us_topic_0125376218_p599218481159"></a><a name="en-us_topic_0125376218_p599218481159"></a>state</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376218_p69921948161512"><a name="en-us_topic_0125376218_p69921948161512"></a><a name="en-us_topic_0125376218_p69921948161512"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376218_p1899254881516"><a name="en-us_topic_0125376218_p1899254881516"></a><a name="en-us_topic_0125376218_p1899254881516"></a>STRING</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376218_p19992548191515"><a name="en-us_topic_0125376218_p19992548191515"></a><a name="en-us_topic_0125376218_p19992548191515"></a>Cluster status. The value <strong id="en-us_topic_0125376218_b842352706191926"><a name="en-us_topic_0125376218_b842352706191926"></a><a name="en-us_topic_0125376218_b842352706191926"></a>FAILED</strong>&nbsp;indicates that the command fails to be executed. The value&nbsp;<strong id="en-us_topic_0125376218_b842352706191940"><a name="en-us_topic_0125376218_b842352706191940"></a><a name="en-us_topic_0125376218_b842352706191940"></a>COMPLETE</strong> indicates that the command is successfully executed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0125376218_row1399274871510"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376218_p1799214812151"><a name="en-us_topic_0125376218_p1799214812151"></a><a name="en-us_topic_0125376218_p1799214812151"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376218_p6992048151514"><a name="en-us_topic_0125376218_p6992048151514"></a><a name="en-us_topic_0125376218_p6992048151514"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376218_p1299274812153"><a name="en-us_topic_0125376218_p1299274812153"></a><a name="en-us_topic_0125376218_p1299274812153"></a>INTEGER</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376218_p1599244817151"><a name="en-us_topic_0125376218_p1599244817151"></a><a name="en-us_topic_0125376218_p1599244817151"></a>Error code returned</p>
    </td>
    </tr>
    <tr id="en-us_topic_0125376218_row1999219482159"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376218_p18992134891515"><a name="en-us_topic_0125376218_p18992134891515"></a><a name="en-us_topic_0125376218_p18992134891515"></a>error_description</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376218_p1599224820152"><a name="en-us_topic_0125376218_p1599224820152"></a><a name="en-us_topic_0125376218_p1599224820152"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376218_p1199217485150"><a name="en-us_topic_0125376218_p1199217485150"></a><a name="en-us_topic_0125376218_p1199217485150"></a>STRING</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376218_p209927489157"><a name="en-us_topic_0125376218_p209927489157"></a><a name="en-us_topic_0125376218_p209927489157"></a>Error code description</p>
    </td>
    </tr>
    <tr id="en-us_topic_0125376218_row15992174861515"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376218_p1399216480154"><a name="en-us_topic_0125376218_p1399216480154"></a><a name="en-us_topic_0125376218_p1399216480154"></a>total_progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376218_p17992848121518"><a name="en-us_topic_0125376218_p17992848121518"></a><a name="en-us_topic_0125376218_p17992848121518"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376218_p899284811154"><a name="en-us_topic_0125376218_p899284811154"></a><a name="en-us_topic_0125376218_p899284811154"></a>FLOAT</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376218_p8992124815159"><a name="en-us_topic_0125376218_p8992124815159"></a><a name="en-us_topic_0125376218_p8992124815159"></a>Total progress</p>
    </td>
    </tr>
    <tr id="en-us_topic_0125376218_row999284814154"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376218_p099284819153"><a name="en-us_topic_0125376218_p099284819153"></a><a name="en-us_topic_0125376218_p099284819153"></a>res_obj</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376218_p59921048161514"><a name="en-us_topic_0125376218_p59921048161514"></a><a name="en-us_topic_0125376218_p59921048161514"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376218_p1899217481159"><a name="en-us_topic_0125376218_p1899217481159"></a><a name="en-us_topic_0125376218_p1899217481159"></a>REFERENCE</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376218_p149921248181515"><a name="en-us_topic_0125376218_p149921248181515"></a><a name="en-us_topic_0125376218_p149921248181515"></a>Response object</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **res\_obj**  parameter description

    <a name="en-us_topic_0125376218_table1921172819173"></a>
    <table><thead align="left"><tr id="en-us_topic_0125376218_row3211528121717"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376218_p18166543141714"><a name="en-us_topic_0125376218_p18166543141714"></a><a name="en-us_topic_0125376218_p18166543141714"></a><strong id="en-us_topic_0125376218_b162774213314533_1_2"><a name="en-us_topic_0125376218_b162774213314533_1_2"></a><a name="en-us_topic_0125376218_b162774213314533_1_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376218_p19170154316177"><a name="en-us_topic_0125376218_p19170154316177"></a><a name="en-us_topic_0125376218_p19170154316177"></a>Mandatory or Not</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376218_p617318434174"><a name="en-us_topic_0125376218_p617318434174"></a><a name="en-us_topic_0125376218_p617318434174"></a><strong>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376218_p121771143131717"><a name="en-us_topic_0125376218_p121771143131717"></a><a name="en-us_topic_0125376218_p121771143131717"></a><strong id="en-us_topic_0125376218_b842352706134712_1"><a name="en-us_topic_0125376218_b842352706134712_1"></a><a name="en-us_topic_0125376218_b842352706134712_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0125376218_row1622528201716"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376218_p1163114151813"><a name="en-us_topic_0125376218_p1163114151813"></a><a name="en-us_topic_0125376218_p1163114151813"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376218_p4635341186"><a name="en-us_topic_0125376218_p4635341186"></a><a name="en-us_topic_0125376218_p4635341186"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376218_p9638846185"><a name="en-us_topic_0125376218_p9638846185"></a><a name="en-us_topic_0125376218_p9638846185"></a>STRING</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376218_p12641124141816"><a name="en-us_topic_0125376218_p12641124141816"></a><a name="en-us_topic_0125376218_p12641124141816"></a>Property name</p>
    </td>
    </tr>
    <tr id="en-us_topic_0125376218_row1722142831712"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376218_p101472103186"><a name="en-us_topic_0125376218_p101472103186"></a><a name="en-us_topic_0125376218_p101472103186"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376218_p11151161061817"><a name="en-us_topic_0125376218_p11151161061817"></a><a name="en-us_topic_0125376218_p11151161061817"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376218_p0157910181815"><a name="en-us_topic_0125376218_p0157910181815"></a><a name="en-us_topic_0125376218_p0157910181815"></a>&lt;T&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376218_p6161151041816"><a name="en-us_topic_0125376218_p6161151041816"></a><a name="en-us_topic_0125376218_p6161151041816"></a>Property value</p>
    </td>
    </tr>
    <tr id="en-us_topic_0125376218_row192282861716"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376218_p9164111014182"><a name="en-us_topic_0125376218_p9164111014182"></a><a name="en-us_topic_0125376218_p9164111014182"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376218_p1716751081817"><a name="en-us_topic_0125376218_p1716751081817"></a><a name="en-us_topic_0125376218_p1716751081817"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376218_p11171410141819"><a name="en-us_topic_0125376218_p11171410141819"></a><a name="en-us_topic_0125376218_p11171410141819"></a>ENUM</p>
    <p id="en-us_topic_0125376218_p1517251016180"><a name="en-us_topic_0125376218_p1517251016180"></a><a name="en-us_topic_0125376218_p1517251016180"></a>&lt;Enumeration&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376218_p617691041817"><a name="en-us_topic_0125376218_p617691041817"></a><a name="en-us_topic_0125376218_p617691041817"></a>Property type</p>
    <p id="en-us_topic_0125376218_p0177141081818"><a name="en-us_topic_0125376218_p0177141081818"></a><a name="en-us_topic_0125376218_p0177141081818"></a>Possible values are:</p>
    <p id="en-us_topic_0125376218_p18178210171810"><a name="en-us_topic_0125376218_p18178210171810"></a><a name="en-us_topic_0125376218_p18178210171810"></a><strong id="en-us_topic_0125376218_b84235270695144"><a name="en-us_topic_0125376218_b84235270695144"></a><a name="en-us_topic_0125376218_b84235270695144"></a>STATUS</strong></p>
    <p id="en-us_topic_0125376218_p918011010186"><a name="en-us_topic_0125376218_p918011010186"></a><a name="en-us_topic_0125376218_p918011010186"></a><strong id="en-us_topic_0125376218_b84235270695147"><a name="en-us_topic_0125376218_b84235270695147"></a><a name="en-us_topic_0125376218_b84235270695147"></a>TEXT</strong></p>
    </td>
    </tr>
    </tbody>
    </table>


## Status Code<a name="en-us_topic_0125376218_section2092982712508"></a>

<a name="en-us_topic_0125376218_table2979011121511"></a>
<table><thead align="left"><tr id="en-us_topic_0125376218_row3981161161515"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.3.1.1"><p id="en-us_topic_0125376218_p398115116158"><a name="en-us_topic_0125376218_p398115116158"></a><a name="en-us_topic_0125376218_p398115116158"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83%" id="mcps1.1.3.1.2"><p id="en-us_topic_0125376218_p1798121191515"><a name="en-us_topic_0125376218_p1798121191515"></a><a name="en-us_topic_0125376218_p1798121191515"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376218_row69813112155"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0125376218_p15667142018546"><a name="en-us_topic_0125376218_p15667142018546"></a><a name="en-us_topic_0125376218_p15667142018546"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0125376218_p23378286542"><a name="en-us_topic_0125376218_p23378286542"></a><a name="en-us_topic_0125376218_p23378286542"></a>The operation is successful.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

