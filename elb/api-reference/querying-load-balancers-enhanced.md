# Querying Load Balancers<a name="EN-US_TOPIC_0141008270"></a>

## Function<a name="en-us_topic_0096561531_en-us_topic_0049139631_section45786357"></a>

This API is used to query load balancers and display them in a list. Filter query and pagination query are supported. Unless otherwise specified, exact match is applied.

## URI<a name="en-us_topic_0096561531_en-us_topic_0049139631_section9424035"></a>

GET /v2.0/lbaas/loadbalancers

## Constraints<a name="section12943112511216"></a>

Parameters  **marker**,  **limit**, and  **page\_reverse**  are used for pagination query. Parameters  **marker**  and  **page\_reverse**  take effect only when they are used together with parameter  **limit**.

## Request<a name="en-us_topic_0096561531_section450814374241"></a>

**Table  1**  Request parameters

<a name="table173202435716"></a>
<table><thead align="left"><tr id="row2997023165716"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="p14996132375711"><a name="p14996132375711"></a><a name="p14996132375711"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="p129971623125717"><a name="p129971623125717"></a><a name="p129971623125717"></a><strong id="en-us_topic_0096561531_b842352706192244"><a name="en-us_topic_0096561531_b842352706192244"></a><a name="en-us_topic_0096561531_b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p6996112319573"><a name="p6996112319573"></a><a name="p6996112319573"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52%" id="mcps1.2.5.1.4"><p id="p19997123155717"><a name="p19997123155717"></a><a name="p19997123155717"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row59971323145714"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p129979231573"><a name="p129979231573"></a><a name="p129979231573"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p199976234571"><a name="p199976234571"></a><a name="p199976234571"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p17997123165717"><a name="p17997123165717"></a><a name="p17997123165717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p4235152211344"><a name="p4235152211344"></a><a name="p4235152211344"></a>Specifies the ID of the load balancer from which pagination query starts, that is, the ID of the last load balancer on the previous page.</p>
<p id="p06221826143418"><a name="p06221826143418"></a><a name="p06221826143418"></a>This parameter must be used together with <strong id="b1557913100515"><a name="b1557913100515"></a><a name="b1557913100515"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row1799772355718"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p79972234578"><a name="p79972234578"></a><a name="p79972234578"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p2099722319571"><a name="p2099722319571"></a><a name="p2099722319571"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p09971123185715"><a name="p09971123185715"></a><a name="p09971123185715"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p163282306342"><a name="p163282306342"></a><a name="p163282306342"></a>Specifies the number of load balancers on each page.</p>
<p id="p8300236113416"><a name="p8300236113416"></a><a name="p8300236113416"></a>The value ranges from <strong id="b5855012175115"><a name="b5855012175115"></a><a name="b5855012175115"></a>0</strong> to <strong id="b1985521215511"><a name="b1985521215511"></a><a name="b1985521215511"></a>intmax</strong>.</p>
</td>
</tr>
<tr id="row11997152313578"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p599717234572"><a name="p599717234572"></a><a name="p599717234572"></a>page_reverse</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p79974232578"><a name="p79974232578"></a><a name="p79974232578"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p0997162312577"><a name="p0997162312577"></a><a name="p0997162312577"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p15227113913341"><a name="p15227113913341"></a><a name="p15227113913341"></a>Specifies the page direction. The value can be <strong id="b123101411515"><a name="b123101411515"></a><a name="b123101411515"></a>true</strong> or <strong id="b14328149512"><a name="b14328149512"></a><a name="b14328149512"></a>false</strong>, and the default value is <strong id="b53218149517"><a name="b53218149517"></a><a name="b53218149517"></a>false</strong>. The last page in the list requested with <strong id="b18337149517"><a name="b18337149517"></a><a name="b18337149517"></a>page_reverse</strong> set to <strong id="b1133314195117"><a name="b1133314195117"></a><a name="b1133314195117"></a>false</strong> will not contain the "next" link, and the last page in the list requested with <strong id="b834141425112"><a name="b834141425112"></a><a name="b834141425112"></a>page_reverse</strong> set to <strong id="b534151465114"><a name="b534151465114"></a><a name="b534151465114"></a>true</strong> will not contain the "previous" link.</p>
<p id="p5244104243413"><a name="p5244104243413"></a><a name="p5244104243413"></a>This parameter must be used together with <strong id="b175751415185110"><a name="b175751415185110"></a><a name="b175751415185110"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row899882319573"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p59971723185718"><a name="p59971723185718"></a><a name="p59971723185718"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p1899718234571"><a name="p1899718234571"></a><a name="p1899718234571"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p2997112318575"><a name="p2997112318575"></a><a name="p2997112318575"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p499914591415"><a name="p499914591415"></a><a name="p499914591415"></a>Specifies the ID of the project where the load balancer is used.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
</td>
</tr>
<tr id="row099812230578"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p1799811232573"><a name="p1799811232573"></a><a name="p1799811232573"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p1099817237571"><a name="p1099817237571"></a><a name="p1099817237571"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p899872385713"><a name="p899872385713"></a><a name="p899872385713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p399819238571"><a name="p399819238571"></a><a name="p399819238571"></a>Specifies the load balancer ID.</p>
</td>
</tr>
<tr id="row59991623185712"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p1199892312578"><a name="p1199892312578"></a><a name="p1199892312578"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p8998162315578"><a name="p8998162315578"></a><a name="p8998162315578"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p3998172312575"><a name="p3998172312575"></a><a name="p3998172312575"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p15998152315573"><a name="p15998152315573"></a><a name="p15998152315573"></a>Provides supplementary information about the load balancer.</p>
<p id="p3290102225719"><a name="p3290102225719"></a><a name="p3290102225719"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row3999192385710"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p1099911237570"><a name="p1099911237570"></a><a name="p1099911237570"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p09991723165710"><a name="p09991723165710"></a><a name="p09991723165710"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p899917231579"><a name="p899917231579"></a><a name="p899917231579"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p17999123195714"><a name="p17999123195714"></a><a name="p17999123195714"></a>Specifies the load balancer name.</p>
<p id="p1057013242577"><a name="p1057013242577"></a><a name="p1057013242577"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row120192455712"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p09991723135710"><a name="p09991723135710"></a><a name="p09991723135710"></a>operating_status</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p109991223175719"><a name="p109991223175719"></a><a name="p109991223175719"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p9999152314575"><a name="p9999152314575"></a><a name="p9999152314575"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p44348299311"><a name="p44348299311"></a><a name="p44348299311"></a>Specifies the operating status of the load balancer.</p>
<div class="p" id="p74553716320"><a name="p74553716320"></a><a name="p74553716320"></a>The value can be <strong id="b842352706165847"><a name="b842352706165847"></a><a name="b842352706165847"></a>ONLINE</strong>, <strong id="b842352706165850"><a name="b842352706165850"></a><a name="b842352706165850"></a>OFFLINE</strong>, <strong id="b842352706165852"><a name="b842352706165852"></a><a name="b842352706165852"></a>DEGRADED</strong>, <strong id="b842352706165855"><a name="b842352706165855"></a><a name="b842352706165855"></a>DISABLED</strong>, or <strong id="b842352706165859"><a name="b842352706165859"></a><a name="b842352706165859"></a>NO_MONITOR</strong>.<div class="note" id="note30324155716"><a name="note30324155716"></a><a name="note30324155716"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p503247571"><a name="p503247571"></a><a name="p503247571"></a>This parameter is reserved.</p>
</div></div>
</div>
</td>
</tr>
<tr id="row211124155719"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p701424175719"><a name="p701424175719"></a><a name="p701424175719"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p80112445710"><a name="p80112445710"></a><a name="p80112445710"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p16016249572"><a name="p16016249572"></a><a name="p16016249572"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p135290391532"><a name="p135290391532"></a><a name="p135290391532"></a>Specifies the provisioning status of the load balancer.</p>
<div class="p" id="p167561741236"><a name="p167561741236"></a><a name="p167561741236"></a>The value can be <strong id="b842352706165943"><a name="b842352706165943"></a><a name="b842352706165943"></a>ACTIVE</strong>, <strong id="b842352706165947"><a name="b842352706165947"></a><a name="b842352706165947"></a>PENDING_CREATE</strong>, or <strong id="b842352706165951"><a name="b842352706165951"></a><a name="b842352706165951"></a>ERROR</strong>.<div class="note" id="note13012455718"><a name="note13012455718"></a><a name="note13012455718"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p90112419574"><a name="p90112419574"></a><a name="p90112419574"></a>This parameter is reserved.</p>
</div></div>
</div>
</td>
</tr>
<tr id="row10152418573"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p17112245570"><a name="p17112245570"></a><a name="p17112245570"></a>vip_address</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p17112405715"><a name="p17112405715"></a><a name="p17112405715"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p201424175713"><a name="p201424175713"></a><a name="p201424175713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p31824165715"><a name="p31824165715"></a><a name="p31824165715"></a>Specifies the private IP address of the load balancer.</p>
<p id="p13202733195720"><a name="p13202733195720"></a><a name="p13202733195720"></a>The value contains a maximum of 64 characters.</p>
</td>
</tr>
<tr id="row16112244576"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p14119244570"><a name="p14119244570"></a><a name="p14119244570"></a>vip_port_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p12132412573"><a name="p12132412573"></a><a name="p12132412573"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p4723204915910"><a name="p4723204915910"></a><a name="p4723204915910"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p171112485712"><a name="p171112485712"></a><a name="p171112485712"></a>Specifies the ID of the port bound to the private IP address of the load balancer.</p>
</td>
</tr>
<tr id="row721424155710"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p81112415576"><a name="p81112415576"></a><a name="p81112415576"></a>vip_subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p1012024125713"><a name="p1012024125713"></a><a name="p1012024125713"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p17766451692"><a name="p17766451692"></a><a name="p17766451692"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p14217247579"><a name="p14217247579"></a><a name="p14217247579"></a>Specifies the ID of the subnet where the load balancer works.</p>
</td>
</tr>
<tr id="row16232465714"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p329245573"><a name="p329245573"></a><a name="p329245573"></a>member_address</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p9212249573"><a name="p9212249573"></a><a name="p9212249573"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p10540553499"><a name="p10540553499"></a><a name="p10540553499"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p10282413574"><a name="p10282413574"></a><a name="p10282413574"></a>Specifies the IP address of the backend server associated with the load balancer.</p>
</td>
</tr>
<tr id="row14372415579"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p16232485711"><a name="p16232485711"></a><a name="p16232485711"></a>member_device_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p1821424115714"><a name="p1821424115714"></a><a name="p1821424115714"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p1022510551190"><a name="p1022510551190"></a><a name="p1022510551190"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p102324125717"><a name="p102324125717"></a><a name="p102324125717"></a>Specifies the ID of the ECS corresponding to the backend server associated with the load balancer.</p>
</td>
</tr>
<tr id="row133102445718"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p43152465714"><a name="p43152465714"></a><a name="p43152465714"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p4320245571"><a name="p4320245571"></a><a name="p4320245571"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p102317571898"><a name="p102317571898"></a><a name="p102317571898"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="p23192410578"><a name="p23192410578"></a><a name="p23192410578"></a>Specifies the ID of the VPC where the load balancer works.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0096561531_section2095085982410"></a>

