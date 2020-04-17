# Updating an EVS Disk \(Deprecated\)<a name="evs_04_2009"></a>

## Function<a name="section41753265"></a>

This API is used to update the name and description of an EVS disk. 

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>This API has been deprecated. Use another API. For details, see  [Updating an EVS Disk](updating-an-evs-disk-cinder-v2.md).  

## URI<a name="section40235071"></a>

-   URI format

    PUT /v2/\{project\_id\}/cloudvolumes/\{volume\_id\}

-   Parameter description

    <a name="table21989419"></a>
    <table><thead align="left"><tr id="row9690616"><th class="cellrowborder" valign="top" width="22.62%" id="mcps1.1.4.1.1"><p id="p46742451"><a name="p46742451"></a><a name="p46742451"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="29.01%" id="mcps1.1.4.1.2"><p id="p28042199"><a name="p28042199"></a><a name="p28042199"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.370000000000005%" id="mcps1.1.4.1.3"><p id="p56825610"><a name="p56825610"></a><a name="p56825610"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39471735"><td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.1 "><p id="p43093956"><a name="p43093956"></a><a name="p43093956"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.01%" headers="mcps1.1.4.1.2 "><p id="p949529"><a name="p949529"></a><a name="p949529"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.370000000000005%" headers="mcps1.1.4.1.3 "><p id="p9803039"><a name="p9803039"></a><a name="p9803039"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row21118492"><td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.1 "><p id="p32876269"><a name="p32876269"></a><a name="p32876269"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.01%" headers="mcps1.1.4.1.2 "><p id="p45732164"><a name="p45732164"></a><a name="p45732164"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.370000000000005%" headers="mcps1.1.4.1.3 "><p id="p13317766"><a name="p13317766"></a><a name="p13317766"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section26571327"></a>

