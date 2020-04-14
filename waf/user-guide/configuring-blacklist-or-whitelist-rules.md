# Configuring Blacklist or Whitelist Rules<a name="EN-US_TOPIC_0193630267"></a>

This section describes how to configure  blacklist or whitelist  rules to block or allow specific IP addresses or address ranges.

Blacklist and Whitelist  only takes effect for specified domain names.

## Prerequisites<a name="section2256777914731"></a>

-   Login credentials have been obtained.
-   The domain name to be protected has been created.

## Procedure<a name="section61533550183130"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Click  **Service List**  at the top of the page and choose  **Security**  \>  **Web Application Firewall**. In the navigation pane, choose  **Domains**. The  **Domains**  page is displayed, as shown in  [Figure 1](#en-us_topic_0193630287_fig4838162174519).

    **Figure  1**  Domains<a name="en-us_topic_0193630287_fig4838162174519"></a>  
    ![](figures/domains-policy.png "domains-policy")

4.  In the  **Operation**  column of the row containing the target domain name, click  **Configure Policy**. The protection configuration page is displayed, as shown in  [Figure 2](#en-us_topic_0193630287_fig16197124372015).

    **Figure  2**  Protection configuration page<a name="en-us_topic_0193630287_fig16197124372015"></a>  
    ![](figures/protection-configuration-page.png "protection-configuration-page")

5.  <a name="li33536816115011"></a>In the  **Blacklist and Whitelist**  configuration area, change  **Status**  as needed and then click  **Save**  in the upper right corner of the  **Protection Status**  list. In the dialog box displayed, click  **Yes**  to save the settings. Otherwise, click  **Cancel**. See  [Figure 3](#fig0358162863015).

    **Figure  3**  Blacklist and Whitelist configuration area<a name="fig0358162863015"></a>  
    ![](figures/blacklist-and-whitelist-configuration-area.png "blacklist-and-whitelist-configuration-area")

6.  Click  **Customize Rule**. On the displayed page, click  **Add Rule**  in the upper left corner to add a blacklist or whitelist rule. See  [Figure 4](#fig337411411269).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If you do not click  **Save**  after changing  **Status**  in  [step 5](#li33536816115011), the  **Warning**  dialog box is displayed when you click  **Customize Rule**.  
    >-   Click  **Yes**  to cancel the previous settings.  
    >-   Click  **No**  and then  **Save**  to save the settings.  

    **Figure  4**  Add Rule \(blacklist or whitelist\)<a name="fig337411411269"></a>  
    ![](figures/add-rule-(blacklist-or-whitelist).png "add-rule-(blacklist-or-whitelist)")

7.  In the displayed dialog box shown in  [Figure 5](#fig22686744114137), specify the parameters by referring to  [Table 1](#table27095251482).

    **Figure  5**  Adding a blacklist or whitelist rule<a name="fig22686744114137"></a>  
    ![](figures/adding-a-blacklist-or-whitelist-rule.png "adding-a-blacklist-or-whitelist-rule")

    **Table  1**  Rule parameters

    <a name="table27095251482"></a>
    <table><thead align="left"><tr id="row137101425382"><th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.2.4.1.1"><p id="p7710142515815"><a name="p7710142515815"></a><a name="p7710142515815"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="36.583658365836584%" id="mcps1.2.4.1.2"><p id="p871117253815"><a name="p871117253815"></a><a name="p871117253815"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.604460446044605%" id="mcps1.2.4.1.3"><p id="p1571112518818"><a name="p1571112518818"></a><a name="p1571112518818"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20711192519818"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.4.1.1 "><p id="p77111025289"><a name="p77111025289"></a><a name="p77111025289"></a>IP Address or Range</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.583658365836584%" headers="mcps1.2.4.1.2 "><a name="ul129831037141019"></a><a name="ul129831037141019"></a><ul id="ul129831037141019"><li>IP address: IP address to be added to the blacklist or whitelist</li><li>IP address range: IP address and subnet mask defining a network segment</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="44.604460446044605%" headers="mcps1.2.4.1.3 "><a name="ul77819464108"></a><a name="ul77819464108"></a><ul id="ul77819464108"><li><strong id="b19851853123111"><a name="b19851853123111"></a><a name="b19851853123111"></a>192.168.2.3</strong></li><li><strong id="b132423494412"><a name="b132423494412"></a><a name="b132423494412"></a>10.1.1.0/24</strong></li></ul>
    </td>
    </tr>
    <tr id="row290515450818"><td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.2.4.1.1 "><p id="p790512451282"><a name="p790512451282"></a><a name="p790512451282"></a>Protective Action</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.583658365836584%" headers="mcps1.2.4.1.2 "><p id="p0906145582"><a name="p0906145582"></a><a name="p0906145582"></a>If <strong id="b256050404144042"><a name="b256050404144042"></a><a name="b256050404144042"></a>IP Address or Range</strong> is to be added to a whitelist, set this parameter to <strong id="b842352706144133"><a name="b842352706144133"></a><a name="b842352706144133"></a>Whitelist</strong>.</p>
    <p id="p678811254215"><a name="p678811254215"></a><a name="p678811254215"></a>If <strong id="b533344072144151"><a name="b533344072144151"></a><a name="b533344072144151"></a>IP Address or Range</strong> is to be added to a blacklist, set this parameter to <strong id="b1340077337144151"><a name="b1340077337144151"></a><a name="b1340077337144151"></a>Blacklist</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.604460446044605%" headers="mcps1.2.4.1.3 "><p id="p10436236121516"><a name="p10436236121516"></a><a name="p10436236121516"></a><span class="parmvalue" id="parmvalue18280195841"><a name="parmvalue18280195841"></a><a name="parmvalue18280195841"></a><b>Blacklist</b></span></p>
    </td>
    </tr>
    </tbody>
    </table>

8.  Click  **OK**.
    -   To modify the added rule, click  **Modify**  in the row containing the target rule.
    -   To delete the added rule, click  **Delete**  in the row containing the target rule.


