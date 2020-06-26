# Updating a Data Source<a name="EN-US_TOPIC_0172486213"></a>

## Function<a name="section11410068144834"></a>

This API is used to update a data source. If the data source does not exist, the system reports an error. This API is compatible with Sahara.

## URI<a name="section4721807314497"></a>

-   Format

    PUT /v1.1/\{project\_id\}/data-sources/\{data\_source\_id\}

-   Parameter description

    **Table  1**  URI parameter description

    <a name="table49499141194754"></a>
    <table><thead align="left"><tr id="row33700024194754"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p16571835194812"><a name="p16571835194812"></a><a name="p16571835194812"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p141410194812"><a name="p141410194812"></a><a name="p141410194812"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p11454278194812"><a name="p11454278194812"></a><a name="p11454278194812"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6505449415356"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p3492262515356"><a name="p3492262515356"></a><a name="p3492262515356"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p1016041415356"><a name="p1016041415356"></a><a name="p1016041415356"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1768719515356"><a name="p1768719515356"></a><a name="p1768719515356"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row20659256153330"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p62787041153330"><a name="p62787041153330"></a><a name="p62787041153330"></a>data_source_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p52585595153330"><a name="p52585595153330"></a><a name="p52585595153330"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p31574830153330"><a name="p31574830153330"></a><a name="p31574830153330"></a>Data source ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section31697334144924"></a>

**Table  2**  Request parameter description

<a name="table1603131015403"></a>
<table><thead align="left"><tr id="row1607843515403"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p2728483015403"><a name="p2728483015403"></a><a name="p2728483015403"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p6258762615403"><a name="p6258762615403"></a><a name="p6258762615403"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p45230398152729"><a name="p45230398152729"></a><a name="p45230398152729"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p3643294215403"><a name="p3643294215403"></a><a name="p3643294215403"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14299430102131"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p11744825102315"><a name="p11744825102315"></a><a name="p11744825102315"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p11806775102315"><a name="p11806775102315"></a><a name="p11806775102315"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p16824758102315"><a name="p16824758102315"></a><a name="p16824758102315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p20628190102315"><a name="p20628190102315"></a><a name="p20628190102315"></a>Data source name</p>
<p id="p51435984102315"><a name="p51435984102315"></a><a name="p51435984102315"></a>Contains 1 to 80 characters and consists of letters, digits, hyphens (-), and underscores (_) only.</p>
</td>
</tr>
<tr id="row46055705102136"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p38704048102359"><a name="p38704048102359"></a><a name="p38704048102359"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p48020182102359"><a name="p48020182102359"></a><a name="p48020182102359"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p64429504102359"><a name="p64429504102359"></a><a name="p64429504102359"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p51407318102359"><a name="p51407318102359"></a><a name="p51407318102359"></a>Data source type</p>
<a name="ul60012686102359"></a><a name="ul60012686102359"></a><ul id="ul60012686102359"><li>hdfs</li><li>obs</li><li>swift (not supported by the current version)</li></ul>
</td>
</tr>
<tr id="row31141531102143"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p57562259102339"><a name="p57562259102339"></a><a name="p57562259102339"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p32031378102339"><a name="p32031378102339"></a><a name="p32031378102339"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p44404814102339"><a name="p44404814102339"></a><a name="p44404814102339"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p40020142102339"><a name="p40020142102339"></a><a name="p40020142102339"></a>Data source URL</p>
<p id="p1953133111171"><a name="p1953133111171"></a><a name="p1953133111171"></a>Contains 1 to 255 characters.</p>
<a name="ul24636959102339"></a><a name="ul24636959102339"></a><ul id="ul24636959102339"><li>If the data source type is HDFS, the value is <strong id="b395615292211"><a name="b395615292211"></a><a name="b395615292211"></a>/</strong><em id="i1215990992211"><a name="i1215990992211"></a><a name="i1215990992211"></a>Save path of the data source</em>.</li><li>If the data source type is OBS, the value is <strong id="b22866623155631"><a name="b22866623155631"></a><a name="b22866623155631"></a>s3a://</strong><em id="i1076191992211"><a name="i1076191992211"></a><a name="i1076191992211"></a>Save path of the data source</em>.</li></ul>
</td>
</tr>
<tr id="row6538721915403"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p3925522010269"><a name="p3925522010269"></a><a name="p3925522010269"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p2555627710269"><a name="p2555627710269"></a><a name="p2555627710269"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p5679259510269"><a name="p5679259510269"></a><a name="p5679259510269"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p3679749310269"><a name="p3679749310269"></a><a name="p3679749310269"></a>Data source description</p>
<p id="p21051431151815"><a name="p21051431151815"></a><a name="p21051431151815"></a>Contains a maximum of 65535 characters.</p>
</td>
</tr>
<tr id="row6526202815403"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p40455002102533"><a name="p40455002102533"></a><a name="p40455002102533"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p55629730102533"><a name="p55629730102533"></a><a name="p55629730102533"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p9714295102533"><a name="p9714295102533"></a><a name="p9714295102533"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p48660416102533"><a name="p48660416102533"></a><a name="p48660416102533"></a>Whether the data source is protected</p>
<a name="ul35290564102533"></a><a name="ul35290564102533"></a><ul id="ul35290564102533"><li>true</li><li>false</li></ul>
<p id="p24126416102533"><a name="p24126416102533"></a><a name="p24126416102533"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row16863865102529"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p5635102102533"><a name="p5635102102533"></a><a name="p5635102102533"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p53790114102533"><a name="p53790114102533"></a><a name="p53790114102533"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p62032007102533"><a name="p62032007102533"></a><a name="p62032007102533"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p58536693102533"><a name="p58536693102533"></a><a name="p58536693102533"></a>Whether the data source is public</p>
<a name="ul57068190102533"></a><a name="ul57068190102533"></a><ul id="ul57068190102533"><li>true</li><li>false</li></ul>
<p id="p62324105102533"><a name="p62324105102533"></a><a name="p62324105102533"></a>The current version does not support this function.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section10069032144933"></a>