-   Parameter description

    <a name="table56177481416"></a>
    <table><thead align="left"><tr id="row19617104815119"><th class="cellrowborder" valign="top" width="16%" id="mcps1.1.5.1.1"><p id="p106178485120"><a name="p106178485120"></a><a name="p106178485120"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.1.5.1.2"><p id="p1361817480115"><a name="p1361817480115"></a><a name="p1361817480115"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.1.5.1.3"><p id="p161813481016"><a name="p161813481016"></a><a name="p161813481016"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="49%" id="mcps1.1.5.1.4"><p id="p76189487116"><a name="p76189487116"></a><a name="p76189487116"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row146181485120"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.1 "><p id="p1261817484111"><a name="p1261817484111"></a><a name="p1261817484111"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p1061818481218"><a name="p1061818481218"></a><a name="p1061818481218"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.3 "><p id="p176183483115"><a name="p176183483115"></a><a name="p176183483115"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="p20618248316"><a name="p20618248316"></a><a name="p20618248316"></a>Specifies the information of the disk to be updated. For details, see <a href="#li44975500">Parameters in the volume field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="li44975500"></a>Parameters in the  **volume**  field

    <a name="table2126321"></a>
    <table><thead align="left"><tr id="row49924131"><th class="cellrowborder" valign="top" width="15.6%" id="mcps1.1.5.1.1"><p id="p37408856172245"><a name="p37408856172245"></a><a name="p37408856172245"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.98%" id="mcps1.1.5.1.2"><p id="p11847581"><a name="p11847581"></a><a name="p11847581"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.990000000000002%" id="mcps1.1.5.1.3"><p id="p20130041"><a name="p20130041"></a><a name="p20130041"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.43%" id="mcps1.1.5.1.4"><p id="p19920592"><a name="p19920592"></a><a name="p19920592"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45067606"><td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.1.5.1.1 "><p id="p26597492"><a name="p26597492"></a><a name="p26597492"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.1.5.1.2 "><p id="p6913218"><a name="p6913218"></a><a name="p6913218"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.5.1.3 "><p id="p10871744171339"><a name="p10871744171339"></a><a name="p10871744171339"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.43%" headers="mcps1.1.5.1.4 "><p id="p30183810114010"><a name="p30183810114010"></a><a name="p30183810114010"></a>Specifies the new name of the disk. Parameters <strong id="b842352706114843"><a name="b842352706114843"></a><a name="b842352706114843"></a>name</strong> and <strong id="b842352706114849"><a name="b842352706114849"></a><a name="b842352706114849"></a>description</strong> cannot be null at the same time. <span id="text52688164811494"><a name="text52688164811494"></a><a name="text52688164811494"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="row62503562"><td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.1.5.1.1 "><p id="p29623765"><a name="p29623765"></a><a name="p29623765"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.1.5.1.2 "><p id="p50714740"><a name="p50714740"></a><a name="p50714740"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.5.1.3 "><p id="p14253264"><a name="p14253264"></a><a name="p14253264"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.43%" headers="mcps1.1.5.1.4 "><p id="p66104967114034"><a name="p66104967114034"></a><a name="p66104967114034"></a>Specifies the new description of the disk. <strong id="b1919190910114922"><a name="b1919190910114922"></a><a name="b1919190910114922"></a>name</strong> and <strong id="b1222832112114922"><a name="b1222832112114922"></a><a name="b1222832112114922"></a>description</strong> cannot be null at the same time. <span id="text1709662760114924"><a name="text1709662760114924"></a><a name="text1709662760114924"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "volume": {
            "name": "test_volume", 
            "description": "test"
        }
    }
    ```


## Response<a name="section37815352"></a>

-   Parameter description

    <a name="table27929698142532"></a>
    <table><thead align="left"><tr id="row42153167142532"><th class="cellrowborder" valign="top" width="21.18%" id="mcps1.1.4.1.1"><p id="p58963386142532"><a name="p58963386142532"></a><a name="p58963386142532"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.35%" id="mcps1.1.4.1.2"><p id="p11304974142532"><a name="p11304974142532"></a><a name="p11304974142532"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.47%" id="mcps1.1.4.1.3"><p id="p16640014142532"><a name="p16640014142532"></a><a name="p16640014142532"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5663883142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p56121360142532"><a name="p56121360142532"></a><a name="p56121360142532"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p49536326142532"><a name="p49536326142532"></a><a name="p49536326142532"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p66719203142532"><a name="p66719203142532"></a><a name="p66719203142532"></a><span id="text193761052172315"><a name="text193761052172315"></a><a name="text193761052172315"></a>Specifies the disk ID.</span></p>
    </td>
    </tr>
    <tr id="row63601923142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p51482101142532"><a name="p51482101142532"></a><a name="p51482101142532"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p9300668142532"><a name="p9300668142532"></a><a name="p9300668142532"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p19730920142532"><a name="p19730920142532"></a><a name="p19730920142532"></a>Specifies the disk URI. For details, see <a href="#li949885516582">Parameters in the links field</a>.</p>
    </td>
    </tr>
    <tr id="row43360557142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p22544263142532"><a name="p22544263142532"></a><a name="p22544263142532"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p14146042142532"><a name="p14146042142532"></a><a name="p14146042142532"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p624200142532"><a name="p624200142532"></a><a name="p624200142532"></a>Specifies the disk name.</p>
    </td>
    </tr>
    <tr id="row5617804142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p52389016142532"><a name="p52389016142532"></a><a name="p52389016142532"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p15651871142532"><a name="p15651871142532"></a><a name="p15651871142532"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p15368644142532"><a name="p15368644142532"></a><a name="p15368644142532"></a>Specifies the disk status. For details, see <a href="evs-disk-status.md">EVS Disk Status</a>.</p>
    </td>
    </tr>
    <tr id="row4100073142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p63670463142532"><a name="p63670463142532"></a><a name="p63670463142532"></a>attachments</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p57033878142532"><a name="p57033878142532"></a><a name="p57033878142532"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p250469142532"><a name="p250469142532"></a><a name="p250469142532"></a>Specifies the disk attachment information. For details, see <a href="#li2847936164017">Parameters in the attachments field</a>.</p>
    </td>
    </tr>
    <tr id="row2254227142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p48374687142532"><a name="p48374687142532"></a><a name="p48374687142532"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p26035535142532"><a name="p26035535142532"></a><a name="p26035535142532"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p27087292142532"><a name="p27087292142532"></a><a name="p27087292142532"></a>Specifies the AZ to which the disk belongs.</p>
    </td>
    </tr>
    <tr id="row42459044142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p16630559142532"><a name="p16630559142532"></a><a name="p16630559142532"></a>source_volid</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p4898051142532"><a name="p4898051142532"></a><a name="p4898051142532"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p58075939142532"><a name="p58075939142532"></a><a name="p58075939142532"></a>Specifies the source disk ID. This parameter has a value if the disk is created from a source disk.</p>
    <p id="p48931232104211"><a name="p48931232104211"></a><a name="p48931232104211"></a><span id="text88578719717"><a name="text88578719717"></a><a name="text88578719717"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="row52921406142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p58775474142532"><a name="p58775474142532"></a><a name="p58775474142532"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p63192947142532"><a name="p63192947142532"></a><a name="p63192947142532"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p10363897142532"><a name="p10363897142532"></a><a name="p10363897142532"></a>Specifies the snapshot ID. This parameter has a value if the disk is created from a snapshot.</p>
    </td>
    </tr>
    <tr id="row26166216142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p39088784142532"><a name="p39088784142532"></a><a name="p39088784142532"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p12074920142532"><a name="p12074920142532"></a><a name="p12074920142532"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p35091945142532"><a name="p35091945142532"></a><a name="p35091945142532"></a>Specifies the disk description.</p>
    </td>
    </tr>
    <tr id="row47392053142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p13551098142532"><a name="p13551098142532"></a><a name="p13551098142532"></a>os-vol-tenant-attr:tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p23897139142532"><a name="p23897139142532"></a><a name="p23897139142532"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p22825763142532"><a name="p22825763142532"></a><a name="p22825763142532"></a>Specifies the ID of the tenant to which the disk belongs. Currently, the returned parameter value is invalid. <span id="text19941457165313"><a name="text19941457165313"></a><a name="text19941457165313"></a>The tenant ID is actually the project ID.</span></p>
    </td>
    </tr>
    <tr id="row4105277142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p64092025142532"><a name="p64092025142532"></a><a name="p64092025142532"></a>volume_image_metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p24071533142532"><a name="p24071533142532"></a><a name="p24071533142532"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p26176672142532"><a name="p26176672142532"></a><a name="p26176672142532"></a>Specifies the metadata of the disk image. Currently, the returned parameter value is invalid.</p>
    <div class="note" id="note1151018162014"><a name="note1151018162014"></a><a name="note1151018162014"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1888154732118"><a name="p1888154732118"></a><a name="p1888154732118"></a>For details about <strong id="b664802919300"><a name="b664802919300"></a><a name="b664802919300"></a>volume_image_metadata</strong>, see <strong id="b0649629203016"><a name="b0649629203016"></a><a name="b0649629203016"></a>Querying Image Details</strong> in the <em id="i186501329183018"><a name="i186501329183018"></a><a name="i186501329183018"></a>Image Management Service API Reference</em>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row34263457142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p23876638142532"><a name="p23876638142532"></a><a name="p23876638142532"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p54959544142532"><a name="p54959544142532"></a><a name="p54959544142532"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p13644385142532"><a name="p13644385142532"></a><a name="p13644385142532"></a>Specifies the time when the disk was created.</p>
    <p id="p4374122920318"><a name="p4374122920318"></a><a name="p4374122920318"></a><span id="text15641134183120"><a name="text15641134183120"></a><a name="text15641134183120"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row55690602142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p14644931142532"><a name="p14644931142532"></a><a name="p14644931142532"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p45388732142532"><a name="p45388732142532"></a><a name="p45388732142532"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p47786148539"><a name="en-us_topic_0098680634_p47786148539"></a><a name="en-us_topic_0098680634_p47786148539"></a>Specifies the disk type.</p>
    </td>
    </tr>
    <tr id="row32535337142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p18116679142532"><a name="p18116679142532"></a><a name="p18116679142532"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p58164905142532"><a name="p58164905142532"></a><a name="p58164905142532"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p38946139142532"><a name="p38946139142532"></a><a name="p38946139142532"></a>Specifies the disk size, in GB.</p>
    </td>
    </tr>
    <tr id="row14970936142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p4686293142532"><a name="p4686293142532"></a><a name="p4686293142532"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p44045434142532"><a name="p44045434142532"></a><a name="p44045434142532"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><div class="p" id="en-us_topic_0098680634_p8780414125315"><a name="en-us_topic_0098680634_p8780414125315"></a><a name="en-us_topic_0098680634_p8780414125315"></a>Specifies whether the disk is bootable.<a name="ul185931714111"></a><a name="ul185931714111"></a><ul id="ul185931714111"><li><strong id="b11471151605411"><a name="b11471151605411"></a><a name="b11471151605411"></a>true</strong>: specifies a bootable disk.</li><li><strong id="b273062095419"><a name="b273062095419"></a><a name="b273062095419"></a>false</strong>: specifies a non-bootable disk.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row34847734142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p4094237142532"><a name="p4094237142532"></a><a name="p4094237142532"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p63197743142532"><a name="p63197743142532"></a><a name="p63197743142532"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p41834554142532"><a name="p41834554142532"></a><a name="p41834554142532"></a>Specifies the disk metadata. For details, see <a href="#li6221175494947">Parameters in the metadata field</a>.</p>
    </td>
    </tr>
    <tr id="row40966670142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p29965975142532"><a name="p29965975142532"></a><a name="p29965975142532"></a>os-vol-host-attr:host</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p11324945142532"><a name="p11324945142532"></a><a name="p11324945142532"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p13457143142532"><a name="p13457143142532"></a><a name="p13457143142532"></a><span id="text203605127103"><a name="text203605127103"></a><a name="text203605127103"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row2027692114591"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p48928701145954"><a name="p48928701145954"></a><a name="p48928701145954"></a>shareable</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p3801857145954"><a name="p3801857145954"></a><a name="p3801857145954"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p46595553145954"><a name="p46595553145954"></a><a name="p46595553145954"></a>Specifies whether the disk is shareable.</p>
    <div class="note" id="note3800959821323"><a name="note3800959821323"></a><a name="note3800959821323"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p45212589213213"><a name="p45212589213213"></a><a name="p45212589213213"></a>This field is no longer used. Use <strong id="b84235270610834"><a name="b84235270610834"></a><a name="b84235270610834"></a>multiattach</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row54005424142532"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0044524833_p129522216412"><a name="en-us_topic_0044524833_p129522216412"></a><a name="en-us_topic_0044524833_p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0044524833_p1595262111415"><a name="en-us_topic_0044524833_p1595262111415"></a><a name="en-us_topic_0044524833_p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0044524833_p109527215417"><a name="en-us_topic_0044524833_p109527215417"></a><a name="en-us_topic_0044524833_p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    <tr id="row36470043213458"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p3792196213528"><a name="p3792196213528"></a><a name="p3792196213528"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p38732436213528"><a name="p38732436213528"></a><a name="p38732436213528"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><div class="p" id="en-us_topic_0098680634_p4781191416535"><a name="en-us_topic_0098680634_p4781191416535"></a><a name="en-us_topic_0098680634_p4781191416535"></a>Specifies whether the disk is shareable.<a name="ul161621719119"></a><a name="ul161621719119"></a><ul id="ul161621719119"><li><strong id="b54016233545"><a name="b54016233545"></a><a name="b54016233545"></a>true</strong>: specifies a shared disk.</li><li><strong id="b1813562425420"><a name="b1813562425420"></a><a name="b1813562425420"></a>false</strong>: specifies a non-shared disk.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row9244758141817"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0098680634_p978017142534"><a name="en-us_topic_0098680634_p978017142534"></a><a name="en-us_topic_0098680634_p978017142534"></a>os-volume-replication:extended_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p12780191455320"><a name="en-us_topic_0098680634_p12780191455320"></a><a name="en-us_topic_0098680634_p12780191455320"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0098680634_p278051495317"><a name="en-us_topic_0098680634_p278051495317"></a><a name="en-us_topic_0098680634_p278051495317"></a><span id="text379518478151"><a name="text379518478151"></a><a name="text379518478151"></a>Reserved field</span></p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li949885516582"></a>Parameters in the  **links**  field

    <a name="table44453603165834"></a>
    <table><thead align="left"><tr id="row67020808165834"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="p59976390165834"><a name="p59976390165834"></a><a name="p59976390165834"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="p43343669105259"><a name="p43343669105259"></a><a name="p43343669105259"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p45826298165834"><a name="p45826298165834"></a><a name="p45826298165834"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20942657165834"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p18633648165834"><a name="p18633648165834"></a><a name="p18633648165834"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p21176318105259"><a name="p21176318105259"></a><a name="p21176318105259"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p50128425165834"><a name="p50128425165834"></a><a name="p50128425165834"></a>Specifies the corresponding shortcut link.</p>
    </td>
    </tr>
    <tr id="row48502642165834"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p36399890165834"><a name="p36399890165834"></a><a name="p36399890165834"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p37560167105259"><a name="p37560167105259"></a><a name="p37560167105259"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p46341215165834"><a name="p46341215165834"></a><a name="p46341215165834"></a>Specifies the shortcut link marker name.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li2847936164017"></a>Parameters in the  **attachments**  field

    <a name="table3307491164033"></a>
    <table><thead align="left"><tr id="row21424691164033"><th class="cellrowborder" valign="top" width="21.687831216878315%" id="mcps1.1.4.1.1"><p id="p57678439164033"><a name="p57678439164033"></a><a name="p57678439164033"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.687831216878315%" id="mcps1.1.4.1.2"><p id="p66852304105349"><a name="p66852304105349"></a><a name="p66852304105349"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.624337566243376%" id="mcps1.1.4.1.3"><p id="p1357476164033"><a name="p1357476164033"></a><a name="p1357476164033"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42846717164033"><td class="cellrowborder" valign="top" width="21.687831216878315%" headers="mcps1.1.4.1.1 "><p id="p48032051164033"><a name="p48032051164033"></a><a name="p48032051164033"></a>server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.687831216878315%" headers="mcps1.1.4.1.2 "><p id="p46327539105349"><a name="p46327539105349"></a><a name="p46327539105349"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p62170963164033"><a name="p62170963164033"></a><a name="p62170963164033"></a>Specifies the ID of the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="row22667763164033"><td class="cellrowborder" valign="top" width="21.687831216878315%" headers="mcps1.1.4.1.1 "><p id="p24149511164033"><a name="p24149511164033"></a><a name="p24149511164033"></a>attachment_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.687831216878315%" headers="mcps1.1.4.1.2 "><p id="p61543187105349"><a name="p61543187105349"></a><a name="p61543187105349"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p919418164033"><a name="p919418164033"></a><a name="p919418164033"></a>Specifies the ID of the attachment information.</p>
    </td>
    </tr>
    <tr id="row57853019113651"><td class="cellrowborder" valign="top" width="21.687831216878315%" headers="mcps1.1.4.1.1 "><p id="p50055523113657"><a name="p50055523113657"></a><a name="p50055523113657"></a>attached_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.687831216878315%" headers="mcps1.1.4.1.2 "><p id="p27965571113657"><a name="p27965571113657"></a><a name="p27965571113657"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p6478808113657"><a name="p6478808113657"></a><a name="p6478808113657"></a>Specifies the time when the disk was attached.</p>
    <p id="p692624863119"><a name="p692624863119"></a><a name="p692624863119"></a><span id="text13941449123112"><a name="text13941449123112"></a><a name="text13941449123112"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row8274763164033"><td class="cellrowborder" valign="top" width="21.687831216878315%" headers="mcps1.1.4.1.1 "><p id="p66276072164033"><a name="p66276072164033"></a><a name="p66276072164033"></a>host_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.687831216878315%" headers="mcps1.1.4.1.2 "><p id="p18942231105349"><a name="p18942231105349"></a><a name="p18942231105349"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p38983264164033"><a name="p38983264164033"></a><a name="p38983264164033"></a>Specifies the name of the physical host accommodating the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="row15305060164033"><td class="cellrowborder" valign="top" width="21.687831216878315%" headers="mcps1.1.4.1.1 "><p id="p31750372164033"><a name="p31750372164033"></a><a name="p31750372164033"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.687831216878315%" headers="mcps1.1.4.1.2 "><p id="p57925736105349"><a name="p57925736105349"></a><a name="p57925736105349"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p8281462164033"><a name="p8281462164033"></a><a name="p8281462164033"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="row7424294164033"><td class="cellrowborder" valign="top" width="21.687831216878315%" headers="mcps1.1.4.1.1 "><p id="p64496914164033"><a name="p64496914164033"></a><a name="p64496914164033"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.687831216878315%" headers="mcps1.1.4.1.2 "><p id="p61473005105349"><a name="p61473005105349"></a><a name="p61473005105349"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p42870577164033"><a name="p42870577164033"></a><a name="p42870577164033"></a>Specifies the device name.</p>
    </td>
    </tr>
    <tr id="row50290878164033"><td class="cellrowborder" valign="top" width="21.687831216878315%" headers="mcps1.1.4.1.1 "><p id="p47029330164033"><a name="p47029330164033"></a><a name="p47029330164033"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.687831216878315%" headers="mcps1.1.4.1.2 "><p id="p13257486105349"><a name="p13257486105349"></a><a name="p13257486105349"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p59986642164033"><a name="p59986642164033"></a><a name="p59986642164033"></a>Specifies the ID of the attached resource.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li6221175494947"></a>Parameters in the  **metadata**  field

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
        "id": "36ba39af-3579-4e6e-adfc-b764349c0f77", 
        "links": [
            {
                "href": "https://volume.region.xxx.xxx-tsi.de/v2/3cfb09080bd944d0b4cdd72ef26857bd/volumes/36ba39af-3579-4e6e-adfc-b764349c0f77", 
                "rel": "self"
            }, 
            {
                "href": "https://volume.region.xxx.xxx-tsi.de/3cfb09080bd944d0b4cdd72ef26857bd/volumes/36ba39af-3579-4e6e-adfc-b764349c0f77", 
                "rel": "bookmark"
            }
        ], 
        "name": "newVolume", 
        "status": "in-use", 
        "attachments": [
            {
                "server_id": "c3d3250c-7ce5-42cc-b620-dd2b63d19ca5", 
                "attachment_id": "011a2bdb-a033-4479-845b-50bd8ed7f4d4", 
                "attached_at": "2017-05-23T11:27:38.604815", 
                "host_name": null, 
                "volume_id": "36ba39af-3579-4e6e-adfc-b764349c0f77", 
                "device": "/dev/sdf", 
                "id": "36ba39af-3579-4e6e-adfc-b764349c0f77"
            }
        ], 
        "description": "new volume", 
        "multiattach": false, 
        "shareable": false, 
        "size": 10, 
        "metadata": {
            "policy": "dc71a9c9-b3fa-429d-a070-037682d82d21", 
            "attached_mode": "rw", 
            "readonly": "False", 
            "hw:passthrough": "false"
        }, 
        "bootable": "false", 
        "availability_zone": "az-dc-1", 
        "os-vol-host-attr:host": null, 
        "source_volid": null, 
        "snapshot_id": null, 
        "created_at": "2017-05-23T09:49:44.481299", 
        "volume_type": "SATA", 
        "os-vol-tenant-attr:tenant_id": null, 
        "os-volume-replication:extended_status": null,
        "volume_image_metadata": null
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


## Status Codes<a name="section4793853"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

