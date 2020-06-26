# Querying Forwarding Rules<a name="EN-US_TOPIC_0116649234"></a>

## Function<a name="section169151579315"></a>

This API is used to query the forwarding rules. Filter query and pagination query are supported. Unless otherwise specified, exact match is applied.

## URI<a name="en-us_topic_0082661925_section7468452145941"></a>

GET /v2.0/lbaas/l7policies/\{l7policy\_id\}/rules

**Table  1**  Parameter description

<a name="table7499543142219"></a>
<table><thead align="left"><tr id="row3499843182216"><th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.1"><p id="p94995435221"><a name="p94995435221"></a><a name="p94995435221"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="10.101010101010102%" id="mcps1.2.5.1.2"><p id="p132241538132114"><a name="p132241538132114"></a><a name="p132241538132114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.3"><p id="p11499144352210"><a name="p11499144352210"></a><a name="p11499144352210"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="62.62626262626263%" id="mcps1.2.5.1.4"><p id="p34997434220"><a name="p34997434220"></a><a name="p34997434220"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1499134372214"><td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.1 "><p id="p2499243172211"><a name="p2499243172211"></a><a name="p2499243172211"></a>l7policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.2 "><p id="p62222038202115"><a name="p62222038202115"></a><a name="p62222038202115"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.3 "><p id="p8499134342213"><a name="p8499134342213"></a><a name="p8499134342213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.62626262626263%" headers="mcps1.2.5.1.4 "><p id="p84991243162216"><a name="p84991243162216"></a><a name="p84991243162216"></a>Specifies the forwarding policy ID.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="section4448184311224"></a>

Parameters  **marker**,  **limit**, and  **page\_reverse**  are used for pagination query. Parameters  **marker**  and  **page\_reverse**  take effect only when they are used together with parameter  **limit**.

## Request<a name="en-us_topic_0082661925_section51859831145941"></a>

**Table  2**  Request parameters

