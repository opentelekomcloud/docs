# Updating One Piece of Metadata for an EVS Snapshot<a name="evs_04_2101"></a>

## Function<a name="section4805694511340"></a>

This API is used to update one piece of the EVS snapshot metadata.

## URI<a name="section268627411340"></a>

-   URI format

    PUT /v2/\{project\_id\}/snapshots/\{snapshot\_id\}/metadata/\{key\}

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
    <tr id="row2758984514653"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p2018501114653"><a name="p2018501114653"></a><a name="p2018501114653"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p2437320514653"><a name="p2437320514653"></a><a name="p2437320514653"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p2807261214653"><a name="p2807261214653"></a><a name="p2807261214653"></a>Specifies the key of the piece of metadata to be updated.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section87667311340"></a>

-   Parameter description

    <a name="table31588048"></a>
    <table><thead align="left"><tr id="row57330849"><th class="cellrowborder" valign="top" width="17.49%" id="mcps1.1.5.1.1"><p id="p13287175"><a name="p13287175"></a><a name="p13287175"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.22%" id="mcps1.1.5.1.2"><p id="p2519427"><a name="p2519427"></a><a name="p2519427"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.299999999999997%" id="mcps1.1.5.1.3"><p id="p2747002"><a name="p2747002"></a><a name="p2747002"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.99%" id="mcps1.1.5.1.4"><p id="p21180630"><a name="p21180630"></a><a name="p21180630"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row53167494153413"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p11599783153413"><a name="p11599783153413"></a><a name="p11599783153413"></a>meta</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.22%" headers="mcps1.1.5.1.2 "><p id="p58405153413"><a name="p58405153413"></a><a name="p58405153413"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p4730855153413"><a name="p4730855153413"></a><a name="p4730855153413"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.99%" headers="mcps1.1.5.1.4 "><p id="p47654998153413"><a name="p47654998153413"></a><a name="p47654998153413"></a>Specifies the metadata to be updated. For details, see <a href="#li54973602211845">Parameter in the metadata field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li54973602211845"></a>Parameter in the  **metadata**  field

    <a name="table32717123212358"></a>
    <table><thead align="left"><tr id="row2280240212358"><th class="cellrowborder" valign="top" width="17.49%" id="mcps1.1.5.1.1"><p id="p50481723212358"><a name="p50481723212358"></a><a name="p50481723212358"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.22%" id="mcps1.1.5.1.2"><p id="p62487767212358"><a name="p62487767212358"></a><a name="p62487767212358"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.48%" id="mcps1.1.5.1.3"><p id="p28344363212358"><a name="p28344363212358"></a><a name="p28344363212358"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.81%" id="mcps1.1.5.1.4"><p id="p14192096212358"><a name="p14192096212358"></a><a name="p14192096212358"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8709150212358"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p34352524212358"><a name="p34352524212358"></a><a name="p34352524212358"></a>key_val</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.22%" headers="mcps1.1.5.1.2 "><p id="p31091026212358"><a name="p31091026212358"></a><a name="p31091026212358"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p35345177212358"><a name="p35345177212358"></a><a name="p35345177212358"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.81%" headers="mcps1.1.5.1.4 "><p id="p44387080212358"><a name="p44387080212358"></a><a name="p44387080212358"></a>Specifies a piece of metadata, which is made up of a key-value pair.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    {
        "meta": {
            "key1": "value1"
        }
    }
    ```


## Response<a name="section5147449911340"></a>

-   Parameter description

    <a name="table11977025201856"></a>
    <table><thead align="left"><tr id="row8102228201856"><th class="cellrowborder" valign="top" width="20.93%" id="mcps1.1.4.1.1"><p id="p10767936126"><a name="p10767936126"></a><a name="p10767936126"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.09%" id="mcps1.1.4.1.2"><p id="p3642697315541"><a name="p3642697315541"></a><a name="p3642697315541"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.98%" id="mcps1.1.4.1.3"><p id="p17319263201856"><a name="p17319263201856"></a><a name="p17319263201856"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60683035201856"><td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.1.4.1.1 "><p id="p16378828201856"><a name="p16378828201856"></a><a name="p16378828201856"></a>meta</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.09%" headers="mcps1.1.4.1.2 "><p id="p6490369115541"><a name="p6490369115541"></a><a name="p6490369115541"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.98%" headers="mcps1.1.4.1.3 "><p id="p20205612201856"><a name="p20205612201856"></a><a name="p20205612201856"></a>Specifies a piece of snapshot metadata, which is made up of a key-value pair.</p>
    </td>
    </tr>
    <tr id="row6728134181412"><td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.09%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.98%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li0419202382514"></a>Parameters in the  **error**  field

    <a name="evs_04_2013_table15441099103019"></a>
    <table><thead align="left"><tr id="evs_04_2013_row54094047103019"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="evs_04_2013_p19541716103019"><a name="evs_04_2013_p19541716103019"></a><a name="evs_04_2013_p19541716103019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="evs_04_2013_p39375186103019"><a name="evs_04_2013_p39375186103019"></a><a name="evs_04_2013_p39375186103019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2013_p38578950103019"><a name="evs_04_2013_p38578950103019"></a><a name="evs_04_2013_p38578950103019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2013_row59401790103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p46815658103019"><a name="evs_04_2013_p46815658103019"></a><a name="evs_04_2013_p46815658103019"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p33971979103019"><a name="evs_04_2013_p33971979103019"></a><a name="evs_04_2013_p33971979103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p21623243103019"><a name="evs_04_2013_p21623243103019"></a><a name="evs_04_2013_p21623243103019"></a>Specifies the error message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="evs_04_2013_row60391466103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p59870541103019"><a name="evs_04_2013_p59870541103019"></a><a name="evs_04_2013_p59870541103019"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p17675690103019"><a name="evs_04_2013_p17675690103019"></a><a name="evs_04_2013_p17675690103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p6087468103019"><a name="evs_04_2013_p6087468103019"></a><a name="evs_04_2013_p6087468103019"></a>Specifies the error code returned when an error occurs.</p>
    <p id="evs_04_2013_p54787218103019"><a name="evs_04_2013_p54787218103019"></a><a name="evs_04_2013_p54787218103019"></a>For details about the error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "meta": {
            "key1": "value1"
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

