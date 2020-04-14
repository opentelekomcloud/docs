# Creating a Certificate<a name="EN-US_TOPIC_0092382557"></a>

## Scenarios<a name="section55362545171830"></a>

To enable authentication for securing data transmission over HTTPS, ELB allows you to deploy certificates on load balancers. 

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   A certificate can be bound to one type of load balancer. Ensure that you have selected the correct type.  

## Create a Certificate<a name="section26868475171830"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0163776996.jpg)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  In the navigation pane, choose  **Certificates**.
5.  Click  **Create Certificate**. In the  **Create Certificate**  dialog box, configure the following parameters:
    -   **Load Balancer Type**: Select  **Enhanced**  or  **Classic**.
    -   **Certificate Name**
    -   **Certificate Type**
        -   **Server certificate**: used for SSL handshake negotiations when an HTTPS listener is added. Both the certificate content and private key are required.
        -   **CA certificate**: issued by a certificate authority \(CA\) and used to verify the certificate issuer. If HTTPS mutual authentication is required, HTTPS connections can be established only when the client provides a certificate issued by a specific CA.

    -   **Domain Name**: If the certificate is used for SNI, a domain name must be specified.
    -   **Certificate Content**: The content must be in PEM format.

        Click  **Upload**  and select the certificate to be uploaded. Ensure that your browser is of the latest version.

    -   **Private Key**

        Click  **Upload**  and select the private key to be uploaded. Ensure that your browser is of the latest version.

        The private key must be an unencrypted one, and its format is as follows:

        ```
        -----BEGIN PRIVATE KEY-----
        [key]
        -----END PRIVATE KEY-----
        ```

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If a certificate chain is used, you need to configure the content and private keys of all certificates in sequence, starting from the sub-certificate, and ensure that the certificate content is configured in the same sequence as private keys. For example, if you have three certificates: sub-certificate, intermediate certificate, and root certificate, the first one to be configured is the sub-certificate, followed by the intermediate certificate, and the last one is the root certificate.  

    -   **Domain Name**

        If the created certificate is used for SNI, you need to specify a domain name. Only one domain name can be specified for each certificate, and the domain name must be the same as that in the certificate.

    -   **Description**


1.  Click  **OK**.

## Delete a Certificate<a name="section8343547171830"></a>

Only certificates that are not in use can be deleted.

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0095109447.jpg)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  In the navigation pane, choose  **Certificates**.
5.  Locate the row that contains the target certificate and click  **Delete**  in the  **Operation**  column.
6.  In the  **Delete Certificate**  dialog box, click  **Yes**.

## Modify a Certificate<a name="section45960980171830"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0095109448.jpg)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  In the navigation pane, choose  **Certificates**.
5.  Locate the row that contains the target certificate and click  **Modify**  in the  **Operation**  column.
6.  In the  **Modify Certificate**  dialog box, modify the certificate information.
7.  Click  **OK**.

## Bind a Certificate<a name="section49683221908"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0162304296.jpg)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Under  **Listeners**, click  **Add Listener**.
6.  In the  **Add Listener**  dialog box, configure the parameters. When  **Frontend Protocol**  is set to  **HTTPS**, a server certificate must be bound to the listener.
7.  Click  **OK**.

