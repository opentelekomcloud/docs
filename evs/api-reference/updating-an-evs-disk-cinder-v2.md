# Updating an EVS Disk<a name="evs_04_2067"></a>

## Function<a name="section60214390"></a>

This API is used to update the EVS disk information.

## URI<a name="section5058598"></a>

-   URI format

    PUT /v2/\{project\_id\}/volumes/\{volume\_id\}

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

-   Parameter description

    <a name="table85492307197"></a>
    <table><thead align="left"><tr id="row15491230181913"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.5.1.1"><p id="p15491730181917"><a name="p15491730181917"></a><a name="p15491730181917"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.1.5.1.2"><p id="p1854973018195"><a name="p1854973018195"></a><a name="p1854973018195"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.1.5.1.3"><p id="p13550630141913"><a name="p13550630141913"></a><a name="p13550630141913"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="49%" id="mcps1.1.5.1.4"><p id="p1555019303199"><a name="p1555019303199"></a><a name="p1555019303199"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1055013081912"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p7550193019199"><a name="p7550193019199"></a><a name="p7550193019199"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.2 "><p id="p655083017196"><a name="p655083017196"></a><a name="p655083017196"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.3 "><p id="p165509307197"><a name="p165509307197"></a><a name="p165509307197"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="p2550143018191"><a name="p2550143018191"></a><a name="p2550143018191"></a>Specifies the information of the disk to be updated. For details, see <a href="#li44975500">Parameters in the volume field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="li44975500"></a>Parameters in the  **volume**  field

    <a name="table2126321"></a>
    <table><thead align="left"><tr id="row49924131"><th class="cellrowborder" valign="top" width="15.6%" id="mcps1.1.5.1.1"><p id="p37408856172245"><a name="p37408856172245"></a><a name="p37408856172245"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.229999999999999%" id="mcps1.1.5.1.2"><p id="p11847581"><a name="p11847581"></a><a name="p11847581"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.11%" id="mcps1.1.5.1.3"><p id="p20130041"><a name="p20130041"></a><a name="p20130041"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.059999999999995%" id="mcps1.1.5.1.4"><p id="p19920592"><a name="p19920592"></a><a name="p19920592"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64095011151910"><td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.1.5.1.1 "><p id="p17428326151912"><a name="p17428326151912"></a><a name="p17428326151912"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.2 "><p id="p2408306151912"><a name="p2408306151912"></a><a name="p2408306151912"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p60855094151912"><a name="p60855094151912"></a><a name="p60855094151912"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p30315611151912"><a name="p30315611151912"></a><a name="p30315611151912"></a>Specifies the disk name. <span id="text445196895201356"><a name="text445196895201356"></a><a name="text445196895201356"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="row22579971154332"><td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.1.5.1.1 "><p id="p38689692151834"><a name="p38689692151834"></a><a name="p38689692151834"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.2 "><p id="p46857371151834"><a name="p46857371151834"></a><a name="p46857371151834"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p37350702151834"><a name="p37350702151834"></a><a name="p37350702151834"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p5508030151834"><a name="p5508030151834"></a><a name="p5508030151834"></a>Specifies the disk description. <span id="text122876569420143"><a name="text122876569420143"></a><a name="text122876569420143"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="row8766885152152"><td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.1.5.1.1 "><p id="p24732045152159"><a name="p24732045152159"></a><a name="p24732045152159"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0098680634_p159017261855"><a name="en-us_topic_0098680634_p159017261855"></a><a name="en-us_topic_0098680634_p159017261855"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p64826762152159"><a name="p64826762152159"></a><a name="p64826762152159"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p63795990152036"><a name="p63795990152036"></a><a name="p63795990152036"></a>Specifies the disk metadata.</p>
    <p id="p16476402152159"><a name="p16476402152159"></a><a name="p16476402152159"></a><span id="text39777218152047"><a name="text39777218152047"></a><a name="text39777218152047"></a>The length of the key or value in the metadata cannot exceed 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="row62503562"><td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.1.5.1.1 "><p id="p8330898151834"><a name="p8330898151834"></a><a name="p8330898151834"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.2 "><p id="p3714153151834"><a name="p3714153151834"></a><a name="p3714153151834"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p32411005151834"><a name="p32411005151834"></a><a name="p32411005151834"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p8045749151834"><a name="p8045749151834"></a><a name="p8045749151834"></a>Specifies also the disk name. You can specify either parameter <strong id="b84235270614459"><a name="b84235270614459"></a><a name="b84235270614459"></a>name</strong> or <strong id="b842352706144516"><a name="b842352706144516"></a><a name="b842352706144516"></a>display_name</strong>. If both parameters are specified, the <strong id="b2131783664144619"><a name="b2131783664144619"></a><a name="b2131783664144619"></a>name</strong> value is used. <span id="text3940679201424"><a name="text3940679201424"></a><a name="text3940679201424"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="row20483630151827"><td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.1.5.1.1 "><p id="p26880332151834"><a name="p26880332151834"></a><a name="p26880332151834"></a>display_description</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.229999999999999%" headers="mcps1.1.5.1.2 "><p id="p29823311151834"><a name="p29823311151834"></a><a name="p29823311151834"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.1.5.1.3 "><p id="p66877970151834"><a name="p66877970151834"></a><a name="p66877970151834"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.059999999999995%" headers="mcps1.1.5.1.4 "><p id="p48406461151834"><a name="p48406461151834"></a><a name="p48406461151834"></a>Specifies also the disk description. You can specify either parameter <strong id="b184203968"><a name="b184203968"></a><a name="b184203968"></a>description</strong> or <strong id="b1703633842"><a name="b1703633842"></a><a name="b1703633842"></a>display_description</strong>. If both parameters are specified, the <strong id="b462393042"><a name="b462393042"></a><a name="b462393042"></a>description</strong> value is used. <span id="text764644858201439"><a name="text764644858201439"></a><a name="text764644858201439"></a>The value can contain a maximum of 255 bytes.</span></p>
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