**Table  3**  Response parameter description

<a name="table51257841151049"></a>
<table><thead align="left"><tr id="row8480851151049"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p15860319151049"><a name="p15860319151049"></a><a name="p15860319151049"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p40813771151049"><a name="p40813771151049"></a><a name="p40813771151049"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p17581180151049"><a name="p17581180151049"></a><a name="p17581180151049"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14789514151049"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p28232664151128"><a name="p28232664151128"></a><a name="p28232664151128"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p32100671151824"><a name="p32100671151824"></a><a name="p32100671151824"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p60375806151049"><a name="p60375806151049"></a><a name="p60375806151049"></a>Data source description</p>
</td>
</tr>
<tr id="row6511344151049"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p59583657151128"><a name="p59583657151128"></a><a name="p59583657151128"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p47113545151824"><a name="p47113545151824"></a><a name="p47113545151824"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p38365320151049"><a name="p38365320151049"></a><a name="p38365320151049"></a>Data source URL</p>
</td>
</tr>
<tr id="row33112539151141"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p64870032151141"><a name="p64870032151141"></a><a name="p64870032151141"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p2060135151824"><a name="p2060135151824"></a><a name="p2060135151824"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p13856035173519"><a name="p13856035173519"></a><a name="p13856035173519"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row22096096151146"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p44953331151146"><a name="p44953331151146"></a><a name="p44953331151146"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p26983233151824"><a name="p26983233151824"></a><a name="p26983233151824"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p25869246151146"><a name="p25869246151146"></a><a name="p25869246151146"></a>Data source creation time</p>
</td>
</tr>
<tr id="row4456002103134"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p25391906103134"><a name="p25391906103134"></a><a name="p25391906103134"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p32099444103134"><a name="p32099444103134"></a><a name="p32099444103134"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p49918133103134"><a name="p49918133103134"></a><a name="p49918133103134"></a>Data source update time</p>
</td>
</tr>
<tr id="row18376161151152"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p10483939151640"><a name="p10483939151640"></a><a name="p10483939151640"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p65650233151640"><a name="p65650233151640"></a><a name="p65650233151640"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p16068681151640"><a name="p16068681151640"></a><a name="p16068681151640"></a>Whether the data source is protected</p>
<a name="ul24233663152954"></a><a name="ul24233663152954"></a><ul id="ul24233663152954"><li>true</li><li>false</li></ul>
<p id="p16709791152954"><a name="p16709791152954"></a><a name="p16709791152954"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row6726034151222"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p20438892151640"><a name="p20438892151640"></a><a name="p20438892151640"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p16062920151640"><a name="p16062920151640"></a><a name="p16062920151640"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p26028163151640"><a name="p26028163151640"></a><a name="p26028163151640"></a>Whether the data source is public</p>
<a name="ul23909441152958"></a><a name="ul23909441152958"></a><ul id="ul23909441152958"><li>true</li><li>false</li></ul>
<p id="p48787181152958"><a name="p48787181152958"></a><a name="p48787181152958"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row25334813151227"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p38853957151227"><a name="p38853957151227"></a><a name="p38853957151227"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p66202595151828"><a name="p66202595151828"></a><a name="p66202595151828"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p60833455151227"><a name="p60833455151227"></a><a name="p60833455151227"></a>Data source type</p>
</td>
</tr>
<tr id="row8652083151249"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p29730140151249"><a name="p29730140151249"></a><a name="p29730140151249"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p17113312151828"><a name="p17113312151828"></a><a name="p17113312151828"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p39995064151249"><a name="p39995064151249"></a><a name="p39995064151249"></a>Data source ID</p>
</td>
</tr>
<tr id="row12228393151256"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p50975775151256"><a name="p50975775151256"></a><a name="p50975775151256"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p21869845151828"><a name="p21869845151828"></a><a name="p21869845151828"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p43580859151256"><a name="p43580859151256"></a><a name="p43580859151256"></a>Data source name</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section205032433315"></a>

-   Example request

    ```
    { 
        "name": "my-data-source-update",  
        "url": "/simple/mapreduce/input",  
        "is_protected": false,  
        "is_public": false,  
        "type": "hdfs",  
        "description": "this is the data source template" 
    }
    ```


-   Example response

    ```
    {
        "data_source": {
            "name": "my-data-source-update",
            "type": "hdfs",
            "url": "/simple/mapreduce/input",
            "description": "this is the data source template",
            "created_at": "2017-06-22T08:28:57",
            "updated_at": "2017-06-22T08:30:08",
            "id": "e275a927-fe72-4b8b-a634-e47a11dca181",
            "tenant_id": "5a3314075bfa49b9ae360f4ecd333695",
            "is_public": false,
            "is_protected": false
        }
    }
    ```


## Status Code<a name="section13299747144948"></a>

[Table 4](#table1584477916050)  describes the status code of this API.

**Table  4**  Status code

<a name="table1584477916050"></a>
<table><thead align="left"><tr id="row1339492016050"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p3411176516050"><a name="p3411176516050"></a><a name="p3411176516050"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p1158961516050"><a name="p1158961516050"></a><a name="p1158961516050"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3719767816050"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6022194016050"><a name="p6022194016050"></a><a name="p6022194016050"></a>202</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The data source has been successfully updated.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