**Table  2**  Response parameters

<a name="en-us_topic_0096561531_table1491517497282"></a>
<table><thead align="left"><tr id="en-us_topic_0096561531_row16917204932819"><th class="cellrowborder" valign="top" width="22.17778222177782%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561531_p591874912286"><a name="en-us_topic_0096561531_p591874912286"></a><a name="en-us_topic_0096561531_p591874912286"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.8071192880712%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561531_p1991913496283"><a name="en-us_topic_0096561531_p1991913496283"></a><a name="en-us_topic_0096561531_p1991913496283"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.01509849015099%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561531_p89213491280"><a name="en-us_topic_0096561531_p89213491280"></a><a name="en-us_topic_0096561531_p89213491280"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561531_row1592214918289"><td class="cellrowborder" valign="top" width="22.17778222177782%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p39241549122817"><a name="en-us_topic_0096561531_p39241549122817"></a><a name="en-us_topic_0096561531_p39241549122817"></a>loadbalancers</p>
</td>
<td class="cellrowborder" valign="top" width="28.8071192880712%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p5925184911281"><a name="en-us_topic_0096561531_p5925184911281"></a><a name="en-us_topic_0096561531_p5925184911281"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="49.01509849015099%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p0926194942810"><a name="en-us_topic_0096561531_p0926194942810"></a><a name="en-us_topic_0096561531_p0926194942810"></a>Lists the load balancers. For details, see <a href="#en-us_topic_0096561531_table10274202983318">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **loadbalancers**  parameter description

