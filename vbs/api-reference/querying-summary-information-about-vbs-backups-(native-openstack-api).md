# Querying Summary Information About VBS Backups \(Native OpenStack API\)<a name="EN-US_TOPIC_0020237258"></a>

## Function<a name="section35026424"></a>

This interface is used to query summary information about a VBS backup.

## URI<a name="section46802360"></a>

-   URI format

    GET /v2/\{project\_id\}/backups

-   Parameter description

    <a name="table35088115"></a>
    <table><thead align="left"><tr id="row58612075"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p49957660"><a name="p49957660"></a><a name="p49957660"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p20038698"><a name="p20038698"></a><a name="p20038698"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p12521852"><a name="p12521852"></a><a name="p12521852"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7637115"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p14626574"><a name="p14626574"></a><a name="p14626574"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p43901854"><a name="p43901854"></a><a name="p43901854"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p64170449"><a name="p64170449"></a><a name="p64170449"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **Request filter**  parameter description

    <a name="table25503279151723"></a>
    <table><thead align="left"><tr id="row56230478151723"><th class="cellrowborder" valign="top" width="14.099999999999998%" id="mcps1.1.5.1.1"><p id="p61804813"><a name="p61804813"></a><a name="p61804813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.34%" id="mcps1.1.5.1.2"><p id="p40133923"><a name="p40133923"></a><a name="p40133923"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.350000000000001%" id="mcps1.1.5.1.3"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.209999999999994%" id="mcps1.1.5.1.4"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54096443151723"><td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.1 "><p id="p58374830151723"><a name="p58374830151723"></a><a name="p58374830151723"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p30740762151723"><a name="p30740762151723"></a><a name="p30740762151723"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.1.5.1.3 "><p id="p6973819151723"><a name="p6973819151723"></a><a name="p6973819151723"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.209999999999994%" headers="mcps1.1.5.1.4 "><p id="p28008505151723"><a name="p28008505151723"></a><a name="p28008505151723"></a>Name of the backup to be queried. This parameter is used to query the backups whose names are specified character strings.</p>
    </td>
    </tr>
    <tr id="row58192668151723"><td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.1 "><p id="p36381618154250"><a name="p36381618154250"></a><a name="p36381618154250"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p61229932154250"><a name="p61229932154250"></a><a name="p61229932154250"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.1.5.1.3 "><p id="p60677479154250"><a name="p60677479154250"></a><a name="p60677479154250"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.209999999999994%" headers="mcps1.1.5.1.4 "><p id="p15928779154250"><a name="p15928779154250"></a><a name="p15928779154250"></a>Status of the backup to be queried. This parameter is used to query the backups in a specified state. The value can be <span class="parmvalue" id="parmvalue5675783710132"><a name="parmvalue5675783710132"></a><a name="parmvalue5675783710132"></a><b>available</b></span>, <span class="parmvalue" id="parmvalue4105848910132"><a name="parmvalue4105848910132"></a><a name="parmvalue4105848910132"></a><b>error</b></span>, <span class="parmvalue" id="parmvalue3398208410132"><a name="parmvalue3398208410132"></a><a name="parmvalue3398208410132"></a><b>restoring</b></span>, <span class="parmvalue" id="parmvalue3740330310132"><a name="parmvalue3740330310132"></a><a name="parmvalue3740330310132"></a><b>creating</b></span>, <span class="parmvalue" id="parmvalue108541110132"><a name="parmvalue108541110132"></a><a name="parmvalue108541110132"></a><b>deleting</b></span>, or <span class="parmvalue" id="parmvalue976870610132"><a name="parmvalue976870610132"></a><a name="parmvalue976870610132"></a><b>error_deleting</b></span>.</p>
    </td>
    </tr>
    <tr id="row19937166154259"><td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.1 "><p id="p4297722154259"><a name="p4297722154259"></a><a name="p4297722154259"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p12571227154259"><a name="p12571227154259"></a><a name="p12571227154259"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.1.5.1.3 "><p id="p11636505154259"><a name="p11636505154259"></a><a name="p11636505154259"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.209999999999994%" headers="mcps1.1.5.1.4 "><p id="p25300480154733"><a name="p25300480154733"></a><a name="p25300480154733"></a>Offset of the queried information</p>
    </td>
    </tr>
    <tr id="row333354215434"><td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.1 "><p id="p158151415434"><a name="p158151415434"></a><a name="p158151415434"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p6099381015434"><a name="p6099381015434"></a><a name="p6099381015434"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.1.5.1.3 "><p id="p4155159115434"><a name="p4155159115434"></a><a name="p4155159115434"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.209999999999994%" headers="mcps1.1.5.1.4 "><p id="p1023569615434"><a name="p1023569615434"></a><a name="p1023569615434"></a>Maximum number of query results that can be returned</p>
    </td>
    </tr>
    <tr id="row49950634163651"><td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.1.5.1.1 "><p id="p19469525163651"><a name="p19469525163651"></a><a name="p19469525163651"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.34%" headers="mcps1.1.5.1.2 "><p id="p33527697163651"><a name="p33527697163651"></a><a name="p33527697163651"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.1.5.1.3 "><p id="p31388933163651"><a name="p31388933163651"></a><a name="p31388933163651"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.209999999999994%" headers="mcps1.1.5.1.4 "><p id="p59475674163651"><a name="p59475674163651"></a><a name="p59475674163651"></a>Disk ID of the backup to be queried. It is used to query the backups for specific disks.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    GET /v2/{project_id}/backups?name=backup&status=error&limit=10&volume_id=7d7c6fbe-d7ee-4b4d-8bae-bdd08b5604bb
    ```


## Request<a name="section18568063"></a>

None

## Response<a name="section32894845"></a>

-   Parameter description

    <a name="table2951652020261"></a>
    <table><thead align="left"><tr id="row6209868220261"><th class="cellrowborder" valign="top" width="27.54275427542754%" id="mcps1.1.4.1.1"><p id="p206186512105"><a name="p206186512105"></a><a name="p206186512105"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.73287328732873%" id="mcps1.1.4.1.2"><p id="p663325112108"><a name="p663325112108"></a><a name="p663325112108"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.724372437243716%" id="mcps1.1.4.1.3"><p id="p463311513104"><a name="p463311513104"></a><a name="p463311513104"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row501535191759"><td class="cellrowborder" valign="top" width="27.54275427542754%" headers="mcps1.1.4.1.1 "><p id="p359032151759"><a name="p359032151759"></a><a name="p359032151759"></a>backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.73287328732873%" headers="mcps1.1.4.1.2 "><p id="p88849851759"><a name="p88849851759"></a><a name="p88849851759"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.724372437243716%" headers="mcps1.1.4.1.3 "><p id="p485952191759"><a name="p485952191759"></a><a name="p485952191759"></a>Backup list returned by the query request. For details, see the <strong id="b116458371315"><a name="b116458371315"></a><a name="b116458371315"></a>backup</strong> field description.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **backup**  field description

    <a name="table15650133662614"></a>
    <table><thead align="left"><tr id="row365093619266"><th class="cellrowborder" valign="top" width="27.54275427542754%" id="mcps1.1.4.1.1"><p id="p146507362268"><a name="p146507362268"></a><a name="p146507362268"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.73287328732873%" id="mcps1.1.4.1.2"><p id="p56501536192610"><a name="p56501536192610"></a><a name="p56501536192610"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.724372437243716%" id="mcps1.1.4.1.3"><p id="p186505364261"><a name="p186505364261"></a><a name="p186505364261"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1365119363268"><td class="cellrowborder" valign="top" width="27.54275427542754%" headers="mcps1.1.4.1.1 "><p id="p76511536162616"><a name="p76511536162616"></a><a name="p76511536162616"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.73287328732873%" headers="mcps1.1.4.1.2 "><p id="p16651143642612"><a name="p16651143642612"></a><a name="p16651143642612"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.724372437243716%" headers="mcps1.1.4.1.3 "><p id="p1765123617268"><a name="p1765123617268"></a><a name="p1765123617268"></a>Backup ID</p>
    </td>
    </tr>
    <tr id="row96514367263"><td class="cellrowborder" valign="top" width="27.54275427542754%" headers="mcps1.1.4.1.1 "><p id="p17651163620268"><a name="p17651163620268"></a><a name="p17651163620268"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.73287328732873%" headers="mcps1.1.4.1.2 "><p id="p8651536112613"><a name="p8651536112613"></a><a name="p8651536112613"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.724372437243716%" headers="mcps1.1.4.1.3 "><p id="p19651536152620"><a name="p19651536152620"></a><a name="p19651536152620"></a>Backup URL. For details, see the <strong id="b28046449416"><a name="b28046449416"></a><a name="b28046449416"></a>links</strong> field description.</p>
    </td>
    </tr>
    <tr id="row10651163610265"><td class="cellrowborder" valign="top" width="27.54275427542754%" headers="mcps1.1.4.1.1 "><p id="p2651936172617"><a name="p2651936172617"></a><a name="p2651936172617"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.73287328732873%" headers="mcps1.1.4.1.2 "><p id="p46517368268"><a name="p46517368268"></a><a name="p46517368268"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.724372437243716%" headers="mcps1.1.4.1.3 "><p id="p1665111364265"><a name="p1665111364265"></a><a name="p1665111364265"></a>Backup name</p>
    </td>
    </tr>
    <tr id="row665119364262"><td class="cellrowborder" valign="top" width="27.54275427542754%" headers="mcps1.1.4.1.1 "><p id="p10651936172617"><a name="p10651936172617"></a><a name="p10651936172617"></a>backups_links</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.73287328732873%" headers="mcps1.1.4.1.2 "><p id="p56511936192610"><a name="p56511936192610"></a><a name="p56511936192610"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.724372437243716%" headers="mcps1.1.4.1.3 "><p id="p66513367266"><a name="p66513367266"></a><a name="p66513367266"></a>Specifies that only part of a tenant's backup information is queried, such as query by page with the limit table specified and when the number of backups exceeds 1000.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **links**  field description

    <a name="table1978423718262"></a>
    <table><thead align="left"><tr id="row2784103742613"><th class="cellrowborder" valign="top" width="27.54275427542754%" id="mcps1.1.4.1.1"><p id="p1978414373266"><a name="p1978414373266"></a><a name="p1978414373266"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.73287328732873%" id="mcps1.1.4.1.2"><p id="p7784163712614"><a name="p7784163712614"></a><a name="p7784163712614"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="43.724372437243716%" id="mcps1.1.4.1.3"><p id="p078413371267"><a name="p078413371267"></a><a name="p078413371267"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row107852375261"><td class="cellrowborder" valign="top" width="27.54275427542754%" headers="mcps1.1.4.1.1 "><p id="p19785123714267"><a name="p19785123714267"></a><a name="p19785123714267"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.73287328732873%" headers="mcps1.1.4.1.2 "><p id="p2078510379264"><a name="p2078510379264"></a><a name="p2078510379264"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.724372437243716%" headers="mcps1.1.4.1.3 "><p id="p14785153772616"><a name="p14785153772616"></a><a name="p14785153772616"></a>Specifies that the URL of the last backup is queried.</p>
    </td>
    </tr>
    <tr id="row6785163712262"><td class="cellrowborder" valign="top" width="27.54275427542754%" headers="mcps1.1.4.1.1 "><p id="p16785113710264"><a name="p16785113710264"></a><a name="p16785113710264"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.73287328732873%" headers="mcps1.1.4.1.2 "><p id="p167851737172617"><a name="p167851737172617"></a><a name="p167851737172617"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.724372437243716%" headers="mcps1.1.4.1.3 "><p id="p16785173752613"><a name="p16785173752613"></a><a name="p16785173752613"></a>Relationship between the query result and <strong id="b842352706202944"><a name="b842352706202944"></a><a name="b842352706202944"></a>href.</strong> The value <strong id="b1636101139174441"><a name="b1636101139174441"></a><a name="b1636101139174441"></a>next</strong> indicates that some backups are not obtained.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
    "backups": [
    {
    "id": "1d1139d8-8989-49d3-8aa1-83eb691e6db2",
    "links": [
    {
    "href": "http://192.168.82.222:8776/v2/b23b579f08c84228b9b4673c46f0c442/backups/1d1139d8-8989-49d3-8aa1-83eb691e6db2",
    "rel": "self"
    },
    {
    "href": "http://192.168.82.222:8776/b23b579f08c84228b9b4673c46f0c442/backups/1d1139d8-8989-49d3-8aa1-83eb691e6db2",
    "rel": "bookmark"
    }
    ],
    "name": null
    },
    {
    "id": "b3cf7a16-decc-4beb-8077-682737d94a58",
    "links": [
    {
    "href": "http://192.168.82.222:8776/v2/b23b579f08c84228b9b4673c46f0c442/backups/b3cf7a16-decc-4beb-8077-682737d94a58",
    "rel": "self"
    },
    {
    "href": "http://192.168.82.222:8776/b23b579f08c84228b9b4673c46f0c442/backups/b3cf7a16-decc-4beb-8077-682737d94a58",
    "rel": "bookmark"
    }
    ],
    "name": null
    }
    ],
    "backups_links": [
        {
          "href": "http://192.168.82.222:8776/b23b579f08c84228b9b4673c46f0c442/backups?limit=1&offset=1&marker=b3cf7a16-decc-4beb-8077-682737d94a58",
          "rel": "next"
        }
      ]
    }
    ```


