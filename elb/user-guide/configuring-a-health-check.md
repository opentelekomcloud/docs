# Configuring a Health Check<a name="EN-US_TOPIC_0164706630"></a>

## Scenarios<a name="section1121010331536"></a>

You can configure a health check when you add a listener. If you have no special requirements, retain the default settings. You can also disable the health check function or change the health check settings.

To change the health check settings of a classic load balancer, locate the row that contains the target listener and click  **Modify**  in the  **Operation**  column.

To configure a health check or change the health check settings of an enhanced load balancer, perform the operations in this topic.

## Procedure<a name="section126005588310"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Click  **Backend Server Groups**, locate the target backend server group, and click its name.
6.  Click  **More**  in the  **Operation**  column.
7.  Select  **Configure Health Check**  from the drop-down list.
8.  In the  **Configure Health Check**  dialog box, enable or disable the health check function. Set the parameters by referring to  [Table 1](#table124201898534).

    **Table  1**  Parameters for configuring a health check

    <a name="table124201898534"></a>
    <table><thead align="left"><tr id="row1641417985317"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p1741415965319"><a name="p1741415965319"></a><a name="p1741415965319"></a><strong id="b898016262017"><a name="b898016262017"></a><a name="b898016262017"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.2"><p id="p134141496538"><a name="p134141496538"></a><a name="p134141496538"></a><strong id="b15852146101315"><a name="b15852146101315"></a><a name="b15852146101315"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.3"><p id="p114141794530"><a name="p114141794530"></a><a name="p114141794530"></a><strong id="b8401841202"><a name="b8401841202"></a><a name="b8401841202"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1941509125312"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p174155905311"><a name="p174155905311"></a><a name="p174155905311"></a>Enable Health Check</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><p id="p15415195533"><a name="p15415195533"></a><a name="p15415195533"></a>Specifies whether to enable health checks.</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="p541519155318"><a name="p541519155318"></a><a name="p541519155318"></a>N/A</p>
    </td>
    </tr>
    <tr id="row44158910530"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p184153920531"><a name="p184153920531"></a><a name="p184153920531"></a>Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><a name="ul1941518935311"></a><a name="ul1941518935311"></a><ul id="ul1941518935311"><li>Specifies the protocol the load balancer uses to perform health checks on backend servers. You can use either TCP or HTTP. A selected protocol cannot be changed.</li><li>If the frontend protocol is UDP, the health check protocol is UDP by default.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="p741518914531"><a name="p741518914531"></a><a name="p741518914531"></a>HTTP</p>
    </td>
    </tr>
    <tr id="row74169955315"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p8415159185317"><a name="p8415159185317"></a><a name="p8415159185317"></a>Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><p id="p0415109125316"><a name="p0415109125316"></a><a name="p0415109125316"></a>Specifies the domain name in the health check request. The domain name consists of digits, letters, hyphens (-), and periods (.), and must start with a digit or letter. This parameter is left blank by default and needs to be set only when the health check protocol is HTTP.</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="p941614910531"><a name="p941614910531"></a><a name="p941614910531"></a>www.elb.com</p>
    </td>
    </tr>
    <tr id="row941639115316"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p154163918539"><a name="p154163918539"></a><a name="p154163918539"></a>Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><p id="p1941659135311"><a name="p1941659135311"></a><a name="p1941659135311"></a>Specifies the port the load balancer uses to perform health checks on backend servers. The port numbers range from 1 to 65535.</p>
    <div class="note" id="note1641616913534"><a name="note1641616913534"></a><a name="note1641616913534"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p14416492538"><a name="p14416492538"></a><a name="p14416492538"></a>This is an optional parameter. If no health check port is specified, the port of each backend server is used for health checks by default.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="p114161199530"><a name="p114161199530"></a><a name="p114161199530"></a>80</p>
    </td>
    </tr>
    <tr id="row641711935319"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p184163913537"><a name="p184163913537"></a><a name="p184163913537"></a>Interval (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><p id="p1941614985312"><a name="p1941614985312"></a><a name="p1941614985312"></a>Specifies the maximum time between health checks in the unit of second.</p>
    <p id="p54161797531"><a name="p54161797531"></a><a name="p54161797531"></a>The value ranges from <strong id="b7952201203"><a name="b7952201203"></a><a name="b7952201203"></a>1</strong> to <strong id="b9961205201"><a name="b9961205201"></a><a name="b9961205201"></a>50</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="p1417209155312"><a name="p1417209155312"></a><a name="p1417209155312"></a>5</p>
    </td>
    </tr>
    <tr id="row541759195312"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p9417179185316"><a name="p9417179185316"></a><a name="p9417179185316"></a>Timeout (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><p id="p7417149135320"><a name="p7417149135320"></a><a name="p7417149135320"></a>Specifies the maximum time required for waiting for a response from the health check in the unit of second. The value ranges from <strong id="b187021821182014"><a name="b187021821182014"></a><a name="b187021821182014"></a>1</strong> to <strong id="b17703112114209"><a name="b17703112114209"></a><a name="b17703112114209"></a>50</strong>.</p>
    <div class="note" id="note193801236164215"><a name="note193801236164215"></a><a name="note193801236164215"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p7380436174211"><a name="p7380436174211"></a><a name="p7380436174211"></a>The timeout must be less than or equal to the interval. Otherwise, the value set for the interval will be used as the timeout.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="p194173975319"><a name="p194173975319"></a><a name="p194173975319"></a>3</p>
    </td>
    </tr>
    <tr id="row541714916532"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p15417394539"><a name="p15417394539"></a><a name="p15417394539"></a>Check Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><p id="p1741712913533"><a name="p1741712913533"></a><a name="p1741712913533"></a>Specifies the health check URL, which is the destination on backend servers for health checks. This parameter is available only when <strong id="b16291122462011"><a name="b16291122462011"></a><a name="b16291122462011"></a>Protocol</strong> is set to <strong id="b3291182462019"><a name="b3291182462019"></a><a name="b3291182462019"></a>HTTP</strong>. The value can contain 1 to 80 characters.</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="p4417119195313"><a name="p4417119195313"></a><a name="p4417119195313"></a>/index.html</p>
    </td>
    </tr>
    <tr id="row1941749175315"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p64172912539"><a name="p64172912539"></a><a name="p64172912539"></a>Maximum Retries</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.2 "><p id="p2041799135312"><a name="p2041799135312"></a><a name="p2041799135312"></a>Specifies the maximum number of health check retries. The value ranges from <strong id="b92049272203"><a name="b92049272203"></a><a name="b92049272203"></a>1</strong> to <strong id="b1205152716209"><a name="b1205152716209"></a><a name="b1205152716209"></a>10</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.3 "><p id="p44171975318"><a name="p44171975318"></a><a name="p44171975318"></a>3</p>
    </td>
    </tr>
    </tbody>
    </table>

9.  Click  **OK**.

