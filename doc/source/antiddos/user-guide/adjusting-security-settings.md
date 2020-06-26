# Adjusting Security Settings<a name="EN-US_TOPIC_0204851517"></a>

## Scenarios<a name="section104821493819"></a>

You can adjust security settings after Anti-DDoS is enabled.

## Prerequisites<a name="section9733010918"></a>

You have obtained an account and its password to log in to the management console.

## Procedure<a name="section164521218919"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon_dt-3.png)  in the upper left corner and select the desired region or project.
3.  Under  **Security**, choose  **Anti-DDoS**. The  **Security Console**  is displayed.
4.  Select the  **Public IP Addresses**  tab, locate the row that contains the IP address for which protection settings need to be modified, and click  **Set Protection**  in the  **Operation**  column, as shown in  [Figure 1](#fig6189986015278).

    **Figure  1**  Public IP address list<a name="fig6189986015278"></a>  
    ![](figures/public-ip-address-list.png "public-ip-address-list")

5.  In the displayed  **Set Protection**  dialog box, set required parameters, as shown in  [Figure 2](#fig415543111219).

    **Figure  2**  Page for setting protection parameters<a name="fig415543111219"></a>  
    ![](figures/page-for-setting-protection-parameters.png "page-for-setting-protection-parameters")

    **Table  1**  Parameter description

    <a name="table84181091119"></a>
    <table><thead align="left"><tr id="row941711013115"><th class="cellrowborder" valign="top" width="20.3%" id="mcps1.2.3.1.1"><p id="p13417140201120"><a name="p13417140201120"></a><a name="p13417140201120"></a><strong id="b543889356144253"><a name="b543889356144253"></a><a name="b543889356144253"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="79.7%" id="mcps1.2.3.1.2"><p id="p16417704114"><a name="p16417704114"></a><a name="p16417704114"></a><strong id="b4102827915513"><a name="b4102827915513"></a><a name="b4102827915513"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row296916541259"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.3.1.1 "><p id="p3970554192510"><a name="p3970554192510"></a><a name="p3970554192510"></a>Protection Settings</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.7%" headers="mcps1.2.3.1.2 "><a name="ul9262156192818"></a><a name="ul9262156192818"></a><ul id="ul9262156192818"><li><strong id="b166082315911"><a name="b166082315911"></a><a name="b166082315911"></a>Default</strong>: In this mode, <strong id="b11795184613617"><a name="b11795184613617"></a><a name="b11795184613617"></a>Traffic Cleaning Threshold</strong> is fixed at <strong id="b17444122414373"><a name="b17444122414373"></a><a name="b17444122414373"></a>120 Mbps</strong>. When the service UDP traffic is greater than 120 Mbps or the TCP traffic is greater than 35,000 pps, traffic scrubbing is triggered and Anti-DDoS will automatically intercept the attack traffic.</li><li><strong id="b16494903337"><a name="b16494903337"></a><a name="b16494903337"></a>Manual</strong>: In this mode, you can set the value of <strong id="b624112156411"><a name="b624112156411"></a><a name="b624112156411"></a>Traffic Cleaning Threshold</strong> based on your service needs and enable <strong id="b774405112416"><a name="b774405112416"></a><a name="b774405112416"></a>CC Defense</strong>.</li></ul>
    <div class="note" id="note07513431808"><a name="note07513431808"></a><a name="note07513431808"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0204851524_ul5873919185614"></a><a name="en-us_topic_0204851524_ul5873919185614"></a><ul id="en-us_topic_0204851524_ul5873919185614"><li>Mbps = Mbit/s (short for 1,000,000 bit/s). It is a unit of transmission rate and refers to the number of bits transmitted per second.</li><li>PPS, short for Packets Per Second, is a measure of throughput for network devices. It means the number of packets sent per second.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row2418805113"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.3.1.1 "><p id="p134171306118"><a name="p134171306118"></a><a name="p134171306118"></a>Traffic Cleaning Threshold</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.7%" headers="mcps1.2.3.1.2 "><p id="p94181009119"><a name="p94181009119"></a><a name="p94181009119"></a>Anti-DDoS scrubs traffic when detecting that the incoming traffic of an IP address exceeds the threshold.</p>
    <a name="ul151454553354"></a><a name="ul151454553354"></a><ul id="ul151454553354"><li>The default value of <strong id="b126312003465"><a name="b126312003465"></a><a name="b126312003465"></a>Traffic Cleaning Threshold</strong> is fixed at <strong id="b2616153424511"><a name="b2616153424511"></a><a name="b2616153424511"></a>120 Mbps</strong> when <strong id="b195362864513"><a name="b195362864513"></a><a name="b195362864513"></a>Protection Settings</strong> is set to <strong id="b1844133914457"><a name="b1844133914457"></a><a name="b1844133914457"></a>Default</strong>.</li><li>If you need to change the value of <strong id="b320665012464"><a name="b320665012464"></a><a name="b320665012464"></a>Traffic Cleaning Threshold</strong>, set <strong id="b13766133511488"><a name="b13766133511488"></a><a name="b13766133511488"></a>Protection Settings</strong> to <strong id="b623764354814"><a name="b623764354814"></a><a name="b623764354814"></a>Manual</strong>. Then you can set the traffic cleaning threshold based on your service traffic. You are advised to set the threshold to a value closest to the purchased bandwidth but not greater than the purchased bandwidth.</li></ul>
    <div class="note" id="note520641233713"><a name="note520641233713"></a><a name="note520641233713"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p14233151211370"><a name="p14233151211370"></a><a name="p14233151211370"></a>If your service traffic is larger than the value of <strong id="b1393451184618"><a name="b1393451184618"></a><a name="b1393451184618"></a>Traffic Cleaning Threshold</strong> you set, traffic scrubbing is triggered. Only attack traffic is intercepted. If service traffic does not trigger scrubbing, no traffic is intercepted.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1941817061112"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.3.1.1 "><p id="p11418150121116"><a name="p11418150121116"></a><a name="p11418150121116"></a>CC Defense</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.7%" headers="mcps1.2.3.1.2 "><a name="ul141814011119"></a><a name="ul141814011119"></a><ul id="ul141814011119"><li><strong id="b3849129115210"><a name="b3849129115210"></a><a name="b3849129115210"></a>CC Defense</strong> is set to <strong id="b1714523885218"><a name="b1714523885218"></a><a name="b1714523885218"></a>Disable</strong> automatically when <strong id="b13783251175110"><a name="b13783251175110"></a><a name="b13783251175110"></a>Protection Settings</strong> is set to <strong id="b11373175615112"><a name="b11373175615112"></a><a name="b11373175615112"></a>Default</strong>. Note that only <strong id="b13518263538"><a name="b13518263538"></a><a name="b13518263538"></a>CC Defense</strong> rather than Anti-DDoS protection is disabled.</li><li>If <strong id="b7580105612275"><a name="b7580105612275"></a><a name="b7580105612275"></a>Protection Settings</strong> is set to <strong id="b185816565277"><a name="b185816565277"></a><a name="b185816565277"></a>Manual</strong>, you can enable <strong id="b358211560273"><a name="b358211560273"></a><a name="b358211560273"></a>CC Defense</strong> based on your service needs.<div class="note" id="note165281359101620"><a name="note165281359101620"></a><a name="note165281359101620"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p19528195921612"><a name="p19528195921612"></a><a name="p19528195921612"></a>CC defense is available only for clients that carry web services and support the full HTTP protocol stack. This is because CC defense works in redirection or redirection+verification code mode. If your client does not support the full HTTP protocol stack, you are advised to disable CC defense.</p>
    </div></div>
    </li></ul>
    </td>
    </tr>
    <tr id="row399342155012"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.3.1.1 "><p id="p5992042145016"><a name="p5992042145016"></a><a name="p5992042145016"></a>HTTP Request Threshold</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.7%" headers="mcps1.2.3.1.2 "><p id="p1610054210500"><a name="p1610054210500"></a><a name="p1610054210500"></a>This parameter is required only when <strong id="b1480711115575"><a name="b1480711115575"></a><a name="b1480711115575"></a>CC Defense</strong> is set to <strong id="b2398105316578"><a name="b2398105316578"></a><a name="b2398105316578"></a>Enable</strong>. The unit is qps (short for queries per second). QPS is a common measure of the amount of search traffic an information retrieval system, such as a search engine or a database, receives during one second.</p>
    <p id="p162141923191417"><a name="p162141923191417"></a><a name="p162141923191417"></a>This parameter is used to defend against a large number of malicious requests targeting websites. Defense against CC attacks, which aim to exhaust server resources by sending specially crafted GET or POST requests, is triggered when the HTTP request rate on a site reaches the selected value. In EIP protection, the maximum recommended value is <strong id="b173791715195816"><a name="b173791715195816"></a><a name="b173791715195816"></a>5000</strong>. In ELB protection, the value can be larger</p>
    <p id="p7814822195420"><a name="p7814822195420"></a><a name="p7814822195420"></a>You are advised to set this parameter to the maximum number of HTTP requests that can be processed by the deployed service. Anti-DDoS will automatically scrub traffic if detecting that the total number of requests exceeds the configured HTTP request threshold. If the value is too large, CC defense will not be triggered promptly.</p>
    <a name="ul1981412245413"></a><a name="ul1981412245413"></a><ul id="ul1981412245413"><li>If the actual HTTP request rate is smaller than the configured value, the deployed service is able to process all HTTP requests, and Anti-DDoS does not need to be involved.</li><li>If the actual HTTP request rate is greater than or equal to the configured value, Anti-DDoS triggers CC defense to analyze and check each request, which affects responses to normal requests.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **OK**  to save the settings.

