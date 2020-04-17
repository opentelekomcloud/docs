# Querying Details About a Disk<a name="evs_04_3034"></a>

## Function<a name="section60214390"></a>

This API is used to query details about a disk.

## URI<a name="section5058598"></a>

-   URI format

    GET /v3/\{project\_id\}/volumes/\{volume\_id\}

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
    <tbody><tr id="row28634009"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p11415415468"><a name="p11415415468"></a><a name="p11415415468"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p30025596"><a name="p30025596"></a><a name="p30025596"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p16154192"><a name="p16154192"></a><a name="p16154192"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row11170003"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p32355065"><a name="p32355065"></a><a name="p32355065"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p3514615"><a name="p3514615"></a><a name="p3514615"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p16248438"><a name="p16248438"></a><a name="p16248438"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section45527389"></a>

-   Example request

    ```
    GET https://{endpoint}/v3/{project_id}/volumes/b104b8db-170d-441b-897a-3c8ba9c5a214
    ```


## Response<a name="section7093323"></a>

-   Parameter description

    <a name="evs_04_2070_table682710305552"></a>
    <table><thead align="left"><tr id="evs_04_2070_row18828730125511"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="evs_04_2070_p17828103014554"><a name="evs_04_2070_p17828103014554"></a><a name="evs_04_2070_p17828103014554"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="evs_04_2070_p982813025513"><a name="evs_04_2070_p982813025513"></a><a name="evs_04_2070_p982813025513"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="evs_04_2070_p10828123085512"><a name="evs_04_2070_p10828123085512"></a><a name="evs_04_2070_p10828123085512"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2070_row6828153014554"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p915785882019"><a name="evs_04_2070_p915785882019"></a><a name="evs_04_2070_p915785882019"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p1157758182017"><a name="evs_04_2070_p1157758182017"></a><a name="evs_04_2070_p1157758182017"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p13157155812209"><a name="evs_04_2070_p13157155812209"></a><a name="evs_04_2070_p13157155812209"></a>Specifies the queried disk. For details, see <a href="#evs_04_2070_li3451542201439">Parameters in the volume field</a>.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row1383518379555"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p129522216412"><a name="evs_04_2070_p129522216412"></a><a name="evs_04_2070_p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p1595262111415"><a name="evs_04_2070_p1595262111415"></a><a name="evs_04_2070_p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p109527215417"><a name="evs_04_2070_p109527215417"></a><a name="evs_04_2070_p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#evs_04_2070_li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2070_li3451542201439"></a>Parameters in the  **volume**  field

    <a name="evs_04_2070_table34701445142557"></a>
    <table><thead align="left"><tr id="evs_04_2070_row12524911142557"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="evs_04_2070_p7884856142557"><a name="evs_04_2070_p7884856142557"></a><a name="evs_04_2070_p7884856142557"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="evs_04_2070_p34693598142557"><a name="evs_04_2070_p34693598142557"></a><a name="evs_04_2070_p34693598142557"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="evs_04_2070_p58539486142557"><a name="evs_04_2070_p58539486142557"></a><a name="evs_04_2070_p58539486142557"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2070_row44077962142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p13545137142557"><a name="evs_04_2070_p13545137142557"></a><a name="evs_04_2070_p13545137142557"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p23414333142557"><a name="evs_04_2070_p23414333142557"></a><a name="evs_04_2070_p23414333142557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p9255075142557"><a name="evs_04_2070_p9255075142557"></a><a name="evs_04_2070_p9255075142557"></a><span id="evs_04_2070_text193761052172315"><a name="evs_04_2070_text193761052172315"></a><a name="evs_04_2070_text193761052172315"></a>Specifies the disk ID.</span></p>
    </td>
    </tr>
    <tr id="evs_04_2070_row16186817142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p36063800142557"><a name="evs_04_2070_p36063800142557"></a><a name="evs_04_2070_p36063800142557"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p35486679142557"><a name="evs_04_2070_p35486679142557"></a><a name="evs_04_2070_p35486679142557"></a>list&lt;map&lt;String, String&gt;&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p27456944142557"><a name="evs_04_2070_p27456944142557"></a><a name="evs_04_2070_p27456944142557"></a>Specifies the disk URI. For details, see <a href="#evs_04_2070_li4929184617138">Parameters in the links field</a>.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row45785905142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p17670785142557"><a name="evs_04_2070_p17670785142557"></a><a name="evs_04_2070_p17670785142557"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p22047453142557"><a name="evs_04_2070_p22047453142557"></a><a name="evs_04_2070_p22047453142557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p33742556142557"><a name="evs_04_2070_p33742556142557"></a><a name="evs_04_2070_p33742556142557"></a>Specifies the disk name.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row35247553142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p36479557142557"><a name="evs_04_2070_p36479557142557"></a><a name="evs_04_2070_p36479557142557"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p2054104142557"><a name="evs_04_2070_p2054104142557"></a><a name="evs_04_2070_p2054104142557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p55209810142557"><a name="evs_04_2070_p55209810142557"></a><a name="evs_04_2070_p55209810142557"></a>Specifies the disk status. For details, see <a href="evs-disk-status.md">EVS Disk Status</a>.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row27126244142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p49742149142557"><a name="evs_04_2070_p49742149142557"></a><a name="evs_04_2070_p49742149142557"></a>attachments</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p2582234142557"><a name="evs_04_2070_p2582234142557"></a><a name="evs_04_2070_p2582234142557"></a>list&lt;map&lt;String, String&gt;&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p30604994142557"><a name="evs_04_2070_p30604994142557"></a><a name="evs_04_2070_p30604994142557"></a>Specifies the disk attachment information. For details, see <a href="#evs_04_2070_li4186567617138">Parameters in the attachments field</a>.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row7009490142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p30897802142557"><a name="evs_04_2070_p30897802142557"></a><a name="evs_04_2070_p30897802142557"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p19694010142557"><a name="evs_04_2070_p19694010142557"></a><a name="evs_04_2070_p19694010142557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p27840420142557"><a name="evs_04_2070_p27840420142557"></a><a name="evs_04_2070_p27840420142557"></a>Specifies the AZ to which the disk belongs.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row49237196142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p28789925142557"><a name="evs_04_2070_p28789925142557"></a><a name="evs_04_2070_p28789925142557"></a>source_volid</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p50282587142557"><a name="evs_04_2070_p50282587142557"></a><a name="evs_04_2070_p50282587142557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p63987579142557"><a name="evs_04_2070_p63987579142557"></a><a name="evs_04_2070_p63987579142557"></a>Specifies the source disk ID. This parameter has a value if the disk is created from a source disk.</p>
    <p id="evs_04_2070_p4357134552610"><a name="evs_04_2070_p4357134552610"></a><a name="evs_04_2070_p4357134552610"></a><span id="evs_04_2070_text18357144552617"><a name="evs_04_2070_text18357144552617"></a><a name="evs_04_2070_text18357144552617"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="evs_04_2070_row39017307142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p6285295142557"><a name="evs_04_2070_p6285295142557"></a><a name="evs_04_2070_p6285295142557"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p39346916142557"><a name="evs_04_2070_p39346916142557"></a><a name="evs_04_2070_p39346916142557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p54429968142557"><a name="evs_04_2070_p54429968142557"></a><a name="evs_04_2070_p54429968142557"></a>Specifies the snapshot ID. This parameter has a value if the disk is created from a snapshot.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row20107664142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p18108106142557"><a name="evs_04_2070_p18108106142557"></a><a name="evs_04_2070_p18108106142557"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p57470472142557"><a name="evs_04_2070_p57470472142557"></a><a name="evs_04_2070_p57470472142557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p46172338142557"><a name="evs_04_2070_p46172338142557"></a><a name="evs_04_2070_p46172338142557"></a>Specifies the disk description.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row12897861142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p38093790142557"><a name="evs_04_2070_p38093790142557"></a><a name="evs_04_2070_p38093790142557"></a>os-vol-tenant-attr:tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p65698111142557"><a name="evs_04_2070_p65698111142557"></a><a name="evs_04_2070_p65698111142557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p5075579142557"><a name="evs_04_2070_p5075579142557"></a><a name="evs_04_2070_p5075579142557"></a>Specifies the ID of the tenant to which the disk belongs. <span id="evs_04_2070_text19941457165313"><a name="evs_04_2070_text19941457165313"></a><a name="evs_04_2070_text19941457165313"></a>The tenant ID is actually the project ID.</span></p>
    </td>
    </tr>
    <tr id="evs_04_2070_row45680217142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p9110107142557"><a name="evs_04_2070_p9110107142557"></a><a name="evs_04_2070_p9110107142557"></a>volume_image_metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p66830090142557"><a name="evs_04_2070_p66830090142557"></a><a name="evs_04_2070_p66830090142557"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p50014861142557"><a name="evs_04_2070_p50014861142557"></a><a name="evs_04_2070_p50014861142557"></a>Specifies the metadata of the disk image.</p>
    <div class="note" id="evs_04_2070_note13108526174911"><a name="evs_04_2070_note13108526174911"></a><a name="evs_04_2070_note13108526174911"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2070_evs_04_2009_p1888154732118"><a name="evs_04_2070_evs_04_2009_p1888154732118"></a><a name="evs_04_2070_evs_04_2009_p1888154732118"></a>For details about <strong id="evs_04_2070_evs_04_2009_b664802919300"><a name="evs_04_2070_evs_04_2009_b664802919300"></a><a name="evs_04_2070_evs_04_2009_b664802919300"></a>volume_image_metadata</strong>, see <strong id="evs_04_2070_evs_04_2009_b0649629203016"><a name="evs_04_2070_evs_04_2009_b0649629203016"></a><a name="evs_04_2070_evs_04_2009_b0649629203016"></a>Querying Image Details</strong> in the <em id="evs_04_2070_evs_04_2009_i186501329183018"><a name="evs_04_2070_evs_04_2009_i186501329183018"></a><a name="evs_04_2070_evs_04_2009_i186501329183018"></a>Image Management Service API Reference</em>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="evs_04_2070_row47480567142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p20720700142557"><a name="evs_04_2070_p20720700142557"></a><a name="evs_04_2070_p20720700142557"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p655154142557"><a name="evs_04_2070_p655154142557"></a><a name="evs_04_2070_p655154142557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p3501903142557"><a name="evs_04_2070_p3501903142557"></a><a name="evs_04_2070_p3501903142557"></a>Specifies the time when the disk was created.</p>
    <p id="evs_04_2070_p766115476237"><a name="evs_04_2070_p766115476237"></a><a name="evs_04_2070_p766115476237"></a><span id="evs_04_2070_text151181202390"><a name="evs_04_2070_text151181202390"></a><a name="evs_04_2070_text151181202390"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="evs_04_2070_row31517135142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p2751105142557"><a name="evs_04_2070_p2751105142557"></a><a name="evs_04_2070_p2751105142557"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p21512968142557"><a name="evs_04_2070_p21512968142557"></a><a name="evs_04_2070_p21512968142557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p16647604142557"><a name="evs_04_2070_p16647604142557"></a><a name="evs_04_2070_p16647604142557"></a>Specifies the disk type.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row15610713142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p56508275142557"><a name="evs_04_2070_p56508275142557"></a><a name="evs_04_2070_p56508275142557"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p13767590142557"><a name="evs_04_2070_p13767590142557"></a><a name="evs_04_2070_p13767590142557"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p628596142557"><a name="evs_04_2070_p628596142557"></a><a name="evs_04_2070_p628596142557"></a>Specifies the disk size, in GB.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row5657368142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p55593700142557"><a name="evs_04_2070_p55593700142557"></a><a name="evs_04_2070_p55593700142557"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p6795819142557"><a name="evs_04_2070_p6795819142557"></a><a name="evs_04_2070_p6795819142557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><div class="p" id="evs_04_2070_en-us_topic_0098680634_p8780414125315"><a name="evs_04_2070_en-us_topic_0098680634_p8780414125315"></a><a name="evs_04_2070_en-us_topic_0098680634_p8780414125315"></a>Specifies whether the disk is bootable.<a name="evs_04_2070_ul185931714111"></a><a name="evs_04_2070_ul185931714111"></a><ul id="evs_04_2070_ul185931714111"><li><strong id="evs_04_2070_b3602437172516"><a name="evs_04_2070_b3602437172516"></a><a name="evs_04_2070_b3602437172516"></a>true</strong>: specifies a bootable disk.</li><li><strong id="evs_04_2070_b14623143811256"><a name="evs_04_2070_b14623143811256"></a><a name="evs_04_2070_b14623143811256"></a>false</strong>: specifies a non-bootable disk.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="evs_04_2070_row42462677142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p16924779142557"><a name="evs_04_2070_p16924779142557"></a><a name="evs_04_2070_p16924779142557"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p28729858142557"><a name="evs_04_2070_p28729858142557"></a><a name="evs_04_2070_p28729858142557"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p2976878614485"><a name="evs_04_2070_p2976878614485"></a><a name="evs_04_2070_p2976878614485"></a>Specifies the disk metadata. For details, see <a href="#evs_04_2070_li29114110314">Parameters in the metadata field</a>.</p>
    <p id="evs_04_2070_p6664089144810"><a name="evs_04_2070_p6664089144810"></a><a name="evs_04_2070_p6664089144810"></a>If <strong id="evs_04_2070_evs_04_2005_b842352706182520"><a name="evs_04_2070_evs_04_2005_b842352706182520"></a><a name="evs_04_2070_evs_04_2005_b842352706182520"></a>metadata</strong> does not contain the <strong id="evs_04_2070_evs_04_2005_b842352706143434"><a name="evs_04_2070_evs_04_2005_b842352706143434"></a><a name="evs_04_2070_evs_04_2005_b842352706143434"></a>hw:passthrough</strong> field, the disk device type is VBD.</p>
    <p id="evs_04_2070_p27113282155030"><a name="evs_04_2070_p27113282155030"></a><a name="evs_04_2070_p27113282155030"></a>If <strong id="evs_04_2070_evs_04_2005_b842352706182629"><a name="evs_04_2070_evs_04_2005_b842352706182629"></a><a name="evs_04_2070_evs_04_2005_b842352706182629"></a>metadata</strong> does not contain the <strong id="evs_04_2070_evs_04_2005_b842352706143455"><a name="evs_04_2070_evs_04_2005_b842352706143455"></a><a name="evs_04_2070_evs_04_2005_b842352706143455"></a>__system__encrypted</strong> field, the disk is not encrypted.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row24435167142557"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p33091499142557"><a name="evs_04_2070_p33091499142557"></a><a name="evs_04_2070_p33091499142557"></a>os-vol-host-attr:host</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p63165723142557"><a name="evs_04_2070_p63165723142557"></a><a name="evs_04_2070_p63165723142557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p33074440142557"><a name="evs_04_2070_p33074440142557"></a><a name="evs_04_2070_p33074440142557"></a><span id="evs_04_2070_text203605127103"><a name="evs_04_2070_text203605127103"></a><a name="evs_04_2070_text203605127103"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="evs_04_2070_row25240105819"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p47452553185118"><a name="evs_04_2070_p47452553185118"></a><a name="evs_04_2070_p47452553185118"></a>encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p18451581185118"><a name="evs_04_2070_p18451581185118"></a><a name="evs_04_2070_p18451581185118"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p27951625185124"><a name="evs_04_2070_p27951625185124"></a><a name="evs_04_2070_p27951625185124"></a><span id="evs_04_2070_text1610112322316"><a name="evs_04_2070_text1610112322316"></a><a name="evs_04_2070_text1610112322316"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="evs_04_2070_row319029143856"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p25841403143856"><a name="evs_04_2070_p25841403143856"></a><a name="evs_04_2070_p25841403143856"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p12778905143856"><a name="evs_04_2070_p12778905143856"></a><a name="evs_04_2070_p12778905143856"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p23431040143856"><a name="evs_04_2070_p23431040143856"></a><a name="evs_04_2070_p23431040143856"></a>Specifies the time when the disk was updated.</p>
    <p id="evs_04_2070_p1042016253342"><a name="evs_04_2070_p1042016253342"></a><a name="evs_04_2070_p1042016253342"></a><span id="evs_04_2070_text16820132513417"><a name="evs_04_2070_text16820132513417"></a><a name="evs_04_2070_text16820132513417"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="evs_04_2070_row6226231314391"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p1008260514391"><a name="evs_04_2070_p1008260514391"></a><a name="evs_04_2070_p1008260514391"></a>os-volume-replication:extended_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p1138464014391"><a name="evs_04_2070_p1138464014391"></a><a name="evs_04_2070_p1138464014391"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p246367414391"><a name="evs_04_2070_p246367414391"></a><a name="evs_04_2070_p246367414391"></a>Reserved field</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row1430942214399"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p1821254814399"><a name="evs_04_2070_p1821254814399"></a><a name="evs_04_2070_p1821254814399"></a>replication_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p6593029014399"><a name="evs_04_2070_p6593029014399"></a><a name="evs_04_2070_p6593029014399"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p5201068114399"><a name="evs_04_2070_p5201068114399"></a><a name="evs_04_2070_p5201068114399"></a>Reserved field</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row1801485814395"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p4991739214395"><a name="evs_04_2070_p4991739214395"></a><a name="evs_04_2070_p4991739214395"></a>os-vol-mig-status-attr:migstat</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p55570357144311"><a name="evs_04_2070_p55570357144311"></a><a name="evs_04_2070_p55570357144311"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p61763041144311"><a name="evs_04_2070_p61763041144311"></a><a name="evs_04_2070_p61763041144311"></a>Reserved field</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row46340323144336"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p62578689144336"><a name="evs_04_2070_p62578689144336"></a><a name="evs_04_2070_p62578689144336"></a>consistencygroup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p20253849144646"><a name="evs_04_2070_p20253849144646"></a><a name="evs_04_2070_p20253849144646"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p9956989144646"><a name="evs_04_2070_p9956989144646"></a><a name="evs_04_2070_p9956989144646"></a>Reserved field</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row36758187144417"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p24623167144417"><a name="evs_04_2070_p24623167144417"></a><a name="evs_04_2070_p24623167144417"></a>os-vol-mig-status-attr:name_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p34730547144648"><a name="evs_04_2070_p34730547144648"></a><a name="evs_04_2070_p34730547144648"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p32527650144648"><a name="evs_04_2070_p32527650144648"></a><a name="evs_04_2070_p32527650144648"></a>Reserved field</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row30115821144625"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p23462435144625"><a name="evs_04_2070_p23462435144625"></a><a name="evs_04_2070_p23462435144625"></a>shareable</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p48108796144650"><a name="evs_04_2070_p48108796144650"></a><a name="evs_04_2070_p48108796144650"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p28827892144650"><a name="evs_04_2070_p28827892144650"></a><a name="evs_04_2070_p28827892144650"></a>Specifies whether the disk is shareable.</p>
    <div class="note" id="evs_04_2070_note3800959821323"><a name="evs_04_2070_note3800959821323"></a><a name="evs_04_2070_note3800959821323"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2070_p45212589213213"><a name="evs_04_2070_p45212589213213"></a><a name="evs_04_2070_p45212589213213"></a>This field is no longer used. Use <strong id="evs_04_2070_b84235270610834"><a name="evs_04_2070_b84235270610834"></a><a name="evs_04_2070_b84235270610834"></a>multiattach</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="evs_04_2070_row4658776614505"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p1551273614505"><a name="evs_04_2070_p1551273614505"></a><a name="evs_04_2070_p1551273614505"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p4857213114505"><a name="evs_04_2070_p4857213114505"></a><a name="evs_04_2070_p4857213114505"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p4886676914505"><a name="evs_04_2070_p4886676914505"></a><a name="evs_04_2070_p4886676914505"></a>Reserved field</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row16426724115040"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p59918584115045"><a name="evs_04_2070_p59918584115045"></a><a name="evs_04_2070_p59918584115045"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p21567161115045"><a name="evs_04_2070_p21567161115045"></a><a name="evs_04_2070_p21567161115045"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><div class="p" id="evs_04_2070_en-us_topic_0098680634_p4781191416535"><a name="evs_04_2070_en-us_topic_0098680634_p4781191416535"></a><a name="evs_04_2070_en-us_topic_0098680634_p4781191416535"></a>Specifies whether the disk is shareable.<a name="evs_04_2070_ul161621719119"></a><a name="evs_04_2070_ul161621719119"></a><ul id="evs_04_2070_ul161621719119"><li><strong id="evs_04_2070_b27111240102513"><a name="evs_04_2070_b27111240102513"></a><a name="evs_04_2070_b27111240102513"></a>true</strong>: specifies a shared disk.</li><li><strong id="evs_04_2070_b6557174211255"><a name="evs_04_2070_b6557174211255"></a><a name="evs_04_2070_b6557174211255"></a>false</strong>: specifies a non-shared disk.</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2070_li4929184617138"></a>Parameters in the  **links**  field

    <a name="evs_04_2070_table53116786111129"></a>
    <table><thead align="left"><tr id="evs_04_2070_row38921210111129"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="evs_04_2070_p65610305111129"><a name="evs_04_2070_p65610305111129"></a><a name="evs_04_2070_p65610305111129"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="evs_04_2070_p12834480111129"><a name="evs_04_2070_p12834480111129"></a><a name="evs_04_2070_p12834480111129"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="evs_04_2070_p52513065111129"><a name="evs_04_2070_p52513065111129"></a><a name="evs_04_2070_p52513065111129"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2070_row25699842111129"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p1312419111129"><a name="evs_04_2070_p1312419111129"></a><a name="evs_04_2070_p1312419111129"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p39197109111129"><a name="evs_04_2070_p39197109111129"></a><a name="evs_04_2070_p39197109111129"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p11067466111129"><a name="evs_04_2070_p11067466111129"></a><a name="evs_04_2070_p11067466111129"></a>Specifies the corresponding shortcut link.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row32498335111129"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p15119502111129"><a name="evs_04_2070_p15119502111129"></a><a name="evs_04_2070_p15119502111129"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p16720145111129"><a name="evs_04_2070_p16720145111129"></a><a name="evs_04_2070_p16720145111129"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p44991477111129"><a name="evs_04_2070_p44991477111129"></a><a name="evs_04_2070_p44991477111129"></a>Specifies the shortcut link marker name.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2070_li4186567617138"></a>Parameters in the  **attachments**  field

    <a name="evs_04_2070_table2886066111147"></a>
    <table><thead align="left"><tr id="evs_04_2070_row7036686111147"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="evs_04_2070_p33100723111147"><a name="evs_04_2070_p33100723111147"></a><a name="evs_04_2070_p33100723111147"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="evs_04_2070_p63912929111147"><a name="evs_04_2070_p63912929111147"></a><a name="evs_04_2070_p63912929111147"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="evs_04_2070_p36546037111147"><a name="evs_04_2070_p36546037111147"></a><a name="evs_04_2070_p36546037111147"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2070_row7439020111147"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p65689739111147"><a name="evs_04_2070_p65689739111147"></a><a name="evs_04_2070_p65689739111147"></a>server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p19268667111147"><a name="evs_04_2070_p19268667111147"></a><a name="evs_04_2070_p19268667111147"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p55737901111147"><a name="evs_04_2070_p55737901111147"></a><a name="evs_04_2070_p55737901111147"></a>Specifies the ID of the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row31879061111147"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p32067121111147"><a name="evs_04_2070_p32067121111147"></a><a name="evs_04_2070_p32067121111147"></a>attachment_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p47300034111147"><a name="evs_04_2070_p47300034111147"></a><a name="evs_04_2070_p47300034111147"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p24142306111147"><a name="evs_04_2070_p24142306111147"></a><a name="evs_04_2070_p24142306111147"></a>Specifies the ID of the attachment information.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row23348196112253"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p12155729112253"><a name="evs_04_2070_p12155729112253"></a><a name="evs_04_2070_p12155729112253"></a>attached_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p45090011112253"><a name="evs_04_2070_p45090011112253"></a><a name="evs_04_2070_p45090011112253"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p19692132112253"><a name="evs_04_2070_p19692132112253"></a><a name="evs_04_2070_p19692132112253"></a>Specifies the time when the disk was attached.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row15954169111147"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p17219276111147"><a name="evs_04_2070_p17219276111147"></a><a name="evs_04_2070_p17219276111147"></a>host_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p52584153111147"><a name="evs_04_2070_p52584153111147"></a><a name="evs_04_2070_p52584153111147"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p65069243111147"><a name="evs_04_2070_p65069243111147"></a><a name="evs_04_2070_p65069243111147"></a>Specifies the name of the physical host accommodating the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row48752281111147"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p56620654111147"><a name="evs_04_2070_p56620654111147"></a><a name="evs_04_2070_p56620654111147"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p22870239111147"><a name="evs_04_2070_p22870239111147"></a><a name="evs_04_2070_p22870239111147"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p63332792111147"><a name="evs_04_2070_p63332792111147"></a><a name="evs_04_2070_p63332792111147"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row33124222111147"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p65816302111147"><a name="evs_04_2070_p65816302111147"></a><a name="evs_04_2070_p65816302111147"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p29520255111147"><a name="evs_04_2070_p29520255111147"></a><a name="evs_04_2070_p29520255111147"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p6214946111147"><a name="evs_04_2070_p6214946111147"></a><a name="evs_04_2070_p6214946111147"></a>Specifies the device name.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_row55934521111147"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_p34402351111147"><a name="evs_04_2070_p34402351111147"></a><a name="evs_04_2070_p34402351111147"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_p35127017111147"><a name="evs_04_2070_p35127017111147"></a><a name="evs_04_2070_p35127017111147"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_p16521419111147"><a name="evs_04_2070_p16521419111147"></a><a name="evs_04_2070_p16521419111147"></a>Specifies the ID of the attached resource.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2070_li29114110314"></a>Parameters in the  **metadata**  field

    <a name="evs_04_2070_evs_04_3004_table3430728295554"></a>
    <table><thead align="left"><tr id="evs_04_2070_evs_04_3004_row4496975195554"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="evs_04_2070_evs_04_3004_p8809200174410"><a name="evs_04_2070_evs_04_3004_p8809200174410"></a><a name="evs_04_2070_evs_04_3004_p8809200174410"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.62%" id="mcps1.1.4.1.2"><p id="evs_04_2070_evs_04_3004_p168135017449"><a name="evs_04_2070_evs_04_3004_p168135017449"></a><a name="evs_04_2070_evs_04_3004_p168135017449"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="evs_04_2070_evs_04_3004_p1282213034412"><a name="evs_04_2070_evs_04_3004_p1282213034412"></a><a name="evs_04_2070_evs_04_3004_p1282213034412"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2070_evs_04_3004_row456195295554"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_evs_04_3004_p1562408795622"><a name="evs_04_2070_evs_04_3004_p1562408795622"></a><a name="evs_04_2070_evs_04_3004_p1562408795622"></a>__system__encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_evs_04_3004_p5759155095622"><a name="evs_04_2070_evs_04_3004_p5759155095622"></a><a name="evs_04_2070_evs_04_3004_p5759155095622"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><div class="p" id="evs_04_2070_evs_04_3004_p177192813501"><a name="evs_04_2070_evs_04_3004_p177192813501"></a><a name="evs_04_2070_evs_04_3004_p177192813501"></a>Specifies the parameter that describes the encryption function in <strong id="evs_04_2070_evs_04_3004_b84235270614509"><a name="evs_04_2070_evs_04_3004_b84235270614509"></a><a name="evs_04_2070_evs_04_3004_b84235270614509"></a>metadata</strong>. The value can be <strong id="evs_04_2070_evs_04_3004_b842352706145015"><a name="evs_04_2070_evs_04_3004_b842352706145015"></a><a name="evs_04_2070_evs_04_3004_b842352706145015"></a>0</strong> or <strong id="evs_04_2070_evs_04_3004_b842352706145020"><a name="evs_04_2070_evs_04_3004_b842352706145020"></a><a name="evs_04_2070_evs_04_3004_b842352706145020"></a>1</strong>.<a name="evs_04_2070_evs_04_3004_ul141951225145011"></a><a name="evs_04_2070_evs_04_3004_ul141951225145011"></a><ul id="evs_04_2070_evs_04_3004_ul141951225145011"><li><strong id="evs_04_2070_evs_04_3004_b842352706145038"><a name="evs_04_2070_evs_04_3004_b842352706145038"></a><a name="evs_04_2070_evs_04_3004_b842352706145038"></a>0</strong>: indicates the disk is not encrypted.</li><li><strong id="evs_04_2070_evs_04_3004_b842352706145058"><a name="evs_04_2070_evs_04_3004_b842352706145058"></a><a name="evs_04_2070_evs_04_3004_b842352706145058"></a>1</strong>: indicates the disk is encrypted.</li><li>If this parameter does not appear, the disk is not encrypted by default.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="evs_04_2070_evs_04_3004_row247050109562"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_evs_04_3004_p241272995622"><a name="evs_04_2070_evs_04_3004_p241272995622"></a><a name="evs_04_2070_evs_04_3004_p241272995622"></a>__system__cmkid</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_evs_04_3004_p6121338895622"><a name="evs_04_2070_evs_04_3004_p6121338895622"></a><a name="evs_04_2070_evs_04_3004_p6121338895622"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_evs_04_3004_p4159804295622"><a name="evs_04_2070_evs_04_3004_p4159804295622"></a><a name="evs_04_2070_evs_04_3004_p4159804295622"></a>Specifies the parameter that describes the encryption CMK ID in <strong id="evs_04_2070_evs_04_3004_b84235270615116"><a name="evs_04_2070_evs_04_3004_b84235270615116"></a><a name="evs_04_2070_evs_04_3004_b84235270615116"></a>metadata</strong>. This parameter is used together with <strong id="evs_04_2070_evs_04_3004_b842352706143827"><a name="evs_04_2070_evs_04_3004_b842352706143827"></a><a name="evs_04_2070_evs_04_3004_b842352706143827"></a>__system__encrypted</strong> for encryption. The length of <strong id="evs_04_2070_evs_04_3004_b84235270614396"><a name="evs_04_2070_evs_04_3004_b84235270614396"></a><a name="evs_04_2070_evs_04_3004_b84235270614396"></a>cmkid</strong> is fixed at 36 bytes.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_evs_04_3004_row60499086104915"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_evs_04_3004_p1478896104915"><a name="evs_04_2070_evs_04_3004_p1478896104915"></a><a name="evs_04_2070_evs_04_3004_p1478896104915"></a>hw:passthrough</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_evs_04_3004_p52681767104915"><a name="evs_04_2070_evs_04_3004_p52681767104915"></a><a name="evs_04_2070_evs_04_3004_p52681767104915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><div class="p" id="evs_04_2070_evs_04_3004_p17177177145116"><a name="evs_04_2070_evs_04_3004_p17177177145116"></a><a name="evs_04_2070_evs_04_3004_p17177177145116"></a>Specifies the parameter that describes the disk device type in <strong id="evs_04_2070_evs_04_3004_b84235270615173"><a name="evs_04_2070_evs_04_3004_b84235270615173"></a><a name="evs_04_2070_evs_04_3004_b84235270615173"></a>metadata</strong>. The value can be <strong id="evs_04_2070_evs_04_3004_b842352706151718"><a name="evs_04_2070_evs_04_3004_b842352706151718"></a><a name="evs_04_2070_evs_04_3004_b842352706151718"></a>true</strong> or <strong id="evs_04_2070_evs_04_3004_b842352706151722"><a name="evs_04_2070_evs_04_3004_b842352706151722"></a><a name="evs_04_2070_evs_04_3004_b842352706151722"></a>false</strong>.<a name="evs_04_2070_evs_04_3004_ul14462208141855"></a><a name="evs_04_2070_evs_04_3004_ul14462208141855"></a><ul id="evs_04_2070_evs_04_3004_ul14462208141855"><li>If this parameter is set to <strong id="evs_04_2070_evs_04_3004_b55868159103732"><a name="evs_04_2070_evs_04_3004_b55868159103732"></a><a name="evs_04_2070_evs_04_3004_b55868159103732"></a>true</strong>, the disk device type is SCSI, that is, Small Computer System Interface (SCSI), which allows ECS OSs to directly access the underlying storage media and supports SCSI reservation commands.</li><li>If this parameter is set to <strong>false</strong>, the disk device type is VBD (the default type), that is, Virtual Block Device (VBD), which supports only simple SCSI read/write commands.</li><li>If this parameter does not appear, the disk device type is VBD.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="evs_04_2070_evs_04_3004_row991210132288"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_evs_04_3004_p3500156018292"><a name="evs_04_2070_evs_04_3004_p3500156018292"></a><a name="evs_04_2070_evs_04_3004_p3500156018292"></a>full_clone</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_evs_04_3004_p1655411118292"><a name="evs_04_2070_evs_04_3004_p1655411118292"></a><a name="evs_04_2070_evs_04_3004_p1655411118292"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_evs_04_3004_p47931946183150"><a name="evs_04_2070_evs_04_3004_p47931946183150"></a><a name="evs_04_2070_evs_04_3004_p47931946183150"></a>Specifies the clone method. When the disk is created from a snapshot, the parameter value is <strong id="evs_04_2070_evs_04_3004_b84235270616922"><a name="evs_04_2070_evs_04_3004_b84235270616922"></a><a name="evs_04_2070_evs_04_3004_b84235270616922"></a>0</strong>, indicating the linked cloning method.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2070_li0419202382514"></a>Parameters in the  **error**  field

    <a name="evs_04_2070_evs_04_2013_table15441099103019"></a>
    <table><thead align="left"><tr id="evs_04_2070_evs_04_2013_row54094047103019"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="evs_04_2070_evs_04_2013_p19541716103019"><a name="evs_04_2070_evs_04_2013_p19541716103019"></a><a name="evs_04_2070_evs_04_2013_p19541716103019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="evs_04_2070_evs_04_2013_p39375186103019"><a name="evs_04_2070_evs_04_2013_p39375186103019"></a><a name="evs_04_2070_evs_04_2013_p39375186103019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2070_evs_04_2013_p38578950103019"><a name="evs_04_2070_evs_04_2013_p38578950103019"></a><a name="evs_04_2070_evs_04_2013_p38578950103019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2070_evs_04_2013_row59401790103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_evs_04_2013_p46815658103019"><a name="evs_04_2070_evs_04_2013_p46815658103019"></a><a name="evs_04_2070_evs_04_2013_p46815658103019"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_evs_04_2013_p33971979103019"><a name="evs_04_2070_evs_04_2013_p33971979103019"></a><a name="evs_04_2070_evs_04_2013_p33971979103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_evs_04_2013_p21623243103019"><a name="evs_04_2070_evs_04_2013_p21623243103019"></a><a name="evs_04_2070_evs_04_2013_p21623243103019"></a>Specifies the error message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="evs_04_2070_evs_04_2013_row60391466103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2070_evs_04_2013_p59870541103019"><a name="evs_04_2070_evs_04_2013_p59870541103019"></a><a name="evs_04_2070_evs_04_2013_p59870541103019"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2070_evs_04_2013_p17675690103019"><a name="evs_04_2070_evs_04_2013_p17675690103019"></a><a name="evs_04_2070_evs_04_2013_p17675690103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2070_evs_04_2013_p6087468103019"><a name="evs_04_2070_evs_04_2013_p6087468103019"></a><a name="evs_04_2070_evs_04_2013_p6087468103019"></a>Specifies the error code returned when an error occurs.</p>
    <p id="evs_04_2070_evs_04_2013_p54787218103019"><a name="evs_04_2070_evs_04_2013_p54787218103019"></a><a name="evs_04_2070_evs_04_2013_p54787218103019"></a>For details about the error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "volume": {
            "attachments": [ ], 
            "links": [
                {
                    "href": "https://volume.az0.dc1.domainname.com/v2/40acc331ac784f34842ba4f08ff2be48/volumes/591ac654-26d8-41be-bb77-4f90699d2d41", 
                    "rel": "self"
                }, 
                {
                    "href": "https://volume.az0.dc1.domainname.com/40acc331ac784f34842ba4f08ff2be48/volumes/591ac654-26d8-41be-bb77-4f90699d2d41", 
                    "rel": "bookmark"
                }
            ], 
            "availability_zone": "az-dc-1", 
            "os-vol-host-attr:host": "az-dc-1#SSD", 
            "encrypted": false, 
            "multiattach": true, 
            "updated_at": "2016-02-03T02:19:29.895237", 
            "os-volume-replication:extended_status": null, 
            "replication_status": "disabled", 
            "snapshot_id": null, 
            "id": "591ac654-26d8-41be-bb77-4f90699d2d41", 
            "size": 40, 
            "user_id": "fd03ee73295e45478d88e15263d2ee4e", 
            "os-vol-tenant-attr:tenant_id": "40acc331ac784f34842ba4f08ff2be48", 
            "volume_image_metadata": null, 
            "os-vol-mig-status-attr:migstat": null, 
            "metadata": {}, 
            "status": "error_restoring", 
            "description": "auto-created_from_restore_from_backup", 
            "source_volid": null, 
            "consistencygroup_id": null, 
            "os-vol-mig-status-attr:name_id": null, 
            "name": "restore_backup_0115efb3-678c-4a9e-bff6-d3cd278238b9", 
            "bootable": "false", 
            "created_at": "2016-02-03T02:19:11.723797", 
            "volume_type": null
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


## Status Codes<a name="section63839913"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

