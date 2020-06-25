# Updating a Listener<a name="EN-US_TOPIC_0096561544"></a>

## Function<a name="en-us_topic_0049139643_section56733847"></a>

This API is used to update a listener, such as listener name, description, associated backend server groups, and server certificates.

## URI<a name="en-us_topic_0049139643_section40842582"></a>

PUT /v2.0/lbaas/listeners/\{listener\_id\}

**Table  1**  Parameter description

<a name="table161976279558"></a>
<table><thead align="left"><tr id="row14233627135520"><th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.1"><p id="p12331727205511"><a name="p12331727205511"></a><a name="p12331727205511"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.2.5.1.2"><p id="p166771515176"><a name="p166771515176"></a><a name="p166771515176"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.3"><p id="p1123362745516"><a name="p1123362745516"></a><a name="p1123362745516"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.4059405940594%" id="mcps1.2.5.1.4"><p id="p4233627105518"><a name="p4233627105518"></a><a name="p4233627105518"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8233102775519"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.1 "><p id="p323352745511"><a name="p323352745511"></a><a name="p323352745511"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.2 "><p id="p1759112319179"><a name="p1759112319179"></a><a name="p1759112319179"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.3 "><p id="p8888936101710"><a name="p8888936101710"></a><a name="p8888936101710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.4059405940594%" headers="mcps1.2.5.1.4 "><p id="p12233027195517"><a name="p12233027195517"></a><a name="p12233027195517"></a>Specifies the listener ID.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="en-us_topic_0049139643_section32038923"></a>

-   If the provisioning status of the associated load balancer is not  **ACTIVE**, the listener cannot be updated.
-   Only the administrator can specify  **connection\_limit**.
-   The  **default\_pool\_id**  parameter has the following constraints:
    -   Its value cannot be the ID of any backend server group of other listeners.
    -   Its value cannot be the ID of any backend server group associated with the forwarding policies set for other listeners.

-   The relationships between the load balancer protocol and the backend server group protocol are as follows:
    -   When the load balancer protocol is  **TCP**, the backend server group protocol must be  **TCP**.
    -   When the load balancer protocol is  **UDP**, the backend server group protocol must be  **UDP**.
    -   When the load balancer protocol is  **HTTP**  or  **TERMINATED\_HTTPS**, the backend server group protocol must be  **HTTP**.


## Request<a name="section156575314510"></a>

**Table  2**  Request parameters

<a name="table1104122261919"></a>
<table><thead align="left"><tr id="row101041422141912"><th class="cellrowborder" valign="top" width="14.44%" id="mcps1.2.5.1.1"><p id="p11105152211918"><a name="p11105152211918"></a><a name="p11105152211918"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.86%" id="mcps1.2.5.1.2"><p id="p1110532213197"><a name="p1110532213197"></a><a name="p1110532213197"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.48%" id="mcps1.2.5.1.3"><p id="p118731136189"><a name="p118731136189"></a><a name="p118731136189"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.220000000000006%" id="mcps1.2.5.1.4"><p id="p1710510228197"><a name="p1710510228197"></a><a name="p1710510228197"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row010532231918"><td class="cellrowborder" valign="top" width="14.44%" headers="mcps1.2.5.1.1 "><p id="p191051422191917"><a name="p191051422191917"></a><a name="p191051422191917"></a>listener</p>
</td>
<td class="cellrowborder" valign="top" width="12.86%" headers="mcps1.2.5.1.2 "><p id="p1510520228193"><a name="p1510520228193"></a><a name="p1510520228193"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.48%" headers="mcps1.2.5.1.3 "><p id="p08731533186"><a name="p08731533186"></a><a name="p08731533186"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="56.220000000000006%" headers="mcps1.2.5.1.4 "><p id="p710522291911"><a name="p710522291911"></a><a name="p710522291911"></a>Specifies the listener. For details, see <a href="#table731744514565">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **listener**  parameter description

