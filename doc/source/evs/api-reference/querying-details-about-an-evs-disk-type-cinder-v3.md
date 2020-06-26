# Querying Details About an EVS Disk Type<a name="evs_04_3036"></a>

## Function<a name="section48630964"></a>

This API is used to query details about an EVS disk type.

## URI<a name="section35025494"></a>

-   URI format

    GET /v3/\{project\_id\}/types/\{type\_id\}

-   Parameter description

    <a name="table3865173"></a>
    <table><thead align="left"><tr id="row43603258"><th class="cellrowborder" valign="top" width="33.33%" id="mcps1.1.4.1.1"><p id="p42202994"><a name="p42202994"></a><a name="p42202994"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.93%" id="mcps1.1.4.1.2"><p id="p62999330"><a name="p62999330"></a><a name="p62999330"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.739999999999995%" id="mcps1.1.4.1.3"><p id="p2672115"><a name="p2672115"></a><a name="p2672115"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15114764"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.1.4.1.1 "><p id="p16336406"><a name="p16336406"></a><a name="p16336406"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.1.4.1.2 "><p id="p48180537"><a name="p48180537"></a><a name="p48180537"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.739999999999995%" headers="mcps1.1.4.1.3 "><p id="p10309404"><a name="p10309404"></a><a name="p10309404"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row25675773"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.1.4.1.1 "><p id="p66471715"><a name="p66471715"></a><a name="p66471715"></a>type_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.1.4.1.2 "><p id="p15499871"><a name="p15499871"></a><a name="p15499871"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.739999999999995%" headers="mcps1.1.4.1.3 "><p id="p47530006"><a name="p47530006"></a><a name="p47530006"></a>Specifies the disk type ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section46793998"></a>

-   Example request

    ```
    GET https://{endpoint}/v3/{project_id}/types/6c81c680-df58-4512-81e7-ecf66d160638
    ```


## Response<a name="section18492804"></a>