<a name="table360792218500"></a>
<table><thead align="left"><tr id="row6791152295011"><th class="cellrowborder" valign="top" width="28.15281528152815%" id="mcps1.2.5.1.1"><p id="p8791112255016"><a name="p8791112255016"></a><a name="p8791112255016"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.041104110411041%" id="mcps1.2.5.1.2"><p id="p177916223503"><a name="p177916223503"></a><a name="p177916223503"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="8.890889088908892%" id="mcps1.2.5.1.3"><p id="p1479102255019"><a name="p1479102255019"></a><a name="p1479102255019"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.91519151915192%" id="mcps1.2.5.1.4"><p id="p16791102219507"><a name="p16791102219507"></a><a name="p16791102219507"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3791522145010"><td class="cellrowborder" valign="top" width="28.15281528152815%" headers="mcps1.2.5.1.1 "><p id="p18791722195020"><a name="p18791722195020"></a><a name="p18791722195020"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="11.041104110411041%" headers="mcps1.2.5.1.2 "><p id="p177915227501"><a name="p177915227501"></a><a name="p177915227501"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.890889088908892%" headers="mcps1.2.5.1.3 "><p id="p479152215504"><a name="p479152215504"></a><a name="p479152215504"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.91519151915192%" headers="mcps1.2.5.1.4 "><p id="p4235152211344"><a name="p4235152211344"></a><a name="p4235152211344"></a>Specifies the ID of the forwarding rule from which pagination query starts, that is, the ID of the last forwarding rule on the previous page.</p>
<p id="p06221826143418"><a name="p06221826143418"></a><a name="p06221826143418"></a>This parameter must be used together with <strong id="b945794234911"><a name="b945794234911"></a><a name="b945794234911"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row1579132218507"><td class="cellrowborder" valign="top" width="28.15281528152815%" headers="mcps1.2.5.1.1 "><p id="p13791102205018"><a name="p13791102205018"></a><a name="p13791102205018"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="11.041104110411041%" headers="mcps1.2.5.1.2 "><p id="p9791622175011"><a name="p9791622175011"></a><a name="p9791622175011"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.890889088908892%" headers="mcps1.2.5.1.3 "><p id="p5791182213509"><a name="p5791182213509"></a><a name="p5791182213509"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51.91519151915192%" headers="mcps1.2.5.1.4 "><p id="p163282306342"><a name="p163282306342"></a><a name="p163282306342"></a>Specifies the number of forwarding rules on each page. </p>
<p id="p8300236113416"><a name="p8300236113416"></a><a name="p8300236113416"></a>The value ranges from <strong id="b139885331515"><a name="b139885331515"></a><a name="b139885331515"></a>0</strong> to <strong id="b179891133135112"><a name="b179891133135112"></a><a name="b179891133135112"></a>intmax</strong>.</p>
</td>
</tr>
<tr id="row1879222220503"><td class="cellrowborder" valign="top" width="28.15281528152815%" headers="mcps1.2.5.1.1 "><p id="p47921922155013"><a name="p47921922155013"></a><a name="p47921922155013"></a>page_reverse</p>
</td>
<td class="cellrowborder" valign="top" width="11.041104110411041%" headers="mcps1.2.5.1.2 "><p id="p167921822185015"><a name="p167921822185015"></a><a name="p167921822185015"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.890889088908892%" headers="mcps1.2.5.1.3 "><p id="p18792922125013"><a name="p18792922125013"></a><a name="p18792922125013"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="51.91519151915192%" headers="mcps1.2.5.1.4 "><p id="p15227113913341"><a name="p15227113913341"></a><a name="p15227113913341"></a>Specifies the page direction. The value can be <strong id="b19958113641314"><a name="b19958113641314"></a><a name="b19958113641314"></a>true</strong> or <strong id="b17959153620133"><a name="b17959153620133"></a><a name="b17959153620133"></a>false</strong>, and the default value is <strong id="b2960153618136"><a name="b2960153618136"></a><a name="b2960153618136"></a>false</strong>. The last page in the list requested with <strong id="b7960173651311"><a name="b7960173651311"></a><a name="b7960173651311"></a>page_reverse</strong> set to <strong id="b196133613131"><a name="b196133613131"></a><a name="b196133613131"></a>false</strong> will not contain the "next" link, and the last page in the list requested with <strong id="b179610369134"><a name="b179610369134"></a><a name="b179610369134"></a>page_reverse</strong> set to <strong id="b16962163671310"><a name="b16962163671310"></a><a name="b16962163671310"></a>true</strong> will not contain the "previous" link.</p>
<p id="p5244104243413"><a name="p5244104243413"></a><a name="p5244104243413"></a>This parameter must be used together with <strong id="b176601535175117"><a name="b176601535175117"></a><a name="b176601535175117"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row18792722135018"><td class="cellrowborder" valign="top" width="28.15281528152815%" headers="mcps1.2.5.1.1 "><p id="p579222210501"><a name="p579222210501"></a><a name="p579222210501"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="11.041104110411041%" headers="mcps1.2.5.1.2 "><p id="p2079282218505"><a name="p2079282218505"></a><a name="p2079282218505"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.890889088908892%" headers="mcps1.2.5.1.3 "><p id="p147921225505"><a name="p147921225505"></a><a name="p147921225505"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.91519151915192%" headers="mcps1.2.5.1.4 "><p id="p177921622135012"><a name="p177921622135012"></a><a name="p177921622135012"></a>Specifies the forwarding rule ID.</p>
</td>
</tr>
<tr id="row187921022165016"><td class="cellrowborder" valign="top" width="28.15281528152815%" headers="mcps1.2.5.1.1 "><p id="p1679232215014"><a name="p1679232215014"></a><a name="p1679232215014"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.041104110411041%" headers="mcps1.2.5.1.2 "><p id="p279222218509"><a name="p279222218509"></a><a name="p279222218509"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.890889088908892%" headers="mcps1.2.5.1.3 "><p id="p1579252214505"><a name="p1579252214505"></a><a name="p1579252214505"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.91519151915192%" headers="mcps1.2.5.1.4 "><p id="p11184131"><a name="p11184131"></a><a name="p11184131"></a>Specifies the ID of the project where the forwarding rule is used.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row079212227502"><td class="cellrowborder" valign="top" width="28.15281528152815%" headers="mcps1.2.5.1.1 "><p id="p187921122155017"><a name="p187921122155017"></a><a name="p187921122155017"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="11.041104110411041%" headers="mcps1.2.5.1.2 "><p id="p5792192205017"><a name="p5792192205017"></a><a name="p5792192205017"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.890889088908892%" headers="mcps1.2.5.1.3 "><p id="p1779252275015"><a name="p1779252275015"></a><a name="p1779252275015"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="51.91519151915192%" headers="mcps1.2.5.1.4 "><p id="p189741017613"><a name="p189741017613"></a><a name="p189741017613"></a>Specifies the administrative status of the forwarding rule.</p>
<p id="p189052592020"><a name="p189052592020"></a><a name="p189052592020"></a>The value can be <strong id="b10805203719514"><a name="b10805203719514"></a><a name="b10805203719514"></a>true</strong> or <strong id="b7806183795117"><a name="b7806183795117"></a><a name="b7806183795117"></a>false</strong>.</p>
<p id="p1610904293213"><a name="p1610904293213"></a><a name="p1610904293213"></a>This parameter is reserved. The default value is <strong id="b135545684516"><a name="b135545684516"></a><a name="b135545684516"></a>true</strong>.</p>
</td>
</tr>
<tr id="row47923228501"><td class="cellrowborder" valign="top" width="28.15281528152815%" headers="mcps1.2.5.1.1 "><p id="p7792112255010"><a name="p7792112255010"></a><a name="p7792112255010"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="11.041104110411041%" headers="mcps1.2.5.1.2 "><p id="p15792122235013"><a name="p15792122235013"></a><a name="p15792122235013"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.890889088908892%" headers="mcps1.2.5.1.3 "><p id="p1792192210506"><a name="p1792192210506"></a><a name="p1792192210506"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.91519151915192%" headers="mcps1.2.5.1.4 "><p id="p1161972619482"><a name="p1161972619482"></a><a name="p1161972619482"></a>Specifies the match type of a forwarding rule.</p>
<p id="p9536114413489"><a name="p9536114413489"></a><a name="p9536114413489"></a>The value can be one of the following:</p>
<a name="ul3525953124817"></a><a name="ul3525953124817"></a><ul id="ul3525953124817"><li><strong id="b15235194317515"><a name="b15235194317515"></a><a name="b15235194317515"></a>HOST_NAME</strong>: matches the domain name in the request.</li><li><strong id="b848794416516"><a name="b848794416516"></a><a name="b848794416516"></a>PATH</strong>: matches the path in the request.</li></ul>
<p id="p15285166489"><a name="p15285166489"></a><a name="p15285166489"></a>The match type of forwarding rules in a forwarding policy must be unique.</p>
</td>
</tr>
<tr id="row1279242295016"><td class="cellrowborder" valign="top" width="28.15281528152815%" headers="mcps1.2.5.1.1 "><p id="p197931722175012"><a name="p197931722175012"></a><a name="p197931722175012"></a>compare_type</p>
</td>
<td class="cellrowborder" valign="top" width="11.041104110411041%" headers="mcps1.2.5.1.2 "><p id="p1979314227506"><a name="p1979314227506"></a><a name="p1979314227506"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.890889088908892%" headers="mcps1.2.5.1.3 "><p id="p1279382265012"><a name="p1279382265012"></a><a name="p1279382265012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.91519151915192%" headers="mcps1.2.5.1.4 "><p id="p51371649125820"><a name="p51371649125820"></a><a name="p51371649125820"></a>Specifies the match mode. The options are as follows:</p>
<p id="p10794420115116"><a name="p10794420115116"></a><a name="p10794420115116"></a>When <strong id="b1170415481515"><a name="b1170415481515"></a><a name="b1170415481515"></a>type</strong> is set to <strong id="b97053486514"><a name="b97053486514"></a><a name="b97053486514"></a>HOST_NAME</strong>, the value of this parameter can only be the following:</p>
<a name="ul15305619145114"></a><a name="ul15305619145114"></a><ul id="ul15305619145114"><li><strong id="b997144919516"><a name="b997144919516"></a><a name="b997144919516"></a>EQUAL_TO</strong>: indicates exact match.</li></ul>
<p id="p13663103020517"><a name="p13663103020517"></a><a name="p13663103020517"></a>When <strong id="b24861451155115"><a name="b24861451155115"></a><a name="b24861451155115"></a>type</strong> is set to <strong id="b1548785125116"><a name="b1548785125116"></a><a name="b1548785125116"></a>PATH</strong>, the value of this parameter can be one of the following:</p>
<a name="ul17531436125112"></a><a name="ul17531436125112"></a><ul id="ul17531436125112"><li><strong id="b11799115213519"><a name="b11799115213519"></a><a name="b11799115213519"></a>REGEX</strong>: indicates regular expression match.</li><li><strong id="b579115435118"><a name="b579115435118"></a><a name="b579115435118"></a>STARTS_WITH</strong>: indicates prefix match.</li><li><strong id="b19176195595116"><a name="b19176195595116"></a><a name="b19176195595116"></a>EQUAL_TO</strong>: indicates exact match.</li></ul>
</td>
</tr>
<tr id="row16793182219506"><td class="cellrowborder" valign="top" width="28.15281528152815%" headers="mcps1.2.5.1.1 "><p id="p187931822165010"><a name="p187931822165010"></a><a name="p187931822165010"></a>invert</p>
</td>
<td class="cellrowborder" valign="top" width="11.041104110411041%" headers="mcps1.2.5.1.2 "><p id="p167931822175012"><a name="p167931822175012"></a><a name="p167931822175012"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.890889088908892%" headers="mcps1.2.5.1.3 "><p id="p19793182210507"><a name="p19793182210507"></a><a name="p19793182210507"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="51.91519151915192%" headers="mcps1.2.5.1.4 "><p id="p1837110431511"><a name="p1837110431511"></a><a name="p1837110431511"></a>Specifies whether reverse match is supported.</p>
<p id="p1497849152414"><a name="p1497849152414"></a><a name="p1497849152414"></a>The value can be <strong id="b8781657185117"><a name="b8781657185117"></a><a name="b8781657185117"></a>true</strong> or <strong id="b478235715513"><a name="b478235715513"></a><a name="b478235715513"></a>false</strong>. The default value is <strong id="b11199059165117"><a name="b11199059165117"></a><a name="b11199059165117"></a>false</strong>.</p>
<p id="p1828957181510"><a name="p1828957181510"></a><a name="p1828957181510"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="row20793122245015"><td class="cellrowborder" valign="top" width="28.15281528152815%" headers="mcps1.2.5.1.1 "><p id="p1379382265013"><a name="p1379382265013"></a><a name="p1379382265013"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="11.041104110411041%" headers="mcps1.2.5.1.2 "><p id="p12793222155016"><a name="p12793222155016"></a><a name="p12793222155016"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.890889088908892%" headers="mcps1.2.5.1.3 "><p id="p19793622105017"><a name="p19793622105017"></a><a name="p19793622105017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.91519151915192%" headers="mcps1.2.5.1.4 "><p id="p781771561717"><a name="p781771561717"></a><a name="p781771561717"></a>Specifies the key of the match content. The default value is <strong id="b20117319528"><a name="b20117319528"></a><a name="b20117319528"></a>null</strong>.</p>
<p id="p198171615161716"><a name="p198171615161716"></a><a name="p198171615161716"></a>This parameter is reserved.</p>
<p id="p259352683110"><a name="p259352683110"></a><a name="p259352683110"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row12793172219508"><td class="cellrowborder" valign="top" width="28.15281528152815%" headers="mcps1.2.5.1.1 "><p id="p3793152214509"><a name="p3793152214509"></a><a name="p3793152214509"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="11.041104110411041%" headers="mcps1.2.5.1.2 "><p id="p117931322175012"><a name="p117931322175012"></a><a name="p117931322175012"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.890889088908892%" headers="mcps1.2.5.1.3 "><p id="p1679382211505"><a name="p1679382211505"></a><a name="p1679382211505"></a>String</p>
<p id="p207931223501"><a name="p207931223501"></a><a name="p207931223501"></a></p>
</td>
<td class="cellrowborder" valign="top" width="51.91519151915192%" headers="mcps1.2.5.1.4 "><p id="p19314172610176"><a name="p19314172610176"></a><a name="p19314172610176"></a>Specifies the value of the match content.</p>
<p id="p93101830103115"><a name="p93101830103115"></a><a name="p93101830103115"></a>The value contains a maximum of 128 characters.</p>
<a name="ul731432621713"></a><a name="ul731432621713"></a><ul id="ul731432621713"><li>When <strong id="b52941659114517"><a name="b52941659114517"></a><a name="b52941659114517"></a>type</strong> is set to <strong id="b1529595910458"><a name="b1529595910458"></a><a name="b1529595910458"></a>HOST_NAME</strong>, the value is a string of a maximum of 100 characters, contains only letters, digits, hyphens (-), and periods (.), and must start with a letter or digit.</li><li>When <strong id="b14496522466"><a name="b14496522466"></a><a name="b14496522466"></a>type</strong> is set to <strong id="b1449614220462"><a name="b1449614220462"></a><a name="b1449614220462"></a>PATH</strong>, the value is a string of a maximum of 128 characters. When the value of <strong id="b3613210175214"><a name="b3613210175214"></a><a name="b3613210175214"></a>compare_type</strong> is set to <strong id="b2614210185218"><a name="b2614210185218"></a><a name="b2614210185218"></a>STARTS_WITH</strong> or <strong id="b7615710205217"><a name="b7615710205217"></a><a name="b7615710205217"></a>EQUAL_TO</strong>, the string must start with a slash (/) and can contain only letters, digits, and special characters _~';@^-%#&amp;$.*+?,=!:|\/()[]{}</li></ul>
</td>
</tr>
<tr id="row1879342295018"><td class="cellrowborder" valign="top" width="28.15281528152815%" headers="mcps1.2.5.1.1 "><p id="p147930223508"><a name="p147930223508"></a><a name="p147930223508"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="11.041104110411041%" headers="mcps1.2.5.1.2 "><p id="p18793112211501"><a name="p18793112211501"></a><a name="p18793112211501"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="8.890889088908892%" headers="mcps1.2.5.1.3 "><p id="p117931022145014"><a name="p117931022145014"></a><a name="p117931022145014"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.91519151915192%" headers="mcps1.2.5.1.4 "><p id="p14704205693714"><a name="p14704205693714"></a><a name="p14704205693714"></a>Specifies the provisioning status of the forwarding rule. The value can be <strong id="b1147310121525"><a name="b1147310121525"></a><a name="b1147310121525"></a>ACTIVE</strong>, <strong id="b3474312175216"><a name="b3474312175216"></a><a name="b3474312175216"></a>PENDING_CREATE</strong>, or <strong id="b154751112165214"><a name="b154751112165214"></a><a name="b154751112165214"></a>ERROR</strong>.</p>
<p id="p178421832011"><a name="p178421832011"></a><a name="p178421832011"></a>The default value is <strong id="b570215132527"><a name="b570215132527"></a><a name="b570215132527"></a>ACTIVE</strong>.</p>
<p id="p210952312206"><a name="p210952312206"></a><a name="p210952312206"></a>This parameter is reserved.</p>
<p id="p11290446163118"><a name="p11290446163118"></a><a name="p11290446163118"></a>The value contains a maximum of 16 characters.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section19463191963013"></a>

