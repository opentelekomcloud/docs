# Step 1: Create a File System<a name="en-us_topic_0034428727"></a>

You can create a file system and mount it to multiple ECSs. Then the ECSs can share the file system. 

## Prerequisites<a name="section4520355910337"></a>

1.  Before creating a file system, ensure that a VPC is available.

    If no VPC is available, create a VPC by referring to section "Creating a VPC" in the  _VPC User Guide_.

2.  Before creating a file system, ensure that an ECS is available and the ECS belongs to the created VPC.

    If no ECS is available, create an ECS by referring to "Creating an ECS" in the  _Elastic Cloud Server User Guide_.


## Logging In to the Management Console<a name="section370015372416"></a>

1.  Log in to the management console using a cloud account.
2.  From the drop-down list in front of  **Homepage**, select a region and a project.
3.  Choose  **Service List**  \>  **Storage**  \>  **Scalable File Service**. The console page is displayed.

## Creating an SFS File System<a name="section62423454145852"></a>

1.  In the upper right corner of the page, click  **Create File System**.
2.  In the dialog box shown in  [Figure 1](#fig18678655184217), set the parameters as described in  [Table 1](#table21372620111743).

    **Figure  1**  Creating a file system<a name="fig18678655184217"></a>  
    ![](figures/creating-a-file-system.png "creating-a-file-system")

    **Table  1**  Parameter description

    <a name="table21372620111743"></a>
    <table><thead align="left"><tr id="row63053364111743"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="p63439848111743"><a name="p63439848111743"></a><a name="p63439848111743"></a><strong id="b842352706143129"><a name="b842352706143129"></a><a name="b842352706143129"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40%" id="mcps1.2.4.1.2"><p id="p38354059111743"><a name="p38354059111743"></a><a name="p38354059111743"></a><strong id="b842352706143138"><a name="b842352706143138"></a><a name="b842352706143138"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27%" id="mcps1.2.4.1.3"><p id="p19671083111743"><a name="p19671083111743"></a><a name="p19671083111743"></a><strong id="b842352706143150"><a name="b842352706143150"></a><a name="b842352706143150"></a>Remarks</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row553014855911"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p0533138175910"><a name="p0533138175910"></a><a name="p0533138175910"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.2 "><p id="p1850816355595"><a name="p1850816355595"></a><a name="p1850816355595"></a>This parameter is mandatory.</p>
    <p id="p1508635135912"><a name="p1508635135912"></a><a name="p1508635135912"></a>Specifies the region of the tenant. Select the current region from the drop-down list in the upper left corner of the page.</p>
    </td>
    <td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.3 "><p id="p145338813592"><a name="p145338813592"></a><a name="p145338813592"></a>You are advised to select the same region as that of the ECS.</p>
    </td>
    </tr>
    <tr id="row42822021111743"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p46031658111743"><a name="p46031658111743"></a><a name="p46031658111743"></a>AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.2 "><p id="p41395637142015"><a name="p41395637142015"></a><a name="p41395637142015"></a>A geographical area with an independent network and an independent power supply</p>
    </td>
    <td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.3 "><p id="p64712299142015"><a name="p64712299142015"></a><a name="p64712299142015"></a>You are advised to select the same AZ as that of the ECS.</p>
    </td>
    </tr>
    <tr id="row13728109142946"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p27756971142958"><a name="p27756971142958"></a><a name="p27756971142958"></a>Protocol Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.2 "><p id="p33722215142958"><a name="p33722215142958"></a><a name="p33722215142958"></a>SFS supports NFS (only the NFSv3 protocol currently) for file system access.</p>
    </td>
    <td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.3 "><p id="p14192182118413"><a name="p14192182118413"></a><a name="p14192182118413"></a>-</p>
    </td>
    </tr>
    <tr id="row13094438111743"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p54016589111743"><a name="p54016589111743"></a><a name="p54016589111743"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.2 "><p id="p276310231694"><a name="p276310231694"></a><a name="p276310231694"></a>This parameter is mandatory.</p>
    <p id="p63273538911"><a name="p63273538911"></a><a name="p63273538911"></a>An ECS cannot access file systems in a different VPC. Select the VPC to which the ECS belongs.</p>
    <div class="note" id="note12561144415432"><a name="note12561144415432"></a><a name="note12561144415432"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul8290124416475"></a><a name="ul8290124416475"></a><ul id="ul8290124416475"><li>By default, all ECSs in a VPC have the same rights. You can modify the VPC in the future.</li><li>Upon creation, only one VPC can be added for each file system. After a file system is created, you can configure multiple VPCs by referring to <a href="configuring-vpcs.md">Configuring VPCs</a> for the SFS file system.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.3 "><p id="p521417761311"><a name="p521417761311"></a><a name="p521417761311"></a>Click <span class="uicontrol" id="uicontrol91032091671143"><a name="uicontrol91032091671143"></a><a name="uicontrol91032091671143"></a><b>View VPC</b></span> to view existing VPCs or create a new one.</p>
    </td>
    </tr>
    <tr id="row8368765111743"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p1140019210106"><a name="p1140019210106"></a><a name="p1140019210106"></a>Maximum Capacity</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.2 "><p id="p51546843143045"><a name="p51546843143045"></a><a name="p51546843143045"></a>Maximum capacity of a single file system. When the used capacity of a file system reaches this value, no more data can be written to the file system. You need to expand the file system.</p>
    </td>
    <td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.3 "><p id="p14544773143045"><a name="p14544773143045"></a><a name="p14544773143045"></a>The value ranges from <strong id="b495219246465"><a name="b495219246465"></a><a name="b495219246465"></a>1 GB</strong> to <strong id="b9294928174619"><a name="b9294928174619"></a><a name="b9294928174619"></a>512,000 GB</strong>.</p>
    </td>
    </tr>
    <tr id="row1142125917469"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p16422105964613"><a name="p16422105964613"></a><a name="p16422105964613"></a>Encryption</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.2 "><p id="p1249678016465"><a name="p1249678016465"></a><a name="p1249678016465"></a>This parameter is optional.</p>
    <p id="p4536216316465"><a name="p4536216316465"></a><a name="p4536216316465"></a>This parameter specifies whether a file system is encrypted. You can create either an encrypted or an unencrypted file system, but you cannot change the encryption settings of an existing file system. If <strong id="b842352706173224"><a name="b842352706173224"></a><a name="b842352706173224"></a>Encryption</strong> is selected, the following parameters will be displayed:</p>
    <a name="ul20582533113110"></a><a name="ul20582533113110"></a><ul id="ul20582533113110"><li><strong id="b7111113015479"><a name="b7111113015479"></a><a name="b7111113015479"></a>Create Agency</strong><p id="p10918109164013"><a name="p10918109164013"></a><a name="p10918109164013"></a>If the KMS access rights are not granted to SFS, this button will be displayed. Otherwise, this button will not be displayed.</p>
    <p id="p891949134019"><a name="p891949134019"></a><a name="p891949134019"></a>Click <span class="uicontrol" id="uicontrol1050882406174133"><a name="uicontrol1050882406174133"></a><a name="uicontrol1050882406174133"></a><b>Create Agency</b></span> to grant SFS the permissions to access KMS. The system automatically creates an agency and names it <span class="parmvalue" id="parmvalue277326926205433"><a name="parmvalue277326926205433"></a><a name="parmvalue277326926205433"></a><b>SFSAccessKMS</b></span>. When <span class="parmname" id="parmname880136436174250"><a name="parmname880136436174250"></a><a name="parmname880136436174250"></a><b>SFSAccessKMS</b></span> is displayed for <span class="parmname" id="parmname778044650114843"><a name="parmname778044650114843"></a><a name="parmname778044650114843"></a><b>Agency Name</b></span>, the KMS access rights have been granted to SFS, and SFS can obtain KMS keys for encrypting or decrypting the file system. After the rights are granted, follow-up operations do not need granting rights again.</p>
    </li></ul>
    <a name="ul25502347165536"></a><a name="ul25502347165536"></a><ul id="ul25502347165536"><li><strong id="b422813416558"><a name="b422813416558"></a><a name="b422813416558"></a>Agency Name</strong><a name="ul8513134614618"></a><a name="ul8513134614618"></a><ul id="ul8513134614618"><li>Agency: An agency is a trust relationship between two tenants or services. A tenant can create an agency to grant resource access rights to another tenant or service.</li><li><strong id="b89331140113116"><a name="b89331140113116"></a><a name="b89331140113116"></a>SFSAccessKMS</strong>: If <span class="parmname" id="parmname62168185217525"><a name="parmname62168185217525"></a><a name="parmname62168185217525"></a><b>Agency Name</b></span> is <span class="parmname" id="parmname283915025175229"><a name="parmname283915025175229"></a><a name="parmname283915025175229"></a><b>SFSAccessKMS</b></span>, KMS keys have been assigned to SFS to encrypt or decrypt the file system.</li></ul>
    </li><li><strong id="b1150162925716"><a name="b1150162925716"></a><a name="b1150162925716"></a>KMS key name</strong><div class="note" id="note1852843918438"><a name="note1852843918438"></a><a name="note1852843918438"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p15528183964319"><a name="p15528183964319"></a><a name="p15528183964319"></a><strong id="b842352706194528"><a name="b842352706194528"></a><a name="b842352706194528"></a>KMS key name</strong> is displayed only after the agency named <strong id="b842352706194644"><a name="b842352706194644"></a><a name="b842352706194644"></a>SFSAccessKMS</strong> has been created. For details, see <strong id="b12408124923211"><a name="b12408124923211"></a><a name="b12408124923211"></a>Create Agency</strong> above.</p>
    </div></div>
    <p id="p25281739184315"><a name="p25281739184315"></a><a name="p25281739184315"></a><span class="parmname" id="parmname908389917194929"><a name="parmname908389917194929"></a><a name="parmname908389917194929"></a><b>KMS key name</b></span> is the identifier of the key, and you can use <span class="parmname" id="parmname1928513733205950"><a name="parmname1928513733205950"></a><a name="parmname1928513733205950"></a><b>KMS key name</b></span> to specify the KMS key that is to be used for encryption. You can select one of the following keys:</p>
    <a name="ul9529539104319"></a><a name="ul9529539104319"></a><ul id="ul9529539104319"><li><strong id="b629161014814"><a name="b629161014814"></a><a name="b629161014814"></a>Default master key</strong>: After the KMS access rights have been granted to SFS, the system automatically creates a <strong id="b169851153484"><a name="b169851153484"></a><a name="b169851153484"></a>Default master key</strong> and names it <span class="parmname" id="parmname5149578616599"><a name="parmname5149578616599"></a><a name="parmname5149578616599"></a><b>sfs/default</b></span>.</li><li><strong id="b20291822134818"><a name="b20291822134818"></a><a name="b20291822134818"></a>Customer master keys (CMKs)</strong>: Existing or newly created keys. For details, see "Creating a CMK" in the <em id="i2897237181"><a name="i2897237181"></a><a name="i2897237181"></a>Key Management Service User Guide</em>.</li></ul>
    <div class="note" id="note1752943984310"><a name="note1752943984310"></a><a name="note1752943984310"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1752953934312"><a name="p1752953934312"></a><a name="p1752953934312"></a>Before you use the encryption function, the KMS access rights must be granted to SFS. If you have the right to grant the permission, grant SFS the permissions to access KMS directly. Otherwise, you need to contact the system administrator to obtain the "Security Administrator" rights first. For more operations, see <a href="file-system-encryption.md">File System Encryption</a>.</p>
    </div></div>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.3 "><p id="p44221059204615"><a name="p44221059204615"></a><a name="p44221059204615"></a>-</p>
    </td>
    </tr>
    <tr id="row17188105215312"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p3468226417632"><a name="p3468226417632"></a><a name="p3468226417632"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.2 "><p id="p5780003817632"><a name="p5780003817632"></a><a name="p5780003817632"></a>User-defined name of the file system. If you create more than one file system, a name suffix is added to each file system name automatically. For example, if you set the name to <strong id="b842352706101053"><a name="b842352706101053"></a><a name="b842352706101053"></a>sfs-name</strong> for two new file systems, the two file system names will be <strong id="b842352706101232"><a name="b842352706101232"></a><a name="b842352706101232"></a>sfs-name-001</strong> and <strong id="b842352706101237"><a name="b842352706101237"></a><a name="b842352706101237"></a>sfs-name-002</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.3 "><p id="p5129151217632"><a name="p5129151217632"></a><a name="p5129151217632"></a>The value can contain only letters, digits, underscores (_), and hyphens (-). When creating a single file system, the value can contain a maximum of 255 characters. When creating file systems in batches, enter 1 to 251 characters.</p>
    </td>
    </tr>
    <tr id="row1519101812360"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p66368562111743"><a name="p66368562111743"></a><a name="p66368562111743"></a>Quantity</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.2 "><p id="p38014935143121"><a name="p38014935143121"></a><a name="p38014935143121"></a>Number of file systems to be created.</p>
    </td>
    <td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.3 "><p id="p1929315710378"><a name="p1929315710378"></a><a name="p1929315710378"></a>Each cloud account can have a total of 512,000 GB for its file systems. Each cloud account can create a maximum of 10 file systems, one by one or in a batch.</p>
    <p id="p28800519103959"><a name="p28800519103959"></a><a name="p28800519103959"></a>If the quantity or total capacity of the file systems you are creating exceeds the upper limit, contact customer service to apply for a higher quota. For details, see <a href="https://docs.otc.t-systems.com/en-us/faq/iaas/en-us_topic_0040259342.html" target="_blank" rel="noopener noreferrer">How Can I Apply for a Higher Quota?</a></p>
    </td>
    </tr>
    <tr id="row41746319498"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p4174113104914"><a name="p4174113104914"></a><a name="p4174113104914"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.2 "><p id="p5904190816573"><a name="p5904190816573"></a><a name="p5904190816573"></a>This parameter is optional.</p>
    <p id="p6161512716573"><a name="p6161512716573"></a><a name="p6161512716573"></a>When creating a file system, you can bind tags to it. Tags are used to identify file system resources, and you can classify and search for file system resources by tag.</p>
    <div class="p" id="p62901921145616"><a name="p62901921145616"></a><a name="p62901921145616"></a>Tags are composed of key-value pairs.<a name="ul2476942816573"></a><a name="ul2476942816573"></a><ul id="ul2476942816573"><li>Key: Mandatory if the file system is going to be tagged.<p id="p6016664116573"><a name="p6016664116573"></a><a name="p6016664116573"></a>A tag key can contain a maximum of 36 characters. It can only contain letters, digits, hyphens (-), and underscores (_).</p>
    </li><li>Value: Optional if the file system is going to be tagged. It can be an empty character string. A tag value can contain a maximum of 43 characters. It can only contain letters, digits, hyphens (-), and underscores (_).<div class="note" id="note1899530816573"><a name="note1899530816573"></a><a name="note1899530816573"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul3674004916573"></a><a name="ul3674004916573"></a><ul id="ul3674004916573"><li>A maximum of 10 tags can be added to one file system.</li><li>The tag keys of the same file system must be unique.</li><li>Except for tagging the file system during disk creation, you can also add, modify, or delete tags for existing file systems.</li></ul>
    </div></div>
    </li></ul>
    </div>
    </td>
    <td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.3 "><p id="p201741839491"><a name="p201741839491"></a><a name="p201741839491"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>

3.  Click  **Create Now**  after the configuration is complete.
4.  Confirm the file system information and click  **Submit**.
5.  Go back to the file system list.

    If the status of the created file system is  **Available**, the file system is created successfully. If the status is  **Creation Failed**, contact the administrator.


