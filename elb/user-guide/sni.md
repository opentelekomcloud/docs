# SNI<a name="EN-US_TOPIC_0161931359"></a>

## Scenarios<a name="section740719161315"></a>

If an application provides multiple domain names and each domain name uses a different certificate, you can enable SNI when adding an HTTPS listener. SNI is an extension to the TLS computer networking protocol and used to address the issue that one server can use only one certificate. SNI allows a server to present multiple certificates on the same IP address and TCP port number and hence allows multiple secure \(HTTPS\) websites \(or any other service over TLS\) to be served by the same IP address without requiring all those sites to use the same certificate. This feature allows the client to submit the domain name information while sending an SSL handshake request. Once receiving the request, the load balancer queries the right certificate based on the domain name and returns it to the client. If no certificate is found, the load balancer will return a default certificate.

Only enhanced load balancers support this function.

## Prerequisites<a name="section1392112210718"></a>

A certificate has been created. For details, see  [Creating a Certificate](creating-a-certificate.md).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Specify the domain name for the SNI certificate. Only one domain name can be specified for each certificate.  

## Procedure<a name="section61198541679"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0155076920.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.

1.  Locate the target load balancer and click its name.
2.  Click  **Listeners**.
    -   For an enhanced load balancer, locate the target listener. In the  **Basic Information**  area, click  **Configure**  on the right of  **SNI**.
    -   For a classic load balancer, click  **Listeners**, locate the target listener, and click  **Modify**  in the  **Operation**  column. In the  **Modify Listener**  dialog box, modify the parameters as needed.

3.  Enable SNI and select the SNI certificate to be used.
4.  Click  **OK**.

