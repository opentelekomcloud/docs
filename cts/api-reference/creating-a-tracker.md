# Creating a Tracker<a name="en-us_topic_0168602251"></a>

All API URLs described in this section are case-sensitive.

## Function<a name="section14842765"></a>

This API is used to create a tracker.

A tracker will be automatically created after CTS is enabled. All traces recorded by CTS are associated with the tracker. Currently, only one management tracker is created for each account in a region.

On the management console, you can query the last seven days of operation records. To obtain more operation records, you can enable Object Storage Service \(OBS\) and deliver operation records to OBS buckets for long-term storage in real time.

Configuring  **Key Event Notification**: You can select whether to send an email, a text message, or an HTTP/HTTPS notification in the event of a key operation. This function is triggered by CTS, but notifications are sent by Simple Message Notification \(SMN\). Therefore, you need to enable SMN and create a notification topic before enabling this configuration item. You can select  **Typical**  or  **All**  based on actual requirements:

-   **Typical**: CTS is suitable for routine audit of enterprises. Currently, CTS can enable text notifications pertaining to key operations such as logging in to IAM or creating or deleting core resources of ECS, VPC, EVS, or KMS.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Because IAM is a global service, the  **Login**  function is only provided for the central region of the current site. After this function is enabled, notifications will be sent upon the login of any region.  

-   **All**: CTS is suitable for interconnecting with your own audit system. It can enable text notifications through SMN for operations of creating, deleting, or changing resources of ECS, IMS, EVS, CSBS, VBS, VPC, DNS, ELB, IAM, KMS, RDS, DDS, SFS, or DMS, or relevant operations triggered by invoking IaaS OpenStack APIs. In  **All**  scenario, you cannot modify any settings, and CTS sends text notifications for all traces sent from interconnected services by default. You are advised to use an SMN topic for which HTTPS is selected.

## URI<a name="section66476022"></a>

POST /v1.0/\{project\_id\}/tracker

For details about the parameters, see  [Table1 Parameters in the URI](creating-a-tracker.md).

**Table  1**  Parameters in the URI

<a name="table6296289"></a>
<table><thead align="left"><tr id="row54465313"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p49614245"><a name="p49614245"></a><a name="p49614245"></a><strong id="b842352706114737"><a name="b842352706114737"></a><a name="b842352706114737"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.82%" id="mcps1.2.5.1.2"><p id="p59330872"><a name="p59330872"></a><a name="p59330872"></a><strong id="b842352706114741"><a name="b842352706114741"></a><a name="b842352706114741"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="22.18%" id="mcps1.2.5.1.3"><p id="p41071365"><a name="p41071365"></a><a name="p41071365"></a><strong id="b842352706114743"><a name="b842352706114743"></a><a name="b842352706114743"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p38446258"><a name="p38446258"></a><a name="p38446258"></a><strong id="b842352706114745"><a name="b842352706114745"></a><a name="b842352706114745"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row27139175"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p50789581"><a name="p50789581"></a><a name="p50789581"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="27.82%" headers="mcps1.2.5.1.2 "><p id="p20315403"><a name="p20315403"></a><a name="p20315403"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.5.1.3 "><p id="p34934986"><a name="p34934986"></a><a name="p34934986"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p11161650"><a name="p11161650"></a><a name="p11161650"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section61413291"></a>

