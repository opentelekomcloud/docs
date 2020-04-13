# Querying Statistics of All Running DCS Instances<a name="EN-US_TOPIC_0237964361"></a>

## Function<a name="section20228022"></a>

This API is used to query the statistics of all DCS instances in the  **Running**  state.

## URI<a name="section47834478"></a>

-   URI format:

    GET /v1.0/\{project\_id\}/instances/statistic

-   Parameter description:

    [Table 1](#table36543171)  describes the parameter of this API.


**Table  1**  Parameter description

<a name="table36543171"></a>
<table><thead align="left"><tr id="row56688054"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p28329695"><a name="p28329695"></a><a name="p28329695"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p13003964"><a name="p13003964"></a><a name="p13003964"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p46688182"><a name="p46688182"></a><a name="p46688182"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p23646388"><a name="p23646388"></a><a name="p23646388"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row36309279"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p55370462"><a name="p55370462"></a><a name="p55370462"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p55822426"><a name="p55822426"></a><a name="p55822426"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p25322618"><a name="p25322618"></a><a name="p25322618"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p37866150"><a name="p37866150"></a><a name="p37866150"></a>Project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section27857118"></a>

None.

## Response<a name="section49387472"></a>

-   Status code:

    If status code "200 OK" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    [Table 2](#table60453091)  describes the response parameter.


**Table  2**  Parameter description

<a name="table60453091"></a>
<table><thead align="left"><tr id="row19206131"><th class="cellrowborder" valign="top" width="19.19191919191919%" id="mcps1.2.4.1.1"><p id="p12192756"><a name="p12192756"></a><a name="p12192756"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="47.474747474747474%" id="mcps1.2.4.1.2"><p id="p48089211"><a name="p48089211"></a><a name="p48089211"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p2911981"><a name="p2911981"></a><a name="p2911981"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row34543924"><td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.4.1.1 "><p id="p46594488"><a name="p46594488"></a><a name="p46594488"></a>statistics</p>
</td>
<td class="cellrowborder" valign="top" width="47.474747474747474%" headers="mcps1.2.4.1.2 "><p id="p16057184"><a name="p16057184"></a><a name="p16057184"></a>Array.</p>
<p id="p10296933"><a name="p10296933"></a><a name="p10296933"></a>For details, see <a href="#ref478566383">Table 3</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p57380926"><a name="p57380926"></a><a name="p57380926"></a>Statistics of all DCS instances in the <strong id="b46666290"><a name="b46666290"></a><a name="b46666290"></a>Running </strong>state.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Parameter description of the statistics array

<a name="ref478566383"></a>
<table><thead align="left"><tr id="row13621136"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p29570261"><a name="p29570261"></a><a name="p29570261"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="p46380963"><a name="p46380963"></a><a name="p46380963"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65%" id="mcps1.2.4.1.3"><p id="p65870497"><a name="p65870497"></a><a name="p65870497"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row33910007"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p62356046"><a name="p62356046"></a><a name="p62356046"></a>keys</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p17674957"><a name="p17674957"></a><a name="p17674957"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p22385437"><a name="p22385437"></a><a name="p22385437"></a>Number of data items stored in the cache.</p>
</td>
</tr>
<tr id="row142347"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p11530135"><a name="p11530135"></a><a name="p11530135"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p61525703"><a name="p61525703"></a><a name="p61525703"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p17526019"><a name="p17526019"></a><a name="p17526019"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row23516450"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p25784284"><a name="p25784284"></a><a name="p25784284"></a>used_memory</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p8152279"><a name="p8152279"></a><a name="p8152279"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p56354875"><a name="p56354875"></a><a name="p56354875"></a>Size of the used memory.</p>
<p id="p37431827"><a name="p37431827"></a><a name="p37431827"></a>Unit: MB.</p>
</td>
</tr>
<tr id="row1342126"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p41603419"><a name="p41603419"></a><a name="p41603419"></a>max_memory</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p14433768"><a name="p14433768"></a><a name="p14433768"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p28284541"><a name="p28284541"></a><a name="p28284541"></a>Overall memory size.</p>
<p id="p53234283"><a name="p53234283"></a><a name="p53234283"></a>Unit: MB.</p>
</td>
</tr>
<tr id="row9346499"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p18868961"><a name="p18868961"></a><a name="p18868961"></a>cmd_get_count</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p51990912"><a name="p51990912"></a><a name="p51990912"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p50514376"><a name="p50514376"></a><a name="p50514376"></a>Number of times the GET command is run.</p>
</td>
</tr>
<tr id="row51976202"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p49322849"><a name="p49322849"></a><a name="p49322849"></a>cmd_set_count</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p35727861"><a name="p35727861"></a><a name="p35727861"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p8275629"><a name="p8275629"></a><a name="p8275629"></a>Number of times the SET command is run.</p>
</td>
</tr>
<tr id="row7371802"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p60245124"><a name="p60245124"></a><a name="p60245124"></a>used_cpu</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p48016903"><a name="p48016903"></a><a name="p48016903"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p64163914"><a name="p64163914"></a><a name="p64163914"></a>CPU usage.</p>
<p id="p40604315"><a name="p40604315"></a><a name="p40604315"></a>Unit: %.</p>
</td>
</tr>
<tr id="row29894517"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p5536817"><a name="p5536817"></a><a name="p5536817"></a>input_kbps</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p45829029"><a name="p45829029"></a><a name="p45829029"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p21163898"><a name="p21163898"></a><a name="p21163898"></a>Incoming traffic of the DCS instance.</p>
<p id="p56257360"><a name="p56257360"></a><a name="p56257360"></a>Unit: kbit/s.</p>
</td>
</tr>
<tr id="row36554200"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p8100198"><a name="p8100198"></a><a name="p8100198"></a>output_kbps</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p52136268"><a name="p52136268"></a><a name="p52136268"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p62288179"><a name="p62288179"></a><a name="p62288179"></a>Outgoing traffic of the DCS instance.</p>
<p id="p23722702"><a name="p23722702"></a><a name="p23722702"></a>Unit: kbit/s.</p>
</td>
</tr>
</tbody>
</table>

-   Example response:

    ```
    { 
     "statistics" : [{ 
                "keys" : 0, 
                "instance_id" : "e008652d-18e0-43ff-924e-072261e0372a", 
                "used_memory" : 0, 
                "max_memory" : 460, 
                "cmd_get_count" : 0, 
                "cmd_set_count" : 0, 
                "used_cpu" : "0.0", 
                "input_kbps" : "0.0", 
                "output_kbps" : "0.0" 
            }, { 
                "keys" : 0, 
                "instance_id" : "e8b98471-55d5-4695-b0bb-8f336a98e207", 
                "used_memory" : 0, 
                "max_memory" : 460, 
                "cmd_get_count" : 0, 
                "cmd_set_count" : 0, 
                "used_cpu" : "0.0", 
                "input_kbps" : "0.03", 
                "output_kbps" : "1.19" 
            }, { 
                "keys" : 0, 
                "instance_id" : "bc61c690-4b34-4cbe-9ce3-11246aea7aba", 
                "used_memory" : 0, 
                "max_memory" : 6963, 
                "cmd_get_count" : 0, 
                "cmd_set_count" : 0, 
                "used_cpu" : "0.0", 
                "input_kbps" : "0.0", 
                "output_kbps" : "0.0" 
            } 
     ] 
    }
    ```


