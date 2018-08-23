# What Is CAA?<a name="dns_faq_032"></a>

Certification Authority Authorization \(CAA\) is a way to ensure that HTTPS certificates are issued by authorized certificate authorities \(CAs\). It is in compliance with IETF RFC6844 specifications. Since September 8, 2017, all CAs are required to check CAA records before issuing a certificate.

## CAA Specifications<a name="section78537244532"></a>

Domain name owners can create CAA records to specify that authorized CAs issue certificates for their domain names.

In the world, hundreds of CAs have the right to issue HTTPS certificates to verify identity of a website. CAA allows you to create a website of specified CAs that are authorized to issue HTTPS certificates for particular domain names to prevent possibly fraudulent certificates. Setting CAA records is a way to enhance security of your websites.

CAs will perform a DNS lookup for CAA records when they issue certificates.

-   If a CA does not find any CAA record, it can issue a certificate for the domain name.

    In this case, any CA is able to issue a certificate for this domain name, and it may be a fraudulent certificate.

-   If the CA finds a CAA record that authorizes it to issue certificates, it will issue a certificate for the domain name.
-   If the CA finds a CAA record but the record does not authorize it to issue certificates, the CA will not be able to issue HTTPS certificate for the domain name. As a result, certificates are not incorrectly issued.

## CAA Record<a name="section167971597533"></a>

A CAA record consists of a flag byte **\[flag\]**, a property tag, and a property value **\[tag\]-\[value\]**. You can create multiple CAA records for a domain name.

**Table 1** Configuration of CAA records

<a name="table17725641112120"></a><table><thead align="left"><tr id="row187268412211"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.1"><p id="p17260416215"><a name="p17260416215"></a><a name="p17260416215"></a>Function</p>
</th>
<th class="cellrowborder" valign="top" width="36%" id="mcps1.2.4.1.2"><p id="p107261741132119"><a name="p107261741132119"></a><a name="p107261741132119"></a>Example</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.4.1.3"><p id="p6726104110214"><a name="p6726104110214"></a><a name="p6726104110214"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row117262041172112"><td class="cellrowborder" rowspan="2" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p137261841172118"><a name="p137261841172118"></a><a name="p137261841172118"></a>Configure a CAA record for one domain name.</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p19726184114218"><a name="p19726184114218"></a><a name="p19726184114218"></a>domain.com.  CAA 0 issue "ca.example.com"</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p45933152818"><a name="p45933152818"></a><a name="p45933152818"></a>Only the specified CA (<strong id="b193760717517189"><a name="b193760717517189"></a><a name="b193760717517189"></a>ca.example.com</strong>) can issue certificates for a particular domain name (<strong id="b110240485517189"><a name="b110240485517189"></a><a name="b110240485517189"></a>domain.com</strong>). Requests to issue certificates for the domain name by other CAs will be rejected.</p>
</td>
</tr>
<tr id="row127268411218"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p072612416211"><a name="p072612416211"></a><a name="p072612416211"></a>domain.com.  CAA 0 issue ";"</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p14726134152119"><a name="p14726134152119"></a><a name="p14726134152119"></a>No CA is allowed to issue certificates for the domain name (<strong id="b84235270615569"><a name="b84235270615569"></a><a name="b84235270615569"></a>domain.com</strong>).</p>
</td>
</tr>
<tr id="row5726341122120"><td class="cellrowborder" rowspan="2" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p149740122612"><a name="p149740122612"></a><a name="p149740122612"></a>Configure that the CA reports to the domain name holder.</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p1172624172110"><a name="p1172624172110"></a><a name="p1172624172110"></a>domain.com. CAA 0 iodef "mailto:admin@domain.com"</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p572613411210"><a name="p572613411210"></a><a name="p572613411210"></a>When a certificate is requested that violates the CAA record, the CA will notify the domain name holder of the violation.</p>
</td>
</tr>
<tr id="row6726114118217"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1472634172117"><a name="p1472634172117"></a><a name="p1472634172117"></a>domain.com. CAA 0 iodef "http:// domain.com/log/"</p>
<p id="p15945133714424"><a name="p15945133714424"></a><a name="p15945133714424"></a>domain.com. CAA 0 iodef "https:// domain.com/log/"</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p177261419213"><a name="p177261419213"></a><a name="p177261419213"></a>Requests to issue certificates by unauthorized CAs will be recorded.</p>
</td>
</tr>
<tr id="row1091554812514"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p15915144822517"><a name="p15915144822517"></a><a name="p15915144822517"></a>Authorize a CA to issue wildcard certificates.</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p591564812251"><a name="p591564812251"></a><a name="p591564812251"></a>domain.com. CAA 0 issuewild "ca.example.com"</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p69154484255"><a name="p69154484255"></a><a name="p69154484255"></a>The specified CA (<strong id="b8423527061622"><a name="b8423527061622"></a><a name="b8423527061622"></a>ca.example.com</strong>) can issue wildcard certificates for the domain name.</p>
</td>
</tr>
<tr id="row6815165112515"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p08156512257"><a name="p08156512257"></a><a name="p08156512257"></a>Configuration example</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p76671429277"><a name="p76671429277"></a><a name="p76671429277"></a>domain.com. CAA 0 issue "ca.abc.com"</p>
<p id="p3667742162717"><a name="p3667742162717"></a><a name="p3667742162717"></a>domain.com. CAA 0 issuewild "ca.def.com"</p>
<p id="p166794217275"><a name="p166794217275"></a><a name="p166794217275"></a>domain.com. CAA 0 iodef "mailto:admin@domain.com"</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p79761441164912"><a name="p79761441164912"></a><a name="p79761441164912"></a>The example configures a CAA record for the domain name <strong id="b8423527061647"><a name="b8423527061647"></a><a name="b8423527061647"></a>domain.com</strong>.</p>
<a name="ul2285344104918"></a><a name="ul2285344104918"></a><ul id="ul2285344104918"><li id="li20765750104917"><a name="li20765750104917"></a><a name="li20765750104917"></a>Only CA <strong id="b84235270616425"><a name="b84235270616425"></a><a name="b84235270616425"></a>ca.abc.com</strong> can issue certificates of all types.</li><li id="li6981012155212"><a name="li6981012155212"></a><a name="li6981012155212"></a>Only CA <strong id="b84235270616454"><a name="b84235270616454"></a><a name="b84235270616454"></a>ca.def.com</strong> can issue wildcard certificates.</li><li id="li12561158144911"><a name="li12561158144911"></a><a name="li12561158144911"></a>Any other CA is not allowed to issue certificates.</li><li id="li92852445491"><a name="li92852445491"></a><a name="li92852445491"></a>When a violation occurs, the CA sends a notification to <strong id="b84235270616554"><a name="b84235270616554"></a><a name="b84235270616554"></a>admin@domain.com</strong>.</li></ul>
</td>
</tr>
</tbody>
</table>

## Checking Whether a CAA Record Takes Effect<a name="section614411459319"></a>

You can verify a CAA record at [http://www.digwebinterface.com](http://www.digwebinterface.com/).

1.  Access [http://www.digwebinterface.com](http://www.digwebinterface.com/).
2.  Enter the following parameters:
    -   **Hostnames or IP addresses**: domain name of the CAA record to be checked
    -   **Type**: **CAA**
    -   **Options**: **Trace**
3.  Click **Dig**.

    **Figure 1** CAA record resolution result<a name="fig139761419101615"></a>
    ![](figures/caa-record-resolution-result.png "CAA record resolution result")


