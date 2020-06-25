# Creating EVS Disks<a name="evs_04_2013"></a>

## Function<a name="section2630087"></a>

This API is used to create one or multiple EVS disks. 

## URI<a name="section23670787"></a>

-   URI format

    POST /v2/\{project\_id\}/cloudvolumes

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

    <a name="table99446146381"></a>
    <table><thead align="left"><tr id="row14945201493812"><th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.1.5.1.1"><p id="p49451414203813"><a name="p49451414203813"></a><a name="p49451414203813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.1.5.1.2"><p id="p7945514153819"><a name="p7945514153819"></a><a name="p7945514153819"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.1.5.1.3"><p id="p14945114203813"><a name="p14945114203813"></a><a name="p14945114203813"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.515151515151516%" id="mcps1.1.5.1.4"><p id="p4946111443810"><a name="p4946111443810"></a><a name="p4946111443810"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11946111410383"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="p11946214173818"><a name="p11946214173818"></a><a name="p11946214173818"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="p394615141385"><a name="p394615141385"></a><a name="p394615141385"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="p1494601423811"><a name="p1494601423811"></a><a name="p1494601423811"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="p9946141418386"><a name="p9946141418386"></a><a name="p9946141418386"></a>Specifies the information of the disks to be created. For details, see <a href="#li10966323">Parameters in the volume field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li10966323"></a>Parameters in the  **volume**  field

    <a name="table31588048"></a>
    <table><thead align="left"><tr id="row57330849"><th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.1.5.1.1"><p id="p13287175"><a name="p13287175"></a><a name="p13287175"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.1.5.1.2"><p id="p2519427"><a name="p2519427"></a><a name="p2519427"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.17171717171717%" id="mcps1.1.5.1.3"><p id="p2747002"><a name="p2747002"></a><a name="p2747002"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.515151515151516%" id="mcps1.1.5.1.4"><p id="p21180630"><a name="p21180630"></a><a name="p21180630"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56407950"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="p5641212"><a name="p5641212"></a><a name="p5641212"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="p54284994"><a name="p54284994"></a><a name="p54284994"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="p35008393"><a name="p35008393"></a><a name="p35008393"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="p17107576"><a name="p17107576"></a><a name="p17107576"></a>Specifies the ID of the backup that can be used to create a disk. This parameter is mandatory when you use a backup to create the disk.</p>
    <div class="note" id="note4897195216919"><a name="note4897195216919"></a><a name="note4897195216919"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1369572181217"><a name="p1369572181217"></a><a name="p1369572181217"></a>For how to obtain the backup ID, see <strong id="b14360201993219"><a name="b14360201993219"></a><a name="b14360201993219"></a>Querying Details About VBS Backups (Native OpenStack API)</strong> in the <em id="i295602815315"><a name="i295602815315"></a><a name="i295602815315"></a>Volume Backup Service API Reference</em>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row19750463"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="p56283646"><a name="p56283646"></a><a name="p56283646"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="p62681466"><a name="p62681466"></a><a name="p62681466"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="p12823082184254"><a name="p12823082184254"></a><a name="p12823082184254"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="p66510234184157"><a name="p66510234184157"></a><a name="p66510234184157"></a>Specifies the AZ where you want to create the disk. If the AZ does not exist, the disk will fail to create.</p>
    <div class="note" id="note18354235112810"><a name="note18354235112810"></a><a name="note18354235112810"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p14110155594414"><a name="p14110155594414"></a><a name="p14110155594414"></a>For details about how to obtain the AZ, see <a href="querying-all-azs-cinder-v2.md">Querying All AZs</a>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row22709757"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="p27551015"><a name="p27551015"></a><a name="p27551015"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="p17039762"><a name="p17039762"></a><a name="p17039762"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="p38043494"><a name="p38043494"></a><a name="p38043494"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="p58865735113756"><a name="p58865735113756"></a><a name="p58865735113756"></a>Specifies the disk description. <span id="text110681216113820"><a name="text110681216113820"></a><a name="text110681216113820"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="row17746329"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="p28166553"><a name="p28166553"></a><a name="p28166553"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="p66898301"><a name="p66898301"></a><a name="p66898301"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="p50053294"><a name="p50053294"></a><a name="p50053294"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><div class="p" id="p27784979"><a name="p27784979"></a><a name="p27784979"></a>Specifies the disk size, in GB. Its value can be as follows:<a name="ul24506304547"></a><a name="ul24506304547"></a><ul id="ul24506304547"><li>System disk: 1 GB to 1024 GB</li><li>Data disk: 10 GB to 32768 GB</li></ul>
    </div>
    <p id="p1869819398426"><a name="p1869819398426"></a><a name="p1869819398426"></a>This parameter is mandatory when you create an empty disk. You can specify the parameter value as required within the value range.</p>
    <p id="p433134181712"><a name="p433134181712"></a><a name="p433134181712"></a>This parameter is mandatory when you create the disk from a snapshot. Ensure that the disk size is greater than or equal to the snapshot size.</p>
    <p id="p108486266429"><a name="p108486266429"></a><a name="p108486266429"></a>This parameter is mandatory when you create the disk from an image. Ensure that the disk size is greater than or equal to the minimum disk capacity required by <strong id="b11901953203815"><a name="b11901953203815"></a><a name="b11901953203815"></a>min_disk</strong> in the image attributes.</p>
    <p id="p55481787"><a name="p55481787"></a><a name="p55481787"></a>This parameter is optional when you create the disk from a backup. If this parameter is not specified, the disk size is equal to the backup size.</p>
    <div class="note" id="note6528620415911"><a name="note6528620415911"></a><a name="note6528620415911"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p5070492815911"><a name="p5070492815911"></a><a name="p5070492815911"></a>If the specified parameter value is a decimal, the integral part of the value is used by default when the request is sent.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row29574043"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="p46687245"><a name="p46687245"></a><a name="p46687245"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="p23570516"><a name="p23570516"></a><a name="p23570516"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="p30163672"><a name="p30163672"></a><a name="p30163672"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="p30342314172932"><a name="p30342314172932"></a><a name="p30342314172932"></a>Specifies the disk name.</p>
    <a name="ul46606633102055"></a><a name="ul46606633102055"></a><ul id="ul46606633102055"><li>If you create disks one by one, the <strong id="b842352706172858"><a name="b842352706172858"></a><a name="b842352706172858"></a>name</strong> value is the disk name. <span id="text101368932114053"><a name="text101368932114053"></a><a name="text101368932114053"></a>The value can contain a maximum of 255 bytes.</span></li><li>If you create multiple disks (the <strong id="b153177451299"><a name="b153177451299"></a><a name="b153177451299"></a>count</strong> value is greater than <strong id="b9330184518293"><a name="b9330184518293"></a><a name="b9330184518293"></a>1</strong>), the system automatically adds a hyphen followed by a four-digit incremental number, such as <strong id="b9331345192917"><a name="b9331345192917"></a><a name="b9331345192917"></a>-0000</strong>, to the end of each disk name. For example, the disk names can be <strong id="b682272110417"><a name="b682272110417"></a><a name="b682272110417"></a>volume-0001</strong> and <strong id="b187076249411"><a name="b187076249411"></a><a name="b187076249411"></a>volume-0002</strong>. <span id="text688013214465"><a name="text688013214465"></a><a name="text688013214465"></a>The value can contain a maximum of 250 bytes.</span></li></ul>
    </td>
    </tr>
    <tr id="row30068235161750"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="p41087296161752"><a name="p41087296161752"></a><a name="p41087296161752"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="p39736646161752"><a name="p39736646161752"></a><a name="p39736646161752"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="p64551757161752"><a name="p64551757161752"></a><a name="p64551757161752"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="p61309820161752"><a name="p61309820161752"></a><a name="p61309820161752"></a>Specifies the snapshot ID. If this parameter is specified, the disk is created from a snapshot.</p>
    <div class="note" id="note13293123112911"><a name="note13293123112911"></a><a name="note13293123112911"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p129419232297"><a name="p129419232297"></a><a name="p129419232297"></a>For details about how to obtain the snapshot ID, see <a href="querying-details-about-evs-snapshots-cinder-v2.md">Querying Details About EVS Snapshots</a>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row65447007"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="p66716242"><a name="p66716242"></a><a name="p66716242"></a>imageRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="p35306501"><a name="p35306501"></a><a name="p35306501"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="p41254304"><a name="p41254304"></a><a name="p41254304"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="p53264332"><a name="p53264332"></a><a name="p53264332"></a>Specifies the image ID. If this parameter is specified, the disk is created from an image.</p>
    <div class="note" id="note13789049151930"><a name="note13789049151930"></a><a name="note13789049151930"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p56992577151930"><a name="p56992577151930"></a><a name="p56992577151930"></a>BMS system disks cannot be created from BMS images.</p>
    <p id="p257253253318"><a name="p257253253318"></a><a name="p257253253318"></a>For details about how to obtain the image ID, see <strong id="b53641122183918"><a name="b53641122183918"></a><a name="b53641122183918"></a>Querying Images</strong> in the <em id="i448612173612"><a name="i448612173612"></a><a name="i448612173612"></a>Image Management Service API Reference</em>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row9616944"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="p40774967"><a name="p40774967"></a><a name="p40774967"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="p14438051"><a name="p14438051"></a><a name="p14438051"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="p41198362184535"><a name="p41198362184535"></a><a name="p41198362184535"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="p14380476104717"><a name="p14380476104717"></a><a name="p14380476104717"></a>Specifies the disk type.</p>
    <div class="p" id="p74576353336"><a name="p74576353336"></a><a name="p74576353336"></a>Currently, the value can be <strong id="b842352706164929"><a name="b842352706164929"></a><a name="b842352706164929"></a>SSD</strong>, <strong id="b842352706164932"><a name="b842352706164932"></a><a name="b842352706164932"></a>SAS</strong>, <strong id="b842352706164937"><a name="b842352706164937"></a><a name="b842352706164937"></a>SATA</strong>, <strong id="b842352706164941"><a name="b842352706164941"></a><a name="b842352706164941"></a>co-p1</strong>, or <strong id="b842352706164944"><a name="b842352706164944"></a><a name="b842352706164944"></a>uh-l1</strong>.<a name="ul11489121916439"></a><a name="ul11489121916439"></a><ul id="ul11489121916439"><li><strong id="b842352706165021"><a name="b842352706165021"></a><a name="b842352706165021"></a>SSD</strong>: specifies the ultra-high I/O disk type.</li><li><strong id="b1784237562165049"><a name="b1784237562165049"></a><a name="b1784237562165049"></a>SAS</strong>: specifies the high I/O disk type.</li><li><strong id="b3295367816515"><a name="b3295367816515"></a><a name="b3295367816515"></a>SATA</strong>: specifies the common I/O disk type.</li><li><strong id="b842352706144211"><a name="b842352706144211"></a><a name="b842352706144211"></a>co-p1</strong>: specifies the high I/O (performance-optimized I) disk type.</li><li><strong id="b842352706144228"><a name="b842352706144228"></a><a name="b842352706144228"></a>uh-l1</strong>: specifies the ultra-high I/O (latency-optimized) disk type.<p id="p14488819154320"><a name="p14488819154320"></a><a name="p14488819154320"></a>Disks of the <strong id="b164425831215049"><a name="b164425831215049"></a><a name="b164425831215049"></a>co-p1</strong> and <strong id="b106632324015049"><a name="b106632324015049"></a><a name="b106632324015049"></a>uh-l1</strong> types are used exclusively for high performance computing (HPC) and SAP HANA Elastic Cloud Servers (ECSs).</p>
    </li></ul>
    </div>
    <p id="p62741351184614"><a name="p62741351184614"></a><a name="p62741351184614"></a>If the specified disk type is not available in the AZ, the disk will fail to create.</p>
    <div class="note" id="note21808274104217"><a name="note21808274104217"></a><a name="note21808274104217"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul5307015718498"></a><a name="ul5307015718498"></a><ul id="ul5307015718498"><li>When the disk is created from a backup:<p id="p60300043123750"><a name="p60300043123750"></a><a name="p60300043123750"></a>If the type of the backup's source disk is <strong id="b4869418451723"><a name="b4869418451723"></a><a name="b4869418451723"></a>SSD</strong>, <strong id="b10527307431723"><a name="b10527307431723"></a><a name="b10527307431723"></a>SAS</strong>, or <strong id="b17340922121723"><a name="b17340922121723"></a><a name="b17340922121723"></a>SATA</strong>, you can create disks of any of these types.</p>
    <p id="p59443049123759"><a name="p59443049123759"></a><a name="p59443049123759"></a>If the type of the backup's source disk is <strong id="b84235270617530"><a name="b84235270617530"></a><a name="b84235270617530"></a>co-p1</strong> or <strong id="b84235270617547"><a name="b84235270617547"></a><a name="b84235270617547"></a>uh-l1</strong>, you can create disks of any of the two types.</p>
    </li><li><span id="text7492111913438"><a name="text7492111913438"></a><a name="text7492111913438"></a>If the disk is created from a snapshot, the volume_type field must be the same as that of the snapshot's source disk.</span></li><li>For details about disk types, see <strong id="b68971258152816"><a name="b68971258152816"></a><a name="b68971258152816"></a>Disk Types and Disk Performance</strong> in the <em id="i176361210290"><a name="i176361210290"></a><a name="i176361210290"></a>Elastic Volume Service User Guide</em>.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row7461047"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="p365031"><a name="p365031"></a><a name="p365031"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="p29567523"><a name="p29567523"></a><a name="p29567523"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="p428797710293"><a name="p428797710293"></a><a name="p428797710293"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="p47906786"><a name="p47906786"></a><a name="p47906786"></a>Specifies the number of disks to be created in a batch. If this parameter is not specified, only one disk is created. You can create a maximum of 100 disks in a batch.</p>
    <p id="p9550502101436"><a name="p9550502101436"></a><a name="p9550502101436"></a>If disks are created from a backup, batch creation is not supported, and this parameter must be set to <span class="parmname" id="parmname1151762787105851"><a name="parmname1151762787105851"></a><a name="parmname1151762787105851"></a><b>1</b></span>.</p>
    <div class="note" id="note57300341151148"><a name="note57300341151148"></a><a name="note57300341151148"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_p5070492815911"><a name="evs_04_2013_p5070492815911"></a><a name="evs_04_2013_p5070492815911"></a>If the specified parameter value is a decimal, the integral part of the value is used by default when the request is sent.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row2434599211437"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="p1778734011437"><a name="p1778734011437"></a><a name="p1778734011437"></a>shareable</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="p3148844911437"><a name="p3148844911437"></a><a name="p3148844911437"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="p42756211437"><a name="p42756211437"></a><a name="p42756211437"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="p3463256011437"><a name="p3463256011437"></a><a name="p3463256011437"></a>Specifies whether the disk is shareable. The value can be <strong id="b1234733726161036"><a name="b1234733726161036"></a><a name="b1234733726161036"></a>true</strong> (shared disk) or <strong id="b441872521161041"><a name="b441872521161041"></a><a name="b441872521161041"></a>false</strong> (common disk).</p>
    <div class="note" id="note3800959821323"><a name="note3800959821323"></a><a name="note3800959821323"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p45212589213213"><a name="p45212589213213"></a><a name="p45212589213213"></a>This field is no longer used. Use <strong id="b84235270610834"><a name="b84235270610834"></a><a name="b84235270610834"></a>multiattach</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row494599159816"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="p424860529816"><a name="p424860529816"></a><a name="p424860529816"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="p188182169816"><a name="p188182169816"></a><a name="p188182169816"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="p478805289816"><a name="p478805289816"></a><a name="p478805289816"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="p323873209920"><a name="p323873209920"></a><a name="p323873209920"></a>Specifies the metadata of the created disk. <span id="text308561318143517"><a name="text308561318143517"></a><a name="text308561318143517"></a>The length of the key or value in the metadata cannot exceed 255 bytes.</span></p>
    <p id="p862801317585"><a name="p862801317585"></a><a name="p862801317585"></a>For details about <strong id="b842352706103929"><a name="b842352706103929"></a><a name="b842352706103929"></a>metadata</strong>, see <a href="#li4145283210319">Parameters in the metadata field</a>. Only the listed parameters can be specified when creating a disk.</p>
    <div class="note" id="note660019322131"><a name="note660019322131"></a><a name="note660019322131"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1600173216137"><a name="p1600173216137"></a><a name="p1600173216137"></a>Parameter values under <strong id="b8423527062049"><a name="b8423527062049"></a><a name="b8423527062049"></a>metadata</strong> cannot be <strong id="b842352706103415"><a name="b842352706103415"></a><a name="b842352706103415"></a>null</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row4752931910472"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="p2466966510472"><a name="p2466966510472"></a><a name="p2466966510472"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="p5208587610472"><a name="p5208587610472"></a><a name="p5208587610472"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="p5820640710472"><a name="p5820640710472"></a><a name="p5820640710472"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><div class="p" id="p4531155053519"><a name="p4531155053519"></a><a name="p4531155053519"></a>Specifies whether the disk is shareable. The default value is <strong id="b842352706193458"><a name="b842352706193458"></a><a name="b842352706193458"></a>false</strong>.<a name="ul202952187368"></a><a name="ul202952187368"></a><ul id="ul202952187368"><li><strong id="b1827893224315"><a name="b1827893224315"></a><a name="b1827893224315"></a>true</strong>: specifies a shared disk.</li><li><strong id="b11816235164319"><a name="b11816235164319"></a><a name="b11816235164319"></a>false</strong>: specifies a non-shared disk.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row42399185112340"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="p11781930112340"><a name="p11781930112340"></a><a name="p11781930112340"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="p14812235112340"><a name="p14812235112340"></a><a name="p14812235112340"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="p58940381112340"><a name="p58940381112340"></a><a name="p58940381112340"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="p9441543112340"><a name="p9441543112340"></a><a name="p9441543112340"></a>Specifies the tags added to the disk during the disk creation.</p>
    <p id="p41351845163840"><a name="p41351845163840"></a><a name="p41351845163840"></a>A maximum of 10 tags can be created for a disk.</p>
    <p id="p51240272203459"><a name="p51240272203459"></a><a name="p51240272203459"></a>Tag keys of a tag must be unique. Deduplication will be performed for duplicate keys. Therefore, only one tag key in the duplicate keys is valid.</p>
    <a name="ul3346152218352"></a><a name="ul3346152218352"></a><ul id="ul3346152218352"><li>Tag key: String type<a name="ul20512635161710"></a><a name="ul20512635161710"></a><ul id="ul20512635161710"><li>Cannot be left blank.</li><li>Must be unique for each resource.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only digits, letters, hyphens (-), and underscores (_).</li></ul>
    </li><li>Tag value: String type<a name="ul145918711181"></a><a name="ul145918711181"></a><ul id="ul145918711181"><li>Can contain a maximum of 43 characters.</li><li>Can contain only digits, letters, hyphens (-), and underscores (_).</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row179945620499"><td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.1 "><p id="p39941261495"><a name="p39941261495"></a><a name="p39941261495"></a>enterprise_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.2 "><p id="p1499413644915"><a name="p1499413644915"></a><a name="p1499413644915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17171717171717%" headers="mcps1.1.5.1.3 "><p id="p79947634918"><a name="p79947634918"></a><a name="p79947634918"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="p35013964916"><a name="p35013964916"></a><a name="p35013964916"></a>Specifies the enterprise project ID. This ID is associated with the disk during the disk creation.</p>
    <p id="p19283159195318"><a name="p19283159195318"></a><a name="p19283159195318"></a><span id="text151724411566"><a name="text151724411566"></a><a name="text151724411566"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:**   
    >Specifying either two of the  **backup\_id**,  **snapshot\_id**, and  **imageRef**  fields is not supported.  

