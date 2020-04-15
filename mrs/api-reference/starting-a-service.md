# Starting a Service<a name="EN-US_TOPIC_0220024733"></a>

## Function <a name="en-us_topic_0125376226_section165916208335"></a>

This API is used to start a specified service.

## URI<a name="en-us_topic_0125376226_s7145b3e17e3d4733be11840a3d8ad534"></a>

-   Format

POST /web/v1/maintain/cluster/\{cluster\_id\}/service/\{service\_name\}/start

-   URI parameter description

<a name="en-us_topic_0125376226_en-us_topic_0110839918_table23263818"></a>
<table><thead align="left"><tr id="en-us_topic_0125376226_en-us_topic_0110839918_row55214998"><th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.1"><p id="en-us_topic_0125376226_en-us_topic_0110839918_p43229817"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p43229817"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p43229817"></a><strong id="en-us_topic_0125376226_b162774213314533_1"><a name="en-us_topic_0125376226_b162774213314533_1"></a><a name="en-us_topic_0125376226_b162774213314533_1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.46%" id="mcps1.1.4.1.2"><p id="en-us_topic_0125376226_en-us_topic_0110839918_p11954326"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p11954326"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p11954326"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="49.08%" id="mcps1.1.4.1.3"><p id="en-us_topic_0125376226_en-us_topic_0110839918_p24370652"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p24370652"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p24370652"></a><strong id="en-us_topic_0125376226_b842352706134712"><a name="en-us_topic_0125376226_b842352706134712"></a><a name="en-us_topic_0125376226_b842352706134712"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376226_en-us_topic_0110839918_row27865835"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p42540195"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p42540195"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p42540195"></a>service_name</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p23203755"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p23203755"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p23203755"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p63261583"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p63261583"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p63261583"></a>Name of the service to be started</p>
</td>
</tr>
<tr id="en-us_topic_0125376226_en-us_topic_0110839918_row32483342"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p13905044"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p13905044"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p13905044"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p52566750"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p52566750"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p52566750"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p30624083"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p30624083"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p30624083"></a>Cluster ID that is displayed on MRS Manager. The default cluster ID is <strong id="en-us_topic_0125376226_b842352706152828"><a name="en-us_topic_0125376226_b842352706152828"></a><a name="en-us_topic_0125376226_b842352706152828"></a>1</strong>, because MRS Manager supports management of only one cluster currently.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0125376226_sa389edb5feaa418d84261d04ea938f19"></a>

-   Example:

    ```
    POST /web/v1/maintain/cluster/{cluster_id}/service/{service_name}/start HTTP/1.1
    Host: example.com
    Content-Type: application/json
    Accept:application/json
    {
      "user_password": "string",
      "only_self": true
    }
    ```

-   Parameter description

**Table  1**  Request parameter description

<a name="en-us_topic_0125376226_en-us_topic_0110839918_table18102480"></a>
<table><thead align="left"><tr id="en-us_topic_0125376226_en-us_topic_0110839918_row37653629"><th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.4.1.1"><p id="en-us_topic_0125376226_en-us_topic_0110839918_p30045122"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p30045122"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p30045122"></a><strong id="en-us_topic_0125376226_b1634817089"><a name="en-us_topic_0125376226_b1634817089"></a><a name="en-us_topic_0125376226_b1634817089"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.4.1.2"><p id="en-us_topic_0125376226_en-us_topic_0110839918_p17735803"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p17735803"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p17735803"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="56.565656565656575%" id="mcps1.2.4.1.3"><p id="en-us_topic_0125376226_en-us_topic_0110839918_p31668621"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p31668621"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p31668621"></a><strong id="en-us_topic_0125376226_b1144369142"><a name="en-us_topic_0125376226_b1144369142"></a><a name="en-us_topic_0125376226_b1144369142"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376226_en-us_topic_0110839918_row15021476"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p8780064"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p8780064"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p8780064"></a>user_password</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p40096617"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p40096617"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p40096617"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="56.565656565656575%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p6856233"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p6856233"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p6856233"></a>Password of the login user. This parameter is used for secondary authentication. You do not need to enter a specific value when starting the service. The parameter value can be null.</p>
</td>
</tr>
<tr id="en-us_topic_0125376226_en-us_topic_0110839918_row61706098"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p32138059"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p32138059"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p32138059"></a>only_self</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p53045956"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p53045956"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p53045956"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="56.565656565656575%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p8012684"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p8012684"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p8012684"></a>Whether to operate only the specified service</p>
<p id="en-us_topic_0125376226_en-us_topic_0110839918_p5005297"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p5005297"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p5005297"></a><strong id="en-us_topic_0125376226_b842352706204759"><a name="en-us_topic_0125376226_b842352706204759"></a><a name="en-us_topic_0125376226_b842352706204759"></a>false</strong>: The services on which the service depends are also started.</p>
<p id="en-us_topic_0125376226_en-us_topic_0110839918_p45047680"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p45047680"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p45047680"></a><strong id="en-us_topic_0125376226_b842352706204833"><a name="en-us_topic_0125376226_b842352706204833"></a><a name="en-us_topic_0125376226_b842352706204833"></a>true</strong>: Only the specified service is started.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0125376226_s8985f9ec35a042b4ac6d4ea7b402f9eb"></a>

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

