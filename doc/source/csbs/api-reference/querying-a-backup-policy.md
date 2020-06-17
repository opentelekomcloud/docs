# Querying a Backup Policy<a name="EN-US_TOPIC_0059304226"></a>

## Function<a name="section64869004"></a>

This API is used to query the backup policy of a specific ID.

## URI<a name="section46950130"></a>

-   URI format

    GET https://\{endpoint\}/v1/\{project\_id\}/policies/\{policy\_id\}

-   Parameter description

    **Table  1**  Parameter description

    <a name="table34747181"></a>
    <table><thead align="left"><tr id="row59205190"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p45356064"><a name="p45356064"></a><a name="p45356064"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p49962569"><a name="p49962569"></a><a name="p49962569"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p20436323"><a name="p20436323"></a><a name="p20436323"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p44729494"><a name="p44729494"></a><a name="p44729494"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46597571"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p16306884"><a name="p16306884"></a><a name="p16306884"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p45789259"><a name="p45789259"></a><a name="p45789259"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p17942461"><a name="p17942461"></a><a name="p17942461"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row60934955"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p36784332"><a name="p36784332"></a><a name="p36784332"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p26740917"><a name="p26740917"></a><a name="p26740917"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p18530703"><a name="p18530703"></a><a name="p18530703"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p24592002"><a name="p24592002"></a><a name="p24592002"></a>Backup policy ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section19897990"></a>

-   Parameter description

None

-   Example request

    ```
    GET https://{endpoint}/v1/{project_id}/policies/{policy_id}
    ```