## Status Codes<a name="section27618155"></a>

-   Normal

    200

-   Abnormal

    <a name="table59178184203255"></a>
    <table><thead align="left"><tr id="row54047877203255"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p15801936203255"><a name="p15801936203255"></a><a name="p15801936203255"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p4888452203255"><a name="p4888452203255"></a><a name="p4888452203255"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60420295203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p62205764203255"><a name="p62205764203255"></a><a name="p62205764203255"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5502113203255"><a name="p5502113203255"></a><a name="p5502113203255"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row49519019203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p51617596203255"><a name="p51617596203255"></a><a name="p51617596203255"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p20275713203255"><a name="p20275713203255"></a><a name="p20275713203255"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row48263690203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p17044857203255"><a name="p17044857203255"></a><a name="p17044857203255"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38456209203255"><a name="p38456209203255"></a><a name="p38456209203255"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row10561563203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p50180290203255"><a name="p50180290203255"></a><a name="p50180290203255"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38071718203255"><a name="p38071718203255"></a><a name="p38071718203255"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row7101146203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p38321955203255"><a name="p38321955203255"></a><a name="p38321955203255"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p17070685203255"><a name="p17070685203255"></a><a name="p17070685203255"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row19418444203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p29390130203255"><a name="p29390130203255"></a><a name="p29390130203255"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p31790300203255"><a name="p31790300203255"></a><a name="p31790300203255"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row17677246203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p22570826203255"><a name="p22570826203255"></a><a name="p22570826203255"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p16297614203255"><a name="p16297614203255"></a><a name="p16297614203255"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row12460805203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2692305203255"><a name="p2692305203255"></a><a name="p2692305203255"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p16750186203255"><a name="p16750186203255"></a><a name="p16750186203255"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row16533951203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p64181621203255"><a name="p64181621203255"></a><a name="p64181621203255"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p31328812203255"><a name="p31328812203255"></a><a name="p31328812203255"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row13523855203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p21690474203255"><a name="p21690474203255"></a><a name="p21690474203255"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p12097945203255"><a name="p12097945203255"></a><a name="p12097945203255"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row41772644203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p28140973203255"><a name="p28140973203255"></a><a name="p28140973203255"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p64826302203255"><a name="p64826302203255"></a><a name="p64826302203255"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row46565809203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p13734210203255"><a name="p13734210203255"></a><a name="p13734210203255"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38729264203255"><a name="p38729264203255"></a><a name="p38729264203255"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row13019061203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p47911033203255"><a name="p47911033203255"></a><a name="p47911033203255"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p55588428203255"><a name="p55588428203255"></a><a name="p55588428203255"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row30533812203255"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p57319716203255"><a name="p57319716203255"></a><a name="p57319716203255"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p12385400203255"><a name="p12385400203255"></a><a name="p12385400203255"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section1362310255432"></a>

For details, see  [Error Codes](error-codes.md).

