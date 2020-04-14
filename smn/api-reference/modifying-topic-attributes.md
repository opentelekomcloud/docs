# Modifying Topic Attributes<a name="smn_api_51007"></a>

## Description<a name="section64935954"></a>

-   API name

    UpdateTopicAttribute


-   Function

    Modify the topic attributes.


## URI<a name="section47552675"></a>

-   URI format

    PUT /v2/\{project\_id\}/notifications/topics/\{topic\_urn\}/attributes/\{name\}


-   Parameter description

    <a name="table60453091"></a>
    <table><thead align="left"><tr id="row31471768"><th class="cellrowborder" valign="top" width="24.80751924807519%" id="mcps1.1.5.1.1"><p id="p66185246"><a name="p66185246"></a><a name="p66185246"></a><strong id="b842352706191030"><a name="b842352706191030"></a><a name="b842352706191030"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.227677232276772%" id="mcps1.1.5.1.2"><p id="p59404709"><a name="p59404709"></a><a name="p59404709"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.447855214478555%" id="mcps1.1.5.1.3"><p id="p47052116"><a name="p47052116"></a><a name="p47052116"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.516948305169482%" id="mcps1.1.5.1.4"><p id="p53125076"><a name="p53125076"></a><a name="p53125076"></a><strong id="b84235270619115"><a name="b84235270619115"></a><a name="b84235270619115"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57297510"><td class="cellrowborder" valign="top" width="24.80751924807519%" headers="mcps1.1.5.1.1 "><p id="p10586695"><a name="p10586695"></a><a name="p10586695"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.227677232276772%" headers="mcps1.1.5.1.2 "><p id="p52215961"><a name="p52215961"></a><a name="p52215961"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.447855214478555%" headers="mcps1.1.5.1.3 "><p id="p1634435"><a name="p1634435"></a><a name="p1634435"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.516948305169482%" headers="mcps1.1.5.1.4 "><p id="p45137179155033"><a name="p45137179155033"></a><a name="p45137179155033"></a>Project ID</p>
    <p id="p65280430"><a name="p65280430"></a><a name="p65280430"></a>See section <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row9249362"><td class="cellrowborder" valign="top" width="24.80751924807519%" headers="mcps1.1.5.1.1 "><p id="p11000853"><a name="p11000853"></a><a name="p11000853"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.227677232276772%" headers="mcps1.1.5.1.2 "><p id="p18653909"><a name="p18653909"></a><a name="p18653909"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.447855214478555%" headers="mcps1.1.5.1.3 "><p id="p34571641"><a name="p34571641"></a><a name="p34571641"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.516948305169482%" headers="mcps1.1.5.1.4 "><p id="p48839530"><a name="p48839530"></a><a name="p48839530"></a>Unique resource ID of a topic. You can obtain it according to <a href="querying-topics.md">Querying Topics</a>.</p>
    </td>
    </tr>
    <tr id="row3251307152236"><td class="cellrowborder" valign="top" width="24.80751924807519%" headers="mcps1.1.5.1.1 "><p id="p62029310152236"><a name="p62029310152236"></a><a name="p62029310152236"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.227677232276772%" headers="mcps1.1.5.1.2 "><p id="p58318222152236"><a name="p58318222152236"></a><a name="p58318222152236"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.447855214478555%" headers="mcps1.1.5.1.3 "><p id="p26155522152236"><a name="p26155522152236"></a><a name="p26155522152236"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.516948305169482%" headers="mcps1.1.5.1.4 "><p id="p43921265152316"><a name="p43921265152316"></a><a name="p43921265152316"></a>Attribute name</p>
    <p id="p28391318113116"><a name="p28391318113116"></a><a name="p28391318113116"></a>Only specified attribute names are supported. For details, see <a href="topic-attribute-list.md">Topic Attribute List</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section25320898"></a>