<a name="en-us_topic_0096561531_table10274202983318"></a>
<table><thead align="left"><tr id="en-us_topic_0096561531_row134151429203316"><th class="cellrowborder" valign="top" width="34.71%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561531_p194153299337"><a name="en-us_topic_0096561531_p194153299337"></a><a name="en-us_topic_0096561531_p194153299337"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23.45%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561531_p741522912332"><a name="en-us_topic_0096561531_p741522912332"></a><a name="en-us_topic_0096561531_p741522912332"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="41.839999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096561531_p741513296334"><a name="en-us_topic_0096561531_p741513296334"></a><a name="en-us_topic_0096561531_p741513296334"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561531_row6415122916332"><td class="cellrowborder" valign="top" width="34.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p10415829113311"><a name="en-us_topic_0096561531_p10415829113311"></a><a name="en-us_topic_0096561531_p10415829113311"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.2 "><p id="p618316081015"><a name="p618316081015"></a><a name="p618316081015"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p1941513297339"><a name="en-us_topic_0096561531_p1941513297339"></a><a name="en-us_topic_0096561531_p1941513297339"></a>Specifies the load balancer ID.</p>
</td>
</tr>
<tr id="en-us_topic_0096561531_row74151329193316"><td class="cellrowborder" valign="top" width="34.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p20415229113312"><a name="en-us_topic_0096561531_p20415229113312"></a><a name="en-us_topic_0096561531_p20415229113312"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p741592933318"><a name="en-us_topic_0096561531_p741592933318"></a><a name="en-us_topic_0096561531_p741592933318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p1341519295331"><a name="en-us_topic_0096561531_p1341519295331"></a><a name="en-us_topic_0096561531_p1341519295331"></a>Specifies the ID of the project where the load balancer is used.</p>
<p id="p13909115215716"><a name="p13909115215716"></a><a name="p13909115215716"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561531_row14415172943316"><td class="cellrowborder" valign="top" width="34.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p1041552912332"><a name="en-us_topic_0096561531_p1041552912332"></a><a name="en-us_topic_0096561531_p1041552912332"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p241692918331"><a name="en-us_topic_0096561531_p241692918331"></a><a name="en-us_topic_0096561531_p241692918331"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p17416152919332"><a name="en-us_topic_0096561531_p17416152919332"></a><a name="en-us_topic_0096561531_p17416152919332"></a>Specifies the load balancer name.</p>
<p id="p20812205415572"><a name="p20812205415572"></a><a name="p20812205415572"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561531_row741615293331"><td class="cellrowborder" valign="top" width="34.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p4416102918335"><a name="en-us_topic_0096561531_p4416102918335"></a><a name="en-us_topic_0096561531_p4416102918335"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p24161129143314"><a name="en-us_topic_0096561531_p24161129143314"></a><a name="en-us_topic_0096561531_p24161129143314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p5416142912334"><a name="en-us_topic_0096561531_p5416142912334"></a><a name="en-us_topic_0096561531_p5416142912334"></a>Provides supplementary information about the load balancer.</p>
<p id="p2049917014587"><a name="p2049917014587"></a><a name="p2049917014587"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561531_row11416629183316"><td class="cellrowborder" valign="top" width="34.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p1541618299335"><a name="en-us_topic_0096561531_p1541618299335"></a><a name="en-us_topic_0096561531_p1541618299335"></a>vip_subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.2 "><p id="p1115108111017"><a name="p1115108111017"></a><a name="p1115108111017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p4335125124117"><a name="p4335125124117"></a><a name="p4335125124117"></a>Specifies the ID of the subnet where the load balancer works.</p>
</td>
</tr>
<tr id="en-us_topic_0096561531_row3416112913318"><td class="cellrowborder" valign="top" width="34.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p1041622923320"><a name="en-us_topic_0096561531_p1041622923320"></a><a name="en-us_topic_0096561531_p1041622923320"></a>vip_port_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.2 "><p id="p14217181041012"><a name="p14217181041012"></a><a name="p14217181041012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p173334177415"><a name="p173334177415"></a><a name="p173334177415"></a>Specifies the ID of the port bound to the private IP address of the load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0096561531_row6416152973312"><td class="cellrowborder" valign="top" width="34.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p174164295334"><a name="en-us_topic_0096561531_p174164295334"></a><a name="en-us_topic_0096561531_p174164295334"></a>provider</p>
</td>
<td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p541611290339"><a name="en-us_topic_0096561531_p541611290339"></a><a name="en-us_topic_0096561531_p541611290339"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p43391417194120"><a name="p43391417194120"></a><a name="p43391417194120"></a>Specifies the provider of the load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0096561531_row341662919337"><td class="cellrowborder" valign="top" width="34.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p1416829143318"><a name="en-us_topic_0096561531_p1416829143318"></a><a name="en-us_topic_0096561531_p1416829143318"></a>vip_address</p>
</td>
<td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p341672912338"><a name="en-us_topic_0096561531_p341672912338"></a><a name="en-us_topic_0096561531_p341672912338"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p64178297334"><a name="en-us_topic_0096561531_p64178297334"></a><a name="en-us_topic_0096561531_p64178297334"></a>Specifies the private IP address of the load balancer.</p>
<p id="p966121119588"><a name="p966121119588"></a><a name="p966121119588"></a>The value contains a maximum of 64 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561531_row041715295337"><td class="cellrowborder" valign="top" width="34.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p1841715293336"><a name="en-us_topic_0096561531_p1841715293336"></a><a name="en-us_topic_0096561531_p1841715293336"></a>listeners</p>
</td>
<td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.2 "><p id="p16382101516102"><a name="p16382101516102"></a><a name="p16382101516102"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p7417112963311"><a name="en-us_topic_0096561531_p7417112963311"></a><a name="en-us_topic_0096561531_p7417112963311"></a>Lists the IDs of listeners added to the load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0096561531_row1541722963311"><td class="cellrowborder" valign="top" width="34.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p1441712910330"><a name="en-us_topic_0096561531_p1441712910330"></a><a name="en-us_topic_0096561531_p1441712910330"></a>pools</p>
</td>
<td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.2 "><p id="p734131711103"><a name="p734131711103"></a><a name="p734131711103"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p104171229123313"><a name="en-us_topic_0096561531_p104171229123313"></a><a name="en-us_topic_0096561531_p104171229123313"></a>Lists the IDs of backend server groups associated with the load balancer.</p>
</td>
</tr>
<tr id="en-us_topic_0096561531_row541772903317"><td class="cellrowborder" valign="top" width="34.71%" headers="mcps1.2.4.1.1 "><p id="p727217358477"><a name="p727217358477"></a><a name="p727217358477"></a>operating_status</p>
</td>
<td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.2 "><p id="p82761735124717"><a name="p82761735124717"></a><a name="p82761735124717"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><a name="ul132852353472"></a><a name="ul132852353472"></a><ul id="ul132852353472"><li>Specifies the operating status of the load balancer.</li><li>The value can be <strong id="b1429468710"><a name="b1429468710"></a><a name="b1429468710"></a>ONLINE</strong>, <strong id="b1832686108"><a name="b1832686108"></a><a name="b1832686108"></a>OFFLINE</strong>, <strong id="b535262960"><a name="b535262960"></a><a name="b535262960"></a>DEGRADED</strong>, <strong id="b1791626513"><a name="b1791626513"></a><a name="b1791626513"></a>DISABLED</strong>, or <strong id="b907397778"><a name="b907397778"></a><a name="b907397778"></a>NO_MONITOR</strong>.</li><li>This parameter is reserved. The default value is <strong id="b842352706145855"><a name="b842352706145855"></a><a name="b842352706145855"></a>ONLINE</strong>.</li><li>The value contains a maximum of 16 characters.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0096561531_row0417192913319"><td class="cellrowborder" valign="top" width="34.71%" headers="mcps1.2.4.1.1 "><p id="p930113351475"><a name="p930113351475"></a><a name="p930113351475"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.2 "><p id="p1533018409328"><a name="p1533018409328"></a><a name="p1533018409328"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><a name="ul631316357476"></a><a name="ul631316357476"></a><ul id="ul631316357476"><li>Specifies the provisioning status of the load balancer.</li><li>The value can be <strong id="b314369784"><a name="b314369784"></a><a name="b314369784"></a>ACTIVE</strong>, <strong id="b1798496154"><a name="b1798496154"></a><a name="b1798496154"></a>PENDING_CREATE</strong>, or <strong id="b1093024091"><a name="b1093024091"></a><a name="b1093024091"></a>ERROR</strong>.</li><li>This parameter is reserved. The default value is <strong id="b261933193"><a name="b261933193"></a><a name="b261933193"></a>ACTIVE</strong>.</li><li>The value contains a maximum of 16 characters.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0096561531_row241822923317"><td class="cellrowborder" valign="top" width="34.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p114181329133314"><a name="en-us_topic_0096561531_p114181329133314"></a><a name="en-us_topic_0096561531_p114181329133314"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p10418172913319"><a name="en-us_topic_0096561531_p10418172913319"></a><a name="en-us_topic_0096561531_p10418172913319"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0096561531_ul06447306414"></a><a name="en-us_topic_0096561531_ul06447306414"></a><ul id="en-us_topic_0096561531_ul06447306414"><li>Specifies the administrative status of the load balancer.</li><li>This parameter is reserved. The default value is <strong id="b14941306419"><a name="b14941306419"></a><a name="b14941306419"></a>true</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0096561531_row1241832912337"><td class="cellrowborder" valign="top" width="34.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p74181229133310"><a name="en-us_topic_0096561531_p74181229133310"></a><a name="en-us_topic_0096561531_p74181229133310"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.2 "><p id="p119521821161017"><a name="p119521821161017"></a><a name="p119521821161017"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p4418112919333"><a name="en-us_topic_0096561531_p4418112919333"></a><a name="en-us_topic_0096561531_p4418112919333"></a>Lists load balancer tags.</p>
</td>
</tr>
<tr id="en-us_topic_0096561531_row15825198135111"><td class="cellrowborder" valign="top" width="34.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p18781627124910"><a name="en-us_topic_0096561531_p18781627124910"></a><a name="en-us_topic_0096561531_p18781627124910"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p18781627204916"><a name="en-us_topic_0096561531_p18781627204916"></a><a name="en-us_topic_0096561531_p18781627204916"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p578162719490"><a name="en-us_topic_0096561531_p578162719490"></a><a name="en-us_topic_0096561531_p578162719490"></a>Specifies the time when the load balancer was created.</p>
<p id="p3462240292"><a name="p3462240292"></a><a name="p3462240292"></a>The UTC time is in <em id="i107131833123516"><a name="i107131833123516"></a><a name="i107131833123516"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
<p id="p9961222125818"><a name="p9961222125818"></a><a name="p9961222125818"></a>The value contains a maximum of 19 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561531_row738211465116"><td class="cellrowborder" valign="top" width="34.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p1541843114495"><a name="en-us_topic_0096561531_p1541843114495"></a><a name="en-us_topic_0096561531_p1541843114495"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p1810172112506"><a name="en-us_topic_0096561531_p1810172112506"></a><a name="en-us_topic_0096561531_p1810172112506"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p341843144919"><a name="en-us_topic_0096561531_p341843144919"></a><a name="en-us_topic_0096561531_p341843144919"></a>Specifies the time when the load balancer was updated.</p>
<p id="p144451017171117"><a name="p144451017171117"></a><a name="p144451017171117"></a>The UTC time is in <em id="i5414988244"><a name="i5414988244"></a><a name="i5414988244"></a>YYYY-MM-DDTHH:MM:SS</em> format.</p>
<p id="p15557192745816"><a name="p15557192745816"></a><a name="p15557192745816"></a>The value contains a maximum of 19 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0096561531_row1368412142819"><td class="cellrowborder" valign="top" width="34.71%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p11729026152811"><a name="en-us_topic_0096561531_p11729026152811"></a><a name="en-us_topic_0096561531_p11729026152811"></a>loadbalancers_links</p>
</td>
<td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.2 "><p id="p1719372441012"><a name="p1719372441012"></a><a name="p1719372441012"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p5542991616"><a name="p5542991616"></a><a name="p5542991616"></a>Provides links to the previous or next page during pagination query, respectively.</p>
<p id="p165764116119"><a name="p165764116119"></a><a name="p165764116119"></a>This parameter exists only in the response body of pagination query.</p>
<p id="p53635145114"><a name="p53635145114"></a><a name="p53635145114"></a>For details, see <a href="#en-us_topic_0096561531_table661975283313">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **loadbalancers\_links**  parameter description

