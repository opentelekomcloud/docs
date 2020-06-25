# Querying the List of Permissions of an Agency on a Project<a name="en-us_topic_0079578164"></a>

## Function Description<a name="s48f1857f7f6d48a3985f62aa814b421d"></a>

This interface is used to query the list of permissions of an agency on a project.

## URI<a name="sfe5ded2143184f9d9e1ae057fbeec16c"></a>

-   URI format

    GET /v3.0/OS-AGENCY/projects/\{project\_id\}/agencies/\{agency\_id\}/roles


-   URI parameter description

    <a name="t2aa5c624f4c74e67979449d61a0ceee3"></a>
    <table><thead align="left"><tr id="r18c4c13a248d44b0bf3aea4524953fa7"><th class="cellrowborder" valign="top" width="18.360000000000003%" id="mcps1.1.5.1.1"><p id="af081f9f416d84fd193f19a8e514c3e52"><a name="af081f9f416d84fd193f19a8e514c3e52"></a><a name="af081f9f416d84fd193f19a8e514c3e52"></a><strong id="a173ae121cc9e48328ca613e72f2a1504"><a name="a173ae121cc9e48328ca613e72f2a1504"></a><a name="a173ae121cc9e48328ca613e72f2a1504"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.48%" id="mcps1.1.5.1.2"><p id="a8c4799aa5ce1465695d91d6d4d55e27d"><a name="a8c4799aa5ce1465695d91d6d4d55e27d"></a><a name="a8c4799aa5ce1465695d91d6d4d55e27d"></a><strong id="b84235270618396_1"><a name="b84235270618396_1"></a><a name="b84235270618396_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.86%" id="mcps1.1.5.1.3"><p id="a57a24f48f77e4ae9955876b9a8f4ee7c"><a name="a57a24f48f77e4ae9955876b9a8f4ee7c"></a><a name="a57a24f48f77e4ae9955876b9a8f4ee7c"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.3%" id="mcps1.1.5.1.4"><p id="ad6aa3bad53c04c0b82b35e497f43bfec"><a name="ad6aa3bad53c04c0b82b35e497f43bfec"></a><a name="ad6aa3bad53c04c0b82b35e497f43bfec"></a><strong id="b20601766145329_1"><a name="b20601766145329_1"></a><a name="b20601766145329_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rdc4170c186354c2f91b3b12f6386737d"><td class="cellrowborder" valign="top" width="18.360000000000003%" headers="mcps1.1.5.1.1 "><p id="a40693609e98c4aaea2351499640cc4af"><a name="a40693609e98c4aaea2351499640cc4af"></a><a name="a40693609e98c4aaea2351499640cc4af"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.5.1.2 "><p id="ac4382c99bc924ab5b78cf6e509a1b0eb"><a name="ac4382c99bc924ab5b78cf6e509a1b0eb"></a><a name="ac4382c99bc924ab5b78cf6e509a1b0eb"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.3 "><p id="a8c96ed441f034e50845d1764bdb63b57"><a name="a8c96ed441f034e50845d1764bdb63b57"></a><a name="a8c96ed441f034e50845d1764bdb63b57"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.3%" headers="mcps1.1.5.1.4 "><p id="a7667ef562ece4a14b23cf0e3f9d24f32"><a name="a7667ef562ece4a14b23cf0e3f9d24f32"></a><a name="a7667ef562ece4a14b23cf0e3f9d24f32"></a>ID of a project under the current domain.</p>
    </td>
    </tr>
    <tr id="r3a9071e9271144ea90ac659d8cb1aa15"><td class="cellrowborder" valign="top" width="18.360000000000003%" headers="mcps1.1.5.1.1 "><p id="af2acb86b260b4702b19ab9673276497f"><a name="af2acb86b260b4702b19ab9673276497f"></a><a name="af2acb86b260b4702b19ab9673276497f"></a>agency_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.48%" headers="mcps1.1.5.1.2 "><p id="ab283131f761148199333bf5f71b82283"><a name="ab283131f761148199333bf5f71b82283"></a><a name="ab283131f761148199333bf5f71b82283"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.3 "><p id="abfa70ffe4158411aae2bba76f5d7b7c6"><a name="abfa70ffe4158411aae2bba76f5d7b7c6"></a><a name="abfa70ffe4158411aae2bba76f5d7b7c6"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.3%" headers="mcps1.1.5.1.4 "><p id="a6ab8ddc960e64012b8e1e90823d4bee1"><a name="a6ab8ddc960e64012b8e1e90823d4bee1"></a><a name="a6ab8ddc960e64012b8e1e90823d4bee1"></a>ID of an agency.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="s55f94d8e06e84a6586f85cdad674bc28"></a>

