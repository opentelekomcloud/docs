# Configuring the Minimum TLS Version and Cipher Suite<a name="waf_01_0093"></a>

The Transport Layer Security \(TLS\) protocol provides confidentiality and integrity of data sent between applications over the Internet. HTTPS is a network protocol constructed based on TLS and HTTP for encrypted transmission and identity authentication. When  **Client Protocol**  for a domain name to be protected is set to  **HTTPS**, you can use WAF to set the minimum TLS version and cipher suite \(a set of cryptographic algorithms\) for the domain name. All requests using the TLS earlier than the minimum TLS version cannot access the protected domain names so that your service is secured.

If  **Client Protocol**  for the domain name to be protected is set to  **HTTP**, TLS is not involved. In this case, skip this section.

TLS v1.1 and the default cipher suite are configured by default in WAF for general security. To better protect your services, you are advised to set the minimum TLS version to a later version and cipher suite to the one having higher security.

## Prerequisites<a name="section1032870191810"></a>

-   The domain name to be protected has been added.
-   **Client Protocol**  is set to  **HTTPS**  for the protected domain name.

## Procedure<a name="section15716426818"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner of the management console and select a region or project.
3.  Click  **Service List**  in the upper right corner of the page and choose  **Security**  \>  **Web Application Firewall**  \>  **Domains**.

    **Figure  1**  Entrance to  **Domains**<a name="fig1174417294716"></a>  
    ![](figures/entrance-to-domains.png "entrance-to-domains")

4.  In the  **Name**  column, click the target domain name to go to the basic information page.
5.  Click  ![](figures/icon-edit.png)  next to the cipher suite name in the row where  **TLS Configuration**  locates.

    **Figure  2**  Modifying TLS configurations<a name="fig31611341193116"></a>  
    ![](figures/modifying-tls-configurations.png "modifying-tls-configurations")

6.  In the  **TLS Configuration**  dialog box, select the minimum TLS version and cipher suite.  [Table 1](#table205284916443)  describes the parameters.

    **Figure  3**  TLS Configuration<a name="fig20250182114398"></a>  
    ![](figures/tls-configuration.png "tls-configuration")

    **Table  1**  TLS configuration parameters

    <a name="table205284916443"></a>
    <table><thead align="left"><tr id="row1352813913442"><th class="cellrowborder" valign="top" width="25.5%" id="mcps1.2.3.1.1"><p id="p1352889184415"><a name="p1352889184415"></a><a name="p1352889184415"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="74.5%" id="mcps1.2.3.1.2"><p id="p1352817912445"><a name="p1352817912445"></a><a name="p1352817912445"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row125291984418"><td class="cellrowborder" valign="top" width="25.5%" headers="mcps1.2.3.1.1 "><p id="p95293910441"><a name="p95293910441"></a><a name="p95293910441"></a>Minimum TLS Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.5%" headers="mcps1.2.3.1.2 "><p id="p178511840162113"><a name="p178511840162113"></a><a name="p178511840162113"></a>Minimum TLS version for accessing the protected domain name</p>
    <a name="ul88021419192214"></a><a name="ul88021419192214"></a><ul id="ul88021419192214"><li>TLS v1.1: Requests using TLS v1.1 or later can access the domain name.</li><li>TLS v1.2: Requests using TLS v1.2 or later can the access domain name.</li></ul>
    <div class="notice" id="note41011232114518"><a name="note41011232114518"></a><a name="note41011232114518"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p4101183212458"><a name="p4101183212458"></a><a name="p4101183212458"></a>Cipher suite 2 is not supported if TLS v1.1 is selected.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row8586125264411"><td class="cellrowborder" valign="top" width="25.5%" headers="mcps1.2.3.1.1 "><p id="p1658745234410"><a name="p1658745234410"></a><a name="p1658745234410"></a>Cipher Suite</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.5%" headers="mcps1.2.3.1.2 "><a name="ul057093310216"></a><a name="ul057093310216"></a><ul id="ul057093310216"><li><strong id="b120917538103"><a name="b120917538103"></a><a name="b120917538103"></a>Default cipher suite</strong>: Good browser compatibility, most clients supported, sufficient for most scenarios</li><li><strong id="b14522731151117"><a name="b14522731151117"></a><a name="b14522731151117"></a>Cipher suite 1</strong>: Recommended configuration, best combination of compatibility and security</li><li><strong id="b101363559137"><a name="b101363559137"></a><a name="b101363559137"></a>Cipher suite 2</strong>: Strict compliance with forward secrecy requirements of PCI DSS and excellent protection, but older browsers may be unable to access the websites</li><li><strong id="b2747911121412"><a name="b2747911121412"></a><a name="b2747911121412"></a>Cipher suite 3</strong>: Support for ECDHE, DHE-GCM, and RSA-AES-GCM algorithms but not CBC</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

