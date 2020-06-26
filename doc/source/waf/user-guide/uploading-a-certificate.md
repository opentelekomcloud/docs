# Uploading a Certificate<a name="waf_01_0090"></a>

This section describes how to upload a certificate.

## Prerequisites<a name="section1573014715269"></a>

Login credentials have been obtained.

## Procedure<a name="section12454862811"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Choose  **Security**  \>  **Web Application Firewall**.
4.  In the navigation pane, choose  **Certificates**. The  **Certificates**  page is displayed, as shown in  [Figure 1](#fig29851531163210).

    **Figure  1**  Certificates<a name="fig29851531163210"></a>  
    ![](figures/certificates.png "certificates")

5.  In the upper right corner of the page, click  **Upload Certificate**. The  **Upload Certificate**  dialog box is displayed. Enter the certificate name, and copy and paste the certificate content and private key to the corresponding text boxes. See  [Figure 2](#fig682518517383).

    **Figure  2**  Uploading a certificate<a name="fig682518517383"></a>  
    ![](figures/uploading-a-certificate.png "uploading-a-certificate")

    >![](/images/icon-note.gif) **NOTE:**   
    >WAF encrypts and saves the private key to keep it safe.  

    Currently, only .pem certificates are supported. If the certificate is not in .pem format, convert it into a .pem certificate by referring to  [Table 1](#waf_01_0002_table1184924815910)  before uploading.

    **Table  1**  Certificate conversion commands

    <a name="waf_01_0002_table1184924815910"></a>
    <table><thead align="left"><tr id="waf_01_0002_row2847448797"><th class="cellrowborder" valign="top" width="21.990000000000002%" id="mcps1.2.3.1.1"><p id="waf_01_0002_p98475489920"><a name="waf_01_0002_p98475489920"></a><a name="waf_01_0002_p98475489920"></a>Format</p>
    </th>
    <th class="cellrowborder" valign="top" width="78.01%" id="mcps1.2.3.1.2"><p id="waf_01_0002_p18847164813920"><a name="waf_01_0002_p18847164813920"></a><a name="waf_01_0002_p18847164813920"></a>How to Convert (In Linux OSs)</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="waf_01_0002_row1784719481093"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.3.1.1 "><p id="waf_01_0002_p68471489919"><a name="waf_01_0002_p68471489919"></a><a name="waf_01_0002_p68471489919"></a>CER/CRT</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.01%" headers="mcps1.2.3.1.2 "><p id="waf_01_0002_p88479481916"><a name="waf_01_0002_p88479481916"></a><a name="waf_01_0002_p88479481916"></a>Rename the <strong id="waf_01_0002_b84235270691740"><a name="waf_01_0002_b84235270691740"></a><a name="waf_01_0002_b84235270691740"></a>cert.crt</strong> certificate file to <strong id="waf_01_0002_b84235270691747"><a name="waf_01_0002_b84235270691747"></a><a name="waf_01_0002_b84235270691747"></a>cert.pem</strong>.</p>
    </td>
    </tr>
    <tr id="waf_01_0002_row1484714481196"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.3.1.1 "><p id="waf_01_0002_p14847164816915"><a name="waf_01_0002_p14847164816915"></a><a name="waf_01_0002_p14847164816915"></a>PFX</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.01%" headers="mcps1.2.3.1.2 "><a name="waf_01_0002_ol178472048299"></a><a name="waf_01_0002_ol178472048299"></a><ol id="waf_01_0002_ol178472048299"><li>Run the following command to obtain a private key. For example, to convert <strong id="waf_01_0002_b124221289249"><a name="waf_01_0002_b124221289249"></a><a name="waf_01_0002_b124221289249"></a>cert.pfx</strong> into <strong id="waf_01_0002_b1423152892418"><a name="waf_01_0002_b1423152892418"></a><a name="waf_01_0002_b1423152892418"></a>cert.key</strong>, run:<p id="waf_01_0002_p18476481912"><a name="waf_01_0002_p18476481912"></a><a name="waf_01_0002_p18476481912"></a><strong id="waf_01_0002_b78471748295"><a name="waf_01_0002_b78471748295"></a><a name="waf_01_0002_b78471748295"></a>openssl pkcs12 -in cert.pfx -nocerts -out cert.key -nodes</strong></p>
    </li><li>Run the following command to obtain a certificate. For example, to convert <strong id="waf_01_0002_b15328203542412"><a name="waf_01_0002_b15328203542412"></a><a name="waf_01_0002_b15328203542412"></a>cert.pfx</strong> into <strong id="waf_01_0002_b4329335122416"><a name="waf_01_0002_b4329335122416"></a><a name="waf_01_0002_b4329335122416"></a>cert.pem</strong>, run:<p id="waf_01_0002_p168471248296"><a name="waf_01_0002_p168471248296"></a><a name="waf_01_0002_p168471248296"></a><strong id="waf_01_0002_b10847164818913"><a name="waf_01_0002_b10847164818913"></a><a name="waf_01_0002_b10847164818913"></a>openssl pkcs12 -in cert.pfx -nokeys -out cert.pem</strong></p>
    </li></ol>
    </td>
    </tr>
    <tr id="waf_01_0002_row15847548495"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.3.1.1 "><p id="waf_01_0002_p12847448399"><a name="waf_01_0002_p12847448399"></a><a name="waf_01_0002_p12847448399"></a>P7B</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.01%" headers="mcps1.2.3.1.2 "><p id="waf_01_0002_p784720481898"><a name="waf_01_0002_p784720481898"></a><a name="waf_01_0002_p784720481898"></a>Run the following command to convert a certificate. For example, to convert <strong id="waf_01_0002_b1992263817248"><a name="waf_01_0002_b1992263817248"></a><a name="waf_01_0002_b1992263817248"></a>cert.p7b</strong> into <strong id="waf_01_0002_b1922113812413"><a name="waf_01_0002_b1922113812413"></a><a name="waf_01_0002_b1922113812413"></a>cert.pem</strong>, run:</p>
    <p id="waf_01_0002_p384734812910"><a name="waf_01_0002_p384734812910"></a><a name="waf_01_0002_p384734812910"></a><strong id="waf_01_0002_b884754812912"><a name="waf_01_0002_b884754812912"></a><a name="waf_01_0002_b884754812912"></a>openssl pkcs7 -print_certs -in cert.p7b -out cert.pem</strong></p>
    </td>
    </tr>
    <tr id="waf_01_0002_row12849154819915"><td class="cellrowborder" valign="top" width="21.990000000000002%" headers="mcps1.2.3.1.1 "><p id="waf_01_0002_p1984713481495"><a name="waf_01_0002_p1984713481495"></a><a name="waf_01_0002_p1984713481495"></a>DER</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.01%" headers="mcps1.2.3.1.2 "><p id="waf_01_0002_p208499482912"><a name="waf_01_0002_p208499482912"></a><a name="waf_01_0002_p208499482912"></a>Run the following command to obtain a certificate. For example, to convert <strong id="waf_01_0002_b1580714614246"><a name="waf_01_0002_b1580714614246"></a><a name="waf_01_0002_b1580714614246"></a>privatekey.der</strong> into <strong id="waf_01_0002_b58072461245"><a name="waf_01_0002_b58072461245"></a><a name="waf_01_0002_b58072461245"></a>cert.key</strong>, run:</p>
    <p id="waf_01_0002_p118496487916"><a name="waf_01_0002_p118496487916"></a><a name="waf_01_0002_p118496487916"></a><strong id="waf_01_0002_b118494481997"><a name="waf_01_0002_b118494481997"></a><a name="waf_01_0002_b118494481997"></a>openssl rsa -inform DER -outform PEM -in privatekey.der -out cert.key</strong></p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **OK**.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   If the number of uploaded certificates reaches the upper limit, refer to  [Deleting a Certificate](deleting-a-certificate.md)  to delete a certificate that is not associated with any domain name and then upload a certificate again.  
    >-   To modify a certificate name, click  ![](figures/icon-edit.png)  next to the target certificate name in the  **Certificate Name**  column.  


