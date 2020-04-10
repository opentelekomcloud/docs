# Querying Details About a Shared File System<a name="EN-US_TOPIC_0090543955"></a>

## Function<a name="section15087702153533"></a>

This interface is used to query the details about a shared file system.

## Command<a name="section60190052153533"></a>

-   Usage

    ```
    manila show <share>
    ```

-   Parameter description

    <a name="table21782343153533"></a>
    <table><thead align="left"><tr id="row42563891153533"><th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.5.1.1"><p id="p25123141153533"><a name="p25123141153533"></a><a name="p25123141153533"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.1.5.1.2"><p id="p21708527153533"><a name="p21708527153533"></a><a name="p21708527153533"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.1.5.1.3"><p id="p13560282153533"><a name="p13560282153533"></a><a name="p13560282153533"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.494949494949495%" id="mcps1.1.5.1.4"><p id="p24641070153533"><a name="p24641070153533"></a><a name="p24641070153533"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49769617153533"><td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.1 "><p id="p4807214153533"><a name="p4807214153533"></a><a name="p4807214153533"></a>share</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.1.5.1.2 "><p id="p53840043153533"><a name="p53840043153533"></a><a name="p53840043153533"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.3 "><p id="p66076208153533"><a name="p66076208153533"></a><a name="p66076208153533"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.494949494949495%" headers="mcps1.1.5.1.4 "><p id="p732575417321"><a name="p732575417321"></a><a name="p732575417321"></a>Specifies name or id for the shared file system.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example command

    ```
    manila show 416112b6-e5c9-4a46-8dd1-80749fc09336
    ```


## Response<a name="section44541646153533"></a>

