# Overview<a name="EN-US_TOPIC_0125375301"></a>

## Scenario<a name="s6f2e081b32fb4d839c7ed36dfeba43da"></a>

Websites of different components are created and hosted on the Master or Core nodes in the MRS cluster by default. You can view information about the components on these websites. The websites can be accessed only through the network of the cluster and are not released on the Internet for security reasons. Common users can access the websites by creating an ECS with a graphical user interface \(GUI\) in the network.

If you do not want to create an extra ECS, you can turn to technical experts or development engineers. They can use the dynamic port forwarding function of the SSH channel to allow you to access the websites.

## Websites<a name="s13534867d95748fdbf7322acf0bb34ca"></a>

**Table  1**  Clusters with Kerberos authentication disabled

<a name="en-us_topic_0069869151_table15477438145833"></a>
<table><thead align="left"><tr id="en-us_topic_0069869151_row51642521145833"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="en-us_topic_0069869151_p66434050145833"><a name="en-us_topic_0069869151_p66434050145833"></a><a name="en-us_topic_0069869151_p66434050145833"></a>Cluster Type</p>
</th>
<th class="cellrowborder" valign="top" width="31.990000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0069869151_p12448942145833"><a name="en-us_topic_0069869151_p12448942145833"></a><a name="en-us_topic_0069869151_p12448942145833"></a>Website Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.010000000000005%" id="mcps1.2.4.1.3"><p id="en-us_topic_0069869151_p1731407145833"><a name="en-us_topic_0069869151_p1731407145833"></a><a name="en-us_topic_0069869151_p1731407145833"></a>Website</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0069869151_row15582671145833"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0069869151_p54236858145833"><a name="en-us_topic_0069869151_p54236858145833"></a><a name="en-us_topic_0069869151_p54236858145833"></a>All Types</p>
</td>
<td class="cellrowborder" valign="top" width="31.990000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0069869151_p31109390145833"><a name="en-us_topic_0069869151_p31109390145833"></a><a name="en-us_topic_0069869151_p31109390145833"></a>MRS Manager</p>
</td>
<td class="cellrowborder" valign="top" width="48.010000000000005%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0069869151_ul54001052154512"></a><a name="en-us_topic_0069869151_ul54001052154512"></a><ul id="en-us_topic_0069869151_ul54001052154512"><li>Applicable&nbsp;to&nbsp;versions&nbsp;earlier&nbsp;than&nbsp;MRS&nbsp;1.9.2<p id="en-us_topic_0069869151_p65275716172746"><a name="en-us_topic_0069869151_p65275716172746"></a><a name="en-us_topic_0069869151_p65275716172746"></a>https://Floating IP address of MRS Manager:28443/web</p>
<div class="note" id="en-us_topic_0069869151_note61259334174512"><a name="en-us_topic_0069869151_note61259334174512"></a><a name="en-us_topic_0069869151_note61259334174512"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0069869151_p14463101174512"><a name="en-us_topic_0069869151_p14463101174512"></a><a name="en-us_topic_0069869151_p14463101174512"></a>Remotely log in to the Master2 node and run the <strong id="en-us_topic_0069869151_b13614173820313"><a name="en-us_topic_0069869151_b13614173820313"></a><a name="en-us_topic_0069869151_b13614173820313"></a>ifconfig</strong> command. In the command output, <strong id="en-us_topic_0069869151_b186141238830"><a name="en-us_topic_0069869151_b186141238830"></a><a name="en-us_topic_0069869151_b186141238830"></a>eth0:wsom</strong> refers to the floating IP address of MRS Manager. Record the actual value of <strong id="en-us_topic_0069869151_b116141538139"><a name="en-us_topic_0069869151_b116141538139"></a><a name="en-us_topic_0069869151_b116141538139"></a>inet</strong>. If you cannot query the floating IP address of MRS Manager on the Master2 node, switch to the Master1 node to query the floating IP address and then record it. If there is only one Master node, log in to this Master node to query the floating IP address and then record it.</p>
</div></div>
</li><li>Applicable&nbsp;to&nbsp;MRS&nbsp;1.9.2&nbsp;or&nbsp;later<p id="en-us_topic_0069869151_p5463837104617"><a name="en-us_topic_0069869151_p5463837104617"></a><a name="en-us_topic_0069869151_p5463837104617"></a>https://&lt;EIP&gt;:9022/mrsmanager?locale=en-us</p>
</li></ul>
</td>
</tr>
<tr id="en-us_topic_0069869151_row63058177145833"><td class="cellrowborder" rowspan="8" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0069869151_p7438721145833"><a name="en-us_topic_0069869151_p7438721145833"></a><a name="en-us_topic_0069869151_p7438721145833"></a>Analysis cluster</p>
<p id="en-us_topic_0069869151_p7659172718392"><a name="en-us_topic_0069869151_p7659172718392"></a><a name="en-us_topic_0069869151_p7659172718392"></a></p>
<p id="en-us_topic_0069869151_p148813171343"><a name="en-us_topic_0069869151_p148813171343"></a><a name="en-us_topic_0069869151_p148813171343"></a></p>
</td>
<td class="cellrowborder" valign="top" width="31.990000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0069869151_p65665509145833"><a name="en-us_topic_0069869151_p65665509145833"></a><a name="en-us_topic_0069869151_p65665509145833"></a>HDFS NameNode</p>
</td>
<td class="cellrowborder" valign="top" width="48.010000000000005%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0069869151_ul129175913114"></a><a name="en-us_topic_0069869151_ul129175913114"></a><ul id="en-us_topic_0069869151_ul129175913114"><li>Applicable to MRS 1.6.3 or earlier<p id="en-us_topic_0069869151_p3463201611415"><a name="en-us_topic_0069869151_p3463201611415"></a><a name="en-us_topic_0069869151_p3463201611415"></a>http://<em id="en-us_topic_0069869151_i1037514178419"><a name="en-us_topic_0069869151_i1037514178419"></a><a name="en-us_topic_0069869151_i1037514178419"></a>IP address of the active NameNode roleinstance</em>:25002/dfshealth.html#tab-overview</p>
</li></ul>
<a name="en-us_topic_0069869151_ul187211925132916"></a><a name="en-us_topic_0069869151_ul187211925132916"></a><ul id="en-us_topic_0069869151_ul187211925132916"><li>Applicable&nbsp;to&nbsp;MRS&nbsp;1.7.2<p id="en-us_topic_0069869151_p124233469418"><a name="en-us_topic_0069869151_p124233469418"></a><a name="en-us_topic_0069869151_p124233469418"></a>http://<em id="en-us_topic_0069869151_i1540934713411"><a name="en-us_topic_0069869151_i1540934713411"></a><a name="en-us_topic_0069869151_i1540934713411"></a>IP address of the active NameNode roleinstance</em>:9870/dfshealth.html#tab-overview</p>
</li></ul>
<a name="en-us_topic_0069869151_ul136071302616"></a><a name="en-us_topic_0069869151_ul136071302616"></a><ul id="en-us_topic_0069869151_ul136071302616"><li>Applicable&nbsp;to&nbsp;MRS&nbsp;1.9.2 or later<p id="en-us_topic_0069869151_p13726585494"><a name="en-us_topic_0069869151_p13726585494"></a><a name="en-us_topic_0069869151_p13726585494"></a>Choose <span class="menucascade" id="en-us_topic_0069869151_menucascade173791882259"><a name="en-us_topic_0069869151_menucascade173791882259"></a><a name="en-us_topic_0069869151_menucascade173791882259"></a><b><span class="uicontrol" id="en-us_topic_0069869151_uicontrol1038015811255"><a name="en-us_topic_0069869151_uicontrol1038015811255"></a><a name="en-us_topic_0069869151_uicontrol1038015811255"></a>Services&nbsp;&gt; HDFS &gt; NameNode Web UI &gt; NameNode (Active)</span></b></span></p>
</li></ul>
</td>
</tr>
<tr id="en-us_topic_0069869151_row4021035315137"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0069869151_p1518535215137"><a name="en-us_topic_0069869151_p1518535215137"></a><a name="en-us_topic_0069869151_p1518535215137"></a>HBase HMaster</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0069869151_ul5506250120"></a><a name="en-us_topic_0069869151_ul5506250120"></a><ul id="en-us_topic_0069869151_ul5506250120"><li>Applicable to MRS 1.6.3 or earlier<p id="en-us_topic_0069869151_p1018971120520"><a name="en-us_topic_0069869151_p1018971120520"></a><a name="en-us_topic_0069869151_p1018971120520"></a>https://<em id="i55391135155217"><a name="i55391135155217"></a><a name="i55391135155217"></a>IP address of the active</em> <em id="en-us_topic_0069869151_i469714111052"><a name="en-us_topic_0069869151_i469714111052"></a><a name="en-us_topic_0069869151_i469714111052"></a>HMaster role instance</em>:21301/master-status</p>
</li></ul>
<a name="en-us_topic_0069869151_ul10483185511615"></a><a name="en-us_topic_0069869151_ul10483185511615"></a><ul id="en-us_topic_0069869151_ul10483185511615"><li>Applicable&nbsp;to&nbsp;MRS&nbsp;1.7.2<p id="en-us_topic_0069869151_p175702514520"><a name="en-us_topic_0069869151_p175702514520"></a><a name="en-us_topic_0069869151_p175702514520"></a>https://<em id="i183821645205219"><a name="i183821645205219"></a><a name="i183821645205219"></a>IP address of the active</em> <em id="en-us_topic_0069869151_i592562513519"><a name="en-us_topic_0069869151_i592562513519"></a><a name="en-us_topic_0069869151_i592562513519"></a>HMaster role instance</em>:16010/master-status</p>
</li><li>Applicable&nbsp;to&nbsp;MRS&nbsp;1.9.2 or later<p id="en-us_topic_0069869151_p32564285251"><a name="en-us_topic_0069869151_p32564285251"></a><a name="en-us_topic_0069869151_p32564285251"></a>Choose <span class="menucascade" id="en-us_topic_0069869151_menucascade1075372216257"><a name="en-us_topic_0069869151_menucascade1075372216257"></a><a name="en-us_topic_0069869151_menucascade1075372216257"></a><b><span class="uicontrol" id="en-us_topic_0069869151_uicontrol2753102212255"><a name="en-us_topic_0069869151_uicontrol2753102212255"></a><a name="en-us_topic_0069869151_uicontrol2753102212255"></a>Services&nbsp;&gt; HBase &gt; HMaster Web UI &gt; HMaster (Active)</span></b></span></p>
</li></ul>
</td>
</tr>
<tr id="en-us_topic_0069869151_row218196015137"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0069869151_p2165523115137"><a name="en-us_topic_0069869151_p2165523115137"></a><a name="en-us_topic_0069869151_p2165523115137"></a>MapReduce JobHistoryServer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0069869151_ul92611191215"></a><a name="en-us_topic_0069869151_ul92611191215"></a><ul id="en-us_topic_0069869151_ul92611191215"><li>Applicable to MRS 1.6.3 or earlier<p id="en-us_topic_0069869151_p141411461854"><a name="en-us_topic_0069869151_p141411461854"></a><a name="en-us_topic_0069869151_p141411461854"></a>http://<em id="en-us_topic_0069869151_i26524711518"><a name="en-us_topic_0069869151_i26524711518"></a><a name="en-us_topic_0069869151_i26524711518"></a>IP address of the JobHistoryServer roleinstance</em>:26012/jobhistory</p>
</li></ul>
<a name="en-us_topic_0069869151_ul278717418717"></a><a name="en-us_topic_0069869151_ul278717418717"></a><ul id="en-us_topic_0069869151_ul278717418717"><li>Applicable&nbsp;to MRS&nbsp;1.7.2<p id="en-us_topic_0069869151_p960451717611"><a name="en-us_topic_0069869151_p960451717611"></a><a name="en-us_topic_0069869151_p960451717611"></a>http://<em id="en-us_topic_0069869151_i1453315181467"><a name="en-us_topic_0069869151_i1453315181467"></a><a name="en-us_topic_0069869151_i1453315181467"></a>IP address of the JobHistoryServer roleinstance</em>:19888/jobhistory</p>
</li><li>Applicable&nbsp;to&nbsp;MRS&nbsp;1.9.2 or later<p id="en-us_topic_0069869151_p1863004112253"><a name="en-us_topic_0069869151_p1863004112253"></a><a name="en-us_topic_0069869151_p1863004112253"></a>Choose <span class="menucascade" id="en-us_topic_0069869151_menucascade196311741122515"><a name="en-us_topic_0069869151_menucascade196311741122515"></a><a name="en-us_topic_0069869151_menucascade196311741122515"></a><b><span class="uicontrol" id="en-us_topic_0069869151_uicontrol1632184113252"><a name="en-us_topic_0069869151_uicontrol1632184113252"></a><a name="en-us_topic_0069869151_uicontrol1632184113252"></a>Services&nbsp;&gt; MapReduce &gt; JobHistoryServer Web UI &gt; JobHistoryServer</span></b></span></p>
</li></ul>
</td>
</tr>
<tr id="en-us_topic_0069869151_row1563977415137"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0069869151_p310642615137"><a name="en-us_topic_0069869151_p310642615137"></a><a name="en-us_topic_0069869151_p310642615137"></a>YARN ResourceManager</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0069869151_ul5844191714129"></a><a name="en-us_topic_0069869151_ul5844191714129"></a><ul id="en-us_topic_0069869151_ul5844191714129"><li>Applicable to MRS 1.6.3 or earlier<p id="en-us_topic_0069869151_p3195124818617"><a name="en-us_topic_0069869151_p3195124818617"></a><a name="en-us_topic_0069869151_p3195124818617"></a>http://<em id="en-us_topic_0069869151_i122111491166"><a name="en-us_topic_0069869151_i122111491166"></a><a name="en-us_topic_0069869151_i122111491166"></a>IP address of the active ResourceManagerrole instance</em>:26000/cluster</p>
</li></ul>
<a name="en-us_topic_0069869151_ul1691913319818"></a><a name="en-us_topic_0069869151_ul1691913319818"></a><ul id="en-us_topic_0069869151_ul1691913319818"><li>Applicable&nbsp;to&nbsp;MRS&nbsp;1.7.2<p id="en-us_topic_0069869151_p66016269183"><a name="en-us_topic_0069869151_p66016269183"></a><a name="en-us_topic_0069869151_p66016269183"></a>http://<em id="en-us_topic_0069869151_i62719593612"><a name="en-us_topic_0069869151_i62719593612"></a><a name="en-us_topic_0069869151_i62719593612"></a>IP address of the active ResourceManagerrole instance</em>:8088/cluster</p>
</li><li>Applicable&nbsp;to&nbsp;MRS&nbsp;1.9.2 or later<p id="en-us_topic_0069869151_p1523982162611"><a name="en-us_topic_0069869151_p1523982162611"></a><a name="en-us_topic_0069869151_p1523982162611"></a>Choose <span class="menucascade" id="en-us_topic_0069869151_menucascade12240142142612"><a name="en-us_topic_0069869151_menucascade12240142142612"></a><a name="en-us_topic_0069869151_menucascade12240142142612"></a><b><span class="uicontrol" id="en-us_topic_0069869151_uicontrol7241926264"><a name="en-us_topic_0069869151_uicontrol7241926264"></a><a name="en-us_topic_0069869151_uicontrol7241926264"></a>Services&nbsp;&gt; Yarn &gt; ResourceManager Web UI &gt; ResourceManager (Active)</span></b></span></p>
</li></ul>
</td>
</tr>
<tr id="en-us_topic_0069869151_row2724320415137"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0069869151_p3175929015137"><a name="en-us_topic_0069869151_p3175929015137"></a><a name="en-us_topic_0069869151_p3175929015137"></a>Spark JobHistory</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0069869151_ul66509078232947"></a><a name="en-us_topic_0069869151_ul66509078232947"></a><ul id="en-us_topic_0069869151_ul66509078232947"><li>Applicable to MRS 1.6.3 or earlier<p id="en-us_topic_0069869151_p6547420716718"><a name="en-us_topic_0069869151_p6547420716718"></a><a name="en-us_topic_0069869151_p6547420716718"></a>http://<em id="i122401752195213"><a name="i122401752195213"></a><a name="i122401752195213"></a>IP address of the</em> <em id="en-us_topic_0069869151_i204641889710"><a name="en-us_topic_0069869151_i204641889710"></a><a name="en-us_topic_0069869151_i204641889710"></a>JobHistory role instance</em>:22500/</p>
</li><li>Applicable&nbsp;to&nbsp;MRS&nbsp;1.7.2<p id="en-us_topic_0069869151_p10653155831016"><a name="en-us_topic_0069869151_p10653155831016"></a><a name="en-us_topic_0069869151_p10653155831016"></a>http://<em id="i6978359145212"><a name="i6978359145212"></a><a name="i6978359145212"></a>IP address of the</em> <em id="en-us_topic_0069869151_i22847151071"><a name="en-us_topic_0069869151_i22847151071"></a><a name="en-us_topic_0069869151_i22847151071"></a>JobHistory role instance</em>:18080/</p>
</li><li>Applicable&nbsp;to&nbsp;MRS&nbsp;1.9.2 or later<p id="en-us_topic_0069869151_p17660161817268"><a name="en-us_topic_0069869151_p17660161817268"></a><a name="en-us_topic_0069869151_p17660161817268"></a>Choose <span class="menucascade" id="en-us_topic_0069869151_menucascade766112188268"><a name="en-us_topic_0069869151_menucascade766112188268"></a><a name="en-us_topic_0069869151_menucascade766112188268"></a><b><span class="uicontrol" id="en-us_topic_0069869151_uicontrol46631418182618"><a name="en-us_topic_0069869151_uicontrol46631418182618"></a><a name="en-us_topic_0069869151_uicontrol46631418182618"></a>Services</span></b> &gt; <b><span class="uicontrol" id="en-us_topic_0069869151_uicontrol1166414181268"><a name="en-us_topic_0069869151_uicontrol1166414181268"></a><a name="en-us_topic_0069869151_uicontrol1166414181268"></a>Spark &gt; Spark Web UI</span></b> &gt; <b><span class="uicontrol" id="en-us_topic_0069869151_uicontrol116652184269"><a name="en-us_topic_0069869151_uicontrol116652184269"></a><a name="en-us_topic_0069869151_uicontrol116652184269"></a>JobHistory</span></b></span>.</p>
</li></ul>
</td>
</tr>
<tr id="en-us_topic_0069869151_row2356032515137"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0069869151_p2758346615137"><a name="en-us_topic_0069869151_p2758346615137"></a><a name="en-us_topic_0069869151_p2758346615137"></a>Hue</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0069869151_ul7737102661710"></a><a name="en-us_topic_0069869151_ul7737102661710"></a><ul id="en-us_topic_0069869151_ul7737102661710"><li>Applicable to MRS 1.6.3 or earlier<p id="en-us_topic_0069869151_p167901358178"><a name="en-us_topic_0069869151_p167901358178"></a><a name="en-us_topic_0069869151_p167901358178"></a>https://<em id="en-us_topic_0069869151_i616614371714"><a name="en-us_topic_0069869151_i616614371714"></a><a name="en-us_topic_0069869151_i616614371714"></a>Floating IP address of Hue</em>:21200</p>
</li></ul>
<a name="en-us_topic_0069869151_ul1823534721714"></a><a name="en-us_topic_0069869151_ul1823534721714"></a><ul id="en-us_topic_0069869151_ul1823534721714"><li>Applicable&nbsp;to&nbsp;MRS&nbsp;1.7.2<p id="en-us_topic_0069869151_p140483513132"><a name="en-us_topic_0069869151_p140483513132"></a><a name="en-us_topic_0069869151_p140483513132"></a>https://<em id="en-us_topic_0069869151_i201631417717"><a name="en-us_topic_0069869151_i201631417717"></a><a name="en-us_topic_0069869151_i201631417717"></a>Floating IP address of Hue</em>:8888</p>
</li><li>Applicable&nbsp;to&nbsp;MRS&nbsp;1.9.2 or later<p id="en-us_topic_0069869151_p1862119316267"><a name="en-us_topic_0069869151_p1862119316267"></a><a name="en-us_topic_0069869151_p1862119316267"></a>Choose <span class="menucascade" id="en-us_topic_0069869151_menucascade6623183122620"><a name="en-us_topic_0069869151_menucascade6623183122620"></a><a name="en-us_topic_0069869151_menucascade6623183122620"></a><b><span class="uicontrol" id="en-us_topic_0069869151_uicontrol96247311261"><a name="en-us_topic_0069869151_uicontrol96247311261"></a><a name="en-us_topic_0069869151_uicontrol96247311261"></a>Services&nbsp;&gt; Hue &gt; Hue Web UI &gt; Hue (Active)</span></b></span></p>
</li></ul>
<p id="en-us_topic_0069869151_p4080600911365"><a name="en-us_topic_0069869151_p4080600911365"></a><a name="en-us_topic_0069869151_p4080600911365"></a>The Loader page is a graphical data migration management tool based on the open source Sqoop web UI and is hosted on the Hue web UI.</p>
<div class="note" id="en-us_topic_0069869151_note12531395145934"><a name="en-us_topic_0069869151_note12531395145934"></a><a name="en-us_topic_0069869151_note12531395145934"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0069869151_p31491048271"><a name="en-us_topic_0069869151_p31491048271"></a><a name="en-us_topic_0069869151_p31491048271"></a>Remotely log in to the Master2 node and run the <strong id="en-us_topic_0069869151_b1187249278"><a name="en-us_topic_0069869151_b1187249278"></a><a name="en-us_topic_0069869151_b1187249278"></a>ifconfig</strong> command. In the command output, <strong id="en-us_topic_0069869151_b181879499719"><a name="en-us_topic_0069869151_b181879499719"></a><a name="en-us_topic_0069869151_b181879499719"></a>eth0:FI_HUE</strong> refers to the floating IP address of Hue. Record the actual value of <strong id="en-us_topic_0069869151_b81872049777"><a name="en-us_topic_0069869151_b81872049777"></a><a name="en-us_topic_0069869151_b81872049777"></a>inet</strong>. If you cannot query the floating IP address of Hue on the Master2 node, switch to the Master1 node to query the floating IP address and then record it. If there is only one Master node, log in to this Master node to query the floating IP address and then record it.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0069869151_row13296203933914"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0069869151_p189213344315"><a name="en-us_topic_0069869151_p189213344315"></a><a name="en-us_topic_0069869151_p189213344315"></a>Tez</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0069869151_p16731151143218"><a name="en-us_topic_0069869151_p16731151143218"></a><a name="en-us_topic_0069869151_p16731151143218"></a>Applicable&nbsp;to&nbsp;MRS&nbsp;2.1.0&nbsp;or&nbsp;later (MRS 2.1.0 or later supports Tez.)</p>
<p id="en-us_topic_0069869151_p1779173017417"><a name="en-us_topic_0069869151_p1779173017417"></a><a name="en-us_topic_0069869151_p1779173017417"></a>Choose <span class="menucascade" id="en-us_topic_0069869151_menucascade147927301941"><a name="en-us_topic_0069869151_menucascade147927301941"></a><a name="en-us_topic_0069869151_menucascade147927301941"></a><b><span class="uicontrol" id="en-us_topic_0069869151_uicontrol47925301545"><a name="en-us_topic_0069869151_uicontrol47925301545"></a><a name="en-us_topic_0069869151_uicontrol47925301545"></a>Services&nbsp;&gt; Tez &gt; Tez Web UI &gt; TezUI</span></b></span></p>
</td>
</tr>
<tr id="en-us_topic_0069869151_row38713177414"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0069869151_p18381822165211"><a name="en-us_topic_0069869151_p18381822165211"></a><a name="en-us_topic_0069869151_p18381822165211"></a>Presto</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p534402412110"><a name="p534402412110"></a><a name="p534402412110"></a>Applicable&nbsp;to&nbsp;MRS 1.9.2  or later</p>
<p id="en-us_topic_0069869151_p4889151348"><a name="en-us_topic_0069869151_p4889151348"></a><a name="en-us_topic_0069869151_p4889151348"></a>Choose <span class="menucascade" id="en-us_topic_0069869151_menucascade149348523812"><a name="en-us_topic_0069869151_menucascade149348523812"></a><a name="en-us_topic_0069869151_menucascade149348523812"></a><b><span class="uicontrol" id="en-us_topic_0069869151_uicontrol09346528814"><a name="en-us_topic_0069869151_uicontrol09346528814"></a><a name="en-us_topic_0069869151_uicontrol09346528814"></a>Services&nbsp;&gt; Presto &gt; Presto Web UI &gt; Coordinator (Active)</span></b></span></p>
</td>
</tr>
<tr id="en-us_topic_0069869151_row2475311015137"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0069869151_p5884492515137"><a name="en-us_topic_0069869151_p5884492515137"></a><a name="en-us_topic_0069869151_p5884492515137"></a>Stream processing cluster</p>
<p id="en-us_topic_0069869151_p13801435748"><a name="en-us_topic_0069869151_p13801435748"></a><a name="en-us_topic_0069869151_p13801435748"></a></p>
</td>
<td class="cellrowborder" valign="top" width="31.990000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0069869151_p170958315137"><a name="en-us_topic_0069869151_p170958315137"></a><a name="en-us_topic_0069869151_p170958315137"></a>Storm</p>
</td>
<td class="cellrowborder" valign="top" width="48.010000000000005%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0069869151_ul8680055172211"></a><a name="en-us_topic_0069869151_ul8680055172211"></a><ul id="en-us_topic_0069869151_ul8680055172211"><li>Applicable&nbsp;to&nbsp;versions&nbsp;earlier&nbsp;than&nbsp;MRS&nbsp;1.9.2<p id="en-us_topic_0069869151_p425855015137"><a name="en-us_topic_0069869151_p425855015137"></a><a name="en-us_topic_0069869151_p425855015137"></a>http://IP address of any UI role instance:29280/index.html</p>
</li></ul>
<a name="en-us_topic_0069869151_ul1782916536222"></a><a name="en-us_topic_0069869151_ul1782916536222"></a><ul id="en-us_topic_0069869151_ul1782916536222"><li>Applicable&nbsp;to&nbsp;MRS&nbsp;1.9.2 or later<p id="p123612029112712"><a name="p123612029112712"></a><a name="p123612029112712"></a>Choose <span class="menucascade" id="menucascade23615294277"><a name="menucascade23615294277"></a><a name="menucascade23615294277"></a><b><span class="uicontrol" id="uicontrol536192914273"><a name="uicontrol536192914273"></a><a name="uicontrol536192914273"></a>Services&nbsp;&gt; Storm &gt; Web UI &gt; UI</span></b></span></p>
</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  2**  Clusters with Kerberos authentication enabled

