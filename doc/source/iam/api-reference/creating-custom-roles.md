# Creating Custom Roles<a name="EN-US_TOPIC_0147658922"></a>

## Function Description<a name="section495175389414"></a>

This interface is used to create a custom role.

>![](/images/icon-note.gif) **NOTE:**   
>The created custom role can be granted to user groups and agencies. For details, see  [Granting Permissions to a User Group of a Domain](granting-permissions-to-a-user-group-of-a-domain.md),  [Granting Permissions to a User Group Corresponding to a Project](granting-permissions-to-a-user-group-corresponding-to-a-project.md),  [Granting Permissions to an Agency on a Project](granting-permissions-to-an-agency-on-a-project.md), and  [Granting Permissions to an Agency on a Domain](granting-permissions-to-an-agency-on-a-domain.md).  

## URI<a name="section3019338085013"></a>

URI format

POST /v3.0/OS-ROLE/roles

## **Request**<a name="section1437107585444"></a>

-   Request header parameter description

    <a name="table2464904210302"></a>
    <table><thead align="left"><tr id="row2827705710302"><th class="cellrowborder" valign="top" width="19.49%" id="mcps1.1.5.1.1"><p id="p919710810302"><a name="p919710810302"></a><a name="p919710810302"></a><strong id="a173ae121cc9e48328ca613e72f2a1504"><a name="a173ae121cc9e48328ca613e72f2a1504"></a><a name="a173ae121cc9e48328ca613e72f2a1504"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.86%" id="mcps1.1.5.1.2"><p id="p676825610302"><a name="p676825610302"></a><a name="p676825610302"></a><strong id="b13634202633213_1"><a name="b13634202633213_1"></a><a name="b13634202633213_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.5.1.3"><p id="p1135788910302"><a name="p1135788910302"></a><a name="p1135788910302"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.21%" id="mcps1.1.5.1.4"><p id="p4757385510302"><a name="p4757385510302"></a><a name="p4757385510302"></a><strong id="b14438018113629"><a name="b14438018113629"></a><a name="b14438018113629"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2982922410302"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p874030410302"><a name="p874030410302"></a><a name="p874030410302"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p3687601910302"><a name="p3687601910302"></a><a name="p3687601910302"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.3 "><p id="p3416757110302"><a name="p3416757110302"></a><a name="p3416757110302"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.21%" headers="mcps1.1.5.1.4 "><p id="p1610984710302"><a name="p1610984710302"></a><a name="p1610984710302"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row4210342910302"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p2756010302"><a name="p2756010302"></a><a name="p2756010302"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p223240610302"><a name="p223240610302"></a><a name="p223240610302"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.3 "><p id="p4660723710302"><a name="p4660723710302"></a><a name="p4660723710302"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.21%" headers="mcps1.1.5.1.4 "><p id="p12765251112910"><a name="p12765251112910"></a><a name="p12765251112910"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request body parameter description

    <a name="table20476227103839"></a>
    <table><thead align="left"><tr id="row27191649103839"><th class="cellrowborder" valign="top" width="19.49%" id="mcps1.1.5.1.1"><p id="p55039964103839"><a name="p55039964103839"></a><a name="p55039964103839"></a><strong id="b37426530113629"><a name="b37426530113629"></a><a name="b37426530113629"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.86%" id="mcps1.1.5.1.2"><p id="p29052075103839"><a name="p29052075103839"></a><a name="p29052075103839"></a><strong id="b1352638344"><a name="b1352638344"></a><a name="b1352638344"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.83%" id="mcps1.1.5.1.3"><p id="p4407863103839"><a name="p4407863103839"></a><a name="p4407863103839"></a><strong id="b214135502"><a name="b214135502"></a><a name="b214135502"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.82%" id="mcps1.1.5.1.4"><p id="p21492583103839"><a name="p21492583103839"></a><a name="p21492583103839"></a><strong id="b1223461972"><a name="b1223461972"></a><a name="b1223461972"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63177635103839"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p17114836103839"><a name="p17114836103839"></a><a name="p17114836103839"></a>role</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p44124514103839"><a name="p44124514103839"></a><a name="p44124514103839"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.83%" headers="mcps1.1.5.1.3 "><p id="p17315892103839"><a name="p17315892103839"></a><a name="p17315892103839"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.82%" headers="mcps1.1.5.1.4 "><p id="p60410035103839"><a name="p60410035103839"></a><a name="p60410035103839"></a>Request body of a user group.</p>
    </td>
    </tr>
    <tr id="row6819406103839"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p15501051103839"><a name="p15501051103839"></a><a name="p15501051103839"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p47625608103839"><a name="p47625608103839"></a><a name="p47625608103839"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.83%" headers="mcps1.1.5.1.3 "><p id="p32469021103839"><a name="p32469021103839"></a><a name="p32469021103839"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.82%" headers="mcps1.1.5.1.4 "><p id="p12745059103839"><a name="p12745059103839"></a><a name="p12745059103839"></a>Displayed name of a role. The value cannot exceed 64 characters.</p>
    </td>
    </tr>
    <tr id="row1556170910313"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p6642061410319"><a name="p6642061410319"></a><a name="p6642061410319"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p1136068710319"><a name="p1136068710319"></a><a name="p1136068710319"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.83%" headers="mcps1.1.5.1.3 "><p id="p4780046010319"><a name="p4780046010319"></a><a name="p4780046010319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.82%" headers="mcps1.1.5.1.4 "><p id="p4663207010319"><a name="p4663207010319"></a><a name="p4663207010319"></a>Display mode of a role.</p>
    <a name="ul1703544910319"></a><a name="ul1703544910319"></a><ul id="ul1703544910319"><li><strong id="b4067993711303"><a name="b4067993711303"></a><a name="b4067993711303"></a>AX</strong>: A role is displayed at the domain layer.</li><li><strong id="b674061011303"><a name="b674061011303"></a><a name="b674061011303"></a>XA</strong>: A role is displayed at the project layer.<div class="note" id="note6156094517252"><a name="note6156094517252"></a><a name="note6156094517252"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p22955343165917"><a name="p22955343165917"></a><a name="p22955343165917"></a>The display mode of a role can only be <strong id="b84235270610383"><a name="b84235270610383"></a><a name="b84235270610383"></a>AX</strong> or <strong id="b84235270610386"><a name="b84235270610386"></a><a name="b84235270610386"></a>XA</strong>. A role cannot be displayed at both the domain and project layers or neither of the two layers. That is, neither <strong id="b842352706104236"><a name="b842352706104236"></a><a name="b842352706104236"></a>AA</strong> nor <strong id="b842352706104526"><a name="b842352706104526"></a><a name="b842352706104526"></a>XX</strong> is allowed.</p>
    </div></div>
    </li></ul>
    </td>
    </tr>
    <tr id="row5662163914486"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p1766203911486"><a name="p1766203911486"></a><a name="p1766203911486"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p11662103914818"><a name="p11662103914818"></a><a name="p11662103914818"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.83%" headers="mcps1.1.5.1.3 "><p id="p19663139124819"><a name="p19663139124819"></a><a name="p19663139124819"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.82%" headers="mcps1.1.5.1.4 "><p id="p116631239124811"><a name="p116631239124811"></a><a name="p116631239124811"></a>Description of a role. The value cannot exceed 256 characters.</p>
    </td>
    </tr>
    <tr id="row29609315103946"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p65157251103946"><a name="p65157251103946"></a><a name="p65157251103946"></a>policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p43245998103946"><a name="p43245998103946"></a><a name="p43245998103946"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.83%" headers="mcps1.1.5.1.3 "><p id="p13264962103946"><a name="p13264962103946"></a><a name="p13264962103946"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.82%" headers="mcps1.1.5.1.4 "><p id="p720101103946"><a name="p720101103946"></a><a name="p720101103946"></a>Permission policy of a role.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the policy format

    <a name="table91819610348"></a>
    <table><thead align="left"><tr id="row4910255010348"><th class="cellrowborder" valign="top" width="19.52%" id="mcps1.1.5.1.1"><p id="p3416513010511"><a name="p3416513010511"></a><a name="p3416513010511"></a><strong id="b1661670500"><a name="b1661670500"></a><a name="b1661670500"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.89%" id="mcps1.1.5.1.2"><p id="p1591217110511"><a name="p1591217110511"></a><a name="p1591217110511"></a><strong id="b1785681031"><a name="b1785681031"></a><a name="b1785681031"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.79%" id="mcps1.1.5.1.3"><p id="p1381751310511"><a name="p1381751310511"></a><a name="p1381751310511"></a><strong id="b1083253350"><a name="b1083253350"></a><a name="b1083253350"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.8%" id="mcps1.1.5.1.4"><p id="p4547677910511"><a name="p4547677910511"></a><a name="p4547677910511"></a><strong id="b220574076"><a name="b220574076"></a><a name="b220574076"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1795602910348"><td class="cellrowborder" valign="top" width="19.52%" headers="mcps1.1.5.1.1 "><p id="p4515225510348"><a name="p4515225510348"></a><a name="p4515225510348"></a>Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.1.5.1.2 "><p id="p3345406210348"><a name="p3345406210348"></a><a name="p3345406210348"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.79%" headers="mcps1.1.5.1.3 "><p id="p39012936101229"><a name="p39012936101229"></a><a name="p39012936101229"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.5.1.4 "><p id="p4611838510348"><a name="p4611838510348"></a><a name="p4611838510348"></a>Version of a policy. The value must be <strong id="b842352706173323"><a name="b842352706173323"></a><a name="b842352706173323"></a>1.1</strong>.</p>
    </td>
    </tr>
    <tr id="row1241228310348"><td class="cellrowborder" valign="top" width="19.52%" headers="mcps1.1.5.1.1 "><p id="p6587084810348"><a name="p6587084810348"></a><a name="p6587084810348"></a>Statement</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.1.5.1.2 "><p id="p3393848610348"><a name="p3393848610348"></a><a name="p3393848610348"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.79%" headers="mcps1.1.5.1.3 "><p id="p906005101236"><a name="p906005101236"></a><a name="p906005101236"></a>JSONArray</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.5.1.4 "><p id="p319969910348"><a name="p319969910348"></a><a name="p319969910348"></a><strong id="b8423527069344"><a name="b8423527069344"></a><a name="b8423527069344"></a>Statement</strong>: The <strong id="b11933382060574_1"><a name="b11933382060574_1"></a><a name="b11933382060574_1"></a>Statement</strong> field contains the <strong id="b84235270605817_1"><a name="b84235270605817_1"></a><a name="b84235270605817_1"></a>Effect</strong> and <strong id="b84235270605820_1"><a name="b84235270605820_1"></a><a name="b84235270605820_1"></a>Action</strong> elements. <strong id="b84235270605810"><a name="b84235270605810"></a><a name="b84235270605810"></a>Effect</strong> indicates whether the policy allows or denies access. <strong id="b84235270605814"><a name="b84235270605814"></a><a name="b84235270605814"></a>Action</strong> indicates authorization items. The number of statements cannot exceed 8.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the statement format

    <a name="table5858327510641"></a>
    <table><thead align="left"><tr id="row234853010641"><th class="cellrowborder" valign="top" width="19.67196719671967%" id="mcps1.1.5.1.1"><p id="p5601325710641"><a name="p5601325710641"></a><a name="p5601325710641"></a><strong id="b278841212"><a name="b278841212"></a><a name="b278841212"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.89188918891889%" id="mcps1.1.5.1.2"><p id="p4077999710641"><a name="p4077999710641"></a><a name="p4077999710641"></a><strong id="b1815906016"><a name="b1815906016"></a><a name="b1815906016"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.791779177917793%" id="mcps1.1.5.1.3"><p id="p1484546110641"><a name="p1484546110641"></a><a name="p1484546110641"></a><strong id="b419627270"><a name="b419627270"></a><a name="b419627270"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.64436443644364%" id="mcps1.1.5.1.4"><p id="p6163170610641"><a name="p6163170610641"></a><a name="p6163170610641"></a><strong id="b1035317281"><a name="b1035317281"></a><a name="b1035317281"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2611227510641"><td class="cellrowborder" valign="top" width="19.67196719671967%" headers="mcps1.1.5.1.1 "><p id="p3471952910641"><a name="p3471952910641"></a><a name="p3471952910641"></a>Effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.89188918891889%" headers="mcps1.1.5.1.2 "><p id="p6081843510641"><a name="p6081843510641"></a><a name="p6081843510641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.791779177917793%" headers="mcps1.1.5.1.3 "><p id="p51739175101251"><a name="p51739175101251"></a><a name="p51739175101251"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.64436443644364%" headers="mcps1.1.5.1.4 "><p id="p44854910641"><a name="p44854910641"></a><a name="p44854910641"></a>The value can be <strong id="b8423527061142"><a name="b8423527061142"></a><a name="b8423527061142"></a>Allow</strong> and <strong id="b8423527061138"><a name="b8423527061138"></a><a name="b8423527061138"></a>Deny</strong>. If both <strong id="b8423527061734_1"><a name="b8423527061734_1"></a><a name="b8423527061734_1"></a>Allow</strong> and <strong id="b8423527061732_1"><a name="b8423527061732_1"></a><a name="b8423527061732_1"></a>Deny</strong> are found in statements, the policy evaluation starts with <strong id="b842352706101627"><a name="b842352706101627"></a><a name="b842352706101627"></a>Deny</strong>.</p>
    </td>
    </tr>
    <tr id="row403694110641"><td class="cellrowborder" valign="top" width="19.67196719671967%" headers="mcps1.1.5.1.1 "><p id="p15866909101431"><a name="p15866909101431"></a><a name="p15866909101431"></a>Action</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.89188918891889%" headers="mcps1.1.5.1.2 "><p id="p10151214101431"><a name="p10151214101431"></a><a name="p10151214101431"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.791779177917793%" headers="mcps1.1.5.1.3 "><p id="p90575969132"><a name="p90575969132"></a><a name="p90575969132"></a>StringArray</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.64436443644364%" headers="mcps1.1.5.1.4 "><p id="p30124746101431"><a name="p30124746101431"></a><a name="p30124746101431"></a>Permission set, which specifies the operation permissions on resources. The number of permission sets cannot exceed 100.</p>
    <p id="p19358101314235"><a name="p19358101314235"></a><a name="p19358101314235"></a>Format:</p>
    <p id="p2687264101431"><a name="p2687264101431"></a><a name="p2687264101431"></a>The value format is <em id="i84235269723526"><a name="i84235269723526"></a><a name="i84235269723526"></a>Service name</em>:<em id="i84235269723639"><a name="i84235269723639"></a><a name="i84235269723639"></a>Resource type</em>:<em id="i84235269723534"><a name="i84235269723534"></a><a name="i84235269723534"></a>Action</em>, for example, <strong id="b842352706165816"><a name="b842352706165816"></a><a name="b842352706165816"></a>vpc:ports:create</strong>.</p>
    <p id="p24185381101431"><a name="p24185381101431"></a><a name="p24185381101431"></a><em id="i84235269711017"><a name="i84235269711017"></a><a name="i84235269711017"></a>Service name</em>: indicates the product name, such as <strong id="b1194612119195"><a name="b1194612119195"></a><a name="b1194612119195"></a>ecs</strong>, <strong id="b9388113991919"><a name="b9388113991919"></a><a name="b9388113991919"></a>evs</strong>, or <strong id="b3519155131912"><a name="b3519155131912"></a><a name="b3519155131912"></a>vpc</strong>. Only lowercase letters are allowed.</p>
    <p id="p16341842101431"><a name="p16341842101431"></a><a name="p16341842101431"></a><em id="i84235269710240"><a name="i84235269710240"></a><a name="i84235269710240"></a>Resource type</em> and <em id="i84235269710254"><a name="i84235269710254"></a><a name="i84235269710254"></a>Action</em>: The values are case-insensitive, and the wildcard (*) is allowed. A wildcard (*) can represent all or part of information about resource types and actions for the specific service.</p>
    </td>
    </tr>
    <tr id="row1793314525213"><td class="cellrowborder" valign="top" width="19.67196719671967%" headers="mcps1.1.5.1.1 "><p id="p159334511526"><a name="p159334511526"></a><a name="p159334511526"></a>Resource</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.89188918891889%" headers="mcps1.1.5.1.2 "><p id="p793310595216"><a name="p793310595216"></a><a name="p793310595216"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.791779177917793%" headers="mcps1.1.5.1.3 "><p id="p59333585213"><a name="p59333585213"></a><a name="p59333585213"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.64436443644364%" headers="mcps1.1.5.1.4 "><a name="ul178901826143415"></a><a name="ul178901826143415"></a><ul id="ul178901826143415"><li>Resources to be managed. After a domain establishes multiple trust relationships between itself and your domain, you can authorize different users to manage resources of the delegating party. Each user can only switch to the specified agencies. You can create custom policies to assign specified permissions to users.</li><li>When creating a custom policy, specify the <strong id="b1527265894720"><a name="b1527265894720"></a><a name="b1527265894720"></a>Action</strong> as <strong id="b1790513384816"><a name="b1790513384816"></a><a name="b1790513384816"></a>iam:agencies:assume</strong>.</li><li>A maximum of 10 resources can be delegated.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Format description of the Resource parameter

    <a name="table755284212333"></a>
    <table><thead align="left"><tr id="row855217422337"><th class="cellrowborder" valign="top" width="19.52%" id="mcps1.1.5.1.1"><p id="p5552184233312"><a name="p5552184233312"></a><a name="p5552184233312"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.89%" id="mcps1.1.5.1.2"><p id="p6552242193314"><a name="p6552242193314"></a><a name="p6552242193314"></a><strong id="b724015774"><a name="b724015774"></a><a name="b724015774"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.79%" id="mcps1.1.5.1.3"><p id="p65531427338"><a name="p65531427338"></a><a name="p65531427338"></a><strong id="b1037293767"><a name="b1037293767"></a><a name="b1037293767"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.8%" id="mcps1.1.5.1.4"><p id="p135531542163310"><a name="p135531542163310"></a><a name="p135531542163310"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1955313429331"><td class="cellrowborder" valign="top" width="19.52%" headers="mcps1.1.5.1.1 "><p id="p195532423339"><a name="p195532423339"></a><a name="p195532423339"></a>uri</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.1.5.1.2 "><p id="p2553134203312"><a name="p2553134203312"></a><a name="p2553134203312"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.79%" headers="mcps1.1.5.1.3 "><p id="p7553642193315"><a name="p7553642193315"></a><a name="p7553642193315"></a>StringArray</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.5.1.4 "><p id="p1715635317473"><a name="p1715635317473"></a><a name="p1715635317473"></a>URI of a delegated resource, which can contain a maximum of 128 characters.</p>
    <p id="p1355354283311"><a name="p1355354283311"></a><a name="p1355354283311"></a>Format: /iam/agencies/{<em id="i1467564118810"><a name="i1467564118810"></a><a name="i1467564118810"></a>agency ID</em>}</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request \(custom policy for a cloud service\)

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X POST -d'{"role":{"display_name":"Customed ECS Viewer","policy":{"Version":"1.1","Statement":[{"Action":["ecs:*:get*","ecs:*:list*","ecs:blockDevice:use","ecs:serverGroups:manage","ecs:serverVolumes:use","evs:*:get*","evs:*:list*","vpc:*:get*","vpc:*:list*","ims:*:get*","ims:*:list*"],"Effect":"Allow"}]},"type":"XA","description":"The read-only permissions to all ECS resources,which can be used for statistics ands urvey."}}' https://10.22.44.158:31943/v3.0/OS-ROLE/roles
    ```


-   Sample request \(custom policy for an agency\)

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X POST -d'{"role":{"display_name":"Customed fine-grained agency","policy":{"Version":"1.1","Statement":[{"Action":["iam:agencies:assume"],"Effect":"Allow","Resource":{"uri":["/iam/agencies/4eb04341ec2d41f5add4f3846d884f2d"]}}]},"type":"AX","description":"Allow sub-user to use agency."}}' https://10.22.44.158:31943/v3.0/OS-ROLE/roles
    ```


