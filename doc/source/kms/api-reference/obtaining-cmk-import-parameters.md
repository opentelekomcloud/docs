# Obtaining CMK Import Parameters<a name="kms_02_0035"></a>

## Function<a name="en-us_topic_0112992295_section2809137816511"></a>

This API enables you to obtain necessary parameters to import a CMK, including a CMK import token and a CMK encryption public key.

>![](/images/icon-note.gif) **NOTE:**   
>The returned public key type is RSA\_2048 by default.  

## URI<a name="en-us_topic_0112992295_section3802320916511"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/get-parameters-for-import

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992295_table964209216511"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992295_row1607974516511"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992295_p13230838154934"><a name="en-us_topic_0112992295_p13230838154934"></a><a name="en-us_topic_0112992295_p13230838154934"></a><strong id="en-us_topic_0112992295_b842352706195125"><a name="en-us_topic_0112992295_b842352706195125"></a><a name="en-us_topic_0112992295_b842352706195125"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992295_p65064970154934"><a name="en-us_topic_0112992295_p65064970154934"></a><a name="en-us_topic_0112992295_p65064970154934"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.55%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992295_p35771181154934"><a name="en-us_topic_0112992295_p35771181154934"></a><a name="en-us_topic_0112992295_p35771181154934"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.79%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992295_p11784586154934"><a name="en-us_topic_0112992295_p11784586154934"></a><a name="en-us_topic_0112992295_p11784586154934"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992295_row2971415116511"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992295_p5803601316511"><a name="en-us_topic_0112992295_p5803601316511"></a><a name="en-us_topic_0112992295_p5803601316511"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992295_p329664916511"><a name="en-us_topic_0112992295_p329664916511"></a><a name="en-us_topic_0112992295_p329664916511"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992295_p4386100291125"><a name="en-us_topic_0112992295_p4386100291125"></a><a name="en-us_topic_0112992295_p4386100291125"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992295_p2026050816511"><a name="en-us_topic_0112992295_p2026050816511"></a><a name="en-us_topic_0112992295_p2026050816511"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992295_section4812685216511"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992295_table1307199216511"></a>
<table><thead align="left"><tr id="en-us_topic_0112992295_row2216064416511"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992295_p14691165413488"><a name="en-us_topic_0112992295_p14691165413488"></a><a name="en-us_topic_0112992295_p14691165413488"></a><strong id="en-us_topic_0112992295_b570331320"><a name="en-us_topic_0112992295_b570331320"></a><a name="en-us_topic_0112992295_b570331320"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992295_p969155484813"><a name="en-us_topic_0112992295_p969155484813"></a><a name="en-us_topic_0112992295_p969155484813"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992295_p46911854104819"><a name="en-us_topic_0112992295_p46911854104819"></a><a name="en-us_topic_0112992295_p46911854104819"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992295_p10691854114810"><a name="en-us_topic_0112992295_p10691854114810"></a><a name="en-us_topic_0112992295_p10691854114810"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992295_row990996316511"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992295_p6450954916511"><a name="en-us_topic_0112992295_p6450954916511"></a><a name="en-us_topic_0112992295_p6450954916511"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992295_p5865974316511"><a name="en-us_topic_0112992295_p5865974316511"></a><a name="en-us_topic_0112992295_p5865974316511"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992295_p194651658369"><a name="en-us_topic_0112992295_p194651658369"></a><a name="en-us_topic_0112992295_p194651658369"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992295_p5381875116511"><a name="en-us_topic_0112992295_p5381875116511"></a><a name="en-us_topic_0112992295_p5381875116511"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992295_parmvalue80435593163333"><a name="en-us_topic_0112992295_parmvalue80435593163333"></a><a name="en-us_topic_0112992295_parmvalue80435593163333"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
<p id="en-us_topic_0112992295_p4509346016511"><a name="en-us_topic_0112992295_p4509346016511"></a><a name="en-us_topic_0112992295_p4509346016511"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
</td>
</tr>
<tr id="en-us_topic_0112992295_row2869160916511"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992295_p1322852165315"><a name="en-us_topic_0112992295_p1322852165315"></a><a name="en-us_topic_0112992295_p1322852165315"></a>wrapping_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992295_p2539755516511"><a name="en-us_topic_0112992295_p2539755516511"></a><a name="en-us_topic_0112992295_p2539755516511"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992295_p48301302716"><a name="en-us_topic_0112992295_p48301302716"></a><a name="en-us_topic_0112992295_p48301302716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0112992295_p5501165794712"><a name="en-us_topic_0112992295_p5501165794712"></a><a name="en-us_topic_0112992295_p5501165794712"></a>Encryption algorithm for CMK material. The following values are enumerated:<a name="en-us_topic_0112992295_ul2802984616441"></a><a name="en-us_topic_0112992295_ul2802984616441"></a><ul id="en-us_topic_0112992295_ul2802984616441"><li>RSAES_PKCS1_V1_5</li><li>RSAES_OAEP_SHA_1</li><li>RSAES_OAEP_SHA_256</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0112992295_row4675342116511"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992295_p2893076916511"><a name="en-us_topic_0112992295_p2893076916511"></a><a name="en-us_topic_0112992295_p2893076916511"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992295_p3090833716511"><a name="en-us_topic_0112992295_p3090833716511"></a><a name="en-us_topic_0112992295_p3090833716511"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992295_p107661929711"><a name="en-us_topic_0112992295_p107661929711"></a><a name="en-us_topic_0112992295_p107661929711"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992295_p19620161172915"><a name="en-us_topic_0112992295_p19620161172915"></a><a name="en-us_topic_0112992295_p19620161172915"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992295_p2054735816511"><a name="en-us_topic_0112992295_p2054735816511"></a><a name="en-us_topic_0112992295_p2054735816511"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992295_section5661868116511"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0112992295_table2760760616511"></a>
<table><thead align="left"><tr id="en-us_topic_0112992295_row4144383516511"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992295_p654882104911"><a name="en-us_topic_0112992295_p654882104911"></a><a name="en-us_topic_0112992295_p654882104911"></a><strong id="en-us_topic_0112992295_b1000250451"><a name="en-us_topic_0112992295_b1000250451"></a><a name="en-us_topic_0112992295_b1000250451"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992295_p185481428495"><a name="en-us_topic_0112992295_p185481428495"></a><a name="en-us_topic_0112992295_p185481428495"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992295_p15481827491"><a name="en-us_topic_0112992295_p15481827491"></a><a name="en-us_topic_0112992295_p15481827491"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992295_p154818217495"><a name="en-us_topic_0112992295_p154818217495"></a><a name="en-us_topic_0112992295_p154818217495"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992295_row2850406516511"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992295_p2712791116511"><a name="en-us_topic_0112992295_p2712791116511"></a><a name="en-us_topic_0112992295_p2712791116511"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992295_p1352290616511"><a name="en-us_topic_0112992295_p1352290616511"></a><a name="en-us_topic_0112992295_p1352290616511"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992295_p63871661575"><a name="en-us_topic_0112992295_p63871661575"></a><a name="en-us_topic_0112992295_p63871661575"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992295_p2161362216511"><a name="en-us_topic_0112992295_p2161362216511"></a><a name="en-us_topic_0112992295_p2161362216511"></a>ID of a CMK in Base64 format</p>
</td>
</tr>
<tr id="en-us_topic_0112992295_row108966291709"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992295_p4333407017714"><a name="en-us_topic_0112992295_p4333407017714"></a><a name="en-us_topic_0112992295_p4333407017714"></a>import_token</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992295_p502689121708"><a name="en-us_topic_0112992295_p502689121708"></a><a name="en-us_topic_0112992295_p502689121708"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992295_p539111618716"><a name="en-us_topic_0112992295_p539111618716"></a><a name="en-us_topic_0112992295_p539111618716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992295_p6372516917828"><a name="en-us_topic_0112992295_p6372516917828"></a><a name="en-us_topic_0112992295_p6372516917828"></a>CMK import token</p>
</td>
</tr>
<tr id="en-us_topic_0112992295_row691841617013"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992295_p1032497917951"><a name="en-us_topic_0112992295_p1032497917951"></a><a name="en-us_topic_0112992295_p1032497917951"></a>expiration_time</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992295_p3247317617012"><a name="en-us_topic_0112992295_p3247317617012"></a><a name="en-us_topic_0112992295_p3247317617012"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992295_p33951561070"><a name="en-us_topic_0112992295_p33951561070"></a><a name="en-us_topic_0112992295_p33951561070"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992295_p5836292317847"><a name="en-us_topic_0112992295_p5836292317847"></a><a name="en-us_topic_0112992295_p5836292317847"></a>Expiration time of the import parameter. The value is a timestamp expressed in the number of seconds since 00:00:00 UTC on January 1, 1970.</p>
</td>
</tr>
<tr id="en-us_topic_0112992295_row5939348917016"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992295_p455624517105"><a name="en-us_topic_0112992295_p455624517105"></a><a name="en-us_topic_0112992295_p455624517105"></a>public_key</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992295_p2303816517015"><a name="en-us_topic_0112992295_p2303816517015"></a><a name="en-us_topic_0112992295_p2303816517015"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992295_p2399364714"><a name="en-us_topic_0112992295_p2399364714"></a><a name="en-us_topic_0112992295_p2399364714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992295_p579022301793"><a name="en-us_topic_0112992295_p579022301793"></a><a name="en-us_topic_0112992295_p579022301793"></a>Public key (in Base64 format) used to encrypt CMK material</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992295_section11823115617213"></a>

