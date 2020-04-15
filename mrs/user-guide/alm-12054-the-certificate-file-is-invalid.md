# ALM-12054 The Certificate File Is Invalid<a name="EN-US_TOPIC_0125375904"></a>

## Description<a name="se385bb5842bf480aa1cd91aa01cd8cf8"></a>

The system checks whether the certificate file is invalid \(has expired or is not yet valid\) on 23:00 every day. This alarm is generated when the certificate file is invalid.

This alarm is cleared if the status of the newly imported certificate is valid.

## Attribute<a name="s20aa1df745f943c7861c65bff6752cba"></a>

<a name="tb846f9c7ae5b47eb8957db28f8f74846"></a>
<table><thead align="left"><tr id="rccc307a5360c46f09ae3f5e29c2ed171"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a68ebbbaae0f44e888a2432c65fcb8044"><a name="a68ebbbaae0f44e888a2432c65fcb8044"></a><a name="a68ebbbaae0f44e888a2432c65fcb8044"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a301829e3d92145f89dd984209d1a0130"><a name="a301829e3d92145f89dd984209d1a0130"></a><a name="a301829e3d92145f89dd984209d1a0130"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="aab65cc59abf84c1685d40b5e3b8378e0"><a name="aab65cc59abf84c1685d40b5e3b8378e0"></a><a name="aab65cc59abf84c1685d40b5e3b8378e0"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="rc90cd2b8d1da41a9b2dcdbfd35f56b28"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a5c297d65e12841189653766ac6dbca20"><a name="a5c297d65e12841189653766ac6dbca20"></a><a name="a5c297d65e12841189653766ac6dbca20"></a>12054</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a333af1b4367348f19adf86a73049dd51"><a name="a333af1b4367348f19adf86a73049dd51"></a><a name="a333af1b4367348f19adf86a73049dd51"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a02bb1838f9cf43188eab7b3af5dc97a3"><a name="a02bb1838f9cf43188eab7b3af5dc97a3"></a><a name="a02bb1838f9cf43188eab7b3af5dc97a3"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s98bf12c77584462f9467499abb61c661"></a>

<a name="t1fef8dda823a4b8dad4a8ce5754220d0"></a>
<table><thead align="left"><tr id="rccef79a078214dfb929f654d3f184d93"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a361f294a2e884172b040924418a1709c"><a name="a361f294a2e884172b040924418a1709c"></a><a name="a361f294a2e884172b040924418a1709c"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a43c2bacce2044b619433c4732f5870aa"><a name="a43c2bacce2044b619433c4732f5870aa"></a><a name="a43c2bacce2044b619433c4732f5870aa"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r09c1b2a2c9364f34b370c4251626a520"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a882b5e3bc93d4dd8a214fb79e16aaf1c"><a name="a882b5e3bc93d4dd8a214fb79e16aaf1c"></a><a name="a882b5e3bc93d4dd8a214fb79e16aaf1c"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a10f0ea544d4f47fea8e505ffcab16042"><a name="a10f0ea544d4f47fea8e505ffcab16042"></a><a name="a10f0ea544d4f47fea8e505ffcab16042"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r8daefd854cc544bcb0b45ac4ffd5bc21"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a3295c62f397c40cbbfdab02a1d16ee59"><a name="a3295c62f397c40cbbfdab02a1d16ee59"></a><a name="a3295c62f397c40cbbfdab02a1d16ee59"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a98ba6c6e2d4a4734bc151897c63c26bb"><a name="a98ba6c6e2d4a4734bc151897c63c26bb"></a><a name="a98ba6c6e2d4a4734bc151897c63c26bb"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rce5edf01720b4968a11ba2a6228a1c8d"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a68d89f7538794d0787188e6e9c236e65"><a name="a68d89f7538794d0787188e6e9c236e65"></a><a name="a68d89f7538794d0787188e6e9c236e65"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a54e2c62f3e064ead903c0fb64c56f7e8"><a name="a54e2c62f3e064ead903c0fb64c56f7e8"></a><a name="a54e2c62f3e064ead903c0fb64c56f7e8"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s0334a0c9d40c4a48af27318eded0116a"></a>

The system reminds users that the certificate file is invalid. If the certificate file expires, some functions are restricted and cannot be used properly.

## Possible Causes<a name="s986b913f3c50478bbee1646b5bec70a0"></a>