## **Response**<a name="section422798898594"></a>

-   Response body parameter description

    <a name="table152994212185"></a>
    <table><thead align="left"><tr id="row173714281818"><th class="cellrowborder" valign="top" width="19.75197519751975%" id="mcps1.1.5.1.1"><p id="p5372426180"><a name="p5372426180"></a><a name="p5372426180"></a><strong id="b660267542"><a name="b660267542"></a><a name="b660267542"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.681868186818683%" id="mcps1.1.5.1.2"><p id="p1056617720581"><a name="p1056617720581"></a><a name="p1056617720581"></a><strong id="b814279931"><a name="b814279931"></a><a name="b814279931"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.75177517751775%" id="mcps1.1.5.1.3"><p id="p15441142151819"><a name="p15441142151819"></a><a name="p15441142151819"></a><strong id="b363812281"><a name="b363812281"></a><a name="b363812281"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.81438143814381%" id="mcps1.1.5.1.4"><p id="p7463424187"><a name="p7463424187"></a><a name="p7463424187"></a><strong id="b433819159"><a name="b433819159"></a><a name="b433819159"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1948142191819"><td class="cellrowborder" valign="top" width="19.75197519751975%" headers="mcps1.1.5.1.1 "><p id="p205084221810"><a name="p205084221810"></a><a name="p205084221810"></a>role</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.681868186818683%" headers="mcps1.1.5.1.2 "><p id="p556717175819"><a name="p556717175819"></a><a name="p556717175819"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.75177517751775%" headers="mcps1.1.5.1.3 "><p id="p195510424182"><a name="p195510424182"></a><a name="p195510424182"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.81438143814381%" headers="mcps1.1.5.1.4 "><p id="p195619421189"><a name="p195619421189"></a><a name="p195619421189"></a>Details of the role.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Description for the role format

    <a name="table11611242141815"></a>
    <table><thead align="left"><tr id="row13671142131817"><th class="cellrowborder" valign="top" width="19.81%" id="mcps1.1.5.1.1"><p id="p16994231814"><a name="p16994231814"></a><a name="p16994231814"></a><strong id="b16646705155652"><a name="b16646705155652"></a><a name="b16646705155652"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.33%" id="mcps1.1.5.1.2"><p id="p47406710214141"><a name="p47406710214141"></a><a name="p47406710214141"></a><strong id="b1273247287"><a name="b1273247287"></a><a name="b1273247287"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.05%" id="mcps1.1.5.1.3"><p id="p47416427185"><a name="p47416427185"></a><a name="p47416427185"></a><strong id="b57746418"><a name="b57746418"></a><a name="b57746418"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.81%" id="mcps1.1.5.1.4"><p id="p1576124212185"><a name="p1576124212185"></a><a name="p1576124212185"></a><strong id="b1595252565"><a name="b1595252565"></a><a name="b1595252565"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2718319318492"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p4332214818492"><a name="p4332214818492"></a><a name="p4332214818492"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p52491180214141"><a name="p52491180214141"></a><a name="p52491180214141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.05%" headers="mcps1.1.5.1.3 "><p id="p1943313718492"><a name="p1943313718492"></a><a name="p1943313718492"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.81%" headers="mcps1.1.5.1.4 "><p id="p3058025418492"><a name="p3058025418492"></a><a name="p3058025418492"></a>ID of the domain to which a role belongs.</p>
    </td>
    </tr>
    <tr id="row185642121813"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p198724213181"><a name="p198724213181"></a><a name="p198724213181"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p20220752214141"><a name="p20220752214141"></a><a name="p20220752214141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.05%" headers="mcps1.1.5.1.3 "><p id="p1690194261820"><a name="p1690194261820"></a><a name="p1690194261820"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.81%" headers="mcps1.1.5.1.4 "><p id="p1193124219186"><a name="p1193124219186"></a><a name="p1193124219186"></a>ID of a role.</p>
    </td>
    </tr>
    <tr id="row18941242151812"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p169614219187"><a name="p169614219187"></a><a name="p169614219187"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p64755119214141"><a name="p64755119214141"></a><a name="p64755119214141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.05%" headers="mcps1.1.5.1.3 "><p id="p119974291818"><a name="p119974291818"></a><a name="p119974291818"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.81%" headers="mcps1.1.5.1.4 "><p id="p121019429189"><a name="p121019429189"></a><a name="p121019429189"></a>Resource links of a role.</p>
    </td>
    </tr>
    <tr id="row1910211424181"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p210417429182"><a name="p210417429182"></a><a name="p210417429182"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p3095987214141"><a name="p3095987214141"></a><a name="p3095987214141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.05%" headers="mcps1.1.5.1.3 "><p id="p1210874251814"><a name="p1210874251814"></a><a name="p1210874251814"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.81%" headers="mcps1.1.5.1.4 "><p id="p141091842191813"><a name="p141091842191813"></a><a name="p141091842191813"></a>Name of a role.</p>
    </td>
    </tr>
    <tr id="row1548265115236"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p5745115415230"><a name="p5745115415230"></a><a name="p5745115415230"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p7745175432314"><a name="p7745175432314"></a><a name="p7745175432314"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.05%" headers="mcps1.1.5.1.3 "><p id="p147452546233"><a name="p147452546233"></a><a name="p147452546233"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.81%" headers="mcps1.1.5.1.4 "><p id="p1429292915554"><a name="p1429292915554"></a><a name="p1429292915554"></a>Display mode of a role.</p>
    <a name="ul8576277103251"></a><a name="ul8576277103251"></a><ul id="ul8576277103251"><li><strong id="b906008316"><a name="b906008316"></a><a name="b906008316"></a>AX</strong>: A role is displayed at the domain layer.</li><li><strong id="b441956651"><a name="b441956651"></a><a name="b441956651"></a>XA</strong>: A role is displayed at the project layer.</li></ul>
    </td>
    </tr>
    <tr id="row57645998214145"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p59369096214145"><a name="p59369096214145"></a><a name="p59369096214145"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p19319748214145"><a name="p19319748214145"></a><a name="p19319748214145"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.05%" headers="mcps1.1.5.1.3 "><p id="p23075900214145"><a name="p23075900214145"></a><a name="p23075900214145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.81%" headers="mcps1.1.5.1.4 "><p id="p12999383214145"><a name="p12999383214145"></a><a name="p12999383214145"></a>Displayed name of a role.</p>
    </td>
    </tr>
    <tr id="row33977091214145"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p65673627214145"><a name="p65673627214145"></a><a name="p65673627214145"></a>catalog</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p34536686214145"><a name="p34536686214145"></a><a name="p34536686214145"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.05%" headers="mcps1.1.5.1.3 "><p id="p3673120214145"><a name="p3673120214145"></a><a name="p3673120214145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.81%" headers="mcps1.1.5.1.4 "><p id="p55700186214145"><a name="p55700186214145"></a><a name="p55700186214145"></a>Directory where a role locates.</p>
    </td>
    </tr>
    <tr id="row53576771214145"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p48279332214145"><a name="p48279332214145"></a><a name="p48279332214145"></a>policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p26134551214145"><a name="p26134551214145"></a><a name="p26134551214145"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.05%" headers="mcps1.1.5.1.3 "><p id="p18445422214145"><a name="p18445422214145"></a><a name="p18445422214145"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.81%" headers="mcps1.1.5.1.4 "><p id="p963217214145"><a name="p963217214145"></a><a name="p963217214145"></a>Policy of a role.</p>
    </td>
    </tr>
    <tr id="row28018958214145"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="p5775123214145"><a name="p5775123214145"></a><a name="p5775123214145"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p40003297214145"><a name="p40003297214145"></a><a name="p40003297214145"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.05%" headers="mcps1.1.5.1.3 "><p id="p47954295214145"><a name="p47954295214145"></a><a name="p47954295214145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.81%" headers="mcps1.1.5.1.4 "><p id="p43833853214145"><a name="p43833853214145"></a><a name="p43833853214145"></a>Description of a role.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example successful response \(custom policy for a cloud service\)

    ```
    {
      "role": {
          "domain_id": "9698542758bc422088c0c3eabfc30d12",
          "id": "24e7a89bffe443979760c4e9715c13a5",
          "links": {
            "self": "www.example.com/v3/roles/9698542758bc422088c0c3eabfc30d12"
          },
          "name": "custom_9698542758bc422088c0c3eabfc30d12_0",
          "type": "XA",
          "display_name": "Customed ECS Viewer",
          "catalog": "CUSTOMED",
          "policy": {
            "Version": "1.1",
            "Statement": [
              {
                "Action": [
                  "ecs:*:get*",
                  "ecs:*:list*",
                  "ecs:blockDevice:use",
                  "ecs:serverGroups:manage",
                  "ecs:serverVolumes:use",
                  "evs:*:get*",
                  "evs:*:list*",
                  "vpc:*:get*",
                  "vpc:*:list*",
                  "ims:*:get*",
                  "ims:*:list*"
                ],
                "Effect": "Allow"
              }
            ]
          },
          "description": "The read-only permissions to all ECS resources, which can be used for statistics and survey."
        }
    }
    ```


