# Enabling Basic Web Protection<a name="waf_01_0008"></a>

This section describes how to enable  basic web protection.

Basic web protection defends against common web attacks, such as SQL injection, XSS attacks, remote buffer overflow attacks, file inclusion, Bash vulnerability exploits, remote command execution, directory traversal, sensitive file access, and command and code injections, and detects webshells, robots \(search engine, scanner, and script tool\), and other crawlers.

## Prerequisites<a name="section2256777914731"></a>

-   Login credentials have been obtained.
-   The domain name to be protected has been created.

## Procedure<a name="section61533550183130"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Click  **Service List**  at the top of the page and choose  **Security**  \>  **Web Application Firewall**. In the navigation pane, choose  **Domains**. The  **Domains**  page is displayed, as shown in  [Figure 1](#fig164792010154510).

    **Figure  1**  Entrance to the domain configuration page<a name="fig164792010154510"></a>  
    ![](figures/entrance-to-the-domain-configuration-page.png "entrance-to-the-domain-configuration-page")

4.  In the  **Operation**  column of the row containing the target domain name, click  **Configure Policy**. The protection configuration page is displayed, as shown in  [Figure 2](#fig16197124372015).

    **Figure  2**  Protection configuration page<a name="fig16197124372015"></a>  
    ![](figures/protection-configuration-page.png "protection-configuration-page")

5.  <a name="li133562015102112"></a>In the  **Basic Web Protection**  configuration area, change  **Status**  and  **Mode**  as needed by referring to  [Table 1](#table42360431192825)  and then click  **Save**  in the upper right corner of the  **Protection Status**  list. In the dialog box displayed, click  **Yes**  to save the settings. Otherwise, click  **Cancel**. See  [Figure 3](#fig193788379).

    **Figure  3**  Basic Web Protection configuration area<a name="fig193788379"></a>  
    ![](figures/basic-web-protection-configuration-area.png "basic-web-protection-configuration-area")

    **Table  1**  Parameter description

    <a name="table42360431192825"></a>
    <table><thead align="left"><tr id="row66262481192825"><th class="cellrowborder" valign="top" width="36.28%" id="mcps1.2.3.1.1"><p id="p54075445192825"><a name="p54075445192825"></a><a name="p54075445192825"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.72%" id="mcps1.2.3.1.2"><p id="p18034950192825"><a name="p18034950192825"></a><a name="p18034950192825"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8899732153112"><td class="cellrowborder" valign="top" width="36.28%" headers="mcps1.2.3.1.1 "><p id="p189011132173111"><a name="p189011132173111"></a><a name="p189011132173111"></a>Status</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.72%" headers="mcps1.2.3.1.2 "><p id="p11901832163110"><a name="p11901832163110"></a><a name="p11901832163110"></a>Status of Basic Web Protection</p>
    <a name="ul115452316468"></a><a name="ul115452316468"></a><ul id="ul115452316468"><li><a name="image4573204012119"></a><a name="image4573204012119"></a><span><img id="image4573204012119" src="figures/icon-open.png"></span>: enabled.</li><li><a name="image1568021112219"></a><a name="image1568021112219"></a><span><img id="image1568021112219" src="figures/icon-close.png"></span>: disabled.</li></ul>
    </td>
    </tr>
    <tr id="row28096830192825"><td class="cellrowborder" valign="top" width="36.28%" headers="mcps1.2.3.1.1 "><p id="p10384205820363"><a name="p10384205820363"></a><a name="p10384205820363"></a>Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.72%" headers="mcps1.2.3.1.2 "><a name="ul946621183715"></a><a name="ul946621183715"></a><ul id="ul946621183715"><li><strong id="b842352706204429"><a name="b842352706204429"></a><a name="b842352706204429"></a>Block</strong>: WAF blocks and logs detected attacks.</li><li><strong id="b842352706204532"><a name="b842352706204532"></a><a name="b842352706204532"></a>Log only</strong>: WAF logs detected attacks only.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

6.  In the  **Basic Web Protection**  configuration area, click  **Advanced Settings**. Enable the protection type that best fits your needs \(see  [Figure 4](#fig185482343414)\).

    >![](/images/icon-note.gif) **NOTE:**   
    >If you do not click  **Save**  after changing  **Status**  and  **Mode**  in  [step 5](#li133562015102112), the  **Warning**  dialog box is displayed when you click  **Advanced Settings**.  
    >-   Click  **Yes**  to cancel the previous settings.  
    >-   Click  **No**  and then  **Save**  to save the settings.  

    **Figure  4**  Basic web protection<a name="fig185482343414"></a>  
    ![](figures/basic-web-protection.png "basic-web-protection")

    **Table  2**  Protection types

    <a name="table72326127527"></a>
    <table><thead align="left"><tr id="en-us_topic_0110861309_row25491137297"><th class="cellrowborder" valign="top" width="40.04%" id="mcps1.2.3.1.1"><p id="en-us_topic_0110861309_p1854915379911"><a name="en-us_topic_0110861309_p1854915379911"></a><a name="en-us_topic_0110861309_p1854915379911"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.96%" id="mcps1.2.3.1.2"><p id="en-us_topic_0110861309_p8549737894"><a name="en-us_topic_0110861309_p8549737894"></a><a name="en-us_topic_0110861309_p8549737894"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0110861309_row354983713918"><td class="cellrowborder" valign="top" width="40.04%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0110861309_p35498371299"><a name="en-us_topic_0110861309_p35498371299"></a><a name="en-us_topic_0110861309_p35498371299"></a>General Check</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.96%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0110861309_p125497371397"><a name="en-us_topic_0110861309_p125497371397"></a><a name="en-us_topic_0110861309_p125497371397"></a>Defends against attacks, such as SQL injection, XSS, remote overflow vulnerability, file inclusion, Bash vulnerabilities, remote command execution, directory traversal, sensitive file access, and command/code injection.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0110861309_row5549123715914"><td class="cellrowborder" valign="top" width="40.04%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0110861309_p754913375913"><a name="en-us_topic_0110861309_p754913375913"></a><a name="en-us_topic_0110861309_p754913375913"></a>Webshell Detection</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.96%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0110861309_p1754993711914"><a name="en-us_topic_0110861309_p1754993711914"></a><a name="en-us_topic_0110861309_p1754993711914"></a>Protects against webshells from upload interface.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0110861309_row85491637993"><td class="cellrowborder" valign="top" width="40.04%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0110861309_p185491637293"><a name="en-us_topic_0110861309_p185491637293"></a><a name="en-us_topic_0110861309_p185491637293"></a>Search Engine</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.96%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0110861309_p45491337791"><a name="en-us_topic_0110861309_p45491337791"></a><a name="en-us_topic_0110861309_p45491337791"></a>Uses web crawlers to find pages for search engines, such as Googlebot and Baiduspider.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0110861309_row2549203710913"><td class="cellrowborder" valign="top" width="40.04%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0110861309_p185492371894"><a name="en-us_topic_0110861309_p185492371894"></a><a name="en-us_topic_0110861309_p185492371894"></a>Scanner</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.96%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0110861309_p14549133716913"><a name="en-us_topic_0110861309_p14549133716913"></a><a name="en-us_topic_0110861309_p14549133716913"></a>Scans for vulnerabilities, viruses, and performs other types of web scans, such as OpenVAS and Nmap.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0110861309_row165491737295"><td class="cellrowborder" valign="top" width="40.04%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0110861309_p195495371592"><a name="en-us_topic_0110861309_p195495371592"></a><a name="en-us_topic_0110861309_p195495371592"></a>Script Tool</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.96%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0110861309_p1754912371891"><a name="en-us_topic_0110861309_p1754912371891"></a><a name="en-us_topic_0110861309_p1754912371891"></a>Executes automatic tasks and program scripts, such as HttpClient, OkHttp, and Python programs.</p>
    <div class="note" id="en-us_topic_0110861309_note18101191317159"><a name="en-us_topic_0110861309_note18101191317159"></a><a name="en-us_topic_0110861309_note18101191317159"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0110861309_p810271317156"><a name="en-us_topic_0110861309_p810271317156"></a><a name="en-us_topic_0110861309_p810271317156"></a>If your application uses scripts such as httpclient, okhttp, and python, disable <strong id="b6559139155311"><a name="b6559139155311"></a><a name="b6559139155311"></a>Script Tool</strong>. Otherwise, WAF will identify such script tools as crawlers and block the application.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0110861309_row155491737693"><td class="cellrowborder" valign="top" width="40.04%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0110861309_p154913372917"><a name="en-us_topic_0110861309_p154913372917"></a><a name="en-us_topic_0110861309_p154913372917"></a>Other</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.96%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0110861309_p115498372912"><a name="en-us_topic_0110861309_p115498372912"></a><a name="en-us_topic_0110861309_p115498372912"></a>Crawlers for other purposes, such as site monitoring, access proxy, and webpage analysis.</p>
    </td>
    </tr>
    </tbody>
    </table>

    1.  Set the protection level.

        In the upper part of the page, select a protection level:  **Low**,  **Medium**, or  **High**. The default value is  **Medium**.

        **Table  3**  Protection levels

        <a name="en-us_topic_0110861309_table4686152913388"></a>
        <table><thead align="left"><tr id="en-us_topic_0110861309_en-us_topic_0165951356_row257619443717"><th class="cellrowborder" valign="top" width="28.849999999999998%" id="mcps1.2.3.1.1"><p id="en-us_topic_0110861309_en-us_topic_0165951356_p2576844573"><a name="en-us_topic_0110861309_en-us_topic_0165951356_p2576844573"></a><a name="en-us_topic_0110861309_en-us_topic_0165951356_p2576844573"></a>Protection Level</p>
        </th>
        <th class="cellrowborder" valign="top" width="71.15%" id="mcps1.2.3.1.2"><p id="en-us_topic_0110861309_en-us_topic_0165951356_p95761144176"><a name="en-us_topic_0110861309_en-us_topic_0165951356_p95761144176"></a><a name="en-us_topic_0110861309_en-us_topic_0165951356_p95761144176"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="en-us_topic_0110861309_en-us_topic_0165951356_row2576644570"><td class="cellrowborder" valign="top" width="28.849999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0110861309_en-us_topic_0165951356_p7576844572"><a name="en-us_topic_0110861309_en-us_topic_0165951356_p7576844572"></a><a name="en-us_topic_0110861309_en-us_topic_0165951356_p7576844572"></a>Low</p>
        </td>
        <td class="cellrowborder" valign="top" width="71.15%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0110861309_en-us_topic_0165951356_p15576174416714"><a name="en-us_topic_0110861309_en-us_topic_0165951356_p15576174416714"></a><a name="en-us_topic_0110861309_en-us_topic_0165951356_p15576174416714"></a>WAF only blocks the requests with obvious attack signatures.</p>
        <p id="en-us_topic_0110861309_en-us_topic_0165951356_p7903127245"><a name="en-us_topic_0110861309_en-us_topic_0165951356_p7903127245"></a><a name="en-us_topic_0110861309_en-us_topic_0165951356_p7903127245"></a>If a large number of false alarms are reported, <strong id="b199281723155420"><a name="b199281723155420"></a><a name="b199281723155420"></a>Low</strong> is recommended.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0110861309_en-us_topic_0165951356_row18576344378"><td class="cellrowborder" valign="top" width="28.849999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0110861309_en-us_topic_0165951356_p20576044476"><a name="en-us_topic_0110861309_en-us_topic_0165951356_p20576044476"></a><a name="en-us_topic_0110861309_en-us_topic_0165951356_p20576044476"></a>Medium</p>
        </td>
        <td class="cellrowborder" valign="top" width="71.15%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0110861309_en-us_topic_0165951356_p2910122920245"><a name="en-us_topic_0110861309_en-us_topic_0165951356_p2910122920245"></a><a name="en-us_topic_0110861309_en-us_topic_0165951356_p2910122920245"></a>The default level is <strong id="b112991290543"><a name="b112991290543"></a><a name="b112991290543"></a>Medium</strong>, which meets a majority of web protection requirements.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0110861309_en-us_topic_0165951356_row857616441575"><td class="cellrowborder" valign="top" width="28.849999999999998%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0110861309_en-us_topic_0165951356_p1857694417714"><a name="en-us_topic_0110861309_en-us_topic_0165951356_p1857694417714"></a><a name="en-us_topic_0110861309_en-us_topic_0165951356_p1857694417714"></a>High</p>
        </td>
        <td class="cellrowborder" valign="top" width="71.15%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0110861309_en-us_topic_0165951356_p55766441379"><a name="en-us_topic_0110861309_en-us_topic_0165951356_p55766441379"></a><a name="en-us_topic_0110861309_en-us_topic_0165951356_p55766441379"></a>WAF blocks the requests with no attack signature but have specific attack patterns.</p>
        <p id="en-us_topic_0110861309_en-us_topic_0165951356_p42472517104"><a name="en-us_topic_0110861309_en-us_topic_0165951356_p42472517104"></a><a name="en-us_topic_0110861309_en-us_topic_0165951356_p42472517104"></a><strong id="b12101397549"><a name="b12101397549"></a><a name="b12101397549"></a>High</strong> is recommended if you want to block SQL injection, XSS, and command injection attacks.</p>
        </td>
        </tr>
        </tbody>
        </table>

    2.  Set the protection type.

        By default,  **General Check**  and  **Scanner**  are enabled. Click  ![](figures/icon-close.png)  to enable other protection types if needed.

    3.  Click  **Save**  in the upper right of the page to save the settings. Otherwise, click  **Cancel**.