## Response<a name="section7093323"></a>

-   Parameter description

    <a name="table1748117172239"></a>
    <table><thead align="left"><tr id="row20481417172314"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="p7481191752317"><a name="p7481191752317"></a><a name="p7481191752317"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="p13481191712238"><a name="p13481191712238"></a><a name="p13481191712238"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.330000000000005%" id="mcps1.1.4.1.3"><p id="p10481111716234"><a name="p10481111716234"></a><a name="p10481111716234"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row204817173238"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p16481161713233"><a name="p16481161713233"></a><a name="p16481161713233"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p74811417152312"><a name="p74811417152312"></a><a name="p74811417152312"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p3481517182317"><a name="p3481517182317"></a><a name="p3481517182317"></a>Specifies the information of the updated disk. For details, see <a href="#li3451542201439">Parameters in the volumes field</a>.</p>
    </td>
    </tr>
    <tr id="row8481121710237"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li3451542201439"></a>Parameters in the  **volumes**  field

    <a name="table34701445142557"></a>
    <table><thead align="left"><tr id="row12524911142557"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="p7884856142557"><a name="p7884856142557"></a><a name="p7884856142557"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="p34693598142557"><a name="p34693598142557"></a><a name="p34693598142557"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.330000000000005%" id="mcps1.1.4.1.3"><p id="p58539486142557"><a name="p58539486142557"></a><a name="p58539486142557"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row444782011610"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p18308336144438"><a name="p18308336144438"></a><a name="p18308336144438"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p6580236144438"><a name="p6580236144438"></a><a name="p6580236144438"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p21928856144438"><a name="p21928856144438"></a><a name="p21928856144438"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="row44077962142557"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p14226985144438"><a name="p14226985144438"></a><a name="p14226985144438"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p50073503191822"><a name="p50073503191822"></a><a name="p50073503191822"></a>list&lt;map&lt;String,String&gt;&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p50473003144438"><a name="p50473003144438"></a><a name="p50473003144438"></a>Specifies the disk URI. For details, see <a href="#li44312371185927">Parameters in the links field</a>.</p>
    </td>
    </tr>
    <tr id="row16186817142557"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p19162411144438"><a name="p19162411144438"></a><a name="p19162411144438"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p8651439144438"><a name="p8651439144438"></a><a name="p8651439144438"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p55103877144438"><a name="p55103877144438"></a><a name="p55103877144438"></a>Specifies the disk name.</p>
    </td>
    </tr>
    <tr id="row2987651144410"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p39625821144438"><a name="p39625821144438"></a><a name="p39625821144438"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p55574965144438"><a name="p55574965144438"></a><a name="p55574965144438"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p24889213144438"><a name="p24889213144438"></a><a name="p24889213144438"></a>Specifies the disk status. For details, see <a href="evs-disk-status.md">EVS Disk Status</a>.</p>
    </td>
    </tr>
    <tr id="row45785905142557"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p24843442144438"><a name="p24843442144438"></a><a name="p24843442144438"></a>attachments</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p66161799144438"><a name="p66161799144438"></a><a name="p66161799144438"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p27432950144438"><a name="p27432950144438"></a><a name="p27432950144438"></a>Specifies the disk attachment information. For details, see <a href="#li55979002185927">Parameters in the attachments field</a>.</p>
    </td>
    </tr>
    <tr id="row35247553142557"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p179170144438"><a name="p179170144438"></a><a name="p179170144438"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p14512814144438"><a name="p14512814144438"></a><a name="p14512814144438"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p58206487144438"><a name="p58206487144438"></a><a name="p58206487144438"></a>Specifies the AZ to which the disk belongs.</p>
    </td>
    </tr>
    <tr id="row27126244142557"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p19727534144438"><a name="p19727534144438"></a><a name="p19727534144438"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p54426427144438"><a name="p54426427144438"></a><a name="p54426427144438"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><div class="p" id="en-us_topic_0098680634_p8780414125315"><a name="en-us_topic_0098680634_p8780414125315"></a><a name="en-us_topic_0098680634_p8780414125315"></a>Specifies whether the disk is bootable.<a name="ul185931714111"></a><a name="ul185931714111"></a><ul id="ul185931714111"><li><strong id="b19673145419183"><a name="b19673145419183"></a><a name="b19673145419183"></a>true</strong>: specifies a bootable disk.</li><li><strong id="b667141719196"><a name="b667141719196"></a><a name="b667141719196"></a>false</strong>: specifies a non-bootable disk.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row52922635184145"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p59662004184223"><a name="p59662004184223"></a><a name="p59662004184223"></a>encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p784118184223"><a name="p784118184223"></a><a name="p784118184223"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p44329057184223"><a name="p44329057184223"></a><a name="p44329057184223"></a><span id="text63417197184223"><a name="text63417197184223"></a><a name="text63417197184223"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="row49237196142557"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p28651206144438"><a name="p28651206144438"></a><a name="p28651206144438"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p1296456144535"><a name="p1296456144535"></a><a name="p1296456144535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p28821893144438"><a name="p28821893144438"></a><a name="p28821893144438"></a>Specifies the time when the disk was created.</p>
    <p id="p586613505312"><a name="p586613505312"></a><a name="p586613505312"></a><span id="text28661350936"><a name="text28661350936"></a><a name="text28661350936"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row39017307142557"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p6085885144438"><a name="p6085885144438"></a><a name="p6085885144438"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p18611115144535"><a name="p18611115144535"></a><a name="p18611115144535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p44410693144438"><a name="p44410693144438"></a><a name="p44410693144438"></a>Specifies the disk description.</p>
    </td>
    </tr>
    <tr id="row20107664142557"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p28923171144438"><a name="p28923171144438"></a><a name="p28923171144438"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p22198851144535"><a name="p22198851144535"></a><a name="p22198851144535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p9630579144438"><a name="p9630579144438"></a><a name="p9630579144438"></a>Specifies the disk type.</p>
    </td>
    </tr>
    <tr id="row12897861142557"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p41370851144438"><a name="p41370851144438"></a><a name="p41370851144438"></a>replication_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p7354807144535"><a name="p7354807144535"></a><a name="p7354807144535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p27786537144438"><a name="p27786537144438"></a><a name="p27786537144438"></a><span id="text6498181171119"><a name="text6498181171119"></a><a name="text6498181171119"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row45680217142557"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p56617581144438"><a name="p56617581144438"></a><a name="p56617581144438"></a>consistencygroup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p25180208144535"><a name="p25180208144535"></a><a name="p25180208144535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p40860550144438"><a name="p40860550144438"></a><a name="p40860550144438"></a><span id="text13343838181111"><a name="text13343838181111"></a><a name="text13343838181111"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row47480567142557"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p58114746144438"><a name="p58114746144438"></a><a name="p58114746144438"></a>source_volid</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p47440982144535"><a name="p47440982144535"></a><a name="p47440982144535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p52975605144438"><a name="p52975605144438"></a><a name="p52975605144438"></a>Specifies the source disk ID.</p>
    <p id="p186622098367"><a name="p186622098367"></a><a name="p186622098367"></a><span id="text12532347191815"><a name="text12532347191815"></a><a name="text12532347191815"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="row31517135142557"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p31619531144438"><a name="p31619531144438"></a><a name="p31619531144438"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p66078031144535"><a name="p66078031144535"></a><a name="p66078031144535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p57055846144438"><a name="p57055846144438"></a><a name="p57055846144438"></a>Specifies the snapshot ID.</p>
    </td>
    </tr>
    <tr id="row15610713142557"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p53325033144438"><a name="p53325033144438"></a><a name="p53325033144438"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p24360403144438"><a name="p24360403144438"></a><a name="p24360403144438"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p42403730144438"><a name="p42403730144438"></a><a name="p42403730144438"></a>Specifies the disk metadata. For details, see <a href="#li29114110314">Parameters in the metadata field</a>.</p>
    </td>
    </tr>
    <tr id="row5657368142557"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p42241765144438"><a name="p42241765144438"></a><a name="p42241765144438"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p66139813144438"><a name="p66139813144438"></a><a name="p66139813144438"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p17400122144438"><a name="p17400122144438"></a><a name="p17400122144438"></a>Specifies the disk size, in GB.</p>
    </td>
    </tr>
    <tr id="row39412545144428"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p1113688144438"><a name="p1113688144438"></a><a name="p1113688144438"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p51894643144540"><a name="p51894643144540"></a><a name="p51894643144540"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p109947201368"><a name="p109947201368"></a><a name="p109947201368"></a>Reserved field</p>
    </td>
    </tr>
    <tr id="row25381049144431"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p26680804144438"><a name="p26680804144438"></a><a name="p26680804144438"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p39072645144540"><a name="p39072645144540"></a><a name="p39072645144540"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p42877354144438"><a name="p42877354144438"></a><a name="p42877354144438"></a>Specifies the time when the disk was updated.</p>
    <p id="p128341116112619"><a name="p128341116112619"></a><a name="p128341116112619"></a><span id="text19834191618261"><a name="text19834191618261"></a><a name="text19834191618261"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row48384415144425"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p51969649144438"><a name="p51969649144438"></a><a name="p51969649144438"></a>shareable</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p48792012144438"><a name="p48792012144438"></a><a name="p48792012144438"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p15113052144438"><a name="p15113052144438"></a><a name="p15113052144438"></a>Specifies whether the disk is shareable.</p>
    <div class="note" id="note1645730517525"><a name="note1645730517525"></a><a name="note1645730517525"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_p45212589213213"><a name="evs_04_2013_p45212589213213"></a><a name="evs_04_2013_p45212589213213"></a>This field is no longer used. Use <strong id="evs_04_2013_b84235270610834"><a name="evs_04_2013_b84235270610834"></a><a name="evs_04_2013_b84235270610834"></a>multiattach</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row42462677142557"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p11561839144438"><a name="p11561839144438"></a><a name="p11561839144438"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p64093800144438"><a name="p64093800144438"></a><a name="p64093800144438"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><div class="p" id="en-us_topic_0098680634_p4781191416535"><a name="en-us_topic_0098680634_p4781191416535"></a><a name="en-us_topic_0098680634_p4781191416535"></a>Specifies whether the disk is shareable.<a name="ul161621719119"></a><a name="ul161621719119"></a><ul id="ul161621719119"><li><strong id="b6752143871917"><a name="b6752143871917"></a><a name="b6752143871917"></a>true</strong>: specifies a shared disk.</li><li><strong id="b95594395195"><a name="b95594395195"></a><a name="b95594395195"></a>false</strong>: specifies a non-shared disk.</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li44312371185927"></a>Parameters in the  **links**  field

    <a name="table24355024185927"></a>
    <table><thead align="left"><tr id="row16225418185927"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="p39190461185927"><a name="p39190461185927"></a><a name="p39190461185927"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="p20310744185927"><a name="p20310744185927"></a><a name="p20310744185927"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.330000000000005%" id="mcps1.1.4.1.3"><p id="p47699944185927"><a name="p47699944185927"></a><a name="p47699944185927"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row38490285185927"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p30705403185927"><a name="p30705403185927"></a><a name="p30705403185927"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p4109689185927"><a name="p4109689185927"></a><a name="p4109689185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p53015590185927"><a name="p53015590185927"></a><a name="p53015590185927"></a>Specifies the corresponding shortcut link.</p>
    </td>
    </tr>
    <tr id="row7378265185927"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p60768596185927"><a name="p60768596185927"></a><a name="p60768596185927"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p23309219185927"><a name="p23309219185927"></a><a name="p23309219185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.330000000000005%" headers="mcps1.1.4.1.3 "><p id="p57795935185927"><a name="p57795935185927"></a><a name="p57795935185927"></a>Specifies the shortcut link marker name.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li55979002185927"></a>Parameters in the  **attachments**  field

    <a name="table6503386185927"></a>
    <table><thead align="left"><tr id="row1296819185927"><th class="cellrowborder" valign="top" width="21.18%" id="mcps1.1.4.1.1"><p id="p37933504185927"><a name="p37933504185927"></a><a name="p37933504185927"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.35%" id="mcps1.1.4.1.2"><p id="p52714965185927"><a name="p52714965185927"></a><a name="p52714965185927"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.47%" id="mcps1.1.4.1.3"><p id="p50913593185927"><a name="p50913593185927"></a><a name="p50913593185927"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row30360408185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p43274016185927"><a name="p43274016185927"></a><a name="p43274016185927"></a>server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p15534392185927"><a name="p15534392185927"></a><a name="p15534392185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p49891705185927"><a name="p49891705185927"></a><a name="p49891705185927"></a>Specifies the ID of the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="row49550172185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p54141023185927"><a name="p54141023185927"></a><a name="p54141023185927"></a>attachment_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p23346722185927"><a name="p23346722185927"></a><a name="p23346722185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p35416329185927"><a name="p35416329185927"></a><a name="p35416329185927"></a>Specifies the ID of the attachment information.</p>
    </td>
    </tr>
    <tr id="row35650386185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p2000176185927"><a name="p2000176185927"></a><a name="p2000176185927"></a>attached_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p27796542185927"><a name="p27796542185927"></a><a name="p27796542185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p38329099185927"><a name="p38329099185927"></a><a name="p38329099185927"></a>Specifies the time when the disk was attached.</p>
    <p id="p3414132514312"><a name="p3414132514312"></a><a name="p3414132514312"></a><span id="text7299269449"><a name="text7299269449"></a><a name="text7299269449"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row9417574185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p24626033185927"><a name="p24626033185927"></a><a name="p24626033185927"></a>host_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p48551632185927"><a name="p48551632185927"></a><a name="p48551632185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p48591276185927"><a name="p48591276185927"></a><a name="p48591276185927"></a>Specifies the name of the physical host accommodating the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="row34668301185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p56668991185927"><a name="p56668991185927"></a><a name="p56668991185927"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p26785545185927"><a name="p26785545185927"></a><a name="p26785545185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p48959624185927"><a name="p48959624185927"></a><a name="p48959624185927"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="row41070280185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p38358373185927"><a name="p38358373185927"></a><a name="p38358373185927"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p20020490185927"><a name="p20020490185927"></a><a name="p20020490185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p22392462185927"><a name="p22392462185927"></a><a name="p22392462185927"></a>Specifies the device name.</p>
    </td>
    </tr>
    <tr id="row205574185927"><td class="cellrowborder" valign="top" width="21.18%" headers="mcps1.1.4.1.1 "><p id="p16651565185927"><a name="p16651565185927"></a><a name="p16651565185927"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p6599487185927"><a name="p6599487185927"></a><a name="p6599487185927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.47%" headers="mcps1.1.4.1.3 "><p id="p14021450185927"><a name="p14021450185927"></a><a name="p14021450185927"></a>Specifies the ID of the attached resource.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li29114110314"></a>Parameters in the  **metadata**  field

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
            "attachments": [ ], 
            "availability_zone": "az-dc-1", 
            "bootable": "false", 
            "consistencygroup_id": null, 
            "created_at": "2016-05-25T02:38:40.392463", 
            "description": "create for api test", 
            "encrypted": false, 
            "id": "8dd7c486-8e9f-49fe-bceb-26aa7e312b66", 
            "links": [
                {
                    "href": "https://volume.localdomain.com:8776/v2/5dd0b0056f3d47b6ab4121667d35621a/volumes/8dd7c486-8e9f-49fe-bceb-26aa7e312b66", 
                    "rel": "self"
                }, 
                {
                    "href": "https://volume.localdomain.com:8776/5dd0b0056f3d47b6ab4121667d35621a/volumes/8dd7c486-8e9f-49fe-bceb-26aa7e312b66", 
                    "rel": "bookmark"
                }
            ], 
            "metadata": {
                "volume_owner": "openapi"
            }, 
            "name": "openapi_vol01", 
            "replication_status": "disabled", 
            "multiattach": false, 
            "size": 40, 
            "snapshot_id": null, 
            "source_volid": null, 
            "status": "creating", 
            "updated_at": null, 
            "user_id": "39f6696ae23740708d0f358a253c2637", 
            "volume_type": "SATA"
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

