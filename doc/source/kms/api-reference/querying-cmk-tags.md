# Querying CMK Tags<a name="kms_02_0043"></a>

## Function<a name="en-us_topic_0112992321_section1176242255117"></a>

This API allows you to query tags of a specified CMK.

TMS may use this API to query all tags of a specified CMK.

## URI<a name="en-us_topic_0112992321_section1227165345118"></a>

-   URI format

    GET /v1.0/\{project\_id\}/kms/\{key\_id\}/tags

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992321_table68661454102512"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992321_row386465419250"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992321_p2739096916511"><a name="en-us_topic_0112992321_p2739096916511"></a><a name="en-us_topic_0112992321_p2739096916511"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992321_p407603016511"><a name="en-us_topic_0112992321_p407603016511"></a><a name="en-us_topic_0112992321_p407603016511"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992321_p6172299916511"><a name="en-us_topic_0112992321_p6172299916511"></a><a name="en-us_topic_0112992321_p6172299916511"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992321_p3350702116511"><a name="en-us_topic_0112992321_p3350702116511"></a><a name="en-us_topic_0112992321_p3350702116511"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992321_row88669548255"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992321_p15864185413256"><a name="en-us_topic_0112992321_p15864185413256"></a><a name="en-us_topic_0112992321_p15864185413256"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992321_p10866105462516"><a name="en-us_topic_0112992321_p10866105462516"></a><a name="en-us_topic_0112992321_p10866105462516"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992321_p182521751910"><a name="en-us_topic_0112992321_p182521751910"></a><a name="en-us_topic_0112992321_p182521751910"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992321_p18866154122512"><a name="en-us_topic_0112992321_p18866154122512"></a><a name="en-us_topic_0112992321_p18866154122512"></a>Project ID</p>
    </td>
    </tr>
    <tr id="en-us_topic_0112992321_row7866105411259"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992321_p188661354122516"><a name="en-us_topic_0112992321_p188661354122516"></a><a name="en-us_topic_0112992321_p188661354122516"></a>key_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992321_p1386615452516"><a name="en-us_topic_0112992321_p1386615452516"></a><a name="en-us_topic_0112992321_p1386615452516"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992321_p142756516912"><a name="en-us_topic_0112992321_p142756516912"></a><a name="en-us_topic_0112992321_p142756516912"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992321_p5866175412520"><a name="en-us_topic_0112992321_p5866175412520"></a><a name="en-us_topic_0112992321_p5866175412520"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992321_parmvalue80435593163333"><a name="en-us_topic_0112992321_parmvalue80435593163333"></a><a name="en-us_topic_0112992321_parmvalue80435593163333"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
    <p id="en-us_topic_0112992321_p58662544251"><a name="en-us_topic_0112992321_p58662544251"></a><a name="en-us_topic_0112992321_p58662544251"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992321_section11363185405213"></a>

None

## Responses<a name="en-us_topic_0112992321_section353620935319"></a>

**Table  2**  Response parameters

<a name="en-us_topic_0112992321_table198991847173016"></a>
<table><thead align="left"><tr id="en-us_topic_0112992321_row11899184723019"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992321_p834764110575"><a name="en-us_topic_0112992321_p834764110575"></a><a name="en-us_topic_0112992321_p834764110575"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992321_p3347144155718"><a name="en-us_topic_0112992321_p3347144155718"></a><a name="en-us_topic_0112992321_p3347144155718"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992321_p3347194175717"><a name="en-us_topic_0112992321_p3347194175717"></a><a name="en-us_topic_0112992321_p3347194175717"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992321_p1347194120578"><a name="en-us_topic_0112992321_p1347194120578"></a><a name="en-us_topic_0112992321_p1347194120578"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992321_row78993471306"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992321_p789910477301"><a name="en-us_topic_0112992321_p789910477301"></a><a name="en-us_topic_0112992321_p789910477301"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992321_p19899204713015"><a name="en-us_topic_0112992321_p19899204713015"></a><a name="en-us_topic_0112992321_p19899204713015"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992321_p138991147153014"><a name="en-us_topic_0112992321_p138991147153014"></a><a name="en-us_topic_0112992321_p138991147153014"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0112992321_p3215143810421"><a name="en-us_topic_0112992321_p3215143810421"></a><a name="en-us_topic_0112992321_p3215143810421"></a>list of tags, including tag keys and tag values.<a name="en-us_topic_0112992321_ul17835144253711"></a><a name="en-us_topic_0112992321_ul17835144253711"></a><ul id="en-us_topic_0112992321_ul17835144253711"><li><strong id="en-us_topic_0112992321_b842352706165737"><a name="en-us_topic_0112992321_b842352706165737"></a><a name="en-us_topic_0112992321_b842352706165737"></a>key</strong> indicates the tag key. A CMK can have a maximum of 10 keys, and each of them is unique and cannot be empty. A key cannot have duplicate values. The value of <strong id="en-us_topic_0112992321_b842352706165433"><a name="en-us_topic_0112992321_b842352706165433"></a><a name="en-us_topic_0112992321_b842352706165433"></a>key</strong> contains a maximum of 36 characters.</li><li><strong id="en-us_topic_0112992321_b842352706165447"><a name="en-us_topic_0112992321_b842352706165447"></a><a name="en-us_topic_0112992321_b842352706165447"></a>value</strong> indicates the tag value. Each tag value can contain a maximum of 43 characters. The relationship between values is <strong id="en-us_topic_0112992321_b842352706165526"><a name="en-us_topic_0112992321_b842352706165526"></a><a name="en-us_topic_0112992321_b842352706165526"></a>AND</strong>.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0112992321_row3937146994858"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992321_p3497239294858"><a name="en-us_topic_0112992321_p3497239294858"></a><a name="en-us_topic_0112992321_p3497239294858"></a>existTagNum</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992321_p866149694858"><a name="en-us_topic_0112992321_p866149694858"></a><a name="en-us_topic_0112992321_p866149694858"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992321_p1419150894858"><a name="en-us_topic_0112992321_p1419150894858"></a><a name="en-us_topic_0112992321_p1419150894858"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992321_p3049260594858"><a name="en-us_topic_0112992321_p3049260594858"></a><a name="en-us_topic_0112992321_p3049260594858"></a>Number of key tags.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992321_section13892161018553"></a>

The following example describes how to query CMK tags.

-   Example request

    None

-   Example response

    ```
    {         "tags": [
               {
                "key": "key1",
                "value": "value1"
               },
               {
                "key": "key2",
                "value": "value3"
               }
               ],
               "existTagsNum":2 
    }
    ```

    or

    ```
    {     
            "error": {        
                  "error_code": "KMS.XXXX",         
                  "error_msg": "XXX"    
              } 
     }
    ```


## Status Codes<a name="en-us_topic_0112992321_section192111133389"></a>

[Table 3](#en-us_topic_0112992321_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  3**  Status codes

<a name="en-us_topic_0112992321_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992321_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992321_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992321_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992321_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992321_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992321_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992321_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992321_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992321_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992321_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992321_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992321_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992321_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992321_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992321_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992321_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992321_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992321_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992321_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992321_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

