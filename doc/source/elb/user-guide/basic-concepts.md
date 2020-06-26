# Basic Concepts<a name="EN-US_TOPIC_0190845961"></a>

**Table  1**  Some concepts about ELB

<a name="table17643195014453"></a>
<table><thead align="left"><tr id="row1644350164511"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.3.1.1"><p id="p864415064515"><a name="p864415064515"></a><a name="p864415064515"></a>Term</p>
</th>
<th class="cellrowborder" valign="top" width="82%" id="mcps1.2.3.1.2"><p id="p96442503458"><a name="p96442503458"></a><a name="p96442503458"></a>Definition</p>
</th>
</tr>
</thead>
<tbody><tr id="row864475011450"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p4644135024515"><a name="p4644135024515"></a><a name="p4644135024515"></a>Load balancer</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p3644250144511"><a name="p3644250144511"></a><a name="p3644250144511"></a>A load balancer distributes incoming traffic across backend servers.</p>
</td>
</tr>
<tr id="row17644115034512"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p186441250134518"><a name="p186441250134518"></a><a name="p186441250134518"></a>Listener</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p2644950114515"><a name="p2644950114515"></a><a name="p2644950114515"></a>A listener listens on requests from clients and routes the requests to backend <span id="text64561152173613"><a name="text64561152173613"></a><a name="text64561152173613"></a>server</span>s based on the settings that you configure when adding the listener.</p>
</td>
</tr>
<tr id="row1364411502455"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p15644155084519"><a name="p15644155084519"></a><a name="p15644155084519"></a>Backend server</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p1464425016457"><a name="p1464425016457"></a><a name="p1464425016457"></a>A backend server is an ECS or BMS added to a backend <span id="en-us_topic_0164706624_text134779184156"><a name="en-us_topic_0164706624_text134779184156"></a><a name="en-us_topic_0164706624_text134779184156"></a>server</span> group associated with a load balancer. When adding a listener to a load balancer, you create or select a backend <span id="en-us_topic_0164706624_text01565413152"><a name="en-us_topic_0164706624_text01565413152"></a><a name="en-us_topic_0164706624_text01565413152"></a>server</span> group to receive requests from the load balancer using the port and protocol you specify for the backend <span id="en-us_topic_0164706624_text12774182671815"><a name="en-us_topic_0164706624_text12774182671815"></a><a name="en-us_topic_0164706624_text12774182671815"></a>server</span> group and the load balancing algorithm you select.</p>
</td>
</tr>
<tr id="row19644950204515"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p156441850134517"><a name="p156441850134517"></a><a name="p156441850134517"></a>Backend server group</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p20644145034510"><a name="p20644145034510"></a><a name="p20644145034510"></a>A backend server group is used to route requests to one or more ECSs or BMSs that have same features. When you add a listener, you select a load balancing algorithm and create or select a backend server group. When the listener settings are met, traffic is routed to the corresponding backend server group.</p>
</td>
</tr>
<tr id="row7644165084514"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p4644205015458"><a name="p4644205015458"></a><a name="p4644205015458"></a>Health check</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p9644125014451"><a name="p9644125014451"></a><a name="p9644125014451"></a>The ELB system periodically sends requests to associated backend servers to check their health statuses. This process is called health check, through which the ELB system decides whether backend servers are able to process requests. If a backend server is detected unhealthy, the load balancer stops routing requests to this server, ensuring service reliability. After the backend server recovers, the load balancer resumes routing requests to it.</p>
</td>
</tr>
<tr id="row20644450204518"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p1964418505454"><a name="p1964418505454"></a><a name="p1964418505454"></a>Redirect</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p5644135015457"><a name="p5644135015457"></a><a name="p5644135015457"></a>HTTPS is an extension of HTTP. HTTPS enables data between a web server and a browser to be encrypted. Redirection allows you to redirect requests from HTTP to HTTPS.</p>
</td>
</tr>
<tr id="row364405094516"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p5462101841813"><a name="p5462101841813"></a><a name="p5462101841813"></a>Sticky session</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p1564418504452"><a name="p1564418504452"></a><a name="p1564418504452"></a>Sticky sessions are a mechanism that checks whether the processes of exchanges between the client and server are associated. This ensures that requests can be routed to the same server before a session elapses.</p>
</td>
</tr>
<tr id="row564410505454"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p7644750164517"><a name="p7644750164517"></a><a name="p7644750164517"></a>WebSocket</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p17963155112120"><a name="p17963155112120"></a><a name="p17963155112120"></a>WebSocket is a new HTML5 protocol that provides full-duplex communication between the browser and the server. WebSocket saves server resources and bandwidth, and enables real-time communication. Both WebSocket and HTTP depend on TCP to transmit data. A handshake connection is required between the browser and server, so that they can communicate with each other only after the connection is established. However, as a bidirectional communication protocol, WebSocket is distinct from HTTP. After a connection is established, both the server and browser (or client agent) can actively send or receive data to or from each other, which is similar to Socket.</p>
</td>
</tr>
<tr id="row3644145013456"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p064585018451"><a name="p064585018451"></a><a name="p064585018451"></a>SNI</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p564595064516"><a name="p564595064516"></a><a name="p564595064516"></a>If an application provides multiple domain names and each domain name uses a different certificate, you can enable SNI when adding an HTTPS listener. SNI is an extension to the TLS computer networking protocol and used to address the issue that one server can use only one certificate. SNI allows a server to present multiple certificates on the same IP address and TCP port number and hence allows multiple secure (HTTPS) websites (or any other service over TLS) to be served by the same IP address without requiring all those sites to use the same certificate. This feature allows the client to submit the domain name information while sending an SSL handshake request. Once receiving the request, the load balancer queries the right certificate based on the domain name and returns it to the client. If no certificate is found, the load balancer will return a default certificate.</p>
</td>
</tr>
<tr id="row1264545054512"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p1764525015454"><a name="p1764525015454"></a><a name="p1764525015454"></a>Persistent connection</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p96451550104515"><a name="p96451550104515"></a><a name="p96451550104515"></a>A persistent connection allows multiple data packets to be sent continuously over a TCP connection. If no data packet is sent during the connection, the client and server need to send link detection packets to each other.</p>
</td>
</tr>
<tr id="row46458501457"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p26451050184518"><a name="p26451050184518"></a><a name="p26451050184518"></a>Short connection</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p15645125017455"><a name="p15645125017455"></a><a name="p15645125017455"></a>A short connection is established when data is exchanged between the client and server. After the data is sent, the connection is closed.</p>
</td>
</tr>
<tr id="row91101346807"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p1811116467011"><a name="p1811116467011"></a><a name="p1811116467011"></a>Concurrent connection</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p7111134616018"><a name="p7111134616018"></a><a name="p7111134616018"></a>Concurrent connections are total TCP connections received from clients and routed to backend servers by a load balancer per second.</p>
</td>
</tr>
</tbody>
</table>

