# Querying All API Versions<a name="kms_02_0048"></a>

## Function<a name="en-us_topic_0133150653_section27849192112353"></a>

This API is used to query the API versions.

## URI<a name="en-us_topic_0133150653_section35184599112353"></a>

-   URI format

    GET /

-   Parameter description

    None


## Requests<a name="en-us_topic_0133150653_section12625030112353"></a>

None

## Responses<a name="en-us_topic_0133150653_section15686020"></a>

**Table  1**  Response parameters

<a name="en-us_topic_0133150653_table5856932152840"></a>
<table><thead align="left"><tr id="en-us_topic_0133150653_row5206426152840"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0133150653_p1577110425210"><a name="en-us_topic_0133150653_p1577110425210"></a><a name="en-us_topic_0133150653_p1577110425210"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0133150653_p167751142326"><a name="en-us_topic_0133150653_p167751142326"></a><a name="en-us_topic_0133150653_p167751142326"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0133150653_p157711420214"><a name="en-us_topic_0133150653_p157711420214"></a><a name="en-us_topic_0133150653_p157711420214"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0133150653_p1877644212217"><a name="en-us_topic_0133150653_p1877644212217"></a><a name="en-us_topic_0133150653_p1877644212217"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0133150653_row25652894105355"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150653_p128251240121912"><a name="en-us_topic_0133150653_p128251240121912"></a><a name="en-us_topic_0133150653_p128251240121912"></a>versions</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150653_p158251400193"><a name="en-us_topic_0133150653_p158251400193"></a><a name="en-us_topic_0133150653_p158251400193"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150653_p882504017190"><a name="en-us_topic_0133150653_p882504017190"></a><a name="en-us_topic_0133150653_p882504017190"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150653_p17826740121915"><a name="en-us_topic_0133150653_p17826740121915"></a><a name="en-us_topic_0133150653_p17826740121915"></a>Version object list. For details, see <a href="#en-us_topic_0133150653_table95441953481">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **versions**  field description

<a name="en-us_topic_0133150653_table95441953481"></a>
<table><thead align="left"><tr id="en-us_topic_0133150653_row115453539811"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0133150653_p15458531386"><a name="en-us_topic_0133150653_p15458531386"></a><a name="en-us_topic_0133150653_p15458531386"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0133150653_p3545453286"><a name="en-us_topic_0133150653_p3545453286"></a><a name="en-us_topic_0133150653_p3545453286"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0133150653_p1754512534812"><a name="en-us_topic_0133150653_p1754512534812"></a><a name="en-us_topic_0133150653_p1754512534812"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0133150653_p854518537818"><a name="en-us_topic_0133150653_p854518537818"></a><a name="en-us_topic_0133150653_p854518537818"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0133150653_row195458536817"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150653_p1554518531488"><a name="en-us_topic_0133150653_p1554518531488"></a><a name="en-us_topic_0133150653_p1554518531488"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150653_p5545253783"><a name="en-us_topic_0133150653_p5545253783"></a><a name="en-us_topic_0133150653_p5545253783"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150653_p1954565314813"><a name="en-us_topic_0133150653_p1954565314813"></a><a name="en-us_topic_0133150653_p1954565314813"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150653_p254513531784"><a name="en-us_topic_0133150653_p254513531784"></a><a name="en-us_topic_0133150653_p254513531784"></a>Version number, for example, <span class="parmvalue" id="en-us_topic_0133150653_parmvalue354510531086"><a name="en-us_topic_0133150653_parmvalue354510531086"></a><a name="en-us_topic_0133150653_parmvalue354510531086"></a><b>v1.0</b></span></p>
</td>
</tr>
<tr id="en-us_topic_0133150653_row15545253689"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150653_p1454515538812"><a name="en-us_topic_0133150653_p1454515538812"></a><a name="en-us_topic_0133150653_p1454515538812"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150653_p85458532818"><a name="en-us_topic_0133150653_p85458532818"></a><a name="en-us_topic_0133150653_p85458532818"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150653_p954514531084"><a name="en-us_topic_0133150653_p954514531084"></a><a name="en-us_topic_0133150653_p954514531084"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150653_p145464537810"><a name="en-us_topic_0133150653_p145464537810"></a><a name="en-us_topic_0133150653_p145464537810"></a>JSON object. For details, see <a href="#en-us_topic_0133150653_table525011561381">Table 3</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0133150653_row95461853187"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150653_p85461253489"><a name="en-us_topic_0133150653_p85461253489"></a><a name="en-us_topic_0133150653_p85461253489"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150653_p954620531681"><a name="en-us_topic_0133150653_p954620531681"></a><a name="en-us_topic_0133150653_p954620531681"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150653_p1854612531682"><a name="en-us_topic_0133150653_p1854612531682"></a><a name="en-us_topic_0133150653_p1854612531682"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150653_p75472531982"><a name="en-us_topic_0133150653_p75472531982"></a><a name="en-us_topic_0133150653_p75472531982"></a>If the APIs of this version support microversions, the supported maximum microversion is returned. If the microversion is not supported, empty character string is returned.</p>
</td>
</tr>
<tr id="en-us_topic_0133150653_row135471953984"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150653_p154712531489"><a name="en-us_topic_0133150653_p154712531489"></a><a name="en-us_topic_0133150653_p154712531489"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150653_p654718531887"><a name="en-us_topic_0133150653_p654718531887"></a><a name="en-us_topic_0133150653_p654718531887"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150653_p165472533814"><a name="en-us_topic_0133150653_p165472533814"></a><a name="en-us_topic_0133150653_p165472533814"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150653_p155474531683"><a name="en-us_topic_0133150653_p155474531683"></a><a name="en-us_topic_0133150653_p155474531683"></a>Version status. Valid values are as follows:</p>
<a name="en-us_topic_0133150653_ul165471353081"></a><a name="en-us_topic_0133150653_ul165471353081"></a><ul id="en-us_topic_0133150653_ul165471353081"><li><strong id="en-us_topic_0133150653_b842352706115252"><a name="en-us_topic_0133150653_b842352706115252"></a><a name="en-us_topic_0133150653_b842352706115252"></a>CURRENT</strong>: widely used version</li><li><strong id="en-us_topic_0133150653_b04965131196"><a name="en-us_topic_0133150653_b04965131196"></a><a name="en-us_topic_0133150653_b04965131196"></a>SUPPORTED</strong>: earlier version which is still supported</li><li><strong id="en-us_topic_0133150653_b842352706115458"><a name="en-us_topic_0133150653_b842352706115458"></a><a name="en-us_topic_0133150653_b842352706115458"></a>DEPRECATED</strong>: deprecated version which may be deleted later</li></ul>
</td>
</tr>
<tr id="en-us_topic_0133150653_row25474538818"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150653_p1454719536816"><a name="en-us_topic_0133150653_p1454719536816"></a><a name="en-us_topic_0133150653_p1454719536816"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150653_p105478535815"><a name="en-us_topic_0133150653_p105478535815"></a><a name="en-us_topic_0133150653_p105478535815"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150653_p754765319816"><a name="en-us_topic_0133150653_p754765319816"></a><a name="en-us_topic_0133150653_p754765319816"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150653_p454775318810"><a name="en-us_topic_0133150653_p454775318810"></a><a name="en-us_topic_0133150653_p454775318810"></a>Version release time, which must be UTC time. For example, the release time of v1 is 2014-06-28T12:20:21Z.</p>
</td>
</tr>
<tr id="en-us_topic_0133150653_row65471053388"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150653_p9547253685"><a name="en-us_topic_0133150653_p9547253685"></a><a name="en-us_topic_0133150653_p9547253685"></a>min_version</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150653_p354710531189"><a name="en-us_topic_0133150653_p354710531189"></a><a name="en-us_topic_0133150653_p354710531189"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150653_p554745319813"><a name="en-us_topic_0133150653_p554745319813"></a><a name="en-us_topic_0133150653_p554745319813"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150653_p65471653187"><a name="en-us_topic_0133150653_p65471653187"></a><a name="en-us_topic_0133150653_p65471653187"></a>If the APIs of this version support microversions, the supported minimum microversion is returned. If the microversion is not supported, empty character string is returned.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **links**  field description

