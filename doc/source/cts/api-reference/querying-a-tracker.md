# Querying a Tracker<a name="en-us_topic_0168602253"></a>

## Function<a name="section36020887"></a>

This API is used to query a tracker created on the  **Tracker Information**  page. The detailed information includes the name of the tracker, name of the OBS bucket for storing traces, and prefix of the traces stored in an OBS bucket.

## URI<a name="section55752527"></a>

GET /v1.0/\{project\_id\}/tracker?tracker\_name=\{tracker\_name\}

For details about the parameters, see  [Table1 Parameters in the URI](querying-a-tracker.md).

**Table  1**  Parameters in the URI

<a name="table9404449"></a>
<table><thead align="left"><tr id="row63328883"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p29365919"><a name="p29365919"></a><a name="p29365919"></a><strong id="b842352706114947"><a name="b842352706114947"></a><a name="b842352706114947"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33%" id="mcps1.2.5.1.2"><p id="p29829272"><a name="p29829272"></a><a name="p29829272"></a><strong id="b842352706114949"><a name="b842352706114949"></a><a name="b842352706114949"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p251973"><a name="p251973"></a><a name="p251973"></a><strong id="b842352706114951"><a name="b842352706114951"></a><a name="b842352706114951"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p20409871"><a name="p20409871"></a><a name="p20409871"></a><strong id="b842352706114953"><a name="b842352706114953"></a><a name="b842352706114953"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row42586845"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p26982424"><a name="p26982424"></a><a name="p26982424"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.2 "><p id="p38092711"><a name="p38092711"></a><a name="p38092711"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p65610739"><a name="p65610739"></a><a name="p65610739"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p12869603"><a name="p12869603"></a><a name="p12869603"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row41229856143234"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p4797734143243"><a name="p4797734143243"></a><a name="p4797734143243"></a>tracker_name</p>
</td>
<td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.2 "><p id="p53072175143243"><a name="p53072175143243"></a><a name="p53072175143243"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p3878953143243"><a name="p3878953143243"></a><a name="p3878953143243"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p45759804143243"><a name="p45759804143243"></a><a name="p45759804143243"></a>Specifies the tracker name.</p>
<p id="p9185054143243"><a name="p9185054143243"></a><a name="p9185054143243"></a>If this parameter is not specified, all trackers will be queried.</p>
<p id="p15556623143243"><a name="p15556623143243"></a><a name="p15556623143243"></a>Currently, only tracker "system" is available.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>CTS supports multiple trackers. If the query request  **GET /v1.0/\{project\_id\}/tracker**  does not contain parameter  **tracker\_name**, the response is in array format. Otherwise, the response is in object format.  

## Request<a name="section32010697"></a>

-   Parameters

    None


-   Example request

    ```
    GET /v1.0/{project_id}/tracker?tracker_name=system
    ```


## Response<a name="section19660823"></a>

