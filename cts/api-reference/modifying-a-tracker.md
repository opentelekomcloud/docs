# Modifying a Tracker<a name="en-us_topic_0168602227"></a>

## Function<a name="section14797678"></a>

Configuration items of the tracker can be modified, including Trace Transfer to OBS, Key Event Notification, Encrypt Trace File, Retrieve Management Traces Using LTS, and Verify Trace File and parameters for enabling and disabling a tracker. Modifying the tracker does not affect the existing operation records. After the modification is complete, the system will immediately start recording operations based on the new rule.

## URI<a name="section66070243"></a>

PUT /v1.0/\{project\_id\}/tracker/\{tracker\_name\}

For details about the parameters, see  [Table1 Parameters in the URI](modifying-a-tracker.md).

**Table  1**  Parameters in the URI

<a name="table25483595"></a>
<table><thead align="left"><tr id="row32913796"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.5.1.1"><p id="p48771786"><a name="p48771786"></a><a name="p48771786"></a><strong id="b842352706114257"><a name="b842352706114257"></a><a name="b842352706114257"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.5.1.2"><p id="p58200593"><a name="p58200593"></a><a name="p58200593"></a><strong id="b84235270611430"><a name="b84235270611430"></a><a name="b84235270611430"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p16627584"><a name="p16627584"></a><a name="p16627584"></a><strong id="b84235270611434"><a name="b84235270611434"></a><a name="b84235270611434"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p4657088"><a name="p4657088"></a><a name="p4657088"></a><strong id="b84235270611437"><a name="b84235270611437"></a><a name="b84235270611437"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row41679865"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.5.1.1 "><p id="p20625874"><a name="p20625874"></a><a name="p20625874"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.2 "><p id="p60083059"><a name="p60083059"></a><a name="p60083059"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p34889605"><a name="p34889605"></a><a name="p34889605"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p7485743"><a name="p7485743"></a><a name="p7485743"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row54714902142926"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.5.1.1 "><p id="p41581713142932"><a name="p41581713142932"></a><a name="p41581713142932"></a>tracker_name</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.2 "><p id="p12675603142932"><a name="p12675603142932"></a><a name="p12675603142932"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p20090946142932"><a name="p20090946142932"></a><a name="p20090946142932"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p16753925142932"><a name="p16753925142932"></a><a name="p16753925142932"></a>Specifies the name of a tracker. Currently, only tracker "system" is available.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section57761279"></a>

