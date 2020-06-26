# Querying the Health Status of a Specified Cluster<a name="EN-US_TOPIC_0220024728"></a>

## Function<a name="en-us_topic_0125376271_section1095111617176"></a>

This API is used to query the health status of a specified cluster. If any component is unavailable, the abnormal cluster health status is returned.

## URI<a name="en-us_topic_0125376271_sa3d698e673b8473abff8e652e459e452"></a>

-   Format

GET /web/v1/cluster/\{cluster\_id\}/status

-   Parameter description

<a name="en-us_topic_0125376271_en-us_topic_0110839913_table18439633"></a>
<table><thead align="left"><tr id="en-us_topic_0125376271_en-us_topic_0110839913_row33864059"><th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.1"><p id="en-us_topic_0125376271_en-us_topic_0110839913_p58634288"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p58634288"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p58634288"></a><strong id="en-us_topic_0125376271_b162774213314533_1"><a name="en-us_topic_0125376271_b162774213314533_1"></a><a name="en-us_topic_0125376271_b162774213314533_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.2"><p id="en-us_topic_0125376271_en-us_topic_0110839913_p51756910"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p51756910"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p51756910"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="49.08%" id="mcps1.1.4.1.3"><p id="en-us_topic_0125376271_en-us_topic_0110839913_p43854424"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p43854424"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p43854424"></a><strong id="en-us_topic_0125376271_b842352706134712"><a name="en-us_topic_0125376271_b842352706134712"></a><a name="en-us_topic_0125376271_b842352706134712"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376271_en-us_topic_0110839913_row62547480"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p33181137"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p33181137"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p33181137"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p3317546"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p3317546"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p3317546"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p3292018"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p3292018"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p3292018"></a>Cluster ID that is displayed on MRS Manager. The default cluster ID is <strong id="en-us_topic_0125376271_b842352706152828"><a name="en-us_topic_0125376271_b842352706152828"></a><a name="en-us_topic_0125376271_b842352706152828"></a>1</strong>, because MRS Manager supports management of only one cluster currently.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0125376271_sf0cd952c6bd6463fa25bee292cda2f7d"></a>

-   Example:

    ```
    GET /web/v1/cluster/{cluster_id}/status HTTP/1.1
    Host: example.com
    Content-Type: application/json
    Accept:application/json
    ```

-   Parameter description

    None


## Response<a name="en-us_topic_0125376271_section8372686259"></a>

-   Example:

    ```
    HTTP/1.1 200 OK
    Data:Wed,02 May 2018 10:10:01 GMT
    Server: example-server
    Content-Type: application/json
    {
      "id": 0,
      "state": "COMPLETE",
      "error_code": 0,
      "error_description": "string",
      "total_progress": 0,
      "res_obj": {
        "state": "GOOD"
      }
    }
    ```


-   Parameter description

**Table  1**  Response parameter description

<a name="en-us_topic_0125376271_en-us_topic_0110839913_table1075086"></a>
<table><thead align="left"><tr id="en-us_topic_0125376271_en-us_topic_0110839913_row9697883"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376271_en-us_topic_0110839913_p47331035"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p47331035"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p47331035"></a><strong id="en-us_topic_0125376271_b162774213314533_1_1"><a name="en-us_topic_0125376271_b162774213314533_1_1"></a><a name="en-us_topic_0125376271_b162774213314533_1_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376271_en-us_topic_0110839913_p8608636"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p8608636"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p8608636"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376271_en-us_topic_0110839913_p26210917"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p26210917"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p26210917"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376271_en-us_topic_0110839913_p37967333"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p37967333"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p37967333"></a><strong id="en-us_topic_0125376271_b842352706134712_1"><a name="en-us_topic_0125376271_b842352706134712_1"></a><a name="en-us_topic_0125376271_b842352706134712_1"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376271_en-us_topic_0110839913_row55455104"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p62678444"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p62678444"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p62678444"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p43789200"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p43789200"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p43789200"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p57264341"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p57264341"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p57264341"></a>LONG</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p24297719"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p24297719"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p24297719"></a>Asynchronous task ID (meaningless in other scenarios). The default value is <strong id="en-us_topic_0125376271_b842352706191850"><a name="en-us_topic_0125376271_b842352706191850"></a><a name="en-us_topic_0125376271_b842352706191850"></a>-1</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0125376271_en-us_topic_0110839913_row17352883"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p63406273"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p63406273"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p63406273"></a>state</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p35634492"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p35634492"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p35634492"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p712715"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p712715"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p712715"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p20028947"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p20028947"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p20028947"></a>Cluster status. The value <strong id="en-us_topic_0125376271_b842352706191926"><a name="en-us_topic_0125376271_b842352706191926"></a><a name="en-us_topic_0125376271_b842352706191926"></a>FAILED</strong>&nbsp;indicates that the command fails to be executed. The value&nbsp;<strong id="en-us_topic_0125376271_b842352706191940"><a name="en-us_topic_0125376271_b842352706191940"></a><a name="en-us_topic_0125376271_b842352706191940"></a>COMPLETE</strong> indicates that the command is successfully executed.</p>
</td>
</tr>
<tr id="en-us_topic_0125376271_en-us_topic_0110839913_row46042798"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p38479195"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p38479195"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p38479195"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p29807080"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p29807080"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p29807080"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p65563261"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p65563261"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p65563261"></a>INTEGER</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p16049536"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p16049536"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p16049536"></a>Error code returned</p>
</td>
</tr>
<tr id="en-us_topic_0125376271_en-us_topic_0110839913_row10228104"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p23170058"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p23170058"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p23170058"></a>error_description</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p64835425"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p64835425"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p64835425"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p17178101"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p17178101"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p17178101"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p60234923"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p60234923"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p60234923"></a>Error code description</p>
</td>
</tr>
<tr id="en-us_topic_0125376271_en-us_topic_0110839913_row5243399"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p22062154"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p22062154"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p22062154"></a>total_progress</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p42204021"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p42204021"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p42204021"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p63082545"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p63082545"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p63082545"></a>FLOAT</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p15374808"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p15374808"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p15374808"></a>Total progress</p>
</td>
</tr>
<tr id="en-us_topic_0125376271_en-us_topic_0110839913_row4155545"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p1054870"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p1054870"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p1054870"></a>res_obj</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p18335664"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p18335664"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p18335664"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p8793806"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p8793806"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p8793806"></a>REFERENCE</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p44201211"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p44201211"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p44201211"></a>Response object</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **res\_obj**  parameter description

