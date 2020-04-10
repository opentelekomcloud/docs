# Adding a Security Group Rule<a name="vpn_03_0802"></a>

## Scenarios<a name="en-us_topic_0118534005_s480ea51d8f2542828c323c6c8eb50861"></a>

After a security group is created, you can add rules to the security group. A rule applies either to inbound traffic \(ingress\) or outbound traffic \(egress\). After ECSs are added to the security group, they are protected by the rules of that group.

-   Inbound rules control incoming traffic to ECSs associated with the security group.
-   Outbound rules control outgoing traffic from ECSs associated with the security group.

## Procedure<a name="en-us_topic_0118534005_section2999103814551"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, choose  **Access Control**  \>  **Security Groups**.
5.  On the  **Security Groups**  page, locate the target security group and click  **Manage Rule**  in the  **Operation**  column to switch to the page for managing inbound and outbound rules.
6.  On the inbound rule tab, click  **Add Rule**. In the displayed dialog box, set required parameters to add an inbound rule.

    You can click  **+**  to add more inbound rules.

    **Figure  1**  Add Inbound Rule<a name="en-us_topic_0118534005_fig172301034104912"></a>  
    ![](figures/add-inbound-rule.png "add-inbound-rule")

    **Table  1**  Inbound rule parameter description

    <a name="en-us_topic_0118534005_table532116198213"></a>
    <table><thead align="left"><tr id="en-us_topic_0118534005_row731911191722"><th class="cellrowborder" valign="top" width="28.299999999999997%" id="mcps1.2.4.1.1"><p id="en-us_topic_0118534005_p17319119020"><a name="en-us_topic_0118534005_p17319119020"></a><a name="en-us_topic_0118534005_p17319119020"></a><strong id="en-us_topic_0118534005_b842352706114331"><a name="en-us_topic_0118534005_b842352706114331"></a><a name="en-us_topic_0118534005_b842352706114331"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.7%" id="mcps1.2.4.1.2"><p id="en-us_topic_0118534005_p431911191622"><a name="en-us_topic_0118534005_p431911191622"></a><a name="en-us_topic_0118534005_p431911191622"></a><strong id="en-us_topic_0118534005_b84235270694155"><a name="en-us_topic_0118534005_b84235270694155"></a><a name="en-us_topic_0118534005_b84235270694155"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.3"><p id="en-us_topic_0118534005_p103191119621"><a name="en-us_topic_0118534005_p103191119621"></a><a name="en-us_topic_0118534005_p103191119621"></a><strong id="en-us_topic_0118534005_b8423527069420"><a name="en-us_topic_0118534005_b8423527069420"></a><a name="en-us_topic_0118534005_b8423527069420"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0118534005_row8320419723"><td class="cellrowborder" valign="top" width="28.299999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p1432013199214"><a name="en-us_topic_0118534005_p1432013199214"></a><a name="en-us_topic_0118534005_p1432013199214"></a>Protocol/Application</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p432017191726"><a name="en-us_topic_0118534005_p432017191726"></a><a name="en-us_topic_0118534005_p432017191726"></a>Specifies the network protocol. Currently, the value can be <strong id="en-us_topic_0118534005_b1166424112017"><a name="en-us_topic_0118534005_b1166424112017"></a><a name="en-us_topic_0118534005_b1166424112017"></a>All</strong>, <strong id="en-us_topic_0118534005_b116533732012"><a name="en-us_topic_0118534005_b116533732012"></a><a name="en-us_topic_0118534005_b116533732012"></a>TCP</strong>, <strong id="en-us_topic_0118534005_b9510134513200"><a name="en-us_topic_0118534005_b9510134513200"></a><a name="en-us_topic_0118534005_b9510134513200"></a>UDP</strong>, <strong id="en-us_topic_0118534005_b10916155713209"><a name="en-us_topic_0118534005_b10916155713209"></a><a name="en-us_topic_0118534005_b10916155713209"></a>ICMP</strong>, <strong id="en-us_topic_0118534005_b175264618215"><a name="en-us_topic_0118534005_b175264618215"></a><a name="en-us_topic_0118534005_b175264618215"></a>GRE</strong>, or others.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118534005_p1332014191216"><a name="en-us_topic_0118534005_p1332014191216"></a><a name="en-us_topic_0118534005_p1332014191216"></a>TCP</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118534005_row1732101910217"><td class="cellrowborder" rowspan="2" valign="top" width="28.299999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p16320131918211"><a name="en-us_topic_0118534005_p16320131918211"></a><a name="en-us_topic_0118534005_p16320131918211"></a>Port &amp; Source</p>
    <p id="en-us_topic_0118534005_p203213191023"><a name="en-us_topic_0118534005_p203213191023"></a><a name="en-us_topic_0118534005_p203213191023"></a></p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p0320141916219"><a name="en-us_topic_0118534005_p0320141916219"></a><a name="en-us_topic_0118534005_p0320141916219"></a><strong id="en-us_topic_0118534005_b6994125616147"><a name="en-us_topic_0118534005_b6994125616147"></a><a name="en-us_topic_0118534005_b6994125616147"></a>Port</strong>: specifies the port or port range over which the traffic can reach your ECS. The value ranges from 1 to 65535. </p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118534005_p332121914218"><a name="en-us_topic_0118534005_p332121914218"></a><a name="en-us_topic_0118534005_p332121914218"></a>22 or 22-30</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118534005_row2032111191124"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p1632116191821"><a name="en-us_topic_0118534005_p1632116191821"></a><a name="en-us_topic_0118534005_p1632116191821"></a><strong id="b83102261419"><a name="b83102261419"></a><a name="b83102261419"></a>Source</strong>: specifies the source of the security group rule. The value can be another security group, a CIDR block, or a single IP address. For example:</p>
    <a name="en-us_topic_0118534005_ul474117187016"></a><a name="en-us_topic_0118534005_ul474117187016"></a><ul id="en-us_topic_0118534005_ul474117187016"><li>xxx.xxx.xxx.xxx/32 (IPv4 address)</li><li>xxx.xxx.xxx.0/24 (subnet CIDR block)</li><li>0.0.0.0/0 (any IP address)</li></ul>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p1332111191324"><a name="en-us_topic_0118534005_p1332111191324"></a><a name="en-us_topic_0118534005_p1332111191324"></a>0.0.0.0/0</p>
    <p id="en-us_topic_0118534005_p1032161911212"><a name="en-us_topic_0118534005_p1032161911212"></a><a name="en-us_topic_0118534005_p1032161911212"></a>default</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118534005_row1844612518515"><td class="cellrowborder" valign="top" width="28.299999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p04476514517"><a name="en-us_topic_0118534005_p04476514517"></a><a name="en-us_topic_0118534005_p04476514517"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p1399275111429"><a name="en-us_topic_0118534005_p1399275111429"></a><a name="en-us_topic_0118534005_p1399275111429"></a>Provides supplementary information about the security group rule. This parameter is optional.</p>
    <p id="en-us_topic_0118534005_p12593482111429"><a name="en-us_topic_0118534005_p12593482111429"></a><a name="en-us_topic_0118534005_p12593482111429"></a>The security group rule description can contain a maximum of 255 characters and cannot contain angle brackets (&lt; or &gt;).</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118534005_p16447351352"><a name="en-us_topic_0118534005_p16447351352"></a><a name="en-us_topic_0118534005_p16447351352"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  On the outbound rule tab, click  **Add Rule**. In the displayed dialog box, set required parameters to add an outbound rule.

    You can click  **+**  to add more outbound rules.

    **Figure  2**  Add Outbound Rule<a name="en-us_topic_0118534005_fig973013416534"></a>  
    ![](figures/add-outbound-rule.png "add-outbound-rule")

    **Table  2**  Outbound rule parameter description

    <a name="en-us_topic_0118534005_table20884115181311"></a>
    <table><thead align="left"><tr id="en-us_topic_0118534005_row1689515114136"><th class="cellrowborder" valign="top" width="28.299999999999997%" id="mcps1.2.4.1.1"><p id="en-us_topic_0118534005_p3897175181310"><a name="en-us_topic_0118534005_p3897175181310"></a><a name="en-us_topic_0118534005_p3897175181310"></a><strong id="b749943084"><a name="b749943084"></a><a name="b749943084"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.7%" id="mcps1.2.4.1.2"><p id="en-us_topic_0118534005_p10898125112133"><a name="en-us_topic_0118534005_p10898125112133"></a><a name="en-us_topic_0118534005_p10898125112133"></a><strong id="b872681780"><a name="b872681780"></a><a name="b872681780"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.3"><p id="en-us_topic_0118534005_p19900145111310"><a name="en-us_topic_0118534005_p19900145111310"></a><a name="en-us_topic_0118534005_p19900145111310"></a><strong id="b1515984461"><a name="b1515984461"></a><a name="b1515984461"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0118534005_row139013518139"><td class="cellrowborder" valign="top" width="28.299999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p6902105141316"><a name="en-us_topic_0118534005_p6902105141316"></a><a name="en-us_topic_0118534005_p6902105141316"></a>Protocol/Application</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p9904751151312"><a name="en-us_topic_0118534005_p9904751151312"></a><a name="en-us_topic_0118534005_p9904751151312"></a>Specifies the network protocol. Currently, the value can be <strong id="en-us_topic_0118534005_b757165142411"><a name="en-us_topic_0118534005_b757165142411"></a><a name="en-us_topic_0118534005_b757165142411"></a>All</strong>, <strong id="en-us_topic_0118534005_b185711451112416"><a name="en-us_topic_0118534005_b185711451112416"></a><a name="en-us_topic_0118534005_b185711451112416"></a>TCP</strong>, <strong id="en-us_topic_0118534005_b857235122419"><a name="en-us_topic_0118534005_b857235122419"></a><a name="en-us_topic_0118534005_b857235122419"></a>UDP</strong>, <strong id="en-us_topic_0118534005_b14572185102415"><a name="en-us_topic_0118534005_b14572185102415"></a><a name="en-us_topic_0118534005_b14572185102415"></a>ICMP</strong>, <strong id="en-us_topic_0118534005_b1257315110245"><a name="en-us_topic_0118534005_b1257315110245"></a><a name="en-us_topic_0118534005_b1257315110245"></a>GRE</strong>, or others.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118534005_p5905951141320"><a name="en-us_topic_0118534005_p5905951141320"></a><a name="en-us_topic_0118534005_p5905951141320"></a>TCP</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118534005_row159061451141316"><td class="cellrowborder" rowspan="2" valign="top" width="28.299999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p990775121315"><a name="en-us_topic_0118534005_p990775121315"></a><a name="en-us_topic_0118534005_p990775121315"></a>Port &amp; Destination</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p16909151181320"><a name="en-us_topic_0118534005_p16909151181320"></a><a name="en-us_topic_0118534005_p16909151181320"></a><strong id="en-us_topic_0118534005_b670323214221"><a name="en-us_topic_0118534005_b670323214221"></a><a name="en-us_topic_0118534005_b670323214221"></a>Port</strong>: specifies the port or port range over which the traffic can leave your ECS. The value ranges from 1 to 65535. </p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118534005_p12912165111310"><a name="en-us_topic_0118534005_p12912165111310"></a><a name="en-us_topic_0118534005_p12912165111310"></a>22 or 22-30</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118534005_row1491445114138"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p4917145119132"><a name="en-us_topic_0118534005_p4917145119132"></a><a name="en-us_topic_0118534005_p4917145119132"></a><strong id="b16986174181619"><a name="b16986174181619"></a><a name="b16986174181619"></a>Destination</strong>: specifies the destination of the security group rule. The value can be another security group, a CIDR block, or a single IP address. For example:</p>
    <a name="en-us_topic_0118534005_ul1971712284017"></a><a name="en-us_topic_0118534005_ul1971712284017"></a><ul id="en-us_topic_0118534005_ul1971712284017"><li>xxx.xxx.xxx.xxx/32 (IPv4 address)</li><li>xxx.xxx.xxx.0/24 (subnet CIDR block)</li><li>0.0.0.0/0 (any IP address)</li></ul>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p992325101316"><a name="en-us_topic_0118534005_p992325101316"></a><a name="en-us_topic_0118534005_p992325101316"></a>0.0.0.0/0</p>
    <p id="en-us_topic_0118534005_p392395115134"><a name="en-us_topic_0118534005_p392395115134"></a><a name="en-us_topic_0118534005_p392395115134"></a>default</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118534005_row139271451151311"><td class="cellrowborder" valign="top" width="28.299999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118534005_p2092855171315"><a name="en-us_topic_0118534005_p2092855171315"></a><a name="en-us_topic_0118534005_p2092855171315"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118534005_p1193019518138"><a name="en-us_topic_0118534005_p1193019518138"></a><a name="en-us_topic_0118534005_p1193019518138"></a>Provides supplementary information about the security group rule. This parameter is optional.</p>
    <p id="en-us_topic_0118534005_p09312514131"><a name="en-us_topic_0118534005_p09312514131"></a><a name="en-us_topic_0118534005_p09312514131"></a>The security group rule description can contain a maximum of 255 characters and cannot contain angle brackets (&lt; or &gt;).</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118534005_p1693210510132"><a name="en-us_topic_0118534005_p1693210510132"></a><a name="en-us_topic_0118534005_p1693210510132"></a>N/A</p>
    </td>
    </tr>
    </tbody>
    </table>

8.  Click  **OK**.

