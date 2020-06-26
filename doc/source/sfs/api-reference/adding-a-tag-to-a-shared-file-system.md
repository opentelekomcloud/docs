# Adding a Tag to a Shared File System<a name="sfs_02_0037"></a>

## Function<a name="section10684447163819"></a>

This API is used to add a tag to a specified shared file system.

A shared file system can have a maximum of 10 tags.

The keys of multiple tags added to a shared file system must be unique.

This API is idempotent. If the key to be added has already been added to the shared file system, the tag is updated.

## URI<a name="section1665327514513"></a>

-   POST /v2/\{project\_id\}/sfs/\{share\_id\}/tags
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
    <table><thead align="left"><tr id="row1137265565217"><th class="cellrowborder" valign="top" width="16.33%" id="mcps1.1.5.1.1"><p id="p9445335122519"><a name="p9445335122519"></a><a name="p9445335122519"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.39%" id="mcps1.1.5.1.2"><p id="p194456353258"><a name="p194456353258"></a><a name="p194456353258"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.24%" id="mcps1.1.5.1.3"><p id="p12445335152517"><a name="p12445335152517"></a><a name="p12445335152517"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.04%" id="mcps1.1.5.1.4"><p id="p1344583582512"><a name="p1344583582512"></a><a name="p1344583582512"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8379125520523"><td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.1.5.1.1 "><p id="p13380755115210"><a name="p13380755115210"></a><a name="p13380755115210"></a>tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.2 "><p id="p1038255513523"><a name="p1038255513523"></a><a name="p1038255513523"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.1.5.1.3 "><p id="p18383165518521"><a name="p18383165518521"></a><a name="p18383165518521"></a>Resource_tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.04%" headers="mcps1.1.5.1.4 "><p id="p938455505218"><a name="p938455505218"></a><a name="p938455505218"></a>Specifies the tag. </p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of field  **resource\_tag**

    <a name="table14385185545214"></a>
    <table><thead align="left"><tr id="row5389135517522"><th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.1.5.1.1"><p id="p102581042162519"><a name="p102581042162519"></a><a name="p102581042162519"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.270000000000001%" id="mcps1.1.5.1.2"><p id="p1027318421254"><a name="p1027318421254"></a><a name="p1027318421254"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.39%" id="mcps1.1.5.1.3"><p id="p327312421253"><a name="p327312421253"></a><a name="p327312421253"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.99%" id="mcps1.1.5.1.4"><p id="p227312429253"><a name="p227312429253"></a><a name="p227312429253"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10396165515211"><td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.1.5.1.1 "><p id="p7397185512522"><a name="p7397185512522"></a><a name="p7397185512522"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.270000000000001%" headers="mcps1.1.5.1.2 "><p id="p19398125516523"><a name="p19398125516523"></a><a name="p19398125516523"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p18399255165215"><a name="p18399255165215"></a><a name="p18399255165215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.1.5.1.4 "><p id="p14400185515528"><a name="p14400185515528"></a><a name="p14400185515528"></a>Specifies the key of the tag. The value can contain a maximum of 36 characters. The key cannot be empty and can only contain letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row144011055105210"><td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.1.5.1.1 "><p id="p144021355135210"><a name="p144021355135210"></a><a name="p144021355135210"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.270000000000001%" headers="mcps1.1.5.1.2 "><p id="p1640495512522"><a name="p1640495512522"></a><a name="p1640495512522"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p16405255185213"><a name="p16405255185213"></a><a name="p16405255185213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.1.5.1.4 "><p id="p240685517526"><a name="p240685517526"></a><a name="p240685517526"></a>Specifies the value of the tag. The value contains a maximum of 43 characters and can be an empty string. It can only contain letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    {
      "tag" : {
        "key" : "key1",
        "value" : "value1"
      }
    }
    ```


## Response<a name="section6408307814513"></a>

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


