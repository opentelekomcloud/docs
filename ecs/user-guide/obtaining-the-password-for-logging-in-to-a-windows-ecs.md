# Obtaining the Password for Logging In to a Windows ECS<a name="EN-US_TOPIC_0031107266"></a>

## Scenarios<a name="section83915017466"></a>

Password authentication is required to log in to a Windows ECS. Therefore, you must use the key file used when you created the ECS to obtain the administrator password generated during ECS creation. The administrator user is  **Administrator**  or the user configured using Cloudbase-Init. This password is randomly generated, offering high security.

You can obtain the initial password for logging in to a Windows ECS through the management console or APIs. For details, see this section.

## Obtaining the Password Through the Management Console<a name="section38475220193847"></a>

1.  Obtain the private key file \(.pem file\) used when you created the ECS.
2.  Log in to the management console.
3.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
4.  Under  **Computing**, click  **Elastic Cloud Server**.
5.  On the  **Elastic Cloud Server**  page, select the target ECS.
6.  In the  **Operation**  column, click  **More**  and select  **Get Password**.
7.  Use either of the following methods to obtain the password through the key file:
    -   Click  **Select File**  and upload the key file from a local directory.
    -   Copy the key file content to the text field.

8.  Click  **Get Password**  to obtain a random password.

## Obtaining the Password Through APIs<a name="section1118765310423"></a>

1.  Obtain the private key file \(.pem file\) used when you created the ECS.
2.  Set up the API calling environment.
3.  Call APIs. For details, see "[API Usage Guidelines](https://docs.otc.t-systems.com/api/ecs/en-us_topic_0020805967.html)" in  _Elastic Cloud Server API Reference_.
4.  <a name="li5770130102852"></a>Obtain the ciphertext password.

    Call the password obtaining APIs to obtain the ciphertext password of the public key encrypted using RSA. The API URI is in the format "GET /v2/\{_tenant\_id_\}/servers/\{_server\_id_\}/os-server-password".

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For instructions about how to call the APIs, see "[Retrieving the Password for Logging In to a Windows ECS \(Native OpenStack API\)](https://docs.otc.t-systems.com/api/ecs/en-us_topic_0031176553.html)" in  _Elastic Cloud Server API Reference_.  

5.  Decrypt the ciphertext password.

    Use the private key file used when you created the ECS to decrypt the ciphertext password obtained in step  [4](#li5770130102852).

    1.  Run the following command to convert the ciphertext password format to ".key -nocrypt" using OpenSSL:

        **openssl pkcs8 -topk8 -inform PEM -outform DER -in rsa\_pem.key -out pkcs8\_der.key -nocrypt**

    2.  Invoke the Java class library  **org.bouncycastle.jce.provider.BouncyCastleProvider**  and use the key file to edit the code decryption ciphertext.