<a name="en-us_topic_0133150653_table525011561381"></a>
<table><thead align="left"><tr id="en-us_topic_0133150653_row132503561082"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0133150653_p1625015615811"><a name="en-us_topic_0133150653_p1625015615811"></a><a name="en-us_topic_0133150653_p1625015615811"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0133150653_p125113569815"><a name="en-us_topic_0133150653_p125113569815"></a><a name="en-us_topic_0133150653_p125113569815"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0133150653_p925105618816"><a name="en-us_topic_0133150653_p925105618816"></a><a name="en-us_topic_0133150653_p925105618816"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0133150653_p1325155614816"><a name="en-us_topic_0133150653_p1325155614816"></a><a name="en-us_topic_0133150653_p1325155614816"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0133150653_row202512562089"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150653_p1425115564818"><a name="en-us_topic_0133150653_p1425115564818"></a><a name="en-us_topic_0133150653_p1425115564818"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150653_p92512056884"><a name="en-us_topic_0133150653_p92512056884"></a><a name="en-us_topic_0133150653_p92512056884"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150653_p62518561389"><a name="en-us_topic_0133150653_p62518561389"></a><a name="en-us_topic_0133150653_p62518561389"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150653_p12511566810"><a name="en-us_topic_0133150653_p12511566810"></a><a name="en-us_topic_0133150653_p12511566810"></a>API URL</p>
</td>
</tr>
<tr id="en-us_topic_0133150653_row142511456987"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133150653_p2251165613814"><a name="en-us_topic_0133150653_p2251165613814"></a><a name="en-us_topic_0133150653_p2251165613814"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133150653_p62522566811"><a name="en-us_topic_0133150653_p62522566811"></a><a name="en-us_topic_0133150653_p62522566811"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133150653_p2252145610820"><a name="en-us_topic_0133150653_p2252145610820"></a><a name="en-us_topic_0133150653_p2252145610820"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133150653_p225212561985"><a name="en-us_topic_0133150653_p225212561985"></a><a name="en-us_topic_0133150653_p225212561985"></a>The default value is <strong id="en-us_topic_0133150653_b555016171571"><a name="en-us_topic_0133150653_b555016171571"></a><a name="en-us_topic_0133150653_b555016171571"></a>self</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0133150653_section12491816289"></a>

The following describes how to query the version information.

-   Example request

    None

-   Example response

    ```
    { 
       "versions":
        [
            {
                "id":"v1.0",
                "links":
                [
                    {
                        
                        "href":"https://kms.eu-de.otc.t-systems.com/v1.0/",
                        "rel":"self"
                    }
                ],
                "min_version":"",
                "status":"CURRENT",
                "version":"",
                "updated":"2018-09-05T08:18:05Z"
            }
        ]
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


## Status Codes<a name="en-us_topic_0133150653_section3454223421"></a>

[Table 4](#en-us_topic_0133150653_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  4**  Status codes

<a name="en-us_topic_0133150653_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0133150653_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0133150653_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0133150653_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0133150653_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0133150653_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0133150653_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0133150653_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0133150653_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0133150653_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0133150653_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0133150653_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0133150653_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0133150653_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0133150653_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0133150653_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0133150653_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0133150653_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0133150653_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0133150653_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0133150653_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

