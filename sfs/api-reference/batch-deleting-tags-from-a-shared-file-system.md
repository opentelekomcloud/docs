# Batch Deleting Tags from a Shared File System<a name="sfs_02_0042"></a>

## Function<a name="section10684447163819"></a>

This API is used to batch delete tags from a specified shared file system.

This API is idempotent. If the tags to be deleted do not exist on the shared file system, the deletion is regarded as successful by default.

## URI<a name="section1665327514513"></a>

-   POST /v2/\{project\_id\}/sfs/\{share\_id\}/tags/action
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


## Request<a name="section5063604914513"></a>

-   Parameter description

    <a name="table1836815510524"></a>
    <table><thead align="left"><tr id="row1137265565217"><th class="cellrowborder" valign="top" width="16.33%" id="mcps1.1.5.1.1"><p id="p96501046163313"><a name="p96501046163313"></a><a name="p96501046163313"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.39%" id="mcps1.1.5.1.2"><p id="p3666184616332"><a name="p3666184616332"></a><a name="p3666184616332"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.24%" id="mcps1.1.5.1.3"><p id="p3666446113310"><a name="p3666446113310"></a><a name="p3666446113310"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.04%" id="mcps1.1.5.1.4"><p id="p2666174623316"><a name="p2666174623316"></a><a name="p2666174623316"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1476962172917"><td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.1.5.1.1 "><p id="p1876919212918"><a name="p1876919212918"></a><a name="p1876919212918"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.2 "><p id="p1276919232920"><a name="p1276919232920"></a><a name="p1276919232920"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.1.5.1.3 "><p id="p10769112142919"><a name="p10769112142919"></a><a name="p10769112142919"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.04%" headers="mcps1.1.5.1.4 "><p id="p197694202910"><a name="p197694202910"></a><a name="p197694202910"></a>Specifies the operation identifier. Possible values are <strong id="b842352706192333"><a name="b842352706192333"></a><a name="b842352706192333"></a>create</strong> and <strong id="b842352706192336"><a name="b842352706192336"></a><a name="b842352706192336"></a>delete</strong>. Use <strong id="b142857603419313"><a name="b142857603419313"></a><a name="b142857603419313"></a>delete</strong> to batch delete tags from a specified shared file system.</p>
    </td>
    </tr>
    <tr id="row8379125520523"><td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.1.5.1.1 "><p id="p13380755115210"><a name="p13380755115210"></a><a name="p13380755115210"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.2 "><p id="p1038255513523"><a name="p1038255513523"></a><a name="p1038255513523"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.1.5.1.3 "><p id="p1393836507"><a name="p1393836507"></a><a name="p1393836507"></a>Array of resource_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.04%" headers="mcps1.1.5.1.4 "><p id="p938455505218"><a name="p938455505218"></a><a name="p938455505218"></a>Specifies the tag list.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of field  **resource\_tag**

    <a name="table14385185545214"></a>
    <table><thead align="left"><tr id="row5389135517522"><th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.1.5.1.1"><p id="p133062052193316"><a name="p133062052193316"></a><a name="p133062052193316"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.270000000000001%" id="mcps1.1.5.1.2"><p id="p332285211337"><a name="p332285211337"></a><a name="p332285211337"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.39%" id="mcps1.1.5.1.3"><p id="p3322452173315"><a name="p3322452173315"></a><a name="p3322452173315"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.99%" id="mcps1.1.5.1.4"><p id="p11322145211339"><a name="p11322145211339"></a><a name="p11322145211339"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10396165515211"><td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.1.5.1.1 "><p id="p7397185512522"><a name="p7397185512522"></a><a name="p7397185512522"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.270000000000001%" headers="mcps1.1.5.1.2 "><p id="p19398125516523"><a name="p19398125516523"></a><a name="p19398125516523"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p18399255165215"><a name="p18399255165215"></a><a name="p18399255165215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.1.5.1.4 "><p id="p2676153813453"><a name="p2676153813453"></a><a name="p2676153813453"></a>Specifies the key of the tag.</p>
    <p id="p14400185515528"><a name="p14400185515528"></a><a name="p14400185515528"></a>The value can contain a maximum of 36 characters. This parameter cannot be left empty.</p>
    </td>
    </tr>
    <tr id="row144011055105210"><td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.1.5.1.1 "><p id="p144021355135210"><a name="p144021355135210"></a><a name="p144021355135210"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.270000000000001%" headers="mcps1.1.5.1.2 "><p id="p1640495512522"><a name="p1640495512522"></a><a name="p1640495512522"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p16405255185213"><a name="p16405255185213"></a><a name="p16405255185213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.1.5.1.4 "><p id="p119131733154512"><a name="p119131733154512"></a><a name="p119131733154512"></a>Specifies the value of the tag.</p>
    <p id="p47721428633"><a name="p47721428633"></a><a name="p47721428633"></a>The value contains a maximum of 43 characters and can be an empty string. If the value is not an empty string, the tag is located and deleted based on the key and value. If the value is an empty string, the tag is located and deleted based on the key.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    {
        "action": "delete",
        "tags": [
            {
                "key": "key1",
                "value": "value1"
            },
            {
                "key": "key2"
            },
            {
                "key": "key3",
                "value": ""
            }
        ]
    }
    ```


## Response<a name="section1060474015305"></a>

-   Parameter description

    None


-   Example response

    None


## Status Codes<a name="section4959408514513"></a>

-   Normal

    204

-   Abnormal

    <a name="table6245403714513"></a>
    <table><thead align="left"><tr id="row1507735814513"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="p1330652014513"><a name="p1330652014513"></a><a name="p1330652014513"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="p408636314513"><a name="p408636314513"></a><a name="p408636314513"></a>Description</p>
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