-   Parameter description

    <a name="table45749458153533"></a>
    <table><thead align="left"><tr id="row59475944153533"><th class="cellrowborder" valign="top" width="14.29%" id="mcps1.1.5.1.1"><p id="p52822192153533"><a name="p52822192153533"></a><a name="p52822192153533"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.310000000000002%" id="mcps1.1.5.1.2"><p id="p50739144153533"><a name="p50739144153533"></a><a name="p50739144153533"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.39%" id="mcps1.1.5.1.3"><p id="p16229976153533"><a name="p16229976153533"></a><a name="p16229976153533"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.01%" id="mcps1.1.5.1.4"><p id="p39559689153533"><a name="p39559689153533"></a><a name="p39559689153533"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row50218242153533"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p41145836153533"><a name="p41145836153533"></a><a name="p41145836153533"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p44478447153533"><a name="p44478447153533"></a><a name="p44478447153533"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p45984434153533"><a name="p45984434153533"></a><a name="p45984434153533"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p648016012410"><a name="p648016012410"></a><a name="p648016012410"></a>Specifies the status of the shared file system. Possible values are <strong id="en-us_topic_0064390792_b842352706102211"><a name="en-us_topic_0064390792_b842352706102211"></a><a name="en-us_topic_0064390792_b842352706102211"></a>creating</strong>, <strong id="en-us_topic_0064390792_b842352706102215"><a name="en-us_topic_0064390792_b842352706102215"></a><a name="en-us_topic_0064390792_b842352706102215"></a>error</strong>, <strong id="en-us_topic_0064390792_b842352706102219"><a name="en-us_topic_0064390792_b842352706102219"></a><a name="en-us_topic_0064390792_b842352706102219"></a>available</strong>, <strong id="en-us_topic_0064390792_b842352706102225"><a name="en-us_topic_0064390792_b842352706102225"></a><a name="en-us_topic_0064390792_b842352706102225"></a>deleting</strong>, <strong id="en-us_topic_0064390792_b842352706102229"><a name="en-us_topic_0064390792_b842352706102229"></a><a name="en-us_topic_0064390792_b842352706102229"></a>error_deleting</strong>, <strong id="en-us_topic_0064390792_b842352706102233"><a name="en-us_topic_0064390792_b842352706102233"></a><a name="en-us_topic_0064390792_b842352706102233"></a>manage_starting</strong>, <strong id="en-us_topic_0064390792_b842352706102237"><a name="en-us_topic_0064390792_b842352706102237"></a><a name="en-us_topic_0064390792_b842352706102237"></a>manage_error</strong>, <strong id="en-us_topic_0064390792_b842352706102241"><a name="en-us_topic_0064390792_b842352706102241"></a><a name="en-us_topic_0064390792_b842352706102241"></a>unmanage_starting</strong>, <strong id="en-us_topic_0064390792_b842352706102245"><a name="en-us_topic_0064390792_b842352706102245"></a><a name="en-us_topic_0064390792_b842352706102245"></a>unmanage_error</strong>, <strong id="en-us_topic_0064390792_b842352706102248"><a name="en-us_topic_0064390792_b842352706102248"></a><a name="en-us_topic_0064390792_b842352706102248"></a>unmanaged</strong>, <strong id="en-us_topic_0064390792_b842352706102251"><a name="en-us_topic_0064390792_b842352706102251"></a><a name="en-us_topic_0064390792_b842352706102251"></a>extending</strong>, <strong id="en-us_topic_0064390792_b842352706102258"><a name="en-us_topic_0064390792_b842352706102258"></a><a name="en-us_topic_0064390792_b842352706102258"></a>extending_error</strong>, <strong id="en-us_topic_0064390792_b84235270610231"><a name="en-us_topic_0064390792_b84235270610231"></a><a name="en-us_topic_0064390792_b84235270610231"></a>shrinking</strong>, <strong id="en-us_topic_0064390792_b84235270610235"><a name="en-us_topic_0064390792_b84235270610235"></a><a name="en-us_topic_0064390792_b84235270610235"></a>shrinking_error</strong>, and <strong id="en-us_topic_0064390792_b842352706102313"><a name="en-us_topic_0064390792_b842352706102313"></a><a name="en-us_topic_0064390792_b842352706102313"></a>shrinking_possible_data_loss_error</strong>.</p>
    </td>
    </tr>
    <tr id="row52404109153533"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p16874466153533"><a name="p16874466153533"></a><a name="p16874466153533"></a>share_type_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p24654528153533"><a name="p24654528153533"></a><a name="p24654528153533"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p50859726153533"><a name="p50859726153533"></a><a name="p50859726153533"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p3698144512423"><a name="p3698144512423"></a><a name="p3698144512423"></a>Specifies the name of a share type. A share type is used to specify the type of the storage service to be allocated. Currently, SFS provides only one share type and the value is fixed to <strong id="b44691142172316"><a name="b44691142172316"></a><a name="b44691142172316"></a>default</strong>.</p>
    </td>
    </tr>
    <tr id="row32647384153533"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p27192438153533"><a name="p27192438153533"></a><a name="p27192438153533"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p55103873153533"><a name="p55103873153533"></a><a name="p55103873153533"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p34228704153533"><a name="p34228704153533"></a><a name="p34228704153533"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p5833189812432"><a name="p5833189812432"></a><a name="p5833189812432"></a>Describes the shared file system.</p>
    </td>
    </tr>
    <tr id="row55336924153533"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p53105821153533"><a name="p53105821153533"></a><a name="p53105821153533"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p6604239153533"><a name="p6604239153533"></a><a name="p6604239153533"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p65181337153533"><a name="p65181337153533"></a><a name="p65181337153533"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p5060491612448"><a name="p5060491612448"></a><a name="p5060491612448"></a>Specifies the availability zone.</p>
    </td>
    </tr>
    <tr id="row4119497153533"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p65243864153533"><a name="p65243864153533"></a><a name="p65243864153533"></a>share_network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p50261627153533"><a name="p50261627153533"></a><a name="p50261627153533"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p44659995153533"><a name="p44659995153533"></a><a name="p44659995153533"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p268130012457"><a name="p268130012457"></a><a name="p268130012457"></a>Specifies the UUID of the share network. This parameter is reserved, because share network management is not supported currently.</p>
    </td>
    </tr>
    <tr id="row9337498153533"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p18139888153533"><a name="p18139888153533"></a><a name="p18139888153533"></a>export_locations</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p60044830153533"><a name="p60044830153533"></a><a name="p60044830153533"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p31793101153533"><a name="p31793101153533"></a><a name="p31793101153533"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p647388281257"><a name="p647388281257"></a><a name="p647388281257"></a>Lists the mount locations. Currently, only a single mount location is supported. This parameter exists only when <strong id="b7786415229221"><a name="b7786415229221"></a><a name="b7786415229221"></a>X-Openstack-Manila-Api-Version</strong> specified in the request header is smaller than <strong id="b1391123459221"><a name="b1391123459221"></a><a name="b1391123459221"></a>2.8</strong>.</p>
    </td>
    </tr>
    <tr id="row24613199153533"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p47512118153533"><a name="p47512118153533"></a><a name="p47512118153533"></a>host</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p23276378153533"><a name="p23276378153533"></a><a name="p23276378153533"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p6338466153533"><a name="p6338466153533"></a><a name="p6338466153533"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p5118509612515"><a name="p5118509612515"></a><a name="p5118509612515"></a>Specifies the host name of the shared file system.</p>
    </td>
    </tr>
    <tr id="row57339441153533"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p13983172153533"><a name="p13983172153533"></a><a name="p13983172153533"></a>access_rules_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p58895127153533"><a name="p58895127153533"></a><a name="p58895127153533"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p5775954153533"><a name="p5775954153533"></a><a name="p5775954153533"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p4014969512556"><a name="p4014969512556"></a><a name="p4014969512556"></a>Specifies the configuration status of the access rule. Possible values are <strong id="b154953287892224"><a name="b154953287892224"></a><a name="b154953287892224"></a>active</strong> (effective), <strong id="b203838660692224"><a name="b203838660692224"></a><a name="b203838660692224"></a>error</strong> (configuration failed), <strong id="b58339120392224"><a name="b58339120392224"></a><a name="b58339120392224"></a>syncing</strong> (configuration in progress).</p>
    </td>
    </tr>
    <tr id="row824811411582"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p6411747411582"><a name="p6411747411582"></a><a name="p6411747411582"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p521316931208"><a name="p521316931208"></a><a name="p521316931208"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p3639137211582"><a name="p3639137211582"></a><a name="p3639137211582"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p534524091269"><a name="p534524091269"></a><a name="p534524091269"></a>Specifies the UUID of the source snapshot that was used to create the shared file system. This parameter is reserved, because snapshots are not supported currently.</p>
    </td>
    </tr>
    <tr id="row4120505911585"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p4927544911585"><a name="p4927544911585"></a><a name="p4927544911585"></a>is_public</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p203874591208"><a name="p203874591208"></a><a name="p203874591208"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p3282619111585"><a name="p3282619111585"></a><a name="p3282619111585"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p1441219224485"><a name="p1441219224485"></a><a name="p1441219224485"></a>(Since API v2.8) Specifies the level of visibility for the shared file system. If this parameter is set to <strong id="b14617151914244"><a name="b14617151914244"></a><a name="b14617151914244"></a>true</strong>, the share can be queried by other tenants using interfaces such as the one in <a href="querying-details-about-a-shared-file-system.md">Querying Details About a Shared File System</a>. If this parameter is set to <strong id="b96190191247"><a name="b96190191247"></a><a name="b96190191247"></a>false</strong>, the share is visible only to the tenant who creates the share. The default value is <strong id="b1062061972415"><a name="b1062061972415"></a><a name="b1062061972415"></a>false</strong>.</p>
    <div class="note" id="note484733973710"><a name="note484733973710"></a><a name="note484733973710"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p414515407435"><a name="p414515407435"></a><a name="p414515407435"></a>Share access rules added for different tenants are isolated from each other. Therefore, even if a share is set to be visible to other tenants, the share can only be queried by other tenants using the interface in <a href="querying-details-about-a-shared-file-system.md">Querying Details About a Shared File System</a>. Other tenants are not allowed to mount or use the share.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row7037111587"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p570006011587"><a name="p570006011587"></a><a name="p570006011587"></a>task_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p313988051208"><a name="p313988051208"></a><a name="p313988051208"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p1845652711587"><a name="p1845652711587"></a><a name="p1845652711587"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p4855490512635"><a name="p4855490512635"></a><a name="p4855490512635"></a>Specifies the data migration status. This parameter is reserved, because data migration is not supported currently.</p>
    </td>
    </tr>
    <tr id="row22290542115820"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p60703506115820"><a name="p60703506115820"></a><a name="p60703506115820"></a>snapshot_support</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p56063021208"><a name="p56063021208"></a><a name="p56063021208"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p51707183115820"><a name="p51707183115820"></a><a name="p51707183115820"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p301648412653"><a name="p301648412653"></a><a name="p301648412653"></a>Specifies whether snapshots are supported. This parameter is reserved, because snapshots are not supported currently.</p>
    </td>
    </tr>
    <tr id="row5531873115824"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p45428548115824"><a name="p45428548115824"></a><a name="p45428548115824"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p604624331208"><a name="p604624331208"></a><a name="p604624331208"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p26239339115824"><a name="p26239339115824"></a><a name="p26239339115824"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p135127181271"><a name="p135127181271"></a><a name="p135127181271"></a>Specifies the UUID of the shared file system.</p>
    </td>
    </tr>
    <tr id="row57049889115839"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p57638326115839"><a name="p57638326115839"></a><a name="p57638326115839"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p536991131208"><a name="p536991131208"></a><a name="p536991131208"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p6613282115839"><a name="p6613282115839"></a><a name="p6613282115839"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p435221471277"><a name="p435221471277"></a><a name="p435221471277"></a>Specifies the size of the shared file system in GB.</p>
    </td>
    </tr>
    <tr id="row703278115843"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p56965587115843"><a name="p56965587115843"></a><a name="p56965587115843"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p221861221208"><a name="p221861221208"></a><a name="p221861221208"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p21957727115843"><a name="p21957727115843"></a><a name="p21957727115843"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p162088612720"><a name="p162088612720"></a><a name="p162088612720"></a>Specifies the name of the shared file system.</p>
    </td>
    </tr>
    <tr id="row51719644115853"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p28541625115853"><a name="p28541625115853"></a><a name="p28541625115853"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p4467491208"><a name="p4467491208"></a><a name="p4467491208"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p27872820115853"><a name="p27872820115853"></a><a name="p27872820115853"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p2123337712740"><a name="p2123337712740"></a><a name="p2123337712740"></a>Specifies the UUID of the share type. A share type is used to specify the type of the storage service to be allocated. Currently, SFS provides only one share type and the value is <strong id="b19150163972517"><a name="b19150163972517"></a><a name="b19150163972517"></a>default</strong>.</p>
    </td>
    </tr>
    <tr id="row22008987115856"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p37897527115856"><a name="p37897527115856"></a><a name="p37897527115856"></a>has_replicas</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p1303409112016"><a name="p1303409112016"></a><a name="p1303409112016"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p7336512115856"><a name="p7336512115856"></a><a name="p7336512115856"></a>boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p2278452012753"><a name="p2278452012753"></a><a name="p2278452012753"></a>Specifies whether replicas exist. This parameter is reserved, because replication is not supported currently.</p>
    </td>
    </tr>
    <tr id="row5634907111598"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p87207711598"><a name="p87207711598"></a><a name="p87207711598"></a>replication_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p3950290312016"><a name="p3950290312016"></a><a name="p3950290312016"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p1744787011598"><a name="p1744787011598"></a><a name="p1744787011598"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p1590880812759"><a name="p1590880812759"></a><a name="p1590880812759"></a>Specifies the replication type. This parameter is reserved, because replication is not supported currently.</p>
    </td>
    </tr>
    <tr id="row10424707115916"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p39094954115916"><a name="p39094954115916"></a><a name="p39094954115916"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p791414512016"><a name="p791414512016"></a><a name="p791414512016"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p11920534115916"><a name="p11920534115916"></a><a name="p11920534115916"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p607052261284"><a name="p607052261284"></a><a name="p607052261284"></a>Specifies the date and time stamp when the shared file system was created.</p>
    </td>
    </tr>
    <tr id="row5465239115920"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p40031246115920"><a name="p40031246115920"></a><a name="p40031246115920"></a>share_proto</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p6515826612016"><a name="p6515826612016"></a><a name="p6515826612016"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p48020391115920"><a name="p48020391115920"></a><a name="p48020391115920"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p3268948712815"><a name="p3268948712815"></a><a name="p3268948712815"></a>Specifies the protocol for sharing file systems.</p>
    </td>
    </tr>
    <tr id="row7136937115929"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p41221023115929"><a name="p41221023115929"></a><a name="p41221023115929"></a>consistency_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p5440937412016"><a name="p5440937412016"></a><a name="p5440937412016"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p2410815115929"><a name="p2410815115929"></a><a name="p2410815115929"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p4099317212832"><a name="p4099317212832"></a><a name="p4099317212832"></a>Specifies the UUID of the consistency group. This parameter is reserved, because consistency groups are not supported currently.</p>
    </td>
    </tr>
    <tr id="row22425047115941"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p4489557115941"><a name="p4489557115941"></a><a name="p4489557115941"></a>source_cgsnapshot_member_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p309572912016"><a name="p309572912016"></a><a name="p309572912016"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p62305158115941"><a name="p62305158115941"></a><a name="p62305158115941"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p3105552012838"><a name="p3105552012838"></a><a name="p3105552012838"></a>Specifies the UUID of the snapshot's source. This parameter is reserved, because consistency snapshot is not supported currently.</p>
    </td>
    </tr>
    <tr id="row55850579115948"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p27603011115948"><a name="p27603011115948"></a><a name="p27603011115948"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p4219439712016"><a name="p4219439712016"></a><a name="p4219439712016"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p43641136115948"><a name="p43641136115948"></a><a name="p43641136115948"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p45271166115948"><a name="p45271166115948"></a><a name="p45271166115948"></a>Tenant ID</p>
    </td>
    </tr>
    <tr id="row41887581115954"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.5.1.1 "><p id="p37450887115954"><a name="p37450887115954"></a><a name="p37450887115954"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.310000000000002%" headers="mcps1.1.5.1.2 "><p id="p13623026115954"><a name="p13623026115954"></a><a name="p13623026115954"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p29723334115954"><a name="p29723334115954"></a><a name="p29723334115954"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.01%" headers="mcps1.1.5.1.4 "><p id="p58779817115954"><a name="p58779817115954"></a><a name="p58779817115954"></a>Sets that one or more metadata key and value pairs as a dictionary of strings.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    # manila show 416112b6-e5c9-4a46-8dd1-80749fc09336
    +-----------------------------+-------------------------------------------------------------------------------+
    | Property                    | Value                                                                         |
    +-----------------------------+-------------------------------------------------------------------------------+
    | status                      | available                                                                     |
    | share_type_name             | default                                                                       |
    | description                 | None                                                                          |
    | availability_zone           | az-01                                                                      |
    | share_network_id            | None                                                                          |
    | export_locations            |                                                                               |
    |                             | path = sfs-nas1.eu-de.otc.t-systems.com:/share-cff11cb8                       |
    |                             | id = 6014f802-7b74-4fb2-8436-a58c94f86e84                                     |
    |                             | preferred = False                                                             |
    | host                        | DJ1@28281404-884d-4eda-8240-c54903a178fe#28281404-884d-4eda-8240-c54903a178fe |
    | access_rules_status         | active                                                                        |
    | snapshot_id                 | None                                                                          |
    | is_public                   | False                                                                         |
    | task_state                  | None                                                                          |
    | snapshot_support            | True                                                                          |
    | id                          | 416112b6-e5c9-4a46-8dd1-80749fc09336                                          |
    | size                        | 1                                                                             |
    | name                        | sample1                                                                      |
    | share_type                  | 500fcfac-357b-4f0f-beeb-240d09da4dab                                          |
    | has_replicas                | False                                                                         |
    | replication_type            | None                                                                          |
    | created_at                  | 2017-10-24T13:27:55.936861                                                    |
    | share_proto                 | NFS                                                                           |
    | consistency_group_id        | None                                                                          |
    | source_cgsnapshot_member_id | None                                                                          |
    | project_id                  | 703fdd5a62c84cbfb1385c212881f695                                              |
    | metadata                    | {u'share_used': u'0'}                                                         |
    +-----------------------------+-------------------------------------
    ```