-   Parameters

    **Table  2**  Parameters in the request

    <a name="table15816986"></a>
    <table><thead align="left"><tr id="row65812741"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.6.1.1"><p id="p29231803"><a name="p29231803"></a><a name="p29231803"></a><strong id="a0eb8e97159684639b27d5812ded25b6b"><a name="a0eb8e97159684639b27d5812ded25b6b"></a><a name="a0eb8e97159684639b27d5812ded25b6b"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22%" id="mcps1.2.6.1.2"><p id="p459281181615"><a name="p459281181615"></a><a name="p459281181615"></a><strong id="b1264755526"><a name="b1264755526"></a><a name="b1264755526"></a>Sub-Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.6.1.3"><p id="p18965813"><a name="p18965813"></a><a name="p18965813"></a><strong id="b1874127586"><a name="b1874127586"></a><a name="b1874127586"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="9%" id="mcps1.2.6.1.4"><p id="p59835867"><a name="p59835867"></a><a name="p59835867"></a><strong id="b1726796345"><a name="b1726796345"></a><a name="b1726796345"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37%" id="mcps1.2.6.1.5"><p id="p14867095"><a name="p14867095"></a><a name="p14867095"></a><strong id="b842352706114757"><a name="b842352706114757"></a><a name="b842352706114757"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63384014"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.1 "><p id="p33831530"><a name="p33831530"></a><a name="p33831530"></a>bucket_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p37201838181615"><a name="p37201838181615"></a><a name="p37201838181615"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.3 "><p id="p55999443"><a name="p55999443"></a><a name="p55999443"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.4 "><p id="p39661040"><a name="p39661040"></a><a name="p39661040"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.6.1.5 "><p id="p1410743531413"><a name="p1410743531413"></a><a name="p1410743531413"></a>Specifies the OBS bucket name. Starts with a digit or letter and contains 3 to 63 characters, including lowercase letters, digits, hyphens (-), and periods (.)</p>
    </td>
    </tr>
    <tr id="row56087165"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.1 "><p id="p46766508"><a name="p46766508"></a><a name="p46766508"></a>file_prefix_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p60558891181615"><a name="p60558891181615"></a><a name="p60558891181615"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.3 "><p id="p29990828"><a name="p29990828"></a><a name="p29990828"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.4 "><p id="p13338021"><a name="p13338021"></a><a name="p13338021"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.6.1.5 "><p id="p6637886"><a name="p6637886"></a><a name="p6637886"></a>Specifies the prefix of a log that needs to be stored in an OBS bucket. The value is a string of 0 to 64 characters and can contain uppercase and lowercase letters (a to z and A to Z), digits (0 to 9), hyphens (-), underscores (_), or periods (.)</p>
    </td>
    </tr>
    <tr id="row21188616101630"><td class="cellrowborder" rowspan="5" valign="top" width="16%" headers="mcps1.2.6.1.1 "><p id="p12680669181856"><a name="p12680669181856"></a><a name="p12680669181856"></a>smn</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p3814879618181"><a name="p3814879618181"></a><a name="p3814879618181"></a>is_support_smn</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.3 "><p id="p1147593101641"><a name="p1147593101641"></a><a name="p1147593101641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.4 "><p id="p25846240101641"><a name="p25846240101641"></a><a name="p25846240101641"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.6.1.5 "><p id="p13170658101641"><a name="p13170658101641"></a><a name="p13170658101641"></a>Specifies whether SMN is supported. When the value is <strong id="b84235270684317"><a name="b84235270684317"></a><a name="b84235270684317"></a>false,</strong> <strong id="b84235270684343"><a name="b84235270684343"></a><a name="b84235270684343"></a>topic_id</strong> and <strong id="b84235270684346"><a name="b84235270684346"></a><a name="b84235270684346"></a>operations</strong> can be left empty.</p>
    </td>
    </tr>
    <tr id="row25954114101630"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p2740280518181"><a name="p2740280518181"></a><a name="p2740280518181"></a>topic_id</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p56708921101641"><a name="p56708921101641"></a><a name="p56708921101641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p30019890101641"><a name="p30019890101641"></a><a name="p30019890101641"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p15692060101641"><a name="p15692060101641"></a><a name="p15692060101641"></a><strong id="b51351969115236"><a name="b51351969115236"></a><a name="b51351969115236"></a>topic_id </strong>is obtained from SMN and in the format of urn:smn:([a-z]|[A-Z]|[0-9]|\-){1,32}:([a-z]|[A-Z]|[0-9]){32}:([a-z]|[A-Z]|[0-9]|\-|\_){1,256}.</p>
    </td>
    </tr>
    <tr id="row36167981101630"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p4531285318181"><a name="p4531285318181"></a><a name="p4531285318181"></a>operations</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p28414707101641"><a name="p28414707101641"></a><a name="p28414707101641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p19889913101641"><a name="p19889913101641"></a><a name="p19889913101641"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><a name="ul162265981116"></a><a name="ul162265981116"></a><ul id="ul162265981116"><li>Specifies trigger conditions for sending a notification when <strong id="b84235270611587"><a name="b84235270611587"></a><a name="b84235270611587"></a>Typical</strong> is selected. You can select <strong id="b2029003476122223"><a name="b2029003476122223"></a><a name="b2029003476122223"></a>delete</strong>, <strong id="b1109728545105053"><a name="b1109728545105053"></a><a name="b1109728545105053"></a>create</strong>, or <strong id="b842352706114716"><a name="b842352706114716"></a><a name="b842352706114716"></a>login</strong> or at least one of them.</li><li>Specifies trigger conditions for sending a notification when <strong id="b327180733115919"><a name="b327180733115919"></a><a name="b327180733115919"></a>All</strong> is selected. All conditions including <strong id="b802164191115919"><a name="b802164191115919"></a><a name="b802164191115919"></a>delete</strong>, <strong id="b908340737115919"><a name="b908340737115919"></a><a name="b908340737115919"></a>create</strong>, <strong id="b1028798214115919"><a name="b1028798214115919"></a><a name="b1028798214115919"></a>change</strong>, and <strong id="b842352706115953"><a name="b842352706115953"></a><a name="b842352706115953"></a>OpenStack API Event</strong> are selected by default. Modification is not allowed.</li></ul>
    </td>
    </tr>
    <tr id="row5504566711366"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1550912618181"><a name="p1550912618181"></a><a name="p1550912618181"></a>is_send_all_key_operation</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p4182555311366"><a name="p4182555311366"></a><a name="p4182555311366"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p3242663711366"><a name="p3242663711366"></a><a name="p3242663711366"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p26362576113742"><a name="p26362576113742"></a><a name="p26362576113742"></a>You can select <strong id="b8423527069510"><a name="b8423527069510"></a><a name="b8423527069510"></a>Typical</strong> or <strong id="b8423527069513"><a name="b8423527069513"></a><a name="b8423527069513"></a>All</strong> for <strong id="b84235270695239"><a name="b84235270695239"></a><a name="b84235270695239"></a>Trigger Condition</strong>.</p>
    <a name="ul6703206511386"></a><a name="ul6703206511386"></a><ul id="ul6703206511386"><li>When the value is <strong id="b8423527069532"><a name="b8423527069532"></a><a name="b8423527069532"></a>false</strong>, <strong id="b84235270695350"><a name="b84235270695350"></a><a name="b84235270695350"></a>operations</strong> cannot be left empty.</li><li>When the value is <strong id="b84235270695415"><a name="b84235270695415"></a><a name="b84235270695415"></a>true</strong>, <strong id="b54327349095423"><a name="b54327349095423"></a><a name="b54327349095423"></a>operations</strong> is not supported.</li></ul>
    </td>
    </tr>
    <tr id="row6120793616567"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p3186393118181"><a name="p3186393118181"></a><a name="p3186393118181"></a>need_notify_user_list</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p582644516567"><a name="p582644516567"></a><a name="p582644516567"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p218002816567"><a name="p218002816567"></a><a name="p218002816567"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p4086784985653"><a name="p4086784985653"></a><a name="p4086784985653"></a>In <strong id="b842352706161739"><a name="b842352706161739"></a><a name="b842352706161739"></a>Typical</strong> scenario, you can specify the users using the login function. When these users log in, notifications will be sent.</p>
    <a name="ul54166538900"></a><a name="ul54166538900"></a><ul id="ul54166538900"><li>After this function is enabled, the value is the list of the specified users. Separate them with a comma (,). A maximum of 50 users is supported.</li><li>If the value is null, the target objects are all users by default.</li></ul>
    </td>
    </tr>
    <tr id="row1417912302422"><td class="cellrowborder" rowspan="3" valign="top" width="16%" headers="mcps1.2.6.1.1 "><p id="p181791230204217"><a name="p181791230204217"></a><a name="p181791230204217"></a>lts</p>
    </td>
    <td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.6.1.2 "><p id="p15179133012421"><a name="p15179133012421"></a><a name="p15179133012421"></a>is_lts_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.6.1.3 "><p id="p21804304422"><a name="p21804304422"></a><a name="p21804304422"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.4 "><p id="p151806302427"><a name="p151806302427"></a><a name="p151806302427"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.6.1.5 "><p id="p635574111276"><a name="p635574111276"></a><a name="p635574111276"></a>Specifies whether to enable the log branch function. When the value is <strong id="b1758501195610"><a name="b1758501195610"></a><a name="b1758501195610"></a>false</strong>, <strong id="b474810314565"><a name="b474810314565"></a><a name="b474810314565"></a>log_group_name</strong> and <strong id="b1717903725615"><a name="b1717903725615"></a><a name="b1717903725615"></a>log_topic_name</strong> can be left empty.</p>
    </td>
    </tr>
    <tr id="row58984934316"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1899159114320"><a name="p1899159114320"></a><a name="p1899159114320"></a>log_group_name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p98991891435"><a name="p98991891435"></a><a name="p98991891435"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p95343249398"><a name="p95343249398"></a><a name="p95343249398"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p98992092430"><a name="p98992092430"></a><a name="p98992092430"></a>Name of the LTS log group.</p>
    </td>
    </tr>
    <tr id="row1147229124318"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p10147112911436"><a name="p10147112911436"></a><a name="p10147112911436"></a>log_topic_name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p5147729144314"><a name="p5147729144314"></a><a name="p5147729144314"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p8147162904313"><a name="p8147162904313"></a><a name="p8147162904313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p16147192919436"><a name="p16147192919436"></a><a name="p16147192919436"></a>Name of the LTS log topic.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
    	"bucket_name" : "obs-f1da",
    	"file_prefix_name" : "yO8Q",
    	"smn" : {
    		"is_support_smn" : true,
    		"topic_id" : "urn:smn:regionId:ea79855fbe0642718cb4df1551c3cb4e:hh",
    		"is_send_all_key_operation" : false,
    		"operations" : ["delete", "create", "login"],
    		"need_notify_user_list" : ["user1", "user2"]
    	},
    	"lts" : {
    		"is_lts_enabled" : true,
    		"log_group_name" : "CTS",
    		"log_topic_name" : "tracker"
    	}
    }
    ```


## Response<a name="section15848707"></a>

-   Parameters

    **Table  3**  Parameters in the response

    <a name="table53933741"></a>
    <table><thead align="left"><tr id="row3099778"><th class="cellrowborder" valign="top" width="24.437556244375564%" id="mcps1.2.5.1.1"><p id="p37202254154847"><a name="p37202254154847"></a><a name="p37202254154847"></a><strong id="b1895435744"><a name="b1895435744"></a><a name="b1895435744"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.23787621237876%" id="mcps1.2.5.1.2"><p id="p38918254154852"><a name="p38918254154852"></a><a name="p38918254154852"></a><strong id="b2138027594"><a name="b2138027594"></a><a name="b2138027594"></a>Sub-Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.497650234976504%" id="mcps1.2.5.1.3"><p id="p3658088"><a name="p3658088"></a><a name="p3658088"></a><strong id="b84235270611488"><a name="b84235270611488"></a><a name="b84235270611488"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.826917308269174%" id="mcps1.2.5.1.4"><p id="p27869743"><a name="p27869743"></a><a name="p27869743"></a><strong id="b260329288"><a name="b260329288"></a><a name="b260329288"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42856673"><td class="cellrowborder" valign="top" width="24.437556244375564%" headers="mcps1.2.5.1.1 "><p id="p48838504"><a name="p48838504"></a><a name="p48838504"></a>bucket_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.23787621237876%" headers="mcps1.2.5.1.2 "><p id="p504861008422"><a name="p504861008422"></a><a name="p504861008422"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.497650234976504%" headers="mcps1.2.5.1.3 "><p id="p63604780"><a name="p63604780"></a><a name="p63604780"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p1473512202311"><a name="p1473512202311"></a><a name="p1473512202311"></a>Specifies the OBS bucket name. Starts with a digit or letter and contains 3 to 63 characters, including lowercase letters, digits, hyphens (-), and periods (.)</p>
    </td>
    </tr>
    <tr id="row62768825"><td class="cellrowborder" valign="top" width="24.437556244375564%" headers="mcps1.2.5.1.1 "><p id="p51110099"><a name="p51110099"></a><a name="p51110099"></a>file_prefix_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.23787621237876%" headers="mcps1.2.5.1.2 "><p id="p628422998422"><a name="p628422998422"></a><a name="p628422998422"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.497650234976504%" headers="mcps1.2.5.1.3 "><p id="p46277382"><a name="p46277382"></a><a name="p46277382"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p57480441"><a name="p57480441"></a><a name="p57480441"></a>Specifies the prefix of a log that needs to be stored in an OBS bucket.</p>
    </td>
    </tr>
    <tr id="row47561922"><td class="cellrowborder" valign="top" width="24.437556244375564%" headers="mcps1.2.5.1.1 "><p id="p27310456"><a name="p27310456"></a><a name="p27310456"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.23787621237876%" headers="mcps1.2.5.1.2 "><p id="p570614508422"><a name="p570614508422"></a><a name="p570614508422"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.497650234976504%" headers="mcps1.2.5.1.3 "><p id="p64663364"><a name="p64663364"></a><a name="p64663364"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p3241099"><a name="p3241099"></a><a name="p3241099"></a>Specifies the status of a tracker. The value is <strong id="b8423527061008"><a name="b8423527061008"></a><a name="b8423527061008"></a>enabled</strong>.</p>
    </td>
    </tr>
    <tr id="row29169897"><td class="cellrowborder" valign="top" width="24.437556244375564%" headers="mcps1.2.5.1.1 "><p id="p13951479"><a name="p13951479"></a><a name="p13951479"></a>tracker_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.23787621237876%" headers="mcps1.2.5.1.2 "><p id="p585747628422"><a name="p585747628422"></a><a name="p585747628422"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.497650234976504%" headers="mcps1.2.5.1.3 "><p id="p56327989"><a name="p56327989"></a><a name="p56327989"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p66273227"><a name="p66273227"></a><a name="p66273227"></a>Specifies the tracker name. Currently, only tracker "system" is available.</p>
    </td>
    </tr>
    <tr id="row34624248103044"><td class="cellrowborder" rowspan="5" valign="top" width="24.437556244375564%" headers="mcps1.2.5.1.1 "><p id="p4096430584254"><a name="p4096430584254"></a><a name="p4096430584254"></a>smn</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.23787621237876%" headers="mcps1.2.5.1.2 "><p id="p5647525784230"><a name="p5647525784230"></a><a name="p5647525784230"></a>is_support_smn</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.497650234976504%" headers="mcps1.2.5.1.3 "><p id="p15338755103056"><a name="p15338755103056"></a><a name="p15338755103056"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p34479652103056"><a name="p34479652103056"></a><a name="p34479652103056"></a>Specifies whether SMN is supported.</p>
    </td>
    </tr>
    <tr id="row26888450103048"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p3272895084230"><a name="p3272895084230"></a><a name="p3272895084230"></a>topic_id</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p40285478103056"><a name="p40285478103056"></a><a name="p40285478103056"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p41898284103056"><a name="p41898284103056"></a><a name="p41898284103056"></a>Specifies the theme of the SMN service.</p>
    </td>
    </tr>
    <tr id="row31139407103048"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p3575800284230"><a name="p3575800284230"></a><a name="p3575800284230"></a>operations</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p43467708141740"><a name="p43467708141740"></a><a name="p43467708141740"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><a name="ul1680596111628"></a><a name="ul1680596111628"></a><ul id="ul1680596111628"><li>Specifies trigger conditions for sending a notification when <strong id="b1218310541"><a name="b1218310541"></a><a name="b1218310541"></a>Typical</strong> is selected. You can select <strong id="b635627774"><a name="b635627774"></a><a name="b635627774"></a>delete</strong>, <strong id="b316836776"><a name="b316836776"></a><a name="b316836776"></a>create</strong>, or <strong id="b1177726463"><a name="b1177726463"></a><a name="b1177726463"></a>login</strong> or at least one of them.</li><li>Specifies trigger conditions for sending a notification when <strong id="b300251051"><a name="b300251051"></a><a name="b300251051"></a>All</strong> is selected. All conditions including <strong id="b1118899929"><a name="b1118899929"></a><a name="b1118899929"></a>delete</strong>, <strong id="b886863853"><a name="b886863853"></a><a name="b886863853"></a>create</strong>, <strong id="b281665585"><a name="b281665585"></a><a name="b281665585"></a>change</strong>, and <strong id="b1661893291"><a name="b1661893291"></a><a name="b1661893291"></a>OpenStack API Event</strong> are selected by default. Modification is not allowed.</li></ul>
    </td>
    </tr>
    <tr id="row56359866141135"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2934443284230"><a name="p2934443284230"></a><a name="p2934443284230"></a>is_send_all_key_operation</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p4692287141740"><a name="p4692287141740"></a><a name="p4692287141740"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p50237768141740"><a name="p50237768141740"></a><a name="p50237768141740"></a>You can select <strong id="b2024965562"><a name="b2024965562"></a><a name="b2024965562"></a>Typical</strong> or <strong id="b1274026880"><a name="b1274026880"></a><a name="b1274026880"></a>All</strong> for <strong id="b1604322855"><a name="b1604322855"></a><a name="b1604322855"></a>Trigger Condition</strong>.</p>
    <a name="ul49486729141740"></a><a name="ul49486729141740"></a><ul id="ul49486729141740"><li>When the value is <strong id="b349158385"><a name="b349158385"></a><a name="b349158385"></a>false</strong>, <strong id="b1031940128"><a name="b1031940128"></a><a name="b1031940128"></a>operations</strong> cannot be left empty.</li><li>When the value is <strong id="b919240022"><a name="b919240022"></a><a name="b919240022"></a>true</strong>, <strong id="b1696461348"><a name="b1696461348"></a><a name="b1696461348"></a>operations</strong> is not supported.</li></ul>
    </td>
    </tr>
    <tr id="row88099699246"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p170344368422"><a name="p170344368422"></a><a name="p170344368422"></a>need_notify_user_list</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p3781643991054"><a name="p3781643991054"></a><a name="p3781643991054"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p28427054172322"><a name="p28427054172322"></a><a name="p28427054172322"></a>In <strong id="b1373042124"><a name="b1373042124"></a><a name="b1373042124"></a>Typical</strong> scenario, you can specify the users using the login function. When these users log in, notifications will be sent.</p>
    <a name="ul54516899172322"></a><a name="ul54516899172322"></a><ul id="ul54516899172322"><li>After this function is enabled, the value is the list of the specified users. Separate them with a comma (,). A maximum of 50 users is supported.</li><li>If the value is null, the target objects are all users by default.</li></ul>
    </td>
    </tr>
    <tr id="row15707182812361"><td class="cellrowborder" rowspan="3" valign="top" width="24.437556244375564%" headers="mcps1.2.5.1.1 "><p id="p207471246153612"><a name="p207471246153612"></a><a name="p207471246153612"></a>lts</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.23787621237876%" headers="mcps1.2.5.1.2 "><p id="p137473468369"><a name="p137473468369"></a><a name="p137473468369"></a>is_lts_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.497650234976504%" headers="mcps1.2.5.1.3 "><p id="p12747164683613"><a name="p12747164683613"></a><a name="p12747164683613"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p137471946123617"><a name="p137471946123617"></a><a name="p137471946123617"></a>Specifies whether to enable the log branch function. When the value is <strong id="b1392011107593"><a name="b1392011107593"></a><a name="b1392011107593"></a>false</strong>, <strong id="b592201015918"><a name="b592201015918"></a><a name="b592201015918"></a>log_group_name</strong> and <strong id="b19922171020596"><a name="b19922171020596"></a><a name="b19922171020596"></a>log_topic_name</strong> can be left empty.</p>
    </td>
    </tr>
    <tr id="row10459153593620"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p674734643620"><a name="p674734643620"></a><a name="p674734643620"></a>log_group_name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p147472469367"><a name="p147472469367"></a><a name="p147472469367"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p67471546153614"><a name="p67471546153614"></a><a name="p67471546153614"></a>Name of the LTS log group.</p>
    </td>
    </tr>
    <tr id="row575383817366"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p274834673612"><a name="p274834673612"></a><a name="p274834673612"></a>log_topic_name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p1474813465364"><a name="p1474813465364"></a><a name="p1474813465364"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p8748846103619"><a name="p8748846103619"></a><a name="p8748846103619"></a>Name of the LTS log topic.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
    	"bucket_name" : "obs-f1da",
    	"file_prefix_name" : "yO8Q",
    	"smn" : {
    		"is_support_smn" : true,
    		"topic_id" : "urn:smn:regionId:ea79855fbe0642718cb4df1551c3cb4e:hh",
    		"is_send_all_key_operation" : false,
    		"operations" : ["delete", "create", "login"],
    		"need_notify_user_list" : ["user1", "user2"]
    	},
    	"lts" : {
    		"is_lts_enabled" : true,
    		"log_group_name" : "CTS",
    		"log_topic_name" : "tracker"
    	}
    }
    ```