The following example describes how to obtain the imported parameter of a CMK \(ID:  **bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e**; encryption algorithm:  **RSAES\_OAEP\_SHA\_1**\).

-   Example request

    ```
    {      
        "key_id": "bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e",
         "wrapping_algorithm":"RSAES_OAEP_SHA_1"
    }
    ```

-   Example response

    ```
    {
        "key_id": "bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e",
        "import_token":"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",
        "expiration_time":1501578672,
        "public_key":"MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnJQqE9GorZ16XMlOQngJfU0SgkMKJpL9W+byIebeKgmDt2I6oVSPckk9y3JiaGjXKYlepawob9b61IRR97Bcr4Sf2p3J6J3gpiYGp1Ai3495rYF+FSZAxW+VDOzbN3vig6SVxcP1PXtaKzQbtNfnlIh+rvSMJpVI3MFHh5lWjEn8L/XpprLy1FqHSSvgB99qwiPw1ZGTL5XGSrIpCV3/ah8u+5VGoIUJZTtiZk6OQDkFH9fxwIahYvLI8/yjrWFLtJuApr7aIrhRN0iDBINxddNh8M0A9sIFoS3D5RNKITjIKIMl/GVz+mHaPjK+91M/b7JrNvinFCMQDGrb/1qoGQIDAQAB"
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


## Status Codes<a name="en-us_topic_0112992295_section655115613254"></a>

[Table 4](#en-us_topic_0112992295_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  4**  Status codes

<a name="en-us_topic_0112992295_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992295_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992295_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992295_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992295_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992295_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992295_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992295_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992295_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992295_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992295_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992295_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992295_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992295_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992295_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992295_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992295_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992295_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992295_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992295_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992295_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).

