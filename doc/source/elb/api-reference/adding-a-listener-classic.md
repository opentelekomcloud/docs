# Adding a Listener<a name="EN-US_TOPIC_0096561506"></a>

## Function<a name="en-us_topic_0020100158_section18389930"></a>

This API is used to add a listener to a load balancer to monitor the status of backend ECSs.

## URI<a name="en-us_topic_0020100158_section31291646"></a>

POST /v1.0/\{project\_id\}/elbaas/listeners

**Table  1**  Parameter description

<a name="en-us_topic_0020100158_table57434139"></a>
<table><thead align="left"><tr id="en-us_topic_0020100158_row461342"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020100158_p37368736"><a name="en-us_topic_0020100158_p37368736"></a><a name="en-us_topic_0020100158_p37368736"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100158_p6968762"><a name="en-us_topic_0020100158_p6968762"></a><a name="en-us_topic_0020100158_p6968762"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100158_p586113175312"><a name="en-us_topic_0020100158_p586113175312"></a><a name="en-us_topic_0020100158_p586113175312"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020100158_p27598869"><a name="en-us_topic_0020100158_p27598869"></a><a name="en-us_topic_0020100158_p27598869"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020100158_row1569185811300"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p1399071505415"><a name="p1399071505415"></a><a name="p1399071505415"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p6162677511304"><a name="en-us_topic_0020100158_p6162677511304"></a><a name="en-us_topic_0020100158_p6162677511304"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p557643211309"><a name="en-us_topic_0020100158_p557643211309"></a><a name="en-us_topic_0020100158_p557643211309"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100158_p35845144113012"><a name="en-us_topic_0020100158_p35845144113012"></a><a name="en-us_topic_0020100158_p35845144113012"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
<tr id="en-us_topic_0020100158_row20915929"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p16468652"><a name="en-us_topic_0020100158_p16468652"></a><a name="en-us_topic_0020100158_p16468652"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p58892473"><a name="en-us_topic_0020100158_p58892473"></a><a name="en-us_topic_0020100158_p58892473"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p47475220175312"><a name="en-us_topic_0020100158_p47475220175312"></a><a name="en-us_topic_0020100158_p47475220175312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100158_ul6107094191929"></a><a name="en-us_topic_0020100158_ul6107094191929"></a><ul id="en-us_topic_0020100158_ul6107094191929"><li>Specifies the listener name.</li><li>The value is a string of 1 to 64 characters that consist of Chinese characters, letters, digits, underscores (_), and hyphens (-).</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100158_row39070558"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p10598606"><a name="en-us_topic_0020100158_p10598606"></a><a name="en-us_topic_0020100158_p10598606"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p53180767"><a name="en-us_topic_0020100158_p53180767"></a><a name="en-us_topic_0020100158_p53180767"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p32682146175312"><a name="en-us_topic_0020100158_p32682146175312"></a><a name="en-us_topic_0020100158_p32682146175312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100158_ul5649167191936"></a><a name="en-us_topic_0020100158_ul5649167191936"></a><ul id="en-us_topic_0020100158_ul5649167191936"><li>Provides supplementary information about the listener.</li><li>The value is a string of 0 to 128 characters and cannot contain angle brackets (&lt; and &gt;).</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100158_row46067993"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p40519951"><a name="en-us_topic_0020100158_p40519951"></a><a name="en-us_topic_0020100158_p40519951"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p60890569"><a name="en-us_topic_0020100158_p60890569"></a><a name="en-us_topic_0020100158_p60890569"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p30008174175312"><a name="en-us_topic_0020100158_p30008174175312"></a><a name="en-us_topic_0020100158_p30008174175312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100158_p3957675"><a name="en-us_topic_0020100158_p3957675"></a><a name="en-us_topic_0020100158_p3957675"></a>Specifies the load balancer ID.</p>
</td>
</tr>
<tr id="en-us_topic_0020100158_row35619075"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p66572856"><a name="en-us_topic_0020100158_p66572856"></a><a name="en-us_topic_0020100158_p66572856"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p23692278"><a name="en-us_topic_0020100158_p23692278"></a><a name="en-us_topic_0020100158_p23692278"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p14743026175312"><a name="en-us_topic_0020100158_p14743026175312"></a><a name="en-us_topic_0020100158_p14743026175312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100158_ul62362923191953"></a><a name="en-us_topic_0020100158_ul62362923191953"></a><ul id="en-us_topic_0020100158_ul62362923191953"><li>Specifies the load balancer protocol.</li><li>The value can be <strong id="b2293730619131"><a name="b2293730619131"></a><a name="b2293730619131"></a>HTTP</strong>, <strong id="b3656174719131"><a name="b3656174719131"></a><a name="b3656174719131"></a>TCP</strong>, <strong id="b1179611865155419"><a name="b1179611865155419"></a><a name="b1179611865155419"></a>HTTPS</strong>, <strong id="b842352706172428"><a name="b842352706172428"></a><a name="b842352706172428"></a>SSL</strong>, or <strong id="b842352706155440"><a name="b842352706155440"></a><a name="b842352706155440"></a>UDP</strong>.</li><li>A UDP listener cannot be added to a private network load balancer.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100158_row53954942"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p8274172"><a name="en-us_topic_0020100158_p8274172"></a><a name="en-us_topic_0020100158_p8274172"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p66228199"><a name="en-us_topic_0020100158_p66228199"></a><a name="en-us_topic_0020100158_p66228199"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p53334487175312"><a name="en-us_topic_0020100158_p53334487175312"></a><a name="en-us_topic_0020100158_p53334487175312"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100158_ul6053553519201"></a><a name="en-us_topic_0020100158_ul6053553519201"></a><ul id="en-us_topic_0020100158_ul6053553519201"><li>Specifies the port used by the load balancer.</li><li>The port number ranges from 1 to 65535.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100158_row6993202"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p29578451"><a name="en-us_topic_0020100158_p29578451"></a><a name="en-us_topic_0020100158_p29578451"></a>backend_protocol</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p47044325"><a name="en-us_topic_0020100158_p47044325"></a><a name="en-us_topic_0020100158_p47044325"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p25126213175312"><a name="en-us_topic_0020100158_p25126213175312"></a><a name="en-us_topic_0020100158_p25126213175312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100158_ul27512692192012"></a><a name="en-us_topic_0020100158_ul27512692192012"></a><ul id="en-us_topic_0020100158_ul27512692192012"><li>Specifies the backend ECS protocol.<p id="en-us_topic_0020100158_p49981105113220"><a name="en-us_topic_0020100158_p49981105113220"></a><a name="en-us_topic_0020100158_p49981105113220"></a>If <strong id="b842352706155857"><a name="b842352706155857"></a><a name="b842352706155857"></a>protocol</strong> is set to <strong id="b55874956102559"><a name="b55874956102559"></a><a name="b55874956102559"></a>UDP</strong>, the value of this parameter can only be <strong id="b1008091204155914"><a name="b1008091204155914"></a><a name="b1008091204155914"></a>UDP</strong>.</p>
<p id="en-us_topic_0020100158_p902425621319"><a name="en-us_topic_0020100158_p902425621319"></a><a name="en-us_topic_0020100158_p902425621319"></a>If <strong id="b11808038155919"><a name="b11808038155919"></a><a name="b11808038155919"></a>protocol</strong> is set to <strong id="b39163482155919"><a name="b39163482155919"></a><a name="b39163482155919"></a>SSL</strong>, the value of this parameter can only be <strong id="b16927020155919"><a name="b16927020155919"></a><a name="b16927020155919"></a>TCP</strong>.</p>
</li><li>The value can be <strong id="b37719544155919"><a name="b37719544155919"></a><a name="b37719544155919"></a>HTTP</strong>, <strong id="b3931576155919"><a name="b3931576155919"></a><a name="b3931576155919"></a>TCP</strong>, or <strong id="b842352706155831"><a name="b842352706155831"></a><a name="b842352706155831"></a>UDP</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100158_row16049999"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p24981566"><a name="en-us_topic_0020100158_p24981566"></a><a name="en-us_topic_0020100158_p24981566"></a>backend_port</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p10240961"><a name="en-us_topic_0020100158_p10240961"></a><a name="en-us_topic_0020100158_p10240961"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p21957347175312"><a name="en-us_topic_0020100158_p21957347175312"></a><a name="en-us_topic_0020100158_p21957347175312"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100158_ul42500047192029"></a><a name="en-us_topic_0020100158_ul42500047192029"></a><ul id="en-us_topic_0020100158_ul42500047192029"><li>Specifies the port used by backend ECSs.</li><li>The port number ranges from 1 to 65535.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100158_row567760"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p45988614"><a name="en-us_topic_0020100158_p45988614"></a><a name="en-us_topic_0020100158_p45988614"></a>lb_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p34090260"><a name="en-us_topic_0020100158_p34090260"></a><a name="en-us_topic_0020100158_p34090260"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p33714649175312"><a name="en-us_topic_0020100158_p33714649175312"></a><a name="en-us_topic_0020100158_p33714649175312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100158_ul9465338192037"></a><a name="en-us_topic_0020100158_ul9465338192037"></a><ul id="en-us_topic_0020100158_ul9465338192037"><li>Specifies the load balancing algorithm.</li><li>The value can be <strong id="b1191925123418"><a name="b1191925123418"></a><a name="b1191925123418"></a>roundrobin</strong>, <strong id="b3100251349"><a name="b3100251349"></a><a name="b3100251349"></a>leastconn</strong>, or <strong id="b171114255348"><a name="b171114255348"></a><a name="b171114255348"></a>source</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100158_row26602077"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p7284614"><a name="en-us_topic_0020100158_p7284614"></a><a name="en-us_topic_0020100158_p7284614"></a>session_sticky</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p53182860"><a name="en-us_topic_0020100158_p53182860"></a><a name="en-us_topic_0020100158_p53182860"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p10999535175312"><a name="en-us_topic_0020100158_p10999535175312"></a><a name="en-us_topic_0020100158_p10999535175312"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100158_ul61391383192047"></a><a name="en-us_topic_0020100158_ul61391383192047"></a><ul id="en-us_topic_0020100158_ul61391383192047"><li>Specifies whether to enable the sticky session feature.</li><li>The value can be <strong id="b10547672195810"><a name="b10547672195810"></a><a name="b10547672195810"></a>true</strong> or <strong id="b46350686195813"><a name="b46350686195813"></a><a name="b46350686195813"></a>false</strong>. The feature is enabled when the value is <strong id="b88931724113813"><a name="b88931724113813"></a><a name="b88931724113813"></a>true</strong>.</li><li>If <strong id="b842352706171718"><a name="b842352706171718"></a><a name="b842352706171718"></a>protocol</strong> is set to <strong id="b842352706171721"><a name="b842352706171721"></a><a name="b842352706171721"></a>SSL</strong>, the sticky session feature is not supported and the parameter is invalid.</li><li>If <strong id="b84235270616318"><a name="b84235270616318"></a><a name="b84235270616318"></a>protocol</strong> is set to <strong id="b84235270616325"><a name="b84235270616325"></a><a name="b84235270616325"></a>HTTP</strong>, <strong id="b84235270616332"><a name="b84235270616332"></a><a name="b84235270616332"></a>HTTPS</strong>, or <strong id="b84235270615430"><a name="b84235270615430"></a><a name="b84235270615430"></a>TCP</strong> and <strong id="b8423527061649"><a name="b8423527061649"></a><a name="b8423527061649"></a>lb_algorithm</strong> is not <strong id="b84235270616422"><a name="b84235270616422"></a><a name="b84235270616422"></a>roundrobin</strong>, the value of this parameter can only be <strong id="b84235270616439"><a name="b84235270616439"></a><a name="b84235270616439"></a>false</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100158_row35416756"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p50184984"><a name="en-us_topic_0020100158_p50184984"></a><a name="en-us_topic_0020100158_p50184984"></a>sticky_session_type</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p38451933"><a name="en-us_topic_0020100158_p38451933"></a><a name="en-us_topic_0020100158_p38451933"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p18547167175312"><a name="en-us_topic_0020100158_p18547167175312"></a><a name="en-us_topic_0020100158_p18547167175312"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><p id="p16233481539"><a name="p16233481539"></a><a name="p16233481539"></a>Specifies where the cookie is from. The only value is <strong id="b8463746126"><a name="b8463746126"></a><a name="b8463746126"></a>insert</strong>, indicating that the cookie is inserted by the load balancer.</p>
<a name="en-us_topic_0020100158_ul1811738819212"></a><a name="en-us_topic_0020100158_ul1811738819212"></a><ul id="en-us_topic_0020100158_ul1811738819212"><li>This parameter is valid when <strong id="b74117531210"><a name="b74117531210"></a><a name="b74117531210"></a>protocol</strong> is set to <strong id="b164155316217"><a name="b164155316217"></a><a name="b164155316217"></a>HTTP</strong> and <strong id="b114117531022"><a name="b114117531022"></a><a name="b114117531022"></a>session_sticky</strong> to <strong id="b741853621"><a name="b741853621"></a><a name="b741853621"></a>true</strong>.</li><li>This parameter is invalid when <strong id="b667609043165942"><a name="b667609043165942"></a><a name="b667609043165942"></a>protocol</strong> is set to <strong id="b1478565795165942"><a name="b1478565795165942"></a><a name="b1478565795165942"></a>TCP</strong>, <strong id="b118101115125914"><a name="b118101115125914"></a><a name="b118101115125914"></a>SSL</strong>, or <strong id="b2360121102648"><a name="b2360121102648"></a><a name="b2360121102648"></a>UDP</strong>, which means that the parameter is unavailable or its value is set to <strong id="b85221350135815"><a name="b85221350135815"></a><a name="b85221350135815"></a>null</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100158_row54041329"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p15271547"><a name="en-us_topic_0020100158_p15271547"></a><a name="en-us_topic_0020100158_p15271547"></a>cookie_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p29035785"><a name="en-us_topic_0020100158_p29035785"></a><a name="en-us_topic_0020100158_p29035785"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p25925576175312"><a name="en-us_topic_0020100158_p25925576175312"></a><a name="en-us_topic_0020100158_p25925576175312"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100158_ul77840192112"></a><a name="en-us_topic_0020100158_ul77840192112"></a><ul id="en-us_topic_0020100158_ul77840192112"><li>Specifies the cookie timeout duration. This parameter is valid when <strong id="b52388588717153"><a name="b52388588717153"></a><a name="b52388588717153"></a>protocol</strong> is set to <strong id="b178090614117153"><a name="b178090614117153"></a><a name="b178090614117153"></a>HTTP</strong>, <strong id="b27246866155919"><a name="b27246866155919"></a><a name="b27246866155919"></a>session_sticky</strong> to <strong id="b43895205155919"><a name="b43895205155919"></a><a name="b43895205155919"></a>true</strong>, and <strong id="b59512528155919"><a name="b59512528155919"></a><a name="b59512528155919"></a>sticky_session_type</strong> to <strong id="b65850708155919"><a name="b65850708155919"></a><a name="b65850708155919"></a>insert</strong>. This parameter is invalid when <strong id="b121408947117235"><a name="b121408947117235"></a><a name="b121408947117235"></a>protocol</strong> is set to <strong id="b84235270618547"><a name="b84235270618547"></a><a name="b84235270618547"></a>TCP</strong>, <strong id="b842352706185317"><a name="b842352706185317"></a><a name="b842352706185317"></a>SSL</strong>, or <strong id="b842352706185323"><a name="b842352706185323"></a><a name="b842352706185323"></a>UDP</strong>.</li><li>The value ranges from <strong id="b1213636123810"><a name="b1213636123810"></a><a name="b1213636123810"></a>1</strong> to <strong id="b169251340163813"><a name="b169251340163813"></a><a name="b169251340163813"></a>1440</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100158_row4399929622116"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p53567632221110"><a name="en-us_topic_0020100158_p53567632221110"></a><a name="en-us_topic_0020100158_p53567632221110"></a>tcp_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p44010958221110"><a name="en-us_topic_0020100158_p44010958221110"></a><a name="en-us_topic_0020100158_p44010958221110"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p8117820221110"><a name="en-us_topic_0020100158_p8117820221110"></a><a name="en-us_topic_0020100158_p8117820221110"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100158_ul63770335192147"></a><a name="en-us_topic_0020100158_ul63770335192147"></a><ul id="en-us_topic_0020100158_ul63770335192147"><li>Specifies the TCP session timeout duration. This parameter is valid when <strong id="b9885729155919"><a name="b9885729155919"></a><a name="b9885729155919"></a>protocol</strong> is set to <strong id="b182340233017235"><a name="b182340233017235"></a><a name="b182340233017235"></a>TCP</strong>.</li><li>The value ranges from <strong id="b1087218533381"><a name="b1087218533381"></a><a name="b1087218533381"></a>1</strong> to <strong id="b745155918382"><a name="b745155918382"></a><a name="b745155918382"></a>1440</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100158_row3860219515041"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p5269499415041"><a name="en-us_topic_0020100158_p5269499415041"></a><a name="en-us_topic_0020100158_p5269499415041"></a>tcp_draining</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p4043609715041"><a name="en-us_topic_0020100158_p4043609715041"></a><a name="en-us_topic_0020100158_p4043609715041"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p73514931518"><a name="en-us_topic_0020100158_p73514931518"></a><a name="en-us_topic_0020100158_p73514931518"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100158_ul17090437192140"></a><a name="en-us_topic_0020100158_ul17090437192140"></a><ul id="en-us_topic_0020100158_ul17090437192140"><li>Specifies whether to maintain TCP connections to a backend ECS that has been removed. This parameter is valid when <strong id="b84235270616396"><a name="b84235270616396"></a><a name="b84235270616396"></a>protocol</strong> is set to <strong id="b842352706163915"><a name="b842352706163915"></a><a name="b842352706163915"></a>TCP</strong>.</li><li>The value can be <strong id="b1845444702162720"><a name="b1845444702162720"></a><a name="b1845444702162720"></a>true</strong> or <strong id="b673679985162720"><a name="b673679985162720"></a><a name="b673679985162720"></a>false</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100158_row6394145615041"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p6329001715041"><a name="en-us_topic_0020100158_p6329001715041"></a><a name="en-us_topic_0020100158_p6329001715041"></a>tcp_draining_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p2621771615041"><a name="en-us_topic_0020100158_p2621771615041"></a><a name="en-us_topic_0020100158_p2621771615041"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p504630031518"><a name="en-us_topic_0020100158_p504630031518"></a><a name="en-us_topic_0020100158_p504630031518"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100158_ul30806154192129"></a><a name="en-us_topic_0020100158_ul30806154192129"></a><ul id="en-us_topic_0020100158_ul30806154192129"><li>Specifies the timeout duration for maintaining TCP connections to a backend ECS that has been removed. The unit is minute.<p id="en-us_topic_0020100158_p6888206113411"><a name="en-us_topic_0020100158_p6888206113411"></a><a name="en-us_topic_0020100158_p6888206113411"></a>This parameter is valid when <strong id="b84235270617553"><a name="b84235270617553"></a><a name="b84235270617553"></a>protocol</strong> is set to <strong id="b8423527061761"><a name="b8423527061761"></a><a name="b8423527061761"></a>TCP</strong> and <strong id="b84235270617611"><a name="b84235270617611"></a><a name="b84235270617611"></a>tcp_draining</strong> to <strong id="b84235270617620"><a name="b84235270617620"></a><a name="b84235270617620"></a>true</strong>.</p>
</li><li>The value ranges from <strong id="b2334127175620"><a name="b2334127175620"></a><a name="b2334127175620"></a>0</strong> to <strong id="b4580171005614"><a name="b4580171005614"></a><a name="b4580171005614"></a>60</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100158_row65993381192220"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p2379924192224"><a name="en-us_topic_0020100158_p2379924192224"></a><a name="en-us_topic_0020100158_p2379924192224"></a>certificate_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p58556147192224"><a name="en-us_topic_0020100158_p58556147192224"></a><a name="en-us_topic_0020100158_p58556147192224"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p45427491192224"><a name="en-us_topic_0020100158_p45427491192224"></a><a name="en-us_topic_0020100158_p45427491192224"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100158_ul54736270192236"></a><a name="en-us_topic_0020100158_ul54736270192236"></a><ul id="en-us_topic_0020100158_ul54736270192236"><li>Specifies the certificate ID. This parameter is mandatory when <strong id="b842352706172418"><a name="b842352706172418"></a><a name="b842352706172418"></a>protocol</strong> is set to <strong id="b842352706172421"><a name="b842352706172421"></a><a name="b842352706172421"></a>HTTPS</strong> or <strong id="b842352706172433"><a name="b842352706172433"></a><a name="b842352706172433"></a>SSL</strong>.</li><li>The ID can be obtained from the certificate list.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100158_row9223301184817"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p9916930184827"><a name="en-us_topic_0020100158_p9916930184827"></a><a name="en-us_topic_0020100158_p9916930184827"></a>certificates</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p65073860184827"><a name="en-us_topic_0020100158_p65073860184827"></a><a name="en-us_topic_0020100158_p65073860184827"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p36491294184827"><a name="en-us_topic_0020100158_p36491294184827"></a><a name="en-us_topic_0020100158_p36491294184827"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100158_ul3004857184827"></a><a name="en-us_topic_0020100158_ul3004857184827"></a><ul id="en-us_topic_0020100158_ul3004857184827"><li>Lists the certificate IDs if <strong id="b842352706172631"><a name="b842352706172631"></a><a name="b842352706172631"></a>protocol</strong> is set to <strong id="b842352706172635"><a name="b842352706172635"></a><a name="b842352706172635"></a>HTTPS</strong>.</li><li>This parameter is mandatory in the SNI scenario and is valid only when the load balancer is a public network load balancer.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100158_row3798661103850"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p39256153103850"><a name="en-us_topic_0020100158_p39256153103850"></a><a name="en-us_topic_0020100158_p39256153103850"></a>udp_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p25631825103850"><a name="en-us_topic_0020100158_p25631825103850"></a><a name="en-us_topic_0020100158_p25631825103850"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p62911958103850"><a name="en-us_topic_0020100158_p62911958103850"></a><a name="en-us_topic_0020100158_p62911958103850"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100158_ul45042833103952"></a><a name="en-us_topic_0020100158_ul45042833103952"></a><ul id="en-us_topic_0020100158_ul45042833103952"><li>Specifies the UDP session timeout duration. This parameter is valid when <strong id="b58034056155919"><a name="b58034056155919"></a><a name="b58034056155919"></a>protocol</strong> is set to <strong id="b52544458155919"><a name="b52544458155919"></a><a name="b52544458155919"></a>UDP</strong>.</li><li>The value ranges from <strong id="b5190103610399"><a name="b5190103610399"></a><a name="b5190103610399"></a>1</strong> to <strong id="b6456183963919"><a name="b6456183963919"></a><a name="b6456183963919"></a>1440</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100158_row45819259155333"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p9702520155436"><a name="en-us_topic_0020100158_p9702520155436"></a><a name="en-us_topic_0020100158_p9702520155436"></a>ssl_protocols</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p47706695155436"><a name="en-us_topic_0020100158_p47706695155436"></a><a name="en-us_topic_0020100158_p47706695155436"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p39037119155436"><a name="en-us_topic_0020100158_p39037119155436"></a><a name="en-us_topic_0020100158_p39037119155436"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100158_ul7890055155436"></a><a name="en-us_topic_0020100158_ul7890055155436"></a><ul id="en-us_topic_0020100158_ul7890055155436"><li>Specifies the supported SSL/TLS protocol version. This parameter is available only when <strong id="b842352706203214"><a name="b842352706203214"></a><a name="b842352706203214"></a>protocol</strong> is set to <strong id="b842352706203232"><a name="b842352706203232"></a><a name="b842352706203232"></a>HTTPS</strong> or <strong id="b842352706173557"><a name="b842352706173557"></a><a name="b842352706173557"></a>SSL</strong>.</li><li>The value is <strong id="b842352706203310"><a name="b842352706203310"></a><a name="b842352706203310"></a>TLSv1.2</strong> or <strong id="b11691232194236"><a name="b11691232194236"></a><a name="b11691232194236"></a>TLSv1.2 TLSv1.1 TLSv1</strong> and the default value is <strong id="b84235270620375"><a name="b84235270620375"></a><a name="b84235270620375"></a>TLSv1.2</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100158_row59770759155338"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100158_p30135916155436"><a name="en-us_topic_0020100158_p30135916155436"></a><a name="en-us_topic_0020100158_p30135916155436"></a>ssl_ciphers</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100158_p25090145155436"><a name="en-us_topic_0020100158_p25090145155436"></a><a name="en-us_topic_0020100158_p25090145155436"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100158_p19035850155436"><a name="en-us_topic_0020100158_p19035850155436"></a><a name="en-us_topic_0020100158_p19035850155436"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100158_ul65508880155436"></a><a name="en-us_topic_0020100158_ul65508880155436"></a><ul id="en-us_topic_0020100158_ul65508880155436"><li>Specifies the cipher suites supported by a specific SSL/TLS protocol version. This parameter is available only when <strong id="b488923883203421"><a name="b488923883203421"></a><a name="b488923883203421"></a>protocol</strong> is set to <strong id="b2038318649203421"><a name="b2038318649203421"></a><a name="b2038318649203421"></a>HTTPS</strong> or <strong id="b842352706173551"><a name="b842352706173551"></a><a name="b842352706173551"></a>SSL</strong>.</li><li>The value is <strong id="b842352706102954"><a name="b842352706102954"></a><a name="b842352706102954"></a>Default</strong>, <strong id="b842352706101415"><a name="b842352706101415"></a><a name="b842352706101415"></a>Extended</strong>, or <strong id="b842352706103022"><a name="b842352706103022"></a><a name="b842352706103022"></a>Strict</strong>.<p id="en-us_topic_0020100158_p41571308155436"><a name="en-us_topic_0020100158_p41571308155436"></a><a name="en-us_topic_0020100158_p41571308155436"></a>The value of <strong id="b1592461146101451"><a name="b1592461146101451"></a><a name="b1592461146101451"></a>Default</strong> is <strong id="b84235270610151"><a name="b84235270610151"></a><a name="b84235270610151"></a>ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256</strong>.</p>
<p id="en-us_topic_0020100158_p38597456155436"><a name="en-us_topic_0020100158_p38597456155436"></a><a name="en-us_topic_0020100158_p38597456155436"></a>The value of <strong id="b1679441012203631"><a name="b1679441012203631"></a><a name="b1679441012203631"></a>Extended</strong> is <strong id="b842352706203650"><a name="b842352706203650"></a><a name="b842352706203650"></a>ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:AES128-SHA256:AES256-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES128-SHA:DHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:AES128-SHA:AES256-SHA:DHE-DSS-AES128-SHA:CAMELLIA128-SHA:EDH-RSA-DES-CBC3-SHA:DES-CBC3-SHA:ECDHE-RSA-RC4-SHA:RC4-SHA:DHE-RSA-AES256-SHA:DHE-DSS-AES256-SHA:DHE-RSA-CAMELLIA256-SHA:DHE-DSS-CAMELLIA256-SHA:CAMELLIA256-SHA:EDH-DSS-DES-CBC3-SHA:DHE-RSA-CAMELLIA128-SHA:DHE-DSS-CAMELLIA128-SHA</strong>.</p>
<p id="en-us_topic_0020100158_p25420824101613"><a name="en-us_topic_0020100158_p25420824101613"></a><a name="en-us_topic_0020100158_p25420824101613"></a>The value of <strong id="b842352706103424"><a name="b842352706103424"></a><a name="b842352706103424"></a>Strict</strong> is <strong id="b842352706103456"><a name="b842352706103456"></a><a name="b842352706103456"></a>ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256</strong>.</p>
<p id="en-us_topic_0020100158_p11832792155436"><a name="en-us_topic_0020100158_p11832792155436"></a><a name="en-us_topic_0020100158_p11832792155436"></a>The default value is <strong id="b38905168155919"><a name="b38905168155919"></a><a name="b38905168155919"></a>Default</strong>. The value can only be set to <strong id="b842352706203730"><a name="b842352706203730"></a><a name="b842352706203730"></a>Extended</strong> if <strong id="b842352706203741"><a name="b842352706203741"></a><a name="b842352706203741"></a>ssl_protocols</strong> is set to <strong id="b842352706203754"><a name="b842352706203754"></a><a name="b842352706203754"></a>TLSv1.2 TLSv1.1 TLSv1</strong>.</p>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020100158_section13189358"></a>