-   Parameter description

    <a name="table16833793185146"></a>
    <table><thead align="left"><tr id="row46280455185146"><th class="cellrowborder" valign="top" width="17.65%" id="mcps1.1.5.1.1"><p id="p57729347185146"><a name="p57729347185146"></a><a name="p57729347185146"></a><strong id="b194441542"><a name="b194441542"></a><a name="b194441542"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.06%" id="mcps1.1.5.1.2"><p id="p45565556185146"><a name="p45565556185146"></a><a name="p45565556185146"></a><strong id="b338584593125"><a name="b338584593125"></a><a name="b338584593125"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.22%" id="mcps1.1.5.1.3"><p id="p66931458185146"><a name="p66931458185146"></a><a name="p66931458185146"></a><strong id="b319561994"><a name="b319561994"></a><a name="b319561994"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.07%" id="mcps1.1.5.1.4"><p id="p52739028185146"><a name="p52739028185146"></a><a name="p52739028185146"></a><strong id="b575156414"><a name="b575156414"></a><a name="b575156414"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7465062185146"><td class="cellrowborder" valign="top" width="17.65%" headers="mcps1.1.5.1.1 "><p id="p690294185146"><a name="p690294185146"></a><a name="p690294185146"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.06%" headers="mcps1.1.5.1.2 "><p id="p55913834185146"><a name="p55913834185146"></a><a name="p55913834185146"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.22%" headers="mcps1.1.5.1.3 "><p id="p32726699185146"><a name="p32726699185146"></a><a name="p32726699185146"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.07%" headers="mcps1.1.5.1.4 "><p id="p33616928185146"><a name="p33616928185146"></a><a name="p33616928185146"></a>Topic attribute value</p>
    <p id="p5140847203117"><a name="p5140847203117"></a><a name="p5140847203117"></a>The value cannot exceed 30 KB. For details, see <a href="#table53240944112753">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1**  Topic attribute values

    <a name="table53240944112753"></a>
    <table><thead align="left"><tr id="row21987414112753"><th class="cellrowborder" valign="top" width="21.709999999999997%" id="mcps1.2.4.1.1"><p id="p35443943112753"><a name="p35443943112753"></a><a name="p35443943112753"></a><strong id="b115563436368"><a name="b115563436368"></a><a name="b115563436368"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.22%" id="mcps1.2.4.1.2"><p id="p1722161112753"><a name="p1722161112753"></a><a name="p1722161112753"></a><strong id="b15203449370"><a name="b15203449370"></a><a name="b15203449370"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.07%" id="mcps1.2.4.1.3"><p id="p47496205112753"><a name="p47496205112753"></a><a name="p47496205112753"></a>Restriction</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44101580112753"><td class="cellrowborder" valign="top" width="21.709999999999997%" headers="mcps1.2.4.1.1 "><p id="p36150079112753"><a name="p36150079112753"></a><a name="p36150079112753"></a>Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.22%" headers="mcps1.2.4.1.2 "><p id="p42475248112753"><a name="p42475248112753"></a><a name="p42475248112753"></a>Policy specification version</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.07%" headers="mcps1.2.4.1.3 "><p id="p17943058112753"><a name="p17943058112753"></a><a name="p17943058112753"></a>Currently, only <strong id="b842352706145948"><a name="b842352706145948"></a><a name="b842352706145948"></a>2016-09-07</strong> is supported.</p>
    </td>
    </tr>
    <tr id="row46405782112753"><td class="cellrowborder" valign="top" width="21.709999999999997%" headers="mcps1.2.4.1.1 "><p id="p61369906112753"><a name="p61369906112753"></a><a name="p61369906112753"></a>Id</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.22%" headers="mcps1.2.4.1.2 "><p id="p4906500112753"><a name="p4906500112753"></a><a name="p4906500112753"></a>Policy ID, which uniquely identifies a policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.07%" headers="mcps1.2.4.1.3 "><p id="p61882243112753"><a name="p61882243112753"></a><a name="p61882243112753"></a>The value cannot be empty.</p>
    </td>
    </tr>
    <tr id="row39288912112753"><td class="cellrowborder" valign="top" width="21.709999999999997%" headers="mcps1.2.4.1.1 "><p id="p14998859112753"><a name="p14998859112753"></a><a name="p14998859112753"></a>Statement</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.22%" headers="mcps1.2.4.1.2 "><p id="p1139155615212"><a name="p1139155615212"></a><a name="p1139155615212"></a>Statements used to configure a topic policy. Each topic policy may contain one or more statements. You can use statements to grant topic permissions to other users or cloud services.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.07%" headers="mcps1.2.4.1.3 "><p id="p31968219112753"><a name="p31968219112753"></a><a name="p31968219112753"></a>A policy must contain at least one statement. For details about elements in a statement, see <a href="#table13574080155334">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Statement elements description

    <a name="table13574080155334"></a>
    <table><thead align="left"><tr id="row2428006155334"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.1"><p id="p66371740155519"><a name="p66371740155519"></a><a name="p66371740155519"></a><strong id="b43082088194323"><a name="b43082088194323"></a><a name="b43082088194323"></a>Element</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.2"><p id="p66616597155519"><a name="p66616597155519"></a><a name="p66616597155519"></a><strong id="b215516115112"><a name="b215516115112"></a><a name="b215516115112"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="p43791157155519"><a name="p43791157155519"></a><a name="p43791157155519"></a>Restriction</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5501174215551"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p2745813215551"><a name="p2745813215551"></a><a name="p2745813215551"></a>Sid</p>
    </td>
    <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.2 "><p id="p951625815551"><a name="p951625815551"></a><a name="p951625815551"></a>Statement ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p3261944415551"><a name="p3261944415551"></a><a name="p3261944415551"></a>The statement ID must be unique, for example, <strong id="b84235270620952"><a name="b84235270620952"></a><a name="b84235270620952"></a>statement01</strong> or <strong id="b39889324202233"><a name="b39889324202233"></a><a name="b39889324202233"></a>statement02</strong>.</p>
    </td>
    </tr>
    <tr id="row2102549615551"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p2303739015551"><a name="p2303739015551"></a><a name="p2303739015551"></a>Effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.2 "><p id="p5408933915551"><a name="p5408933915551"></a><a name="p5408933915551"></a>Statement effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p1916032815551"><a name="p1916032815551"></a><a name="p1916032815551"></a>The value can be <strong id="b84235270615257"><a name="b84235270615257"></a><a name="b84235270615257"></a>Allow</strong> or <strong id="b8423527061530"><a name="b8423527061530"></a><a name="b8423527061530"></a>Deny</strong>.</p>
    </td>
    </tr>
    <tr id="row233616615551"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p923559515551"><a name="p923559515551"></a><a name="p923559515551"></a>Principal</p>
    <p id="p143555201842"><a name="p143555201842"></a><a name="p143555201842"></a>NotPrincipal</p>
    </td>
    <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.2 "><a name="ul56995346416"></a><a name="ul56995346416"></a><ul id="ul56995346416"><li><strong id="b842352706123826"><a name="b842352706123826"></a><a name="b842352706123826"></a>Principal</strong>: object to which the statement applies</li><li><strong id="b842352706123922"><a name="b842352706123922"></a><a name="b842352706123922"></a>NotPrincipal</strong>: object to which the statement does not apply<p id="p716351816"><a name="p716351816"></a><a name="p716351816"></a>There are currently two supported values:</p>
    <a name="ul64637189213"></a><a name="ul64637189213"></a><ul id="ul64637189213"><li><strong id="b842352706103025"><a name="b842352706103025"></a><a name="b842352706103025"></a>CSP</strong>: one or more cloud users</li><li><strong id="b842352706103143"><a name="b842352706103143"></a><a name="b842352706103143"></a>Service</strong>: one or more cloud services</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p44931755164956"><a name="p44931755164956"></a><a name="p44931755164956"></a>Either the <strong id="b842352706185140"><a name="b842352706185140"></a><a name="b842352706185140"></a>Principal</strong> or <strong id="b842352706185145"><a name="b842352706185145"></a><a name="b842352706185145"></a>NotPrincipal</strong> element must be configured.</p>
    <a name="ul866085865315"></a><a name="ul866085865315"></a><ul id="ul866085865315"><li>If you enter <strong id="b842352706185224"><a name="b842352706185224"></a><a name="b842352706185224"></a>CSP</strong>, you must specify user information in the format <strong id="b842352706185337"><a name="b842352706185337"></a><a name="b842352706185337"></a>urn:csp:iam::domainId:root</strong>. You need to obtain the domain ID of each user you specify.</li><li>If you enter <strong id="b842352706185631"><a name="b842352706185631"></a><a name="b842352706185631"></a>Service</strong>, you must specify the cloud service names in lower case.</li></ul>
    </td>
    </tr>
    <tr id="row2239846215551"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p5316167715551"><a name="p5316167715551"></a><a name="p5316167715551"></a>Action</p>
    <p id="p586515126814"><a name="p586515126814"></a><a name="p586515126814"></a>NotAction</p>
    </td>
    <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.2 "><a name="ul139511146291"></a><a name="ul139511146291"></a><ul id="ul139511146291"><li><strong id="b84235270612425"><a name="b84235270612425"></a><a name="b84235270612425"></a>Action</strong>: allowed statement action</li></ul>
    <a name="ul16815171817"></a><a name="ul16815171817"></a><ul id="ul16815171817"><li><strong id="b84235270614829"><a name="b84235270614829"></a><a name="b84235270614829"></a>NotAction</strong>: statement action not allowed<p id="p328452812317"><a name="p328452812317"></a><a name="p328452812317"></a>You can use a wildcard character to configure a set of actions, for example, <strong id="b842352706104048_1"><a name="b842352706104048_1"></a><a name="b842352706104048_1"></a>SMN:Update*</strong> and <strong id="b842352706104054_1"><a name="b842352706104054_1"></a><a name="b842352706104054_1"></a>SMN:Delete*</strong>. If you only enter a wildcard character (*) in a statement, all supported actions are allowed.</p>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p58838218165112"><a name="p58838218165112"></a><a name="p58838218165112"></a>Either the <strong id="b36039682201848"><a name="b36039682201848"></a><a name="b36039682201848"></a>Action</strong> or <strong id="b55921686201848"><a name="b55921686201848"></a><a name="b55921686201848"></a>NotAction</strong> element must be configured.</p>
    <p id="p2900090715551"><a name="p2900090715551"></a><a name="p2900090715551"></a>The following actions are supported:</p>
    <a name="ul5968157515551"></a><a name="ul5968157515551"></a><ul id="ul5968157515551"><li>SMN:UpdateTopic</li><li>SMN:DeleteTopic</li><li>SMN:QueryTopicDetail</li><li>SMN:ListTopicAttributes</li><li>SMN:UpdateTopicAttribute</li><li>SMN:DeleteTopicAttributes</li><li>SMN:DeleteTopicAttributeByName</li><li>SMN:ListSubscriptionsByTopic</li><li>SMN:Subscribe</li><li>SMN:Unsubscribe</li><li>SMN:Publish</li></ul>
    </td>
    </tr>
    <tr id="row3341670315551"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p129519266014"><a name="p129519266014"></a><a name="p129519266014"></a>Resource</p>
    <p id="p840677215551"><a name="p840677215551"></a><a name="p840677215551"></a>NotResource</p>
    </td>
    <td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.2 "><a name="ul72911752161111"></a><a name="ul72911752161111"></a><ul id="ul72911752161111"><li><strong id="b661596660"><a name="b661596660"></a><a name="b661596660"></a>Resource</strong>: topic to which a statement applies</li><li><strong id="b123380417"><a name="b123380417"></a><a name="b123380417"></a>NotResource</strong>: topic to which a statement does not apply</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p14977997165224"><a name="p14977997165224"></a><a name="p14977997165224"></a>Either the <strong id="b842352706194447_5"><a name="b842352706194447_5"></a><a name="b842352706194447_5"></a>Resource</strong> or <strong id="b84235270619452_5"><a name="b84235270619452_5"></a><a name="b84235270619452_5"></a>NotResource</strong> element must be configured.</p>
    <p id="p6045376015551"><a name="p6045376015551"></a><a name="p6045376015551"></a>You need to enter a topic URN.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    PUT https://{SMN_Endpoint}/v2/{project_id}/notifications/topics/{topic_urn}/attributes/access_policy
    ```

    ```
    {
       "value": "{
             \"Version\": \"2016-09-07\", 
             \"Id\": \"__default_policy_ID\", 
             \"Statement\": [
                {
                  \"Sid\": \"__user_pub_0\",
                  \"Effect\": \"Allow\",
                  \"Principal\": {
                    \"CSP\": [
                            \"urn:csp:iam::{domainID}:root\"
                           ]
                     },
                  \"Action\": [\"SMN:Publish\",\"SMN:QueryTopicDetail\"],
                  \"Resource\": \"{topic_urn}\"
                  },
                  {
                  \"Sid\": \"__service_pub_0\", 
                  \"Effect\": \"Allow\",
                  \"Principal\": {
                     \"Service\": [\"obs\"]
                     },
                  \"Action\": [\"SMN:Publish\",\"SMN:QueryTopicDetail\"],
                  \"Resource\": \"{topic_urn}\"
                  }
                 ]
              }"
      }
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You need to replace  **\{project\_id\}**,  **\{domainID\}**, and  **\{topic\_urn\}**  with the actual values.  
    >**domainID**  indicates the user's domain ID. To obtain it, log in to the SMN console, click  **My Credential**  in the username drop-down list on the upper right.  


