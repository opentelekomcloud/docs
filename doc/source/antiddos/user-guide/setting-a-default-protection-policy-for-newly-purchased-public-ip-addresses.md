# Setting a Default Protection Policy for Newly Purchased Public IP Addresses<a name="EN-US_TOPIC_0258573747"></a>

After you set a default protection policy, the newly purchased public IP addresses will be protected based on the default protection policy.

## Prerequisites<a name="section2445144802214"></a>

You have obtained an account and its password to log in to the management console.

## Procedure<a name="section153322312232"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon_dt-0.png)  in the upper left corner and select the desired region or project.
3.  Choose  **Security**  \>  **Anti-DDoS**. The Anti-DDoS service management page is displayed.
4.  The  **Public IP Addresses**  tab page is displayed by default. Click  **Set Default Protection Policy**.

    **Figure  1**  Setting a default protection policy for newly purchased public ip addresses<a name="fig87135471034"></a>  
    ![](figures/setting-a-default-protection-policy-for-newly-purchased-public-ip-addresses.png "setting-a-default-protection-policy-for-newly-purchased-public-ip-addresses")

5.  Configure the default protection policy.

    **Figure  2**  Configuring the default protection policy<a name="fig182831259165614"></a>  
    ![](figures/configuring-the-default-protection-policy.png "configuring-the-default-protection-policy")

    **Table  1**  Parameter description

    <a name="table1245516550574"></a>
    <table><thead align="left"><tr id="ree2ae48f896d4ec2bede69c7f3faa943"><th class="cellrowborder" valign="top" width="20.39%" id="mcps1.2.3.1.1"><p id="a13a961abe1bd4ae7833413b2d60d3077"><a name="a13a961abe1bd4ae7833413b2d60d3077"></a><a name="a13a961abe1bd4ae7833413b2d60d3077"></a><strong id="b10104174220432"><a name="b10104174220432"></a><a name="b10104174220432"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="79.61%" id="mcps1.2.3.1.2"><p id="adcd709073c4c4f5ead440f1540e21651"><a name="adcd709073c4c4f5ead440f1540e21651"></a><a name="adcd709073c4c4f5ead440f1540e21651"></a><strong id="b1757813433435"><a name="b1757813433435"></a><a name="b1757813433435"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row462471113516"><td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.2.3.1.1 "><p id="p4888314215513"><a name="p4888314215513"></a><a name="p4888314215513"></a>Traffic Cleaning Threshold</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.61%" headers="mcps1.2.3.1.2 "><p id="p9617192718260"><a name="p9617192718260"></a><a name="p9617192718260"></a>Anti-DDoS scrubs traffic when detecting that the incoming traffic of an IP address exceeds the threshold.</p>
    <p id="p19162832630"><a name="p19162832630"></a><a name="p19162832630"></a>Configure this parameter based on your actual needs. You are advised to set the threshold to a value closest to the purchased bandwidth but not greater than the purchased bandwidth.</p>
    <p id="p1919135214219"><a name="p1919135214219"></a><a name="p1919135214219"></a>If <strong id="b78681410124619"><a name="b78681410124619"></a><a name="b78681410124619"></a>Traffic Cleaning Threshold</strong> is set to <strong id="b8566213124610"><a name="b8566213124610"></a><a name="b8566213124610"></a>Unlimited</strong>, your public IP addresses get almost no protection from DDoS attacks.</p>
    </td>
    </tr>
    <tr id="row13123900172033"><td class="cellrowborder" valign="top" width="20.39%" headers="mcps1.2.3.1.1 "><p id="p6111610215513"><a name="p6111610215513"></a><a name="p6111610215513"></a>CC Defense</p>
    </td>
    <td class="cellrowborder" valign="top" width="79.61%" headers="mcps1.2.3.1.2 "><a name="ul937993715513"></a><a name="ul937993715513"></a><ul id="ul937993715513"><li><strong id="b1535524712474"><a name="b1535524712474"></a><a name="b1535524712474"></a>Disable</strong>: disables the defense.</li><li><strong id="b1375875711472"><a name="b1375875711472"></a><a name="b1375875711472"></a>Enable</strong>: enables the defense.<div class="note" id="en-us_topic_0204851514_note34180542121252"><a name="en-us_topic_0204851514_note34180542121252"></a><a name="en-us_topic_0204851514_note34180542121252"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0204851514_p39189427121252"><a name="en-us_topic_0204851514_p39189427121252"></a><a name="en-us_topic_0204851514_p39189427121252"></a>CC defense is available only for clients supporting the full HTTP protocol stack because CC defense works in redirection or redirection+verification code mode. If your client does not support the full HTTP protocol stack, you are advised to disable CC defense.</p>
    </div></div>
    </li><li><strong id="b18153154104820"><a name="b18153154104820"></a><a name="b18153154104820"></a>HTTP Request Threshold</strong><p id="en-us_topic_0204851514_p47233133112711"><a name="en-us_topic_0204851514_p47233133112711"></a><a name="en-us_topic_0204851514_p47233133112711"></a>This option is available only when CC defense is enabled.</p>
    <p id="en-us_topic_0204851514_p728529515513"><a name="en-us_topic_0204851514_p728529515513"></a><a name="en-us_topic_0204851514_p728529515513"></a>You are advised to set this parameter to the maximum number of HTTP requests that can be processed by the deployed service. Anti-DDoS automatically scrubs traffic if the total number of detected requests exceeds this threshold. If the value is too large, CC defense will not be triggered promptly.</p>
    <a name="en-us_topic_0204851514_ul1623789311289"></a><a name="en-us_topic_0204851514_ul1623789311289"></a><ul id="en-us_topic_0204851514_ul1623789311289"><li>If the actual HTTP request rate is smaller than the configured value, the deployed service is able to process all HTTP requests, and Anti-DDoS does not need to be involved.</li><li>If the actual HTTP request rate is greater than or equal to the configured value, Anti-DDoS triggers CC defense to analyze and check each request, which affects responses to normal requests.</li></ul>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **OK**.

    After the default protection policy is set, the newly purchased public IP addresses are protected based on the default protection policy. For details about how to adjust a configured protection policy, see  [Adjusting Security Settings](adjusting-security-settings.md).


