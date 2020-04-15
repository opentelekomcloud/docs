# Querying the Number of EVS Disks by Tag<a name="evs_04_2032"></a>

## Function<a name="section5299350116935"></a>

This API is used to query the number of EVS disks by tag.

## Constraints<a name="section4466609116935"></a>

None

## URI<a name="section1378135716935"></a>

-   URI format

    POST /v2/\{project\_id\}/os-vendor-volumes/resource\_instances/action

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
    </tbody>
    </table>


## Request<a name="section33444519162337"></a>

-   Parameter description

    <a name="table50618906162337"></a>
    <table><thead align="left"><tr id="row13155682162337"><th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.1.5.1.1"><p id="p58977321162337"><a name="p58977321162337"></a><a name="p58977321162337"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.15%" id="mcps1.1.5.1.2"><p id="p12433688162337"><a name="p12433688162337"></a><a name="p12433688162337"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.71%" id="mcps1.1.5.1.3"><p id="p495832162337"><a name="p495832162337"></a><a name="p495832162337"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.97%" id="mcps1.1.5.1.4"><p id="p40162449162337"><a name="p40162449162337"></a><a name="p40162449162337"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row31932906162337"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p36428555162337"><a name="p36428555162337"></a><a name="p36428555162337"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p65031837162337"><a name="p65031837162337"></a><a name="p65031837162337"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.71%" headers="mcps1.1.5.1.3 "><p id="p33087431162337"><a name="p33087431162337"></a><a name="p33087431162337"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.97%" headers="mcps1.1.5.1.4 "><p id="p62836274162337"><a name="p62836274162337"></a><a name="p62836274162337"></a>Specifies the key-value pairs of the tag. For details, see <a href="#li8528152083214">Parameters in the tags field</a>.</p>
    <p id="p19962184814712"><a name="p19962184814712"></a><a name="p19962184814712"></a>The <strong id="b842352706195728"><a name="b842352706195728"></a><a name="b842352706195728"></a>tags</strong> field cannot be left empty.</p>
    <p id="p1858507716"><a name="p1858507716"></a><a name="p1858507716"></a>One tag list can contain a maximum of 10 keys.</p>
    <p id="p175842500716"><a name="p175842500716"></a><a name="p175842500716"></a>Tag keys in a tag list must be unique.</p>
    <p id="p485184792415"><a name="p485184792415"></a><a name="p485184792415"></a>When multiple keys are specified in a tag list, only the disks having all specified keys are queried.</p>
    <div class="note" id="note1570710453511"><a name="note1570710453511"></a><a name="note1570710453511"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1970754173519"><a name="p1970754173519"></a><a name="p1970754173519"></a>If multiple tag lists are specified in the request, only the disks that meet the requirements of the last tag list are queried.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row142661428014"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p2091381011019"><a name="p2091381011019"></a><a name="p2091381011019"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p123011191302"><a name="p123011191302"></a><a name="p123011191302"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.71%" headers="mcps1.1.5.1.3 "><p id="p1191320101905"><a name="p1191320101905"></a><a name="p1191320101905"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.97%" headers="mcps1.1.5.1.4 "><p id="p59131110807"><a name="p59131110807"></a><a name="p59131110807"></a>Specifies the operation identifier.</p>
    <p id="p10913191020016"><a name="p10913191020016"></a><a name="p10913191020016"></a>Specifying <strong id="b130008727820429"><a name="b130008727820429"></a><a name="b130008727820429"></a>count</strong> queries the number of disks by tag.</p>
    </td>
    </tr>
    <tr id="row8888748016"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p159133101403"><a name="p159133101403"></a><a name="p159133101403"></a>matches</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p1623519196018"><a name="p1623519196018"></a><a name="p1623519196018"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.71%" headers="mcps1.1.5.1.3 "><p id="p109131110706"><a name="p109131110706"></a><a name="p109131110706"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.97%" headers="mcps1.1.5.1.4 "><p id="p129139109019"><a name="p129139109019"></a><a name="p129139109019"></a>Specifies the query criteria that the resource supports. For details, see <a href="#li15751146383">Parameters in the matches field</a>.</p>
    <p id="p47601518719"><a name="p47601518719"></a><a name="p47601518719"></a>The <strong id="b84235270620140"><a name="b84235270620140"></a><a name="b84235270620140"></a>matches</strong> field cannot be left empty.</p>
    <p id="p1547919526720"><a name="p1547919526720"></a><a name="p1547919526720"></a>Tag keys in the list must be unique.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li8528152083214"></a>Parameters in the  **tags**  field

    <a name="table205290203323"></a>
    <table><thead align="left"><tr id="row13530142033210"><th class="cellrowborder" valign="top" width="15.409999999999998%" id="mcps1.1.5.1.1"><p id="p19530182011329"><a name="p19530182011329"></a><a name="p19530182011329"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.040000000000001%" id="mcps1.1.5.1.2"><p id="p20530120163211"><a name="p20530120163211"></a><a name="p20530120163211"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.72%" id="mcps1.1.5.1.3"><p id="p8530122014321"><a name="p8530122014321"></a><a name="p8530122014321"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.83%" id="mcps1.1.5.1.4"><p id="p18533172017325"><a name="p18533172017325"></a><a name="p18533172017325"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row253510208321"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p17535320203220"><a name="p17535320203220"></a><a name="p17535320203220"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.2 "><p id="p175351020123212"><a name="p175351020123212"></a><a name="p175351020123212"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.72%" headers="mcps1.1.5.1.3 "><p id="p953522010321"><a name="p953522010321"></a><a name="p953522010321"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.83%" headers="mcps1.1.5.1.4 "><div class="p" id="p95031611113614"><a name="p95031611113614"></a><a name="p95031611113614"></a>Specifies the tag key.<a name="evs_04_2027_ul20512635161710"></a><a name="evs_04_2027_ul20512635161710"></a><ul id="evs_04_2027_ul20512635161710"><li>Cannot be left blank.</li><li>Must be unique for each resource.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only digits, letters, hyphens (-), and underscores (_).</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row853810204325"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p1053816201325"><a name="p1053816201325"></a><a name="p1053816201325"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.2 "><p id="p74479101218"><a name="p74479101218"></a><a name="p74479101218"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.72%" headers="mcps1.1.5.1.3 "><p id="p1538920193219"><a name="p1538920193219"></a><a name="p1538920193219"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.83%" headers="mcps1.1.5.1.4 "><div class="p" id="p14911418386"><a name="p14911418386"></a><a name="p14911418386"></a>Specifies the tag value.<a name="evs_04_2027_ul4512173118234"></a><a name="evs_04_2027_ul4512173118234"></a><ul id="evs_04_2027_ul4512173118234"><li>Can contain a maximum of 43 characters.</li><li>Can contain only digits, letters, hyphens (-), and underscores (_).</li></ul>
    </div>
    <p id="p1227514181481"><a name="p1227514181481"></a><a name="p1227514181481"></a>One value list can contain a maximum of 10 values.</p>
    <p id="p1227515189810"><a name="p1227515189810"></a><a name="p1227515189810"></a>Tag values in a value list must be unique.</p>
    <p id="p527561814813"><a name="p527561814813"></a><a name="p527561814813"></a>If the value list is left empty, any tag value can be matched.</p>
    <p id="p1242618182519"><a name="p1242618182519"></a><a name="p1242618182519"></a>When multiple values are specified in a value list and the key requirements are met, disks that have any of the specified values are queried.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li15751146383"></a>Parameters in the  **matches**  field

    <a name="table0778462086"></a>
    <table><thead align="left"><tr id="row38414461289"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.5.1.1"><p id="p1487946584"><a name="p1487946584"></a><a name="p1487946584"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.1.5.1.2"><p id="p119224615820"><a name="p119224615820"></a><a name="p119224615820"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.1.5.1.3"><p id="p194174619818"><a name="p194174619818"></a><a name="p194174619818"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="41%" id="mcps1.1.5.1.4"><p id="p109604613817"><a name="p109604613817"></a><a name="p109604613817"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14989461387"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p810194617814"><a name="p810194617814"></a><a name="p810194617814"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.2 "><p id="p17102646681"><a name="p17102646681"></a><a name="p17102646681"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.3 "><p id="p131037466813"><a name="p131037466813"></a><a name="p131037466813"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.5.1.4 "><p id="p12710163971119"><a name="p12710163971119"></a><a name="p12710163971119"></a>Specifies the tag key. The value is of the enumerated type.</p>
    <p id="p1110654618817"><a name="p1110654618817"></a><a name="p1110654618817"></a>The value can be as follows:</p>
    <a name="ul168395111111"></a><a name="ul168395111111"></a><ul id="ul168395111111"><li><strong id="b842352706202849"><a name="b842352706202849"></a><a name="b842352706202849"></a>resource_name</strong>: disk name.</li><li><strong id="b842352706183338"><a name="b842352706183338"></a><a name="b842352706183338"></a>service_type</strong>: service type.</li></ul>
    </td>
    </tr>
    <tr id="row81181246181"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p111201646386"><a name="p111201646386"></a><a name="p111201646386"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.2 "><p id="p7121346287"><a name="p7121346287"></a><a name="p7121346287"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.3 "><p id="p1122164618815"><a name="p1122164618815"></a><a name="p1122164618815"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.5.1.4 "><p id="p91249461180"><a name="p91249461180"></a><a name="p91249461180"></a>Specifies the tag value.</p>
    <a name="ul1956812345128"></a><a name="ul1956812345128"></a><ul id="ul1956812345128"><li>It can contain up to 255 Unicode characters.</li><li>An empty string specifies an exact match, and a non-empty string specifies a fuzzy query.</li><li>If <strong id="b84235270621716"><a name="b84235270621716"></a><a name="b84235270621716"></a>resource_name</strong> is specified for <strong id="b84235270621725"><a name="b84235270621725"></a><a name="b84235270621725"></a>key</strong>, spaces before and after the tag value will be discarded.</li><li>If <strong id="b148953074121824"><a name="b148953074121824"></a><a name="b148953074121824"></a>service_type</strong> is specified for <strong id="b72635002321824"><a name="b72635002321824"></a><a name="b72635002321824"></a>key</strong>, the value is of the enumerated type. It can be <strong id="b842352706211020"><a name="b842352706211020"></a><a name="b842352706211020"></a>EVS</strong> or <strong id="b842352706211023"><a name="b842352706211023"></a><a name="b842352706211023"></a>DSS</strong> and is case-insensitive.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "action": "count", 
        "tags": [
            {
                "key": "key1", 
                "values": [
                    "value1", 
                    "value2"
                ]
            }
        ], 
        "matches": [
            {
                "key": "resource_name", 
                "value": "resource1"
            }, 
            {
                "key": "service_type", 
                "value": "EVS"
            }
        ]
    }
    ```


## Response<a name="section3215934016935"></a>

-   Parameter description

    <a name="table716338716935"></a>
    <table><thead align="left"><tr id="row2937460716935"><th class="cellrowborder" valign="top" width="19.27807219278072%" id="mcps1.1.4.1.1"><p id="p3053299616935"><a name="p3053299616935"></a><a name="p3053299616935"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.0975902409759%" id="mcps1.1.4.1.2"><p id="p5725363416935"><a name="p5725363416935"></a><a name="p5725363416935"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.624337566243376%" id="mcps1.1.4.1.3"><p id="p3278200616935"><a name="p3278200616935"></a><a name="p3278200616935"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63271571172633"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p24723652172633"><a name="p24723652172633"></a><a name="p24723652172633"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p56458834172633"><a name="p56458834172633"></a><a name="p56458834172633"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p52593571172633"><a name="p52593571172633"></a><a name="p52593571172633"></a>Specifies the total number of disks that meet the query criteria.</p>
    </td>
    </tr>
    <tr id="row1217715882314"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
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
        "total_count": 1000
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
        "computeFault": {
            "message": "The server has either erred or is incapable of performing the requested operation.", 
            "code": 500
        }
    }
    ```


## Status Codes<a name="section6050296116935"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

