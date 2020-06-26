# Querying Loading Progress of a Lazyloading Disk<a name="evs_04_3006"></a>

## Function<a name="section1936774116116"></a>

This API is used to query the loading progress of a lazyloading disk.

## URI<a name="section5058598"></a>

-   URI format

    GET /v3/\{project\_id\}/os-vendor-volumes/\{volume\_id\}/internal-info

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


## Request<a name="section148111757132213"></a>

None

## Response<a name="section0512135353410"></a>

-   Parameter description

    <a name="table54141621245"></a>
    <table><thead align="left"><tr id="row19414321146"><th class="cellrowborder" valign="top" width="22.5%" id="mcps1.1.4.1.1"><p id="p7414192348"><a name="p7414192348"></a><a name="p7414192348"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.4.1.2"><p id="p17414226419"><a name="p17414226419"></a><a name="p17414226419"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.5%" id="mcps1.1.4.1.3"><p id="p184145212412"><a name="p184145212412"></a><a name="p184145212412"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row104141721746"><td class="cellrowborder" valign="top" width="22.5%" headers="mcps1.1.4.1.1 "><p id="p341410220413"><a name="p341410220413"></a><a name="p341410220413"></a>info</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.2 "><p id="p114145211417"><a name="p114145211417"></a><a name="p114145211417"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.5%" headers="mcps1.1.4.1.3 "><p id="p1941413214419"><a name="p1941413214419"></a><a name="p1941413214419"></a>Specifies the loading information, in percentage. For details, see <a href="#li362475412012">Parameter in the info field</a>.</p>
    </td>
    </tr>
    <tr id="row344911414299"><td class="cellrowborder" valign="top" width="22.5%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.5%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li362475412012"></a>Parameter in the  **info**  field

    <a name="table19635165418206"></a>
    <table><thead align="left"><tr id="row1263515547207"><th class="cellrowborder" valign="top" width="22.5%" id="mcps1.1.4.1.1"><p id="p1863525402013"><a name="p1863525402013"></a><a name="p1863525402013"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.1.4.1.2"><p id="p763615413205"><a name="p763615413205"></a><a name="p763615413205"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.5%" id="mcps1.1.4.1.3"><p id="p15636175442017"><a name="p15636175442017"></a><a name="p15636175442017"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row464365482018"><td class="cellrowborder" valign="top" width="22.5%" headers="mcps1.1.4.1.1 "><p id="p11643185452017"><a name="p11643185452017"></a><a name="p11643185452017"></a>loading_progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.2 "><p id="p6643054102018"><a name="p6643054102018"></a><a name="p6643054102018"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.5%" headers="mcps1.1.4.1.3 "><p id="p564395442015"><a name="p564395442015"></a><a name="p564395442015"></a>Specifies the loading progress of the lazyloading disk.</p>
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
        "info": {
            "loading_progress": 36
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