<a name="table731744514565"></a>
<table><thead align="left"><tr id="row54161545205611"><th class="cellrowborder" valign="top" width="24.34%" id="mcps1.2.5.1.1"><p id="p341664575620"><a name="p341664575620"></a><a name="p341664575620"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.23%" id="mcps1.2.5.1.2"><p id="p741654511563"><a name="p741654511563"></a><a name="p741654511563"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.24%" id="mcps1.2.5.1.3"><p id="p1841664515610"><a name="p1841664515610"></a><a name="p1841664515610"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47.19%" id="mcps1.2.5.1.4"><p id="p11416184516568"><a name="p11416184516568"></a><a name="p11416184516568"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row24161453564"><td class="cellrowborder" valign="top" width="24.34%" headers="mcps1.2.5.1.1 "><p id="p1141624514568"><a name="p1141624514568"></a><a name="p1141624514568"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="13.23%" headers="mcps1.2.5.1.2 "><p id="p4416184565612"><a name="p4416184565612"></a><a name="p4416184565612"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.24%" headers="mcps1.2.5.1.3 "><p id="p4416124516561"><a name="p4416124516561"></a><a name="p4416124516561"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.19%" headers="mcps1.2.5.1.4 "><p id="p19416145135616"><a name="p19416145135616"></a><a name="p19416145135616"></a>Specifies the listener name.</p>
<p id="p38262421513"><a name="p38262421513"></a><a name="p38262421513"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row241764565615"><td class="cellrowborder" valign="top" width="24.34%" headers="mcps1.2.5.1.1 "><p id="p841724555610"><a name="p841724555610"></a><a name="p841724555610"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="13.23%" headers="mcps1.2.5.1.2 "><p id="p17417114515618"><a name="p17417114515618"></a><a name="p17417114515618"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.24%" headers="mcps1.2.5.1.3 "><p id="p24176455563"><a name="p24176455563"></a><a name="p24176455563"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.19%" headers="mcps1.2.5.1.4 "><p id="p341714451563"><a name="p341714451563"></a><a name="p341714451563"></a>Provides supplementary information about the listener.</p>
<p id="p193910375315"><a name="p193910375315"></a><a name="p193910375315"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row1041719451568"><td class="cellrowborder" valign="top" width="24.34%" headers="mcps1.2.5.1.1 "><p id="p1417184515611"><a name="p1417184515611"></a><a name="p1417184515611"></a>connection_limit</p>
</td>
<td class="cellrowborder" valign="top" width="13.23%" headers="mcps1.2.5.1.2 "><p id="p134170450566"><a name="p134170450566"></a><a name="p134170450566"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.24%" headers="mcps1.2.5.1.3 "><p id="p6417134515562"><a name="p6417134515562"></a><a name="p6417134515562"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="47.19%" headers="mcps1.2.5.1.4 "><p id="p122921011101219"><a name="p122921011101219"></a><a name="p122921011101219"></a>Specifies the maximum number of connections.</p>
<p id="p1273031315128"><a name="p1273031315128"></a><a name="p1273031315128"></a>The value ranges from <strong id="b842352706194030"><a name="b842352706194030"></a><a name="b842352706194030"></a>-1</strong> to <strong id="b842352706194035"><a name="b842352706194035"></a><a name="b842352706194035"></a>2147483647</strong>.</p>
<p id="p1320141512124"><a name="p1320141512124"></a><a name="p1320141512124"></a>This parameter is reserved. Only the administrator can specify the maximum number of connections.</p>
</td>
</tr>
<tr id="row1358781513715"><td class="cellrowborder" valign="top" width="24.34%" headers="mcps1.2.5.1.1 "><p id="p177961619133720"><a name="p177961619133720"></a><a name="p177961619133720"></a>http2_enable</p>
</td>
<td class="cellrowborder" valign="top" width="13.23%" headers="mcps1.2.5.1.2 "><p id="p37966194371"><a name="p37966194371"></a><a name="p37966194371"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.24%" headers="mcps1.2.5.1.3 "><p id="p879616198379"><a name="p879616198379"></a><a name="p879616198379"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="47.19%" headers="mcps1.2.5.1.4 "><p id="p2172181721213"><a name="p2172181721213"></a><a name="p2172181721213"></a>Specifies whether to use HTTP/2.</p>
<p id="p1430264813914"><a name="p1430264813914"></a><a name="p1430264813914"></a>The value can be <strong id="b13011748153918"><a name="b13011748153918"></a><a name="b13011748153918"></a>true</strong> or <strong id="b17302148193910"><a name="b17302148193910"></a><a name="b17302148193910"></a>false</strong>.</p>
<a name="ul177871354123912"></a><a name="ul177871354123912"></a><ul id="ul177871354123912"><li><strong id="b2078715543392"><a name="b2078715543392"></a><a name="b2078715543392"></a>true</strong>: HTTP/2 is used.</li><li><strong id="b1390925603917"><a name="b1390925603917"></a><a name="b1390925603917"></a>false</strong>: HTTP/2 is not used.</li></ul>
<p id="p2811192019122"><a name="p2811192019122"></a><a name="p2811192019122"></a>This parameter is valid only when the load balancer protocol is set to <strong id="b84235270620954"><a name="b84235270620954"></a><a name="b84235270620954"></a>TERMINATED_HTTPS</strong>.</p>
</td>
</tr>
<tr id="row1741714511564"><td class="cellrowborder" valign="top" width="24.34%" headers="mcps1.2.5.1.1 "><p id="p17417545175610"><a name="p17417545175610"></a><a name="p17417545175610"></a>default_pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.23%" headers="mcps1.2.5.1.2 "><p id="p1241719453561"><a name="p1241719453561"></a><a name="p1241719453561"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.24%" headers="mcps1.2.5.1.3 "><p id="p1963855182217"><a name="p1963855182217"></a><a name="p1963855182217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.19%" headers="mcps1.2.5.1.4 "><p id="p1772112214122"><a name="p1772112214122"></a><a name="p1772112214122"></a>Specifies the ID of the associated backend server group.</p>
<p id="p14540192616121"><a name="p14540192616121"></a><a name="p14540192616121"></a>If a request does not match the forwarding policy, the request is forwarded to the default backend server group for processing. If the value is <strong id="b842352706201335"><a name="b842352706201335"></a><a name="b842352706201335"></a>null</strong>, the listener has no default backend server group.</p>
<div class="p" id="p1129132921213"><a name="p1129132921213"></a><a name="p1129132921213"></a>This parameter has the following constraints:<a name="ul7527145916134"></a><a name="ul7527145916134"></a><ul id="ul7527145916134"><li>Its value cannot be the ID of any backend server group associated with the forwarding policies set for other listeners.</li><li>Its value cannot be the ID of any backend server group associated with the forwarding policies set for other listeners.</li></ul>
</div>
<div class="p" id="p1943563171217"><a name="p1943563171217"></a><a name="p1943563171217"></a>The relationships between the load balancer protocol and the backend server group protocol are as follows:<a name="ul10547150145714"></a><a name="ul10547150145714"></a><ul id="ul10547150145714"><li>When the load balancer protocol is <strong id="b93031437394"><a name="b93031437394"></a><a name="b93031437394"></a>TCP</strong>, the backend server group protocol must be <strong id="b3304153163911"><a name="b3304153163911"></a><a name="b3304153163911"></a>TCP</strong>.</li><li>When the load balancer protocol is <strong id="b791313563911"><a name="b791313563911"></a><a name="b791313563911"></a>UDP</strong>, the backend server group protocol must be <strong id="b991455143914"><a name="b991455143914"></a><a name="b991455143914"></a>UDP</strong>.</li><li>When the load balancer protocol is <strong id="b120261010395"><a name="b120261010395"></a><a name="b120261010395"></a>HTTP</strong> or <strong id="b15205210123910"><a name="b15205210123910"></a><a name="b15205210123910"></a>TERMINATED_HTTPS</strong>, the backend server group protocol must be <strong id="b920619109397"><a name="b920619109397"></a><a name="b920619109397"></a>HTTP</strong>.</li></ul>
</div>
</td>
</tr>
<tr id="row181617417460"><td class="cellrowborder" valign="top" width="24.34%" headers="mcps1.2.5.1.1 "><p id="p8645708547"><a name="p8645708547"></a><a name="p8645708547"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="13.23%" headers="mcps1.2.5.1.2 "><p id="p12390167113820"><a name="p12390167113820"></a><a name="p12390167113820"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.24%" headers="mcps1.2.5.1.3 "><p id="p96457019548"><a name="p96457019548"></a><a name="p96457019548"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="47.19%" headers="mcps1.2.5.1.4 "><p id="p17558035131214"><a name="p17558035131214"></a><a name="p17558035131214"></a>Specifies the administrative status of the listener.</p>
<p id="p122651837121219"><a name="p122651837121219"></a><a name="p122651837121219"></a>This parameter is reserved. The value can only be <strong id="b842352706194139"><a name="b842352706194139"></a><a name="b842352706194139"></a>true</strong>.</p>
</td>
</tr>
<tr id="row2417104516568"><td class="cellrowborder" valign="top" width="24.34%" headers="mcps1.2.5.1.1 "><p id="p6417345105618"><a name="p6417345105618"></a><a name="p6417345105618"></a>default_tls_container_ref</p>
</td>
<td class="cellrowborder" valign="top" width="13.23%" headers="mcps1.2.5.1.2 "><p id="p8417445155611"><a name="p8417445155611"></a><a name="p8417445155611"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.24%" headers="mcps1.2.5.1.3 "><p id="p11417945165614"><a name="p11417945165614"></a><a name="p11417945165614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.19%" headers="mcps1.2.5.1.4 "><p id="p1751318401124"><a name="p1751318401124"></a><a name="p1751318401124"></a>Specifies the ID of the server certificate used by the listener. </p>
<p id="p6960184614316"><a name="p6960184614316"></a><a name="p6960184614316"></a>The value contains a maximum of 128 characters.</p>
<div class="note" id="note11834424141915"><a name="note11834424141915"></a><a name="note11834424141915"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p4834524191915"><a name="p4834524191915"></a><a name="p4834524191915"></a>This parameter is valid only when <strong id="b1057311774211"><a name="b1057311774211"></a><a name="b1057311774211"></a>protocol</strong> is set to <strong id="b3573131718426"><a name="b3573131718426"></a><a name="b3573131718426"></a>TERMINATED_HTTPS</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row18418164517561"><td class="cellrowborder" valign="top" width="24.34%" headers="mcps1.2.5.1.1 "><p id="p641810458566"><a name="p641810458566"></a><a name="p641810458566"></a>client_ca_tls_container_ref</p>
</td>
<td class="cellrowborder" valign="top" width="13.23%" headers="mcps1.2.5.1.2 "><p id="p441884518560"><a name="p441884518560"></a><a name="p441884518560"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.24%" headers="mcps1.2.5.1.3 "><p id="p15418154555619"><a name="p15418154555619"></a><a name="p15418154555619"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.19%" headers="mcps1.2.5.1.4 "><p id="p1744120112011"><a name="p1744120112011"></a><a name="p1744120112011"></a>Specifies the ID of the CA certificate used by the listener. </p>
<p id="p8118561831"><a name="p8118561831"></a><a name="p8118561831"></a>The value contains a maximum of 128 characters.</p>
<div class="note" id="note10785192018522"><a name="note10785192018522"></a><a name="note10785192018522"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p2786020105210"><a name="p2786020105210"></a><a name="p2786020105210"></a>This parameter is valid only when <strong id="b9850119104210"><a name="b9850119104210"></a><a name="b9850119104210"></a>protocol</strong> is set to <strong id="b8852519184216"><a name="b8852519184216"></a><a name="b8852519184216"></a>TERMINATED_HTTPS</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row196971413121317"><td class="cellrowborder" valign="top" width="24.34%" headers="mcps1.2.5.1.1 "><p id="p76977135137"><a name="p76977135137"></a><a name="p76977135137"></a>sni_container_refs</p>
</td>
<td class="cellrowborder" valign="top" width="13.23%" headers="mcps1.2.5.1.2 "><p id="p6697813171310"><a name="p6697813171310"></a><a name="p6697813171310"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.24%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0096561533_p422512115486"><a name="en-us_topic_0096561533_p422512115486"></a><a name="en-us_topic_0096561533_p422512115486"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="47.19%" headers="mcps1.2.5.1.4 "><p id="p199055457125"><a name="p199055457125"></a><a name="p199055457125"></a>Lists the IDs of SNI certificates (server certificates with a domain name) used by the listener.</p>
<p id="p1259148121215"><a name="p1259148121215"></a><a name="p1259148121215"></a>If the parameter value is an empty list, the SNI feature is disabled.</p>
<div class="note" id="note42979249526"><a name="note42979249526"></a><a name="note42979249526"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1329752414524"><a name="p1329752414524"></a><a name="p1329752414524"></a>This parameter is valid only when <strong id="b773042017429"><a name="b773042017429"></a><a name="b773042017429"></a>protocol</strong> is set to <strong id="b873162024210"><a name="b873162024210"></a><a name="b873162024210"></a>TERMINATED_HTTPS</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row139481915361"><td class="cellrowborder" valign="top" width="24.34%" headers="mcps1.2.5.1.1 "><p id="p108551029191718"><a name="p108551029191718"></a><a name="p108551029191718"></a>tls_ciphers_policy</p>
</td>
<td class="cellrowborder" valign="top" width="13.23%" headers="mcps1.2.5.1.2 "><p id="p1985511298179"><a name="p1985511298179"></a><a name="p1985511298179"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.24%" headers="mcps1.2.5.1.3 "><p id="p18855429181713"><a name="p18855429181713"></a><a name="p18855429181713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47.19%" headers="mcps1.2.5.1.4 "><p id="p39741913115313"><a name="p39741913115313"></a><a name="p39741913115313"></a>Specifies the security policy used by the listener. This parameter is valid only when the listener protocol is set to <strong id="b1790442618139"><a name="b1790442618139"></a><a name="b1790442618139"></a>TERMINATED_HTTPS</strong>.</p>
<p id="p567518010317"><a name="p567518010317"></a><a name="p567518010317"></a>The value can be <strong id="b1036891194516"><a name="b1036891194516"></a><a name="b1036891194516"></a>tls-1-0</strong>, <strong id="b143681911114510"><a name="b143681911114510"></a><a name="b143681911114510"></a>tls-1-1</strong>, <strong id="b136961184510"><a name="b136961184510"></a><a name="b136961184510"></a>tls-1-2</strong>, or <strong id="b83691113456"><a name="b83691113456"></a><a name="b83691113456"></a>tls-1-2-strict</strong>, and the default value is <strong id="b8370181184519"><a name="b8370181184519"></a><a name="b8370181184519"></a>tls-1-0</strong>. For details of cipher suites for each security policy, see <a href="#table15427162993713">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **tls\_ciphers\_policy**  parameter description