<a name="t8c43ca9bbc5e4592892dd840c35d080a"></a>
<table><thead align="left"><tr id="rd03950d2735a4b43a9d86927a2d06fc8"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="a8cce8378b1c346338dd24e76f82ff473"><a name="a8cce8378b1c346338dd24e76f82ff473"></a><a name="a8cce8378b1c346338dd24e76f82ff473"></a>Cluster Type</p>
</th>
<th class="cellrowborder" valign="top" width="31.990000000000002%" id="mcps1.2.4.1.2"><p id="a8491c61eaecd4da58c9a8bc75c0bb1df"><a name="a8491c61eaecd4da58c9a8bc75c0bb1df"></a><a name="a8491c61eaecd4da58c9a8bc75c0bb1df"></a>Website Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.010000000000005%" id="mcps1.2.4.1.3"><p id="a6bcf2409822f44058567542f8159f969"><a name="a6bcf2409822f44058567542f8159f969"></a><a name="a6bcf2409822f44058567542f8159f969"></a>Website</p>
</th>
</tr>
</thead>
<tbody><tr id="r7c67e16e6b9748958e258fe40ef6670e"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="a1a86c9e51e804328890b56e63b4b520c"><a name="a1a86c9e51e804328890b56e63b4b520c"></a><a name="a1a86c9e51e804328890b56e63b4b520c"></a>All Types</p>
</td>
<td class="cellrowborder" valign="top" width="31.990000000000002%" headers="mcps1.2.4.1.2 "><p id="add3bdf70647c46fb8f589daa27805b39"><a name="add3bdf70647c46fb8f589daa27805b39"></a><a name="add3bdf70647c46fb8f589daa27805b39"></a>MRS Manager</p>
</td>
<td class="cellrowborder" valign="top" width="48.010000000000005%" headers="mcps1.2.4.1.3 "><a name="ul72014441599"></a><a name="ul72014441599"></a><ul id="ul72014441599"><li>Applicable&nbsp;to&nbsp;versions&nbsp;earlier&nbsp;than&nbsp;MRS&nbsp;1.9.2<p id="p1620184495919"><a name="p1620184495919"></a><a name="p1620184495919"></a>https://Floating IP address of MRS Manager:28443/web</p>
<div class="note" id="note92011447595"><a name="note92011447595"></a><a name="note92011447595"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p172184465910"><a name="p172184465910"></a><a name="p172184465910"></a>Remotely log in to the Master2 node and run the <strong id="b1021544165911"><a name="b1021544165911"></a><a name="b1021544165911"></a>ifconfig</strong> command. In the command output, <strong id="b921134425917"><a name="b921134425917"></a><a name="b921134425917"></a>eth0:wsom</strong> refers to the floating IP address of MRS Manager. Record the actual value of <strong id="b1721104418598"><a name="b1721104418598"></a><a name="b1721104418598"></a>inet</strong>. If you cannot query the floating IP address of MRS Manager on the Master2 node, switch to the Master1 node to query the floating IP address and then record it. If there is only one Master node, log in to this Master node to query the floating IP address and then record it.</p>
</div></div>
</li><li>Applicable&nbsp;to&nbsp;MRS&nbsp;1.9.2&nbsp;or&nbsp;later<p id="p92119448598"><a name="p92119448598"></a><a name="p92119448598"></a>https://&lt;EIP&gt;:9022/mrsmanager?locale=en-us</p>
</li></ul>
</td>
</tr>
<tr id="rfd77d85c2e66427bb8585c4d02aaa08d"><td class="cellrowborder" rowspan="8" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="a82be20cec91547069ae57cc5104115c0"><a name="a82be20cec91547069ae57cc5104115c0"></a><a name="a82be20cec91547069ae57cc5104115c0"></a>Analysis cluster</p>
<p id="p1254710399018"><a name="p1254710399018"></a><a name="p1254710399018"></a></p>
<p id="p101934401109"><a name="p101934401109"></a><a name="p101934401109"></a></p>
</td>
<td class="cellrowborder" valign="top" width="31.990000000000002%" headers="mcps1.2.4.1.2 "><p id="a025561b7381140cea470fe2f0a860b9b"><a name="a025561b7381140cea470fe2f0a860b9b"></a><a name="a025561b7381140cea470fe2f0a860b9b"></a>HDFS NameNode</p>
</td>
<td class="cellrowborder" valign="top" width="48.010000000000005%" headers="mcps1.2.4.1.3 "><p id="a83380cd16b024bc4bdaf630144e2d3dc"><a name="a83380cd16b024bc4bdaf630144e2d3dc"></a><a name="a83380cd16b024bc4bdaf630144e2d3dc"></a>Choose <span class="menucascade" id="m31884c8710f54b289055f113ddc3a943"><a name="m31884c8710f54b289055f113ddc3a943"></a><a name="m31884c8710f54b289055f113ddc3a943"></a><b><span class="uicontrol" id="u22f73282cdc24d7689426e480ecb9cfb"><a name="u22f73282cdc24d7689426e480ecb9cfb"></a><a name="u22f73282cdc24d7689426e480ecb9cfb"></a>Service &gt; HDFS &gt; NameNode WebUI &gt; NameNode (Active)</span></b></span></p>
</td>
</tr>
<tr id="r5a6b75e80a2e4f2db402cfcf73ff7572"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="ace27dbeffbac47ecb6bd1faebd8c55ac"><a name="ace27dbeffbac47ecb6bd1faebd8c55ac"></a><a name="ace27dbeffbac47ecb6bd1faebd8c55ac"></a>HBase HMaster</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="ab841dda03ce4453b97290b20d6f224ee"><a name="ab841dda03ce4453b97290b20d6f224ee"></a><a name="ab841dda03ce4453b97290b20d6f224ee"></a>Choose <span class="menucascade" id="m278f8d07499647e9b37ca7260d41a822"><a name="m278f8d07499647e9b37ca7260d41a822"></a><a name="m278f8d07499647e9b37ca7260d41a822"></a><b><span class="uicontrol" id="ub713d67ec0f14d05ae9d3ba7f10dcf36"><a name="ub713d67ec0f14d05ae9d3ba7f10dcf36"></a><a name="ub713d67ec0f14d05ae9d3ba7f10dcf36"></a>Service &gt; HBase &gt; HMaster WebUI &gt; HMaster (Active)</span></b></span></p>
</td>
</tr>
<tr id="r672f9be2e2024fee9548672f2812e4a3"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="a4f713f66253f49419482efb2c71b88c1"><a name="a4f713f66253f49419482efb2c71b88c1"></a><a name="a4f713f66253f49419482efb2c71b88c1"></a>MapReduce JobHistoryServer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="aa71840084d1b4f0bbe5774454052c0b6"><a name="aa71840084d1b4f0bbe5774454052c0b6"></a><a name="aa71840084d1b4f0bbe5774454052c0b6"></a>Choose <span class="menucascade" id="m4093c1959a514de49eb7315579109fb6"><a name="m4093c1959a514de49eb7315579109fb6"></a><a name="m4093c1959a514de49eb7315579109fb6"></a><b><span class="uicontrol" id="u1b6335239f494e698d618f3c2b1e9f5a"><a name="u1b6335239f494e698d618f3c2b1e9f5a"></a><a name="u1b6335239f494e698d618f3c2b1e9f5a"></a>Service &gt; MapReduce &gt; JobHistoryServer WebUI &gt; JobHistoryServer</span></b></span></p>
</td>
</tr>
<tr id="r519b789a89de40fb9f145737b50c5c4c"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="ab52379de19914e87af220a5bc1904195"><a name="ab52379de19914e87af220a5bc1904195"></a><a name="ab52379de19914e87af220a5bc1904195"></a>YARN ResourceManager</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="a11e25d861cd84972a1f7f700e288a3f4"><a name="a11e25d861cd84972a1f7f700e288a3f4"></a><a name="a11e25d861cd84972a1f7f700e288a3f4"></a>Choose <span class="menucascade" id="m0ae88dc119e64806a00963fa062b62fe"><a name="m0ae88dc119e64806a00963fa062b62fe"></a><a name="m0ae88dc119e64806a00963fa062b62fe"></a><b><span class="uicontrol" id="u35bc1842ed2f47b0a0fa10a95967ca8e"><a name="u35bc1842ed2f47b0a0fa10a95967ca8e"></a><a name="u35bc1842ed2f47b0a0fa10a95967ca8e"></a>Service &gt; Yarn &gt; ResourceManager WebUI &gt; ResourceManager (Active)</span></b></span></p>
</td>
</tr>
<tr id="rc382c67a03c848d7ab8fc669651fa989"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="a511a03921a59410d9e2be0904f84459b"><a name="a511a03921a59410d9e2be0904f84459b"></a><a name="a511a03921a59410d9e2be0904f84459b"></a>Spark JobHistory</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="ac8397611cc37440a81b5eef74bee6616"><a name="ac8397611cc37440a81b5eef74bee6616"></a><a name="ac8397611cc37440a81b5eef74bee6616"></a>Choose <span class="menucascade" id="m6b8634fe46e342f8ba1dd0258e62d065"><a name="m6b8634fe46e342f8ba1dd0258e62d065"></a><a name="m6b8634fe46e342f8ba1dd0258e62d065"></a><b><span class="uicontrol" id="u34fb41171c1049cc8296bdb37c76a210"><a name="u34fb41171c1049cc8296bdb37c76a210"></a><a name="u34fb41171c1049cc8296bdb37c76a210"></a>Service</span></b> &gt; <b><span class="uicontrol" id="uec27f28d057a436f97d3848c42e82d41"><a name="uec27f28d057a436f97d3848c42e82d41"></a><a name="uec27f28d057a436f97d3848c42e82d41"></a>Spark &gt; Spark WebUI &gt;</span></b> &gt; <b><span class="uicontrol" id="u1faa6e1faff448b2a0f70cb76056e547"><a name="u1faa6e1faff448b2a0f70cb76056e547"></a><a name="u1faa6e1faff448b2a0f70cb76056e547"></a>JobHistory</span></b></span>.</p>
</td>
</tr>
<tr id="r3ad586fa58b240bba1404a0b71915192"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="aa7c3b496599f4f42a5a183b884791cf4"><a name="aa7c3b496599f4f42a5a183b884791cf4"></a><a name="aa7c3b496599f4f42a5a183b884791cf4"></a>Hue</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="a757ca742e93b425a9f80cf43e4541844"><a name="a757ca742e93b425a9f80cf43e4541844"></a><a name="a757ca742e93b425a9f80cf43e4541844"></a>Choose <span class="menucascade" id="m9736ea92ad6743389df12da2ee04430d"><a name="m9736ea92ad6743389df12da2ee04430d"></a><a name="m9736ea92ad6743389df12da2ee04430d"></a><b><span class="uicontrol" id="u5eb268218936404a8e78077f4c720e11"><a name="u5eb268218936404a8e78077f4c720e11"></a><a name="u5eb268218936404a8e78077f4c720e11"></a>Service &gt; Hue &gt; Hue WebUI &gt; Hue (Active)</span></b></span></p>
<p id="a8c84ccad24744643bd66a78ef44e610a"><a name="a8c84ccad24744643bd66a78ef44e610a"></a><a name="a8c84ccad24744643bd66a78ef44e610a"></a>The Loader page is a graphical data migration management tool based on the open source Sqoop WebUI and is hosted on the Hue WebUI.</p>
</td>
</tr>
<tr id="row354611391909"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p117834212015"><a name="p117834212015"></a><a name="p117834212015"></a>Tez</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p71781742205"><a name="p71781742205"></a><a name="p71781742205"></a>Choose <span class="menucascade" id="menucascade41781842900"><a name="menucascade41781842900"></a><a name="menucascade41781842900"></a><b><span class="uicontrol" id="uicontrol217820422014"><a name="uicontrol217820422014"></a><a name="uicontrol217820422014"></a>Services&nbsp;&gt; Tez &gt; Tez Web UI &gt; TezUI</span></b></span></p>
</td>
</tr>
<tr id="row201932400014"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p91781542506"><a name="p91781542506"></a><a name="p91781542506"></a>Presto</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1961711170119"><a name="p1961711170119"></a><a name="p1961711170119"></a>Choose <span class="menucascade" id="menucascade01782421018"><a name="menucascade01782421018"></a><a name="menucascade01782421018"></a><b><span class="uicontrol" id="uicontrol91781742202"><a name="uicontrol91781742202"></a><a name="uicontrol91781742202"></a>Services&nbsp;&gt; Presto &gt; Presto Web UI &gt; Coordinator (Active)</span></b></span></p>
</td>
</tr>
<tr id="rf048deb8fc9344d4a6856fb414783eef"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="ae876cf53b936432ca4bede7f93d7b700"><a name="ae876cf53b936432ca4bede7f93d7b700"></a><a name="ae876cf53b936432ca4bede7f93d7b700"></a>Stream processing cluster</p>
</td>
<td class="cellrowborder" valign="top" width="31.990000000000002%" headers="mcps1.2.4.1.2 "><p id="a3e5e24edf0e4445abb8116b5d056393c"><a name="a3e5e24edf0e4445abb8116b5d056393c"></a><a name="a3e5e24edf0e4445abb8116b5d056393c"></a>Storm</p>
</td>
<td class="cellrowborder" valign="top" width="48.010000000000005%" headers="mcps1.2.4.1.3 "><p id="affed9872d31a4a3ab779f0a03ebe22ec"><a name="affed9872d31a4a3ab779f0a03ebe22ec"></a><a name="affed9872d31a4a3ab779f0a03ebe22ec"></a>Choose <span class="menucascade" id="m2a19b15c4dca43e283ace6ea12f049e1"><a name="m2a19b15c4dca43e283ace6ea12f049e1"></a><a name="m2a19b15c4dca43e283ace6ea12f049e1"></a><b><span class="uicontrol" id="u72ab8cc4980e4896b8d22a848572fa28"><a name="u72ab8cc4980e4896b8d22a848572fa28"></a><a name="u72ab8cc4980e4896b8d22a848572fa28"></a>Service &gt; Storm &gt; WebUI &gt; UI</span></b></span></p>
</td>
</tr>
</tbody>
</table>

