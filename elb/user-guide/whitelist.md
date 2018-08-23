# Whitelist<a name="en-us_elb_03_0003"></a>

You can add a whitelist to specify the IP addresses that can access the listener.

> ![](public_sys-resources/icon-notice.gif) **NOTICE:** 

> Only enhanced load balancers provide this function. Adding the whitelist may cause service risks. Once the whitelist is set, only the IP addresses specified in the whitelist can access the listener.

> If access control is enabled but no whitelist is added, the listener cannot be accessed.

## Add a Whitelist<a name="section9017688174523"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0094007003.png)  and select the desired region and project.
3.  Under  **Network**, click  **Elastic Load Balance**.

1.  On the  **Elastic Load Balance**  page, locate the row that contains the target load balancer and click its name.
2.  In the  **Listeners**  area, locate the row that contains the target listener, click  **More**  in the  **Operation**  column, and select  **Configure Access Control**  from the drop-down list. In the displayed  **Configure Access Control**  dialog box, enable  **Access Control**  and enter the IP addresses as prompted.

    **Figure  1**  Configuring access control<a name="fig3436377817590"></a>
    ![](figures/configuring-access-control.jpg "Configuring access control")

    **Table  1**  Parameter description

    <a name="table3263104318541"></a><table><thead align="left"><tr id="row6556870018541"><th class="cellrowborder" valign="top" width="22.81%" id="mcps1.2.4.1.1"><p id="p60775331862"><a name="p60775331862"></a><a name="p60775331862"></a><strong id="b842352706114331"><a name="b842352706114331"></a><a name="b842352706114331"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.129999999999995%" id="mcps1.2.4.1.2"><p id="p5449227018541"><a name="p5449227018541"></a><a name="p5449227018541"></a><strong id="b8423527061772"><a name="b8423527061772"></a><a name="b8423527061772"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.06%" id="mcps1.2.4.1.3"><p id="p5179777918541"><a name="p5179777918541"></a><a name="p5179777918541"></a><strong id="b842352706194150"><a name="b842352706194150"></a><a name="b842352706194150"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6352683318541"><td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.1 "><p id="p4539988218541"><a name="p4539988218541"></a><a name="p4539988218541"></a>Access Control</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><a name="ul25916715105429"></a><a name="ul25916715105429"></a><ul id="ul25916715105429"><li id="li1083249618957"><a name="li1083249618957"></a><a name="li1083249618957"></a>If access control is enabled but no whitelist is added, no IP address is allowed to access the listener.</li><li id="li28326823181114"><a name="li28326823181114"></a><a name="li28326823181114"></a>If access control is enabled and the whitelist is added, only IP addresses specified in the whitelist can access the listener.</li></ul>
    <a name="ul32263783105429"></a><a name="ul32263783105429"></a><ul id="ul32263783105429"><li id="li52501725181052"><a name="li52501725181052"></a><a name="li52501725181052"></a>If access control is disabled, the listener can be accessed from any IP address.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p3949107318541"><a name="p3949107318541"></a><a name="p3949107318541"></a>N/A</p>
    </td>
    </tr>
    <tr id="row1987534018541"><td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.1 "><p id="p6639869918541"><a name="p6639869918541"></a><a name="p6639869918541"></a>Whitelist</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.129999999999995%" headers="mcps1.2.4.1.2 "><p id="p39771091184017"><a name="p39771091184017"></a><a name="p39771091184017"></a>Lists the IP addresses or network segments that can access the listener.</p>
    <div class="note" id="note1238160118401"><a name="note1238160118401"></a><a name="note1238160118401"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p58558164184037"><a name="p58558164184037"></a><a name="p58558164184037"></a>A maximum of 300 IP addresses or network segments can be entered. A comma (,) is used to separate every two IP addresses or network segments.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.3 "><p id="p3823315618541"><a name="p3823315618541"></a><a name="p3823315618541"></a>10.168.2.24, 10.168.16.0/24</p>
    </td>
    </tr>
    </tbody>
    </table>

3.  Click  **OK**.

