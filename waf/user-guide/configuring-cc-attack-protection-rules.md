# Configuring CC Attack Protection Rules<a name="waf_01_0009"></a>

This section describes how to configure CC attack protection rules.

With these rules, rate limiting policies are set based on the IP addresses, cookies, or Referer field to accurately identify and mitigate  CC attacks.

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

5.  <a name="li54077254163213"></a>In the  **CC Attack Protection**  configuration area, change  **Status**  as needed and then click  **Save**  in the upper right corner of the  **Protection Status**  list. In the dialog box displayed, click  **Yes**  to save the settings. Otherwise, click  **Cancel**. See  [Figure 3](#fig102851827142620).

    **Figure  3**  CC Attack Protection configuration area<a name="fig102851827142620"></a>  
    ![](figures/cc-attack-protection-configuration-area.png "cc-attack-protection-configuration-area")

6.  Click  **Customize Rule**. On the displayed page, click  **Add Rule**  in the upper left corner to add a CC attack protection rule. See  [Figure 4](#fig115115503317).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If you do not click  **Save**  after changing  **Status**  in  [step 5](#li54077254163213), the  **Warning**  dialog box is displayed when you click  **Customize Rule**.  
    >-   Click  **Yes**  to cancel the previous settings.  
    >-   Click  **No**  and then  **Save**  to save the settings.  

    WAF creates a default CC attack protection rule. The rule can be modified but cannot be deleted.  **Rate Limit**  in the rule is 500 requests/5 seconds by default and it can be adjusted up to 10000 requests/5 seconds. If you want a higher rate limit than the maximum value, contact the administrator.

    **Figure  4**  Add Rule \(CC Attack Protection\)<a name="fig115115503317"></a>  
    ![](figures/add-rule-(cc-attack-protection).png "add-rule-(cc-attack-protection)")

7.  In the displayed dialog box shown in  [Figure 5](#fig8736181862118), specify the parameters by referring to  [Table 1](#table19744111819217).

    **Figure  5**  Adding a CC attack protection rule<a name="fig8736181862118"></a>  
    ![](figures/adding-a-cc-attack-protection-rule.png "adding-a-cc-attack-protection-rule")

    **Table  1**  Rule parameters

    <a name="table19744111819217"></a>
    <table><thead align="left"><tr id="row137372018152111"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.1"><p id="p1773791892116"><a name="p1773791892116"></a><a name="p1773791892116"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.88%" id="mcps1.2.4.1.2"><p id="p27379188215"><a name="p27379188215"></a><a name="p27379188215"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.12%" id="mcps1.2.4.1.3"><p id="p8737181818212"><a name="p8737181818212"></a><a name="p8737181818212"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1373871812117"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p1373751862112"><a name="p1373751862112"></a><a name="p1373751862112"></a>Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.88%" headers="mcps1.2.4.1.2 "><p id="p37371318202111"><a name="p37371318202111"></a><a name="p37371318202111"></a>URL excluding a domain name</p>
    <a name="ul1515617591337"></a><a name="ul1515617591337"></a><ul id="ul1515617591337"><li>Prefix match: The path ending with * indicates that the path is used as a prefix. For example, if the path to be protected is <strong id="b147631916184_1"><a name="b147631916184_1"></a><a name="b147631916184_1"></a>/admin/test.php</strong> or <strong id="b1368516691812_1"><a name="b1368516691812_1"></a><a name="b1368516691812_1"></a>/adminabc</strong>, set <strong id="b3514135671817_1"><a name="b3514135671817_1"></a><a name="b3514135671817_1"></a>Path</strong> to <span class="parmvalue" id="parmvalue12617113514412_2"><a name="parmvalue12617113514412_2"></a><a name="parmvalue12617113514412_2"></a><b>/admin*</b></span>.</li><li>Exact match: The path to be entered must match the path to be protected. If the path to be protected is <span class="parmvalue" id="parmvalue1760919669113230"><a name="parmvalue1760919669113230"></a><a name="parmvalue1760919669113230"></a><b>/admin</b></span>, set <strong id="b842352706142234"><a name="b842352706142234"></a><a name="b842352706142234"></a>Path</strong> to <span class="parmvalue" id="parmvalue1062412806113239"><a name="parmvalue1062412806113239"></a><a name="parmvalue1062412806113239"></a><b>/admin</b></span>.</li></ul>
    <div class="note" id="note0434164315340"><a name="note0434164315340"></a><a name="note0434164315340"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul20707155819344"></a><a name="ul20707155819344"></a><ul id="ul20707155819344"><li>The path supports prefix and exact matches only and does not support regular expressions.</li><li>The path cannot contain two or more consecutive slashes. For example, <span class="parmvalue" id="parmvalue750983013418"><a name="parmvalue750983013418"></a><a name="parmvalue750983013418"></a><b>///admin</b></span>. If you enter <strong id="b7509330174115"><a name="b7509330174115"></a><a name="b7509330174115"></a>///admin</strong>, the WAF engine converts <strong id="b8509153018410"><a name="b8509153018410"></a><a name="b8509153018410"></a>///</strong> to <strong id="b1150911301417"><a name="b1150911301417"></a><a name="b1150911301417"></a>/</strong>.</li></ul>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="30.12%" headers="mcps1.2.4.1.3 "><p id="p1173811852111"><a name="p1173811852111"></a><a name="p1173811852111"></a><strong id="b474314318528"><a name="b474314318528"></a><a name="b474314318528"></a>/admin*</strong></p>
    </td>
    </tr>
    <tr id="row1773971812119"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p773811822118"><a name="p773811822118"></a><a name="p773811822118"></a>Rate Limit Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.88%" headers="mcps1.2.4.1.2 "><a name="ul77394180214"></a><a name="ul77394180214"></a><ul id="ul77394180214"><li><strong id="b842352706113154"><a name="b842352706113154"></a><a name="b842352706113154"></a>Per IP address</strong>: A web visitor is identified by the IP address.</li><li><strong id="b84235270617197"><a name="b84235270617197"></a><a name="b84235270617197"></a>Per user</strong>: A web visitor is identified by the cookie key value.</li><li><strong id="b13627924151612"><a name="b13627924151612"></a><a name="b13627924151612"></a>Other</strong>: A web visitor is identified by the Referer field (user-defined request source).<div class="note" id="note8678492076"><a name="note8678492076"></a><a name="note8678492076"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p068134920713"><a name="p068134920713"></a><a name="p068134920713"></a>If <strong id="b1419813094415"><a name="b1419813094415"></a><a name="b1419813094415"></a>Rate Limit Mode</strong> is <strong id="b1726153412446"><a name="b1726153412446"></a><a name="b1726153412446"></a>Other</strong>, <strong id="b11679262444"><a name="b11679262444"></a><a name="b11679262444"></a>Content</strong> of <strong id="b026113854417"><a name="b026113854417"></a><a name="b026113854417"></a>Referer</strong> is set to a complete URL containing the domain name. The <strong id="b2046414444510"><a name="b2046414444510"></a><a name="b2046414444510"></a>Content</strong> field supports prefix match and exact match only, and cannot contain two or more consecutive slashes, for example, <strong id="b105281836144615"><a name="b105281836144615"></a><a name="b105281836144615"></a>///admin</strong>. If you enter <strong id="b2279355194618"><a name="b2279355194618"></a><a name="b2279355194618"></a>///admin</strong>, the WAF engine converts it to <strong id="b321772064712"><a name="b321772064712"></a><a name="b321772064712"></a>/admin</strong>.</p>
    <p id="p12718311202113"><a name="p12718311202113"></a><a name="p12718311202113"></a>For example, if <strong id="b12025287466"><a name="b12025287466"></a><a name="b12025287466"></a>Path</strong> is <strong id="b63908694613"><a name="b63908694613"></a><a name="b63908694613"></a>/admin</strong> and you do not want visitors to access the page from <strong id="b93901634612"><a name="b93901634612"></a><a name="b93901634612"></a>www.test.com</strong>, set <strong id="b183902604610"><a name="b183902604610"></a><a name="b183902604610"></a>Content</strong> to <strong id="b239018610464"><a name="b239018610464"></a><a name="b239018610464"></a>http://www.test.com</strong>.</p>
    </div></div>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="30.12%" headers="mcps1.2.4.1.3 "><p id="p12641105306"><a name="p12641105306"></a><a name="p12641105306"></a><strong id="b18912182193618"><a name="b18912182193618"></a><a name="b18912182193618"></a>Per user</strong></p>
    </td>
    </tr>
    <tr id="row8739818162118"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p1073931852111"><a name="p1073931852111"></a><a name="p1073931852111"></a>User Identifier</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.88%" headers="mcps1.2.4.1.2 "><p id="p87395187212"><a name="p87395187212"></a><a name="p87395187212"></a>A cookie field that you need to set if <strong id="b1482117374596"><a name="b1482117374596"></a><a name="b1482117374596"></a>Rate Limit Mode</strong> is <strong id="b158297373595"><a name="b158297373595"></a><a name="b158297373595"></a>Per user</strong>. This value supports exact match only and does not support regular expressions.</p>
    <p id="p1573911812216"><a name="p1573911812216"></a><a name="p1573911812216"></a>If a website uses the <strong id="b328185111497"><a name="b328185111497"></a><a name="b328185111497"></a>name</strong> field in the cookie to uniquely identify a web visitor, enter <strong id="b1319481524"><a name="b1319481524"></a><a name="b1319481524"></a>name</strong>. If you do not set this value, WAF will automatically assign one.</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.12%" headers="mcps1.2.4.1.3 "><p id="p47391018152116"><a name="p47391018152116"></a><a name="p47391018152116"></a><strong id="b842352706175455"><a name="b842352706175455"></a><a name="b842352706175455"></a>name</strong></p>
    </td>
    </tr>
    <tr id="row0741101862119"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p16739181862117"><a name="p16739181862117"></a><a name="p16739181862117"></a>Rate Limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.88%" headers="mcps1.2.4.1.2 "><p id="p0741618112115"><a name="p0741618112115"></a><a name="p0741618112115"></a>Number of requests allowed from a web visitor in the rate limiting period. The visitor's access request is denied if the limit is reached. </p>
    </td>
    <td class="cellrowborder" valign="top" width="30.12%" headers="mcps1.2.4.1.3 "><p id="p574111815216"><a name="p574111815216"></a><a name="p574111815216"></a><strong id="b418225811492"><a name="b418225811492"></a><a name="b418225811492"></a>10</strong> requests <strong id="b1128928504"><a name="b1128928504"></a><a name="b1128928504"></a>60</strong> seconds</p>
    </td>
    </tr>
    <tr id="row6741418122113"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p3741181822119"><a name="p3741181822119"></a><a name="p3741181822119"></a>Protective Action</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.88%" headers="mcps1.2.4.1.2 "><p id="p1474151814212"><a name="p1474151814212"></a><a name="p1474151814212"></a>Action to perform if the maximum number of requests is reached. Options are <strong id="b842352706113641"><a name="b842352706113641"></a><a name="b842352706113641"></a>Verification code</strong> and <strong id="b842352706113644"><a name="b842352706113644"></a><a name="b842352706113644"></a>Block</strong>.</p>
    <a name="ul374111183213"></a><a name="ul374111183213"></a><ul id="ul374111183213"><li class="MsoBodyText"><strong id="b84235270616218"><a name="b84235270616218"></a><a name="b84235270616218"></a>Verification code</strong>: A verification code is displayed when the number of requests reaches the maximum limit within a specified period. Upon completing the verification, you are no longer restricted by the maximum number of requests allowed.</li><li class="MsoBodyText"><strong id="b84235270616156"><a name="b84235270616156"></a><a name="b84235270616156"></a>Block</strong>: Requests are blocked if the maximum number of requests is reached.<div class="note" id="note151854308411"><a name="note151854308411"></a><a name="note151854308411"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1918615300417"><a name="p1918615300417"></a><a name="p1918615300417"></a>If <strong id="b12911181920812"><a name="b12911181920812"></a><a name="b12911181920812"></a>Rate Limit Mode</strong> is <strong id="b179116192818"><a name="b179116192818"></a><a name="b179116192818"></a>Other</strong>, <strong id="b1091121919817"><a name="b1091121919817"></a><a name="b1091121919817"></a>Protective Action</strong> can only be <strong id="b1391131917811"><a name="b1391131917811"></a><a name="b1391131917811"></a>Block</strong>.</p>
    </div></div>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="30.12%" headers="mcps1.2.4.1.3 "><p id="p1774111819212"><a name="p1774111819212"></a><a name="p1774111819212"></a><strong id="b84235270617552"><a name="b84235270617552"></a><a name="b84235270617552"></a>Block</strong></p>
    </td>
    </tr>
    <tr id="row1274120181210"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p19741191892111"><a name="p19741191892111"></a><a name="p19741191892111"></a>Block Duration</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.88%" headers="mcps1.2.4.1.2 "><p id="p1774110185217"><a name="p1774110185217"></a><a name="p1774110185217"></a>Time required for the page to be restored to normal state after being blocked</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.12%" headers="mcps1.2.4.1.3 "><p id="p20741121822113"><a name="p20741121822113"></a><a name="p20741121822113"></a><strong id="b1014032417533"><a name="b1014032417533"></a><a name="b1014032417533"></a>600</strong> seconds</p>
    </td>
    </tr>
    <tr id="row8744101812218"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p1574181819218"><a name="p1574181819218"></a><a name="p1574181819218"></a>Block Page</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.88%" headers="mcps1.2.4.1.2 "><p id="p5743218112117"><a name="p5743218112117"></a><a name="p5743218112117"></a>Error page displayed when the maximum number of requests has been reached. This parameter is set only when <strong id="b185243972419"><a name="b185243972419"></a><a name="b185243972419"></a>Protective Action</strong> is <strong id="b875517426248"><a name="b875517426248"></a><a name="b875517426248"></a>Block</strong>.</p>
    <a name="ul15743111812116"></a><a name="ul15743111812116"></a><ul id="ul15743111812116"><li>If you select <strong id="b1542916259"><a name="b1542916259"></a><a name="b1542916259"></a>Default settings</strong>, the default block page is displayed.</li><li>If you select <strong id="b9715913245"><a name="b9715913245"></a><a name="b9715913245"></a>Customize</strong>, set a custom message.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="30.12%" headers="mcps1.2.4.1.3 "><p id="p374411811219"><a name="p374411811219"></a><a name="p374411811219"></a><strong id="b1762118882414"><a name="b1762118882414"></a><a name="b1762118882414"></a>Customize</strong></p>
    </td>
    </tr>
    <tr id="row157442018202118"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p774418186216"><a name="p774418186216"></a><a name="p774418186216"></a>Block Page Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.88%" headers="mcps1.2.4.1.2 "><p id="p1074481852115"><a name="p1074481852115"></a><a name="p1074481852115"></a>If you select <strong id="b84235270611431"><a name="b84235270611431"></a><a name="b84235270611431"></a>Customize</strong> for <strong id="b84235270611435"><a name="b84235270611435"></a><a name="b84235270611435"></a>Block Page</strong>, select a type of the block page among options <strong id="b842352706114240"><a name="b842352706114240"></a><a name="b842352706114240"></a>application/json</strong>, <strong id="b842352706114245"><a name="b842352706114245"></a><a name="b842352706114245"></a>text/html</strong>, and <strong id="b842352706114249"><a name="b842352706114249"></a><a name="b842352706114249"></a>text/xml</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.12%" headers="mcps1.2.4.1.3 "><p id="p117442018182120"><a name="p117442018182120"></a><a name="p117442018182120"></a><strong id="b16761111417312"><a name="b16761111417312"></a><a name="b16761111417312"></a>text/html</strong></p>
    </td>
    </tr>
    <tr id="row1574471819217"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p207441181218"><a name="p207441181218"></a><a name="p207441181218"></a>Page Content</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.88%" headers="mcps1.2.4.1.2 "><p id="p14744161812218"><a name="p14744161812218"></a><a name="p14744161812218"></a>If you select <strong id="b1677346641114332"><a name="b1677346641114332"></a><a name="b1677346641114332"></a>Customize</strong> for <strong id="b1140464710114332"><a name="b1140464710114332"></a><a name="b1140464710114332"></a>Block Page</strong>, set the content to be returned.</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.12%" headers="mcps1.2.4.1.3 "><p id="p7744121802116"><a name="p7744121802116"></a><a name="p7744121802116"></a><strong id="b842352706175530"><a name="b842352706175530"></a><a name="b842352706175530"></a>&lt;html&gt;&lt;body&gt;Forbidden&lt;/body&gt;&lt;/html&gt;</strong></p>
    </td>
    </tr>
    </tbody>
    </table>

8.  Click  **OK**. The added CC attack protection rule is displayed in the rule list.
    -   To modify the added rule, click  **Modify**  in the row containing the target rule.
    -   The default CC attack protection rule created by WAF can be modified but cannot be deleted.
    -   To delete the added rule, click  **Delete**  in the row containing the target rule.


