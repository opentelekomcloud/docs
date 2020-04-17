# Querying Details About a Disk \(Deprecated\)<a name="evs_04_0052"></a>

## Function<a name="section60214390"></a>

This API is used to query details about a disk.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>This API has been deprecated. Use another API. For details, see  [Querying Details About a Disk](querying-details-about-a-disk-cinder-v3.md).  

## URI<a name="section5058598"></a>

-   URI format

    GET /v1/\{project\_id\}/volumes/\{volume\_id\}

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
    GET https://{endpoint}/v1/{project_id}/volumes/b104b8db-170d-441b-897a-3c8ba9c5a214
    ```


## Response<a name="section7093323"></a>

-   Parameter description

    <a name="table18977112434313"></a>
    <table><thead align="left"><tr id="row3977132419439"><th class="cellrowborder" valign="top" width="22.467753224677534%" id="mcps1.1.4.1.1"><p id="p159773247431"><a name="p159773247431"></a><a name="p159773247431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.297570242975702%" id="mcps1.1.4.1.2"><p id="p12977324154317"><a name="p12977324154317"></a><a name="p12977324154317"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.23467653234677%" id="mcps1.1.4.1.3"><p id="p597722424317"><a name="p597722424317"></a><a name="p597722424317"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row89773247438"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p1397772413439"><a name="p1397772413439"></a><a name="p1397772413439"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p29771324204317"><a name="p29771324204317"></a><a name="p29771324204317"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p179771624124315"><a name="p179771624124315"></a><a name="p179771624124315"></a>Specifies the disk information. For details, see <a href="#li3451542201439">Parameters in the volume field</a>.</p>
    </td>
    </tr>
    <tr id="row987510557481"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li3451542201439"></a>Parameters in the  **volume**  field

    <a name="table34701445142557"></a>
    <table><thead align="left"><tr id="row12524911142557"><th class="cellrowborder" valign="top" width="22.467753224677534%" id="mcps1.1.4.1.1"><p id="p7884856142557"><a name="p7884856142557"></a><a name="p7884856142557"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.297570242975702%" id="mcps1.1.4.1.2"><p id="p34693598142557"><a name="p34693598142557"></a><a name="p34693598142557"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.23467653234677%" id="mcps1.1.4.1.3"><p id="p58539486142557"><a name="p58539486142557"></a><a name="p58539486142557"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row444782011610"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p66683282154651"><a name="p66683282154651"></a><a name="p66683282154651"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p32636789154651"><a name="p32636789154651"></a><a name="p32636789154651"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p9255075142557"><a name="p9255075142557"></a><a name="p9255075142557"></a><span id="text193761052172315"><a name="text193761052172315"></a><a name="text193761052172315"></a>Specifies the disk ID.</span></p>
    </td>
    </tr>
    <tr id="row44077962142557"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p30586043154651"><a name="p30586043154651"></a><a name="p30586043154651"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p9772661154635"><a name="p9772661154635"></a><a name="p9772661154635"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p38052791154651"><a name="p38052791154651"></a><a name="p38052791154651"></a>Specifies the disk name.</p>
    </td>
    </tr>
    <tr id="row16186817142557"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p24524218154651"><a name="p24524218154651"></a><a name="p24524218154651"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p3143623154637"><a name="p3143623154637"></a><a name="p3143623154637"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p29828016154651"><a name="p29828016154651"></a><a name="p29828016154651"></a>Specifies the disk status. For details, see <a href="evs-disk-status.md">EVS Disk Status</a>.</p>
    </td>
    </tr>
    <tr id="row45785905142557"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p1352242154651"><a name="p1352242154651"></a><a name="p1352242154651"></a>attachments</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p42422738154651"><a name="p42422738154651"></a><a name="p42422738154651"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p35126047154651"><a name="p35126047154651"></a><a name="p35126047154651"></a>Specifies the attachment information.</p>
    </td>
    </tr>
    <tr id="row35247553142557"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p38411786154651"><a name="p38411786154651"></a><a name="p38411786154651"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p62102892154639"><a name="p62102892154639"></a><a name="p62102892154639"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p21400414154651"><a name="p21400414154651"></a><a name="p21400414154651"></a>Specifies the AZ to which the disk belongs.</p>
    </td>
    </tr>
    <tr id="row27126244142557"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p31645621154651"><a name="p31645621154651"></a><a name="p31645621154651"></a>os-vol-host-attr:host</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p44910102154640"><a name="p44910102154640"></a><a name="p44910102154640"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p30932940154651"><a name="p30932940154651"></a><a name="p30932940154651"></a><span id="text8624191685913"><a name="text8624191685913"></a><a name="text8624191685913"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row7009490142557"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p1535595154651"><a name="p1535595154651"></a><a name="p1535595154651"></a>source_volid</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p62551737154640"><a name="p62551737154640"></a><a name="p62551737154640"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p34514964154651"><a name="p34514964154651"></a><a name="p34514964154651"></a>Specifies the source disk ID. This parameter has a value if the disk is created from a source disk.</p>
    <p id="p11914151216505"><a name="p11914151216505"></a><a name="p11914151216505"></a><span id="text18357144552617"><a name="text18357144552617"></a><a name="text18357144552617"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="row49237196142557"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p62693997154651"><a name="p62693997154651"></a><a name="p62693997154651"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p28398340154644"><a name="p28398340154644"></a><a name="p28398340154644"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p18936934154651"><a name="p18936934154651"></a><a name="p18936934154651"></a>Specifies the snapshot ID. This parameter has a value if the disk is created from a snapshot.</p>
    </td>
    </tr>
    <tr id="row39017307142557"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p47707972154651"><a name="p47707972154651"></a><a name="p47707972154651"></a>display_description</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p40680894154646"><a name="p40680894154646"></a><a name="p40680894154646"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p42443707154651"><a name="p42443707154651"></a><a name="p42443707154651"></a>Specifies the disk description.</p>
    </td>
    </tr>
    <tr id="row20107664142557"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p4276225154651"><a name="p4276225154651"></a><a name="p4276225154651"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p55282734154647"><a name="p55282734154647"></a><a name="p55282734154647"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p54211604154651"><a name="p54211604154651"></a><a name="p54211604154651"></a>Specifies the time when the disk was created.</p>
    <p id="p128341116112619"><a name="p128341116112619"></a><a name="p128341116112619"></a><span id="text19834191618261"><a name="text19834191618261"></a><a name="text19834191618261"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row12897861142557"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p60247422154651"><a name="p60247422154651"></a><a name="p60247422154651"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p51779673154648"><a name="p51779673154648"></a><a name="p51779673154648"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p42804410154651"><a name="p42804410154651"></a><a name="p42804410154651"></a>Specifies the disk type.</p>
    </td>
    </tr>
    <tr id="row45680217142557"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p65902234154651"><a name="p65902234154651"></a><a name="p65902234154651"></a>os-vol-tenant-attr:tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p14564094154649"><a name="p14564094154649"></a><a name="p14564094154649"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p7523113475716"><a name="p7523113475716"></a><a name="p7523113475716"></a>Specifies the ID of the tenant to which the disk belongs. <span id="text19941457165313"><a name="text19941457165313"></a><a name="text19941457165313"></a>The tenant ID is actually the project ID.</span></p>
    </td>
    </tr>
    <tr id="row47480567142557"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p22901376154651"><a name="p22901376154651"></a><a name="p22901376154651"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p43072149154651"><a name="p43072149154651"></a><a name="p43072149154651"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p947705154651"><a name="p947705154651"></a><a name="p947705154651"></a>Specifies the disk size, in GB.</p>
    </td>
    </tr>
    <tr id="row31517135142557"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p19789024154651"><a name="p19789024154651"></a><a name="p19789024154651"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p159017261855"><a name="en-us_topic_0098680634_p159017261855"></a><a name="en-us_topic_0098680634_p159017261855"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p4822480314495"><a name="p4822480314495"></a><a name="p4822480314495"></a>Specifies the disk metadata.</p>
    <p id="p1534925154651"><a name="p1534925154651"></a><a name="p1534925154651"></a>If <strong id="evs_04_2005_b842352706182520"><a name="evs_04_2005_b842352706182520"></a><a name="evs_04_2005_b842352706182520"></a>metadata</strong> does not contain the <strong id="evs_04_2005_b842352706143434"><a name="evs_04_2005_b842352706143434"></a><a name="evs_04_2005_b842352706143434"></a>hw:passthrough</strong> field, the disk device type is VBD.</p>
    <p id="p1134831215404"><a name="p1134831215404"></a><a name="p1134831215404"></a>If <strong id="evs_04_2005_b842352706182629"><a name="evs_04_2005_b842352706182629"></a><a name="evs_04_2005_b842352706182629"></a>metadata</strong> does not contain the <strong id="evs_04_2005_b842352706143455"><a name="evs_04_2005_b842352706143455"></a><a name="evs_04_2005_b842352706143455"></a>__system__encrypted</strong> field, the disk is not encrypted.</p>
    </td>
    </tr>
    <tr id="row15610713142557"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p45218866154651"><a name="p45218866154651"></a><a name="p45218866154651"></a>os-vol-mig-status-attr:migstat</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p37723694154653"><a name="p37723694154653"></a><a name="p37723694154653"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p978016142531"><a name="en-us_topic_0098680634_p978016142531"></a><a name="en-us_topic_0098680634_p978016142531"></a><span id="text203605127103"><a name="text203605127103"></a><a name="text203605127103"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row5657368142557"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p7111161154651"><a name="p7111161154651"></a><a name="p7111161154651"></a>os-vol-mig-status-attr:name_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p2604538915471"><a name="p2604538915471"></a><a name="p2604538915471"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p61553832154651"><a name="p61553832154651"></a><a name="p61553832154651"></a><span id="text117680327233"><a name="text117680327233"></a><a name="text117680327233"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row24435167142557"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p4466064154651"><a name="p4466064154651"></a><a name="p4466064154651"></a>os-volume-replication:extended_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p944841515473"><a name="p944841515473"></a><a name="p944841515473"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p10508856154651"><a name="p10508856154651"></a><a name="p10508856154651"></a><span id="text379518478151"><a name="text379518478151"></a><a name="text379518478151"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row15562216185816"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p53797707185823"><a name="p53797707185823"></a><a name="p53797707185823"></a>encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p62647029185823"><a name="p62647029185823"></a><a name="p62647029185823"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p63407626185825"><a name="p63407626185825"></a><a name="p63407626185825"></a><span id="text14572822181912"><a name="text14572822181912"></a><a name="text14572822181912"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="row319029143856"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p41938891154651"><a name="p41938891154651"></a><a name="p41938891154651"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p4460388215477"><a name="p4460388215477"></a><a name="p4460388215477"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><div class="p" id="en-us_topic_0058762429_en-us_topic_0098680634_p8780414125315"><a name="en-us_topic_0058762429_en-us_topic_0098680634_p8780414125315"></a><a name="en-us_topic_0058762429_en-us_topic_0098680634_p8780414125315"></a>Specifies whether the disk is bootable.<a name="en-us_topic_0058762429_ul185931714111"></a><a name="en-us_topic_0058762429_ul185931714111"></a><ul id="en-us_topic_0058762429_ul185931714111"><li><strong id="b7690719164217"><a name="b7690719164217"></a><a name="b7690719164217"></a>true</strong>: specifies a bootable disk.</li><li><strong id="b8564120154216"><a name="b8564120154216"></a><a name="b8564120154216"></a>false</strong>: specifies a non-bootable disk.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row6226231314391"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p56347645154651"><a name="p56347645154651"></a><a name="p56347645154651"></a>shareable</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p368674015478"><a name="p368674015478"></a><a name="p368674015478"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p64877853154651"><a name="p64877853154651"></a><a name="p64877853154651"></a>Specifies whether the disk is shareable.</p>
    <div class="note" id="note1645730517525"><a name="note1645730517525"></a><a name="note1645730517525"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_p45212589213213"><a name="evs_04_2013_p45212589213213"></a><a name="evs_04_2013_p45212589213213"></a>This field is no longer used. Use <strong id="evs_04_2013_b84235270610834"><a name="evs_04_2013_b84235270610834"></a><a name="evs_04_2013_b84235270610834"></a>multiattach</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1430942214399"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p51315026154651"><a name="p51315026154651"></a><a name="p51315026154651"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p4808386110597"><a name="p4808386110597"></a><a name="p4808386110597"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><div class="p" id="en-us_topic_0058762429_en-us_topic_0098680634_p4781191416535"><a name="en-us_topic_0058762429_en-us_topic_0098680634_p4781191416535"></a><a name="en-us_topic_0058762429_en-us_topic_0098680634_p4781191416535"></a>Specifies whether the disk is shareable.<a name="en-us_topic_0058762429_ul161621719119"></a><a name="en-us_topic_0058762429_ul161621719119"></a><ul id="en-us_topic_0058762429_ul161621719119"><li><strong id="b201214226427"><a name="b201214226427"></a><a name="b201214226427"></a>true</strong>: specifies a shared disk.</li><li><strong id="b1950132210426"><a name="b1950132210426"></a><a name="b1950132210426"></a>false</strong>: specifies a non-shared disk.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row1801485814395"><td class="cellrowborder" valign="top" width="22.467753224677534%" headers="mcps1.1.4.1.1 "><p id="p43505026154651"><a name="p43505026154651"></a><a name="p43505026154651"></a>volume_image_metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.297570242975702%" headers="mcps1.1.4.1.2 "><p id="p34246222154651"><a name="p34246222154651"></a><a name="p34246222154651"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.23467653234677%" headers="mcps1.1.4.1.3 "><p id="p8988855154651"><a name="p8988855154651"></a><a name="p8988855154651"></a>Specifies whether the disk is created from an image. This field has a value if the disk is created from an image. Otherwise, it is left empty.</p>
    <div class="note" id="note151343244518"><a name="note151343244518"></a><a name="note151343244518"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2009_p1888154732118"><a name="evs_04_2009_p1888154732118"></a><a name="evs_04_2009_p1888154732118"></a>For details about <strong id="evs_04_2009_b664802919300"><a name="evs_04_2009_b664802919300"></a><a name="evs_04_2009_b664802919300"></a>volume_image_metadata</strong>, see <strong id="evs_04_2009_b0649629203016"><a name="evs_04_2009_b0649629203016"></a><a name="evs_04_2009_b0649629203016"></a>Querying Image Details</strong> in the <em id="evs_04_2009_i186501329183018"><a name="evs_04_2009_i186501329183018"></a><a name="evs_04_2009_i186501329183018"></a>Image Management Service API Reference</em>.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameters in the  **attachments**  field

    <a name="evs_04_2067_table6503386185927"></a>
    <table><thead align="left"><tr id="evs_04_2067_row1296819185927"><th class="cellrowborder" valign="top" width="21.18%" id="mcps1.1.4.1.1"><p id="evs_04_2067_p37933504185927"><a name="evs_04_2067_p37933504185927"></a><a name="evs_04_2067_p37933504185927"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.35%" id="mcps1.1.4.1.2"><p id="evs_04_2067_p52714965185927"><a name="evs_04_2067_p52714965185927"></a><a name="evs_04_2067_p52714965185927"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.47%" id="mcps1.1.4.1.3"><p id="evs_04_2067_p50913593185927"><a name="evs_04_2067_p50913593185927"></a><a name="evs_04_2067_p50913593185927"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2067_row30360408185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p43274016185927"><a name="evs_04_2067_p43274016185927"></a><a name="evs_04_2067_p43274016185927"></a>server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p15534392185927"><a name="evs_04_2067_p15534392185927"></a><a name="evs_04_2067_p15534392185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p49891705185927"><a name="evs_04_2067_p49891705185927"></a><a name="evs_04_2067_p49891705185927"></a>Specifies the ID of the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="evs_04_2067_row49550172185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p54141023185927"><a name="evs_04_2067_p54141023185927"></a><a name="evs_04_2067_p54141023185927"></a>attachment_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p23346722185927"><a name="evs_04_2067_p23346722185927"></a><a name="evs_04_2067_p23346722185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p35416329185927"><a name="evs_04_2067_p35416329185927"></a><a name="evs_04_2067_p35416329185927"></a>Specifies the ID of the attachment information.</p>
    </td>
    </tr>
    <tr id="evs_04_2067_row35650386185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p2000176185927"><a name="evs_04_2067_p2000176185927"></a><a name="evs_04_2067_p2000176185927"></a>attached_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p27796542185927"><a name="evs_04_2067_p27796542185927"></a><a name="evs_04_2067_p27796542185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p38329099185927"><a name="evs_04_2067_p38329099185927"></a><a name="evs_04_2067_p38329099185927"></a>Specifies the time when the disk was attached.</p>
    <p id="evs_04_2067_p3414132514312"><a name="evs_04_2067_p3414132514312"></a><a name="evs_04_2067_p3414132514312"></a><span id="evs_04_2067_text7299269449"><a name="evs_04_2067_text7299269449"></a><a name="evs_04_2067_text7299269449"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="evs_04_2067_row9417574185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p24626033185927"><a name="evs_04_2067_p24626033185927"></a><a name="evs_04_2067_p24626033185927"></a>host_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p48551632185927"><a name="evs_04_2067_p48551632185927"></a><a name="evs_04_2067_p48551632185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p48591276185927"><a name="evs_04_2067_p48591276185927"></a><a name="evs_04_2067_p48591276185927"></a>Specifies the name of the physical host accommodating the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="evs_04_2067_row34668301185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p56668991185927"><a name="evs_04_2067_p56668991185927"></a><a name="evs_04_2067_p56668991185927"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p26785545185927"><a name="evs_04_2067_p26785545185927"></a><a name="evs_04_2067_p26785545185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p48959624185927"><a name="evs_04_2067_p48959624185927"></a><a name="evs_04_2067_p48959624185927"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="evs_04_2067_row41070280185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p38358373185927"><a name="evs_04_2067_p38358373185927"></a><a name="evs_04_2067_p38358373185927"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p20020490185927"><a name="evs_04_2067_p20020490185927"></a><a name="evs_04_2067_p20020490185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p22392462185927"><a name="evs_04_2067_p22392462185927"></a><a name="evs_04_2067_p22392462185927"></a>Specifies the device name.</p>
    </td>
    </tr>
    <tr id="evs_04_2067_row205574185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="evs_04_2067_p16651565185927"><a name="evs_04_2067_p16651565185927"></a><a name="evs_04_2067_p16651565185927"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="evs_04_2067_p6599487185927"><a name="evs_04_2067_p6599487185927"></a><a name="evs_04_2067_p6599487185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="evs_04_2067_p14021450185927"><a name="evs_04_2067_p14021450185927"></a><a name="evs_04_2067_p14021450185927"></a>Specifies the ID of the attached resource.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameters in the  **metadata**  field

    <a name="evs_04_3004_table3430728295554"></a>
    <table><thead align="left"><tr id="evs_04_3004_row4496975195554"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="evs_04_3004_p8809200174410"><a name="evs_04_3004_p8809200174410"></a><a name="evs_04_3004_p8809200174410"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.62%" id="mcps1.1.4.1.2"><p id="evs_04_3004_p168135017449"><a name="evs_04_3004_p168135017449"></a><a name="evs_04_3004_p168135017449"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="evs_04_3004_p1282213034412"><a name="evs_04_3004_p1282213034412"></a><a name="evs_04_3004_p1282213034412"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_3004_row456195295554"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_3004_p1562408795622"><a name="evs_04_3004_p1562408795622"></a><a name="evs_04_3004_p1562408795622"></a>__system__encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="evs_04_3004_p5759155095622"><a name="evs_04_3004_p5759155095622"></a><a name="evs_04_3004_p5759155095622"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><div class="p" id="evs_04_3004_p177192813501"><a name="evs_04_3004_p177192813501"></a><a name="evs_04_3004_p177192813501"></a>Specifies the parameter that describes the encryption function in <strong id="evs_04_3004_b84235270614509"><a name="evs_04_3004_b84235270614509"></a><a name="evs_04_3004_b84235270614509"></a>metadata</strong>. The value can be <strong id="evs_04_3004_b842352706145015"><a name="evs_04_3004_b842352706145015"></a><a name="evs_04_3004_b842352706145015"></a>0</strong> or <strong id="evs_04_3004_b842352706145020"><a name="evs_04_3004_b842352706145020"></a><a name="evs_04_3004_b842352706145020"></a>1</strong>.<a name="evs_04_3004_ul141951225145011"></a><a name="evs_04_3004_ul141951225145011"></a><ul id="evs_04_3004_ul141951225145011"><li><strong id="evs_04_3004_b842352706145038"><a name="evs_04_3004_b842352706145038"></a><a name="evs_04_3004_b842352706145038"></a>0</strong>: indicates the disk is not encrypted.</li><li><strong id="evs_04_3004_b842352706145058"><a name="evs_04_3004_b842352706145058"></a><a name="evs_04_3004_b842352706145058"></a>1</strong>: indicates the disk is encrypted.</li><li>If this parameter does not appear, the disk is not encrypted by default.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="evs_04_3004_row247050109562"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_3004_p241272995622"><a name="evs_04_3004_p241272995622"></a><a name="evs_04_3004_p241272995622"></a>__system__cmkid</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="evs_04_3004_p6121338895622"><a name="evs_04_3004_p6121338895622"></a><a name="evs_04_3004_p6121338895622"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_3004_p4159804295622"><a name="evs_04_3004_p4159804295622"></a><a name="evs_04_3004_p4159804295622"></a>Specifies the parameter that describes the encryption CMK ID in <strong id="evs_04_3004_b84235270615116"><a name="evs_04_3004_b84235270615116"></a><a name="evs_04_3004_b84235270615116"></a>metadata</strong>. This parameter is used together with <strong id="evs_04_3004_b842352706143827"><a name="evs_04_3004_b842352706143827"></a><a name="evs_04_3004_b842352706143827"></a>__system__encrypted</strong> for encryption. The length of <strong id="evs_04_3004_b84235270614396"><a name="evs_04_3004_b84235270614396"></a><a name="evs_04_3004_b84235270614396"></a>cmkid</strong> is fixed at 36 bytes.</p>
    </td>
    </tr>
    <tr id="evs_04_3004_row60499086104915"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_3004_p1478896104915"><a name="evs_04_3004_p1478896104915"></a><a name="evs_04_3004_p1478896104915"></a>hw:passthrough</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="evs_04_3004_p52681767104915"><a name="evs_04_3004_p52681767104915"></a><a name="evs_04_3004_p52681767104915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><div class="p" id="evs_04_3004_p17177177145116"><a name="evs_04_3004_p17177177145116"></a><a name="evs_04_3004_p17177177145116"></a>Specifies the parameter that describes the disk device type in <strong id="evs_04_3004_b84235270615173"><a name="evs_04_3004_b84235270615173"></a><a name="evs_04_3004_b84235270615173"></a>metadata</strong>. The value can be <strong id="evs_04_3004_b842352706151718"><a name="evs_04_3004_b842352706151718"></a><a name="evs_04_3004_b842352706151718"></a>true</strong> or <strong id="evs_04_3004_b842352706151722"><a name="evs_04_3004_b842352706151722"></a><a name="evs_04_3004_b842352706151722"></a>false</strong>.<a name="evs_04_3004_ul14462208141855"></a><a name="evs_04_3004_ul14462208141855"></a><ul id="evs_04_3004_ul14462208141855"><li>If this parameter is set to <strong id="evs_04_3004_b55868159103732"><a name="evs_04_3004_b55868159103732"></a><a name="evs_04_3004_b55868159103732"></a>true</strong>, the disk device type is SCSI, that is, Small Computer System Interface (SCSI), which allows ECS OSs to directly access the underlying storage media and supports SCSI reservation commands.</li><li>If this parameter is set to <strong>false</strong>, the disk device type is VBD (the default type), that is, Virtual Block Device (VBD), which supports only simple SCSI read/write commands.</li><li>If this parameter does not appear, the disk device type is VBD.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="evs_04_3004_row991210132288"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="evs_04_3004_p3500156018292"><a name="evs_04_3004_p3500156018292"></a><a name="evs_04_3004_p3500156018292"></a>full_clone</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="evs_04_3004_p1655411118292"><a name="evs_04_3004_p1655411118292"></a><a name="evs_04_3004_p1655411118292"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="evs_04_3004_p47931946183150"><a name="evs_04_3004_p47931946183150"></a><a name="evs_04_3004_p47931946183150"></a>Specifies the clone method. When the disk is created from a snapshot, the parameter value is <strong id="evs_04_3004_b84235270616922"><a name="evs_04_3004_b84235270616922"></a><a name="evs_04_3004_b84235270616922"></a>0</strong>, indicating the linked cloning method.</p>
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
        "volume": {
            "attachments": [],
            "availability_zone": "az-dc-1",
            "os-vol-host-attr:host": "db-rabbitmq201#LVM_iSCSI",
            "encrypted": false,
            "os-volume-replication:extended_status": null,
            "volume_image_metadata": null,
            "snapshot_id": null,
            "id": "da4f9c7a-c275-4bc9-80c4-76c7d479a218",
            "size": 1,
            "os-vol-tenant-attr:tenant_id": "3dab0aaf682849678a94ec7b5a3af2ce",
            "os-vol-mig-status-attr:migstat": null,
            "metadata": {},
            "status": "available",
            "display_description": null,
            "source_volid": null,
            "os-vol-mig-status-attr:name_id": null,
            "display_name": "test",
            "bootable": "false",
            "created_at": "2014-12-18T17:14:38.000000",
            "volume_type": "SATA",
            "multiattach": false
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
        "itemNotFound": {
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

