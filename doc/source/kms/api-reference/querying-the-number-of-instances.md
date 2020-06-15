# Querying the Number of Instances<a name="kms_02_0024"></a>

## Function<a name="en-us_topic_0112992320_section27849192112353"></a>

This API is used to query the number of instances, that is, the number of CMKs created.

>![](/images/icon-note.gif) **NOTE:**   
>Default Master Keys are automatically created by services and are not included in this query.  

## URI<a name="en-us_topic_0112992320_section35184599112353"></a>

-   URI format

    GET /v1.0/\{project\_id\}/kms/user-instances

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992320_table63109676112353"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992320_row49827042112353"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992320_p9458563112353"><a name="en-us_topic_0112992320_p9458563112353"></a><a name="en-us_topic_0112992320_p9458563112353"></a><strong id="en-us_topic_0112992320_b842352706185937"><a name="en-us_topic_0112992320_b842352706185937"></a><a name="en-us_topic_0112992320_b842352706185937"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992320_p27946133112353"><a name="en-us_topic_0112992320_p27946133112353"></a><a name="en-us_topic_0112992320_p27946133112353"></a><strong id="en-us_topic_0112992320_b842352706185940"><a name="en-us_topic_0112992320_b842352706185940"></a><a name="en-us_topic_0112992320_b842352706185940"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.55%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992320_p49044287112353"><a name="en-us_topic_0112992320_p49044287112353"></a><a name="en-us_topic_0112992320_p49044287112353"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.79%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992320_p13164330112353"><a name="en-us_topic_0112992320_p13164330112353"></a><a name="en-us_topic_0112992320_p13164330112353"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992320_row59677822112353"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992320_p2065377112353"><a name="en-us_topic_0112992320_p2065377112353"></a><a name="en-us_topic_0112992320_p2065377112353"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992320_p33077886112353"><a name="en-us_topic_0112992320_p33077886112353"></a><a name="en-us_topic_0112992320_p33077886112353"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992320_p62063099112353"><a name="en-us_topic_0112992320_p62063099112353"></a><a name="en-us_topic_0112992320_p62063099112353"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992320_p61055104112353"><a name="en-us_topic_0112992320_p61055104112353"></a><a name="en-us_topic_0112992320_p61055104112353"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992320_section12625030112353"></a>

None

## Responses<a name="en-us_topic_0112992320_section15686020"></a>

**Table  2**  Response parameters

<a name="en-us_topic_0112992320_table5856932152840"></a>
<table><thead align="left"><tr id="en-us_topic_0112992320_row5206426152840"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992320_p19067323152840"><a name="en-us_topic_0112992320_p19067323152840"></a><a name="en-us_topic_0112992320_p19067323152840"></a><strong id="en-us_topic_0112992320_b8423527061909"><a name="en-us_topic_0112992320_b8423527061909"></a><a name="en-us_topic_0112992320_b8423527061909"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992320_p9786487152840"><a name="en-us_topic_0112992320_p9786487152840"></a><a name="en-us_topic_0112992320_p9786487152840"></a><strong id="en-us_topic_0112992320_b84235270619014"><a name="en-us_topic_0112992320_b84235270619014"></a><a name="en-us_topic_0112992320_b84235270619014"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992320_p949325152840"><a name="en-us_topic_0112992320_p949325152840"></a><a name="en-us_topic_0112992320_p949325152840"></a><strong id="en-us_topic_0112992320_b84235270619012"><a name="en-us_topic_0112992320_b84235270619012"></a><a name="en-us_topic_0112992320_b84235270619012"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992320_p54508002152840"><a name="en-us_topic_0112992320_p54508002152840"></a><a name="en-us_topic_0112992320_p54508002152840"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992320_row25652894105355"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992320_p9370319112738"><a name="en-us_topic_0112992320_p9370319112738"></a><a name="en-us_topic_0112992320_p9370319112738"></a>instance_num</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992320_p6949493112738"><a name="en-us_topic_0112992320_p6949493112738"></a><a name="en-us_topic_0112992320_p6949493112738"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992320_p20798408112738"><a name="en-us_topic_0112992320_p20798408112738"></a><a name="en-us_topic_0112992320_p20798408112738"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992320_p26038079112738"><a name="en-us_topic_0112992320_p26038079112738"></a><a name="en-us_topic_0112992320_p26038079112738"></a>Number of non-default CMKs</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992320_section12491816289"></a>

-   Example request

    None

-   Example response

    ```
    { 
        "instance_num": 15
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


## Status Codes<a name="en-us_topic_0112992320_section3454223421"></a>

[Table 3](#en-us_topic_0112992320_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  3**  Status codes

<a name="en-us_topic_0112992320_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992320_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992320_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992320_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992320_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992320_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992320_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992320_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992320_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992320_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992320_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992320_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992320_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992320_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992320_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992320_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992320_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992320_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992320_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992320_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992320_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