No HA root certificate or HA user certificate is imported, certificate import fails or the certificate file is invalid.

## Procedure<a name="s4d53019ab5e34258ac2d2edba766cb48"></a>

**Locate the alarm cause.**

1.  On MRS Manager, view the real-time alarm list and locate the target alarm.

    In the  **Alarm Details**  area, view the additional information about the alarm.

    -   If  **CA Certificate**  is displayed in the additional information, use PuTTY to log in to the active OMS node as user  **omm**  and go to  [2](#ldc52a42db13d48328a026bff9dd75530).
    -   If  **HA root Certificate**  is displayed in the additional information, check  **Location**  to obtain the name of the host involved in this alarm. Then use PuTTY to log in to the host as user  **omm**  and go to  [3](#l7262e1dca30a4c2f84cfa9c2dd551e41).
    -   If  **HA server Certificate**  is displayed in the additional information, check  **Location**  to obtain the name of the host involved in this alarm. Then use PuTTY to log in to the host as user  **omm**  and go to  [4](#lb5b3ee755a6044bc83c8773257f0e40b).


**Check the validity period of the certificate file.**

1.  <a name="ldc52a42db13d48328a026bff9dd75530"></a>Check whether the current system time is in the validity period of the CA certificate.

    Run the  **openssl x509 -noout -text -in $\{CONTROLLER\_HOME\}/security/cert/root/ca.crt**  command to check the effective time and due time of the CA certificate.

    -   If yes, go to  [8](#l53a3fb0662f149f4abebb00abc8da359).
    -   If no, go to  [5](#lf410375ea78240ec816195bb8ecb2de2).

2.  <a name="l7262e1dca30a4c2f84cfa9c2dd551e41"></a>Check whether the current system time is in the validity period of the HA root certificate.

    Run the  **openssl x509 -noout -text -in $\{CONTROLLER\_HOME\}/security/certHA/root-ca.crt**  command to check the effective time and expiration time of the HA root certificate.

    -   If yes, go to  [8](#l53a3fb0662f149f4abebb00abc8da359).
    -   If no, go to  [6](#l6a0fcc42838d4695a806d210674f050d).

3.  <a name="lb5b3ee755a6044bc83c8773257f0e40b"></a>Check whether the current system time is in the validity period of the HA user certificate.

    Run the  **openssl x509 -noout -text -in $\{CONTROLLER\_HOME\}/security/certHA/server.crt**  command to check the effective time and expiration time of the HA user certificate.

    -   If yes, go to  [8](#l53a3fb0662f149f4abebb00abc8da359).
    -   If no, go to  [6](#l6a0fcc42838d4695a806d210674f050d).

        The example of the effective time and expiration time of the HA/CA certificate:

        ```
        Certificate: 
            Data: 
                Version: 3 (0x2) 
                Serial Number: 
                    97:d5:0e:84:af:ec:34:d8 
                Signature Algorithm: sha256WithRSAEncryption 
               Issuer: C=CountryName, ST=State, L=Locality, O=Organization, OU=IT, CN=HADOOP.COM 
                Validity 
                    Not Before: Dec 13 06:38:26 2016 GMT           //The effective time. 
                    Not After : Dec 11 06:38:26 2026 GMT             //The expiration time.
        ```



**Import the certificate file.**

1.  <a name="lf410375ea78240ec816195bb8ecb2de2"></a>Import a new CA certificate file.

    Apply for or generate a CA certificate file and import it to the system. For details, see section  **Replacing HA Certificates**  in the  _Administrator Guide_. Manually clear the alarm and check whether this alarm is generated again during periodic check.

    -   If yes, go to  [8](#l53a3fb0662f149f4abebb00abc8da359)
    -   If no, no further action is required.

2.  <a name="l6a0fcc42838d4695a806d210674f050d"></a>Import a new HA certificate file.

    Apply for or generate an HA certificate file and import it to the system. For details, see section R**eplacing HA Certificates**  in the  _Administrator Guide_. Manually clear the alarm and check whether this alarm is generated again during periodic check.

    -   If yes, go to  [8](#l53a3fb0662f149f4abebb00abc8da359).
    -   If no, no further action is required.


**Collect fault information.**

1.  On MRS Manager, choose  **System**  \>  **Export Log**.
2.  <a name="l53a3fb0662f149f4abebb00abc8da359"></a>Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="s7685691e28ee4bfc9d341dcc8bb04b46"></a>

N/A