<a name="en-us_topic_0096561531_table661975283313"></a>
<table><thead align="left"><tr id="en-us_topic_0096561531_row12653175213336"><th class="cellrowborder" valign="top" width="34.69%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096561531_p15653195215335"><a name="en-us_topic_0096561531_p15653195215335"></a><a name="en-us_topic_0096561531_p15653195215335"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23.47%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096561531_p065315253310"><a name="en-us_topic_0096561531_p065315253310"></a><a name="en-us_topic_0096561531_p065315253310"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="41.839999999999996%" id="mcps1.2.4.1.3"><p id="p12802125811616"><a name="p12802125811616"></a><a name="p12802125811616"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096561531_row206531152103314"><td class="cellrowborder" valign="top" width="34.69%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p1465311528337"><a name="en-us_topic_0096561531_p1465311528337"></a><a name="en-us_topic_0096561531_p1465311528337"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p12653952113318"><a name="en-us_topic_0096561531_p12653952113318"></a><a name="en-us_topic_0096561531_p12653952113318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p1653852193312"><a name="en-us_topic_0096561531_p1653852193312"></a><a name="en-us_topic_0096561531_p1653852193312"></a>Provides links to the previous or next page during pagination query, respectively.</p>
</td>
</tr>
<tr id="en-us_topic_0096561531_row186535529338"><td class="cellrowborder" valign="top" width="34.69%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p1065325215337"><a name="en-us_topic_0096561531_p1065325215337"></a><a name="en-us_topic_0096561531_p1065325215337"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561531_p165305243318"><a name="en-us_topic_0096561531_p165305243318"></a><a name="en-us_topic_0096561531_p165305243318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p1772113411218"><a name="p1772113411218"></a><a name="p1772113411218"></a>Specifies the prompt of the previous or next page.</p>
<p id="p422510443113"><a name="p422510443113"></a><a name="p422510443113"></a>The value can be <strong id="b842352706175823"><a name="b842352706175823"></a><a name="b842352706175823"></a>next</strong> or <strong id="b842352706175826"><a name="b842352706175826"></a><a name="b842352706175826"></a>previous</strong>. The value <strong id="b8423527062079"><a name="b8423527062079"></a><a name="b8423527062079"></a>next</strong> indicates the Hypertext Reference (href) containing the URL of the next page, and <strong id="b84235270620752"><a name="b84235270620752"></a><a name="b84235270620752"></a>previous</strong> indicates the href containing the URL of the previous page.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section82498348322"></a>

