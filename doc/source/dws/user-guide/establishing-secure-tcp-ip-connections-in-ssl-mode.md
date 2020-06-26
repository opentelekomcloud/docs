# Establishing Secure TCP/IP Connections in SSL Mode<a name="dws_01_0038"></a>

If the client or JDBC/ODBC driver needs to use SSL connection, you must configure related SSL connection parameters in the client or application code. The DWS management console provides the SSL certificate required by the client. The SSL certificate contains the default certificate, private key, root certificate, and private key password encryption file required by the client. Download the SSL certificate to the host where the client resides and specify the path of the certificate on the client.

>![](/images/icon-note.gif) **NOTE:**   
>Using the default certificate may pose security risks. To improve system security, you are advised to periodically change the certificate to prevent password cracking. If you need to replace the certificate, contact the customer service personnel.  

For more information about SSL certificates, see section  [Downloading the SSL Certificate File](downloading-the-ssl-certificate-file.md). The following parts are included in this section:

-   [Configuring Digital Certificate Parameters Related to SSL Authentication on the gsql Client](#s7b66e0954a7a4e11a25e29b79e46fd0f)
-   [SSL Authentication Modes and Client Parameters](#sde292a534d1b4609a5b09e9b0e8789cc)

## Configuring Digital Certificate Parameters Related to SSL Authentication on the gsql Client<a name="s7b66e0954a7a4e11a25e29b79e46fd0f"></a>

After a data warehouse cluster is deployed, the SSL authentication mode is enabled by default. The server certificate, private key, and root certificate have been configured by default. You need to configure the client parameters.

1.  Log in to the DWS management console, download the SSL certificate, and upload it to the host where the gsql client is installed.
    1.  Download the SSL certificate. For details, see section  [Downloading the SSL Certificate File](downloading-the-ssl-certificate-file.md).
    2.  Use WinSCP to upload SSL certificate  **dws\_ssl\_cert.tar.gz**  to a directory on the client host, for example,  **/home/dbadmin/dws\_ssl/**.
    3.  Use PuTTY to remotely log in to the host.
    4.  Run the following commands to navigate to the directory where the SSL certificate is stored and decompress the SSL certificate:

        **cd /home/dbadmin/dws\_ssl/**

        **tar -xvf dws\_ssl\_cert.tar.gz**

2.  Configure digital certificate parameters related to SSL authentication on the host of the gsql client.

    There are two SSL authentication modes: bidirectional authentication and unidirectional authentication. Different authentication modes require different client environment variables. For details, see  [SSL Authentication Modes and Client Parameters](#sde292a534d1b4609a5b09e9b0e8789cc).

    The following parameters must be configured for bidirectional authentication:

    ```
    export PGSSLCERT="/home/dbadmin/dws_ssl/sslcert/client.crt"
    export PGSSLKEY="/home/dbadmin/dws_ssl/sslcert/client.key"
    export PGSSLMODE="verify-ca"
    export PGSSLROOTCERT="/home/dbadmin/dws_ssl/sslcert/cacert.pem"
    ```

    The following parameters must be configured for unidirectional authentication:

    ```
    export PGSSLMODE="verify-ca"
    export PGSSLROOTCERT="/home/dbadmin/dws_ssl/sslcert/cacert.pem"
    ```

    >![](/images/icon-notice.gif) **NOTICE:**   
    >-   You are advised to use bidirectional authentication for security purposes.  
    >-   The environment variables configured for a client must contain the absolute file paths.  

3.  Change the client private key permissions.

    The permissions on the client's root certificate, private key, certificate, and encrypted private key file must be  **600**. If the permissions do not meet the requirement, the client cannot connect to the cluster in SSL mode.

    ```
    chmod 600 client.key
    chmod 600 client.crt
    chmod 600 client.key.cipher
    chmod 600 client.key.rand
    chmod 600 cacert.pem
    ```


## SSL Authentication Modes and Client Parameters<a name="sde292a534d1b4609a5b09e9b0e8789cc"></a>

SSL authentication has two authentication modes: bidirectional certification and unidirectional authentication. Table  [Table 1](#table267519441727)  shows the differences between these two modes. You are advised to use bidirectional authentication for security purposes.

**Table  1**  Authentication modes

<a name="table267519441727"></a>
<table><thead align="left"><tr id="row1569712441123"><th class="cellrowborder" valign="top" width="14.321432143214322%" id="mcps1.2.5.1.1"><p id="p6706134413210"><a name="p6706134413210"></a><a name="p6706134413210"></a><strong id="b187421811143819"><a name="b187421811143819"></a><a name="b187421811143819"></a>Authentication Mode</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.912691269126913%" id="mcps1.2.5.1.2"><p id="p187063441212"><a name="p187063441212"></a><a name="p187063441212"></a><strong id="b84235270619454"><a name="b84235270619454"></a><a name="b84235270619454"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.73337333733373%" id="mcps1.2.5.1.3"><p id="p17149441227"><a name="p17149441227"></a><a name="p17149441227"></a><strong id="b842352706155354"><a name="b842352706155354"></a><a name="b842352706155354"></a>Environment Variables Configured on a Client</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.032503250325032%" id="mcps1.2.5.1.4"><p id="p371410441425"><a name="p371410441425"></a><a name="p371410441425"></a><strong id="b84235270615542"><a name="b84235270615542"></a><a name="b84235270615542"></a>Maintenance</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row167211244327"><td class="cellrowborder" valign="top" width="14.321432143214322%" headers="mcps1.2.5.1.1 "><p id="p20721184419215"><a name="p20721184419215"></a><a name="p20721184419215"></a>Bidirectional certification (recommended)</p>
</td>
<td class="cellrowborder" valign="top" width="26.912691269126913%" headers="mcps1.2.5.1.2 "><p id="p1772914441226"><a name="p1772914441226"></a><a name="p1772914441226"></a>The client verifies the server's certificate and the server verifies the client's certificate. Connection can be set up after the verifications are successful.</p>
</td>
<td class="cellrowborder" valign="top" width="33.73337333733373%" headers="mcps1.2.5.1.3 "><p id="p872910441723"><a name="p872910441723"></a><a name="p872910441723"></a>Set the following environment variables:</p>
<a name="ul2072910443216"></a><a name="ul2072910443216"></a><ul id="ul2072910443216"><li>PGSSLCERT</li><li>PGSSLKEY</li><li>PGSSLROOTCERT</li><li>PGSSLMODE</li></ul>
</td>
<td class="cellrowborder" valign="top" width="25.032503250325032%" headers="mcps1.2.5.1.4 "><p id="p1575364414211"><a name="p1575364414211"></a><a name="p1575364414211"></a>This authentication mode is applicable to scenarios that require high data security. When using this mode, you are advised to set the <strong id="b163331714105315"><a name="b163331714105315"></a><a name="b163331714105315"></a>PGSSLMODE</strong> client variable to <strong id="b842352706161133"><a name="b842352706161133"></a><a name="b842352706161133"></a>verify-ca</strong> for network data security purposes.</p>
</td>
</tr>
<tr id="row1475394418216"><td class="cellrowborder" valign="top" width="14.321432143214322%" headers="mcps1.2.5.1.1 "><p id="p67533441527"><a name="p67533441527"></a><a name="p67533441527"></a>Unidirectional authentication</p>
</td>
<td class="cellrowborder" valign="top" width="26.912691269126913%" headers="mcps1.2.5.1.2 "><p id="p27601449217"><a name="p27601449217"></a><a name="p27601449217"></a>The client verifies the server's certificate, whereas the server does not verify the client's certificate. The server loads the certificate information and sends it to the client. The client verifies the server's certificate according to the root certificate.</p>
</td>
<td class="cellrowborder" valign="top" width="33.73337333733373%" headers="mcps1.2.5.1.3 "><p id="p976014441621"><a name="p976014441621"></a><a name="p976014441621"></a>Set the following environment variables:</p>
<a name="ul117605446218"></a><a name="ul117605446218"></a><ul id="ul117605446218"><li>PGSSLROOTCERT</li><li>PGSSLMODE</li></ul>
</td>
<td class="cellrowborder" valign="top" width="25.032503250325032%" headers="mcps1.2.5.1.4 "><p id="p8776154411212"><a name="p8776154411212"></a><a name="p8776154411212"></a>To prevent TCP-based link spoofing, you are advised to use the SSL certificate authentication. In addition to configuring the client root certificate, you are advised to set the <strong id="b874116425412"><a name="b874116425412"></a><a name="b874116425412"></a>PGSSLMODE</strong> variable to <strong id="b842352706161335"><a name="b842352706161335"></a><a name="b842352706161335"></a>verify-ca</strong> on the client.</p>
</td>
</tr>
</tbody>
</table>

Configure environment variables related to SSL authentication on the client. For details, see  [Table 2](#ta677cb1a89d44c9194fccd705cd8536b).

>![](/images/icon-note.gif) **NOTE:**   
>An example path of environment variables is  _/home/dbadmin_/dws\_ssl/ \(for example\). Replace it with the actual path.  

**Table  2**  Client parameters

<a name="ta677cb1a89d44c9194fccd705cd8536b"></a>
<table><thead align="left"><tr id="r693a23e9f1fc401991d0b5b1935d5f14"><th class="cellrowborder" valign="top" width="13.059999999999999%" id="mcps1.2.4.1.1"><p id="ac997c35479554144b8b5b4cc42a0fe9b"><a name="ac997c35479554144b8b5b4cc42a0fe9b"></a><a name="ac997c35479554144b8b5b4cc42a0fe9b"></a><strong id="b84235270614338"><a name="b84235270614338"></a><a name="b84235270614338"></a>Environment Variable</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.5%" id="mcps1.2.4.1.2"><p id="a79ab5df6f7184f1ba1182cebe37aba1f"><a name="a79ab5df6f7184f1ba1182cebe37aba1f"></a><a name="a79ab5df6f7184f1ba1182cebe37aba1f"></a><strong id="b958814275910"><a name="b958814275910"></a><a name="b958814275910"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.44%" id="mcps1.2.4.1.3"><p id="add9a30ea89944b029b11267fce65560f"><a name="add9a30ea89944b029b11267fce65560f"></a><a name="add9a30ea89944b029b11267fce65560f"></a><strong id="b1780718312591"><a name="b1780718312591"></a><a name="b1780718312591"></a>Value Range</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r0fdff6a8c4604b0085fde42ee812f19c"><td class="cellrowborder" valign="top" width="13.059999999999999%" headers="mcps1.2.4.1.1 "><p id="a549c19c7102543fcb90a28218883abd1"><a name="a549c19c7102543fcb90a28218883abd1"></a><a name="a549c19c7102543fcb90a28218883abd1"></a>PGSSLCERT</p>
</td>
<td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.4.1.2 "><p id="ace4f0b4e7ea141a8bc493cb37db2787b"><a name="ace4f0b4e7ea141a8bc493cb37db2787b"></a><a name="ace4f0b4e7ea141a8bc493cb37db2787b"></a>Specifies the certificate files for a client, including the public key. Certificates prove the legal identity of the client and the public key is sent to the remote end for data encryption.</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.3 "><div class="p" id="ab99a81f37e964f8989ec22d276a71524"><a name="ab99a81f37e964f8989ec22d276a71524"></a><a name="ab99a81f37e964f8989ec22d276a71524"></a>The absolute path of the files must be specified, for example:<pre class="screen" id="s73eed45436f247d3b0aa2793be2c3b2b"><a name="s73eed45436f247d3b0aa2793be2c3b2b"></a><a name="s73eed45436f247d3b0aa2793be2c3b2b"></a><strong id="aab10f26161af4f439885adfd437bcf79"><a name="aab10f26161af4f439885adfd437bcf79"></a><a name="aab10f26161af4f439885adfd437bcf79"></a>export PGSSLCERT='</strong><em id="ac2b9f5a488c54c508350a7c2cbf00f7f"><a name="ac2b9f5a488c54c508350a7c2cbf00f7f"></a><a name="ac2b9f5a488c54c508350a7c2cbf00f7f"></a>/home/dbadmin/dws_ssl/sslcert/client.crt</em><strong id="adf3392f15ef94523a2a2fbb67b831b2d"><a name="adf3392f15ef94523a2a2fbb67b831b2d"></a><a name="adf3392f15ef94523a2a2fbb67b831b2d"></a>'</strong></pre>
</div>
<p id="a4dd04f97cc2947578a4c772b5fc940bb"><a name="a4dd04f97cc2947578a4c772b5fc940bb"></a><a name="a4dd04f97cc2947578a4c772b5fc940bb"></a>Default value: null</p>
</td>
</tr>
<tr id="r084c31e8317f465eb874eb0e9e86d406"><td class="cellrowborder" valign="top" width="13.059999999999999%" headers="mcps1.2.4.1.1 "><p id="a86422608eaa54780863a677d3b1278a6"><a name="a86422608eaa54780863a677d3b1278a6"></a><a name="a86422608eaa54780863a677d3b1278a6"></a>PGSSLKEY</p>
</td>
<td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.4.1.2 "><p id="aa6f92387a9ee470fb8b213933602f2be"><a name="aa6f92387a9ee470fb8b213933602f2be"></a><a name="aa6f92387a9ee470fb8b213933602f2be"></a>Specifies the private key file for the client to encrypt digital signatures and data encrypted using the public key.</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.3 "><div class="p" id="aaf81cd1e2e52407faa765c6dd1df3e54"><a name="aaf81cd1e2e52407faa765c6dd1df3e54"></a><a name="aaf81cd1e2e52407faa765c6dd1df3e54"></a>The absolute path of the files must be specified, for example:<pre class="screen" id="s2af627baf9884f3a80754b76e7867f04"><a name="s2af627baf9884f3a80754b76e7867f04"></a><a name="s2af627baf9884f3a80754b76e7867f04"></a><strong id="a83caad5e6c6443c2b155c77ad92328fe"><a name="a83caad5e6c6443c2b155c77ad92328fe"></a><a name="a83caad5e6c6443c2b155c77ad92328fe"></a>export PGSSLKEY='</strong><em id="abf0cdfee30e746948a2e666e76e4dbc3"><a name="abf0cdfee30e746948a2e666e76e4dbc3"></a><a name="abf0cdfee30e746948a2e666e76e4dbc3"></a>/home/dbadmin/dws_ssl/sslcert/client.key</em><strong id="ae4441b615cfe45099009689a65dc6a4c"><a name="ae4441b615cfe45099009689a65dc6a4c"></a><a name="ae4441b615cfe45099009689a65dc6a4c"></a>'</strong></pre>
</div>
<p id="acf9c37a97b7a41f8bce36c3b8f5f7ac9"><a name="acf9c37a97b7a41f8bce36c3b8f5f7ac9"></a><a name="acf9c37a97b7a41f8bce36c3b8f5f7ac9"></a>Default value: null</p>
</td>
</tr>
<tr id="r270600e0ed22419e9aa59b2594c7a7ad"><td class="cellrowborder" valign="top" width="13.059999999999999%" headers="mcps1.2.4.1.1 "><p id="a15d5ef3031cc45f598a6dedecec583d1"><a name="a15d5ef3031cc45f598a6dedecec583d1"></a><a name="a15d5ef3031cc45f598a6dedecec583d1"></a>PGSSLMODE</p>
</td>
<td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.4.1.2 "><p id="ad062e38ba4c74db8a03784118462553e"><a name="ad062e38ba4c74db8a03784118462553e"></a><a name="ad062e38ba4c74db8a03784118462553e"></a>Specifies whether to negotiate with the server about SSL connection and specifies the priority of the SSL connection.</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.3 "><p id="a5da623819f854148a127ed4be98b04ad"><a name="a5da623819f854148a127ed4be98b04ad"></a><a name="a5da623819f854148a127ed4be98b04ad"></a><strong id="b842352706161759"><a name="b842352706161759"></a><a name="b842352706161759"></a>Values and meanings</strong>:</p>
<a name="u7d09de5313a447fa82ea025f413a880e"></a><a name="u7d09de5313a447fa82ea025f413a880e"></a><ul id="u7d09de5313a447fa82ea025f413a880e"><li><strong id="b84235270616196"><a name="b84235270616196"></a><a name="b84235270616196"></a>disable</strong>: only tries to establish a non-SSL connection.</li><li><strong id="b842352706161935"><a name="b842352706161935"></a><a name="b842352706161935"></a>allow</strong>: tries to establish a non-SSL connection first, and then an SSL connection if the first attempt fails.</li><li><strong id="b842352706162016"><a name="b842352706162016"></a><a name="b842352706162016"></a>prefer</strong>: tries to establish an SSL connection first, and then a non-SSL connection if the first attempt fails.</li><li><strong id="b842352706162047"><a name="b842352706162047"></a><a name="b842352706162047"></a>require</strong>: only tries to establish an SSL connection. If there is a CA file, perform the verification according to the scenario in which the parameter is set to <strong id="b842352706162118"><a name="b842352706162118"></a><a name="b842352706162118"></a>verify-ca</strong>.</li><li><strong id="b842352706162135"><a name="b842352706162135"></a><a name="b842352706162135"></a>verify-ca</strong>: tries to establish an SSL connection and check whether the server certificate is issued by a trusted CA.</li><li><strong id="b922295117459"><a name="b922295117459"></a><a name="b922295117459"></a>verify-full</strong>: DWS does not support this mode.</li></ul>
<p id="ad52e2e8bcb744dcaad79751d4f7142c5"><a name="ad52e2e8bcb744dcaad79751d4f7142c5"></a><a name="ad52e2e8bcb744dcaad79751d4f7142c5"></a>Default value: <strong id="b842352706162329"><a name="b842352706162329"></a><a name="b842352706162329"></a>prefer</strong></p>
</td>
</tr>
<tr id="rb5dcab5059754d01a026b27f91b57b88"><td class="cellrowborder" valign="top" width="13.059999999999999%" headers="mcps1.2.4.1.1 "><p id="ab1d23d61a5144ae48c513eb4d6319bec"><a name="ab1d23d61a5144ae48c513eb4d6319bec"></a><a name="ab1d23d61a5144ae48c513eb4d6319bec"></a>PGSSLROOTCERT</p>
</td>
<td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.4.1.2 "><p id="ac5d471f990fd4c818ef1fe2a1361bc64"><a name="ac5d471f990fd4c818ef1fe2a1361bc64"></a><a name="ac5d471f990fd4c818ef1fe2a1361bc64"></a>Specifies the root certificate file for issuing client certificates. The root certificate is used to verify the server certificate.</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.3 "><div class="p" id="a6eca431ed7a7455386e439aee4700ddb"><a name="a6eca431ed7a7455386e439aee4700ddb"></a><a name="a6eca431ed7a7455386e439aee4700ddb"></a>The absolute path of the files must be specified, for example:<pre class="screen" id="s7a0e2350df624457a69bcc0f28731040"><a name="s7a0e2350df624457a69bcc0f28731040"></a><a name="s7a0e2350df624457a69bcc0f28731040"></a><strong id="a2631be659e414a04a31eab51b60bdae8"><a name="a2631be659e414a04a31eab51b60bdae8"></a><a name="a2631be659e414a04a31eab51b60bdae8"></a>export PGSSLROOTCERT='</strong><em id="a438271a226ca418a85b1b363be514719"><a name="a438271a226ca418a85b1b363be514719"></a><a name="a438271a226ca418a85b1b363be514719"></a>/home<em id="a81b9f79000bc4c8bbff2a206f35a5bc4"><a name="a81b9f79000bc4c8bbff2a206f35a5bc4"></a><a name="a81b9f79000bc4c8bbff2a206f35a5bc4"></a>/dbadmin</em>/dws_ssl/sslcert/certca.pem</em><strong id="a74b5a8a4bdee4286b95da3f6ba3ef3a7"><a name="a74b5a8a4bdee4286b95da3f6ba3ef3a7"></a><a name="a74b5a8a4bdee4286b95da3f6ba3ef3a7"></a>'</strong></pre>
</div>
<p id="aac5dc0607a4f45f7a5c2f47f78352913"><a name="aac5dc0607a4f45f7a5c2f47f78352913"></a><a name="aac5dc0607a4f45f7a5c2f47f78352913"></a><strong id="a2ed4b99be61f4c1d9d2987d01803df49"><a name="a2ed4b99be61f4c1d9d2987d01803df49"></a><a name="a2ed4b99be61f4c1d9d2987d01803df49"></a>Default value</strong>: null</p>
</td>
</tr>
<tr id="r6a3daf2e70ed4aadab7bf9392364c073"><td class="cellrowborder" valign="top" width="13.059999999999999%" headers="mcps1.2.4.1.1 "><p id="a6e94fe35451d40a3931e169e99e131f1"><a name="a6e94fe35451d40a3931e169e99e131f1"></a><a name="a6e94fe35451d40a3931e169e99e131f1"></a>PGSSLCRL</p>
</td>
<td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.4.1.2 "><p id="a60486564cd984fa5b2aee6b98d099135"><a name="a60486564cd984fa5b2aee6b98d099135"></a><a name="a60486564cd984fa5b2aee6b98d099135"></a>Specifies the certificate revocation list file, which is used to check whether a server certificate is in the list. If yes, the certificate invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.3 "><div class="p" id="afdcd8445916d4a5aa45e3956e0600bf7"><a name="afdcd8445916d4a5aa45e3956e0600bf7"></a><a name="afdcd8445916d4a5aa45e3956e0600bf7"></a>The absolute path of the files must be specified, for example:<pre class="screen" id="sf92ee112422348ca96baccb84b6e00c1"><a name="sf92ee112422348ca96baccb84b6e00c1"></a><a name="sf92ee112422348ca96baccb84b6e00c1"></a><strong id="acf75a07b2dbd4767a045e24aa1da77c6"><a name="acf75a07b2dbd4767a045e24aa1da77c6"></a><a name="acf75a07b2dbd4767a045e24aa1da77c6"></a>export PGSSLCRL='</strong><em id="aa220958df01a4a6898d3d18ba1ad54f8"><a name="aa220958df01a4a6898d3d18ba1ad54f8"></a><a name="aa220958df01a4a6898d3d18ba1ad54f8"></a>/home/dbadmin/dws_ssl/sslcert/sslcrl-file.crl</em><strong id="aca3334defad540cb9f536727f298a9c9"><a name="aca3334defad540cb9f536727f298a9c9"></a><a name="aca3334defad540cb9f536727f298a9c9"></a>'</strong></pre>
</div>
<p id="ab3529867cb0741659875df6619c2de2d"><a name="ab3529867cb0741659875df6619c2de2d"></a><a name="ab3529867cb0741659875df6619c2de2d"></a><strong id="b285918328411"><a name="b285918328411"></a><a name="b285918328411"></a>Default value</strong>: null</p>
</td>
</tr>
</tbody>
</table>

