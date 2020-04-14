# Modifying a Listener<a name="EN-US_TOPIC_0096561508"></a>

## Function<a name="en-us_topic_0020100160_section4781813"></a>

This API is used to modify the listener information, including the listener name, description, and status.

## URI<a name="en-us_topic_0020100160_section43036322"></a>

PUT /v1.0/\{project\_id\}/elbaas/listeners/\{listener\_id\}

**Table  1**  Parameter description

<a name="en-us_topic_0020100160_table9289124"></a>
<table><thead align="left"><tr id="en-us_topic_0020100160_row26669028"><th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020100160_p12707688"><a name="en-us_topic_0020100160_p12707688"></a><a name="en-us_topic_0020100160_p12707688"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100160_p22689808"><a name="en-us_topic_0020100160_p22689808"></a><a name="en-us_topic_0020100160_p22689808"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100160_p54629719175950"><a name="en-us_topic_0020100160_p54629719175950"></a><a name="en-us_topic_0020100160_p54629719175950"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="61.61616161616161%" id="mcps1.2.5.1.4"><p id="p1164191644317"><a name="p1164191644317"></a><a name="p1164191644317"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020100160_row55573578113226"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="p1063965785816"><a name="p1063965785816"></a><a name="p1063965785816"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100160_p25167590113245"><a name="en-us_topic_0020100160_p25167590113245"></a><a name="en-us_topic_0020100160_p25167590113245"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100160_p62345018113249"><a name="en-us_topic_0020100160_p62345018113249"></a><a name="en-us_topic_0020100160_p62345018113249"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100160_p57392946113251"><a name="en-us_topic_0020100160_p57392946113251"></a><a name="en-us_topic_0020100160_p57392946113251"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
<tr id="en-us_topic_0020100160_row20374254"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100160_p39701876"><a name="en-us_topic_0020100160_p39701876"></a><a name="en-us_topic_0020100160_p39701876"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100160_p61735358"><a name="en-us_topic_0020100160_p61735358"></a><a name="en-us_topic_0020100160_p61735358"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100160_p62931151175950"><a name="en-us_topic_0020100160_p62931151175950"></a><a name="en-us_topic_0020100160_p62931151175950"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100160_p34508084"><a name="en-us_topic_0020100160_p34508084"></a><a name="en-us_topic_0020100160_p34508084"></a>Specifies the listener ID.</p>
</td>
</tr>
<tr id="en-us_topic_0020100160_row42137308"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100160_p57678784"><a name="en-us_topic_0020100160_p57678784"></a><a name="en-us_topic_0020100160_p57678784"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100160_p41469957"><a name="en-us_topic_0020100160_p41469957"></a><a name="en-us_topic_0020100160_p41469957"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100160_p64258455175950"><a name="en-us_topic_0020100160_p64258455175950"></a><a name="en-us_topic_0020100160_p64258455175950"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100160_ul168989449327"></a><a name="en-us_topic_0020100160_ul168989449327"></a><ul id="en-us_topic_0020100160_ul168989449327"><li>Specifies the listener name.</li><li>The value is a string of 1 to 64 characters that consist of Chinese characters, letters, digits, underscores (_), and hyphens (-).</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100160_row16353430"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100160_p49559423"><a name="en-us_topic_0020100160_p49559423"></a><a name="en-us_topic_0020100160_p49559423"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100160_p54890288"><a name="en-us_topic_0020100160_p54890288"></a><a name="en-us_topic_0020100160_p54890288"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100160_p21840952175950"><a name="en-us_topic_0020100160_p21840952175950"></a><a name="en-us_topic_0020100160_p21840952175950"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100160_ul430844529340"></a><a name="en-us_topic_0020100160_ul430844529340"></a><ul id="en-us_topic_0020100160_ul430844529340"><li>Provides supplementary information about the listener.</li><li>The value is a string of 0 to 128 characters and cannot contain angle brackets (&lt; and &gt;).</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100160_row304174251997"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100160_p537368181997"><a name="en-us_topic_0020100160_p537368181997"></a><a name="en-us_topic_0020100160_p537368181997"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100160_p577149761997"><a name="en-us_topic_0020100160_p577149761997"></a><a name="en-us_topic_0020100160_p577149761997"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100160_p33965204191013"><a name="en-us_topic_0020100160_p33965204191013"></a><a name="en-us_topic_0020100160_p33965204191013"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100160_ul206529799350"></a><a name="en-us_topic_0020100160_ul206529799350"></a><ul id="en-us_topic_0020100160_ul206529799350"><li>Specifies the port used by the load balancer.</li><li>The port number ranges from 1 to 65535.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100160_row5798233419938"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100160_p3288012019938"><a name="en-us_topic_0020100160_p3288012019938"></a><a name="en-us_topic_0020100160_p3288012019938"></a>backend_port</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100160_p4604402719938"><a name="en-us_topic_0020100160_p4604402719938"></a><a name="en-us_topic_0020100160_p4604402719938"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100160_p56852872191045"><a name="en-us_topic_0020100160_p56852872191045"></a><a name="en-us_topic_0020100160_p56852872191045"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100160_ul52526178941"></a><a name="en-us_topic_0020100160_ul52526178941"></a><ul id="en-us_topic_0020100160_ul52526178941"><li>Specifies the port used by backend ECSs.</li><li>The port number ranges from 1 to 65535.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100160_row47219577161424"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100160_p22429676161455"><a name="en-us_topic_0020100160_p22429676161455"></a><a name="en-us_topic_0020100160_p22429676161455"></a>lb_algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100160_p4864473161455"><a name="en-us_topic_0020100160_p4864473161455"></a><a name="en-us_topic_0020100160_p4864473161455"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100160_p58478051161455"><a name="en-us_topic_0020100160_p58478051161455"></a><a name="en-us_topic_0020100160_p58478051161455"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100160_ul548588509410"></a><a name="en-us_topic_0020100160_ul548588509410"></a><ul id="en-us_topic_0020100160_ul548588509410"><li>Specifies the load balancing algorithm.</li><li>The value can be <strong>roundrobin</strong>, <strong>leastconn</strong>, or <strong>source</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100160_row39298132105852"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100160_p29032133105852"><a name="en-us_topic_0020100160_p29032133105852"></a><a name="en-us_topic_0020100160_p29032133105852"></a>tcp_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100160_p2792574105852"><a name="en-us_topic_0020100160_p2792574105852"></a><a name="en-us_topic_0020100160_p2792574105852"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100160_p24871976105852"><a name="en-us_topic_0020100160_p24871976105852"></a><a name="en-us_topic_0020100160_p24871976105852"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100160_ul63770335192147"></a><a name="en-us_topic_0020100160_ul63770335192147"></a><ul id="en-us_topic_0020100160_ul63770335192147"><li>Specifies the TCP session timeout duration. This parameter is valid when <strong id="b121408947117235"><a name="b121408947117235"></a><a name="b121408947117235"></a>protocol</strong> is set to <strong id="b182340233017235"><a name="b182340233017235"></a><a name="b182340233017235"></a>TCP</strong>.</li><li>The value ranges from <strong id="b13218040407"><a name="b13218040407"></a><a name="b13218040407"></a>1</strong> to <strong id="b2817136164019"><a name="b2817136164019"></a><a name="b2817136164019"></a>1440</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100160_row189139051566"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100160_p81207881566"><a name="en-us_topic_0020100160_p81207881566"></a><a name="en-us_topic_0020100160_p81207881566"></a>tcp_draining</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100160_p538041091566"><a name="en-us_topic_0020100160_p538041091566"></a><a name="en-us_topic_0020100160_p538041091566"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100160_p631655421566"><a name="en-us_topic_0020100160_p631655421566"></a><a name="en-us_topic_0020100160_p631655421566"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100160_ul393854149420"></a><a name="en-us_topic_0020100160_ul393854149420"></a><ul id="en-us_topic_0020100160_ul393854149420"><li>Specifies whether to maintain TCP connections to a backend ECS that has been removed. This parameter is valid when <strong id="b84235270616396"><a name="b84235270616396"></a><a name="b84235270616396"></a>protocol</strong> is set to <strong id="b842352706163915"><a name="b842352706163915"></a><a name="b842352706163915"></a>TCP</strong>.</li><li>The value can be <strong id="b1845444702162720"><a name="b1845444702162720"></a><a name="b1845444702162720"></a>true</strong> or <strong id="b673679985162720"><a name="b673679985162720"></a><a name="b673679985162720"></a>false</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100160_row393842471566"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100160_p326273311566"><a name="en-us_topic_0020100160_p326273311566"></a><a name="en-us_topic_0020100160_p326273311566"></a>tcp_draining_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100160_p255681741566"><a name="en-us_topic_0020100160_p255681741566"></a><a name="en-us_topic_0020100160_p255681741566"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100160_p577562261566"><a name="en-us_topic_0020100160_p577562261566"></a><a name="en-us_topic_0020100160_p577562261566"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100160_ul471245999430"></a><a name="en-us_topic_0020100160_ul471245999430"></a><ul id="en-us_topic_0020100160_ul471245999430"><li>Specifies the timeout duration for maintaining TCP connections to a backend ECS that has been removed. The unit is minute.<p id="en-us_topic_0020100160_p24011364113725"><a name="en-us_topic_0020100160_p24011364113725"></a><a name="en-us_topic_0020100160_p24011364113725"></a>This parameter is valid when <strong id="b84235270617553"><a name="b84235270617553"></a><a name="b84235270617553"></a>protocol</strong> is set to <strong id="b8423527061761"><a name="b8423527061761"></a><a name="b8423527061761"></a>TCP</strong> and <strong id="b84235270617611"><a name="b84235270617611"></a><a name="b84235270617611"></a>tcp_draining</strong> to <strong id="b84235270617620"><a name="b84235270617620"></a><a name="b84235270617620"></a>true</strong>.</p>
</li><li>The value ranges from <strong id="b635843813563"><a name="b635843813563"></a><a name="b635843813563"></a>0</strong> to <strong id="b9706194055619"><a name="b9706194055619"></a><a name="b9706194055619"></a>60</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100160_row56817769104542"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100160_p1095405210465"><a name="en-us_topic_0020100160_p1095405210465"></a><a name="en-us_topic_0020100160_p1095405210465"></a>udp_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100160_p3059558010465"><a name="en-us_topic_0020100160_p3059558010465"></a><a name="en-us_topic_0020100160_p3059558010465"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100160_p69793410465"><a name="en-us_topic_0020100160_p69793410465"></a><a name="en-us_topic_0020100160_p69793410465"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100160_ul750390410465"></a><a name="en-us_topic_0020100160_ul750390410465"></a><ul id="en-us_topic_0020100160_ul750390410465"><li>Specifies the UDP session timeout duration. This parameter is valid when <strong id="b2040813087"><a name="b2040813087"></a><a name="b2040813087"></a>protocol</strong> is set to <strong id="b1576024018"><a name="b1576024018"></a><a name="b1576024018"></a>UDP</strong>.</li><li>The value ranges from <strong id="b5193101413406"><a name="b5193101413406"></a><a name="b5193101413406"></a>1</strong> to <strong id="b1695941711406"><a name="b1695941711406"></a><a name="b1695941711406"></a>1440</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100160_row6459909894829"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100160_p4661929694837"><a name="en-us_topic_0020100160_p4661929694837"></a><a name="en-us_topic_0020100160_p4661929694837"></a>ssl_protocols</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100160_p1806662694837"><a name="en-us_topic_0020100160_p1806662694837"></a><a name="en-us_topic_0020100160_p1806662694837"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100160_p5411058894837"><a name="en-us_topic_0020100160_p5411058894837"></a><a name="en-us_topic_0020100160_p5411058894837"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100160_ul51896692211821"></a><a name="en-us_topic_0020100160_ul51896692211821"></a><ul id="en-us_topic_0020100160_ul51896692211821"><li>Specifies the supported SSL/TLS protocol version. This parameter is available only when <strong id="b842352706203214"><a name="b842352706203214"></a><a name="b842352706203214"></a>protocol</strong> is set to <strong id="b842352706203232"><a name="b842352706203232"></a><a name="b842352706203232"></a>HTTPS</strong> or <strong id="b842352706173557"><a name="b842352706173557"></a><a name="b842352706173557"></a>SSL</strong>.</li><li>The value is <strong id="b842352706203310"><a name="b842352706203310"></a><a name="b842352706203310"></a>TLSv1.2</strong> or <strong id="b26736002204755"><a name="b26736002204755"></a><a name="b26736002204755"></a>TLSv1.2 TLSv1.1 TLSv1 </strong>and the default value is <strong id="b84235270620375"><a name="b84235270620375"></a><a name="b84235270620375"></a>TLSv1.2</strong>.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100160_row527232394834"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100160_p4216749494837"><a name="en-us_topic_0020100160_p4216749494837"></a><a name="en-us_topic_0020100160_p4216749494837"></a>ssl_ciphers</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100160_p6012386294837"><a name="en-us_topic_0020100160_p6012386294837"></a><a name="en-us_topic_0020100160_p6012386294837"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100160_p3819463494837"><a name="en-us_topic_0020100160_p3819463494837"></a><a name="en-us_topic_0020100160_p3819463494837"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100160_ul55735025211821"></a><a name="en-us_topic_0020100160_ul55735025211821"></a><ul id="en-us_topic_0020100160_ul55735025211821"><li>Specifies the cipher suites supported by a specific SSL/TLS protocol version. This parameter is available only when <strong id="b1938472571311"><a name="b1938472571311"></a><a name="b1938472571311"></a>protocol</strong> is set to <strong id="b173851425191310"><a name="b173851425191310"></a><a name="b173851425191310"></a>HTTPS</strong> or <strong id="b15385152514132"><a name="b15385152514132"></a><a name="b15385152514132"></a>SSL</strong>.</li><li>The value is <strong id="b842352706102954"><a name="b842352706102954"></a><a name="b842352706102954"></a>Default</strong>, <strong id="b842352706101415"><a name="b842352706101415"></a><a name="b842352706101415"></a>Extended</strong>, or <strong id="b842352706103022"><a name="b842352706103022"></a><a name="b842352706103022"></a>Strict</strong>.<p id="en-us_topic_0020100160_p29970700211821"><a name="en-us_topic_0020100160_p29970700211821"></a><a name="en-us_topic_0020100160_p29970700211821"></a>The value of <strong id="b1592461146101451"><a name="b1592461146101451"></a><a name="b1592461146101451"></a>Default</strong> is <strong id="b84235270610151"><a name="b84235270610151"></a><a name="b84235270610151"></a>ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256</strong>.</p>
<p id="en-us_topic_0020100160_p1300844211821"><a name="en-us_topic_0020100160_p1300844211821"></a><a name="en-us_topic_0020100160_p1300844211821"></a>The value of <strong id="b1679441012203631"><a name="b1679441012203631"></a><a name="b1679441012203631"></a>Extended</strong> is <strong id="b842352706203650"><a name="b842352706203650"></a><a name="b842352706203650"></a>ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:AES128-SHA256:AES256-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES128-SHA:DHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:AES128-SHA:AES256-SHA:DHE-DSS-AES128-SHA:CAMELLIA128-SHA:EDH-RSA-DES-CBC3-SHA:DES-CBC3-SHA:ECDHE-RSA-RC4-SHA:RC4-SHA:DHE-RSA-AES256-SHA:DHE-DSS-AES256-SHA:DHE-RSA-CAMELLIA256-SHA:DHE-DSS-CAMELLIA256-SHA:CAMELLIA256-SHA:EDH-DSS-DES-CBC3-SHA:DHE-RSA-CAMELLIA128-SHA:DHE-DSS-CAMELLIA128-SHA</strong>.</p>
<p id="en-us_topic_0020100160_p11707601211821"><a name="en-us_topic_0020100160_p11707601211821"></a><a name="en-us_topic_0020100160_p11707601211821"></a>The value of <strong id="b842352706103424"><a name="b842352706103424"></a><a name="b842352706103424"></a>Strict</strong> is <strong id="b842352706103456"><a name="b842352706103456"></a><a name="b842352706103456"></a>ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256</strong>.</p>
<p id="en-us_topic_0020100160_p38259546211821"><a name="en-us_topic_0020100160_p38259546211821"></a><a name="en-us_topic_0020100160_p38259546211821"></a>The default value is <strong id="b63854404"><a name="b63854404"></a><a name="b63854404"></a>Default</strong>. The value can only be set to <strong id="b842352706203730"><a name="b842352706203730"></a><a name="b842352706203730"></a>Extended</strong> if <strong id="b842352706203741"><a name="b842352706203741"></a><a name="b842352706203741"></a>ssl_protocols</strong> is set to <strong id="b842352706203754"><a name="b842352706203754"></a><a name="b842352706203754"></a>TLSv1.2 TLSv1.1 TLSv1</strong>.</p>
</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100160_row171627801988"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100160_p4592064619814"><a name="en-us_topic_0020100160_p4592064619814"></a><a name="en-us_topic_0020100160_p4592064619814"></a>certificate_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100160_p2858485119814"><a name="en-us_topic_0020100160_p2858485119814"></a><a name="en-us_topic_0020100160_p2858485119814"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100160_p3367161319814"><a name="en-us_topic_0020100160_p3367161319814"></a><a name="en-us_topic_0020100160_p3367161319814"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100160_ul4304612319814"></a><a name="en-us_topic_0020100160_ul4304612319814"></a><ul id="en-us_topic_0020100160_ul4304612319814"><li>Specifies the default certificate ID. This parameter is mandatory when <strong id="b84235270620497"><a name="b84235270620497"></a><a name="b84235270620497"></a>protocol</strong> is set to <strong id="b436618102610"><a name="b436618102610"></a><a name="b436618102610"></a>HTTPS</strong> or <strong id="b5711045266"><a name="b5711045266"></a><a name="b5711045266"></a>SSL</strong>.</li><li>The ID can be obtained from the certificate list.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0020100160_row4393669219811"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100160_p1521564819814"><a name="en-us_topic_0020100160_p1521564819814"></a><a name="en-us_topic_0020100160_p1521564819814"></a>certificates</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100160_p2450794519814"><a name="en-us_topic_0020100160_p2450794519814"></a><a name="en-us_topic_0020100160_p2450794519814"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100160_p3898649019814"><a name="en-us_topic_0020100160_p3898649019814"></a><a name="en-us_topic_0020100160_p3898649019814"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0020100160_ul378911619814"></a><a name="en-us_topic_0020100160_ul378911619814"></a><ul id="en-us_topic_0020100160_ul378911619814"><li>Lists the certificate IDs if <strong id="b842352706172631"><a name="b842352706172631"></a><a name="b842352706172631"></a>protocol</strong> is set to <strong id="b842352706172635"><a name="b842352706172635"></a><a name="b842352706172635"></a>HTTPS</strong>.</li><li>This parameter is mandatory in the SNI scenario.</li><li>This parameter is valid only when the load balancer is a public network load balancer.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020100160_section51782583"></a>