**Table  3**  Response parameters

<a name="table0996611195215"></a>
<table><thead align="left"><tr id="row173041215215"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.4.1.1"><p id="p103061225213"><a name="p103061225213"></a><a name="p103061225213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.4.1.2"><p id="p1330171214526"><a name="p1330171214526"></a><a name="p1330171214526"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.4059405940594%" id="mcps1.2.4.1.3"><p id="p113061219521"><a name="p113061219521"></a><a name="p113061219521"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row73021275214"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p153041218522"><a name="p153041218522"></a><a name="p153041218522"></a>rules</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561533_p422512115486"><a name="en-us_topic_0096561533_p422512115486"></a><a name="en-us_topic_0096561533_p422512115486"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="59.4059405940594%" headers="mcps1.2.4.1.3 "><p id="p430412105214"><a name="p430412105214"></a><a name="p430412105214"></a>Lists the forwarding rules. For details, see <a href="#table19731219105316">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **rules**  parameter description

<a name="table19731219105316"></a>
<table><thead align="left"><tr id="row18222814135918"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.4.1.1"><p id="p102227144592"><a name="p102227144592"></a><a name="p102227144592"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.4.1.2"><p id="p922291411591"><a name="p922291411591"></a><a name="p922291411591"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.59595959595959%" id="mcps1.2.4.1.3"><p id="p945745517918"><a name="p945745517918"></a><a name="p945745517918"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row102221114205912"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p122261415596"><a name="p122261415596"></a><a name="p122261415596"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p888713113107"><a name="p888713113107"></a><a name="p888713113107"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p52228141594"><a name="p52228141594"></a><a name="p52228141594"></a>Specifies the forwarding rule ID.</p>
</td>
</tr>
<tr id="row202222146591"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p11222111412593"><a name="p11222111412593"></a><a name="p11222111412593"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p4222914145911"><a name="p4222914145911"></a><a name="p4222914145911"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p1266711718204"><a name="p1266711718204"></a><a name="p1266711718204"></a>Specifies the ID of the project where the forwarding rule is used.</p>
<p id="p59353183315"><a name="p59353183315"></a><a name="p59353183315"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row722213149597"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p1622251465915"><a name="p1622251465915"></a><a name="p1622251465915"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p19222111414597"><a name="p19222111414597"></a><a name="p19222111414597"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p1979757131619"><a name="p1979757131619"></a><a name="p1979757131619"></a>Specifies the administrative status of the forwarding rule.</p>
<p id="p179812717162"><a name="p179812717162"></a><a name="p179812717162"></a>The value can be <strong id="b13873153515213"><a name="b13873153515213"></a><a name="b13873153515213"></a>true</strong> or <strong id="b7875173595217"><a name="b7875173595217"></a><a name="b7875173595217"></a>false</strong>.</p>
<p id="p19533221134218"><a name="p19533221134218"></a><a name="p19533221134218"></a>This parameter is reserved. The default value is <strong id="b1380214713469"><a name="b1380214713469"></a><a name="b1380214713469"></a>true</strong>.</p>
</td>
</tr>
<tr id="row4224114155917"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p92241147592"><a name="p92241147592"></a><a name="p92241147592"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p222481475913"><a name="p222481475913"></a><a name="p222481475913"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p199311319151611"><a name="p199311319151611"></a><a name="p199311319151611"></a>Specifies the match type of a forwarding rule.</p>
<p id="p293131991615"><a name="p293131991615"></a><a name="p293131991615"></a>The value can be one of the following:</p>
<a name="ul13931161917169"></a><a name="ul13931161917169"></a><ul id="ul13931161917169"><li><strong id="b101137424524"><a name="b101137424524"></a><a name="b101137424524"></a>HOST_NAME</strong>: matches the domain name in the request.</li><li><strong id="b136271243135215"><a name="b136271243135215"></a><a name="b136271243135215"></a>PATH</strong>: matches the path in the request.</li></ul>
</td>
</tr>
<tr id="row622461465910"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p162241814165916"><a name="p162241814165916"></a><a name="p162241814165916"></a>compare_type</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p12241214105911"><a name="p12241214105911"></a><a name="p12241214105911"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p928234417166"><a name="p928234417166"></a><a name="p928234417166"></a>Specifies the match mode. The options are as follows:</p>
<p id="p112828447167"><a name="p112828447167"></a><a name="p112828447167"></a>When <strong id="b95681446175216"><a name="b95681446175216"></a><a name="b95681446175216"></a>type</strong> is set to <strong id="b7569124625212"><a name="b7569124625212"></a><a name="b7569124625212"></a>HOST_NAME</strong>, the value of this parameter can only be the following:</p>
<a name="ul128264412167"></a><a name="ul128264412167"></a><ul id="ul128264412167"><li><strong id="b5178648125214"><a name="b5178648125214"></a><a name="b5178648125214"></a>EQUAL_TO</strong>: indicates exact match.</li></ul>
<p id="p2028224451611"><a name="p2028224451611"></a><a name="p2028224451611"></a>When <strong id="b0318144913529"><a name="b0318144913529"></a><a name="b0318144913529"></a>type</strong> is set to <strong id="b13194499524"><a name="b13194499524"></a><a name="b13194499524"></a>PATH</strong>, the value of this parameter can be one of the following:</p>
<a name="ul162821144131610"></a><a name="ul162821144131610"></a><ul id="ul162821144131610"><li><strong id="b1239115531524"><a name="b1239115531524"></a><a name="b1239115531524"></a>REGEX</strong>: indicates regular expression match.</li><li><strong id="b2261205520526"><a name="b2261205520526"></a><a name="b2261205520526"></a>STARTS_WITH</strong>: indicates prefix match.</li><li><strong id="b134151756115216"><a name="b134151756115216"></a><a name="b134151756115216"></a>EQUAL_TO</strong>: indicates exact match.</li></ul>
</td>
</tr>
<tr id="row322461410591"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p622481485911"><a name="p622481485911"></a><a name="p622481485911"></a>invert</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p1622411412594"><a name="p1622411412594"></a><a name="p1622411412594"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p4697172743112"><a name="p4697172743112"></a><a name="p4697172743112"></a>Specifies whether reverse match is supported.</p>
<p id="p20699112712319"><a name="p20699112712319"></a><a name="p20699112712319"></a>The value can be <strong id="b689217587527"><a name="b689217587527"></a><a name="b689217587527"></a>true</strong> or <strong id="b18931658125215"><a name="b18931658125215"></a><a name="b18931658125215"></a>false</strong>. The default value is <strong id="b12501400536"><a name="b12501400536"></a><a name="b12501400536"></a>false</strong>.</p>
<p id="p10700172773113"><a name="p10700172773113"></a><a name="p10700172773113"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="row19224714125916"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p172241014165910"><a name="p172241014165910"></a><a name="p172241014165910"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p922415146591"><a name="p922415146591"></a><a name="p922415146591"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p2070622763110"><a name="p2070622763110"></a><a name="p2070622763110"></a>Specifies the key of the match content. The default value is <strong id="b94609318531"><a name="b94609318531"></a><a name="b94609318531"></a>null</strong>.</p>
<p id="p170832743110"><a name="p170832743110"></a><a name="p170832743110"></a>This parameter is reserved.</p>
<p id="p161342783311"><a name="p161342783311"></a><a name="p161342783311"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row622481417593"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p15224151413595"><a name="p15224151413595"></a><a name="p15224151413595"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p622413146591"><a name="p622413146591"></a><a name="p622413146591"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p571492763113"><a name="p571492763113"></a><a name="p571492763113"></a>Specifies the value of the match content.</p>
<p id="p181971511193320"><a name="p181971511193320"></a><a name="p181971511193320"></a>The value contains a maximum of 128 characters.</p>
<a name="ul1171713278316"></a><a name="ul1171713278316"></a><ul id="ul1171713278316"><li>When <strong id="b82412164537"><a name="b82412164537"></a><a name="b82412164537"></a>type</strong> is set to <strong id="b11251516115317"><a name="b11251516115317"></a><a name="b11251516115317"></a>HOST_NAME</strong>, the value is a string of a maximum of 100 characters, contains only letters, digits, hyphens (-), and periods (.), and must start with a letter or digit.</li><li>When <strong id="b4809101715319"><a name="b4809101715319"></a><a name="b4809101715319"></a>type</strong> is set to <strong id="b7810121755310"><a name="b7810121755310"></a><a name="b7810121755310"></a>PATH</strong>, the value is a string of a maximum of 128 characters. When the value of <strong id="b421410195531"><a name="b421410195531"></a><a name="b421410195531"></a>compare_type</strong> is set to <strong id="b2215919165317"><a name="b2215919165317"></a><a name="b2215919165317"></a>STARTS_WITH</strong> or <strong id="b121681911534"><a name="b121681911534"></a><a name="b121681911534"></a>EQUAL_TO</strong>, the string must start with a slash (/) and can contain only letters, digits, and special characters _~';@^-%#&amp;$.*+?,=!:| \/()[]{}</li></ul>
</td>
</tr>
<tr id="row2224191419593"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p2022412148597"><a name="p2022412148597"></a><a name="p2022412148597"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p622431415599"><a name="p622431415599"></a><a name="p622431415599"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p1672832743114"><a name="p1672832743114"></a><a name="p1672832743114"></a>Specifies the provisioning status of the forwarding rule. The value can be <strong id="b11726102075319"><a name="b11726102075319"></a><a name="b11726102075319"></a>ACTIVE</strong>, <strong id="b10727182018534"><a name="b10727182018534"></a><a name="b10727182018534"></a>PENDING_CREATE</strong>, or <strong id="b187288206536"><a name="b187288206536"></a><a name="b187288206536"></a>ERROR</strong>.</p>
<p id="p0730172712319"><a name="p0730172712319"></a><a name="p0730172712319"></a>The default value is <strong id="b8486172295313"><a name="b8486172295313"></a><a name="b8486172295313"></a>ACTIVE</strong>.</p>
<p id="p15731227143118"><a name="p15731227143118"></a><a name="p15731227143118"></a>This parameter is reserved.</p>
<p id="p0974191614335"><a name="p0974191614335"></a><a name="p0974191614335"></a>The value contains a maximum of 16 characters.</p>
</td>
</tr>
<tr id="row19648113693111"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p164843612317"><a name="p164843612317"></a><a name="p164843612317"></a>rules_links</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p732292491914"><a name="p732292491914"></a><a name="p732292491914"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p5542991616"><a name="p5542991616"></a><a name="p5542991616"></a>Provides links to the previous or next page during pagination query, respectively.</p>
<p id="p165764116119"><a name="p165764116119"></a><a name="p165764116119"></a>This parameter exists only in the response body of pagination query.</p>
<p id="p53635145114"><a name="p53635145114"></a><a name="p53635145114"></a>For details, see <a href="#table121191126442">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **rules\_links**  parameter description