## Response<a name="section26561495"></a>

-   Parameter description

    <a name="table38552084"></a>
    <table><thead align="left"><tr id="row10058158"><th class="cellrowborder" valign="top" width="30.04%" id="mcps1.1.4.1.1"><p id="p9404449"><a name="p9404449"></a><a name="p9404449"></a><strong id="b553820258"><a name="b553820258"></a><a name="b553820258"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.380000000000003%" id="mcps1.1.4.1.2"><p id="p23562876"><a name="p23562876"></a><a name="p23562876"></a><strong id="b1323124260"><a name="b1323124260"></a><a name="b1323124260"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.58%" id="mcps1.1.4.1.3"><p id="p29544808"><a name="p29544808"></a><a name="p29544808"></a><strong id="b534984603"><a name="b534984603"></a><a name="b534984603"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33089041"><td class="cellrowborder" valign="top" width="30.04%" headers="mcps1.1.4.1.1 "><p id="p62966687"><a name="p62966687"></a><a name="p62966687"></a>request_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.380000000000003%" headers="mcps1.1.4.1.2 "><p id="p27997"><a name="p27997"></a><a name="p27997"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.58%" headers="mcps1.1.4.1.3 "><p id="p2267763"><a name="p2267763"></a><a name="p2267763"></a>Request ID, which is unique</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "request_id":"6837531fd3f54550927b930180a706bf"
    }
    ```


## Returned Value<a name="section37726867"></a>

See  [Returned Value](returned-value.md).

## Error Code<a name="section73211020122511"></a>

See  [Error Code](error-code.md).

