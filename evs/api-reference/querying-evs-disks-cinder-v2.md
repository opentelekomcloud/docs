# Querying EVS Disks<a name="evs_04_2068"></a>

## Function<a name="section60214390"></a>

This API is used to query EVS disks.

## URI<a name="section5058598"></a>

-   URI format

    GET /v2/\{project\_id\}/volumes

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

    <a name="table48630339152531"></a>
    <table><thead align="left"><tr id="row30502978152531"><th class="cellrowborder" valign="top" width="17.599999999999998%" id="mcps1.1.5.1.1"><p id="p54822134152531"><a name="p54822134152531"></a><a name="p54822134152531"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.54%" id="mcps1.1.5.1.2"><p id="p11407863152531"><a name="p11407863152531"></a><a name="p11407863152531"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.05%" id="mcps1.1.5.1.3"><p id="p51621676152531"><a name="p51621676152531"></a><a name="p51621676152531"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.809999999999995%" id="mcps1.1.5.1.4"><p id="p20606205152531"><a name="p20606205152531"></a><a name="p20606205152531"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row58489940152531"><td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.1.5.1.1 "><p id="p49168107152914"><a name="p49168107152914"></a><a name="p49168107152914"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.2 "><p id="p23193765152914"><a name="p23193765152914"></a><a name="p23193765152914"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.1.5.1.3 "><p id="p66755704152914"><a name="p66755704152914"></a><a name="p66755704152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.809999999999995%" headers="mcps1.1.5.1.4 "><p id="p38502923152914"><a name="p38502923152914"></a><a name="p38502923152914"></a><span id="text138882914373"><a name="text138882914373"></a><a name="text138882914373"></a>Specifies the ID of the last record on the previous page. The returned value is the value of the item after this one.</span></p>
    </td>
    </tr>
    <tr id="row38948343152859"><td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.1.5.1.1 "><p id="p17125818152914"><a name="p17125818152914"></a><a name="p17125818152914"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.2 "><p id="p14491527153320"><a name="p14491527153320"></a><a name="p14491527153320"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.1.5.1.3 "><p id="p22259725152914"><a name="p22259725152914"></a><a name="p22259725152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.809999999999995%" headers="mcps1.1.5.1.4 "><p id="p58207321152914"><a name="p58207321152914"></a><a name="p58207321152914"></a>Specifies the disk name. <span id="text256503808201536"><a name="text256503808201536"></a><a name="text256503808201536"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="row61932754152911"><td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.1.5.1.1 "><p id="p20335623152914"><a name="p20335623152914"></a><a name="p20335623152914"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.2 "><p id="p36572733152914"><a name="p36572733152914"></a><a name="p36572733152914"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.1.5.1.3 "><p id="p9601396152914"><a name="p9601396152914"></a><a name="p9601396152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.809999999999995%" headers="mcps1.1.5.1.4 "><p id="p39515603152914"><a name="p39515603152914"></a><a name="p39515603152914"></a>Specifies the maximum number of query results that can be returned.</p>
    <p id="p99431755191418"><a name="p99431755191418"></a><a name="p99431755191418"></a><span id="text138349551887"><a name="text138349551887"></a><a name="text138349551887"></a>The value ranges from 1 to 1000, and the default value is 1000. The returned value cannot exceed this limit.</span></p>
    <p id="p14657115572511"><a name="p14657115572511"></a><a name="p14657115572511"></a>If the tenant has more than 50 disks in total, you are advised to use this parameter and set its value to <strong id="b8423527069161"><a name="b8423527069161"></a><a name="b8423527069161"></a>50</strong> to improve the query efficiency. Examples are provided as follows:</p>
    <p id="p1233994321914"><a name="p1233994321914"></a><a name="p1233994321914"></a><strong id="b9984595891811"><a name="b9984595891811"></a><a name="b9984595891811"></a>GET /v2/</strong><em id="i40797784691811"><a name="i40797784691811"></a><a name="i40797784691811"></a>xxx</em><strong id="b172149191991811"><a name="b172149191991811"></a><a name="b172149191991811"></a>/volumes?limit=50</strong>: Queries the 1–50 disks. <strong id="b842352706102346"><a name="b842352706102346"></a><a name="b842352706102346"></a>GET /v2/</strong><em id="i587306121102343"><a name="i587306121102343"></a><a name="i587306121102343"></a>xxx</em><strong id="b842352706102351"><a name="b842352706102351"></a><a name="b842352706102351"></a>/volumes?offset=50&amp;limit=50</strong>: Queries the 51–100 disks.</p>
    </td>
    </tr>
    <tr id="row4561665015299"><td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.1.5.1.1 "><p id="p17172513152914"><a name="p17172513152914"></a><a name="p17172513152914"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.2 "><p id="p43305182153332"><a name="p43305182153332"></a><a name="p43305182153332"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.1.5.1.3 "><p id="p60186269152914"><a name="p60186269152914"></a><a name="p60186269152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.809999999999995%" headers="mcps1.1.5.1.4 "><p id="p43249593152914"><a name="p43249593152914"></a><a name="p43249593152914"></a>Specifies the keyword based on which the returned results are sorted. The value can be <strong id="b4477124205215"><a name="b4477124205215"></a><a name="b4477124205215"></a>id</strong>, <strong id="b8481162412525"><a name="b8481162412525"></a><a name="b8481162412525"></a>status</strong>, <strong id="b154811824125212"><a name="b154811824125212"></a><a name="b154811824125212"></a>size</strong>, or <strong id="b104821244522"><a name="b104821244522"></a><a name="b104821244522"></a>created_at</strong>, and the default value is <strong id="b4482182418529"><a name="b4482182418529"></a><a name="b4482182418529"></a>created_at</strong>.</p>
    </td>
    </tr>
    <tr id="row5831630415296"><td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.1.5.1.1 "><p id="p54896674152914"><a name="p54896674152914"></a><a name="p54896674152914"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.2 "><p id="p4460297153338"><a name="p4460297153338"></a><a name="p4460297153338"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.1.5.1.3 "><p id="p3809857152914"><a name="p3809857152914"></a><a name="p3809857152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.809999999999995%" headers="mcps1.1.5.1.4 "><div class="p" id="p2025341125211"><a name="p2025341125211"></a><a name="p2025341125211"></a>Specifies the result sorting order. The default value is <strong id="b194631533125210"><a name="b194631533125210"></a><a name="b194631533125210"></a>desc</strong>.<a name="ul107075455529"></a><a name="ul107075455529"></a><ul id="ul107075455529"><li><strong id="b154772344529"><a name="b154772344529"></a><a name="b154772344529"></a>desc</strong>: indicates the descending order.</li><li><strong id="b139815359524"><a name="b139815359524"></a><a name="b139815359524"></a>asc</strong>: indicates the ascending order.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row1669400215294"><td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.1.5.1.1 "><p id="p19336748152914"><a name="p19336748152914"></a><a name="p19336748152914"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.2 "><p id="p22139675153443"><a name="p22139675153443"></a><a name="p22139675153443"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.1.5.1.3 "><p id="p32652321152914"><a name="p32652321152914"></a><a name="p32652321152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.809999999999995%" headers="mcps1.1.5.1.4 "><p id="p1812219549521"><a name="p1812219549521"></a><a name="p1812219549521"></a>Specifies the offset.</p>
    <p id="p27592310152914"><a name="p27592310152914"></a><a name="p27592310152914"></a>All disks after this offset will be queried. The value must be an integer greater than 0 but less than the number of disks.</p>
    </td>
    </tr>
    <tr id="row4150243115292"><td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.1.5.1.1 "><p id="p49243814152914"><a name="p49243814152914"></a><a name="p49243814152914"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.2 "><p id="p15960789153343"><a name="p15960789153343"></a><a name="p15960789153343"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.1.5.1.3 "><p id="p26598214152914"><a name="p26598214152914"></a><a name="p26598214152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.809999999999995%" headers="mcps1.1.5.1.4 "><p id="p6971702152914"><a name="p6971702152914"></a><a name="p6971702152914"></a>Specifies the disk status. For details, see <a href="evs-disk-status.md">EVS Disk Status</a>.</p>
    </td>
    </tr>
    <tr id="row33130210152857"><td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.1.5.1.1 "><p id="p49206403152914"><a name="p49206403152914"></a><a name="p49206403152914"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.2 "><p id="p6448822153343"><a name="p6448822153343"></a><a name="p6448822153343"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.1.5.1.3 "><p id="p49578561152914"><a name="p49578561152914"></a><a name="p49578561152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.809999999999995%" headers="mcps1.1.5.1.4 "><p id="p56440503152914"><a name="p56440503152914"></a><a name="p56440503152914"></a>Specifies the disk metadata.</p>
    </td>
    </tr>
    <tr id="row20664390152531"><td class="cellrowborder" valign="top" width="17.599999999999998%" headers="mcps1.1.5.1.1 "><p id="p7393147152914"><a name="p7393147152914"></a><a name="p7393147152914"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.1.5.1.2 "><p id="p59504247153343"><a name="p59504247153343"></a><a name="p59504247153343"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.1.5.1.3 "><p id="p53841259152914"><a name="p53841259152914"></a><a name="p53841259152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.809999999999995%" headers="mcps1.1.5.1.4 "><p id="p66174752152914"><a name="p66174752152914"></a><a name="p66174752152914"></a>Specifies the AZ.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section45527389"></a>