-   Example successful response \(custom policy for an agency\)

    ```
    {
      "role": {
          "domain_id": "9698542758bc422088c0c3eabfc30d12",
          "id": "5c03c324d4784435baaedb6a9bf01321",
          "links": {
            "self": "www.example.com/v3/roles/9698542758bc422088c0c3eabfc30d12"
          },
          "name": "custom_9698542758bc422088c0c3eabfc30d12_1",
          "type": "AX",
          "display_name": "Customed fine-grained agency",
          "catalog": "CUSTOMED",
          "policy": {
            "Version": "1.1",
            "Statement": [
              {
                "Action": [
                  "iam:agencies:assume"
                ],
                "Effect": "Allow",
                "Resource": {
                "uri": [
                  "/iam/agencies/4eb04341ec2d41f5add4f3846d884f2d"
                ]
               }
              }
            ]
          },
          "description": "Allow sub-user to use agency."
        }
    }
    ```


-   Error response body parameter description

    <a name="table11369132715418"></a>
    <table><thead align="left"><tr id="row1937712715414"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.5.1.1"><p id="p1237819270542"><a name="p1237819270542"></a><a name="p1237819270542"></a><strong id="b1817204460"><a name="b1817204460"></a><a name="b1817204460"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.1.5.1.2"><p id="p338319273549"><a name="p338319273549"></a><a name="p338319273549"></a><strong id="b476485815"><a name="b476485815"></a><a name="b476485815"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.06%" id="mcps1.1.5.1.3"><p id="p15386152755413"><a name="p15386152755413"></a><a name="p15386152755413"></a><strong id="b1850247174"><a name="b1850247174"></a><a name="b1850247174"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.940000000000005%" id="mcps1.1.5.1.4"><p id="p538916276547"><a name="p538916276547"></a><a name="p538916276547"></a><strong id="b1801963599"><a name="b1801963599"></a><a name="b1801963599"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row93911227135417"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p339310274543"><a name="p339310274543"></a><a name="p339310274543"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p16394152716546"><a name="p16394152716546"></a><a name="p16394152716546"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p1339662755417"><a name="p1339662755417"></a><a name="p1339662755417"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p1397172725415"><a name="p1397172725415"></a><a name="p1397172725415"></a>Response error</p>
    </td>
    </tr>
    <tr id="row18399927115419"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p1024473095615"><a name="p1024473095615"></a><a name="p1024473095615"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p1740352725417"><a name="p1740352725417"></a><a name="p1740352725417"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p84051327155415"><a name="p84051327155415"></a><a name="p84051327155415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p154064276547"><a name="p154064276547"></a><a name="p154064276547"></a>Error details</p>
    </td>
    </tr>
    <tr id="row372143818575"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p157237386575"><a name="p157237386575"></a><a name="p157237386575"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p1723193895712"><a name="p1723193895712"></a><a name="p1723193895712"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p472318381579"><a name="p472318381579"></a><a name="p472318381579"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p1172313855711"><a name="p1172313855711"></a><a name="p1172313855711"></a>Error code</p>
    </td>
    </tr>
    <tr id="row12320192018583"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p1132012017585"><a name="p1132012017585"></a><a name="p1132012017585"></a>title</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p9320122095810"><a name="p9320122095810"></a><a name="p9320122095810"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p2032082014581"><a name="p2032082014581"></a><a name="p2032082014581"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p681134632"><a name="p681134632"></a><a name="p681134632"></a>Error type</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response \(failed response\)

    ```
    {
      "error": {
        "message": "Authentication failed",
        "code": 401,
        "title": "Unauthorized"
      }
    }
    ```