<a name="en-us_topic_0125376271_en-us_topic_0110839913_table23528308"></a>
<table><thead align="left"><tr id="en-us_topic_0125376271_en-us_topic_0110839913_row52992545"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376271_en-us_topic_0110839913_p64537776"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p64537776"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p64537776"></a><strong id="en-us_topic_0125376271_b162774213314533_1_2"><a name="en-us_topic_0125376271_b162774213314533_1_2"></a><a name="en-us_topic_0125376271_b162774213314533_1_2"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376271_en-us_topic_0110839913_p60177363"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p60177363"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p60177363"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376271_en-us_topic_0110839913_p42528243"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p42528243"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p42528243"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376271_en-us_topic_0110839913_p60468685"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p60468685"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p60468685"></a><strong id="en-us_topic_0125376271_b842352706134712_2"><a name="en-us_topic_0125376271_b842352706134712_2"></a><a name="en-us_topic_0125376271_b842352706134712_2"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376271_en-us_topic_0110839913_row66125294"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p54548629"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p54548629"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p54548629"></a>state</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p56362791"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p56362791"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p56362791"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p1983374"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p1983374"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p1983374"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376271_en-us_topic_0110839913_p56146472"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p56146472"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p56146472"></a>Cluster health status</p>
<p id="en-us_topic_0125376271_en-us_topic_0110839913_p35556202"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p35556202"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p35556202"></a><strong id="en-us_topic_0125376271_b842352706193848"><a name="en-us_topic_0125376271_b842352706193848"></a><a name="en-us_topic_0125376271_b842352706193848"></a>Good</strong>: The cluster is healthy.</p>
<p id="en-us_topic_0125376271_en-us_topic_0110839913_p51570366"><a name="en-us_topic_0125376271_en-us_topic_0110839913_p51570366"></a><a name="en-us_topic_0125376271_en-us_topic_0110839913_p51570366"></a><strong id="en-us_topic_0125376271_b842352706194221"><a name="en-us_topic_0125376271_b842352706194221"></a><a name="en-us_topic_0125376271_b842352706194221"></a>Bad</strong>: The cluster is unhealthy.</p>
</td>
</tr>
</tbody>
</table>

## Status Code<a name="en-us_topic_0125376271_section2092982712508"></a>

<a name="en-us_topic_0125376271_table2979011121511"></a>
<table><thead align="left"><tr id="en-us_topic_0125376271_row3981161161515"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.3.1.1"><p id="en-us_topic_0125376271_p398115116158"><a name="en-us_topic_0125376271_p398115116158"></a><a name="en-us_topic_0125376271_p398115116158"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83%" id="mcps1.1.3.1.2"><p id="en-us_topic_0125376271_p1798121191515"><a name="en-us_topic_0125376271_p1798121191515"></a><a name="en-us_topic_0125376271_p1798121191515"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376271_row69813112155"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0125376271_p15667142018546"><a name="en-us_topic_0125376271_p15667142018546"></a><a name="en-us_topic_0125376271_p15667142018546"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0125376271_p23378286542"><a name="en-us_topic_0125376271_p23378286542"></a><a name="en-us_topic_0125376271_p23378286542"></a>The operation is successful.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

