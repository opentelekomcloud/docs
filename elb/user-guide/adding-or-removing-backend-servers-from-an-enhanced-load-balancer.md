# Adding or Removing Backend Servers from an Enhanced Load Balancer<a name="EN-US_TOPIC_0164706626"></a>

## Scenarios<a name="section2632564716543"></a>

When using ELB, ensure that at least a healthy backend server is in the backend server group associated with your load balancer. If the number of requests increases, you need to add more backend servers.

After a backend server is removed, it cannot receive requests from the load balancer. You can add it back to the backend server group when the traffic goes up again.

If a load balancer is associated with an AS group, instances in the AS group are automatically added to the backend server group of the load balancer. If instances are removed from the AS group, they will be automatically removed from the backend server group.

## Add Backend Servers<a name="section388715404610"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Click  **Backend Server Groups**, locate the target backend server group, and click its name.
6.  In the  **Basic Information**  area, click  **Add**  in the upper left corner of the server list. Select the subnet where the backend servers reside, select the backend servers to be added, and click  **Next**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If a backend server has multiple NICs, you can only select the subnet where the primary NIC resides and use the primary NIC to add the backend server.  

7.  Set the weights of backend ports and, and click  **OK**.
8.  Click  **OK**.

## Remove Backend Servers<a name="section689235434617"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Click  **Backend Server Groups**, locate the target backend server group, and click its name.
6.  In the  **Basic Information**  area, click  **Remove**  in the  **Operation**  column to remove a backend server. To remove multiple backend servers, select all the backend servers to be removed and click  **Remove**  above the server list.
7.  In the displayed dialog box, click  **Yes**.

