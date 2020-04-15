# Creating EVS Disks<a name="evs_04_3003"></a>

## Function<a name="section2630087"></a>

This API is used to create one or multiple EVS disks. 

## URI<a name="section23670787"></a>

-   URI format

    POST /v3/\{project\_id\}/cloudvolumes

-   Parameter description

    <a name="table35460209"></a>
    <table><thead align="left"><tr id="row34639550"><th class="cellrowborder" valign="top" width="28.822882288228826%" id="mcps1.1.4.1.1"><p id="p54340147"><a name="p54340147"></a><a name="p54340147"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.752675267526755%" id="mcps1.1.4.1.2"><p id="p39475801"><a name="p39475801"></a><a name="p39475801"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.42444244424442%" id="mcps1.1.4.1.3"><p id="p43423319"><a name="p43423319"></a><a name="p43423319"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row27627990"><td class="cellrowborder" valign="top" width="28.822882288228826%" headers="mcps1.1.4.1.1 "><p id="p23274750"><a name="p23274750"></a><a name="p23274750"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.752675267526755%" headers="mcps1.1.4.1.2 "><p id="p6206582"><a name="p6206582"></a><a name="p6206582"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.42444244424442%" headers="mcps1.1.4.1.3 "><p id="p32971110"><a name="p32971110"></a><a name="p32971110"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section11710498"></a>

