# Deleting One Piece of Metadata for an EVS Snapshot<a name="evs_04_3067"></a>

## Function<a name="section4805694511340"></a>

This API is used to delete one piece of the EVS snapshot metadata.

## URI<a name="section268627411340"></a>

-   URI format

    DELETE /v3/\{project\_id\}/snapshots/\{snapshot\_id\}/metadata/\{key\}

-   Parameter description

    <a name="table5655293911340"></a>
    <table><thead align="left"><tr id="row4718979611340"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.4.1.1"><p id="p6427715211340"><a name="p6427715211340"></a><a name="p6427715211340"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.1.4.1.2"><p id="p3906685711340"><a name="p3906685711340"></a><a name="p3906685711340"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.9%" id="mcps1.1.4.1.3"><p id="p1029885411340"><a name="p1029885411340"></a><a name="p1029885411340"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2890086411340"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p5926863811340"><a name="p5926863811340"></a><a name="p5926863811340"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p3603037711340"><a name="p3603037711340"></a><a name="p3603037711340"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p3277940011340"><a name="p3277940011340"></a><a name="p3277940011340"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row2657914711340"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p542726811340"><a name="p542726811340"></a><a name="p542726811340"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p3695552511340"><a name="p3695552511340"></a><a name="p3695552511340"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p4060754311340"><a name="p4060754311340"></a><a name="p4060754311340"></a>Specifies the snapshot ID.</p>
    </td>
    </tr>
    <tr id="row5469147141539"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p40347759141539"><a name="p40347759141539"></a><a name="p40347759141539"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p46943076141539"><a name="p46943076141539"></a><a name="p46943076141539"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p44292834141539"><a name="p44292834141539"></a><a name="p44292834141539"></a>Specifies the key of the piece of metadata to be deleted.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section87667311340"></a>

-   Example request

    ```
    DELETE https://{endpoint}/v3/{project_id}/snapshots/f9faf7df-fdc1-4093-9ef3-5cba06eef995/metadata/value1
    ```


## Response<a name="section5147449911340"></a>

-   Parameter description

    <a name="evs_04_2104_table11977025201856"></a>
    <table><thead align="left"><tr id="evs_04_2104_row8102228201856"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="evs_04_2104_p52300707201856"><a name="evs_04_2104_p52300707201856"></a><a name="evs_04_2104_p52300707201856"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.62%" id="mcps1.1.4.1.2"><p id="evs_04_2104_p3642697315541"><a name="evs_04_2104_p3642697315541"></a><a name="evs_04_2104_p3642697315541"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="evs_04_2104_p17319263201856"><a name="evs_04_2104_p17319263201856"></a><a name="evs_04_2104_p17319263201856"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2104_row135502511261"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_2104_p129522216412"><a name="evs_04_2104_p129522216412"></a><a name="evs_04_2104_p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="evs_04_2104_p1595262111415"><a name="evs_04_2104_p1595262111415"></a><a name="evs_04_2104_p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2104_p109527215417"><a name="evs_04_2104_p109527215417"></a><a name="evs_04_2104_p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#evs_04_2104_li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2104_li0419202382514"></a>Parameters in the  **error**  field

    <a name="evs_04_2104_evs_04_2013_table15441099103019"></a>
    <table><thead align="left"><tr id="evs_04_2104_evs_04_2013_row54094047103019"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="evs_04_2104_evs_04_2013_p19541716103019"><a name="evs_04_2104_evs_04_2013_p19541716103019"></a><a name="evs_04_2104_evs_04_2013_p19541716103019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="evs_04_2104_evs_04_2013_p39375186103019"><a name="evs_04_2104_evs_04_2013_p39375186103019"></a><a name="evs_04_2104_evs_04_2013_p39375186103019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2104_evs_04_2013_p38578950103019"><a name="evs_04_2104_evs_04_2013_p38578950103019"></a><a name="evs_04_2104_evs_04_2013_p38578950103019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2104_evs_04_2013_row59401790103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2104_evs_04_2013_p46815658103019"><a name="evs_04_2104_evs_04_2013_p46815658103019"></a><a name="evs_04_2104_evs_04_2013_p46815658103019"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2104_evs_04_2013_p33971979103019"><a name="evs_04_2104_evs_04_2013_p33971979103019"></a><a name="evs_04_2104_evs_04_2013_p33971979103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2104_evs_04_2013_p21623243103019"><a name="evs_04_2104_evs_04_2013_p21623243103019"></a><a name="evs_04_2104_evs_04_2013_p21623243103019"></a>Specifies the error message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="evs_04_2104_evs_04_2013_row60391466103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2104_evs_04_2013_p59870541103019"><a name="evs_04_2104_evs_04_2013_p59870541103019"></a><a name="evs_04_2104_evs_04_2013_p59870541103019"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2104_evs_04_2013_p17675690103019"><a name="evs_04_2104_evs_04_2013_p17675690103019"></a><a name="evs_04_2104_evs_04_2013_p17675690103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2104_evs_04_2013_p6087468103019"><a name="evs_04_2104_evs_04_2013_p6087468103019"></a><a name="evs_04_2104_evs_04_2013_p6087468103019"></a>Specifies the error code returned when an error occurs.</p>
    <p id="evs_04_2104_evs_04_2013_p54787218103019"><a name="evs_04_2104_evs_04_2013_p54787218103019"></a><a name="evs_04_2104_evs_04_2013_p54787218103019"></a>For details about the error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    None

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


## Status Codes<a name="section1751558211340"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

