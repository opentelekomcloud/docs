# Adding Metadata of an EVS Disk<a name="evs_04_2074"></a>

## Function<a name="section60214390"></a>

This API is used to add or update the metadata of an EVS disk.

## URI<a name="section5058598"></a>

-   URI format

    POST /v2/\{project\_id\}/volumes/\{volume\_id\}/metadata

-   Parameter description

    <a name="table58294385"></a>
    <table><thead align="left"><tr id="row24683273"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p53188122"><a name="p53188122"></a><a name="p53188122"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p13270664"><a name="p13270664"></a><a name="p13270664"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p1182010"><a name="p1182010"></a><a name="p1182010"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row28634009"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p37653388"><a name="p37653388"></a><a name="p37653388"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p30025596"><a name="p30025596"></a><a name="p30025596"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p16154192"><a name="p16154192"></a><a name="p16154192"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row11170003"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p32355065"><a name="p32355065"></a><a name="p32355065"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p3514615"><a name="p3514615"></a><a name="p3514615"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p16248438"><a name="p16248438"></a><a name="p16248438"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section45527389"></a>

-   Parameter description

    <a name="table31588048"></a>
    <table><thead align="left"><tr id="row57330849"><th class="cellrowborder" valign="top" width="17.491749174917494%" id="mcps1.1.5.1.1"><p id="p13287175"><a name="p13287175"></a><a name="p13287175"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.96129612961296%" id="mcps1.1.5.1.2"><p id="p2519427"><a name="p2519427"></a><a name="p2519427"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.481748174817483%" id="mcps1.1.5.1.3"><p id="p2747002"><a name="p2747002"></a><a name="p2747002"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.06520652065206%" id="mcps1.1.5.1.4"><p id="p21180630"><a name="p21180630"></a><a name="p21180630"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row53167494153413"><td class="cellrowborder" valign="top" width="17.491749174917494%" headers="mcps1.1.5.1.1 "><p id="p11599783153413"><a name="p11599783153413"></a><a name="p11599783153413"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.96129612961296%" headers="mcps1.1.5.1.2 "><p id="p58405153413"><a name="p58405153413"></a><a name="p58405153413"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.481748174817483%" headers="mcps1.1.5.1.3 "><p id="p4730855153413"><a name="p4730855153413"></a><a name="p4730855153413"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.06520652065206%" headers="mcps1.1.5.1.4 "><p id="p203071547124818"><a name="p203071547124818"></a><a name="p203071547124818"></a>Specifies the metadata to be updated. For details, see <a href="#li54973602211845">Parameter in the metadata field</a>.</p>
    <p id="p47654998153413"><a name="p47654998153413"></a><a name="p47654998153413"></a><span id="text17527183012510"><a name="text17527183012510"></a><a name="text17527183012510"></a>The length of the key or value in the metadata cannot exceed 255 bytes.</span></p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li54973602211845"></a>Parameter in the  **metadata**  field

    <a name="table32717123212358"></a>
    <table><thead align="left"><tr id="row2280240212358"><th class="cellrowborder" valign="top" width="17.49%" id="mcps1.1.5.1.1"><p id="p50481723212358"><a name="p50481723212358"></a><a name="p50481723212358"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.959999999999999%" id="mcps1.1.5.1.2"><p id="p62487767212358"><a name="p62487767212358"></a><a name="p62487767212358"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.299999999999997%" id="mcps1.1.5.1.3"><p id="p28344363212358"><a name="p28344363212358"></a><a name="p28344363212358"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.25%" id="mcps1.1.5.1.4"><p id="p14192096212358"><a name="p14192096212358"></a><a name="p14192096212358"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8709150212358"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p34352524212358"><a name="p34352524212358"></a><a name="p34352524212358"></a>key_val</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.959999999999999%" headers="mcps1.1.5.1.2 "><p id="p31091026212358"><a name="p31091026212358"></a><a name="p31091026212358"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p35345177212358"><a name="p35345177212358"></a><a name="p35345177212358"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.25%" headers="mcps1.1.5.1.4 "><p id="p44387080212358"><a name="p44387080212358"></a><a name="p44387080212358"></a>Specifies the metadata information, which is made up of one or multiple key-value pairs.</p>
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


## Response<a name="section7093323"></a>

-   Parameter description

    <a name="table11977025201856"></a>
    <table><thead align="left"><tr id="row8102228201856"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="p11709178184818"><a name="p11709178184818"></a><a name="p11709178184818"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="p67131989483"><a name="p67131989483"></a><a name="p67131989483"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p87153824811"><a name="p87153824811"></a><a name="p87153824811"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60683035201856"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p16378828201856"><a name="p16378828201856"></a><a name="p16378828201856"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p6490369115541"><a name="p6490369115541"></a><a name="p6490369115541"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p20205612201856"><a name="p20205612201856"></a><a name="p20205612201856"></a>Specifies the disk metadata, which is made up of key-value pairs.</p>
    </td>
    </tr>
    <tr id="row11511747165814"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
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


## Status Codes<a name="section63839913"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

