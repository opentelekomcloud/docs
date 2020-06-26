# Querying Project Tags<a name="kms_02_0044"></a>

## Function<a name="en-us_topic_0112992316_section396540155814"></a>

This API enables you to query all tag sets of a specified project.

## URI<a name="en-us_topic_0112992316_section45111117115918"></a>

-   URI format

    GET /v1.0/\{project\_id\}/kms/tags

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992316_table5241461905"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992316_row42402064012"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992316_p202401061602"><a name="en-us_topic_0112992316_p202401061602"></a><a name="en-us_topic_0112992316_p202401061602"></a><strong id="en-us_topic_0112992316_b842352706202545"><a name="en-us_topic_0112992316_b842352706202545"></a><a name="en-us_topic_0112992316_b842352706202545"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.02%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992316_p0240763013"><a name="en-us_topic_0112992316_p0240763013"></a><a name="en-us_topic_0112992316_p0240763013"></a><strong id="en-us_topic_0112992316_b842352706202614_1"><a name="en-us_topic_0112992316_b842352706202614_1"></a><a name="en-us_topic_0112992316_b842352706202614_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992316_p32401367016"><a name="en-us_topic_0112992316_p32401367016"></a><a name="en-us_topic_0112992316_p32401367016"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992316_p172401161700"><a name="en-us_topic_0112992316_p172401161700"></a><a name="en-us_topic_0112992316_p172401161700"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992316_row7241766019"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992316_p1424046504"><a name="en-us_topic_0112992316_p1424046504"></a><a name="en-us_topic_0112992316_p1424046504"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.02%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992316_p4241176705"><a name="en-us_topic_0112992316_p4241176705"></a><a name="en-us_topic_0112992316_p4241176705"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992316_p4386100291125"><a name="en-us_topic_0112992316_p4386100291125"></a><a name="en-us_topic_0112992316_p4386100291125"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992316_p142411260018"><a name="en-us_topic_0112992316_p142411260018"></a><a name="en-us_topic_0112992316_p142411260018"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992316_section2099414217011"></a>

None

## Responses<a name="en-us_topic_0112992316_section8148203216011"></a>

**Table  2**  Response parameters

<a name="en-us_topic_0112992316_table17789425210"></a>
<table><thead align="left"><tr id="en-us_topic_0112992316_row077610421225"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992316_p1577110425210"><a name="en-us_topic_0112992316_p1577110425210"></a><a name="en-us_topic_0112992316_p1577110425210"></a><strong id="en-us_topic_0112992316_b905946974"><a name="en-us_topic_0112992316_b905946974"></a><a name="en-us_topic_0112992316_b905946974"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992316_p167751142326"><a name="en-us_topic_0112992316_p167751142326"></a><a name="en-us_topic_0112992316_p167751142326"></a><strong id="en-us_topic_0112992316_b842352706202614_3"><a name="en-us_topic_0112992316_b842352706202614_3"></a><a name="en-us_topic_0112992316_b842352706202614_3"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992316_p157711420214"><a name="en-us_topic_0112992316_p157711420214"></a><a name="en-us_topic_0112992316_p157711420214"></a><strong id="en-us_topic_0112992316_b842352706202612"><a name="en-us_topic_0112992316_b842352706202612"></a><a name="en-us_topic_0112992316_b842352706202612"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992316_p1877644212217"><a name="en-us_topic_0112992316_p1877644212217"></a><a name="en-us_topic_0112992316_p1877644212217"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992316_row13778742121"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992316_p377634219218"><a name="en-us_topic_0112992316_p377634219218"></a><a name="en-us_topic_0112992316_p377634219218"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992316_p11777642424"><a name="en-us_topic_0112992316_p11777642424"></a><a name="en-us_topic_0112992316_p11777642424"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992316_p776212466137"><a name="en-us_topic_0112992316_p776212466137"></a><a name="en-us_topic_0112992316_p776212466137"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0112992316_p2811222164320"><a name="en-us_topic_0112992316_p2811222164320"></a><a name="en-us_topic_0112992316_p2811222164320"></a>list of tags, including tag keys and tag values.<a name="en-us_topic_0112992316_ul17835144253711"></a><a name="en-us_topic_0112992316_ul17835144253711"></a><ul id="en-us_topic_0112992316_ul17835144253711"><li><strong id="en-us_topic_0112992316_b842352706165737"><a name="en-us_topic_0112992316_b842352706165737"></a><a name="en-us_topic_0112992316_b842352706165737"></a>key</strong> indicates the tag key. A CMK can have a maximum of 10 keys, and each of them is unique and cannot be empty. A key cannot have duplicate values. The value of <strong id="en-us_topic_0112992316_b842352706165433"><a name="en-us_topic_0112992316_b842352706165433"></a><a name="en-us_topic_0112992316_b842352706165433"></a>key</strong> contains a maximum of 36 characters.</li><li><strong id="en-us_topic_0112992316_b842352706165447"><a name="en-us_topic_0112992316_b842352706165447"></a><a name="en-us_topic_0112992316_b842352706165447"></a>value</strong> indicates the tag value. Each tag value can contain a maximum of 43 characters. The relationship between values is <strong id="en-us_topic_0112992316_b842352706165526"><a name="en-us_topic_0112992316_b842352706165526"></a><a name="en-us_topic_0112992316_b842352706165526"></a>AND</strong>.</li></ul>
</div>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992316_section12430172338"></a>

The following example describes how to query project tags.

-   Example request

    None

-   Example response

    ```
    {            "tags": [
                 { 
                   "key": "key1",
                   "values": [
                       "value1",
                       "value2"
                     ]
                  },
                 {
                   "key": "key2",
                   "values": [
                       "value1",
                       "value2"
                    ]
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


## Status Codes<a name="en-us_topic_0112992316_section192111133389"></a>

[Table 3](#en-us_topic_0112992316_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  3**  Status codes

<a name="en-us_topic_0112992316_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992316_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992316_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992316_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992316_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992316_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992316_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992316_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992316_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992316_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992316_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992316_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992316_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992316_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992316_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992316_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992316_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992316_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992316_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992316_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992316_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