-   Request parameters

    None


-   Example request

    ```
    {
        "name": "listener1",
        "description": "",
        "loadbalancer_id": "0b07acf06d243925bc24a0ac7445267a",
        "protocol": "HTTP",
        "port": 88,
        "backend_protocol": "HTTP",
        "backend_port": 80,
        "lb_algorithm": "roundrobin",
        "session_sticky": true,
        "sticky_session_type": "insert",
        "cookie_timeout": 100,
        "tcp_draining": true,
        "tcp_draining_timeout": 5
    }
    ```


## Response<a name="en-us_topic_0020100158_section51595365"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="en-us_topic_0020100158_table21717427154613"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100158_row14831958154613"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100158_p60537982154613"><a name="en-us_topic_0020100158_p60537982154613"></a><a name="en-us_topic_0020100158_p60537982154613"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100158_p56002375174110"><a name="en-us_topic_0020100158_p56002375174110"></a><a name="en-us_topic_0020100158_p56002375174110"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="62%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100158_p39444710154613"><a name="en-us_topic_0020100158_p39444710154613"></a><a name="en-us_topic_0020100158_p39444710154613"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100158_row54920009105559"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p19335774105559"><a name="en-us_topic_0020100158_p19335774105559"></a><a name="en-us_topic_0020100158_p19335774105559"></a>update_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p22693884105559"><a name="en-us_topic_0020100158_p22693884105559"></a><a name="en-us_topic_0020100158_p22693884105559"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100158_p26265290105559"><a name="en-us_topic_0020100158_p26265290105559"></a><a name="en-us_topic_0020100158_p26265290105559"></a>Specifies the time when the listener was updated.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row18853328112435"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p61871354112435"><a name="en-us_topic_0020100158_p61871354112435"></a><a name="en-us_topic_0020100158_p61871354112435"></a>backend_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p45523776112435"><a name="en-us_topic_0020100158_p45523776112435"></a><a name="en-us_topic_0020100158_p45523776112435"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100158_p63547210112435"><a name="en-us_topic_0020100158_p63547210112435"></a><a name="en-us_topic_0020100158_p63547210112435"></a>Specifies the port used by backend ECSs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row33344085112451"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p1611443112451"><a name="en-us_topic_0020100158_p1611443112451"></a><a name="en-us_topic_0020100158_p1611443112451"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p63418047112451"><a name="en-us_topic_0020100158_p63418047112451"></a><a name="en-us_topic_0020100158_p63418047112451"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100158_p36588143112451"><a name="en-us_topic_0020100158_p36588143112451"></a><a name="en-us_topic_0020100158_p36588143112451"></a>Specifies the listener ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row3132217011256"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p4791064611256"><a name="en-us_topic_0020100158_p4791064611256"></a><a name="en-us_topic_0020100158_p4791064611256"></a>backend_protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p5555709011256"><a name="en-us_topic_0020100158_p5555709011256"></a><a name="en-us_topic_0020100158_p5555709011256"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100158_p383046711256"><a name="en-us_topic_0020100158_p383046711256"></a><a name="en-us_topic_0020100158_p383046711256"></a>Specifies the protocol used by backend ECSs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row55939016112520"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p49640788112520"><a name="en-us_topic_0020100158_p49640788112520"></a><a name="en-us_topic_0020100158_p49640788112520"></a>sticky_session_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p61480912112520"><a name="en-us_topic_0020100158_p61480912112520"></a><a name="en-us_topic_0020100158_p61480912112520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p650285517815"><a name="p650285517815"></a><a name="p650285517815"></a>Specifies where the cookie is from. The only value is <strong id="b1833462017910"><a name="b1833462017910"></a><a name="b1833462017910"></a>insert</strong>, indicating that the cookie is inserted by the load balancer. This parameter is valid when <strong id="b141157415910"><a name="b141157415910"></a><a name="b141157415910"></a>protocol</strong> is set to <strong id="b10120341291"><a name="b10120341291"></a><a name="b10120341291"></a>HTTP </strong>and <strong id="b012434120911"><a name="b012434120911"></a><a name="b012434120911"></a>session_sticky</strong> to <strong id="b1112914112912"><a name="b1112914112912"></a><a name="b1112914112912"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row599332112531"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p4592171112531"><a name="en-us_topic_0020100158_p4592171112531"></a><a name="en-us_topic_0020100158_p4592171112531"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p36421590112531"><a name="en-us_topic_0020100158_p36421590112531"></a><a name="en-us_topic_0020100158_p36421590112531"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100158_p64467690112531"><a name="en-us_topic_0020100158_p64467690112531"></a><a name="en-us_topic_0020100158_p64467690112531"></a>Provides supplementary information about the listener.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row25347929112539"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p51496117112539"><a name="en-us_topic_0020100158_p51496117112539"></a><a name="en-us_topic_0020100158_p51496117112539"></a>loadbalancer_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p10435921112539"><a name="en-us_topic_0020100158_p10435921112539"></a><a name="en-us_topic_0020100158_p10435921112539"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100158_p40003298112539"><a name="en-us_topic_0020100158_p40003298112539"></a><a name="en-us_topic_0020100158_p40003298112539"></a>Specifies the load balancer ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row529666112553"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p53216976112553"><a name="en-us_topic_0020100158_p53216976112553"></a><a name="en-us_topic_0020100158_p53216976112553"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p15607836112553"><a name="en-us_topic_0020100158_p15607836112553"></a><a name="en-us_topic_0020100158_p15607836112553"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100158_p56275171112553"><a name="en-us_topic_0020100158_p56275171112553"></a><a name="en-us_topic_0020100158_p56275171112553"></a>Specifies the time when the listener was created.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row5813313811266"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p435933911266"><a name="en-us_topic_0020100158_p435933911266"></a><a name="en-us_topic_0020100158_p435933911266"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p1756217311266"><a name="en-us_topic_0020100158_p1756217311266"></a><a name="en-us_topic_0020100158_p1756217311266"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100158_p1324989511266"><a name="en-us_topic_0020100158_p1324989511266"></a><a name="en-us_topic_0020100158_p1324989511266"></a>Specifies the listener status. The value can be <strong id="b84235270693852"><a name="b84235270693852"></a><a name="b84235270693852"></a>ACTIVE</strong>, <strong id="b84235270693858"><a name="b84235270693858"></a><a name="b84235270693858"></a>PENDING_CREATE</strong>, or <strong id="b8423527069394"><a name="b8423527069394"></a><a name="b8423527069394"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row23256810112620"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p12891195112620"><a name="en-us_topic_0020100158_p12891195112620"></a><a name="en-us_topic_0020100158_p12891195112620"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p37553845112620"><a name="en-us_topic_0020100158_p37553845112620"></a><a name="en-us_topic_0020100158_p37553845112620"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100158_p21962587112620"><a name="en-us_topic_0020100158_p21962587112620"></a><a name="en-us_topic_0020100158_p21962587112620"></a>Specifies the protocol used for load balancing at Layer 4 or Layer 7.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row23310338112631"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p39880824112631"><a name="en-us_topic_0020100158_p39880824112631"></a><a name="en-us_topic_0020100158_p39880824112631"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p9121275112631"><a name="en-us_topic_0020100158_p9121275112631"></a><a name="en-us_topic_0020100158_p9121275112631"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100158_p625848112631"><a name="en-us_topic_0020100158_p625848112631"></a><a name="en-us_topic_0020100158_p625848112631"></a>Specifies the port used by the load balancer.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row62566796112640"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p65083069112640"><a name="en-us_topic_0020100158_p65083069112640"></a><a name="en-us_topic_0020100158_p65083069112640"></a>cookie_timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p37237251112640"><a name="en-us_topic_0020100158_p37237251112640"></a><a name="en-us_topic_0020100158_p37237251112640"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100158_ul32758886114017"></a><a name="en-us_topic_0020100158_ul32758886114017"></a><ul id="en-us_topic_0020100158_ul32758886114017"><li>Specifies the cookie timeout duration in the unit of minute. This parameter is valid when <strong id="b22338460155919"><a name="b22338460155919"></a><a name="b22338460155919"></a>session_sticky</strong> is set to <strong id="b66828420155919"><a name="b66828420155919"></a><a name="b66828420155919"></a>true</strong> and <strong id="b64584873155919"><a name="b64584873155919"></a><a name="b64584873155919"></a>sticky_session_type</strong> to <strong id="b44392948155919"><a name="b44392948155919"></a><a name="b44392948155919"></a>insert</strong>.</li><li>The value ranges from <strong id="b12522477399"><a name="b12522477399"></a><a name="b12522477399"></a>1</strong> to <strong id="b17837195016396"><a name="b17837195016396"></a><a name="b17837195016396"></a>1440</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row12943832112654"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p41617568112654"><a name="en-us_topic_0020100158_p41617568112654"></a><a name="en-us_topic_0020100158_p41617568112654"></a>admin_state_up</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p15579875112654"><a name="en-us_topic_0020100158_p15579875112654"></a><a name="en-us_topic_0020100158_p15579875112654"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100158_ul43214919122310"></a><a name="en-us_topic_0020100158_ul43214919122310"></a><ul id="en-us_topic_0020100158_ul43214919122310"><li>Specifies the administrative status of the load balancer.</li><li>Two options are available:<p id="en-us_topic_0020100158_p29618964122310"><a name="en-us_topic_0020100158_p29618964122310"></a><a name="en-us_topic_0020100158_p29618964122310"></a><strong id="b84235270615441"><a name="b84235270615441"></a><a name="b84235270615441"></a>false</strong>: The load balancer is disabled.</p>
    <p id="en-us_topic_0020100158_p5417219112300"><a name="en-us_topic_0020100158_p5417219112300"></a><a name="en-us_topic_0020100158_p5417219112300"></a><strong id="b842352706154416"><a name="b842352706154416"></a><a name="b842352706154416"></a>true</strong>: The load balancer is working properly.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row3479764711276"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p6289229911276"><a name="en-us_topic_0020100158_p6289229911276"></a><a name="en-us_topic_0020100158_p6289229911276"></a>session_sticky</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p6111147611276"><a name="en-us_topic_0020100158_p6111147611276"></a><a name="en-us_topic_0020100158_p6111147611276"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100158_p5108249311276"><a name="en-us_topic_0020100158_p5108249311276"></a><a name="en-us_topic_0020100158_p5108249311276"></a>Specifies whether to enable the sticky session feature. The feature is enabled when the value is <strong id="b4076309155919"><a name="b4076309155919"></a><a name="b4076309155919"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row4627360112726"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p37159682112726"><a name="en-us_topic_0020100158_p37159682112726"></a><a name="en-us_topic_0020100158_p37159682112726"></a>lb_algorithm</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p57144240112726"><a name="en-us_topic_0020100158_p57144240112726"></a><a name="en-us_topic_0020100158_p57144240112726"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100158_p65280694112726"><a name="en-us_topic_0020100158_p65280694112726"></a><a name="en-us_topic_0020100158_p65280694112726"></a>Specifies the load balancing algorithm.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row48184499112748"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p28728206112748"><a name="en-us_topic_0020100158_p28728206112748"></a><a name="en-us_topic_0020100158_p28728206112748"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p45283315112748"><a name="en-us_topic_0020100158_p45283315112748"></a><a name="en-us_topic_0020100158_p45283315112748"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100158_p44069876112748"><a name="en-us_topic_0020100158_p44069876112748"></a><a name="en-us_topic_0020100158_p44069876112748"></a>Specifies the listener name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row733305615859"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p5106616415859"><a name="en-us_topic_0020100158_p5106616415859"></a><a name="en-us_topic_0020100158_p5106616415859"></a>tcp_draining</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p3765702915859"><a name="en-us_topic_0020100158_p3765702915859"></a><a name="en-us_topic_0020100158_p3765702915859"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100158_ul27127532192359"></a><a name="en-us_topic_0020100158_ul27127532192359"></a><ul id="en-us_topic_0020100158_ul27127532192359"><li>Specifies whether to maintain TCP connections to a backend ECS that has been removed. This parameter is valid when <strong id="b60818144155919"><a name="b60818144155919"></a><a name="b60818144155919"></a>protocol</strong> is set to <strong id="b10492386155919"><a name="b10492386155919"></a><a name="b10492386155919"></a>TCP</strong>.</li><li>The value can be <strong id="b8815401155919"><a name="b8815401155919"></a><a name="b8815401155919"></a>true</strong> or <strong id="b12229752155919"><a name="b12229752155919"></a><a name="b12229752155919"></a>false</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row6046710715859"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p2215775615859"><a name="en-us_topic_0020100158_p2215775615859"></a><a name="en-us_topic_0020100158_p2215775615859"></a>tcp_draining_timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p1924037015859"><a name="en-us_topic_0020100158_p1924037015859"></a><a name="en-us_topic_0020100158_p1924037015859"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100158_ul57494889192412"></a><a name="en-us_topic_0020100158_ul57494889192412"></a><ul id="en-us_topic_0020100158_ul57494889192412"><li>Specifies the timeout duration for maintaining TCP connections to a backend ECS that has been removed in the unit of minute.<p id="en-us_topic_0020100158_p55709469114058"><a name="en-us_topic_0020100158_p55709469114058"></a><a name="en-us_topic_0020100158_p55709469114058"></a>This parameter is valid when <strong id="b51490896155919"><a name="b51490896155919"></a><a name="b51490896155919"></a>protocol</strong> is set to <strong id="b60764881155919"><a name="b60764881155919"></a><a name="b60764881155919"></a>TCP</strong> and <strong id="b10013022155919"><a name="b10013022155919"></a><a name="b10013022155919"></a>tcp_draining</strong> to <strong id="b23008334155919"><a name="b23008334155919"></a><a name="b23008334155919"></a>true</strong>.</p>
    </li><li>The value ranges from <strong id="b115441723135612"><a name="b115441723135612"></a><a name="b115441723135612"></a>0</strong> to <strong id="b10725182615565"><a name="b10725182615565"></a><a name="b10725182615565"></a>60</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row3950876919312"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p4592700819328"><a name="en-us_topic_0020100158_p4592700819328"></a><a name="en-us_topic_0020100158_p4592700819328"></a>ssl_protocols</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p2910020719328"><a name="en-us_topic_0020100158_p2910020719328"></a><a name="en-us_topic_0020100158_p2910020719328"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100158_ul516171213255"></a><a name="en-us_topic_0020100158_ul516171213255"></a><ul id="en-us_topic_0020100158_ul516171213255"><li>Specifies the supported SSL/TLS protocol version.</li><li>This parameter is available only when <strong id="b842352706173219"><a name="b842352706173219"></a><a name="b842352706173219"></a>protocol</strong> is set to <strong id="b842352706173222"><a name="b842352706173222"></a><a name="b842352706173222"></a>HTTPS</strong> or <strong id="b842352706181923"><a name="b842352706181923"></a><a name="b842352706181923"></a>SSL</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row6340712519315"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p1571312819328"><a name="en-us_topic_0020100158_p1571312819328"></a><a name="en-us_topic_0020100158_p1571312819328"></a>ssl_ciphers</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p6480388419328"><a name="en-us_topic_0020100158_p6480388419328"></a><a name="en-us_topic_0020100158_p6480388419328"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100158_ul2094040721332"></a><a name="en-us_topic_0020100158_ul2094040721332"></a><ul id="en-us_topic_0020100158_ul2094040721332"><li>Specifies the cipher suite of an encryption protocol.</li><li>This parameter is available only when <strong id="b65909934155919"><a name="b65909934155919"></a><a name="b65909934155919"></a>protocol</strong> is set to <strong id="b56318499155919"><a name="b56318499155919"></a><a name="b56318499155919"></a>HTTPS</strong> or <strong id="b65504537155919"><a name="b65504537155919"></a><a name="b65504537155919"></a>SSL</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row3421333519319"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p5715067519328"><a name="en-us_topic_0020100158_p5715067519328"></a><a name="en-us_topic_0020100158_p5715067519328"></a>certificate_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p6580199019328"><a name="en-us_topic_0020100158_p6580199019328"></a><a name="en-us_topic_0020100158_p6580199019328"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100158_ul43113047213310"></a><a name="en-us_topic_0020100158_ul43113047213310"></a><ul id="en-us_topic_0020100158_ul43113047213310"><li>Specifies the default certificate ID.</li><li>This parameter is available only when <strong id="b1768828155919"><a name="b1768828155919"></a><a name="b1768828155919"></a>protocol</strong> is set to <strong id="b15919455155919"><a name="b15919455155919"></a><a name="b15919455155919"></a>HTTPS</strong> or <strong id="b14407493155919"><a name="b14407493155919"></a><a name="b14407493155919"></a>SSL</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row5877129719322"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100158_p560472819328"><a name="en-us_topic_0020100158_p560472819328"></a><a name="en-us_topic_0020100158_p560472819328"></a>certificates</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100158_p5132986019328"><a name="en-us_topic_0020100158_p5132986019328"></a><a name="en-us_topic_0020100158_p5132986019328"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100158_ul47134914213235"></a><a name="en-us_topic_0020100158_ul47134914213235"></a><ul id="en-us_topic_0020100158_ul47134914213235"><li>Lists the certificate IDs if <strong id="b62757485155919"><a name="b62757485155919"></a><a name="b62757485155919"></a>protocol</strong> is set to <strong id="b27946455155919"><a name="b27946455155919"></a><a name="b27946455155919"></a>HTTPS</strong>.</li><li>This parameter is mandatory in the SNI scenario.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "update_time": "2015-09-15 07:41:17",
        "backend_port": 80,
        "tcp_draining": true,
        "id": "248425d7b97dc26920eb23720115e068",
        "backend_protocol": "HTTP",
        "sticky_session_type": "insert",
        "description": "",
        "loadbalancer_id": "0b07acf06d243925bc24a0ac7445267a",
        "create_time": "2015-09-15 07:41:17",
        "status": "ACTIVE",
        "protocol": "TCP",
        "port": 88,
        "cookie_timeout": 100,
        "admin_state_up": true,
        "session_sticky": true,
        "lb_algorithm": "roundrobin",
        "name": "listener1",
        "tcp_draining": true,
        "tcp_draining_timeout": 5
    }
    ```


## Status Code<a name="en-us_topic_0020100158_section61705107"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0020100158_table55746241151444"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100158_row2933765151444"><th class="cellrowborder" valign="top" width="12.26%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020100158_p36308450151444"><a name="en-us_topic_0020100158_p36308450151444"></a><a name="en-us_topic_0020100158_p36308450151444"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.5%" id="mcps1.1.4.1.2"><p id="p20658614155915"><a name="p20658614155915"></a><a name="p20658614155915"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020100158_p55303327151444"><a name="en-us_topic_0020100158_p55303327151444"></a><a name="en-us_topic_0020100158_p55303327151444"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100158_row50384484151444"><td class="cellrowborder" valign="top" width="12.26%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100158_p54611418151444"><a name="en-us_topic_0020100158_p54611418151444"></a><a name="en-us_topic_0020100158_p54611418151444"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.5%" headers="mcps1.1.4.1.2 "><p id="p570624225916"><a name="p570624225916"></a><a name="p570624225916"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100158_p61448744151444"><a name="en-us_topic_0020100158_p61448744151444"></a><a name="en-us_topic_0020100158_p61448744151444"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row16167792151444"><td class="cellrowborder" valign="top" width="12.26%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100158_p34522807151444"><a name="en-us_topic_0020100158_p34522807151444"></a><a name="en-us_topic_0020100158_p34522807151444"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.5%" headers="mcps1.1.4.1.2 "><p id="p570711427599"><a name="p570711427599"></a><a name="p570711427599"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100158_p44883945151444"><a name="en-us_topic_0020100158_p44883945151444"></a><a name="en-us_topic_0020100158_p44883945151444"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row1302327151444"><td class="cellrowborder" valign="top" width="12.26%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100158_p38379639151444"><a name="en-us_topic_0020100158_p38379639151444"></a><a name="en-us_topic_0020100158_p38379639151444"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.5%" headers="mcps1.1.4.1.2 "><p id="p197071142175919"><a name="p197071142175919"></a><a name="p197071142175919"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100158_p21743064151444"><a name="en-us_topic_0020100158_p21743064151444"></a><a name="en-us_topic_0020100158_p21743064151444"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row61469852151444"><td class="cellrowborder" valign="top" width="12.26%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100158_p13002129151444"><a name="en-us_topic_0020100158_p13002129151444"></a><a name="en-us_topic_0020100158_p13002129151444"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.5%" headers="mcps1.1.4.1.2 "><p id="p117074428598"><a name="p117074428598"></a><a name="p117074428598"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100158_p46539514151444"><a name="en-us_topic_0020100158_p46539514151444"></a><a name="en-us_topic_0020100158_p46539514151444"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row16202446151444"><td class="cellrowborder" valign="top" width="12.26%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100158_p37329729151444"><a name="en-us_topic_0020100158_p37329729151444"></a><a name="en-us_topic_0020100158_p37329729151444"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.5%" headers="mcps1.1.4.1.2 "><p id="p147073421594"><a name="p147073421594"></a><a name="p147073421594"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100158_p3809180151444"><a name="en-us_topic_0020100158_p3809180151444"></a><a name="en-us_topic_0020100158_p3809180151444"></a>System error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100158_row34282624151444"><td class="cellrowborder" valign="top" width="12.26%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100158_p25429196151444"><a name="en-us_topic_0020100158_p25429196151444"></a><a name="en-us_topic_0020100158_p25429196151444"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.5%" headers="mcps1.1.4.1.2 "><p id="p147075427593"><a name="p147075427593"></a><a name="p147075427593"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100158_p46498963151444"><a name="en-us_topic_0020100158_p46498963151444"></a><a name="en-us_topic_0020100158_p46498963151444"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