## Response<a name="section44864185"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table36024147"></a>
    <table><thead align="left"><tr id="row38832030"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p17731724315"><a name="p17731724315"></a><a name="p17731724315"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p4926171432"><a name="p4926171432"></a><a name="p4926171432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p2921017134314"><a name="p2921017134314"></a><a name="p2921017134314"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5848912"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p3999858"><a name="p3999858"></a><a name="p3999858"></a>policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p3504679"><a name="p3504679"></a><a name="p3504679"></a>policy_resp</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p15443595"><a name="p15443595"></a><a name="p15443595"></a>Query response</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **policy\_resp**

    **Table  3**  Parameter description of field  **policy\_resp**

    <a name="table42971646"></a>
    <table><thead align="left"><tr id="row19193659"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p1431162015431"><a name="p1431162015431"></a><a name="p1431162015431"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p1232792044318"><a name="p1232792044318"></a><a name="p1232792044318"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p3327102074313"><a name="p3327102074313"></a><a name="p3327102074313"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11457841"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p55669957"><a name="p55669957"></a><a name="p55669957"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p44153282"><a name="p44153282"></a><a name="p44153282"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p19646075"><a name="p19646075"></a><a name="p19646075"></a>Creation time, for example, <strong id="b576361416218"><a name="b576361416218"></a><a name="b576361416218"></a>2017-04-18T01:21:52.701973</strong></p>
    </td>
    </tr>
    <tr id="row42596951"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p27800986"><a name="p27800986"></a><a name="p27800986"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p377729"><a name="p377729"></a><a name="p377729"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p5382040916350"><a name="p5382040916350"></a><a name="p5382040916350"></a>Backup policy description</p>
    <p id="p30596085"><a name="p30596085"></a><a name="p30596085"></a>The value consists of 0 to 255 characters and must not contain a greater-than sign (&gt;) or less-than sign (&lt;).</p>
    </td>
    </tr>
    <tr id="row6929316"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p24403744"><a name="p24403744"></a><a name="p24403744"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p58329702"><a name="p58329702"></a><a name="p58329702"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p27085440"><a name="p27085440"></a><a name="p27085440"></a>Backup policy ID</p>
    </td>
    </tr>
    <tr id="row42442371"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p15280018"><a name="p15280018"></a><a name="p15280018"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p58669387"><a name="p58669387"></a><a name="p58669387"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p4186901716351"><a name="p4186901716351"></a><a name="p4186901716351"></a>Backup policy name</p>
    <p id="p54599876"><a name="p54599876"></a><a name="p54599876"></a>The value consists of 1 to 255 characters and can contain only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row21636836"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p7753264"><a name="p7753264"></a><a name="p7753264"></a>parameters</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p651535"><a name="p651535"></a><a name="p651535"></a>policy_param</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p52774385"><a name="p52774385"></a><a name="p52774385"></a>Parameters of a backup policy</p>
    </td>
    </tr>
    <tr id="row5207424"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p19148163"><a name="p19148163"></a><a name="p19148163"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p3310301"><a name="p3310301"></a><a name="p3310301"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p66807810"><a name="p66807810"></a><a name="p66807810"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row64399384"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p48967581"><a name="p48967581"></a><a name="p48967581"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p26168421"><a name="p26168421"></a><a name="p26168421"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p39267319"><a name="p39267319"></a><a name="p39267319"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b101718441745"><a name="b101718441745"></a><a name="b101718441745"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    <tr id="row17861557"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p37499989"><a name="p37499989"></a><a name="p37499989"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p16336415"><a name="p16336415"></a><a name="p16336415"></a>List&lt;resource&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p48181273"><a name="p48181273"></a><a name="p48181273"></a>Backup object list</p>
    </td>
    </tr>
    <tr id="row30978280"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p26212750"><a name="p26212750"></a><a name="p26212750"></a>scheduled_operations</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p48944014"><a name="p48944014"></a><a name="p48944014"></a>List&lt;scheduled_operation_resp&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p5042234"><a name="p5042234"></a><a name="p5042234"></a>Scheduling period list</p>
    </td>
    </tr>
    <tr id="row45380106"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p51909999"><a name="p51909999"></a><a name="p51909999"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p4023675"><a name="p4023675"></a><a name="p4023675"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p57482225"><a name="p57482225"></a><a name="p57482225"></a>Backup policy status</p>
    </td>
    </tr>
    <tr id="row697335312236"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p097325311231"><a name="p097325311231"></a><a name="p097325311231"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p11973353162317"><a name="p11973353162317"></a><a name="p11973353162317"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p16951038142"><a name="p16951038142"></a><a name="p16951038142"></a>Tag list</p>
    <p id="p0973053162317"><a name="p0973053162317"></a><a name="p0973053162317"></a>Keys in the tag list must be unique.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **policy\_param**

    **Table  4**  Parameter description of field  **policy\_param**

    <a name="table25548648"></a>
    <table><thead align="left"><tr id="row64122593"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p931182464312"><a name="p931182464312"></a><a name="p931182464312"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p13261124144316"><a name="p13261124144316"></a><a name="p13261124144316"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p1732682454313"><a name="p1732682454313"></a><a name="p1732682454313"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row27161214"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p52574749"><a name="p52574749"></a><a name="p52574749"></a>common</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p3370112"><a name="p3370112"></a><a name="p3370112"></a>common_param</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p4543636"><a name="p4543636"></a><a name="p4543636"></a>General backup policy parameters, which are blank by default</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource**

    **Table  5**  Parameter description of field  **resource**

    <a name="table32490229"></a>
    <table><thead align="left"><tr id="row57020674"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p1167132964314"><a name="p1167132964314"></a><a name="p1167132964314"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p068520296432"><a name="p068520296432"></a><a name="p068520296432"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p11685129104318"><a name="p11685129104318"></a><a name="p11685129104318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39696990"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p61339649"><a name="p61339649"></a><a name="p61339649"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p64690095"><a name="p64690095"></a><a name="p64690095"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p5406347"><a name="p5406347"></a><a name="p5406347"></a>ID of the object to be backed up</p>
    </td>
    </tr>
    <tr id="row48657127"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p48913182"><a name="p48913182"></a><a name="p48913182"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p4804387"><a name="p4804387"></a><a name="p4804387"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p2427141062110"><a name="p2427141062110"></a><a name="p2427141062110"></a>Entity object type of backup objects</p>
    <p id="p53611072"><a name="p53611072"></a><a name="p53611072"></a>The value is fixed at <strong id="b108016592298"><a name="b108016592298"></a><a name="b108016592298"></a>OS::Nova::Server</strong>, indicating that the object type is ECSs.</p>
    </td>
    </tr>
    <tr id="row12737606"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p25113165"><a name="p25113165"></a><a name="p25113165"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p15217020"><a name="p15217020"></a><a name="p15217020"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p24619125"><a name="p24619125"></a><a name="p24619125"></a>Backup object name</p>
    </td>
    </tr>
    <tr id="row39813284499"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p777318533616"><a name="p777318533616"></a><a name="p777318533616"></a>extra_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10773185103617"><a name="p10773185103617"></a><a name="p10773185103617"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1677325193612"><a name="p1677325193612"></a><a name="p1677325193612"></a>Additional information about the backup object</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **scheduled\_operation\_resp**

    **Table  6**  Parameter description of field  **scheduled\_operation\_resp**

    <a name="table47992078"></a>
    <table><thead align="left"><tr id="row27160073"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p121851442124320"><a name="p121851442124320"></a><a name="p121851442124320"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p132022042164312"><a name="p132022042164312"></a><a name="p132022042164312"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p13202204284313"><a name="p13202204284313"></a><a name="p13202204284313"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18334049"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p8662994"><a name="p8662994"></a><a name="p8662994"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p63805112"><a name="p63805112"></a><a name="p63805112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p42177151163518"><a name="p42177151163518"></a><a name="p42177151163518"></a>Scheduling period description</p>
    <p id="p831615"><a name="p831615"></a><a name="p831615"></a>The value consists of 0 to 255 characters and must not contain a greater-than sign (&gt;) or less-than sign (&lt;).</p>
    </td>
    </tr>
    <tr id="row7484535"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p2267583"><a name="p2267583"></a><a name="p2267583"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p46554464"><a name="p46554464"></a><a name="p46554464"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p530493163520"><a name="p530493163520"></a><a name="p530493163520"></a>Whether the scheduling period is enabled</p>
    <p id="p12815241"><a name="p12815241"></a><a name="p12815241"></a>The default value is <strong id="b1267155877163142"><a name="b1267155877163142"></a><a name="b1267155877163142"></a>true</strong>. If it is set to <strong id="b219270352163144"><a name="b219270352163144"></a><a name="b219270352163144"></a>false</strong>, automatic scheduling is disabled but manual scheduling is supported.</p>
    </td>
    </tr>
    <tr id="row48228313"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p14179266"><a name="p14179266"></a><a name="p14179266"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p17281810"><a name="p17281810"></a><a name="p17281810"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p60180051163527"><a name="p60180051163527"></a><a name="p60180051163527"></a>Scheduling period name</p>
    <p id="p57649352"><a name="p57649352"></a><a name="p57649352"></a>The value consists of 1 to 255 characters and can contain only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row49082128"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p16229428"><a name="p16229428"></a><a name="p16229428"></a>operation_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p46624455"><a name="p46624455"></a><a name="p46624455"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p18484485"><a name="p18484485"></a><a name="p18484485"></a>Operation type, which can be backup </p>
    <p id="p32142637"><a name="p32142637"></a><a name="p32142637"></a>Enumeration values: <strong id="b12576143115291"><a name="b12576143115291"></a><a name="b12576143115291"></a>backup</strong></p>
    </td>
    </tr>
    <tr id="row20848283"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p10989362"><a name="p10989362"></a><a name="p10989362"></a>operation_definition</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p26286721"><a name="p26286721"></a><a name="p26286721"></a>operation_definition</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p48849674"><a name="p48849674"></a><a name="p48849674"></a>Scheduling period parameters</p>
    </td>
    </tr>
    <tr id="row36993883"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p43714507"><a name="p43714507"></a><a name="p43714507"></a>trigger</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p54705592"><a name="p54705592"></a><a name="p54705592"></a>trigger_resp</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1968006"><a name="p1968006"></a><a name="p1968006"></a>Scheduling policy</p>
    </td>
    </tr>
    <tr id="row17712059"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p25390687"><a name="p25390687"></a><a name="p25390687"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p24097279"><a name="p24097279"></a><a name="p24097279"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p5722572"><a name="p5722572"></a><a name="p5722572"></a>Scheduling period ID</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **operation\_definition**

    **Table  7**  Parameter description of field  **operation\_definition**

    <a name="table23403672"></a>
    <table><thead align="left"><tr id="row43233365"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p13271646154318"><a name="p13271646154318"></a><a name="p13271646154318"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p43416461439"><a name="p43416461439"></a><a name="p43416461439"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p12341174612436"><a name="p12341174612436"></a><a name="p12341174612436"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61572465"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p21313750"><a name="p21313750"></a><a name="p21313750"></a>max_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p51754458"><a name="p51754458"></a><a name="p51754458"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1662615433283"><a name="p1662615433283"></a><a name="p1662615433283"></a>Maximum number of backups that can be automatically created for a backup object. The value can be <strong id="b01531347165319"><a name="b01531347165319"></a><a name="b01531347165319"></a>-1</strong> or ranges from <strong id="b6154947135315"><a name="b6154947135315"></a><a name="b6154947135315"></a>0</strong> to <strong id="b015414717531"><a name="b015414717531"></a><a name="b015414717531"></a>99999</strong>. If the value is set to <strong id="b29611748175313"><a name="b29611748175313"></a><a name="b29611748175313"></a>-1</strong>, the backups will not be cleared even though the configured retained backup quantity limit is exceeded.</p>
    </td>
    </tr>
    <tr id="row13819033"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p45599851"><a name="p45599851"></a><a name="p45599851"></a>retention_duration_days</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p9311222"><a name="p9311222"></a><a name="p9311222"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p762624392810"><a name="p762624392810"></a><a name="p762624392810"></a>Duration of retaining a backup, in days. The value can be <strong id="b16964175111530"><a name="b16964175111530"></a><a name="b16964175111530"></a>-1</strong> or ranges from <strong id="b2964185105311"><a name="b2964185105311"></a><a name="b2964185105311"></a>0</strong> to <strong id="b19965155115535"><a name="b19965155115535"></a><a name="b19965155115535"></a>99999</strong>. If the value is set to <strong id="b32891955195310"><a name="b32891955195310"></a><a name="b32891955195310"></a>-1</strong>, backups will not be cleared even though the configured retention duration is exceeded.</p>
    </td>
    </tr>
    <tr id="row9885939"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p62563629"><a name="p62563629"></a><a name="p62563629"></a>permanent</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p42163091"><a name="p42163091"></a><a name="p42163091"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p59767182"><a name="p59767182"></a><a name="p59767182"></a>Whether backups are permanently retained</p>
    </td>
    </tr>
    <tr id="row1112065753117"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p3120557143113"><a name="p3120557143113"></a><a name="p3120557143113"></a>plan_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p7121857103119"><a name="p7121857103119"></a><a name="p7121857103119"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p9121145713110"><a name="p9121145713110"></a><a name="p9121145713110"></a>Backup policy ID</p>
    </td>
    </tr>
    <tr id="row312210216335"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p1112282183319"><a name="p1112282183319"></a><a name="p1112282183319"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p212262133315"><a name="p212262133315"></a><a name="p212262133315"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p9122821334"><a name="p9122821334"></a><a name="p9122821334"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b121738341958"><a name="b121738341958"></a><a name="b121738341958"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **trigger\_resp**

    **Table  8**  Parameter description of field  **trigger\_resp**

    <a name="table9303578"></a>
    <table><thead align="left"><tr id="row47580858"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p1065465034319"><a name="p1065465034319"></a><a name="p1065465034319"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p867115054318"><a name="p867115054318"></a><a name="p867115054318"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p1671150104320"><a name="p1671150104320"></a><a name="p1671150104320"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54961897"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p22728661"><a name="p22728661"></a><a name="p22728661"></a>properties</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p6849025"><a name="p6849025"></a><a name="p6849025"></a>trigger_properties_resp</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p17900178"><a name="p17900178"></a><a name="p17900178"></a>Scheduler properties</p>
    </td>
    </tr>
    <tr id="row26883882"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p30110853"><a name="p30110853"></a><a name="p30110853"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p55923996"><a name="p55923996"></a><a name="p55923996"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p33549865"><a name="p33549865"></a><a name="p33549865"></a>Scheduler ID</p>
    </td>
    </tr>
    <tr id="row33513332"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p30225352"><a name="p30225352"></a><a name="p30225352"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1844030"><a name="p1844030"></a><a name="p1844030"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p15148719"><a name="p15148719"></a><a name="p15148719"></a>Scheduler name</p>
    </td>
    </tr>
    <tr id="row2120750"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p37563094"><a name="p37563094"></a><a name="p37563094"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p27713086"><a name="p27713086"></a><a name="p27713086"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p30167503"><a name="p30167503"></a><a name="p30167503"></a>Scheduling type</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field** trigger\_properties\_resp **

    **Table  9**  Parameter description of field  **trigger\_properties\_resp**

    <a name="table27648680"></a>
    <table><thead align="left"><tr id="row2508217"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p13655125294317"><a name="p13655125294317"></a><a name="p13655125294317"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p176711052194319"><a name="p176711052194319"></a><a name="p176711052194319"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p9671175218434"><a name="p9671175218434"></a><a name="p9671175218434"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35099287"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p24470004"><a name="p24470004"></a><a name="p24470004"></a>pattern</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p23298284"><a name="p23298284"></a><a name="p23298284"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p9649851163558"><a name="p9649851163558"></a><a name="p9649851163558"></a>Scheduling policy of the scheduler</p>
    <p id="p8112855"><a name="p8112855"></a><a name="p8112855"></a> The value consists of a maximum of 10,240 characters. The scheduling policy complies with iCalendar RFC 2445, but it supports only four parameters, which are <strong id="b158702517271"><a name="b158702517271"></a><a name="b158702517271"></a>FREQ</strong>, <strong id="b1870115118279"><a name="b1870115118279"></a><a name="b1870115118279"></a>BYDAY</strong>, <strong id="b1187011517278"><a name="b1187011517278"></a><a name="b1187011517278"></a>BYHOUR</strong>, and <strong id="b5870145116279"><a name="b5870145116279"></a><a name="b5870145116279"></a>BYMINUTE</strong>. <strong id="b1087019519274"><a name="b1087019519274"></a><a name="b1087019519274"></a>FREQ</strong> can be set to <strong id="b2870951112710"><a name="b2870951112710"></a><a name="b2870951112710"></a>WEEKLY</strong> and <strong id="b18870155112711"><a name="b18870155112711"></a><a name="b18870155112711"></a>DAILY</strong>, <strong id="b68701051182714"><a name="b68701051182714"></a><a name="b68701051182714"></a>BYDAY</strong> can be set to <strong id="b287017510278"><a name="b287017510278"></a><a name="b287017510278"></a>MO</strong>, <strong id="b20870155114272"><a name="b20870155114272"></a><a name="b20870155114272"></a>TU</strong>, <strong id="b48711451192716"><a name="b48711451192716"></a><a name="b48711451192716"></a>WE</strong>, <strong id="b1687115515274"><a name="b1687115515274"></a><a name="b1687115515274"></a>TH</strong>, <strong id="b587115114275"><a name="b587115114275"></a><a name="b587115114275"></a>FR</strong>, <strong id="b1871351162713"><a name="b1871351162713"></a><a name="b1871351162713"></a>SA</strong>, and <strong id="b487145122716"><a name="b487145122716"></a><a name="b487145122716"></a>SU</strong> (seven days of a week), <strong id="b15871251162717"><a name="b15871251162717"></a><a name="b15871251162717"></a>BYHOUR</strong> ranges from 0 hours to 23 hours, and <strong id="b17871145112276"><a name="b17871145112276"></a><a name="b17871145112276"></a>BYMINUTE</strong> ranges from 0 minutes to 59 minutes. The scheduling interval must not be less than 1 hour. A maximum of 24 time points are allowed in a day.</p>
    </td>
    </tr>
    <tr id="row5906832"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p8691401"><a name="p8691401"></a><a name="p8691401"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p48857155"><a name="p48857155"></a><a name="p48857155"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p65115477"><a name="p65115477"></a><a name="p65115477"></a>Scheduler start time, for example, <strong id="b785111820216"><a name="b785111820216"></a><a name="b785111820216"></a>2017-04-18T01:21:52.701973</strong></p>
    </td>
    </tr>
    <tr id="row3925102501419"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p3927152511410"><a name="p3927152511410"></a><a name="p3927152511410"></a>format</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p99279252143"><a name="p99279252143"></a><a name="p99279252143"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1392742517147"><a name="p1392742517147"></a><a name="p1392742517147"></a>Scheduler type</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource\_tag**

    **Table  10**  Parameter description of field  **resource\_tag**

    <a name="table1431115645119"></a>
    <table><thead align="left"><tr id="row4339106155119"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p69041455124319"><a name="p69041455124319"></a><a name="p69041455124319"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p129044555438"><a name="p129044555438"></a><a name="p129044555438"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p59041455144318"><a name="p59041455144318"></a><a name="p59041455144318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63768665110"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p10380567512"><a name="p10380567512"></a><a name="p10380567512"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1739414617517"><a name="p1739414617517"></a><a name="p1739414617517"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p13925135105714"><a name="p13925135105714"></a><a name="p13925135105714"></a>Tag key</p>
    <p id="p7327206587"><a name="p7327206587"></a><a name="p7327206587"></a>It consists of up to 36 characters.</p>
    <p id="p145821075819"><a name="p145821075819"></a><a name="p145821075819"></a>It cannot be an empty string.</p>
    <p id="p14766132412516"><a name="p14766132412516"></a><a name="p14766132412516"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row1116111556513"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p1816118554511"><a name="p1816118554511"></a><a name="p1816118554511"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1116145519518"><a name="p1116145519518"></a><a name="p1116145519518"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1966153512589"><a name="p1966153512589"></a><a name="p1966153512589"></a>Tag value</p>
    <p id="p8808725135910"><a name="p8808725135910"></a><a name="p8808725135910"></a>It consists of up to 43 characters.</p>
    <p id="p919321595"><a name="p919321595"></a><a name="p919321595"></a>It can be an empty string.</p>
    <p id="p735402619438"><a name="p735402619438"></a><a name="p735402619438"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "policy" : {
        "created_at" : "2017-03-07T09:31:08.265000",
        "description" : "My plan",
        "id" : "27b11f3f-578d-4464-89d1-7c6d5894f753",
        "name" : "my-plan",
        "parameters" : {
          "common" : {
          }
        },
        "project_id" : "tenant",
        "provider_id" : "c714180d-ea34-4b13-9a5e-577c7c416eec",
        "resources" : [ {
          "id" : "45baf976-c20a-4894-a7c3-c94b7376bf55",
          "name" : "resource1",
          "type" : "OS::Nova::Server",
          "extra_info" : {
        }
        }, {
          "id" : "5aa119a8-d25b-45a7-8d1b-88e127885635",
          "name" : "resource2",
          "type" : "OS::Nova::Server", 
          "extra_info" : {
        }
        } ],
        "scheduled_operations" : [ {
          "description" : "My backup policy",
          "enabled" : true,
          "id" : "3b2fdf8c-2cc2-4887-9605-a8443922f6f2",
          "name" : "my-backup-policy",
          "operation_definition" : {
            "max_backups" : "20",
            "plan_id" : "27b11f3f-578d-4464-89d1-7c6d5894f753",
            "provider_id" : "c714180d-ea34-4b13-9a5e-577c7c416eec"
          },
          "operation_type" : "backup",
          "trigger" : {
            "id" : "f1246246-ec6a-4e9a-917e-d050dc2808c9",
            "name" : "default",
            "properties" : {
              "pattern" : "BEGIN:VCALENDAR\r\nBEGIN:VEVENT\r\nRRULE:FREQ=WEEKLY;BYDAY=TH;BYHOUR=12;BYMINUTE=27\r\nEND:VEVENT\r\nEND:VCALENDAR\r\n",
              "start_time" : "2017-03-07 09:31:08",
              "format": "ical"
            },
            "type" : "time"
          },
          "trigger_id" : "f1246246-ec6a-4e9a-917e-d050dc2808c9"
        } ],
        "status" : "disabled"
      }
    }
    ```


## Status Codes<a name="section1124484"></a>

-   Normal

    <a name="table19986118"></a>
    <table><thead align="left"><tr id="row50931523"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p31812687"><a name="p31812687"></a><a name="p31812687"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p26690815"><a name="p26690815"></a><a name="p26690815"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14472379"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p31412076"><a name="p31412076"></a><a name="p31412076"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p61350266"><a name="p61350266"></a><a name="p61350266"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table3315660"></a>
    <table><thead align="left"><tr id="row29897299"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p5762144"><a name="p5762144"></a><a name="p5762144"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p64080501"><a name="p64080501"></a><a name="p64080501"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23138107"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p62247385"><a name="p62247385"></a><a name="p62247385"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p8873464"><a name="p8873464"></a><a name="p8873464"></a>Invalid request parameters.</p>
    </td>
    </tr>
    <tr id="row12752320"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p26304962"><a name="p26304962"></a><a name="p26304962"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p50327193"><a name="p50327193"></a><a name="p50327193"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row50291560"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p47084569"><a name="p47084569"></a><a name="p47084569"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p55753746"><a name="p55753746"></a><a name="p55753746"></a>No operation permission.</p>
    </td>
    </tr>
    <tr id="row32021674"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p43618787"><a name="p43618787"></a><a name="p43618787"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p43460857"><a name="p43460857"></a><a name="p43460857"></a>Requested object not found.</p>
    </td>
    </tr>
    <tr id="row55603394"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p7581037"><a name="p7581037"></a><a name="p7581037"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p10084265"><a name="p10084265"></a><a name="p10084265"></a>Service internal error.</p>
    </td>
    </tr>
    <tr id="row23649525"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p36563340"><a name="p36563340"></a><a name="p36563340"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p8840584"><a name="p8840584"></a><a name="p8840584"></a>Service unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).