<a name="table15427162993713"></a>
<table><thead align="left"><tr id="en-us_topic_0096561542_row204784101539"><th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561542_p147851075312"><a name="en-us_topic_0096561542_p147851075312"></a><a name="en-us_topic_0096561542_p147851075312"></a>Security Policy</p>
</th>
<th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561542_p2478181015313"><a name="en-us_topic_0096561542_p2478181015313"></a><a name="en-us_topic_0096561542_p2478181015313"></a>TLS Version</p>
</th>
<th class="cellrowborder" valign="top" width="69.69696969696969%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561542_p5478131085310"><a name="en-us_topic_0096561542_p5478131085310"></a><a name="en-us_topic_0096561542_p5478131085310"></a>Cipher Suite</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561542_row125843182408"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p12584131812401"><a name="en-us_topic_0096561542_p12584131812401"></a><a name="en-us_topic_0096561542_p12584131812401"></a>tls-1-0</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p1358411811405"><a name="en-us_topic_0096561542_p1358411811405"></a><a name="en-us_topic_0096561542_p1358411811405"></a>TLSv1.2 TLSv1.1 TLSv1</p>
</td>
<td class="cellrowborder" rowspan="3" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p152111143203617"><a name="en-us_topic_0096561542_p152111143203617"></a><a name="en-us_topic_0096561542_p152111143203617"></a>ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:AES128-SHA256:AES256-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:AES128-SHA:AES256-SHA</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row1250119222406"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p050232216409"><a name="en-us_topic_0096561542_p050232216409"></a><a name="en-us_topic_0096561542_p050232216409"></a>tls-1-1</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p185021822194019"><a name="en-us_topic_0096561542_p185021822194019"></a><a name="en-us_topic_0096561542_p185021822194019"></a>TLSv1.2 TLSv1.1</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row19159426144017"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p31598266400"><a name="en-us_topic_0096561542_p31598266400"></a><a name="en-us_topic_0096561542_p31598266400"></a>tls-1-2</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p315914265406"><a name="en-us_topic_0096561542_p315914265406"></a><a name="en-us_topic_0096561542_p315914265406"></a>TLSv1.2</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row148501331204010"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p18850153164010"><a name="en-us_topic_0096561542_p18850153164010"></a><a name="en-us_topic_0096561542_p18850153164010"></a>tls-1-2-strict</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p3850531104014"><a name="en-us_topic_0096561542_p3850531104014"></a><a name="en-us_topic_0096561542_p3850531104014"></a>TLSv1.2</p>
</td>
<td class="cellrowborder" valign="top" width="69.69696969696969%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p12274148203711"><a name="en-us_topic_0096561542_p12274148203711"></a><a name="en-us_topic_0096561542_p12274148203711"></a>ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:AES128-SHA256:AES256-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section1747815593616"></a>