-   Parameters

    **Table  2**  Parameters in the request

    <a name="table65557227153241"></a>
    <table><thead align="left"><tr id="row6305742153241"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.6.1.1"><p id="p41003092153241"><a name="p41003092153241"></a><a name="p41003092153241"></a><strong id="a0eb8e97159684639b27d5812ded25b6b"><a name="a0eb8e97159684639b27d5812ded25b6b"></a><a name="a0eb8e97159684639b27d5812ded25b6b"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.6.1.2"><p id="p5354930192235"><a name="p5354930192235"></a><a name="p5354930192235"></a><strong id="b842352706154949"><a name="b842352706154949"></a><a name="b842352706154949"></a>Sub-Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.6.1.3"><p id="p32916126153241"><a name="p32916126153241"></a><a name="p32916126153241"></a><strong id="b84235270611430_1"><a name="b84235270611430_1"></a><a name="b84235270611430_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.2.6.1.4"><p id="p48960532153241"><a name="p48960532153241"></a><a name="p48960532153241"></a><strong id="b84235270611434_1"><a name="b84235270611434_1"></a><a name="b84235270611434_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.3939393939394%" id="mcps1.2.6.1.5"><p id="p6380192153241"><a name="p6380192153241"></a><a name="p6380192153241"></a><strong id="b842352706114321"><a name="b842352706114321"></a><a name="b842352706114321"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row47033511153241"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.1 "><p id="p51618067153241"><a name="p51618067153241"></a><a name="p51618067153241"></a>bucket_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.6.1.2 "><p id="p4252611892235"><a name="p4252611892235"></a><a name="p4252611892235"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.3 "><p id="p20313932153241"><a name="p20313932153241"></a><a name="p20313932153241"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.6.1.4 "><p id="p34815801153241"><a name="p34815801153241"></a><a name="p34815801153241"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.3939393939394%" headers="mcps1.2.6.1.5 "><p id="p1473512202311"><a name="p1473512202311"></a><a name="p1473512202311"></a>Specifies the OBS bucket name. Starts with a digit or letter and contains 3 to 63 characters, including lowercase letters, digits, hyphens (-), and periods (.)</p>
    </td>
    </tr>
    <tr id="row13568862153241"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.1 "><p id="p25336029153241"><a name="p25336029153241"></a><a name="p25336029153241"></a>file_prefix_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.6.1.2 "><p id="p2206349992235"><a name="p2206349992235"></a><a name="p2206349992235"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.3 "><p id="p38952493153241"><a name="p38952493153241"></a><a name="p38952493153241"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.6.1.4 "><p id="p1035382153241"><a name="p1035382153241"></a><a name="p1035382153241"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.3939393939394%" headers="mcps1.2.6.1.5 "><p id="p16757087153241"><a name="p16757087153241"></a><a name="p16757087153241"></a>Specifies the prefix of a log that needs to be stored in an OBS bucket. The value is a string of 0 to 64 characters and can contain uppercase and lowercase letters (a to z and A to Z), digits (0 to 9), hyphens (-), underscores (_), or periods (.)</p>
    </td>
    </tr>
    <tr id="row16596055153241"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.1 "><p id="p2103187153241"><a name="p2103187153241"></a><a name="p2103187153241"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.6.1.2 "><p id="p4231297292235"><a name="p4231297292235"></a><a name="p4231297292235"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.3 "><p id="p36140484153241"><a name="p36140484153241"></a><a name="p36140484153241"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.6.1.4 "><p id="p41698130153241"><a name="p41698130153241"></a><a name="p41698130153241"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.3939393939394%" headers="mcps1.2.6.1.5 "><p id="p22105380153241"><a name="p22105380153241"></a><a name="p22105380153241"></a>Specifies the status of a tracker. The value can be <strong id="b842352706102816"><a name="b842352706102816"></a><a name="b842352706102816"></a>enabled</strong> or <strong id="b842352706102819"><a name="b842352706102819"></a><a name="b842352706102819"></a>disabled</strong>. If you change the value to <strong id="b909741105102839"><a name="b909741105102839"></a><a name="b909741105102839"></a>disabled</strong>, the tracker stops recording traces.</p>
    </td>
    </tr>
    <tr id="row18709412171616"><td class="cellrowborder" rowspan="3" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.1 "><p id="p070951213162"><a name="p070951213162"></a><a name="p070951213162"></a>data_bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.6.1.2 "><p id="p147091212181611"><a name="p147091212181611"></a><a name="p147091212181611"></a>data_bucket_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.3 "><p id="p37095129167"><a name="p37095129167"></a><a name="p37095129167"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.6.1.4 "><p id="p1709151219165"><a name="p1709151219165"></a><a name="p1709151219165"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.3939393939394%" headers="mcps1.2.6.1.5 "><p id="p1908162512015"><a name="p1908162512015"></a><a name="p1908162512015"></a>Specifies the bucket name of the data class tracker.</p>
    <a name="ul2139143062018"></a><a name="ul2139143062018"></a><ul id="ul2139143062018"><li>This parameter is mandatory whenever the data class tracker is enabled or disabled.</li><li>This parameter is not invalid for the management class tracker.</li></ul>
    </td>
    </tr>
    <tr id="row15566131012163"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p105661710111610"><a name="p105661710111610"></a><a name="p105661710111610"></a>data_event</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p5566410181611"><a name="p5566410181611"></a><a name="p5566410181611"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p125661810181618"><a name="p125661810181618"></a><a name="p125661810181618"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p75661510131616"><a name="p75661510131616"></a><a name="p75661510131616"></a>Specifies the type of operations tracked by the data tracker.</p>
    <a name="ul18739104810214"></a><a name="ul18739104810214"></a><ul id="ul18739104810214"><li>This parameter is mandatory whenever the data class tracker is enabled or disabled.</li><li>This parameter is not invalid for the management class tracker.</li></ul>
    </td>
    </tr>
    <tr id="row1587118181617"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1287288163"><a name="p1287288163"></a><a name="p1287288163"></a>search_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p48728101613"><a name="p48728101613"></a><a name="p48728101613"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p2087188121611"><a name="p2087188121611"></a><a name="p2087188121611"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p10871688163"><a name="p10871688163"></a><a name="p10871688163"></a>Specifies whether to enable trace analysis for the data tracker.</p>
    <a name="ul15211082211"></a><a name="ul15211082211"></a><ul id="ul15211082211"><li>This parameter is mandatory whenever the data class tracker is enabled or disabled.</li><li>This parameter is not invalid for the management class tracker.</li></ul>
    </td>
    </tr>
    <tr id="row1930328992724"><td class="cellrowborder" rowspan="5" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.1 "><p id="p3593567292859"><a name="p3593567292859"></a><a name="p3593567292859"></a>smn</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.6.1.2 "><p id="p3867517692729"><a name="p3867517692729"></a><a name="p3867517692729"></a>is_support_smn</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.3 "><p id="p4568152992729"><a name="p4568152992729"></a><a name="p4568152992729"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.6.1.4 "><p id="p921640092729"><a name="p921640092729"></a><a name="p921640092729"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.3939393939394%" headers="mcps1.2.6.1.5 "><p id="p833089892729"><a name="p833089892729"></a><a name="p833089892729"></a>Specifies whether SMN is supported. When the value is <strong id="b84235270684317"><a name="b84235270684317"></a><a name="b84235270684317"></a>false,</strong> <strong id="b84235270684343"><a name="b84235270684343"></a><a name="b84235270684343"></a>topic_id</strong> and <strong id="b84235270684346"><a name="b84235270684346"></a><a name="b84235270684346"></a>operations</strong> can be left empty.</p>
    </td>
    </tr>
    <tr id="row11105136153241"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p4907961992345"><a name="p4907961992345"></a><a name="p4907961992345"></a>topic_id</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p47681201153241"><a name="p47681201153241"></a><a name="p47681201153241"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p36972074153241"><a name="p36972074153241"></a><a name="p36972074153241"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p41948052153241"><a name="p41948052153241"></a><a name="p41948052153241"></a><strong id="b842352706121543"><a name="b842352706121543"></a><a name="b842352706121543"></a>topic_id</strong> is obtained from SMN and in the format of urn:smn:([a-z]|[A-Z]|[0-9]|\-){1,32}:([a-z]|[A-Z]|[0-9]){32}:([a-z]|[A-Z]|[0-9]|\-|\_){1,256}.</p>
    </td>
    </tr>
    <tr id="row41988155153241"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1001795692345"><a name="p1001795692345"></a><a name="p1001795692345"></a>operations</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p33778322142644"><a name="p33778322142644"></a><a name="p33778322142644"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p51689595142644"><a name="p51689595142644"></a><a name="p51689595142644"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><a name="ul162265981116"></a><a name="ul162265981116"></a><ul id="ul162265981116"><li>Specifies trigger conditions for sending a notification when <strong id="b84235270611587"><a name="b84235270611587"></a><a name="b84235270611587"></a>Typical</strong> is selected. You can select <strong id="b2029003476122223"><a name="b2029003476122223"></a><a name="b2029003476122223"></a>delete</strong>, <strong id="b1109728545105053"><a name="b1109728545105053"></a><a name="b1109728545105053"></a>create</strong>, or <strong id="b842352706114716"><a name="b842352706114716"></a><a name="b842352706114716"></a>login</strong> or at least one of them.</li><li>Specifies trigger conditions for sending a notification when <strong id="b327180733115919"><a name="b327180733115919"></a><a name="b327180733115919"></a>All</strong> is selected. All conditions including <strong id="b802164191115919"><a name="b802164191115919"></a><a name="b802164191115919"></a>delete</strong>, <strong id="b908340737115919"><a name="b908340737115919"></a><a name="b908340737115919"></a>create</strong>, <strong id="b1028798214115919"><a name="b1028798214115919"></a><a name="b1028798214115919"></a>change</strong>, and <strong id="b842352706115953"><a name="b842352706115953"></a><a name="b842352706115953"></a>OpenStack API Event</strong> are selected by default. Modification is not allowed.</li></ul>
    </td>
    </tr>
    <tr id="row42322546142356"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p5533322892345"><a name="p5533322892345"></a><a name="p5533322892345"></a>is_send_all_key_operation</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p7142676142644"><a name="p7142676142644"></a><a name="p7142676142644"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p41685908142644"><a name="p41685908142644"></a><a name="p41685908142644"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p21115405142644"><a name="p21115405142644"></a><a name="p21115405142644"></a>You can select <strong id="b8423527069510"><a name="b8423527069510"></a><a name="b8423527069510"></a>Typical</strong> or <strong id="b8423527069513"><a name="b8423527069513"></a><a name="b8423527069513"></a>All</strong> for <strong id="b84235270695239"><a name="b84235270695239"></a><a name="b84235270695239"></a>Trigger Condition</strong>.</p>
    <a name="ul55820918142644"></a><a name="ul55820918142644"></a><ul id="ul55820918142644"><li>When the value is <strong id="b8423527069532"><a name="b8423527069532"></a><a name="b8423527069532"></a>false</strong>, <strong id="b84235270695350"><a name="b84235270695350"></a><a name="b84235270695350"></a>operations</strong> cannot be left empty.</li><li>When the value is <strong id="b84235270695415"><a name="b84235270695415"></a><a name="b84235270695415"></a>true</strong>, <strong id="b54327349095423"><a name="b54327349095423"></a><a name="b54327349095423"></a>operations</strong> is not supported.</li></ul>
    </td>
    </tr>
    <tr id="row2191026891511"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p549632592345"><a name="p549632592345"></a><a name="p549632592345"></a>need_notify_user_list</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p2337876891513"><a name="p2337876891513"></a><a name="p2337876891513"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1463208191513"><a name="p1463208191513"></a><a name="p1463208191513"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p33266591172353"><a name="p33266591172353"></a><a name="p33266591172353"></a>In <strong id="b842352706161739"><a name="b842352706161739"></a><a name="b842352706161739"></a>Typical</strong> scenario, you can specify the users using the login function. When these users log in, notifications will be sent.</p>
    <a name="ul30963871172353"></a><a name="ul30963871172353"></a><ul id="ul30963871172353"><li>After this function is enabled, the value is the list of the specified users. Separate them with a comma (,). A maximum of 50 users is supported.</li><li>If the value is null, the target objects are all users by default.</li></ul>
    </td>
    </tr>
    <tr id="row18488101217413"><td class="cellrowborder" rowspan="3" valign="top" width="19.191919191919194%" headers="mcps1.2.6.1.1 "><p id="p61511723174117"><a name="p61511723174117"></a><a name="p61511723174117"></a>lts</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.6.1.2 "><p id="p15179133012421"><a name="p15179133012421"></a><a name="p15179133012421"></a>is_lts_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.6.1.3 "><p id="p21804304422"><a name="p21804304422"></a><a name="p21804304422"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.6.1.4 "><p id="p151806302427"><a name="p151806302427"></a><a name="p151806302427"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.3939393939394%" headers="mcps1.2.6.1.5 "><p id="p635574111276"><a name="p635574111276"></a><a name="p635574111276"></a>Specifies whether to enable the log branch function. When the value is <strong id="b233216532167"><a name="b233216532167"></a><a name="b233216532167"></a>false</strong>, <strong id="b193331753101610"><a name="b193331753101610"></a><a name="b193331753101610"></a>log_group_name</strong> and <strong id="b103341253191618"><a name="b103341253191618"></a><a name="b103341253191618"></a>log_topic_name</strong> can be left empty.</p>
    </td>
    </tr>
    <tr id="row2631618174112"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1899159114320"><a name="p1899159114320"></a><a name="p1899159114320"></a>log_group_name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p98991891435"><a name="p98991891435"></a><a name="p98991891435"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p12631111819415"><a name="p12631111819415"></a><a name="p12631111819415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p98992092430"><a name="p98992092430"></a><a name="p98992092430"></a>Name of the LTS log group.</p>
    </td>
    </tr>
    <tr id="row18430131684111"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p10147112911436"><a name="p10147112911436"></a><a name="p10147112911436"></a>log_topic_name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p5147729144314"><a name="p5147729144314"></a><a name="p5147729144314"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p8147162904313"><a name="p8147162904313"></a><a name="p8147162904313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.6.1.4 "><p id="p16147192919436"><a name="p16147192919436"></a><a name="p16147192919436"></a>Name of the LTS log stream.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    PUT /v1.0/{project_id}/tracker/system   
    {
    	"bucket_name" : "my_created_bucket",
    	"file_prefix_name" : "some_folder",
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
    	},
    	"status" : "disabled"
    }
    ```


## Response<a name="section50089467"></a>

-   Parameters

    **Table  3**  Parameters in the response

    <a name="table14626574"></a>
    <table><thead align="left"><tr id="row8821459"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p43449544"><a name="p43449544"></a><a name="p43449544"></a><strong id="a0eb8e97159684639b27d5812ded25b6b_1"><a name="a0eb8e97159684639b27d5812ded25b6b_1"></a><a name="a0eb8e97159684639b27d5812ded25b6b_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p3157590892913"><a name="p3157590892913"></a><a name="p3157590892913"></a><strong id="a0eb8e97159684639b27d5812ded25b6b_2"><a name="a0eb8e97159684639b27d5812ded25b6b_2"></a><a name="a0eb8e97159684639b27d5812ded25b6b_2"></a>Sub-Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26%" id="mcps1.2.5.1.3"><p id="p29752153"><a name="p29752153"></a><a name="p29752153"></a><strong id="b842352706114330"><a name="b842352706114330"></a><a name="b842352706114330"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32%" id="mcps1.2.5.1.4"><p id="p61114224"><a name="p61114224"></a><a name="p61114224"></a><strong id="b842352706114333"><a name="b842352706114333"></a><a name="b842352706114333"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51305074"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p62070345"><a name="p62070345"></a><a name="p62070345"></a>tracker_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p751175192913"><a name="p751175192913"></a><a name="p751175192913"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.3 "><p id="p61642077"><a name="p61642077"></a><a name="p61642077"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.5.1.4 "><p id="p26952341"><a name="p26952341"></a><a name="p26952341"></a>Specifies the tracker name. Currently, only tracker "system" is available.</p>
    </td>
    </tr>
    <tr id="row41244482"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p52468780"><a name="p52468780"></a><a name="p52468780"></a>bucket_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p447210392913"><a name="p447210392913"></a><a name="p447210392913"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.3 "><p id="p22112815"><a name="p22112815"></a><a name="p22112815"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.5.1.4 "><p id="p178572143147"><a name="p178572143147"></a><a name="p178572143147"></a>Specifies the OBS bucket name. Starts with a digit or letter and contains 3 to 63 characters, including lowercase letters, digits, hyphens (-), and periods (.)</p>
    </td>
    </tr>
    <tr id="row14114947"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p2460041"><a name="p2460041"></a><a name="p2460041"></a>file_prefix_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p2669604392913"><a name="p2669604392913"></a><a name="p2669604392913"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.3 "><p id="p65045669"><a name="p65045669"></a><a name="p65045669"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.5.1.4 "><p id="p34207804"><a name="p34207804"></a><a name="p34207804"></a>Specifies the prefix of a log that needs to be stored in an OBS bucket.</p>
    </td>
    </tr>
    <tr id="row39434786"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p40101120"><a name="p40101120"></a><a name="p40101120"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p1489586892913"><a name="p1489586892913"></a><a name="p1489586892913"></a>N/A</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.3 "><p id="p26965262"><a name="p26965262"></a><a name="p26965262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.5.1.4 "><p id="p36702580"><a name="p36702580"></a><a name="p36702580"></a>Specifies the status of a tracker. The value can be <strong id="b8423527061008"><a name="b8423527061008"></a><a name="b8423527061008"></a>enabled</strong> or <strong id="b842352706103021"><a name="b842352706103021"></a><a name="b842352706103021"></a>disabled</strong>.</p>
    </td>
    </tr>
    <tr id="row3009162610383"><td class="cellrowborder" rowspan="5" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p3422097892947"><a name="p3422097892947"></a><a name="p3422097892947"></a>smn</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p3961943692932"><a name="p3961943692932"></a><a name="p3961943692932"></a>is_support_smn</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.3 "><p id="p16791672103811"><a name="p16791672103811"></a><a name="p16791672103811"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.5.1.4 "><p id="p17948192103811"><a name="p17948192103811"></a><a name="p17948192103811"></a>Specifies whether SMN is supported.</p>
    </td>
    </tr>
    <tr id="row3194735710383"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2575788392932"><a name="p2575788392932"></a><a name="p2575788392932"></a>topic_id</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p39647986103811"><a name="p39647986103811"></a><a name="p39647986103811"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p57370277103811"><a name="p57370277103811"></a><a name="p57370277103811"></a>Specifies the theme of the SMN service.</p>
    </td>
    </tr>
    <tr id="row6462071910383"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p5412406292932"><a name="p5412406292932"></a><a name="p5412406292932"></a>operations</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p25958905142820"><a name="p25958905142820"></a><a name="p25958905142820"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><a name="ul4173273911713"></a><a name="ul4173273911713"></a><ul id="ul4173273911713"><li>Specifies trigger conditions for sending a notification when <strong id="b2707665115337"><a name="b2707665115337"></a><a name="b2707665115337"></a>Typical</strong> is selected. You can select <strong id="b24368987115337"><a name="b24368987115337"></a><a name="b24368987115337"></a>delete</strong>, <strong id="b17994293115337"><a name="b17994293115337"></a><a name="b17994293115337"></a>create</strong>, or <strong id="b27730912115337"><a name="b27730912115337"></a><a name="b27730912115337"></a>login</strong> or at least one of them.</li><li>Specifies trigger conditions for sending a notification when <strong id="b327180733115919_1"><a name="b327180733115919_1"></a><a name="b327180733115919_1"></a>All</strong> is selected. All conditions including <strong id="b802164191115919_1"><a name="b802164191115919_1"></a><a name="b802164191115919_1"></a>delete</strong>, <strong id="b908340737115919_1"><a name="b908340737115919_1"></a><a name="b908340737115919_1"></a>create</strong>, <strong id="b1028798214115919_1"><a name="b1028798214115919_1"></a><a name="b1028798214115919_1"></a>change</strong>, and <strong id="b842352706115953_1"><a name="b842352706115953_1"></a><a name="b842352706115953_1"></a>OpenStack API Event</strong> are selected by default. Modification is not allowed.</li></ul>
    </td>
    </tr>
    <tr id="row40623323142724"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p6353838492932"><a name="p6353838492932"></a><a name="p6353838492932"></a>is_send_all_key_operation</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p49544814142820"><a name="p49544814142820"></a><a name="p49544814142820"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p53707034142820"><a name="p53707034142820"></a><a name="p53707034142820"></a>You can select <strong id="b8423527069510_1"><a name="b8423527069510_1"></a><a name="b8423527069510_1"></a>Typical</strong> or <strong id="b8423527069513_1"><a name="b8423527069513_1"></a><a name="b8423527069513_1"></a>All</strong> for <strong id="b84235270695239_1"><a name="b84235270695239_1"></a><a name="b84235270695239_1"></a>Trigger Condition</strong>.</p>
    <a name="ul13601258142820"></a><a name="ul13601258142820"></a><ul id="ul13601258142820"><li>When the value is <strong id="b8423527069532_1"><a name="b8423527069532_1"></a><a name="b8423527069532_1"></a>false</strong>, <strong id="b84235270695350_1"><a name="b84235270695350_1"></a><a name="b84235270695350_1"></a>operations</strong> cannot be left empty.</li><li>When the value is <strong id="b84235270695415_1"><a name="b84235270695415_1"></a><a name="b84235270695415_1"></a>true</strong>, <strong id="b54327349095423_1"><a name="b54327349095423_1"></a><a name="b54327349095423_1"></a>operations</strong> is not supported.</li></ul>
    </td>
    </tr>
    <tr id="row110514099174"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1436616492932"><a name="p1436616492932"></a><a name="p1436616492932"></a>need_notify_user_list</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p6377514591732"><a name="p6377514591732"></a><a name="p6377514591732"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p4086784985653"><a name="p4086784985653"></a><a name="p4086784985653"></a>In <strong id="b842352706161739_1"><a name="b842352706161739_1"></a><a name="b842352706161739_1"></a>Typical</strong> scenario, you can specify the users using the login function. When these users log in, notifications will be sent.</p>
    <a name="ul54166538900"></a><a name="ul54166538900"></a><ul id="ul54166538900"><li>After this function is enabled, the value is the list of the specified users. Separate them with a comma (,). A maximum of 50 users is supported.</li><li>If the value is null, the target objects are all users by default.</li></ul>
    </td>
    </tr>
    <tr id="row95091143144210"><td class="cellrowborder" rowspan="3" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p55601316434"><a name="p55601316434"></a><a name="p55601316434"></a>lts</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p14509743104218"><a name="p14509743104218"></a><a name="p14509743104218"></a>is_lts_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.5.1.3 "><p id="p1856113320439"><a name="p1856113320439"></a><a name="p1856113320439"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.5.1.4 "><p id="p95090437427"><a name="p95090437427"></a><a name="p95090437427"></a>Specifies whether to enable the log branch function.</p>
    </td>
    </tr>
    <tr id="row051818491427"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p12518174934217"><a name="p12518174934217"></a><a name="p12518174934217"></a>log_group_name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p057010479435"><a name="p057010479435"></a><a name="p057010479435"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p16762144134414"><a name="p16762144134414"></a><a name="p16762144134414"></a>Name of the LTS log group.</p>
    </td>
    </tr>
    <tr id="row17662477421"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1856110317430"><a name="p1856110317430"></a><a name="p1856110317430"></a>log_topic_name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p187444984310"><a name="p187444984310"></a><a name="p187444984310"></a>String</p>
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
	"file_prefix_name" : "some_folder",
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
	},
	"status" : "disabled"
}
```

