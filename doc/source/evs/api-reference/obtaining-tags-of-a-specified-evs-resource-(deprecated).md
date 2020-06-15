# Obtaining Tags of a Specified EVS Resource \(Deprecated\)<a name="evs_04_2038"></a>

## Function<a name="section17386310104128"></a>

This API is used to obtain the tags of a specified EVS resource.

>![](/images/icon-notice.gif) **NOTICE:**   
>This API has been deprecated. Use another API. For details, see  [Querying Tags of an EVS Disk](querying-tags-of-an-evs-disk.md).  

## Constraints<a name="section58153866104128"></a>

None

## URI<a name="section48475837104128"></a>

-   URI format

    GET /v2/\{project\_id\}/os-vendor-tags/\{resource\_type\}/\{resource\_id\}

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

None

## Response<a name="section26860493104128"></a>

-   Parameter description

    <a name="table1895094016425"></a>
    <table><thead align="left"><tr id="row3352726916425"><th class="cellrowborder" valign="top" width="19.05%" id="mcps1.1.4.1.1"><p id="p3135425816425"><a name="p3135425816425"></a><a name="p3135425816425"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.810000000000002%" id="mcps1.1.4.1.2"><p id="p5666695116425"><a name="p5666695116425"></a><a name="p5666695116425"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p876337116425"><a name="p876337116425"></a><a name="p876337116425"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3874449016425"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p5129601816425"><a name="p5129601816425"></a><a name="p5129601816425"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p6133677816425"><a name="p6133677816425"></a><a name="p6133677816425"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p4585325916425"><a name="p4585325916425"></a><a name="p4585325916425"></a>Specifies the key-value pair of the tag.</p>
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
        "itemNotFound": {
            "message": "XXXX", 
            "code": "XXX"
        }
    }
    ```


## Status Codes<a name="section46084594151835"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

