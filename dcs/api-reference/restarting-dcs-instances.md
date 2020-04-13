# Restarting DCS Instances<a name="EN-US_TOPIC_0237964365"></a>

## Function<a name="section29579387"></a>

This API is used to restart DCS instances.

## URI<a name="section64887899"></a>

-   URI format:

    PUT /v1.0/\{project\_id\}/instances/status

-   Parameter description:

    [Table 1](#table50009058)  describes the parameter of this API.


**Table  1**  Parameter description

<a name="table50009058"></a>
<table><thead align="left"><tr id="row19077772"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p1795723"><a name="p1795723"></a><a name="p1795723"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p11235870"><a name="p11235870"></a><a name="p11235870"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p37690286"><a name="p37690286"></a><a name="p37690286"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p33014306"><a name="p33014306"></a><a name="p33014306"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row56913123"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p46560216"><a name="p46560216"></a><a name="p46560216"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p13281129"><a name="p13281129"></a><a name="p13281129"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p2029696"><a name="p2029696"></a><a name="p2029696"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p30187650"><a name="p30187650"></a><a name="p30187650"></a>Project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section47120180"></a>

-   Request parameter:

    [Table 2](#table47428342)  describes request parameters.


**Table  2**  Parameter description

<a name="table47428342"></a>
<table><thead align="left"><tr id="row30161299"><th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.5.1.1"><p id="p27146137"><a name="p27146137"></a><a name="p27146137"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.2.5.1.2"><p id="p51353525"><a name="p51353525"></a><a name="p51353525"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.5.1.3"><p id="p65994828"><a name="p65994828"></a><a name="p65994828"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="32.323232323232325%" id="mcps1.2.5.1.4"><p id="p43980872"><a name="p43980872"></a><a name="p43980872"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5680913"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.1 "><p id="p57500814"><a name="p57500814"></a><a name="p57500814"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.2 "><p id="p27054376"><a name="p27054376"></a><a name="p27054376"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.3 "><p id="p43920838"><a name="p43920838"></a><a name="p43920838"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="32.323232323232325%" headers="mcps1.2.5.1.4 "><p id="p818129"><a name="p818129"></a><a name="p818129"></a>Action performed on DCS instances.</p>
<p id="p7363162"><a name="p7363162"></a><a name="p7363162"></a>Options: restart.</p>
</td>
</tr>
<tr id="row66268464"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.1 "><p id="p66145356"><a name="p66145356"></a><a name="p66145356"></a>instances</p>
</td>
<td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.2.5.1.2 "><p id="p56173580"><a name="p56173580"></a><a name="p56173580"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.3 "><p id="p53766104"><a name="p53766104"></a><a name="p53766104"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="32.323232323232325%" headers="mcps1.2.5.1.4 "><p id="p60087193"><a name="p60087193"></a><a name="p60087193"></a>List of DCS instance IDs.</p>
</td>
</tr>
</tbody>
</table>

-   Example request:

    ```
    { 
     "action": "restart", 
     "instances": [ 
            "2e803f66-fbb0-47ad-b6cb-fb87f5bed4ef" 
     ] 
    }
    ```


## Response<a name="section21428441"></a>

-   Status code:

    If status code "200 OK" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    [Table 3](#table24201902)  describes the response parameter.


**Table  3**  Parameter description

<a name="table24201902"></a>
<table><thead align="left"><tr id="row27302557"><th class="cellrowborder" valign="top" width="19.19191919191919%" id="mcps1.2.4.1.1"><p id="p64023541"><a name="p64023541"></a><a name="p64023541"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p18524317"><a name="p18524317"></a><a name="p18524317"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.474747474747474%" id="mcps1.2.4.1.3"><p id="p24074685"><a name="p24074685"></a><a name="p24074685"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3892478"><td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.4.1.1 "><p id="p46855303"><a name="p46855303"></a><a name="p46855303"></a>results</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p37183233"><a name="p37183233"></a><a name="p37183233"></a>Array.</p>
<p id="p66213648"><a name="p66213648"></a><a name="p66213648"></a>For details, see <a href="#ref478571394">Table 4</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="47.474747474747474%" headers="mcps1.2.4.1.3 "><p id="p18476519"><a name="p18476519"></a><a name="p18476519"></a>An indicator of whether the action is performed successfully.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Parameter description of the results array

<a name="ref478571394"></a>
<table><thead align="left"><tr id="row45092695"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.1"><p id="p28629701"><a name="p28629701"></a><a name="p28629701"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p37304419"><a name="p37304419"></a><a name="p37304419"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63%" id="mcps1.2.4.1.3"><p id="p1759065"><a name="p1759065"></a><a name="p1759065"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8266576"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p65612911"><a name="p65612911"></a><a name="p65612911"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p13045599"><a name="p13045599"></a><a name="p13045599"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p50060616"><a name="p50060616"></a><a name="p50060616"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row47892361"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.1 "><p id="p54075993"><a name="p54075993"></a><a name="p54075993"></a>result</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p18079285"><a name="p18079285"></a><a name="p18079285"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63%" headers="mcps1.2.4.1.3 "><p id="p55136006"><a name="p55136006"></a><a name="p55136006"></a>An indicator of whether the action is performed successfully for the DCS instance.</p>
<p id="p26462014"><a name="p26462014"></a><a name="p26462014"></a>Options: success and failed.</p>
</td>
</tr>
</tbody>
</table>

-   Example response:

    ```
    { 
     "results": [ 
            { 
                "result": "success", 
                "instance": "2e803f66-fbb0-47ad-b6cb-fb87f5bed4ef" 
            } 
     ] 
    }
    ```


