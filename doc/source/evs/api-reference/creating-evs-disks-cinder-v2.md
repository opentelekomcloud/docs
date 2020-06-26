# Creating EVS Disks<a name="evs_04_2065"></a>

## Function<a name="section60214390"></a>

This API is used to create one or multiple EVS disks.

## URI<a name="section5058598"></a>

-   URI format

    POST /v2/\{project\_id\}/volumes

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


## Request<a name="section45527389"></a>

-   Parameter description

    <a name="table14875192916817"></a>
    <table><thead align="left"><tr id="row787616296812"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.5.1.1"><p id="p16876529689"><a name="p16876529689"></a><a name="p16876529689"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.1.5.1.2"><p id="p787612917814"><a name="p787612917814"></a><a name="p787612917814"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.3"><p id="p1876122910813"><a name="p1876122910813"></a><a name="p1876122910813"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="49%" id="mcps1.1.5.1.4"><p id="p1387612912813"><a name="p1387612912813"></a><a name="p1387612912813"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row178767291181"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p6877132916817"><a name="p6877132916817"></a><a name="p6877132916817"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0098680634_p159017261855"><a name="en-us_topic_0098680634_p159017261855"></a><a name="en-us_topic_0098680634_p159017261855"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p38777298820"><a name="p38777298820"></a><a name="p38777298820"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="p138771229785"><a name="p138771229785"></a><a name="p138771229785"></a>Specifies the information of the disks to be created. For details, see <a href="#li10966323">Parameters in the volume field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li10966323"></a>Parameters in the  **volume**  field

    <a name="table31588048"></a>
    <table><thead align="left"><tr id="row57330849"><th class="cellrowborder" valign="top" width="17.49%" id="mcps1.1.5.1.1"><p id="p13287175"><a name="p13287175"></a><a name="p13287175"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.530000000000001%" id="mcps1.1.5.1.2"><p id="p2519427"><a name="p2519427"></a><a name="p2519427"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.36%" id="mcps1.1.5.1.3"><p id="p2747002"><a name="p2747002"></a><a name="p2747002"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.62%" id="mcps1.1.5.1.4"><p id="p21180630"><a name="p21180630"></a><a name="p21180630"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19750463"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p56283646"><a name="p56283646"></a><a name="p56283646"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.1.5.1.2 "><p id="p62681466"><a name="p62681466"></a><a name="p62681466"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.1.5.1.3 "><p id="p44033946"><a name="p44033946"></a><a name="p44033946"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.62%" headers="mcps1.1.5.1.4 "><p id="p2830512315431"><a name="p2830512315431"></a><a name="p2830512315431"></a>Specifies the AZ where you want to create the disk. If the AZ does not exist, the disk will fail to create.</p>
    <div class="note" id="note18354235112810"><a name="note18354235112810"></a><a name="note18354235112810"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p14110155594414"><a name="p14110155594414"></a><a name="p14110155594414"></a>For details about how to obtain the AZ, see <a href="querying-all-azs-cinder-v2.md">Querying All AZs</a>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row38837194143627"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p56611368143638"><a name="p56611368143638"></a><a name="p56611368143638"></a>source_volid</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.1.5.1.2 "><p id="p22118134143638"><a name="p22118134143638"></a><a name="p22118134143638"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.1.5.1.3 "><p id="p46738440143638"><a name="p46738440143638"></a><a name="p46738440143638"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.62%" headers="mcps1.1.5.1.4 "><p id="p27717319143638"><a name="p27717319143638"></a><a name="p27717319143638"></a>Specifies the source disk ID. If this parameter is specified, the disk is cloned from an existing disk. Currently, this function is not supported.</p>
    </td>
    </tr>
    <tr id="row22709757"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p27551015"><a name="p27551015"></a><a name="p27551015"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.1.5.1.2 "><p id="p17039762"><a name="p17039762"></a><a name="p17039762"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.1.5.1.3 "><p id="p38043494"><a name="p38043494"></a><a name="p38043494"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.62%" headers="mcps1.1.5.1.4 "><p id="p5711105614375"><a name="p5711105614375"></a><a name="p5711105614375"></a>Specifies the disk description. <span id="text36053742182144"><a name="text36053742182144"></a><a name="text36053742182144"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="row28636870143814"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p42660241143822"><a name="p42660241143822"></a><a name="p42660241143822"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.1.5.1.2 "><p id="p32927512143822"><a name="p32927512143822"></a><a name="p32927512143822"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.1.5.1.3 "><p id="p49882844143822"><a name="p49882844143822"></a><a name="p49882844143822"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.62%" headers="mcps1.1.5.1.4 "><p id="p13978564143822"><a name="p13978564143822"></a><a name="p13978564143822"></a>Specifies the snapshot ID. If this parameter is specified, the disk is created from a snapshot.</p>
    <div class="note" id="note13293123112911"><a name="note13293123112911"></a><a name="note13293123112911"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p129419232297"><a name="p129419232297"></a><a name="p129419232297"></a>For details about how to obtain the snapshot ID, see <a href="querying-details-about-evs-snapshots-cinder-v2.md">Querying Details About EVS Snapshots</a>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row35520574142458"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p55945721142836"><a name="p55945721142836"></a><a name="p55945721142836"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.1.5.1.2 "><p id="p35309578142836"><a name="p35309578142836"></a><a name="p35309578142836"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.1.5.1.3 "><p id="p41503608142836"><a name="p41503608142836"></a><a name="p41503608142836"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.62%" headers="mcps1.1.5.1.4 "><div class="p" id="en-us_topic_0044524833_p27784979"><a name="en-us_topic_0044524833_p27784979"></a><a name="en-us_topic_0044524833_p27784979"></a>Specifies the disk size, in GB. Its value can be as follows:<a name="en-us_topic_0044524833_ul24506304547"></a><a name="en-us_topic_0044524833_ul24506304547"></a><ul id="en-us_topic_0044524833_ul24506304547"><li>System disk: 1 GB to 1024 GB</li><li>Data disk: 10 GB to 32768 GB</li></ul>
    </div>
    <p id="en-us_topic_0044524833_p1869819398426"><a name="en-us_topic_0044524833_p1869819398426"></a><a name="en-us_topic_0044524833_p1869819398426"></a>This parameter is mandatory when you create an empty disk. You can specify the parameter value as required within the value range.</p>
    <p id="en-us_topic_0044524833_p433134181712"><a name="en-us_topic_0044524833_p433134181712"></a><a name="en-us_topic_0044524833_p433134181712"></a>This parameter is mandatory when you create the disk from a snapshot. Ensure that the disk size is greater than or equal to the snapshot size.</p>
    <p id="en-us_topic_0044524833_p108486266429"><a name="en-us_topic_0044524833_p108486266429"></a><a name="en-us_topic_0044524833_p108486266429"></a>This parameter is mandatory when you create the disk from an image. Ensure that the disk size is greater than or equal to the minimum disk capacity required by <strong id="b11303145264115"><a name="b11303145264115"></a><a name="b11303145264115"></a>min_disk</strong> in the image attributes.</p>
    </td>
    </tr>
    <tr id="row729385014252"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p29547213143016"><a name="p29547213143016"></a><a name="p29547213143016"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.1.5.1.2 "><p id="p44514090143016"><a name="p44514090143016"></a><a name="p44514090143016"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.1.5.1.3 "><p id="p48871527143016"><a name="p48871527143016"></a><a name="p48871527143016"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.62%" headers="mcps1.1.5.1.4 "><p id="p44011641143911"><a name="p44011641143911"></a><a name="p44011641143911"></a>Specifies the disk name. <span id="text816587925182150"><a name="text816587925182150"></a><a name="text816587925182150"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="row4663112514255"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p4059158214322"><a name="p4059158214322"></a><a name="p4059158214322"></a>imageRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.1.5.1.2 "><p id="p6669267314322"><a name="p6669267314322"></a><a name="p6669267314322"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.1.5.1.3 "><p id="p3339747014322"><a name="p3339747014322"></a><a name="p3339747014322"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.62%" headers="mcps1.1.5.1.4 "><p id="p2084053914322"><a name="p2084053914322"></a><a name="p2084053914322"></a>Specifies the image ID. If this parameter is specified, the disk is created from an image.</p>
    <div class="note" id="note13789049151930"><a name="note13789049151930"></a><a name="note13789049151930"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p56992577151930"><a name="p56992577151930"></a><a name="p56992577151930"></a>BMS system disks cannot be created from BMS images.</p>
    <p id="p257253253318"><a name="p257253253318"></a><a name="p257253253318"></a>For how to obtain the image ID, see <strong id="b890312719431"><a name="b890312719431"></a><a name="b890312719431"></a>Querying Images</strong> in the <em id="i89044774316"><a name="i89044774316"></a><a name="i89044774316"></a>Image Management Service API Reference</em>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1270246214258"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p31198636143253"><a name="p31198636143253"></a><a name="p31198636143253"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.1.5.1.2 "><p id="p44061594143253"><a name="p44061594143253"></a><a name="p44061594143253"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.1.5.1.3 "><p id="p12219401143253"><a name="p12219401143253"></a><a name="p12219401143253"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.62%" headers="mcps1.1.5.1.4 "><p id="p14380476104717"><a name="p14380476104717"></a><a name="p14380476104717"></a>Specifies the disk type.</p>
    <div class="p" id="p8238097154214"><a name="p8238097154214"></a><a name="p8238097154214"></a>Currently, the value can be <strong id="b842352706164929"><a name="b842352706164929"></a><a name="b842352706164929"></a>SSD</strong>, <strong id="b842352706164932"><a name="b842352706164932"></a><a name="b842352706164932"></a>SAS</strong>, <strong id="b842352706164937"><a name="b842352706164937"></a><a name="b842352706164937"></a>SATA</strong>, <strong id="b842352706164941"><a name="b842352706164941"></a><a name="b842352706164941"></a>co-p1</strong>, or <strong id="b842352706164944"><a name="b842352706164944"></a><a name="b842352706164944"></a>uh-l1</strong>.<a name="ul134741431422"></a><a name="ul134741431422"></a><ul id="ul134741431422"><li><strong id="b842352706165021"><a name="b842352706165021"></a><a name="b842352706165021"></a>SSD</strong>: specifies the ultra-high I/O disk type.</li><li><strong id="b1784237562165049"><a name="b1784237562165049"></a><a name="b1784237562165049"></a>SAS</strong>: specifies the high I/O disk type.</li><li><strong id="b3295367816515"><a name="b3295367816515"></a><a name="b3295367816515"></a>SATA</strong>: specifies the common I/O disk type.</li><li><strong id="b842352706144211"><a name="b842352706144211"></a><a name="b842352706144211"></a>co-p1</strong>: specifies the high I/O (performance-optimized I) disk type.</li><li><strong id="b842352706144228"><a name="b842352706144228"></a><a name="b842352706144228"></a>uh-l1</strong>: specifies the ultra-high I/O (latency-optimized) disk type.<p id="p347411431520"><a name="p347411431520"></a><a name="p347411431520"></a>Disks of the <strong id="b108664633815116"><a name="b108664633815116"></a><a name="b108664633815116"></a>co-p1</strong> and <strong id="b104594858115116"><a name="b104594858115116"></a><a name="b104594858115116"></a>uh-l1</strong> types are used exclusively for HPC ECSs and SAP HANA ECSs.</p>
    </li></ul>
    </div>
    <p id="p62741351184614"><a name="p62741351184614"></a><a name="p62741351184614"></a>If the specified disk type is not available in the AZ, the disk will fail to create.</p>
    <div class="note" id="note21808274104217"><a name="note21808274104217"></a><a name="note21808274104217"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul5307015718498"></a><a name="ul5307015718498"></a><ul id="ul5307015718498"><li><span id="text7492111913438"><a name="text7492111913438"></a><a name="text7492111913438"></a>If the disk is created from a snapshot, the volume_type field must be the same as that of the snapshot's source disk.</span></li><li>For details about disk types, see <strong id="b1948292818449"><a name="b1948292818449"></a><a name="b1948292818449"></a>Disk Types and Disk Performance</strong> in the <em id="i1548392874414"><a name="i1548392874414"></a><a name="i1548392874414"></a>Elastic Volume Service User Guide</em>.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row5295776142511"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p1235117143943"><a name="p1235117143943"></a><a name="p1235117143943"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.1.5.1.2 "><p id="p32935684143943"><a name="p32935684143943"></a><a name="p32935684143943"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.1.5.1.3 "><p id="p50544710143943"><a name="p50544710143943"></a><a name="p50544710143943"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.62%" headers="mcps1.1.5.1.4 "><p id="p480861143943"><a name="p480861143943"></a><a name="p480861143943"></a>Specifies the disk metadata. <span id="text124606225420127"><a name="text124606225420127"></a><a name="text124606225420127"></a>The length of the key or value in the metadata cannot exceed 255 bytes.</span></p>
    <p id="p618213246557"><a name="p618213246557"></a><a name="p618213246557"></a>For details about <strong id="b84235270610317"><a name="b84235270610317"></a><a name="b84235270610317"></a>metadata</strong>, see <a href="#li4145283210319">Parameters in the metadata field</a>. The table lists some fields. You can also specify other fields based on the disk creation requirements.</p>
    <div class="note" id="note660019322131"><a name="note660019322131"></a><a name="note660019322131"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_p1600173216137"><a name="evs_04_2013_p1600173216137"></a><a name="evs_04_2013_p1600173216137"></a>Parameter values under <strong id="evs_04_2013_b8423527062049"><a name="evs_04_2013_b8423527062049"></a><a name="evs_04_2013_b8423527062049"></a>metadata</strong> cannot be <strong id="evs_04_2013_b842352706103415"><a name="evs_04_2013_b842352706103415"></a><a name="evs_04_2013_b842352706103415"></a>null</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row24630747142515"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p38669085144023"><a name="p38669085144023"></a><a name="p38669085144023"></a>source_replica</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.1.5.1.2 "><p id="p45188191144023"><a name="p45188191144023"></a><a name="p45188191144023"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.1.5.1.3 "><p id="p36364878144023"><a name="p36364878144023"></a><a name="p36364878144023"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.62%" headers="mcps1.1.5.1.4 "><p id="p59874001144023"><a name="p59874001144023"></a><a name="p59874001144023"></a>Specifies the source disk ID. If this parameter is specified, the disk is cloned from an existing disk. Currently, this function is not supported.</p>
    </td>
    </tr>
    <tr id="row33780455142518"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p56697807144126"><a name="p56697807144126"></a><a name="p56697807144126"></a>consistencygroup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.1.5.1.2 "><p id="p29119653144126"><a name="p29119653144126"></a><a name="p29119653144126"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.1.5.1.3 "><p id="p9881663144126"><a name="p9881663144126"></a><a name="p9881663144126"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.62%" headers="mcps1.1.5.1.4 "><p id="p62217221144126"><a name="p62217221144126"></a><a name="p62217221144126"></a><span id="text13343838181111"><a name="text13343838181111"></a><a name="text13343838181111"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row7839669175144"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p3052489817525"><a name="p3052489817525"></a><a name="p3052489817525"></a>shareable</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.1.5.1.2 "><p id="p5659770517525"><a name="p5659770517525"></a><a name="p5659770517525"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.1.5.1.3 "><p id="p2101135517525"><a name="p2101135517525"></a><a name="p2101135517525"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.62%" headers="mcps1.1.5.1.4 "><p id="p2419821017525"><a name="p2419821017525"></a><a name="p2419821017525"></a>Specifies whether the disk is shareable. The value can be <strong id="b842352706113232"><a name="b842352706113232"></a><a name="b842352706113232"></a>true</strong> (sharable) or <strong id="b842352706113236"><a name="b842352706113236"></a><a name="b842352706113236"></a>false</strong> (not sharable). This is an extended attribute. </p>
    <div class="note" id="note1645730517525"><a name="note1645730517525"></a><a name="note1645730517525"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_p45212589213213"><a name="evs_04_2013_p45212589213213"></a><a name="evs_04_2013_p45212589213213"></a>This field is no longer used. Use <strong id="evs_04_2013_b84235270610834"><a name="evs_04_2013_b84235270610834"></a><a name="evs_04_2013_b84235270610834"></a>multiattach</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row46893009142655"><td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.1.5.1.1 "><p id="p16191875144233"><a name="p16191875144233"></a><a name="p16191875144233"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.1.5.1.2 "><p id="p36473476144233"><a name="p36473476144233"></a><a name="p36473476144233"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.1.5.1.3 "><p id="p1561611144233"><a name="p1561611144233"></a><a name="p1561611144233"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.62%" headers="mcps1.1.5.1.4 "><div class="p" id="p4531155053519"><a name="p4531155053519"></a><a name="p4531155053519"></a>Specifies whether the disk is shareable. The default value is <strong id="b789259195017"><a name="b789259195017"></a><a name="b789259195017"></a>false</strong>.<a name="ul202952187368"></a><a name="ul202952187368"></a><ul id="ul202952187368"><li><strong id="b2087914016511"><a name="b2087914016511"></a><a name="b2087914016511"></a>true</strong>: specifies a shared disk.</li><li><strong id="b11149315519"><a name="b11149315519"></a><a name="b11149315519"></a>false</strong>: specifies a non-shared disk.</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:**   
    >Specifying either two of the  **source\_volid**,  **snapshot\_id**, and  **imageRef**  fields is not supported.  

