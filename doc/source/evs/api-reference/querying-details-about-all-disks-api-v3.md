# Querying Details About All Disks<a name="evs_04_3004"></a>

## Function<a name="section60214390"></a>

This API is used to query details about all disks.

## URI<a name="section5058598"></a>

-   URI format

    GET /v3/\{project\_id\}/os-vendor-volumes/detail

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

    <a name="evs_04_2010_table48630339152531"></a>
    <table><thead align="left"><tr id="evs_04_2010_row30502978152531"><th class="cellrowborder" valign="top" width="17.5982401759824%" id="mcps1.1.5.1.1"><p id="evs_04_2010_p54822134152531"><a name="evs_04_2010_p54822134152531"></a><a name="evs_04_2010_p54822134152531"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.798420157984202%" id="mcps1.1.5.1.2"><p id="evs_04_2010_p11407863152531"><a name="evs_04_2010_p11407863152531"></a><a name="evs_04_2010_p11407863152531"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.418258174182583%" id="mcps1.1.5.1.3"><p id="evs_04_2010_p51621676152531"><a name="evs_04_2010_p51621676152531"></a><a name="evs_04_2010_p51621676152531"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.185081491850816%" id="mcps1.1.5.1.4"><p id="evs_04_2010_p20606205152531"><a name="evs_04_2010_p20606205152531"></a><a name="evs_04_2010_p20606205152531"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2010_row58489940152531"><td class="cellrowborder" valign="top" width="17.5982401759824%" headers="mcps1.1.5.1.1 "><p id="evs_04_2010_p49168107152914"><a name="evs_04_2010_p49168107152914"></a><a name="evs_04_2010_p49168107152914"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.798420157984202%" headers="mcps1.1.5.1.2 "><p id="evs_04_2010_p23193765152914"><a name="evs_04_2010_p23193765152914"></a><a name="evs_04_2010_p23193765152914"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.418258174182583%" headers="mcps1.1.5.1.3 "><p id="evs_04_2010_p66755704152914"><a name="evs_04_2010_p66755704152914"></a><a name="evs_04_2010_p66755704152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.185081491850816%" headers="mcps1.1.5.1.4 "><p id="evs_04_2010_p38502923152914"><a name="evs_04_2010_p38502923152914"></a><a name="evs_04_2010_p38502923152914"></a><span id="evs_04_2010_text1348145625919"><a name="evs_04_2010_text1348145625919"></a><a name="evs_04_2010_text1348145625919"></a>Specifies the ID of the last record on the previous page. The returned value is the value of the item after this one.</span></p>
    </td>
    </tr>
    <tr id="evs_04_2010_row38948343152859"><td class="cellrowborder" valign="top" width="17.5982401759824%" headers="mcps1.1.5.1.1 "><p id="evs_04_2010_p17125818152914"><a name="evs_04_2010_p17125818152914"></a><a name="evs_04_2010_p17125818152914"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.798420157984202%" headers="mcps1.1.5.1.2 "><p id="evs_04_2010_p14491527153320"><a name="evs_04_2010_p14491527153320"></a><a name="evs_04_2010_p14491527153320"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.418258174182583%" headers="mcps1.1.5.1.3 "><p id="evs_04_2010_p22259725152914"><a name="evs_04_2010_p22259725152914"></a><a name="evs_04_2010_p22259725152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.185081491850816%" headers="mcps1.1.5.1.4 "><p id="evs_04_2010_p58207321152914"><a name="evs_04_2010_p58207321152914"></a><a name="evs_04_2010_p58207321152914"></a>Specifies the disk name. <span id="evs_04_2010_text37302935152245"><a name="evs_04_2010_text37302935152245"></a><a name="evs_04_2010_text37302935152245"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="evs_04_2010_row61932754152911"><td class="cellrowborder" valign="top" width="17.5982401759824%" headers="mcps1.1.5.1.1 "><p id="evs_04_2010_p20335623152914"><a name="evs_04_2010_p20335623152914"></a><a name="evs_04_2010_p20335623152914"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.798420157984202%" headers="mcps1.1.5.1.2 "><p id="evs_04_2010_p36572733152914"><a name="evs_04_2010_p36572733152914"></a><a name="evs_04_2010_p36572733152914"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.418258174182583%" headers="mcps1.1.5.1.3 "><p id="evs_04_2010_p9601396152914"><a name="evs_04_2010_p9601396152914"></a><a name="evs_04_2010_p9601396152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.185081491850816%" headers="mcps1.1.5.1.4 "><p id="evs_04_2010_p39515603152914"><a name="evs_04_2010_p39515603152914"></a><a name="evs_04_2010_p39515603152914"></a>Specifies the maximum number of query results that can be returned.</p>
    <p id="evs_04_2010_p2642143814912"><a name="evs_04_2010_p2642143814912"></a><a name="evs_04_2010_p2642143814912"></a><span id="evs_04_2010_text138349551887"><a name="evs_04_2010_text138349551887"></a><a name="evs_04_2010_text138349551887"></a>The value ranges from 1 to 1000, and the default value is 1000. The returned value cannot exceed this limit.</span></p>
    </td>
    </tr>
    <tr id="evs_04_2010_row4561665015299"><td class="cellrowborder" valign="top" width="17.5982401759824%" headers="mcps1.1.5.1.1 "><p id="evs_04_2010_p17172513152914"><a name="evs_04_2010_p17172513152914"></a><a name="evs_04_2010_p17172513152914"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.798420157984202%" headers="mcps1.1.5.1.2 "><p id="evs_04_2010_p43305182153332"><a name="evs_04_2010_p43305182153332"></a><a name="evs_04_2010_p43305182153332"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.418258174182583%" headers="mcps1.1.5.1.3 "><p id="evs_04_2010_p60186269152914"><a name="evs_04_2010_p60186269152914"></a><a name="evs_04_2010_p60186269152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.185081491850816%" headers="mcps1.1.5.1.4 "><p id="evs_04_2010_p43249593152914"><a name="evs_04_2010_p43249593152914"></a><a name="evs_04_2010_p43249593152914"></a>Specifies the keyword based on which the returned results are sorted. The value can be <strong id="evs_04_2010_b842352706101941"><a name="evs_04_2010_b842352706101941"></a><a name="evs_04_2010_b842352706101941"></a>id</strong>, <strong id="evs_04_2010_b842352706101934"><a name="evs_04_2010_b842352706101934"></a><a name="evs_04_2010_b842352706101934"></a>status</strong>, <strong id="evs_04_2010_b842352706101930"><a name="evs_04_2010_b842352706101930"></a><a name="evs_04_2010_b842352706101930"></a>size</strong>, or <strong id="evs_04_2010_b842352706101927"><a name="evs_04_2010_b842352706101927"></a><a name="evs_04_2010_b842352706101927"></a>created_at</strong>, and the default value is <strong id="evs_04_2010_b2063116951191130"><a name="evs_04_2010_b2063116951191130"></a><a name="evs_04_2010_b2063116951191130"></a>created_at</strong>.</p>
    </td>
    </tr>
    <tr id="evs_04_2010_row5831630415296"><td class="cellrowborder" valign="top" width="17.5982401759824%" headers="mcps1.1.5.1.1 "><p id="evs_04_2010_p54896674152914"><a name="evs_04_2010_p54896674152914"></a><a name="evs_04_2010_p54896674152914"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.798420157984202%" headers="mcps1.1.5.1.2 "><p id="evs_04_2010_p4460297153338"><a name="evs_04_2010_p4460297153338"></a><a name="evs_04_2010_p4460297153338"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.418258174182583%" headers="mcps1.1.5.1.3 "><p id="evs_04_2010_p3809857152914"><a name="evs_04_2010_p3809857152914"></a><a name="evs_04_2010_p3809857152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.185081491850816%" headers="mcps1.1.5.1.4 "><p id="evs_04_2010_p40162964152914"><a name="evs_04_2010_p40162964152914"></a><a name="evs_04_2010_p40162964152914"></a>Specifies the result sorting order. The default value is <strong id="evs_04_2010_b911545915227"><a name="evs_04_2010_b911545915227"></a><a name="evs_04_2010_b911545915227"></a>desc</strong>.</p>
    <a name="evs_04_2010_ul329874211485"></a><a name="evs_04_2010_ul329874211485"></a><ul id="evs_04_2010_ul329874211485"><li><strong id="evs_04_2010_b842352706143516"><a name="evs_04_2010_b842352706143516"></a><a name="evs_04_2010_b842352706143516"></a>desc</strong>: indicates the descending order.</li><li><strong id="evs_04_2010_b84235270614353"><a name="evs_04_2010_b84235270614353"></a><a name="evs_04_2010_b84235270614353"></a>asc</strong>: indicates the ascending order.</li></ul>
    </td>
    </tr>
    <tr id="evs_04_2010_row1669400215294"><td class="cellrowborder" valign="top" width="17.5982401759824%" headers="mcps1.1.5.1.1 "><p id="evs_04_2010_p19336748152914"><a name="evs_04_2010_p19336748152914"></a><a name="evs_04_2010_p19336748152914"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.798420157984202%" headers="mcps1.1.5.1.2 "><p id="evs_04_2010_p22139675153443"><a name="evs_04_2010_p22139675153443"></a><a name="evs_04_2010_p22139675153443"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.418258174182583%" headers="mcps1.1.5.1.3 "><p id="evs_04_2010_p32652321152914"><a name="evs_04_2010_p32652321152914"></a><a name="evs_04_2010_p32652321152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.185081491850816%" headers="mcps1.1.5.1.4 "><p id="evs_04_2010_p27592310152914"><a name="evs_04_2010_p27592310152914"></a><a name="evs_04_2010_p27592310152914"></a>Specifies the offset. All disks after this offset will be queried. The value must be an integer greater than 0 but less than the number of disks.</p>
    </td>
    </tr>
    <tr id="evs_04_2010_row4150243115292"><td class="cellrowborder" valign="top" width="17.5982401759824%" headers="mcps1.1.5.1.1 "><p id="evs_04_2010_p49243814152914"><a name="evs_04_2010_p49243814152914"></a><a name="evs_04_2010_p49243814152914"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.798420157984202%" headers="mcps1.1.5.1.2 "><p id="evs_04_2010_p15960789153343"><a name="evs_04_2010_p15960789153343"></a><a name="evs_04_2010_p15960789153343"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.418258174182583%" headers="mcps1.1.5.1.3 "><p id="evs_04_2010_p26598214152914"><a name="evs_04_2010_p26598214152914"></a><a name="evs_04_2010_p26598214152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.185081491850816%" headers="mcps1.1.5.1.4 "><p id="evs_04_2010_p6971702152914"><a name="evs_04_2010_p6971702152914"></a><a name="evs_04_2010_p6971702152914"></a>Specifies the disk status. For details, see <a href="evs-disk-status.md">EVS Disk Status</a>.</p>
    </td>
    </tr>
    <tr id="evs_04_2010_row33130210152857"><td class="cellrowborder" valign="top" width="17.5982401759824%" headers="mcps1.1.5.1.1 "><p id="evs_04_2010_p49206403152914"><a name="evs_04_2010_p49206403152914"></a><a name="evs_04_2010_p49206403152914"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.798420157984202%" headers="mcps1.1.5.1.2 "><p id="evs_04_2010_p6448822153343"><a name="evs_04_2010_p6448822153343"></a><a name="evs_04_2010_p6448822153343"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.418258174182583%" headers="mcps1.1.5.1.3 "><p id="evs_04_2010_p49578561152914"><a name="evs_04_2010_p49578561152914"></a><a name="evs_04_2010_p49578561152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.185081491850816%" headers="mcps1.1.5.1.4 "><p id="evs_04_2010_p56440503152914"><a name="evs_04_2010_p56440503152914"></a><a name="evs_04_2010_p56440503152914"></a>Specifies the disk metadata.</p>
    </td>
    </tr>
    <tr id="evs_04_2010_row20664390152531"><td class="cellrowborder" valign="top" width="17.5982401759824%" headers="mcps1.1.5.1.1 "><p id="evs_04_2010_p7393147152914"><a name="evs_04_2010_p7393147152914"></a><a name="evs_04_2010_p7393147152914"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.798420157984202%" headers="mcps1.1.5.1.2 "><p id="evs_04_2010_p59504247153343"><a name="evs_04_2010_p59504247153343"></a><a name="evs_04_2010_p59504247153343"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.418258174182583%" headers="mcps1.1.5.1.3 "><p id="evs_04_2010_p53841259152914"><a name="evs_04_2010_p53841259152914"></a><a name="evs_04_2010_p53841259152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.185081491850816%" headers="mcps1.1.5.1.4 "><p id="evs_04_2010_p66174752152914"><a name="evs_04_2010_p66174752152914"></a><a name="evs_04_2010_p66174752152914"></a>Specifies the AZ to which the disk belongs.</p>
    </td>
    </tr>
    <tr id="evs_04_2010_row433212398420"><td class="cellrowborder" valign="top" width="17.5982401759824%" headers="mcps1.1.5.1.1 "><p id="evs_04_2010_p1441713429428"><a name="evs_04_2010_p1441713429428"></a><a name="evs_04_2010_p1441713429428"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.798420157984202%" headers="mcps1.1.5.1.2 "><p id="evs_04_2010_p1541984214429"><a name="evs_04_2010_p1541984214429"></a><a name="evs_04_2010_p1541984214429"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.418258174182583%" headers="mcps1.1.5.1.3 "><p id="evs_04_2010_p18419174234210"><a name="evs_04_2010_p18419174234210"></a><a name="evs_04_2010_p18419174234210"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.185081491850816%" headers="mcps1.1.5.1.4 "><div class="p" id="evs_04_2010_p16419144210429"><a name="evs_04_2010_p16419144210429"></a><a name="evs_04_2010_p16419144210429"></a>Specifies whether the disk is shareable.<a name="evs_04_2010_ul202952187368"></a><a name="evs_04_2010_ul202952187368"></a><ul id="evs_04_2010_ul202952187368"><li><strong id="evs_04_2010_b129131333763"><a name="evs_04_2010_b129131333763"></a><a name="evs_04_2010_b129131333763"></a>true</strong>: specifies a shared disk.</li><li><strong id="evs_04_2010_b22446368610"><a name="evs_04_2010_b22446368610"></a><a name="evs_04_2010_b22446368610"></a>false</strong>: specifies a non-shared disk.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="evs_04_2010_row176903519453"><td class="cellrowborder" valign="top" width="17.5982401759824%" headers="mcps1.1.5.1.1 "><p id="evs_04_2010_p1857152194612"><a name="evs_04_2010_p1857152194612"></a><a name="evs_04_2010_p1857152194612"></a>dedicated_storage_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.798420157984202%" headers="mcps1.1.5.1.2 "><p id="evs_04_2010_p18571162124611"><a name="evs_04_2010_p18571162124611"></a><a name="evs_04_2010_p18571162124611"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.418258174182583%" headers="mcps1.1.5.1.3 "><p id="evs_04_2010_p857120219462"><a name="evs_04_2010_p857120219462"></a><a name="evs_04_2010_p857120219462"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.185081491850816%" headers="mcps1.1.5.1.4 "><p id="evs_04_2010_p1857162154615"><a name="evs_04_2010_p1857162154615"></a><a name="evs_04_2010_p1857162154615"></a>Specifies the ID of the DSS storage pool. All disks in the DSS storage pool can be filtered out. Only precise match is supported.</p>
    </td>
    </tr>
    <tr id="evs_04_2010_row10814055174517"><td class="cellrowborder" valign="top" width="17.5982401759824%" headers="mcps1.1.5.1.1 "><p id="evs_04_2010_p125717218464"><a name="evs_04_2010_p125717218464"></a><a name="evs_04_2010_p125717218464"></a>dedicated_storage_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.798420157984202%" headers="mcps1.1.5.1.2 "><p id="evs_04_2010_p157110213469"><a name="evs_04_2010_p157110213469"></a><a name="evs_04_2010_p157110213469"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.418258174182583%" headers="mcps1.1.5.1.3 "><p id="evs_04_2010_p1557117211469"><a name="evs_04_2010_p1557117211469"></a><a name="evs_04_2010_p1557117211469"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.185081491850816%" headers="mcps1.1.5.1.4 "><p id="evs_04_2010_p2057114211466"><a name="evs_04_2010_p2057114211466"></a><a name="evs_04_2010_p2057114211466"></a>Specifies the name of the DSS storage pool. All disks in the DSS storage pool can be filtered out. Fuzzy match is supported.</p>
    </td>
    </tr>
    <tr id="evs_04_2010_row1484019429236"><td class="cellrowborder" valign="top" width="17.5982401759824%" headers="mcps1.1.5.1.1 "><p id="evs_04_2010_p4338154142317"><a name="evs_04_2010_p4338154142317"></a><a name="evs_04_2010_p4338154142317"></a>volume_type_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.798420157984202%" headers="mcps1.1.5.1.2 "><p id="evs_04_2010_p193381354122315"><a name="evs_04_2010_p193381354122315"></a><a name="evs_04_2010_p193381354122315"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.418258174182583%" headers="mcps1.1.5.1.3 "><p id="evs_04_2010_p3338754132315"><a name="evs_04_2010_p3338754132315"></a><a name="evs_04_2010_p3338754132315"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.185081491850816%" headers="mcps1.1.5.1.4 "><p id="evs_04_2010_p3338155422319"><a name="evs_04_2010_p3338155422319"></a><a name="evs_04_2010_p3338155422319"></a>Specifies the disk type ID.</p>
    </td>
    </tr>
    <tr id="evs_04_2010_row1758151163616"><td class="cellrowborder" valign="top" width="17.5982401759824%" headers="mcps1.1.5.1.1 "><p id="evs_04_2010_p85819112362"><a name="evs_04_2010_p85819112362"></a><a name="evs_04_2010_p85819112362"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.798420157984202%" headers="mcps1.1.5.1.2 "><p id="evs_04_2010_p75815112367"><a name="evs_04_2010_p75815112367"></a><a name="evs_04_2010_p75815112367"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.418258174182583%" headers="mcps1.1.5.1.3 "><p id="evs_04_2010_p3581911193617"><a name="evs_04_2010_p3581911193617"></a><a name="evs_04_2010_p3581911193617"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.185081491850816%" headers="mcps1.1.5.1.4 "><p id="evs_04_2010_p45812118360"><a name="evs_04_2010_p45812118360"></a><a name="evs_04_2010_p45812118360"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="evs_04_2010_row3113151415129"><td class="cellrowborder" valign="top" width="17.5982401759824%" headers="mcps1.1.5.1.1 "><p id="evs_04_2010_p11113121412125"><a name="evs_04_2010_p11113121412125"></a><a name="evs_04_2010_p11113121412125"></a>ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.798420157984202%" headers="mcps1.1.5.1.2 "><p id="evs_04_2010_p1811371412124"><a name="evs_04_2010_p1811371412124"></a><a name="evs_04_2010_p1811371412124"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.418258174182583%" headers="mcps1.1.5.1.3 "><p id="evs_04_2010_p9113191413128"><a name="evs_04_2010_p9113191413128"></a><a name="evs_04_2010_p9113191413128"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.185081491850816%" headers="mcps1.1.5.1.4 "><p id="evs_04_2010_p7651828190"><a name="evs_04_2010_p7651828190"></a><a name="evs_04_2010_p7651828190"></a>Specifies the disk IDs. The parameter value is in the <em id="evs_04_2010_i842352697194353"><a name="evs_04_2010_i842352697194353"></a><a name="evs_04_2010_i842352697194353"></a>ids=['id1','id2',...,'idx']</em> format. In the response, the <strong id="evs_04_2010_b842352706111955"><a name="evs_04_2010_b842352706111955"></a><a name="evs_04_2010_b842352706111955"></a>ids</strong> value contains valid disk IDs only. Invalid disk IDs will be ignored.</p>
    <p id="evs_04_2010_p2640155471814"><a name="evs_04_2010_p2640155471814"></a><a name="evs_04_2010_p2640155471814"></a>Details about a maximum of 60 disks can be queried.</p>
    <p id="evs_04_2010_p649163291315"><a name="evs_04_2010_p649163291315"></a><a name="evs_04_2010_p649163291315"></a>If parameters <strong id="evs_04_2010_b84235270611260"><a name="evs_04_2010_b84235270611260"></a><a name="evs_04_2010_b84235270611260"></a>id</strong> and <strong id="evs_04_2010_b84235270611263"><a name="evs_04_2010_b84235270611263"></a><a name="evs_04_2010_b84235270611263"></a>ids</strong> are both specified in the request, <strong id="evs_04_2010_b842352706112623"><a name="evs_04_2010_b842352706112623"></a><a name="evs_04_2010_b842352706112623"></a>id</strong> will be ignored.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section50413755"></a>