**Table  5**  Response parameters

<a name="table860073013198"></a>
<table><thead align="left"><tr id="row1860103031913"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="p10601730151913"><a name="p10601730151913"></a><a name="p10601730151913"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.2"><p id="p186011330181914"><a name="p186011330181914"></a><a name="p186011330181914"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.2.4.1.3"><p id="p344893632310"><a name="p344893632310"></a><a name="p344893632310"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row760313081917"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="p14603730171917"><a name="p14603730171917"></a><a name="p14603730171917"></a>listener</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p9603130131913"><a name="p9603130131913"></a><a name="p9603130131913"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.4.1.3 "><p id="p66031330141919"><a name="p66031330141919"></a><a name="p66031330141919"></a>Specifies the listener. For details, see <a href="#table99341410115717">Table 6</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **listeners**  parameter description

<a name="table99341410115717"></a>
<table><thead align="left"><tr id="en-us_topic_0096561542_row34671725195410"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561542_p946792525418"><a name="en-us_topic_0096561542_p946792525418"></a><a name="en-us_topic_0096561542_p946792525418"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561542_p8467142519541"><a name="en-us_topic_0096561542_p8467142519541"></a><a name="en-us_topic_0096561542_p8467142519541"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561542_p104671125165411"><a name="en-us_topic_0096561542_p104671125165411"></a><a name="en-us_topic_0096561542_p104671125165411"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561542_row12467122519549"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p8467425205419"><a name="en-us_topic_0096561542_p8467425205419"></a><a name="en-us_topic_0096561542_p8467425205419"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p3467192515543"><a name="en-us_topic_0096561542_p3467192515543"></a><a name="en-us_topic_0096561542_p3467192515543"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p9467132535416"><a name="en-us_topic_0096561542_p9467132535416"></a><a name="en-us_topic_0096561542_p9467132535416"></a>Specifies the listener ID.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row124679252544"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p44682025175413"><a name="en-us_topic_0096561542_p44682025175413"></a><a name="en-us_topic_0096561542_p44682025175413"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p146811253546"><a name="en-us_topic_0096561542_p146811253546"></a><a name="en-us_topic_0096561542_p146811253546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p19468192515548"><a name="en-us_topic_0096561542_p19468192515548"></a><a name="en-us_topic_0096561542_p19468192515548"></a>Specifies the ID of the project where the listener is used.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row746816255547"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p184683251549"><a name="en-us_topic_0096561542_p184683251549"></a><a name="en-us_topic_0096561542_p184683251549"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p1046842519548"><a name="en-us_topic_0096561542_p1046842519548"></a><a name="en-us_topic_0096561542_p1046842519548"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p44681425125418"><a name="en-us_topic_0096561542_p44681425125418"></a><a name="en-us_topic_0096561542_p44681425125418"></a>Specifies the listener name.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row1046812512541"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p546862545411"><a name="en-us_topic_0096561542_p546862545411"></a><a name="en-us_topic_0096561542_p546862545411"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p154685252543"><a name="en-us_topic_0096561542_p154685252543"></a><a name="en-us_topic_0096561542_p154685252543"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p14468172517540"><a name="en-us_topic_0096561542_p14468172517540"></a><a name="en-us_topic_0096561542_p14468172517540"></a>Provides supplementary information about the listener.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row1046832595418"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p17468125125414"><a name="en-us_topic_0096561542_p17468125125414"></a><a name="en-us_topic_0096561542_p17468125125414"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p746811255546"><a name="en-us_topic_0096561542_p746811255546"></a><a name="en-us_topic_0096561542_p746811255546"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p201601841193216"><a name="en-us_topic_0096561542_p201601841193216"></a><a name="en-us_topic_0096561542_p201601841193216"></a>Specifies the load balancer protocol.</p>
<p id="en-us_topic_0096561542_p0300344103218"><a name="en-us_topic_0096561542_p0300344103218"></a><a name="en-us_topic_0096561542_p0300344103218"></a>The value can be <strong id="en-us_topic_0096561542_b103871119189"><a name="en-us_topic_0096561542_b103871119189"></a><a name="en-us_topic_0096561542_b103871119189"></a>TCP</strong>, <strong id="en-us_topic_0096561542_b1038921117183"><a name="en-us_topic_0096561542_b1038921117183"></a><a name="en-us_topic_0096561542_b1038921117183"></a>HTTP</strong>, <strong id="en-us_topic_0096561542_b183906115182"><a name="en-us_topic_0096561542_b183906115182"></a><a name="en-us_topic_0096561542_b183906115182"></a>UDP</strong>, or <strong id="en-us_topic_0096561542_b193911311181810"><a name="en-us_topic_0096561542_b193911311181810"></a><a name="en-us_topic_0096561542_b193911311181810"></a>TERMINATED_HTTPS</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row1346912520548"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p144691225205414"><a name="en-us_topic_0096561542_p144691225205414"></a><a name="en-us_topic_0096561542_p144691225205414"></a>protocol_port</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p446952515416"><a name="en-us_topic_0096561542_p446952515416"></a><a name="en-us_topic_0096561542_p446952515416"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p18323468323"><a name="en-us_topic_0096561542_p18323468323"></a><a name="en-us_topic_0096561542_p18323468323"></a>Specifies the port used by the load balancer.</p>
<p id="en-us_topic_0096561542_p7688104743213"><a name="en-us_topic_0096561542_p7688104743213"></a><a name="en-us_topic_0096561542_p7688104743213"></a>The port number ranges from 1 to 65535.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row1546932511547"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p19469202585413"><a name="en-us_topic_0096561542_p19469202585413"></a><a name="en-us_topic_0096561542_p19469202585413"></a>loadbalancers</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p546911258548"><a name="en-us_topic_0096561542_p546911258548"></a><a name="en-us_topic_0096561542_p546911258548"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p16788191994017"><a name="en-us_topic_0096561542_p16788191994017"></a><a name="en-us_topic_0096561542_p16788191994017"></a>Specifies the ID of the associated load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row16469625125411"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p3469112575415"><a name="en-us_topic_0096561542_p3469112575415"></a><a name="en-us_topic_0096561542_p3469112575415"></a>connection_limit</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p144691725185411"><a name="en-us_topic_0096561542_p144691725185411"></a><a name="en-us_topic_0096561542_p144691725185411"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p636816504321"><a name="en-us_topic_0096561542_p636816504321"></a><a name="en-us_topic_0096561542_p636816504321"></a>Specifies the maximum number of connections.</p>
<p id="en-us_topic_0096561542_p17992184321313"><a name="en-us_topic_0096561542_p17992184321313"></a><a name="en-us_topic_0096561542_p17992184321313"></a>The value ranges from <strong id="en-us_topic_0096561542_b1262188182"><a name="en-us_topic_0096561542_b1262188182"></a><a name="en-us_topic_0096561542_b1262188182"></a>-1</strong> to <strong id="en-us_topic_0096561542_b182018161820"><a name="en-us_topic_0096561542_b182018161820"></a><a name="en-us_topic_0096561542_b182018161820"></a>2147483647</strong>. The default value is <strong id="en-us_topic_0096561542_b780161918188"><a name="en-us_topic_0096561542_b780161918188"></a><a name="en-us_topic_0096561542_b780161918188"></a>-1</strong>, indicating that there is no restriction on maximum connections.</p>
<p id="en-us_topic_0096561542_p8758551203215"><a name="en-us_topic_0096561542_p8758551203215"></a><a name="en-us_topic_0096561542_p8758551203215"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row44691325175419"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p446922525410"><a name="en-us_topic_0096561542_p446922525410"></a><a name="en-us_topic_0096561542_p446922525410"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p3469102512549"><a name="en-us_topic_0096561542_p3469102512549"></a><a name="en-us_topic_0096561542_p3469102512549"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p257371723315"><a name="en-us_topic_0096561542_p257371723315"></a><a name="en-us_topic_0096561542_p257371723315"></a>Specifies the administrative status of the listener.</p>
<p id="en-us_topic_0096561542_p1316712043315"><a name="en-us_topic_0096561542_p1316712043315"></a><a name="en-us_topic_0096561542_p1316712043315"></a>This parameter is reserved. The value can only be <strong id="en-us_topic_0096561542_b17553924141815"><a name="en-us_topic_0096561542_b17553924141815"></a><a name="en-us_topic_0096561542_b17553924141815"></a>true</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row155261945821"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p149771721230"><a name="en-us_topic_0096561542_p149771721230"></a><a name="en-us_topic_0096561542_p149771721230"></a>http2_enable</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p149775217319"><a name="en-us_topic_0096561542_p149775217319"></a><a name="en-us_topic_0096561542_p149775217319"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p483792111330"><a name="en-us_topic_0096561542_p483792111330"></a><a name="en-us_topic_0096561542_p483792111330"></a>Specifies whether to use HTTP/2.</p>
<p id="en-us_topic_0096561542_p183584202475"><a name="en-us_topic_0096561542_p183584202475"></a><a name="en-us_topic_0096561542_p183584202475"></a>The value can be <strong id="en-us_topic_0096561542_b53581020204716"><a name="en-us_topic_0096561542_b53581020204716"></a><a name="en-us_topic_0096561542_b53581020204716"></a>true</strong> or <strong id="en-us_topic_0096561542_b93584201473"><a name="en-us_topic_0096561542_b93584201473"></a><a name="en-us_topic_0096561542_b93584201473"></a>false</strong>.</p>
<a name="en-us_topic_0096561542_ul2055452614479"></a><a name="en-us_topic_0096561542_ul2055452614479"></a><ul id="en-us_topic_0096561542_ul2055452614479"><li><strong id="en-us_topic_0096561542_b155372615476"><a name="en-us_topic_0096561542_b155372615476"></a><a name="en-us_topic_0096561542_b155372615476"></a>true</strong>: HTTP/2 is used.</li><li><strong id="en-us_topic_0096561542_b366918288476"><a name="en-us_topic_0096561542_b366918288476"></a><a name="en-us_topic_0096561542_b366918288476"></a>false</strong>: HTTP/2 is not used.</li></ul>
<p id="en-us_topic_0096561542_p3519192712331"><a name="en-us_topic_0096561542_p3519192712331"></a><a name="en-us_topic_0096561542_p3519192712331"></a>This parameter is valid only when the load balancer protocol is set to <strong id="en-us_topic_0096561542_b167901226151113"><a name="en-us_topic_0096561542_b167901226151113"></a><a name="en-us_topic_0096561542_b167901226151113"></a>TERMINATED_HTTPS</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row1547012555419"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p20470112585411"><a name="en-us_topic_0096561542_p20470112585411"></a><a name="en-us_topic_0096561542_p20470112585411"></a>default_pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p9470525195410"><a name="en-us_topic_0096561542_p9470525195410"></a><a name="en-us_topic_0096561542_p9470525195410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p3466142973313"><a name="en-us_topic_0096561542_p3466142973313"></a><a name="en-us_topic_0096561542_p3466142973313"></a>Specifies the ID of the associated backend server group.</p>
<p id="en-us_topic_0096561542_p149661432143316"><a name="en-us_topic_0096561542_p149661432143316"></a><a name="en-us_topic_0096561542_p149661432143316"></a>If a request does not match the forwarding policy, the request is forwarded to the default backend server group for processing. If the value is <strong id="en-us_topic_0096561542_b125951581919"><a name="en-us_topic_0096561542_b125951581919"></a><a name="en-us_topic_0096561542_b125951581919"></a>null</strong>, the listener has no default backend server group.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row94701258544"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p114701625185416"><a name="en-us_topic_0096561542_p114701625185416"></a><a name="en-us_topic_0096561542_p114701625185416"></a>default_tls_container_ref</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p194705259542"><a name="en-us_topic_0096561542_p194705259542"></a><a name="en-us_topic_0096561542_p194705259542"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p8103123513337"><a name="en-us_topic_0096561542_p8103123513337"></a><a name="en-us_topic_0096561542_p8103123513337"></a>Specifies the ID of the server certificate used by the listener. For details, see <a href="certificate_enhanced.rst">Certificate</a>.</p>
<p id="en-us_topic_0096561542_p15749173783317"><a name="en-us_topic_0096561542_p15749173783317"></a><a name="en-us_topic_0096561542_p15749173783317"></a>This parameter is mandatory when <strong id="en-us_topic_0096561542_b771517531197"><a name="en-us_topic_0096561542_b771517531197"></a><a name="en-us_topic_0096561542_b771517531197"></a>protocol</strong> is set to <strong id="en-us_topic_0096561542_b11716753181920"><a name="en-us_topic_0096561542_b11716753181920"></a><a name="en-us_topic_0096561542_b11716753181920"></a>TERMINATED_HTTPS</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row174701325205420"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p347010254548"><a name="en-us_topic_0096561542_p347010254548"></a><a name="en-us_topic_0096561542_p347010254548"></a>client_ca_tls_container_ref</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p4470825185414"><a name="en-us_topic_0096561542_p4470825185414"></a><a name="en-us_topic_0096561542_p4470825185414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p1867105844415"><a name="en-us_topic_0096561542_p1867105844415"></a><a name="en-us_topic_0096561542_p1867105844415"></a>Specifies the ID of the CA certificate used by the listener. For details, see <a href="certificate_enhanced.rst">Certificate</a>.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row1947122517545"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p1247117256543"><a name="en-us_topic_0096561542_p1247117256543"></a><a name="en-us_topic_0096561542_p1247117256543"></a>sni_container_refs</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p7471172515547"><a name="en-us_topic_0096561542_p7471172515547"></a><a name="en-us_topic_0096561542_p7471172515547"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p33961341163319"><a name="en-us_topic_0096561542_p33961341163319"></a><a name="en-us_topic_0096561542_p33961341163319"></a>Lists the IDs of SNI certificates (server certificates with a domain name) used by the listener.</p>
<p id="en-us_topic_0096561542_p8259184619337"><a name="en-us_topic_0096561542_p8259184619337"></a><a name="en-us_topic_0096561542_p8259184619337"></a>If the parameter value is an empty list, the SNI feature is disabled.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row18840123882117"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p38408381214"><a name="en-us_topic_0096561542_p38408381214"></a><a name="en-us_topic_0096561542_p38408381214"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p12840538162110"><a name="en-us_topic_0096561542_p12840538162110"></a><a name="en-us_topic_0096561542_p12840538162110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p19840203842114"><a name="en-us_topic_0096561542_p19840203842114"></a><a name="en-us_topic_0096561542_p19840203842114"></a>Tags the listener.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row109815596568"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p18781627124910"><a name="en-us_topic_0096561542_p18781627124910"></a><a name="en-us_topic_0096561542_p18781627124910"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p18781627204916"><a name="en-us_topic_0096561542_p18781627204916"></a><a name="en-us_topic_0096561542_p18781627204916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p15848951122220"><a name="en-us_topic_0096561542_p15848951122220"></a><a name="en-us_topic_0096561542_p15848951122220"></a>Specifies the time when the listener was created. The UTC time is in <em id="en-us_topic_0096561542_i1017723733015"><a name="en-us_topic_0096561542_i1017723733015"></a><a name="en-us_topic_0096561542_i1017723733015"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row122703319572"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p1541843114495"><a name="en-us_topic_0096561542_p1541843114495"></a><a name="en-us_topic_0096561542_p1541843114495"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p1810172112506"><a name="en-us_topic_0096561542_p1810172112506"></a><a name="en-us_topic_0096561542_p1810172112506"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p341843144919"><a name="en-us_topic_0096561542_p341843144919"></a><a name="en-us_topic_0096561542_p341843144919"></a>Specifies the time when the listener was updated. The UTC time is in <em id="en-us_topic_0096561542_i12883301256"><a name="en-us_topic_0096561542_i12883301256"></a><a name="en-us_topic_0096561542_i12883301256"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
</td>
</tr>
<tr id="en-us_topic_0096561542_row674511497493"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561542_p15804713184311"><a name="en-us_topic_0096561542_p15804713184311"></a><a name="en-us_topic_0096561542_p15804713184311"></a>tls_ciphers_policy</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561542_p78041413134319"><a name="en-us_topic_0096561542_p78041413134319"></a><a name="en-us_topic_0096561542_p78041413134319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561542_p546123425013"><a name="en-us_topic_0096561542_p546123425013"></a><a name="en-us_topic_0096561542_p546123425013"></a>Specifies the security policy used by the listener. This parameter is valid only when the load balancer protocol is set to <strong id="en-us_topic_0096561542_b156051134122510"><a name="en-us_topic_0096561542_b156051134122510"></a><a name="en-us_topic_0096561542_b156051134122510"></a>TERMINATED_HTTPS</strong>.</p>
<p id="en-us_topic_0096561542_p3241114918325"><a name="en-us_topic_0096561542_p3241114918325"></a><a name="en-us_topic_0096561542_p3241114918325"></a>The value can be <strong id="en-us_topic_0096561542_b13885173792519"><a name="en-us_topic_0096561542_b13885173792519"></a><a name="en-us_topic_0096561542_b13885173792519"></a>tls-1-0</strong>, <strong id="en-us_topic_0096561542_b15887123752517"><a name="en-us_topic_0096561542_b15887123752517"></a><a name="en-us_topic_0096561542_b15887123752517"></a>tls-1-1</strong>, <strong id="en-us_topic_0096561542_b9887123742520"><a name="en-us_topic_0096561542_b9887123742520"></a><a name="en-us_topic_0096561542_b9887123742520"></a>tls-1-2</strong>, or <strong id="en-us_topic_0096561542_b13889133713252"><a name="en-us_topic_0096561542_b13889133713252"></a><a name="en-us_topic_0096561542_b13889133713252"></a>tls-1-2-strict</strong>, and the default value is <strong id="en-us_topic_0096561542_b2088953792517"><a name="en-us_topic_0096561542_b2088953792517"></a><a name="en-us_topic_0096561542_b2088953792517"></a>tls-1-0</strong>. For details of cipher suites for each security policy, see <a href="adding-a-listener-enhanced.md#table1247813103533">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section1135692595416"></a>

