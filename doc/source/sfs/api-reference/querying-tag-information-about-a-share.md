# Querying Tag Information About a Share<a name="sfs_02_0039"></a>

## Function<a name="section10684447163819"></a>

This API is used to query all tag information about the specified shared file system.

## URI<a name="section1665327514513"></a>

-   GET /v2/\{project\_id\}/sfs/\{share\_id\}/tags
-   Parameter description

    <a name="table22021759152019"></a>
    <table><thead align="left"><tr id="row16139965152019"><th class="cellrowborder" valign="top" width="18.56%" id="mcps1.1.5.1.1"><p id="p17124101410431"><a name="p17124101410431"></a><a name="p17124101410431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.4%" id="mcps1.1.5.1.2"><p id="p1612415146430"><a name="p1612415146430"></a><a name="p1612415146430"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.65%" id="mcps1.1.5.1.3"><p id="p312416148432"><a name="p312416148432"></a><a name="p312416148432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.39%" id="mcps1.1.5.1.4"><p id="p3124181464318"><a name="p3124181464318"></a><a name="p3124181464318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55089343152019"><td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.1.5.1.1 "><p id="p1781134044818"><a name="p1781134044818"></a><a name="p1781134044818"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.4%" headers="mcps1.1.5.1.2 "><p id="p59952126152019"><a name="p59952126152019"></a><a name="p59952126152019"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.65%" headers="mcps1.1.5.1.3 "><p id="p24284048152019"><a name="p24284048152019"></a><a name="p24284048152019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.39%" headers="mcps1.1.5.1.4 "><p id="p20850895152019"><a name="p20850895152019"></a><a name="p20850895152019"></a>Specifies the project ID of the operator.</p>
    </td>
    </tr>
    <tr id="row3119103219486"><td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.1.5.1.1 "><p id="p1011933217487"><a name="p1011933217487"></a><a name="p1011933217487"></a>share_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.4%" headers="mcps1.1.5.1.2 "><p id="p18120163210481"><a name="p18120163210481"></a><a name="p18120163210481"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.65%" headers="mcps1.1.5.1.3 "><p id="p11120113294813"><a name="p11120113294813"></a><a name="p11120113294813"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.39%" headers="mcps1.1.5.1.4 "><p id="p13120143211489"><a name="p13120143211489"></a><a name="p13120143211489"></a>Specifies the share ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section1041111631610"></a>

-   Parameter description

    None

-   Example request

    None


## Response<a name="section6408307814513"></a>