<a name="table121191126442"></a>
<table><thead align="left"><tr id="row20223825440"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p1322317218448"><a name="p1322317218448"></a><a name="p1322317218448"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p12223102174417"><a name="p12223102174417"></a><a name="p12223102174417"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p1916893712107"><a name="p1916893712107"></a><a name="p1916893712107"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row422311294414"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p6223172154412"><a name="p6223172154412"></a><a name="p6223172154412"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p11963432121013"><a name="p11963432121013"></a><a name="p11963432121013"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p1653852193312"><a name="en-us_topic_0096561531_p1653852193312"></a><a name="en-us_topic_0096561531_p1653852193312"></a>Provides links to the previous or next page during pagination query, respectively.</p>
</td>
</tr>
<tr id="row1222316274420"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1222310218449"><a name="p1222310218449"></a><a name="p1222310218449"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1022316204415"><a name="p1022316204415"></a><a name="p1022316204415"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1772113411218"><a name="p1772113411218"></a><a name="p1772113411218"></a>Specifies the prompt of the previous or next page.</p>
<p id="p422510443113"><a name="p422510443113"></a><a name="p422510443113"></a>The value can be <strong id="b12464285315"><a name="b12464285315"></a><a name="b12464285315"></a>next</strong> or <strong id="b35204245313"><a name="b35204245313"></a><a name="b35204245313"></a>previous</strong>. The value <strong id="b1218104485313"><a name="b1218104485313"></a><a name="b1218104485313"></a>next</strong> indicates the href containing the URL of the next page, and <strong id="b618213444531"><a name="b618213444531"></a><a name="b618213444531"></a>previous</strong> indicates the href containing the URL of the previous page.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section486963719554"></a>

-   Example request: Querying all forwarding rules of a specific forwarding policy

    ```
    GET https://{Endpoint}/v2.0/lbaas/l7policies/5ae0e1e7-5f0f-47a1-b39f-5d4c428a1586/rules
    ```

-   Example response

    ```
    {
        "rules": [
            {
                "compare_type": "EQUAL_TO", 
                "provisioning_status": "ACTIVE",
                "admin_state_up": true, 
                "tenant_id": "a31d2bdcf7604c0faaddb058e1e08819", 
       
                "invert": false, 
                "value": "www.test.com", 
                "key": null, 
                "type": "HOST_NAME", 
                "id": "67d8a8fa-b0dd-4bd4-a85b-671db19b2ef3"
            }, 
            {
                "compare_type": "EQUAL_TO",
                "provisioning_status": "ACTIVE", 
                "admin_state_up": true, 
                "tenant_id": "a31d2bdcf7604c0faaddb058e1e08819",
      
                "invert": false, 
                "value": "/aaa.html", 
                "key": null, 
                "type": "PATH", 
                "id": "f02b3bca-69d2-4335-a3fa-a8054e996213"
            }
        ]
    }
    ```


## Status Code<a name="section1236210248158"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

