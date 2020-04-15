# Creating a Data Source<a name="EN-US_TOPIC_0172486222"></a>

## Function<a name="section11410068144834"></a>

This API is used to create a data source. This API is compatible with Sahara.

## URI<a name="section4721807314497"></a>

-   Format

    POST /v1.1/\{project\_id\}/data-sources

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
    </tbody>
    </table>


## Request<a name="section31697334144924"></a>

**Table  2**  Request parameter description

<a name="table19445385114112"></a>
<table><thead align="left"><tr id="row1790422114112"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p10806517114112"><a name="p10806517114112"></a><a name="p10806517114112"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p2912680114112"><a name="p2912680114112"></a><a name="p2912680114112"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p34600536114112"><a name="p34600536114112"></a><a name="p34600536114112"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.2.5.1.4"><p id="p51180012114112"><a name="p51180012114112"></a><a name="p51180012114112"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row51940301114112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p39771773145713"><a name="p39771773145713"></a><a name="p39771773145713"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p29636830145713"><a name="p29636830145713"></a><a name="p29636830145713"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p7598676145713"><a name="p7598676145713"></a><a name="p7598676145713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p53534038145713"><a name="p53534038145713"></a><a name="p53534038145713"></a>Data source name</p>
<p id="p667497994849"><a name="p667497994849"></a><a name="p667497994849"></a>Contains 1 to 80 characters and consists of letters, digits, hyphens (-), and underscores (_) only.</p>
</td>
</tr>
<tr id="row18284370114112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p43646883145713"><a name="p43646883145713"></a><a name="p43646883145713"></a>url</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p4937219915237"><a name="p4937219915237"></a><a name="p4937219915237"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p5870587215316"><a name="p5870587215316"></a><a name="p5870587215316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p57957308145713"><a name="p57957308145713"></a><a name="p57957308145713"></a>Data source URL</p>
<p id="p195891015248"><a name="p195891015248"></a><a name="p195891015248"></a>Contains 1 to 255 characters.</p>
<a name="ul197417161574"></a><a name="ul197417161574"></a><ul id="ul197417161574"><li>If the data source type is HDFS, the value is <strong id="b282583209530"><a name="b282583209530"></a><a name="b282583209530"></a>/</strong><em id="i389248869530"><a name="i389248869530"></a><a name="i389248869530"></a>Save path of the data source</em>.</li><li>If the data source type is OBS, the value is <strong id="b57629220155547"><a name="b57629220155547"></a><a name="b57629220155547"></a>s3a://</strong><em id="i59859279538"><a name="i59859279538"></a><a name="i59859279538"></a>Save path of the data source</em>.</li></ul>
</td>
</tr>
<tr id="row475482215758"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4959628115758"><a name="p4959628115758"></a><a name="p4959628115758"></a>credentials</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p5787579615758"><a name="p5787579615758"></a><a name="p5787579615758"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p5742790415758"><a name="p5742790415758"></a><a name="p5742790415758"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p2114864415758"><a name="p2114864415758"></a><a name="p2114864415758"></a>Authentication information. The current version does not support this function.</p>
</td>
</tr>
<tr id="row2693395895552"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p3416696195552"><a name="p3416696195552"></a><a name="p3416696195552"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1606046195552"><a name="p1606046195552"></a><a name="p1606046195552"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p2582896195552"><a name="p2582896195552"></a><a name="p2582896195552"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1177112695552"><a name="p1177112695552"></a><a name="p1177112695552"></a>Whether the data source is protected</p>
<a name="ul360256379574"></a><a name="ul360256379574"></a><ul id="ul360256379574"><li>true</li><li>false</li></ul>
<p id="p6483812795728"><a name="p6483812795728"></a><a name="p6483812795728"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row4788217195558"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p5325060395558"><a name="p5325060395558"></a><a name="p5325060395558"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p1833155995558"><a name="p1833155995558"></a><a name="p1833155995558"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p846133695558"><a name="p846133695558"></a><a name="p846133695558"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p1427965495558"><a name="p1427965495558"></a><a name="p1427965495558"></a>Whether the data source is public</p>
<a name="ul5208982895717"></a><a name="ul5208982895717"></a><ul id="ul5208982895717"><li>true</li><li>false</li></ul>
<p id="p6105735395725"><a name="p6105735395725"></a><a name="p6105735395725"></a>The current version does not support this function.</p>
</td>
</tr>
<tr id="row34155459114112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p62216246145713"><a name="p62216246145713"></a><a name="p62216246145713"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p2060969915237"><a name="p2060969915237"></a><a name="p2060969915237"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1226219015318"><a name="p1226219015318"></a><a name="p1226219015318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p40587883145713"><a name="p40587883145713"></a><a name="p40587883145713"></a>Data source type</p>
<a name="ul2600786315532"></a><a name="ul2600786315532"></a><ul id="ul2600786315532"><li>hdfs</li><li>obs</li><li>swift (not supported by the current version)</li></ul>
</td>
</tr>
<tr id="row41150634114112"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p54100889145713"><a name="p54100889145713"></a><a name="p54100889145713"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p3011949115237"><a name="p3011949115237"></a><a name="p3011949115237"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p3471563715318"><a name="p3471563715318"></a><a name="p3471563715318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.5.1.4 "><p id="p8987936145713"><a name="p8987936145713"></a><a name="p8987936145713"></a>Data source description</p>
<p id="p85145142518"><a name="p85145142518"></a><a name="p85145142518"></a>Contains a maximum of 65535 characters.</p>
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
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p20842175017348"><a name="p20842175017348"></a><a name="p20842175017348"></a>Project ID. For details on how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row22096096151146"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p44953331151146"><a name="p44953331151146"></a><a name="p44953331151146"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p26983233151824"><a name="p26983233151824"></a><a name="p26983233151824"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p25869246151146"><a name="p25869246151146"></a><a name="p25869246151146"></a>Data source creation time</p>
</td>
</tr>
<tr id="row44747700151120"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p685049151120"><a name="p685049151120"></a><a name="p685049151120"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p65422913151120"><a name="p65422913151120"></a><a name="p65422913151120"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p64764563151120"><a name="p64764563151120"></a><a name="p64764563151120"></a>Data source update time</p>
</td>
</tr>
<tr id="row18376161151152"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p10483939151640"><a name="p10483939151640"></a><a name="p10483939151640"></a>is_protected</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p65650233151640"><a name="p65650233151640"></a><a name="p65650233151640"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p16068681151640"><a name="p16068681151640"></a><a name="p16068681151640"></a>Whether the data source is protected</p>
</td>
</tr>
<tr id="row6726034151222"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p20438892151640"><a name="p20438892151640"></a><a name="p20438892151640"></a>is_public</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p16062920151640"><a name="p16062920151640"></a><a name="p16062920151640"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p26028163151640"><a name="p26028163151640"></a><a name="p26028163151640"></a>Whether the data source is public</p>
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
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p39995064151249"><a name="p39995064151249"></a><a name="p39995064151249"></a>ID returned by the system after the data source is created</p>
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

## Example<a name="section16281131022217"></a>

-   Example request

    ```
    { 
        "name": "my-data-source",  
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
            "name": "my-data-source",
            "type": "hdfs",
            "url": "/simple/mapreduce/input",
            "description": "this is the data source template",
            "created_at": "2017-06-22T08:28:57",
            "updated_at": null,
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
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4613894216050"><a name="p4613894216050"></a><a name="p4613894216050"></a>The data source has been successfully created.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Codes](status-codes.md).

