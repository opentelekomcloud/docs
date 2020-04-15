# Obtaining ECS Management Console Logs<a name="EN-US_TOPIC_0065817689"></a>

## Function<a name="en-us_topic_0062473752_section6511166111343"></a>

This API is used to obtain ECS management console logs.

## URI<a name="en-us_topic_0062473752_section34513797111412"></a>

POST /v2/\{project\_id\}/servers/\{server\_id\}/action

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/action

[Table 1](#en-us_topic_0062473752_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0062473752_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0062473752_row44937496"><th class="cellrowborder" valign="top" width="16.79%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.919999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.29%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0062473752_row1664874"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0062473752_p637140"><a name="en-us_topic_0062473752_p637140"></a><a name="en-us_topic_0062473752_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0062473752_p51608407"><a name="en-us_topic_0062473752_p51608407"></a><a name="en-us_topic_0062473752_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.29%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0062473752_row41565035"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0062473752_p11324657"><a name="en-us_topic_0062473752_p11324657"></a><a name="en-us_topic_0062473752_p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0062473752_p44882061"><a name="en-us_topic_0062473752_p44882061"></a><a name="en-us_topic_0062473752_p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.29%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0062473752_p11568292"><a name="en-us_topic_0062473752_p11568292"></a><a name="en-us_topic_0062473752_p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="en-us_topic_0062473752_section5849161002917"></a>

This API will be discarded since a version later than microversion 2.5. When using this API, set the microversion to 2.5 or earlier.

## Request<a name="en-us_topic_0062473752_section65631367111524"></a>

[Table 2](#en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_table44724688204850)  describes the request parameters.

**Table  2**  Request parameters

<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_table44724688204850"></a>
<table><thead align="left"><tr id="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_row1798761204850"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.1"><p id="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_p39560242204918"><a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_p39560242204918"></a><a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_p39560242204918"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.5.1.2"><p id="p1654518298340"><a name="p1654518298340"></a><a name="p1654518298340"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.3"><p id="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_p50263001204918"><a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_p50263001204918"></a><a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_p50263001204918"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.2.5.1.4"><p id="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_p2596798204918"><a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_p2596798204918"></a><a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_p2596798204918"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_row5848663204850"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0092803065_p38460826103157"><a name="en-us_topic_0092803065_p38460826103157"></a><a name="en-us_topic_0092803065_p38460826103157"></a>os-getConsoleOutput</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p054517291342"><a name="p054517291342"></a><a name="p054517291342"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_p1059631204933"><a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_p1059631204933"></a><a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_p1059631204933"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_p40030009204933"><a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_p40030009204933"></a><a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0058745339_p40030009204933"></a>Obtaining ECS management console logs.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  os-getConsoleOutput parameter description

<a name="en-us_topic_0062473752_table1919246111545"></a>
<table><thead align="left"><tr id="en-us_topic_0062473752_row13301030111545"><th class="cellrowborder" valign="top" width="16.73832616738326%" id="mcps1.2.5.1.1"><p id="en-us_topic_0062473752_p4762453511162"><a name="en-us_topic_0062473752_p4762453511162"></a><a name="en-us_topic_0062473752_p4762453511162"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.958204179582044%" id="mcps1.2.5.1.2"><p id="p21255118343"><a name="p21255118343"></a><a name="p21255118343"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.22867713228677%" id="mcps1.2.5.1.3"><p id="en-us_topic_0062473752_p3238214511162"><a name="en-us_topic_0062473752_p3238214511162"></a><a name="en-us_topic_0062473752_p3238214511162"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.07479252074793%" id="mcps1.2.5.1.4"><p id="en-us_topic_0062473752_p5970125811162"><a name="en-us_topic_0062473752_p5970125811162"></a><a name="en-us_topic_0062473752_p5970125811162"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0062473752_row28117068111545"><td class="cellrowborder" valign="top" width="16.73832616738326%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0062473752_p5262467711162"><a name="en-us_topic_0062473752_p5262467711162"></a><a name="en-us_topic_0062473752_p5262467711162"></a>length</p>
</td>
<td class="cellrowborder" valign="top" width="17.958204179582044%" headers="mcps1.2.5.1.2 "><p id="p9126131110342"><a name="p9126131110342"></a><a name="p9126131110342"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.22867713228677%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0062473752_p3474040511162"><a name="en-us_topic_0062473752_p3474040511162"></a><a name="en-us_topic_0062473752_p3474040511162"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52.07479252074793%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0062473752_p3009609811162"><a name="en-us_topic_0062473752_p3009609811162"></a><a name="en-us_topic_0062473752_p3009609811162"></a>Specifies the number of request log rows. The value is greater than or equal to -1, which indicates that the output is not limited.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0062473752_section52662293111617"></a>

None

## Example Request<a name="en-us_topic_0062473752_section1818910413020"></a>

```
POST https://{endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/servers/47e9be4e-a7b9-471f-92d9-ffc83814e07a/action
POST https://{endpoint}/v2.1/9c53a566cb3443ab910cf0daebca90c4/servers/47e9be4e-a7b9-471f-92d9-ffc83814e07a/action
```

```
{
   "os-getConsoleOutput" : {
        "length" : "50"
    }
}
```

## Example Response<a name="section674081414549"></a>

```
{
    "output": "FAKE CONSOLEOUTPUT\nANOTHER\nLAST LINE"
}
```

## Returned Values<a name="en-us_topic_0062473752_section29686359111912"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

