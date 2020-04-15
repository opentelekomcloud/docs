# Checking the Login<a name="EN-US_TOPIC_0220024726"></a>

## Function<a name="en-us_topic_0125376217_section10164165933618"></a>

This API is used to check the login after a login request is submitted.

## URI<a name="en-us_topic_0125376217_s4ba458a90f404e0592cdbfb06cf206ee"></a>

GET /web/v1/access/login\_check

## Request<a name="en-us_topic_0125376217_s047f3728c7ee421a915db3e28ae4d55e"></a>

-   Example:

    ```
    GET /web/v1/access/login_check HTTP/1.1
    Host: example.com
    Content-Type: application/json
    Accept:application/json
    ```

-   Parameter description

    None


## Response<a name="en-us_topic_0125376217_sede0e6eaeae5491f92e940a31873f285"></a>

-   Example:

    ```
    HTTP/1.1 200 OK
    Data:Wed,02 May 2018 10:10:01 GMT
    Server: example-server
    Content-Type: application/json
    {
      "id": 0,
      "state": "NEW",
      "error_code": 0,
      "error_description": "string",
      "total_progress": 0,
      "modify_pwd": true,
      "exist_cluster": true,
      "remind_pwd": true,
      "ref_URL": "string"
      "token": "string"
    }
    ```

-   Response parameter description

