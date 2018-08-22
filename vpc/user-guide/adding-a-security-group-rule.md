# Adding a Security Group Rule<a name="en-us_topic_0030971613"></a>

## Scenarios<a name="en-us_topic_0030969470_s480ea51d8f2542828c323c6c8eb50861"></a>

After a security group is created, it has default rules. You can add new inbound and outbound rules to the security group.

-   Inbound rules control incoming traffic to servers in the security group.
-   Outbound rules control outgoing traffic from servers in the security group.

## Procedure<a name="en-us_topic_0030969470_section2999103814551"></a>

1.  Log in to the management console.
2.  Click  ![](figures/en-us_image_0118621993.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click **Virtual Private Cloud**.
4.  In the navigation pane on the left, click  **Security Group**.
5.  On the  **Security Group** page, locate the target security group and click **Manage Rule** in the **Operation**  column to switch to the page for managing inbound and outbound rules.
6.  On the  **Inbound** tab, click **Add Rule**. In the displayed dialog box, set required parameters to add an inbound rule.

    You can click  **+**  to add more inbound rules.

    **Figure  1**  Add Inbound Rule<a name="en-us_topic_0030969470_fig172301034104912"></a>
    ![](figures/add-inbound-rule.png "Add Inbound Rule")

    **Table  1**  Inbound rule parameter description

    <a name="en-us_topic_0030969470_table532116198213"></a><table><thead align="left"><tr id="en-us_topic_0030969470_row731911191722"><th class="cellrowborder" valign="top" width="28.299999999999997%" id="mcps1.2.4.1.1"><p id="en-us_topic_0030969470_p17319119020"><a name="en-us_topic_0030969470_p17319119020"></a><a name="en-us_topic_0030969470_p17319119020"></a><strong id="en-us_topic_0030969470_b842352706114331"><a name="en-us_topic_0030969470_b842352706114331"></a><a name="en-us_topic_0030969470_b842352706114331"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.7%" id="mcps1.2.4.1.2"><p id="en-us_topic_0030969470_p431911191622"><a name="en-us_topic_0030969470_p431911191622"></a><a name="en-us_topic_0030969470_p431911191622"></a><strong id="en-us_topic_0030969470_b84235270694155"><a name="en-us_topic_0030969470_b84235270694155"></a><a name="en-us_topic_0030969470_b84235270694155"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.3"><p id="en-us_topic_0030969470_p103191119621"><a name="en-us_topic_0030969470_p103191119621"></a><a name="en-us_topic_0030969470_p103191119621"></a><strong id="en-us_topic_0030969470_b8423527069420"><a name="en-us_topic_0030969470_b8423527069420"></a><a name="en-us_topic_0030969470_b8423527069420"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0030969470_row8320419723"><td class="cellrowborder" valign="top" width="28.299999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0030969470_p1432013199214"><a name="en-us_topic_0030969470_p1432013199214"></a><a name="en-us_topic_0030969470_p1432013199214"></a>Protocol/Application</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0030969470_p432017191726"><a name="en-us_topic_0030969470_p432017191726"></a><a name="en-us_topic_0030969470_p432017191726"></a>Specifies the network protocol for which the security group rule takes effect. The value can be <strong id="en-us_topic_0030969470_b84235270613479"><a name="en-us_topic_0030969470_b84235270613479"></a><a name="en-us_topic_0030969470_b84235270613479"></a>TCP</strong>,&nbsp;<strong id="en-us_topic_0030969470_b842352706134713"><a name="en-us_topic_0030969470_b842352706134713"></a><a name="en-us_topic_0030969470_b842352706134713"></a>UDP</strong>,&nbsp;<strong id="en-us_topic_0030969470_b842352706134716"><a name="en-us_topic_0030969470_b842352706134716"></a><a name="en-us_topic_0030969470_b842352706134716"></a>ICMP</strong>, or&nbsp;<strong id="en-us_topic_0030969470_b842352706134721"><a name="en-us_topic_0030969470_b842352706134721"></a><a name="en-us_topic_0030969470_b842352706134721"></a>ANY</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0030969470_p1332014191216"><a name="en-us_topic_0030969470_p1332014191216"></a><a name="en-us_topic_0030969470_p1332014191216"></a>TCP</p>
    </td>
    </tr>
    <tr id="en-us_topic_0030969470_row1732101910217"><td class="cellrowborder" valign="top" width="28.299999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0030969470_p16320131918211"><a name="en-us_topic_0030969470_p16320131918211"></a><a name="en-us_topic_0030969470_p16320131918211"></a>Port Range/ICMP Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0030969470_p0320141916219"><a name="en-us_topic_0030969470_p0320141916219"></a><a name="en-us_topic_0030969470_p0320141916219"></a>Specifies the port or port range for which the security group rule takes effect. The value ranges from <strong id="en-us_topic_0030969470_b842352706135645"><a name="en-us_topic_0030969470_b842352706135645"></a><a name="en-us_topic_0030969470_b842352706135645"></a>1</strong>&nbsp;to&nbsp;<strong id="en-us_topic_0030969470_b842352706135649"><a name="en-us_topic_0030969470_b842352706135649"></a><a name="en-us_topic_0030969470_b842352706135649"></a>65535</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0030969470_p332121914218"><a name="en-us_topic_0030969470_p332121914218"></a><a name="en-us_topic_0030969470_p332121914218"></a>22 or 22-30</p>
    </td>
    </tr>
    <tr id="en-us_topic_0030969470_row2032111191124"><td class="cellrowborder" valign="top" width="28.299999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0030969470_p203213191023"><a name="en-us_topic_0030969470_p203213191023"></a><a name="en-us_topic_0030969470_p203213191023"></a>Source</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0030969470_p1632116191821"><a name="en-us_topic_0030969470_p1632116191821"></a><a name="en-us_topic_0030969470_p1632116191821"></a>Specifies the source of the security group rule. The value can be an IP address or a security group.</p>
    <p id="en-us_topic_0030969470_p1732115192210"><a name="en-us_topic_0030969470_p1732115192210"></a><a name="en-us_topic_0030969470_p1732115192210"></a>For example:</p>
    <p id="en-us_topic_0030969470_p123211198214"><a name="en-us_topic_0030969470_p123211198214"></a><a name="en-us_topic_0030969470_p123211198214"></a>xxx.xxx.xxx.xxx/32 (IPv4 address)</p>
    <p id="en-us_topic_0030969470_p1532141911212"><a name="en-us_topic_0030969470_p1532141911212"></a><a name="en-us_topic_0030969470_p1532141911212"></a>xxx.xxx.xxx.0/24 (subnet)</p>
    <p id="en-us_topic_0030969470_p93211419525"><a name="en-us_topic_0030969470_p93211419525"></a><a name="en-us_topic_0030969470_p93211419525"></a>0.0.0.0/0 (any IP address)</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0030969470_p1332111191324"><a name="en-us_topic_0030969470_p1332111191324"></a><a name="en-us_topic_0030969470_p1332111191324"></a>0.0.0.0/0</p>
    <p id="en-us_topic_0030969470_p1032161911212"><a name="en-us_topic_0030969470_p1032161911212"></a><a name="en-us_topic_0030969470_p1032161911212"></a>default</p>
    </td>
    </tr>
    <tr id="en-us_topic_0030969470_row1844612518515"><td class="cellrowborder" valign="top" width="28.299999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0030969470_p04476514517"><a name="en-us_topic_0030969470_p04476514517"></a><a name="en-us_topic_0030969470_p04476514517"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0030969470_p1399275111429"><a name="en-us_topic_0030969470_p1399275111429"></a><a name="en-us_topic_0030969470_p1399275111429"></a>Provides supplementary information about the security group. This parameter is optional.</p>
    <p id="en-us_topic_0030969470_p12593482111429"><a name="en-us_topic_0030969470_p12593482111429"></a><a name="en-us_topic_0030969470_p12593482111429"></a>The security group description can contain a maximum of 255 characters and cannot contain angle brackets (&lt;) or (&gt;).</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0030969470_p16447351352"><a name="en-us_topic_0030969470_p16447351352"></a><a name="en-us_topic_0030969470_p16447351352"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  On the  **Outbound** tab, click **Add Rule**. In the displayed dialog box, set required parameters to add an outbound rule.

    You can click  **+**  to add more outbound rules.

    **Figure  2**  Add Outbound Rule<a name="en-us_topic_0030969470_fig973013416534"></a>
    ![](figures/add-outbound-rule.png "Add Outbound Rule")

    **Table  2**  Outbound rule parameter description

    <a name="en-us_topic_0030969470_table20884115181311"></a><table><thead align="left"><tr id="en-us_topic_0030969470_row1689515114136"><th class="cellrowborder" valign="top" width="28.299999999999997%" id="mcps1.2.4.1.1"><p id="en-us_topic_0030969470_p3897175181310"><a name="en-us_topic_0030969470_p3897175181310"></a><a name="en-us_topic_0030969470_p3897175181310"></a><strong id="en-us_topic_0030969470_b842352706114331_1"><a name="en-us_topic_0030969470_b842352706114331_1"></a><a name="en-us_topic_0030969470_b842352706114331_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.7%" id="mcps1.2.4.1.2"><p id="en-us_topic_0030969470_p10898125112133"><a name="en-us_topic_0030969470_p10898125112133"></a><a name="en-us_topic_0030969470_p10898125112133"></a><strong id="en-us_topic_0030969470_b84235270694155_1"><a name="en-us_topic_0030969470_b84235270694155_1"></a><a name="en-us_topic_0030969470_b84235270694155_1"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.3"><p id="en-us_topic_0030969470_p19900145111310"><a name="en-us_topic_0030969470_p19900145111310"></a><a name="en-us_topic_0030969470_p19900145111310"></a><strong id="en-us_topic_0030969470_b8423527069420_1"><a name="en-us_topic_0030969470_b8423527069420_1"></a><a name="en-us_topic_0030969470_b8423527069420_1"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0030969470_row139013518139"><td class="cellrowborder" valign="top" width="28.299999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0030969470_p6902105141316"><a name="en-us_topic_0030969470_p6902105141316"></a><a name="en-us_topic_0030969470_p6902105141316"></a>Protocol/Application</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0030969470_p9904751151312"><a name="en-us_topic_0030969470_p9904751151312"></a><a name="en-us_topic_0030969470_p9904751151312"></a>Specifies the network protocol for which the security group rule takes effect. The value can be <strong id="en-us_topic_0030969470_b84235270613479_1"><a name="en-us_topic_0030969470_b84235270613479_1"></a><a name="en-us_topic_0030969470_b84235270613479_1"></a>TCP</strong>,&nbsp;<strong id="en-us_topic_0030969470_b842352706134713_1"><a name="en-us_topic_0030969470_b842352706134713_1"></a><a name="en-us_topic_0030969470_b842352706134713_1"></a>UDP</strong>,&nbsp;<strong id="en-us_topic_0030969470_b842352706134716_1"><a name="en-us_topic_0030969470_b842352706134716_1"></a><a name="en-us_topic_0030969470_b842352706134716_1"></a>ICMP</strong>, or&nbsp;<strong id="en-us_topic_0030969470_b842352706134721_1"><a name="en-us_topic_0030969470_b842352706134721_1"></a><a name="en-us_topic_0030969470_b842352706134721_1"></a>ANY</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0030969470_p5905951141320"><a name="en-us_topic_0030969470_p5905951141320"></a><a name="en-us_topic_0030969470_p5905951141320"></a>TCP</p>
    </td>
    </tr>
    <tr id="en-us_topic_0030969470_row159061451141316"><td class="cellrowborder" valign="top" width="28.299999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0030969470_p990775121315"><a name="en-us_topic_0030969470_p990775121315"></a><a name="en-us_topic_0030969470_p990775121315"></a>Port Range/ICMP Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0030969470_p16909151181320"><a name="en-us_topic_0030969470_p16909151181320"></a><a name="en-us_topic_0030969470_p16909151181320"></a>Specifies the port or port range for which the security group rule takes effect. The value ranges from <strong id="en-us_topic_0030969470_b842352706135645_1"><a name="en-us_topic_0030969470_b842352706135645_1"></a><a name="en-us_topic_0030969470_b842352706135645_1"></a>1</strong>&nbsp;to&nbsp;<strong id="en-us_topic_0030969470_b842352706135649_1"><a name="en-us_topic_0030969470_b842352706135649_1"></a><a name="en-us_topic_0030969470_b842352706135649_1"></a>65535</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0030969470_p12912165111310"><a name="en-us_topic_0030969470_p12912165111310"></a><a name="en-us_topic_0030969470_p12912165111310"></a>22 or 22-30</p>
    </td>
    </tr>
    <tr id="en-us_topic_0030969470_row1491445114138"><td class="cellrowborder" valign="top" width="28.299999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0030969470_p12916125151313"><a name="en-us_topic_0030969470_p12916125151313"></a><a name="en-us_topic_0030969470_p12916125151313"></a>Destination</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0030969470_p4917145119132"><a name="en-us_topic_0030969470_p4917145119132"></a><a name="en-us_topic_0030969470_p4917145119132"></a>Specifies the destination of the security group rule. The value can be an IP address or a security group.</p>
    <p id="en-us_topic_0030969470_p11918851161319"><a name="en-us_topic_0030969470_p11918851161319"></a><a name="en-us_topic_0030969470_p11918851161319"></a>For example:</p>
    <p id="en-us_topic_0030969470_p18919155171315"><a name="en-us_topic_0030969470_p18919155171315"></a><a name="en-us_topic_0030969470_p18919155171315"></a>xxx.xxx.xxx.xxx/32 (IPv4 address)</p>
    <p id="en-us_topic_0030969470_p5920155111316"><a name="en-us_topic_0030969470_p5920155111316"></a><a name="en-us_topic_0030969470_p5920155111316"></a>xxx.xxx.xxx.0/24 (subnet)</p>
    <p id="en-us_topic_0030969470_p2092045115132"><a name="en-us_topic_0030969470_p2092045115132"></a><a name="en-us_topic_0030969470_p2092045115132"></a>0.0.0.0/0 (any IP address)</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0030969470_p992325101316"><a name="en-us_topic_0030969470_p992325101316"></a><a name="en-us_topic_0030969470_p992325101316"></a>0.0.0.0/0</p>
    <p id="en-us_topic_0030969470_p392395115134"><a name="en-us_topic_0030969470_p392395115134"></a><a name="en-us_topic_0030969470_p392395115134"></a>default</p>
    </td>
    </tr>
    <tr id="en-us_topic_0030969470_row139271451151311"><td class="cellrowborder" valign="top" width="28.299999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0030969470_p2092855171315"><a name="en-us_topic_0030969470_p2092855171315"></a><a name="en-us_topic_0030969470_p2092855171315"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0030969470_p1193019518138"><a name="en-us_topic_0030969470_p1193019518138"></a><a name="en-us_topic_0030969470_p1193019518138"></a>Provides supplementary information about the security group. This parameter is optional.</p>
    <p id="en-us_topic_0030969470_p09312514131"><a name="en-us_topic_0030969470_p09312514131"></a><a name="en-us_topic_0030969470_p09312514131"></a>The security group description can contain a maximum of 255 characters and cannot contain angle brackets (&lt;) or (&gt;).</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0030969470_p1693210510132"><a name="en-us_topic_0030969470_p1693210510132"></a><a name="en-us_topic_0030969470_p1693210510132"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>


