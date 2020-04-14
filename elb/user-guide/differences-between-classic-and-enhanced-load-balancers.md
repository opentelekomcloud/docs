# Differences Between Classic and Enhanced Load Balancers<a name="EN-US_TOPIC_0096587173"></a>

ELB provides two types of load balancers: classic load balancer and enhanced load balancer. Select an appropriate type based on application scenarios and your business needs.

-   Classic load balancers are applicable to web services with low traffic and simple applications.
-   Enhanced load balancers provide comprehensive Layer 7 load balancing capabilities and more powerful forwarding performance that features domain name or URL-based request routing. They are good choices for web services with high access traffic.

The two types of load balancers feature differently.  [Table 1](#en-us_topic_0195703738_en-us_topic_0096587173_table6357031615712)  lists the comparisons. \(√ indicates supported features, and — indicates the features that are not supported.\)

**Table  1**  Feature comparisons

<a name="en-us_topic_0195703738_en-us_topic_0096587173_table6357031615712"></a>
<table><thead align="left"><tr id="en-us_topic_0195703738_en-us_topic_0096587173_row2772050015712"><th class="cellrowborder" valign="top" width="19.698030196980305%" id="mcps1.2.5.1.1"><p id="en-us_topic_0195703738_en-us_topic_0096587173_p4504482815755"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p4504482815755"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p4504482815755"></a>Feature</p>
</th>
<th class="cellrowborder" valign="top" width="54.934506549345066%" id="mcps1.2.5.1.2"><p id="en-us_topic_0195703738_p9925916112214"><a name="en-us_topic_0195703738_p9925916112214"></a><a name="en-us_topic_0195703738_p9925916112214"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="12.928707129287071%" id="mcps1.2.5.1.3"><p id="en-us_topic_0195703738_en-us_topic_0096587173_p2475243715755"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p2475243715755"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p2475243715755"></a>Classic Load Balancer</p>
</th>
<th class="cellrowborder" valign="top" width="12.438756124387561%" id="mcps1.2.5.1.4"><p id="en-us_topic_0195703738_en-us_topic_0096587173_p5879037915755"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p5879037915755"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p5879037915755"></a>Enhanced Load Balancer</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0195703738_en-us_topic_0096587173_row6356639815712"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p3229821710363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p3229821710363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p3229821710363"></a>Public and private network load balancing</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><a name="en-us_topic_0195703738_ul6185840112516"></a><a name="en-us_topic_0195703738_ul6185840112516"></a><ul id="en-us_topic_0195703738_ul6185840112516"><li>Each public network load balancer has a public IP address bound and routes requests from clients to backend servers over the Internet.</li><li>Private network load balancers work in a VPC and route requests from clients to backend servers that are in the same VPC.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p6601881810363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p6601881810363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p6601881810363"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p4592404710363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p4592404710363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p4592404710363"></a>√</p>
</td>
</tr>
<tr id="en-us_topic_0195703738_en-us_topic_0096587173_row895479615712"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p14153648705"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p14153648705"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p14153648705"></a>Layer 4 (TCP or UDP) and Layer 7 load balancing (HTTP or HTTPS)</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><a name="en-us_topic_0195703738_ul44151727485"></a><a name="en-us_topic_0195703738_ul44151727485"></a><ul id="en-us_topic_0195703738_ul44151727485"><li>Layer 4 load balancing: supports TCP and UDP. After receiving requests from the clients, the load balancer directly routes the requests to backend servers. Load balancing at Layer 4 features high routing efficiency and fast data transmission.</li><li>Layer 7 load balancing: supports HTTP and HTTPS. After receiving a request, the load balancer identifies the fields in the HTTP/HTTPS packet header and routes the request based on these fields. Though the routing efficiency is lower than that at Layer 4, load balancing at Layer 7 provides some advanced functions such as encrypted transmission and cookie-based sticky sessions.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p3411734710363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p3411734710363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p3411734710363"></a>√ (UDP not supported for private network load balancers)</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p19691124315148"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p19691124315148"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p19691124315148"></a>√</p>
</td>
</tr>
<tr id="en-us_topic_0195703738_en-us_topic_0096587173_row7028404153925"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p5428175710363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p5428175710363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p5428175710363"></a>Load balancing algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><p id="p181149441214"><a name="p181149441214"></a><a name="p181149441214"></a>Both enhanced and classic load balancers support round robin, least connections, and source IP hash. Enhanced load balancers also allow you to set weights for your backend servers and route requests based on server weights.</p>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p5956993310363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p5956993310363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p5956993310363"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p6043528110363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p6043528110363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p6043528110363"></a>√</p>
</td>
</tr>
<tr id="en-us_topic_0195703738_en-us_topic_0096587173_row27107177153925"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p3390510010363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p3390510010363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p3390510010363"></a>Sticky session</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0195703738_p392651662216"><a name="en-us_topic_0195703738_p392651662216"></a><a name="en-us_topic_0195703738_p392651662216"></a>Sticky sessions can identify the association between the client and backend server. Once this feature is enabled, requests from the same client are routed to the same backend server during the session.</p>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p6195858810363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p6195858810363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p6195858810363"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p5258971210363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p5258971210363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p5258971210363"></a>√</p>
</td>
</tr>
<tr id="en-us_topic_0195703738_en-us_topic_0096587173_row48722680155017"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p1873900110363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1873900110363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1873900110363"></a>WebSocket protocol</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0195703738_p12926111622212"><a name="en-us_topic_0195703738_p12926111622212"></a><a name="en-us_topic_0195703738_p12926111622212"></a>WebSocket is a new HTML5 protocol that provides full-duplex communication between the browser and the server. WebSocket saves server resources and bandwidth, and enables real-time communication.</p>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p2835467010363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p2835467010363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p2835467010363"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p1502689610363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1502689610363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1502689610363"></a>√</p>
</td>
</tr>
<tr id="en-us_topic_0195703738_en-us_topic_0096587173_row39069843155017"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p1586285410363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1586285410363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1586285410363"></a>Domain name- or URL-based forwarding</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0195703738_p199261316172211"><a name="en-us_topic_0195703738_p199261316172211"></a><a name="en-us_topic_0195703738_p199261316172211"></a>ELB allows you to add forwarding policies to forward requests to different backend server groups based on the domain names or URLs specified in the forwarding policies. Currently, you can add forwarding policies only to HTTP or HTTPS listeners.</p>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p4728709610363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p4728709610363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p4728709610363"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p504955310363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p504955310363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p504955310363"></a>√</p>
</td>
</tr>
<tr id="en-us_topic_0195703738_en-us_topic_0096587173_row47086911155017"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p2785298210363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p2785298210363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p2785298210363"></a>ECSs as backend servers</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0195703738_p18926111692217"><a name="en-us_topic_0195703738_p18926111692217"></a><a name="en-us_topic_0195703738_p18926111692217"></a>You can add ECSs to backend server groups to receive requests from load balancers.</p>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p598418810363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p598418810363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p598418810363"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p1495723810363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1495723810363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1495723810363"></a>√</p>
</td>
</tr>
<tr id="en-us_topic_0195703738_en-us_topic_0096587173_row46158875155023"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p4232997810363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p4232997810363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p4232997810363"></a>Access control (whitelist)</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0195703738_p9926171612215"><a name="en-us_topic_0195703738_p9926171612215"></a><a name="en-us_topic_0195703738_p9926171612215"></a>You can add a whitelist to specify the IP addresses that can access a listener.</p>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p617616610363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p617616610363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p617616610363"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p3050746310363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p3050746310363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p3050746310363"></a>√</p>
</td>
</tr>
<tr id="en-us_topic_0195703738_en-us_topic_0096587173_row17544173155023"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p2690725010363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p2690725010363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p2690725010363"></a>Standard OpenStack APIs</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0195703738_p9926216172213"><a name="en-us_topic_0195703738_p9926216172213"></a><a name="en-us_topic_0195703738_p9926216172213"></a>Both OpenStack native and proprietary APIs are supported, and the two types of APIs are compatible with each other.</p>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p4215914510363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p4215914510363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p4215914510363"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p5944762210363"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p5944762210363"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p5944762210363"></a>√</p>
</td>
</tr>
<tr id="en-us_topic_0195703738_en-us_topic_0096587173_row59281454142913"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p1492825413296"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1492825413296"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1492825413296"></a>BMSs as backend servers</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0195703738_p0762193112576"><a name="en-us_topic_0195703738_p0762193112576"></a><a name="en-us_topic_0195703738_p0762193112576"></a>BMSs can also be used as backend servers to receive requests.</p>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p392855416299"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p392855416299"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p392855416299"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p38512179378"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p38512179378"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p38512179378"></a>√</p>
</td>
</tr>
<tr id="en-us_topic_0195703738_en-us_topic_0096587173_row187941725193118"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p032510418311"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p032510418311"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p032510418311"></a>SNI for certificates</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0195703738_p692621616226"><a name="en-us_topic_0195703738_p692621616226"></a><a name="en-us_topic_0195703738_p692621616226"></a>Server Name Indication (SNI) is an extension to Transport Layer Security (TLS) and is used to resolve the issue that a server uses multiple domain names and certificates. After SNI is enabled, you need to deploy certificates corresponding to the domain names.</p>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p1327941113112"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1327941113112"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1327941113112"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p9328164133110"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p9328164133110"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p9328164133110"></a>√</p>
</td>
</tr>
<tr id="en-us_topic_0195703738_en-us_topic_0096587173_row14422449125319"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p1442216491533"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1442216491533"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1442216491533"></a>SSL protocols and cipher suites</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0195703738_p1992661662214"><a name="en-us_topic_0195703738_p1992661662214"></a><a name="en-us_topic_0195703738_p1992661662214"></a>Load balancers use SSL to receive requests from clients. A variety of cipher suites are supported, which are categorized into default suite, extended suite, and strict suite.</p>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p114222490532"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p114222490532"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p114222490532"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p242217497533"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p242217497533"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p242217497533"></a>—</p>
</td>
</tr>
<tr id="en-us_topic_0195703738_en-us_topic_0096587173_row68631143155616"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p10863124311562"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p10863124311562"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p10863124311562"></a>SSL protocol</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0195703738_p12926171620226"><a name="en-us_topic_0195703738_p12926171620226"></a><a name="en-us_topic_0195703738_p12926171620226"></a>Load balancers use SSL to receive requests from clients.</p>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p38631743165611"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p38631743165611"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p38631743165611"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p58635433562"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p58635433562"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p58635433562"></a>—</p>
</td>
</tr>
<tr id="en-us_topic_0195703738_en-us_topic_0096587173_row1383115695416"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p128311656205420"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p128311656205420"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p128311656205420"></a>OBS storage for access logs</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0195703738_p8323182514483"><a name="en-us_topic_0195703738_p8323182514483"></a><a name="en-us_topic_0195703738_p8323182514483"></a>Access logs of load balancers can be dumped to OBS buckets for storage.</p>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p1783155615415"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1783155615415"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1783155615415"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p92481516105516"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p92481516105516"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p92481516105516"></a>—</p>
</td>
</tr>
<tr id="en-us_topic_0195703738_en-us_topic_0096587173_row257915119235"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p15580612236"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p15580612236"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p15580612236"></a>Server weight</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0195703738_p1392616161222"><a name="en-us_topic_0195703738_p1392616161222"></a><a name="en-us_topic_0195703738_p1392616161222"></a>Enhanced load balancers provide two algorithms that can route requests based on server weights: weighted round robin and weighted least connections.</p>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p196781017236"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p196781017236"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p196781017236"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p1058010132314"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1058010132314"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1058010132314"></a>√</p>
</td>
</tr>
<tr id="en-us_topic_0195703738_en-us_topic_0096587173_row117071371990"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p87097374916"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p87097374916"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p87097374916"></a>Modification to the certificate content</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0195703738_p19926121618228"><a name="en-us_topic_0195703738_p19926121618228"></a><a name="en-us_topic_0195703738_p19926121618228"></a>After a certificate is created, you can modify its content.</p>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p484018107108"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p484018107108"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p484018107108"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p177112811108"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p177112811108"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p177112811108"></a>√</p>
</td>
</tr>
<tr id="en-us_topic_0195703738_en-us_topic_0096587173_row419320111017"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p41972015106"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p41972015106"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p41972015106"></a>Mutual authentication</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0195703738_p13927916172220"><a name="en-us_topic_0195703738_p13927916172220"></a><a name="en-us_topic_0195703738_p13927916172220"></a>The identities of both communication parties are authenticated to ensure security. Therefore, you need to deploy both the server certificate and client certificate. Currently, only HTTPS listeners support this feature.</p>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p12191205102"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p12191205102"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p12191205102"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p639118121115"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p639118121115"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p639118121115"></a>√</p>
</td>
</tr>
<tr id="en-us_topic_0195703738_en-us_topic_0096587173_row9668172933114"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p1566919293315"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1566919293315"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1566919293315"></a>HTTP redirection</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0195703738_p1592717161225"><a name="en-us_topic_0195703738_p1592717161225"></a><a name="en-us_topic_0195703738_p1592717161225"></a>HTTP traffic is redirected to HTTPS. When the client sends an HTTP request, the backend server returns an HTTPS response. Currently, only enhanced load balancers support this feature.</p>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p1544442153215"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1544442153215"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p1544442153215"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0195703738_en-us_topic_0096587173_p134444283210"><a name="en-us_topic_0195703738_en-us_topic_0096587173_p134444283210"></a><a name="en-us_topic_0195703738_en-us_topic_0096587173_p134444283210"></a>√</p>
</td>
</tr>
<tr id="row543492212472"><td class="cellrowborder" valign="top" width="19.698030196980305%" headers="mcps1.2.5.1.1 "><p id="p124359225474"><a name="p124359225474"></a><a name="p124359225474"></a>Performance monitoring on a per listener basis</p>
</td>
<td class="cellrowborder" valign="top" width="54.934506549345066%" headers="mcps1.2.5.1.2 "><p id="p18435192215478"><a name="p18435192215478"></a><a name="p18435192215478"></a>Cloud Eye is a monitoring service, which allows you to monitor your resources, including load balancers.</p>
</td>
<td class="cellrowborder" valign="top" width="12.928707129287071%" headers="mcps1.2.5.1.3 "><p id="p1028542095210"><a name="p1028542095210"></a><a name="p1028542095210"></a>—</p>
</td>
<td class="cellrowborder" valign="top" width="12.438756124387561%" headers="mcps1.2.5.1.4 "><p id="p8285102020522"><a name="p8285102020522"></a><a name="p8285102020522"></a>√</p>
</td>
</tr>
</tbody>
</table>