<a name="en-us_topic_0125376217_en-us_topic_0110839910_table56762234"></a>
<table><thead align="left"><tr id="en-us_topic_0125376217_en-us_topic_0110839910_row60536997"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.1.5.1.1"><p id="en-us_topic_0125376217_en-us_topic_0110839910_p4549718"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p4549718"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p4549718"></a><strong id="en-us_topic_0125376217_b7617970162543"><a name="en-us_topic_0125376217_b7617970162543"></a><a name="en-us_topic_0125376217_b7617970162543"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.1.5.1.2"><p id="en-us_topic_0125376217_en-us_topic_0110839910_p32982843"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p32982843"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p32982843"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.1.5.1.3"><p id="en-us_topic_0125376217_en-us_topic_0110839910_p54364604"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p54364604"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p54364604"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.1.5.1.4"><p id="en-us_topic_0125376217_en-us_topic_0110839910_p6068860"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p6068860"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p6068860"></a><strong id="en-us_topic_0125376217_b842352706134712"><a name="en-us_topic_0125376217_b842352706134712"></a><a name="en-us_topic_0125376217_b842352706134712"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376217_en-us_topic_0110839910_row21815680"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p22239656"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p22239656"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p22239656"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p56581725"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p56581725"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p56581725"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p19716998"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p19716998"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p19716998"></a>LONG</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p43359308"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p43359308"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p43359308"></a>Asynchronous task ID (meaningless in other scenarios). The default value is <strong id="en-us_topic_0125376217_b842352706191850"><a name="en-us_topic_0125376217_b842352706191850"></a><a name="en-us_topic_0125376217_b842352706191850"></a>-1</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0125376217_en-us_topic_0110839910_row54689460"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p661272"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p661272"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p661272"></a>state</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p53563101"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p53563101"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p53563101"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p43643947"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p43643947"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p43643947"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p32012887"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p32012887"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p32012887"></a>Cluster status. The value <strong id="en-us_topic_0125376217_b842352706191926"><a name="en-us_topic_0125376217_b842352706191926"></a><a name="en-us_topic_0125376217_b842352706191926"></a>FAILED</strong>&nbsp;indicates that the command fails to be executed. The value&nbsp;<strong id="en-us_topic_0125376217_b842352706191940"><a name="en-us_topic_0125376217_b842352706191940"></a><a name="en-us_topic_0125376217_b842352706191940"></a>COMPLETE</strong> indicates that the command is successfully executed.</p>
</td>
</tr>
<tr id="en-us_topic_0125376217_en-us_topic_0110839910_row19680527"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p50618827"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p50618827"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p50618827"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p6484348"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p6484348"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p6484348"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p55470218"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p55470218"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p55470218"></a>INTEGER</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p36441454"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p36441454"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p36441454"></a>Error code returned</p>
</td>
</tr>
<tr id="en-us_topic_0125376217_en-us_topic_0110839910_row59537635"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p57819120"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p57819120"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p57819120"></a>error_description</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p52837125"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p52837125"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p52837125"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p51948747"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p51948747"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p51948747"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p47237200"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p47237200"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p47237200"></a>Error code description</p>
</td>
</tr>
<tr id="en-us_topic_0125376217_en-us_topic_0110839910_row22481618"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p9071785"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p9071785"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p9071785"></a>total_progress</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p63726013"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p63726013"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p63726013"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p61533429"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p61533429"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p61533429"></a>FLOAT</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p43270153"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p43270153"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p43270153"></a>Total progress</p>
</td>
</tr>
<tr id="en-us_topic_0125376217_en-us_topic_0110839910_row53887058"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p2775549"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p2775549"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p2775549"></a>modify_pwd</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p23492921"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p23492921"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p23492921"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p23878445"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p23878445"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p23878445"></a>BOOLEAN</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p34508910"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p34508910"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p34508910"></a>Whether to change the password. The password does not need to be changed by default.</p>
</td>
</tr>
<tr id="en-us_topic_0125376217_en-us_topic_0110839910_row42144734"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p58280312"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p58280312"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p58280312"></a>exist_cluster</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p23084822"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p23084822"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p23084822"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p57931297"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p57931297"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p57931297"></a>BOOLEAN</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p2734428"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p2734428"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p2734428"></a>Whether a cluster exists</p>
</td>
</tr>
<tr id="en-us_topic_0125376217_en-us_topic_0110839910_row24609853"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p47241071"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p47241071"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p47241071"></a>remind_pwd</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p1321529"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p1321529"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p1321529"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p39935044"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p39935044"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p39935044"></a>BOOLEAN</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p8928760"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p8928760"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p8928760"></a>Whether to remind the user to change the password</p>
</td>
</tr>
<tr id="en-us_topic_0125376217_en-us_topic_0110839910_row13249979"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p66615359"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p66615359"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p66615359"></a>ref_URL</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p27134992"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p27134992"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p27134992"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p50450709"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p50450709"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p50450709"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376217_en-us_topic_0110839910_p40687087"><a name="en-us_topic_0125376217_en-us_topic_0110839910_p40687087"></a><a name="en-us_topic_0125376217_en-us_topic_0110839910_p40687087"></a>URL to be redirected</p>
</td>
</tr>
<tr id="en-us_topic_0125376217_row6248447183218"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376217_p62481547133212"><a name="en-us_topic_0125376217_p62481547133212"></a><a name="en-us_topic_0125376217_p62481547133212"></a>token</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376217_p643512415335"><a name="en-us_topic_0125376217_p643512415335"></a><a name="en-us_topic_0125376217_p643512415335"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376217_p1724884717322"><a name="en-us_topic_0125376217_p1724884717322"></a><a name="en-us_topic_0125376217_p1724884717322"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376217_p824816477322"><a name="en-us_topic_0125376217_p824816477322"></a><a name="en-us_topic_0125376217_p824816477322"></a>Token that is responded after login and check</p>
</td>
</tr>
</tbody>
</table>

## Status Code<a name="en-us_topic_0125376217_section2092982712508"></a>

<a name="en-us_topic_0125376217_table2979011121511"></a>
<table><thead align="left"><tr id="en-us_topic_0125376217_row3981161161515"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.3.1.1"><p id="en-us_topic_0125376217_p398115116158"><a name="en-us_topic_0125376217_p398115116158"></a><a name="en-us_topic_0125376217_p398115116158"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83%" id="mcps1.1.3.1.2"><p id="en-us_topic_0125376217_p1798121191515"><a name="en-us_topic_0125376217_p1798121191515"></a><a name="en-us_topic_0125376217_p1798121191515"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376217_row69813112155"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0125376217_p15667142018546"><a name="en-us_topic_0125376217_p15667142018546"></a><a name="en-us_topic_0125376217_p15667142018546"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0125376217_p67110329349"><a name="en-us_topic_0125376217_p67110329349"></a><a name="en-us_topic_0125376217_p67110329349"></a>The operation is successful.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