-   Example request 1: Querying all load balancers

    ```
    GET https://{Endpoint}/v2.0/lbaas/loadbalancers
    ```

-   Example response 1

    ```
    {
        "loadbalancers": [
            {
                "description": "simple lb",
                "admin_state_up": true,
                "tenant_id": "1a3e005cf9ce40308c900bcb08e5320c",
     
                "provisioning_status": "ACTIVE",
                "vip_subnet_id": "5328f1e6-ce29-44f1-9493-b128a5653350",
                "listeners": [
                    {
                        "id": "45196943-2907-4369-87b1-c009b1d7ac35"
                    }
                ],
                "vip_address": "10.0.0.2",
                "vip_port_id": "cbced4fe-6f6f-4fd6-9348-0c3d1219d6ca",
                "provider": "vlb",
                "pools": [
                    {
                        "id": "21d49cf7-4fd3-4cb6-8c48-b7fc6c259aab"
                }
                ],
                "id": "a9729389-6147-41a3-ab22-a24aed8692b2",
                "operating_status": "ONLINE",
                "tags": [],
                "name": "loadbalancer1",
                "created_at": "2018-07-25T01:54:13", 
                "updated_at": "2018-07-25T01:54:14"
            }
    ]
    }
    ```

-   Example request 2: Querying load balancers by page \(each page contains one load balancer. The ID of the start load balancer is  **165b6a38-5278-4569-b747-b2ee65ea84a4**. The load balancer after  **165b6a38-5278-4569-b747-b2ee65ea84a4**  is the queried load balancer.\)

    ```
    GET https://{Endpoint}/v2.0/lbaas/loadbalancers?limit=1&marker=165b6a38-5278-4569-b747-b2ee65ea84a4
    ```

