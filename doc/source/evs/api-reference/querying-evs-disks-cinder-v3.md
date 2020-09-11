# Querying EVS Disks<a name="evs_04_3032"></a>

## Function<a name="section60214390"></a>

This API is used to query EVS disks.

## URI<a name="section5058598"></a>

-   URI format

    GET /v3/\{project\_id\}/volumes

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
    </tbody>
    </table>

-   Request filter parameters

    <a name="en-us_topic_0058762430_table48630339152531"></a>
    <table><thead align="left"><tr id="en-us_topic_0058762430_row30502978152531"><th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.1.5.1.1"><p id="en-us_topic_0058762430_p54822134152531"><a name="en-us_topic_0058762430_p54822134152531"></a><a name="en-us_topic_0058762430_p54822134152531"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.1.5.1.2"><p id="en-us_topic_0058762430_p11407863152531"><a name="en-us_topic_0058762430_p11407863152531"></a><a name="en-us_topic_0058762430_p11407863152531"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.1.5.1.3"><p id="en-us_topic_0058762430_p51621676152531"><a name="en-us_topic_0058762430_p51621676152531"></a><a name="en-us_topic_0058762430_p51621676152531"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.51485148514851%" id="mcps1.1.5.1.4"><p id="en-us_topic_0058762430_p20606205152531"><a name="en-us_topic_0058762430_p20606205152531"></a><a name="en-us_topic_0058762430_p20606205152531"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0058762430_row58489940152531"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762430_p49168107152914"><a name="en-us_topic_0058762430_p49168107152914"></a><a name="en-us_topic_0058762430_p49168107152914"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762430_p23193765152914"><a name="en-us_topic_0058762430_p23193765152914"></a><a name="en-us_topic_0058762430_p23193765152914"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762430_p66755704152914"><a name="en-us_topic_0058762430_p66755704152914"></a><a name="en-us_topic_0058762430_p66755704152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0058762430_p38502923152914"><a name="en-us_topic_0058762430_p38502923152914"></a><a name="en-us_topic_0058762430_p38502923152914"></a><span id="text387847143818"><a name="text387847143818"></a><a name="text387847143818"></a>Specifies the ID of the last record on the previous page. The returned value is the value of the item after this one.</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762430_row38948343152859"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762430_p17125818152914"><a name="en-us_topic_0058762430_p17125818152914"></a><a name="en-us_topic_0058762430_p17125818152914"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762430_p14491527153320"><a name="en-us_topic_0058762430_p14491527153320"></a><a name="en-us_topic_0058762430_p14491527153320"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762430_p22259725152914"><a name="en-us_topic_0058762430_p22259725152914"></a><a name="en-us_topic_0058762430_p22259725152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0058762430_p58207321152914"><a name="en-us_topic_0058762430_p58207321152914"></a><a name="en-us_topic_0058762430_p58207321152914"></a>Specifies the disk name. <span id="en-us_topic_0058762430_text37302935152245"><a name="en-us_topic_0058762430_text37302935152245"></a><a name="en-us_topic_0058762430_text37302935152245"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762430_row61932754152911"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762430_p20335623152914"><a name="en-us_topic_0058762430_p20335623152914"></a><a name="en-us_topic_0058762430_p20335623152914"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762430_p36572733152914"><a name="en-us_topic_0058762430_p36572733152914"></a><a name="en-us_topic_0058762430_p36572733152914"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762430_p9601396152914"><a name="en-us_topic_0058762430_p9601396152914"></a><a name="en-us_topic_0058762430_p9601396152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0058762430_p39515603152914"><a name="en-us_topic_0058762430_p39515603152914"></a><a name="en-us_topic_0058762430_p39515603152914"></a>Specifies the maximum number of query results that can be returned.</p>
    <p id="p149391124171211"><a name="p149391124171211"></a><a name="p149391124171211"></a><span id="text138349551887"><a name="text138349551887"></a><a name="text138349551887"></a>The value ranges from 1 to 1000, and the default value is 1000. The returned value cannot exceed this limit.</span></p>
    <p id="en-us_topic_0058762430_p14657115572511"><a name="en-us_topic_0058762430_p14657115572511"></a><a name="en-us_topic_0058762430_p14657115572511"></a>If the tenant has more than 50 disks in total, you are advised to use this parameter and set its value to <strong id="b8423527069161"><a name="b8423527069161"></a><a name="b8423527069161"></a>50</strong> to improve the query efficiency. Examples are provided as follows:</p>
    <p id="en-us_topic_0058762430_p1233994321914"><a name="en-us_topic_0058762430_p1233994321914"></a><a name="en-us_topic_0058762430_p1233994321914"></a><strong id="b9984595891811"><a name="b9984595891811"></a><a name="b9984595891811"></a>GET /v3/</strong><em id="i40797784691811"><a name="i40797784691811"></a><a name="i40797784691811"></a>xxx</em><strong id="b172149191991811"><a name="b172149191991811"></a><a name="b172149191991811"></a>/volumes?limit=50</strong>: Queries the 1–50 disks. <strong id="b842352706102346"><a name="b842352706102346"></a><a name="b842352706102346"></a>GET /v3/</strong><em id="i587306121102343"><a name="i587306121102343"></a><a name="i587306121102343"></a>xxx</em><strong id="b842352706102351"><a name="b842352706102351"></a><a name="b842352706102351"></a>/volumes?offset=50&amp;limit=50</strong>: Queries the 51–100 disks.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762430_row4561665015299"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762430_p17172513152914"><a name="en-us_topic_0058762430_p17172513152914"></a><a name="en-us_topic_0058762430_p17172513152914"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762430_p43305182153332"><a name="en-us_topic_0058762430_p43305182153332"></a><a name="en-us_topic_0058762430_p43305182153332"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762430_p60186269152914"><a name="en-us_topic_0058762430_p60186269152914"></a><a name="en-us_topic_0058762430_p60186269152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="p43249593152914"><a name="p43249593152914"></a><a name="p43249593152914"></a>Specifies the keyword based on which the returned results are sorted. The value can be <strong id="b88241560412"><a name="b88241560412"></a><a name="b88241560412"></a>id</strong>, <strong id="b18257567418"><a name="b18257567418"></a><a name="b18257567418"></a>status</strong>, <strong id="b182665618411"><a name="b182665618411"></a><a name="b182665618411"></a>size</strong>, or <strong id="b18826145617418"><a name="b18826145617418"></a><a name="b18826145617418"></a>created_at</strong>, and the default value is <strong id="b6827185615410"><a name="b6827185615410"></a><a name="b6827185615410"></a>created_at</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762430_row5831630415296"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762430_p54896674152914"><a name="en-us_topic_0058762430_p54896674152914"></a><a name="en-us_topic_0058762430_p54896674152914"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762430_p4460297153338"><a name="en-us_topic_0058762430_p4460297153338"></a><a name="en-us_topic_0058762430_p4460297153338"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762430_p3809857152914"><a name="en-us_topic_0058762430_p3809857152914"></a><a name="en-us_topic_0058762430_p3809857152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><div class="p" id="p2025341125211"><a name="p2025341125211"></a><a name="p2025341125211"></a>Specifies the result sorting order. The default value is <strong id="b11889552514"><a name="b11889552514"></a><a name="b11889552514"></a>desc</strong>.<a name="ul107075455529"></a><a name="ul107075455529"></a><ul id="ul107075455529"><li><strong id="b73126714514"><a name="b73126714514"></a><a name="b73126714514"></a>desc</strong>: specifies the descending order.</li><li><strong id="b927011820511"><a name="b927011820511"></a><a name="b927011820511"></a>asc</strong>: specifies the ascending order.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="en-us_topic_0058762430_row1669400215294"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762430_p19336748152914"><a name="en-us_topic_0058762430_p19336748152914"></a><a name="en-us_topic_0058762430_p19336748152914"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762430_p22139675153443"><a name="en-us_topic_0058762430_p22139675153443"></a><a name="en-us_topic_0058762430_p22139675153443"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762430_p32652321152914"><a name="en-us_topic_0058762430_p32652321152914"></a><a name="en-us_topic_0058762430_p32652321152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="p02247913491"><a name="p02247913491"></a><a name="p02247913491"></a>Specifies the offset.</p>
    <p id="en-us_topic_0058762430_p27592310152914"><a name="en-us_topic_0058762430_p27592310152914"></a><a name="en-us_topic_0058762430_p27592310152914"></a>All disks after this offset will be queried. The value must be an integer greater than 0 but less than the number of disks.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762430_row4150243115292"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762430_p49243814152914"><a name="en-us_topic_0058762430_p49243814152914"></a><a name="en-us_topic_0058762430_p49243814152914"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762430_p15960789153343"><a name="en-us_topic_0058762430_p15960789153343"></a><a name="en-us_topic_0058762430_p15960789153343"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762430_p26598214152914"><a name="en-us_topic_0058762430_p26598214152914"></a><a name="en-us_topic_0058762430_p26598214152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0058762430_p6971702152914"><a name="en-us_topic_0058762430_p6971702152914"></a><a name="en-us_topic_0058762430_p6971702152914"></a>Specifies the disk status. For details, see <a href="evs-disk-status.md">EVS Disk Status</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762430_row33130210152857"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762430_p49206403152914"><a name="en-us_topic_0058762430_p49206403152914"></a><a name="en-us_topic_0058762430_p49206403152914"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762430_p6448822153343"><a name="en-us_topic_0058762430_p6448822153343"></a><a name="en-us_topic_0058762430_p6448822153343"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762430_p49578561152914"><a name="en-us_topic_0058762430_p49578561152914"></a><a name="en-us_topic_0058762430_p49578561152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0058762430_p56440503152914"><a name="en-us_topic_0058762430_p56440503152914"></a><a name="en-us_topic_0058762430_p56440503152914"></a>Specifies the disk metadata.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762430_row20664390152531"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762430_p7393147152914"><a name="en-us_topic_0058762430_p7393147152914"></a><a name="en-us_topic_0058762430_p7393147152914"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762430_p59504247153343"><a name="en-us_topic_0058762430_p59504247153343"></a><a name="en-us_topic_0058762430_p59504247153343"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762430_p53841259152914"><a name="en-us_topic_0058762430_p53841259152914"></a><a name="en-us_topic_0058762430_p53841259152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0058762430_p66174752152914"><a name="en-us_topic_0058762430_p66174752152914"></a><a name="en-us_topic_0058762430_p66174752152914"></a>Specifies the AZ.</p>
    </td>
    </tr>
    <tr id="row6313218203319"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="p555112711331"><a name="p555112711331"></a><a name="p555112711331"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="p9551927163312"><a name="p9551927163312"></a><a name="p9551927163312"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="p13551152715338"><a name="p13551152715338"></a><a name="p13551152715338"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="p2066824720366"><a name="p2066824720366"></a><a name="p2066824720366"></a>Specifies whether the query result contains system disks. The values are as follows:</p>
    <a name="ul10404210173715"></a><a name="ul10404210173715"></a><ul id="ul10404210173715"><li><strong id="b84235270611643"><a name="b84235270611643"></a><a name="b84235270611643"></a>True</strong>, <strong id="b84235270611646"><a name="b84235270611646"></a><a name="b84235270611646"></a>true</strong>, and <strong id="b84235270611648"><a name="b84235270611648"></a><a name="b84235270611648"></a>1</strong>: The query result contains system disks only.</li><li><strong id="b84235270611738"><a name="b84235270611738"></a><a name="b84235270611738"></a>False</strong>, <strong id="b84235270611740"><a name="b84235270611740"></a><a name="b84235270611740"></a>false</strong>, and <strong id="b84235270611746"><a name="b84235270611746"></a><a name="b84235270611746"></a>0</strong>: The query result does not contain system disks.</li></ul>
    <p id="p1555132715333"><a name="p1555132715333"></a><a name="p1555132715333"></a>This parameter is supported when the request version is 3.2 or later.</p>
    </td>
    </tr>
    <tr id="row4314161817332"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="p75521327113313"><a name="p75521327113313"></a><a name="p75521327113313"></a>migration_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="p655282715338"><a name="p655282715338"></a><a name="p655282715338"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="p14552122793312"><a name="p14552122793312"></a><a name="p14552122793312"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="p6552122783310"><a name="p6552122783310"></a><a name="p6552122783310"></a>Specifies the migration status. The value can be <strong id="b84235270618289"><a name="b84235270618289"></a><a name="b84235270618289"></a>starting</strong>, <strong id="b842352706182812"><a name="b842352706182812"></a><a name="b842352706182812"></a>migrating</strong>, <strong id="b842352706182815"><a name="b842352706182815"></a><a name="b842352706182815"></a>success</strong>, or <strong id="b842352706182821"><a name="b842352706182821"></a><a name="b842352706182821"></a>error</strong>.</p>
    </td>
    </tr>
    <tr id="row3314218173316"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="p1355262793315"><a name="p1355262793315"></a><a name="p1355262793315"></a>name~</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="p15552102720334"><a name="p15552102720334"></a><a name="p15552102720334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="p12552102719334"><a name="p12552102719334"></a><a name="p12552102719334"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="p11552182715331"><a name="p11552182715331"></a><a name="p11552182715331"></a>Specifies the fuzzy search by disk name. This parameter is supported when the request version is 3.31 or later.</p>
    </td>
    </tr>
    <tr id="row531419184331"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="p555232714335"><a name="p555232714335"></a><a name="p555232714335"></a>status~</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="p11553122753313"><a name="p11553122753313"></a><a name="p11553122753313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="p1955322717338"><a name="p1955322717338"></a><a name="p1955322717338"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="p25531427163315"><a name="p25531427163315"></a><a name="p25531427163315"></a>Specifies the fuzzy search by disk status. This parameter is supported when the request version is 3.31 or later.</p>
    </td>
    </tr>
    <tr id="row1631421833317"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="p13553122718335"><a name="p13553122718335"></a><a name="p13553122718335"></a>availability_zone~</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="p19553327153317"><a name="p19553327153317"></a><a name="p19553327153317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="p955392711337"><a name="p955392711337"></a><a name="p955392711337"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="p155362723314"><a name="p155362723314"></a><a name="p155362723314"></a>Specifies the fuzzy search by AZ. This parameter is supported when the request version is 3.31 or later.</p>
    </td>
    </tr>
    <tr id="row9315171810335"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="p16553112711338"><a name="p16553112711338"></a><a name="p16553112711338"></a>migration_status~</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="p1255322763313"><a name="p1255322763313"></a><a name="p1255322763313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="p855362710335"><a name="p855362710335"></a><a name="p855362710335"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="p45541272332"><a name="p45541272332"></a><a name="p45541272332"></a>Specifies the fuzzy search by migration status. This parameter is supported when the request version is 3.31 or later.</p>
    </td>
    </tr>
    <tr id="row17315718133316"><td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.1 "><p id="p155547276337"><a name="p155547276337"></a><a name="p155547276337"></a>with_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.1.5.1.2 "><p id="p855442773311"><a name="p855442773311"></a><a name="p855442773311"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="p1055420271339"><a name="p1055420271339"></a><a name="p1055420271339"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="p355419276334"><a name="p355419276334"></a><a name="p355419276334"></a>Specifies to return parameter <strong id="b842352706111032"><a name="b842352706111032"></a><a name="b842352706111032"></a>counts</strong> in the response. This parameter indicates the number of disks queried. This parameter is in the <em id="i842352697111123"><a name="i842352697111123"></a><a name="i842352697111123"></a>with_count=true</em> format and is supported when the request version is 3.45 or later.</p>
    <p id="p13551640195317"><a name="p13551640195317"></a><a name="p13551640195317"></a>This parameter can be used together with parameters <strong id="b842352706155655"><a name="b842352706155655"></a><a name="b842352706155655"></a>marker</strong>, <strong id="b842352706155659"><a name="b842352706155659"></a><a name="b842352706155659"></a>limit</strong>, <strong id="b84235270615572"><a name="b84235270615572"></a><a name="b84235270615572"></a>sort_key</strong>, <strong id="b84235270615576"><a name="b84235270615576"></a><a name="b84235270615576"></a>sort_dir</strong>, or <strong id="b842352706155718"><a name="b842352706155718"></a><a name="b842352706155718"></a>offset</strong> in the table. It cannot be used with other filter parameters.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section45527389"></a>

