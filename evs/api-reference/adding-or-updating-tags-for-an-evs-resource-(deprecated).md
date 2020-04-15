# Adding or Updating Tags for an EVS Resource \(Deprecated\)<a name="evs_04_2036"></a>

## Function<a name="section17386310104128"></a>

This API is used to add or update tags for an EVS resource.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>This API has been deprecated. Use another API. For details, see  [Batch Adding Tags for the Specified EVS Disk](batch-adding-tags-for-the-specified-evs-disk.md).  

## Constraints<a name="section58153866104128"></a>

-   A tag is composed of a key-value pair.
    -   Key:
        -   Must be unique for each resource.
        -   Can contain a maximum of 36 characters.
        -   Can contain only digits, letters, hyphens \(-\), and underscores \(\_\).

    -   Value:
        -   Can contain a maximum of 43 characters.
        -   Can contain only digits, letters, hyphens \(-\), and underscores \(\_\).



-   A maximum of 10 tags can be created for an EVS resource.

## URI<a name="section48475837104128"></a>

-   URI format

    POST /v2/\{project\_id\}/os-vendor-tags/\{resource\_type\}/\{resource\_id\}

-   Parameter description

    <a name="table28484833104128"></a>
    <table><thead align="left"><tr id="row60547305104128"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.4.1.1"><p id="p5384679104128"><a name="p5384679104128"></a><a name="p5384679104128"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.1.4.1.2"><p id="p33505894104128"><a name="p33505894104128"></a><a name="p33505894104128"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.9%" id="mcps1.1.4.1.3"><p id="p29622926104128"><a name="p29622926104128"></a><a name="p29622926104128"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row50646790104128"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p8749302104128"><a name="p8749302104128"></a><a name="p8749302104128"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p37604871104128"><a name="p37604871104128"></a><a name="p37604871104128"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p26095712104128"><a name="p26095712104128"></a><a name="p26095712104128"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row40869685152038"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p33171521152058"><a name="p33171521152058"></a><a name="p33171521152058"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p2538652152058"><a name="p2538652152058"></a><a name="p2538652152058"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p42707547152038"><a name="p42707547152038"></a><a name="p42707547152038"></a>Specifies the resource type. The value can be <strong id="b842352706193556"><a name="b842352706193556"></a><a name="b842352706193556"></a>volumes</strong>, <strong id="b84235270619367"><a name="b84235270619367"></a><a name="b84235270619367"></a>snapshots</strong>, or <strong id="b842352706193615"><a name="b842352706193615"></a><a name="b842352706193615"></a>backups</strong>.</p>
    </td>
    </tr>
    <tr id="row255647152042"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p38738380152058"><a name="p38738380152058"></a><a name="p38738380152058"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p50801043152058"><a name="p50801043152058"></a><a name="p50801043152058"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p33198438152042"><a name="p33198438152042"></a><a name="p33198438152042"></a>Specifies the resource ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section33377962104128"></a>

-   Parameter description

    <a name="table16590896104128"></a>
    <table><thead align="left"><tr id="row60389002104128"><th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.1.5.1.1"><p id="p1625381416113"><a name="p1625381416113"></a><a name="p1625381416113"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.59%" id="mcps1.1.5.1.2"><p id="p1513999104128"><a name="p1513999104128"></a><a name="p1513999104128"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.279999999999998%" id="mcps1.1.5.1.3"><p id="p55525100104128"><a name="p55525100104128"></a><a name="p55525100104128"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.96%" id="mcps1.1.5.1.4"><p id="p1239270104128"><a name="p1239270104128"></a><a name="p1239270104128"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33272036104128"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p37459679152411"><a name="p37459679152411"></a><a name="p37459679152411"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.59%" headers="mcps1.1.5.1.2 "><p id="p59805966104128"><a name="p59805966104128"></a><a name="p59805966104128"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.1.5.1.3 "><p id="p12445066104128"><a name="p12445066104128"></a><a name="p12445066104128"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.96%" headers="mcps1.1.5.1.4 "><p id="p1417386104128"><a name="p1417386104128"></a><a name="p1417386104128"></a>Specifies the key-value pair of the tag.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of the request header parameter

    <a name="table2028154215261"></a>
    <table><thead align="left"><tr id="row5873922415261"><th class="cellrowborder" valign="top" width="17.23%" id="mcps1.1.5.1.1"><p id="p1076316158116"><a name="p1076316158116"></a><a name="p1076316158116"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.49%" id="mcps1.1.5.1.2"><p id="p1398844406"><a name="p1398844406"></a><a name="p1398844406"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.240000000000002%" id="mcps1.1.5.1.3"><p id="p69908410015"><a name="p69908410015"></a><a name="p69908410015"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.04%" id="mcps1.1.5.1.4"><p id="p1727312315261"><a name="p1727312315261"></a><a name="p1727312315261"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5694570715261"><td class="cellrowborder" valign="top" width="17.23%" headers="mcps1.1.5.1.1 "><p id="p4919953115261"><a name="p4919953115261"></a><a name="p4919953115261"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.2 "><p id="p209931941909"><a name="p209931941909"></a><a name="p209931941909"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.1.5.1.3 "><p id="p399418412010"><a name="p399418412010"></a><a name="p399418412010"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.04%" headers="mcps1.1.5.1.4 "><p id="p2823169515261"><a name="p2823169515261"></a><a name="p2823169515261"></a>Specifies the type. The value can be <strong id="b842352706194129"><a name="b842352706194129"></a><a name="b842352706194129"></a>application/json</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {  
         "tags" : { 
            "key_0" : "value_0", 
            "key_1" : "value_1"  
         } 
    }
    ```


>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If the request body contains an existing key of the resource, the original tag containing this key will be overwritten. For example,  **"key\_1":"val\_1"**  is an existing tag of the resource. If the request body contains  **"key\_1":"val\_11"**, the tag of  **key\_1**  for this resource is  **"key\_1":"val\_11"**.  

## Response<a name="section26860493104128"></a>

-   Parameter description

    <a name="table37832011153258"></a>
    <table><thead align="left"><tr id="row17828636153258"><th class="cellrowborder" valign="top" width="19.05%" id="mcps1.1.4.1.1"><p id="p34833401153258"><a name="p34833401153258"></a><a name="p34833401153258"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.810000000000002%" id="mcps1.1.4.1.2"><p id="p2933214153258"><a name="p2933214153258"></a><a name="p2933214153258"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p51686370153258"><a name="p51686370153258"></a><a name="p51686370153258"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row25846481153258"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p13190249153258"><a name="p13190249153258"></a><a name="p13190249153258"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p61777233153258"><a name="p61777233153258"></a><a name="p61777233153258"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p49997362153258"><a name="p49997362153258"></a><a name="p49997362153258"></a>Specifies the key-value pair of the tag.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {  
         "tags" : { 
            "key_0" : "value_0", 
            "key_1" : "value_1"  
         } 
    }
    ```

    or

    ```
    {
        "error": {
            "message": "XXXX", 
            "code": "XXX"
        }
    }
    ```

    In the preceding example,  **error**  indicates a general error, for example,  **badRequest**  or  **itemNotFound**. An example is provided as follows:

    ```
    {
        "badRequest": {
            "message": "Invalid tags: Tags property value contains invalid characters.", 
            "code": 400
        }
    }
    ```


## Status Codes<a name="section46084594151835"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