-   Parameter description

    <a name="evs_04_2013_table99446146381"></a>
    <table><thead align="left"><tr id="evs_04_2013_row14945201493812"><th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.1.5.1.1"><p id="evs_04_2013_p49451414203813"><a name="evs_04_2013_p49451414203813"></a><a name="evs_04_2013_p49451414203813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.1.5.1.2"><p id="evs_04_2013_p7945514153819"><a name="evs_04_2013_p7945514153819"></a><a name="evs_04_2013_p7945514153819"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.1.5.1.3"><p id="evs_04_2013_p14945114203813"><a name="evs_04_2013_p14945114203813"></a><a name="evs_04_2013_p14945114203813"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.515151515151516%" id="mcps1.1.5.1.4"><p id="evs_04_2013_p4946111443810"><a name="evs_04_2013_p4946111443810"></a><a name="evs_04_2013_p4946111443810"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2013_row11946111410383"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p11946214173818"><a name="evs_04_2013_p11946214173818"></a><a name="evs_04_2013_p11946214173818"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p394615141385"><a name="evs_04_2013_p394615141385"></a><a name="evs_04_2013_p394615141385"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p1494601423811"><a name="evs_04_2013_p1494601423811"></a><a name="evs_04_2013_p1494601423811"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="evs_04_2013_p9946141418386"><a name="evs_04_2013_p9946141418386"></a><a name="evs_04_2013_p9946141418386"></a>Specifies the information of the disks to be created. For details, see <a href="#evs_04_2013_li10966323">Parameters in the volume field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2013_li10966323"></a>Parameters in the  **volume**  field

    <a name="evs_04_2013_table31588048"></a>
    <table><thead align="left"><tr id="evs_04_2013_row57330849"><th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.1.5.1.1"><p id="evs_04_2013_p13287175"><a name="evs_04_2013_p13287175"></a><a name="evs_04_2013_p13287175"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.1.5.1.2"><p id="evs_04_2013_p2519427"><a name="evs_04_2013_p2519427"></a><a name="evs_04_2013_p2519427"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.1.5.1.3"><p id="evs_04_2013_p2747002"><a name="evs_04_2013_p2747002"></a><a name="evs_04_2013_p2747002"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.515151515151516%" id="mcps1.1.5.1.4"><p id="evs_04_2013_p21180630"><a name="evs_04_2013_p21180630"></a><a name="evs_04_2013_p21180630"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2013_row56407950"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p5641212"><a name="evs_04_2013_p5641212"></a><a name="evs_04_2013_p5641212"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p54284994"><a name="evs_04_2013_p54284994"></a><a name="evs_04_2013_p54284994"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p35008393"><a name="evs_04_2013_p35008393"></a><a name="evs_04_2013_p35008393"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="evs_04_2013_p17107576"><a name="evs_04_2013_p17107576"></a><a name="evs_04_2013_p17107576"></a>Specifies the ID of the backup that can be used to create a disk. This parameter is mandatory when you use a backup to create the disk.</p>
    <div class="note" id="evs_04_2013_note4897195216919"><a name="evs_04_2013_note4897195216919"></a><a name="evs_04_2013_note4897195216919"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_p1369572181217"><a name="evs_04_2013_p1369572181217"></a><a name="evs_04_2013_p1369572181217"></a>For how to obtain the backup ID, see <strong id="evs_04_2013_b14360201993219"><a name="evs_04_2013_b14360201993219"></a><a name="evs_04_2013_b14360201993219"></a>Querying Details About VBS Backups (Native OpenStack API)</strong> in the <em id="evs_04_2013_i295602815315"><a name="evs_04_2013_i295602815315"></a><a name="evs_04_2013_i295602815315"></a>Volume Backup Service API Reference</em>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="evs_04_2013_row19750463"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p56283646"><a name="evs_04_2013_p56283646"></a><a name="evs_04_2013_p56283646"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p62681466"><a name="evs_04_2013_p62681466"></a><a name="evs_04_2013_p62681466"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p12823082184254"><a name="evs_04_2013_p12823082184254"></a><a name="evs_04_2013_p12823082184254"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="evs_04_2013_p66510234184157"><a name="evs_04_2013_p66510234184157"></a><a name="evs_04_2013_p66510234184157"></a>Specifies the AZ where you want to create the disk. If the AZ does not exist, the disk will fail to create.</p>
    <div class="note" id="evs_04_2013_note18354235112810"><a name="evs_04_2013_note18354235112810"></a><a name="evs_04_2013_note18354235112810"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_p14110155594414"><a name="evs_04_2013_p14110155594414"></a><a name="evs_04_2013_p14110155594414"></a>For details about how to obtain the AZ, see <a href="querying-all-azs-cinder-v2.md">Querying All AZs</a>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="evs_04_2013_row22709757"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p27551015"><a name="evs_04_2013_p27551015"></a><a name="evs_04_2013_p27551015"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p17039762"><a name="evs_04_2013_p17039762"></a><a name="evs_04_2013_p17039762"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p38043494"><a name="evs_04_2013_p38043494"></a><a name="evs_04_2013_p38043494"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="evs_04_2013_p58865735113756"><a name="evs_04_2013_p58865735113756"></a><a name="evs_04_2013_p58865735113756"></a>Specifies the disk description. <span id="evs_04_2013_text110681216113820"><a name="evs_04_2013_text110681216113820"></a><a name="evs_04_2013_text110681216113820"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="evs_04_2013_row17746329"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p28166553"><a name="evs_04_2013_p28166553"></a><a name="evs_04_2013_p28166553"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p66898301"><a name="evs_04_2013_p66898301"></a><a name="evs_04_2013_p66898301"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p50053294"><a name="evs_04_2013_p50053294"></a><a name="evs_04_2013_p50053294"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><div class="p" id="evs_04_2013_p27784979"><a name="evs_04_2013_p27784979"></a><a name="evs_04_2013_p27784979"></a>Specifies the disk size, in GB. Its value can be as follows:<a name="evs_04_2013_ul24506304547"></a><a name="evs_04_2013_ul24506304547"></a><ul id="evs_04_2013_ul24506304547"><li>System disk: 1 GB to 1024 GB</li><li>Data disk: 10 GB to 32768 GB</li></ul>
    </div>
    <p id="evs_04_2013_p1869819398426"><a name="evs_04_2013_p1869819398426"></a><a name="evs_04_2013_p1869819398426"></a>This parameter is mandatory when you create an empty disk. You can specify the parameter value as required within the value range.</p>
    <p id="evs_04_2013_p433134181712"><a name="evs_04_2013_p433134181712"></a><a name="evs_04_2013_p433134181712"></a>This parameter is mandatory when you create the disk from a snapshot. Ensure that the disk size is greater than or equal to the snapshot size.</p>
    <p id="evs_04_2013_p108486266429"><a name="evs_04_2013_p108486266429"></a><a name="evs_04_2013_p108486266429"></a>This parameter is mandatory when you create the disk from an image. Ensure that the disk size is greater than or equal to the minimum disk capacity required by <strong id="evs_04_2013_b11901953203815"><a name="evs_04_2013_b11901953203815"></a><a name="evs_04_2013_b11901953203815"></a>min_disk</strong> in the image attributes.</p>
    <p id="evs_04_2013_p55481787"><a name="evs_04_2013_p55481787"></a><a name="evs_04_2013_p55481787"></a>This parameter is optional when you create the disk from a backup. If this parameter is not specified, the disk size is equal to the backup size.</p>
    <div class="note" id="evs_04_2013_note6528620415911"><a name="evs_04_2013_note6528620415911"></a><a name="evs_04_2013_note6528620415911"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_p5070492815911"><a name="evs_04_2013_p5070492815911"></a><a name="evs_04_2013_p5070492815911"></a>If the specified parameter value is a decimal, the integral part of the value is used by default when the request is sent.</p>
    </div></div>
    </td>
    </tr>
    <tr id="evs_04_2013_row29574043"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p46687245"><a name="evs_04_2013_p46687245"></a><a name="evs_04_2013_p46687245"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p23570516"><a name="evs_04_2013_p23570516"></a><a name="evs_04_2013_p23570516"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p30163672"><a name="evs_04_2013_p30163672"></a><a name="evs_04_2013_p30163672"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="evs_04_2013_p30342314172932"><a name="evs_04_2013_p30342314172932"></a><a name="evs_04_2013_p30342314172932"></a>Specifies the disk name.</p>
    <a name="evs_04_2013_ul46606633102055"></a><a name="evs_04_2013_ul46606633102055"></a><ul id="evs_04_2013_ul46606633102055"><li>If you create disks one by one, the <strong id="evs_04_2013_b842352706172858"><a name="evs_04_2013_b842352706172858"></a><a name="evs_04_2013_b842352706172858"></a>name</strong> value is the disk name. <span id="evs_04_2013_text101368932114053"><a name="evs_04_2013_text101368932114053"></a><a name="evs_04_2013_text101368932114053"></a>The value can contain a maximum of 255 bytes.</span></li><li>If you create multiple disks (the <strong id="evs_04_2013_b153177451299"><a name="evs_04_2013_b153177451299"></a><a name="evs_04_2013_b153177451299"></a>count</strong> value is greater than <strong id="evs_04_2013_b9330184518293"><a name="evs_04_2013_b9330184518293"></a><a name="evs_04_2013_b9330184518293"></a>1</strong>), the system automatically adds a hyphen followed by a four-digit incremental number, such as <strong id="evs_04_2013_b9331345192917"><a name="evs_04_2013_b9331345192917"></a><a name="evs_04_2013_b9331345192917"></a>-0000</strong>, to the end of each disk name. For example, the disk names can be <strong id="evs_04_2013_b682272110417"><a name="evs_04_2013_b682272110417"></a><a name="evs_04_2013_b682272110417"></a>volume-0001</strong> and <strong id="evs_04_2013_b187076249411"><a name="evs_04_2013_b187076249411"></a><a name="evs_04_2013_b187076249411"></a>volume-0002</strong>. <span id="evs_04_2013_text688013214465"><a name="evs_04_2013_text688013214465"></a><a name="evs_04_2013_text688013214465"></a>The value can contain a maximum of 250 bytes.</span></li></ul>
    </td>
    </tr>
    <tr id="evs_04_2013_row30068235161750"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p41087296161752"><a name="evs_04_2013_p41087296161752"></a><a name="evs_04_2013_p41087296161752"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p39736646161752"><a name="evs_04_2013_p39736646161752"></a><a name="evs_04_2013_p39736646161752"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p64551757161752"><a name="evs_04_2013_p64551757161752"></a><a name="evs_04_2013_p64551757161752"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="evs_04_2013_p61309820161752"><a name="evs_04_2013_p61309820161752"></a><a name="evs_04_2013_p61309820161752"></a>Specifies the snapshot ID. If this parameter is specified, the disk is created from a snapshot.</p>
    <div class="note" id="evs_04_2013_note13293123112911"><a name="evs_04_2013_note13293123112911"></a><a name="evs_04_2013_note13293123112911"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_p129419232297"><a name="evs_04_2013_p129419232297"></a><a name="evs_04_2013_p129419232297"></a>For details about how to obtain the snapshot ID, see <a href="querying-details-about-evs-snapshots-cinder-v2.md">Querying Details About EVS Snapshots</a>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="evs_04_2013_row65447007"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p66716242"><a name="evs_04_2013_p66716242"></a><a name="evs_04_2013_p66716242"></a>imageRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p35306501"><a name="evs_04_2013_p35306501"></a><a name="evs_04_2013_p35306501"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p41254304"><a name="evs_04_2013_p41254304"></a><a name="evs_04_2013_p41254304"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="evs_04_2013_p53264332"><a name="evs_04_2013_p53264332"></a><a name="evs_04_2013_p53264332"></a>Specifies the image ID. If this parameter is specified, the disk is created from an image.</p>
    <div class="note" id="evs_04_2013_note13789049151930"><a name="evs_04_2013_note13789049151930"></a><a name="evs_04_2013_note13789049151930"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_p56992577151930"><a name="evs_04_2013_p56992577151930"></a><a name="evs_04_2013_p56992577151930"></a>BMS system disks cannot be created from BMS images.</p>
    <p id="evs_04_2013_p257253253318"><a name="evs_04_2013_p257253253318"></a><a name="evs_04_2013_p257253253318"></a>For details about how to obtain the image ID, see <strong id="evs_04_2013_b53641122183918"><a name="evs_04_2013_b53641122183918"></a><a name="evs_04_2013_b53641122183918"></a>Querying Images</strong> in the <em id="evs_04_2013_i448612173612"><a name="evs_04_2013_i448612173612"></a><a name="evs_04_2013_i448612173612"></a>Image Management Service API Reference</em>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="evs_04_2013_row9616944"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p40774967"><a name="evs_04_2013_p40774967"></a><a name="evs_04_2013_p40774967"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p14438051"><a name="evs_04_2013_p14438051"></a><a name="evs_04_2013_p14438051"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p41198362184535"><a name="evs_04_2013_p41198362184535"></a><a name="evs_04_2013_p41198362184535"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="evs_04_2013_p14380476104717"><a name="evs_04_2013_p14380476104717"></a><a name="evs_04_2013_p14380476104717"></a>Specifies the disk type.</p>
    <div class="p" id="evs_04_2013_p74576353336"><a name="evs_04_2013_p74576353336"></a><a name="evs_04_2013_p74576353336"></a>Currently, the value can be <strong id="evs_04_2013_b842352706164929"><a name="evs_04_2013_b842352706164929"></a><a name="evs_04_2013_b842352706164929"></a>SSD</strong>, <strong id="evs_04_2013_b842352706164932"><a name="evs_04_2013_b842352706164932"></a><a name="evs_04_2013_b842352706164932"></a>SAS</strong>, <strong id="evs_04_2013_b842352706164937"><a name="evs_04_2013_b842352706164937"></a><a name="evs_04_2013_b842352706164937"></a>SATA</strong>, <strong id="evs_04_2013_b842352706164941"><a name="evs_04_2013_b842352706164941"></a><a name="evs_04_2013_b842352706164941"></a>co-p1</strong>, or <strong id="evs_04_2013_b842352706164944"><a name="evs_04_2013_b842352706164944"></a><a name="evs_04_2013_b842352706164944"></a>uh-l1</strong>.<a name="evs_04_2013_ul11489121916439"></a><a name="evs_04_2013_ul11489121916439"></a><ul id="evs_04_2013_ul11489121916439"><li><strong id="evs_04_2013_b842352706165021"><a name="evs_04_2013_b842352706165021"></a><a name="evs_04_2013_b842352706165021"></a>SSD</strong>: specifies the ultra-high I/O disk type.</li><li><strong id="evs_04_2013_b1784237562165049"><a name="evs_04_2013_b1784237562165049"></a><a name="evs_04_2013_b1784237562165049"></a>SAS</strong>: specifies the high I/O disk type.</li><li><strong id="evs_04_2013_b3295367816515"><a name="evs_04_2013_b3295367816515"></a><a name="evs_04_2013_b3295367816515"></a>SATA</strong>: specifies the common I/O disk type.</li><li><strong id="evs_04_2013_b842352706144211"><a name="evs_04_2013_b842352706144211"></a><a name="evs_04_2013_b842352706144211"></a>co-p1</strong>: specifies the high I/O (performance-optimized I) disk type.</li><li><strong id="evs_04_2013_b842352706144228"><a name="evs_04_2013_b842352706144228"></a><a name="evs_04_2013_b842352706144228"></a>uh-l1</strong>: specifies the ultra-high I/O (latency-optimized) disk type.<p id="evs_04_2013_p14488819154320"><a name="evs_04_2013_p14488819154320"></a><a name="evs_04_2013_p14488819154320"></a>Disks of the <strong id="evs_04_2013_b164425831215049"><a name="evs_04_2013_b164425831215049"></a><a name="evs_04_2013_b164425831215049"></a>co-p1</strong> and <strong id="evs_04_2013_b106632324015049"><a name="evs_04_2013_b106632324015049"></a><a name="evs_04_2013_b106632324015049"></a>uh-l1</strong> types are used exclusively for high performance computing (HPC) and SAP HANA Elastic Cloud Servers (ECSs).</p>
    </li></ul>
    </div>
    <p id="evs_04_2013_p62741351184614"><a name="evs_04_2013_p62741351184614"></a><a name="evs_04_2013_p62741351184614"></a>If the specified disk type is not available in the AZ, the disk will fail to create.</p>
    <div class="note" id="evs_04_2013_note21808274104217"><a name="evs_04_2013_note21808274104217"></a><a name="evs_04_2013_note21808274104217"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="evs_04_2013_ul5307015718498"></a><a name="evs_04_2013_ul5307015718498"></a><ul id="evs_04_2013_ul5307015718498"><li>When the disk is created from a backup:<p id="evs_04_2013_p60300043123750"><a name="evs_04_2013_p60300043123750"></a><a name="evs_04_2013_p60300043123750"></a>If the type of the backup's source disk is <strong id="evs_04_2013_b4869418451723"><a name="evs_04_2013_b4869418451723"></a><a name="evs_04_2013_b4869418451723"></a>SSD</strong>, <strong id="evs_04_2013_b10527307431723"><a name="evs_04_2013_b10527307431723"></a><a name="evs_04_2013_b10527307431723"></a>SAS</strong>, or <strong id="evs_04_2013_b17340922121723"><a name="evs_04_2013_b17340922121723"></a><a name="evs_04_2013_b17340922121723"></a>SATA</strong>, you can create disks of any of these types.</p>
    <p id="evs_04_2013_p59443049123759"><a name="evs_04_2013_p59443049123759"></a><a name="evs_04_2013_p59443049123759"></a>If the type of the backup's source disk is <strong id="evs_04_2013_b84235270617530"><a name="evs_04_2013_b84235270617530"></a><a name="evs_04_2013_b84235270617530"></a>co-p1</strong> or <strong id="evs_04_2013_b84235270617547"><a name="evs_04_2013_b84235270617547"></a><a name="evs_04_2013_b84235270617547"></a>uh-l1</strong>, you can create disks of any of the two types.</p>
    </li><li><span id="evs_04_2013_text7492111913438"><a name="evs_04_2013_text7492111913438"></a><a name="evs_04_2013_text7492111913438"></a>If the disk is created from a snapshot, the volume_type field must be the same as that of the snapshot's source disk.</span></li><li>For details about disk types, see <strong id="evs_04_2013_b68971258152816"><a name="evs_04_2013_b68971258152816"></a><a name="evs_04_2013_b68971258152816"></a>Disk Types and Disk Performance</strong> in the <em id="evs_04_2013_i176361210290"><a name="evs_04_2013_i176361210290"></a><a name="evs_04_2013_i176361210290"></a>Elastic Volume Service User Guide</em>.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="evs_04_2013_row7461047"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p365031"><a name="evs_04_2013_p365031"></a><a name="evs_04_2013_p365031"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p29567523"><a name="evs_04_2013_p29567523"></a><a name="evs_04_2013_p29567523"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p428797710293"><a name="evs_04_2013_p428797710293"></a><a name="evs_04_2013_p428797710293"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="evs_04_2013_p47906786"><a name="evs_04_2013_p47906786"></a><a name="evs_04_2013_p47906786"></a>Specifies the number of disks to be created in a batch. If this parameter is not specified, only one disk is created. You can create a maximum of 100 disks in a batch.</p>
    <p id="evs_04_2013_p9550502101436"><a name="evs_04_2013_p9550502101436"></a><a name="evs_04_2013_p9550502101436"></a>If disks are created from a backup, batch creation is not supported, and this parameter must be set to <span class="parmname" id="evs_04_2013_parmname1151762787105851"><a name="evs_04_2013_parmname1151762787105851"></a><a name="evs_04_2013_parmname1151762787105851"></a><b>1</b></span>.</p>
    <div class="note" id="evs_04_2013_note57300341151148"><a name="evs_04_2013_note57300341151148"></a><a name="evs_04_2013_note57300341151148"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_evs_04_2013_p5070492815911"><a name="evs_04_2013_evs_04_2013_p5070492815911"></a><a name="evs_04_2013_evs_04_2013_p5070492815911"></a>If the specified parameter value is a decimal, the integral part of the value is used by default when the request is sent.</p>
    </div></div>
    </td>
    </tr>
    <tr id="evs_04_2013_row2434599211437"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p1778734011437"><a name="evs_04_2013_p1778734011437"></a><a name="evs_04_2013_p1778734011437"></a>shareable</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p3148844911437"><a name="evs_04_2013_p3148844911437"></a><a name="evs_04_2013_p3148844911437"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p42756211437"><a name="evs_04_2013_p42756211437"></a><a name="evs_04_2013_p42756211437"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="evs_04_2013_p3463256011437"><a name="evs_04_2013_p3463256011437"></a><a name="evs_04_2013_p3463256011437"></a>Specifies whether the disk is shareable. The value can be <strong id="evs_04_2013_b1234733726161036"><a name="evs_04_2013_b1234733726161036"></a><a name="evs_04_2013_b1234733726161036"></a>true</strong> (shared disk) or <strong id="evs_04_2013_b441872521161041"><a name="evs_04_2013_b441872521161041"></a><a name="evs_04_2013_b441872521161041"></a>false</strong> (common disk).</p>
    <div class="note" id="evs_04_2013_note3800959821323"><a name="evs_04_2013_note3800959821323"></a><a name="evs_04_2013_note3800959821323"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_p45212589213213"><a name="evs_04_2013_p45212589213213"></a><a name="evs_04_2013_p45212589213213"></a>This field is no longer used. Use <strong id="evs_04_2013_b84235270610834"><a name="evs_04_2013_b84235270610834"></a><a name="evs_04_2013_b84235270610834"></a>multiattach</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="evs_04_2013_row494599159816"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p424860529816"><a name="evs_04_2013_p424860529816"></a><a name="evs_04_2013_p424860529816"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p188182169816"><a name="evs_04_2013_p188182169816"></a><a name="evs_04_2013_p188182169816"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p478805289816"><a name="evs_04_2013_p478805289816"></a><a name="evs_04_2013_p478805289816"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="evs_04_2013_p323873209920"><a name="evs_04_2013_p323873209920"></a><a name="evs_04_2013_p323873209920"></a>Specifies the metadata of the created disk. <span id="evs_04_2013_text308561318143517"><a name="evs_04_2013_text308561318143517"></a><a name="evs_04_2013_text308561318143517"></a>The length of the key or value in the metadata cannot exceed 255 bytes.</span></p>
    <p id="evs_04_2013_p862801317585"><a name="evs_04_2013_p862801317585"></a><a name="evs_04_2013_p862801317585"></a>For details about <strong id="evs_04_2013_b842352706103929"><a name="evs_04_2013_b842352706103929"></a><a name="evs_04_2013_b842352706103929"></a>metadata</strong>, see <a href="#evs_04_2013_li4145283210319">Parameters in the metadata field</a>. Only the listed parameters can be specified when creating a disk.</p>
    <div class="note" id="evs_04_2013_note660019322131"><a name="evs_04_2013_note660019322131"></a><a name="evs_04_2013_note660019322131"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_p1600173216137"><a name="evs_04_2013_p1600173216137"></a><a name="evs_04_2013_p1600173216137"></a>Parameter values under <strong id="evs_04_2013_b8423527062049"><a name="evs_04_2013_b8423527062049"></a><a name="evs_04_2013_b8423527062049"></a>metadata</strong> cannot be <strong id="evs_04_2013_b842352706103415"><a name="evs_04_2013_b842352706103415"></a><a name="evs_04_2013_b842352706103415"></a>null</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="evs_04_2013_row4752931910472"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p2466966510472"><a name="evs_04_2013_p2466966510472"></a><a name="evs_04_2013_p2466966510472"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p5208587610472"><a name="evs_04_2013_p5208587610472"></a><a name="evs_04_2013_p5208587610472"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p5820640710472"><a name="evs_04_2013_p5820640710472"></a><a name="evs_04_2013_p5820640710472"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><div class="p" id="evs_04_2013_p4531155053519"><a name="evs_04_2013_p4531155053519"></a><a name="evs_04_2013_p4531155053519"></a>Specifies whether the disk is shareable. The default value is <strong id="evs_04_2013_b842352706193458"><a name="evs_04_2013_b842352706193458"></a><a name="evs_04_2013_b842352706193458"></a>false</strong>.<a name="evs_04_2013_ul202952187368"></a><a name="evs_04_2013_ul202952187368"></a><ul id="evs_04_2013_ul202952187368"><li><strong id="evs_04_2013_b1827893224315"><a name="evs_04_2013_b1827893224315"></a><a name="evs_04_2013_b1827893224315"></a>true</strong>: specifies a shared disk.</li><li><strong id="evs_04_2013_b11816235164319"><a name="evs_04_2013_b11816235164319"></a><a name="evs_04_2013_b11816235164319"></a>false</strong>: specifies a non-shared disk.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="evs_04_2013_row42399185112340"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p11781930112340"><a name="evs_04_2013_p11781930112340"></a><a name="evs_04_2013_p11781930112340"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p14812235112340"><a name="evs_04_2013_p14812235112340"></a><a name="evs_04_2013_p14812235112340"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p58940381112340"><a name="evs_04_2013_p58940381112340"></a><a name="evs_04_2013_p58940381112340"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="evs_04_2013_p9441543112340"><a name="evs_04_2013_p9441543112340"></a><a name="evs_04_2013_p9441543112340"></a>Specifies the tags added to the disk during the disk creation.</p>
    <p id="evs_04_2013_p41351845163840"><a name="evs_04_2013_p41351845163840"></a><a name="evs_04_2013_p41351845163840"></a>A maximum of 10 tags can be created for a disk.</p>
    <p id="evs_04_2013_p51240272203459"><a name="evs_04_2013_p51240272203459"></a><a name="evs_04_2013_p51240272203459"></a>Tag keys of a tag must be unique. Deduplication will be performed for duplicate keys. Therefore, only one tag key in the duplicate keys is valid.</p>
    <a name="evs_04_2013_ul3346152218352"></a><a name="evs_04_2013_ul3346152218352"></a><ul id="evs_04_2013_ul3346152218352"><li>Tag key: String type<a name="evs_04_2013_ul20512635161710"></a><a name="evs_04_2013_ul20512635161710"></a><ul id="evs_04_2013_ul20512635161710"><li>Cannot be left blank.</li><li>Must be unique for each resource.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only digits, letters, hyphens (-), and underscores (_).</li></ul>
    </li><li>Tag value: String type<a name="evs_04_2013_ul145918711181"></a><a name="evs_04_2013_ul145918711181"></a><ul id="evs_04_2013_ul145918711181"><li>Can contain a maximum of 43 characters.</li><li>Can contain only digits, letters, hyphens (-), and underscores (_).</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="evs_04_2013_row179945620499"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p39941261495"><a name="evs_04_2013_p39941261495"></a><a name="evs_04_2013_p39941261495"></a>enterprise_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p1499413644915"><a name="evs_04_2013_p1499413644915"></a><a name="evs_04_2013_p1499413644915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p79947634918"><a name="evs_04_2013_p79947634918"></a><a name="evs_04_2013_p79947634918"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="evs_04_2013_p35013964916"><a name="evs_04_2013_p35013964916"></a><a name="evs_04_2013_p35013964916"></a>Specifies the enterprise project ID. This ID is associated with the disk during the disk creation.</p>
    <p id="evs_04_2013_p19283159195318"><a name="evs_04_2013_p19283159195318"></a><a name="evs_04_2013_p19283159195318"></a><span id="evs_04_2013_text151724411566"><a name="evs_04_2013_text151724411566"></a><a name="evs_04_2013_text151724411566"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Specifying either two of the  **backup\_id**,  **snapshot\_id**, and  **imageRef**  fields is not supported.  

