# Configuring Data Masking Rules<a name="waf_01_0017"></a>

This section describes how to configure data masking rules.  Data Masking  prevents such data as usernames and passwords from being displayed in event logs.

## Prerequisites<a name="section2256777914731"></a>

-   Login credentials have been obtained.
-   The domain name to be protected has been created.

## Procedure<a name="section121983568447"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Click  **Service List**  at the top of the page and choose  **Security**  \>  **Web Application Firewall**. In the navigation pane, choose  **Domains**. The  **Domains**  page is displayed, as shown in  [Figure 1](#waf_01_0008_fig164792010154510).

    **Figure  1**  Entrance to the domain configuration page<a name="waf_01_0008_fig164792010154510"></a>  
    ![](figures/entrance-to-the-domain-configuration-page.png "entrance-to-the-domain-configuration-page")

4.  In the  **Operation**  column of the row containing the target domain name, click  **Configure Policy**. The protection configuration page is displayed, as shown in  [Figure 2](#waf_01_0008_fig16197124372015).

    **Figure  2**  Protection configuration page<a name="waf_01_0008_fig16197124372015"></a>  
    ![](figures/protection-configuration-page.png "protection-configuration-page")

5.  <a name="li45442459125143"></a>In the  **Data Masking**  configuration area, change  **Status**  as needed and then click  **Save**  in the upper right corner of the  **Protection Status**  list. In the dialog box displayed, click  **Yes**  to save the settings. Otherwise, click  **Cancel**. See  [Figure 3](#fig163378412590).

    **Figure  3**  Data Masking configuration area<a name="fig163378412590"></a>  
    ![](figures/data-masking-configuration-area.png "data-masking-configuration-area")

6.  Click  **Customize Rule**. On the displayed page, click  **Add Rule**  in the upper left corner to add a data masking rule. See  [Figure 4](#fig187391447920).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If you do not click  **Save**  after changing  **Status**  in  [step 5](#li45442459125143), the  **Warning**  dialog box is displayed when you click  **Customize Rule**.  
    >-   Click  **Yes**  to cancel the previous settings.  
    >-   Click  **No**  and then  **Save**  to save the settings.  

    **Figure  4**  Add Rule \(Data Masking\)<a name="fig187391447920"></a>  
    ![](figures/add-rule-(data-masking).png "add-rule-(data-masking)")

7.  In the displayed dialog box shown in  [Figure 5](#fig49385421125519), specify the parameters by referring to  [Table 1](#table4696626918715).

    **Figure  5**  Adding a data masking rule<a name="fig49385421125519"></a>  
    ![](figures/adding-a-data-masking-rule.png "adding-a-data-masking-rule")

    **Table  1**  Rule parameters

    <a name="table4696626918715"></a>
    <table><thead align="left"><tr id="row151760118715"><th class="cellrowborder" valign="top" width="15.85%" id="mcps1.2.4.1.1"><p id="p3258956818715"><a name="p3258956818715"></a><a name="p3258956818715"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.2%" id="mcps1.2.4.1.2"><p id="p2250934518715"><a name="p2250934518715"></a><a name="p2250934518715"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="31.95%" id="mcps1.2.4.1.3"><p id="p2986065181135"><a name="p2986065181135"></a><a name="p2986065181135"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row125751318715"><td class="cellrowborder" valign="top" width="15.85%" headers="mcps1.2.4.1.1 "><p id="p3474973518715"><a name="p3474973518715"></a><a name="p3474973518715"></a>Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.2%" headers="mcps1.2.4.1.2 "><p id="p6326519018715"><a name="p6326519018715"></a><a name="p6326519018715"></a>URL excluding a domain name</p>
    <a name="ul1515617591337"></a><a name="ul1515617591337"></a><ul id="ul1515617591337"><li>Prefix match: The path ending with * indicates that the path is used as a prefix. For example, if the path to be protected is <strong id="b174531018122"><a name="b174531018122"></a><a name="b174531018122"></a>/admin/test.php</strong> or <strong id="b164537185220"><a name="b164537185220"></a><a name="b164537185220"></a>/adminabc</strong>, set <strong id="b184531918121"><a name="b184531918121"></a><a name="b184531918121"></a>Path</strong> to <span class="parmvalue" id="parmvalue345318181421"><a name="parmvalue345318181421"></a><a name="parmvalue345318181421"></a><b>/admin*</b></span>.</li><li>Exact match: The path to be entered must match the path to be protected. If the path to be protected is <span class="parmvalue" id="parmvalue65783211923"><a name="parmvalue65783211923"></a><a name="parmvalue65783211923"></a><b>/admin</b></span>, set <strong id="b05781021825"><a name="b05781021825"></a><a name="b05781021825"></a>Path</strong> to <span class="parmvalue" id="parmvalue55781221228"><a name="parmvalue55781221228"></a><a name="parmvalue55781221228"></a><b>/admin</b></span>.</li></ul>
    <div class="note" id="note86025529534"><a name="note86025529534"></a><a name="note86025529534"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul20707155819344"></a><a name="ul20707155819344"></a><ul id="ul20707155819344"><li>The path supports prefix and exact matches only and does not support regular expressions.</li><li>The path cannot contain two or more consecutive slashes. For example, <span class="parmvalue" id="parmvalue6814192517581"><a name="parmvalue6814192517581"></a><a name="parmvalue6814192517581"></a><b>///admin</b></span>. If you enter <strong id="b981419256582"><a name="b981419256582"></a><a name="b981419256582"></a>///admin</strong>, the WAF engine converts <strong id="b1081415253585"><a name="b1081415253585"></a><a name="b1081415253585"></a>///</strong> to <strong id="b19814122511589"><a name="b19814122511589"></a><a name="b19814122511589"></a>/</strong>.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="31.95%" headers="mcps1.2.4.1.3 "><p id="p40544725181135"><a name="p40544725181135"></a><a name="p40544725181135"></a><strong id="b240272934615"><a name="b240272934615"></a><a name="b240272934615"></a>/admin/login.php</strong></p>
    <p id="p11951173761619"><a name="p11951173761619"></a><a name="p11951173761619"></a>For example, if the URL to be protected is <span class="filepath" id="filepath17219125201"><a name="filepath17219125201"></a><a name="filepath17219125201"></a><b>http://www.example.com/admin/login.php</b></span>, set <strong id="b1723129201"><a name="b1723129201"></a><a name="b1723129201"></a>Path</strong> to <strong id="b12191272014"><a name="b12191272014"></a><a name="b12191272014"></a>/admin/login.php</strong>.</p>
    </td>
    </tr>
    <tr id="row12212154685910"><td class="cellrowborder" valign="top" width="15.85%" headers="mcps1.2.4.1.1 "><p id="p182121546175911"><a name="p182121546175911"></a><a name="p182121546175911"></a>Masked Field</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.2%" headers="mcps1.2.4.1.2 "><div class="p" id="p4124255145815"><a name="p4124255145815"></a><a name="p4124255145815"></a>A field set to be masked<a name="ul16778520183811"></a><a name="ul16778520183811"></a><ul id="ul16778520183811"><li><strong id="b1343103515012"><a name="b1343103515012"></a><a name="b1343103515012"></a>Params</strong>: A request parameter</li><li><strong id="b3268543155016"><a name="b3268543155016"></a><a name="b3268543155016"></a>Header</strong>: A user-defined HTTP header</li></ul>
    </div>
    </td>
    <td class="cellrowborder" rowspan="2" valign="top" width="31.95%" headers="mcps1.2.4.1.3 "><a name="ul3574205795514"></a><a name="ul3574205795514"></a><ul id="ul3574205795514"><li>If <strong id="b33911257154612"><a name="b33911257154612"></a><a name="b33911257154612"></a>Masked Field</strong> is <strong id="b16810122213477"><a name="b16810122213477"></a><a name="b16810122213477"></a>Params</strong>, set <strong id="b15130102919477"><a name="b15130102919477"></a><a name="b15130102919477"></a>Subfield</strong> according to your actual needs. If it is set to <strong id="b9644145594714"><a name="b9644145594714"></a><a name="b9644145594714"></a>id</strong>, content that matches <strong id="b786051518488"><a name="b786051518488"></a><a name="b786051518488"></a>id</strong> is masked.</li><li>If <strong id="b1579816587"><a name="b1579816587"></a><a name="b1579816587"></a>Masked Field</strong> is <span class="parmvalue" id="parmvalue1852725718"><a name="parmvalue1852725718"></a><a name="parmvalue1852725718"></a><b>Header</b></span>, set <span class="parmname" id="parmname1948091887"><a name="parmname1948091887"></a><a name="parmname1948091887"></a><b>Subfield</b></span> according to your actual needs. If it is set to <span class="parmvalue" id="parmvalue366156849"><a name="parmvalue366156849"></a><a name="parmvalue366156849"></a><b>Accept</b></span>, content that matches <span class="parmvalue" id="parmvalue2093604268"><a name="parmvalue2093604268"></a><a name="parmvalue2093604268"></a><b>Accept</b></span> is masked.</li></ul>
    </td>
    </tr>
    <tr id="row3251580618715"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1653459218715"><a name="p1653459218715"></a><a name="p1653459218715"></a>Subfield</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p12165125012131"><a name="p12165125012131"></a><a name="p12165125012131"></a>Set the parameter based on <strong id="b771614580578"><a name="b771614580578"></a><a name="b771614580578"></a>Masked Field</strong>. The masked field will not be displayed in the log.</p>
    <div class="notice" id="note106664883710"><a name="note106664883710"></a><a name="note106664883710"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="waf_01_0010_p954031113102"><a name="waf_01_0010_p954031113102"></a><a name="waf_01_0010_p954031113102"></a>The length of a subfield cannot exceed 2048 bytes. Only digits, letters, underscores (_), and hyphens (-) are allowed.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

8.  Click  **OK**.
    -   To modify the added rule, click  **Modify**  in the row containing the target rule.
    -   To delete the added rule, click  **Delete**  in the row containing the target rule.


