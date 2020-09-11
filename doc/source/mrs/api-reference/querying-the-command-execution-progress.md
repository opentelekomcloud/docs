# Querying the Command Execution Progress<a name="EN-US_TOPIC_0220024730"></a>

## Function<a name="en-us_topic_0125376258_section132313464914"></a>

This API is used to query the command execution progress by command ID, including the total progress and the detailed progress of each step.

## URI<a name="en-us_topic_0125376258_sd919b2e337864622b820bd95e2c3c1c1"></a>

-   Format

GET /web/v1/common/command/\{command\_id\}/progress

-   URI parameter description

<a name="en-us_topic_0125376258_en-us_topic_0110839915_table61567624"></a>
<table><thead align="left"><tr id="en-us_topic_0125376258_en-us_topic_0110839915_row43465205"><th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.1"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p31020730"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p31020730"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p31020730"></a><strong id="en-us_topic_0125376258_b162774213314533_1"><a name="en-us_topic_0125376258_b162774213314533_1"></a><a name="en-us_topic_0125376258_b162774213314533_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.2"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p29651187"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p29651187"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p29651187"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="49.08%" id="mcps1.1.4.1.3"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p27389957"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p27389957"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p27389957"></a><strong id="en-us_topic_0125376258_b842352706134712"><a name="en-us_topic_0125376258_b842352706134712"></a><a name="en-us_topic_0125376258_b842352706134712"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376258_en-us_topic_0110839915_row3994012"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p55079576"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p55079576"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p55079576"></a>command_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p32260705"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p32260705"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p32260705"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376258_p38163105386"><a name="en-us_topic_0125376258_p38163105386"></a><a name="en-us_topic_0125376258_p38163105386"></a>Command ID, which can be obtained from the response of the asynchronous request</p>
<p id="en-us_topic_0125376258_p14816710113815"><a name="en-us_topic_0125376258_p14816710113815"></a><a name="en-us_topic_0125376258_p14816710113815"></a>Asynchronous requests include requests for saving configurations and starting and stopping services.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0125376258_sd64edd6241824b7cb64f9a14b940004c"></a>

-   Example:

    ```
    GET /web/v1/common/command/{command_id}/progress HTTP/1.1
    Host: example.com
    Content-Type: application/json
    Accept:application/json
    ```

-   Parameter description

    None


