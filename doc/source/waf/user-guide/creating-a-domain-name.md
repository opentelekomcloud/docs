# Creating a Domain Name<a name="waf_01_0002"></a>

This section describes how to  create a domain name and connect it  to WAF. After connecting a domain name, WAF works as a reverse proxy between the client and server. The real IP address of the server is hidden and only the IP address of WAF is visible to web visitors.

## Prerequisites<a name="section2256777914731"></a>

Login credentials have been obtained.

## Domain Configuration Principle<a name="section155061806348"></a>

-   [Figure 1](#en-us_topic_0110861354_fig030435404518)  shows how WAF works if the web server is using a proxy.

    **Figure  1**  A proxy configured<a name="en-us_topic_0110861354_fig030435404518"></a>  
    ![](figures/a-proxy-configured.png "a-proxy-configured")

    -   DNS resolves the domain name to the IP address of a proxy \(such as AAD\) before your site is moved to WAF. In this case, the traffic passes through the proxy and then the proxy routes the traffic back to the origin server.
    -   After your site is moved to WAF, DNS resolves your domain name to the access address of WAF. In this way, the proxy forwards the traffic to WAF. WAF then filters out illegitimate traffic and only routes legitimate traffic back to the origin server.
        1.  Change the back-to-source IP address of the proxy to the access address of WAF.
        2.  Add a WAF subdomain name and TXT record to the DNS records of your DNS provider.



-   [Figure 2](#en-us_topic_0110861354_fig1624119317528)  shows how WAF works if the web server does not use a proxy.

    **Figure  2**  No proxy configured<a name="en-us_topic_0110861354_fig1624119317528"></a>  
    ![](figures/no-proxy-configured.png "no-proxy-configured")

    -   DNS resolves your domain name to the origin server IP address before your site is moved to WAF. Therefore, web visitors can directly access the server.
    -   After your site is moved to WAF, DNS resolves your domain name to the CNAME of WAF. In this way, the traffic passes through WAF. WAF then filters out illegitimate traffic and only routes legitimate traffic back to the origin server.


## Procedure<a name="section18585791172619"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Choose  **Security**  \>  **Web Application Firewall**.
4.  In the navigation pane, choose  **Domains**. The  **Domains**  page is displayed, as shown in  [Figure 3](#fig15593418182219).

    **Figure  3**  Domains<a name="fig15593418182219"></a>  
    ![](figures/domains.png "domains")

5.  In the upper right corner of the domain name list, click  **Create Domain**.
6.  On the displayed page, configure basic settings.  [Figure 4](#fig175731754141418)  shows this page.  [Table 1](#table7692122554811)  describes the parameters.

    **Figure  4**  Configuring basic settings<a name="fig175731754141418"></a>  
    ![](figures/configuring-basic-settings.png "configuring-basic-settings")

    **Table  1**  Parameter description

    <a name="table7692122554811"></a>
    <table><thead align="left"><tr id="row1068752517484"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.1"><p id="p768742524817"><a name="p768742524817"></a><a name="p768742524817"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="60.5%" id="mcps1.2.4.1.2"><p id="p1168782534812"><a name="p1168782534812"></a><a name="p1168782534812"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.5%" id="mcps1.2.4.1.3"><p id="p12687162544815"><a name="p12687162544815"></a><a name="p12687162544815"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1368718254486"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p41871027399"><a name="p41871027399"></a><a name="p41871027399"></a>Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.5%" headers="mcps1.2.4.1.2 "><p id="p168710252489"><a name="p168710252489"></a><a name="p168710252489"></a>A domain name to be protected, which can be a single domain name or a wildcard domain name.</p>
    <a name="ul9206119142513"></a><a name="ul9206119142513"></a><ul id="ul9206119142513"><li>Single domain name: For example, <em id="i115753818458"><a name="i115753818458"></a><a name="i115753818458"></a>www.example.com</em></li><li>Wildcard domain name<a name="ul776103520251"></a><a name="ul776103520251"></a><ul id="ul776103520251"><li>If the server IP address of each subdomain name is the same, enter a wildcard domain name. For example, <strong id="b5326475234"><a name="b5326475234"></a><a name="b5326475234"></a>*.example.com</strong>.</li><li>If the server IP addresses of subdomain names are different, add subdomain names as single domain names one by one.</li></ul>
    </li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.3 "><p id="p1268714259482"><a name="p1268714259482"></a><a name="p1268714259482"></a>Single domain name: <strong id="b565872715916"><a name="b565872715916"></a><a name="b565872715916"></a>www.example.com</strong></p>
    <p id="p176877251487"><a name="p176877251487"></a><a name="p176877251487"></a>Wildcard domain name: <strong id="b8143143511918"><a name="b8143143511918"></a><a name="b8143143511918"></a>*.example.com</strong></p>
    </td>
    </tr>
    <tr id="row116884252488"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p468762516482"><a name="p468762516482"></a><a name="p468762516482"></a>Non-standard Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.5%" headers="mcps1.2.4.1.2 "><p id="p8687182544810"><a name="p8687182544810"></a><a name="p8687182544810"></a>Set this parameter only if <strong id="b912632651413"><a name="b912632651413"></a><a name="b912632651413"></a>Non-standard Port</strong> is selected.</p>
    <a name="ul86882025104815"></a><a name="ul86882025104815"></a><ul id="ul86882025104815"><li>If <strong id="b18507162234"><a name="b18507162234"></a><a name="b18507162234"></a>Client Protocol</strong> is <strong id="b1051161617234"><a name="b1051161617234"></a><a name="b1051161617234"></a>HTTP</strong>, WAF protects the standard port 80 only by default. To protect a non-standard port, select <strong id="b64291331373"><a name="b64291331373"></a><a name="b64291331373"></a>Non-standard Port</strong> and then select a value from the <strong id="b152616182313"><a name="b152616182313"></a><a name="b152616182313"></a>Non-standard Port</strong> drop-down list.</li><li>If <strong id="b1029192017233"><a name="b1029192017233"></a><a name="b1029192017233"></a>Client Protocol</strong> is <strong id="b17292192012311"><a name="b17292192012311"></a><a name="b17292192012311"></a>HTTPS</strong>, WAF protects the standard port 443 only by default. To protect a non-standard port, select <strong id="b880711291070"><a name="b880711291070"></a><a name="b880711291070"></a>Non-standard Port</strong> and then select a value from the <strong id="b112931120122312"><a name="b112931120122312"></a><a name="b112931120122312"></a>Non-standard Port</strong> drop-down list.</li></ul>
    <p id="p325812018477"><a name="p325812018477"></a><a name="p325812018477"></a>For details about non-standard ports supported by WAF, see <a href="web-application-firewall.md">Web Application Firewall</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.3 "><p id="p86881725164816"><a name="p86881725164816"></a><a name="p86881725164816"></a><strong id="b19591135613711"><a name="b19591135613711"></a><a name="b19591135613711"></a>4443</strong></p>
    </td>
    </tr>
    <tr id="row5690192514820"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p116898254489"><a name="p116898254489"></a><a name="p116898254489"></a>Server Configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.5%" headers="mcps1.2.4.1.2 "><p id="p568972554814"><a name="p568972554814"></a><a name="p568972554814"></a>Address configurations of the web server, including <strong id="b15392185820484"><a name="b15392185820484"></a><a name="b15392185820484"></a>Client Protocol</strong>, <strong id="b1240118583488"><a name="b1240118583488"></a><a name="b1240118583488"></a>Server Protocol</strong>, <strong id="b940275817489"><a name="b940275817489"></a><a name="b940275817489"></a>Server Address</strong>, and <strong id="b2402058204818"><a name="b2402058204818"></a><a name="b2402058204818"></a>Server Port</strong>.</p>
    <a name="ul16689625134815"></a><a name="ul16689625134815"></a><ul id="ul16689625134815"><li><strong id="b82686283108"><a name="b82686283108"></a><a name="b82686283108"></a>Client Protocol:</strong> Type of client protocol. The options are <strong id="b8423527062032_3"><a name="b8423527062032_3"></a><a name="b8423527062032_3"></a>HTTP</strong> and <strong id="b842352706201123"><a name="b842352706201123"></a><a name="b842352706201123"></a>HTTPS</strong>.</li><li><strong id="b1012093220101"><a name="b1012093220101"></a><a name="b1012093220101"></a>Server Protocol</strong>: Protocol used by WAF to forward requests to the server. The options are <strong id="b754363541"><a name="b754363541"></a><a name="b754363541"></a>HTTP</strong> and <strong id="b1575463089"><a name="b1575463089"></a><a name="b1575463089"></a>HTTPS</strong>.<div class="note" id="note031411715256"><a name="note031411715256"></a><a name="note031411715256"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p113161117172510"><a name="p113161117172510"></a><a name="p113161117172510"></a>For details about configuring <strong id="b171101317514"><a name="b171101317514"></a><a name="b171101317514"></a>Client Protocol</strong> and <strong id="b111101314517"><a name="b111101314517"></a><a name="b111101314517"></a>Server Protocol</strong>, see <a href="#section645014318511">Rules for Configuring Client Protocol and Server Protocol</a>.</p>
    </div></div>
    </li><li><strong id="b161617122319"><a name="b161617122319"></a><a name="b161617122319"></a>Server Address</strong>: IP address (generally the A record before the domain name is connected to WAF) or domain name (generally the CNAME before the domain name is connected to WAF) of the web server that a client accesses<div class="note" id="note7392258153815"><a name="note7392258153815"></a><a name="note7392258153815"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p4393175815389"><a name="p4393175815389"></a><a name="p4393175815389"></a>Web Application Firewall (WAF) does not support health check. If you want to use health check, use WAF along with Elastic Load Balancing (ELB). For details about how to configure ELB, see <a href="https://docs.otc.t-systems.com/en-us/usermanual/elb/en-us_topic_0052569729.html" target="_blank" rel="noopener noreferrer">Backend Server (Enhanced Load Balancer)</a>. After ELB is configured, the elastic IP address (EIP) of ELB is used as the value of <strong id="b1142624815286"><a name="b1142624815286"></a><a name="b1142624815286"></a>Server Address</strong> to connect to WAF for health check.</p>
    </div></div>
    </li><li><strong id="b842352706201213"><a name="b842352706201213"></a><a name="b842352706201213"></a>Server Port</strong>: port number used by the web server</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.3 "><p id="p20689192524820"><a name="p20689192524820"></a><a name="p20689192524820"></a><strong id="b842352706102612"><a name="b842352706102612"></a><a name="b842352706102612"></a>Client Protocol</strong>: <strong id="b842352706102615"><a name="b842352706102615"></a><a name="b842352706102615"></a>HTTPS</strong></p>
    <p id="p568922544813"><a name="p568922544813"></a><a name="p568922544813"></a><strong id="b842352706102635"><a name="b842352706102635"></a><a name="b842352706102635"></a>Server Protocol</strong>: <strong id="b842352706102639"><a name="b842352706102639"></a><a name="b842352706102639"></a>HTTPS</strong></p>
    <p id="p1368915251486"><a name="p1368915251486"></a><a name="p1368915251486"></a><strong id="b842352706102659"><a name="b842352706102659"></a><a name="b842352706102659"></a>Server Address</strong>: <strong id="b84235270610273"><a name="b84235270610273"></a><a name="b84235270610273"></a>192.168.1.1</strong></p>
    <p id="p13689162510483"><a name="p13689162510483"></a><a name="p13689162510483"></a><strong id="b1846145272915"><a name="b1846145272915"></a><a name="b1846145272915"></a>Server Port</strong>: <strong id="b116735558290"><a name="b116735558290"></a><a name="b116735558290"></a>443</strong></p>
    </td>
    </tr>
    <tr id="row76909251484"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p169072504811"><a name="p169072504811"></a><a name="p169072504811"></a>Certificate Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.5%" headers="mcps1.2.4.1.2 "><p id="p1223816455594"><a name="p1223816455594"></a><a name="p1223816455594"></a>If <strong id="b1646942183414"><a name="b1646942183414"></a><a name="b1646942183414"></a>Client Protocol</strong> is <strong id="b14634223414"><a name="b14634223414"></a><a name="b14634223414"></a>HTTPS</strong>, select an existing certificate or upload a new certificate. For details about how to upload a new certificate, see <a href="#li1098265701316">7</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.5%" headers="mcps1.2.4.1.3 "><p id="p86901825134813"><a name="p86901825134813"></a><a name="p86901825134813"></a>--</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  <a name="li1098265701316"></a>Upload a new certificate if  **Client Protocol**  is  **HTTPS**.
    1.  Click  **Upload Certificate**. The  **Upload Certificate**  dialog box is displayed. Enter the certificate name, and copy and paste the certificate content and private key to the corresponding text boxes. See  [Figure 5](#fig7846148397).

        **Figure  5**  Uploading a certificate<a name="fig7846148397"></a>  
        ![](figures/uploading-a-certificate.png "uploading-a-certificate")

        >![](/images/icon-note.gif) **NOTE:**   
        >WAF encrypts and saves the private key to keep it safe.  

        Currently, only .pem certificates are supported. If the certificate is not in .pem format, convert it into a .pem certificate by referring to  [Table 2](#table1184924815910)  before uploading.

        **Table  2**  Certificate conversion commands

        <a name="table1184924815910"></a>
        <table><thead align="left"><tr id="row2847448797"><th class="cellrowborder" valign="top" width="21.990000000000002%" id="mcps1.2.3.1.1"><p id="p98475489920"><a name="p98475489920"></a><a name="p98475489920"></a>Format</p>
        </th>
        <th class="cellrowborder" valign="top" width="78.01%" id="mcps1.2.3.1.2"><p id="p18847164813920"><a name="p18847164813920"></a><a name="p18847164813920"></a>How to Convert (In Linux OSs)</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row1784719481093"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.3.1.1 "><p id="p68471489919"><a name="p68471489919"></a><a name="p68471489919"></a>CER/CRT</p>
        </td>
        <td class="cellrowborder" valign="top" width="78.01%" headers="mcps1.2.3.1.2 "><p id="p88479481916"><a name="p88479481916"></a><a name="p88479481916"></a>Rename the <strong id="b84235270691740"><a name="b84235270691740"></a><a name="b84235270691740"></a>cert.crt</strong> certificate file to <strong id="b84235270691747"><a name="b84235270691747"></a><a name="b84235270691747"></a>cert.pem</strong>.</p>
        </td>
        </tr>
        <tr id="row1484714481196"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.3.1.1 "><p id="p14847164816915"><a name="p14847164816915"></a><a name="p14847164816915"></a>PFX</p>
        </td>
        <td class="cellrowborder" valign="top" width="78.01%" headers="mcps1.2.3.1.2 "><a name="ol178472048299"></a><a name="ol178472048299"></a><ol id="ol178472048299"><li>Run the following command to obtain a private key. For example, to convert <strong id="b124221289249"><a name="b124221289249"></a><a name="b124221289249"></a>cert.pfx</strong> into <strong id="b1423152892418"><a name="b1423152892418"></a><a name="b1423152892418"></a>cert.key</strong>, run:<p id="p18476481912"><a name="p18476481912"></a><a name="p18476481912"></a><strong id="b78471748295"><a name="b78471748295"></a><a name="b78471748295"></a>openssl pkcs12 -in cert.pfx -nocerts -out cert.key -nodes</strong></p>
        </li><li>Run the following command to obtain a certificate. For example, to convert <strong id="b15328203542412"><a name="b15328203542412"></a><a name="b15328203542412"></a>cert.pfx</strong> into <strong id="b4329335122416"><a name="b4329335122416"></a><a name="b4329335122416"></a>cert.pem</strong>, run:<p id="p168471248296"><a name="p168471248296"></a><a name="p168471248296"></a><strong id="b10847164818913"><a name="b10847164818913"></a><a name="b10847164818913"></a>openssl pkcs12 -in cert.pfx -nokeys -out cert.pem</strong></p>
        </li></ol>
        </td>
        </tr>
        <tr id="row15847548495"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.3.1.1 "><p id="p12847448399"><a name="p12847448399"></a><a name="p12847448399"></a>P7B</p>
        </td>
        <td class="cellrowborder" valign="top" width="78.01%" headers="mcps1.2.3.1.2 "><p id="p784720481898"><a name="p784720481898"></a><a name="p784720481898"></a>Run the following command to convert a certificate. For example, to convert <strong id="b1992263817248"><a name="b1992263817248"></a><a name="b1992263817248"></a>cert.p7b</strong> into <strong id="b1922113812413"><a name="b1922113812413"></a><a name="b1922113812413"></a>cert.pem</strong>, run:</p>
        <p id="p384734812910"><a name="p384734812910"></a><a name="p384734812910"></a><strong id="b884754812912"><a name="b884754812912"></a><a name="b884754812912"></a>openssl pkcs7 -print_certs -in cert.p7b -out cert.pem</strong></p>
        </td>
        </tr>
        <tr id="row12849154819915"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.3.1.1 "><p id="p1984713481495"><a name="p1984713481495"></a><a name="p1984713481495"></a>DER</p>
        </td>
        <td class="cellrowborder" valign="top" width="78.01%" headers="mcps1.2.3.1.2 "><p id="p208499482912"><a name="p208499482912"></a><a name="p208499482912"></a>Run the following command to obtain a certificate. For example, to convert <strong id="b1580714614246"><a name="b1580714614246"></a><a name="b1580714614246"></a>privatekey.der</strong> into <strong id="b58072461245"><a name="b58072461245"></a><a name="b58072461245"></a>cert.key</strong>, run:</p>
        <p id="p118496487916"><a name="p118496487916"></a><a name="p118496487916"></a><strong id="b118494481997"><a name="b118494481997"></a><a name="b118494481997"></a>openssl rsa -inform DER -outform PEM -in privatekey.der -out cert.key</strong></p>
        </td>
        </tr>
        </tbody>
        </table>

    2.  Click  **OK**.

8.  Set  **Proxy Configured**. The default value is  **No**.

    >![](/images/icon-notice.gif) **NOTICE:**   
    >The bypassed option is unavailable during proxy use.  

    -   If your website is using a proxy such as Advanced Anti-DDoS \(AAD\), Content Delivery Network \(CDN\), or any other cloud acceleration service, select  **Yes**  so that the WAF security policies take effect on the origin server IP address. If this parameter is  **No**, WAF cannot obtain the real IP address requested by a web visitor.

        >![](/images/icon-note.gif) **NOTE:**   
        >If a proxy such as CDN is used, WAF obtains the real source IP address of a client from the HTTP Header  **X-Forwarded-For**  by default. If the proxy does not use  **X-Forwarded-For**  to identify the real source IP address of a client, click  ![](figures/icon-edit.png)  next to  **X-Forwarded-For**  in the row of  **Source IP Header**. In the dialog box displayed, select an existing source IP header or select  **Custom**  and enter a source IP header.  

    -   If your website does not use a proxy, select  **No**.

9.  \(Optional\) Configure a tag.

    You can select an existing tag key and tag value from the  **Tag key**  and  **Tag value**  drop-down lists or click  **View predefined tags**  to create a tag on the TMS console.

10. Click  **Create Now**. In the upper right corner of the page,  **Domain created successfully**  is displayed, indicating that the domain name is created.

    >![](/images/icon-note.gif) **NOTE:**   
    >If you do not want to connect the domain name to WAF in this step, click  **Next**. Then click  **Finish**.  **DNS**  is displayed as  **Unconfigured**. Later, you can refer to  [Connecting a Domain Name](connecting-a-domain-name-to-waf.md)  to finish domain connection.  

    -   If a proxy such as CDN or AAD is used, you need to configure the back-to-source IP address, subdomain name, and TXT record.  [Figure 6](#waf_01_0056_fig450482413592)  displays the configurations.

        **Figure  6**  Connecting a domain name<a name="waf_01_0056_fig450482413592"></a>  
        ![](figures/connecting-a-domain-name.png "connecting-a-domain-name")

        1.  Configure the back-to-source IP address of the proxy on the website.

            For example, change the back-to-source IP address of CDN or AAD to the WAF IP address as shown in  [Figure 6](#waf_01_0056_fig450482413592).

        2.  Configure  **Subdomain Name**  and  **TXT Record**.

            Add a subdomain name and TXT record to the DNS records of your DNS provider.

        >![](/images/icon-notice.gif) **NOTICE:**   
        >The high availability of our system, which is based on multi-AZ deployments to support both active-active and disaster recovery, relies on the WAF CNAME record.  

    -   If no proxy is used, the CNAME record must be configured.  [Figure 7](#waf_01_0056_fig84741317702)  displays the configuration.

        **Figure  7**  Connecting a domain name \(CNAME record\)<a name="waf_01_0056_fig84741317702"></a>  
        ![](figures/connecting-a-domain-name-(cname-record).png "connecting-a-domain-name-(cname-record)")

        1.  Go to your DNS provider and configure the CNAME record. For details, contact your DNS provider.

            >![](/images/icon-notice.gif) **NOTICE:**   
            >The high availability of our system, which is based on multi-AZ deployments to support both active-active and disaster recovery, relies on the WAF CNAME record. Therefore,  
            >1.  Do not modify the hosts file. Add the CNAME record directly to the DNS records of your DNS provider.  
            >2.  Do not use the A record to replace the CNAME record.  

            The CNAME binding method of some common DNS providers is listed for your reference. If the following configuration is inconsistent with the actual configuration, rely on information provided by the DNS providers.

            1.  Log in to the management console of the DNS provider.
            2.  Go to the domain resolution record page.
            3.  Set the CNAME resolution record.
                -   Set the record type to  **CNAME**.
                -   Generally, enter the domain name prefix in the host record. For example, if the protected domain name is  **admin.demo.com**, enter  **admin**  in the host record.
                -   The record value is the CNAME generated by WAF.
                -   Resolution line: keep the default value  **TTL**.

            4.  Click  **Save**.

            >![](/images/icon-notice.gif) **NOTICE:**   
            >The preceding resolution methods are provided by third parties. This document does not control or assume responsibility for any third party content, including but not limited to its accuracy, compatibility, reliability, availability, legitimacy, appropriateness, performance, non-infringement, or status update, unless otherwise specified in this document.  

        2.  Verify that the CNAME has been configured.
            1.  In Windows, choose  **Start**  \>  **Run**. Then enter  **cmd**  and press  **Enter**.
            2.  Run the following command to query the CNAME. If the configured CNAME is displayed, the configuration is successful.

                **nslookup www.**_domain_**.com**



11. After the domain name is connected to WAF, click  **Next**.
12. Click  **Finish**.

    You can view the DNS status and mode of the domain name in the domain list.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   If your web server is using other firewalls, disable the firewalls or whitelist the WAF IP address ranges.  
    >-   If your web server is using personal security software, replace it with enterprise security software and whitelist the WAF IP address ranges.  
    >-   If a domain name has been connected to WAF,  **DNS**  should be  **Normal**. If  **DNS**  is  **Unconfigured**, choose  **More \> Check DNS**  in the  **Operation**  column of the target domain name to check the DNS status. If the problem persists, perform domain connection again by referring to  [What Should I Do If the DNS Status Is Unconfigured?](what-should-i-do-if-the-dns-status-is-unconfigured.md).  
    >-   After a domain name is created, WAF protection is enabled by default. The mode of Basic Web Protection is  **Log only**  \(detected attacks are only logged but not blocked.\). WAF creates a CC attack protection rule for the domain name by default. The rule can be modified but cannot be deleted.  **Rate Limit**  in the rule is 500 requests/5 seconds by default and it can be adjusted up to 10000 requests/5 seconds. If you want a higher rate limit than the maximum value, contact the administrator.  


## Rules for Configuring Client Protocol and Server Protocol<a name="section645014318511"></a>

WAF provides various protocol types. If your website is www.example.com, WAF provides the following four access modes:

-   HTTP mode. See  [Figure 8](#fig53041342142615).

    **Figure  8**  HTTP mode<a name="fig53041342142615"></a>  
    ![](figures/http-mode.png "http-mode")

    >![](/images/icon-notice.gif) **NOTICE:**   
    >This configuration allows web visitors to access your website over HTTP only. If they access over HTTPS, they receive the 302 Found code and are redirected to http://www.example.com.  

-   HTTPS mode. This configuration allows web visitors to access your website over HTTPS only. If they access over HTTP, they are redirected to https://www.example.com. See  [Figure 9](#fig7444410153315).

    **Figure  9**  HTTPS mode<a name="fig7444410153315"></a>  
    ![](figures/https-mode.png "https-mode")

    >![](/images/icon-notice.gif) **NOTICE:**   
    >-   If web visitors access your website over HTTPS, the website returns a successful response.  
    >-   If web visitors access your website over HTTP, they receive the 302 Found code and are directed to https://www.example.com.  

-   HTTP and HTTPS mode. See  [Figure 10](#fig3389134713400).

    **Figure  10**  HTTP and HTTPS mode<a name="fig3389134713400"></a>  
    ![](figures/http-and-https-mode.png "http-and-https-mode")

    >![](/images/icon-notice.gif) **NOTICE:**   
    >-   If web visitors access your website over HTTP, the website returns a successful response but no communication between the browser and website is encrypted.  
    >-   If web visitors access your website over HTTPS, the website returns a successful response and all communications between the browser and website are encrypted.  

-   HTTPS/HTTP mode. See  [Figure 11](#fig11273129104514).

    **Figure  11**  HTTPS/HTTP mode<a name="fig11273129104514"></a>  
    ![](figures/https-http-mode.png "https-http-mode")

    >![](/images/icon-notice.gif) **NOTICE:**   
    >If web visitors access your website over HTTPS, WAF forwards the requests to your origin server over HTTP.  


