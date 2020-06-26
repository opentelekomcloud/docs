# Stopping a Service<a name="EN-US_TOPIC_0220024734"></a>

## Function <a name="en-us_topic_0125376207_section1772474704712"></a>

This API is used to stop a specified service.

## URI<a name="en-us_topic_0125376207_sb9bf8e16ff894d989c1ce75073e203ab"></a>

-   Format

POST /web/v1/maintain/cluster/\{cluster\_id\}/service/\{service\_name\}/stop

-   URI parameter description

<a name="en-us_topic_0125376207_en-us_topic_0110839919_table22964363"></a>
<table><thead align="left"><tr id="en-us_topic_0125376207_en-us_topic_0110839919_row31097035"><th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.1"><p id="en-us_topic_0125376207_en-us_topic_0110839919_p35831867"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p35831867"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p35831867"></a><strong id="en-us_topic_0125376207_b162774213314533_1"><a name="en-us_topic_0125376207_b162774213314533_1"></a><a name="en-us_topic_0125376207_b162774213314533_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.2"><p id="en-us_topic_0125376207_en-us_topic_0110839919_p16700087"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p16700087"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p16700087"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="49.08%" id="mcps1.1.4.1.3"><p id="en-us_topic_0125376207_en-us_topic_0110839919_p45230279"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p45230279"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p45230279"></a><strong id="en-us_topic_0125376207_b842352706134712"><a name="en-us_topic_0125376207_b842352706134712"></a><a name="en-us_topic_0125376207_b842352706134712"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376207_en-us_topic_0110839919_row39773978"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p466794"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p466794"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p466794"></a>service_name</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p37810334"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p37810334"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p37810334"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p41806332"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p41806332"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p41806332"></a>Name of the service to be stopped</p>
</td>
</tr>
<tr id="en-us_topic_0125376207_en-us_topic_0110839919_row40712668"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p9391796"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p9391796"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p9391796"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p22537988"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p22537988"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p22537988"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p36147099"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p36147099"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p36147099"></a>Cluster ID that is displayed on MRS Manager. The default cluster ID is <strong id="en-us_topic_0125376207_b842352706152828"><a name="en-us_topic_0125376207_b842352706152828"></a><a name="en-us_topic_0125376207_b842352706152828"></a>1</strong>, because MRS Manager supports management of only one cluster currently.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0125376207_s8a44ad9620a7423ab7add53ac804f9bf"></a>

-   Example:

    ```
    POST /web/v1/maintain/cluster/{cluster_id}/service/{service_name}/stop HTTP/1.1
    Host: example.com
    Content-Type: application/json
    Accept:application/json
    {
      "user_password": "string",
      "only_self": true
    }
    ```

-   Request parameter description

**Table  1**  Request parameter description