<a name="en-us_topic_0125376226_en-us_topic_0110839918_table46926526"></a>
<table><thead align="left"><tr id="en-us_topic_0125376226_en-us_topic_0110839918_row60217622"><th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.1.5.1.1"><p id="en-us_topic_0125376226_en-us_topic_0110839918_p45789215"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p45789215"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p45789215"></a><strong id="en-us_topic_0125376226_b356034048"><a name="en-us_topic_0125376226_b356034048"></a><a name="en-us_topic_0125376226_b356034048"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.1.5.1.2"><p id="en-us_topic_0125376226_en-us_topic_0110839918_p17938969"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p17938969"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p17938969"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="20.292029202920293%" id="mcps1.1.5.1.3"><p id="en-us_topic_0125376226_en-us_topic_0110839918_p43770412"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p43770412"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p43770412"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.123912391239124%" id="mcps1.1.5.1.4"><p id="en-us_topic_0125376226_en-us_topic_0110839918_p50100742"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p50100742"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p50100742"></a><strong id="en-us_topic_0125376226_b139853461"><a name="en-us_topic_0125376226_b139853461"></a><a name="en-us_topic_0125376226_b139853461"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376226_en-us_topic_0110839918_row31628298"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p11755375"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p11755375"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p11755375"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p12661341"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p12661341"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p12661341"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p18935675"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p18935675"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p18935675"></a>LONG</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p18616839"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p18616839"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p18616839"></a>Asynchronous task ID (meaningless in other scenarios). The default value is <strong id="en-us_topic_0125376226_b842352706191850"><a name="en-us_topic_0125376226_b842352706191850"></a><a name="en-us_topic_0125376226_b842352706191850"></a>-1</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0125376226_en-us_topic_0110839918_row33333830"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p15685685"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p15685685"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p15685685"></a>state</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p62580961"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p62580961"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p62580961"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p35893041"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p35893041"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p35893041"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p31778432"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p31778432"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p31778432"></a>Cluster status. The value <strong id="en-us_topic_0125376226_b842352706191926"><a name="en-us_topic_0125376226_b842352706191926"></a><a name="en-us_topic_0125376226_b842352706191926"></a>FAILED</strong> indicates that the command fails to be executed. The value <strong id="en-us_topic_0125376226_b842352706191940"><a name="en-us_topic_0125376226_b842352706191940"></a><a name="en-us_topic_0125376226_b842352706191940"></a>COMPLETE</strong> indicates that the command is successfully executed. The value <strong id="en-us_topic_0125376226_b1512215825111"><a name="en-us_topic_0125376226_b1512215825111"></a><a name="en-us_topic_0125376226_b1512215825111"></a>IN_PROGRESS</strong> indicates that the command is being executed.</p>
</td>
</tr>
<tr id="en-us_topic_0125376226_en-us_topic_0110839918_row17570434"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p13919031"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p13919031"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p13919031"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p53699741"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p53699741"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p53699741"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p54711771"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p54711771"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p54711771"></a>INTEGER</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p22637498"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p22637498"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p22637498"></a>Error code returned</p>
</td>
</tr>
<tr id="en-us_topic_0125376226_en-us_topic_0110839918_row2410891"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p61064511"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p61064511"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p61064511"></a>error_description</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p47278359"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p47278359"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p47278359"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p4341884"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p4341884"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p4341884"></a>STRING</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p51271045"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p51271045"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p51271045"></a>Error code description</p>
</td>
</tr>
<tr id="en-us_topic_0125376226_en-us_topic_0110839918_row58786223"><td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p64063627"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p64063627"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p64063627"></a>total_progress</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p21771295"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p21771295"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p21771295"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="20.292029202920293%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p18644500"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p18644500"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p18644500"></a>FLOAT</p>
</td>
<td class="cellrowborder" valign="top" width="39.123912391239124%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0125376226_en-us_topic_0110839918_p29689414"><a name="en-us_topic_0125376226_en-us_topic_0110839918_p29689414"></a><a name="en-us_topic_0125376226_en-us_topic_0110839918_p29689414"></a>Total progress</p>
</td>
</tr>
</tbody>
</table>

## Status Code<a name="en-us_topic_0125376226_section2092982712508"></a>

<a name="en-us_topic_0125376226_table2979011121511"></a>
<table><thead align="left"><tr id="en-us_topic_0125376226_row3981161161515"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.3.1.1"><p id="en-us_topic_0125376226_p398115116158"><a name="en-us_topic_0125376226_p398115116158"></a><a name="en-us_topic_0125376226_p398115116158"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83%" id="mcps1.1.3.1.2"><p id="en-us_topic_0125376226_p1798121191515"><a name="en-us_topic_0125376226_p1798121191515"></a><a name="en-us_topic_0125376226_p1798121191515"></a>Description </p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376226_row69813112155"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0125376226_p15667142018546"><a name="en-us_topic_0125376226_p15667142018546"></a><a name="en-us_topic_0125376226_p15667142018546"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0125376226_p23378286542"><a name="en-us_topic_0125376226_p23378286542"></a><a name="en-us_topic_0125376226_p23378286542"></a>The operation is successful.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

