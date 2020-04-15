# Updating Metadata of an EVS Disk<a name="evs_04_3040"></a>

## Function<a name="section19390540"></a>

This API is used to update the metadata of an EVS disk.

## URI<a name="section40297137"></a>

-   URI format

    PUT /v3/\{project\_id\}/volumes/\{volume\_id\}/metadata

-   Parameter description

    <a name="table8745607"></a>
    <table><thead align="left"><tr id="row15985080"><th class="cellrowborder" valign="top" width="30.509999999999998%" id="mcps1.1.4.1.1"><p id="p19723089"><a name="p19723089"></a><a name="p19723089"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.48%" id="mcps1.1.4.1.2"><p id="p54066375"><a name="p54066375"></a><a name="p54066375"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.01%" id="mcps1.1.4.1.3"><p id="p17300225"><a name="p17300225"></a><a name="p17300225"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59140967"><td class="cellrowborder" valign="top" width="30.509999999999998%" headers="mcps1.1.4.1.1 "><p id="p25689059"><a name="p25689059"></a><a name="p25689059"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p439002"><a name="p439002"></a><a name="p439002"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.4.1.3 "><p id="p35559222"><a name="p35559222"></a><a name="p35559222"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row51597550"><td class="cellrowborder" valign="top" width="30.509999999999998%" headers="mcps1.1.4.1.1 "><p id="p18651996"><a name="p18651996"></a><a name="p18651996"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.4.1.2 "><p id="p34416674"><a name="p34416674"></a><a name="p34416674"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.4.1.3 "><p id="p36287209"><a name="p36287209"></a><a name="p36287209"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section27129916"></a>

-   Parameter description

    <a name="evs_04_2076_table31588048"></a>
    <table><thead align="left"><tr id="evs_04_2076_row57330849"><th class="cellrowborder" valign="top" width="17.49%" id="mcps1.1.5.1.1"><p id="evs_04_2076_p13287175"><a name="evs_04_2076_p13287175"></a><a name="evs_04_2076_p13287175"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.22%" id="mcps1.1.5.1.2"><p id="evs_04_2076_p2519427"><a name="evs_04_2076_p2519427"></a><a name="evs_04_2076_p2519427"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.42%" id="mcps1.1.5.1.3"><p id="evs_04_2076_p2747002"><a name="evs_04_2076_p2747002"></a><a name="evs_04_2076_p2747002"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.870000000000005%" id="mcps1.1.5.1.4"><p id="evs_04_2076_p21180630"><a name="evs_04_2076_p21180630"></a><a name="evs_04_2076_p21180630"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2076_row53167494153413"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="evs_04_2076_p11599783153413"><a name="evs_04_2076_p11599783153413"></a><a name="evs_04_2076_p11599783153413"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.22%" headers="mcps1.1.5.1.2 "><p id="evs_04_2076_p58405153413"><a name="evs_04_2076_p58405153413"></a><a name="evs_04_2076_p58405153413"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.1.5.1.3 "><p id="evs_04_2076_p4730855153413"><a name="evs_04_2076_p4730855153413"></a><a name="evs_04_2076_p4730855153413"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.870000000000005%" headers="mcps1.1.5.1.4 "><p id="evs_04_2076_p47654998153413"><a name="evs_04_2076_p47654998153413"></a><a name="evs_04_2076_p47654998153413"></a>Specifies the disk metadata to be updated. For details, see <a href="#evs_04_2076_li54973602211845">Parameter in the metadata field</a>.</p>
    <p id="evs_04_2076_p16564956142512"><a name="evs_04_2076_p16564956142512"></a><a name="evs_04_2076_p16564956142512"></a><span id="evs_04_2076_text17527183012510"><a name="evs_04_2076_text17527183012510"></a><a name="evs_04_2076_text17527183012510"></a>The length of the key or value in the metadata cannot exceed 255 bytes.</span></p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2076_li54973602211845"></a>Parameter in the  **metadata**  field

    <a name="evs_04_2076_table32717123212358"></a>
    <table><thead align="left"><tr id="evs_04_2076_row2280240212358"><th class="cellrowborder" valign="top" width="17.49%" id="mcps1.1.5.1.1"><p id="evs_04_2076_p1603155994915"><a name="evs_04_2076_p1603155994915"></a><a name="evs_04_2076_p1603155994915"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.22%" id="mcps1.1.5.1.2"><p id="evs_04_2076_p62487767212358"><a name="evs_04_2076_p62487767212358"></a><a name="evs_04_2076_p62487767212358"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.05%" id="mcps1.1.5.1.3"><p id="evs_04_2076_p28344363212358"><a name="evs_04_2076_p28344363212358"></a><a name="evs_04_2076_p28344363212358"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.24%" id="mcps1.1.5.1.4"><p id="evs_04_2076_p14192096212358"><a name="evs_04_2076_p14192096212358"></a><a name="evs_04_2076_p14192096212358"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2076_row8709150212358"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="evs_04_2076_p34352524212358"><a name="evs_04_2076_p34352524212358"></a><a name="evs_04_2076_p34352524212358"></a>key_val</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.22%" headers="mcps1.1.5.1.2 "><p id="evs_04_2076_p31091026212358"><a name="evs_04_2076_p31091026212358"></a><a name="evs_04_2076_p31091026212358"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.05%" headers="mcps1.1.5.1.3 "><p id="evs_04_2076_p35345177212358"><a name="evs_04_2076_p35345177212358"></a><a name="evs_04_2076_p35345177212358"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.24%" headers="mcps1.1.5.1.4 "><p id="evs_04_2076_p44387080212358"><a name="evs_04_2076_p44387080212358"></a><a name="evs_04_2076_p44387080212358"></a>Specifies the metadata information, which is made up of one or multiple key-value pairs.</p>
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