-   Parameter description

    <a name="table1836815510524"></a>
    <table><thead align="left"><tr id="row1137265565217"><th class="cellrowborder" valign="top" width="20.26%" id="mcps1.1.4.1.1"><p id="p1220553717265"><a name="p1220553717265"></a><a name="p1220553717265"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.18%" id="mcps1.1.4.1.2"><p id="p722173732618"><a name="p722173732618"></a><a name="p722173732618"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.56%" id="mcps1.1.4.1.3"><p id="p12221183792610"><a name="p12221183792610"></a><a name="p12221183792610"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8379125520523"><td class="cellrowborder" valign="top" width="20.26%" headers="mcps1.1.4.1.1 "><p id="p13380755115210"><a name="p13380755115210"></a><a name="p13380755115210"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.18%" headers="mcps1.1.4.1.2 "><p id="p999215189579"><a name="p999215189579"></a><a name="p999215189579"></a>Array of resource_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.56%" headers="mcps1.1.4.1.3 "><p id="p938455505218"><a name="p938455505218"></a><a name="p938455505218"></a>Specifies the list of tags.</p>
    </td>
    </tr>
    <tr id="row118571741145214"><td class="cellrowborder" valign="top" width="20.26%" headers="mcps1.1.4.1.1 "><p id="p162874465213"><a name="p162874465213"></a><a name="p162874465213"></a>sys_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.18%" headers="mcps1.1.4.1.2 "><p id="p128844115218"><a name="p128844115218"></a><a name="p128844115218"></a>Array of resource_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.56%" headers="mcps1.1.4.1.3 "><p id="p172864425217"><a name="p172864425217"></a><a name="p172864425217"></a>Only the op_service permission can obtain this field.</p>
    <a name="ol13281444125215"></a><a name="ol13281444125215"></a><ol id="ol13281444125215"><li>Currently, only one resource_tag structure key is used, <strong id="b5237534359"><a name="b5237534359"></a><a name="b5237534359"></a>_sys_enterprise_project_id</strong>.</li><li>Currently, <strong id="b834933063519"><a name="b834933063519"></a><a name="b834933063519"></a>key</strong> contains only one value.</li></ol>
    <p id="p42864485214"><a name="p42864485214"></a><a name="p42864485214"></a>This field cannot be returned in non-op_service scenarios.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of field  **resource\_tag**

    <a name="table14385185545214"></a>
    <table><thead align="left"><tr id="row5389135517522"><th class="cellrowborder" valign="top" width="20.01%" id="mcps1.1.4.1.1"><p id="p19554127162720"><a name="p19554127162720"></a><a name="p19554127162720"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.33%" id="mcps1.1.4.1.2"><p id="p175546782715"><a name="p175546782715"></a><a name="p175546782715"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.66%" id="mcps1.1.4.1.3"><p id="p1055418792713"><a name="p1055418792713"></a><a name="p1055418792713"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10396165515211"><td class="cellrowborder" valign="top" width="20.01%" headers="mcps1.1.4.1.1 "><p id="p7397185512522"><a name="p7397185512522"></a><a name="p7397185512522"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.33%" headers="mcps1.1.4.1.2 "><p id="p18399255165215"><a name="p18399255165215"></a><a name="p18399255165215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.66%" headers="mcps1.1.4.1.3 "><p id="p14400185515528"><a name="p14400185515528"></a><a name="p14400185515528"></a>Specifies the key of the tag.</p>
    </td>
    </tr>
    <tr id="row144011055105210"><td class="cellrowborder" valign="top" width="20.01%" headers="mcps1.1.4.1.1 "><p id="p144021355135210"><a name="p144021355135210"></a><a name="p144021355135210"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.33%" headers="mcps1.1.4.1.2 "><p id="p16405255185213"><a name="p16405255185213"></a><a name="p16405255185213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.66%" headers="mcps1.1.4.1.3 "><p id="p240685517526"><a name="p240685517526"></a><a name="p240685517526"></a>Specifies the value of the tag.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
           "tags": [
            {
                "key": "key1",
                "value": "value1"
            },
            {
                "key": "key2",
                "value": ""
            }
        ]
    }
    ```


## Status Codes<a name="section4959408514513"></a>

-   Normal

    200

-   Abnormal

    <a name="table6245403714513"></a>
    <table><thead align="left"><tr id="row1507735814513"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="p1330652014513"><a name="p1330652014513"></a><a name="p1330652014513"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="p408636314513"><a name="p408636314513"></a><a name="p408636314513"></a><strong id="b84235270615228"><a name="b84235270615228"></a><a name="b84235270615228"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3477393214513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p6522508214513"><a name="p6522508214513"></a><a name="p6522508214513"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p4874025614513"><a name="p4874025614513"></a><a name="p4874025614513"></a>Invalid value.</p>
    </td>
    </tr>
    <tr id="row3600912414513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p3105792214513"><a name="p3105792214513"></a><a name="p3105792214513"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p3266375714513"><a name="p3266375714513"></a><a name="p3266375714513"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row2553835814513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p5534113514513"><a name="p5534113514513"></a><a name="p5534113514513"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p5344692014513"><a name="p5344692014513"></a><a name="p5344692014513"></a>Access to the requested page is forbidden.</p>
    </td>
    </tr>
    <tr id="row1126023214513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p3966357214513"><a name="p3966357214513"></a><a name="p3966357214513"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p5863278914513"><a name="p5863278914513"></a><a name="p5863278914513"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row1011562214513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1405905414513"><a name="p1405905414513"></a><a name="p1405905414513"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p6504160314513"><a name="p6504160314513"></a><a name="p6504160314513"></a>The request is not completed because of a service error.</p>
    </td>
    </tr>
    </tbody>
    </table>


