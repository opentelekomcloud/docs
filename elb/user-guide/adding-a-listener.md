# Adding a Listener<a name="EN-US_TOPIC_0166390466"></a>

## Scenarios<a name="section18950295143553"></a>

After creating a load balancer, you need to add at least one listener to the load balancer. A listener is a process that checks for requests using the protocol and port you configure for connections from clients to the load balancer, and the protocol and port from the load balancer to backend servers.

A listener also defines the health check configuration, based on which the load balancer continually checks the running statuses of backend servers. If a backend server is detected unhealthy, the load balancer routes traffic to these healthy ones. Traffic forwarding to this server resumes once it recovers.

## Add a Listener to an Enhanced Load Balancer<a name="section117173315403"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0166397871.jpg)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Under  **Listeners**, click  **Add Listener**. Configure the parameters by referring to  [Table 1](#table1441020925310),  [Table 2](#table6414109125314), and  [Table 3](#table124201898534).

    **Table  1**  Parameters for configuring a listener

    <a name="table1441020925310"></a>
    <table><thead align="left"><tr id="row6406792539"><th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.4.1.1"><p id="p14406149145315"><a name="p14406149145315"></a><a name="p14406149145315"></a><strong id="b12120195118401"><a name="b12120195118401"></a><a name="b12120195118401"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.535353535353536%" id="mcps1.2.4.1.2"><p id="p1540699185318"><a name="p1540699185318"></a><a name="p1540699185318"></a><strong id="b247810711505"><a name="b247810711505"></a><a name="b247810711505"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.4.1.3"><p id="p64061696536"><a name="p64061696536"></a><a name="p64061696536"></a><strong id="b476112875018"><a name="b476112875018"></a><a name="b476112875018"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row540649135313"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p114061099530"><a name="p114061099530"></a><a name="p114061099530"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p20406999532"><a name="p20406999532"></a><a name="p20406999532"></a>Specifies the listener name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p740618913531"><a name="p740618913531"></a><a name="p740618913531"></a>listener-pnqy</p>
    </td>
    </tr>
    <tr id="row1940718915310"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p10406391536"><a name="p10406391536"></a><a name="p10406391536"></a>Frontend Protocol/Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p1940615919533"><a name="p1940615919533"></a><a name="p1940615919533"></a>Specifies the protocol and port the load balancer uses to receive requests from clients and forward the requests to backend servers.</p>
    <p id="p14406159155310"><a name="p14406159155310"></a><a name="p14406159155310"></a>The port numbers range from 1 to 65535, and the following protocols are supported:</p>
    <a name="ul144061395537"></a><a name="ul144061395537"></a><ul id="ul144061395537"><li>HTTP</li></ul>
    <a name="ul74069935313"></a><a name="ul74069935313"></a><ul id="ul74069935313"><li>TCP</li><li>HTTPS</li><li>UDP</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p174061798536"><a name="p174061798536"></a><a name="p174061798536"></a>HTTP/80</p>
    </td>
    </tr>
    <tr id="row12407189195311"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p16407189175314"><a name="p16407189175314"></a><a name="p16407189175314"></a>Redirect</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p640720914532"><a name="p640720914532"></a><a name="p640720914532"></a>Redirects requests to an HTTPS listener when HTTP is used as the frontend protocol. If you have both HTTPS and HTTP listeners, you can use this feature to redirect the requests from the HTTP listener to the HTTPS listener to ensure security.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p94074916539"><a name="p94074916539"></a><a name="p94074916539"></a>N/A</p>
    </td>
    </tr>
    <tr id="row14407129145313"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p184071992539"><a name="p184071992539"></a><a name="p184071992539"></a>Redirected To</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p18407896536"><a name="p18407896536"></a><a name="p18407896536"></a>Specifies the HTTPS listener to which requests are redirected.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p184076985311"><a name="p184076985311"></a><a name="p184076985311"></a>N/A</p>
    </td>
    </tr>
    <tr id="row8407159115311"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p1540749135315"><a name="p1540749135315"></a><a name="p1540749135315"></a>Server Certificate</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p164079916535"><a name="p164079916535"></a><a name="p164079916535"></a>Specifies the certificate the server uses to authenticate the client when HTTPS is used as the frontend protocol.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p2040712955313"><a name="p2040712955313"></a><a name="p2040712955313"></a>N/A</p>
    </td>
    </tr>
    <tr id="row1840817965315"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p540739155315"><a name="p540739155315"></a><a name="p540739155315"></a>Enable SNI</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p74089911535"><a name="p74089911535"></a><a name="p74089911535"></a>Specifies whether to enable Server Name Indication (SNI) when HTTPS is used as the frontend protocol.</p>
    <p id="p7408139175310"><a name="p7408139175310"></a><a name="p7408139175310"></a>SNI is an extension to Transport Layer Security (TLS) and is used to resolve the issue that a server uses multiple domain names and certificates. This feature allows the client to submit the domain name information while sending an SSL handshake request. Once receiving the request, the load balancer queries the right certificate based on the domain name and returns it to the client. If no certificate is found, the load balancer will return a default certificate.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p19408189115312"><a name="p19408189115312"></a><a name="p19408189115312"></a>N/A</p>
    </td>
    </tr>
    <tr id="row54081398531"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p154080910537"><a name="p154080910537"></a><a name="p154080910537"></a>SNI Certificate</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p18408199185312"><a name="p18408199185312"></a><a name="p18408199185312"></a>Specifies the certificate associated with the domain name when the frontend protocol is HTTPS and SNI is enabled.</p>
    <p id="p174088918535"><a name="p174088918535"></a><a name="p174088918535"></a>You can select an existing certificate or create one.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p174081918533"><a name="p174081918533"></a><a name="p174081918533"></a>N/A</p>
    </td>
    </tr>
    <tr id="row1793611249220"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p1793717247218"><a name="p1793717247218"></a><a name="p1793717247218"></a>Advanced Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p093710244218"><a name="p093710244218"></a><a name="p093710244218"></a>Provides some additional features.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p993719241922"><a name="p993719241922"></a><a name="p993719241922"></a>N/A</p>
    </td>
    </tr>
    <tr id="row92711114697"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p12854547567"><a name="p12854547567"></a><a name="p12854547567"></a>Security Policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p208516541560"><a name="p208516541560"></a><a name="p208516541560"></a>Specifies the security policy you can use when you select HTTPS as the frontend protocol. For more information, see <a href="security-policy.md">Security Policy</a>. The following options are available:</p>
    <a name="ul5540161813580"></a><a name="ul5540161813580"></a><ul id="ul5540161813580"><li><strong id="b165381424191216"><a name="b165381424191216"></a><a name="b165381424191216"></a>Security Policy TLS-1-0</strong></li><li><strong id="b868316273133"><a name="b868316273133"></a><a name="b868316273133"></a>Security Policy TLS-1-1</strong></li><li><strong id="b560012919133"><a name="b560012919133"></a><a name="b560012919133"></a>Security Policy TLS-1-2</strong></li><li><strong id="b14123831111316"><a name="b14123831111316"></a><a name="b14123831111316"></a>Security Policy TLS-1-2-Strict</strong></li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p148514545563"><a name="p148514545563"></a><a name="p148514545563"></a>Security Policy TLS-1-0</p>
    </td>
    </tr>
    <tr id="row054792718213"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p85481272213"><a name="p85481272213"></a><a name="p85481272213"></a>Idle Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p4548152716217"><a name="p4548152716217"></a><a name="p4548152716217"></a>Specifies the length of time for a connection to keep alive, in seconds. If no request is received within this period, the load balancer closes the connection and establishes a new one with the client when the next request arrives. This parameter is mandatory when <strong id="b322113683015"><a name="b322113683015"></a><a name="b322113683015"></a>Frontend Protocol</strong> is set to <strong id="b927113912305"><a name="b927113912305"></a><a name="b927113912305"></a>TCP</strong>, <strong id="b63621242173011"><a name="b63621242173011"></a><a name="b63621242173011"></a>HTTP</strong> or <strong id="b1355674613019"><a name="b1355674613019"></a><a name="b1355674613019"></a>HTTPS</strong>. </p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p6548202714219"><a name="p6548202714219"></a><a name="p6548202714219"></a>30</p>
    </td>
    </tr>
    <tr id="row1914443014215"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p614412302217"><a name="p614412302217"></a><a name="p614412302217"></a>Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p1414473010213"><a name="p1414473010213"></a><a name="p1414473010213"></a>Specifies the length of time after which the load balancer closes the connection if the load balancer does not receive a request from the client, in the unit of seconds. This parameter is mandatory when <strong id="b747912566309"><a name="b747912566309"></a><a name="b747912566309"></a>Frontend Protocol</strong> is set to <strong id="b16479185633012"><a name="b16479185633012"></a><a name="b16479185633012"></a>HTTP</strong> or <strong id="b104791256193019"><a name="b104791256193019"></a><a name="b104791256193019"></a>HTTPS</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p181441930182114"><a name="p181441930182114"></a><a name="p181441930182114"></a>30</p>
    </td>
    </tr>
    <tr id="row1689019166216"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p0286103216253"><a name="p0286103216253"></a><a name="p0286103216253"></a>Response Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p189171672114"><a name="p189171672114"></a><a name="p189171672114"></a>Specifies the length of time after which the load balancer sends a 504 Gateway Timeout error to the client if the load balancer receives no response from the backend server, in the unit of seconds. This parameter is mandatory when <strong id="b463736123216"><a name="b463736123216"></a><a name="b463736123216"></a>Frontend Protocol</strong> is set to <strong id="b1163710617325"><a name="b1163710617325"></a><a name="b1163710617325"></a>HTTP</strong> or <strong id="b1963716143210"><a name="b1963716143210"></a><a name="b1963716143210"></a>HTTPS</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p11891191617213"><a name="p11891191617213"></a><a name="p11891191617213"></a>30</p>
    </td>
    </tr>
    <tr id="row1240949195314"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p1940929105310"><a name="p1940929105310"></a><a name="p1940929105310"></a>Mutual Authentication</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p24099919539"><a name="p24099919539"></a><a name="p24099919539"></a>Specifies whether to enable mutual authentication between the server and client. To enable mutual authentication, both a server certificate and CA certificate are required. This feature can be enabled when <strong id="b5235414131418"><a name="b5235414131418"></a><a name="b5235414131418"></a>Frontend Protocol</strong> is set to <strong id="b1877575113165"><a name="b1877575113165"></a><a name="b1877575113165"></a>HTTPS</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p14093917539"><a name="p14093917539"></a><a name="p14093917539"></a>N/A</p>
    </td>
    </tr>
    <tr id="row1441049115319"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p144091935311"><a name="p144091935311"></a><a name="p144091935311"></a>CA Certificate</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p6409199155319"><a name="p6409199155319"></a><a name="p6409199155319"></a>Specifies the certificate the server uses to authenticate the client when HTTPS is used as the frontend protocol. This parameter is mandatory when <strong id="b161806193141"><a name="b161806193141"></a><a name="b161806193141"></a>Frontend Protocol</strong> is set to <strong id="b1618161917147"><a name="b1618161917147"></a><a name="b1618161917147"></a>HTTPS</strong> and mutual authentication is enabled.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p13410194536"><a name="p13410194536"></a><a name="p13410194536"></a>N/A</p>
    </td>
    </tr>
    <tr id="row24101993534"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p241015975311"><a name="p241015975311"></a><a name="p241015975311"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p1741017985316"><a name="p1741017985316"></a><a name="p1741017985316"></a>Provides supplementary information about the listener.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p1041019920538"><a name="p1041019920538"></a><a name="p1041019920538"></a>N/A</p>
    </td>
    </tr>
    <tr id="row134101995313"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p84103915314"><a name="p84103915314"></a><a name="p84103915314"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p941079175316"><a name="p941079175316"></a><a name="p941079175316"></a>Adds tags to the listener. Each tag is a key-value pair, and the tag key is unique.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p12410189115317"><a name="p12410189115317"></a><a name="p12410189115317"></a>11/11</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Parameters for adding a backend server group

    <a name="table6414109125314"></a>
    <table><thead align="left"><tr id="row24119915312"><th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.4.1.1"><p id="p1341114918533"><a name="p1341114918533"></a><a name="p1341114918533"></a><strong id="b08081543111411"><a name="b08081543111411"></a><a name="b08081543111411"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.535353535353536%" id="mcps1.2.4.1.2"><p id="p13411119115314"><a name="p13411119115314"></a><a name="p13411119115314"></a><strong id="b1960354431415"><a name="b1960354431415"></a><a name="b1960354431415"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.4.1.3"><p id="p1441116918537"><a name="p1441116918537"></a><a name="p1441116918537"></a><strong id="b173045452145"><a name="b173045452145"></a><a name="b173045452145"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row941189135319"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p174111699530"><a name="p174111699530"></a><a name="p174111699530"></a>Backend Server Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p1241118935319"><a name="p1241118935319"></a><a name="p1241118935319"></a>Specifies a group of servers with the same features that receive requests from the load balancer. You can select <strong id="b178791121105620"><a name="b178791121105620"></a><a name="b178791121105620"></a>Create new</strong> or <strong id="b259952513566"><a name="b259952513566"></a><a name="b259952513566"></a>Use existing</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p1341113935310"><a name="p1341113935310"></a><a name="p1341113935310"></a>Create new</p>
    </td>
    </tr>
    <tr id="row541279125318"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p1741120913539"><a name="p1741120913539"></a><a name="p1741120913539"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p204128965312"><a name="p204128965312"></a><a name="p204128965312"></a>Specifies the backend server group name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p13412699533"><a name="p13412699533"></a><a name="p13412699533"></a>server_group-sq4v</p>
    </td>
    </tr>
    <tr id="row64123910531"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p54120975314"><a name="p54120975314"></a><a name="p54120975314"></a>Backend Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p1241215910537"><a name="p1241215910537"></a><a name="p1241215910537"></a>Specifies the protocol used by backend servers to receive requests.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p841216919534"><a name="p841216919534"></a><a name="p841216919534"></a>HTTP</p>
    </td>
    </tr>
    <tr id="row184131694530"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p741211985316"><a name="p741211985316"></a><a name="p741211985316"></a>Load Balancing Algorithm</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p241213913535"><a name="p241213913535"></a><a name="p241213913535"></a>Specifies the algorithm the load balancer uses to distribute traffic.</p>
    <a name="ul164121491534"></a><a name="ul164121491534"></a><ul id="ul164121491534"><li><strong id="b99191559153"><a name="b99191559153"></a><a name="b99191559153"></a>Weighted round robin</strong>: Requests are routed to different servers based on their weights, which indicate server processing performance. Backend servers with higher weights receive proportionately more requests, whereas equal-weighted servers receive the same number of requests.</li><li><strong id="b157766981616"><a name="b157766981616"></a><a name="b157766981616"></a>Weighted least connections</strong>: In addition to the weight assigned to each server, the number of connections processed by each backend server is also considered. Requests are routed to the server with the lowest connections-to-weight ratio.</li><li><strong id="b6318161517164"><a name="b6318161517164"></a><a name="b6318161517164"></a>Source IP hash</strong>: The source IP address of the request is input into a hash algorithm, and the resulting hash is used to identify a server in the static fragment table.</li></ul>
    <div class="note" id="note341217917533"><a name="note341217917533"></a><a name="note341217917533"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p9412129185318"><a name="p9412129185318"></a><a name="p9412129185318"></a>Choose an appropriate algorithm based on your requirement to distribute requests and improve load balancing capabilities.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p1541319915534"><a name="p1541319915534"></a><a name="p1541319915534"></a>Weighted round robin</p>
    </td>
    </tr>
    <tr id="row11413149115315"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p184131091534"><a name="p184131091534"></a><a name="p184131091534"></a>Sticky Session</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p1441319955312"><a name="p1441319955312"></a><a name="p1441319955312"></a>Specifies whether to enable sticky sessions. After this feature is enabled, all requests from a client during one session are sent to the same backend server.</p>
    <div class="note" id="note941399195314"><a name="note941399195314"></a><a name="note941399195314"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p841318975316"><a name="p841318975316"></a><a name="p841318975316"></a>For HTTP and HTTPS listeners, enabling or disabling sticky sessions may cause few seconds of service interruption.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p14131975315"><a name="p14131975315"></a><a name="p14131975315"></a>N/A</p>
    </td>
    </tr>
    <tr id="row84141394533"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p1741329145317"><a name="p1741329145317"></a><a name="p1741329145317"></a>Sticky Session Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p154132095532"><a name="p154132095532"></a><a name="p154132095532"></a>Specifies the sticky session type. The following options are available:</p>
    <a name="ul1241312925312"></a><a name="ul1241312925312"></a><ul id="ul1241312925312"><li><strong id="b151514495166"><a name="b151514495166"></a><a name="b151514495166"></a>Source IP address</strong>: The hash of the source IP address of the request is used to identify a server in the static fragment table.</li><li><strong id="b1354916515165"><a name="b1354916515165"></a><a name="b1354916515165"></a>Load balancer cookie</strong>: The load balancer generates a cookie after receiving a request from the client. All subsequent requests with the cookie are routed to the same backend server for processing.</li><li><strong id="b16971614202315"><a name="b16971614202315"></a><a name="b16971614202315"></a>Application cookie</strong>: This method relies on backend applications. The application on the first backend server that receives the request generates a cookie. All subsequent requests that contain the cookie will be processed by the same backend server.</li></ul>
    <div class="note" id="note184149920533"><a name="note184149920533"></a><a name="note184149920533"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul67056312135"></a><a name="ul67056312135"></a><ul id="ul67056312135"><li><strong id="b637914234238"><a name="b637914234238"></a><a name="b637914234238"></a>Source IP address</strong> is the only choice available when TCP is used as the frontend protocol. If <strong id="b1270752462312"><a name="b1270752462312"></a><a name="b1270752462312"></a>HTTP</strong> or <strong id="b17708192452313"><a name="b17708192452313"></a><a name="b17708192452313"></a>HTTPS</strong> is selected as the frontend protocol, the sticky session type can be <strong id="b1570982452319"><a name="b1570982452319"></a><a name="b1570982452319"></a>Load balancer cookie</strong> or <strong id="b87101245237"><a name="b87101245237"></a><a name="b87101245237"></a>Application cookie</strong>. Choose an appropriate sticky session type to better distribute requests and improve load balancing.</li><li>Sticky sessions at Layer 4 are maintained for one minute, while sticky sessions at Layer 7 are maintained for 24 hours.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p941410911535"><a name="p941410911535"></a><a name="p941410911535"></a>Source IP address</p>
    </td>
    </tr>
    <tr id="row17414596534"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p14147913531"><a name="p14147913531"></a><a name="p14147913531"></a>Cookie Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p10414159125310"><a name="p10414159125310"></a><a name="p10414159125310"></a>Specifies the cookie name. When <strong id="b178261442103913"><a name="b178261442103913"></a><a name="b178261442103913"></a>Application cookie</strong> is selected, you need to enter a cookie name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p194143935314"><a name="p194143935314"></a><a name="p194143935314"></a>cookieName-qsps</p>
    </td>
    </tr>
    <tr id="row541414919539"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p19414798530"><a name="p19414798530"></a><a name="p19414798530"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p1141469115313"><a name="p1141469115313"></a><a name="p1141469115313"></a>Provides supplementary information about the backend server group.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p114141696531"><a name="p114141696531"></a><a name="p114141696531"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Parameters for configuring a health check

    <a name="table124201898534"></a>
    <table><thead align="left"><tr id="row1641417985317"><th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.4.1.1"><p id="p1741415965319"><a name="p1741415965319"></a><a name="p1741415965319"></a><strong id="b95900520405"><a name="b95900520405"></a><a name="b95900520405"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.535353535353536%" id="mcps1.2.4.1.2"><p id="p134141496538"><a name="p134141496538"></a><a name="p134141496538"></a><strong id="b187845694015"><a name="b187845694015"></a><a name="b187845694015"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.4.1.3"><p id="p114141794530"><a name="p114141794530"></a><a name="p114141794530"></a><strong id="b758414784016"><a name="b758414784016"></a><a name="b758414784016"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1941509125312"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p174155905311"><a name="p174155905311"></a><a name="p174155905311"></a>Enable Health Check</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p15415195533"><a name="p15415195533"></a><a name="p15415195533"></a>Specifies whether to enable health checks.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p541519155318"><a name="p541519155318"></a><a name="p541519155318"></a>N/A</p>
    </td>
    </tr>
    <tr id="row44158910530"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p184153920531"><a name="p184153920531"></a><a name="p184153920531"></a>Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><a name="ul1941518935311"></a><a name="ul1941518935311"></a><ul id="ul1941518935311"><li>Specifies the protocol the load balancer uses to perform health checks on backend servers. You can use either TCP or HTTP. A selected protocol cannot be changed.</li><li>If the frontend protocol is UDP, the health check protocol is UDP by default.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p741518914531"><a name="p741518914531"></a><a name="p741518914531"></a>HTTP</p>
    </td>
    </tr>
    <tr id="row74169955315"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p8415159185317"><a name="p8415159185317"></a><a name="p8415159185317"></a>Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p0415109125316"><a name="p0415109125316"></a><a name="p0415109125316"></a>Specifies the domain name in the health check request. The domain name consists of digits, letters, hyphens (-), and periods (.), and must start with a digit or letter. This parameter is left blank by default and needs to be set only when <strong id="b182819464498"><a name="b182819464498"></a><a name="b182819464498"></a>Protocol</strong> is set to <strong id="b1728264614492"><a name="b1728264614492"></a><a name="b1728264614492"></a>HTTP</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p941614910531"><a name="p941614910531"></a><a name="p941614910531"></a>www.elb.com</p>
    </td>
    </tr>
    <tr id="row941639115316"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p154163918539"><a name="p154163918539"></a><a name="p154163918539"></a>Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p1941659135311"><a name="p1941659135311"></a><a name="p1941659135311"></a>Specifies the port the load balancer uses to perform health checks on backend servers. The port numbers range from 1 to 65535.</p>
    <div class="note" id="note1641616913534"><a name="note1641616913534"></a><a name="note1641616913534"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p14416492538"><a name="p14416492538"></a><a name="p14416492538"></a>This is an optional parameter. If no health check port is specified, the port of each backend server is used for health checks by default.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p114161199530"><a name="p114161199530"></a><a name="p114161199530"></a>80</p>
    </td>
    </tr>
    <tr id="row184161396534"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p24161914533"><a name="p24161914533"></a><a name="p24161914533"></a>Advanced Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p04167995319"><a name="p04167995319"></a><a name="p04167995319"></a>Provides some advanced features. Two options are available, <strong id="b154431621714"><a name="b154431621714"></a><a name="b154431621714"></a>Default</strong> and <strong id="b944320211118"><a name="b944320211118"></a><a name="b944320211118"></a>Custom</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p1416209135317"><a name="p1416209135317"></a><a name="p1416209135317"></a>Default</p>
    </td>
    </tr>
    <tr id="row641711935319"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p184163913537"><a name="p184163913537"></a><a name="p184163913537"></a>Interval (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p1941614985312"><a name="p1941614985312"></a><a name="p1941614985312"></a>Specifies the maximum time between health checks in the unit of second.</p>
    <p id="p54161797531"><a name="p54161797531"></a><a name="p54161797531"></a>The value ranges from <strong id="b1512992712117"><a name="b1512992712117"></a><a name="b1512992712117"></a>1</strong> to <strong id="b613012711111"><a name="b613012711111"></a><a name="b613012711111"></a>50</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p1417209155312"><a name="p1417209155312"></a><a name="p1417209155312"></a>5</p>
    </td>
    </tr>
    <tr id="row541759195312"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p9417179185316"><a name="p9417179185316"></a><a name="p9417179185316"></a>Timeout (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p7417149135320"><a name="p7417149135320"></a><a name="p7417149135320"></a>Specifies the maximum time required for waiting for a response from the health check in the unit of second. The value ranges from <strong id="b151413331914"><a name="b151413331914"></a><a name="b151413331914"></a>1</strong> to <strong id="b951443319110"><a name="b951443319110"></a><a name="b951443319110"></a>50</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p194173975319"><a name="p194173975319"></a><a name="p194173975319"></a>10</p>
    </td>
    </tr>
    <tr id="row541714916532"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p15417394539"><a name="p15417394539"></a><a name="p15417394539"></a>Check Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p1741712913533"><a name="p1741712913533"></a><a name="p1741712913533"></a>Specifies the health check URL, which is the destination on backend servers for health checks. This parameter is available only when <strong id="b1338144513113"><a name="b1338144513113"></a><a name="b1338144513113"></a>Protocol</strong> is set to <strong id="b933810451712"><a name="b933810451712"></a><a name="b933810451712"></a>HTTP</strong>. The value can contain 1 to 80 characters.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p4417119195313"><a name="p4417119195313"></a><a name="p4417119195313"></a>/index.html</p>
    </td>
    </tr>
    <tr id="row1941749175315"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.1 "><p id="p64172912539"><a name="p64172912539"></a><a name="p64172912539"></a>Maximum Retries</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.535353535353536%" headers="mcps1.2.4.1.2 "><p id="p2041799135312"><a name="p2041799135312"></a><a name="p2041799135312"></a>Specifies the maximum number of health check retries. The value ranges from <strong id="b137670513118"><a name="b137670513118"></a><a name="b137670513118"></a>1</strong> to <strong id="b157672511613"><a name="b157672511613"></a><a name="b157672511613"></a>10</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.4.1.3 "><p id="p44171975318"><a name="p44171975318"></a><a name="p44171975318"></a>3</p>
    </td>
    </tr>
    </tbody>
    </table>