## Returned Value<a name="section8420641"></a>

-   Normal

    **Table  4**  Return code for successful requests

    <a name="table60176744"></a>
    <table><thead align="left"><tr id="row29373839"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p30470722"><a name="p30470722"></a><a name="p30470722"></a><strong id="b842352706114836"><a name="b842352706114836"></a><a name="b842352706114836"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p52209455"><a name="p52209455"></a><a name="p52209455"></a><strong id="b842352706114839"><a name="b842352706114839"></a><a name="b842352706114839"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1107452"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p22594769"><a name="p22594769"></a><a name="p22594769"></a>201</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p18237015"><a name="p18237015"></a><a name="p18237015"></a>The request is successfully processed.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    **Table  5**  Return code for failed requests

    <a name="table803253"></a>
    <table><thead align="left"><tr id="row52486654"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p23560597"><a name="p23560597"></a><a name="p23560597"></a><strong id="b842352706114843"><a name="b842352706114843"></a><a name="b842352706114843"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p29360233"><a name="p29360233"></a><a name="p29360233"></a><strong id="b842352706114845"><a name="b842352706114845"></a><a name="b842352706114845"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29368673"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p30052326"><a name="p30052326"></a><a name="p30052326"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p18319327"><a name="p18319327"></a><a name="p18319327"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row30656219"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p125790"><a name="p125790"></a><a name="p125790"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p10189001"><a name="p10189001"></a><a name="p10189001"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row24592149"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p45807089"><a name="p45807089"></a><a name="p45807089"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p19386696"><a name="p19386696"></a><a name="p19386696"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row15217222102323"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p24897581102326"><a name="p24897581102326"></a><a name="p24897581102326"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p64583667202827"><a name="p64583667202827"></a><a name="p64583667202827"></a>Your access request is rejected.</p>
    </td>
    </tr>
    <tr id="row6941675111321"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p25404772111321"><a name="p25404772111321"></a><a name="p25404772111321"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p26590306112511"><a name="p26590306112511"></a><a name="p26590306112511"></a>The requested OBS bucket does not exist.</p>
    </td>
    </tr>
    </tbody>
    </table>


