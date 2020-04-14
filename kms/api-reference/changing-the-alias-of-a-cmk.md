# Changing the Alias of a CMK<a name="kms_02_0026"></a>

## Function<a name="en-us_topic_0112992307_section6685482991125"></a>

This API enables you to change the alias of a CMK.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   A Default Master Key \(the alias suffix of which is  **/default**\) does not allow alias changes.  
>-   A CMK in  **Scheduled deletion**  status does not allow alias changes.  

## URI<a name="en-us_topic_0112992307_section3191906891125"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/update-key-alias

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992307_table6116459691125"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992307_row2741617991125"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992307_p611804291125"><a name="en-us_topic_0112992307_p611804291125"></a><a name="en-us_topic_0112992307_p611804291125"></a><strong id="en-us_topic_0112992307_b84235270619643"><a name="en-us_topic_0112992307_b84235270619643"></a><a name="en-us_topic_0112992307_b84235270619643"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992307_p2579942291125"><a name="en-us_topic_0112992307_p2579942291125"></a><a name="en-us_topic_0112992307_p2579942291125"></a><strong id="en-us_topic_0112992307_b84235270619645"><a name="en-us_topic_0112992307_b84235270619645"></a><a name="en-us_topic_0112992307_b84235270619645"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.55%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992307_p937843891125"><a name="en-us_topic_0112992307_p937843891125"></a><a name="en-us_topic_0112992307_p937843891125"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.79%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992307_p2145602791125"><a name="en-us_topic_0112992307_p2145602791125"></a><a name="en-us_topic_0112992307_p2145602791125"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992307_row6021661291125"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992307_p4570740291125"><a name="en-us_topic_0112992307_p4570740291125"></a><a name="en-us_topic_0112992307_p4570740291125"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992307_p1131205291125"><a name="en-us_topic_0112992307_p1131205291125"></a><a name="en-us_topic_0112992307_p1131205291125"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992307_p4386100291125"><a name="en-us_topic_0112992307_p4386100291125"></a><a name="en-us_topic_0112992307_p4386100291125"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992307_p6308031091125"><a name="en-us_topic_0112992307_p6308031091125"></a><a name="en-us_topic_0112992307_p6308031091125"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992307_section3085187891125"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992307_table6419419691821"></a>
<table><thead align="left"><tr id="en-us_topic_0112992307_row3033405791821"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992307_p4113955391821"><a name="en-us_topic_0112992307_p4113955391821"></a><a name="en-us_topic_0112992307_p4113955391821"></a><strong id="en-us_topic_0112992307_b493609562"><a name="en-us_topic_0112992307_b493609562"></a><a name="en-us_topic_0112992307_b493609562"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992307_p476054391821"><a name="en-us_topic_0112992307_p476054391821"></a><a name="en-us_topic_0112992307_p476054391821"></a><strong id="en-us_topic_0112992307_b84235270619717"><a name="en-us_topic_0112992307_b84235270619717"></a><a name="en-us_topic_0112992307_b84235270619717"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992307_p4396951091821"><a name="en-us_topic_0112992307_p4396951091821"></a><a name="en-us_topic_0112992307_p4396951091821"></a><strong id="en-us_topic_0112992307_b84235270619712"><a name="en-us_topic_0112992307_b84235270619712"></a><a name="en-us_topic_0112992307_b84235270619712"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992307_p5005970191821"><a name="en-us_topic_0112992307_p5005970191821"></a><a name="en-us_topic_0112992307_p5005970191821"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992307_row2830395191821"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992307_p3801801143225"><a name="en-us_topic_0112992307_p3801801143225"></a><a name="en-us_topic_0112992307_p3801801143225"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992307_p46233878143225"><a name="en-us_topic_0112992307_p46233878143225"></a><a name="en-us_topic_0112992307_p46233878143225"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992307_p7551153620218"><a name="en-us_topic_0112992307_p7551153620218"></a><a name="en-us_topic_0112992307_p7551153620218"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992307_p53956617143225"><a name="en-us_topic_0112992307_p53956617143225"></a><a name="en-us_topic_0112992307_p53956617143225"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992307_parmvalue80435593163333"><a name="en-us_topic_0112992307_parmvalue80435593163333"></a><a name="en-us_topic_0112992307_parmvalue80435593163333"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
<p id="en-us_topic_0112992307_p10107472143225"><a name="en-us_topic_0112992307_p10107472143225"></a><a name="en-us_topic_0112992307_p10107472143225"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
</td>
</tr>
<tr id="en-us_topic_0112992307_row601748291821"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992307_p13453928143217"><a name="en-us_topic_0112992307_p13453928143217"></a><a name="en-us_topic_0112992307_p13453928143217"></a>key_alias</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992307_p23067306143217"><a name="en-us_topic_0112992307_p23067306143217"></a><a name="en-us_topic_0112992307_p23067306143217"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992307_p744193816210"><a name="en-us_topic_0112992307_p744193816210"></a><a name="en-us_topic_0112992307_p744193816210"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992307_p56512465143217"><a name="en-us_topic_0112992307_p56512465143217"></a><a name="en-us_topic_0112992307_p56512465143217"></a>Alias of a CMK whose length is 1 to 255 characters and which matches the regular expression <strong id="en-us_topic_0112992307_b842352706112538"><a name="en-us_topic_0112992307_b842352706112538"></a><a name="en-us_topic_0112992307_b842352706112538"></a>^[a-zA-Z0-9:/_-]{1,255}$</strong>. Suffix of the alias cannot be <strong id="en-us_topic_0112992307_b842352706112556"><a name="en-us_topic_0112992307_b842352706112556"></a><a name="en-us_topic_0112992307_b842352706112556"></a>/default</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0112992307_row315093291821"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992307_p5389896591821"><a name="en-us_topic_0112992307_p5389896591821"></a><a name="en-us_topic_0112992307_p5389896591821"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992307_p3451131791821"><a name="en-us_topic_0112992307_p3451131791821"></a><a name="en-us_topic_0112992307_p3451131791821"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992307_p4126174020210"><a name="en-us_topic_0112992307_p4126174020210"></a><a name="en-us_topic_0112992307_p4126174020210"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992307_p13154914142714"><a name="en-us_topic_0112992307_p13154914142714"></a><a name="en-us_topic_0112992307_p13154914142714"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992307_p4395331691821"><a name="en-us_topic_0112992307_p4395331691821"></a><a name="en-us_topic_0112992307_p4395331691821"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992307_section955024991125"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0112992307_table4661953591125"></a>
<table><thead align="left"><tr id="en-us_topic_0112992307_row5741486791125"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992307_p2009266891125"><a name="en-us_topic_0112992307_p2009266891125"></a><a name="en-us_topic_0112992307_p2009266891125"></a><strong id="en-us_topic_0112992307_b84235270619742"><a name="en-us_topic_0112992307_b84235270619742"></a><a name="en-us_topic_0112992307_b84235270619742"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992307_p2618658291125"><a name="en-us_topic_0112992307_p2618658291125"></a><a name="en-us_topic_0112992307_p2618658291125"></a><strong id="en-us_topic_0112992307_b84235270619748"><a name="en-us_topic_0112992307_b84235270619748"></a><a name="en-us_topic_0112992307_b84235270619748"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992307_p1689338191125"><a name="en-us_topic_0112992307_p1689338191125"></a><a name="en-us_topic_0112992307_p1689338191125"></a><strong id="en-us_topic_0112992307_b84235270619745"><a name="en-us_topic_0112992307_b84235270619745"></a><a name="en-us_topic_0112992307_b84235270619745"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992307_p4073839291125"><a name="en-us_topic_0112992307_p4073839291125"></a><a name="en-us_topic_0112992307_p4073839291125"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992307_row1147544291125"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992307_p708028792054"><a name="en-us_topic_0112992307_p708028792054"></a><a name="en-us_topic_0112992307_p708028792054"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992307_p1443169492054"><a name="en-us_topic_0112992307_p1443169492054"></a><a name="en-us_topic_0112992307_p1443169492054"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992307_p46508422023"><a name="en-us_topic_0112992307_p46508422023"></a><a name="en-us_topic_0112992307_p46508422023"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992307_p2811658392054"><a name="en-us_topic_0112992307_p2811658392054"></a><a name="en-us_topic_0112992307_p2811658392054"></a>CMK ID</p>
</td>
</tr>
<tr id="en-us_topic_0112992307_row5657868491125"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992307_p2878556892054"><a name="en-us_topic_0112992307_p2878556892054"></a><a name="en-us_topic_0112992307_p2878556892054"></a>key_alias</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992307_p1776938992054"><a name="en-us_topic_0112992307_p1776938992054"></a><a name="en-us_topic_0112992307_p1776938992054"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992307_p488214441922"><a name="en-us_topic_0112992307_p488214441922"></a><a name="en-us_topic_0112992307_p488214441922"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992307_p3003444392054"><a name="en-us_topic_0112992307_p3003444392054"></a><a name="en-us_topic_0112992307_p3003444392054"></a>Alias of a CMK</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992307_section32834116430"></a>

The following is an example about how to modify a CMK whose alias ID is  **bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e**  and alias is  **test**.

-   Example request

    ```
    {
        "key_alias": "test",      
        "key_id": "bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e"
    }
    ```

-   Example response

    ```
    {
        "key_info": {           
            "key_id": "bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e",
            "key_alias": "test"
         }
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


## Status Codes<a name="en-us_topic_0112992307_section3454223421"></a>

[Table 4](#en-us_topic_0112992307_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  4**  Status codes

<a name="en-us_topic_0112992307_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992307_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992307_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992307_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992307_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992307_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992307_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992307_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992307_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992307_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992307_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992307_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992307_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992307_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992307_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992307_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992307_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992307_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992307_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992307_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992307_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