-   Parameter description

    <a name="evs_04_2072_table154241211124616"></a>
    <table><thead align="left"><tr id="evs_04_2072_row342551116468"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="evs_04_2072_p14251411164617"><a name="evs_04_2072_p14251411164617"></a><a name="evs_04_2072_p14251411164617"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="evs_04_2072_p642517110469"><a name="evs_04_2072_p642517110469"></a><a name="evs_04_2072_p642517110469"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="evs_04_2072_p104258110465"><a name="evs_04_2072_p104258110465"></a><a name="evs_04_2072_p104258110465"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2072_row8425131110465"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2072_p2425101134615"><a name="evs_04_2072_p2425101134615"></a><a name="evs_04_2072_p2425101134615"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2072_p5425011174619"><a name="evs_04_2072_p5425011174619"></a><a name="evs_04_2072_p5425011174619"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2072_p9425181174611"><a name="evs_04_2072_p9425181174611"></a><a name="evs_04_2072_p9425181174611"></a>Specifies the details of queried disk types. For details, see <a href="#evs_04_2072_li27654073201555">Parameters in the volume_type field</a>.</p>
    </td>
    </tr>
    <tr id="evs_04_2072_row1742591164617"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2072_p129522216412"><a name="evs_04_2072_p129522216412"></a><a name="evs_04_2072_p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2072_p1595262111415"><a name="evs_04_2072_p1595262111415"></a><a name="evs_04_2072_p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2072_p109527215417"><a name="evs_04_2072_p109527215417"></a><a name="evs_04_2072_p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#evs_04_2072_li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2072_li27654073201555"></a>Parameters in the  **volume\_type**  field

    <a name="evs_04_2072_table6170753515253"></a>
    <table><thead align="left"><tr id="evs_04_2072_row4217445215253"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="evs_04_2072_p6068742915253"><a name="evs_04_2072_p6068742915253"></a><a name="evs_04_2072_p6068742915253"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="evs_04_2072_p1673474815253"><a name="evs_04_2072_p1673474815253"></a><a name="evs_04_2072_p1673474815253"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="evs_04_2072_p658034115253"><a name="evs_04_2072_p658034115253"></a><a name="evs_04_2072_p658034115253"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2072_row6324564115253"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2072_p2262329715253"><a name="evs_04_2072_p2262329715253"></a><a name="evs_04_2072_p2262329715253"></a>extra_specs</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2072_p2054778215253"><a name="evs_04_2072_p2054778215253"></a><a name="evs_04_2072_p2054778215253"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2072_p5940085315253"><a name="evs_04_2072_p5940085315253"></a><a name="evs_04_2072_p5940085315253"></a>Specifies the disk type specifications. For details, see <a href="#evs_04_2072_li1957456185414">Parameters in the extra_specs field</a>.</p>
    </td>
    </tr>
    <tr id="evs_04_2072_row1760216615253"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2072_p1648936615253"><a name="evs_04_2072_p1648936615253"></a><a name="evs_04_2072_p1648936615253"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2072_p6057028715253"><a name="evs_04_2072_p6057028715253"></a><a name="evs_04_2072_p6057028715253"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2072_p5006999315253"><a name="evs_04_2072_p5006999315253"></a><a name="evs_04_2072_p5006999315253"></a>Specifies the name of the disk type.</p>
    </td>
    </tr>
    <tr id="evs_04_2072_row4797675615253"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2072_p6091205315253"><a name="evs_04_2072_p6091205315253"></a><a name="evs_04_2072_p6091205315253"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2072_p3492929915253"><a name="evs_04_2072_p3492929915253"></a><a name="evs_04_2072_p3492929915253"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2072_p6147315615253"><a name="evs_04_2072_p6147315615253"></a><a name="evs_04_2072_p6147315615253"></a>Specifies the ID of the disk type.</p>
    </td>
    </tr>
    <tr id="evs_04_2072_row29065010162354"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2072_p42044028162413"><a name="evs_04_2072_p42044028162413"></a><a name="evs_04_2072_p42044028162413"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2072_p50123125162413"><a name="evs_04_2072_p50123125162413"></a><a name="evs_04_2072_p50123125162413"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2072_p24390255162413"><a name="evs_04_2072_p24390255162413"></a><a name="evs_04_2072_p24390255162413"></a>Specifies the description of the disk type.</p>
    </td>
    </tr>
    <tr id="evs_04_2072_row18405511162410"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2072_p63756107162413"><a name="evs_04_2072_p63756107162413"></a><a name="evs_04_2072_p63756107162413"></a>qos_specs_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2072_p63971081162413"><a name="evs_04_2072_p63971081162413"></a><a name="evs_04_2072_p63971081162413"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2072_p15431098162413"><a name="evs_04_2072_p15431098162413"></a><a name="evs_04_2072_p15431098162413"></a><span id="evs_04_2072_text381293214497"><a name="evs_04_2072_text381293214497"></a><a name="evs_04_2072_text381293214497"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="evs_04_2072_row4485204316243"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2072_p42090474162413"><a name="evs_04_2072_p42090474162413"></a><a name="evs_04_2072_p42090474162413"></a>is_public</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2072_p53885223162413"><a name="evs_04_2072_p53885223162413"></a><a name="evs_04_2072_p53885223162413"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2072_p11454306162413"><a name="evs_04_2072_p11454306162413"></a><a name="evs_04_2072_p11454306162413"></a><span id="evs_04_2072_text3111131184916"><a name="evs_04_2072_text3111131184916"></a><a name="evs_04_2072_text3111131184916"></a>Reserved field</span></p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2072_li1957456185414"></a>Parameters in the  **extra\_specs**  field

    <a name="evs_04_2072_evs_04_2071_table1763545695210"></a>
    <table><thead align="left"><tr id="evs_04_2072_evs_04_2071_row16361656165213"><th class="cellrowborder" valign="top" width="21.45%" id="mcps1.1.4.1.1"><p id="evs_04_2072_evs_04_2071_p1763619566527"><a name="evs_04_2072_evs_04_2071_p1763619566527"></a><a name="evs_04_2072_evs_04_2071_p1763619566527"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.41%" id="mcps1.1.4.1.2"><p id="evs_04_2072_evs_04_2071_p18636105619529"><a name="evs_04_2072_evs_04_2071_p18636105619529"></a><a name="evs_04_2072_evs_04_2071_p18636105619529"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="evs_04_2072_evs_04_2071_p186361556155214"><a name="evs_04_2072_evs_04_2071_p186361556155214"></a><a name="evs_04_2072_evs_04_2071_p186361556155214"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2072_evs_04_2071_row56365565526"><td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.1.4.1.1 "><p id="evs_04_2072_evs_04_2071_p063625610529"><a name="evs_04_2072_evs_04_2071_p063625610529"></a><a name="evs_04_2072_evs_04_2071_p063625610529"></a>volume_backend_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.41%" headers="mcps1.1.4.1.2 "><p id="evs_04_2072_evs_04_2071_p3636165635219"><a name="evs_04_2072_evs_04_2071_p3636165635219"></a><a name="evs_04_2072_evs_04_2071_p3636165635219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2072_evs_04_2071_p17636185614527"><a name="evs_04_2072_evs_04_2071_p17636185614527"></a><a name="evs_04_2072_evs_04_2071_p17636185614527"></a><span id="evs_04_2072_evs_04_2071_text205233101097"><a name="evs_04_2072_evs_04_2071_text205233101097"></a><a name="evs_04_2072_evs_04_2071_text205233101097"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="evs_04_2072_evs_04_2071_row156362568523"><td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.1.4.1.1 "><p id="evs_04_2072_evs_04_2071_p863675695214"><a name="evs_04_2072_evs_04_2071_p863675695214"></a><a name="evs_04_2072_evs_04_2071_p863675695214"></a>availability-zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.41%" headers="mcps1.1.4.1.2 "><p id="evs_04_2072_evs_04_2071_p8636175665214"><a name="evs_04_2072_evs_04_2071_p8636175665214"></a><a name="evs_04_2072_evs_04_2071_p8636175665214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2072_evs_04_2071_p18636356185213"><a name="evs_04_2072_evs_04_2071_p18636356185213"></a><a name="evs_04_2072_evs_04_2071_p18636356185213"></a><span id="evs_04_2072_evs_04_2071_text533914121390"><a name="evs_04_2072_evs_04_2071_text533914121390"></a><a name="evs_04_2072_evs_04_2071_text533914121390"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="evs_04_2072_evs_04_2071_row17844276596"><td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.1.4.1.1 "><p id="evs_04_2072_evs_04_2071_p178418274593"><a name="evs_04_2072_evs_04_2071_p178418274593"></a><a name="evs_04_2072_evs_04_2071_p178418274593"></a>HW:availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.41%" headers="mcps1.1.4.1.2 "><p id="evs_04_2072_evs_04_2071_p168416276599"><a name="evs_04_2072_evs_04_2071_p168416276599"></a><a name="evs_04_2072_evs_04_2071_p168416276599"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2072_evs_04_2071_p1540410211408"><a name="evs_04_2072_evs_04_2071_p1540410211408"></a><a name="evs_04_2072_evs_04_2071_p1540410211408"></a><span id="evs_04_2072_evs_04_2071_evs_04_2071_text533914121390"><a name="evs_04_2072_evs_04_2071_evs_04_2071_text533914121390"></a><a name="evs_04_2072_evs_04_2071_evs_04_2071_text533914121390"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="evs_04_2072_evs_04_2071_row3637135611527"><td class="cellrowborder" valign="top" width="21.45%" headers="mcps1.1.4.1.1 "><p id="evs_04_2072_evs_04_2071_p163710561529"><a name="evs_04_2072_evs_04_2071_p163710561529"></a><a name="evs_04_2072_evs_04_2071_p163710561529"></a>RESKEY:availability_zones</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.41%" headers="mcps1.1.4.1.2 "><p id="evs_04_2072_evs_04_2071_p166374562525"><a name="evs_04_2072_evs_04_2071_p166374562525"></a><a name="evs_04_2072_evs_04_2071_p166374562525"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2072_evs_04_2071_p3637756205214"><a name="evs_04_2072_evs_04_2071_p3637756205214"></a><a name="evs_04_2072_evs_04_2071_p3637756205214"></a>Specifies the AZs that support the current disk type.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2072_li0419202382514"></a>Parameters in the  **error**  field

    <a name="evs_04_2072_evs_04_2013_table15441099103019"></a>
    <table><thead align="left"><tr id="evs_04_2072_evs_04_2013_row54094047103019"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="evs_04_2072_evs_04_2013_p19541716103019"><a name="evs_04_2072_evs_04_2013_p19541716103019"></a><a name="evs_04_2072_evs_04_2013_p19541716103019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="evs_04_2072_evs_04_2013_p39375186103019"><a name="evs_04_2072_evs_04_2013_p39375186103019"></a><a name="evs_04_2072_evs_04_2013_p39375186103019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2072_evs_04_2013_p38578950103019"><a name="evs_04_2072_evs_04_2013_p38578950103019"></a><a name="evs_04_2072_evs_04_2013_p38578950103019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2072_evs_04_2013_row59401790103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2072_evs_04_2013_p46815658103019"><a name="evs_04_2072_evs_04_2013_p46815658103019"></a><a name="evs_04_2072_evs_04_2013_p46815658103019"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2072_evs_04_2013_p33971979103019"><a name="evs_04_2072_evs_04_2013_p33971979103019"></a><a name="evs_04_2072_evs_04_2013_p33971979103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2072_evs_04_2013_p21623243103019"><a name="evs_04_2072_evs_04_2013_p21623243103019"></a><a name="evs_04_2072_evs_04_2013_p21623243103019"></a>Specifies the error message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="evs_04_2072_evs_04_2013_row60391466103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2072_evs_04_2013_p59870541103019"><a name="evs_04_2072_evs_04_2013_p59870541103019"></a><a name="evs_04_2072_evs_04_2013_p59870541103019"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2072_evs_04_2013_p17675690103019"><a name="evs_04_2072_evs_04_2013_p17675690103019"></a><a name="evs_04_2072_evs_04_2013_p17675690103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2072_evs_04_2013_p6087468103019"><a name="evs_04_2072_evs_04_2013_p6087468103019"></a><a name="evs_04_2072_evs_04_2013_p6087468103019"></a>Specifies the error code returned when an error occurs.</p>
    <p id="evs_04_2072_evs_04_2013_p54787218103019"><a name="evs_04_2072_evs_04_2013_p54787218103019"></a><a name="evs_04_2072_evs_04_2013_p54787218103019"></a>For details about the error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "volume_type": {
            "extra_specs": {
                "volume_backend_name": "SATA", 
                "availability-zone": "az-dc-1"
            }, 
            "name": "SATA", 
            "qos_specs_id": null, 
            "is_public": true, 
            "id": "ea6e3c13-aac5-46e0-b280-745ed272e662", 
            "description": null
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


## Status Codes<a name="section32217513"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

