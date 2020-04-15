# Create an EVS Disk<a name="en-us_topic_0021738346"></a>

## Scenarios<a name="s0e5639e1ba7b4924a177eb1b9ae1c5b2"></a>

When a server is created, the system disk is automatically created and attached. You do not need to create the system disk separately.

Data disks can be created during or after the server creation. If you create data disks during the server creation, the system will automatically attach the data disks to the server. If you create data disks after the server creation, you need to manually attach the created data disks to the server.

This topic describes how to separately create disks on the EVS console.

## Procedure<a name="s9aed06edc7654d9182b7e97b045df907"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Storage**, click  **Elastic Volume Service**.

    The disk list page is displayed.

4.  Click  **Create Disk**.
    -   [Figure 1](#fig107262034017)  shows the parameter setting of non-encrypted disks.

        **Figure  1**  Non-encrypted disks<a name="fig107262034017"></a>  
        ![](figures/non-encrypted-disks.png "non-encrypted-disks")

    -   [Figure 2](#fig1523406103916)  shows the parameter setting of encrypted disks.

        **Figure  2**  Encrypted disks<a name="fig1523406103916"></a>  
        ![](figures/encrypted-disks.png "encrypted-disks")

5.  Configure basic disk information according to  [Table 1](#table112183734214).

    **Table  1**  Parameter description

    <a name="table112183734214"></a>
    <table><thead align="left"><tr id="row15973936184217"><th class="cellrowborder" valign="top" width="15.920000000000002%" id="mcps1.2.4.1.1"><p id="p189731536134214"><a name="p189731536134214"></a><a name="p189731536134214"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.18%" id="mcps1.2.4.1.2"><p id="p597311365429"><a name="p597311365429"></a><a name="p597311365429"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.900000000000002%" id="mcps1.2.4.1.3"><p id="p09731836154215"><a name="p09731836154215"></a><a name="p09731836154215"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1797393616422"><td class="cellrowborder" valign="top" width="15.920000000000002%" headers="mcps1.2.4.1.1 "><p id="p10973143654215"><a name="p10973143654215"></a><a name="p10973143654215"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.18%" headers="mcps1.2.4.1.2 "><p id="p3973143634215"><a name="p3973143634215"></a><a name="p3973143634215"></a>Mandatory</p>
    <p id="p1097303624212"><a name="p1097303624212"></a><a name="p1097303624212"></a>Resources are region-specific and cannot be used across regions through internal network connections. For low network latency and quick resource access, select the nearest region.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.900000000000002%" headers="mcps1.2.4.1.3 "><p id="p397319366420"><a name="p397319366420"></a><a name="p397319366420"></a>eu-de</p>
    </td>
    </tr>
    <tr id="row149751336154210"><td class="cellrowborder" valign="top" width="15.920000000000002%" headers="mcps1.2.4.1.1 "><p id="p7973103644215"><a name="p7973103644215"></a><a name="p7973103644215"></a>AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.18%" headers="mcps1.2.4.1.2 "><p id="p119731736104219"><a name="p119731736104219"></a><a name="p119731736104219"></a>Mandatory</p>
    <p id="p159732366429"><a name="p159732366429"></a><a name="p159732366429"></a>Specifies the availability zone (AZ) where you want to create the disk.</p>
    <div class="note" id="note18975153616420"><a name="note18975153616420"></a><a name="note18975153616420"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul6974173694218"></a><a name="ul6974173694218"></a><ul id="ul6974173694218"><li>Disks can only be attached to the servers in the same AZ.</li><li>You cannot change the AZ of the disk after the disk has been created.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="19.900000000000002%" headers="mcps1.2.4.1.3 "><p id="p1197563619427"><a name="p1197563619427"></a><a name="p1197563619427"></a>eu-de-1</p>
    </td>
    </tr>
    <tr id="row1798263604216"><td class="cellrowborder" valign="top" width="15.920000000000002%" headers="mcps1.2.4.1.1 "><p id="p11976133654213"><a name="p11976133654213"></a><a name="p11976133654213"></a>Disk Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.18%" headers="mcps1.2.4.1.2 "><p id="p169764368425"><a name="p169764368425"></a><a name="p169764368425"></a>Mandatory</p>
    <a name="ul7981536134213"></a><a name="ul7981536134213"></a><ul id="ul7981536134213"><li>Common I/O</li><li>High I/O</li><li>Ultra-high I/O</li><li>High I/O (Performance optimized I)</li><li>Ultra-high I/O (Latency optimized)</li></ul>
    <div class="note" id="note398233684212"><a name="note398233684212"></a><a name="note398233684212"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul179822362421"></a><a name="ul179822362421"></a><ul id="ul179822362421"><li>When disks are created from backups:<p id="p59816362426"><a name="p59816362426"></a><a name="p59816362426"></a>If the disk type of the backup's source disk is common I/O, high I/O, or ultra-high I/O, you can create disks of any of these types.</p>
    <p id="p298119367422"><a name="p298119367422"></a><a name="p298119367422"></a>If the disk type of the backup's source disk is high I/O (performance optimized I) or ultra-high I/O (latency optimized), you can create disks of any of the two types.</p>
    </li><li>When a disk is created from a snapshot, the disk type of the newly created disk will be consistent with that of the snapshot's source disk.</li><li>For details about disk types, see <a href="disk-types-and-disk-performance.md">Disk Types and Disk Performance</a>.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="19.900000000000002%" headers="mcps1.2.4.1.3 "><p id="p15982163684216"><a name="p15982163684216"></a><a name="p15982163684216"></a>Common I/O</p>
    </td>
    </tr>
    <tr id="row1983193624212"><td class="cellrowborder" valign="top" width="15.920000000000002%" headers="mcps1.2.4.1.1 "><p id="p49821136164211"><a name="p49821136164211"></a><a name="p49821136164211"></a>Capacity (GB)</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.18%" headers="mcps1.2.4.1.2 "><p id="p998293694218"><a name="p998293694218"></a><a name="p998293694218"></a>Mandatory</p>
    <p id="p139829363427"><a name="p139829363427"></a><a name="p139829363427"></a>Specifies the disk size. Only data disks can be created on the current page, and the disk capacity ranges from 10 GB to 32768 GB.</p>
    <div class="note" id="note109826365426"><a name="note109826365426"></a><a name="note109826365426"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul498243619426"></a><a name="ul498243619426"></a><ul id="ul498243619426"><li>When you use a backup to create a disk, the disk capacity must be greater than or equal to the backup size. In the condition that you do not specify the disk capacity, if the backup size is smaller than 10 GB, the default capacity 10 GB will be used as the disk capacity; if the backup size is greater than 10 GB, the disk capacity will be consistent with the backup size.</li><li>When you use a snapshot to create a disk, the disk capacity must be greater than or equal to the snapshot size. In the condition that you do not specify the disk capacity, if the snapshot size is smaller than 10 GB, the default capacity 10 GB will be used as the disk capacity; if the snapshot size is greater than 10 GB, the disk capacity will be consistent with the snapshot size.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="19.900000000000002%" headers="mcps1.2.4.1.3 "><p id="p1298353644211"><a name="p1298353644211"></a><a name="p1298353644211"></a>20 GB</p>
    </td>
    </tr>
    <tr id="row2984183611420"><td class="cellrowborder" valign="top" width="15.920000000000002%" headers="mcps1.2.4.1.1 "><p id="p1598317367425"><a name="p1598317367425"></a><a name="p1598317367425"></a>Create from backup</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.18%" headers="mcps1.2.4.1.2 "><p id="p119831336134216"><a name="p119831336134216"></a><a name="p119831336134216"></a>Optional</p>
    <p id="p09831736124215"><a name="p09831736124215"></a><a name="p09831736124215"></a>Specifies to create the disk from a backup.</p>
    <p id="p119841336194213"><a name="p119841336194213"></a><a name="p119841336194213"></a>Click <span class="uicontrol" id="uicontrol544415541"><a name="uicontrol544415541"></a><a name="uicontrol544415541"></a><b>Select Data Source</b></span> and choose <span class="uicontrol" id="uicontrol817747703"><a name="uicontrol817747703"></a><a name="uicontrol817747703"></a><b>Create from backup</b></span>. On the displayed page, select the target backup and click <span class="uicontrol" id="uicontrol1059505053"><a name="uicontrol1059505053"></a><a name="uicontrol1059505053"></a><b>OK</b></span>.</p>
    <div class="note" id="note19984536174218"><a name="note19984536174218"></a><a name="note19984536174218"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul19841836134210"></a><a name="ul19841836134210"></a><ul id="ul19841836134210"><li>You can select a backup created by the current tenant or shared with the current tenant by another tenant.</li><li>One backup cannot be used for concurrent disk creation operations at the same time. For example, if you are creating disk A from a backup, this backup can be used to create another disk only after disk A has been created.</li><li>If a disk is created from a backup of a system disk, the new disk can be used as a data disk only.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="19.900000000000002%" headers="mcps1.2.4.1.3 "><p id="p1498418368420"><a name="p1498418368420"></a><a name="p1498418368420"></a>autobackup-001</p>
    </td>
    </tr>
    <tr id="row2985103644214"><td class="cellrowborder" valign="top" width="15.920000000000002%" headers="mcps1.2.4.1.1 "><p id="p3984143674212"><a name="p3984143674212"></a><a name="p3984143674212"></a>Create from snapshot</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.18%" headers="mcps1.2.4.1.2 "><p id="p5984336134213"><a name="p5984336134213"></a><a name="p5984336134213"></a>Optional</p>
    <p id="p398403644212"><a name="p398403644212"></a><a name="p398403644212"></a>Specifies to create the disk from a snapshot.</p>
    <p id="p15984153616422"><a name="p15984153616422"></a><a name="p15984153616422"></a>Click <span class="uicontrol" id="uicontrol1197007394"><a name="uicontrol1197007394"></a><a name="uicontrol1197007394"></a><b>Select Data Source</b></span> and choose <span class="uicontrol" id="uicontrol1474011893"><a name="uicontrol1474011893"></a><a name="uicontrol1474011893"></a><b>Create from snapshot</b></span>. On the displayed page, select the target snapshot and click <span class="uicontrol" id="uicontrol1999769601"><a name="uicontrol1999769601"></a><a name="uicontrol1999769601"></a><b>OK</b></span>.</p>
    <div class="note" id="note8985236204211"><a name="note8985236204211"></a><a name="note8985236204211"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul109855362427"></a><a name="ul109855362427"></a><ul id="ul109855362427"><li>The disk type of the new disk is the same as that of the snapshot's source disk.</li><li>The device type of the new disk is the same as that of the snapshot's source disk.</li><li>The encryption attribute of the new disk is the same as that of the snapshot's source disk.</li></ul>
    <p id="p1298553612429"><a name="p1298553612429"></a><a name="p1298553612429"></a>For details about the disk creation from snapshots, see <a href="creating-an-evs-disk-from-a-snapshot.md">Creating an EVS Disk from a Snapshot</a>.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="19.900000000000002%" headers="mcps1.2.4.1.3 "><p id="p14985636134213"><a name="p14985636134213"></a><a name="p14985636134213"></a>snapshot-001</p>
    </td>
    </tr>
    <tr id="row99899364420"><td class="cellrowborder" valign="top" width="15.920000000000002%" headers="mcps1.2.4.1.1 "><p id="p198817360422"><a name="p198817360422"></a><a name="p198817360422"></a>Disk Sharing</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.18%" headers="mcps1.2.4.1.2 "><p id="p109887363422"><a name="p109887363422"></a><a name="p109887363422"></a>Optional</p>
    <a name="ul1098973615425"></a><a name="ul1098973615425"></a><ul id="ul1098973615425"><li>If <strong id="b84235270618446"><a name="b84235270618446"></a><a name="b84235270618446"></a>Share</strong> is not selected, a common disk is created.</li><li>If <strong id="b535330305"><a name="b535330305"></a><a name="b535330305"></a>Share</strong> is selected, a shared disk is created, and the shared disk can be attached to multiple <span id="text6882325758511"><a name="text6882325758511"></a><a name="text6882325758511"></a>servers</span>.</li></ul>
    <p id="p1198919366428"><a name="p1198919366428"></a><a name="p1198919366428"></a>When both <span class="parmname" id="parmname1837218253"><a name="parmname1837218253"></a><a name="parmname1837218253"></a><b>SCSI</b></span> and <span class="parmname" id="parmname1537718821"><a name="parmname1537718821"></a><a name="parmname1537718821"></a><b>Share</b></span> are selected, a shared SCSI disk is created.</p>
    <div class="note" id="note898912368427"><a name="note898912368427"></a><a name="note898912368427"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p598915364424"><a name="p598915364424"></a><a name="p598915364424"></a>The sharing attribute of a disk cannot be changed once the disk has been created.</p>
    <p id="p09891336134219"><a name="p09891336134219"></a><a name="p09891336134219"></a>For details about shared EVS disks, see <a href="managing-a-shared-evs-disk.md">Managing a Shared EVS Disk</a>.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="19.900000000000002%" headers="mcps1.2.4.1.3 "><p id="p189891336114212"><a name="p189891336114212"></a><a name="p189891336114212"></a>-</p>
    </td>
    </tr>
    <tr id="row17990136144217"><td class="cellrowborder" valign="top" width="15.920000000000002%" headers="mcps1.2.4.1.1 "><p id="p89891436104219"><a name="p89891436104219"></a><a name="p89891436104219"></a>SCSI</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.18%" headers="mcps1.2.4.1.2 "><p id="p89898367422"><a name="p89898367422"></a><a name="p89898367422"></a>Optional</p>
    <a name="ul1599043654217"></a><a name="ul1599043654217"></a><ul id="ul1599043654217"><li>If <span class="parmname" id="parmname1497567905161058"><a name="parmname1497567905161058"></a><a name="parmname1497567905161058"></a><b>SCSI</b></span> is not selected, a VBD disk is created. VBD is the default device type of EVS disks.</li><li>If <span class="parmname" id="parmname1861345965"><a name="parmname1861345965"></a><a name="parmname1861345965"></a><b>SCSI</b></span> is selected, a SCSI disk is created. Such disks allow the server OS to directly access the underlying storage media and send SCSI commands to the disks.</li></ul>
    <div class="note" id="note1399063674220"><a name="note1399063674220"></a><a name="note1399063674220"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p999010363428"><a name="p999010363428"></a><a name="p999010363428"></a>The device type of a disk cannot be changed once the disk has been created.</p>
    <p id="p11990183634217"><a name="p11990183634217"></a><a name="p11990183634217"></a>For details about the ECS types, OSs, and ECS software supported by SCSI EVS disks, see <a href="device-types-and-usage-instructions.md">Device Types and Usage Instructions</a>.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="19.900000000000002%" headers="mcps1.2.4.1.3 "><p id="p18990736114220"><a name="p18990736114220"></a><a name="p18990736114220"></a>-</p>
    </td>
    </tr>
    <tr id="row12993153624217"><td class="cellrowborder" valign="top" width="15.920000000000002%" headers="mcps1.2.4.1.1 "><p id="p29910363426"><a name="p29910363426"></a><a name="p29910363426"></a>Encryption</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.18%" headers="mcps1.2.4.1.2 "><p id="p109911436184210"><a name="p109911436184210"></a><a name="p109911436184210"></a>Optional</p>
    <p id="p399113614424"><a name="p399113614424"></a><a name="p399113614424"></a>Disk encryption is used for data disk encryption only. For system disk encryption, see the <i><cite id="citef4388b6885de4292b71c351b65c8dd50175020"><a name="citef4388b6885de4292b71c351b65c8dd50175020"></a><a name="citef4388b6885de4292b71c351b65c8dd50175020"></a>Image Management Service User Guide</cite></i>.</p>
    <p id="p1399118363429"><a name="p1399118363429"></a><a name="p1399118363429"></a>To use the disk encryption function, select <strong id="b18457415243"><a name="b18457415243"></a><a name="b18457415243"></a>Encryption</strong>. The displayed dialog box contains the following parameters:</p>
    <a name="ul1199111367421"></a><a name="ul1199111367421"></a><ul id="ul1199111367421"><li>Create Agency<p id="p109916369423"><a name="p109916369423"></a><a name="p109916369423"></a>An agency is a trust relationship between two tenants or services. A tenant can create an agency to grant resource access rights to another tenant or service. If the KMS access rights are not granted to EVS, the <strong id="b172328317249"><a name="b172328317249"></a><a name="b172328317249"></a>Create Agency</strong> dialog box will be displayed. Otherwise, it will not be displayed.</p>
    <p id="p189918364421"><a name="p189918364421"></a><a name="p189918364421"></a>Click <span class="uicontrol" id="uicontrol11216185249"><a name="uicontrol11216185249"></a><a name="uicontrol11216185249"></a><b>Yes</b></span> to grant the KMS access rights to EVS. After the rights have been granted, EVS can obtain KMS keys to encrypt or decrypt EVS disks.</p>
    <p id="p199113617422"><a name="p199113617422"></a><a name="p199113617422"></a>After the KMS access rights have been granted, follow-up operations do not require the rights to be granted again.</p>
    </li></ul>
    <a name="ul1799263664217"></a><a name="ul1799263664217"></a><ul id="ul1799263664217"><li>KMS Key Name<div class="note" id="note69914366421"><a name="note69914366421"></a><a name="note69914366421"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p599119360424"><a name="p599119360424"></a><a name="p599119360424"></a><strong id="b112993643"><a name="b112993643"></a><a name="b112993643"></a>KMS Key Name</strong> is displayed only after the KMS access rights have been granted. For details, see "Create Agency" above.</p>
    </div></div>
    <div class="p" id="p16992183614216"><a name="p16992183614216"></a><a name="p16992183614216"></a><span class="parmname" id="parmname908389917194929"><a name="parmname908389917194929"></a><a name="parmname908389917194929"></a><b>KMS Key Name</b></span> is the identifier of the key, and you can use <span class="parmname" id="parmname1928513733205950"><a name="parmname1928513733205950"></a><a name="parmname1928513733205950"></a><b>KMS Key Name</b></span> to specify the KMS key that is to be used for encryption. One of the following keys can be used:<a name="ul1799243624213"></a><a name="ul1799243624213"></a><ul id="ul1799243624213"><li>Default Master Key: After the KMS access rights have been granted to EVS, the system automatically creates a Default Master Key and names it <span class="parmname" id="parmname1396879911"><a name="parmname1396879911"></a><a name="parmname1396879911"></a><b>evs/default</b></span>.</li><li>CMKs: Existing or newly created CMKs. For details, see <span class="menucascade" id="menucascade1800490284"><a name="menucascade1800490284"></a><a name="menucascade1800490284"></a><b><span class="uicontrol" id="uicontrol1163911522"><a name="uicontrol1163911522"></a><a name="uicontrol1163911522"></a>Management</span></b> &gt; <b><span class="uicontrol" id="uicontrol702248970"><a name="uicontrol702248970"></a><a name="uicontrol702248970"></a>Creating a CMK</span></b></span> in the <em id="i1541960636"><a name="i1541960636"></a><a name="i1541960636"></a>Key Management Service User Guide</em>.</li></ul>
    </div>
    </li></ul>
    <div class="note" id="note799211361423"><a name="note799211361423"></a><a name="note799211361423"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul109922036184217"></a><a name="ul109922036184217"></a><ul id="ul109922036184217"><li>Before you use the EVS disk encryption function, KMS access rights need to be granted to EVS. If you have the right to grant the permission, grant the KMS access rights to EVS directly. If you do not have this permission, contact a user with the security administrator rights to grant KMS access rights to EVS, then repeat the preceding operations.</li><li>The encryption attribute of a disk cannot be changed after the disk is created.</li></ul>
    <p id="p139921367428"><a name="p139921367428"></a><a name="p139921367428"></a>For details, see <a href="evs-disk-encryption.md">EVS Disk Encryption</a>.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="19.900000000000002%" headers="mcps1.2.4.1.3 "><p id="p17992123654211"><a name="p17992123654211"></a><a name="p17992123654211"></a>-</p>
    </td>
    </tr>
    <tr id="row19994183614428"><td class="cellrowborder" valign="top" width="15.920000000000002%" headers="mcps1.2.4.1.1 "><p id="p4993163610426"><a name="p4993163610426"></a><a name="p4993163610426"></a>Auto Backup</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.18%" headers="mcps1.2.4.1.2 "><p id="p15993183654220"><a name="p15993183654220"></a><a name="p15993183654220"></a>Optional</p>
    <p id="p16993173674220"><a name="p16993173674220"></a><a name="p16993173674220"></a>If auto backup is enabled, the system automatically creates backups for the disk data at specified time points and deletes outdated backups according to the configured backup policy.</p>
    <p id="p799319367426"><a name="p799319367426"></a><a name="p799319367426"></a>When <strong id="b8423527061186"><a name="b8423527061186"></a><a name="b8423527061186"></a>Enable</strong> is selected, a backup policy must be configured. You can either use the default backup policy or customize the policy based on your service requirements.</p>
    <div class="note" id="note129941336154210"><a name="note129941336154210"></a><a name="note129941336154210"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p99938368422"><a name="p99938368422"></a><a name="p99938368422"></a>For details about the backup policy, see <a href="managing-evs-backup.md">Managing EVS Backup</a>.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="19.900000000000002%" headers="mcps1.2.4.1.3 "><p id="p13994123684212"><a name="p13994123684212"></a><a name="p13994123684212"></a>-</p>
    </td>
    </tr>
    <tr id="row14998636154217"><td class="cellrowborder" valign="top" width="15.920000000000002%" headers="mcps1.2.4.1.1 "><p id="p09941136134213"><a name="p09941136134213"></a><a name="p09941136134213"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.18%" headers="mcps1.2.4.1.2 "><p id="p599423616421"><a name="p599423616421"></a><a name="p599423616421"></a>Optional</p>
    <p id="p1099463615428"><a name="p1099463615428"></a><a name="p1099463615428"></a>During the EVS disk creation, you can tag the EVS resources. Tags identify cloud resources for purposes of easy categorization and quick search.</p>
    <div class="p" id="p799853664212"><a name="p799853664212"></a><a name="p799853664212"></a>A tag is composed of a key-value pair.<a name="ul1799712361420"></a><a name="ul1799712361420"></a><ul id="ul1799712361420"><li>Key: Mandatory if the disk is going to be tagged<a name="ul1599593611424"></a><a name="ul1599593611424"></a><ul id="ul1599593611424"><li>Must be unique for each resource.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only digits, letters, hyphens (-), and underscores (_).</li></ul>
    </li><li>Value: Optional if the disk is going to be tagged<a name="ul799783611429"></a><a name="ul799783611429"></a><ul id="ul799783611429"><li>Can contain a maximum of 43 characters.</li><li>Can contain only digits, letters, hyphens (-), and underscores (_).</li></ul>
    </li></ul>
    <div class="note" id="note19989363423"><a name="note19989363423"></a><a name="note19989363423"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul8997133624218"></a><a name="ul8997133624218"></a><ul id="ul8997133624218"><li>A maximum of 10 tags can be added for an EVS disk.</li><li>Tag keys of the same EVS disk must be unique.</li><li>Except for tagging the disk during disk creation, you can also add, modify, or delete tags for existing disks. For details, see <a href="managing-a-tag.md">Managing a Tag</a>.</li></ul>
    <p id="p13631933203016"><a name="p13631933203016"></a><a name="p13631933203016"></a>For details about tags, see the <em id="i1970719132416"><a name="i1970719132416"></a><a name="i1970719132416"></a>Tag Management Service User Guide</em>.</p>
    </div></div>
    </div>
    </td>
    <td class="cellrowborder" valign="top" width="19.900000000000002%" headers="mcps1.2.4.1.3 "><p id="p99981536104215"><a name="p99981536104215"></a><a name="p99981536104215"></a>-</p>
    </td>
    </tr>
    <tr id="row18999183619422"><td class="cellrowborder" valign="top" width="15.920000000000002%" headers="mcps1.2.4.1.1 "><p id="p299863624215"><a name="p299863624215"></a><a name="p299863624215"></a>Disk Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.18%" headers="mcps1.2.4.1.2 "><p id="p16998736144210"><a name="p16998736144210"></a><a name="p16998736144210"></a>Mandatory</p>
    <a name="ul599813369428"></a><a name="ul599813369428"></a><ul id="ul599813369428"><li>If you create disks one by one, this parameter value is used as the actual disk name.<p id="p149981236154219"><a name="p149981236154219"></a><a name="p149981236154219"></a>The name can contain a maximum of 64 characters.</p>
    </li><li>If you create disks in a batch, this parameter value is used as the prefix of disk names, and one disk name will be composed of this parameter value and a four-digit number.<p id="p13998133694218"><a name="p13998133694218"></a><a name="p13998133694218"></a>The name can contain a maximum of 59 characters.</p>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="19.900000000000002%" headers="mcps1.2.4.1.3 "><p id="p1399912369420"><a name="p1399912369420"></a><a name="p1399912369420"></a>For example, if you create two disks and set <span class="parmvalue" id="parmvalue1555518781"><a name="parmvalue1555518781"></a><a name="parmvalue1555518781"></a><b>volume</b></span> for <strong id="b2079410964"><a name="b2079410964"></a><a name="b2079410964"></a>Disk Name</strong>, the EVS disk names will be <span class="parmvalue" id="parmvalue831044111"><a name="parmvalue831044111"></a><a name="parmvalue831044111"></a><b>volume-0001</b></span> and <span class="parmvalue" id="parmvalue1517007758"><a name="parmvalue1517007758"></a><a name="parmvalue1517007758"></a><b>volume-0002</b></span>.</p>
    </td>
    </tr>
    <tr id="row72537144213"><td class="cellrowborder" valign="top" width="15.920000000000002%" headers="mcps1.2.4.1.1 "><p id="p19093714215"><a name="p19093714215"></a><a name="p19093714215"></a>Quantity</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.18%" headers="mcps1.2.4.1.2 "><p id="p31153710428"><a name="p31153710428"></a><a name="p31153710428"></a>Optional</p>
    <p id="p61203784215"><a name="p61203784215"></a><a name="p61203784215"></a>Specifies the number of disks to be created. The default value is set to <span class="parmvalue" id="parmvalue1377885403"><a name="parmvalue1377885403"></a><a name="parmvalue1377885403"></a><b>1</b></span>, which means only one disk is created. Currently, you can create up to 100 disks at a time.</p>
    <div class="note" id="note21103712426"><a name="note21103712426"></a><a name="note21103712426"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul8143719427"></a><a name="ul8143719427"></a><ul id="ul8143719427"><li>If the disk is created from a backup, batch creation is not possible, and this parameter must be set to <span class="parmname" id="parmname621614722"><a name="parmname621614722"></a><a name="parmname621614722"></a><b>1</b></span>.</li><li>If the disk is created from a snapshot, batch creation is not possible, and this parameter must be set to <span class="parmname" id="parmname430007285"><a name="parmname430007285"></a><a name="parmname430007285"></a><b>1</b></span>.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="19.900000000000002%" headers="mcps1.2.4.1.3 "><p id="p412375420"><a name="p412375420"></a><a name="p412375420"></a>1</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **Create Now**.
7.  On the  **Details**  page, check the disk details.
    -   If you do not need to modify the specifications, click  **Submit**  to start the creation.
    -   If you need to modify the specifications, click  **Previous**  to modify parameters.

8.  In the disk list, view the disk status.

    When the disk status changes to  **Available**, the disk is successfully created.


