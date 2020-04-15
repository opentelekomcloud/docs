# Resetting Tags of an EVS Resource \(Deprecated\)<a name="evs_04_2040"></a>

## Function<a name="section5299350116935"></a>

This API is used to reset the tags of an EVS resource, and the existing tags will be deleted.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>This API call exists for compatibility reasons only and has been deprecated.  

## Constraints<a name="section4466609116935"></a>

-   A tag is composed of a key-value pair.
    -   Key:
        -   Must be unique for each resource.
        -   Can contain a maximum of 36 characters.
        -   Can contain only digits, letters, hyphens \(-\), and underscores \(\_\).

    -   Value:
        -   Can contain a maximum of 43 characters.
        -   Can contain only digits, letters, hyphens \(-\), and underscores \(\_\).



-   A maximum of 10 tags can be created for an EVS resource.

## URI<a name="section1378135716935"></a>

-   URI format

    PUT /v2/\{project\_id\}/os-vendor-tags/\{resource\_type\}/\{resource\_id\}

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


## Request<a name="section33444519162337"></a>

-   Parameter description

    <a name="table50618906162337"></a>
    <table><thead align="left"><tr id="row13155682162337"><th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.1.5.1.1"><p id="p58977321162337"><a name="p58977321162337"></a><a name="p58977321162337"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.15%" id="mcps1.1.5.1.2"><p id="p12433688162337"><a name="p12433688162337"></a><a name="p12433688162337"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.5.1.3"><p id="p495832162337"><a name="p495832162337"></a><a name="p495832162337"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.96%" id="mcps1.1.5.1.4"><p id="p40162449162337"><a name="p40162449162337"></a><a name="p40162449162337"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row31932906162337"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p36428555162337"><a name="p36428555162337"></a><a name="p36428555162337"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p65031837162337"><a name="p65031837162337"></a><a name="p65031837162337"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.5.1.3 "><p id="p33087431162337"><a name="p33087431162337"></a><a name="p33087431162337"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.96%" headers="mcps1.1.5.1.4 "><p id="p62836274162337"><a name="p62836274162337"></a><a name="p62836274162337"></a>Specifies the key-value pair of the tag.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of the request header parameter

    <a name="evs_04_2036_table2028154215261"></a>
    <table><thead align="left"><tr id="evs_04_2036_row5873922415261"><th class="cellrowborder" valign="top" width="17.23%" id="mcps1.1.5.1.1"><p id="evs_04_2036_p1076316158116"><a name="evs_04_2036_p1076316158116"></a><a name="evs_04_2036_p1076316158116"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.49%" id="mcps1.1.5.1.2"><p id="evs_04_2036_p1398844406"><a name="evs_04_2036_p1398844406"></a><a name="evs_04_2036_p1398844406"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.240000000000002%" id="mcps1.1.5.1.3"><p id="evs_04_2036_p69908410015"><a name="evs_04_2036_p69908410015"></a><a name="evs_04_2036_p69908410015"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.04%" id="mcps1.1.5.1.4"><p id="evs_04_2036_p1727312315261"><a name="evs_04_2036_p1727312315261"></a><a name="evs_04_2036_p1727312315261"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2036_row5694570715261"><td class="cellrowborder" valign="top" width="17.23%" headers="mcps1.1.5.1.1 "><p id="evs_04_2036_p4919953115261"><a name="evs_04_2036_p4919953115261"></a><a name="evs_04_2036_p4919953115261"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.2 "><p id="evs_04_2036_p209931941909"><a name="evs_04_2036_p209931941909"></a><a name="evs_04_2036_p209931941909"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.240000000000002%" headers="mcps1.1.5.1.3 "><p id="evs_04_2036_p399418412010"><a name="evs_04_2036_p399418412010"></a><a name="evs_04_2036_p399418412010"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.04%" headers="mcps1.1.5.1.4 "><p id="evs_04_2036_p2823169515261"><a name="evs_04_2036_p2823169515261"></a><a name="evs_04_2036_p2823169515261"></a>Specifies the type. The value can be <strong id="evs_04_2036_b842352706194129"><a name="evs_04_2036_b842352706194129"></a><a name="evs_04_2036_b842352706194129"></a>application/json</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "tags": {
            "key_new": "value_new"
        }
    }
    ```


## Response<a name="section31780302162337"></a>

-   Parameter description

    <a name="table3322832162337"></a>
    <table><thead align="left"><tr id="row13298017162337"><th class="cellrowborder" valign="top" width="21.66%" id="mcps1.1.4.1.1"><p id="p3397559162337"><a name="p3397559162337"></a><a name="p3397559162337"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.11%" id="mcps1.1.4.1.2"><p id="p6766862162337"><a name="p6766862162337"></a><a name="p6766862162337"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.230000000000004%" id="mcps1.1.4.1.3"><p id="p38425053162337"><a name="p38425053162337"></a><a name="p38425053162337"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row25421606162337"><td class="cellrowborder" valign="top" width="21.66%" headers="mcps1.1.4.1.1 "><p id="p45884175162337"><a name="p45884175162337"></a><a name="p45884175162337"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.11%" headers="mcps1.1.4.1.2 "><p id="p25630656162337"><a name="p25630656162337"></a><a name="p25630656162337"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.230000000000004%" headers="mcps1.1.4.1.3 "><p id="p55032476162337"><a name="p55032476162337"></a><a name="p55032476162337"></a>Specifies the key-value pair of the tag.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "tags": {
            "key_new": "value_new"
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
            "message": "Invalid tags: Tags property key contains invalid characters.", 
            "code": 400
        }
    }
    ```


## Status Codes<a name="section9636891162337"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