-   Example response 2

    ```
    {
        "loadbalancers": [
            {
                "description": "",
                "provisioning_status": "ACTIVE",
                "tenant_id": "601240b9c5c94059b63d484c92cfe308",
      
                "admin_state_up": true,
                "provider": "vlb",
                "pools": [
                    {
                        "id": "b13dba4c-a44c-4c40-8f6e-ce7a162b9f22"
                    },
                    {
                        "id": "4b9e765f-82ee-4128-911b-0a2d9ebc74c7"
                    }
                ],
                "listeners": [
                    {
                        "id": "21c41336-d0d3-4349-8641-6e82b4a4d097"
                    }
                ],
                "vip_port_id": "44ac5d9b-b0c0-4810-9a9d-c4dbf541e47e",
                "operating_status": "ONLINE",
                "vip_address": "192.168.0.234",
                "vip_subnet_id": "9d60827e-0e5c-490a-8183-0b6ebf9084ca",
                "id": "e79a7dd6-3a38-429a-95f9-c7f78b346cbe",
                "tags": [],
                "name": "elb-robot",
                "created_at": "2018-07-25T01:54:13", 
                "updated_at": "2018-07-25T01:54:14"
            }
        ],
        "loadbalancers_links": [
            {
                "href": "https://network.Region.dc1.domainname.com/v2.0/lbaas/loadbalancers?limit=10&marker=e79a7dd6-3a38-429a-95f9-c7f78b346cbe&page_reverse=True",
                  "rel": "previous"
            }
        ]
    }
    ```

