# Backend ECS \(Enhanced Load Balancer\)<a name="en-us_topic_0052569729"></a>

## Scenarios<a name="section2632564716543"></a>

This section provides operations for you to add backend ECSs to a load balancer or remove ECSs from a load balancer when you do not want to use them.

## Add Backend ECSs<a name="section34413097203352"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0091131338.png)  and select the desired region and project.
3.  Under  **Network**, click **Elastic Load Balance**.
4.  On the  **Elastic Load Balance**  page, locate the row that contains the target load balancer and click its name.
5.  Add Backend ECSs

    Click  **Backend ECS Groups**, locate the row that contains the target ECS group, and click **More** \> **Add Backend ECS** in the **Operation**  column.

6.  Click  **OK**.

## Remove Backend ECSs<a name="section4570707083236"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0108914826.png)  and select the desired region and project.
3.  Under  **Network**, click **Elastic Load Balance**.
4.  On the  **Elastic Load Balance**  page, locate the row that contains the target load balancer and click its name.
5.  Select the backend ECSs to be removed.

    Click  **Backend ECS Groups** and locate the target ECS group. Click the number in the **Backend ECSs** column. In the displayed **Backend ECS**  dialog box, select the ECSs.

6.  To remove a single backend ECS, locate the row that contains the target ECS and click  **Remove** in the **Operation** column. To remove multiple backend ECSs, select all ECSs to be removed and click **Remove**  above the ECS list.
7.  In the displayed  **Remove Backend ECS** dialog box, click **OK**.