## **Status Codes**<a name="section5556784894735"></a>

<a name="en-us_topic_0032920307_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0032920307_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0032920307_p51565323"><a name="en-us_topic_0032920307_p51565323"></a><a name="en-us_topic_0032920307_p51565323"></a><strong id="b23486412155652"><a name="b23486412155652"></a><a name="b23486412155652"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0032920307_p16041657"><a name="en-us_topic_0032920307_p16041657"></a><a name="en-us_topic_0032920307_p16041657"></a><strong id="b20601766145329_9"><a name="b20601766145329_9"></a><a name="b20601766145329_9"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0032920307_row24305815"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0032920307_p22613965"><a name="en-us_topic_0032920307_p22613965"></a><a name="en-us_topic_0032920307_p22613965"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0032920307_p19791876"><a name="en-us_topic_0032920307_p19791876"></a><a name="en-us_topic_0032920307_p19791876"></a>The request is successful.</p>
</td>
</tr>
<tr id="en-us_topic_0032920307_row43909159"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0032920307_p66980994"><a name="en-us_topic_0032920307_p66980994"></a><a name="en-us_topic_0032920307_p66980994"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0032920307_p56751409"><a name="en-us_topic_0032920307_p56751409"></a><a name="en-us_topic_0032920307_p56751409"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row460808479497"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p120744399497"><a name="p120744399497"></a><a name="p120744399497"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p385055099497"><a name="p385055099497"></a><a name="p385055099497"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="en-us_topic_0032920307_row41000636"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0032920307_p32717189"><a name="en-us_topic_0032920307_p32717189"></a><a name="en-us_topic_0032920307_p32717189"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0032920307_p32846614"><a name="en-us_topic_0032920307_p32846614"></a><a name="en-us_topic_0032920307_p32846614"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row6698780174113"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p33175165174115"><a name="p33175165174115"></a><a name="p33175165174115"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2833855174115"><a name="p2833855174115"></a><a name="p2833855174115"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