## Add a Backend Server Group<a name="section27164710517"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Under  **Backend Server Groups**, click  **Add Backend Server Group**.
6.  In the  **Add Backend Server Group**  dialog box, configure the parameters.

    For details about the parameters, see  [Table 1](#en-us_topic_0091131437_table83118104911)  and  [Table 2](#en-us_topic_0091131437_table736610293).

    **Table  1**  Parameters for adding a backend server group

    <a name="en-us_topic_0091131437_table83118104911"></a>
    <table><thead align="left"><tr id="en-us_topic_0091131437_en-us_topic_0091131454_row24119915312"><th class="cellrowborder" valign="top" width="20.48%" id="mcps1.2.4.1.1"><p id="en-us_topic_0091131437_en-us_topic_0091131454_p1341114918533"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1341114918533"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1341114918533"></a><strong id="b18126201013317"><a name="b18126201013317"></a><a name="b18126201013317"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.66%" id="mcps1.2.4.1.2"><p id="en-us_topic_0091131437_en-us_topic_0091131454_p13411119115314"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p13411119115314"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p13411119115314"></a><strong id="b1473341119333"><a name="b1473341119333"></a><a name="b1473341119333"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.86%" id="mcps1.2.4.1.3"><p id="en-us_topic_0091131437_en-us_topic_0091131454_p1441116918537"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1441116918537"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1441116918537"></a><strong id="b125001112123317"><a name="b125001112123317"></a><a name="b125001112123317"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0091131437_en-us_topic_0091131454_row541279125318"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p1741120913539"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1741120913539"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1741120913539"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.66%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p204128965312"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p204128965312"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p204128965312"></a>Specifies the backend server group name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p13412699533"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p13412699533"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p13412699533"></a>server_group-sq4v</p>
    </td>
    </tr>
    <tr id="en-us_topic_0091131437_en-us_topic_0091131454_row64123910531"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p54120975314"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p54120975314"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p54120975314"></a>Backend Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.66%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p1241215910537"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1241215910537"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1241215910537"></a>Specifies the protocol used by backend servers to receive requests.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p841216919534"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p841216919534"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p841216919534"></a>HTTP</p>
    </td>
    </tr>
    <tr id="en-us_topic_0091131437_en-us_topic_0091131454_row184131694530"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p741211985316"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p741211985316"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p741211985316"></a>Load Balancing Algorithm</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.66%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p241213913535"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p241213913535"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p241213913535"></a>Specifies the algorithm the load balancer uses to distribute traffic.</p>
    <a name="en-us_topic_0091131437_en-us_topic_0091131454_ul164121491534"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_ul164121491534"></a><ul id="en-us_topic_0091131437_en-us_topic_0091131454_ul164121491534"><li><strong id="b335892953310"><a name="b335892953310"></a><a name="b335892953310"></a>Weighted round robin</strong>: Requests are routed to different servers based on their weights, which indicate server processing performance. Backend servers with higher weights receive proportionately more requests, whereas equal-weighted servers receive the same number of requests.</li><li><strong id="b17501632183314"><a name="b17501632183314"></a><a name="b17501632183314"></a>Weighted least connections</strong>: The <strong id="b1581114953314"><a name="b1581114953314"></a><a name="b1581114953314"></a>Least connections</strong> algorithm uses the number of active connections to each backend server to make its load balancing decision. Building on <strong id="b1558214983318"><a name="b1558214983318"></a><a name="b1558214983318"></a>Least connections</strong>, the <strong id="b1158284983319"><a name="b1158284983319"></a><a name="b1158284983319"></a>Weighted least connections</strong> algorithm assigns a weight to each server based on their processing capability.</li><li><strong id="b06301352734"><a name="b06301352734"></a><a name="b06301352734"></a>Source IP hash</strong>: The source IP address of the request is input into a hash algorithm, and the resulting hash is used to identify a server in the static fragment table.</li></ul>
    <div class="note" id="en-us_topic_0091131437_en-us_topic_0091131454_note341217917533"><a name="en-us_topic_0091131437_en-us_topic_0091131454_note341217917533"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_note341217917533"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0091131437_en-us_topic_0091131454_p9412129185318"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p9412129185318"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p9412129185318"></a>Choose an appropriate algorithm based on your requirement to distribute requests and improve load balancing capabilities.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p1541319915534"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1541319915534"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1541319915534"></a>Weighted round robin</p>
    </td>
    </tr>
    <tr id="en-us_topic_0091131437_en-us_topic_0091131454_row11413149115315"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p184131091534"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p184131091534"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p184131091534"></a>Sticky Session</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.66%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p1441319955312"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1441319955312"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1441319955312"></a>If the sticky session feature is enabled, all requests from the same client during one session are sent to the same backend server.</p>
    <div class="note" id="en-us_topic_0091131437_en-us_topic_0091131454_note941399195314"><a name="en-us_topic_0091131437_en-us_topic_0091131454_note941399195314"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_note941399195314"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0091131437_en-us_topic_0091131454_p841318975316"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p841318975316"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p841318975316"></a>For HTTP and HTTPS listeners, enabling or disabling sticky sessions may cause few seconds of service interruption.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p14131975315"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p14131975315"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p14131975315"></a>N/A</p>
    </td>
    </tr>
    <tr id="en-us_topic_0091131437_en-us_topic_0091131454_row84141394533"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p1741329145317"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1741329145317"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1741329145317"></a>Sticky Session Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.66%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p154132095532"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p154132095532"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p154132095532"></a>Specifies the sticky session type. The following options are available:</p>
    <a name="en-us_topic_0091131437_en-us_topic_0091131454_ul1241312925312"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_ul1241312925312"></a><ul id="en-us_topic_0091131437_en-us_topic_0091131454_ul1241312925312"><li><strong id="b48271443310"><a name="b48271443310"></a><a name="b48271443310"></a>Source IP address</strong>: Requests with the same source IP address are routed to the same backend server for processing.</li><li><strong id="b1543710281349"><a name="b1543710281349"></a><a name="b1543710281349"></a>Load balancer cookie</strong>: The load balancer generates a cookie after receiving a request from the client. All subsequent requests with the cookie are routed to the same backend server for processing.</li><li><strong id="b102181430153419"><a name="b102181430153419"></a><a name="b102181430153419"></a>Application cookie</strong>: This method relies on backend applications. The application on the first backend server that receives the request generates a cookie. All subsequent requests that contain the cookie will be processed by the same backend server.</li></ul>
    <div class="note" id="en-us_topic_0091131437_en-us_topic_0091131454_note184149920533"><a name="en-us_topic_0091131437_en-us_topic_0091131454_note184149920533"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_note184149920533"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul67056312135"></a><a name="ul67056312135"></a><ul id="ul67056312135"><li><strong id="b19285193512344"><a name="b19285193512344"></a><a name="b19285193512344"></a>Source IP address</strong> is the only choice available when TCP is used as the frontend protocol. If <strong id="b34571736133419"><a name="b34571736133419"></a><a name="b34571736133419"></a>HTTP</strong> or <strong id="b8458436193416"><a name="b8458436193416"></a><a name="b8458436193416"></a>HTTPS</strong> is selected as the frontend protocol, the sticky session type can be <strong id="b44581436203416"><a name="b44581436203416"></a><a name="b44581436203416"></a>Load balancer cookie</strong> or <strong id="b1345911364340"><a name="b1345911364340"></a><a name="b1345911364340"></a>Application cookie</strong>. Choose an appropriate sticky session type to better distribute requests and improve load balancing.</li><li>Sticky sessions at Layer 4 are maintained for one minute, while sticky sessions at Layer 7 are maintained for 24 hours.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p941410911535"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p941410911535"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p941410911535"></a>App cookie</p>
    </td>
    </tr>
    <tr id="en-us_topic_0091131437_en-us_topic_0091131454_row17414596534"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p14147913531"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p14147913531"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p14147913531"></a>Cookie Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.66%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p10414159125310"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p10414159125310"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p10414159125310"></a>Specifies the cookie name. When <strong id="b2246104213349"><a name="b2246104213349"></a><a name="b2246104213349"></a>Application cookie</strong> is selected, you need to enter a cookie name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p194143935314"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p194143935314"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p194143935314"></a>cookieName-qsps</p>
    </td>
    </tr>
    <tr id="en-us_topic_0091131437_en-us_topic_0091131454_row541414919539"><td class="cellrowborder" valign="top" width="20.48%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p19414798530"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p19414798530"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p19414798530"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.66%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p1141469115313"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1141469115313"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1141469115313"></a>Provides supplementary information about the backend server group.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p114141696531"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p114141696531"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p114141696531"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Parameters for configuring a health check

    <a name="en-us_topic_0091131437_table736610293"></a>
    <table><thead align="left"><tr id="en-us_topic_0091131437_en-us_topic_0091131454_row1641417985317"><th class="cellrowborder" valign="top" width="20.849999999999998%" id="mcps1.2.4.1.1"><p id="en-us_topic_0091131437_en-us_topic_0091131454_p1741415965319"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1741415965319"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1741415965319"></a><strong id="b836215173514"><a name="b836215173514"></a><a name="b836215173514"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.29%" id="mcps1.2.4.1.2"><p id="en-us_topic_0091131437_en-us_topic_0091131454_p134141496538"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p134141496538"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p134141496538"></a><strong id="b15533564352"><a name="b15533564352"></a><a name="b15533564352"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.86%" id="mcps1.2.4.1.3"><p id="en-us_topic_0091131437_en-us_topic_0091131454_p114141794530"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p114141794530"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p114141794530"></a><strong id="b537119723518"><a name="b537119723518"></a><a name="b537119723518"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0091131437_en-us_topic_0091131454_row1941509125312"><td class="cellrowborder" valign="top" width="20.849999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p174155905311"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p174155905311"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p174155905311"></a>Enable Health Check</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.29%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p15415195533"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p15415195533"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p15415195533"></a>Specifies whether to enable health checks.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p541519155318"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p541519155318"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p541519155318"></a>N/A</p>
    </td>
    </tr>
    <tr id="en-us_topic_0091131437_en-us_topic_0091131454_row44158910530"><td class="cellrowborder" valign="top" width="20.849999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p184153920531"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p184153920531"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p184153920531"></a>Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.29%" headers="mcps1.2.4.1.2 "><p id="p18031258175016"><a name="p18031258175016"></a><a name="p18031258175016"></a>Specifies the protocol the load balancer uses to perform health checks on backend servers.</p>
    <a name="en-us_topic_0091131437_en-us_topic_0091131454_ul1941518935311"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_ul1941518935311"></a><ul id="en-us_topic_0091131437_en-us_topic_0091131454_ul1941518935311"><li>If the frontend protocol is TCP, HTTP or HTTPS, the health check protocol can be TCP or HTTP. The health check protocol cannot be changed once it is set.</li><li>If the frontend protocol is UDP, the health check protocol is UDP by default.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p741518914531"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p741518914531"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p741518914531"></a>HTTP</p>
    </td>
    </tr>
    <tr id="en-us_topic_0091131437_en-us_topic_0091131454_row74169955315"><td class="cellrowborder" valign="top" width="20.849999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p8415159185317"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p8415159185317"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p8415159185317"></a>Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.29%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p0415109125316"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p0415109125316"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p0415109125316"></a>Specifies the domain name in the health check request. The domain name consists of digits, letters, hyphens (-), and periods (.), and must start with a digit or letter. This parameter is left blank by default and needs to be set only when the health check protocol is HTTP.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p941614910531"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p941614910531"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p941614910531"></a>www.elb.com</p>
    </td>
    </tr>
    <tr id="en-us_topic_0091131437_en-us_topic_0091131454_row941639115316"><td class="cellrowborder" valign="top" width="20.849999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p154163918539"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p154163918539"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p154163918539"></a>Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.29%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p1941659135311"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1941659135311"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1941659135311"></a>Specifies the port the load balancer uses to perform health checks on backend servers. This is an optional parameter. The port numbers range from 1 to 65535.</p>
    <div class="note" id="en-us_topic_0091131437_en-us_topic_0091131454_note1641616913534"><a name="en-us_topic_0091131437_en-us_topic_0091131454_note1641616913534"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_note1641616913534"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0091131437_en-us_topic_0091131454_p14416492538"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p14416492538"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p14416492538"></a>If no port is specified, the port of each backend server is used for health checks by default.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p114161199530"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p114161199530"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p114161199530"></a>80</p>
    </td>
    </tr>
    <tr id="en-us_topic_0091131437_en-us_topic_0091131454_row184161396534"><td class="cellrowborder" valign="top" width="20.849999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p24161914533"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p24161914533"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p24161914533"></a>Advanced Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.29%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p04167995319"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p04167995319"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p04167995319"></a>Provides some advanced features. Two options are available, <strong id="b9513120204710"><a name="b9513120204710"></a><a name="b9513120204710"></a>Default</strong> and <strong id="b10514112024720"><a name="b10514112024720"></a><a name="b10514112024720"></a>Custom</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p1416209135317"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1416209135317"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1416209135317"></a>Default</p>
    </td>
    </tr>
    <tr id="en-us_topic_0091131437_en-us_topic_0091131454_row641711935319"><td class="cellrowborder" valign="top" width="20.849999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p184163913537"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p184163913537"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p184163913537"></a>Interval (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.29%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p1941614985312"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1941614985312"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1941614985312"></a>Specifies the maximum time between health checks in the unit of second.</p>
    <p id="en-us_topic_0091131437_en-us_topic_0091131454_p54161797531"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p54161797531"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p54161797531"></a>The value ranges from <strong id="b48734487366"><a name="b48734487366"></a><a name="b48734487366"></a>1</strong> to <strong id="b3873144810369"><a name="b3873144810369"></a><a name="b3873144810369"></a>50</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p1417209155312"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1417209155312"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1417209155312"></a>5</p>
    </td>
    </tr>
    <tr id="en-us_topic_0091131437_en-us_topic_0091131454_row541759195312"><td class="cellrowborder" valign="top" width="20.849999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p9417179185316"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p9417179185316"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p9417179185316"></a>Timeout (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.29%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p7417149135320"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p7417149135320"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p7417149135320"></a>Specifies the maximum time required for waiting for a response from the health check in the unit of second. The value ranges from <strong id="b16793125416361"><a name="b16793125416361"></a><a name="b16793125416361"></a>1</strong> to <strong id="b167941554193618"><a name="b167941554193618"></a><a name="b167941554193618"></a>50</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p194173975319"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p194173975319"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p194173975319"></a>10</p>
    </td>
    </tr>
    <tr id="en-us_topic_0091131437_en-us_topic_0091131454_row541714916532"><td class="cellrowborder" valign="top" width="20.849999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p15417394539"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p15417394539"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p15417394539"></a>Check Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.29%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p1741712913533"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1741712913533"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p1741712913533"></a>Specifies the health check URL, which is the destination on backend servers for health checks. This parameter is available only when <strong id="b152511831145617"><a name="b152511831145617"></a><a name="b152511831145617"></a>Protocol</strong> is set to <strong id="b32521231105620"><a name="b32521231105620"></a><a name="b32521231105620"></a>HTTP</strong>. The value can contain 1 to 80 characters.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p4417119195313"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p4417119195313"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p4417119195313"></a>/index.html</p>
    </td>
    </tr>
    <tr id="en-us_topic_0091131437_en-us_topic_0091131454_row1941749175315"><td class="cellrowborder" valign="top" width="20.849999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p64172912539"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p64172912539"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p64172912539"></a>Maximum Retries</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.29%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p2041799135312"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p2041799135312"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p2041799135312"></a>Specifies the maximum number of health check retries. The value ranges from <strong id="b1832193935617"><a name="b1832193935617"></a><a name="b1832193935617"></a>1</strong> to <strong id="b15322123975619"><a name="b15322123975619"></a><a name="b15322123975619"></a>10</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.86%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0091131437_en-us_topic_0091131454_p44171975318"><a name="en-us_topic_0091131437_en-us_topic_0091131454_p44171975318"></a><a name="en-us_topic_0091131437_en-us_topic_0091131454_p44171975318"></a>3</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

## Modify a Backend Server Group<a name="section54011642158"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.jpg)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Click  **Backend Server Groups**, locate the target backend server group, and click  ![](figures/icon-edit.png)  on the right of its name.
6.  In the displayed dialog box, modify the parameters as needed and click  **OK**.

## Delete a Backend Server Group<a name="section01807511112"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.jpg)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Click  **Backend Server Groups**, locate the target backend server group, and click  ![](figures/icon-delete.png)  on the right of its name.
6.  In the displayed dialog box, click  **Yes**.

