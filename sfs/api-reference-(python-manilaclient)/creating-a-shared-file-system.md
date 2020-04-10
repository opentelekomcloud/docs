# Creating a Shared File System<a name="EN-US_TOPIC_0090543713"></a>

## Function<a name="section19292742153528"></a>

This interface is used to create a shared file system.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This interface is an asynchronous interface. Successful command execution only indicates that the command is successfully delivered. Later, you can query the status and path of the shared file system by referring to  [Querying Details About a Shared File System](querying-details-about-a-shared-file-system.md)  to identify whether the creation is complete and successful.  

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>After a share is created successfully, the share can be used only after you add share access rules by referring to  [Adding Share Access Rules](adding-share-access-rules.md).  

## Command<a name="section38656901153528"></a>

-   Usage

    ```
    manila create [--snapshot-id <snapshot-id>] [--name <name>]
                  [--metadata [<key=value> [<key=value> ...]]]
                  [--share-network <network-info>]
                  [--description <description>] [--share-type <share-type>]
                  [--public] [--availability-zone <availability-zone>]
                  [--consistency-group <consistency-group>]
                  <share_protocol> <size>
    ```

-   Parameter description

    <a name="table27214586153528"></a>
    <table><thead align="left"><tr id="row23638080153528"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.5.1.1"><p id="p35636289153528"><a name="p35636289153528"></a><a name="p35636289153528"></a><strong id="b842352706155520"><a name="b842352706155520"></a><a name="b842352706155520"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.1.5.1.2"><p id="p858291153528"><a name="p858291153528"></a><a name="p858291153528"></a><strong id="b842352706155525"><a name="b842352706155525"></a><a name="b842352706155525"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.1.5.1.3"><p id="p2412733153528"><a name="p2412733153528"></a><a name="p2412733153528"></a><strong id="b842352706155528"><a name="b842352706155528"></a><a name="b842352706155528"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.494949494949495%" id="mcps1.1.5.1.4"><p id="p61213704153528"><a name="p61213704153528"></a><a name="p61213704153528"></a><strong id="b842352706155531"><a name="b842352706155531"></a><a name="b842352706155531"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59363004153528"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p43673983153528"><a name="p43673983153528"></a><a name="p43673983153528"></a>share_protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p47931772153528"><a name="p47931772153528"></a><a name="p47931772153528"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p57268313153528"><a name="p57268313153528"></a><a name="p57268313153528"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p11516537101641"><a name="p11516537101641"></a><a name="p11516537101641"></a>Specifies the protocol for sharing file systems. The value is <strong id="b110975476995629"><a name="b110975476995629"></a><a name="b110975476995629"></a>NFS</strong>.</p>
    </td>
    </tr>
    <tr id="row6886964153528"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p20973177153528"><a name="p20973177153528"></a><a name="p20973177153528"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p64784046171956"><a name="p64784046171956"></a><a name="p64784046171956"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p31844545153528"><a name="p31844545153528"></a><a name="p31844545153528"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p22894227101728"><a name="p22894227101728"></a><a name="p22894227101728"></a>Specifies the size of the shared file system in GB.</p>
    </td>
    </tr>
    <tr id="row62115249153528"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p65279249153528"><a name="p65279249153528"></a><a name="p65279249153528"></a>snapshot-id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p53127826153528"><a name="p53127826153528"></a><a name="p53127826153528"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p8386651153528"><a name="p8386651153528"></a><a name="p8386651153528"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p27129783102229"><a name="p27129783102229"></a><a name="p27129783102229"></a>Specifies the UUID (0 to 36 characters) of the source snapshot that was used to create the shared file system. This parameter is reserved, because snapshots are not supported currently.</p>
    </td>
    </tr>
    <tr id="row6962628153528"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p26568961102326"><a name="p26568961102326"></a><a name="p26568961102326"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p4602261102326"><a name="p4602261102326"></a><a name="p4602261102326"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p37238861102326"><a name="p37238861102326"></a><a name="p37238861102326"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p63557778102326"><a name="p63557778102326"></a><a name="p63557778102326"></a>Specifies the name of the shared file system. The value contains 0 to 255 characters.</p>
    </td>
    </tr>
    <tr id="row46282950153528"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p417160110244"><a name="p417160110244"></a><a name="p417160110244"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p235540710244"><a name="p235540710244"></a><a name="p235540710244"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p5657031810244"><a name="p5657031810244"></a><a name="p5657031810244"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0064390791_p6058769417377"><a name="en-us_topic_0064390791_p6058769417377"></a><a name="en-us_topic_0064390791_p6058769417377"></a>Specifies the metadata information used to create the share. The value consists of one or more key and value pairs organized as a dictionary of strings. </p>
    <div class="caution" id="note92849475810"><a name="note92849475810"></a><a name="note92849475810"></a><span class="cautiontitle"> CAUTION: </span><div class="cautionbody"><p id="p18406141714416"><a name="p18406141714416"></a><a name="p18406141714416"></a>For security concerns, the API for modifying the metadata field is not enabled. Therefore, ensure that the parameters and values are correct when creating a share with data encryption using the metadata field.</p>
    </div></div>
    <div class="warning" id="note1328410415817"><a name="note1328410415817"></a><a name="note1328410415817"></a><span class="warningtitle"> WARNING: </span><div class="warningbody"><p id="p192838418589"><a name="p192838418589"></a><a name="p192838418589"></a>Unless otherwise specified (for example, <strong id="b842352706203556"><a name="b842352706203556"></a><a name="b842352706203556"></a>#sfs_crypt_key_id</strong>), the keys that comply with the following rules in the <strong id="b84235270620449"><a name="b84235270620449"></a><a name="b84235270620449"></a>metadata</strong> field are for internal use of the system. Do not customize the settings to avoid internal system errors caused by conflicts with system predefined keys.</p>
    <a name="ul162841542583"></a><a name="ul162841542583"></a><ul id="ul162841542583"><li>Key <strong id="b842352706105824"><a name="b842352706105824"></a><a name="b842352706105824"></a>share_used</strong>. Key <strong id="b57221420155815"><a name="b57221420155815"></a><a name="b57221420155815"></a>share_used</strong> is used to indicate the used capacity of the share.</li><li>Keys that start with <strong id="b842352706105911"><a name="b842352706105911"></a><a name="b842352706105911"></a>#sfs</strong>. The SFS system uses the keys that start with <strong id="b11442844241"><a name="b11442844241"></a><a name="b11442844241"></a>#sfs</strong> for internal use. Do not customize the key unless otherwise specified.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row54010649153528"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p46171242102426"><a name="p46171242102426"></a><a name="p46171242102426"></a>share-network</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p48883142102426"><a name="p48883142102426"></a><a name="p48883142102426"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p111599102426"><a name="p111599102426"></a><a name="p111599102426"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p9039564102426"><a name="p9039564102426"></a><a name="p9039564102426"></a>Specifies the UUID or name of the share network to which the share service belongs or will be created. This parameter is reserved, because share network management is not supported currently.</p>
    </td>
    </tr>
    <tr id="row30838117153528"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p6488575102626"><a name="p6488575102626"></a><a name="p6488575102626"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p55812541102626"><a name="p55812541102626"></a><a name="p55812541102626"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p24521939102626"><a name="p24521939102626"></a><a name="p24521939102626"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p40120042102626"><a name="p40120042102626"></a><a name="p40120042102626"></a>Describes the shared file system. The value contains 0 to 255 characters.</p>
    </td>
    </tr>
    <tr id="row41977955114953"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p44771156114953"><a name="p44771156114953"></a><a name="p44771156114953"></a>share-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p2585014114953"><a name="p2585014114953"></a><a name="p2585014114953"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p41424489115019"><a name="p41424489115019"></a><a name="p41424489115019"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p67049327115019"><a name="p67049327115019"></a><a name="p67049327115019"></a>Specifies the share type. This value determines the storage service type for the shared file system, such as high-performance storage (composed of SSDs) or large-capacity storage (composed of SATA disks). Currently, only one service type is supported and the value is automatically set to <strong id="b45821118192011"><a name="b45821118192011"></a><a name="b45821118192011"></a>default</strong>. Do not manually set it, because the file service will fail to be applied for if an unsupported type is entered.</p>
    </td>
    </tr>
    <tr id="row14491587102645"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p61298295102658"><a name="p61298295102658"></a><a name="p61298295102658"></a>public</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p66214864102658"><a name="p66214864102658"></a><a name="p66214864102658"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p61803802102658"><a name="p61803802102658"></a><a name="p61803802102658"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p40052093102658"><a name="p40052093102658"></a><a name="p40052093102658"></a>(Since API v2.8) Specifies the level of visibility for the shared file system. If this parameter is set to <strong id="b152423717216"><a name="b152423717216"></a><a name="b152423717216"></a>true</strong>, the share can be queried by other tenants using interfaces such as the one in <a href="querying-details-about-a-shared-file-system.md">Querying Details About a Shared File System</a>. If this parameter is set to <strong id="b62441776217"><a name="b62441776217"></a><a name="b62441776217"></a>false</strong>, the share is visible only to the tenant who creates it. The default value is <strong id="b1424477202111"><a name="b1424477202111"></a><a name="b1424477202111"></a>false</strong>.</p>
    <div class="note" id="note484733973710"><a name="note484733973710"></a><a name="note484733973710"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p414515407435"><a name="p414515407435"></a><a name="p414515407435"></a>Share access rules added by different tenants are isolated from each other. Therefore, even if a share is set to be visible to other tenants, the share can only be queried by other tenants using the interface in <a href="querying-details-about-a-shared-file-system.md">Querying Details About a Shared File System</a>. Other tenants are not allowed to mount or use the share.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row20192649102728"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p7310326102735"><a name="p7310326102735"></a><a name="p7310326102735"></a>consistency-group</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p55265554102735"><a name="p55265554102735"></a><a name="p55265554102735"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p47324923102735"><a name="p47324923102735"></a><a name="p47324923102735"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p8113560102735"><a name="p8113560102735"></a><a name="p8113560102735"></a>(Since API v2.4) Specifies the UUID of the consistency group in which the shared file system will be created. The share type of <strong id="b52549123210041"><a name="b52549123210041"></a><a name="b52549123210041"></a>share_network_id</strong> of the consistency group must be consistent with <strong id="b114047218910041"><a name="b114047218910041"></a><a name="b114047218910041"></a>share_type</strong>. SFS does not support the consistency group. Therefore, this parameter is reserved and you do not need to fill in this parameter.</p>
    </td>
    </tr>
    </tbody>
    </table>

    -   Description of field  **metadata**  \(when creating a share with the encryption function\)

        When creating a share with the encryption function, obtain the key ID, domain ID, and key alias of the encryption key using the HTTPS request by referring to section  **Querying the List of CMKs**  in the  _Key Management Service API Reference_. Then, in the  **metadata**  field, set the key-value pairs according to the following table. Ensure that the key-value pairs in the  **metadata**  field are correct.

        <a name="table122834414587"></a>
        <table><thead align="left"><tr id="row11279184155814"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p827915418584"><a name="p827915418584"></a><a name="p827915418584"></a><strong id="b842352706201325"><a name="b842352706201325"></a><a name="b842352706201325"></a>Key</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="12%" id="mcps1.1.5.1.2"><p id="p1027924165811"><a name="p1027924165811"></a><a name="p1027924165811"></a><strong id="b842352706201318"><a name="b842352706201318"></a><a name="b842352706201318"></a>Value Type</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="12%" id="mcps1.1.5.1.3"><p id="p20279144135815"><a name="p20279144135815"></a><a name="p20279144135815"></a><strong id="b1976135172815"><a name="b1976135172815"></a><a name="b1976135172815"></a>Mandatory</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="51%" id="mcps1.1.5.1.4"><p id="p11279949583"><a name="p11279949583"></a><a name="p11279949583"></a><strong id="b842352706155531_1"><a name="b842352706155531_1"></a><a name="b842352706155531_1"></a>Description</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row162815413589"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p17280741589"><a name="p17280741589"></a><a name="p17280741589"></a>#sfs_crypt_key_id</p>
        </td>
        <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p22808415585"><a name="p22808415585"></a><a name="p22808415585"></a>string</p>
        </td>
        <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.3 "><p id="p72809410588"><a name="p72809410588"></a><a name="p72809410588"></a>Yes</p>
        </td>
        <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p1428012465811"><a name="p1428012465811"></a><a name="p1428012465811"></a>Specifies the encryption key ID.</p>
        <p id="p1528094155814"><a name="p1528094155814"></a><a name="p1528094155814"></a>If this string, as well as <strong id="b842352706102249"><a name="b842352706102249"></a><a name="b842352706102249"></a>#sfs_crypt_domain_id</strong> and <strong id="b842352706102259"><a name="b842352706102259"></a><a name="b842352706102259"></a>#sfs_crypt_alias</strong> exist at the same time, the data encryption function is enabled. </p>
        </td>
        </tr>
        <tr id="row1282134135811"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p92811944582"><a name="p92811944582"></a><a name="p92811944582"></a>#sfs_crypt_domain_id</p>
        </td>
        <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p228116416581"><a name="p228116416581"></a><a name="p228116416581"></a>string</p>
        </td>
        <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.3 "><p id="p728154195817"><a name="p728154195817"></a><a name="p728154195817"></a>Yes</p>
        </td>
        <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p42811646587"><a name="p42811646587"></a><a name="p42811646587"></a>Specifies the tenant domain ID.</p>
        <p id="p122813417588"><a name="p122813417588"></a><a name="p122813417588"></a>If this string, as well as <strong id="b842352706102249_1"><a name="b842352706102249_1"></a><a name="b842352706102249_1"></a>#sfs_crypt_key_id</strong> and <strong id="b842352706102259_1"><a name="b842352706102259_1"></a><a name="b842352706102259_1"></a>#sfs_crypt_alias</strong> exist at the same time, the data encryption function is enabled. </p>
        </td>
        </tr>
        <tr id="row112837445819"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p1728284145811"><a name="p1728284145811"></a><a name="p1728284145811"></a>#sfs_crypt_alias</p>
        </td>
        <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p02821841582"><a name="p02821841582"></a><a name="p02821841582"></a>string</p>
        </td>
        <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.3 "><p id="p02824415586"><a name="p02824415586"></a><a name="p02824415586"></a>Yes</p>
        </td>
        <td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.5.1.4 "><p id="p1628217410583"><a name="p1628217410583"></a><a name="p1628217410583"></a>Specifies the encryption key alias in metadata. </p>
        <p id="p152821741585"><a name="p152821741585"></a><a name="p152821741585"></a>If this string, as well as <strong id="b842352706102249_2"><a name="b842352706102249_2"></a><a name="b842352706102249_2"></a>#sfs_crypt_key_id</strong> and <strong id="b842352706102259_2"><a name="b842352706102259_2"></a><a name="b842352706102259_2"></a>#sfs_crypt_domain_id</strong> exist at the same time, the data encryption function is enabled. </p>
        </td>
        </tr>
        </tbody>
        </table>

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >-   You are advised to use the default primary key  **sfs/default**  to create an encrypted share. For details, see section "File System Encryption" and "Managing Encrypted File Systems" in the  _Scalable File Service User Guide_.  


-   Example command

    ```
     manila create NFS 10 --name sharename
    ```


-   Example command \(creating a share with data encryption\)

    ```
     manila create NFS 10 --name sharename --metadata "#sfs_crypt_key_id"=9130c90d-73b8-4203-b790-d49f98d503df "#sfs_crypt_domain_id"=3b2d9670690444c582942801ed7d457b "#sfs_crypt_alias"=sfs/default
    ```


## Response<a name="section59946297153528"></a>

-   Parameter description

    <a name="table49714460153528"></a>
    <table><thead align="left"><tr id="row45175191153528"><th class="cellrowborder" valign="top" width="14.29%" id="mcps1.1.5.1.1"><p id="p35311894153528"><a name="p35311894153528"></a><a name="p35311894153528"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.310000000000002%" id="mcps1.1.5.1.2"><p id="p41691198153528"><a name="p41691198153528"></a><a name="p41691198153528"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.39%" id="mcps1.1.5.1.3"><p id="p21543862153528"><a name="p21543862153528"></a><a name="p21543862153528"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.01%" id="mcps1.1.5.1.4"><p id="p222374153528"><a name="p222374153528"></a><a name="p222374153528"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18012343153528"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p66727941102949"><a name="p66727941102949"></a><a name="p66727941102949"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p36254165102949"><a name="p36254165102949"></a><a name="p36254165102949"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p50906270102949"><a name="p50906270102949"></a><a name="p50906270102949"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p29767175102949"><a name="p29767175102949"></a><a name="p29767175102949"></a>Specifies the status of the shared file system. This interface is an asynchronous interface. The available value of <strong id="b18456289320"><a name="b18456289320"></a><a name="b18456289320"></a>status</strong> is only <strong id="b7606736203214"><a name="b7606736203214"></a><a name="b7606736203214"></a>creating</strong>.</p>
    </td>
    </tr>
    <tr id="row5234311153528"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p19926244103020"><a name="p19926244103020"></a><a name="p19926244103020"></a>share_type_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p3413076103020"><a name="p3413076103020"></a><a name="p3413076103020"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p8023720103020"><a name="p8023720103020"></a><a name="p8023720103020"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p45941577103020"><a name="p45941577103020"></a><a name="p45941577103020"></a>Specifies the name of a share type. A share type is used to specify the type of the storage service to be allocated. Currently, only one share type is provided for SFS and the value is fixed to <strong id="b37631845164114"><a name="b37631845164114"></a><a name="b37631845164114"></a>default</strong>.</p>
    </td>
    </tr>
    <tr id="row24388892153528"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p64361452103047"><a name="p64361452103047"></a><a name="p64361452103047"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p45895162103047"><a name="p45895162103047"></a><a name="p45895162103047"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p26520652103047"><a name="p26520652103047"></a><a name="p26520652103047"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p689227103047"><a name="p689227103047"></a><a name="p689227103047"></a>Describes the shared file system.</p>
    </td>
    </tr>
    <tr id="row21753137153528"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p978648710314"><a name="p978648710314"></a><a name="p978648710314"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p5450800210314"><a name="p5450800210314"></a><a name="p5450800210314"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p5307205410314"><a name="p5307205410314"></a><a name="p5307205410314"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p386908110314"><a name="p386908110314"></a><a name="p386908110314"></a>Specifies the availability zone.</p>
    </td>
    </tr>
    <tr id="row16286629153528"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p3981153103130"><a name="p3981153103130"></a><a name="p3981153103130"></a>share_network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p54037967103130"><a name="p54037967103130"></a><a name="p54037967103130"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p14999210103130"><a name="p14999210103130"></a><a name="p14999210103130"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p6976473103130"><a name="p6976473103130"></a><a name="p6976473103130"></a>Specifies the UUID of the share network. This parameter is reserved, because share network management is not supported currently.</p>
    </td>
    </tr>
    <tr id="row45827491153528"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p8039998103144"><a name="p8039998103144"></a><a name="p8039998103144"></a>host</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p47260081103144"><a name="p47260081103144"></a><a name="p47260081103144"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p2861324103144"><a name="p2861324103144"></a><a name="p2861324103144"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p30440696103144"><a name="p30440696103144"></a><a name="p30440696103144"></a>Specifies the host name of the shared file system.</p>
    </td>
    </tr>
    <tr id="row44760283153528"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p13713010103232"><a name="p13713010103232"></a><a name="p13713010103232"></a>access_rules_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p37012063103232"><a name="p37012063103232"></a><a name="p37012063103232"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p45187116103232"><a name="p45187116103232"></a><a name="p45187116103232"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p36277761103232"><a name="p36277761103232"></a><a name="p36277761103232"></a>Specifies the configuration status of the access rule. Possible values are <strong id="b55325600410330"><a name="b55325600410330"></a><a name="b55325600410330"></a>active </strong>(effective), <strong id="b126933326610330"><a name="b126933326610330"></a><a name="b126933326610330"></a>error</strong> (configuration failed), <strong id="b82882759010330"><a name="b82882759010330"></a><a name="b82882759010330"></a>syncing</strong> (configuration in progress).</p>
    </td>
    </tr>
    <tr id="row23817669153528"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p52988576103251"><a name="p52988576103251"></a><a name="p52988576103251"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p64216252103251"><a name="p64216252103251"></a><a name="p64216252103251"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p34133884103251"><a name="p34133884103251"></a><a name="p34133884103251"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p13381192103251"><a name="p13381192103251"></a><a name="p13381192103251"></a>Specifies the UUID of the source snapshot that was used to create the shared file system. This parameter is reserved, because snapshots are not supported currently.</p>
    </td>
    </tr>
    <tr id="row18572806103258"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p657379103410"><a name="p657379103410"></a><a name="p657379103410"></a>is_public</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p53247705103410"><a name="p53247705103410"></a><a name="p53247705103410"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p18096848103410"><a name="p18096848103410"></a><a name="p18096848103410"></a>bool</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p18985333144714"><a name="p18985333144714"></a><a name="p18985333144714"></a>(Since API v2.8) Specifies the level of visibility for the shared file system. If this parameter is set to <strong id="b17334514114113"><a name="b17334514114113"></a><a name="b17334514114113"></a>true</strong>, the share can be queried by other tenants using interfaces such as the one in <a href="querying-details-about-a-shared-file-system.md">Querying Details About a Shared File System</a>. If this parameter is set to <strong id="b2337131420418"><a name="b2337131420418"></a><a name="b2337131420418"></a>false</strong>, the share is visible only to the tenant who creates it. The default value is <strong id="b11337111404118"><a name="b11337111404118"></a><a name="b11337111404118"></a>false</strong>.</p>
    <div class="note" id="note1499273364716"><a name="note1499273364716"></a><a name="note1499273364716"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p4997113314472"><a name="p4997113314472"></a><a name="p4997113314472"></a>Share access rules added for different tenants are isolated from each other. Therefore, even if a share is set to be visible to other tenants, the share can only be queried by other tenants using the interface in <a href="querying-details-about-a-shared-file-system.md">Querying Details About a Shared File System</a>. Other tenants are not allowed to mount or use the share.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row3383371410332"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p48718966103433"><a name="p48718966103433"></a><a name="p48718966103433"></a>task_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p53922183103433"><a name="p53922183103433"></a><a name="p53922183103433"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p5620704103433"><a name="p5620704103433"></a><a name="p5620704103433"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p52623914103433"><a name="p52623914103433"></a><a name="p52623914103433"></a>Specifies the data migration status. This parameter is reserved, because data migration is not supported currently.</p>
    </td>
    </tr>
    <tr id="row40934719103449"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p64129108103455"><a name="p64129108103455"></a><a name="p64129108103455"></a>snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p27075279103455"><a name="p27075279103455"></a><a name="p27075279103455"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p45614003103455"><a name="p45614003103455"></a><a name="p45614003103455"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p3746726103455"><a name="p3746726103455"></a><a name="p3746726103455"></a>Specifies whether snapshots are supported. This parameter is reserved, because snapshots are not supported currently.</p>
    </td>
    </tr>
    <tr id="row6284470710352"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p18755660103543"><a name="p18755660103543"></a><a name="p18755660103543"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p42813491103543"><a name="p42813491103543"></a><a name="p42813491103543"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p45340738103543"><a name="p45340738103543"></a><a name="p45340738103543"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p48721186103543"><a name="p48721186103543"></a><a name="p48721186103543"></a>Specifies the UUID of the shared file system.</p>
    </td>
    </tr>
    <tr id="row14860576103510"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p38894945103556"><a name="p38894945103556"></a><a name="p38894945103556"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p63482844103556"><a name="p63482844103556"></a><a name="p63482844103556"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p41836715103556"><a name="p41836715103556"></a><a name="p41836715103556"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p33330743103556"><a name="p33330743103556"></a><a name="p33330743103556"></a>Specifies the size of the shared file system in GB.</p>
    </td>
    </tr>
    <tr id="row464556110367"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p38414037103737"><a name="p38414037103737"></a><a name="p38414037103737"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p24529316103737"><a name="p24529316103737"></a><a name="p24529316103737"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p40717575103737"><a name="p40717575103737"></a><a name="p40717575103737"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p9789287103737"><a name="p9789287103737"></a><a name="p9789287103737"></a>Specifies the name of the shared file system.</p>
    </td>
    </tr>
    <tr id="row41178551103610"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p46135584103825"><a name="p46135584103825"></a><a name="p46135584103825"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p45994806103825"><a name="p45994806103825"></a><a name="p45994806103825"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p34591842103825"><a name="p34591842103825"></a><a name="p34591842103825"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p50475785103825"><a name="p50475785103825"></a><a name="p50475785103825"></a>Specifies the UUID of the share type.</p>
    </td>
    </tr>
    <tr id="row53392877103615"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p8961529103849"><a name="p8961529103849"></a><a name="p8961529103849"></a>has_replicas</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p54795248103849"><a name="p54795248103849"></a><a name="p54795248103849"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p9230095103849"><a name="p9230095103849"></a><a name="p9230095103849"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p9440255103849"><a name="p9440255103849"></a><a name="p9440255103849"></a>Specifies whether replicas exist. This parameter is reserved, because replication is not supported currently.</p>
    </td>
    </tr>
    <tr id="row6027005103624"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p10717140103930"><a name="p10717140103930"></a><a name="p10717140103930"></a>replication_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p62782040103930"><a name="p62782040103930"></a><a name="p62782040103930"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p52180480103930"><a name="p52180480103930"></a><a name="p52180480103930"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p65869365103930"><a name="p65869365103930"></a><a name="p65869365103930"></a>Specifies the replication type. This parameter is reserved, because replication is not supported currently.</p>
    </td>
    </tr>
    <tr id="row35287353103628"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p25420908103946"><a name="p25420908103946"></a><a name="p25420908103946"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p45827685103946"><a name="p45827685103946"></a><a name="p45827685103946"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p21054974103946"><a name="p21054974103946"></a><a name="p21054974103946"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p27731295103946"><a name="p27731295103946"></a><a name="p27731295103946"></a>Specifies the date and time stamp when the shared file system was created.</p>
    </td>
    </tr>
    <tr id="row6561462103631"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p24957897103959"><a name="p24957897103959"></a><a name="p24957897103959"></a>share_proto</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p8323759103959"><a name="p8323759103959"></a><a name="p8323759103959"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p3135915103959"><a name="p3135915103959"></a><a name="p3135915103959"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p52682530103959"><a name="p52682530103959"></a><a name="p52682530103959"></a>Specifies the protocol for sharing file systems.</p>
    </td>
    </tr>
    <tr id="row36420811103634"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p46438954104016"><a name="p46438954104016"></a><a name="p46438954104016"></a>consistency_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p3458940104016"><a name="p3458940104016"></a><a name="p3458940104016"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p11738747104016"><a name="p11738747104016"></a><a name="p11738747104016"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p11314446104016"><a name="p11314446104016"></a><a name="p11314446104016"></a>Specifies the UUID of the consistency group. This parameter is reserved, because consistency groups are not supported currently.</p>
    </td>
    </tr>
    <tr id="row12702687103713"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p10666632104031"><a name="p10666632104031"></a><a name="p10666632104031"></a>source_cgsnapshot_member_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p58690859104031"><a name="p58690859104031"></a><a name="p58690859104031"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p56339147104031"><a name="p56339147104031"></a><a name="p56339147104031"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p68175104031"><a name="p68175104031"></a><a name="p68175104031"></a>Specifies the UUID of the snapshot's source. This parameter is reserved, because consistency snapshot is not supported currently.</p>
    </td>
    </tr>
    <tr id="row60504676103718"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p58464796104046"><a name="p58464796104046"></a><a name="p58464796104046"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p38027998104046"><a name="p38027998104046"></a><a name="p38027998104046"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p60369013104046"><a name="p60369013104046"></a><a name="p60369013104046"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p58051913104046"><a name="p58051913104046"></a><a name="p58051913104046"></a>Specifies the UUID of the project in which the shared file system was created.</p>
    </td>
    </tr>
    <tr id="row24001404104050"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p1947516510410"><a name="p1947516510410"></a><a name="p1947516510410"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p3398450910410"><a name="p3398450910410"></a><a name="p3398450910410"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p128185410410"><a name="p128185410410"></a><a name="p128185410410"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p3672135110410"><a name="p3672135110410"></a><a name="p3672135110410"></a>Sets that one or more metadata key and value pairs as a dictionary of strings.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

```
+-----------------------------+-------------------------------------+
| Property                    | Value                                |
+-----------------------------+-------------------------------------+
| status                      | creating                             |
| share_type_name             | default                              |
| description                 | None                                 |
| availability_zone           | None                                 |
| share_network_id            | None                                 |
| host                        |                                      |
| access_rules_status         | active                               |
| snapshot_id                 | None                                 |
| is_public                   | False                                |
| task_state                  | None                                 |
| snapshot_support            | True                                 |
| id                          | b4e1665d-2a63-4056-855a-4902720a2a07 |
| size                        | 10                                   |
| name                        | None                                 |
| share_type                  | 500fcfac-357b-4f0f-beeb-240d09da4dab |
| has_replicas                | False                                |
| replication_type            | None                                 |
| created_at                  | 2017-12-27T02:14:38.983181           |
| share_proto                 | NFS                                  |
| consistency_group_id        | None                                 |
| source_cgsnapshot_member_id | None                                 |
| project_id                  | 703fdd5a62c84cbfb1385c212881f695     |
| metadata                    | {}                                   |
+-----------------------------+-------------------------------------+
```