-   <a name="li4145283210319"></a>Parameters in the  **metadata**  field

    <a name="table3430728295554"></a>
    <table><thead align="left"><tr id="row4496975195554"><th class="cellrowborder" valign="top" width="17.48%" id="mcps1.1.5.1.1"><p id="p8809200174410"><a name="p8809200174410"></a><a name="p8809200174410"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.409999999999998%" id="mcps1.1.5.1.2"><p id="p168135017449"><a name="p168135017449"></a><a name="p168135017449"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.48%" id="mcps1.1.5.1.3"><p id="p1381850154410"><a name="p1381850154410"></a><a name="p1381850154410"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.63%" id="mcps1.1.5.1.4"><p id="p1282213034412"><a name="p1282213034412"></a><a name="p1282213034412"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row456195295554"><td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.1 "><p id="p1562408795622"><a name="p1562408795622"></a><a name="p1562408795622"></a>__system__encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.2 "><p id="p5759155095622"><a name="p5759155095622"></a><a name="p5759155095622"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p3440400295622"><a name="p3440400295622"></a><a name="p3440400295622"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.1.5.1.4 "><p id="p729227516614"><a name="p729227516614"></a><a name="p729227516614"></a>Specifies the parameter that describes the encryption function in <strong id="b984769519171255"><a name="b984769519171255"></a><a name="b984769519171255"></a>metadata</strong>. The value can be <strong id="b1822406336171255"><a name="b1822406336171255"></a><a name="b1822406336171255"></a>0</strong> (encryption function disabled) or <strong id="b1135630132171255"><a name="b1135630132171255"></a><a name="b1135630132171255"></a>1</strong> (encryption function enabled).</p>
    <p id="p3526077895622"><a name="p3526077895622"></a><a name="p3526077895622"></a>If this parameter does not exist, the disk will not be encrypted by default.</p>
    </td>
    </tr>
    <tr id="row247050109562"><td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.1 "><p id="p241272995622"><a name="p241272995622"></a><a name="p241272995622"></a>__system__cmkid</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.2 "><p id="p6121338895622"><a name="p6121338895622"></a><a name="p6121338895622"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p5933737595622"><a name="p5933737595622"></a><a name="p5933737595622"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.1.5.1.4 "><p id="p4159804295622"><a name="p4159804295622"></a><a name="p4159804295622"></a>Specifies the parameter that describes the encryption CMK ID in <strong id="b84235270615128"><a name="b84235270615128"></a><a name="b84235270615128"></a>metadata</strong>. This parameter is used together with <strong id="b842352706143827"><a name="b842352706143827"></a><a name="b842352706143827"></a>__system__encrypted</strong> for encryption. The length of <strong id="b84235270614396"><a name="b84235270614396"></a><a name="b84235270614396"></a>cmkid</strong> is fixed at 36 bytes.</p>
    <div class="note" id="note16994174013320"><a name="note16994174013320"></a><a name="note16994174013320"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p399515405333"><a name="p399515405333"></a><a name="p399515405333"></a>For details about how to obtain the CMK ID, see <strong id="b842352706154213"><a name="b842352706154213"></a><a name="b842352706154213"></a>Querying the List of CMKs</strong> in the <em id="i842352697153936"><a name="i842352697153936"></a><a name="i842352697153936"></a>Key Management Service API Reference</em>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row60499086104915"><td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.1 "><p id="p1478896104915"><a name="p1478896104915"></a><a name="p1478896104915"></a>hw:passthrough</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.2 "><p id="p52681767104915"><a name="p52681767104915"></a><a name="p52681767104915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p39364763104915"><a name="p39364763104915"></a><a name="p39364763104915"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.1.5.1.4 "><a name="ul14462208141855"></a><a name="ul14462208141855"></a><ul id="ul14462208141855"><li>If this parameter is set to <strong id="b84235270620365"><a name="b84235270620365"></a><a name="b84235270620365"></a>true</strong>, the disk device type will be SCSI, which allows ECS OSs to directly access underlying storage media. SCSI reservation command is supported.</li><li>If this parameter is set to <strong id="b84235270620394"><a name="b84235270620394"></a><a name="b84235270620394"></a>false</strong>, the disk device type will be VBD, that is, Virtual Block Device, which supports only simple SCSI read/write commands.</li><li>If this parameter does not exist, the disk device type will be VBD, the default type.</li></ul>
    </td>
    </tr>
    <tr id="row991210132288"><td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.1 "><p id="p3500156018292"><a name="p3500156018292"></a><a name="p3500156018292"></a>full_clone</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.2 "><p id="p1655411118292"><a name="p1655411118292"></a><a name="p1655411118292"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p6581460618292"><a name="p6581460618292"></a><a name="p6581460618292"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.63%" headers="mcps1.1.5.1.4 "><p id="p47931946183150"><a name="p47931946183150"></a><a name="p47931946183150"></a>If the disk is created from a snapshot and linked cloning needs to be used, set this parameter to <strong id="b1229424292111849"><a name="b1229424292111849"></a><a name="b1229424292111849"></a>0</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:**   
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

    <a name="table735313581437"></a>
    <table><thead align="left"><tr id="row153536585313"><th class="cellrowborder" valign="top" width="21.157884211578843%" id="mcps1.1.4.1.1"><p id="p123541158732"><a name="p123541158732"></a><a name="p123541158732"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.197880211978802%" id="mcps1.1.4.1.2"><p id="p1435411581320"><a name="p1435411581320"></a><a name="p1435411581320"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="p13541058036"><a name="p13541058036"></a><a name="p13541058036"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1135495819312"><td class="cellrowborder" valign="top" width="21.157884211578843%" headers="mcps1.1.4.1.1 "><p id="p33545583319"><a name="p33545583319"></a><a name="p33545583319"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.197880211978802%" headers="mcps1.1.4.1.2 "><p id="p19354165810317"><a name="p19354165810317"></a><a name="p19354165810317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p435416581936"><a name="p435416581936"></a><a name="p435416581936"></a>Specifies the task ID.</p>
    <div class="note" id="note335410589314"><a name="note335410589314"></a><a name="note335410589314"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1435514588312"><a name="p1435514588312"></a><a name="p1435514588312"></a>For details about how to query the task status, see <a href="querying-task-status.md">Querying Task Status</a>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row195162113414"><td class="cellrowborder" valign="top" width="21.157884211578843%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.197880211978802%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li24688256">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li24688256"></a>Parameters in the  **error**  field

    <a name="table15441099103019"></a>
    <table><thead align="left"><tr id="row54094047103019"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="p19541716103019"><a name="p19541716103019"></a><a name="p19541716103019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="p39375186103019"><a name="p39375186103019"></a><a name="p39375186103019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="p38578950103019"><a name="p38578950103019"></a><a name="p38578950103019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59401790103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p46815658103019"><a name="p46815658103019"></a><a name="p46815658103019"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p33971979103019"><a name="p33971979103019"></a><a name="p33971979103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p21623243103019"><a name="p21623243103019"></a><a name="p21623243103019"></a>Specifies the error message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="row60391466103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p59870541103019"><a name="p59870541103019"></a><a name="p59870541103019"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p17675690103019"><a name="p17675690103019"></a><a name="p17675690103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p6087468103019"><a name="p6087468103019"></a><a name="p6087468103019"></a>Specifies the error code returned when an error occurs.</p>
    <p id="p54787218103019"><a name="p54787218103019"></a><a name="p54787218103019"></a>For details about the error code, see <a href="error-codes.md">Error Codes</a>.</p>
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


## Status Codes<a name="section9026257"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

