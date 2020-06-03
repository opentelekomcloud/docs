# Configuring Precise Protection Rules<a name="waf_01_0010"></a>

This section describes how to configure  precise protection  rules.

With these rules, WAF allows you to customize combinations of HTTP headers, cookies, URLs, request parameters, and IP addresses, improving defense accuracy.

## Prerequisites<a name="section2256777914731"></a>

-   Login credentials have been obtained.
-   The domain name to be protected has been created.

## Procedure<a name="section61533550183130"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Click  **Service List**  at the top of the page and choose  **Security**  \>  **Web Application Firewall**. In the navigation pane, choose  **Domains**. The  **Domains**  page is displayed, as shown in  [Figure 1](#waf_01_0008_fig164792010154510).

    **Figure  1**  Entrance to the domain configuration page<a name="waf_01_0008_fig164792010154510"></a>  
    ![](figures/entrance-to-the-domain-configuration-page.png "entrance-to-the-domain-configuration-page")

4.  In the  **Operation**  column of the row containing the target domain name, click  **Configure Policy**. The protection configuration page is displayed, as shown in  [Figure 2](#waf_01_0008_fig16197124372015).

    **Figure  2**  Protection configuration page<a name="waf_01_0008_fig16197124372015"></a>  
    ![](figures/protection-configuration-page.png "protection-configuration-page")

5.  <a name="li58723545102836"></a>In the  **Precise Protection**  configuration area, change  **Status**  as needed and then click  **Save**  in the upper right corner of the  **Protection Status**  list. In the dialog box displayed, click  **Yes**  to save the settings. Otherwise, click  **Cancel**. See  [Figure 3](#fig275911394277).

    **Figure  3**  Precise Protection configuration area<a name="fig275911394277"></a>  
    ![](figures/precise-protection-configuration-area.png "precise-protection-configuration-area")

6.  Click  **Customize Rule**. On the displayed page, set  **Detection Mode**. See  [Figure 4](#fig104318414612).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If you do not click  **Save**  after changing  **Status**  in  [step 5](#li58723545102836), the  **Warning**  dialog box is displayed when you click  **Customize Rule**.  
    >-   Click  **Yes**  to cancel the previous settings.  
    >-   Click  **No**  and then  **Save**  to save the settings.  

    Two detection modes are available:

    -   Instant Detection immediately ends threat detection after blocking a request that meets Precise Protection specified conditions.
    -   Full Detection finishes all threat detections before blocking requests that meet Precise Protection specified conditions.

    The default detection mode is  **Instant Detection**. After changing a detection mode, click  **Save**.

    **Figure  4**  Setting Detection Mode<a name="fig104318414612"></a>  
    ![](figures/setting-detection-mode.png "setting-detection-mode")

7.  In the upper left corner of the  **Precise Protection**  page, click  **Add Rule**. See  [Figure 5](#fig124514224012).

    **Figure  5**  Add Rule \(Precise Protection\)<a name="fig124514224012"></a>  
    ![](figures/add-rule-(precise-protection).png "add-rule-(precise-protection)")

8.  In the displayed dialog box shown in  [Figure 6](#fig39459217174738), specify the parameters by referring to  [Table 1](#table2299936310457).

    **Figure  6**  Adding a precise protection rule<a name="fig39459217174738"></a>  
    ![](figures/adding-a-precise-protection-rule.png "adding-a-precise-protection-rule")

    **Table  1**  Rule parameters

    <a name="table2299936310457"></a>
    <table><thead align="left"><tr id="row6587906910457"><th class="cellrowborder" valign="top" width="14.31%" id="mcps1.2.4.1.1"><p id="p4300370110457"><a name="p4300370110457"></a><a name="p4300370110457"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.24999999999999%" id="mcps1.2.4.1.2"><p id="p6074778910457"><a name="p6074778910457"></a><a name="p6074778910457"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="34.44%" id="mcps1.2.4.1.3"><p id="p49407333103735"><a name="p49407333103735"></a><a name="p49407333103735"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row135917531044"><td class="cellrowborder" valign="top" width="14.31%" headers="mcps1.2.4.1.1 "><p id="p185920531448"><a name="p185920531448"></a><a name="p185920531448"></a>Rule Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.24999999999999%" headers="mcps1.2.4.1.2 "><p id="p35922536413"><a name="p35922536413"></a><a name="p35922536413"></a>Customizable rule name</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.44%" headers="mcps1.2.4.1.3 "><p id="p7592175315417"><a name="p7592175315417"></a><a name="p7592175315417"></a><strong id="b842352706175632"><a name="b842352706175632"></a><a name="b842352706175632"></a>test-gz1</strong></p>
    </td>
    </tr>
    <tr id="row985919110457"><td class="cellrowborder" valign="top" width="14.31%" headers="mcps1.2.4.1.1 "><p id="p6039702210457"><a name="p6039702210457"></a><a name="p6039702210457"></a>Protective Action</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.24999999999999%" headers="mcps1.2.4.1.2 "><p id="p6032064210457"><a name="p6032064210457"></a><a name="p6032064210457"></a>Its value is <strong id="b84235270612506"><a name="b84235270612506"></a><a name="b84235270612506"></a>Block</strong> or <strong id="b84235270612509"><a name="b84235270612509"></a><a name="b84235270612509"></a>Allow</strong>. The default value is <strong id="b19967114335620"><a name="b19967114335620"></a><a name="b19967114335620"></a>Block</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.44%" headers="mcps1.2.4.1.3 "><p id="p42571074103735"><a name="p42571074103735"></a><a name="p42571074103735"></a><strong id="b842352706175637"><a name="b842352706175637"></a><a name="b842352706175637"></a>Block</strong></p>
    </td>
    </tr>
    <tr id="row67041622103812"><td class="cellrowborder" valign="top" width="14.31%" headers="mcps1.2.4.1.1 "><p id="p6704202210380"><a name="p6704202210380"></a><a name="p6704202210380"></a>Effective Since</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.24999999999999%" headers="mcps1.2.4.1.2 "><p id="p1070492283816"><a name="p1070492283816"></a><a name="p1070492283816"></a>Select <strong id="b84235270693153"><a name="b84235270693153"></a><a name="b84235270693153"></a>Immediately</strong> or select <strong id="b84235270693156"><a name="b84235270693156"></a><a name="b84235270693156"></a>Customize</strong> to set a period. This period can only be a time segment in the future.</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.44%" headers="mcps1.2.4.1.3 "><p id="p87041322113820"><a name="p87041322113820"></a><a name="p87041322113820"></a><strong id="b84235270693217"><a name="b84235270693217"></a><a name="b84235270693217"></a>Immediately</strong></p>
    </td>
    </tr>
    <tr id="row601487010457"><td class="cellrowborder" valign="top" width="14.31%" headers="mcps1.2.4.1.1 "><p id="p1744246310457"><a name="p1744246310457"></a><a name="p1744246310457"></a>Condition List</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.24999999999999%" headers="mcps1.2.4.1.2 "><div class="p" id="p355343310457"><a name="p355343310457"></a><a name="p355343310457"></a>Click <strong id="b81669187421"><a name="b81669187421"></a><a name="b81669187421"></a>Add</strong> to add conditions. You must add one to thirty conditions to a protection rule. If more than one condition is added, all the conditions must be met simultaneously for the rule to take effect.<a name="ul61829843104748"></a><a name="ul61829843104748"></a><ul id="ul61829843104748"><li><strong id="b842352706134812"><a name="b842352706134812"></a><a name="b842352706134812"></a>Field</strong></li><li><strong id="b136405281019"><a name="b136405281019"></a><a name="b136405281019"></a>Subfield</strong>: Configure this field only when <span class="parmvalue" id="parmvalue10793315133817"><a name="parmvalue10793315133817"></a><a name="parmvalue10793315133817"></a><b>Params</b></span>, <span class="parmvalue" id="parmvalue7793131533815"><a name="parmvalue7793131533815"></a><a name="parmvalue7793131533815"></a><b>Cookie</b></span>, or <span class="parmvalue" id="parmvalue242742372716"><a name="parmvalue242742372716"></a><a name="parmvalue242742372716"></a><b>Header</b></span> is selected.<div class="notice" id="note85400119109"><a name="note85400119109"></a><a name="note85400119109"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p954031113102"><a name="p954031113102"></a><a name="p954031113102"></a>The length of a subfield cannot exceed 2048 bytes. Only digits, letters, underscores (_), and hyphens (-) are allowed.</p>
    </div></div>
    </li><li><strong id="b14964124454514"><a name="b14964124454514"></a><a name="b14964124454514"></a>Logic</strong>: Select the desired logical relationship from the drop-down list.</li><li><strong id="b842352706125548"><a name="b842352706125548"></a><a name="b842352706125548"></a>Content</strong>: Enter or select the content of condition matching.</li></ul>
    </div>
    <div class="note" id="note661931813411"><a name="note661931813411"></a><a name="note661931813411"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p106195186413"><a name="p106195186413"></a><a name="p106195186413"></a>For detailed configurations, see <a href="#table13543174312394">Table 2</a>.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="34.44%" headers="mcps1.2.4.1.3 "><a name="ul13199878104428"></a><a name="ul13199878104428"></a><ul id="ul13199878104428"><li><strong id="b98121122152719"><a name="b98121122152719"></a><a name="b98121122152719"></a>Path</strong> <strong id="b312333372710"><a name="b312333372710"></a><a name="b312333372710"></a>Include</strong> <span class="parmvalue" id="parmvalue1914790105042"><a name="parmvalue1914790105042"></a><a name="parmvalue1914790105042"></a><b>/admin</b></span></li><li><strong id="b842352706125635"><a name="b842352706125635"></a><a name="b842352706125635"></a>User Agent</strong> <strong id="b842352706172915"><a name="b842352706172915"></a><a name="b842352706172915"></a>Prefix is not</strong> <strong id="b842352706125715"><a name="b842352706125715"></a><a name="b842352706125715"></a>mozilla/5.0</strong></li><li><strong id="b1140413892316"><a name="b1140413892316"></a><a name="b1140413892316"></a>IP</strong> <strong id="b46624355233"><a name="b46624355233"></a><a name="b46624355233"></a>Equal to</strong> <span class="parmvalue" id="parmvalue911917185191"><a name="parmvalue911917185191"></a><a name="parmvalue911917185191"></a><b>192.168.2.3</b></span></li><li><strong id="b842352706125722"><a name="b842352706125722"></a><a name="b842352706125722"></a>Cookie key1</strong> <strong id="b384491198125730"><a name="b384491198125730"></a><a name="b384491198125730"></a>Prefix is not</strong> <strong id="b842352706125739"><a name="b842352706125739"></a><a name="b842352706125739"></a>Nessus</strong></li></ul>
    </td>
    </tr>
    <tr id="row1662111271019"><td class="cellrowborder" valign="top" width="14.31%" headers="mcps1.2.4.1.1 "><p id="p10621172711012"><a name="p10621172711012"></a><a name="p10621172711012"></a>Priority</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.24999999999999%" headers="mcps1.2.4.1.2 "><p id="p1462172718019"><a name="p1462172718019"></a><a name="p1462172718019"></a>Priority of a rule being executed</p>
    <p id="p1199618571115"><a name="p1199618571115"></a><a name="p1199618571115"></a>Smaller values correspond to higher priorities. If two rules are assigned with the same priority, the rule added earlier has higher priority.</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.44%" headers="mcps1.2.4.1.3 "><p id="p662112271010"><a name="p662112271010"></a><a name="p662112271010"></a><strong id="b842352706174327"><a name="b842352706174327"></a><a name="b842352706174327"></a>5</strong></p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Condition list configurations

    <a name="table13543174312394"></a>
    <table><thead align="left"><tr id="row4545174315393"><th class="cellrowborder" valign="top" width="20.71792820717928%" id="mcps1.2.5.1.1"><p id="p754544383917"><a name="p754544383917"></a><a name="p754544383917"></a>Field</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.35746425357464%" id="mcps1.2.5.1.2"><p id="p25459434391"><a name="p25459434391"></a><a name="p25459434391"></a>Example Subfield</p>
    </th>
    <th class="cellrowborder" valign="top" width="28.947105289471054%" id="mcps1.2.5.1.3"><p id="p254519433398"><a name="p254519433398"></a><a name="p254519433398"></a>Logic</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.97750224977502%" id="mcps1.2.5.1.4"><p id="p198160263426"><a name="p198160263426"></a><a name="p198160263426"></a>Example Content</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1545114318391"><td class="cellrowborder" valign="top" width="20.71792820717928%" headers="mcps1.2.5.1.1 "><p id="p14545943123913"><a name="p14545943123913"></a><a name="p14545943123913"></a><strong id="b42111217155716"><a name="b42111217155716"></a><a name="b42111217155716"></a>Path</strong>: URL excluding a domain name. This value supports exact match only. That is, the path to be protected must match the path specified here. For example, if the path to be protected is <span class="parmvalue" id="parmvalue1768152135715"><a name="parmvalue1768152135715"></a><a name="parmvalue1768152135715"></a><b>/admin</b></span>, set <strong id="b7684121155720"><a name="b7684121155720"></a><a name="b7684121155720"></a>Path</strong> to <span class="parmvalue" id="parmvalue86861421185719"><a name="parmvalue86861421185719"></a><a name="parmvalue86861421185719"></a><b>/admin</b></span>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.35746425357464%" headers="mcps1.2.5.1.2 "><p id="p854510433396"><a name="p854510433396"></a><a name="p854510433396"></a>--</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.947105289471054%" headers="mcps1.2.5.1.3 "><p id="p16545643133913"><a name="p16545643133913"></a><a name="p16545643133913"></a><strong id="b1990475714378"><a name="b1990475714378"></a><a name="b1990475714378"></a>Include</strong>, <strong id="b17635093816"><a name="b17635093816"></a><a name="b17635093816"></a>Exclude</strong>, <strong id="b144676473817"><a name="b144676473817"></a><a name="b144676473817"></a>Equal to</strong>, <strong id="b2435208113811"><a name="b2435208113811"></a><a name="b2435208113811"></a>Not equal to</strong>, <strong id="b3608412113820"><a name="b3608412113820"></a><a name="b3608412113820"></a>Prefix is</strong>, <strong id="b189385269389"><a name="b189385269389"></a><a name="b189385269389"></a>Prefix is not</strong>, <strong id="b191173112387"><a name="b191173112387"></a><a name="b191173112387"></a>Suffix is</strong>, or <strong id="b9940345386"><a name="b9940345386"></a><a name="b9940345386"></a>Suffix is not</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="24.97750224977502%" headers="mcps1.2.5.1.4 "><p id="p3816126184210"><a name="p3816126184210"></a><a name="p3816126184210"></a><strong id="b1069515911449"><a name="b1069515911449"></a><a name="b1069515911449"></a>/buy/phone/</strong></p>
    </td>
    </tr>
    <tr id="row362081410432"><td class="cellrowborder" valign="top" width="20.71792820717928%" headers="mcps1.2.5.1.1 "><p id="p14550191054413"><a name="p14550191054413"></a><a name="p14550191054413"></a><strong id="b76123351226"><a name="b76123351226"></a><a name="b76123351226"></a>User Agent</strong>: A user agent of the scanner to be protected</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.35746425357464%" headers="mcps1.2.5.1.2 "><p id="p662081414436"><a name="p662081414436"></a><a name="p662081414436"></a>--</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.947105289471054%" headers="mcps1.2.5.1.3 "><p id="p573712375110"><a name="p573712375110"></a><a name="p573712375110"></a><strong id="b1375224318390"><a name="b1375224318390"></a><a name="b1375224318390"></a>Include</strong>, <strong id="b10752184353916"><a name="b10752184353916"></a><a name="b10752184353916"></a>Exclude</strong>, <strong id="b18752124333916"><a name="b18752124333916"></a><a name="b18752124333916"></a>Equal to</strong>, <strong id="b1976710434393"><a name="b1976710434393"></a><a name="b1976710434393"></a>Not equal to</strong>, <strong id="b576714317395"><a name="b576714317395"></a><a name="b576714317395"></a>Prefix is</strong>, <strong id="b47671443133912"><a name="b47671443133912"></a><a name="b47671443133912"></a>Prefix is not</strong>, <strong id="b8767124311397"><a name="b8767124311397"></a><a name="b8767124311397"></a>Suffix is</strong>, or <strong id="b11783124318398"><a name="b11783124318398"></a><a name="b11783124318398"></a>Suffix is not</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="24.97750224977502%" headers="mcps1.2.5.1.4 "><p id="p6620111410435"><a name="p6620111410435"></a><a name="p6620111410435"></a><strong id="b130712328562"><a name="b130712328562"></a><a name="b130712328562"></a>Mozilla/5.0 (Windows NT 6.1)</strong></p>
    </td>
    </tr>
    <tr id="row323411238439"><td class="cellrowborder" valign="top" width="20.71792820717928%" headers="mcps1.2.5.1.1 "><p id="p723419233430"><a name="p723419233430"></a><a name="p723419233430"></a><strong id="b162061481921"><a name="b162061481921"></a><a name="b162061481921"></a>IP</strong>: An IP address of the visitor to be protected</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.35746425357464%" headers="mcps1.2.5.1.2 "><p id="p1234152310436"><a name="p1234152310436"></a><a name="p1234152310436"></a>--</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.947105289471054%" headers="mcps1.2.5.1.3 "><p id="p9234122318430"><a name="p9234122318430"></a><a name="p9234122318430"></a><strong id="b12791842391"><a name="b12791842391"></a><a name="b12791842391"></a>Equal to</strong> or <strong id="b49415410397"><a name="b49415410397"></a><a name="b49415410397"></a>Not equal to</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="24.97750224977502%" headers="mcps1.2.5.1.4 "><p id="p423442318436"><a name="p423442318436"></a><a name="p423442318436"></a><strong id="b16001648161516"><a name="b16001648161516"></a><a name="b16001648161516"></a>192.168.2.3</strong></p>
    </td>
    </tr>
    <tr id="row17545184303914"><td class="cellrowborder" valign="top" width="20.71792820717928%" headers="mcps1.2.5.1.1 "><p id="p1654518431392"><a name="p1654518431392"></a><a name="p1654518431392"></a><strong id="b186907431422"><a name="b186907431422"></a><a name="b186907431422"></a>Params</strong>: A request parameter to be protected</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.35746425357464%" headers="mcps1.2.5.1.2 "><p id="p159120152001"><a name="p159120152001"></a><a name="p159120152001"></a><strong id="b9123926101519"><a name="b9123926101519"></a><a name="b9123926101519"></a>sttl</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="28.947105289471054%" headers="mcps1.2.5.1.3 "><p id="p15545164315393"><a name="p15545164315393"></a><a name="p15545164315393"></a><strong id="b1087765853920"><a name="b1087765853920"></a><a name="b1087765853920"></a>Include</strong>, <strong id="b587718583392"><a name="b587718583392"></a><a name="b587718583392"></a>Exclude</strong>, <strong id="b889375819394"><a name="b889375819394"></a><a name="b889375819394"></a>Equal to</strong>, <strong id="b18893458193918"><a name="b18893458193918"></a><a name="b18893458193918"></a>Not equal to</strong>, <strong id="b168931583396"><a name="b168931583396"></a><a name="b168931583396"></a>Prefix is</strong>, <strong id="b8893115812392"><a name="b8893115812392"></a><a name="b8893115812392"></a>Prefix is not</strong>, <strong id="b1908458173914"><a name="b1908458173914"></a><a name="b1908458173914"></a>Suffix is</strong>, or <strong id="b7908558143913"><a name="b7908558143913"></a><a name="b7908558143913"></a>Suffix is not</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="24.97750224977502%" headers="mcps1.2.5.1.4 "><p id="p124131623102"><a name="p124131623102"></a><a name="p124131623102"></a><strong id="b15732135131516"><a name="b15732135131516"></a><a name="b15732135131516"></a>201901150929</strong></p>
    </td>
    </tr>
    <tr id="row15281420164313"><td class="cellrowborder" valign="top" width="20.71792820717928%" headers="mcps1.2.5.1.1 "><p id="p8281172044315"><a name="p8281172044315"></a><a name="p8281172044315"></a><strong id="b18627194144014"><a name="b18627194144014"></a><a name="b18627194144014"></a>Cookie</strong>: A small piece of data to identify web visitors</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.35746425357464%" headers="mcps1.2.5.1.2 "><p id="p7281192015435"><a name="p7281192015435"></a><a name="p7281192015435"></a><strong id="b59723484424"><a name="b59723484424"></a><a name="b59723484424"></a>name</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="28.947105289471054%" headers="mcps1.2.5.1.3 "><p id="p1969715507264"><a name="p1969715507264"></a><a name="p1969715507264"></a><strong id="b7707133513405"><a name="b7707133513405"></a><a name="b7707133513405"></a>Include</strong>, <strong id="b972213574011"><a name="b972213574011"></a><a name="b972213574011"></a>Exclude</strong>, <strong id="b1472273534020"><a name="b1472273534020"></a><a name="b1472273534020"></a>Equal to</strong>, <strong id="b187222356406"><a name="b187222356406"></a><a name="b187222356406"></a>Not equal to</strong>, <strong id="b14722635204010"><a name="b14722635204010"></a><a name="b14722635204010"></a>Prefix is</strong>, <strong id="b1273843514020"><a name="b1273843514020"></a><a name="b1273843514020"></a>Prefix is not</strong>, <strong id="b673813584016"><a name="b673813584016"></a><a name="b673813584016"></a>Suffix is</strong>, or <strong id="b10738143514013"><a name="b10738143514013"></a><a name="b10738143514013"></a>Suffix is not</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="24.97750224977502%" headers="mcps1.2.5.1.4 "><p id="p19281162034311"><a name="p19281162034311"></a><a name="p19281162034311"></a><strong id="b518161011435"><a name="b518161011435"></a><a name="b518161011435"></a>Nessus</strong></p>
    </td>
    </tr>
    <tr id="row4281142015438"><td class="cellrowborder" valign="top" width="20.71792820717928%" headers="mcps1.2.5.1.1 "><p id="p1328162011433"><a name="p1328162011433"></a><a name="p1328162011433"></a><strong id="b1433018561622"><a name="b1433018561622"></a><a name="b1433018561622"></a>Referer</strong>: A user-defined request resource</p>
    <p id="p3649202911486"><a name="p3649202911486"></a><a name="p3649202911486"></a>For example, if the protected path is <strong id="b97241919319"><a name="b97241919319"></a><a name="b97241919319"></a>/admin/xxx</strong> and you do not want visitors to access the page from <strong id="b77240192114"><a name="b77240192114"></a><a name="b77240192114"></a>www.test.com</strong>, set <strong id="b1372416191110"><a name="b1372416191110"></a><a name="b1372416191110"></a>Content</strong> to <strong id="b117249191210"><a name="b117249191210"></a><a name="b117249191210"></a>http://www.test.com</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.35746425357464%" headers="mcps1.2.5.1.2 "><p id="p828102017432"><a name="p828102017432"></a><a name="p828102017432"></a>--</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.947105289471054%" headers="mcps1.2.5.1.3 "><p id="p149508393243"><a name="p149508393243"></a><a name="p149508393243"></a><strong id="b918015534418"><a name="b918015534418"></a><a name="b918015534418"></a>Include</strong>, <strong id="b161807574416"><a name="b161807574416"></a><a name="b161807574416"></a>Exclude</strong>, <strong id="b418018519442"><a name="b418018519442"></a><a name="b418018519442"></a>Equal to</strong>, <strong id="b9180175154420"><a name="b9180175154420"></a><a name="b9180175154420"></a>Not equal to</strong>, <strong id="b61801851445"><a name="b61801851445"></a><a name="b61801851445"></a>Prefix is</strong>, <strong id="b819616510448"><a name="b819616510448"></a><a name="b819616510448"></a>Prefix is not</strong>, <strong id="b8196135184411"><a name="b8196135184411"></a><a name="b8196135184411"></a>Suffix is</strong>, or <strong id="b171961056443"><a name="b171961056443"></a><a name="b171961056443"></a>Suffix is not</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="24.97750224977502%" headers="mcps1.2.5.1.4 "><p id="p01281435201914"><a name="p01281435201914"></a><a name="p01281435201914"></a><strong id="b121911376714"><a name="b121911376714"></a><a name="b121911376714"></a>http://www.test.com</strong></p>
    </td>
    </tr>
    <tr id="row22811220114314"><td class="cellrowborder" valign="top" width="20.71792820717928%" headers="mcps1.2.5.1.1 "><p id="p4281120114316"><a name="p4281120114316"></a><a name="p4281120114316"></a><strong id="b1472121436"><a name="b1472121436"></a><a name="b1472121436"></a>Header</strong>: A user-defined HTTP header</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.35746425357464%" headers="mcps1.2.5.1.2 "><p id="p8281132010435"><a name="p8281132010435"></a><a name="p8281132010435"></a><strong id="b420012352169"><a name="b420012352169"></a><a name="b420012352169"></a>Accept</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="28.947105289471054%" headers="mcps1.2.5.1.3 "><p id="p945414713275"><a name="p945414713275"></a><a name="p945414713275"></a><strong id="b41447443610"><a name="b41447443610"></a><a name="b41447443610"></a>Include</strong>, <strong id="b201445444618"><a name="b201445444618"></a><a name="b201445444618"></a>Exclude</strong>, <strong id="b814415441066"><a name="b814415441066"></a><a name="b814415441066"></a>Equal to</strong>, <strong id="b914414441614"><a name="b914414441614"></a><a name="b914414441614"></a>Not equal to</strong>, <strong id="b0144044968"><a name="b0144044968"></a><a name="b0144044968"></a>Prefix is</strong>, <strong id="b2014413441760"><a name="b2014413441760"></a><a name="b2014413441760"></a>Prefix is not</strong>, <strong id="b714418447620"><a name="b714418447620"></a><a name="b714418447620"></a>Suffix is</strong>, or <strong id="b91448441961"><a name="b91448441961"></a><a name="b91448441961"></a>Suffix is not</strong></p>
    </td>
    <td class="cellrowborder" valign="top" width="24.97750224977502%" headers="mcps1.2.5.1.4 "><p id="p2028152064316"><a name="p2028152064316"></a><a name="p2028152064316"></a><strong id="b10842145118168"><a name="b10842145118168"></a><a name="b10842145118168"></a>text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8</strong></p>
    </td>
    </tr>
    </tbody>
    </table>

9.  Click  **OK**.
    -   To modify the added rule, click  **Modify**  in the row containing the target rule.
    -   To delete the added rule, click  **Delete**  in the row containing the target rule.