## Add a Backend ECS Group<a name="section48256848192138"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0108916759.png)  and select the desired region and project.
3.  Under  **Network**, click **Elastic Load Balance**.
4.  On the  **Elastic Load Balance**  page, locate the row that contains the target load balancer and click its name.
5.  In the  **Backend ECS Groups** area, click **Add Backend ECS Group**.
6.  In the  **Add Backend ECS Group**  dialog box, specify the parameters.

    **Table  1**  Backend ECS group parameters

    <a name="table13386555204145"></a><table><thead align="left"><tr id="row65767688204145"><th class="cellrowborder" valign="top" width="15.790000000000001%" id="mcps1.2.5.1.1"><p id="p28916226204145"><a name="p28916226204145"></a><a name="p28916226204145"></a><strong id="b842352706154048"><a name="b842352706154048"></a><a name="b842352706154048"></a>Item</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.919999999999998%" id="mcps1.2.5.1.2"><p id="p60513007204145"><a name="p60513007204145"></a><a name="p60513007204145"></a><strong id="b842352706114331"><a name="b842352706114331"></a><a name="b842352706114331"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.290000000000006%" id="mcps1.2.5.1.3"><p id="p2606524204145"><a name="p2606524204145"></a><a name="p2606524204145"></a><strong id="b8423527061772"><a name="b8423527061772"></a><a name="b8423527061772"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p9801873204145"><a name="p9801873204145"></a><a name="p9801873204145"></a><strong id="b842352706151735"><a name="b842352706151735"></a><a name="b842352706151735"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55133924204145"><td class="cellrowborder" rowspan="7" valign="top" width="15.790000000000001%" headers="mcps1.2.5.1.1 "><p id="p36662850204145"><a name="p36662850204145"></a><a name="p36662850204145"></a>Backend ECS Group</p>
    <p id="p35166714145822"><a name="p35166714145822"></a><a name="p35166714145822"></a></p>
    </td>
    <td class="cellrowborder" valign="top" width="19.919999999999998%" headers="mcps1.2.5.1.2 "><p id="p16900877204145"><a name="p16900877204145"></a><a name="p16900877204145"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.290000000000006%" headers="mcps1.2.5.1.3 "><p id="p224284220322"><a name="p224284220322"></a><a name="p224284220322"></a>Specifies the name of the backend ECS group.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p2104570020334"><a name="p2104570020334"></a><a name="p2104570020334"></a>pool-6wk8</p>
    </td>
    </tr>
    <tr id="row164924312044"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p142141582044"><a name="p142141582044"></a><a name="p142141582044"></a>Backend Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><a name="ul894972820437"></a><a name="ul894972820437"></a><ul id="ul894972820437"><li id="li5644129220437"><a name="li5644129220437"></a><a name="li5644129220437"></a>HTTP</li><li id="li460855320437"><a name="li460855320437"></a><a name="li460855320437"></a>TCP</li></ul>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p1483444820448"><a name="p1483444820448"></a><a name="p1483444820448"></a>HTTP</p>
    </td>
    </tr>
    <tr id="row3980616204145"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p11473595204145"><a name="p11473595204145"></a><a name="p11473595204145"></a>Load Balancing Algorithm</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p21429387145630"><a name="p21429387145630"></a><a name="p21429387145630"></a>Specifies the algorithm the load balancer uses to distribute traffic.</p>
    <a name="ul7499292145718"></a><a name="ul7499292145718"></a><ul id="ul7499292145718"><li id="li384769145718"><a name="li384769145718"></a><a name="li384769145718"></a><strong id="b842352706102822"><a name="b842352706102822"></a><a name="b842352706102822"></a>Weighted round robin</strong>: Connection requests are forwarded to backend ECSs in sequence, and ECSs with higher weights receive more requests.</li><li id="li3462929145718"><a name="li3462929145718"></a><a name="li3462929145718"></a><strong id="b842352706102829"><a name="b842352706102829"></a><a name="b842352706102829"></a>Weighted least connections</strong>: In addition to the weight assigned to each backend ECS, the number of connections processed by each ECS is also considered. New connection requests are forwarded to the ECS processing the least connection requests, and the number of requests handled by this ECS depends on the assigned weight value.</li></ul>
    <a name="ul58646761145630"></a><a name="ul58646761145630"></a><ul id="ul58646761145630"><li id="li5142960145630"><a name="li5142960145630"></a><a name="li5142960145630"></a><strong id="b84235270616237"><a name="b84235270616237"></a><a name="b84235270616237"></a>Source IP hash</strong>: The source IP address of the request is used as the hash key to identify an ECS in the static fragment table.</li></ul>
    <div class="note" id="note46286645145630"><a name="note46286645145630"></a><a name="note46286645145630"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p13926621145630"><a name="p13926621145630"></a><a name="p13926621145630"></a>As access traffic changes, choose the most appropriate algorithm to improve load balancing.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p49222416204145"><a name="p49222416204145"></a><a name="p49222416204145"></a>Weighted round robin</p>
    </td>
    </tr>
    <tr id="row5054851220556"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p86255772062"><a name="p86255772062"></a><a name="p86255772062"></a>Sticky Session</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p709894720556"><a name="p709894720556"></a><a name="p709894720556"></a>If the sticky session feature is enabled, all requests from the same client during one session will be sent to the same backend ECS.</p>
    <div class="note" id="note586599751148"><a name="note586599751148"></a><a name="note586599751148"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p581777271148"><a name="p581777271148"></a><a name="p581777271148"></a>This feature is supported only when <strong id="b842352706144645"><a name="b842352706144645"></a><a name="b842352706144645"></a>Load Balancing Algorithm</strong>&nbsp;is set to&nbsp;<strong id="b84235270614472"><a name="b84235270614472"></a><a name="b84235270614472"></a>Round robin</strong>.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p3814384320556"><a name="p3814384320556"></a><a name="p3814384320556"></a>N/A</p>
    </td>
    </tr>
    <tr id="row40348565204145"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p49580487204145"><a name="p49580487204145"></a><a name="p49580487204145"></a>Sticky Session Type</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><a name="ul5771460114575"></a><a name="ul5771460114575"></a><ul id="ul5771460114575"><li id="li4966936614575"><a name="li4966936614575"></a><a name="li4966936614575"></a><strong>Source IP address</strong>: The source IP address of the request is used as the hash key to identify an ECS in the static fragment table.</li><li id="li4437111414575"><a name="li4437111414575"></a><a name="li4437111414575"></a><strong id="b842352706162813"><a name="b842352706162813"></a><a name="b842352706162813"></a>HTTP cookie</strong>: The load balancer generates a cookie after it receives a request from a client. All the subsequent requests with the cookie are distributed to the same backend ECS.</li><li id="li6379571014575"><a name="li6379571014575"></a><a name="li6379571014575"></a><strong id="b84235270613618"><a name="b84235270613618"></a><a name="b84235270613618"></a>App cookie</strong>: This type of sticky session relies on backend applications. All requests with the cookie generated by backend applications are distributed to the same backend ECS.</li></ul>
    <div class="note" id="note3729048314575"><a name="note3729048314575"></a><a name="note3729048314575"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p7003514575"><a name="p7003514575"></a><a name="p7003514575"></a><strong id="b44249155162219"><a name="b44249155162219"></a><a name="b44249155162219"></a>Source IP address</strong>&nbsp;is the only choice available when TCP is used as the frontend protocol. If HTTP or HTTPS is used as the frontend protocol, the sticky session type can be&nbsp;<strong id="b842352706221152"><a name="b842352706221152"></a><a name="b842352706221152"></a>HTTP cookie</strong>&nbsp;or&nbsp;<strong id="b842352706221155"><a name="b842352706221155"></a><a name="b842352706221155"></a>App cookie</strong>. Choose an appropriate sticky session type to better distribute access traffic and improve load balancing.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p20915307204145"><a name="p20915307204145"></a><a name="p20915307204145"></a>Source IP address</p>
    </td>
    </tr>
    <tr id="row5692576920440"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p31970301145835"><a name="p31970301145835"></a><a name="p31970301145835"></a>Cookie Name</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p40825260145835"><a name="p40825260145835"></a><a name="p40825260145835"></a>Specifies the cookie name. When <strong id="b84235270617853"><a name="b84235270617853"></a><a name="b84235270617853"></a>App cookie</strong> is selected, you need to enter a cookie name.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p4040038720440"><a name="p4040038720440"></a><a name="p4040038720440"></a>cookie1223</p>
    </td>
    </tr>
    <tr id="row26277034145822"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p40858067145837"><a name="p40858067145837"></a><a name="p40858067145837"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p21169113145837"><a name="p21169113145837"></a><a name="p21169113145837"></a>Provides supplementary information about the backend ECS group.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 ">&nbsp;&nbsp;</td>
    </tr>
    <tr id="row219072620440"><td class="cellrowborder" rowspan="6" valign="top" width="15.790000000000001%" headers="mcps1.2.5.1.1 "><p id="p1971653720440"><a name="p1971653720440"></a><a name="p1971653720440"></a>Health check</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.919999999999998%" headers="mcps1.2.5.1.2 "><p id="p5353569020440"><a name="p5353569020440"></a><a name="p5353569020440"></a>Health Check Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.290000000000006%" headers="mcps1.2.5.1.3 "><p id="p544931821528"><a name="p544931821528"></a><a name="p544931821528"></a>Specifies the health check protocol. You can use either TCP or HTTP. Once you have selected a specific protocol, you cannot change it.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p144589691528"><a name="p144589691528"></a><a name="p144589691528"></a>HTTP</p>
    </td>
    </tr>
    <tr id="row0925349133116"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 ">&nbsp;</td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 ">&nbsp;</td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 ">&nbsp;</td>
    </tr>
    <tr id="row5399119120440"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p3378432320440"><a name="p3378432320440"></a><a name="p3378432320440"></a>Interval</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p44971531528"><a name="p44971531528"></a><a name="p44971531528"></a>Specifies the maximum amount of time between health checks in the unit of second.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p287250801528"><a name="p287250801528"></a><a name="p287250801528"></a>5 seconds</p>
    </td>
    </tr>
    <tr id="row1060927520440"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1664267420440"><a name="p1664267420440"></a><a name="p1664267420440"></a>Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p26183001528"><a name="p26183001528"></a><a name="p26183001528"></a>Specifies the maximum amount of time you need to wait when receiving a response from the health check in the unit of second.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p107557221528"><a name="p107557221528"></a><a name="p107557221528"></a>10 seconds</p>
    </td>
    </tr>
    <tr id="row5446335811145"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p4244991711145"><a name="p4244991711145"></a><a name="p4244991711145"></a>Check Path</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p562931721528"><a name="p562931721528"></a><a name="p562931721528"></a>Specifies the health check path, which is a URL. This parameter is required if <strong id="b842352706111632"><a name="b842352706111632"></a><a name="b842352706111632"></a>Health Check Protocol</strong>&nbsp;is set to&nbsp;<strong id="b842352706111636"><a name="b842352706111636"></a><a name="b842352706111636"></a>HTTP</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p634530741528"><a name="p634530741528"></a><a name="p634530741528"></a>/index.html</p>
    </td>
    </tr>
    <tr id="row25687371161842"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p29859754161842"><a name="p29859754161842"></a><a name="p29859754161842"></a>Maximum Retries</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p2144411516197"><a name="p2144411516197"></a><a name="p2144411516197"></a>Specifies the maximum number of retries for the health check. The value ranges from 1 to 10.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p5925178816197"><a name="p5925178816197"></a><a name="p5925178816197"></a>3</p>
    </td>
    </tr>
    </tbody>
    </table>


## Disable Health Checks<a name="section776541715592"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0121243604.png)  and select the desired region and project.
3.  Under  **Network**, click **Elastic Load Balance**.
4.  On the  **Elastic Load Balance**  page, locate the row that contains the target load balancer and click its name.
5.  Click  **Backend ECS Groups**, locate the row that contains the backend ECS group for which you want to stop the health checks.
6.  Click  **More** in the **Operation**  column.
7.  Select  **Configure Health Check**  from the drop-down list.
8.  In the displayed  **Configure Health Check**  dialog box, disable the health check function.