1.  Click  **Finish**.
2.  Click  **OK**.

## Add a Listener to a Classic Load Balancer<a name="section7841311103416"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0166397902.jpg)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Click  **Classic**, locate the target load balancer, and click its name.
5.  Under  **Listeners**, click  **Add Listener**. In the  **Add Listener**  dialog box, specify the parameters by referring to  [Table 4](#table3947759918410).

    **Table  4**  Parameter description

    <a name="table3947759918410"></a>
    <table><thead align="left"><tr id="row1918557218410"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p25669989184122"><a name="p25669989184122"></a><a name="p25669989184122"></a><strong id="b9372723144"><a name="b9372723144"></a><a name="b9372723144"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54%" id="mcps1.2.4.1.2"><p id="p66003208184122"><a name="p66003208184122"></a><a name="p66003208184122"></a><strong id="b9046885193651"><a name="b9046885193651"></a><a name="b9046885193651"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.3"><p id="p44659603184122"><a name="p44659603184122"></a><a name="p44659603184122"></a><strong id="b61709088193651"><a name="b61709088193651"></a><a name="b61709088193651"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3253628418410"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p9051947184122"><a name="p9051947184122"></a><a name="p9051947184122"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p62119074184122"><a name="p62119074184122"></a><a name="p62119074184122"></a>Specifies the listener name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p59487507161644"><a name="p59487507161644"></a><a name="p59487507161644"></a>listener-ssgu</p>
    </td>
    </tr>
    <tr id="row66795703161723"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p55255176161725"><a name="p55255176161725"></a><a name="p55255176161725"></a>Frontend Protocol/Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p566915862411"><a name="p566915862411"></a><a name="p566915862411"></a>Specifies the protocol and port the load balancer uses to receive requests from clients and forward the requests to backend servers. The port numbers range from 1 to 65535.</p>
    <p id="p60247126141642"><a name="p60247126141642"></a><a name="p60247126141642"></a>Public network load balancers support the following protocols:</p>
    <a name="ul64785515141838"></a><a name="ul64785515141838"></a><ul id="ul64785515141838"><li>HTTP</li><li>TCP</li><li>HTTPS</li><li>UDP</li><li>SSL</li></ul>
    <p id="p56845019104911"><a name="p56845019104911"></a><a name="p56845019104911"></a>Private network load balancers support the following protocols:</p>
    <a name="ul59199498104954"></a><a name="ul59199498104954"></a><ul id="ul59199498104954"><li>HTTP</li><li>TCP</li><li>HTTPS</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p7129598161725"><a name="p7129598161725"></a><a name="p7129598161725"></a>TCP/80</p>
    <p id="p49979242124539"><a name="p49979242124539"></a><a name="p49979242124539"></a>UDP/80</p>
    <p id="p34532864101423"><a name="p34532864101423"></a><a name="p34532864101423"></a>HTTP/80</p>
    <p id="p86058693432"><a name="p86058693432"></a><a name="p86058693432"></a>HTTPS/443</p>
    <p id="p29201162155524"><a name="p29201162155524"></a><a name="p29201162155524"></a>SSL/443</p>
    </td>
    </tr>
    <tr id="row49179263162422"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p39960184162422"><a name="p39960184162422"></a><a name="p39960184162422"></a>Backend Protocol/Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p15549454162422"><a name="p15549454162422"></a><a name="p15549454162422"></a>Specifies the protocol used by backend servers to receive requests. The port numbers range from 1 to 65535.</p>
    <a name="ul115418117206"></a><a name="ul115418117206"></a><ul id="ul115418117206"><li>TCP: layer-4 load balancing. When <strong id="b842352706144454"><a name="b842352706144454"></a><a name="b842352706144454"></a>Frontend Protocol</strong> is set to <strong id="b84235270614451"><a name="b84235270614451"></a><a name="b84235270614451"></a>SSL</strong>, <strong id="b84235270614457"><a name="b84235270614457"></a><a name="b84235270614457"></a>Backend Protocol</strong> is <strong id="b842352706144511"><a name="b842352706144511"></a><a name="b842352706144511"></a>TCP</strong> by default.</li><li>UDP: layer-4 load balancing. When <strong id="b589306666"><a name="b589306666"></a><a name="b589306666"></a>Frontend Protocol</strong> is set to <strong id="b1393199421"><a name="b1393199421"></a><a name="b1393199421"></a>UDP</strong>, <strong id="b1471478617"><a name="b1471478617"></a><a name="b1471478617"></a>Backend Protocol</strong> is <strong id="b2036138733"><a name="b2036138733"></a><a name="b2036138733"></a>UDP</strong> by default.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p66231138124610"><a name="p66231138124610"></a><a name="p66231138124610"></a>TCP/22</p>
    </td>
    </tr>
    <tr id="row62337098162422"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p24162975162422"><a name="p24162975162422"></a><a name="p24162975162422"></a>Load Balancing Algorithm</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p11043993162422"><a name="p11043993162422"></a><a name="p11043993162422"></a>Specifies the algorithm the load balancer uses to distribute traffic.</p>
    <a name="ul5968188218551"></a><a name="ul5968188218551"></a><ul id="ul5968188218551"><li><strong id="en-us_topic_0118840331_b842352706102822"><a name="en-us_topic_0118840331_b842352706102822"></a><a name="en-us_topic_0118840331_b842352706102822"></a>Round robin</strong>: New connection requests are distributed sequentially across all ECSs, so that request workload is evenly shared.</li><li><strong id="en-us_topic_0118840331_b842352706103735"><a name="en-us_topic_0118840331_b842352706103735"></a><a name="en-us_topic_0118840331_b842352706103735"></a>Least connections</strong>: New connection requests are forwarded to the ECS processing the least number of connections at that time.</li><li><strong id="en-us_topic_0118840331_b84235270616237"><a name="en-us_topic_0118840331_b84235270616237"></a><a name="en-us_topic_0118840331_b84235270616237"></a>Source IP hash</strong>: The source IP address of the request is input into a hash algorithm, and the resulting hash is used to identify an ECS in the static fragment table.</li></ul>
    <div class="note" id="note449753855814"><a name="note449753855814"></a><a name="note449753855814"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p12497163811587"><a name="p12497163811587"></a><a name="p12497163811587"></a>Choose an appropriate algorithm based on your requirement to distribute requests and improve load balancing capabilities.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p22148268162422"><a name="p22148268162422"></a><a name="p22148268162422"></a>Round robin</p>
    </td>
    </tr>
    <tr id="row6077438093536"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2377775393536"><a name="p2377775393536"></a><a name="p2377775393536"></a>Default Certificate</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p4694985993536"><a name="p4694985993536"></a><a name="p4694985993536"></a>Specifies the certificate used by an HTTPS load balancer.</p>
    <p id="p4904405162422"><a name="p4904405162422"></a><a name="p4904405162422"></a>You can select an existing certificate or create one.</p>
    <p id="p833794293717"><a name="p833794293717"></a><a name="p833794293717"></a>This parameter is available only when HTTPS is used as the frontend protocol.</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p4484222593536"><a name="p4484222593536"></a><a name="p4484222593536"></a>N/A</p>
    </td>
    </tr>
    <tr id="row7501782152651"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p50902905152739"><a name="p50902905152739"></a><a name="p50902905152739"></a>Enable SNI</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p29494611152739"><a name="p29494611152739"></a><a name="p29494611152739"></a>Specifies whether to enable SNI when the frontend protocol is HTTPS.</p>
    <p id="p64124909152739"><a name="p64124909152739"></a><a name="p64124909152739"></a>SNI is an extension to Transport Layer Security (TLS) and is used to resolve the issue that a server uses multiple domain names and certificates. This feature allows the client to submit the domain name information while sending an SSL handshake request. Once receiving the request, the load balancer queries the right certificate based on the domain name and returns it to the client. If no certificate is found, the load balancer will return a default certificate.</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p26735145152739"><a name="p26735145152739"></a><a name="p26735145152739"></a>N/A</p>
    </td>
    </tr>
    <tr id="row18107119152656"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p28350476152739"><a name="p28350476152739"></a><a name="p28350476152739"></a>SNI Certificate</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p14687240152739"><a name="p14687240152739"></a><a name="p14687240152739"></a>Specifies the certificate associated with the domain name when the frontend protocol is HTTPS and SNI is enabled.</p>
    <p id="p65076304152739"><a name="p65076304152739"></a><a name="p65076304152739"></a>You can select an existing certificate or create one.</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p61767758152739"><a name="p61767758152739"></a><a name="p61767758152739"></a>N/A</p>
    </td>
    </tr>
    <tr id="row46636939152656"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p65757227152739"><a name="p65757227152739"></a><a name="p65757227152739"></a>SSL Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p24735162152739"><a name="p24735162152739"></a><a name="p24735162152739"></a>Specifies the encryption protocol used by an HTTPS load balancer. This parameter is used to enable a specified encryption protocol. The following options are available:</p>
    <a name="ul57391130152739"></a><a name="ul57391130152739"></a><ul id="ul57391130152739"><li><strong id="b139748193383"><a name="b139748193383"></a><a name="b139748193383"></a>TLSv1.2</strong></li><li><strong id="b1092419914381"><a name="b1092419914381"></a><a name="b1092419914381"></a>TLSv1.2 TLSv1.1 TLSv1</strong></li></ul>
    <p id="p29312012152739"><a name="p29312012152739"></a><a name="p29312012152739"></a>This parameter is available only when HTTPS is used as the frontend protocol.</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p27837997152739"><a name="p27837997152739"></a><a name="p27837997152739"></a>TLSv1.2</p>
    </td>
    </tr>
    <tr id="row52414897152722"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p27023193152739"><a name="p27023193152739"></a><a name="p27023193152739"></a>SSL Cipher</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p41395063152739"><a name="p41395063152739"></a><a name="p41395063152739"></a>Specifies the cipher suite used by an HTTPS load balancer. The following options are available:</p>
    <a name="ul64665817152739"></a><a name="ul64665817152739"></a><ul id="ul64665817152739"><li><strong id="b764716253385"><a name="b764716253385"></a><a name="b764716253385"></a>Default Cipher</strong></li><li><strong id="b6369438114837"><a name="b6369438114837"></a><a name="b6369438114837"></a>Extended Cipher</strong></li><li><strong id="b6645293914841"><a name="b6645293914841"></a><a name="b6645293914841"></a>Strict Cipher</strong></li></ul>
    <p id="p10192267152739"><a name="p10192267152739"></a><a name="p10192267152739"></a>This parameter is available only when HTTPS is used as the frontend protocol. <strong id="b84235270619212"><a name="b84235270619212"></a><a name="b84235270619212"></a>Extended Cipher</strong> is the only available choice when <strong id="b842352706192026"><a name="b842352706192026"></a><a name="b842352706192026"></a>SSL Protocol</strong> is set to <strong id="b842352706192049"><a name="b842352706192049"></a><a name="b842352706192049"></a>TLSv1.2 TLSv1.1 TLSv1</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p48188037152739"><a name="p48188037152739"></a><a name="p48188037152739"></a>Default Cipher</p>
    </td>
    </tr>
    <tr id="row38569529152051"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p37941618152117"><a name="p37941618152117"></a><a name="p37941618152117"></a>Sticky Session</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p53372194152117"><a name="p53372194152117"></a><a name="p53372194152117"></a>Specifies whether to enable the sticky session feature.</p>
    <p id="p10587703152117"><a name="p10587703152117"></a><a name="p10587703152117"></a>After this feature is enabled, all requests from a client during one session are sent to the same backend server.</p>
    <div class="note" id="note586599751148"><a name="note586599751148"></a><a name="note586599751148"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p581777271148"><a name="p581777271148"></a><a name="p581777271148"></a>This feature is supported only when <strong id="b842352706144645"><a name="b842352706144645"></a><a name="b842352706144645"></a>Load Balancing Algorithm</strong> is set to <strong id="b84235270614472"><a name="b84235270614472"></a><a name="b84235270614472"></a>Round robin</strong>.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p52297615152117"><a name="p52297615152117"></a><a name="p52297615152117"></a>N/A</p>
    </td>
    </tr>
    <tr id="row38165688152018"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p7946880152018"><a name="p7946880152018"></a><a name="p7946880152018"></a>Stickiness Duration (min)</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p15559793153157"><a name="p15559793153157"></a><a name="p15559793153157"></a>Specifies the duration that sticky sessions are maintained in minutes. The value ranges from <strong id="b104814561069"><a name="b104814561069"></a><a name="b104814561069"></a>1</strong> to <strong id="b17493561663"><a name="b17493561663"></a><a name="b17493561663"></a>1440</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p63006969152018"><a name="p63006969152018"></a><a name="p63006969152018"></a>5</p>
    </td>
    </tr>
    <tr id="row1131412618410"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1316186194114"><a name="p1316186194114"></a><a name="p1316186194114"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p43164694115"><a name="p43164694115"></a><a name="p43164694115"></a>Provides supplementary information about the listener.</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p1931696104111"><a name="p1931696104111"></a><a name="p1931696104111"></a>N/A</p>
    </td>
    </tr>
    <tr id="row37894296162422"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p5504344162422"><a name="p5504344162422"></a><a name="p5504344162422"></a>Health Check Protocol/Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p43198726162422"><a name="p43198726162422"></a><a name="p43198726162422"></a>Specifies the protocol and port used for performing health checks on backend servers. The port numbers range from 1 to 65535.</p>
    <div class="note" id="note9781344114112"><a name="note9781344114112"></a><a name="note9781344114112"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p20923240114112"><a name="p20923240114112"></a><a name="p20923240114112"></a>When UDP is used for health checks, security group rules of backend servers must allow access using ICMP.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p9435957162422"><a name="p9435957162422"></a><a name="p9435957162422"></a>HTTP/80</p>
    </td>
    </tr>
    <tr id="row2064894118410"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p32956516184122"><a name="p32956516184122"></a><a name="p32956516184122"></a>Interval (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p25870774163512"><a name="p25870774163512"></a><a name="p25870774163512"></a>Specifies the maximum time between health checks in the unit of second.</p>
    <p id="p17123758558"><a name="p17123758558"></a><a name="p17123758558"></a>The value ranges from <strong id="b1528002713718"><a name="b1528002713718"></a><a name="b1528002713718"></a>1</strong> to <strong id="b728011275717"><a name="b728011275717"></a><a name="b728011275717"></a>5</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p32682136163516"><a name="p32682136163516"></a><a name="p32682136163516"></a>5</p>
    </td>
    </tr>
    <tr id="row577303118410"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p43486880184122"><a name="p43486880184122"></a><a name="p43486880184122"></a>Timeout (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p6084546163512"><a name="p6084546163512"></a><a name="p6084546163512"></a>Specifies the maximum time required for waiting for a response from the health check in the unit of second.</p>
    <p id="p333347163818"><a name="p333347163818"></a><a name="p333347163818"></a>The value ranges from <strong id="b459193410713"><a name="b459193410713"></a><a name="b459193410713"></a>1</strong> to <strong id="b12592203417717"><a name="b12592203417717"></a><a name="b12592203417717"></a>50</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p20753786163516"><a name="p20753786163516"></a><a name="p20753786163516"></a>10</p>
    </td>
    </tr>
    <tr id="row1853746318410"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p61652718184122"><a name="p61652718184122"></a><a name="p61652718184122"></a>Healthy Threshold</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p58496162163512"><a name="p58496162163512"></a><a name="p58496162163512"></a>Specifies the number of consecutive health checks necessary for a backend server to be considered healthy. The value ranges from <strong id="b6640649973"><a name="b6640649973"></a><a name="b6640649973"></a>1</strong> to <strong id="b1838375215715"><a name="b1838375215715"></a><a name="b1838375215715"></a>10</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p7746215163516"><a name="p7746215163516"></a><a name="p7746215163516"></a>3</p>
    </td>
    </tr>
    <tr id="row51204614184116"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p53302206184122"><a name="p53302206184122"></a><a name="p53302206184122"></a>Unhealthy Threshold</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p37642080163512"><a name="p37642080163512"></a><a name="p37642080163512"></a>Specifies the number of consecutive health checks necessary for a backend server to be considered unhealthy. The value ranges from <strong id="b580220581179"><a name="b580220581179"></a><a name="b580220581179"></a>1</strong> to <strong id="b18803058973"><a name="b18803058973"></a><a name="b18803058973"></a>10</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p32899075163516"><a name="p32899075163516"></a><a name="p32899075163516"></a>3</p>
    </td>
    </tr>
    <tr id="row30656460163438"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p7472684163438"><a name="p7472684163438"></a><a name="p7472684163438"></a>Check Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.4.1.2 "><p id="p1307686163438"><a name="p1307686163438"></a><a name="p1307686163438"></a>Specifies the health check URL, which is the destination on backend servers for health checks. This parameter is available only when <strong id="b7713321483"><a name="b7713321483"></a><a name="b7713321483"></a>Health Check Protocol</strong> is set to <strong id="b7714527820"><a name="b7714527820"></a><a name="b7714527820"></a>HTTP</strong>. The value can contain 1 to 80 characters.</p>
    <div class="note" id="note610554891062"><a name="note610554891062"></a><a name="note610554891062"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p126284931062"><a name="p126284931062"></a><a name="p126284931062"></a>The path can contain only letters, digits, and the following special characters: -/.%?#&amp;_=</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.3 "><p id="p38813732163438"><a name="p38813732163438"></a><a name="p38813732163438"></a>/test.html</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **OK**.

