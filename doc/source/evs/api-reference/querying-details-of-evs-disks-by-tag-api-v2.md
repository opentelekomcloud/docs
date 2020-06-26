# Querying Details of EVS Disks by Tag<a name="evs_04_2034"></a>

## Function<a name="section5299350116935"></a>

This API is used to query the details of EVS disks by tag.

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
    <table><thead align="left"><tr id="row13155682162337"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.5.1.1"><p id="p58977321162337"><a name="p58977321162337"></a><a name="p58977321162337"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.2"><p id="p12433688162337"><a name="p12433688162337"></a><a name="p12433688162337"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.11%" id="mcps1.1.5.1.3"><p id="p495832162337"><a name="p495832162337"></a><a name="p495832162337"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.89%" id="mcps1.1.5.1.4"><p id="p40162449162337"><a name="p40162449162337"></a><a name="p40162449162337"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row31932906162337"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p36428555162337"><a name="p36428555162337"></a><a name="p36428555162337"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.2 "><p id="p65031837162337"><a name="p65031837162337"></a><a name="p65031837162337"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.11%" headers="mcps1.1.5.1.3 "><p id="p33087431162337"><a name="p33087431162337"></a><a name="p33087431162337"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.89%" headers="mcps1.1.5.1.4 "><p id="p62836274162337"><a name="p62836274162337"></a><a name="p62836274162337"></a>Specifies the key-value pairs of the tag. For details, see <a href="#li8528152083214">Parameters in the tags field</a>.</p>
    <p id="p1858507716"><a name="p1858507716"></a><a name="p1858507716"></a>One tag list can contain a maximum of 10 keys.</p>
    <p id="p175842500716"><a name="p175842500716"></a><a name="p175842500716"></a>Tag keys in a tag list must be unique.</p>
    <p id="p14391151142511"><a name="p14391151142511"></a><a name="p14391151142511"></a>When multiple keys are specified in a tag list, only the disks having all specified keys are queried.</p>
    <div class="note" id="note1461127173813"><a name="note1461127173813"></a><a name="note1461127173813"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2032_p1970754173519"><a name="evs_04_2032_p1970754173519"></a><a name="evs_04_2032_p1970754173519"></a>If multiple tag lists are specified in the request, only the disks that meet the requirements of the last tag list are queried.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row862173882314"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p1487452192311"><a name="p1487452192311"></a><a name="p1487452192311"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.2 "><p id="p08795219233"><a name="p08795219233"></a><a name="p08795219233"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.11%" headers="mcps1.1.5.1.3 "><p id="p47340819249"><a name="p47340819249"></a><a name="p47340819249"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.89%" headers="mcps1.1.5.1.4 "><p id="p987115282319"><a name="p987115282319"></a><a name="p987115282319"></a>Specifies the number of query records.</p>
    <p id="p118795218237"><a name="p118795218237"></a><a name="p118795218237"></a><span id="text138349551887"><a name="text138349551887"></a><a name="text138349551887"></a>The value ranges from 1 to 1000, and the default value is 1000. The returned value cannot exceed this limit.</span></p>
    </td>
    </tr>
    <tr id="row94258428238"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p3871352132317"><a name="p3871352132317"></a><a name="p3871352132317"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.2 "><p id="p38720529235"><a name="p38720529235"></a><a name="p38720529235"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.11%" headers="mcps1.1.5.1.3 "><p id="p17737483247"><a name="p17737483247"></a><a name="p17737483247"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.89%" headers="mcps1.1.5.1.4 "><p id="p68718528233"><a name="p68718528233"></a><a name="p68718528233"></a>Specifies the index location.</p>
    <p id="p787185218237"><a name="p787185218237"></a><a name="p787185218237"></a>The minimum value is <strong id="b18744142621611"><a name="b18744142621611"></a><a name="b18744142621611"></a>0</strong>, which is also the default value.</p>
    <p id="p387145252319"><a name="p387145252319"></a><a name="p387145252319"></a>The first record in the query result is the offset+1 record that meets the query criteria.</p>
    </td>
    </tr>
    <tr id="row6793144415239"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p1687152172313"><a name="p1687152172313"></a><a name="p1687152172313"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.2 "><p id="p1187552192314"><a name="p1187552192314"></a><a name="p1187552192314"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.11%" headers="mcps1.1.5.1.3 "><p id="p97390817249"><a name="p97390817249"></a><a name="p97390817249"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.89%" headers="mcps1.1.5.1.4 "><p id="p987652192316"><a name="p987652192316"></a><a name="p987652192316"></a>Specifies the operation identifier.</p>
    <p id="p118795202312"><a name="p118795202312"></a><a name="p118795202312"></a>Specifying <strong id="b130008727820429"><a name="b130008727820429"></a><a name="b130008727820429"></a>filter</strong> queries the details of disks by tag.</p>
    </td>
    </tr>
    <tr id="row8888748016"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p159133101403"><a name="p159133101403"></a><a name="p159133101403"></a>matches</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.2 "><p id="p1623519196018"><a name="p1623519196018"></a><a name="p1623519196018"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.11%" headers="mcps1.1.5.1.3 "><p id="p109131110706"><a name="p109131110706"></a><a name="p109131110706"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.89%" headers="mcps1.1.5.1.4 "><p id="p129139109019"><a name="p129139109019"></a><a name="p129139109019"></a>Specifies the query criteria that the resource supports. For details, see <a href="#li15751146383">Parameters in the matches field</a>.</p>
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
    <th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.1.5.1.3"><p id="p8530122014321"><a name="p8530122014321"></a><a name="p8530122014321"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.629999999999995%" id="mcps1.1.5.1.4"><p id="p18533172017325"><a name="p18533172017325"></a><a name="p18533172017325"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row253510208321"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p17535320203220"><a name="p17535320203220"></a><a name="p17535320203220"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.2 "><p id="p175351020123212"><a name="p175351020123212"></a><a name="p175351020123212"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p953522010321"><a name="p953522010321"></a><a name="p953522010321"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.629999999999995%" headers="mcps1.1.5.1.4 "><p id="p1520310020114"><a name="p1520310020114"></a><a name="p1520310020114"></a>Specifies the tag key.</p>
    </td>
    </tr>
    <tr id="row853810204325"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p1053816201325"><a name="p1053816201325"></a><a name="p1053816201325"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.2 "><p id="p13538520153211"><a name="p13538520153211"></a><a name="p13538520153211"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p1538920193219"><a name="p1538920193219"></a><a name="p1538920193219"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.629999999999995%" headers="mcps1.1.5.1.4 "><p id="p945418465250"><a name="p945418465250"></a><a name="p945418465250"></a>Specifies the tag value.</p>
    <a name="ul133722079613"></a><a name="ul133722079613"></a><ul id="ul133722079613"><li>One value list can contain a maximum of 10 values.</li><li>Tag values in a value list must be unique.</li><li>If the value list is left empty, any tag value can be matched. When multiple values are specified in a value list and the key requirements are met, disks that have any of the specified values are queried.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li15751146383"></a>Parameters in the  **matches**  field

    <a name="table0778462086"></a>
    <table><thead align="left"><tr id="row38414461289"><th class="cellrowborder" valign="top" width="16%" id="mcps1.1.5.1.1"><p id="p1487946584"><a name="p1487946584"></a><a name="p1487946584"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.1.5.1.2"><p id="p119224615820"><a name="p119224615820"></a><a name="p119224615820"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.1.5.1.3"><p id="p194174619818"><a name="p194174619818"></a><a name="p194174619818"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="41%" id="mcps1.1.5.1.4"><p id="p109604613817"><a name="p109604613817"></a><a name="p109604613817"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14989461387"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.1 "><p id="p810194617814"><a name="p810194617814"></a><a name="p810194617814"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.5.1.2 "><p id="p17102646681"><a name="p17102646681"></a><a name="p17102646681"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.3 "><p id="p131037466813"><a name="p131037466813"></a><a name="p131037466813"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.5.1.4 "><p id="p12710163971119"><a name="p12710163971119"></a><a name="p12710163971119"></a>Specifies the tag key. The value is of the enumerated type.</p>
    <p id="p1110654618817"><a name="p1110654618817"></a><a name="p1110654618817"></a>The value can be as follows:</p>
    <a name="ul168395111111"></a><a name="ul168395111111"></a><ul id="ul168395111111"><li><strong id="b842352706202849"><a name="b842352706202849"></a><a name="b842352706202849"></a>resource_name</strong>: disk name.</li><li><strong id="b842352706183338"><a name="b842352706183338"></a><a name="b842352706183338"></a>service_type</strong>: service type.</li></ul>
    </td>
    </tr>
    <tr id="row81181246181"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.1 "><p id="p111201646386"><a name="p111201646386"></a><a name="p111201646386"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.5.1.2 "><p id="p7121346287"><a name="p7121346287"></a><a name="p7121346287"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.5.1.3 "><p id="p1122164618815"><a name="p1122164618815"></a><a name="p1122164618815"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.5.1.4 "><p id="p91249461180"><a name="p91249461180"></a><a name="p91249461180"></a>Specifies the tag value.</p>
    <a name="ul1956812345128"></a><a name="ul1956812345128"></a><ul id="ul1956812345128"><li>It can contain up to 255 characters.</li><li>If <strong id="b84235270621231"><a name="b84235270621231"></a><a name="b84235270621231"></a>resource_name</strong> is specified for <strong id="b84235270621234"><a name="b84235270621234"></a><a name="b84235270621234"></a>key</strong>, the tag value uses a fuzzy match.</li><li>If <strong id="b148953074121824"><a name="b148953074121824"></a><a name="b148953074121824"></a>service_type</strong> is specified for <strong id="b72635002321824"><a name="b72635002321824"></a><a name="b72635002321824"></a>key</strong>, the value is of the enumerated type. It can be <strong id="b842352706211020"><a name="b842352706211020"></a><a name="b842352706211020"></a>EVS</strong> or <strong id="b842352706211023"><a name="b842352706211023"></a><a name="b842352706211023"></a>DSS</strong> and is case-insensitive.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "offset": "100", 
        "limit": "100", 
        "action": "filter", 
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
    <table><thead align="left"><tr id="row2937460716935"><th class="cellrowborder" valign="top" width="22.37%" id="mcps1.1.4.1.1"><p id="p3053299616935"><a name="p3053299616935"></a><a name="p3053299616935"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.74%" id="mcps1.1.4.1.2"><p id="p5725363416935"><a name="p5725363416935"></a><a name="p5725363416935"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.89%" id="mcps1.1.4.1.3"><p id="p3278200616935"><a name="p3278200616935"></a><a name="p3278200616935"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63271571172633"><td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.1.4.1.1 "><p id="p24723652172633"><a name="p24723652172633"></a><a name="p24723652172633"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.1.4.1.2 "><p id="p56458834172633"><a name="p56458834172633"></a><a name="p56458834172633"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.89%" headers="mcps1.1.4.1.3 "><p id="p52593571172633"><a name="p52593571172633"></a><a name="p52593571172633"></a>Specifies the total number of disks that meet the query criteria.</p>
    </td>
    </tr>
    <tr id="row96879441311"><td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.1.4.1.1 "><p id="p261775003110"><a name="p261775003110"></a><a name="p261775003110"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.1.4.1.2 "><p id="p1361765083118"><a name="p1361765083118"></a><a name="p1361765083118"></a>List&lt;resource&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.89%" headers="mcps1.1.4.1.3 "><p id="p06172508319"><a name="p06172508319"></a><a name="p06172508319"></a>Specifies the resources that meet the query criteria. For details, see <a href="#li95931326163214">Parameters in the resources field</a>.</p>
    </td>
    </tr>
    <tr id="row961262962717"><td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.89%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li95931326163214"></a>Parameters in the  **resources**  field

    <a name="table8575132033210"></a>
    <table><thead align="left"><tr id="row156391220173215"><th class="cellrowborder" valign="top" width="23.380000000000003%" id="mcps1.1.4.1.1"><p id="p1963910206321"><a name="p1963910206321"></a><a name="p1963910206321"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.48%" id="mcps1.1.4.1.2"><p id="p18639920103214"><a name="p18639920103214"></a><a name="p18639920103214"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p176391320153219"><a name="p176391320153219"></a><a name="p176391320153219"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row106392209321"><td class="cellrowborder" valign="top" width="23.380000000000003%" headers="mcps1.1.4.1.1 "><p id="p6639920143219"><a name="p6639920143219"></a><a name="p6639920143219"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.48%" headers="mcps1.1.4.1.2 "><p id="p1864042093215"><a name="p1864042093215"></a><a name="p1864042093215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p17640112015324"><a name="p17640112015324"></a><a name="p17640112015324"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="row964062083211"><td class="cellrowborder" valign="top" width="23.380000000000003%" headers="mcps1.1.4.1.1 "><p id="p2640152023219"><a name="p2640152023219"></a><a name="p2640152023219"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.48%" headers="mcps1.1.4.1.2 "><p id="p3640720123212"><a name="p3640720123212"></a><a name="p3640720123212"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p1964019207321"><a name="p1964019207321"></a><a name="p1964019207321"></a>Specifies the disk name.</p>
    </td>
    </tr>
    <tr id="row116403209327"><td class="cellrowborder" valign="top" width="23.380000000000003%" headers="mcps1.1.4.1.1 "><p id="p1664015207321"><a name="p1664015207321"></a><a name="p1664015207321"></a>resource_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.48%" headers="mcps1.1.4.1.2 "><p id="p11640192033218"><a name="p11640192033218"></a><a name="p11640192033218"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p1640520123214"><a name="p1640520123214"></a><a name="p1640520123214"></a>Specifies the resource details.</p>
    </td>
    </tr>
    <tr id="row56401020193215"><td class="cellrowborder" valign="top" width="23.380000000000003%" headers="mcps1.1.4.1.1 "><p id="p1964012013217"><a name="p1964012013217"></a><a name="p1964012013217"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.48%" headers="mcps1.1.4.1.2 "><p id="p19640142093213"><a name="p19640142093213"></a><a name="p19640142093213"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p1640120143218"><a name="p1640120143218"></a><a name="p1640120143218"></a>Specifies the tag list. For details, see <a href="#li3876131217349">Parameters in the tags field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li3876131217349"></a>Parameters in the  **tags**  field

    <a name="table198791012123412"></a>
    <table><thead align="left"><tr id="row8889141218341"><th class="cellrowborder" valign="top" width="23.380000000000003%" id="mcps1.1.4.1.1"><p id="p68931812203414"><a name="p68931812203414"></a><a name="p68931812203414"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.78%" id="mcps1.1.4.1.2"><p id="p2089701233414"><a name="p2089701233414"></a><a name="p2089701233414"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.84%" id="mcps1.1.4.1.3"><p id="p390341263413"><a name="p390341263413"></a><a name="p390341263413"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14906111253419"><td class="cellrowborder" valign="top" width="23.380000000000003%" headers="mcps1.1.4.1.1 "><p id="p3909112163416"><a name="p3909112163416"></a><a name="p3909112163416"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.1.4.1.2 "><p id="p1912161283417"><a name="p1912161283417"></a><a name="p1912161283417"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.84%" headers="mcps1.1.4.1.3 "><p id="p2866151481"><a name="p2866151481"></a><a name="p2866151481"></a>Specifies the tag key.</p>
    </td>
    </tr>
    <tr id="row39391412103418"><td class="cellrowborder" valign="top" width="23.380000000000003%" headers="mcps1.1.4.1.1 "><p id="p179412125347"><a name="p179412125347"></a><a name="p179412125347"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.78%" headers="mcps1.1.4.1.2 "><p id="p159431312163417"><a name="p159431312163417"></a><a name="p159431312163417"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.84%" headers="mcps1.1.4.1.3 "><p id="p92449569473"><a name="p92449569473"></a><a name="p92449569473"></a>Specifies the tag value.</p>
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
    	"total_count": 1,
    	"resources": [{
    		"resource_name": "resource1",
    		"resource_detail": {
    			"attachments": [{
    				"server_id": "2080869e-ba46-4ea5-b45e-3191ac0f1d54",
    				"attachment_id": "1335f039-7a42-4d1e-be49-ac584db0ba0b",
    				"attached_at": "2019-08-06T07:00:21.842812",
    				"host_name": null,
    				"volume_id": "7fa6b592-ac75-460d-a28a-bb17429d1eb2",
    				"device": "/dev/vda",
    				"id": "7fa6b592-ac75-460d-a28a-bb17429d1eb2"
    			}],
    			"links": [{
    				"href": "https://volume.Region.dc1.domainname.com/v2/051375756c80d5eb2ff0c014498645fb/volumes/7fa6b592-ac75-460d-a28a-bb17429d1eb2",
    				"rel": "self"
    			},
    			{
    				"href": "https://volume.Region.dc1.domainname.com/051375756c80d5eb2ff0c014498645fb/volumes/7fa6b592-ac75-460d-a28a-bb17429d1eb2",
    				"rel": "bookmark"
    			}],
    			"availability_zone": "kvmxen.dc1",
    			"os-vol-host-attr:host": "az21.dc1#2",
    			"encrypted": false,
    			"dedicated_storage_id": null,
    			"enterprise_project_id": "0",
    			"updated_at": "2019-08-09T06:19:35.874737",
    			"os-volume-replication:extended_status": null,
    			"replication_status": "disabled",
    			"snapshot_id": null,
    			"id": "7fa6b592-ac75-460d-a28a-bb17429d1eb2",
    			"size": 40,
    			"user_id": "75f26e17348643bfb7718578b04635c2",
    			"os-vol-tenant-attr:tenant_id": "051375756c80d5eb2ff0c014498645fb",
    			"service_type": "EVS",
    			"os-vol-mig-status-attr:migstat": null,
    			"metadata": {
    				
    			},
    			"status": "in-use",
    			"volume_image_metadata": {
    				"size": "0",
    				"__quick_start": "False",
    				"container_format": "bare",
    				"min_ram": "0",
    				"image_name": "test-hua-centos7.3-0725",
    				"image_id": "c6c153a6-dde8-4bac-8e40-3d7619436934",
    				"__os_type": "Linux",
    				"min_disk": "20",
    				"__support_kvm": "true",
    				"virtual_env_type": "FusionCompute",
    				"__description": "",
    				"__os_version": "CentOS 7.3 64bit",
    				"__os_bit": "64",
    				"__image_source_type": "uds",
    				"__support_xen": "true",
    				"file_format": "zvhd2",
    				"checksum": "d41d8cd98f00b204e9800998ecf8427e",
    				"__imagetype": "gold",
    				"disk_format": "zvhd2",
    				"__image_cache_type": "Not_Cache",
    				"__isregistered": "true",
    				"__image_location": "192.168.46.200:5443:pcsimsregion:c6c153a6-dde8-4bac-8e40-3d7619436934",
    				"__image_size": "911269888",
    				"__platform": "CentOS"
    			},
    			"description": "",
    			"multiattach": false,
    			"source_volid": null,
    			"consistencygroup_id": null,
    			"os-vol-mig-status-attr:name_id": null,
    			"name": "resource1",
    			"bootable": "true",
    			"created_at": "2019-08-06T06:59:03.056682",
    			"volume_type": "SAS",
    			"shareable": false,
    			"dedicated_storage_name": null
    		},
    		"tags": [{
    			"key": "key1",
    			"value": "value1"
    		},
    		{
    			"key": "key1",
    			"value": "value2"
    		}],
    		"resource_id": "7fa6b592-ac75-460d-a28a-bb17429d1eb2"
    	}]
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

