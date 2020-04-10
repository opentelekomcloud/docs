# Creating a Shared File System<a name="sfs_02_0021"></a>

## Function<a name="sc880cc1b32be442c93ddc31872c5bba9"></a>

This API is used to create a shared file system. After the file system is created, you need to mount the file system to ECSs to achieve shared file storage. 

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This API is an asynchronous API. If the returned status code is  **200**, the API request is successfully delivered and received. Later, you can query the status and path of the shared file system by referring to  [Querying Details About a Shared File System](querying-details-about-a-shared-file-system.md)  to identify whether the creation is complete and successful. If the status of the shared file system becomes  **available**  or the shared path is generated, the creation is successful.  

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>After a shared file system is created successfully, it can be used only after you add share access rules by referring to  [Adding Share Access Rules](adding-share-access-rules.md).  

## URI<a name="s40540b8c32644992ba338ed32c274e1a"></a>

-   POST /v2/\{project\_id\}/shares
-   Parameter description

    <a name="t5f48f75db9b14c6cbfd2879dd1e7c8d1"></a>
    <table><thead align="left"><tr id="ree8732a49c9f4cbfa3cbd26bda2eb442"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.1.5.1.1"><p id="p17124101410431"><a name="p17124101410431"></a><a name="p17124101410431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.1.5.1.2"><p id="p1612415146430"><a name="p1612415146430"></a><a name="p1612415146430"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.1.5.1.3"><p id="p312416148432"><a name="p312416148432"></a><a name="p312416148432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.45454545454546%" id="mcps1.1.5.1.4"><p id="p3124181464318"><a name="p3124181464318"></a><a name="p3124181464318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r7dc74f4a31004f8eb4e868a93369c8a0"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.1.5.1.1 "><p id="adf798e5d942b4301b652796bdf092f4a"><a name="adf798e5d942b4301b652796bdf092f4a"></a><a name="adf798e5d942b4301b652796bdf092f4a"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="a2326f73739854b4fa1892e0648821849"><a name="a2326f73739854b4fa1892e0648821849"></a><a name="a2326f73739854b4fa1892e0648821849"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.5.1.3 "><p id="ac77b318c2668498189dbee0fbb5fdb09"><a name="ac77b318c2668498189dbee0fbb5fdb09"></a><a name="ac77b318c2668498189dbee0fbb5fdb09"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.1.5.1.4 "><p id="a7f191d8fed27458ba04d994b7c934b80"><a name="a7f191d8fed27458ba04d994b7c934b80"></a><a name="a7f191d8fed27458ba04d994b7c934b80"></a>Specifies the project ID of the operator.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s836831b048ae41e7abcc3643f6328971"></a>