The following example shows how to query the shared disks in the  **available**  state.

-   Example request

    ```
    GET https://{endpoint}/v3/{project_id}/os-vendor-volumes/detail?status=available&multiattach=true
    ```


## Response<a name="section7902226102914"></a>

-   Parameter description

    <a name="en-us_topic_0098680634_table34701445142557"></a>
    <table><thead align="left"><tr id="en-us_topic_0098680634_row12524911142557"><th class="cellrowborder" valign="top" width="18.82%" id="mcps1.1.4.1.1"><p id="en-us_topic_0098680634_p7884856142557"><a name="en-us_topic_0098680634_p7884856142557"></a><a name="en-us_topic_0098680634_p7884856142557"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.53%" id="mcps1.1.4.1.2"><p id="en-us_topic_0098680634_p34693598142557"><a name="en-us_topic_0098680634_p34693598142557"></a><a name="en-us_topic_0098680634_p34693598142557"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.65%" id="mcps1.1.4.1.3"><p id="en-us_topic_0098680634_p58539486142557"><a name="en-us_topic_0098680634_p58539486142557"></a><a name="en-us_topic_0098680634_p58539486142557"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0098680634_row42521635152937"><td class="cellrowborder" valign="top" width="18.82%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p14844956152939"><a name="en-us_topic_0098680634_p14844956152939"></a><a name="en-us_topic_0098680634_p14844956152939"></a>volumes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.53%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p61590812152939"><a name="en-us_topic_0098680634_p61590812152939"></a><a name="en-us_topic_0098680634_p61590812152939"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p34852014152939"><a name="en-us_topic_0098680634_p34852014152939"></a><a name="en-us_topic_0098680634_p34852014152939"></a>Specifies the list of queried disks. For details, see <a href="#li6938526142910">Parameters in the volumes field</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row15981815184017"><td class="cellrowborder" valign="top" width="18.82%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p16197151919407"><a name="en-us_topic_0098680634_p16197151919407"></a><a name="en-us_topic_0098680634_p16197151919407"></a>volumes_links</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.53%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p12197151915402"><a name="en-us_topic_0098680634_p12197151915402"></a><a name="en-us_topic_0098680634_p12197151915402"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p17197141954017"><a name="en-us_topic_0098680634_p17197141954017"></a><a name="en-us_topic_0098680634_p17197141954017"></a>Specifies the query position marker in the disk list. If only some disks are returned in this query, the URL of the last disk queried will be returned. You can use this URL to continue to query the remaining disks in the next query. For details, see <a href="#li497317268296">Parameters in the links field</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row444782011610"><td class="cellrowborder" valign="top" width="18.82%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p0730182411511"><a name="en-us_topic_0098680634_p0730182411511"></a><a name="en-us_topic_0098680634_p0730182411511"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.53%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p1573092465118"><a name="en-us_topic_0098680634_p1573092465118"></a><a name="en-us_topic_0098680634_p1573092465118"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p10730152455119"><a name="en-us_topic_0098680634_p10730152455119"></a><a name="en-us_topic_0098680634_p10730152455119"></a>Specifies the number of queried disks. This value is not affected by the pagination.</p>
    </td>
    </tr>
    <tr id="row862173712912"><td class="cellrowborder" valign="top" width="18.82%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p129522216412"><a name="en-us_topic_0098680634_p129522216412"></a><a name="en-us_topic_0098680634_p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.53%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p1595262111415"><a name="en-us_topic_0098680634_p1595262111415"></a><a name="en-us_topic_0098680634_p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p109527215417"><a name="en-us_topic_0098680634_p109527215417"></a><a name="en-us_topic_0098680634_p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li6938526142910"></a>Parameters in the  **volumes**  field

    <a name="en-us_topic_0098680634_table9519314115310"></a>
    <table><thead align="left"><tr id="en-us_topic_0098680634_row07772014165315"><th class="cellrowborder" valign="top" width="20.1%" id="mcps1.1.4.1.1"><p id="en-us_topic_0098680634_p977791416537"><a name="en-us_topic_0098680634_p977791416537"></a><a name="en-us_topic_0098680634_p977791416537"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.43%" id="mcps1.1.4.1.2"><p id="en-us_topic_0098680634_p1777191445316"><a name="en-us_topic_0098680634_p1777191445316"></a><a name="en-us_topic_0098680634_p1777191445316"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.47%" id="mcps1.1.4.1.3"><p id="en-us_topic_0098680634_p9894141375614"><a name="en-us_topic_0098680634_p9894141375614"></a><a name="en-us_topic_0098680634_p9894141375614"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0098680634_row157775141539"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p1577716144532"><a name="en-us_topic_0098680634_p1577716144532"></a><a name="en-us_topic_0098680634_p1577716144532"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p2077712145534"><a name="en-us_topic_0098680634_p2077712145534"></a><a name="en-us_topic_0098680634_p2077712145534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p577711405310"><a name="en-us_topic_0098680634_p577711405310"></a><a name="en-us_topic_0098680634_p577711405310"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row197771014165318"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p1777771465312"><a name="en-us_topic_0098680634_p1777771465312"></a><a name="en-us_topic_0098680634_p1777771465312"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p1577781445313"><a name="en-us_topic_0098680634_p1577781445313"></a><a name="en-us_topic_0098680634_p1577781445313"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p377719149537"><a name="en-us_topic_0098680634_p377719149537"></a><a name="en-us_topic_0098680634_p377719149537"></a>Specifies the disk URI. For details, see <a href="#li497317268296">Parameters in the links field</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row14777131435317"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p677751415313"><a name="en-us_topic_0098680634_p677751415313"></a><a name="en-us_topic_0098680634_p677751415313"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p7777614185310"><a name="en-us_topic_0098680634_p7777614185310"></a><a name="en-us_topic_0098680634_p7777614185310"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p977716143532"><a name="en-us_topic_0098680634_p977716143532"></a><a name="en-us_topic_0098680634_p977716143532"></a>Specifies the disk name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row377719149532"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p17777714195313"><a name="en-us_topic_0098680634_p17777714195313"></a><a name="en-us_topic_0098680634_p17777714195313"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p17771514195316"><a name="en-us_topic_0098680634_p17771514195316"></a><a name="en-us_topic_0098680634_p17771514195316"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p137771014165316"><a name="en-us_topic_0098680634_p137771014165316"></a><a name="en-us_topic_0098680634_p137771014165316"></a>Specifies the disk status. For details, see <a href="evs-disk-status.md">EVS Disk Status</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row1577714145535"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p8777171445317"><a name="en-us_topic_0098680634_p8777171445317"></a><a name="en-us_topic_0098680634_p8777171445317"></a>attachments</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p14777161435318"><a name="en-us_topic_0098680634_p14777161435318"></a><a name="en-us_topic_0098680634_p14777161435318"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p1977761417532"><a name="en-us_topic_0098680634_p1977761417532"></a><a name="en-us_topic_0098680634_p1977761417532"></a>Specifies the disk attachment information. For details, see <a href="#li14979192617290">Parameters in the attachments field</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row137779149535"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p7777614155317"><a name="en-us_topic_0098680634_p7777614155317"></a><a name="en-us_topic_0098680634_p7777614155317"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p977731415320"><a name="en-us_topic_0098680634_p977731415320"></a><a name="en-us_topic_0098680634_p977731415320"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p1577710143534"><a name="en-us_topic_0098680634_p1577710143534"></a><a name="en-us_topic_0098680634_p1577710143534"></a>Specifies the AZ to which the disk belongs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row577741415319"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p16777171425319"><a name="en-us_topic_0098680634_p16777171425319"></a><a name="en-us_topic_0098680634_p16777171425319"></a>os-vol-host-attr:host</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p8777201414538"><a name="en-us_topic_0098680634_p8777201414538"></a><a name="en-us_topic_0098680634_p8777201414538"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p1677701445318"><a name="en-us_topic_0098680634_p1677701445318"></a><a name="en-us_topic_0098680634_p1677701445318"></a><span id="text61531054125615"><a name="text61531054125615"></a><a name="text61531054125615"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row19777171445315"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p13777914155316"><a name="en-us_topic_0098680634_p13777914155316"></a><a name="en-us_topic_0098680634_p13777914155316"></a>source_volid</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p9777101475310"><a name="en-us_topic_0098680634_p9777101475310"></a><a name="en-us_topic_0098680634_p9777101475310"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p97771314105319"><a name="en-us_topic_0098680634_p97771314105319"></a><a name="en-us_topic_0098680634_p97771314105319"></a>Specifies the source disk ID. This parameter has a value if the disk is created from a source disk.</p>
    <p id="p102771156662"><a name="p102771156662"></a><a name="p102771156662"></a><span id="text88578719717"><a name="text88578719717"></a><a name="text88578719717"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row1577751412539"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p10777201435317"><a name="en-us_topic_0098680634_p10777201435317"></a><a name="en-us_topic_0098680634_p10777201435317"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p87771614125315"><a name="en-us_topic_0098680634_p87771614125315"></a><a name="en-us_topic_0098680634_p87771614125315"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p877714143532"><a name="en-us_topic_0098680634_p877714143532"></a><a name="en-us_topic_0098680634_p877714143532"></a>Specifies the snapshot ID. This parameter has a value if the disk is created from a snapshot.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row7777114155318"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p8777151410534"><a name="en-us_topic_0098680634_p8777151410534"></a><a name="en-us_topic_0098680634_p8777151410534"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p17778191485311"><a name="en-us_topic_0098680634_p17778191485311"></a><a name="en-us_topic_0098680634_p17778191485311"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p3778181416532"><a name="en-us_topic_0098680634_p3778181416532"></a><a name="en-us_topic_0098680634_p3778181416532"></a>Specifies the disk description.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row67785148537"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p277810146537"><a name="en-us_topic_0098680634_p277810146537"></a><a name="en-us_topic_0098680634_p277810146537"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p3778141415318"><a name="en-us_topic_0098680634_p3778141415318"></a><a name="en-us_topic_0098680634_p3778141415318"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p47781314105312"><a name="en-us_topic_0098680634_p47781314105312"></a><a name="en-us_topic_0098680634_p47781314105312"></a>Specifies the time when the disk was created.</p>
    <p id="en-us_topic_0098680634_p20997172813263"><a name="en-us_topic_0098680634_p20997172813263"></a><a name="en-us_topic_0098680634_p20997172813263"></a><span id="en-us_topic_0098680634_text17996183912613"><a name="en-us_topic_0098680634_text17996183912613"></a><a name="en-us_topic_0098680634_text17996183912613"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row67781214105315"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p377811416530"><a name="en-us_topic_0098680634_p377811416530"></a><a name="en-us_topic_0098680634_p377811416530"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p0778131415310"><a name="en-us_topic_0098680634_p0778131415310"></a><a name="en-us_topic_0098680634_p0778131415310"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p47786148539"><a name="en-us_topic_0098680634_p47786148539"></a><a name="en-us_topic_0098680634_p47786148539"></a>Specifies the disk type.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row137786149533"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p14778214185315"><a name="en-us_topic_0098680634_p14778214185315"></a><a name="en-us_topic_0098680634_p14778214185315"></a>os-vol-tenant-attr:tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p19778514175310"><a name="en-us_topic_0098680634_p19778514175310"></a><a name="en-us_topic_0098680634_p19778514175310"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p1677871415318"><a name="en-us_topic_0098680634_p1677871415318"></a><a name="en-us_topic_0098680634_p1677871415318"></a>Specifies the ID of the tenant to which the disk belongs. <span id="text19941457165313"><a name="text19941457165313"></a><a name="text19941457165313"></a>The tenant ID is actually the project ID.</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row18778181445315"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p12778114205320"><a name="en-us_topic_0098680634_p12778114205320"></a><a name="en-us_topic_0098680634_p12778114205320"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p18778141414532"><a name="en-us_topic_0098680634_p18778141414532"></a><a name="en-us_topic_0098680634_p18778141414532"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p2778614165317"><a name="en-us_topic_0098680634_p2778614165317"></a><a name="en-us_topic_0098680634_p2778614165317"></a>Specifies the disk size, in GB.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row19778191410534"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p6778101415532"><a name="en-us_topic_0098680634_p6778101415532"></a><a name="en-us_topic_0098680634_p6778101415532"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p17788145537"><a name="en-us_topic_0098680634_p17788145537"></a><a name="en-us_topic_0098680634_p17788145537"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p1778814165312"><a name="en-us_topic_0098680634_p1778814165312"></a><a name="en-us_topic_0098680634_p1778814165312"></a>Specifies the disk metadata. For details, see <a href="#li4145283210319">Parameters in the metadata field</a>.</p>
    <p id="en-us_topic_0098680634_p87781014105314"><a name="en-us_topic_0098680634_p87781014105314"></a><a name="en-us_topic_0098680634_p87781014105314"></a>If <strong id="b842352706192015"><a name="b842352706192015"></a><a name="b842352706192015"></a>metadata</strong> does not contain the <strong id="b842352706143434"><a name="b842352706143434"></a><a name="b842352706143434"></a>hw:passthrough</strong> field, the disk device type is VBD.</p>
    <p id="en-us_topic_0098680634_p137786148534"><a name="en-us_topic_0098680634_p137786148534"></a><a name="en-us_topic_0098680634_p137786148534"></a>If <strong id="b842352706192028"><a name="b842352706192028"></a><a name="b842352706192028"></a>metadata</strong> does not contain the <strong id="b842352706143455"><a name="b842352706143455"></a><a name="b842352706143455"></a>__system__encrypted</strong> field, the disk is not encrypted.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row877851418537"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p17778214105317"><a name="en-us_topic_0098680634_p17778214105317"></a><a name="en-us_topic_0098680634_p17778214105317"></a>os-vol-mig-status-attr:migstat</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p177891485319"><a name="en-us_topic_0098680634_p177891485319"></a><a name="en-us_topic_0098680634_p177891485319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p978016142531"><a name="en-us_topic_0098680634_p978016142531"></a><a name="en-us_topic_0098680634_p978016142531"></a><span id="text203605127103"><a name="text203605127103"></a><a name="text203605127103"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row1278081415531"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p17780101425317"><a name="en-us_topic_0098680634_p17780101425317"></a><a name="en-us_topic_0098680634_p17780101425317"></a>os-vol-mig-status-attr:name_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p47801514165310"><a name="en-us_topic_0098680634_p47801514165310"></a><a name="en-us_topic_0098680634_p47801514165310"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p278041410539"><a name="en-us_topic_0098680634_p278041410539"></a><a name="en-us_topic_0098680634_p278041410539"></a><span id="text1664319572108"><a name="text1664319572108"></a><a name="text1664319572108"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row7780171418539"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p978017142534"><a name="en-us_topic_0098680634_p978017142534"></a><a name="en-us_topic_0098680634_p978017142534"></a>os-volume-replication:extended_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p12780191455320"><a name="en-us_topic_0098680634_p12780191455320"></a><a name="en-us_topic_0098680634_p12780191455320"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p278051495317"><a name="en-us_topic_0098680634_p278051495317"></a><a name="en-us_topic_0098680634_p278051495317"></a><span id="text13411355121016"><a name="text13411355121016"></a><a name="text13411355121016"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row15780614195318"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p47452553185118"><a name="en-us_topic_0098680634_p47452553185118"></a><a name="en-us_topic_0098680634_p47452553185118"></a>encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p18451581185118"><a name="en-us_topic_0098680634_p18451581185118"></a><a name="en-us_topic_0098680634_p18451581185118"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p27951625185124"><a name="en-us_topic_0098680634_p27951625185124"></a><a name="en-us_topic_0098680634_p27951625185124"></a><span id="en-us_topic_0098680634_text141191141115618"><a name="en-us_topic_0098680634_text141191141115618"></a><a name="en-us_topic_0098680634_text141191141115618"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row778012145537"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p47806145531"><a name="en-us_topic_0098680634_p47806145531"></a><a name="en-us_topic_0098680634_p47806145531"></a>replication_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p378051485319"><a name="en-us_topic_0098680634_p378051485319"></a><a name="en-us_topic_0098680634_p378051485319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p1478011145538"><a name="en-us_topic_0098680634_p1478011145538"></a><a name="en-us_topic_0098680634_p1478011145538"></a><span id="text6498181171119"><a name="text6498181171119"></a><a name="text6498181171119"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row127801014115315"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p1780101435315"><a name="en-us_topic_0098680634_p1780101435315"></a><a name="en-us_topic_0098680634_p1780101435315"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p147803142534"><a name="en-us_topic_0098680634_p147803142534"></a><a name="en-us_topic_0098680634_p147803142534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p1780314115312"><a name="en-us_topic_0098680634_p1780314115312"></a><a name="en-us_topic_0098680634_p1780314115312"></a>Reserved field</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row478012147531"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p207801914195310"><a name="en-us_topic_0098680634_p207801914195310"></a><a name="en-us_topic_0098680634_p207801914195310"></a>consistencygroup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p57802014195314"><a name="en-us_topic_0098680634_p57802014195314"></a><a name="en-us_topic_0098680634_p57802014195314"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p478011417532"><a name="en-us_topic_0098680634_p478011417532"></a><a name="en-us_topic_0098680634_p478011417532"></a><span id="text13343838181111"><a name="text13343838181111"></a><a name="text13343838181111"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row5780814175319"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p117801414155319"><a name="en-us_topic_0098680634_p117801414155319"></a><a name="en-us_topic_0098680634_p117801414155319"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p18780121416536"><a name="en-us_topic_0098680634_p18780121416536"></a><a name="en-us_topic_0098680634_p18780121416536"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><div class="p" id="en-us_topic_0098680634_p8780414125315"><a name="en-us_topic_0098680634_p8780414125315"></a><a name="en-us_topic_0098680634_p8780414125315"></a>Specifies whether the disk is bootable.<a name="ul185931714111"></a><a name="ul185931714111"></a><ul id="ul185931714111"><li><strong id="b2087914016511"><a name="b2087914016511"></a><a name="b2087914016511"></a>true</strong>: specifies a bootable disk.</li><li><strong id="b11149315519"><a name="b11149315519"></a><a name="b11149315519"></a>false</strong>: specifies a non-bootable disk.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row18780121455311"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p1478018149536"><a name="en-us_topic_0098680634_p1478018149536"></a><a name="en-us_topic_0098680634_p1478018149536"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p1078151416531"><a name="en-us_topic_0098680634_p1078151416531"></a><a name="en-us_topic_0098680634_p1078151416531"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p178141465319"><a name="en-us_topic_0098680634_p178141465319"></a><a name="en-us_topic_0098680634_p178141465319"></a>Specifies the time when the disk was updated.</p>
    <p id="en-us_topic_0098680634_p134522013390"><a name="en-us_topic_0098680634_p134522013390"></a><a name="en-us_topic_0098680634_p134522013390"></a><span id="text5297134511122"><a name="text5297134511122"></a><a name="text5297134511122"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row1578113141536"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p1578191419531"><a name="en-us_topic_0098680634_p1578191419531"></a><a name="en-us_topic_0098680634_p1578191419531"></a>shareable</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p378121416538"><a name="en-us_topic_0098680634_p378121416538"></a><a name="en-us_topic_0098680634_p378121416538"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p17811114125319"><a name="en-us_topic_0098680634_p17811114125319"></a><a name="en-us_topic_0098680634_p17811114125319"></a>Specifies whether the disk is shareable.</p>
    <div class="note" id="en-us_topic_0098680634_note3800959821323"><a name="en-us_topic_0098680634_note3800959821323"></a><a name="en-us_topic_0098680634_note3800959821323"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0098680634_p45212589213213"><a name="en-us_topic_0098680634_p45212589213213"></a><a name="en-us_topic_0098680634_p45212589213213"></a>This field is no longer used. Use <strong id="b16681781226"><a name="b16681781226"></a><a name="b16681781226"></a>multiattach</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row157811614145318"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p3781191418536"><a name="en-us_topic_0098680634_p3781191418536"></a><a name="en-us_topic_0098680634_p3781191418536"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p37812014135310"><a name="en-us_topic_0098680634_p37812014135310"></a><a name="en-us_topic_0098680634_p37812014135310"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><div class="p" id="en-us_topic_0098680634_p4781191416535"><a name="en-us_topic_0098680634_p4781191416535"></a><a name="en-us_topic_0098680634_p4781191416535"></a>Specifies whether the disk is shareable.<a name="ul161621719119"></a><a name="ul161621719119"></a><ul id="ul161621719119"><li><strong id="b38592404"><a name="b38592404"></a><a name="b38592404"></a>true</strong>: specifies a shared disk.</li><li><strong id="b1912927100"><a name="b1912927100"></a><a name="b1912927100"></a>false</strong>: specifies a non-shared disk.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row11781131475317"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p19781814165316"><a name="en-us_topic_0098680634_p19781814165316"></a><a name="en-us_topic_0098680634_p19781814165316"></a>volume_image_metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p5781314145311"><a name="en-us_topic_0098680634_p5781314145311"></a><a name="en-us_topic_0098680634_p5781314145311"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p15781414175316"><a name="en-us_topic_0098680634_p15781414175316"></a><a name="en-us_topic_0098680634_p15781414175316"></a>Specifies the metadata of the disk image. This field has a value if the disk is created from an image. Otherwise, it is left empty.</p>
    <div class="note" id="en-us_topic_0098680634_note410975220289"><a name="en-us_topic_0098680634_note410975220289"></a><a name="en-us_topic_0098680634_note410975220289"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0098680634_en-us_topic_0044524893_p1888154732118"><a name="en-us_topic_0098680634_en-us_topic_0044524893_p1888154732118"></a><a name="en-us_topic_0098680634_en-us_topic_0044524893_p1888154732118"></a>For details about <strong id="b84235270611295"><a name="b84235270611295"></a><a name="b84235270611295"></a>volume_image_metadata</strong>, see <strong id="b842352706112917"><a name="b842352706112917"></a><a name="b842352706112917"></a>Querying Image Details</strong> in the <em id="i842352697112925"><a name="i842352697112925"></a><a name="i842352697112925"></a>Image Management Service API Reference</em>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row1678151415535"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p12781121410537"><a name="en-us_topic_0098680634_p12781121410537"></a><a name="en-us_topic_0098680634_p12781121410537"></a>dedicated_storage_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p1278151417534"><a name="en-us_topic_0098680634_p1278151417534"></a><a name="en-us_topic_0098680634_p1278151417534"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p12781111465310"><a name="en-us_topic_0098680634_p12781111465310"></a><a name="en-us_topic_0098680634_p12781111465310"></a>Specifies the ID of the DSS storage pool accommodating the disk.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row16781161411537"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p1178131435314"><a name="en-us_topic_0098680634_p1178131435314"></a><a name="en-us_topic_0098680634_p1178131435314"></a>dedicated_storage_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p1478161475312"><a name="en-us_topic_0098680634_p1478161475312"></a><a name="en-us_topic_0098680634_p1478161475312"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p1781171475316"><a name="en-us_topic_0098680634_p1781171475316"></a><a name="en-us_topic_0098680634_p1781171475316"></a>Specifies the name of the DSS storage pool accommodating the disk.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row13766235174313"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p69881644104318"><a name="en-us_topic_0098680634_p69881644104318"></a><a name="en-us_topic_0098680634_p69881644104318"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p1198854414439"><a name="en-us_topic_0098680634_p1198854414439"></a><a name="en-us_topic_0098680634_p1198854414439"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p18988144418437"><a name="en-us_topic_0098680634_p18988144418437"></a><a name="en-us_topic_0098680634_p18988144418437"></a>Specifies the disk tags.</p>
    <p id="en-us_topic_0098680634_p898894418432"><a name="en-us_topic_0098680634_p898894418432"></a><a name="en-us_topic_0098680634_p898894418432"></a>This field has values if the disk has tags. Otherwise, it is left empty.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row73891538114311"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p149881344124319"><a name="en-us_topic_0098680634_p149881344124319"></a><a name="en-us_topic_0098680634_p149881344124319"></a>wwn</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p3988174494319"><a name="en-us_topic_0098680634_p3988174494319"></a><a name="en-us_topic_0098680634_p3988174494319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p6988244114313"><a name="en-us_topic_0098680634_p6988244114313"></a><a name="en-us_topic_0098680634_p6988244114313"></a>Specifies the unique identifier used when attaching the disk.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0098680634_row86151047729"><td class="cellrowborder" valign="top" width="20.1%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p39941261495"><a name="en-us_topic_0098680634_p39941261495"></a><a name="en-us_topic_0098680634_p39941261495"></a>enterprise_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p1499413644915"><a name="en-us_topic_0098680634_p1499413644915"></a><a name="en-us_topic_0098680634_p1499413644915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p35013964916"><a name="en-us_topic_0098680634_p35013964916"></a><a name="en-us_topic_0098680634_p35013964916"></a>Specifies the ID of the enterprise project associated with the disk.</p>
    <p id="en-us_topic_0098680634_p4355195619465"><a name="en-us_topic_0098680634_p4355195619465"></a><a name="en-us_topic_0098680634_p4355195619465"></a><span id="en-us_topic_0098680634_text7359175617461"><a name="en-us_topic_0098680634_text7359175617461"></a><a name="en-us_topic_0098680634_text7359175617461"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li497317268296"></a>Parameters in the  **links**  field

    <a name="evs_04_2010_evs_04_2067_table24355024185927"></a>
    <table><thead align="left"><tr id="evs_04_2010_evs_04_2067_row16225418185927"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="evs_04_2010_evs_04_2067_p39190461185927"><a name="evs_04_2010_evs_04_2067_p39190461185927"></a><a name="evs_04_2010_evs_04_2067_p39190461185927"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="evs_04_2010_evs_04_2067_p20310744185927"><a name="evs_04_2010_evs_04_2067_p20310744185927"></a><a name="evs_04_2010_evs_04_2067_p20310744185927"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.330000000000005%" id="mcps1.1.4.1.3"><p id="evs_04_2010_evs_04_2067_p47699944185927"><a name="evs_04_2010_evs_04_2067_p47699944185927"></a><a name="evs_04_2010_evs_04_2067_p47699944185927"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2010_evs_04_2067_row38490285185927"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_2010_evs_04_2067_p30705403185927"><a name="evs_04_2010_evs_04_2067_p30705403185927"></a><a name="evs_04_2010_evs_04_2067_p30705403185927"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2010_evs_04_2067_p4109689185927"><a name="evs_04_2010_evs_04_2067_p4109689185927"></a><a name="evs_04_2010_evs_04_2067_p4109689185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="evs_04_2010_evs_04_2067_p53015590185927"><a name="evs_04_2010_evs_04_2067_p53015590185927"></a><a name="evs_04_2010_evs_04_2067_p53015590185927"></a>Specifies the corresponding shortcut link.</p>
    </td>
    </tr>
    <tr id="evs_04_2010_evs_04_2067_row7378265185927"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_2010_evs_04_2067_p60768596185927"><a name="evs_04_2010_evs_04_2067_p60768596185927"></a><a name="evs_04_2010_evs_04_2067_p60768596185927"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2010_evs_04_2067_p23309219185927"><a name="evs_04_2010_evs_04_2067_p23309219185927"></a><a name="evs_04_2010_evs_04_2067_p23309219185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="evs_04_2010_evs_04_2067_p57795935185927"><a name="evs_04_2010_evs_04_2067_p57795935185927"></a><a name="evs_04_2010_evs_04_2067_p57795935185927"></a>Specifies the shortcut link marker name.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li14979192617290"></a>Parameters in the  **attachments**  field

    <a name="evs_04_2010_evs_04_2067_table6503386185927"></a>
    <table><thead align="left"><tr id="evs_04_2010_evs_04_2067_row1296819185927"><th class="cellrowborder" valign="top" width="21.18%" id="mcps1.1.4.1.1"><p id="evs_04_2010_evs_04_2067_p37933504185927"><a name="evs_04_2010_evs_04_2067_p37933504185927"></a><a name="evs_04_2010_evs_04_2067_p37933504185927"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.35%" id="mcps1.1.4.1.2"><p id="evs_04_2010_evs_04_2067_p52714965185927"><a name="evs_04_2010_evs_04_2067_p52714965185927"></a><a name="evs_04_2010_evs_04_2067_p52714965185927"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.47%" id="mcps1.1.4.1.3"><p id="evs_04_2010_evs_04_2067_p50913593185927"><a name="evs_04_2010_evs_04_2067_p50913593185927"></a><a name="evs_04_2010_evs_04_2067_p50913593185927"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2010_evs_04_2067_row30360408185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2010_evs_04_2067_p43274016185927"><a name="evs_04_2010_evs_04_2067_p43274016185927"></a><a name="evs_04_2010_evs_04_2067_p43274016185927"></a>server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2010_evs_04_2067_p15534392185927"><a name="evs_04_2010_evs_04_2067_p15534392185927"></a><a name="evs_04_2010_evs_04_2067_p15534392185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2010_evs_04_2067_p49891705185927"><a name="evs_04_2010_evs_04_2067_p49891705185927"></a><a name="evs_04_2010_evs_04_2067_p49891705185927"></a>Specifies the ID of the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="evs_04_2010_evs_04_2067_row49550172185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2010_evs_04_2067_p54141023185927"><a name="evs_04_2010_evs_04_2067_p54141023185927"></a><a name="evs_04_2010_evs_04_2067_p54141023185927"></a>attachment_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2010_evs_04_2067_p23346722185927"><a name="evs_04_2010_evs_04_2067_p23346722185927"></a><a name="evs_04_2010_evs_04_2067_p23346722185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2010_evs_04_2067_p35416329185927"><a name="evs_04_2010_evs_04_2067_p35416329185927"></a><a name="evs_04_2010_evs_04_2067_p35416329185927"></a>Specifies the ID of the attachment information.</p>
    </td>
    </tr>
    <tr id="evs_04_2010_evs_04_2067_row35650386185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2010_evs_04_2067_p2000176185927"><a name="evs_04_2010_evs_04_2067_p2000176185927"></a><a name="evs_04_2010_evs_04_2067_p2000176185927"></a>attached_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2010_evs_04_2067_p27796542185927"><a name="evs_04_2010_evs_04_2067_p27796542185927"></a><a name="evs_04_2010_evs_04_2067_p27796542185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2010_evs_04_2067_p38329099185927"><a name="evs_04_2010_evs_04_2067_p38329099185927"></a><a name="evs_04_2010_evs_04_2067_p38329099185927"></a>Specifies the time when the disk was attached.</p>
    <p id="evs_04_2010_evs_04_2067_p3414132514312"><a name="evs_04_2010_evs_04_2067_p3414132514312"></a><a name="evs_04_2010_evs_04_2067_p3414132514312"></a><span id="evs_04_2010_evs_04_2067_text7299269449"><a name="evs_04_2010_evs_04_2067_text7299269449"></a><a name="evs_04_2010_evs_04_2067_text7299269449"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="evs_04_2010_evs_04_2067_row9417574185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2010_evs_04_2067_p24626033185927"><a name="evs_04_2010_evs_04_2067_p24626033185927"></a><a name="evs_04_2010_evs_04_2067_p24626033185927"></a>host_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2010_evs_04_2067_p48551632185927"><a name="evs_04_2010_evs_04_2067_p48551632185927"></a><a name="evs_04_2010_evs_04_2067_p48551632185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2010_evs_04_2067_p48591276185927"><a name="evs_04_2010_evs_04_2067_p48591276185927"></a><a name="evs_04_2010_evs_04_2067_p48591276185927"></a>Specifies the name of the physical host accommodating the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="evs_04_2010_evs_04_2067_row34668301185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2010_evs_04_2067_p56668991185927"><a name="evs_04_2010_evs_04_2067_p56668991185927"></a><a name="evs_04_2010_evs_04_2067_p56668991185927"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2010_evs_04_2067_p26785545185927"><a name="evs_04_2010_evs_04_2067_p26785545185927"></a><a name="evs_04_2010_evs_04_2067_p26785545185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2010_evs_04_2067_p48959624185927"><a name="evs_04_2010_evs_04_2067_p48959624185927"></a><a name="evs_04_2010_evs_04_2067_p48959624185927"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="evs_04_2010_evs_04_2067_row41070280185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2010_evs_04_2067_p38358373185927"><a name="evs_04_2010_evs_04_2067_p38358373185927"></a><a name="evs_04_2010_evs_04_2067_p38358373185927"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2010_evs_04_2067_p20020490185927"><a name="evs_04_2010_evs_04_2067_p20020490185927"></a><a name="evs_04_2010_evs_04_2067_p20020490185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2010_evs_04_2067_p22392462185927"><a name="evs_04_2010_evs_04_2067_p22392462185927"></a><a name="evs_04_2010_evs_04_2067_p22392462185927"></a>Specifies the device name.</p>
    </td>
    </tr>
    <tr id="evs_04_2010_evs_04_2067_row205574185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2010_evs_04_2067_p16651565185927"><a name="evs_04_2010_evs_04_2067_p16651565185927"></a><a name="evs_04_2010_evs_04_2067_p16651565185927"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2010_evs_04_2067_p6599487185927"><a name="evs_04_2010_evs_04_2067_p6599487185927"></a><a name="evs_04_2010_evs_04_2067_p6599487185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2010_evs_04_2067_p14021450185927"><a name="evs_04_2010_evs_04_2067_p14021450185927"></a><a name="evs_04_2010_evs_04_2067_p14021450185927"></a>Specifies the ID of the attached resource.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li4145283210319"></a>Parameters in the  **metadata**  field

    <a name="table3430728295554"></a>
    <table><thead align="left"><tr id="row4496975195554"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="p8809200174410"><a name="p8809200174410"></a><a name="p8809200174410"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.62%" id="mcps1.1.4.1.2"><p id="p168135017449"><a name="p168135017449"></a><a name="p168135017449"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p1282213034412"><a name="p1282213034412"></a><a name="p1282213034412"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row456195295554"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p1562408795622"><a name="p1562408795622"></a><a name="p1562408795622"></a>__system__encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p5759155095622"><a name="p5759155095622"></a><a name="p5759155095622"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><div class="p" id="p177192813501"><a name="p177192813501"></a><a name="p177192813501"></a>Specifies the parameter that describes the encryption function in <strong id="b84235270614509"><a name="b84235270614509"></a><a name="b84235270614509"></a>metadata</strong>. The value can be <strong id="b842352706145015"><a name="b842352706145015"></a><a name="b842352706145015"></a>0</strong> or <strong id="b842352706145020"><a name="b842352706145020"></a><a name="b842352706145020"></a>1</strong>.<a name="ul141951225145011"></a><a name="ul141951225145011"></a><ul id="ul141951225145011"><li><strong id="b842352706145038"><a name="b842352706145038"></a><a name="b842352706145038"></a>0</strong>: indicates the disk is not encrypted.</li><li><strong id="b842352706145058"><a name="b842352706145058"></a><a name="b842352706145058"></a>1</strong>: indicates the disk is encrypted.</li><li>If this parameter does not appear, the disk is not encrypted by default.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row247050109562"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p241272995622"><a name="p241272995622"></a><a name="p241272995622"></a>__system__cmkid</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p6121338895622"><a name="p6121338895622"></a><a name="p6121338895622"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p4159804295622"><a name="p4159804295622"></a><a name="p4159804295622"></a>Specifies the parameter that describes the encryption CMK ID in <strong id="b84235270615116"><a name="b84235270615116"></a><a name="b84235270615116"></a>metadata</strong>. This parameter is used together with <strong id="b842352706143827"><a name="b842352706143827"></a><a name="b842352706143827"></a>__system__encrypted</strong> for encryption. The length of <strong id="b84235270614396"><a name="b84235270614396"></a><a name="b84235270614396"></a>cmkid</strong> is fixed at 36 bytes.</p>
    </td>
    </tr>
    <tr id="row60499086104915"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p1478896104915"><a name="p1478896104915"></a><a name="p1478896104915"></a>hw:passthrough</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p52681767104915"><a name="p52681767104915"></a><a name="p52681767104915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><div class="p" id="p17177177145116"><a name="p17177177145116"></a><a name="p17177177145116"></a>Specifies the parameter that describes the disk device type in <strong id="b84235270615173"><a name="b84235270615173"></a><a name="b84235270615173"></a>metadata</strong>. The value can be <strong id="b842352706151718"><a name="b842352706151718"></a><a name="b842352706151718"></a>true</strong> or <strong id="b842352706151722"><a name="b842352706151722"></a><a name="b842352706151722"></a>false</strong>.<a name="ul14462208141855"></a><a name="ul14462208141855"></a><ul id="ul14462208141855"><li>If this parameter is set to <strong id="b55868159103732"><a name="b55868159103732"></a><a name="b55868159103732"></a>true</strong>, the disk device type is SCSI, that is, Small Computer System Interface (SCSI), which allows ECS OSs to directly access the underlying storage media and supports SCSI reservation commands.</li><li>If this parameter is set to <strong>false</strong>, the disk device type is VBD (the default type), that is, Virtual Block Device (VBD), which supports only simple SCSI read/write commands.</li><li>If this parameter does not appear, the disk device type is VBD.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row991210132288"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p3500156018292"><a name="p3500156018292"></a><a name="p3500156018292"></a>full_clone</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p1655411118292"><a name="p1655411118292"></a><a name="p1655411118292"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p47931946183150"><a name="p47931946183150"></a><a name="p47931946183150"></a>Specifies the clone method. When the disk is created from a snapshot, the parameter value is <strong id="b84235270616922"><a name="b84235270616922"></a><a name="b84235270616922"></a>0</strong>, indicating the linked cloning method.</p>
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
        "count": 1, 
        "volumes": [
            {
                "attachments": [ ], 
                "availability_zone": "az-dc-1", 
                "bootable": "false", 
                "consistencygroup_id": null, 
                "created_at": "2016-05-25T02:42:10.856332", 
                "description": null, 
                "encrypted": false, 
                "id": "b104b8db-170d-441b-897a-3c8ba9c5a214", 
                "links": [
                    {
                        "href": "https://volume.localdomain.com:8776/v3/dd14c6ac581f40059e27f5320b60bf2f/volumes/b104b8db-170d-441b-897a-3c8ba9c5a214", 
                        "rel": "self"
                    }, 
                    {
                        "href": "https://volume.localdomain.com:8776/dd14c6ac581f40059e27f5320b60bf2f/volumes/b104b8db-170d-441b-897a-3c8ba9c5a214", 
                        "rel": "bookmark"
                    }
                ], 
                "metadata": {}, 
                "name": "zjb_u25_test", 
                "os-vol-host-attr:host": "pod01.xxx#SATA", 
                "volume_image_metadata": { }, 
                "os-vol-mig-status-attr:migstat": null, 
                "os-vol-mig-status-attr:name_id": null, 
                "os-vol-tenant-attr:tenant_id": "dd14c6ac581f40059e27f5320b60bf2f", 
                "os-volume-replication:extended_status": null, 
                "replication_status": "disabled", 
                "multiattach": false, 
                "size": 1, 
                "snapshot_id": null, 
                "source_volid": null, 
                "status": "available", 
                "updated_at": "2016-05-25T02:42:22.341984", 
                "user_id": "b0524e8342084ef5b74f158f78fc3049", 
                "volume_type": "SATA", 
                "service_type": "EVS", 
                "dedicated_storage_id": null, 
                "dedicated_storage_name": null, 
                "wwn": " 688860300000d136fa16f48f05992360"
            }
        ], 
        "volumes_links": [
            {
                "href": "https://volume.localdomain.com:8776/v3/dd14c6ac581f40059e27f5320b60bf2f/volumes/detail?limit=1&marker=b104b8db-170d-441b-897a-3c8ba9c5a214", 
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