## Returned Value<a name="section48152024"></a>

-   Normal

    **Table  4**  Return code for successful requests

    <a name="table40184969"></a>
    <table><thead align="left"><tr id="row47078488"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p55261147"><a name="p55261147"></a><a name="p55261147"></a><strong id="b842352706114339"><a name="b842352706114339"></a><a name="b842352706114339"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p46967960"><a name="p46967960"></a><a name="p46967960"></a><strong id="b842352706114342"><a name="b842352706114342"></a><a name="b842352706114342"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46308405"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p59993306"><a name="p59993306"></a><a name="p59993306"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p27619632"><a name="p27619632"></a><a name="p27619632"></a>The request is successfully processed.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    **Table  5**  Return code for failed requests

    <a name="table22597726"></a>
    <table><thead align="left"><tr id="row47637903"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p33464950"><a name="p33464950"></a><a name="p33464950"></a><strong id="b842352706114346"><a name="b842352706114346"></a><a name="b842352706114346"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p26306458"><a name="p26306458"></a><a name="p26306458"></a><strong id="b842352706114349"><a name="b842352706114349"></a><a name="b842352706114349"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4060124914320"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p1792165414323"><a name="p1792165414323"></a><a name="p1792165414323"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p4236789014323"><a name="p4236789014323"></a><a name="p4236789014323"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row50448354"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p59784887"><a name="p59784887"></a><a name="p59784887"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p10737664"><a name="p10737664"></a><a name="p10737664"></a>The server failed to find the requested resource.</p>
    </td>
    </tr>
    <tr id="row29530116"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p43129175"><a name="p43129175"></a><a name="p43129175"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p3802258"><a name="p3802258"></a><a name="p3802258"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row7482544102614"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p63810326102628"><a name="p63810326102628"></a><a name="p63810326102628"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p1253885102628"><a name="p1253885102628"></a><a name="p1253885102628"></a>Your access request is rejected.</p>
    </td>
    </tr>
    <tr id="row60099241102618"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p3443958102638"><a name="p3443958102638"></a><a name="p3443958102638"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p10525145102638"><a name="p10525145102638"></a><a name="p10525145102638"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    </tbody>
    </table>