<a name="en-us_topic_0125376207_en-us_topic_0110839919_table52586183"></a>
<table><thead align="left"><tr id="en-us_topic_0125376207_en-us_topic_0110839919_row61378506"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376207_en-us_topic_0110839919_p5603129"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p5603129"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p5603129"></a><strong id="en-us_topic_0125376207_b815201919"><a name="en-us_topic_0125376207_b815201919"></a><a name="en-us_topic_0125376207_b815201919"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376207_en-us_topic_0110839919_p51200337"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p51200337"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p51200337"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376207_en-us_topic_0110839919_p53586617"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p53586617"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p53586617"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376207_en-us_topic_0110839919_p9233635"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p9233635"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p9233635"></a><strong id="en-us_topic_0125376207_b1095689397"><a name="en-us_topic_0125376207_b1095689397"></a><a name="en-us_topic_0125376207_b1095689397"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376207_en-us_topic_0110839919_row9727005"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p49689968"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p49689968"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p49689968"></a>user_password</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p65464451"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p65464451"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p65464451"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p1020286"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p1020286"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p1020286"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376207_p421610270133"><a name="en-us_topic_0125376207_p421610270133"></a><a name="en-us_topic_0125376207_p421610270133"></a>Password of the login user. This parameter is used for secondary authentication. If you call REST APIs, secondary authentication is not required and you do not need to set this parameter.</p>
</td>
</tr>
<tr id="en-us_topic_0125376207_en-us_topic_0110839919_row43670673"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p47663658"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p47663658"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p47663658"></a>only_self</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p35551095"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p35551095"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p35551095"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p61066465"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p61066465"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p61066465"></a>BOOLEAN</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376207_p1474655510588"><a name="en-us_topic_0125376207_p1474655510588"></a><a name="en-us_topic_0125376207_p1474655510588"></a>Whether to operate only the specified service</p>
<p id="en-us_topic_0125376207_p17465557584"><a name="en-us_topic_0125376207_p17465557584"></a><a name="en-us_topic_0125376207_p17465557584"></a><strong id="en-us_topic_0125376207_b842352706204759"><a name="en-us_topic_0125376207_b842352706204759"></a><a name="en-us_topic_0125376207_b842352706204759"></a>false</strong>: The services depending on the service are also stopped.</p>
<p id="en-us_topic_0125376207_p27461755165812"><a name="en-us_topic_0125376207_p27461755165812"></a><a name="en-us_topic_0125376207_p27461755165812"></a><strong id="en-us_topic_0125376207_b842352706204833"><a name="en-us_topic_0125376207_b842352706204833"></a><a name="en-us_topic_0125376207_b842352706204833"></a>true</strong>: Only the specified service is stopped.</p>
<p id="en-us_topic_0125376207_p17466554586"><a name="en-us_topic_0125376207_p17466554586"></a><a name="en-us_topic_0125376207_p17466554586"></a>If you call REST APIs, secondary authentication is not required and you do not need to set this parameter.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0125376207_s88d2bea3977f4f49bdbed2e0102dce7f"></a>

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
      "total_progress": 0
    }
    ```

-   Response parameter description

<a name="en-us_topic_0125376207_en-us_topic_0110839919_table47159308"></a>
<table><thead align="left"><tr id="en-us_topic_0125376207_en-us_topic_0110839919_row24324526"><th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.1"><p id="en-us_topic_0125376207_en-us_topic_0110839919_p24129567"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p24129567"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p24129567"></a><strong id="en-us_topic_0125376207_b686132343"><a name="en-us_topic_0125376207_b686132343"></a><a name="en-us_topic_0125376207_b686132343"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.2"><p id="en-us_topic_0125376207_en-us_topic_0110839919_p8337942"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p8337942"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p8337942"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="49.08%" id="mcps1.1.4.1.3"><p id="en-us_topic_0125376207_en-us_topic_0110839919_p42731707"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p42731707"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p42731707"></a><strong id="en-us_topic_0125376207_b1607995288"><a name="en-us_topic_0125376207_b1607995288"></a><a name="en-us_topic_0125376207_b1607995288"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376207_en-us_topic_0110839919_row38716256"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p49009017"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p49009017"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p49009017"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p10307439"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p10307439"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p10307439"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p61915010"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p61915010"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p61915010"></a>Asynchronous task ID (meaningless in other scenarios). The default value is <strong id="en-us_topic_0125376207_b842352706191850"><a name="en-us_topic_0125376207_b842352706191850"></a><a name="en-us_topic_0125376207_b842352706191850"></a>-1</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0125376207_en-us_topic_0110839919_row20364184"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p38886230"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p38886230"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p38886230"></a>state</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p62776900"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p62776900"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p62776900"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p34139205"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p34139205"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p34139205"></a>Cluster status. The value <strong id="en-us_topic_0125376207_b842352706191926"><a name="en-us_topic_0125376207_b842352706191926"></a><a name="en-us_topic_0125376207_b842352706191926"></a>FAILED</strong> indicates that the command fails to be executed. The value <strong id="en-us_topic_0125376207_b842352706191940"><a name="en-us_topic_0125376207_b842352706191940"></a><a name="en-us_topic_0125376207_b842352706191940"></a>COMPLETE</strong> indicates that the command is successfully executed. The value <strong id="en-us_topic_0125376207_b1512215825111"><a name="en-us_topic_0125376207_b1512215825111"></a><a name="en-us_topic_0125376207_b1512215825111"></a>IN_PROGRESS</strong> indicates that the command is being executed.</p>
</td>
</tr>
<tr id="en-us_topic_0125376207_en-us_topic_0110839919_row38817391"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p57201005"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p57201005"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p57201005"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p2769839"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p2769839"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p2769839"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p366853"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p366853"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p366853"></a>Error code returned</p>
</td>
</tr>
<tr id="en-us_topic_0125376207_en-us_topic_0110839919_row3301680"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p66109542"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p66109542"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p66109542"></a>error_description</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p53272692"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p53272692"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p53272692"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p44975555"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p44975555"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p44975555"></a>Error code description</p>
</td>
</tr>
<tr id="en-us_topic_0125376207_en-us_topic_0110839919_row2126816"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p38054408"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p38054408"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p38054408"></a>total_progress</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p62508221"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p62508221"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p62508221"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376207_en-us_topic_0110839919_p37634732"><a name="en-us_topic_0125376207_en-us_topic_0110839919_p37634732"></a><a name="en-us_topic_0125376207_en-us_topic_0110839919_p37634732"></a>Total progress</p>
</td>
</tr>
</tbody>
</table>

## Status Code<a name="en-us_topic_0125376207_section2092982712508"></a>

<a name="en-us_topic_0125376207_table2979011121511"></a>
<table><thead align="left"><tr id="en-us_topic_0125376207_row3981161161515"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.3.1.1"><p id="en-us_topic_0125376207_p398115116158"><a name="en-us_topic_0125376207_p398115116158"></a><a name="en-us_topic_0125376207_p398115116158"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83%" id="mcps1.1.3.1.2"><p id="en-us_topic_0125376207_p1798121191515"><a name="en-us_topic_0125376207_p1798121191515"></a><a name="en-us_topic_0125376207_p1798121191515"></a>Description </p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376207_row69813112155"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0125376207_p15667142018546"><a name="en-us_topic_0125376207_p15667142018546"></a><a name="en-us_topic_0125376207_p15667142018546"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0125376207_p23378286542"><a name="en-us_topic_0125376207_p23378286542"></a><a name="en-us_topic_0125376207_p23378286542"></a>The operation is successful.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

