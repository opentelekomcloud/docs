# Viewing Basic Information<a name="waf_01_0020"></a>

This section describes how to view domain information and edit server information.

## Prerequisites<a name="section558884313202"></a>

Login credentials have been obtained.

## Procedure<a name="section47859253215"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Click  **Service List**  at the top of the page and choose  **Security**  \>  **Web Application Firewall**. In the navigation pane, choose  **Domains**. The  **Domains**  page is displayed, as shown in  [Figure 1](#fig1378145118527).  [Table 1](#table147842051135211)  describes the parameters.

    In the upper right corner of the list, query domain information by domain name, policy name, or tag.

    **Figure  1**  Domains page<a name="fig1378145118527"></a>  
    ![](figures/domains-page.png "domains-page")

    **Table  1**  Parameter description

    <a name="table147842051135211"></a>
    <table><thead align="left"><tr id="row7782051165217"><th class="cellrowborder" valign="top" width="37.11%" id="mcps1.2.3.1.1"><p id="p5781251175210"><a name="p5781251175210"></a><a name="p5781251175210"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="62.89%" id="mcps1.2.3.1.2"><p id="p117811751185217"><a name="p117811751185217"></a><a name="p117811751185217"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15782195116525"><td class="cellrowborder" valign="top" width="37.11%" headers="mcps1.2.3.1.1 "><p id="p11782851115217"><a name="p11782851115217"></a><a name="p11782851115217"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.89%" headers="mcps1.2.3.1.2 "><p id="p19782175110522"><a name="p19782175110522"></a><a name="p19782175110522"></a>Protected domain name</p>
    </td>
    </tr>
    <tr id="row107831051145219"><td class="cellrowborder" valign="top" width="37.11%" headers="mcps1.2.3.1.1 "><p id="p978245135210"><a name="p978245135210"></a><a name="p978245135210"></a>Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.89%" headers="mcps1.2.3.1.2 "><p id="p27821751155220"><a name="p27821751155220"></a><a name="p27821751155220"></a>WAF mode of the protected domain name</p>
    <a name="ul87831351155214"></a><a name="ul87831351155214"></a><ul id="ul87831351155214"><li><span class="parmvalue" id="parmvalue20374113365019"><a name="parmvalue20374113365019"></a><a name="parmvalue20374113365019"></a><b>Enabled</b></span>: WAF is enabled.</li><li><span class="parmvalue" id="parmvalue28710829111810"><a name="parmvalue28710829111810"></a><a name="parmvalue28710829111810"></a><b>Disabled</b></span>: WAF is disabled.</li><li><span class="parmvalue" id="parmvalue394717218275"><a name="parmvalue394717218275"></a><a name="parmvalue394717218275"></a><b>Bypassed</b></span>: In this mode, requests are directly sent to the backend server without passing through WAF.</li></ul>
    </td>
    </tr>
    <tr id="row478315116526"><td class="cellrowborder" valign="top" width="37.11%" headers="mcps1.2.3.1.1 "><p id="p17783105135211"><a name="p17783105135211"></a><a name="p17783105135211"></a>DNS</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.89%" headers="mcps1.2.3.1.2 "><p id="p15783251155213"><a name="p15783251155213"></a><a name="p15783251155213"></a>DNS resolution status</p>
    <a name="ul478345116523"></a><a name="ul478345116523"></a><ul id="ul478345116523"><li><strong id="b33911916711"><a name="b33911916711"></a><a name="b33911916711"></a>Unconfigured</strong>: The domain name is not connected to WAF or domain connection fails. Refer to <a href="what-should-i-do-if-the-dns-status-is-unconfigured.md">What Should I Do If the DNS Status Is Unconfigured?</a> to solve the problem.</li><li><strong id="b61076368385"><a name="b61076368385"></a><a name="b61076368385"></a>Normal</strong>: The domain name is connected to WAF.</li></ul>
    </td>
    </tr>
    <tr id="row1378315513523"><td class="cellrowborder" valign="top" width="37.11%" headers="mcps1.2.3.1.1 "><p id="p7783451205220"><a name="p7783451205220"></a><a name="p7783451205220"></a>Protection Status over Past 3 Days</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.89%" headers="mcps1.2.3.1.2 "><p id="p167835516520"><a name="p167835516520"></a><a name="p167835516520"></a>Protection status of the domain name over the past three days. Choose <strong id="b62357357308"><a name="b62357357308"></a><a name="b62357357308"></a>More &gt;View Attack</strong> in the <strong id="b79611239203020"><a name="b79611239203020"></a><a name="b79611239203020"></a>Operation</strong> column to view specific protection logs.</p>
    </td>
    </tr>
    <tr id="row137841551105220"><td class="cellrowborder" valign="top" width="37.11%" headers="mcps1.2.3.1.1 "><p id="p1878445145210"><a name="p1878445145210"></a><a name="p1878445145210"></a>Policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.89%" headers="mcps1.2.3.1.2 "><p id="p47841051115212"><a name="p47841051115212"></a><a name="p47841051115212"></a>Policy configuration of the domain name. Click <strong id="b18736245174219"><a name="b18736245174219"></a><a name="b18736245174219"></a>Configure Policy</strong> to configure rules. For details, see <a href="rule_configurations.rst">Rule Configurations</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  In the  **Name**  column, click the target domain name to go to the basic information page.