## Response<a name="section42842654"></a>

-   Parameter description

    <a name="evs_04_2076_table11977025201856"></a>
    <table><thead align="left"><tr id="evs_04_2076_row8102228201856"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="evs_04_2076_p52300707201856"><a name="evs_04_2076_p52300707201856"></a><a name="evs_04_2076_p52300707201856"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="evs_04_2076_p3642697315541"><a name="evs_04_2076_p3642697315541"></a><a name="evs_04_2076_p3642697315541"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="evs_04_2076_p17319263201856"><a name="evs_04_2076_p17319263201856"></a><a name="evs_04_2076_p17319263201856"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2076_row60683035201856"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2076_p16378828201856"><a name="evs_04_2076_p16378828201856"></a><a name="evs_04_2076_p16378828201856"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2076_p6490369115541"><a name="evs_04_2076_p6490369115541"></a><a name="evs_04_2076_p6490369115541"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2076_p20205612201856"><a name="evs_04_2076_p20205612201856"></a><a name="evs_04_2076_p20205612201856"></a>Specifies the disk metadata, which is made up of key-value pairs.</p>
    </td>
    </tr>
    <tr id="evs_04_2076_row1896317141164"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2076_p129522216412"><a name="evs_04_2076_p129522216412"></a><a name="evs_04_2076_p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2076_p1595262111415"><a name="evs_04_2076_p1595262111415"></a><a name="evs_04_2076_p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2076_p109527215417"><a name="evs_04_2076_p109527215417"></a><a name="evs_04_2076_p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#evs_04_2076_li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2076_li0419202382514"></a>Parameters in the  **error**  field

    <a name="evs_04_2076_evs_04_2013_table15441099103019"></a>
    <table><thead align="left"><tr id="evs_04_2076_evs_04_2013_row54094047103019"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="evs_04_2076_evs_04_2013_p19541716103019"><a name="evs_04_2076_evs_04_2013_p19541716103019"></a><a name="evs_04_2076_evs_04_2013_p19541716103019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="evs_04_2076_evs_04_2013_p39375186103019"><a name="evs_04_2076_evs_04_2013_p39375186103019"></a><a name="evs_04_2076_evs_04_2013_p39375186103019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2076_evs_04_2013_p38578950103019"><a name="evs_04_2076_evs_04_2013_p38578950103019"></a><a name="evs_04_2076_evs_04_2013_p38578950103019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2076_evs_04_2013_row59401790103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2076_evs_04_2013_p46815658103019"><a name="evs_04_2076_evs_04_2013_p46815658103019"></a><a name="evs_04_2076_evs_04_2013_p46815658103019"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2076_evs_04_2013_p33971979103019"><a name="evs_04_2076_evs_04_2013_p33971979103019"></a><a name="evs_04_2076_evs_04_2013_p33971979103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2076_evs_04_2013_p21623243103019"><a name="evs_04_2076_evs_04_2013_p21623243103019"></a><a name="evs_04_2076_evs_04_2013_p21623243103019"></a>Specifies the error message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="evs_04_2076_evs_04_2013_row60391466103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2076_evs_04_2013_p59870541103019"><a name="evs_04_2076_evs_04_2013_p59870541103019"></a><a name="evs_04_2076_evs_04_2013_p59870541103019"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2076_evs_04_2013_p17675690103019"><a name="evs_04_2076_evs_04_2013_p17675690103019"></a><a name="evs_04_2076_evs_04_2013_p17675690103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2076_evs_04_2013_p6087468103019"><a name="evs_04_2076_evs_04_2013_p6087468103019"></a><a name="evs_04_2076_evs_04_2013_p6087468103019"></a>Specifies the error code returned when an error occurs.</p>
    <p id="evs_04_2076_evs_04_2013_p54787218103019"><a name="evs_04_2076_evs_04_2013_p54787218103019"></a><a name="evs_04_2076_evs_04_2013_p54787218103019"></a>For details about the error code, see <a href="error-codes.md">Error Codes</a>.</p>
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

    In the preceding example,  **error**  indicates a general error, for example,  **badrequest**  or  **itemNotFound**. An example is provided as follows:

    ```
    {
        "badrequest": {
            "message": "XXXX", 
            "code": "XXX"
        }
    }
    ```


## Status Codes<a name="section50039568"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