-   Example request 3: Filtering the load balancer using the IP address of a backend server \(192.168.0.191\)

    ```
    GET https://{Endpoint}/v2.0/lbaas/loadbalancers?member_address=192.168.0.181
    ```


-   Example response 3

    ```
    {
        "loadbalancers": [
            {
                "description": "",
                "provisioning_status": "ACTIVE",
                "tenant_id": "601240b9c5c94059b63d484c92cfe308",
     
                "created_at": "2018-11-29T13:55:20",
                "admin_state_up": true,
                "update_at": "2018-11-29T13:55:21",
                "id": "c1127125-64a9-4394-a08a-ef3be8f7ef9c",
                "pools": [
                    {
                        "id": "2f6895be-019b-4c82-9b53-c4a2ac009e20"
                    }
                ],
                "listeners": [
                    {
                        "id": "5c63d176-444f-4c75-9cfe-bcb8a05a845c"
                    }
                ],
                "vip_port_id": "434ac600-b779-4428-b7a7-830e047511f1",
                "operating_status": "ONLINE",
                "vip_address": "192.168.0.181",
                "vip_subnet_id": "9a303536-417c-45dc-a6db-1234b9e1c2b2",
                "provider": "vlb",
                "tags": [],
                "name": "elb-ftci"
    
            }
        ]
    }
    ```


## Status Code<a name="en-us_topic_0096561531_en-us_topic_0049139631_section51281965"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