-   <a name="evs_04_2013_li4145283210319"></a>Parameters in the  **metadata**  field

    <a name="evs_04_2013_table3430728295554"></a>
    <table><thead align="left"><tr id="evs_04_2013_row4496975195554"><th class="cellrowborder" valign="top" width="17.48%" id="mcps1.1.5.1.1"><p id="evs_04_2013_p8809200174410"><a name="evs_04_2013_p8809200174410"></a><a name="evs_04_2013_p8809200174410"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.409999999999998%" id="mcps1.1.5.1.2"><p id="evs_04_2013_p168135017449"><a name="evs_04_2013_p168135017449"></a><a name="evs_04_2013_p168135017449"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.48%" id="mcps1.1.5.1.3"><p id="evs_04_2013_p1381850154410"><a name="evs_04_2013_p1381850154410"></a><a name="evs_04_2013_p1381850154410"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.63%" id="mcps1.1.5.1.4"><p id="evs_04_2013_p1282213034412"><a name="evs_04_2013_p1282213034412"></a><a name="evs_04_2013_p1282213034412"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2013_row456195295554"><td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p1562408795622"><a name="evs_04_2013_p1562408795622"></a><a name="evs_04_2013_p1562408795622"></a>__system__encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p5759155095622"><a name="evs_04_2013_p5759155095622"></a><a name="evs_04_2013_p5759155095622"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p3440400295622"><a name="evs_04_2013_p3440400295622"></a><a name="evs_04_2013_p3440400295622"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.1.5.1.4 "><p id="evs_04_2013_p729227516614"><a name="evs_04_2013_p729227516614"></a><a name="evs_04_2013_p729227516614"></a>Specifies the parameter that describes the encryption function in <strong id="evs_04_2013_b984769519171255"><a name="evs_04_2013_b984769519171255"></a><a name="evs_04_2013_b984769519171255"></a>metadata</strong>. The value can be <strong id="evs_04_2013_b1822406336171255"><a name="evs_04_2013_b1822406336171255"></a><a name="evs_04_2013_b1822406336171255"></a>0</strong> (encryption function disabled) or <strong id="evs_04_2013_b1135630132171255"><a name="evs_04_2013_b1135630132171255"></a><a name="evs_04_2013_b1135630132171255"></a>1</strong> (encryption function enabled).</p>
    <p id="evs_04_2013_p3526077895622"><a name="evs_04_2013_p3526077895622"></a><a name="evs_04_2013_p3526077895622"></a>If this parameter does not exist, the disk will not be encrypted by default.</p>
    </td>
    </tr>
    <tr id="evs_04_2013_row247050109562"><td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p241272995622"><a name="evs_04_2013_p241272995622"></a><a name="evs_04_2013_p241272995622"></a>__system__cmkid</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p6121338895622"><a name="evs_04_2013_p6121338895622"></a><a name="evs_04_2013_p6121338895622"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p5933737595622"><a name="evs_04_2013_p5933737595622"></a><a name="evs_04_2013_p5933737595622"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.1.5.1.4 "><p id="evs_04_2013_p4159804295622"><a name="evs_04_2013_p4159804295622"></a><a name="evs_04_2013_p4159804295622"></a>Specifies the parameter that describes the encryption CMK ID in <strong id="evs_04_2013_b84235270615128"><a name="evs_04_2013_b84235270615128"></a><a name="evs_04_2013_b84235270615128"></a>metadata</strong>. This parameter is used together with <strong id="evs_04_2013_b842352706143827"><a name="evs_04_2013_b842352706143827"></a><a name="evs_04_2013_b842352706143827"></a>__system__encrypted</strong> for encryption. The length of <strong id="evs_04_2013_b84235270614396"><a name="evs_04_2013_b84235270614396"></a><a name="evs_04_2013_b84235270614396"></a>cmkid</strong> is fixed at 36 bytes.</p>
    <div class="note" id="evs_04_2013_note16994174013320"><a name="evs_04_2013_note16994174013320"></a><a name="evs_04_2013_note16994174013320"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_p399515405333"><a name="evs_04_2013_p399515405333"></a><a name="evs_04_2013_p399515405333"></a>For details about how to obtain the CMK ID, see <strong id="evs_04_2013_b842352706154213"><a name="evs_04_2013_b842352706154213"></a><a name="evs_04_2013_b842352706154213"></a>Querying the List of CMKs</strong> in the <em id="evs_04_2013_i842352697153936"><a name="evs_04_2013_i842352697153936"></a><a name="evs_04_2013_i842352697153936"></a>Key Management Service API Reference</em>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="evs_04_2013_row60499086104915"><td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p1478896104915"><a name="evs_04_2013_p1478896104915"></a><a name="evs_04_2013_p1478896104915"></a>hw:passthrough</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p52681767104915"><a name="evs_04_2013_p52681767104915"></a><a name="evs_04_2013_p52681767104915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p39364763104915"><a name="evs_04_2013_p39364763104915"></a><a name="evs_04_2013_p39364763104915"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.1.5.1.4 "><a name="evs_04_2013_ul14462208141855"></a><a name="evs_04_2013_ul14462208141855"></a><ul id="evs_04_2013_ul14462208141855"><li>If this parameter is set to <strong id="evs_04_2013_b84235270620365"><a name="evs_04_2013_b84235270620365"></a><a name="evs_04_2013_b84235270620365"></a>true</strong>, the disk device type will be SCSI, which allows ECS OSs to directly access underlying storage media. SCSI reservation command is supported.</li><li>If this parameter is set to <strong id="evs_04_2013_b84235270620394"><a name="evs_04_2013_b84235270620394"></a><a name="evs_04_2013_b84235270620394"></a>false</strong>, the disk device type will be VBD, that is, Virtual Block Device, which supports only simple SCSI read/write commands.</li><li>If this parameter does not exist, the disk device type will be VBD, the default type.</li></ul>
    </td>
    </tr>
    <tr id="evs_04_2013_row991210132288"><td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.1 "><p id="evs_04_2013_p3500156018292"><a name="evs_04_2013_p3500156018292"></a><a name="evs_04_2013_p3500156018292"></a>full_clone</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.2 "><p id="evs_04_2013_p1655411118292"><a name="evs_04_2013_p1655411118292"></a><a name="evs_04_2013_p1655411118292"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="evs_04_2013_p6581460618292"><a name="evs_04_2013_p6581460618292"></a><a name="evs_04_2013_p6581460618292"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.1.5.1.4 "><p id="evs_04_2013_p47931946183150"><a name="evs_04_2013_p47931946183150"></a><a name="evs_04_2013_p47931946183150"></a>If the disk is created from a snapshot and linked cloning needs to be used, set this parameter to <strong id="evs_04_2013_b1229424292111849"><a name="evs_04_2013_b1229424292111849"></a><a name="evs_04_2013_b1229424292111849"></a>0</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >When creating a disk, you can only specify the fields of  **metadata**  listed in the preceding table.  
    >-   If the disk is created from a snapshot,  **\_\_system\_\_encrypted**  and  **\_\_system\_\_cmkid**  are not supported, and the newly created disk has the same encryption attribute as that of the snapshot's source disk.  
    >-   If the disk is created from an image,  **\_\_system\_\_encrypted**  and  **\_\_system\_\_cmkid**  are not supported, and the newly created disk has the same encryption attribute as that of the image.  
    >-   If the disk is created from a snapshot,  **hw:passthrough**  is not supported, and the newly created disk has the same device type as that of the snapshot's source disk.  
    >-   If the disk is created from an image,  **hw:passthrough**  is not supported, and the device type of newly created disk is VBD.  