-   Example request: Updating a listener

    ```
    PUT https://{Endpoint}/v2.0/lbaas/listeners/f622c150-72f5-4263-a47a-e5003c652aa3
    
    {  
        "listener": {  
            "description": "my listener",  
            "name": "listener-jy-test2", 
            "default_pool_id": "c61310de-9a06-4f0c-850c-6f4797b9984c", 
            "default_tls_container_ref": "23b58a961a4d4c95be585e98046e657a", 
            "client_ca_tls_container_ref": "417a0976969f497db8cbb083bff343ba"
        }  
    }
    ```


-   Example response

    ```
    {
        "listener": {
            "client_ca_tls_container_ref": "417a0976969f497db8cbb083bff343ba",
            "protocol": "TERMINATED_HTTPS",
            "description": "my listener",
            "default_tls_container_ref": "23b58a961a4d4c95be585e98046e657a",
            "admin_state_up": true,
            "http2_enable": false,
            "loadbalancers": [
                {
                    "id": "165b6a38-5278-4569-b747-b2ee65ea84a4"
                }
            ],
            "tenant_id": "601240b9c5c94059b63d484c92cfe308",
     
            "sni_container_refs": [],
            "connection_limit": -1,
            "protocol_port": 443,
            "tags": [],
            "default_pool_id": "c61310de-9a06-4f0c-850c-6f4797b9984c",
            "id": "f622c150-72f5-4263-a47a-e5003c652aa3",
            "name": "listener-jy-test2",
            "tls_ciphers_policy": "tls-1-0", 
            "created_at": "2018-07-25T01:54:13", 
            "updated_at": "2018-07-25T01:54:14"
      
        }
    }
    ```


## Status Code<a name="en-us_topic_0049139643_section408842"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