The following example shows how to query the disks in the  **available**  state.

-   Example request

    ```
    GET https://{endpoint}/v3/{project_id}/volumes?status=available
    ```


## Response<a name="section7093323"></a>

-   Parameter description

    <a name="table47135197203"></a>
    <table><thead align="left"><tr id="row1971411197206"><th class="cellrowborder" valign="top" width="21.52%" id="mcps1.1.4.1.1"><p id="p18714119102015"><a name="p18714119102015"></a><a name="p18714119102015"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.34%" id="mcps1.1.4.1.2"><p id="p2714171962013"><a name="p2714171962013"></a><a name="p2714171962013"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p1971411912014"><a name="p1971411912014"></a><a name="p1971411912014"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10714519142015"><td class="cellrowborder" valign="top" width="21.52%" headers="mcps1.1.4.1.1 "><p id="p171411918201"><a name="p171411918201"></a><a name="p171411918201"></a>volumes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.34%" headers="mcps1.1.4.1.2 "><p id="p471441982010"><a name="p471441982010"></a><a name="p471441982010"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p177147197207"><a name="p177147197207"></a><a name="p177147197207"></a>Specifies the list of queried disks. For details, see <a href="#en-us_topic_0058762430_li3451542201439">Parameters in the volumes field</a>.</p>
    </td>
    </tr>
    <tr id="row971541982016"><td class="cellrowborder" valign="top" width="21.52%" headers="mcps1.1.4.1.1 "><p id="p1715219112015"><a name="p1715219112015"></a><a name="p1715219112015"></a>volumes_links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.34%" headers="mcps1.1.4.1.2 "><p id="p157151719152012"><a name="p157151719152012"></a><a name="p157151719152012"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p671511199201"><a name="p671511199201"></a><a name="p671511199201"></a>Specifies the query position marker in the disk list. If only some disks are returned in this query, the URL of the last disk queried will be returned. You can use this URL to continue to query the remaining disks in the next query.</p>
    </td>
    </tr>
    <tr id="row14715719102010"><td class="cellrowborder" valign="top" width="21.52%" headers="mcps1.1.4.1.1 "><p id="p10715141942016"><a name="p10715141942016"></a><a name="p10715141942016"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.34%" headers="mcps1.1.4.1.2 "><p id="p1366719501195"><a name="p1366719501195"></a><a name="p1366719501195"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p37151919162013"><a name="p37151919162013"></a><a name="p37151919162013"></a>Specifies the number of records returned in this query.</p>
    </td>
    </tr>
    <tr id="row1294462562116"><td class="cellrowborder" valign="top" width="21.52%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.34%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="en-us_topic_0058762430_li3451542201439"></a>Parameters in the  **volumes**  field

    <a name="en-us_topic_0058762430_table34701445142557"></a>
    <table><thead align="left"><tr id="en-us_topic_0058762430_row12524911142557"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="en-us_topic_0058762430_p7884856142557"><a name="en-us_topic_0058762430_p7884856142557"></a><a name="en-us_topic_0058762430_p7884856142557"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="en-us_topic_0058762430_p34693598142557"><a name="en-us_topic_0058762430_p34693598142557"></a><a name="en-us_topic_0058762430_p34693598142557"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="en-us_topic_0058762430_p58539486142557"><a name="en-us_topic_0058762430_p58539486142557"></a><a name="en-us_topic_0058762430_p58539486142557"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0058762430_row444782011610"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762430_p9640386153059"><a name="en-us_topic_0058762430_p9640386153059"></a><a name="en-us_topic_0058762430_p9640386153059"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762430_p42673774153059"><a name="en-us_topic_0058762430_p42673774153059"></a><a name="en-us_topic_0058762430_p42673774153059"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762430_p4455949153059"><a name="en-us_topic_0058762430_p4455949153059"></a><a name="en-us_topic_0058762430_p4455949153059"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762430_row44077962142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762430_p27161806153059"><a name="en-us_topic_0058762430_p27161806153059"></a><a name="en-us_topic_0058762430_p27161806153059"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762430_p52622641153059"><a name="en-us_topic_0058762430_p52622641153059"></a><a name="en-us_topic_0058762430_p52622641153059"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762430_p49157451153059"><a name="en-us_topic_0058762430_p49157451153059"></a><a name="en-us_topic_0058762430_p49157451153059"></a>Specifies the disk URI. For details, see <a href="#en-us_topic_0058762430_li1077125119136">Parameters in the links field</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762430_row16186817142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762430_p66757462153059"><a name="en-us_topic_0058762430_p66757462153059"></a><a name="en-us_topic_0058762430_p66757462153059"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762430_p38645307153059"><a name="en-us_topic_0058762430_p38645307153059"></a><a name="en-us_topic_0058762430_p38645307153059"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762430_p14572483153059"><a name="en-us_topic_0058762430_p14572483153059"></a><a name="en-us_topic_0058762430_p14572483153059"></a>Specifies the disk name. <span id="text1081494105183234"><a name="text1081494105183234"></a><a name="text1081494105183234"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="en-us_topic_0058762430_li1077125119136"></a>Parameters in the  **links**  field

    <a name="en-us_topic_0058762430_en-us_topic_0058762429_table24355024185927"></a>
    <table><thead align="left"><tr id="en-us_topic_0058762430_en-us_topic_0058762429_row16225418185927"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="en-us_topic_0058762430_en-us_topic_0058762429_p39190461185927"><a name="en-us_topic_0058762430_en-us_topic_0058762429_p39190461185927"></a><a name="en-us_topic_0058762430_en-us_topic_0058762429_p39190461185927"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="en-us_topic_0058762430_en-us_topic_0058762429_p20310744185927"><a name="en-us_topic_0058762430_en-us_topic_0058762429_p20310744185927"></a><a name="en-us_topic_0058762430_en-us_topic_0058762429_p20310744185927"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.330000000000005%" id="mcps1.1.4.1.3"><p id="en-us_topic_0058762430_en-us_topic_0058762429_p47699944185927"><a name="en-us_topic_0058762430_en-us_topic_0058762429_p47699944185927"></a><a name="en-us_topic_0058762430_en-us_topic_0058762429_p47699944185927"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0058762430_en-us_topic_0058762429_row38490285185927"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762430_en-us_topic_0058762429_p30705403185927"><a name="en-us_topic_0058762430_en-us_topic_0058762429_p30705403185927"></a><a name="en-us_topic_0058762430_en-us_topic_0058762429_p30705403185927"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762430_en-us_topic_0058762429_p4109689185927"><a name="en-us_topic_0058762430_en-us_topic_0058762429_p4109689185927"></a><a name="en-us_topic_0058762430_en-us_topic_0058762429_p4109689185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762430_en-us_topic_0058762429_p53015590185927"><a name="en-us_topic_0058762430_en-us_topic_0058762429_p53015590185927"></a><a name="en-us_topic_0058762430_en-us_topic_0058762429_p53015590185927"></a>Specifies the corresponding shortcut link.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0058762430_en-us_topic_0058762429_row7378265185927"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0058762430_en-us_topic_0058762429_p60768596185927"><a name="en-us_topic_0058762430_en-us_topic_0058762429_p60768596185927"></a><a name="en-us_topic_0058762430_en-us_topic_0058762429_p60768596185927"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0058762430_en-us_topic_0058762429_p23309219185927"><a name="en-us_topic_0058762430_en-us_topic_0058762429_p23309219185927"></a><a name="en-us_topic_0058762430_en-us_topic_0058762429_p23309219185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0058762430_en-us_topic_0058762429_p57795935185927"><a name="en-us_topic_0058762430_en-us_topic_0058762429_p57795935185927"></a><a name="en-us_topic_0058762430_en-us_topic_0058762429_p57795935185927"></a>Specifies the shortcut link marker name.</p>
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
        "count": 3, 
        "volumes": [
            {
                "id": "6b604cef-9bd8-4f5a-ae56-45839e6e1f0a", 
                "links": [
                    {
                        "href": "https://volume.localdomain.com:8776/v2/dd14c6ac581f40059e27f5320b60bf2f/volumes/6b604cef-9bd8-4f5a-ae56-45839e6e1f0a", 
                        "rel": "self"
                    }, 
                    {
                        "href": "https://volume.localdomain.com:8776/dd14c6ac581f40059e27f5320b60bf2f/volumes/6b604cef-9bd8-4f5a-ae56-45839e6e1f0a", 
                        "rel": "bookmark"
                    }
                ], 
                "name": "zjb_u25_test"
            }, 
            {
                "id": "2bce4552-9a7d-48fa-8484-abbbf64b206e", 
                "links": [
                    {
                        "href": "https://volume.localdomain.com:8776/v2/dd14c6ac581f40059e27f5320b60bf2f/volumes/2bce4552-9a7d-48fa-8484-abbbf64b206e", 
                        "rel": "self"
                    }, 
                    {
                        "href": "https://volume.localdomain.com:8776/dd14c6ac581f40059e27f5320b60bf2f/volumes/2bce4552-9a7d-48fa-8484-abbbf64b206e", 
                        "rel": "bookmark"
                    }
                ], 
                "name": "zjb_u25_test"
            }, 
            {
                "id": "3f1b98ec-a8b5-4e92-a727-88def62d5ad3", 
                "links": [
                    {
                        "href": "https://volume.localdomain.com:8776/v2/dd14c6ac581f40059e27f5320b60bf2f/volumes/3f1b98ec-a8b5-4e92-a727-88def62d5ad3", 
                        "rel": "self"
                    }, 
                    {
                        "href": "https://volume.localdomain.com:8776/dd14c6ac581f40059e27f5320b60bf2f/volumes/3f1b98ec-a8b5-4e92-a727-88def62d5ad3", 
                        "rel": "bookmark"
                    }
                ], 
                "name": "zjb_u25_test"
            }
        ], 
        "volumes_links": [
            {
                "href": "https://volume.localdomain.com:8776/v2/dd14c6ac581f40059e27f5320b60bf2f/volumes?limit=3&marker=3f1b98ec-a8b5-4e92-a727-88def62d5ad3", 
                "rel": "next"
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

    In the preceding example,  **error**  indicates a general error, for example,  **badRequest**  or  **itemNotFound**. An example is provided as follows:

    ```
    { 
        "badRequest": { 
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

