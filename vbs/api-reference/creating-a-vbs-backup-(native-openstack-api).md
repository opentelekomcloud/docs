# Creating a VBS Backup \(Native OpenStack API\)<a name="EN-US_TOPIC_0060614329"></a>

## Function<a name="section128772267269"></a>

This interface is used to create a VBS backup.

## URI<a name="section108771626172620"></a>

-   URI format

    POST /v2/\{project\_id\}/backups

-   Parameter description

    <a name="table10877182612265"></a>
    <table><thead align="left"><tr id="row3878162632617"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p19878132612265"><a name="p19878132612265"></a><a name="p19878132612265"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p5878826102618"><a name="p5878826102618"></a><a name="p5878826102618"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p58781263267"><a name="p58781263267"></a><a name="p58781263267"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row48783267269"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p587817266261"><a name="p587817266261"></a><a name="p587817266261"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p1787815263261"><a name="p1787815263261"></a><a name="p1787815263261"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p64170449"><a name="p64170449"></a><a name="p64170449"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section6878142612269"></a>

-   Parameter description

    <a name="table1687812615267"></a>
    <table><thead align="left"><tr id="row2087872611268"><th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.1.5.1.1"><p id="p61804813"><a name="p61804813"></a><a name="p61804813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.1.5.1.2"><p id="p40133923"><a name="p40133923"></a><a name="p40133923"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.1.5.1.3"><p id="p14225104112"><a name="p14225104112"></a><a name="p14225104112"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.57575757575757%" id="mcps1.1.5.1.4"><p id="p29622330"><a name="p29622330"></a><a name="p29622330"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16879926172613"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.5.1.1 "><p id="p5879192692614"><a name="p5879192692614"></a><a name="p5879192692614"></a>backup</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.5.1.2 "><p id="p12879202622616"><a name="p12879202622616"></a><a name="p12879202622616"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.5.1.3 "><p id="p148794268268"><a name="p148794268268"></a><a name="p148794268268"></a>dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.57575757575757%" headers="mcps1.1.5.1.4 "><p id="p1687902642619"><a name="p1687902642619"></a><a name="p1687902642619"></a>Backup to be created For details, see the <strong id="b1540811222213"><a name="b1540811222213"></a><a name="b1540811222213"></a>backup</strong> field description.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   **backup**  field description

    <a name="table240511311239"></a>
    <table><thead align="left"><tr id="row15405203142317"><th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.1.5.1.1"><p id="p1140683112236"><a name="p1140683112236"></a><a name="p1140683112236"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.1.5.1.2"><p id="p140618312238"><a name="p140618312238"></a><a name="p140618312238"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.1.5.1.3"><p id="p9406163182310"><a name="p9406163182310"></a><a name="p9406163182310"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.57575757575757%" id="mcps1.1.5.1.4"><p id="p540683142313"><a name="p540683142313"></a><a name="p540683142313"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15406113116236"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.5.1.1 "><p id="p194061131182315"><a name="p194061131182315"></a><a name="p194061131182315"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.5.1.2 "><p id="p1540603172313"><a name="p1540603172313"></a><a name="p1540603172313"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.5.1.3 "><p id="p12406231172313"><a name="p12406231172313"></a><a name="p12406231172313"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.57575757575757%" headers="mcps1.1.5.1.4 "><p id="p16406193118232"><a name="p16406193118232"></a><a name="p16406193118232"></a>ID of the disk to be backed up</p>
    </td>
    </tr>
    <tr id="row84061431172314"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.5.1.1 "><p id="p124061931112310"><a name="p124061931112310"></a><a name="p124061931112310"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.5.1.2 "><p id="p1240623115232"><a name="p1240623115232"></a><a name="p1240623115232"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.5.1.3 "><p id="p9406163115235"><a name="p9406163115235"></a><a name="p9406163115235"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.57575757575757%" headers="mcps1.1.5.1.4 "><p id="p104061631192311"><a name="p104061631192311"></a><a name="p104061631192311"></a>Snapshot ID of the disk to be backed up</p>
    </td>
    </tr>
    <tr id="row1540616316238"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.5.1.1 "><p id="p1540613118234"><a name="p1540613118234"></a><a name="p1540613118234"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.5.1.2 "><p id="p184061331162314"><a name="p184061331162314"></a><a name="p184061331162314"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.5.1.3 "><p id="p11406153111232"><a name="p11406153111232"></a><a name="p11406153111232"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.57575757575757%" headers="mcps1.1.5.1.4 "><p id="p1406193116239"><a name="p1406193116239"></a><a name="p1406193116239"></a>Backup name. The value is a string of 1 to 64 characters that can contain digits, letters, underscores (_), and hyphens (-), not starting with <strong id="b17747512133815"><a name="b17747512133815"></a><a name="b17747512133815"></a>auto</strong>.</p>
    </td>
    </tr>
    <tr id="row184061231122312"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.5.1.1 "><p id="p34062031102312"><a name="p34062031102312"></a><a name="p34062031102312"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.5.1.2 "><p id="p17406153113239"><a name="p17406153113239"></a><a name="p17406153113239"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.5.1.3 "><p id="p7406231162310"><a name="p7406231162310"></a><a name="p7406231162310"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.57575757575757%" headers="mcps1.1.5.1.4 "><p id="p24061731152311"><a name="p24061731152311"></a><a name="p24061731152311"></a>Backup description. The value consists of 0 to 255 characters and must not contain a greater-than sign (&gt;) or less-than sign (&lt;).</p>
    </td>
    </tr>
    <tr id="row64061731132317"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.5.1.1 "><p id="p16406531112315"><a name="p16406531112315"></a><a name="p16406531112315"></a>container</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.5.1.2 "><p id="p3406731162320"><a name="p3406731162320"></a><a name="p3406731162320"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.5.1.3 "><p id="p2040619315231"><a name="p2040619315231"></a><a name="p2040619315231"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.57575757575757%" headers="mcps1.1.5.1.4 "><p id="p1406103122314"><a name="p1406103122314"></a><a name="p1406103122314"></a>Backup container. This parameter is reserved and will be skipped.</p>
    </td>
    </tr>
    <tr id="row7406103162313"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.5.1.1 "><p id="p840663172310"><a name="p840663172310"></a><a name="p840663172310"></a>incremental</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.5.1.2 "><p id="p64061931112316"><a name="p64061931112316"></a><a name="p64061931112316"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.5.1.3 "><p id="p2406113152319"><a name="p2406113152319"></a><a name="p2406113152319"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.57575757575757%" headers="mcps1.1.5.1.4 "><p id="p1440633117234"><a name="p1440633117234"></a><a name="p1440633117234"></a>Whether it is an incremental backup. The value <strong id="b944876071173146"><a name="b944876071173146"></a><a name="b944876071173146"></a>true</strong> indicates an incremental backup and <strong id="b635798495173146"><a name="b635798495173146"></a><a name="b635798495173146"></a>false</strong> indicates a full backup. VBS generates a full backup for the initial backup operation and incremental backups for subsequent backup operations. Therefore, this parameter will be skipped.</p>
    </td>
    </tr>
    <tr id="row184061931182311"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.5.1.1 "><p id="p17406031152316"><a name="p17406031152316"></a><a name="p17406031152316"></a>force</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.5.1.2 "><p id="p240643119238"><a name="p240643119238"></a><a name="p240643119238"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.5.1.3 "><p id="p19406631182313"><a name="p19406631182313"></a><a name="p19406631182313"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.57575757575757%" headers="mcps1.1.5.1.4 "><p id="p940663118234"><a name="p940663118234"></a><a name="p940663118234"></a>Whether to forcibly back up the attached volumes. <strong id="b1398201636194330"><a name="b1398201636194330"></a><a name="b1398201636194330"></a>true</strong> indicates a forcible backup and <strong id="b12911634194330"><a name="b12911634194330"></a><a name="b12911634194330"></a>false</strong> indicates a non-forcible backup. The value defaults to <strong id="b20900114021420"><a name="b20900114021420"></a><a name="b20900114021420"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row184064319233"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.1.5.1.1 "><p id="p8406133118233"><a name="p8406133118233"></a><a name="p8406133118233"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.1.5.1.2 "><p id="p9406163117238"><a name="p9406163117238"></a><a name="p9406163117238"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.5.1.3 "><p id="p940619313239"><a name="p940619313239"></a><a name="p940619313239"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.57575757575757%" headers="mcps1.1.5.1.4 "><p id="p144061231152318"><a name="p144061231152318"></a><a name="p144061231152318"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "backup": {
            "volume_id": "c68ae7fb-0aa5-4a97-ab01-ed02c5b7e768",
            "snapshot_id": "2bb856e1-b3d8-4432-a858-09e4ce939389",
            "name": "backup1",
            "description": "Backup_Demo"
        }
    }
    ```


## Response<a name="section1688092620262"></a>

-   Parameter description

    <a name="table2088152642611"></a>
    <table><thead align="left"><tr id="row988120268264"><th class="cellrowborder" valign="top" width="15.428457154284573%" id="mcps1.1.4.1.1"><p id="p1143211420109"><a name="p1143211420109"></a><a name="p1143211420109"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.088391160883912%" id="mcps1.1.4.1.2"><p id="p343211145109"><a name="p343211145109"></a><a name="p343211145109"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="68.48315168483151%" id="mcps1.1.4.1.3"><p id="p154329144105"><a name="p154329144105"></a><a name="p154329144105"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row209732037181912"><td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.1.4.1.1 "><p id="p69734375196"><a name="p69734375196"></a><a name="p69734375196"></a>backup</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.088391160883912%" headers="mcps1.1.4.1.2 "><p id="p397313741919"><a name="p397313741919"></a><a name="p397313741919"></a>dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.48315168483151%" headers="mcps1.1.4.1.3 "><p id="p12974337121919"><a name="p12974337121919"></a><a name="p12974337121919"></a>Information about the created backup</p>
    </td>
    </tr>
    <tr id="row588162613261"><td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.1.4.1.1 "><p id="p18811526192613"><a name="p18811526192613"></a><a name="p18811526192613"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.088391160883912%" headers="mcps1.1.4.1.2 "><p id="p2881142652619"><a name="p2881142652619"></a><a name="p2881142652619"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.48315168483151%" headers="mcps1.1.4.1.3 "><p id="p988119267264"><a name="p988119267264"></a><a name="p988119267264"></a>Backup ID</p>
    </td>
    </tr>
    <tr id="row17881122692616"><td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.1.4.1.1 "><p id="p1888152672615"><a name="p1888152672615"></a><a name="p1888152672615"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.088391160883912%" headers="mcps1.1.4.1.2 "><p id="p88821626182611"><a name="p88821626182611"></a><a name="p88821626182611"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.48315168483151%" headers="mcps1.1.4.1.3 "><p id="p1288212267264"><a name="p1288212267264"></a><a name="p1288212267264"></a>Backup name</p>
    </td>
    </tr>
    <tr id="row16882182642616"><td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.1.4.1.1 "><p id="p7882152613264"><a name="p7882152613264"></a><a name="p7882152613264"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.088391160883912%" headers="mcps1.1.4.1.2 "><p id="p1047631013245"><a name="p1047631013245"></a><a name="p1047631013245"></a>list&lt;dict&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.48315168483151%" headers="mcps1.1.4.1.3 "><p id="p8882826102616"><a name="p8882826102616"></a><a name="p8882826102616"></a>Information about the backup URL</p>
    </td>
    </tr>
    <tr id="row106053292415"><td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.1.4.1.1 "><p id="p2938115917245"><a name="p2938115917245"></a><a name="p2938115917245"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.088391160883912%" headers="mcps1.1.4.1.2 "><p id="p5938135932418"><a name="p5938135932418"></a><a name="p5938135932418"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.48315168483151%" headers="mcps1.1.4.1.3 "><p id="p149387596241"><a name="p149387596241"></a><a name="p149387596241"></a>Backup URL</p>
    </td>
    </tr>
    <tr id="row826935102410"><td class="cellrowborder" valign="top" width="15.428457154284573%" headers="mcps1.1.4.1.1 "><p id="p893825917243"><a name="p893825917243"></a><a name="p893825917243"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.088391160883912%" headers="mcps1.1.4.1.2 "><p id="p2939195972410"><a name="p2939195972410"></a><a name="p2939195972410"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.48315168483151%" headers="mcps1.1.4.1.3 "><p id="p9939159112419"><a name="p9939159112419"></a><a name="p9939159112419"></a>Relationship between the query result and <strong id="b84235270620223"><a name="b84235270620223"></a><a name="b84235270620223"></a>href</strong></p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "backup": {
        "id": "54ba0e69-48a0-4a77-9cdf-a7979a7e2648",
        "links": [
          {
            "href": "https://volume.Region.dc1.domainname.com/v2/5751d8c3f2f6415993ee4326b41630ec/backups/54ba0e69-48a0-4a77-9cdf-a7979a7e2648",
            "rel": "self"
          },
          {
            "href": "https://volume.Region.dc1.domainname.com/5751d8c3f2f6415993ee4326b41630ec/backups/54ba0e69-48a0-4a77-9cdf-a7979a7e2648",
            "rel": "bookmark"
          }
        ],
        "name": "backup1"
      }
    }
    ```

    or

    ```
    {
    "badRequest": {
    "code": "XXXX",
    "message": "XXX"
    }
    }
    ```


