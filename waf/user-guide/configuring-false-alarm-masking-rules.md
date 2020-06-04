# Configuring False Alarm Masking Rules<a name="waf_01_0016"></a>

This section describes how to configure  false alarm masking  rules.

You can add false alarms to the whitelist and ignore certain event IDs \(for example, skip XSS check for a specified URL\).

False alarm masking only applies to events logged by built-in basic web protection rules. If you want to mask events logged by custom rules, delete the rules.

## Prerequisites<a name="section2256777914731"></a>

-   Login credentials have been obtained.
-   The domain name to be protected has been created.

## Procedure<a name="section6607803193933"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Click  **Service List**  at the top of the page and choose  **Security**  \>  **Web Application Firewall**. In the navigation pane, choose  **Domains**. The  **Domains**  page is displayed, as shown in  [Figure 1](#waf_01_0008_fig164792010154510).

    **Figure  1**  Entrance to the domain configuration page<a name="waf_01_0008_fig164792010154510"></a>  
    ![](figures/entrance-to-the-domain-configuration-page.png "entrance-to-the-domain-configuration-page")

4.  In the  **Operation**  column of the row containing the target domain name, click  **Configure Policy**. The protection configuration page is displayed, as shown in  [Figure 2](#waf_01_0008_fig16197124372015).

    **Figure  2**  Protection configuration page<a name="waf_01_0008_fig16197124372015"></a>  
    ![](figures/protection-configuration-page.png "protection-configuration-page")

5.  <a name="li58723545102836"></a>In the  **False Alarm Masking**  configuration area, change  **Status**  as needed and then click  **Save**  in the upper right corner of the  **Protection Status**  list. In the dialog box displayed, click  **Yes**  to save the settings. Otherwise, click  **Cancel**. See  [Figure 3](#fig44151977327).

    **Figure  3**  False Alarm Masking configuration area<a name="fig44151977327"></a>  
    ![](figures/false-alarm-masking-configuration-area.png "false-alarm-masking-configuration-area")

6.  Click  **Customize Rule**. On the displayed page, click  **Add Rule**  in the upper left corner to add a false alarm masking rule. See  [Figure 4](#fig106802271583).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If you do not click  **Save**  after changing  **Status**  in  [step 5](#li58723545102836), the  **Warning**  dialog box is displayed when you click  **Customize Rule**.  
    >-   Click  **Yes**  to cancel the previous settings.  
    >-   Click  **No**  and then  **Save**  to save the settings.  

    **Figure  4**  Add Rule \(False Alarm Masking\)<a name="fig106802271583"></a>  
    ![](figures/add-rule-(false-alarm-masking).png "add-rule-(false-alarm-masking)")

7.  In the displayed dialog box shown in  [Figure 5](#fig14415389105236), specify the parameters by referring to  [Table 1](#table4696626918715).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >False alarm masking only applies to events logged by built-in basic web protection rules. If you want to mask events logged by custom rules, delete the rules.  

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
    <td class="cellrowborder" valign="top" width="44.21%" headers="mcps1.2.4.1.2 "><p id="p167454859433"><a name="p167454859433"></a><a name="p167454859433"></a>ID of the built-in rule corresponding to the attack event for which the false alarm masking is to be performed</p>
    <p id="p6423359118715"><a name="p6423359118715"></a><a name="p6423359118715"></a>This value consists of six digits and cannot be empty.</p>
    <div class="note" id="note15329144717121"><a name="note15329144717121"></a><a name="note15329144717121"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p23323472126"><a name="p23323472126"></a><a name="p23323472126"></a>To obtain the event ID, go to the <strong id="b3808145084718"><a name="b3808145084718"></a><a name="b3808145084718"></a>Events</strong> page, select the <strong id="b17809175024718"><a name="b17809175024718"></a><a name="b17809175024718"></a>Search</strong> tab, locate the row where the attack event resides, and click <strong id="b1810115012472"><a name="b1810115012472"></a><a name="b1810115012472"></a>Handle False Alarm</strong> in the <strong id="b081075018472"><a name="b081075018472"></a><a name="b081075018472"></a>Operation</strong> column. You can then obtain the event ID on the displayed dialog box.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="31.95%" headers="mcps1.2.4.1.3 "><p id="p62897256181135"><a name="p62897256181135"></a><a name="p62897256181135"></a><strong id="b13249101223112"><a name="b13249101223112"></a><a name="b13249101223112"></a>000006</strong></p>
    </td>
    </tr>
    </tbody>
    </table>

8.  Click  **OK**. If  **Rule added successfully**  is displayed in the upper right corner, the rule is added.

    To delete the added rule, click  **Delete**  in the row containing the target rule.


