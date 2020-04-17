# Adding Metadata of an EVS Snapshot<a name="evs_04_3062"></a>

## Function<a name="section4805694511340"></a>

This API is used to add the metadata of an EVS snapshot.

## URI<a name="section268627411340"></a>

-   URI format

    POST /v3/\{project\_id\}/snapshots/\{snapshot\_id\}/metadata

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
    <tbody><tr id="row2890086411340"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p116468178394"><a name="p116468178394"></a><a name="p116468178394"></a>project_id</p>
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
    </tbody>
    </table>


## Request<a name="section87667311340"></a>

-   Parameter description

    <a name="evs_04_2099_table9796961112814"></a>
    <table><thead align="left"><tr id="evs_04_2099_row1541837112814"><th class="cellrowborder" valign="top" width="19.86801319868013%" id="mcps1.1.5.1.1"><p id="evs_04_2099_p51734634112841"><a name="evs_04_2099_p51734634112841"></a><a name="evs_04_2099_p51734634112841"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.978402159784022%" id="mcps1.1.5.1.2"><p id="evs_04_2099_p29755832112841"><a name="evs_04_2099_p29755832112841"></a><a name="evs_04_2099_p29755832112841"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.238176182381764%" id="mcps1.1.5.1.3"><p id="evs_04_2099_p61412231112841"><a name="evs_04_2099_p61412231112841"></a><a name="evs_04_2099_p61412231112841"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.1.5.1.4"><p id="evs_04_2099_p8334847112841"><a name="evs_04_2099_p8334847112841"></a><a name="evs_04_2099_p8334847112841"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2099_row15415933112814"><td class="cellrowborder" valign="top" width="19.86801319868013%" headers="mcps1.1.5.1.1 "><p id="evs_04_2099_p40731045112814"><a name="evs_04_2099_p40731045112814"></a><a name="evs_04_2099_p40731045112814"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.978402159784022%" headers="mcps1.1.5.1.2 "><p id="evs_04_2099_p10880325112814"><a name="evs_04_2099_p10880325112814"></a><a name="evs_04_2099_p10880325112814"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.238176182381764%" headers="mcps1.1.5.1.3 "><p id="evs_04_2099_p8891142112814"><a name="evs_04_2099_p8891142112814"></a><a name="evs_04_2099_p8891142112814"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.1.5.1.4 "><p id="evs_04_2099_p49093903112814"><a name="evs_04_2099_p49093903112814"></a><a name="evs_04_2099_p49093903112814"></a>Specifies the metadata to be added. For details, see <a href="#evs_04_2099_li39191951112814">Parameter in the metadata field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2099_li39191951112814"></a>Parameter in the  **metadata**  field

    <a name="evs_04_2099_table17183241112814"></a>
    <table><thead align="left"><tr id="evs_04_2099_row29429246112814"><th class="cellrowborder" valign="top" width="19.68%" id="mcps1.1.5.1.1"><p id="evs_04_2099_p59908985112845"><a name="evs_04_2099_p59908985112845"></a><a name="evs_04_2099_p59908985112845"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.54%" id="mcps1.1.5.1.2"><p id="evs_04_2099_p20789580112845"><a name="evs_04_2099_p20789580112845"></a><a name="evs_04_2099_p20789580112845"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.86%" id="mcps1.1.5.1.3"><p id="evs_04_2099_p6234457112845"><a name="evs_04_2099_p6234457112845"></a><a name="evs_04_2099_p6234457112845"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.92%" id="mcps1.1.5.1.4"><p id="evs_04_2099_p35228998112845"><a name="evs_04_2099_p35228998112845"></a><a name="evs_04_2099_p35228998112845"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2099_row40467139112814"><td class="cellrowborder" valign="top" width="19.68%" headers="mcps1.1.5.1.1 "><p id="evs_04_2099_p56612845112814"><a name="evs_04_2099_p56612845112814"></a><a name="evs_04_2099_p56612845112814"></a>key_val</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.2 "><p id="evs_04_2099_p22237723112814"><a name="evs_04_2099_p22237723112814"></a><a name="evs_04_2099_p22237723112814"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.1.5.1.3 "><p id="evs_04_2099_p56425142112814"><a name="evs_04_2099_p56425142112814"></a><a name="evs_04_2099_p56425142112814"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.92%" headers="mcps1.1.5.1.4 "><p id="evs_04_2099_p7033765112814"><a name="evs_04_2099_p7033765112814"></a><a name="evs_04_2099_p7033765112814"></a>Specifies the metadata information, which is made up of one or multiple key-value pairs.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "metadata": {
            "key1": "value1", 
            "key2": "value2"
        }
    }
    ```


## Response<a name="section5147449911340"></a>

-   Parameter description

    <a name="evs_04_2099_table11977025201856"></a>
    <table><thead align="left"><tr id="evs_04_2099_row8102228201856"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="evs_04_2099_p52300707201856"><a name="evs_04_2099_p52300707201856"></a><a name="evs_04_2099_p52300707201856"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="evs_04_2099_p3642697315541"><a name="evs_04_2099_p3642697315541"></a><a name="evs_04_2099_p3642697315541"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="evs_04_2099_p17319263201856"><a name="evs_04_2099_p17319263201856"></a><a name="evs_04_2099_p17319263201856"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2099_row60683035201856"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2099_p16378828201856"><a name="evs_04_2099_p16378828201856"></a><a name="evs_04_2099_p16378828201856"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2099_p6490369115541"><a name="evs_04_2099_p6490369115541"></a><a name="evs_04_2099_p6490369115541"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2099_p20205612201856"><a name="evs_04_2099_p20205612201856"></a><a name="evs_04_2099_p20205612201856"></a>Specifies the snapshot metadata, which is made up of key-value pairs.</p>
    </td>
    </tr>
    <tr id="evs_04_2099_row1193419413714"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2099_p129522216412"><a name="evs_04_2099_p129522216412"></a><a name="evs_04_2099_p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2099_p1595262111415"><a name="evs_04_2099_p1595262111415"></a><a name="evs_04_2099_p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2099_p109527215417"><a name="evs_04_2099_p109527215417"></a><a name="evs_04_2099_p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#evs_04_2099_li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2099_li0419202382514"></a>Parameters in the  **error**  field

    <a name="evs_04_2099_evs_04_2013_table15441099103019"></a>
    <table><thead align="left"><tr id="evs_04_2099_evs_04_2013_row54094047103019"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="evs_04_2099_evs_04_2013_p19541716103019"><a name="evs_04_2099_evs_04_2013_p19541716103019"></a><a name="evs_04_2099_evs_04_2013_p19541716103019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="evs_04_2099_evs_04_2013_p39375186103019"><a name="evs_04_2099_evs_04_2013_p39375186103019"></a><a name="evs_04_2099_evs_04_2013_p39375186103019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2099_evs_04_2013_p38578950103019"><a name="evs_04_2099_evs_04_2013_p38578950103019"></a><a name="evs_04_2099_evs_04_2013_p38578950103019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2099_evs_04_2013_row59401790103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2099_evs_04_2013_p46815658103019"><a name="evs_04_2099_evs_04_2013_p46815658103019"></a><a name="evs_04_2099_evs_04_2013_p46815658103019"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2099_evs_04_2013_p33971979103019"><a name="evs_04_2099_evs_04_2013_p33971979103019"></a><a name="evs_04_2099_evs_04_2013_p33971979103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2099_evs_04_2013_p21623243103019"><a name="evs_04_2099_evs_04_2013_p21623243103019"></a><a name="evs_04_2099_evs_04_2013_p21623243103019"></a>Specifies the error message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="evs_04_2099_evs_04_2013_row60391466103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2099_evs_04_2013_p59870541103019"><a name="evs_04_2099_evs_04_2013_p59870541103019"></a><a name="evs_04_2099_evs_04_2013_p59870541103019"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2099_evs_04_2013_p17675690103019"><a name="evs_04_2099_evs_04_2013_p17675690103019"></a><a name="evs_04_2099_evs_04_2013_p17675690103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2099_evs_04_2013_p6087468103019"><a name="evs_04_2099_evs_04_2013_p6087468103019"></a><a name="evs_04_2099_evs_04_2013_p6087468103019"></a>Specifies the error code returned when an error occurs.</p>
    <p id="evs_04_2099_evs_04_2013_p54787218103019"><a name="evs_04_2099_evs_04_2013_p54787218103019"></a><a name="evs_04_2099_evs_04_2013_p54787218103019"></a>For details about the error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "metadata": {
            "key1": "value1", 
            "key2": "value2"
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