## Response<a name="en-us_topic_0125376258_s318b876a953c4974ad48f83be32b094c"></a>

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
        "cluster_id": 0,
        "step_list": [
          {
            "name": "string",
            "description": "string"
          }
        ],
        "fail_entity_list": [
          {
            "fail_entity": "string",
            "operation_type": "string"
          }
        ],
        "total_step_size": 0
      }
    }
    ```

-   Parameter description

**Table  1**  Response parameter description

<a name="en-us_topic_0125376258_en-us_topic_0110839915_table42073913"></a>
<table><thead align="left"><tr id="en-us_topic_0125376258_en-us_topic_0110839915_row46197435"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p51004735"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p51004735"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p51004735"></a><strong id="en-us_topic_0125376258_b162774213314533_1_1"><a name="en-us_topic_0125376258_b162774213314533_1_1"></a><a name="en-us_topic_0125376258_b162774213314533_1_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p37742864"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p37742864"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p37742864"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p37273109"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p37273109"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p37273109"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p2159343"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p2159343"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p2159343"></a><strong id="en-us_topic_0125376258_b842352706134712_1"><a name="en-us_topic_0125376258_b842352706134712_1"></a><a name="en-us_topic_0125376258_b842352706134712_1"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376258_en-us_topic_0110839915_row40689110"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p7483642"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p7483642"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p7483642"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p2195266"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p2195266"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p2195266"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p43598871"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p43598871"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p43598871"></a>LONG</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p20058992"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p20058992"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p20058992"></a>Asynchronous task ID (meaningless in other scenarios). The default value is <strong id="en-us_topic_0125376258_b842352706191850"><a name="en-us_topic_0125376258_b842352706191850"></a><a name="en-us_topic_0125376258_b842352706191850"></a>-1</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0125376258_en-us_topic_0110839915_row46313202"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p60381886"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p60381886"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p60381886"></a>state</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p59094594"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p59094594"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p59094594"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p21932839"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p21932839"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p21932839"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p42197016"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p42197016"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p42197016"></a>Cluster status. The value <strong id="en-us_topic_0125376258_b842352706191926"><a name="en-us_topic_0125376258_b842352706191926"></a><a name="en-us_topic_0125376258_b842352706191926"></a>FAILED</strong>&nbsp;indicates that the command fails to be executed. The value&nbsp;<strong id="en-us_topic_0125376258_b842352706191940"><a name="en-us_topic_0125376258_b842352706191940"></a><a name="en-us_topic_0125376258_b842352706191940"></a>COMPLETE</strong> indicates that the command is successfully executed.</p>
</td>
</tr>
<tr id="en-us_topic_0125376258_en-us_topic_0110839915_row44228825"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p25765033"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p25765033"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p25765033"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p6592901"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p6592901"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p6592901"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p64262998"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p64262998"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p64262998"></a>INTEGER</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p23110933"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p23110933"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p23110933"></a>Error code returned</p>
</td>
</tr>
<tr id="en-us_topic_0125376258_en-us_topic_0110839915_row6671808"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p3545613"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p3545613"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p3545613"></a>error_description</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p18759226"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p18759226"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p18759226"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p43102319"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p43102319"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p43102319"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p4211794"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p4211794"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p4211794"></a>Error code description</p>
</td>
</tr>
<tr id="en-us_topic_0125376258_en-us_topic_0110839915_row37906154"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p50499596"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p50499596"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p50499596"></a>total_progress</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p63935491"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p63935491"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p63935491"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p11392311"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p11392311"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p11392311"></a>FLOAT</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p48142285"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p48142285"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p48142285"></a>Total progress</p>
</td>
</tr>
<tr id="en-us_topic_0125376258_en-us_topic_0110839915_row30627385"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p64899100"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p64899100"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p64899100"></a>res_obj</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p22335719"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p22335719"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p22335719"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p64362819"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p64362819"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p64362819"></a>REFERENCE</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p50939954"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p50939954"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p50939954"></a>Response object</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **res\_obj**  parameter description

<a name="en-us_topic_0125376258_en-us_topic_0110839915_table32495643"></a>
<table><thead align="left"><tr id="en-us_topic_0125376258_en-us_topic_0110839915_row54638644"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p63654061"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p63654061"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p63654061"></a><strong id="en-us_topic_0125376258_b162774213314533_1_2"><a name="en-us_topic_0125376258_b162774213314533_1_2"></a><a name="en-us_topic_0125376258_b162774213314533_1_2"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p55705286"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p55705286"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p55705286"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p15834279"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p15834279"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p15834279"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p3507726"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p3507726"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p3507726"></a><strong id="en-us_topic_0125376258_b842352706134712_2"><a name="en-us_topic_0125376258_b842352706134712_2"></a><a name="en-us_topic_0125376258_b842352706134712_2"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376258_en-us_topic_0110839915_row15690402"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p62963013"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p62963013"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p62963013"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p66839330"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p66839330"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p66839330"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p45276639"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p45276639"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p45276639"></a>INTEGER</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p46370664"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p46370664"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p46370664"></a>Cluster ID</p>
</td>
</tr>
<tr id="en-us_topic_0125376258_en-us_topic_0110839915_row14682800"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p48456183"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p48456183"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p48456183"></a>step_list</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p32636713"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p32636713"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p32636713"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p26328112"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p26328112"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p26328112"></a>ARRAY_REFERENCE</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p4792001"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p4792001"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p4792001"></a>Records the progress of each step in an array. A command may be divided into multiple steps for execution.</p>
</td>
</tr>
<tr id="en-us_topic_0125376258_en-us_topic_0110839915_row43128017"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p3708474"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p3708474"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p3708474"></a>fail_entity_list</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p31950976"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p31950976"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p31950976"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p37892234"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p37892234"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p37892234"></a>ARRAY_REFERENCE</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p21907564"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p21907564"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p21907564"></a>List of failed operations. Currently, this function is supported for starting, stopping, and restarting the service. Other operations are not supported (an empty array is returned).</p>
</td>
</tr>
<tr id="en-us_topic_0125376258_en-us_topic_0110839915_row62950355"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p65814015"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p65814015"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p65814015"></a>total_step_size</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p29335032"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p29335032"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p29335032"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p27327397"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p27327397"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p27327397"></a>INTEGER</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p4531576"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p4531576"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p4531576"></a>Total command execution progress. The value ranges from 0 to 100.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **step\_list**  parameter description

<a name="en-us_topic_0125376258_en-us_topic_0110839915_table31513351"></a>
<table><thead align="left"><tr id="en-us_topic_0125376258_en-us_topic_0110839915_row63574456"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p49257331"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p49257331"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p49257331"></a><strong id="en-us_topic_0125376258_b162774213314533_1_3"><a name="en-us_topic_0125376258_b162774213314533_1_3"></a><a name="en-us_topic_0125376258_b162774213314533_1_3"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p30420887"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p30420887"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p30420887"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p48172746"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p48172746"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p48172746"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p14940377"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p14940377"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p14940377"></a><strong id="en-us_topic_0125376258_b842352706134712_3"><a name="en-us_topic_0125376258_b842352706134712_3"></a><a name="en-us_topic_0125376258_b842352706134712_3"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376258_en-us_topic_0110839915_row2211039"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p44876477"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p44876477"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p44876477"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p11116060"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p11116060"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p11116060"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p27985700"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p27985700"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p27985700"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p15003965"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p15003965"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p15003965"></a>Partition name</p>
</td>
</tr>
<tr id="en-us_topic_0125376258_en-us_topic_0110839915_row817961"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p66254894"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p66254894"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p66254894"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p65046183"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p65046183"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p65046183"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p34249469"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p34249469"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p34249469"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p37592761"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p37592761"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p37592761"></a>Description</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **fail\_entity\_list**  parameter description

<a name="en-us_topic_0125376258_en-us_topic_0110839915_table25114768"></a>
<table><thead align="left"><tr id="en-us_topic_0125376258_en-us_topic_0110839915_row43903439"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p66517662"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p66517662"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p66517662"></a><strong id="en-us_topic_0125376258_b162774213314533_1_4"><a name="en-us_topic_0125376258_b162774213314533_1_4"></a><a name="en-us_topic_0125376258_b162774213314533_1_4"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p19221566"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p19221566"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p19221566"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p13443031"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p13443031"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p13443031"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376258_en-us_topic_0110839915_p36670851"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p36670851"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p36670851"></a><strong id="en-us_topic_0125376258_b842352706134712_4"><a name="en-us_topic_0125376258_b842352706134712_4"></a><a name="en-us_topic_0125376258_b842352706134712_4"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376258_en-us_topic_0110839915_row17548941"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p12178136"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p12178136"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p12178136"></a>fail_entity</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p46904972"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p46904972"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p46904972"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p41206351"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p41206351"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p41206351"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p48824334"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p48824334"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p48824334"></a>Failed instance</p>
</td>
</tr>
<tr id="en-us_topic_0125376258_en-us_topic_0110839915_row36765828"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p25242057"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p25242057"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p25242057"></a>operation_type</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p31340714"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p31340714"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p31340714"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p55569937"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p55569937"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p55569937"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376258_en-us_topic_0110839915_p14888430"><a name="en-us_topic_0125376258_en-us_topic_0110839915_p14888430"></a><a name="en-us_topic_0125376258_en-us_topic_0110839915_p14888430"></a>Operation type: STOP or START</p>
</td>
</tr>
</tbody>
</table>

## Status Code<a name="en-us_topic_0125376258_section2092982712508"></a>

<a name="en-us_topic_0125376258_table2979011121511"></a>
<table><thead align="left"><tr id="en-us_topic_0125376258_row3981161161515"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.3.1.1"><p id="en-us_topic_0125376258_p398115116158"><a name="en-us_topic_0125376258_p398115116158"></a><a name="en-us_topic_0125376258_p398115116158"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83%" id="mcps1.1.3.1.2"><p id="en-us_topic_0125376258_p1798121191515"><a name="en-us_topic_0125376258_p1798121191515"></a><a name="en-us_topic_0125376258_p1798121191515"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376258_row69813112155"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0125376258_p15667142018546"><a name="en-us_topic_0125376258_p15667142018546"></a><a name="en-us_topic_0125376258_p15667142018546"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0125376258_p23378286542"><a name="en-us_topic_0125376258_p23378286542"></a><a name="en-us_topic_0125376258_p23378286542"></a>The operation is successful.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

