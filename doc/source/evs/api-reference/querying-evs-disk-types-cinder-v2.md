# Querying EVS Disk Types<a name="evs_04_2071"></a>

## Function<a name="section18389930"></a>

This API is used to query EVS disk types and display the query results in a list.

## URI<a name="section31291646"></a>

-   URI format

    GET /v2/\{project\_id\}/types

-   Parameter description

    <a name="table57434139"></a>
    <table><thead align="left"><tr id="row461342"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p37368736"><a name="p37368736"></a><a name="p37368736"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p6968762"><a name="p6968762"></a><a name="p6968762"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p27598869"><a name="p27598869"></a><a name="p27598869"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20915929"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p16468652"><a name="p16468652"></a><a name="p16468652"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p58892473"><a name="p58892473"></a><a name="p58892473"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p5560998"><a name="p5560998"></a><a name="p5560998"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section13189358"></a>

-   Example request

    ```
    GET https://{endpoint}/v2/{project_id}/types
    ```


## Response<a name="section51595365"></a>

-   Parameter description

    <a name="table157189144113"></a>
    <table><thead align="left"><tr id="row37118915416"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="p671295419"><a name="p671295419"></a><a name="p671295419"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="p47159114117"><a name="p47159114117"></a><a name="p47159114117"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p1671199174116"><a name="p1671199174116"></a><a name="p1671199174116"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row177120964114"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p14711298413"><a name="p14711298413"></a><a name="p14711298413"></a>volume_types</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p971892416"><a name="p971892416"></a><a name="p971892416"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p157117910419"><a name="p157117910419"></a><a name="p157117910419"></a>Specifies the list of queried disk types. For details, see <a href="#li61994451201537">Parameters in the volume_types field</a>.</p>
    </td>
    </tr>
    <tr id="row971797416"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li61994451201537"></a>Parameters in the  **volume\_types**  field

    <a name="table5015685217931"></a>
    <table><thead align="left"><tr id="row3525603317931"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="p3716642517931"><a name="p3716642517931"></a><a name="p3716642517931"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="p459600531514"><a name="p459600531514"></a><a name="p459600531514"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p4241583117931"><a name="p4241583117931"></a><a name="p4241583117931"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1313028517931"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p5692013517931"><a name="p5692013517931"></a><a name="p5692013517931"></a>extra_specs</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p317768361514"><a name="p317768361514"></a><a name="p317768361514"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p5928829717931"><a name="p5928829717931"></a><a name="p5928829717931"></a>Specifies the disk type specifications. For details, see <a href="#li963595619529">Parameters in the extra_specs field</a>.</p>
    </td>
    </tr>
    <tr id="row6655870217931"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p2254579917931"><a name="p2254579917931"></a><a name="p2254579917931"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p378706671514"><a name="p378706671514"></a><a name="p378706671514"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p1505171317931"><a name="p1505171317931"></a><a name="p1505171317931"></a>Specifies the name of the disk type.</p>
    </td>
    </tr>
    <tr id="row124769217931"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p3395425317931"><a name="p3395425317931"></a><a name="p3395425317931"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p476251801514"><a name="p476251801514"></a><a name="p476251801514"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p3954068517931"><a name="p3954068517931"></a><a name="p3954068517931"></a>Specifies the ID of the disk type.</p>
    </td>
    </tr>
    <tr id="row17240824161631"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p54329535161631"><a name="p54329535161631"></a><a name="p54329535161631"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p38616177161631"><a name="p38616177161631"></a><a name="p38616177161631"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p24780220161631"><a name="p24780220161631"></a><a name="p24780220161631"></a>Specifies the description of the disk type.</p>
    </td>
    </tr>
    <tr id="row1027115162029"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p16087523162029"><a name="p16087523162029"></a><a name="p16087523162029"></a>qos_specs_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p28020971162029"><a name="p28020971162029"></a><a name="p28020971162029"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p34413580162029"><a name="p34413580162029"></a><a name="p34413580162029"></a><span id="text3111131184916"><a name="text3111131184916"></a><a name="text3111131184916"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row12948331162139"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p42181927162139"><a name="p42181927162139"></a><a name="p42181927162139"></a>is_public</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p61292894162139"><a name="p61292894162139"></a><a name="p61292894162139"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p26369379162139"><a name="p26369379162139"></a><a name="p26369379162139"></a><span id="text10706161911492"><a name="text10706161911492"></a><a name="text10706161911492"></a>Reserved field</span></p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li963595619529"></a>Parameters in the  **extra\_specs**  field

    <a name="table1763545695210"></a>
    <table><thead align="left"><tr id="row16361656165213"><th class="cellrowborder" valign="top" width="21.45%" id="mcps1.1.4.1.1"><p id="p1763619566527"><a name="p1763619566527"></a><a name="p1763619566527"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.41%" id="mcps1.1.4.1.2"><p id="p18636105619529"><a name="p18636105619529"></a><a name="p18636105619529"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p186361556155214"><a name="p186361556155214"></a><a name="p186361556155214"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56365565526"><td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.1.4.1.1 "><p id="p063625610529"><a name="p063625610529"></a><a name="p063625610529"></a>volume_backend_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.41%" headers="mcps1.1.4.1.2 "><p id="p3636165635219"><a name="p3636165635219"></a><a name="p3636165635219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p17636185614527"><a name="p17636185614527"></a><a name="p17636185614527"></a><span id="text205233101097"><a name="text205233101097"></a><a name="text205233101097"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row156362568523"><td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.1.4.1.1 "><p id="p863675695214"><a name="p863675695214"></a><a name="p863675695214"></a>availability-zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.41%" headers="mcps1.1.4.1.2 "><p id="p8636175665214"><a name="p8636175665214"></a><a name="p8636175665214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p18636356185213"><a name="p18636356185213"></a><a name="p18636356185213"></a><span id="text533914121390"><a name="text533914121390"></a><a name="text533914121390"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row17844276596"><td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.1.4.1.1 "><p id="p178418274593"><a name="p178418274593"></a><a name="p178418274593"></a>HW:availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.41%" headers="mcps1.1.4.1.2 "><p id="p168416276599"><a name="p168416276599"></a><a name="p168416276599"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p1540410211408"><a name="p1540410211408"></a><a name="p1540410211408"></a><span id="evs_04_2071_text533914121390"><a name="evs_04_2071_text533914121390"></a><a name="evs_04_2071_text533914121390"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row3637135611527"><td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.1.4.1.1 "><p id="p163710561529"><a name="p163710561529"></a><a name="p163710561529"></a>RESKEY:availability_zones</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.41%" headers="mcps1.1.4.1.2 "><p id="p166374562525"><a name="p166374562525"></a><a name="p166374562525"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p3637756205214"><a name="p3637756205214"></a><a name="p3637756205214"></a>Specifies the AZs that support the current disk type.</p>
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
        "volume_types": [
            {
                "extra_specs": {
                    "volume_backend_name": "SAS", 
                    "availability-zone": "az-dc-1"
                }, 
                "name": "SAS", 
                "qos_specs_id": null, 
                "id": "6c81c680-df58-4512-81e7-ecf66d160638", 
                "is_public": true, 
                "description": null
            }, 
            {
                "extra_specs": {
                    "volume_backend_name": "SATA", 
                    "availability-zone": "az-dc-1"
                }, 
                "name": "SATA", 
                "qos_specs_id": "585f29d6-7147-42e7-bfb8-ca214f640f6f", 
                "is_public": true, 
                "id": "ea6e3c13-aac5-46e0-b280-745ed272e662", 
                "description": null
            }, 
            {
                "extra_specs": {
                    "volume_backend_name": "SSD", 
                    "availability-zone": "az-dc-1"
                }, 
                "name": "SSD", 
                "qos_specs_id": "39b0c29a-308b-4f86-b478-5d3d02a43837", 
                "is_public": true, 
                "id": "6f2dee9e-82f0-4be3-ad89-bae605a3d24f", 
                "description": null
            }
        ]
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


## Status Codes<a name="section61705107"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