-   Request parameters

    None


-   Example request

    ```
    {
        "name": "lis",
        "description": "",
        "port": 9090,
        "backend_port": 9090,
        "lb_algorithm": "roundrobin"
    }
    ```


## Response<a name="en-us_topic_0020100160_section63390070"></a>

-   Response parameters

    **Table  2**  Parameter description

    <a name="en-us_topic_0020100160_table2976606163828"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100160_row726656163828"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100160_p58859194163828"><a name="en-us_topic_0020100160_p58859194163828"></a><a name="en-us_topic_0020100160_p58859194163828"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100160_p2865400163828"><a name="en-us_topic_0020100160_p2865400163828"></a><a name="en-us_topic_0020100160_p2865400163828"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="65%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100160_p30770851163828"><a name="en-us_topic_0020100160_p30770851163828"></a><a name="en-us_topic_0020100160_p30770851163828"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100160_row9410978163828"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p24091742163828"><a name="en-us_topic_0020100160_p24091742163828"></a><a name="en-us_topic_0020100160_p24091742163828"></a>update_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p5274046163828"><a name="en-us_topic_0020100160_p5274046163828"></a><a name="en-us_topic_0020100160_p5274046163828"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100160_p24544554163828"><a name="en-us_topic_0020100160_p24544554163828"></a><a name="en-us_topic_0020100160_p24544554163828"></a>Specifies the time when the listener was updated.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row19574401163828"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p42022635163828"><a name="en-us_topic_0020100160_p42022635163828"></a><a name="en-us_topic_0020100160_p42022635163828"></a>backend_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p48390294163828"><a name="en-us_topic_0020100160_p48390294163828"></a><a name="en-us_topic_0020100160_p48390294163828"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100160_p27299754163828"><a name="en-us_topic_0020100160_p27299754163828"></a><a name="en-us_topic_0020100160_p27299754163828"></a>Specifies the port used by backend ECSs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row44371194163828"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p37296957163828"><a name="en-us_topic_0020100160_p37296957163828"></a><a name="en-us_topic_0020100160_p37296957163828"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p1154685163828"><a name="en-us_topic_0020100160_p1154685163828"></a><a name="en-us_topic_0020100160_p1154685163828"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100160_p26420641163828"><a name="en-us_topic_0020100160_p26420641163828"></a><a name="en-us_topic_0020100160_p26420641163828"></a>Specifies the listener ID in UUID format.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row36459180163828"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p403618163828"><a name="en-us_topic_0020100160_p403618163828"></a><a name="en-us_topic_0020100160_p403618163828"></a>backend_protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p32693104163828"><a name="en-us_topic_0020100160_p32693104163828"></a><a name="en-us_topic_0020100160_p32693104163828"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100160_p30895807163828"><a name="en-us_topic_0020100160_p30895807163828"></a><a name="en-us_topic_0020100160_p30895807163828"></a>Specifies the protocol used by backend ECSs.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row9626815163828"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p41574513163828"><a name="en-us_topic_0020100160_p41574513163828"></a><a name="en-us_topic_0020100160_p41574513163828"></a>sticky_session_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p12092408163828"><a name="en-us_topic_0020100160_p12092408163828"></a><a name="en-us_topic_0020100160_p12092408163828"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="p1931532105417"><a name="p1931532105417"></a><a name="p1931532105417"></a>Specifies where the cookie is from. The only value is <strong id="b6338190125213"><a name="b6338190125213"></a><a name="b6338190125213"></a>insert</strong>, indicating that the cookie is inserted by the load balancer.</p>
    <a name="en-us_topic_0020100158_ul1811738819212"></a><a name="en-us_topic_0020100158_ul1811738819212"></a><ul id="en-us_topic_0020100158_ul1811738819212"><li>This parameter is valid when <strong id="b1622718256530"><a name="b1622718256530"></a><a name="b1622718256530"></a>protocol</strong> is set to <strong id="b82271825205315"><a name="b82271825205315"></a><a name="b82271825205315"></a>HTTP</strong> and <strong id="b15227925115313"><a name="b15227925115313"></a><a name="b15227925115313"></a>session_sticky</strong> to <strong id="b13227162545317"><a name="b13227162545317"></a><a name="b13227162545317"></a>true</strong>.</li><li>This parameter is invalid when <strong id="b667609043165942"><a name="b667609043165942"></a><a name="b667609043165942"></a>protocol</strong> is set to <strong id="b1478565795165942"><a name="b1478565795165942"></a><a name="b1478565795165942"></a>TCP</strong>, <strong id="b17681111994912"><a name="b17681111994912"></a><a name="b17681111994912"></a>SSL</strong>, or <strong id="b2360121102648"><a name="b2360121102648"></a><a name="b2360121102648"></a>UDP</strong>, which means that the parameter is unavailable or its value is set to <strong id="b5386110135812"><a name="b5386110135812"></a><a name="b5386110135812"></a>null</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row24104864163828"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p6336969163828"><a name="en-us_topic_0020100160_p6336969163828"></a><a name="en-us_topic_0020100160_p6336969163828"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p43532515163828"><a name="en-us_topic_0020100160_p43532515163828"></a><a name="en-us_topic_0020100160_p43532515163828"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100160_p36472854163828"><a name="en-us_topic_0020100160_p36472854163828"></a><a name="en-us_topic_0020100160_p36472854163828"></a>Provides supplementary information about the listener.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row59820232163828"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p13600594163828"><a name="en-us_topic_0020100160_p13600594163828"></a><a name="en-us_topic_0020100160_p13600594163828"></a>loadbalancer_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p27906312163828"><a name="en-us_topic_0020100160_p27906312163828"></a><a name="en-us_topic_0020100160_p27906312163828"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100160_p45818836163828"><a name="en-us_topic_0020100160_p45818836163828"></a><a name="en-us_topic_0020100160_p45818836163828"></a>Specifies the load balancer ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row9716340163828"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p48826105163828"><a name="en-us_topic_0020100160_p48826105163828"></a><a name="en-us_topic_0020100160_p48826105163828"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p62600455163828"><a name="en-us_topic_0020100160_p62600455163828"></a><a name="en-us_topic_0020100160_p62600455163828"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100160_p37472069163828"><a name="en-us_topic_0020100160_p37472069163828"></a><a name="en-us_topic_0020100160_p37472069163828"></a>Specifies the time when the listener was created.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row1704301163828"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p3830711163828"><a name="en-us_topic_0020100160_p3830711163828"></a><a name="en-us_topic_0020100160_p3830711163828"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p41852165163828"><a name="en-us_topic_0020100160_p41852165163828"></a><a name="en-us_topic_0020100160_p41852165163828"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100160_p34582208163828"><a name="en-us_topic_0020100160_p34582208163828"></a><a name="en-us_topic_0020100160_p34582208163828"></a>Specifies the listener status. The value can be <strong id="b84235270693852"><a name="b84235270693852"></a><a name="b84235270693852"></a>ACTIVE</strong>, <strong id="b84235270693858"><a name="b84235270693858"></a><a name="b84235270693858"></a>PENDING_CREATE</strong>, or <strong id="b8423527069394"><a name="b8423527069394"></a><a name="b8423527069394"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row42804417163828"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p44605770163828"><a name="en-us_topic_0020100160_p44605770163828"></a><a name="en-us_topic_0020100160_p44605770163828"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p56297587163828"><a name="en-us_topic_0020100160_p56297587163828"></a><a name="en-us_topic_0020100160_p56297587163828"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100160_p63810660163828"><a name="en-us_topic_0020100160_p63810660163828"></a><a name="en-us_topic_0020100160_p63810660163828"></a>Specifies the protocol used for load balancing at Layer 4 or Layer 7.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row37425031163828"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p11528696163828"><a name="en-us_topic_0020100160_p11528696163828"></a><a name="en-us_topic_0020100160_p11528696163828"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p61409222163828"><a name="en-us_topic_0020100160_p61409222163828"></a><a name="en-us_topic_0020100160_p61409222163828"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100160_p8091096163828"><a name="en-us_topic_0020100160_p8091096163828"></a><a name="en-us_topic_0020100160_p8091096163828"></a>Specifies the port used by the load balancer.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row5711007163828"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p59938386163828"><a name="en-us_topic_0020100160_p59938386163828"></a><a name="en-us_topic_0020100160_p59938386163828"></a>cookie_timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p23171135163828"><a name="en-us_topic_0020100160_p23171135163828"></a><a name="en-us_topic_0020100160_p23171135163828"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><a name="ul584103516614"></a><a name="ul584103516614"></a><ul id="ul584103516614"><li>Specifies the cookie timeout duration. This parameter is valid when <strong>session_sticky</strong> is set to <strong>true</strong> and <strong>sticky_session_type</strong> to <strong>insert</strong>.</li><li>The value ranges from <strong id="b991950194019"><a name="b991950194019"></a><a name="b991950194019"></a>1</strong> to <strong id="b716655304017"><a name="b716655304017"></a><a name="b716655304017"></a>1440</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row47432814163828"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p16852719163828"><a name="en-us_topic_0020100160_p16852719163828"></a><a name="en-us_topic_0020100160_p16852719163828"></a>admin_state_up</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p22892964163828"><a name="en-us_topic_0020100160_p22892964163828"></a><a name="en-us_topic_0020100160_p22892964163828"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100160_ul29920851122422"></a><a name="en-us_topic_0020100160_ul29920851122422"></a><ul id="en-us_topic_0020100160_ul29920851122422"><li>Specifies the administrative status of the load balancer.</li><li>Two options are available:<p id="en-us_topic_0020100160_p48208035122914"><a name="en-us_topic_0020100160_p48208035122914"></a><a name="en-us_topic_0020100160_p48208035122914"></a><strong id="b84235270615441"><a name="b84235270615441"></a><a name="b84235270615441"></a>false</strong>: The load balancer is disabled.</p>
    <p id="en-us_topic_0020100160_p17351332122929"><a name="en-us_topic_0020100160_p17351332122929"></a><a name="en-us_topic_0020100160_p17351332122929"></a><strong id="b842352706154416"><a name="b842352706154416"></a><a name="b842352706154416"></a>true</strong>: The load balancer is working properly.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row45199739112617"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p10145341112621"><a name="en-us_topic_0020100160_p10145341112621"></a><a name="en-us_topic_0020100160_p10145341112621"></a>healthcheck_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p16466317112621"><a name="en-us_topic_0020100160_p16466317112621"></a><a name="en-us_topic_0020100160_p16466317112621"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100160_p58703318112621"><a name="en-us_topic_0020100160_p58703318112621"></a><a name="en-us_topic_0020100160_p58703318112621"></a>Specifies the health check ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row45972644163828"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p32796716163828"><a name="en-us_topic_0020100160_p32796716163828"></a><a name="en-us_topic_0020100160_p32796716163828"></a>session_sticky</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p39288324163828"><a name="en-us_topic_0020100160_p39288324163828"></a><a name="en-us_topic_0020100160_p39288324163828"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100160_p28237652163828"><a name="en-us_topic_0020100160_p28237652163828"></a><a name="en-us_topic_0020100160_p28237652163828"></a>Specifies whether to enable the sticky session feature. The feature is enabled when the value is <strong id="b3064351115846"><a name="b3064351115846"></a><a name="b3064351115846"></a>true</strong>. This parameter is valid only when <strong>protocol</strong> is set to <strong>HTTP</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row52812281163828"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p49936369163828"><a name="en-us_topic_0020100160_p49936369163828"></a><a name="en-us_topic_0020100160_p49936369163828"></a>lb_algorithm</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p18314102163828"><a name="en-us_topic_0020100160_p18314102163828"></a><a name="en-us_topic_0020100160_p18314102163828"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100160_p7047279163828"><a name="en-us_topic_0020100160_p7047279163828"></a><a name="en-us_topic_0020100160_p7047279163828"></a>Specifies the load balancing algorithm.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row63425515163828"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p37193070163828"><a name="en-us_topic_0020100160_p37193070163828"></a><a name="en-us_topic_0020100160_p37193070163828"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p59848665163828"><a name="en-us_topic_0020100160_p59848665163828"></a><a name="en-us_topic_0020100160_p59848665163828"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100160_p15903701163828"><a name="en-us_topic_0020100160_p15903701163828"></a><a name="en-us_topic_0020100160_p15903701163828"></a>Specifies the listener name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row1188671015102"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p6662318315102"><a name="en-us_topic_0020100160_p6662318315102"></a><a name="en-us_topic_0020100160_p6662318315102"></a>tcp_draining</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p2776876115102"><a name="en-us_topic_0020100160_p2776876115102"></a><a name="en-us_topic_0020100160_p2776876115102"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100160_ul12105328113812"></a><a name="en-us_topic_0020100160_ul12105328113812"></a><ul id="en-us_topic_0020100160_ul12105328113812"><li>Specifies whether to maintain TCP connections to a backend ECS that has been removed. This parameter is valid when <strong id="b190340412"><a name="b190340412"></a><a name="b190340412"></a>protocol</strong> is set to <strong id="b9648309"><a name="b9648309"></a><a name="b9648309"></a>TCP</strong>.</li><li>The value can be <strong id="b838714417584"><a name="b838714417584"></a><a name="b838714417584"></a>true</strong> or <strong id="b038784115811"><a name="b038784115811"></a><a name="b038784115811"></a>false</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row877728615102"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p1779473715102"><a name="en-us_topic_0020100160_p1779473715102"></a><a name="en-us_topic_0020100160_p1779473715102"></a>tcp_draining_timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p3208758115102"><a name="en-us_topic_0020100160_p3208758115102"></a><a name="en-us_topic_0020100160_p3208758115102"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0020100160_ul40286558113818"></a><a name="en-us_topic_0020100160_ul40286558113818"></a><ul id="en-us_topic_0020100160_ul40286558113818"><li>Specifies the timeout duration for maintaining TCP connections to a backend ECS that has been removed. The unit is minute.<p id="en-us_topic_0020100160_p3371275711394"><a name="en-us_topic_0020100160_p3371275711394"></a><a name="en-us_topic_0020100160_p3371275711394"></a>This parameter is valid when <strong id="b530737829"><a name="b530737829"></a><a name="b530737829"></a>protocol</strong> is set to <strong id="b1916899219"><a name="b1916899219"></a><a name="b1916899219"></a>TCP</strong> and <strong id="b729969729"><a name="b729969729"></a><a name="b729969729"></a>tcp_draining</strong> to <strong id="b479838316"><a name="b479838316"></a><a name="b479838316"></a>true</strong>.</p>
    </li><li>The value ranges from <strong id="b1111644918562"><a name="b1111644918562"></a><a name="b1111644918562"></a>0</strong> to <strong id="b823415155620"><a name="b823415155620"></a><a name="b823415155620"></a>60</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row610194889517"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p385455149523"><a name="en-us_topic_0020100160_p385455149523"></a><a name="en-us_topic_0020100160_p385455149523"></a>certificate_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p351789589523"><a name="en-us_topic_0020100160_p351789589523"></a><a name="en-us_topic_0020100160_p351789589523"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100160_p120311499538"><a name="en-us_topic_0020100160_p120311499538"></a><a name="en-us_topic_0020100160_p120311499538"></a>Specifies the ID of the SSL certificate for security authentication.</p>
    <p id="en-us_topic_0020100160_p309233509523"><a name="en-us_topic_0020100160_p309233509523"></a><a name="en-us_topic_0020100160_p309233509523"></a>This parameter is mandatory when <strong id="b8423527061428"><a name="b8423527061428"></a><a name="b8423527061428"></a>protocol</strong> is set to <strong id="b84235270614212"><a name="b84235270614212"></a><a name="b84235270614212"></a>HTTPS</strong> or <strong id="b842352706182053"><a name="b842352706182053"></a><a name="b842352706182053"></a>SSL</strong>. Otherwise, the parameter value is <strong id="b4428435195955"><a name="b4428435195955"></a><a name="b4428435195955"></a>null</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row2718176119844"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100160_p1268269419846"><a name="en-us_topic_0020100160_p1268269419846"></a><a name="en-us_topic_0020100160_p1268269419846"></a>certificates</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100160_p2066530719846"><a name="en-us_topic_0020100160_p2066530719846"></a><a name="en-us_topic_0020100160_p2066530719846"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100160_p6327715619846"><a name="en-us_topic_0020100160_p6327715619846"></a><a name="en-us_topic_0020100160_p6327715619846"></a>Lists the certificate IDs if <strong id="b1498106891"><a name="b1498106891"></a><a name="b1498106891"></a>protocol</strong> is set to <strong id="b1423380154"><a name="b1423380154"></a><a name="b1423380154"></a>HTTPS</strong>.</p>
    <p id="en-us_topic_0020100160_p3262349619846"><a name="en-us_topic_0020100160_p3262349619846"></a><a name="en-us_topic_0020100160_p3262349619846"></a>This parameter is mandatory in the SNI scenario.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "update_time": "2016-12-01 07:12:59",
        "backend_port": 9090,
        "id": "a824584fb3ba4d39ba0cf372c7cbbb67",
        "backend_protocol": "TCP",
        "sticky_session_type": null,
        "certificate_id": null,
        "description": "",
        "loadbalancer_id": "f54c65b1b5dd4a4f95b71b44796ac013",
        "create_time": "2016-12-01 07:12:43",
        "admin_state_up": false,
        "status": "ACTIVE",
        "protocol": "TCP",
        "cookie_timeout": 100,
        "port": 9092,
        "tcp_draining": true,
        "tcp_timeout": 1,
        "lb_algorithm": "roundrobin",
        "healthcheck_id": null,
        "session_sticky": true,
        "tcp_draining_timeout": 5,
        "name": "lis"
    
    }
    ```


## Status Code<a name="en-us_topic_0020100160_section33639718"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0020100160_table17356615150"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100160_row4835797915150"><th class="cellrowborder" valign="top" width="12.26%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020100160_p2468225215150"><a name="en-us_topic_0020100160_p2468225215150"></a><a name="en-us_topic_0020100160_p2468225215150"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.5%" id="mcps1.1.4.1.2"><p id="p1519862818447"><a name="p1519862818447"></a><a name="p1519862818447"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020100160_p5310543415150"><a name="en-us_topic_0020100160_p5310543415150"></a><a name="en-us_topic_0020100160_p5310543415150"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100160_row657290815150"><td class="cellrowborder" valign="top" width="12.26%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100160_p6264356315150"><a name="en-us_topic_0020100160_p6264356315150"></a><a name="en-us_topic_0020100160_p6264356315150"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.5%" headers="mcps1.1.4.1.2 "><p id="p1846124334418"><a name="p1846124334418"></a><a name="p1846124334418"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100160_p4096383815150"><a name="en-us_topic_0020100160_p4096383815150"></a><a name="en-us_topic_0020100160_p4096383815150"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row3313022715150"><td class="cellrowborder" valign="top" width="12.26%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100160_p6630272015150"><a name="en-us_topic_0020100160_p6630272015150"></a><a name="en-us_topic_0020100160_p6630272015150"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.5%" headers="mcps1.1.4.1.2 "><p id="p1446943144413"><a name="p1446943144413"></a><a name="p1446943144413"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100160_p181122115150"><a name="en-us_topic_0020100160_p181122115150"></a><a name="en-us_topic_0020100160_p181122115150"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row1630099515150"><td class="cellrowborder" valign="top" width="12.26%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100160_p4531218415150"><a name="en-us_topic_0020100160_p4531218415150"></a><a name="en-us_topic_0020100160_p4531218415150"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.5%" headers="mcps1.1.4.1.2 "><p id="p4461343194414"><a name="p4461343194414"></a><a name="p4461343194414"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100160_p4640826515150"><a name="en-us_topic_0020100160_p4640826515150"></a><a name="en-us_topic_0020100160_p4640826515150"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row1502120815150"><td class="cellrowborder" valign="top" width="12.26%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100160_p875836815150"><a name="en-us_topic_0020100160_p875836815150"></a><a name="en-us_topic_0020100160_p875836815150"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.5%" headers="mcps1.1.4.1.2 "><p id="p646943104411"><a name="p646943104411"></a><a name="p646943104411"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100160_p3833919215150"><a name="en-us_topic_0020100160_p3833919215150"></a><a name="en-us_topic_0020100160_p3833919215150"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row950840915150"><td class="cellrowborder" valign="top" width="12.26%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100160_p3198369315150"><a name="en-us_topic_0020100160_p3198369315150"></a><a name="en-us_topic_0020100160_p3198369315150"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.5%" headers="mcps1.1.4.1.2 "><p id="p13469438449"><a name="p13469438449"></a><a name="p13469438449"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100160_p4054234115150"><a name="en-us_topic_0020100160_p4054234115150"></a><a name="en-us_topic_0020100160_p4054234115150"></a>System error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100160_row2933675415150"><td class="cellrowborder" valign="top" width="12.26%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100160_p2746690815150"><a name="en-us_topic_0020100160_p2746690815150"></a><a name="en-us_topic_0020100160_p2746690815150"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.5%" headers="mcps1.1.4.1.2 "><p id="p10461643154412"><a name="p10461643154412"></a><a name="p10461643154412"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100160_p1022710315150"><a name="en-us_topic_0020100160_p1022710315150"></a><a name="en-us_topic_0020100160_p1022710315150"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


