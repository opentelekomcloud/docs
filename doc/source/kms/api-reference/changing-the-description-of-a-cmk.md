# Changing the Description of a CMK<a name="kms_02_0027"></a>

## Function<a name="en-us_topic_0112992285_section6685482991125"></a>

This API enables you to change the description of a CMK.

>![](/images/icon-note.gif) **NOTE:**   
>-   A Default Master Key \(the alias suffix of which is  **/default**\) does not allow alias changes.  
>-   A CMK in  **Scheduled deletion**  status does not allow description changes.  

## URI<a name="en-us_topic_0112992285_section3191906891125"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/update-key-description

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992285_table6116459691125"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992285_row2741617991125"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992285_p611804291125"><a name="en-us_topic_0112992285_p611804291125"></a><a name="en-us_topic_0112992285_p611804291125"></a><strong id="en-us_topic_0112992285_b84235270619104"><a name="en-us_topic_0112992285_b84235270619104"></a><a name="en-us_topic_0112992285_b84235270619104"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992285_p2579942291125"><a name="en-us_topic_0112992285_p2579942291125"></a><a name="en-us_topic_0112992285_p2579942291125"></a><strong id="en-us_topic_0112992285_b84235270619106"><a name="en-us_topic_0112992285_b84235270619106"></a><a name="en-us_topic_0112992285_b84235270619106"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.55%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992285_p937843891125"><a name="en-us_topic_0112992285_p937843891125"></a><a name="en-us_topic_0112992285_p937843891125"></a><strong id="en-us_topic_0112992285_b84235270619109"><a name="en-us_topic_0112992285_b84235270619109"></a><a name="en-us_topic_0112992285_b84235270619109"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40.79%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992285_p2145602791125"><a name="en-us_topic_0112992285_p2145602791125"></a><a name="en-us_topic_0112992285_p2145602791125"></a><strong id="en-us_topic_0112992285_b842352706191013"><a name="en-us_topic_0112992285_b842352706191013"></a><a name="en-us_topic_0112992285_b842352706191013"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992285_row6021661291125"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992285_p4570740291125"><a name="en-us_topic_0112992285_p4570740291125"></a><a name="en-us_topic_0112992285_p4570740291125"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992285_p1131205291125"><a name="en-us_topic_0112992285_p1131205291125"></a><a name="en-us_topic_0112992285_p1131205291125"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992285_p17684501212"><a name="en-us_topic_0112992285_p17684501212"></a><a name="en-us_topic_0112992285_p17684501212"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992285_p6308031091125"><a name="en-us_topic_0112992285_p6308031091125"></a><a name="en-us_topic_0112992285_p6308031091125"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992285_section3085187891125"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992285_table6419419691821"></a>
<table><thead align="left"><tr id="en-us_topic_0112992285_row3033405791821"><th class="cellrowborder" valign="top" width="22.447755224477554%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992285_p4113955391821"><a name="en-us_topic_0112992285_p4113955391821"></a><a name="en-us_topic_0112992285_p4113955391821"></a><strong id="en-us_topic_0112992285_b842352706191032"><a name="en-us_topic_0112992285_b842352706191032"></a><a name="en-us_topic_0112992285_b842352706191032"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.308469153084694%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992285_p4396951091821"><a name="en-us_topic_0112992285_p4396951091821"></a><a name="en-us_topic_0112992285_p4396951091821"></a><strong id="en-us_topic_0112992285_b842352706191035"><a name="en-us_topic_0112992285_b842352706191035"></a><a name="en-us_topic_0112992285_b842352706191035"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.36816318368163%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992285_p476054391821"><a name="en-us_topic_0112992285_p476054391821"></a><a name="en-us_topic_0112992285_p476054391821"></a><strong id="en-us_topic_0112992285_b842352706191038"><a name="en-us_topic_0112992285_b842352706191038"></a><a name="en-us_topic_0112992285_b842352706191038"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43.87561243875613%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992285_p5005970191821"><a name="en-us_topic_0112992285_p5005970191821"></a><a name="en-us_topic_0112992285_p5005970191821"></a><strong id="en-us_topic_0112992285_b842352706191041"><a name="en-us_topic_0112992285_b842352706191041"></a><a name="en-us_topic_0112992285_b842352706191041"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992285_row2830395191821"><td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992285_p41161123143326"><a name="en-us_topic_0112992285_p41161123143326"></a><a name="en-us_topic_0112992285_p41161123143326"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992285_p4386100291125"><a name="en-us_topic_0112992285_p4386100291125"></a><a name="en-us_topic_0112992285_p4386100291125"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992285_p12063482143326"><a name="en-us_topic_0112992285_p12063482143326"></a><a name="en-us_topic_0112992285_p12063482143326"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992285_p37618023143326"><a name="en-us_topic_0112992285_p37618023143326"></a><a name="en-us_topic_0112992285_p37618023143326"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992285_parmvalue80435593163333"><a name="en-us_topic_0112992285_parmvalue80435593163333"></a><a name="en-us_topic_0112992285_parmvalue80435593163333"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
<p id="en-us_topic_0112992285_p52558345143326"><a name="en-us_topic_0112992285_p52558345143326"></a><a name="en-us_topic_0112992285_p52558345143326"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
</td>
</tr>
<tr id="en-us_topic_0112992285_row601748291821"><td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992285_p1123746293430"><a name="en-us_topic_0112992285_p1123746293430"></a><a name="en-us_topic_0112992285_p1123746293430"></a>key_description</p>
</td>
<td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992285_p952418211233"><a name="en-us_topic_0112992285_p952418211233"></a><a name="en-us_topic_0112992285_p952418211233"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992285_p4346013693430"><a name="en-us_topic_0112992285_p4346013693430"></a><a name="en-us_topic_0112992285_p4346013693430"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992285_p3061008993430"><a name="en-us_topic_0112992285_p3061008993430"></a><a name="en-us_topic_0112992285_p3061008993430"></a>CMK description (The value ranges from 0 to 255 characters.)</p>
</td>
</tr>
<tr id="en-us_topic_0112992285_row315093291821"><td class="cellrowborder" valign="top" width="22.447755224477554%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992285_p5389896591821"><a name="en-us_topic_0112992285_p5389896591821"></a><a name="en-us_topic_0112992285_p5389896591821"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="15.308469153084694%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992285_p384402210314"><a name="en-us_topic_0112992285_p384402210314"></a><a name="en-us_topic_0112992285_p384402210314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992285_p3451131791821"><a name="en-us_topic_0112992285_p3451131791821"></a><a name="en-us_topic_0112992285_p3451131791821"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="43.87561243875613%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992285_p1353627112719"><a name="en-us_topic_0112992285_p1353627112719"></a><a name="en-us_topic_0112992285_p1353627112719"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992285_p4395331691821"><a name="en-us_topic_0112992285_p4395331691821"></a><a name="en-us_topic_0112992285_p4395331691821"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992285_section955024991125"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0112992285_table4661953591125"></a>
<table><thead align="left"><tr id="en-us_topic_0112992285_row5741486791125"><th class="cellrowborder" valign="top" width="21.997800219978004%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992285_p2009266891125"><a name="en-us_topic_0112992285_p2009266891125"></a><a name="en-us_topic_0112992285_p2009266891125"></a><strong id="en-us_topic_0112992285_b842352706191126"><a name="en-us_topic_0112992285_b842352706191126"></a><a name="en-us_topic_0112992285_b842352706191126"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.978402159784022%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992285_p1689338191125"><a name="en-us_topic_0112992285_p1689338191125"></a><a name="en-us_topic_0112992285_p1689338191125"></a><strong id="en-us_topic_0112992285_b842352706191129"><a name="en-us_topic_0112992285_b842352706191129"></a><a name="en-us_topic_0112992285_b842352706191129"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.858214178582145%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992285_p2618658291125"><a name="en-us_topic_0112992285_p2618658291125"></a><a name="en-us_topic_0112992285_p2618658291125"></a><strong id="en-us_topic_0112992285_b842352706191132"><a name="en-us_topic_0112992285_b842352706191132"></a><a name="en-us_topic_0112992285_b842352706191132"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="44.16558344165583%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992285_p4073839291125"><a name="en-us_topic_0112992285_p4073839291125"></a><a name="en-us_topic_0112992285_p4073839291125"></a><strong id="en-us_topic_0112992285_b842352706191134"><a name="en-us_topic_0112992285_b842352706191134"></a><a name="en-us_topic_0112992285_b842352706191134"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992285_row1147544291125"><td class="cellrowborder" valign="top" width="21.997800219978004%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992285_p708028792054"><a name="en-us_topic_0112992285_p708028792054"></a><a name="en-us_topic_0112992285_p708028792054"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.978402159784022%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992285_p1574126631"><a name="en-us_topic_0112992285_p1574126631"></a><a name="en-us_topic_0112992285_p1574126631"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992285_p1443169492054"><a name="en-us_topic_0112992285_p1443169492054"></a><a name="en-us_topic_0112992285_p1443169492054"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44.16558344165583%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992285_p2811658392054"><a name="en-us_topic_0112992285_p2811658392054"></a><a name="en-us_topic_0112992285_p2811658392054"></a>CMK ID</p>
</td>
</tr>
<tr id="en-us_topic_0112992285_row5657868491125"><td class="cellrowborder" valign="top" width="21.997800219978004%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992285_p1402298193456"><a name="en-us_topic_0112992285_p1402298193456"></a><a name="en-us_topic_0112992285_p1402298193456"></a>key_description</p>
</td>
<td class="cellrowborder" valign="top" width="15.978402159784022%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992285_p1390982717312"><a name="en-us_topic_0112992285_p1390982717312"></a><a name="en-us_topic_0112992285_p1390982717312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992285_p1776938992054"><a name="en-us_topic_0112992285_p1776938992054"></a><a name="en-us_topic_0112992285_p1776938992054"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44.16558344165583%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992285_p3003444392054"><a name="en-us_topic_0112992285_p3003444392054"></a><a name="en-us_topic_0112992285_p3003444392054"></a>Description of a CMK</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992285_section2139731104419"></a>

The following is an example about how to modify a CMK whose alias ID is  **bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e**  and description is  **test**.

-   Example request

    ```
    {
        "key_id": "bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e",
        "key_description": "test"     
    }
    ```

-   Example response

    ```
    {
        "key_info": {           
            "key_id": "bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e",
            "key_description": "test"        
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


## Status Codes<a name="en-us_topic_0112992285_section3454223421"></a>

[Table 4](#en-us_topic_0112992285_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  4**  Status codes

<a name="en-us_topic_0112992285_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992285_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992285_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992285_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992285_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992285_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992285_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992285_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992285_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992285_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992285_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992285_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992285_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992285_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992285_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992285_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992285_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992285_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992285_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992285_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992285_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