-   Parameters

    **Table  2**  Parameters in the request

    <a name="table52782726"></a>
    <table><thead align="left"><tr id="row3591713"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="p22493366"><a name="p22493366"></a><a name="p22493366"></a><strong id="a0eb8e97159684639b27d5812ded25b6b"><a name="a0eb8e97159684639b27d5812ded25b6b"></a><a name="a0eb8e97159684639b27d5812ded25b6b"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="p5285226593223"><a name="p5285226593223"></a><a name="p5285226593223"></a><strong id="b528767639"><a name="b528767639"></a><a name="b528767639"></a>Sub-Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.5.1.3"><p id="p10023380"><a name="p10023380"></a><a name="p10023380"></a><strong id="b84235270611502"><a name="b84235270611502"></a><a name="b84235270611502"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31%" id="mcps1.2.5.1.4"><p id="p6587426"><a name="p6587426"></a><a name="p6587426"></a><strong id="b84235270611504"><a name="b84235270611504"></a><a name="b84235270611504"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63819464"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p1994095"><a name="p1994095"></a><a name="p1994095"></a>tracker_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p5317504493223"><a name="p5317504493223"></a><a name="p5317504493223"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.5.1.3 "><p id="p27303998"><a name="p27303998"></a><a name="p27303998"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.4 "><p id="p64140254"><a name="p64140254"></a><a name="p64140254"></a>Specifies the tracker name. Currently, only tracker "system" is available.</p>
    </td>
    </tr>
    <tr id="row40391380"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p50476336"><a name="p50476336"></a><a name="p50476336"></a>bucket_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p1221131293223"><a name="p1221131293223"></a><a name="p1221131293223"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.5.1.3 "><p id="p62051376"><a name="p62051376"></a><a name="p62051376"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.4 "><p id="p1473512202311"><a name="p1473512202311"></a><a name="p1473512202311"></a>Specifies the OBS bucket name. Starts with a digit or letter and contains 3 to 63 characters, including lowercase letters, digits, hyphens (-), and periods (.)</p>
    </td>
    </tr>
    <tr id="row4078883"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p61954093"><a name="p61954093"></a><a name="p61954093"></a>file_prefix_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p4959221293223"><a name="p4959221293223"></a><a name="p4959221293223"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.5.1.3 "><p id="p52225656"><a name="p52225656"></a><a name="p52225656"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.4 "><p id="p2419756"><a name="p2419756"></a><a name="p2419756"></a>Specifies the prefix of a log that needs to be stored in an OBS bucket.</p>
    </td>
    </tr>
    <tr id="row21777804"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p19171695"><a name="p19171695"></a><a name="p19171695"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p5754626593223"><a name="p5754626593223"></a><a name="p5754626593223"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.5.1.3 "><p id="p9403471"><a name="p9403471"></a><a name="p9403471"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.4 "><p id="p23483667"><a name="p23483667"></a><a name="p23483667"></a>Specifies the status of a tracker. The value can be <strong id="b842352706103716"><a name="b842352706103716"></a><a name="b842352706103716"></a>enabled</strong>, <strong id="b842352706103719"><a name="b842352706103719"></a><a name="b842352706103719"></a>disabled</strong>, or <strong id="b842352706103721"><a name="b842352706103721"></a><a name="b842352706103721"></a>error</strong>. If the value is set to <strong id="b200278414910382"><a name="b200278414910382"></a><a name="b200278414910382"></a>error</strong>, the <strong id="b842352706103814"><a name="b842352706103814"></a><a name="b842352706103814"></a>detail</strong> field is required for specifying the source of the error.</p>
    </td>
    </tr>
    <tr id="row10026414"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p6833220"><a name="p6833220"></a><a name="p6833220"></a>detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p3073591193223"><a name="p3073591193223"></a><a name="p3073591193223"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.5.1.3 "><p id="p16619954"><a name="p16619954"></a><a name="p16619954"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.4 "><p id="p51626474103855"><a name="p51626474103855"></a><a name="p51626474103855"></a>Indicates the tracker exception cause. It is only returned in the response when the tracker status becomes abnormal. The value of this parameter can be one of the following:</p>
    <a name="ul24832001185617"></a><a name="ul24832001185617"></a><ul id="ul24832001185617"><li><strong id="b16705287185938"><a name="b16705287185938"></a><a name="b16705287185938"></a>bucketPolicyError</strong></li><li><strong id="b40975921902"><a name="b40975921902"></a><a name="b40975921902"></a>noBucket</strong></li><li><strong id="b44965523185710"><a name="b44965523185710"></a><a name="b44965523185710"></a>arrears</strong></li></ul>
    </td>
    </tr>
    <tr id="row53729006153350"><td class="cellrowborder" rowspan="5" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p102388909339"><a name="p102388909339"></a><a name="p102388909339"></a>smn</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p4247397893255"><a name="p4247397893255"></a><a name="p4247397893255"></a>is_support_smn</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.5.1.3 "><p id="p294253153350"><a name="p294253153350"></a><a name="p294253153350"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.4 "><p id="p23834514153350"><a name="p23834514153350"></a><a name="p23834514153350"></a>Specifies whether SMN is supported.</p>
    </td>
    </tr>
    <tr id="row35796051153350"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2634402393255"><a name="p2634402393255"></a><a name="p2634402393255"></a>topic_id</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p64270030153350"><a name="p64270030153350"></a><a name="p64270030153350"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p38489973153350"><a name="p38489973153350"></a><a name="p38489973153350"></a>Specifies the theme of the SMN service.</p>
    </td>
    </tr>
    <tr id="row48716581153350"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1165833693255"><a name="p1165833693255"></a><a name="p1165833693255"></a>operations</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p868598414443"><a name="p868598414443"></a><a name="p868598414443"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><a name="ul162265981116"></a><a name="ul162265981116"></a><ul id="ul162265981116"><li>Specifies trigger conditions for sending a notification when <strong id="b84235270611587"><a name="b84235270611587"></a><a name="b84235270611587"></a>Typical</strong> is selected. You can select <strong id="b2029003476122223"><a name="b2029003476122223"></a><a name="b2029003476122223"></a>Delete</strong>, <strong id="b1109728545105053"><a name="b1109728545105053"></a><a name="b1109728545105053"></a>Create</strong>, or <strong id="b842352706114716"><a name="b842352706114716"></a><a name="b842352706114716"></a>Login</strong> or at least one of them.</li><li>Specifies trigger conditions for sending a notification when <strong id="b327180733115919"><a name="b327180733115919"></a><a name="b327180733115919"></a>All</strong> is selected. All conditions including <strong id="b802164191115919"><a name="b802164191115919"></a><a name="b802164191115919"></a>Delete</strong>, <strong id="b908340737115919"><a name="b908340737115919"></a><a name="b908340737115919"></a>Create</strong>, <strong id="b1028798214115919"><a name="b1028798214115919"></a><a name="b1028798214115919"></a>Change</strong>, and <strong id="b842352706115953"><a name="b842352706115953"></a><a name="b842352706115953"></a>OpenStack API Event</strong> are selected by default. Modification is not allowed.</li></ul>
    </td>
    </tr>
    <tr id="row27214492144317"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p4321042393255"><a name="p4321042393255"></a><a name="p4321042393255"></a>is_send_all_key_operation</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p4803191214443"><a name="p4803191214443"></a><a name="p4803191214443"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p6537969214443"><a name="p6537969214443"></a><a name="p6537969214443"></a>You can select <strong id="b8423527069510"><a name="b8423527069510"></a><a name="b8423527069510"></a>Typical</strong> or <strong id="b8423527069513"><a name="b8423527069513"></a><a name="b8423527069513"></a>All</strong> for <strong id="b84235270695239"><a name="b84235270695239"></a><a name="b84235270695239"></a>Trigger Condition</strong>.</p>
    <a name="ul5154632014443"></a><a name="ul5154632014443"></a><ul id="ul5154632014443"><li>When the value is <strong id="b8423527069532"><a name="b8423527069532"></a><a name="b8423527069532"></a>false</strong>, <strong id="b84235270695350"><a name="b84235270695350"></a><a name="b84235270695350"></a>operations</strong> cannot be left empty.</li><li>When the value is <strong id="b84235270695415"><a name="b84235270695415"></a><a name="b84235270695415"></a>true</strong>, <strong id="b54327349095423"><a name="b54327349095423"></a><a name="b54327349095423"></a>operations</strong> is not supported.</li></ul>
    </td>
    </tr>
    <tr id="row60228229104441"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2634125493255"><a name="p2634125493255"></a><a name="p2634125493255"></a>need_notify_user_list</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p26562119104443"><a name="p26562119104443"></a><a name="p26562119104443"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p4086784985653"><a name="p4086784985653"></a><a name="p4086784985653"></a>In <strong id="b842352706161739"><a name="b842352706161739"></a><a name="b842352706161739"></a>Typical</strong> scenario, you can specify the users using the login function. When these users log in, notifications will be sent.</p>
    <a name="ul54166538900"></a><a name="ul54166538900"></a><ul id="ul54166538900"><li>After this function is enabled, the value is the list of the specified users. Separate them with a comma (,). A maximum of 50 users is supported.</li><li>If the value is null, the target objects are all users by default.</li></ul>
    </td>
    </tr>
    <tr id="row155771347164415"><td class="cellrowborder" rowspan="3" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p1777165534417"><a name="p1777165534417"></a><a name="p1777165534417"></a></p>
    <p id="p55601316434"><a name="p55601316434"></a><a name="p55601316434"></a>lts</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p14509743104218"><a name="p14509743104218"></a><a name="p14509743104218"></a>is_lts_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.5.1.3 "><p id="p1856113320439"><a name="p1856113320439"></a><a name="p1856113320439"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.4 "><p id="p95090437427"><a name="p95090437427"></a><a name="p95090437427"></a>Specifies whether to enable the log branch function.</p>
    </td>
    </tr>
    <tr id="row127417505441"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p12518174934217"><a name="p12518174934217"></a><a name="p12518174934217"></a>log_group_name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p1674150124417"><a name="p1674150124417"></a><a name="p1674150124417"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p16762144134414"><a name="p16762144134414"></a><a name="p16762144134414"></a>Name of the LTS log group.</p>
    </td>
    </tr>
    <tr id="row1811320523443"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1856110317430"><a name="p1856110317430"></a><a name="p1856110317430"></a>log_topic_name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p057010479435"><a name="p057010479435"></a><a name="p057010479435"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p165611032431"><a name="p165611032431"></a><a name="p165611032431"></a>Name of the LTS log stream.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
    	"bucket_name" : "my_created_bucket",
    	"tracker_name" : "system",
    	"detail" : "noBucket",
    	"file_prefix_name" : "some_folder",
    	"status" : "disabled",
    	"smn" : {
    		"is_support_smn" : false,
    		"topic_id" : "urn:smn:regionId:328c0a60cba6444ead0579aa0c244f04:cts-test",
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


## Returned Value<a name="section42729680"></a>

-   Normal

    **Table  3**  Return code for successful requests

    <a name="table6647531"></a>
    <table><thead align="left"><tr id="row10320902"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p30686701"><a name="p30686701"></a><a name="p30686701"></a><strong id="b842352706115013"><a name="b842352706115013"></a><a name="b842352706115013"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p2594873"><a name="p2594873"></a><a name="p2594873"></a><strong id="b842352706115016"><a name="b842352706115016"></a><a name="b842352706115016"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8858194"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p46425119"><a name="p46425119"></a><a name="p46425119"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p2338313"><a name="p2338313"></a><a name="p2338313"></a>The request is successful and the query result is returned.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    **Table  4**  Return code for failed requests

    <a name="table55185655"></a>
    <table><thead align="left"><tr id="row52664332"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p37952469"><a name="p37952469"></a><a name="p37952469"></a><strong id="b842352706115021"><a name="b842352706115021"></a><a name="b842352706115021"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p54251110"><a name="p54251110"></a><a name="p54251110"></a><strong id="b842352706114414"><a name="b842352706114414"></a><a name="b842352706114414"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17196062143218"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p18626238143219"><a name="p18626238143219"></a><a name="p18626238143219"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p32330300143219"><a name="p32330300143219"></a><a name="p32330300143219"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row32263784"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p63229698"><a name="p63229698"></a><a name="p63229698"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p21331933"><a name="p21331933"></a><a name="p21331933"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row17231827102823"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p30719169102843"><a name="p30719169102843"></a><a name="p30719169102843"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p5224799102843"><a name="p5224799102843"></a><a name="p5224799102843"></a>Your access request is rejected.</p>
    </td>
    </tr>
    <tr id="row6592212102831"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p50782544102843"><a name="p50782544102843"></a><a name="p50782544102843"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p13237565202942"><a name="p13237565202942"></a><a name="p13237565202942"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    </tbody>
    </table>