-   Example request

    ```
    {
        "volume": {
            "backup_id": null, 
            "count": 1, 
            "availability_zone": "az-dc-1", 
            "description": "test_volume_1", 
            "size": 120, 
            "name": "test_volume_1", 
            "volume_type": "SSD", 
            "metadata": {
                "__system__encrypted": "1", 
                "__system__cmkid": "37b0d52e-c249-40d6-83cb-2b93f22445bd"
            }
        }
    }
    ```


## Response<a name="section38285619"></a>

-   Parameter description

    <a name="evs_04_2013_table735313581437"></a>
    <table><thead align="left"><tr id="evs_04_2013_row153536585313"><th class="cellrowborder" valign="top" width="21.157884211578843%" id="mcps1.1.4.1.1"><p id="evs_04_2013_p123541158732"><a name="evs_04_2013_p123541158732"></a><a name="evs_04_2013_p123541158732"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.197880211978802%" id="mcps1.1.4.1.2"><p id="evs_04_2013_p1435411581320"><a name="evs_04_2013_p1435411581320"></a><a name="evs_04_2013_p1435411581320"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2013_p13541058036"><a name="evs_04_2013_p13541058036"></a><a name="evs_04_2013_p13541058036"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2013_row1135495819312"><td class="cellrowborder" valign="top" width="21.157884211578843%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p33545583319"><a name="evs_04_2013_p33545583319"></a><a name="evs_04_2013_p33545583319"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.197880211978802%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p19354165810317"><a name="evs_04_2013_p19354165810317"></a><a name="evs_04_2013_p19354165810317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p435416581936"><a name="evs_04_2013_p435416581936"></a><a name="evs_04_2013_p435416581936"></a>Specifies the task ID.</p>
    <div class="note" id="evs_04_2013_note335410589314"><a name="evs_04_2013_note335410589314"></a><a name="evs_04_2013_note335410589314"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_p1435514588312"><a name="evs_04_2013_p1435514588312"></a><a name="evs_04_2013_p1435514588312"></a>For details about how to query the task status, see <a href="querying-task-status.md">Querying Task Status</a>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="evs_04_2013_row195162113414"><td class="cellrowborder" valign="top" width="21.157884211578843%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p129522216412"><a name="evs_04_2013_p129522216412"></a><a name="evs_04_2013_p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.197880211978802%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p1595262111415"><a name="evs_04_2013_p1595262111415"></a><a name="evs_04_2013_p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p109527215417"><a name="evs_04_2013_p109527215417"></a><a name="evs_04_2013_p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#evs_04_2013_li24688256">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="evs_04_2013_li24688256"></a>Parameters in the  **error**  field

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
        "job_id": "70a599e0-31e7-49b7-b260-868f441e862b"
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


## Status Codes<a name="section8169161010338"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

