# Updating Alarm Notification Configurations<a name="EN-US_TOPIC_0193631122"></a>

## Function Description<a name="section12455270"></a>

This API is used to update alarm notification configurations.

## URI<a name="section2243982"></a>

-   URI format

    PUT /v1/\{project\_id\}/waf/config/alert/\{alertconfig\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table31420987"></a>
    <table><thead align="left"><tr id="row6087910"><th class="cellrowborder" valign="top" width="17.528247175282473%" id="mcps1.2.5.1.1"><p id="p23358735"><a name="p23358735"></a><a name="p23358735"></a><strong id="b84708559510"><a name="b84708559510"></a><a name="b84708559510"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.58804119588041%" id="mcps1.2.5.1.2"><p id="p13009388"><a name="p13009388"></a><a name="p13009388"></a><strong id="b1977525605112"><a name="b1977525605112"></a><a name="b1977525605112"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.58804119588041%" id="mcps1.2.5.1.3"><p id="p47127526"><a name="p47127526"></a><a name="p47127526"></a><strong id="b423135825113"><a name="b423135825113"></a><a name="b423135825113"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.295670432956705%" id="mcps1.2.5.1.4"><p id="p59233252"><a name="p59233252"></a><a name="p59233252"></a><strong id="b176521659165114"><a name="b176521659165114"></a><a name="b176521659165114"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row33164111"><td class="cellrowborder" valign="top" width="17.528247175282473%" headers="mcps1.2.5.1.1 "><p id="p1938446"><a name="p1938446"></a><a name="p1938446"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p22796426"><a name="p22796426"></a><a name="p22796426"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.3 "><p id="p34571178"><a name="p34571178"></a><a name="p34571178"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.295670432956705%" headers="mcps1.2.5.1.4 "><p id="p48802006"><a name="p48802006"></a><a name="p48802006"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row36564877"><td class="cellrowborder" valign="top" width="17.528247175282473%" headers="mcps1.2.5.1.1 "><p id="p8965047"><a name="p8965047"></a><a name="p8965047"></a>alertconfig_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p55080226"><a name="p55080226"></a><a name="p55080226"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.3 "><p id="p32313334"><a name="p32313334"></a><a name="p32313334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.295670432956705%" headers="mcps1.2.5.1.4 "><p id="p134361"><a name="p134361"></a><a name="p134361"></a>Specifies the ID of the alarm notification configuration to be updated. For details about how to query the alarm configuration ID, see <a href="querying-alarm-notification-configurations.md">Querying Alarm Notification Configurations</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section20195840"></a>

Request parameters

**Table  2**  Parameter description

<a name="table30841001"></a>
<table><thead align="left"><tr id="row28720700"><th class="cellrowborder" valign="top" width="17.528247175282473%" id="mcps1.2.5.1.1"><p id="p44675403"><a name="p44675403"></a><a name="p44675403"></a><strong id="b1194253735211"><a name="b1194253735211"></a><a name="b1194253735211"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.58804119588041%" id="mcps1.2.5.1.2"><p id="p61937923"><a name="p61937923"></a><a name="p61937923"></a><strong id="b2439239195213"><a name="b2439239195213"></a><a name="b2439239195213"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.58804119588041%" id="mcps1.2.5.1.3"><p id="p50915851"><a name="p50915851"></a><a name="p50915851"></a><strong id="b15881184045211"><a name="b15881184045211"></a><a name="b15881184045211"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43.295670432956705%" id="mcps1.2.5.1.4"><p id="p30543243"><a name="p30543243"></a><a name="p30543243"></a><strong id="b171701442135213"><a name="b171701442135213"></a><a name="b171701442135213"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row58083628"><td class="cellrowborder" valign="top" width="17.528247175282473%" headers="mcps1.2.5.1.1 "><p id="p7153429"><a name="p7153429"></a><a name="p7153429"></a>enabled</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p42556911"><a name="p42556911"></a><a name="p42556911"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.3 "><p id="p24557794"><a name="p24557794"></a><a name="p24557794"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="43.295670432956705%" headers="mcps1.2.5.1.4 "><p id="p155702112116"><a name="p155702112116"></a><a name="p155702112116"></a>Specifies whether to send an alarm notification.</p>
<a name="ul11892104301314"></a><a name="ul11892104301314"></a><ul id="ul11892104301314"><li><strong id="b1054620558265"><a name="b1054620558265"></a><a name="b1054620558265"></a>true</strong>: Send the alarm notification.</li><li><strong id="b487454872614"><a name="b487454872614"></a><a name="b487454872614"></a>false</strong>: Do not send the alarm notification.</li></ul>
</td>
</tr>
<tr id="row51674174"><td class="cellrowborder" valign="top" width="17.528247175282473%" headers="mcps1.2.5.1.1 "><p id="p24858548"><a name="p24858548"></a><a name="p24858548"></a>topic_urn</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p276544"><a name="p276544"></a><a name="p276544"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.3 "><p id="p22400071"><a name="p22400071"></a><a name="p22400071"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.295670432956705%" headers="mcps1.2.5.1.4 "><p id="p2466483"><a name="p2466483"></a><a name="p2466483"></a>Specifies the SMN topic to which an alarm is sent.</p>
<div class="note" id="note154521052162615"><a name="note154521052162615"></a><a name="note154521052162615"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1045313528261"><a name="p1045313528261"></a><a name="p1045313528261"></a>The selected topic must be a topic whose subscription information has been configured on the SMN console.</p>
</div></div>
</td>
</tr>
<tr id="row22198355"><td class="cellrowborder" valign="top" width="17.528247175282473%" headers="mcps1.2.5.1.1 "><p id="p53236305"><a name="p53236305"></a><a name="p53236305"></a>sendfreq</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p17173415"><a name="p17173415"></a><a name="p17173415"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.3 "><p id="p48869374"><a name="p48869374"></a><a name="p48869374"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43.295670432956705%" headers="mcps1.2.5.1.4 "><p id="p12326947425"><a name="p12326947425"></a><a name="p12326947425"></a>Specifies the minimum interval between two alarms in minutes. The options are <strong id="b598212207298"><a name="b598212207298"></a><a name="b598212207298"></a>5</strong>, <strong id="b1498210208299"><a name="b1498210208299"></a><a name="b1498210208299"></a>15</strong>, <strong id="b8983172018297"><a name="b8983172018297"></a><a name="b8983172018297"></a>30</strong>, and <strong id="b1298392016292"><a name="b1298392016292"></a><a name="b1298392016292"></a>60</strong>.</p>
</td>
</tr>
<tr id="row58076012"><td class="cellrowborder" valign="top" width="17.528247175282473%" headers="mcps1.2.5.1.1 "><p id="p6536507"><a name="p6536507"></a><a name="p6536507"></a>times</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p59695047"><a name="p59695047"></a><a name="p59695047"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.3 "><p id="p3460599"><a name="p3460599"></a><a name="p3460599"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43.295670432956705%" headers="mcps1.2.5.1.4 "><p id="p833113471522"><a name="p833113471522"></a><a name="p833113471522"></a>Specifies the alarm threshold. Alarm notifications are sent when the number of attacks is greater than or equal to the threshold within the configured period. This value is greater than or equal to <strong id="b179911625162711"><a name="b179911625162711"></a><a name="b179911625162711"></a>1</strong>.</p>
</td>
</tr>
<tr id="row39748818"><td class="cellrowborder" valign="top" width="17.528247175282473%" headers="mcps1.2.5.1.1 "><p id="p65537676"><a name="p65537676"></a><a name="p65537676"></a>threat</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p6951559"><a name="p6951559"></a><a name="p6951559"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.3 "><p id="p26205419"><a name="p26205419"></a><a name="p26205419"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="43.295670432956705%" headers="mcps1.2.5.1.4 "><p id="p42264158"><a name="p42264158"></a><a name="p42264158"></a>Specifies the list of event types.</p>
<a name="ul527919447315"></a><a name="ul527919447315"></a><ul id="ul527919447315"><li><strong id="b209171815103210"><a name="b209171815103210"></a><a name="b209171815103210"></a>all</strong> refers to all types of events.</li><li><span class="parmvalue" id="parmvalue950934320599"><a name="parmvalue950934320599"></a><a name="parmvalue950934320599"></a><b>cc</b></span> refers to CC attack.</li><li><span class="parmvalue" id="parmvalue8746852848"><a name="parmvalue8746852848"></a><a name="parmvalue8746852848"></a><b>cmdi</b></span> refers to command injection.</li><li><span class="parmvalue" id="parmvalue1293617551746"><a name="parmvalue1293617551746"></a><a name="parmvalue1293617551746"></a><b>custom</b></span> refers to Precise Protection events.</li><li><span class="parmvalue" id="parmvalue4445735943"><a name="parmvalue4445735943"></a><a name="parmvalue4445735943"></a><b>illegal</b></span> refers to invalid requests.</li><li><span class="parmvalue" id="parmvalue095312591241"><a name="parmvalue095312591241"></a><a name="parmvalue095312591241"></a><b>sqli</b></span> refers to SQL injection.</li><li><span class="parmvalue" id="parmvalue561033517"><a name="parmvalue561033517"></a><a name="parmvalue561033517"></a><b>lfi</b></span> refers to local file inclusion.</li><li><strong id="b11501862511"><a name="b11501862511"></a><a name="b11501862511"></a>robot</strong> refers to malicious crawlers.</li><li><span class="parmvalue" id="parmvalue1078113311833"><a name="parmvalue1078113311833"></a><a name="parmvalue1078113311833"></a><b>antitamper</b></span> refers to Web Tamper Protection events.</li><li><span class="parmvalue" id="parmvalue137765121957"><a name="parmvalue137765121957"></a><a name="parmvalue137765121957"></a><b>rfi</b></span> refers to remote file inclusion.</li><li><span class="parmvalue" id="parmvalue1092168516"><a name="parmvalue1092168516"></a><a name="parmvalue1092168516"></a><b>vuln</b></span> refers to other types of attacks.</li><li><span class="parmvalue" id="parmvalue18629181910520"><a name="parmvalue18629181910520"></a><a name="parmvalue18629181910520"></a><b>xss</b></span> refers to XSS attack.</li><li><span class="parmvalue" id="parmvalue255119221157"><a name="parmvalue255119221157"></a><a name="parmvalue255119221157"></a><b>whiteblackip</b></span> refers to Blacklist and Whitelist events.</li><li><span class="parmvalue" id="parmvalue1943011268512"><a name="parmvalue1943011268512"></a><a name="parmvalue1943011268512"></a><b>webshell</b></span> refers to webshells.</li></ul>
</td>
</tr>
<tr id="row44833110"><td class="cellrowborder" valign="top" width="17.528247175282473%" headers="mcps1.2.5.1.1 "><p id="p7603302"><a name="p7603302"></a><a name="p7603302"></a>locale</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.2 "><p id="p11887706"><a name="p11887706"></a><a name="p11887706"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.58804119588041%" headers="mcps1.2.5.1.3 "><p id="p23380123"><a name="p23380123"></a><a name="p23380123"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.295670432956705%" headers="mcps1.2.5.1.4 "><p id="p14741776"><a name="p14741776"></a><a name="p14741776"></a>Specifies the language configuration. Only <strong id="b189224610456"><a name="b189224610456"></a><a name="b189224610456"></a>zh-cn</strong> and <strong id="b1392114611454"><a name="b1392114611454"></a><a name="b1392114611454"></a>en-us</strong> are supported. The default value is <strong id="b510013461451"><a name="b510013461451"></a><a name="b510013461451"></a>en-us</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section47544838"></a>

Response parameters

**Table  3**  Parameter description

<a name="table64771846"></a>
<table><thead align="left"><tr id="row64088200"><th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.1"><p id="p23761692"><a name="p23761692"></a><a name="p23761692"></a><strong id="b335911034612"><a name="b335911034612"></a><a name="b335911034612"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.189999999999998%" id="mcps1.2.4.1.2"><p id="p45648893"><a name="p45648893"></a><a name="p45648893"></a><strong id="b1775510964614"><a name="b1775510964614"></a><a name="b1775510964614"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="63.63999999999999%" id="mcps1.2.4.1.3"><p id="p6572818"><a name="p6572818"></a><a name="p6572818"></a><strong id="b159781810204613"><a name="b159781810204613"></a><a name="b159781810204613"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row62636227"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p40369658"><a name="p40369658"></a><a name="p40369658"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p48716828"><a name="p48716828"></a><a name="p48716828"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p53749011"><a name="p53749011"></a><a name="p53749011"></a>Specifies the unique ID of an alarm configuration.</p>
</td>
</tr>
<tr id="row13979058"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p58561923"><a name="p58561923"></a><a name="p58561923"></a>enabled</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p45895324"><a name="p45895324"></a><a name="p45895324"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p68819531435"><a name="p68819531435"></a><a name="p68819531435"></a>Specifies whether to send an alarm notification.</p>
<a name="ul1488225312313"></a><a name="ul1488225312313"></a><ul id="ul1488225312313"><li><strong id="b18957132842816"><a name="b18957132842816"></a><a name="b18957132842816"></a>true</strong>: Send the alarm notification.</li><li><strong id="b250223222817"><a name="b250223222817"></a><a name="b250223222817"></a>false</strong>: Do not send the alarm notification.</li></ul>
</td>
</tr>
<tr id="row37477597"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p15786515"><a name="p15786515"></a><a name="p15786515"></a>topic_urn</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p3639309"><a name="p3639309"></a><a name="p3639309"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p26348595"><a name="p26348595"></a><a name="p26348595"></a>Specifies the user-defined SMN topic. Users can receive alarm notifications by SMS or email.</p>
</td>
</tr>
<tr id="row35810771"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p14991335"><a name="p14991335"></a><a name="p14991335"></a>sendfreq</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p6338652"><a name="p6338652"></a><a name="p6338652"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p43668826"><a name="p43668826"></a><a name="p43668826"></a>Specifies the minimum interval between two alarms in minutes. The options are <strong id="b117934149302"><a name="b117934149302"></a><a name="b117934149302"></a>5</strong>, <strong id="b279451493018"><a name="b279451493018"></a><a name="b279451493018"></a>15</strong>, <strong id="b4794181473010"><a name="b4794181473010"></a><a name="b4794181473010"></a>30</strong>, and <strong id="b1879531417304"><a name="b1879531417304"></a><a name="b1879531417304"></a>60</strong>.</p>
</td>
</tr>
<tr id="row57475115"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p24972744"><a name="p24972744"></a><a name="p24972744"></a>times</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p9526402"><a name="p9526402"></a><a name="p9526402"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p33441088"><a name="p33441088"></a><a name="p33441088"></a>Specifies the alarm threshold. Alarm notifications are sent when the number of attacks is greater than or equal to the threshold within the configured period. This value is greater than or equal to <strong id="b24872374299"><a name="b24872374299"></a><a name="b24872374299"></a>1</strong>.</p>
</td>
</tr>
<tr id="row32534340"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p18035908"><a name="p18035908"></a><a name="p18035908"></a>threat</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p51622461"><a name="p51622461"></a><a name="p51622461"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p20669782"><a name="p20669782"></a><a name="p20669782"></a>Specifies the list of event types.</p>
<a name="ul1638611231235"></a><a name="ul1638611231235"></a><ul id="ul1638611231235"><li><strong id="b38850355326"><a name="b38850355326"></a><a name="b38850355326"></a>all</strong> refers to all types of events.</li><li><span class="parmvalue" id="parmvalue914220448610"><a name="parmvalue914220448610"></a><a name="parmvalue914220448610"></a><b>cc</b></span> refers to CC attack.</li><li><span class="parmvalue" id="parmvalue7997147466"><a name="parmvalue7997147466"></a><a name="parmvalue7997147466"></a><b>cmdi</b></span> refers to command injection.</li><li><span class="parmvalue" id="parmvalue259433114114"><a name="parmvalue259433114114"></a><a name="parmvalue259433114114"></a><b>custom</b></span> refers to Precise Protection events.</li><li><span class="parmvalue" id="parmvalue6357659162915"><a name="parmvalue6357659162915"></a><a name="parmvalue6357659162915"></a><b>illegal</b></span> refers to invalid requests.</li><li><span class="parmvalue" id="parmvalue181171418519"><a name="parmvalue181171418519"></a><a name="parmvalue181171418519"></a><b>sqli</b></span> refers to SQL injection.</li><li><span class="parmvalue" id="parmvalue106036153019"><a name="parmvalue106036153019"></a><a name="parmvalue106036153019"></a><b>lfi</b></span> refers to local file inclusion.</li><li><strong id="b1088417783012"><a name="b1088417783012"></a><a name="b1088417783012"></a>robot</strong> refers to malicious crawlers.</li><li><span class="parmvalue" id="parmvalue104141723330"><a name="parmvalue104141723330"></a><a name="parmvalue104141723330"></a><b>antitamper</b></span> refers to Web Tamper Protection events.</li><li><span class="parmvalue" id="parmvalue1246061473016"><a name="parmvalue1246061473016"></a><a name="parmvalue1246061473016"></a><b>rfi</b></span> refers to remote file inclusion.</li><li><span class="parmvalue" id="parmvalue91394167302"><a name="parmvalue91394167302"></a><a name="parmvalue91394167302"></a><b>vuln</b></span> refers to other types of attacks.</li><li><span class="parmvalue" id="parmvalue180482710516"><a name="parmvalue180482710516"></a><a name="parmvalue180482710516"></a><b>xss</b></span> refers to XSS attack.</li><li><span class="parmvalue" id="parmvalue56334710415"><a name="parmvalue56334710415"></a><a name="parmvalue56334710415"></a><b>whiteblackip</b></span> refers to Blacklist and Whitelist events.</li><li><span class="parmvalue" id="parmvalue13624173513516"><a name="parmvalue13624173513516"></a><a name="parmvalue13624173513516"></a><b>webshell</b></span> refers to webshells.</li></ul>
</td>
</tr>
<tr id="row51810310"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p35885554"><a name="p35885554"></a><a name="p35885554"></a>locale</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.2 "><p id="p21048787"><a name="p21048787"></a><a name="p21048787"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.63999999999999%" headers="mcps1.2.4.1.3 "><p id="p27230225"><a name="p27230225"></a><a name="p27230225"></a>Specifies the language configuration. Only <strong id="b07158190325"><a name="b07158190325"></a><a name="b07158190325"></a>zh-cn</strong> and <strong id="b571641993216"><a name="b571641993216"></a><a name="b571641993216"></a>en-us</strong> are supported. The default value is <strong id="b0717719123220"><a name="b0717719123220"></a><a name="b0717719123220"></a>en-us</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section9662958171611"></a>

-   Request example

    ```
    {
        "enabled": true,
        "topic_urn": "urn:smn:eude:fca6f667ac5f4d9798d1641dfd38106b:wbtest",
        "sendfreq": 5,
        "times": 200,
        "threat": ["xss", "sqli", "cmdi"]
    }
    ```


-   Response example

    ```
    {
        "id": "37b4bbe8a562453aa0163a96e6b71dd6",
        "enabled": true,
        "topic_urn": "urn:smn:eude:fca6f667ac5f4d9798d1641dfd38106b:wbtest",
        "sendfreq": 5,
        "times": 200,
        "threat": ["xss", "sqli", "cmdi"],
        "locale": "en-us"
    }
    ```


## Status Code<a name="section25250359"></a>

[Table 4](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  4**  Status code

<a name="en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0"></a>
<table><thead align="left"><tr id="en-us_topic_0193631139_r3d6e2f205c444705bdbb9daaac74e575"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"><a name="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"></a><a name="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="19.41%" id="mcps1.2.4.1.2"><p id="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"><a name="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"></a><a name="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"></a>Meaning</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0193631139_rc7b2adc390904a1ba79e303017797786"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"><a name="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"></a><a name="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="19.41%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"></a>The request has succeeded.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