The following example shows how to query the disks in the  **available**  state.

-   Example request

    ```
    GET https://{endpoint}/v2/{project_id}/volumes?status=available
    ```


## Response<a name="section7093323"></a>

-   Parameter description

    <a name="table682710305552"></a>
    <table><thead align="left"><tr id="row18828730125511"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="p17828103014554"><a name="p17828103014554"></a><a name="p17828103014554"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="p982813025513"><a name="p982813025513"></a><a name="p982813025513"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p10828123085512"><a name="p10828123085512"></a><a name="p10828123085512"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6828153014554"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p1828130105513"><a name="p1828130105513"></a><a name="p1828130105513"></a>volumes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p582813013559"><a name="p582813013559"></a><a name="p582813013559"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p158281930195514"><a name="p158281930195514"></a><a name="p158281930195514"></a>Specifies the list of queried disks. For details, see <a href="#li3451542201439">Parameters in the volumes field</a>.</p>
    </td>
    </tr>
    <tr id="row16651711135716"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p20139619153059"><a name="p20139619153059"></a><a name="p20139619153059"></a>volumes_links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p20696419153059"><a name="p20696419153059"></a><a name="p20696419153059"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p27977197153059"><a name="p27977197153059"></a><a name="p27977197153059"></a>Specifies the query position marker in the disk list. If only some disks are returned in this query, the URL of the last disk queried will be returned. You can use this URL to continue to query the remaining disks in the next query.</p>
    </td>
    </tr>
    <tr id="row1383518379555"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li3451542201439"></a>Parameters in the  **volumes**  field

    <a name="table34701445142557"></a>
    <table><thead align="left"><tr id="row12524911142557"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="p7884856142557"><a name="p7884856142557"></a><a name="p7884856142557"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="p34693598142557"><a name="p34693598142557"></a><a name="p34693598142557"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p58539486142557"><a name="p58539486142557"></a><a name="p58539486142557"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row444782011610"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p9640386153059"><a name="p9640386153059"></a><a name="p9640386153059"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p42673774153059"><a name="p42673774153059"></a><a name="p42673774153059"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p4455949153059"><a name="p4455949153059"></a><a name="p4455949153059"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="row44077962142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p27161806153059"><a name="p27161806153059"></a><a name="p27161806153059"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p52622641153059"><a name="p52622641153059"></a><a name="p52622641153059"></a>list&lt;map&lt;String, String&gt;&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p49157451153059"><a name="p49157451153059"></a><a name="p49157451153059"></a>Specifies the disk URI. For details, see <a href="#li1077125119136">Parameters in the links field</a>.</p>
    </td>
    </tr>
    <tr id="row16186817142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p66757462153059"><a name="p66757462153059"></a><a name="p66757462153059"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p38645307153059"><a name="p38645307153059"></a><a name="p38645307153059"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p14572483153059"><a name="p14572483153059"></a><a name="p14572483153059"></a>Specifies the disk name. <span id="text416107395201549"><a name="text416107395201549"></a><a name="text416107395201549"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li1077125119136"></a>Parameters in the  **links**  field

    <a name="evs_04_2067_table24355024185927"></a>
    <table><thead align="left"><tr id="evs_04_2067_row16225418185927"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="evs_04_2067_p39190461185927"><a name="evs_04_2067_p39190461185927"></a><a name="evs_04_2067_p39190461185927"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="evs_04_2067_p20310744185927"><a name="evs_04_2067_p20310744185927"></a><a name="evs_04_2067_p20310744185927"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.330000000000005%" id="mcps1.1.4.1.3"><p id="evs_04_2067_p47699944185927"><a name="evs_04_2067_p47699944185927"></a><a name="evs_04_2067_p47699944185927"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2067_row38490285185927"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p30705403185927"><a name="evs_04_2067_p30705403185927"></a><a name="evs_04_2067_p30705403185927"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p4109689185927"><a name="evs_04_2067_p4109689185927"></a><a name="evs_04_2067_p4109689185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p53015590185927"><a name="evs_04_2067_p53015590185927"></a><a name="evs_04_2067_p53015590185927"></a>Specifies the corresponding shortcut link.</p>
    </td>
    </tr>
    <tr id="evs_04_2067_row7378265185927"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p60768596185927"><a name="evs_04_2067_p60768596185927"></a><a name="evs_04_2067_p60768596185927"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p23309219185927"><a name="evs_04_2067_p23309219185927"></a><a name="evs_04_2067_p23309219185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p57795935185927"><a name="evs_04_2067_p57795935185927"></a><a name="evs_04_2067_p57795935185927"></a>Specifies the shortcut link marker name.</p>
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

