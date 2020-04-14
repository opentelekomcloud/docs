# Configuring False Alarm Masking Rules<a name="EN-US_TOPIC_0193630291"></a>

This section describes how to configure  false alarm masking  rules.

You can add false alarms to the whitelist and ignore certain rule IDs \(for example, skip XSS check for a specified URL\).

## Prerequisites<a name="section2256777914731"></a>

-   Login credentials have been obtained.
-   The domain name to be protected has been created.

## Procedure<a name="section6607803193933"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Click  **Service List**  at the top of the page and choose  **Security**  \>  **Web Application Firewall**. In the navigation pane, choose  **Domains**. The  **Domains**  page is displayed, as shown in  [Figure 1](#en-us_topic_0193630287_fig4838162174519).

    **Figure  1**  Domains<a name="en-us_topic_0193630287_fig4838162174519"></a>  
    ![](figures/domains-policy.png "domains-policy")

4.  In the  **Operation**  column of the row containing the target domain name, click  **Configure Policy**. The protection configuration page is displayed, as shown in  [Figure 2](#en-us_topic_0193630287_fig16197124372015).

    **Figure  2**  Protection configuration page<a name="en-us_topic_0193630287_fig16197124372015"></a>  
    ![](figures/protection-configuration-page.png "protection-configuration-page")

5.  <a name="li58723545102836"></a>In the  **False Alarm Masking**  configuration area, change  **Status**  as needed and then click  **Save**  in the upper right corner of the  **Protection Status**  list. In the dialog box displayed, click  **Yes**  to save the settings. Otherwise, click  **Cancel**. See  [Figure 3](#fig44151977327).

    **Figure  3**  False Alarm Masking configuration area<a name="fig44151977327"></a>  
    ![](figures/false-alarm-masking-configuration-area.png "false-alarm-masking-configuration-area")

6.  Click  **Customize Rule**. On the displayed page, click  **Add Rule**  in the upper left corner to add a false alarm masking rule. See  [Figure 4](#fig106802271583).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If you do not click  **Save**  after changing  **Status**  in  [step 5](#li58723545102836), the  **Warning**  dialog box is displayed when you click  **Customize Rule**.  
    >-   Click  **Yes**  to cancel the previous settings.  
    >-   Click  **No**  and then  **Save**  to save the settings.  

    **Figure  4**  Add Rule \(false alarm masking\)<a name="fig106802271583"></a>  
    ![](figures/add-rule-(false-alarm-masking).png "add-rule-(false-alarm-masking)")

7.  In the displayed dialog box shown in  [Figure 5](#fig14415389105236), specify the parameters by referring to  [Table 1](#table4696626918715).

    **Figure  5**  Adding a false alarm masking rule<a name="fig14415389105236"></a>  
    ![](figures/adding-a-false-alarm-masking-rule.png "adding-a-false-alarm-masking-rule")

    **Table  1**  Rule parameters

    <a name="table4696626918715"></a>
    <table><thead align="left"><tr id="row151760118715"><th class="cellrowborder" valign="top" width="23.84%" id="mcps1.2.4.1.1"><p id="p3258956818715"><a name="p3258956818715"></a><a name="p3258956818715"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.21%" id="mcps1.2.4.1.2"><p id="p2250934518715"><a name="p2250934518715"></a><a name="p2250934518715"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="31.95%" id="mcps1.2.4.1.3"><p id="p2986065181135"><a name="p2986065181135"></a><a name="p2986065181135"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row125751318715"><td class="cellrowborder" valign="top" width="23.84%" headers="mcps1.2.4.1.1 "><p id="p3474973518715"><a name="p3474973518715"></a><a name="p3474973518715"></a>Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.21%" headers="mcps1.2.4.1.2 "><p id="p6326519018715"><a name="p6326519018715"></a><a name="p6326519018715"></a>Misreported URL excluding a domain name</p>
    <a name="ul1515617591337"></a><a name="ul1515617591337"></a><ul id="ul1515617591337"><li>Prefix match: The path ending with * indicates that the path is used as a prefix. For example, if the path to be protected is <strong id="b76511353115"><a name="b76511353115"></a><a name="b76511353115"></a>/admin/test.php</strong> or <strong id="b17651205114"><a name="b17651205114"></a><a name="b17651205114"></a>/adminabc</strong>, set <strong id="b16511154110"><a name="b16511154110"></a><a name="b16511154110"></a>Path</strong> to <span class="parmvalue" id="parmvalue76519510115"><a name="parmvalue76519510115"></a><a name="parmvalue76519510115"></a><b>/admin*</b></span>.</li><li>Exact match: The path to be entered must match the path to be protected. If the path to be protected is <span class="parmvalue" id="parmvalue55713102016"><a name="parmvalue55713102016"></a><a name="parmvalue55713102016"></a><b>/admin</b></span>, set <strong id="b15579106114"><a name="b15579106114"></a><a name="b15579106114"></a>Path</strong> to <span class="parmvalue" id="parmvalue16572108114"><a name="parmvalue16572108114"></a><a name="parmvalue16572108114"></a><b>/admin</b></span>.</li></ul>
    <div class="note" id="note15799173511525"><a name="note15799173511525"></a><a name="note15799173511525"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul20707155819344"></a><a name="ul20707155819344"></a><ul id="ul20707155819344"><li>The path supports prefix and exact matches only and does not support regular expressions.</li><li>The path cannot contain two or more consecutive slashes. For example, <span class="parmvalue" id="parmvalue206275112571"><a name="parmvalue206275112571"></a><a name="parmvalue206275112571"></a><b>///admin</b></span>. If you enter <strong id="b1878115110573"><a name="b1878115110573"></a><a name="b1878115110573"></a>///admin</strong>, the WAF engine converts <strong id="b19787513575"><a name="b19787513575"></a><a name="b19787513575"></a>///</strong> to <strong id="b1478451105713"><a name="b1478451105713"></a><a name="b1478451105713"></a>/</strong>.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="31.95%" headers="mcps1.2.4.1.3 "><p id="p40544725181135"><a name="p40544725181135"></a><a name="p40544725181135"></a><strong id="b178411434203019"><a name="b178411434203019"></a><a name="b178411434203019"></a>/admin</strong></p>
    <p id="p14223101141616"><a name="p14223101141616"></a><a name="p14223101141616"></a>For example, if the URL to be protected is <span class="filepath" id="filepath14343134195810"><a name="filepath14343134195810"></a><a name="filepath14343134195810"></a><b>http://www.example.com/admin</b></span>, set <strong id="b9343124145815"><a name="b9343124145815"></a><a name="b9343124145815"></a>Path</strong> to <strong id="b4343164105816"><a name="b4343164105816"></a><a name="b4343164105816"></a>/admin</strong>.</p>
    </td>
    </tr>
    <tr id="row3251580618715"><td class="cellrowborder" valign="top" width="23.84%" headers="mcps1.2.4.1.1 "><p id="p1653459218715"><a name="p1653459218715"></a><a name="p1653459218715"></a>Event ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.21%" headers="mcps1.2.4.1.2 "><p id="p167454859433"><a name="p167454859433"></a><a name="p167454859433"></a>ID of a misreported event in <strong id="b1383471217119"><a name="b1383471217119"></a><a name="b1383471217119"></a>Events</strong> whose type is not <strong id="b58421127117"><a name="b58421127117"></a><a name="b58421127117"></a>Custom</strong>.</p>
    <p id="p173433969435"><a name="p173433969435"></a><a name="p173433969435"></a>Click <strong id="b84235270619268"><a name="b84235270619268"></a><a name="b84235270619268"></a>Handle False Alarm</strong> in the row containing the attack event to obtain the event ID.</p>
    <p id="p6423359118715"><a name="p6423359118715"></a><a name="p6423359118715"></a>This value consists of six digits and cannot be empty.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.95%" headers="mcps1.2.4.1.3 "><p id="p62897256181135"><a name="p62897256181135"></a><a name="p62897256181135"></a><strong id="b13249101223112"><a name="b13249101223112"></a><a name="b13249101223112"></a>000006</strong></p>
    </td>
    </tr>
    </tbody>
    </table>

8.  Click  **OK**. If  **Rule added successfully**  is displayed in the upper right corner, the rule is added.

    To delete the added rule, click  **Delete**  in the row containing the target rule.


