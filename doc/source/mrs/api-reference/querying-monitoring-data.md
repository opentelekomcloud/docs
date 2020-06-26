# Querying Monitoring Data<a name="EN-US_TOPIC_0220024735"></a>

## Function<a name="en-us_topic_0125376240_section37142316118"></a>

This API is used to query performance monitoring items supported by a specified host.

## URI<a name="en-us_topic_0125376240_s77df913e57104a28933dd75a92e8a89a"></a>

-   Format

GET /web/v1/monitor/metrics\_info

-   Parameter description

<a name="en-us_topic_0125376240_en-us_topic_0110839920_table183737"></a>
<table><thead align="left"><tr id="en-us_topic_0125376240_en-us_topic_0110839920_row61019838"><th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.1"><p id="en-us_topic_0125376240_en-us_topic_0110839920_p43659812"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p43659812"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p43659812"></a><strong id="en-us_topic_0125376240_b162774213314533_1"><a name="en-us_topic_0125376240_b162774213314533_1"></a><a name="en-us_topic_0125376240_b162774213314533_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.2"><p id="en-us_topic_0125376240_en-us_topic_0110839920_p46783883"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p46783883"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p46783883"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="49.08%" id="mcps1.1.4.1.3"><p id="en-us_topic_0125376240_en-us_topic_0110839920_p58907084"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p58907084"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p58907084"></a><strong id="en-us_topic_0125376240_b842352706134712"><a name="en-us_topic_0125376240_b842352706134712"></a><a name="en-us_topic_0125376240_b842352706134712"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376240_en-us_topic_0110839920_row6744461"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p9430463"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p9430463"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p9430463"></a>metric_names</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p25670025"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p25670025"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p25670025"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376240_p1541894101515"><a name="en-us_topic_0125376240_p1541894101515"></a><a name="en-us_topic_0125376240_p1541894101515"></a>Monitoring metric name. Use commas (,) to separate metric names. You can enter a maximum of 10 metric names at a time.</p>
<p id="en-us_topic_0125376240_p186861210157"><a name="en-us_topic_0125376240_p186861210157"></a><a name="en-us_topic_0125376240_p186861210157"></a>Example metric names are as follows:</p>
<a name="en-us_topic_0125376240_ul1560181415158"></a><a name="en-us_topic_0125376240_ul1560181415158"></a><ul id="en-us_topic_0125376240_ul1560181415158"><li><strong id="en-us_topic_0125376240_b84235270693734"><a name="en-us_topic_0125376240_b84235270693734"></a><a name="en-us_topic_0125376240_b84235270693734"></a>hm_cpu_used</strong>: CPU usage</li><li><strong id="en-us_topic_0125376240_b84235270693745"><a name="en-us_topic_0125376240_b84235270693745"></a><a name="en-us_topic_0125376240_b84235270693745"></a>hm_cpu_core_num</strong>: Number of CPU cores</li></ul>
</td>
</tr>
<tr id="en-us_topic_0125376240_en-us_topic_0110839920_row42996619"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p60174095"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p60174095"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p60174095"></a>metric_period</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p42263520"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p42263520"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p42263520"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p21582271"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p21582271"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p21582271"></a>Metric period, which can be real time, 5 minutes, 30 minutes, or 60 minutes</p>
</td>
</tr>
<tr id="en-us_topic_0125376240_en-us_topic_0110839920_row60022717"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p30001885"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p30001885"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p30001885"></a>start_time</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p14233630"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p14233630"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p14233630"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p12738823"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p12738823"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p12738823"></a>Start time, expressed in milliseconds. The data type is Long. The default value is the earliest system time.</p>
</td>
</tr>
<tr id="en-us_topic_0125376240_en-us_topic_0110839920_row47540544"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p25578838"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p25578838"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p25578838"></a>end_time</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p58620034"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p58620034"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p58620034"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376240_p157791737171511"><a name="en-us_topic_0125376240_p157791737171511"></a><a name="en-us_topic_0125376240_p157791737171511"></a>End time, expressed in milliseconds. The data type is Long. The default value is the latest system time.</p>
</td>
</tr>
<tr id="en-us_topic_0125376240_en-us_topic_0110839920_row20299897"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p33678960"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p33678960"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p33678960"></a>hosts</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p43641231"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p43641231"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p43641231"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p12065346"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p12065346"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p12065346"></a>List of host names to be queried. Use commas (,) to separate host names. You can enter a maximum of 50 host names to meet the input length requirements of the browser.</p>
</td>
</tr>
<tr id="en-us_topic_0125376240_en-us_topic_0110839920_row41479253"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p4376358"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p4376358"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p4376358"></a>host_group</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p18940756"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p18940756"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p18940756"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p602952"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p602952"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p602952"></a>Name of the host group created by a user. This function is not available in the current version.</p>
</td>
</tr>
<tr id="en-us_topic_0125376240_en-us_topic_0110839920_row5426570"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p36899007"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p36899007"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p36899007"></a>metric_node_type</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p36029605"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p36029605"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p36029605"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376240_p0661344104911"><a name="en-us_topic_0125376240_p0661344104911"></a><a name="en-us_topic_0125376240_p0661344104911"></a>You can set this parameter to obtain the monitoring metrics of a node. The possible values are as follows:</p>
<a name="en-us_topic_0125376240_ul4661154474911"></a><a name="en-us_topic_0125376240_ul4661154474911"></a><ul id="en-us_topic_0125376240_ul4661154474911"><li><strong id="en-us_topic_0125376240_b842352706174939"><a name="en-us_topic_0125376240_b842352706174939"></a><a name="en-us_topic_0125376240_b842352706174939"></a>active</strong>: Indicates that you can obtain monitoring metrics of the active node.</li><li><strong id="en-us_topic_0125376240_b842352706175039"><a name="en-us_topic_0125376240_b842352706175039"></a><a name="en-us_topic_0125376240_b842352706175039"></a>standby</strong>: Indicates that you can obtain monitoring metrics of the standby node.</li><li><strong id="en-us_topic_0125376240_b842352706175039_1"><a name="en-us_topic_0125376240_b842352706175039_1"></a><a name="en-us_topic_0125376240_b842352706175039_1"></a>all</strong>: Indicates that you can obtain monitoring metrics of all nodes.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0125376240_en-us_topic_0110839920_row32957959"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p52349023"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p52349023"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p52349023"></a>extend</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p12412484"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p12412484"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p12412484"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p564979"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p564979"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p564979"></a>Metric extended field, which records information about small metrics</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0125376240_s820fc85f0a4f4f6f846ca5418d2e084d"></a>

