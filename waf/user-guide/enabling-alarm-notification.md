# Enabling Alarm Notification<a name="EN-US_TOPIC_0193630334"></a>

This section describes how to enable notification for attack logs. Once this function is enabled, WAF sends attack logs to users by email or SMS.

## Prerequisites<a name="section2256777914731"></a>

-   Login credentials have been obtained.
-   The SMN service has been enabled.

## Procedure<a name="section61533550183130"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Choose  **Security**  \>  **Web Application Firewall**. In the navigation pane, choose  **Events**. The  **Events**  page is displayed.
4.  Click the  **Notify**  tab and configure alarm notification parameters by referring to  [Table 1](#table4725363915334)  \(see  [Figure 1](#fig40676821112218)\).

    **Figure  1**  Configuring alarm notification<a name="fig40676821112218"></a>  
    ![](figures/configuring-alarm-notification.png "configuring-alarm-notification")

    **Table  1**  Notification setting parameters

    <a name="table4725363915334"></a>
    <table><thead align="left"><tr id="row4914351215334"><th class="cellrowborder" valign="top" width="34.97%" id="mcps1.2.3.1.1"><p id="p5659630615334"><a name="p5659630615334"></a><a name="p5659630615334"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="65.03%" id="mcps1.2.3.1.2"><p id="p2089811115334"><a name="p2089811115334"></a><a name="p2089811115334"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8143191772214"><td class="cellrowborder" valign="top" width="34.97%" headers="mcps1.2.3.1.1 "><p id="p614381719223"><a name="p614381719223"></a><a name="p614381719223"></a>Notification ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.03%" headers="mcps1.2.3.1.2 "><p id="p914413176228"><a name="p914413176228"></a><a name="p914413176228"></a>Alarm event ID</p>
    </td>
    </tr>
    <tr id="row5386527415334"><td class="cellrowborder" valign="top" width="34.97%" headers="mcps1.2.3.1.1 "><p id="p101105415334"><a name="p101105415334"></a><a name="p101105415334"></a>Notification</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.03%" headers="mcps1.2.3.1.2 "><p id="p515811198121"><a name="p515811198121"></a><a name="p515811198121"></a>Whether to enable notification</p>
    <a name="ul131371286465"></a><a name="ul131371286465"></a><ul id="ul131371286465"><li><a name="image1832717314313"></a><a name="image1832717314313"></a><span><img id="image1832717314313" src="figures/icon-open.png"></span>: enabled.</li><li><a name="image830217398315"></a><a name="image830217398315"></a><span><img id="image830217398315" src="figures/icon-close.png"></span>: disabled.</li></ul>
    </td>
    </tr>
    <tr id="row6597002315334"><td class="cellrowborder" valign="top" width="34.97%" headers="mcps1.2.3.1.1 "><p id="p4197165315334"><a name="p4197165315334"></a><a name="p4197165315334"></a>Notification Topic</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.03%" headers="mcps1.2.3.1.2 "><p id="p58551974153615"><a name="p58551974153615"></a><a name="p58551974153615"></a>Click the drop-down list to select an available topic or click <strong id="b842352706155449"><a name="b842352706155449"></a><a name="b842352706155449"></a>View Topic</strong> to create a topic.</p>
    <p id="p6285082315377"><a name="p6285082315377"></a><a name="p6285082315377"></a>For more information, see the <i><cite id="citec547fbf3e78d45c2be6f1d80107124ac090842"><a name="citec547fbf3e78d45c2be6f1d80107124ac090842"></a><a name="citec547fbf3e78d45c2be6f1d80107124ac090842"></a>Simple Message Notification User Guide</cite></i>.</p>
    </td>
    </tr>
    <tr id="row2091915305414"><td class="cellrowborder" valign="top" width="34.97%" headers="mcps1.2.3.1.1 "><p id="p17919330341"><a name="p17919330341"></a><a name="p17919330341"></a>Threshold</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.03%" headers="mcps1.2.3.1.2 "><p id="p1191973010415"><a name="p1191973010415"></a><a name="p1191973010415"></a>Alarm threshold</p>
    <div class="note" id="note1284420159813"><a name="note1284420159813"></a><a name="note1284420159813"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p16845171517813"><a name="p16845171517813"></a><a name="p16845171517813"></a>Alarm notifications are sent when the number of attacks is greater than or equal to the threshold within the configured period.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row7449192820129"><td class="cellrowborder" valign="top" width="34.97%" headers="mcps1.2.3.1.1 "><p id="p1695504815239"><a name="p1695504815239"></a><a name="p1695504815239"></a>Event Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.03%" headers="mcps1.2.3.1.2 "><p id="p14492280127"><a name="p14492280127"></a><a name="p14492280127"></a>By default, <strong id="b3979810418"><a name="b3979810418"></a><a name="b3979810418"></a>All</strong> is selected. You can also click <strong id="b12976814419"><a name="b12976814419"></a><a name="b12976814419"></a>Customize</strong> to specify event types.</p>
    <p id="p1377911561506"><a name="p1377911561506"></a><a name="p1377911561506"></a>For details about event types, see <a href="#table1553610114533">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  List of event types

    <a name="table1553610114533"></a>
    <table><thead align="left"><tr id="row1453912185318"><th class="cellrowborder" valign="top" width="32.87%" id="mcps1.2.3.1.1"><p id="p453916116537"><a name="p453916116537"></a><a name="p453916116537"></a>Event Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="67.13%" id="mcps1.2.3.1.2"><p id="p453931155317"><a name="p453931155317"></a><a name="p453931155317"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4539916539"><td class="cellrowborder" valign="top" width="32.87%" headers="mcps1.2.3.1.1 "><p id="p145393119534"><a name="p145393119534"></a><a name="p145393119534"></a>Challenge Collapsar</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.13%" headers="mcps1.2.3.1.2 "><p id="p17539117532"><a name="p17539117532"></a><a name="p17539117532"></a>CC attack. When you find out that your website is experiencing slowed processing and high bandwidth usage, it may have been under CC attacks.</p>
    </td>
    </tr>
    <tr id="row65396116533"><td class="cellrowborder" valign="top" width="32.87%" headers="mcps1.2.3.1.1 "><p id="p85393115534"><a name="p85393115534"></a><a name="p85393115534"></a>Command Injection</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.13%" headers="mcps1.2.3.1.2 "><p id="p1539191195316"><a name="p1539191195316"></a><a name="p1539191195316"></a>Command injection. It is a technique used by hackers to execute system commands on a server by chaining commands and bypassing blacklists to invoke web application interfaces.</p>
    </td>
    </tr>
    <tr id="row1353981135312"><td class="cellrowborder" valign="top" width="32.87%" headers="mcps1.2.3.1.1 "><p id="p1353921155315"><a name="p1353921155315"></a><a name="p1353921155315"></a>Custom</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.13%" headers="mcps1.2.3.1.2 "><p id="p8818163314392"><a name="p8818163314392"></a><a name="p8818163314392"></a>Events logged by one or more precise protection rules</p>
    </td>
    </tr>
    <tr id="row553913195311"><td class="cellrowborder" valign="top" width="32.87%" headers="mcps1.2.3.1.1 "><p id="p953921205315"><a name="p953921205315"></a><a name="p953921205315"></a>Illegal Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.13%" headers="mcps1.2.3.1.2 "><p id="p195390135319"><a name="p195390135319"></a><a name="p195390135319"></a>Invalid requests. For example, more than 512 parameters are used.</p>
    </td>
    </tr>
    <tr id="row13539141105315"><td class="cellrowborder" valign="top" width="32.87%" headers="mcps1.2.3.1.1 "><p id="p55394195314"><a name="p55394195314"></a><a name="p55394195314"></a>SQL Injection</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.13%" headers="mcps1.2.3.1.2 "><p id="p153931165313"><a name="p153931165313"></a><a name="p153931165313"></a>SQL injection. It is a common web attack whereby attackers inject malicious SQL commands into database query strings to deceive the server into executing them. By exploiting these commands, the attacker can obtain sensitive information, add users, export files, or even gain the highest permissions to the database or system.</p>
    </td>
    </tr>
    <tr id="row95391115311"><td class="cellrowborder" valign="top" width="32.87%" headers="mcps1.2.3.1.1 "><p id="p4539161185312"><a name="p4539161185312"></a><a name="p4539161185312"></a>Local File Inclusion</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.13%" headers="mcps1.2.3.1.2 "><p id="p125391117536"><a name="p125391117536"></a><a name="p125391117536"></a>Local file inclusion (LFI) allows attackers to access files on a local server or download sensitive configurations. The vulnerability occurs due to the use of user-supplied input without proper validation.</p>
    </td>
    </tr>
    <tr id="row115397112537"><td class="cellrowborder" valign="top" width="32.87%" headers="mcps1.2.3.1.1 "><p id="p853918145318"><a name="p853918145318"></a><a name="p853918145318"></a>Scanner &amp; Crawler</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.13%" headers="mcps1.2.3.1.2 "><p id="p195391914539"><a name="p195391914539"></a><a name="p195391914539"></a>Scanner and crawler attack events</p>
    </td>
    </tr>
    <tr id="row11821203345811"><td class="cellrowborder" valign="top" width="32.87%" headers="mcps1.2.3.1.1 "><p id="p08231933205811"><a name="p08231933205811"></a><a name="p08231933205811"></a>AntiTamper</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.13%" headers="mcps1.2.3.1.2 "><p id="p38231733145815"><a name="p38231733145815"></a><a name="p38231733145815"></a>Events logged by one or more web tamper protection rules</p>
    </td>
    </tr>
    <tr id="row13982194075812"><td class="cellrowborder" valign="top" width="32.87%" headers="mcps1.2.3.1.1 "><p id="p49825405588"><a name="p49825405588"></a><a name="p49825405588"></a>Remote File Inclusion</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.13%" headers="mcps1.2.3.1.2 "><p id="p129821740135819"><a name="p129821740135819"></a><a name="p129821740135819"></a>Remote file inclusion</p>
    </td>
    </tr>
    <tr id="row41031146145816"><td class="cellrowborder" valign="top" width="32.87%" headers="mcps1.2.3.1.1 "><p id="p9105144611586"><a name="p9105144611586"></a><a name="p9105144611586"></a>Miscellaneous</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.13%" headers="mcps1.2.3.1.2 "><p id="p4105154618586"><a name="p4105154618586"></a><a name="p4105154618586"></a>Other types of attacks, such as a combination of SQL injection and command injection attacks or certain CVE vulnerabilities</p>
    </td>
    </tr>
    <tr id="row810594617585"><td class="cellrowborder" valign="top" width="32.87%" headers="mcps1.2.3.1.1 "><p id="p1010513465585"><a name="p1010513465585"></a><a name="p1010513465585"></a>Cross Site Scripting</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.13%" headers="mcps1.2.3.1.2 "><p id="p710504616584"><a name="p710504616584"></a><a name="p710504616584"></a>XSS. It is a type of attacks that exploits security vulnerabilities in web applications. XSS enables attackers to inject auto-executed malicious codes into webpages to steal users' information when they visit the pages.</p>
    </td>
    </tr>
    <tr id="row79372513587"><td class="cellrowborder" valign="top" width="32.87%" headers="mcps1.2.3.1.1 "><p id="p16937155113585"><a name="p16937155113585"></a><a name="p16937155113585"></a>Black/White IP</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.13%" headers="mcps1.2.3.1.2 "><p id="p59372516580"><a name="p59372516580"></a><a name="p59372516580"></a>Events logged by one or more blacklist or whitelist rules</p>
    </td>
    </tr>
    <tr id="row1893718516583"><td class="cellrowborder" valign="top" width="32.87%" headers="mcps1.2.3.1.1 "><p id="p1893725195819"><a name="p1893725195819"></a><a name="p1893725195819"></a>Webshell</p>
    </td>
    <td class="cellrowborder" valign="top" width="67.13%" headers="mcps1.2.3.1.2 "><p id="p1388112819518"><a name="p1388112819518"></a><a name="p1388112819518"></a>A webshell is an attack script. After intruding into a website, an attacker adds an .asp, .php, .jsp, or .cgi script file with normal webpage files. Then, the attacker accesses the file from a web browser and uses it as a backdoor to obtain a command execution environment for controlling the web server. For this reason, webshells are also called backdoor tools.</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **Save**.