-   Request header parameter description

    <a name="tdbe70f15bc7d49b6a23afd3d4b2200b0"></a>
    <table><thead align="left"><tr id="r0183ddc5d1e44f7bbb33b611f4a7eba1"><th class="cellrowborder" valign="top" width="18.56%" id="mcps1.1.5.1.1"><p id="a686a86141a60438ca8daa521fc171b65"><a name="a686a86141a60438ca8daa521fc171b65"></a><a name="a686a86141a60438ca8daa521fc171b65"></a><strong id="b62655484144322"><a name="b62655484144322"></a><a name="b62655484144322"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.459999999999997%" id="mcps1.1.5.1.2"><p id="a987b6ec3275142678866ad2a4d2cb6bc"><a name="a987b6ec3275142678866ad2a4d2cb6bc"></a><a name="a987b6ec3275142678866ad2a4d2cb6bc"></a><strong id="b84235270618396_3"><a name="b84235270618396_3"></a><a name="b84235270618396_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.4%" id="mcps1.1.5.1.3"><p id="ab73c433bc94940f193659eda3fc3bffb"><a name="ab73c433bc94940f193659eda3fc3bffb"></a><a name="ab73c433bc94940f193659eda3fc3bffb"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.58%" id="mcps1.1.5.1.4"><p id="a2a0caa56617840adb1a30f86e39c759c"><a name="a2a0caa56617840adb1a30f86e39c759c"></a><a name="a2a0caa56617840adb1a30f86e39c759c"></a><strong id="b20601766145329_3"><a name="b20601766145329_3"></a><a name="b20601766145329_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r27a84c3d7e7246a8b705ec299daa27c5"><td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.1.5.1.1 "><p id="ab88e0563a1bd49a586f3361c9c66c85c"><a name="ab88e0563a1bd49a586f3361c9c66c85c"></a><a name="ab88e0563a1bd49a586f3361c9c66c85c"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.459999999999997%" headers="mcps1.1.5.1.2 "><p id="a255d4e6cd16e4622af9250aa8ac21078"><a name="a255d4e6cd16e4622af9250aa8ac21078"></a><a name="a255d4e6cd16e4622af9250aa8ac21078"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.4%" headers="mcps1.1.5.1.3 "><p id="a184d2ad93eb1453da466311b8f2ecfa2"><a name="a184d2ad93eb1453da466311b8f2ecfa2"></a><a name="a184d2ad93eb1453da466311b8f2ecfa2"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.58%" headers="mcps1.1.5.1.4 "><p id="ae1b8420f4bf14f849b98f906d5efe919"><a name="ae1b8420f4bf14f849b98f906d5efe919"></a><a name="ae1b8420f4bf14f849b98f906d5efe919"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="r3c0e62e0463c4e388d7f1bd5e92d820f"><td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.1.5.1.1 "><p id="aaec0543ccbda4911a062562fb2db2330"><a name="aaec0543ccbda4911a062562fb2db2330"></a><a name="aaec0543ccbda4911a062562fb2db2330"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.459999999999997%" headers="mcps1.1.5.1.2 "><p id="accdd3e8baa7f47fc807bbc16ce141f99"><a name="accdd3e8baa7f47fc807bbc16ce141f99"></a><a name="accdd3e8baa7f47fc807bbc16ce141f99"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.4%" headers="mcps1.1.5.1.3 "><p id="ace027e4985744723948acbf16a7f2fa0"><a name="ace027e4985744723948acbf16a7f2fa0"></a><a name="ace027e4985744723948acbf16a7f2fa0"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.58%" headers="mcps1.1.5.1.4 "><p id="p24365116114316"><a name="p24365116114316"></a><a name="p24365116114316"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H "X-Auth-Token:$token" -H 'Content-Type:application/json;charset=utf8' -X GET https://sample.domain.com/v3.0/OS-AGENCY/projects/0945241c5ebc4660bac540d48f2a2c14/agencies/37f90258b820472bbc8a0f4f0bfd720d/roles
    ```


## Response<a name="s06000b8879ab4e03a6a9bb9819efc6cf"></a>

-   Response body parameter description

    <a name="table1197403313610"></a>
    <table><thead align="left"><tr id="row7135103417619"><th class="cellrowborder" valign="top" width="18.59%" id="mcps1.1.5.1.1"><p id="p11351734662"><a name="p11351734662"></a><a name="p11351734662"></a><strong id="b51087662144322"><a name="b51087662144322"></a><a name="b51087662144322"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.59%" id="mcps1.1.5.1.2"><p id="p1513513346616"><a name="p1513513346616"></a><a name="p1513513346616"></a><strong id="b84235270618396_5"><a name="b84235270618396_5"></a><a name="b84235270618396_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.35%" id="mcps1.1.5.1.3"><p id="p12135183418616"><a name="p12135183418616"></a><a name="p12135183418616"></a><strong id="b842352706143526_5"><a name="b842352706143526_5"></a><a name="b842352706143526_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.47%" id="mcps1.1.5.1.4"><p id="p1913510342618"><a name="p1913510342618"></a><a name="p1913510342618"></a><strong id="b20601766145329_5"><a name="b20601766145329_5"></a><a name="b20601766145329_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61356341861"><td class="cellrowborder" valign="top" width="18.59%" headers="mcps1.1.5.1.1 "><p id="p191354341265"><a name="p191354341265"></a><a name="p191354341265"></a>roles</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.59%" headers="mcps1.1.5.1.2 "><p id="p4135133417619"><a name="p4135133417619"></a><a name="p4135133417619"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.35%" headers="mcps1.1.5.1.3 "><p id="p18135183419616"><a name="p18135183419616"></a><a name="p18135183419616"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.47%" headers="mcps1.1.5.1.4 "><p id="p16136734669"><a name="p16136734669"></a><a name="p16136734669"></a>List of roles.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the role format

    <a name="table179862331160"></a>
    <table><thead align="left"><tr id="row013633411613"><th class="cellrowborder" valign="top" width="18.990000000000002%" id="mcps1.1.5.1.1"><p id="p1713617342614"><a name="p1713617342614"></a><a name="p1713617342614"></a><strong id="b63701145144322"><a name="b63701145144322"></a><a name="b63701145144322"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.32%" id="mcps1.1.5.1.2"><p id="p1513683415612"><a name="p1513683415612"></a><a name="p1513683415612"></a><strong id="b84235270618396_7"><a name="b84235270618396_7"></a><a name="b84235270618396_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.35%" id="mcps1.1.5.1.3"><p id="p13136134667"><a name="p13136134667"></a><a name="p13136134667"></a><strong id="b842352706143526_7"><a name="b842352706143526_7"></a><a name="b842352706143526_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.34%" id="mcps1.1.5.1.4"><p id="p1513683416619"><a name="p1513683416619"></a><a name="p1513683416619"></a><strong id="b20601766145329_7"><a name="b20601766145329_7"></a><a name="b20601766145329_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41368341465"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p141368349618"><a name="p141368349618"></a><a name="p141368349618"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.32%" headers="mcps1.1.5.1.2 "><p id="p1313616343616"><a name="p1313616343616"></a><a name="p1313616343616"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.35%" headers="mcps1.1.5.1.3 "><p id="p813643416614"><a name="p813643416614"></a><a name="p813643416614"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.34%" headers="mcps1.1.5.1.4 "><p id="p19136934663"><a name="p19136934663"></a><a name="p19136934663"></a>ID of a role.</p>
    </td>
    </tr>
    <tr id="row1513613341768"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p6136123420612"><a name="p6136123420612"></a><a name="p6136123420612"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.32%" headers="mcps1.1.5.1.2 "><p id="p181369340612"><a name="p181369340612"></a><a name="p181369340612"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.35%" headers="mcps1.1.5.1.3 "><p id="p613717348616"><a name="p613717348616"></a><a name="p613717348616"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.34%" headers="mcps1.1.5.1.4 "><p id="p61371534960"><a name="p61371534960"></a><a name="p61371534960"></a>Name of a role.</p>
    </td>
    </tr>
    <tr id="row313718341068"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p18137134467"><a name="p18137134467"></a><a name="p18137134467"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.32%" headers="mcps1.1.5.1.2 "><p id="p7137534160"><a name="p7137534160"></a><a name="p7137534160"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.35%" headers="mcps1.1.5.1.3 "><p id="p313743413618"><a name="p313743413618"></a><a name="p313743413618"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.34%" headers="mcps1.1.5.1.4 "><p id="p513712341267"><a name="p513712341267"></a><a name="p513712341267"></a>ID of the domain to which a role belongs.</p>
    </td>
    </tr>
    <tr id="row213718343620"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p81372349620"><a name="p81372349620"></a><a name="p81372349620"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.32%" headers="mcps1.1.5.1.2 "><p id="p16137103412612"><a name="p16137103412612"></a><a name="p16137103412612"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.35%" headers="mcps1.1.5.1.3 "><p id="p1313712341069"><a name="p1313712341069"></a><a name="p1313712341069"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.34%" headers="mcps1.1.5.1.4 "><p id="p81371134667"><a name="p81371134667"></a><a name="p81371134667"></a>Display mode of a role.</p>
    <a name="ul15044348114419"></a><a name="ul15044348114419"></a><ul id="ul15044348114419"><li><strong id="b4067993711303"><a name="b4067993711303"></a><a name="b4067993711303"></a>AX</strong>: A role is displayed at the domain layer.</li><li><strong id="b674061011303"><a name="b674061011303"></a><a name="b674061011303"></a>XA</strong>: A role is displayed at the project layer.</li><li><strong id="b911853911303"><a name="b911853911303"></a><a name="b911853911303"></a>AA</strong>: A role is displayed at both the domain and project layers.</li><li><strong id="b17466753113117"><a name="b17466753113117"></a><a name="b17466753113117"></a>XX</strong>: A role is not displayed at the domain or project layer.</li></ul>
    </td>
    </tr>
    <tr id="row4137163412617"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p613712349613"><a name="p613712349613"></a><a name="p613712349613"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.32%" headers="mcps1.1.5.1.2 "><p id="p1813715342614"><a name="p1813715342614"></a><a name="p1813715342614"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.35%" headers="mcps1.1.5.1.3 "><p id="p51371334867"><a name="p51371334867"></a><a name="p51371334867"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.34%" headers="mcps1.1.5.1.4 "><p id="p3137634366"><a name="p3137634366"></a><a name="p3137634366"></a>Displayed name of a role.</p>
    </td>
    </tr>
    <tr id="row201371934965"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p191371534562"><a name="p191371534562"></a><a name="p191371534562"></a>catalog</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.32%" headers="mcps1.1.5.1.2 "><p id="p5137434764"><a name="p5137434764"></a><a name="p5137434764"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.35%" headers="mcps1.1.5.1.3 "><p id="p1413711341862"><a name="p1413711341862"></a><a name="p1413711341862"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.34%" headers="mcps1.1.5.1.4 "><p id="p8137183413612"><a name="p8137183413612"></a><a name="p8137183413612"></a>Directory where a role locates.</p>
    </td>
    </tr>
    <tr id="row1713720342617"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p71379346610"><a name="p71379346610"></a><a name="p71379346610"></a>policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.32%" headers="mcps1.1.5.1.2 "><p id="p1513763415613"><a name="p1513763415613"></a><a name="p1513763415613"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.35%" headers="mcps1.1.5.1.3 "><p id="p19137123416611"><a name="p19137123416611"></a><a name="p19137123416611"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.34%" headers="mcps1.1.5.1.4 "><p id="p613733419619"><a name="p613733419619"></a><a name="p613733419619"></a>Policy of a role.</p>
    </td>
    </tr>
    <tr id="row113853412618"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.5.1.1 "><p id="p18138173413613"><a name="p18138173413613"></a><a name="p18138173413613"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.32%" headers="mcps1.1.5.1.2 "><p id="p16138134762"><a name="p16138134762"></a><a name="p16138134762"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.35%" headers="mcps1.1.5.1.3 "><p id="p1313863412612"><a name="p1313863412612"></a><a name="p1313863412612"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.34%" headers="mcps1.1.5.1.4 "><p id="p3138734967"><a name="p3138734967"></a><a name="p3138734967"></a>Description of a role.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response \(successful request\)

    ```
    {
      "roles": [
        {
          "catalog": "BASE",
          "display_name": "Tenant Guest",
          "name": "readonly",
          "policy": {
            "Version": "1.0",
            "Statement": [
              {
                "Action": [
                  "::Get",
                  "::List"
                ],
                "Effect": "Allow"
              },
              {
                "Action": [
                  "identity:*"
                ],
                "Effect": "Deny"
              }
            ]
          },
          "domain_id": null,
          "type": "AA",
          "id": "b32d99a7778d4fd9aa5bc616c3dc4e5f",
          "description": "Tenant Guest"
        }
      ]
    }
    ```


-   Sample response \(request failed\)

    ```
    {
      "error": {
        "message": "You are not authorized to perform the requested action: identity:list_domain_grants",
        "code": 403,
        "title": "Forbidden"
      }
    }
    ```


## **Status Codes**<a name="scf548a47ab574da29926f89ef11f04ae"></a>

<a name="tb53a27db12514b78ad298186ef40e680"></a>
<table><thead align="left"><tr id="r279e3eb7e49b4038972afa957729a748"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a9bedbb306c1c4c5a92b6662fb91c79e9"><a name="a9bedbb306c1c4c5a92b6662fb91c79e9"></a><a name="a9bedbb306c1c4c5a92b6662fb91c79e9"></a><strong id="b63505764144322"><a name="b63505764144322"></a><a name="b63505764144322"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a52ffdf443ea24d128f4e34c0107d0926"><a name="a52ffdf443ea24d128f4e34c0107d0926"></a><a name="a52ffdf443ea24d128f4e34c0107d0926"></a><strong id="b20601766145329_9"><a name="b20601766145329_9"></a><a name="b20601766145329_9"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="red8d37eb6722412b88f3eb1e4f5bab7f"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a87de5f8b9420480f966e3eb889329931"><a name="a87de5f8b9420480f966e3eb889329931"></a><a name="a87de5f8b9420480f966e3eb889329931"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ad8bc42b733a44c5c9404c6bcc526e731"><a name="ad8bc42b733a44c5c9404c6bcc526e731"></a><a name="ad8bc42b733a44c5c9404c6bcc526e731"></a>The request is successful.</p>
</td>
</tr>
<tr id="rda51c028632943a9a6fa1eb0365f3664"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a745635e99e6a45a9be223af7cc9d2ee8"><a name="a745635e99e6a45a9be223af7cc9d2ee8"></a><a name="a745635e99e6a45a9be223af7cc9d2ee8"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a1de7e41af81e4726b60783ac3ec12540"><a name="a1de7e41af81e4726b60783ac3ec12540"></a><a name="a1de7e41af81e4726b60783ac3ec12540"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="r026dcca6127245af881a1a315754e829"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="abbaaccafee2440d392f1a96549b5315e"><a name="abbaaccafee2440d392f1a96549b5315e"></a><a name="abbaaccafee2440d392f1a96549b5315e"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="af05f4624b2714dc5b4a303761edd70cb"><a name="af05f4624b2714dc5b4a303761edd70cb"></a><a name="af05f4624b2714dc5b4a303761edd70cb"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="r69ed72922d0d4fc2a55306dfeb35088a"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a22e902a300dc4c848ae5cb3a38c9ffdb"><a name="a22e902a300dc4c848ae5cb3a38c9ffdb"></a><a name="a22e902a300dc4c848ae5cb3a38c9ffdb"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aedf5ad7f6ce548df8c144eb22d4169e3"><a name="aedf5ad7f6ce548df8c144eb22d4169e3"></a><a name="aedf5ad7f6ce548df8c144eb22d4169e3"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="rd2bf1b5d8b2045cc81056adcd99a218e"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="afe93fd683f8c4b8b8a04e62378c114cd"><a name="afe93fd683f8c4b8b8a04e62378c114cd"></a><a name="afe93fd683f8c4b8b8a04e62378c114cd"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ad557276af93c4191ad5f64824f932feb"><a name="ad557276af93c4191ad5f64824f932feb"></a><a name="ad557276af93c4191ad5f64824f932feb"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>