-   <a name="li4145283210319"></a>Parameters in the  **metadata**  field

    <a name="en-us_topic_0044524833_table3430728295554"></a>
    <table><thead align="left"><tr id="en-us_topic_0044524833_row4496975195554"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.5.1.1"><p id="en-us_topic_0044524833_p5979314595726"><a name="en-us_topic_0044524833_p5979314595726"></a><a name="en-us_topic_0044524833_p5979314595726"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.1.5.1.2"><p id="en-us_topic_0044524833_p1140655395726"><a name="en-us_topic_0044524833_p1140655395726"></a><a name="en-us_topic_0044524833_p1140655395726"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.1.5.1.3"><p id="en-us_topic_0044524833_p5151561095726"><a name="en-us_topic_0044524833_p5151561095726"></a><a name="en-us_topic_0044524833_p5151561095726"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.1.5.1.4"><p id="en-us_topic_0044524833_p1201488395726"><a name="en-us_topic_0044524833_p1201488395726"></a><a name="en-us_topic_0044524833_p1201488395726"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0044524833_row456195295554"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0044524833_p1562408795622"><a name="en-us_topic_0044524833_p1562408795622"></a><a name="en-us_topic_0044524833_p1562408795622"></a>__system__encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0044524833_p5759155095622"><a name="en-us_topic_0044524833_p5759155095622"></a><a name="en-us_topic_0044524833_p5759155095622"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0044524833_p3440400295622"><a name="en-us_topic_0044524833_p3440400295622"></a><a name="en-us_topic_0044524833_p3440400295622"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p4269864016712"><a name="p4269864016712"></a><a name="p4269864016712"></a>Specifies the parameter that describes the encryption function in <strong id="b842352706102526"><a name="b842352706102526"></a><a name="b842352706102526"></a>metadata</strong>. The value can be <strong id="b842352706102532"><a name="b842352706102532"></a><a name="b842352706102532"></a>0</strong> (encryption function disabled) or <strong id="b842352706102535"><a name="b842352706102535"></a><a name="b842352706102535"></a>1</strong> (encryption function enabled).</p>
    <p id="en-us_topic_0044524833_p3526077895622"><a name="en-us_topic_0044524833_p3526077895622"></a><a name="en-us_topic_0044524833_p3526077895622"></a>If this parameter does not exist, the disk will not be encrypted by default.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0044524833_row247050109562"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0044524833_p241272995622"><a name="en-us_topic_0044524833_p241272995622"></a><a name="en-us_topic_0044524833_p241272995622"></a>__system__cmkid</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0044524833_p6121338895622"><a name="en-us_topic_0044524833_p6121338895622"></a><a name="en-us_topic_0044524833_p6121338895622"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0044524833_p5933737595622"><a name="en-us_topic_0044524833_p5933737595622"></a><a name="en-us_topic_0044524833_p5933737595622"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0044524833_p4159804295622"><a name="en-us_topic_0044524833_p4159804295622"></a><a name="en-us_topic_0044524833_p4159804295622"></a>Specifies the parameter that describes the encryption CMK ID in <strong id="b84235270615116"><a name="b84235270615116"></a><a name="b84235270615116"></a>metadata</strong>. This parameter is used together with <strong id="b842352706143827"><a name="b842352706143827"></a><a name="b842352706143827"></a>__system__encrypted</strong> for encryption. The length of <strong id="b84235270614396"><a name="b84235270614396"></a><a name="b84235270614396"></a>cmkid</strong> is fixed at 36 bytes.</p>
    <div class="note" id="note1483983117491"><a name="note1483983117491"></a><a name="note1483983117491"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_p399515405333"><a name="evs_04_2013_p399515405333"></a><a name="evs_04_2013_p399515405333"></a>For details about how to obtain the CMK ID, see <strong id="evs_04_2013_b842352706154213"><a name="evs_04_2013_b842352706154213"></a><a name="evs_04_2013_b842352706154213"></a>Querying the List of CMKs</strong> in the <em id="evs_04_2013_i842352697153936"><a name="evs_04_2013_i842352697153936"></a><a name="evs_04_2013_i842352697153936"></a>Key Management Service API Reference</em>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0044524833_row60499086104915"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0044524833_p1478896104915"><a name="en-us_topic_0044524833_p1478896104915"></a><a name="en-us_topic_0044524833_p1478896104915"></a>hw:passthrough</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0044524833_p52681767104915"><a name="en-us_topic_0044524833_p52681767104915"></a><a name="en-us_topic_0044524833_p52681767104915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0044524833_p39364763104915"><a name="en-us_topic_0044524833_p39364763104915"></a><a name="en-us_topic_0044524833_p39364763104915"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><a name="en-us_topic_0044524833_ul14462208141855"></a><a name="en-us_topic_0044524833_ul14462208141855"></a><ul id="en-us_topic_0044524833_ul14462208141855"><li>If this parameter is set to <strong id="b59715515475"><a name="b59715515475"></a><a name="b59715515475"></a>true</strong>, the disk device type is SCSI, which allows ECS OSs to directly access the underlying storage media and supports SCSI reservation commands.</li><li>If this parameter is set to <strong id="b84235270620394"><a name="b84235270620394"></a><a name="b84235270620394"></a>false</strong>, the disk device type will be VBD, which supports only simple SCSI read/write commands.</li><li>If this parameter does not exist, the disk device type will be VBD, the default type.<div class="note" id="en-us_topic_0044524833_note30831239112110"><a name="en-us_topic_0044524833_note30831239112110"></a><a name="en-us_topic_0044524833_note30831239112110"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0044524833_p9045701112110"><a name="en-us_topic_0044524833_p9045701112110"></a><a name="en-us_topic_0044524833_p9045701112110"></a>If parameter <strong id="b566443801111854"><a name="b566443801111854"></a><a name="b566443801111854"></a>shareable</strong> is set to <strong id="b840555499111854"><a name="b840555499111854"></a><a name="b840555499111854"></a>true</strong> and parameter <strong id="b347106191111854"><a name="b347106191111854"></a><a name="b347106191111854"></a>hw:passthrough</strong> is not specified, shared VBD disks are created.</p>
    </div></div>
    </li></ul>
    </td>
    </tr>
    <tr id="row6091294618292"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p3500156018292"><a name="p3500156018292"></a><a name="p3500156018292"></a>full_clone</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="p1655411118292"><a name="p1655411118292"></a><a name="p1655411118292"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.3 "><p id="p6581460618292"><a name="p6581460618292"></a><a name="p6581460618292"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p47931946183150"><a name="p47931946183150"></a><a name="p47931946183150"></a>If the disk is created from a snapshot and linked cloning needs to be used, set this parameter to <strong id="b46641830125217"><a name="b46641830125217"></a><a name="b46641830125217"></a>0</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:**   
    >The preceding table provides only some parameters in  **metadata**  for your reference. You can also specify other fields based on the disk creation requirements.  
    >-   If the disk is created from a snapshot,  **\_\_system\_\_encrypted**  and  **\_\_system\_\_cmkid**  are not supported, and the newly created disk has the same encryption attribute as that of the snapshot's source disk.  
    >-   If the disk is created from an image,  **\_\_system\_\_encrypted**  and  **\_\_system\_\_cmkid**  are not supported, and the newly created disk has the same encryption attribute as that of the image.  
    >-   If the disk is created from a snapshot,  **hw:passthrough**  is not supported, and the newly created disk has the same device type as that of the snapshot's source disk.  
    >-   If the disk is created from an image,  **hw:passthrough**  is not supported, and the device type of newly created disk is VBD.  