## Status Codes<a name="section17882202616269"></a>

-   Normal

    202

-   Abnormal

    <a name="table7883926192615"></a>
    <table><thead align="left"><tr id="row188372632618"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p1688302618266"><a name="p1688302618266"></a><a name="p1688302618266"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p8883192616268"><a name="p8883192616268"></a><a name="p8883192616268"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2088382652612"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p178837261267"><a name="p178837261267"></a><a name="p178837261267"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p13883132619261"><a name="p13883132619261"></a><a name="p13883132619261"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row688318265265"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p988382692617"><a name="p988382692617"></a><a name="p988382692617"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p188831026162620"><a name="p188831026162620"></a><a name="p188831026162620"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row28831326142613"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p12883122618262"><a name="p12883122618262"></a><a name="p12883122618262"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p16883162612614"><a name="p16883162612614"></a><a name="p16883162612614"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row58839263265"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p9883122620266"><a name="p9883122620266"></a><a name="p9883122620266"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1488392616263"><a name="p1488392616263"></a><a name="p1488392616263"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row118831626152615"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p78831226112614"><a name="p78831226112614"></a><a name="p78831226112614"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p488362682611"><a name="p488362682611"></a><a name="p488362682611"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row1288419267265"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1488419266260"><a name="p1488419266260"></a><a name="p1488419266260"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p18841626122612"><a name="p18841626122612"></a><a name="p18841626122612"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row16884162602620"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p138843264264"><a name="p138843264264"></a><a name="p138843264264"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p88841926142612"><a name="p88841926142612"></a><a name="p88841926142612"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row18884112662617"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p178841126102610"><a name="p178841126102610"></a><a name="p178841126102610"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p38841526192614"><a name="p38841526192614"></a><a name="p38841526192614"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row288452672617"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p14884182612267"><a name="p14884182612267"></a><a name="p14884182612267"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p13884182662616"><a name="p13884182662616"></a><a name="p13884182662616"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row1988412692612"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p48841426182619"><a name="p48841426182619"></a><a name="p48841426182619"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p788419265260"><a name="p788419265260"></a><a name="p788419265260"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row148844263260"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2088442614267"><a name="p2088442614267"></a><a name="p2088442614267"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1788412617261"><a name="p1788412617261"></a><a name="p1788412617261"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row088462622611"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p18884152614267"><a name="p18884152614267"></a><a name="p18884152614267"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1288462632611"><a name="p1288462632611"></a><a name="p1288462632611"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row178846268263"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1588412261264"><a name="p1588412261264"></a><a name="p1588412261264"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2884192614266"><a name="p2884192614266"></a><a name="p2884192614266"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row19885162622618"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p8885112662616"><a name="p8885112662616"></a><a name="p8885112662616"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p888519268261"><a name="p888519268261"></a><a name="p888519268261"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section1362310255432"></a>

For details, see  [Error Codes](error-codes.md).

