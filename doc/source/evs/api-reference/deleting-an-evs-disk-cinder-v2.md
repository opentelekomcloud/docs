# Deleting an EVS Disk<a name="evs_04_2066"></a>

## Function<a name="section10932885"></a>

This API is used to delete an EVS disk.

## URI<a name="section31287108"></a>

-   URI format

    DELETE /v2/\{project\_id\}/volumes/\{volume\_id\}

-   Parameter description

    <a name="table44522499"></a>
    <table><thead align="left"><tr id="row39474480"><th class="cellrowborder" valign="top" width="33.33%" id="mcps1.1.4.1.1"><p id="p43316293"><a name="p43316293"></a><a name="p43316293"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.549999999999997%" id="mcps1.1.4.1.2"><p id="p18958859"><a name="p18958859"></a><a name="p18958859"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.12%" id="mcps1.1.4.1.3"><p id="p59272617"><a name="p59272617"></a><a name="p59272617"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row36352712"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.1.4.1.1 "><p id="p58888592"><a name="p58888592"></a><a name="p58888592"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.1.4.1.2 "><p id="p5246632"><a name="p5246632"></a><a name="p5246632"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.1.4.1.3 "><p id="p22324024"><a name="p22324024"></a><a name="p22324024"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row66698493"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.1.4.1.1 "><p id="p33868853"><a name="p33868853"></a><a name="p33868853"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.1.4.1.2 "><p id="p59022586"><a name="p59022586"></a><a name="p59022586"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.1.4.1.3 "><p id="p16100147"><a name="p16100147"></a><a name="p16100147"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request filter parameters

    <a name="table114096539515"></a>
    <table><thead align="left"><tr id="row64913538519"><th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.1.5.1.1"><p id="p14491115311514"><a name="p14491115311514"></a><a name="p14491115311514"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.1.5.1.2"><p id="p54911753125116"><a name="p54911753125116"></a><a name="p54911753125116"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.1.5.1.3"><p id="p10491105315113"><a name="p10491105315113"></a><a name="p10491105315113"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.45454545454546%" id="mcps1.1.5.1.4"><p id="p16491553125110"><a name="p16491553125110"></a><a name="p16491553125110"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64916530515"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="p14491953135112"><a name="p14491953135112"></a><a name="p14491953135112"></a>cascade</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.1.5.1.2 "><p id="p15491185365111"><a name="p15491185365111"></a><a name="p15491185365111"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.3 "><p id="p349155345117"><a name="p349155345117"></a><a name="p349155345117"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.1.5.1.4 "><p id="p1941233905911"><a name="p1941233905911"></a><a name="p1941233905911"></a>Specifies to delete all snapshots associated with the disk. The default value is <strong id="b842352706161355"><a name="b842352706161355"></a><a name="b842352706161355"></a>false</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section13148517"></a>

The following example shows how to delete a disk and all its snapshots.

-   Example request

    ```
    DELETE https://{endpoint}/v2/{project_id}/volumes/{volume_id}?cascade=true
    ```


## Response<a name="section51227795"></a>

-   Parameter description

    <a name="table46654279102454"></a>
    <table><thead align="left"><tr id="row6664264102454"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="p2934472102454"><a name="p2934472102454"></a><a name="p2934472102454"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.62%" id="mcps1.1.4.1.2"><p id="p1338569102927"><a name="p1338569102927"></a><a name="p1338569102927"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p23036595102454"><a name="p23036595102454"></a><a name="p23036595102454"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12419334102454"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
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

    In the preceding example,  **error**  indicates a general error, for example,  **badrequest**  or  **itemNotFound**. An example is provided as follows:

    ```
    {
        "itemNotFound": {
            "message": "XXXX", 
            "code": "XXX"
        }
    }
    ```


## Status Codes<a name="section58396974"></a>

-   Normal

    202


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