-   Example:

    ```
    GET /web/v1/monitor/metrics_info?metric_names=null&metric_period=null&start_time=null&end_time=null&hosts=null&host_group=null&metric_node_type=null&extend=null HTTP/1.1
    Host: example.com
    Content-Type: application/json
    Accept:application/json
    ```

-   Parameter description

    None


## Response<a name="en-us_topic_0125376240_sc1e6a76efabf4f93b2b36539371117d6"></a>

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
    "metric_datas": {
      "additionalProp1": [
        {
          "time": 0,
          "value": "string",
          "node": "string"
        }
      ]
    }
  }
}
```

-   Request parameter description

**Table  1**  Response parameter description

<a name="en-us_topic_0125376240_en-us_topic_0110839920_table2347214"></a>
<table><thead align="left"><tr id="en-us_topic_0125376240_en-us_topic_0110839920_row54013670"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376240_en-us_topic_0110839920_p13031110"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p13031110"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p13031110"></a><strong id="en-us_topic_0125376240_b162774213314533_1_1"><a name="en-us_topic_0125376240_b162774213314533_1_1"></a><a name="en-us_topic_0125376240_b162774213314533_1_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376240_en-us_topic_0110839920_p48886962"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p48886962"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p48886962"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376240_en-us_topic_0110839920_p421011"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p421011"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p421011"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376240_en-us_topic_0110839920_p2070146"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p2070146"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p2070146"></a><strong id="en-us_topic_0125376240_b842352706134712_1"><a name="en-us_topic_0125376240_b842352706134712_1"></a><a name="en-us_topic_0125376240_b842352706134712_1"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376240_en-us_topic_0110839920_row33464133"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p26240261"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p26240261"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p26240261"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p45086377"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p45086377"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p45086377"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p28117914"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p28117914"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p28117914"></a>LONG</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p15839175"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p15839175"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p15839175"></a>Asynchronous task ID (meaningless in other scenarios). The default value is <strong id="en-us_topic_0125376240_b842352706191850"><a name="en-us_topic_0125376240_b842352706191850"></a><a name="en-us_topic_0125376240_b842352706191850"></a>-1</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0125376240_en-us_topic_0110839920_row8334847"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p4033991"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p4033991"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p4033991"></a>state</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p58317831"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p58317831"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p58317831"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p26123880"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p26123880"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p26123880"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p4132540"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p4132540"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p4132540"></a>Cluster status. The value <strong id="en-us_topic_0125376240_b842352706191926"><a name="en-us_topic_0125376240_b842352706191926"></a><a name="en-us_topic_0125376240_b842352706191926"></a>FAILED</strong>&nbsp;indicates that the command fails to be executed. The value&nbsp;<strong id="en-us_topic_0125376240_b842352706191940"><a name="en-us_topic_0125376240_b842352706191940"></a><a name="en-us_topic_0125376240_b842352706191940"></a>COMPLETE</strong> indicates that the command is successfully executed.</p>
</td>
</tr>
<tr id="en-us_topic_0125376240_en-us_topic_0110839920_row37192867"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p59832271"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p59832271"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p59832271"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p14575816"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p14575816"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p14575816"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p39790453"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p39790453"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p39790453"></a>INTEGER</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p7033928"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p7033928"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p7033928"></a>Error code returned</p>
</td>
</tr>
<tr id="en-us_topic_0125376240_en-us_topic_0110839920_row63305353"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p27459986"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p27459986"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p27459986"></a>error_description</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p9666363"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p9666363"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p9666363"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p44777900"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p44777900"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p44777900"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p9004739"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p9004739"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p9004739"></a>Error code description</p>
</td>
</tr>
<tr id="en-us_topic_0125376240_en-us_topic_0110839920_row13933792"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p54895391"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p54895391"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p54895391"></a>total_progress</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p17341682"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p17341682"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p17341682"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p62499010"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p62499010"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p62499010"></a>FLOAT</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p10903468"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p10903468"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p10903468"></a>Total progress</p>
</td>
</tr>
<tr id="en-us_topic_0125376240_en-us_topic_0110839920_row31022349"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p29782380"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p29782380"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p29782380"></a>res_obj</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p63562612"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p63562612"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p63562612"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p48297932"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p48297932"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p48297932"></a>REFERENCE</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p19205369"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p19205369"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p19205369"></a>Response object</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **res\_obj**  parameter description

<a name="en-us_topic_0125376240_en-us_topic_0110839920_table12131070"></a>
<table><thead align="left"><tr id="en-us_topic_0125376240_en-us_topic_0110839920_row52918685"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376240_en-us_topic_0110839920_p58555089"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p58555089"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p58555089"></a><strong id="en-us_topic_0125376240_b162774213314533_1_2"><a name="en-us_topic_0125376240_b162774213314533_1_2"></a><a name="en-us_topic_0125376240_b162774213314533_1_2"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376240_en-us_topic_0110839920_p45341798"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p45341798"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p45341798"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376240_en-us_topic_0110839920_p48807044"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p48807044"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p48807044"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376240_en-us_topic_0110839920_p18664735"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p18664735"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p18664735"></a><strong id="en-us_topic_0125376240_b842352706134712_2"><a name="en-us_topic_0125376240_b842352706134712_2"></a><a name="en-us_topic_0125376240_b842352706134712_2"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376240_en-us_topic_0110839920_row35448558"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p52760974"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p52760974"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p52760974"></a>metric_datas</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p45780519"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p45780519"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p45780519"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p17234528"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p17234528"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p17234528"></a>MAP</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p42831213"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p42831213"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p42831213"></a>Monitoring data.</p>
<p id="en-us_topic_0125376240_en-us_topic_0110839920_p49936605"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p49936605"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p49936605"></a>Key indicates the name of a monitoring item.</p>
<p id="en-us_topic_0125376240_en-us_topic_0110839920_p46776267"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p46776267"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p46776267"></a>Value indicates a list of monitored metric parameters queried.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **metricDataBean**  parameter description

<a name="en-us_topic_0125376240_en-us_topic_0110839920_table30781293"></a>
<table><thead align="left"><tr id="en-us_topic_0125376240_en-us_topic_0110839920_row59931476"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376240_en-us_topic_0110839920_p22611353"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p22611353"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p22611353"></a><strong id="en-us_topic_0125376240_b162774213314533_1_3"><a name="en-us_topic_0125376240_b162774213314533_1_3"></a><a name="en-us_topic_0125376240_b162774213314533_1_3"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376240_en-us_topic_0110839920_p19580282"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p19580282"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p19580282"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376240_en-us_topic_0110839920_p42499041"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p42499041"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p42499041"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376240_en-us_topic_0110839920_p43359934"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p43359934"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p43359934"></a><strong id="en-us_topic_0125376240_b842352706134712_3"><a name="en-us_topic_0125376240_b842352706134712_3"></a><a name="en-us_topic_0125376240_b842352706134712_3"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376240_en-us_topic_0110839920_row22493766"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p10055771"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p10055771"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p10055771"></a>time</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p9211108"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p9211108"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p9211108"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p7902282"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p7902282"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p7902282"></a>BIGDECIMAL</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p58224438"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p58224438"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p58224438"></a>Time when monitoring metric value is collected</p>
</td>
</tr>
<tr id="en-us_topic_0125376240_en-us_topic_0110839920_row54257894"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p32813323"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p32813323"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p32813323"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p40633529"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p40633529"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p40633529"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p2981527"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p2981527"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p2981527"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p65453923"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p65453923"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p65453923"></a>Monitoring metric value</p>
</td>
</tr>
<tr id="en-us_topic_0125376240_en-us_topic_0110839920_row52214402"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p1508145"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p1508145"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p1508145"></a>node</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p55050909"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p55050909"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p55050909"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p29938605"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p29938605"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p29938605"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376240_en-us_topic_0110839920_p30133576"><a name="en-us_topic_0125376240_en-us_topic_0110839920_p30133576"></a><a name="en-us_topic_0125376240_en-us_topic_0110839920_p30133576"></a>Node where the monitoring metric is collected</p>
</td>
</tr>
<tr id="en-us_topic_0125376240_row1728912311711"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376240_p3289193119715"><a name="en-us_topic_0125376240_p3289193119715"></a><a name="en-us_topic_0125376240_p3289193119715"></a>extend</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376240_p1828916311078"><a name="en-us_topic_0125376240_p1828916311078"></a><a name="en-us_topic_0125376240_p1828916311078"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376240_p1728915311372"><a name="en-us_topic_0125376240_p1728915311372"></a><a name="en-us_topic_0125376240_p1728915311372"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376240_p82891311173"><a name="en-us_topic_0125376240_p82891311173"></a><a name="en-us_topic_0125376240_p82891311173"></a>Metric extended field, which records information about small metrics</p>
</td>
</tr>
</tbody>
</table>

## Status Code<a name="en-us_topic_0125376240_section2092982712508"></a>

<a name="en-us_topic_0125376240_table2979011121511"></a>
<table><thead align="left"><tr id="en-us_topic_0125376240_row3981161161515"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.3.1.1"><p id="en-us_topic_0125376240_p398115116158"><a name="en-us_topic_0125376240_p398115116158"></a><a name="en-us_topic_0125376240_p398115116158"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83%" id="mcps1.1.3.1.2"><p id="en-us_topic_0125376240_p1798121191515"><a name="en-us_topic_0125376240_p1798121191515"></a><a name="en-us_topic_0125376240_p1798121191515"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376240_row69813112155"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0125376240_p15667142018546"><a name="en-us_topic_0125376240_p15667142018546"></a><a name="en-us_topic_0125376240_p15667142018546"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0125376240_p23378286542"><a name="en-us_topic_0125376240_p23378286542"></a><a name="en-us_topic_0125376240_p23378286542"></a>The operation is successful.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