-   Parameter description

    <a name="ta99ed8550b4848b7a80ce4606bf642dd"></a>
    <table><thead align="left"><tr id="r9b1296e4f59e4b979ed7edb46aee4ecd"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.1.5.1.1"><p id="p1757642617507"><a name="p1757642617507"></a><a name="p1757642617507"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.1.5.1.2"><p id="p18576122611507"><a name="p18576122611507"></a><a name="p18576122611507"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.1.5.1.3"><p id="p4591132645017"><a name="p4591132645017"></a><a name="p4591132645017"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.45454545454546%" id="mcps1.1.5.1.4"><p id="p25911826205017"><a name="p25911826205017"></a><a name="p25911826205017"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r668380448fc647729cea4b2954700bdb"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.1.5.1.1 "><p id="aecfc60cecb4e440e9e804b3b199fd629"><a name="aecfc60cecb4e440e9e804b3b199fd629"></a><a name="aecfc60cecb4e440e9e804b3b199fd629"></a>share</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.1.5.1.2 "><p id="a829cdcbedaf7466a9884bb541705ba82"><a name="a829cdcbedaf7466a9884bb541705ba82"></a><a name="a829cdcbedaf7466a9884bb541705ba82"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.1.5.1.3 "><p id="a3f0a2ab9ce5743ae9074158b34089cb4"><a name="a3f0a2ab9ce5743ae9074158b34089cb4"></a><a name="a3f0a2ab9ce5743ae9074158b34089cb4"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.1.5.1.4 "><p id="a89908adb44af4223b6805e3cc99a5f43"><a name="a89908adb44af4223b6805e3cc99a5f43"></a><a name="a89908adb44af4223b6805e3cc99a5f43"></a>For details, see the description of the <strong id="b162591515345"><a name="b162591515345"></a><a name="b162591515345"></a>share</strong> field.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of the  **share**  field

    <a name="t02fa2a8d319442e18936e45a4b0868e9"></a>
    <table><thead align="left"><tr id="r0d59edb1d3b84778ac0d399ba307cea3"><th class="cellrowborder" valign="top" width="24%" id="mcps1.1.5.1.1"><p id="p89501128115014"><a name="p89501128115014"></a><a name="p89501128115014"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.1.5.1.2"><p id="p15950132815504"><a name="p15950132815504"></a><a name="p15950132815504"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="12%" id="mcps1.1.5.1.3"><p id="p12966112865014"><a name="p12966112865014"></a><a name="p12966112865014"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.1.5.1.4"><p id="p4966172895016"><a name="p4966172895016"></a><a name="p4966172895016"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r51c142ecbaf2461ba473dee4939fca92"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.1 "><p id="abf39f6a279534cb4b823a51069c9102e"><a name="abf39f6a279534cb4b823a51069c9102e"></a><a name="abf39f6a279534cb4b823a51069c9102e"></a>share_proto</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.2 "><p id="acedc2a0b65b64463b4ceecbe0a4c8fff"><a name="acedc2a0b65b64463b4ceecbe0a4c8fff"></a><a name="acedc2a0b65b64463b4ceecbe0a4c8fff"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.3 "><p id="ae54b1ae095b34db0a389cf59563b381e"><a name="ae54b1ae095b34db0a389cf59563b381e"></a><a name="ae54b1ae095b34db0a389cf59563b381e"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0064390791_p918786017377"><a name="en-us_topic_0064390791_p918786017377"></a><a name="en-us_topic_0064390791_p918786017377"></a>Specifies the file system sharing protocol. The valid value can be NFS (for Linux OS) or CIFS (for Windows OS).</p>
    </td>
    </tr>
    <tr id="rb6f27e5a457a4ff485aff112009f5f5e"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.1 "><p id="ad8bd9fbb693544b29bbc443f93e486b3"><a name="ad8bd9fbb693544b29bbc443f93e486b3"></a><a name="ad8bd9fbb693544b29bbc443f93e486b3"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.2 "><p id="a8faf576e9d954661b4a168718934ec62"><a name="a8faf576e9d954661b4a168718934ec62"></a><a name="a8faf576e9d954661b4a168718934ec62"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.3 "><p id="a06029c2e26cd42debd4becdce81ac1fc"><a name="a06029c2e26cd42debd4becdce81ac1fc"></a><a name="a06029c2e26cd42debd4becdce81ac1fc"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="a484024b86d384cb7a43cda72ba89c0d2"><a name="a484024b86d384cb7a43cda72ba89c0d2"></a><a name="a484024b86d384cb7a43cda72ba89c0d2"></a>Specifies the size (GB) of the shared file system. The applied capacity of the shared file system cannot be larger than the allowed quota. To view the allowed quota, see <a href="quota-management.md">Quota Management</a>.</p>
    </td>
    </tr>
    <tr id="re3d7e94336ce48e080a0203246c79233"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0064390791_p556864917377"><a name="en-us_topic_0064390791_p556864917377"></a><a name="en-us_topic_0064390791_p556864917377"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.2 "><p id="a51808a58ff4943d8821a6aa2cd50815e"><a name="a51808a58ff4943d8821a6aa2cd50815e"></a><a name="a51808a58ff4943d8821a6aa2cd50815e"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.3 "><p id="a6ec135df9996496b890874cabc7c0069"><a name="a6ec135df9996496b890874cabc7c0069"></a><a name="a6ec135df9996496b890874cabc7c0069"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="a6e5bd9ce802544a0a1b5db1cc36d16aa"><a name="a6e5bd9ce802544a0a1b5db1cc36d16aa"></a><a name="a6e5bd9ce802544a0a1b5db1cc36d16aa"></a>Specifies the name of the shared file system, which contains 0 to 255 characters and can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="r3215dc216ecd4baba1c22f7b8c977ccb"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.1 "><p id="ab0014e64ec834c0ca04949c9b99fff6f"><a name="ab0014e64ec834c0ca04949c9b99fff6f"></a><a name="ab0014e64ec834c0ca04949c9b99fff6f"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.2 "><p id="a842ca980f7724dddb00c6f833105a645"><a name="a842ca980f7724dddb00c6f833105a645"></a><a name="a842ca980f7724dddb00c6f833105a645"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.3 "><p id="abbaf9735800440888dba5a42f3f7377f"><a name="abbaf9735800440888dba5a42f3f7377f"></a><a name="abbaf9735800440888dba5a42f3f7377f"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="ae51bbc680dea4e4b8b8d254a1b75d6e5"><a name="ae51bbc680dea4e4b8b8d254a1b75d6e5"></a><a name="ae51bbc680dea4e4b8b8d254a1b75d6e5"></a>Specifies the description of the shared file system, which contains 0 to 255 characters and can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="r4b66af4ae7544e00a7c4dc5a7e984249"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.1 "><p id="ae1662c7d08d24a70a04c673d6674b843"><a name="ae1662c7d08d24a70a04c673d6674b843"></a><a name="ae1662c7d08d24a70a04c673d6674b843"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0064390791_p982989317377"><a name="en-us_topic_0064390791_p982989317377"></a><a name="en-us_topic_0064390791_p982989317377"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.3 "><p id="adf07feef971540c0aed0af3de0f22705"><a name="adf07feef971540c0aed0af3de0f22705"></a><a name="adf07feef971540c0aed0af3de0f22705"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0064390791_p231285917377"><a name="en-us_topic_0064390791_p231285917377"></a><a name="en-us_topic_0064390791_p231285917377"></a>Specifies the UUID (0 to 36 characters) of the source snapshot that is used to create the shared file system. This parameter is reserved, because snapshots are not supported currently.</p>
    </td>
    </tr>
    <tr id="r662719c5cfa34258af8e257b5c1ea960"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0064390791_p835319317377"><a name="en-us_topic_0064390791_p835319317377"></a><a name="en-us_topic_0064390791_p835319317377"></a>is_public</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0064390791_p552002117377"><a name="en-us_topic_0064390791_p552002117377"></a><a name="en-us_topic_0064390791_p552002117377"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.3 "><p id="a6715ff9ed50b4f0ca762bd5b4483d10e"><a name="a6715ff9ed50b4f0ca762bd5b4483d10e"></a><a name="a6715ff9ed50b4f0ca762bd5b4483d10e"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0064390791_p4518009717377"><a name="en-us_topic_0064390791_p4518009717377"></a><a name="en-us_topic_0064390791_p4518009717377"></a>(Supported by API versions from v2.8 to v2.42). Specifies whether a file system can be publicly seen. If it is set to <strong id="b1592338151712"><a name="b1592338151712"></a><a name="b1592338151712"></a>true</strong>, the file system can be seen publicly. If it is set to <strong id="b119317389173"><a name="b119317389173"></a><a name="b119317389173"></a>false</strong>, the file system can be seen privately. The default value is <strong id="b793103818172"><a name="b793103818172"></a><a name="b793103818172"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="rf853704a03034e04a82e69a45778e907"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.1 "><p id="af48a7a717e004099a3e7eb3534b2dcd1"><a name="af48a7a717e004099a3e7eb3534b2dcd1"></a><a name="af48a7a717e004099a3e7eb3534b2dcd1"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.2 "><p id="a1497b69599b846f992b9680c2047b21e"><a name="a1497b69599b846f992b9680c2047b21e"></a><a name="a1497b69599b846f992b9680c2047b21e"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.3 "><p id="aa22557fd59b44a82a602bb17d3fba92a"><a name="aa22557fd59b44a82a602bb17d3fba92a"></a><a name="aa22557fd59b44a82a602bb17d3fba92a"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="a41d262e33af445198b732394c490f871"><a name="a41d262e33af445198b732394c490f871"></a><a name="a41d262e33af445198b732394c490f871"></a>Specifies the share type. This value determines the storage service type for the shared file system, such as high-performance storage (composed of SSDs) or large-capacity storage (composed of SATA disks). Currently, only one service type is supported and the parameter will be automatically set to the supported one. Do not manually set it, because application for the file service will fail if an unsupported type is entered.</p>
    </td>
    </tr>
    <tr id="rdb8427ac5c5040ceb6b039ce081b2b89"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0064390791_p56786017377"><a name="en-us_topic_0064390791_p56786017377"></a><a name="en-us_topic_0064390791_p56786017377"></a>share_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.2 "><p id="ae04759b7b185454c9ba7ce1393a013e7"><a name="ae04759b7b185454c9ba7ce1393a013e7"></a><a name="ae04759b7b185454c9ba7ce1393a013e7"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.3 "><p id="ae9dc7fcdada64780a79e944a2981c927"><a name="ae9dc7fcdada64780a79e944a2981c927"></a><a name="ae9dc7fcdada64780a79e944a2981c927"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="aa4d58b85debc41369c45a510ff4a2ba3"><a name="aa4d58b85debc41369c45a510ff4a2ba3"></a><a name="aa4d58b85debc41369c45a510ff4a2ba3"></a>(Supported by API versions from v2.31 to v2.42.) Specifies the UUID of the consistency group to which the share is to be created. SFS does not support a consistency group. Therefore, this field is invalid, and this parameter is not needed.</p>
    </td>
    </tr>
    <tr id="r96d56af1208f43ff95b9c166f495547f"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.1 "><p id="a41a8c875b39a4f42873c25d2b14ceb27"><a name="a41a8c875b39a4f42873c25d2b14ceb27"></a><a name="a41a8c875b39a4f42873c25d2b14ceb27"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0064390791_p940226217377"><a name="en-us_topic_0064390791_p940226217377"></a><a name="en-us_topic_0064390791_p940226217377"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.3 "><p id="adc11f31cab9b4ca29fa3a79485facc63"><a name="adc11f31cab9b4ca29fa3a79485facc63"></a><a name="adc11f31cab9b4ca29fa3a79485facc63"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="a601cd5bbc0b84d549010518ab3700f17"><a name="a601cd5bbc0b84d549010518ab3700f17"></a><a name="a601cd5bbc0b84d549010518ab3700f17"></a>Specifies the availability zone name. If this parameter is left blank, the default availability zone will be used. If the default availability zone contains no storage resources, the creation of the shared file system fails. The value contains 0 to 255 characters.</p>
    </td>
    </tr>
    <tr id="r37b1498aaaf14640a550c276ef015453"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.1 "><p id="a4b3268db7b854aeeae9ab4b4245c97e7"><a name="a4b3268db7b854aeeae9ab4b4245c97e7"></a><a name="a4b3268db7b854aeeae9ab4b4245c97e7"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0064390791_p992060317377"><a name="en-us_topic_0064390791_p992060317377"></a><a name="en-us_topic_0064390791_p992060317377"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.3 "><p id="a36009adc6677473f8fb24aadb966d861"><a name="a36009adc6677473f8fb24aadb966d861"></a><a name="a36009adc6677473f8fb24aadb966d861"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="a3d762128ac7f40ddbf20b115af03dafe"><a name="a3d762128ac7f40ddbf20b115af03dafe"></a><a name="a3d762128ac7f40ddbf20b115af03dafe"></a>Specifies the metadata information used to create the shared file system. The value consists of one or more key and value pairs organized as a dictionary of strings. For details, see the description of the <strong id="b38181233465"><a name="b38181233465"></a><a name="b38181233465"></a>metadata</strong> field.</p>
    <div class="caution" id="note92849475810"><a name="note92849475810"></a><a name="note92849475810"></a><span class="cautiontitle"> CAUTION: </span><div class="cautionbody"><a name="ul67781628350"></a><a name="ul67781628350"></a><ul id="ul67781628350"><li>For security concerns, the API for modifying the <strong id="b842352706204348"><a name="b842352706204348"></a><a name="b842352706204348"></a>metadata</strong> field is not opened yet. Therefore, ensure that the parameters and values are correct when creating a shared file system with data encryption using the <strong id="b842352706204358"><a name="b842352706204358"></a><a name="b842352706204358"></a>metadata</strong> field.</li><li>Unless otherwise specified (for example, <strong id="b842352706203556"><a name="b842352706203556"></a><a name="b842352706203556"></a>#sfs_crypt_key_id</strong>), the keys that comply with the following rules in the <strong id="b84235270620449"><a name="b84235270620449"></a><a name="b84235270620449"></a>metadata</strong> field are for internal use of the system. Do not customize the settings to avoid internal system errors caused by conflicts with system predefined keys.<a name="ul54791373516"></a><a name="ul54791373516"></a><ul id="ul54791373516"><li>Key <strong id="b842352706105824"><a name="b842352706105824"></a><a name="b842352706105824"></a>share_used</strong></li><li>Keys that start with <strong id="b842352706105911"><a name="b842352706105911"></a><a name="b842352706105911"></a>#sfs</strong></li></ul>
    </li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="r8eccdae91fe34e3ab5ee354d5a31148e"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.1 "><p id="a99046cd671d241f780d619131e94cfc3"><a name="a99046cd671d241f780d619131e94cfc3"></a><a name="a99046cd671d241f780d619131e94cfc3"></a>share_network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0064390791_p214793017377"><a name="en-us_topic_0064390791_p214793017377"></a><a name="en-us_topic_0064390791_p214793017377"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.3 "><p id="a112af38fb1884ba5a95789317ea1dea4"><a name="a112af38fb1884ba5a95789317ea1dea4"></a><a name="a112af38fb1884ba5a95789317ea1dea4"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="a854f4fa06ee54b609ae8d4726a14c656"><a name="a854f4fa06ee54b609ae8d4726a14c656"></a><a name="a854f4fa06ee54b609ae8d4726a14c656"></a>Specifies the UUID (0 to 36 characters) of the share network to which the share service belongs or will be created. This parameter is reserved, because share network management is not supported currently.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of  **metadata**  fields \(creating a shared file system with the encryption function\)

    When creating a shared file system with the encryption function, obtain the key ID, domain ID, and key alias of the encryption key using the HTTPS request by referring to section  **Querying the List of CMKs**  in the  _Key Management Service API Reference_. Then, in the  **metadata**  field, set the key-value pairs according to the following table. Ensure that the key-value pairs in the  **metadata**  field are correct.

    <a name="table122834414587"></a>
    <table><thead align="left"><tr id="row11279184155814"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p827915418584"><a name="p827915418584"></a><a name="p827915418584"></a><strong id="b842352706201325"><a name="b842352706201325"></a><a name="b842352706201325"></a>key</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12%" id="mcps1.1.5.1.2"><p id="p1027924165811"><a name="p1027924165811"></a><a name="p1027924165811"></a><strong id="b842352706201318"><a name="b842352706201318"></a><a name="b842352706201318"></a>Value Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.1.5.1.3"><p id="p20279144135815"><a name="p20279144135815"></a><a name="p20279144135815"></a><strong id="b84235270615219"><a name="b84235270615219"></a><a name="b84235270615219"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.1.5.1.4"><p id="p11279949583"><a name="p11279949583"></a><a name="p11279949583"></a><strong id="b84235270615228"><a name="b84235270615228"></a><a name="b84235270615228"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row162815413589"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p17280741589"><a name="p17280741589"></a><a name="p17280741589"></a>#sfs_crypt_key_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p22808415585"><a name="p22808415585"></a><a name="p22808415585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p72809410588"><a name="p72809410588"></a><a name="p72809410588"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p1428012465811"><a name="p1428012465811"></a><a name="p1428012465811"></a>Specifies the encryption key ID.</p>
    <p id="p1528094155814"><a name="p1528094155814"></a><a name="p1528094155814"></a>If this field, <strong id="b842352706102249"><a name="b842352706102249"></a><a name="b842352706102249"></a>#sfs_crypt_domain_id</strong>, and <strong id="b842352706102259"><a name="b842352706102259"></a><a name="b842352706102259"></a>#sfs_crypt_alias</strong> exist at the same time, the data encryption function is enabled.</p>
    </td>
    </tr>
    <tr id="row1282134135811"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p92811944582"><a name="p92811944582"></a><a name="p92811944582"></a>#sfs_crypt_domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p228116416581"><a name="p228116416581"></a><a name="p228116416581"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p728154195817"><a name="p728154195817"></a><a name="p728154195817"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p42811646587"><a name="p42811646587"></a><a name="p42811646587"></a>Specifies the tenant domain ID.</p>
    <p id="p122813417588"><a name="p122813417588"></a><a name="p122813417588"></a>If this field, <strong id="b338852589"><a name="b338852589"></a><a name="b338852589"></a>#sfs_crypt_key_id</strong>, and <strong id="b2068393553"><a name="b2068393553"></a><a name="b2068393553"></a>#sfs_crypt_alias</strong> exist at the same time, the data encryption function is enabled.</p>
    </td>
    </tr>
    <tr id="row112837445819"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p1728284145811"><a name="p1728284145811"></a><a name="p1728284145811"></a>#sfs_crypt_alias</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p02821841582"><a name="p02821841582"></a><a name="p02821841582"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.3 "><p id="p02824415586"><a name="p02824415586"></a><a name="p02824415586"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p1628217410583"><a name="p1628217410583"></a><a name="p1628217410583"></a>Specifies the encryption key alias.</p>
    <p id="p152821741585"><a name="p152821741585"></a><a name="p152821741585"></a>If this field, <strong id="b626918840"><a name="b626918840"></a><a name="b626918840"></a>#sfs_crypt_key_id</strong>, and <strong id="b867974003"><a name="b867974003"></a><a name="b867974003"></a>#sfs_crypt_domain_id</strong> exist at the same time, the data encryption function is enabled.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   You are advised to use the default primary key  **sfs/default**  to create an encrypted shared file system. For details, see section "File System Encryption" and "Encryption" in the  _Scalable File Service User Guide_.  


-   Example request: POST https://\{endpoint\}/v2/16e1ab15c35a457e9c2b2aa189f544e1/shares

    ```
    {
       "share": {
           "share_type": null,
           "name": "test",
           "snapshot_id": null,
           "description": "test description",
           "metadata": {
               "key1": "value1",
               "key2": "value2"
           },
           "share_proto": "NFS",
           "share_network_id": null,
           "size": 1,
           "is_public": false
       }
    }
    ```


-   Example request \(creating a shared file system with data encryption function\): POST https://\{endpoint\}/v2/16e1ab15c35a457e9c2b2aa189f544e1/shares

    ```
    {
       "share": {
           "share_type": null,
           "name": "test",
           "snapshot_id": null,
           "description": "test description",
           "metadata": {
               "#sfs_crypt_key_id": "9130c90d-73b8-4203-b790-d49f98d503df",
               "#sfs_crypt_domain_id": "3b2d9670690444c582942801ed7d457b",
               "#sfs_crypt_alias": "sfs/default"
           },
           "share_proto": "NFS",
           "share_network_id": null,
           "size": 1,
           "is_public": false
       }
    }
    ```


## Response<a name="s1487e0d77aa44726b32e39e9b52b242b"></a>

-   Parameter description

    <a name="tda30386a6e9d4540a4eb716742253a1b"></a>
    <table><thead align="left"><tr id="r8ada73019fa5407c8e16f6e1f7bc4bb1"><th class="cellrowborder" valign="top" width="16.93830616938306%" id="mcps1.1.4.1.1"><p id="p88858351506"><a name="p88858351506"></a><a name="p88858351506"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.507649235076496%" id="mcps1.1.4.1.2"><p id="p1688543515018"><a name="p1688543515018"></a><a name="p1688543515018"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.55404459554045%" id="mcps1.1.4.1.3"><p id="p18851135175014"><a name="p18851135175014"></a><a name="p18851135175014"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r1a20df0633434edc9d860eaf14b9a981"><td class="cellrowborder" valign="top" width="16.93830616938306%" headers="mcps1.1.4.1.1 "><p id="a7a0494ee07fe4977b3a761e9700c2259"><a name="a7a0494ee07fe4977b3a761e9700c2259"></a><a name="a7a0494ee07fe4977b3a761e9700c2259"></a>share</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.507649235076496%" headers="mcps1.1.4.1.2 "><p id="aab44f3064cf049479255909280c43ccf"><a name="aab44f3064cf049479255909280c43ccf"></a><a name="aab44f3064cf049479255909280c43ccf"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.55404459554045%" headers="mcps1.1.4.1.3 "><p id="afa73e2f572e845479878686baa515ac2"><a name="afa73e2f572e845479878686baa515ac2"></a><a name="afa73e2f572e845479878686baa515ac2"></a>For details, see the description of the <strong id="b869211819562"><a name="b869211819562"></a><a name="b869211819562"></a>share</strong> field.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description of the  **share**  field

    <a name="en-us_topic_0064390794_table28597308"></a>
    <table><thead align="left"><tr id="en-us_topic_0064390794_row26120409"><th class="cellrowborder" valign="top" width="18.84%" id="mcps1.1.4.1.1"><p id="p1873317135612"><a name="p1873317135612"></a><a name="p1873317135612"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.91%" id="mcps1.1.4.1.2"><p id="p473111755617"><a name="p473111755617"></a><a name="p473111755617"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.25%" id="mcps1.1.4.1.3"><p id="p0732017135611"><a name="p0732017135611"></a><a name="p0732017135611"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0064390794_row46308405"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p28090732115456"><a name="en-us_topic_0064390794_p28090732115456"></a><a name="en-us_topic_0064390794_p28090732115456"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p60756818115456"><a name="en-us_topic_0064390794_p60756818115456"></a><a name="en-us_topic_0064390794_p60756818115456"></a>array</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p53809467171857"><a name="en-us_topic_0064390794_p53809467171857"></a><a name="en-us_topic_0064390794_p53809467171857"></a>Specifies the links of shared file systems.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row32071293"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p20630446115456"><a name="en-us_topic_0064390794_p20630446115456"></a><a name="en-us_topic_0064390794_p20630446115456"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p60453459115456"><a name="en-us_topic_0064390794_p60453459115456"></a><a name="en-us_topic_0064390794_p60453459115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p35525415171857"><a name="en-us_topic_0064390794_p35525415171857"></a><a name="en-us_topic_0064390794_p35525415171857"></a>Specifies the availability zone.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row5492535895012"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1976898095012"><a name="en-us_topic_0064390794_p1976898095012"></a><a name="en-us_topic_0064390794_p1976898095012"></a>share_server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p4995572295012"><a name="en-us_topic_0064390794_p4995572295012"></a><a name="en-us_topic_0064390794_p4995572295012"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p1988170695012"><a name="en-us_topic_0064390794_p1988170695012"></a><a name="en-us_topic_0064390794_p1988170695012"></a>Specifies the UUID for managing share services.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row51382007"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p27750209115456"><a name="en-us_topic_0064390794_p27750209115456"></a><a name="en-us_topic_0064390794_p27750209115456"></a>share_network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p33174447115456"><a name="en-us_topic_0064390794_p33174447115456"></a><a name="en-us_topic_0064390794_p33174447115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p59674002171857"><a name="en-us_topic_0064390794_p59674002171857"></a><a name="en-us_topic_0064390794_p59674002171857"></a>Specifies the UUID of the share network. This parameter is reserved, because share network management is not supported currently.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row39279891115440"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p39186779115456"><a name="en-us_topic_0064390794_p39186779115456"></a><a name="en-us_topic_0064390794_p39186779115456"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p20012545115456"><a name="en-us_topic_0064390794_p20012545115456"></a><a name="en-us_topic_0064390794_p20012545115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p17092907171857"><a name="en-us_topic_0064390794_p17092907171857"></a><a name="en-us_topic_0064390794_p17092907171857"></a>Specifies the UUID of the source snapshot that is used to create the shared file system. This parameter is reserved, because snapshots are not supported currently.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row5321904710035"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1577556910035"><a name="en-us_topic_0064390794_p1577556910035"></a><a name="en-us_topic_0064390794_p1577556910035"></a>snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p2164239410035"><a name="en-us_topic_0064390794_p2164239410035"></a><a name="en-us_topic_0064390794_p2164239410035"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p820346510035"><a name="en-us_topic_0064390794_p820346510035"></a><a name="en-us_topic_0064390794_p820346510035"></a>Specifies whether snapshots are supported. This parameter is reserved, because snapshots are not supported currently. This field is supported by API v2.2 and later versions.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row66254026115429"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p66240344115456"><a name="en-us_topic_0064390794_p66240344115456"></a><a name="en-us_topic_0064390794_p66240344115456"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p63867663115456"><a name="en-us_topic_0064390794_p63867663115456"></a><a name="en-us_topic_0064390794_p63867663115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p45589478171857"><a name="en-us_topic_0064390794_p45589478171857"></a><a name="en-us_topic_0064390794_p45589478171857"></a>Specifies the UUID of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row25775244115437"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p57485250115456"><a name="en-us_topic_0064390794_p57485250115456"></a><a name="en-us_topic_0064390794_p57485250115456"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p25793701115456"><a name="en-us_topic_0064390794_p25793701115456"></a><a name="en-us_topic_0064390794_p25793701115456"></a>integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p42544068172855"><a name="en-us_topic_0064390794_p42544068172855"></a><a name="en-us_topic_0064390794_p42544068172855"></a>Specifies the size (GB) of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row2811743793851"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p602036689397"><a name="en-us_topic_0064390794_p602036689397"></a><a name="en-us_topic_0064390794_p602036689397"></a>share_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p606046069397"><a name="en-us_topic_0064390794_p606046069397"></a><a name="en-us_topic_0064390794_p606046069397"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p100260429397"><a name="en-us_topic_0064390794_p100260429397"></a><a name="en-us_topic_0064390794_p100260429397"></a>Specifies the UUID of the consistency group. This parameter is reserved, because consistency groups are not supported currently. This field is supported by API versions from v2.31 to v2.42.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row14146850115432"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p43647722115456"><a name="en-us_topic_0064390794_p43647722115456"></a><a name="en-us_topic_0064390794_p43647722115456"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p45804593115456"><a name="en-us_topic_0064390794_p45804593115456"></a><a name="en-us_topic_0064390794_p45804593115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p36017679171857"><a name="en-us_topic_0064390794_p36017679171857"></a><a name="en-us_topic_0064390794_p36017679171857"></a>Specifies the UUID of the project to which the shared file system belongs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row27677209115427"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p30561506115456"><a name="en-us_topic_0064390794_p30561506115456"></a><a name="en-us_topic_0064390794_p30561506115456"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p59562882115456"><a name="en-us_topic_0064390794_p59562882115456"></a><a name="en-us_topic_0064390794_p59562882115456"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390792_p42083247173855"><a name="en-us_topic_0064390792_p42083247173855"></a><a name="en-us_topic_0064390792_p42083247173855"></a>Sets one or more metadata key and value pairs as a dictionary of strings. <strong id="b1139105052915"><a name="b1139105052915"></a><a name="b1139105052915"></a>share_used</strong> is the key, and the corresponding value is the used capacity of the shared file system in the unit of Bytes. </p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row21024096115415"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p23577146115456"><a name="en-us_topic_0064390794_p23577146115456"></a><a name="en-us_topic_0064390794_p23577146115456"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p30700686115456"><a name="en-us_topic_0064390794_p30700686115456"></a><a name="en-us_topic_0064390794_p30700686115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p9195044171857"><a name="en-us_topic_0064390794_p9195044171857"></a><a name="en-us_topic_0064390794_p9195044171857"></a>Specifies the status of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row665580195924"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p224903195924"><a name="en-us_topic_0064390794_p224903195924"></a><a name="en-us_topic_0064390794_p224903195924"></a>task_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p5905231595924"><a name="en-us_topic_0064390794_p5905231595924"></a><a name="en-us_topic_0064390794_p5905231595924"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p1850821095924"><a name="en-us_topic_0064390794_p1850821095924"></a><a name="en-us_topic_0064390794_p1850821095924"></a>Specifies the data migration status. This parameter is reserved, because data migration is not supported currently. This field is supported by API v2.5 and later versions.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row939599610316"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p2287823910316"><a name="en-us_topic_0064390794_p2287823910316"></a><a name="en-us_topic_0064390794_p2287823910316"></a>has_replicas</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p4870772510316"><a name="en-us_topic_0064390794_p4870772510316"></a><a name="en-us_topic_0064390794_p4870772510316"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p5301165710316"><a name="en-us_topic_0064390794_p5301165710316"></a><a name="en-us_topic_0064390794_p5301165710316"></a>Specifies whether replicas exist. This parameter is reserved, because replication is not supported currently. This field is supported by API versions from v2.11 to v2.42.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row48841735810"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1388510311817"><a name="en-us_topic_0064390794_p1388510311817"></a><a name="en-us_topic_0064390794_p1388510311817"></a>replication_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p088617317817"><a name="en-us_topic_0064390794_p088617317817"></a><a name="en-us_topic_0064390794_p088617317817"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p178861331480"><a name="en-us_topic_0064390794_p178861331480"></a><a name="en-us_topic_0064390794_p178861331480"></a>Specifies the replication type. This parameter is reserved, because replication is not supported currently. This field is supported by API versions from v2.11 to v2.42.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row38372338115421"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p61202789115456"><a name="en-us_topic_0064390794_p61202789115456"></a><a name="en-us_topic_0064390794_p61202789115456"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p58478870115456"><a name="en-us_topic_0064390794_p58478870115456"></a><a name="en-us_topic_0064390794_p58478870115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p59409689171857"><a name="en-us_topic_0064390794_p59409689171857"></a><a name="en-us_topic_0064390794_p59409689171857"></a>Describes the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row35274029115424"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p58169755115456"><a name="en-us_topic_0064390794_p58169755115456"></a><a name="en-us_topic_0064390794_p58169755115456"></a>host</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p14129699115456"><a name="en-us_topic_0064390794_p14129699115456"></a><a name="en-us_topic_0064390794_p14129699115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p24446366171857"><a name="en-us_topic_0064390794_p24446366171857"></a><a name="en-us_topic_0064390794_p24446366171857"></a>Specifies the name of the host. This field is visible only to the administrator.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row10855127115417"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p66003741115456"><a name="en-us_topic_0064390794_p66003741115456"></a><a name="en-us_topic_0064390794_p66003741115456"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p44702790115456"><a name="en-us_topic_0064390794_p44702790115456"></a><a name="en-us_topic_0064390794_p44702790115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p37552527171857"><a name="en-us_topic_0064390794_p37552527171857"></a><a name="en-us_topic_0064390794_p37552527171857"></a>Specifies the name of the shared file system.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row6259894411544"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p66214260115456"><a name="en-us_topic_0064390794_p66214260115456"></a><a name="en-us_topic_0064390794_p66214260115456"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p61754840115456"><a name="en-us_topic_0064390794_p61754840115456"></a><a name="en-us_topic_0064390794_p61754840115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p62484878171857"><a name="en-us_topic_0064390794_p62484878171857"></a><a name="en-us_topic_0064390794_p62484878171857"></a>Specifies the date and time stamp when the shared file system was created.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row2256685795641"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1597610695641"><a name="en-us_topic_0064390794_p1597610695641"></a><a name="en-us_topic_0064390794_p1597610695641"></a>access_rules_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p6230051595641"><a name="en-us_topic_0064390794_p6230051595641"></a><a name="en-us_topic_0064390794_p6230051595641"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p1317697095641"><a name="en-us_topic_0064390794_p1317697095641"></a><a name="en-us_topic_0064390794_p1317697095641"></a>Specifies the configuration status of the access rule. Possible values are <strong id="b907975238111834"><a name="b907975238111834"></a><a name="b907975238111834"></a>active</strong> (effective), <strong id="b1456498747111834"><a name="b1456498747111834"></a><a name="b1456498747111834"></a>error</strong> (configuration failed), and <strong id="b1045032779111834"><a name="b1045032779111834"></a><a name="b1045032779111834"></a>syncing</strong> (configuration in progress). This field is supported by API v2.10 and later versions.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row66328432115411"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p11825073115456"><a name="en-us_topic_0064390794_p11825073115456"></a><a name="en-us_topic_0064390794_p11825073115456"></a>share_proto</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p18306875115456"><a name="en-us_topic_0064390794_p18306875115456"></a><a name="en-us_topic_0064390794_p18306875115456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p51666373171857"><a name="en-us_topic_0064390794_p51666373171857"></a><a name="en-us_topic_0064390794_p51666373171857"></a>Specifies the protocol for sharing file systems.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row4389128911547"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p745300812118"><a name="en-us_topic_0064390794_p745300812118"></a><a name="en-us_topic_0064390794_p745300812118"></a>share_type_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p6682275212118"><a name="en-us_topic_0064390794_p6682275212118"></a><a name="en-us_topic_0064390794_p6682275212118"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p55872650172937"><a name="en-us_topic_0064390794_p55872650172937"></a><a name="en-us_topic_0064390794_p55872650172937"></a>Specifies the storage service type assigned for the shared file system, such as high-performance storage (composed of SSDs) and large-capacity storage (composed of SATA disks). This field is supported by API v2.6 and later versions.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row1997612012118"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p97495795244"><a name="en-us_topic_0064390794_p97495795244"></a><a name="en-us_topic_0064390794_p97495795244"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p2135204095244"><a name="en-us_topic_0064390794_p2135204095244"></a><a name="en-us_topic_0064390794_p2135204095244"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p5179364095244"><a name="en-us_topic_0064390794_p5179364095244"></a><a name="en-us_topic_0064390794_p5179364095244"></a>Specifies the UUID of the share type.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row6380688295244"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p945114017196"><a name="p945114017196"></a><a name="p945114017196"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="p54519014190"><a name="p54519014190"></a><a name="p54519014190"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="p114511106197"><a name="p114511106197"></a><a name="p114511106197"></a>Specifies the volume type. The definition of this parameter is the same as that of <strong id="b12198418181516"><a name="b12198418181516"></a><a name="b12198418181516"></a>share_type</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row1256499495932"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p157881131005"><a name="en-us_topic_0064390794_p157881131005"></a><a name="en-us_topic_0064390794_p157881131005"></a>export_locations</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p630797391005"><a name="en-us_topic_0064390794_p630797391005"></a><a name="en-us_topic_0064390794_p630797391005"></a>array</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p91852451005"><a name="en-us_topic_0064390794_p91852451005"></a><a name="en-us_topic_0064390794_p91852451005"></a>Lists the mount locations. Currently, only a single mount location is supported. This parameter exists only when <strong id="b1232113020245"><a name="b1232113020245"></a><a name="b1232113020245"></a>X-Openstack-Manila-Api-Version</strong> specified in the request header is smaller than <strong id="b1432230122419"><a name="b1432230122419"></a><a name="b1432230122419"></a>2.9</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row1105050495936"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p522666391005"><a name="en-us_topic_0064390794_p522666391005"></a><a name="en-us_topic_0064390794_p522666391005"></a>export_location</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p232762111005"><a name="en-us_topic_0064390794_p232762111005"></a><a name="en-us_topic_0064390794_p232762111005"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p63249321005"><a name="en-us_topic_0064390794_p63249321005"></a><a name="en-us_topic_0064390794_p63249321005"></a>Specifies the mount location. This parameter exists only when <strong id="b10567185315269"><a name="b10567185315269"></a><a name="b10567185315269"></a>X-Openstack-Manila-Api-Version</strong> specified in the request header is smaller than <strong id="b17568125322617"><a name="b17568125322617"></a><a name="b17568125322617"></a>2.9</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row760346112115"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p1190063912115"><a name="en-us_topic_0064390794_p1190063912115"></a><a name="en-us_topic_0064390794_p1190063912115"></a>is_public</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p2442773012115"><a name="en-us_topic_0064390794_p2442773012115"></a><a name="en-us_topic_0064390794_p2442773012115"></a>bool</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p19950543172949"><a name="en-us_topic_0064390794_p19950543172949"></a><a name="en-us_topic_0064390794_p19950543172949"></a>Specifies the visibility level of the shared file system. If it is set to <strong id="b1554011107273"><a name="b1554011107273"></a><a name="b1554011107273"></a>true</strong>, the file system can be seen publicly. If it is set to <strong id="b354114101275"><a name="b354114101275"></a><a name="b354114101275"></a>false</strong>, the file system can be seen privately. The default value is <strong id="b2542010112711"><a name="b2542010112711"></a><a name="b2542010112711"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0064390794_row138591369913"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0064390794_p285910611913"><a name="en-us_topic_0064390794_p285910611913"></a><a name="en-us_topic_0064390794_p285910611913"></a>source_share_group_snapshot_member_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0064390794_p1486018614919"><a name="en-us_topic_0064390794_p1486018614919"></a><a name="en-us_topic_0064390794_p1486018614919"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0064390794_p4860362096"><a name="en-us_topic_0064390794_p4860362096"></a><a name="en-us_topic_0064390794_p4860362096"></a>Specifies the UUID of the snapshot's source. This parameter is reserved, because consistency snapshots are not supported currently. This field is supported by API v2.31 and later versions.</p>
    </td>
    </tr>
    <tr id="row194415943614"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p154405943611"><a name="p154405943611"></a><a name="p154405943611"></a>revert_to_snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="p744185915361"><a name="p744185915361"></a><a name="p744185915361"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="p15445590367"><a name="p15445590367"></a><a name="p15445590367"></a>Specifies whether rollback from snapshot is supported. This parameter is reserved, because snapshots are not supported currently. This field is supported by API v2.27 and later versions.</p>
    </td>
    </tr>
    <tr id="row23739416379"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p2373749375"><a name="p2373749375"></a><a name="p2373749375"></a>create_share_from_snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="p183731148374"><a name="p183731148374"></a><a name="p183731148374"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="p437313415378"><a name="p437313415378"></a><a name="p437313415378"></a>Specifies whether creation of shared file systems from snapshot is supported. This parameter is reserved, because snapshots are not supported currently. This field is supported by API v2.24 and later versions.</p>
    </td>
    </tr>
    <tr id="row19420198183711"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p34207819375"><a name="p34207819375"></a><a name="p34207819375"></a>mount_snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="p1542014812379"><a name="p1542014812379"></a><a name="p1542014812379"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="p134208810373"><a name="p134208810373"></a><a name="p134208810373"></a>Specifies whether snapshot mount is supported. This parameter is reserved, because snapshots are not supported currently. This field is supported by API v2.32 and later versions.</p>
    </td>
    </tr>
    <tr id="row850218421401"><td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.1.4.1.1 "><p id="p1350254215401"><a name="p1350254215401"></a><a name="p1350254215401"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.91%" headers="mcps1.1.4.1.2 "><p id="p13502164284012"><a name="p13502164284012"></a><a name="p13502164284012"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.25%" headers="mcps1.1.4.1.3 "><p id="p205021542164013"><a name="p205021542164013"></a><a name="p205021542164013"></a>Specifies the user ID. This field is supported by API v2.16 and later versions.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "share": {
            "status": "creating",
            "project_id": "16e1ab15c35a457e9c2b2aa189f544e1",
            "name": "share_London",
            "share_type": "25747776-08e5-494f-ab40-a64b9d20d8f7",
            "availability_zone": "az1.dc1",
            "created_at": "2015-09-18T10:25:24.533287",
            "export_location": null,
            "links": [
                {
                    "href": "http://192.168.198.54:8786/v2/16e1ab15c35a457e9c2b2aa189f544e1/shares/011d21e2-fbc3-4e4a-9993-9ea223f73264",
                    "rel": "self"
                },
                {
                    "href": "http://192.168.198.54:8786/16e1ab15c35a457e9c2b2aa189f544e1/shares/011d21e2-fbc3-4e4a-9993-9ea223f73264",
                    "rel": "bookmark"
                }
            ],
            "share_network_id": null,
            "export_locations": [],
            "share_proto": "NFS",
            "host": null,
            "volume_type": "default",
            "snapshot_id": null,
            "is_public": true,
            "metadata": {
                "project": "my_app",
                "aim": "doc"
            },
            "id": "011d21e2-fbc3-4e4a-9993-9ea223f73264",
            "size": 1,
            "description": "My custom share London"
        }
    }
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >When the client receives the system response, the shared file system is still being created. For this reason, the shared path cannot be queried immediately. You can use the API of  [Querying Mount Locations of a Shared File System](querying-mount-locations-of-a-shared-file-system.md)  to query the shared path after the creation is complete.  