-   Example request

    ```
    {
        "volume": {
            "name": "openapi_vol01", 
            "imageRef": "027cf713-45a6-45f0-ac1b-0ccc57ac12e2", 
            "availability_zone": "az-dc-1", 
            "description": "create for api test", 
            "volume_type": "SATA", 
            "metadata": {
                "volume_owner": "openapi"
            },  
            "multiattach": false, 
            "size": 40
        }, 
    }
    ```


## Response<a name="section7093323"></a>

-   Parameter description

    <a name="table192671691419"></a>
    <table><thead align="left"><tr id="row1626713984113"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="p626716915410"><a name="p626716915410"></a><a name="p626716915410"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.35%" id="mcps1.1.4.1.2"><p id="p10268199164120"><a name="p10268199164120"></a><a name="p10268199164120"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.65%" id="mcps1.1.4.1.3"><p id="p226814984116"><a name="p226814984116"></a><a name="p226814984116"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20268997416"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p192684913418"><a name="p192684913418"></a><a name="p192684913418"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p1326816984113"><a name="p1326816984113"></a><a name="p1326816984113"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p1826816912416"><a name="p1826816912416"></a><a name="p1826816912416"></a>Specifies the information of the created disks. For details, see <a href="#li3451542201439">Parameters in the volumes field</a>.</p>
    </td>
    </tr>
    <tr id="row197012674215"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li3451542201439"></a>Parameters in the  **volumes**  field

    <a name="table34701445142557"></a>
    <table><thead align="left"><tr id="row12524911142557"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.4.1.1"><p id="p7884856142557"><a name="p7884856142557"></a><a name="p7884856142557"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.35%" id="mcps1.1.4.1.2"><p id="p34693598142557"><a name="p34693598142557"></a><a name="p34693598142557"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.65%" id="mcps1.1.4.1.3"><p id="p58539486142557"><a name="p58539486142557"></a><a name="p58539486142557"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row444782011610"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p18308336144438"><a name="p18308336144438"></a><a name="p18308336144438"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p6580236144438"><a name="p6580236144438"></a><a name="p6580236144438"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p21928856144438"><a name="p21928856144438"></a><a name="p21928856144438"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="row44077962142557"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p14226985144438"><a name="p14226985144438"></a><a name="p14226985144438"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p11535156144438"><a name="p11535156144438"></a><a name="p11535156144438"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p50473003144438"><a name="p50473003144438"></a><a name="p50473003144438"></a>Specifies the disk URI. For details, see <a href="#li1043159617124">Parameters in the links field</a>.</p>
    </td>
    </tr>
    <tr id="row16186817142557"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p19162411144438"><a name="p19162411144438"></a><a name="p19162411144438"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p8651439144438"><a name="p8651439144438"></a><a name="p8651439144438"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p55103877144438"><a name="p55103877144438"></a><a name="p55103877144438"></a>Specifies the disk name.</p>
    </td>
    </tr>
    <tr id="row2987651144410"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p39625821144438"><a name="p39625821144438"></a><a name="p39625821144438"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p55574965144438"><a name="p55574965144438"></a><a name="p55574965144438"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p24889213144438"><a name="p24889213144438"></a><a name="p24889213144438"></a>Specifies the disk status. For details, see <a href="evs-disk-status.md">EVS Disk Status</a>.</p>
    </td>
    </tr>
    <tr id="row45785905142557"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p24843442144438"><a name="p24843442144438"></a><a name="p24843442144438"></a>attachments</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p66161799144438"><a name="p66161799144438"></a><a name="p66161799144438"></a>list</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p27432950144438"><a name="p27432950144438"></a><a name="p27432950144438"></a>Specifies the disk attachment information. For details, see <a href="#li3900093617124">Parameters in the attachments field</a>.</p>
    </td>
    </tr>
    <tr id="row35247553142557"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p179170144438"><a name="p179170144438"></a><a name="p179170144438"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p14512814144438"><a name="p14512814144438"></a><a name="p14512814144438"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p58206487144438"><a name="p58206487144438"></a><a name="p58206487144438"></a>Specifies the AZ to which the disk belongs.</p>
    </td>
    </tr>
    <tr id="row27126244142557"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p19727534144438"><a name="p19727534144438"></a><a name="p19727534144438"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p54426427144438"><a name="p54426427144438"></a><a name="p54426427144438"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><div class="p" id="en-us_topic_0098680634_p8780414125315"><a name="en-us_topic_0098680634_p8780414125315"></a><a name="en-us_topic_0098680634_p8780414125315"></a>Specifies whether the disk is bootable.<a name="ul185931714111"></a><a name="ul185931714111"></a><ul id="ul185931714111"><li><strong id="b1867946184516"><a name="b1867946184516"></a><a name="b1867946184516"></a>true</strong>: specifies a bootable disk.</li><li><strong id="b1317878184511"><a name="b1317878184511"></a><a name="b1317878184511"></a>false</strong>: specifies a non-bootable disk.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row17610291172344"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p5866739172351"><a name="p5866739172351"></a><a name="p5866739172351"></a>encrypted</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p5443865172351"><a name="p5443865172351"></a><a name="p5443865172351"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p15286422172351"><a name="p15286422172351"></a><a name="p15286422172351"></a><span id="text115706570229"><a name="text115706570229"></a><a name="text115706570229"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="row49237196142557"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p28651206144438"><a name="p28651206144438"></a><a name="p28651206144438"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p1296456144535"><a name="p1296456144535"></a><a name="p1296456144535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p28821893144438"><a name="p28821893144438"></a><a name="p28821893144438"></a>Specifies the time when the disk was created.</p>
    <p id="p586613505312"><a name="p586613505312"></a><a name="p586613505312"></a><span id="text28661350936"><a name="text28661350936"></a><a name="text28661350936"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row39017307142557"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p6085885144438"><a name="p6085885144438"></a><a name="p6085885144438"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p18611115144535"><a name="p18611115144535"></a><a name="p18611115144535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p44410693144438"><a name="p44410693144438"></a><a name="p44410693144438"></a>Specifies the disk description.</p>
    </td>
    </tr>
    <tr id="row20107664142557"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p28923171144438"><a name="p28923171144438"></a><a name="p28923171144438"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p22198851144535"><a name="p22198851144535"></a><a name="p22198851144535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p9630579144438"><a name="p9630579144438"></a><a name="p9630579144438"></a>Specifies the disk type.</p>
    </td>
    </tr>
    <tr id="row12897861142557"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p41370851144438"><a name="p41370851144438"></a><a name="p41370851144438"></a>replication_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p7354807144535"><a name="p7354807144535"></a><a name="p7354807144535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p27786537144438"><a name="p27786537144438"></a><a name="p27786537144438"></a><span id="text6498181171119"><a name="text6498181171119"></a><a name="text6498181171119"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row45680217142557"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p56617581144438"><a name="p56617581144438"></a><a name="p56617581144438"></a>consistencygroup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p25180208144535"><a name="p25180208144535"></a><a name="p25180208144535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p40860550144438"><a name="p40860550144438"></a><a name="p40860550144438"></a>Specifies the ID of the consistency group where the disk belongs.</p>
    <p id="p1919420431188"><a name="p1919420431188"></a><a name="p1919420431188"></a><span id="text161944439182"><a name="text161944439182"></a><a name="text161944439182"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="row47480567142557"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p58114746144438"><a name="p58114746144438"></a><a name="p58114746144438"></a>source_volid</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p47440982144535"><a name="p47440982144535"></a><a name="p47440982144535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p52975605144438"><a name="p52975605144438"></a><a name="p52975605144438"></a>Specifies the source disk ID.</p>
    <p id="p14532184716186"><a name="p14532184716186"></a><a name="p14532184716186"></a><span id="text12532347191815"><a name="text12532347191815"></a><a name="text12532347191815"></a>Currently, this field is not supported by EVS.</span></p>
    </td>
    </tr>
    <tr id="row31517135142557"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p31619531144438"><a name="p31619531144438"></a><a name="p31619531144438"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p66078031144535"><a name="p66078031144535"></a><a name="p66078031144535"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p57055846144438"><a name="p57055846144438"></a><a name="p57055846144438"></a>Specifies the snapshot ID.</p>
    </td>
    </tr>
    <tr id="row15610713142557"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p53325033144438"><a name="p53325033144438"></a><a name="p53325033144438"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p24360403144438"><a name="p24360403144438"></a><a name="p24360403144438"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p42403730144438"><a name="p42403730144438"></a><a name="p42403730144438"></a>Specifies the disk metadata. For details, see <a href="#li29114110314">Parameters in the metadata field</a>.</p>
    </td>
    </tr>
    <tr id="row5657368142557"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p42241765144438"><a name="p42241765144438"></a><a name="p42241765144438"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p66139813144438"><a name="p66139813144438"></a><a name="p66139813144438"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p17400122144438"><a name="p17400122144438"></a><a name="p17400122144438"></a>Specifies the disk size, in GB.</p>
    </td>
    </tr>
    <tr id="row39412545144428"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p1113688144438"><a name="p1113688144438"></a><a name="p1113688144438"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p51894643144540"><a name="p51894643144540"></a><a name="p51894643144540"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p26218517352"><a name="p26218517352"></a><a name="p26218517352"></a>Reserved field</p>
    </td>
    </tr>
    <tr id="row25381049144431"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p26680804144438"><a name="p26680804144438"></a><a name="p26680804144438"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p39072645144540"><a name="p39072645144540"></a><a name="p39072645144540"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p42877354144438"><a name="p42877354144438"></a><a name="p42877354144438"></a>Specifies the time when the disk was updated.</p>
    <p id="p15772145473814"><a name="p15772145473814"></a><a name="p15772145473814"></a><span id="text151181202390"><a name="text151181202390"></a><a name="text151181202390"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row48384415144425"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p51969649144438"><a name="p51969649144438"></a><a name="p51969649144438"></a>shareable</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p5099125121957"><a name="p5099125121957"></a><a name="p5099125121957"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><p id="p15113052144438"><a name="p15113052144438"></a><a name="p15113052144438"></a>Specifies whether the disk is shareable.</p>
    <div class="note" id="note182866179314"><a name="note182866179314"></a><a name="note182866179314"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="evs_04_2013_p45212589213213_1"><a name="evs_04_2013_p45212589213213_1"></a><a name="evs_04_2013_p45212589213213_1"></a>This field is no longer used. Use <strong id="evs_04_2013_b84235270610834_1"><a name="evs_04_2013_b84235270610834_1"></a><a name="evs_04_2013_b84235270610834_1"></a>multiattach</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row42462677142557"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.4.1.1 "><p id="p11561839144438"><a name="p11561839144438"></a><a name="p11561839144438"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.1.4.1.2 "><p id="p64093800144438"><a name="p64093800144438"></a><a name="p64093800144438"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.65%" headers="mcps1.1.4.1.3 "><div class="p" id="en-us_topic_0098680634_p4781191416535"><a name="en-us_topic_0098680634_p4781191416535"></a><a name="en-us_topic_0098680634_p4781191416535"></a>Specifies whether the disk is shareable.<a name="ul161621719119"></a><a name="ul161621719119"></a><ul id="ul161621719119"><li><strong id="b181751317104517"><a name="b181751317104517"></a><a name="b181751317104517"></a>true</strong>: specifies a shared disk.</li><li><strong id="b1948624590"><a name="b1948624590"></a><a name="b1948624590"></a>false</strong>: specifies a non-shared disk.</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li1043159617124"></a>Parameters in the  **links**  field

    <a name="table4005083311851"></a>
    <table><thead align="left"><tr id="row4647546111851"><th class="cellrowborder" valign="top" width="19.27807219278072%" id="mcps1.1.4.1.1"><p id="p641601411851"><a name="p641601411851"></a><a name="p641601411851"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.0975902409759%" id="mcps1.1.4.1.2"><p id="p4993509511851"><a name="p4993509511851"></a><a name="p4993509511851"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.624337566243376%" id="mcps1.1.4.1.3"><p id="p6579322611851"><a name="p6579322611851"></a><a name="p6579322611851"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2765107611851"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p2514470311851"><a name="p2514470311851"></a><a name="p2514470311851"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p2345507511851"><a name="p2345507511851"></a><a name="p2345507511851"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p812224311851"><a name="p812224311851"></a><a name="p812224311851"></a>Specifies the corresponding shortcut link.</p>
    </td>
    </tr>
    <tr id="row599132611851"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p1553537811851"><a name="p1553537811851"></a><a name="p1553537811851"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p5040609911851"><a name="p5040609911851"></a><a name="p5040609911851"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p193416911851"><a name="p193416911851"></a><a name="p193416911851"></a>Specifies the shortcut link marker name.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li3900093617124"></a>Parameters in the  **attachments**  field

    <a name="table3471673811913"></a>
    <table><thead align="left"><tr id="row950913211913"><th class="cellrowborder" valign="top" width="19.27807219278072%" id="mcps1.1.4.1.1"><p id="p3204224811913"><a name="p3204224811913"></a><a name="p3204224811913"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.0975902409759%" id="mcps1.1.4.1.2"><p id="p4528532911913"><a name="p4528532911913"></a><a name="p4528532911913"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.624337566243376%" id="mcps1.1.4.1.3"><p id="p2610634411913"><a name="p2610634411913"></a><a name="p2610634411913"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3423911011913"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p2190452911913"><a name="p2190452911913"></a><a name="p2190452911913"></a>server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p2943640011913"><a name="p2943640011913"></a><a name="p2943640011913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p6002094011913"><a name="p6002094011913"></a><a name="p6002094011913"></a>Specifies the ID of the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="row331754911913"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p28604711913"><a name="p28604711913"></a><a name="p28604711913"></a>attachment_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p2316983311913"><a name="p2316983311913"></a><a name="p2316983311913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p1570218411913"><a name="p1570218411913"></a><a name="p1570218411913"></a>Specifies the ID of the attachment information.</p>
    </td>
    </tr>
    <tr id="row41611216113819"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p26997962113823"><a name="p26997962113823"></a><a name="p26997962113823"></a>attached_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p39351338113823"><a name="p39351338113823"></a><a name="p39351338113823"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p16333436113823"><a name="p16333436113823"></a><a name="p16333436113823"></a>Specifies the time when the disk was attached.</p>
    <p id="p103581088395"><a name="p103581088395"></a><a name="p103581088395"></a><span id="text136037162396"><a name="text136037162396"></a><a name="text136037162396"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row710192811913"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p3838529111913"><a name="p3838529111913"></a><a name="p3838529111913"></a>host_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p2220087511913"><a name="p2220087511913"></a><a name="p2220087511913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p3370764811913"><a name="p3370764811913"></a><a name="p3370764811913"></a>Specifies the name of the physical host accommodating the server to which the disk is attached.</p>
    </td>
    </tr>
    <tr id="row3493337611913"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p1103121411913"><a name="p1103121411913"></a><a name="p1103121411913"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p2111318111913"><a name="p2111318111913"></a><a name="p2111318111913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p1089110111913"><a name="p1089110111913"></a><a name="p1089110111913"></a>Specifies the disk ID.</p>
    </td>
    </tr>
    <tr id="row3091104611913"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p2076682611913"><a name="p2076682611913"></a><a name="p2076682611913"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p439134611913"><a name="p439134611913"></a><a name="p439134611913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p2192276811913"><a name="p2192276811913"></a><a name="p2192276811913"></a>Specifies the device name.</p>
    </td>
    </tr>
    <tr id="row6308718811913"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.4.1.1 "><p id="p978858311913"><a name="p978858311913"></a><a name="p978858311913"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.0975902409759%" headers="mcps1.1.4.1.2 "><p id="p5467773011913"><a name="p5467773011913"></a><a name="p5467773011913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.624337566243376%" headers="mcps1.1.4.1.3 "><p id="p4371205011913"><a name="p4371205011913"></a><a name="p4371205011913"></a>Specifies the ID of the attached resource.</p>
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

    202


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

