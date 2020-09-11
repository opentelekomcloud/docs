# How Can I View and Modify Kernel Parameters of a Linux ECS?<a name="EN-US_TOPIC_0107659745"></a>

This document describes common Linux kernel parameters and how to view and modify them. Modify the kernel parameters only if the parameter settings affect your services. If the parameter settings must be modified, ensure that:

-   The target parameter settings meet service requirements.
-   Learn the kernel parameters to be modified, which vary depending on OS versions. For details about common kernel parameters, see  [Table 1](#table15253154115313).
-   Back up key ECS data before modifying kernel parameter settings.

## Background<a name="section192621849125219"></a>

**Table  1**  Common Linux kernel parameters

<a name="table15253154115313"></a>
<table><thead align="left"><tr id="row925310485320"><th class="cellrowborder" valign="top" width="34%" id="mcps1.2.3.1.1"><p id="p3253114125316"><a name="p3253114125316"></a><a name="p3253114125316"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.2.3.1.2"><p id="p12253443539"><a name="p12253443539"></a><a name="p12253443539"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1325317420532"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p62792019155413"><a name="p62792019155413"></a><a name="p62792019155413"></a>net.core.rmem_default</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p9279519185414"><a name="p9279519185414"></a><a name="p9279519185414"></a>Specifies the default size (in bytes) of the window for receiving TCP data.</p>
</td>
</tr>
<tr id="row1325364125316"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p14279111965414"><a name="p14279111965414"></a><a name="p14279111965414"></a>net.core.rmem_max</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p2279131918542"><a name="p2279131918542"></a><a name="p2279131918542"></a>Specifies the maximum size (in bytes) of the window for receiving TCP data.</p>
</td>
</tr>
<tr id="row10253740532"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p10279171975412"><a name="p10279171975412"></a><a name="p10279171975412"></a>net.core.wmem_default</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p9279181916549"><a name="p9279181916549"></a><a name="p9279181916549"></a>Specifies the default size (in bytes) of the window for transmitting TCP data.</p>
</td>
</tr>
<tr id="row42546475310"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p11279201917540"><a name="p11279201917540"></a><a name="p11279201917540"></a>net.core.wmem_max</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p72792197542"><a name="p72792197542"></a><a name="p72792197542"></a>Specifies the maximum size (in bytes) of the window for transmitting TCP data.</p>
</td>
</tr>
<tr id="row13254164165313"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p13279131965411"><a name="p13279131965411"></a><a name="p13279131965411"></a>net.core.netdev_max_backlog</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p15279171911549"><a name="p15279171911549"></a><a name="p15279171911549"></a>Specifies the maximum number of packets that can be sent to a queue when the rate at which each network port receives packets is faster than the rate at which the kernel processes these packets.</p>
</td>
</tr>
<tr id="row172541349536"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p1327941955416"><a name="p1327941955416"></a><a name="p1327941955416"></a>net.core.somaxconn</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p112791119135414"><a name="p112791119135414"></a><a name="p112791119135414"></a>Defines the maximum length of the listening queue for each port in the system. This parameter applies globally.</p>
</td>
</tr>
<tr id="row1125411415318"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p427921911547"><a name="p427921911547"></a><a name="p427921911547"></a>net.core.optmem_max</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p10279181917545"><a name="p10279181917545"></a><a name="p10279181917545"></a>Specifies the maximum size of the buffer allowed by each socket.</p>
</td>
</tr>
<tr id="row1191115175317"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p4279161912542"><a name="p4279161912542"></a><a name="p4279161912542"></a>net.ipv4.tcp_mem</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p1027911191548"><a name="p1027911191548"></a><a name="p1027911191548"></a>Uses the TCP stack to show memory usage in memory pages (4 KB generally).</p>
<p id="p132791019185418"><a name="p132791019185418"></a><a name="p132791019185418"></a>The first value is the lower limit of memory usage.</p>
<p id="p1427917193540"><a name="p1427917193540"></a><a name="p1427917193540"></a>The second value is the upper limit of the load added to the buffer when the memory is overloaded.</p>
<p id="p727919198540"><a name="p727919198540"></a><a name="p727919198540"></a>The third value is the upper limit of memory usage. When this value is reached, packets can be discarded to reduce memory usage. For a large BDP, increase the parameter value as needed. The unit of this parameter is memory page but not byte.</p>
</td>
</tr>
<tr id="row612110125418"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p2279121935416"><a name="p2279121935416"></a><a name="p2279121935416"></a>net.ipv4.tcp_rmem</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p0279181915548"><a name="p0279181915548"></a><a name="p0279181915548"></a>Specifies the memory used by sockets for automatic optimization.</p>
<p id="p12791119125416"><a name="p12791119125416"></a><a name="p12791119125416"></a>The first value is the minimum number of bytes allocated to the socket buffer for receiving data.</p>
<p id="p127921916546"><a name="p127921916546"></a><a name="p127921916546"></a>The second value is the default value, which is overwritten by <strong id="b8423527062018"><a name="b8423527062018"></a><a name="b8423527062018"></a>rmem_default</strong>. The buffer size can increase to this value when the system load is not heavy.</p>
<p id="p327915192549"><a name="p327915192549"></a><a name="p327915192549"></a>The third value is the maximum number of bytes allocated to the socket buffer for receiving data. This value is overwritten by <strong id="b84235270620328"><a name="b84235270620328"></a><a name="b84235270620328"></a>rmem_max</strong>.</p>
</td>
</tr>
<tr id="row4484131211542"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p152791119185415"><a name="p152791119185415"></a><a name="p152791119185415"></a>net.ipv4.tcp_wmem</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p62791919165419"><a name="p62791919165419"></a><a name="p62791919165419"></a>Specifies the memory used by sockets for automatic optimization.</p>
<p id="p13279121985415"><a name="p13279121985415"></a><a name="p13279121985415"></a>The first value is the minimum number of bytes allocated to the socket buffer for transmitting data.</p>
<p id="p10279131945411"><a name="p10279131945411"></a><a name="p10279131945411"></a>The second value is the default value, which is overwritten by <strong id="b1765230813"><a name="b1765230813"></a><a name="b1765230813"></a>wmem_default</strong>. The buffer size can increase to this value when the system load is not heavy.</p>
<p id="p1127931955419"><a name="p1127931955419"></a><a name="p1127931955419"></a>The third value is the maximum number of bytes allocated to the socket buffer for transmitting data. This value is overwritten by <strong id="b480241570"><a name="b480241570"></a><a name="b480241570"></a>wmem_max</strong>.</p>
</td>
</tr>
<tr id="row9484201215410"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p927991916543"><a name="p927991916543"></a><a name="p927991916543"></a>net.ipv4.tcp_keepalive_time</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p19279181945420"><a name="p19279181945420"></a><a name="p19279181945420"></a>Specifies the interval at which keepalive detection messages are sent in seconds for checking TCP connections.</p>
</td>
</tr>
<tr id="row1348411205416"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p112791419145413"><a name="p112791419145413"></a><a name="p112791419145413"></a>net.ipv4.tcp_keepalive_intvl</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p12279181945411"><a name="p12279181945411"></a><a name="p12279181945411"></a>Specifies the interval at which keepalive detection messages are resent in seconds when no response is received.</p>
</td>
</tr>
<tr id="row748491245418"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p10279619115413"><a name="p10279619115413"></a><a name="p10279619115413"></a>net.ipv4.tcp_keepalive_probes</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p1127931917544"><a name="p1127931917544"></a><a name="p1127931917544"></a>Specifies the maximum number of keepalive detection messages that are sent to determine a TCP connection failure.</p>
</td>
</tr>
<tr id="row44849127542"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p92793194545"><a name="p92793194545"></a><a name="p92793194545"></a>net.ipv4.tcp_sack</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p62792190549"><a name="p62792190549"></a><a name="p62792190549"></a>Enables selective acknowledgment (value <strong id="b842352706201018"><a name="b842352706201018"></a><a name="b842352706201018"></a>1</strong> indicates enabled). This configuration allows the transmitter to resend only lost packets, thereby improving system performance. However, this configuration will increase the CPU usage. You are suggested to enable selective acknowledgment for WAN communication.</p>
</td>
</tr>
<tr id="row2121903549"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p102801519185417"><a name="p102801519185417"></a><a name="p102801519185417"></a>net.ipv4.tcp_fack</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p1628016193546"><a name="p1628016193546"></a><a name="p1628016193546"></a>Enables forwarding acknowledgment for selective acknowledgment (SACK), thereby reducing congestion. You are suggested to enable forwarding acknowledgment.</p>
</td>
</tr>
<tr id="row1121180195411"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p12280121914549"><a name="p12280121914549"></a><a name="p12280121914549"></a>net.ipv4.tcp_timestamps</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p8280141919544"><a name="p8280141919544"></a><a name="p8280141919544"></a>Specifies a TCP timestamp, which will add 12 bytes in the TCP packet header. This configuration calculates RTT using RFC1323, a more precise retransmission method upon timeout than retransmission. You are suggested to use this configuration for higher system performance.</p>
</td>
</tr>
<tr id="row1812117015543"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p16280191918544"><a name="p16280191918544"></a><a name="p16280191918544"></a>net.ipv4.tcp_window_scaling</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p628021925411"><a name="p628021925411"></a><a name="p628021925411"></a>Enables RFC1323-based window scaling by setting the parameter value to <strong id="b842352706202458"><a name="b842352706202458"></a><a name="b842352706202458"></a>1</strong> if the TCP window is larger than 64 KB. The maximum TCP window is 1 GB. This parameter takes effect only when window scaling is enabled on both ends of the TCP connection.</p>
</td>
</tr>
<tr id="row5732156145420"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p1828071913544"><a name="p1828071913544"></a><a name="p1828071913544"></a>net.ipv4.tcp_syncookies</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p1128011915415"><a name="p1128011915415"></a><a name="p1128011915415"></a>Specifies whether to enable TCP synchronization (<strong id="b842352706202721"><a name="b842352706202721"></a><a name="b842352706202721"></a>syncookie</strong>). This configuration prevents socket overloading when a large number of connections are attempted to set up. <strong id="b842352706202743"><a name="b842352706202743"></a><a name="b842352706202743"></a>CONFIG_SYN_COOKIES</strong> must be enabled in the kernel for compilation. The default value is <strong>0</strong>, indicating that TCP synchronization is disabled.</p>
</td>
</tr>
<tr id="row157321062544"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p1428018197542"><a name="p1428018197542"></a><a name="p1428018197542"></a>net.ipv4.tcp_tw_reuse</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p19645218349"><a name="p19645218349"></a><a name="p19645218349"></a>Specifies whether a <strong id="b1127844296195551"><a name="b1127844296195551"></a><a name="b1127844296195551"></a>TIME-WAIT</strong> socket (<strong id="b842352706203136"><a name="b842352706203136"></a><a name="b842352706203136"></a>TIME-WAIT</strong> port) can be used for new TCP connections.</p>
<div class="notice" id="note12102153419"><a name="note12102153419"></a><a name="note12102153419"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p1121112116344"><a name="p1121112116344"></a><a name="p1121112116344"></a>This parameter cannot be set to <strong id="b842352706204934"><a name="b842352706204934"></a><a name="b842352706204934"></a>1</strong> if NAT is enabled. Otherwise, an error will occur in remote ECS logins.</p>
</div></div>
</td>
</tr>
<tr id="row12732161544"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p228031935420"><a name="p228031935420"></a><a name="p228031935420"></a>net.ipv4.tcp_tw_recycle</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p19857534103412"><a name="p19857534103412"></a><a name="p19857534103412"></a>Allows fast recycle of <strong id="b842352706203228"><a name="b842352706203228"></a><a name="b842352706203228"></a>TIME-WAIT</strong> sockets.</p>
<div class="notice" id="note10828103418341"><a name="note10828103418341"></a><a name="note10828103418341"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p2085333453411"><a name="p2085333453411"></a><a name="p2085333453411"></a>This parameter cannot be set to <strong id="b669078907"><a name="b669078907"></a><a name="b669078907"></a>1</strong> if NAT is enabled. Otherwise, an error will occur in remote ECS logins.</p>
</div></div>
</td>
</tr>
<tr id="row207320620546"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p828131912544"><a name="p828131912544"></a><a name="p828131912544"></a>net.ipv4.tcp_fin_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p528121915542"><a name="p528121915542"></a><a name="p528121915542"></a>Specifies the time (in seconds) during which a socket TCP connection that is disconnected from the local end retains in <strong id="b842352706201143"><a name="b842352706201143"></a><a name="b842352706201143"></a>FIN-WAIT-2</strong> state. Process suspension may be caused by the disconnection from the peer end, continuous connection from the peer end, or unexpected causes.</p>
</td>
</tr>
<tr id="row6732156105411"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p1428181912547"><a name="p1428181912547"></a><a name="p1428181912547"></a>net.ipv4.ip_local_port_range</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p62812019195414"><a name="p62812019195414"></a><a name="p62812019195414"></a>Specifies local port numbers allowed by TCP/UDP.</p>
</td>
</tr>
<tr id="row373218619548"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p20281219145419"><a name="p20281219145419"></a><a name="p20281219145419"></a>net.ipv4.tcp_max_syn_backlog</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p628191911540"><a name="p628191911540"></a><a name="p628191911540"></a>Specifies the maximum number of connection requests that are not acknowledged by the peer end and that can be stored in the queue. The default value is <strong id="b543394205328"><a name="b543394205328"></a><a name="b543394205328"></a>1024</strong>. If the server is frequently overloaded, try to increase the value.</p>
</td>
</tr>
<tr id="row27334665418"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p162811619155420"><a name="p162811619155420"></a><a name="p162811619155420"></a>net.ipv4.tcp_low_latency</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p172811819135414"><a name="p172811819135414"></a><a name="p172811819135414"></a>This option should be disabled if the TCP/IP stack is used for high throughput, low latency.</p>
</td>
</tr>
<tr id="row17733263549"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p17281181915540"><a name="p17281181915540"></a><a name="p17281181915540"></a>net.ipv4.tcp_westwood</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p13281101915416"><a name="p13281101915416"></a><a name="p13281101915416"></a>Enables the congestion control algorithm on the transmitter end to evaluate throughput and improve the overall bandwidth utilization. You are suggested to enable the congestion control algorithm for WAN communication.</p>
</td>
</tr>
<tr id="row573310675413"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p1528111995419"><a name="p1528111995419"></a><a name="p1528111995419"></a>net.ipv4.tcp_bic</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p6281151975415"><a name="p6281151975415"></a><a name="p6281151975415"></a>Enables binary increase congestion for fast long-distance networks so that the connections with operations being performed at a rate of Gbit/s can be functional. You are suggested to enable binary increase congestion for WAN communication.</p>
</td>
</tr>
<tr id="row3121900541"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p10281101975417"><a name="p10281101975417"></a><a name="p10281101975417"></a>net.ipv4.tcp_max_tw_buckets</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p428101985414"><a name="p428101985414"></a><a name="p428101985414"></a>Specifies the number of TIME_WAIT buckets, which defaults to <strong id="b84235270623220"><a name="b84235270623220"></a><a name="b84235270623220"></a>180000</strong>. If the number of buckets exceeds the default value, extra ones will be cleared.</p>
</td>
</tr>
<tr id="row161217010549"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p1328261945413"><a name="p1328261945413"></a><a name="p1328261945413"></a>net.ipv4.tcp_synack_retries</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p20282171955418"><a name="p20282171955418"></a><a name="p20282171955418"></a>Specifies the number of times that SYN+ACK packets are retransmitted in <strong id="b84235270623326"><a name="b84235270623326"></a><a name="b84235270623326"></a>SYN_RECV</strong> state.</p>
</td>
</tr>
<tr id="row121218055411"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p142826199549"><a name="p142826199549"></a><a name="p142826199549"></a>net.ipv4.tcp_abort_on_overflow</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p15282019105416"><a name="p15282019105416"></a><a name="p15282019105416"></a>When this parameter is set to <strong id="b842352706231511"><a name="b842352706231511"></a><a name="b842352706231511"></a>1</strong>, if the system receives a large number of requests within a short period of time but fails to process them, the system will send reset packets to terminate the connections. It is recommended that you improve system processing capabilities by optimizing the application efficiency but not simply performing reset operations.</p>
<p id="p728281918547"><a name="p728281918547"></a><a name="p728281918547"></a>Default value: <strong id="b842352706232515"><a name="b842352706232515"></a><a name="b842352706232515"></a>0</strong></p>
</td>
</tr>
<tr id="row15500355185313"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p5282419205419"><a name="p5282419205419"></a><a name="p5282419205419"></a>net.ipv4.route.max_size</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p1028219195544"><a name="p1028219195544"></a><a name="p1028219195544"></a>Specifies the maximum number of routes allowed by the kernel.</p>
</td>
</tr>
<tr id="row350014551530"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p14282111975410"><a name="p14282111975410"></a><a name="p14282111975410"></a>net.ipv4.ip_forward</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p928271919549"><a name="p928271919549"></a><a name="p928271919549"></a>Forward packets between interfaces.</p>
</td>
</tr>
<tr id="row115001355185316"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p72821119115418"><a name="p72821119115418"></a><a name="p72821119115418"></a>net.ipv4.ip_default_ttl</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p428251914540"><a name="p428251914540"></a><a name="p428251914540"></a>Specifies the maximum number of hops that a packet can pass through.</p>
</td>
</tr>
<tr id="row1050005512535"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p12282141945413"><a name="p12282141945413"></a><a name="p12282141945413"></a>net.netfilter.nf_conntrack_tcp_timeout_established</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p82827194548"><a name="p82827194548"></a><a name="p82827194548"></a>Clears iptables connections that are inactive for a specified period of time.</p>
</td>
</tr>
<tr id="row175004559535"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p12282181965414"><a name="p12282181965414"></a><a name="p12282181965414"></a>net.netfilter.nf_conntrack_max</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p10282111915419"><a name="p10282111915419"></a><a name="p10282111915419"></a>Specifies the maximum value of hash entries.</p>
</td>
</tr>
</tbody>
</table>

## Viewing Kernel Parameters<a name="section68511530163412"></a>

-   Method 1: Run the cat command in  **/proc/sys**  to view file content.

    **/proc/sys/**  is a pseudo directory generated after the Linux kernel is started. The  **net**  folder in this directory stores all kernel parameters that have taken effect in the system. The directory tree structure is determined based on complete parameter names. For example,  **net.ipv4.tcp\_tw\_recycle**  corresponds to the  **/proc/sys/net/ipv4/tcp\_tw\_recycle**  file, and the content of the file is the parameter value.

    An example is provided as follows:

    To view the  **net.ipv4.tcp\_tw\_recycle**  value, run the following command:

    **cat /proc/sys/net/ipv4/tcp\_tw\_recycle**

-   Method 2: Use the  **/etc/sysctl.conf**  file.

    Run the following command to view all parameters that have taken effect in the system:

    **/usr/sbin/sysctl –a**

    ```
    net.ipv4.tcp_syncookies = 1
    net.ipv4.tcp_max_tw_buckets = 4096
    net.ipv4.tcp_tw_reuse = 1
    net.ipv4.tcp_tw_recycle = 1
    net.ipv4.tcp_keepalive_time = 1800
    net.ipv4.tcp_fin_timeout = 30
    ......
    net.ipv4.tcp_keepalive_time = 1200
    net.ipv4.ip_local_port_range = 1024 65000
    net.ipv4.tcp_max_syn_backlog = 8192
    net.ipv4.tcp_rmem = 16384 174760 349520
    net.ipv4.tcp_wmem = 16384 131072 262144
    net.ipv4.tcp_mem = 262144 524288 1048576
    ......
    ```


## Modifying Kernel Parameter Settings<a name="section1996094863415"></a>

-   Method 1: Run the echo command in  **/proc/sys**  to modify the file for the target kernel parameters.

    The parameter values changed using this method take effect only during the current running and will be reset after the system is restarted. This method is used for temporary verification. To make the modification take effect permanently, see method 2.

    **/proc/sys/**  is a pseudo directory generated after the Linux kernel is started. The  **net**  folder in this directory stores all kernel parameters that have taken effect in the system. The directory tree structure is determined based on complete parameter names. For example,  **net.ipv4.tcp\_tw\_recycle**  corresponds to the  **/proc/sys/net/ipv4/tcp\_tw\_recycle**  file, and the content of the file is the parameter value.

    An example is provided as follows:

    To change the  **net.ipv4.tcp\_tw\_recycle**  value to  **0**, run the following command:

    **echo "0" \> /proc/sys/net/ipv4/tcp\_tw\_recycle**

-   Method 2: Use the  **/etc/sysctl.conf**  file.

    The parameter values changed using this method take effect permanently.

    1.  Run the following command to change the value of a specified parameter:

        **/sbin/sysctl -w kernel.domainname="**_example.com_**"**

        An example is provided as follows:

        sysctl -w net.ipv4.tcp\_tw\_recycle="0"

    2.  Run the following command to change the parameter value in the  **/etc/sysctl.conf**  file:

        **vi /etc/sysctl.conf**

    3.  Run the following command for the configuration to take effect:

        **/sbin/sysctl -p**



