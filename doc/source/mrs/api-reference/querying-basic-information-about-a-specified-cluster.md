# Querying Basic Information About a Specified Cluster<a name="EN-US_TOPIC_0220024729"></a>

## Function<a name="en-us_topic_0125376248_section237714892916"></a>

This API is used to query basic information about a specified cluster.

## URI<a name="en-us_topic_0125376248_s44fca647018e47b988e6cd2bf27c9f3e"></a>

GET /web/v1/clusters

## Request<a name="en-us_topic_0125376248_s75b3c59ea5b84f32915af2b3ad3e74c8"></a>

-   Example:

    ```
    GET /web/v1/clusters HTTP/1.1
    Host: example.com
    Content-Type: application/json
    Accept:application/json
    ```

-   Parameter description

    None


## Response<a name="en-us_topic_0125376248_s46f04ddfae8243d9afc20c9a3a4ddbca"></a>

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
        "clusters": [
          {
            "stack": "string",
            "id": 0,
            "name": "string",
            "description": "string",
            "version": "string",
            "cluster_state": "string",
            "stack_model": "string",
            "lic_state": "string"
          }
        ]
      }
    }
    ```

-   Parameter description

**Table  1**  Response parameter description

<a name="en-us_topic_0125376248_en-us_topic_0110839914_table26655514"></a>
<table><thead align="left"><tr id="en-us_topic_0125376248_en-us_topic_0110839914_row33519278"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376248_en-us_topic_0110839914_p30706959"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p30706959"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p30706959"></a><strong id="en-us_topic_0125376248_b162774213314533_1"><a name="en-us_topic_0125376248_b162774213314533_1"></a><a name="en-us_topic_0125376248_b162774213314533_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376248_en-us_topic_0110839914_p4235745"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p4235745"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p4235745"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376248_en-us_topic_0110839914_p7551051"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p7551051"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p7551051"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376248_en-us_topic_0110839914_p29745197"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p29745197"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p29745197"></a><strong id="en-us_topic_0125376248_b842352706134712"><a name="en-us_topic_0125376248_b842352706134712"></a><a name="en-us_topic_0125376248_b842352706134712"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376248_en-us_topic_0110839914_row60550794"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p5667271"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p5667271"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p5667271"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p56395788"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p56395788"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p56395788"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p4656130"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p4656130"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p4656130"></a>LONG</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p20658199"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p20658199"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p20658199"></a>Asynchronous task ID (meaningless in other scenarios). The default value is <strong id="en-us_topic_0125376248_b842352706191850"><a name="en-us_topic_0125376248_b842352706191850"></a><a name="en-us_topic_0125376248_b842352706191850"></a>-1</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0125376248_en-us_topic_0110839914_row51706065"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p27441752"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p27441752"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p27441752"></a>state</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p8189468"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p8189468"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p8189468"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p59367172"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p59367172"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p59367172"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p47905403"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p47905403"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p47905403"></a>Cluster status. The value <strong id="en-us_topic_0125376248_b842352706191926"><a name="en-us_topic_0125376248_b842352706191926"></a><a name="en-us_topic_0125376248_b842352706191926"></a>FAILED</strong>&nbsp;indicates that the command fails to be executed. The value&nbsp;<strong id="en-us_topic_0125376248_b842352706191940"><a name="en-us_topic_0125376248_b842352706191940"></a><a name="en-us_topic_0125376248_b842352706191940"></a>COMPLETE</strong> indicates that the command is successfully executed.</p>
</td>
</tr>
<tr id="en-us_topic_0125376248_en-us_topic_0110839914_row28495449"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p26430055"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p26430055"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p26430055"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p60459685"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p60459685"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p60459685"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p65396283"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p65396283"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p65396283"></a>INTEGER</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p62021665"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p62021665"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p62021665"></a>Error code returned</p>
</td>
</tr>
<tr id="en-us_topic_0125376248_en-us_topic_0110839914_row21324079"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p49528827"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p49528827"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p49528827"></a>error_description</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p52412011"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p52412011"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p52412011"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p17514471"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p17514471"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p17514471"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p43196472"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p43196472"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p43196472"></a>Error code description</p>
</td>
</tr>
<tr id="en-us_topic_0125376248_en-us_topic_0110839914_row53223935"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p16171442"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p16171442"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p16171442"></a>total_progress</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p34818463"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p34818463"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p34818463"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p1723244"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p1723244"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p1723244"></a>FLOAT</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p35098661"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p35098661"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p35098661"></a>Total progress</p>
</td>
</tr>
<tr id="en-us_topic_0125376248_en-us_topic_0110839914_row47452501"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p18447404"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p18447404"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p18447404"></a>res_obj</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p17844718"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p17844718"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p17844718"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p36136069"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p36136069"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p36136069"></a>REFERENCE</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p5348574"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p5348574"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p5348574"></a>Response object</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **res\_obj**  parameter description

<a name="en-us_topic_0125376248_en-us_topic_0110839914_table30581384"></a>
<table><thead align="left"><tr id="en-us_topic_0125376248_en-us_topic_0110839914_row8548577"><th class="cellrowborder" valign="top" width="28.71287128712871%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376248_en-us_topic_0110839914_p21346104"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p21346104"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p21346104"></a><strong id="en-us_topic_0125376248_b162774213314533_1_1"><a name="en-us_topic_0125376248_b162774213314533_1_1"></a><a name="en-us_topic_0125376248_b162774213314533_1_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.71287128712871%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376248_en-us_topic_0110839914_p51312884"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p51312884"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p51312884"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376248_en-us_topic_0110839914_p62702973"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p62702973"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p62702973"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="21.782178217821784%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376248_en-us_topic_0110839914_p24554866"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p24554866"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p24554866"></a><strong id="en-us_topic_0125376248_b842352706134712_1"><a name="en-us_topic_0125376248_b842352706134712_1"></a><a name="en-us_topic_0125376248_b842352706134712_1"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376248_en-us_topic_0110839914_row42787133"><td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p43205724"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p43205724"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p43205724"></a>clusters</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p10002744"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p10002744"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p10002744"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p4915896"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p4915896"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p4915896"></a>ARRAY_REFERENCE</p>
</td>
<td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p32915445"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p32915445"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p32915445"></a>Records all installed clusters in arrays.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **clusters**  parameter description

<a name="en-us_topic_0125376248_en-us_topic_0110839914_table48905408"></a>
<table><thead align="left"><tr id="en-us_topic_0125376248_en-us_topic_0110839914_row21673883"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376248_en-us_topic_0110839914_p10754092"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p10754092"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p10754092"></a><strong id="en-us_topic_0125376248_b162774213314533_1_2"><a name="en-us_topic_0125376248_b162774213314533_1_2"></a><a name="en-us_topic_0125376248_b162774213314533_1_2"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376248_en-us_topic_0110839914_p65775089"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p65775089"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p65775089"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376248_en-us_topic_0110839914_p26181970"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p26181970"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p26181970"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376248_en-us_topic_0110839914_p22249650"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p22249650"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p22249650"></a><strong id="en-us_topic_0125376248_b842352706134712_2"><a name="en-us_topic_0125376248_b842352706134712_2"></a><a name="en-us_topic_0125376248_b842352706134712_2"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376248_en-us_topic_0110839914_row57391254"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p18179998"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p18179998"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p18179998"></a>stack</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p63293747"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p63293747"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p63293747"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p26519868"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p26519868"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p26519868"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p11564706"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p11564706"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p11564706"></a>Cluster version information</p>
</td>
</tr>
<tr id="en-us_topic_0125376248_en-us_topic_0110839914_row36973498"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p42063358"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p42063358"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p42063358"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p51688867"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p51688867"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p51688867"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p26048721"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p26048721"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p26048721"></a>INTEGER</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p7745692"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p7745692"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p7745692"></a>Cluster ID</p>
</td>
</tr>
<tr id="en-us_topic_0125376248_en-us_topic_0110839914_row2602367"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p9465178"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p9465178"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p9465178"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p28481929"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p28481929"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p28481929"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p25334901"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p25334901"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p25334901"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p20847922"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p20847922"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p20847922"></a>Cluster name</p>
</td>
</tr>
<tr id="en-us_topic_0125376248_en-us_topic_0110839914_row53413578"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p31532581"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p31532581"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p31532581"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p4002281"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p4002281"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p4002281"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p55749308"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p55749308"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p55749308"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p45895083"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p45895083"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p45895083"></a>Cluster description</p>
</td>
</tr>
<tr id="en-us_topic_0125376248_en-us_topic_0110839914_row10402569"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p37301726"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p37301726"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p37301726"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p1540943"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p1540943"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p1540943"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p57707590"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p57707590"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p57707590"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p32486611"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p32486611"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p32486611"></a>Cluster version</p>
</td>
</tr>
<tr id="en-us_topic_0125376248_en-us_topic_0110839914_row23944047"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p60419656"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p60419656"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p60419656"></a>cluster_state</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p62154002"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p62154002"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p62154002"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p1309429"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p1309429"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p1309429"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p32571967"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p32571967"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p32571967"></a>Cluster status. Possible values are as follows:</p>
<p id="en-us_topic_0125376248_en-us_topic_0110839914_p24712251"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p24712251"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p24712251"></a><strong id="en-us_topic_0125376248_b7665208153512"><a name="en-us_topic_0125376248_b7665208153512"></a><a name="en-us_topic_0125376248_b7665208153512"></a>Null</strong>: There is no special status.</p>
<p id="en-us_topic_0125376248_en-us_topic_0110839914_p21083667"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p21083667"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p21083667"></a><strong id="en-us_topic_0125376248_b842352706194852"><a name="en-us_topic_0125376248_b842352706194852"></a><a name="en-us_topic_0125376248_b842352706194852"></a>installingPatch</strong>: The patch is being installed.</p>
</td>
</tr>
<tr id="en-us_topic_0125376248_en-us_topic_0110839914_row55535282"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p2064014"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p2064014"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p2064014"></a>stack_model</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p32967479"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p32967479"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p32967479"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p53120148"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p53120148"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p53120148"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p8899447"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p8899447"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p8899447"></a>Security mode of a cluster. Possible values are as follows:</p>
<p id="en-us_topic_0125376248_en-us_topic_0110839914_p12986160"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p12986160"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p12986160"></a>NoSec: Normal mode</p>
<p id="en-us_topic_0125376248_en-us_topic_0110839914_p49766582"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p49766582"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p49766582"></a>Sec: Security mode</p>
</td>
</tr>
<tr id="en-us_topic_0125376248_en-us_topic_0110839914_row45246057"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p41051970"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p41051970"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p41051970"></a>lic_state</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p36875235"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p36875235"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p36875235"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p34104053"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p34104053"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p34104053"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376248_en-us_topic_0110839914_p67087582"><a name="en-us_topic_0125376248_en-us_topic_0110839914_p67087582"></a><a name="en-us_topic_0125376248_en-us_topic_0110839914_p67087582"></a>License status</p>
</td>
</tr>
</tbody>
</table>

## Status Code<a name="en-us_topic_0125376248_section2092982712508"></a>

<a name="en-us_topic_0125376248_table2979011121511"></a>
<table><thead align="left"><tr id="en-us_topic_0125376248_row3981161161515"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.3.1.1"><p id="en-us_topic_0125376248_p398115116158"><a name="en-us_topic_0125376248_p398115116158"></a><a name="en-us_topic_0125376248_p398115116158"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83%" id="mcps1.1.3.1.2"><p id="en-us_topic_0125376248_p1798121191515"><a name="en-us_topic_0125376248_p1798121191515"></a><a name="en-us_topic_0125376248_p1798121191515"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376248_row69813112155"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0125376248_p15667142018546"><a name="en-us_topic_0125376248_p15667142018546"></a><a name="en-us_topic_0125376248_p15667142018546"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0125376248_p524694913339"><a name="en-us_topic_0125376248_p524694913339"></a><a name="en-us_topic_0125376248_p524694913339"></a>The operation is successful.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