5.  View domain information.
    1.  View  **Basic Information**  and  **WAF Information**. See  [Figure 2](#fig1902122615546)  and  [Figure 3](#fig16903112618542).

        In the upper right corner of the domain information page, click  ![](figures/icon-refresh.png)  to refresh the page.

        **Figure  2**  Viewing basic information \(with a proxy\)<a name="fig1902122615546"></a>  
        ![](figures/viewing-basic-information-(with-a-proxy).png "viewing-basic-information-(with-a-proxy)")

        >![](/images/icon-note.gif) **NOTE:**   
        >-   **Domain ID**: unique ID of a domain name that is generated randomly  
        >-   **Creation Time**: time when a domain name is created  
        >-   Click  ![](figures/icon-copy.png)  in the  **Access Address**,  **Subdomain Name**,  **TXT Record**, or  **WAF IP Address Range**  row to copy the required value.  
        >-   To update a certificate if  **Client Protocol**  is  **HTTPS**, click  ![](figures/icon-edit.png)  next to the value of  **Certificate Name**. In the dialog box displayed, select an existing certificate.  
        >-   If your web server stops using a proxy, click  ![](figures/icon-edit.png)  next to the value of  **Proxy Configured**. In the dialog box displayed, select  **No**.  

        **Figure  3**  Viewing basic information \(without a proxy\)<a name="fig16903112618542"></a>  
        ![](figures/viewing-basic-information-(without-a-proxy).png "viewing-basic-information-(without-a-proxy)")

        >![](/images/icon-note.gif) **NOTE:**   
        >-   **Domain ID**: unique ID of a domain name that is generated randomly  
        >-   **Creation Time**: time when a domain name is created  
        >-   Click  ![](figures/icon-copy.png)  in the target row to copy the value of  **CNAME**  or  **WAF IP Address Range**.  
        >-   To update a certificate if  **Client Protocol**  is  **HTTPS**, click  ![](figures/icon-edit.png)  next to the value of  **Certificate Name**. In the dialog box displayed, select an existing certificate.  
        >-   If your web server starts using a proxy, click  ![](figures/icon-edit.png)  next to the value of  **Proxy Configured**. In the dialog box displayed, select  **Yes**.  

    2.  View  **Server Information**.

        **Figure  4**  Server Information<a name="fig104141220121620"></a>  
        ![](figures/server-information.png "server-information")

        Click  **Edit Server Information**. On the  **Edit Server Information**  page shown in  [Figure 5](#fig3368635172714), edit server configurations \(such as client protocol and associated certificate\).

        **Figure  5**  Editing server information<a name="fig3368635172714"></a>  
        ![](figures/editing-server-information.png "editing-server-information")

        >![](/images/icon-note.gif) **NOTE:**   
        >Web Application Firewall \(WAF\) does not support health check. If you want to use health check, use WAF along with Elastic Load Balancing \(ELB\). For details about how to configure ELB, see  [Backend Server \(Enhanced Load Balancer\)](https://docs.otc.t-systems.com/en-us/usermanual/elb/en-us_topic_0052569729.html). After ELB is configured, the elastic IP address \(EIP\) of ELB is used as the value of  **Server Address**  to connect to WAF for health check.  

    3.  Click the  **Tags**  tab and view the tags, as shown in  [Figure 6](#fig1814661617294).

        **Figure  6**  Tags<a name="fig1814661617294"></a>  
        ![](figures/tags.png "tags")

        -   In the  **Operation**  column of the tag list, click  **Edit**  to change the value.
        -   Click  **Delete**  to delete a tag. A deleted tag cannot be restored. Exercise caution when performing this operation.
        -   In the upper left corner of the tag list, click  **Add Tag**  to add one. See  [Figure 7](#fig0811031133312).

            You can select an existing tag key and tag value from the  **Tag key**  and  **Tag value**  drop-down lists or click  **View predefined tags**  to create a tag on the TMS console.

            **Figure  7**  Add Tag<a name="fig0811031133312"></a>  
            ![](figures/add-tag.png "add-tag")




## Related Operations<a name="section125161643628"></a>

In the  **Operation**  column of the domain list

-   Click  **Switch Mode**  to switch the WAF mode.
-   Click  **Configure Policy**  to configure WAF protection rules.
-   Choose  **More**  \>  **Check DNS**  to check the DNS resolution status.
-   Choose  **More**  \>  **View Attack**  to view WAF protection logs.
-   Choose  **More**  \>  **View Metric**  to view WAF monitoring logs. For details, see the  _Cloud Eye User Guide_.
-   Choose  **More**  \>  **Delete**  to delete a domain name.

