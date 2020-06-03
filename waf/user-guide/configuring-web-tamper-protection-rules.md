# Configuring Web Tamper Protection Rules<a name="waf_01_0014"></a>

This section describes how to configure  web tamper protection \(WTP\)  rules.

You can configure these rules to prevent a static webpage from being tampered with.

WTP has the following advantages:

-   Quicker response to requests

    After a WTP rule is configured, WAF caches the static webpage on the server. When receiving a request from a web visitor, WAF returns the cached page to the visitor.

-   Web tamper protection

    If an attacker modifies a static webpage on the server, WAF returns the cached original webpage to web visitors, ensuring that visitors never access tampered-with pages.

    WAF can randomly extract a request from a web visitor to compare the requested page with the webpage on the server. If WAF detects that the page has been tampered with, it notifies the user by SMS or email. For details about alarm notification settings, see  [Enabling Alarm Notification](enabling-alarm-notification.md).


## Prerequisites<a name="section58249606174339"></a>

-   Login credentials have been obtained.
-   The domain name to be protected has been created.

## Procedure<a name="section613293693121"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Click  **Service List**  at the top of the page and choose  **Security**  \>  **Web Application Firewall**. In the navigation pane, choose  **Domains**. The  **Domains**  page is displayed, as shown in  [Figure 1](#waf_01_0008_fig164792010154510).

    **Figure  1**  Entrance to the domain configuration page<a name="waf_01_0008_fig164792010154510"></a>  
    ![](figures/entrance-to-the-domain-configuration-page.png "entrance-to-the-domain-configuration-page")

4.  In the  **Operation**  column of the row containing the target domain name, click  **Configure Policy**. The protection configuration page is displayed, as shown in  [Figure 2](#waf_01_0008_fig16197124372015).

    **Figure  2**  Protection configuration page<a name="waf_01_0008_fig16197124372015"></a>  
    ![](figures/protection-configuration-page.png "protection-configuration-page")

5.  <a name="li58723545102836"></a>In the  **Web Tamper Protection**  configuration area, change  **Status**  as needed and then click  **Save**  in the upper right corner of the  **Protection Status**  list. In the dialog box displayed, click  **Yes**  to save the settings. Otherwise, click  **Cancel**. See  [Figure 3](#fig10572033304).

    **Figure  3**  Web Tamper Protection configuration area<a name="fig10572033304"></a>  
    ![](figures/web-tamper-protection-configuration-area.png "web-tamper-protection-configuration-area")

6.  Click  **Customize Rule**. On the displayed page, click  **Add Rule**  in the upper left corner to add a web tamper protection rule. See  [Figure 4](#fig13289432775).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If you do not click  **Save**  after changing  **Status**  in  [step 5](#li58723545102836), the  **Warning**  dialog box is displayed when you click  **Customize Rule**.  
    >-   Click  **Yes**  to cancel the previous settings.  
    >-   Click  **No**  and then  **Save**  to save the settings.  

    **Figure  4**  Add Rule \(Web Tamper Protection\)<a name="fig13289432775"></a>  
    ![](figures/add-rule-(web-tamper-protection).png "add-rule-(web-tamper-protection)")

7.  In the displayed dialog box shown in  [Figure 5](#fig13729129125420), specify the parameters by referring to  [Table 1](#table2046816299203).

    **Figure  5**  Adding a web tamper protection rule<a name="fig13729129125420"></a>  
    ![](figures/adding-a-web-tamper-protection-rule.png "adding-a-web-tamper-protection-rule")

    **Table  1**  Rule parameters

    <a name="table2046816299203"></a>
    <table><thead align="left"><tr id="row546914299207"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p2046911299201"><a name="p2046911299201"></a><a name="p2046911299201"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="37.15%" id="mcps1.2.4.1.2"><p id="p1646915299201"><a name="p1646915299201"></a><a name="p1646915299201"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="39.85%" id="mcps1.2.4.1.3"><p id="p18470929192015"><a name="p18470929192015"></a><a name="p18470929192015"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13866404146"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p15386184091420"><a name="p15386184091420"></a><a name="p15386184091420"></a>Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.15%" headers="mcps1.2.4.1.2 "><p id="p772611281566"><a name="p772611281566"></a><a name="p772611281566"></a>Domain name to be protected</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p113861340181412"><a name="p113861340181412"></a><a name="p113861340181412"></a><strong id="b17216759131516"><a name="b17216759131516"></a><a name="b17216759131516"></a>www.example.com</strong></p>
    </td>
    </tr>
    <tr id="row1247062911209"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p4470122917203"><a name="p4470122917203"></a><a name="p4470122917203"></a>Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.15%" headers="mcps1.2.4.1.2 "><p id="p54707298202"><a name="p54707298202"></a><a name="p54707298202"></a>URL excluding a domain name</p>
    <div class="note" id="note62479477297"><a name="note62479477297"></a><a name="note62479477297"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul20707155819344"></a><a name="ul20707155819344"></a><ul id="ul20707155819344"><li>The path does not support regular expressions.</li><li>The path cannot contain two or more consecutive slashes. For example, <span class="parmvalue" id="parmvalue388515306519"><a name="parmvalue388515306519"></a><a name="parmvalue388515306519"></a><b>///admin</b></span>. If you enter <strong id="b1188518304517"><a name="b1188518304517"></a><a name="b1188518304517"></a>///admin</strong>, the WAF engine converts <strong id="b38850301511"><a name="b38850301511"></a><a name="b38850301511"></a>///</strong> to <strong id="b168856302052"><a name="b168856302052"></a><a name="b168856302052"></a>/</strong>.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="39.85%" headers="mcps1.2.4.1.3 "><p id="p1345741151911"><a name="p1345741151911"></a><a name="p1345741151911"></a><strong id="b177644110299"><a name="b177644110299"></a><a name="b177644110299"></a>/admin</strong></p>
    <p id="p1047152952012"><a name="p1047152952012"></a><a name="p1047152952012"></a>For example, if the URL to be protected is <span class="filepath" id="filepath1627493212383"><a name="filepath1627493212383"></a><a name="filepath1627493212383"></a><b>http://www.example.com/admin</b></span>, set <strong id="b19427477917"><a name="b19427477917"></a><a name="b19427477917"></a>Path</strong> to <strong id="b1885651497"><a name="b1885651497"></a><a name="b1885651497"></a>/admin</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

8.  Click  **OK**.
    -   In the event of changes on the protected webpage, WAF needs to re-cache the webpage content. In this case, click  **Update Cache**  in the row containing the target rule.
    -   To delete the added rule, click  **Delete**  in the row containing the target rule.