## Status Code<a name="sa5e037c233dc48e99754edb2a3e10718"></a>

-   Normal

    200

-   Abnormal

    <a name="t2090d44083d34718a5469023c0c64add"></a>
    <table><thead align="left"><tr id="ra369a8c86fba486db6b80296100f3699"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="aef56a0bee1724b0993bff1e74bd97796"><a name="aef56a0bee1724b0993bff1e74bd97796"></a><a name="aef56a0bee1724b0993bff1e74bd97796"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="a7923be73f3d642c48f49e12d9f575dbd"><a name="a7923be73f3d642c48f49e12d9f575dbd"></a><a name="a7923be73f3d642c48f49e12d9f575dbd"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r9caf832a2eb74734a12db37bb5922e9c"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390791_p887409917377"><a name="en-us_topic_0064390791_p887409917377"></a><a name="en-us_topic_0064390791_p887409917377"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="ac915b170d5f2455096491b02762241ac"><a name="ac915b170d5f2455096491b02762241ac"></a><a name="ac915b170d5f2455096491b02762241ac"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="r10cfd100de64484f99318a78375120ff"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a8193fd1ffce7479897c3de382c2eed15"><a name="a8193fd1ffce7479897c3de382c2eed15"></a><a name="a8193fd1ffce7479897c3de382c2eed15"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390791_p52210117377"><a name="en-us_topic_0064390791_p52210117377"></a><a name="en-us_topic_0064390791_p52210117377"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="r7a403b9870eb4da5b2a875a5b1539ffd"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="adbf7968a9dac42c49b53777be2aaf544"><a name="adbf7968a9dac42c49b53777be2aaf544"></a><a name="adbf7968a9dac42c49b53777be2aaf544"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a0bc87a6af4f1456e8086bde01aebec6b"><a name="a0bc87a6af4f1456e8086bde01aebec6b"></a><a name="a0bc87a6af4f1456e8086bde01aebec6b"></a>Access to the requested page is forbidden.</p>
    </td>
    </tr>
    <tr id="r3422b1bb54164104949a1a121c137932"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a26dbdb35ea5c4d08b5c6ea8b184b8656"><a name="a26dbdb35ea5c4d08b5c6ea8b184b8656"></a><a name="a26dbdb35ea5c4d08b5c6ea8b184b8656"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="acf1017be1cb84275bbbb87052f6ab21a"><a name="acf1017be1cb84275bbbb87052f6ab21a"></a><a name="acf1017be1cb84275bbbb87052f6ab21a"></a>The requested page was not found.</p>
    </td>
    </tr>
    <tr id="r98d495bd3a4f4d0b87572a4bd4173ce1"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a8c7636bd87f64006979cb1f8fdf6bbcc"><a name="a8c7636bd87f64006979cb1f8fdf6bbcc"></a><a name="a8c7636bd87f64006979cb1f8fdf6bbcc"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a969e484ebb1d4f95a1c5d8803eb5805b"><a name="a969e484ebb1d4f95a1c5d8803eb5805b"></a><a name="a969e484ebb1d4f95a1c5d8803eb5805b"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="rde52d6cce4fb49bda58bd438829c8b74"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0064390791_p781488717377"><a name="en-us_topic_0064390791_p781488717377"></a><a name="en-us_topic_0064390791_p781488717377"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="afa6f5ee4d9d5461ca179b522cbea0d34"><a name="afa6f5ee4d9d5461ca179b522cbea0d34"></a><a name="afa6f5ee4d9d5461ca179b522cbea0d34"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="r101c5bbfb8784aa883c87c38ef66d1ba"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a4d23d1ea32c3487e8fa03fa7a39543d8"><a name="a4d23d1ea32c3487e8fa03fa7a39543d8"></a><a name="a4d23d1ea32c3487e8fa03fa7a39543d8"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390791_p300388217377"><a name="en-us_topic_0064390791_p300388217377"></a><a name="en-us_topic_0064390791_p300388217377"></a>You must use the proxy server for authentication. Then the request can be processed.</p>
    </td>
    </tr>
    <tr id="r6206a8382c46402ab86f280e940f1756"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a0c0a0346efed4a158e3f78aad3f92502"><a name="a0c0a0346efed4a158e3f78aad3f92502"></a><a name="a0c0a0346efed4a158e3f78aad3f92502"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390791_p752846017377"><a name="en-us_topic_0064390791_p752846017377"></a><a name="en-us_topic_0064390791_p752846017377"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="r1f59abfea4d945d5853b088375ec075b"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a4de368473ace407db9497a6d22044206"><a name="a4de368473ace407db9497a6d22044206"></a><a name="a4de368473ace407db9497a6d22044206"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="a1e52611413ef42368e1fc74cedce0b14"><a name="a1e52611413ef42368e1fc74cedce0b14"></a><a name="a1e52611413ef42368e1fc74cedce0b14"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="r33f68eb575084d3d9c7a652797fa1d77"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a696b29b12cea423cbd6649f0ffd68db8"><a name="a696b29b12cea423cbd6649f0ffd68db8"></a><a name="a696b29b12cea423cbd6649f0ffd68db8"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="ad20c3d1dc2b146f0a4632048769e0e72"><a name="ad20c3d1dc2b146f0a4632048769e0e72"></a><a name="ad20c3d1dc2b146f0a4632048769e0e72"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="rc1e0e831ad8742b6b88bdfea358028be"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="af622f29f0130447f8615637fb7feb757"><a name="af622f29f0130447f8615637fb7feb757"></a><a name="af622f29f0130447f8615637fb7feb757"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="ac3e5fdea4e1d4f7c9d3668ee30ed96f7"><a name="ac3e5fdea4e1d4f7c9d3668ee30ed96f7"></a><a name="ac3e5fdea4e1d4f7c9d3668ee30ed96f7"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="r1ffb7ea16483434fbcdc681f373bb28d"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a636bca04b6c74339a4e3f28eaa7e32bc"><a name="a636bca04b6c74339a4e3f28eaa7e32bc"></a><a name="a636bca04b6c74339a4e3f28eaa7e32bc"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="af68a220ad6d3488cad0a0361f2f94967"><a name="af68a220ad6d3488cad0a0361f2f94967"></a><a name="af68a220ad6d3488cad0a0361f2f94967"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="r6658762006d1444084add1f582fae6bd"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a71922f19bd4b44a88fc41255846b5660"><a name="a71922f19bd4b44a88fc41255846b5660"></a><a name="a71922f19bd4b44a88fc41255846b5660"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0064390791_p361803117377"><a name="en-us_topic_0064390791_p361803117377"></a><a name="en-us_topic_0064390791_p361803117377"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="rec0c716ad62543e4ac5806fcb22b8c54"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="a612773caf040494fa785db348dd7e335"><a name="a612773caf040494fa785db348dd7e335"></a><a name="a612773caf040494fa785db348dd7e335"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="aa509f60996454e90b1521e61e3da4d9d"><a name="aa509f60996454e90b1521e61e3da4d9d"></a><a name="aa509f60996454e90b1521e61e3da4d9d"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


