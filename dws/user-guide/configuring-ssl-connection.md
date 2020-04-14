# Configuring SSL Connection<a name="dws_01_0076"></a>

DWS supports connections in SSL authentication mode so that data transmitted between the DWS client and the database can be encrypted. The SSL connection mode delivers higher security than the common mode. By default, the SSL function is enabled in a cluster to allow SSL or non-SSL connections from the client. To ensure security, you are advised to enable SSL connection. If you want to use SSL connection forcibly, enable  **Require SSL Connection**  for the cluster.

On the  **Security Settings**  page of the cluster, you can enable or disable  **Require SSL Connection**.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   After you have changed the security setting parameters and the changes take effect, the cluster may be restarted, which makes the cluster unavailable temporarily.  
>-   To modify the cluster's security configuration, ensure that the following conditions are met:  
>    -   The  **Cluster Status**  is  **Available**  or  **Low performance**.  
>    -   The  **Task Information**  cannot be  **Creating snapshot**,  **Scaling out**,  **Configuring**, or  **Restarting**.  

The following parts are included in this section:

-   [Configuring SSL Connection](#section478703071283)
-   [Combinations of SSL Connection Parameters on the Client and Server](#section1916311515557)

## Configuring SSL Connection<a name="section478703071283"></a>

1.  Log in to the management console at  [https://console.otc.t-systems.com/dws/](https://console.otc.t-systems.com/dws/).
2.  In the navigation tree on the left, click  **Cluster Management**.
3.  In the cluster list, click the name of a cluster. On the page that is displayed, click  **Security Settings**.

    By default,  **Configuration Status**  is  **Synchronized**, which indicates that the latest database result is displayed.

4.  In the  **SSL Connection**  area, click  **Require SSL Connection**  switch to enable the function \(recommended\).

    ![](figures/icon-button2.png): indicates that the server forcibly requires SSL connection.

    ![](figures/icon_dws_off.jpg): indicates that the server does not forcibly require SSL connection. This function is disabled by default.

    **Figure  1**  View of SSL connection<a name="fig624582833812"></a>  
    ![](figures/view-of-ssl-connection.png "view-of-ssl-connection")

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   If the gsql client or ODBC driver provided by DWS is used, DWS supports the TLSv1.2 SSL protocol.  
    >-   If the JDBC driver provided by DWS is used, DWS supports SSL protocols, such as SSLv3, TLSv1, TLSv1.1, and TLSv1.2. The SSL protocol used between the client and the database depends on the Java Development Kit \(JDK\) version used by the client. Generally, JDK supports multiple SSL protocols.  

5.  Click  **Apply**.

    The system automatically saves the SSL connection settings. On the  **Security Settings**  page,  **Configuration Status**  is  **Applying**. After  **Configuration Status**  changes to  **Synchronized**, the settings have been saved and taken effect.


## Combinations of SSL Connection Parameters on the Client and Server<a name="section1916311515557"></a>

Whether the client uses the SSL encryption connection mode and whether to verify the server certificate depend on client parameter  **sslmode**  and server \(cluster\) parameters  **ssl**  and  **require\_ssl**. The parameters are described as follows:

-   **ssl \(Server\)**

    The  **ssl**  parameter indicates whether to enable the SSL function.  **on**  indicates that the function is enabled, and  **off**  indicates that the function is disabled. 

    -   The default value is  **on**  for clusters whose version is later than 1.3.1 \(including 1.3.1\), and you cannot set this parameter on the DWS management console.
    -   For clusters whose version is earlier than 1.3.1, the default value is  **on**  \(enabled\). You can set this parameter in the  **SSL Connection**  area on the cluster's  **Security Settings**  page of the DWS management console. 

-   **require\_ssl \(Server\)**

    The  **require\_ssl**  parameter specifies whether the server forcibly requires SSL connection. This parameter is valid only when  **ssl**  is set to  **on**.  **on**: The server forcibly requires SSL connection.  **off**: The server does not require SSL connection.

    -   The default value is  **off**  \(disabled\) for clusters whose version is later than 1.3.1 \(including 1.3.1. You can set the  **require\_ssl**  parameter in the  **Require SSL Connection**  area of the cluster's  **Security Settings**  page on the DWS management console.
    -   For clusters whose version is earlier than 1.3.1, the default value is  **off**, and you cannot set this parameter on the DWS management console.

-   **sslmode \(Client\)**

    You can set this parameter in the SQL client tool.

    -   In the gsql command line client, this parameter is the  **PGSSLMODE**  parameter.
    -   On the Data Studio client, this parameter is the  **SSL Mode**  parameter.


The combinations of client parameter  **sslmode**  and server parameters  **ssl**  and  **require\_ssl**  are as follows:

**Table  1**  Combinations of SSL connection parameters on the client and server

<a name="table15451139114317"></a>
<table><thead align="left"><tr id="r307948f04d9a4095912f140f8cd1bd5b"><th class="cellrowborder" valign="top" width="10.66%" id="mcps1.2.5.1.1"><p id="a59eb9cfe2b74465589c4201cb2786f13"><a name="a59eb9cfe2b74465589c4201cb2786f13"></a><a name="a59eb9cfe2b74465589c4201cb2786f13"></a><strong id="b196519391394"><a name="b196519391394"></a><a name="b196519391394"></a>ssl (Server)</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.85%" id="mcps1.2.5.1.2"><p id="a1ff465f2151a46b4a705e6d0af826667"><a name="a1ff465f2151a46b4a705e6d0af826667"></a><a name="a1ff465f2151a46b4a705e6d0af826667"></a><strong id="b129116421913"><a name="b129116421913"></a><a name="b129116421913"></a>sslmode (Client)</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.119999999999997%" id="mcps1.2.5.1.3"><p id="a21e2b71e6d3442f399ecbaa910c403e3"><a name="a21e2b71e6d3442f399ecbaa910c403e3"></a><a name="a21e2b71e6d3442f399ecbaa910c403e3"></a><strong id="b71667441493"><a name="b71667441493"></a><a name="b71667441493"></a>require_ssl (Server)</strong></p>
</th>
<th class="cellrowborder" valign="top" width="57.37%" id="mcps1.2.5.1.4"><p id="a2ec28134f0b640ef9b2e5e7278143263"><a name="a2ec28134f0b640ef9b2e5e7278143263"></a><a name="a2ec28134f0b640ef9b2e5e7278143263"></a><strong id="b8854114510917"><a name="b8854114510917"></a><a name="b8854114510917"></a>Result</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="ra2a059fd895446cbbf6341c28fa72933"><td class="cellrowborder" rowspan="10" valign="top" width="10.66%" headers="mcps1.2.5.1.1 "><p id="a6c5db1dc8ac64f5dab62873acc90feb8"><a name="a6c5db1dc8ac64f5dab62873acc90feb8"></a><a name="a6c5db1dc8ac64f5dab62873acc90feb8"></a>on</p>
</td>
<td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.2.5.1.2 "><p id="a04e8c409415a4dc59a286912d3d86980"><a name="a04e8c409415a4dc59a286912d3d86980"></a><a name="a04e8c409415a4dc59a286912d3d86980"></a>disable</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.5.1.3 "><p id="a2c94bb8985b7408cab4effcb6b2d25bb"><a name="a2c94bb8985b7408cab4effcb6b2d25bb"></a><a name="a2c94bb8985b7408cab4effcb6b2d25bb"></a>on</p>
</td>
<td class="cellrowborder" valign="top" width="57.37%" headers="mcps1.2.5.1.4 "><p id="a4c51a6b2f8d94d78a3cf149c57ef2ded"><a name="a4c51a6b2f8d94d78a3cf149c57ef2ded"></a><a name="a4c51a6b2f8d94d78a3cf149c57ef2ded"></a>The server requires SSL, but the client disables SSL for the connection. As a result, the connection cannot be set up.</p>
</td>
</tr>
<tr id="rd88db7a758da49a1a619f9af8c4ac342"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="a3e1c1504c9a84a9d95153ac05ac3620a"><a name="a3e1c1504c9a84a9d95153ac05ac3620a"></a><a name="a3e1c1504c9a84a9d95153ac05ac3620a"></a>disable</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="a2ef6d1cf42064013a1b13f38ebb3d3c5"><a name="a2ef6d1cf42064013a1b13f38ebb3d3c5"></a><a name="a2ef6d1cf42064013a1b13f38ebb3d3c5"></a>off</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="a9eb2e113c08548949b6f121b9f1aa12f"><a name="a9eb2e113c08548949b6f121b9f1aa12f"></a><a name="a9eb2e113c08548949b6f121b9f1aa12f"></a>The connection is not encrypted.</p>
</td>
</tr>
<tr id="r37bc02ba9309434ab46ba793f4397acd"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="ab963f8e14feb4d9ca2690ed6e2e381fd"><a name="ab963f8e14feb4d9ca2690ed6e2e381fd"></a><a name="ab963f8e14feb4d9ca2690ed6e2e381fd"></a>allow</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="af9a02ab3119749868eafe31efc459483"><a name="af9a02ab3119749868eafe31efc459483"></a><a name="af9a02ab3119749868eafe31efc459483"></a>on</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="ac03e3fa81fa544428f6bcd938b31651b"><a name="ac03e3fa81fa544428f6bcd938b31651b"></a><a name="ac03e3fa81fa544428f6bcd938b31651b"></a>The connection is encrypted.</p>
</td>
</tr>
<tr id="ra108bd4d83b64da18d807c7efb87fa7b"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="a33586b8a8e6c42448da18a5023d62ddd"><a name="a33586b8a8e6c42448da18a5023d62ddd"></a><a name="a33586b8a8e6c42448da18a5023d62ddd"></a>allow</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="a0c58503c57304ebd895e2df63dc37e2a"><a name="a0c58503c57304ebd895e2df63dc37e2a"></a><a name="a0c58503c57304ebd895e2df63dc37e2a"></a>off</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="ae0b4a3e232ec47c59f6320f77e8a0b56"><a name="ae0b4a3e232ec47c59f6320f77e8a0b56"></a><a name="ae0b4a3e232ec47c59f6320f77e8a0b56"></a>The connection is not encrypted.</p>
</td>
</tr>
<tr id="rc29ce24722724644b86325712833073f"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="a5d16271f72a048e48a8c54bb786ffec8"><a name="a5d16271f72a048e48a8c54bb786ffec8"></a><a name="a5d16271f72a048e48a8c54bb786ffec8"></a>prefer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="ada5004daab5f499aac8eea85fe4be30c"><a name="ada5004daab5f499aac8eea85fe4be30c"></a><a name="ada5004daab5f499aac8eea85fe4be30c"></a>on</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="a29b2a0fb86d54e5590ba54ca758b0d46"><a name="a29b2a0fb86d54e5590ba54ca758b0d46"></a><a name="a29b2a0fb86d54e5590ba54ca758b0d46"></a>The connection is encrypted.</p>
</td>
</tr>
<tr id="r3a03f8b223ca41289e0a5d07e031b82f"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="ae19a34e3627f4fcf83ae6cf1fe711ccb"><a name="ae19a34e3627f4fcf83ae6cf1fe711ccb"></a><a name="ae19a34e3627f4fcf83ae6cf1fe711ccb"></a>prefer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="a4790cd7b269947fdb8be97d11ffaefb3"><a name="a4790cd7b269947fdb8be97d11ffaefb3"></a><a name="a4790cd7b269947fdb8be97d11ffaefb3"></a>off</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="a94b84ef39f6245209a3c87a973ace1f6"><a name="a94b84ef39f6245209a3c87a973ace1f6"></a><a name="a94b84ef39f6245209a3c87a973ace1f6"></a>The connection is encrypted.</p>
</td>
</tr>
<tr id="r8ec9b59dbb414995a79d0009e5c8886e"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="a25dba740d54e4f91ab06685a0004f343"><a name="a25dba740d54e4f91ab06685a0004f343"></a><a name="a25dba740d54e4f91ab06685a0004f343"></a>require</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="a7024e9a0fd3f408c8625f3cd9c04c4f7"><a name="a7024e9a0fd3f408c8625f3cd9c04c4f7"></a><a name="a7024e9a0fd3f408c8625f3cd9c04c4f7"></a>on</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="acea2ce32efa24eaf9180c039c2f26cdf"><a name="acea2ce32efa24eaf9180c039c2f26cdf"></a><a name="acea2ce32efa24eaf9180c039c2f26cdf"></a>The connection is encrypted.</p>
</td>
</tr>
<tr id="re0fd51ed19db438085e586b18858b075"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="a01f46f1b51fc4b9e88a601fe33777eed"><a name="a01f46f1b51fc4b9e88a601fe33777eed"></a><a name="a01f46f1b51fc4b9e88a601fe33777eed"></a>require</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="a66dd731765ec4acdb9fc0b48493e2cc7"><a name="a66dd731765ec4acdb9fc0b48493e2cc7"></a><a name="a66dd731765ec4acdb9fc0b48493e2cc7"></a>off</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="aa81d5ff4e65f4aa19f234e467067822e"><a name="aa81d5ff4e65f4aa19f234e467067822e"></a><a name="aa81d5ff4e65f4aa19f234e467067822e"></a>The connection is encrypted.</p>
</td>
</tr>
<tr id="r2bf644086d8341c7924be5f85b475119"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="a3e962e78f1cb4a6b8989359ad8f846d6"><a name="a3e962e78f1cb4a6b8989359ad8f846d6"></a><a name="a3e962e78f1cb4a6b8989359ad8f846d6"></a>verify-ca</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="a86fa72da3a8f4e459f9382ec628272e2"><a name="a86fa72da3a8f4e459f9382ec628272e2"></a><a name="a86fa72da3a8f4e459f9382ec628272e2"></a>on</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="a788a5385706543af9c1e7cd59b308223"><a name="a788a5385706543af9c1e7cd59b308223"></a><a name="a788a5385706543af9c1e7cd59b308223"></a>The connection is encrypted and the server certificate is verified.</p>
</td>
</tr>
<tr id="r6df066f6e4f446cbabdc4c095dd5fa45"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="a6790a2f64b454000909f3ea0459d156a"><a name="a6790a2f64b454000909f3ea0459d156a"></a><a name="a6790a2f64b454000909f3ea0459d156a"></a>verify-ca</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="a55fb7e3f8bd84c3cbe7b691df3311141"><a name="a55fb7e3f8bd84c3cbe7b691df3311141"></a><a name="a55fb7e3f8bd84c3cbe7b691df3311141"></a>off</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="a46e5ea9a74174a3b9407363f04903ee1"><a name="a46e5ea9a74174a3b9407363f04903ee1"></a><a name="a46e5ea9a74174a3b9407363f04903ee1"></a>The connection is encrypted and the server certificate is verified.</p>
</td>
</tr>
<tr id="r11788da03f0d46d6ac63666dba1c9bc0"><td class="cellrowborder" rowspan="10" valign="top" width="10.66%" headers="mcps1.2.5.1.1 "><p id="aa4743b987f6c43599183bf3656378590"><a name="aa4743b987f6c43599183bf3656378590"></a><a name="aa4743b987f6c43599183bf3656378590"></a>off</p>
</td>
<td class="cellrowborder" valign="top" width="14.85%" headers="mcps1.2.5.1.2 "><p id="a01c12124b9af4aa4aed302840ddb1218"><a name="a01c12124b9af4aa4aed302840ddb1218"></a><a name="a01c12124b9af4aa4aed302840ddb1218"></a>disable</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.5.1.3 "><p id="a2a31a310793041c7a31fe151496c3011"><a name="a2a31a310793041c7a31fe151496c3011"></a><a name="a2a31a310793041c7a31fe151496c3011"></a>on</p>
</td>
<td class="cellrowborder" valign="top" width="57.37%" headers="mcps1.2.5.1.4 "><p id="a2bdb44f2eb48491b9724aaa83888e97a"><a name="a2bdb44f2eb48491b9724aaa83888e97a"></a><a name="a2bdb44f2eb48491b9724aaa83888e97a"></a>The connection is not encrypted.</p>
</td>
</tr>
<tr id="rb726132290824207b3c1d76a29537aaa"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="a4e719b97f3c64c6d9cf93b5bcef16a08"><a name="a4e719b97f3c64c6d9cf93b5bcef16a08"></a><a name="a4e719b97f3c64c6d9cf93b5bcef16a08"></a>disable</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="ad79674378a4a4eff8c33550ba920a4a1"><a name="ad79674378a4a4eff8c33550ba920a4a1"></a><a name="ad79674378a4a4eff8c33550ba920a4a1"></a>off</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="a333ff5e881ca42ccb73e9ce93fc91a9f"><a name="a333ff5e881ca42ccb73e9ce93fc91a9f"></a><a name="a333ff5e881ca42ccb73e9ce93fc91a9f"></a>The connection is not encrypted.</p>
</td>
</tr>
<tr id="r25e678e3d40d40a98f2b0c715c404b80"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="ab1cbef6de7e548c1a94254849a888f24"><a name="ab1cbef6de7e548c1a94254849a888f24"></a><a name="ab1cbef6de7e548c1a94254849a888f24"></a>allow</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="a7925dc9cced2492ba47d8816e9931ca9"><a name="a7925dc9cced2492ba47d8816e9931ca9"></a><a name="a7925dc9cced2492ba47d8816e9931ca9"></a>on</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="acd981c348c91449aa993c7b6ce3fb48b"><a name="acd981c348c91449aa993c7b6ce3fb48b"></a><a name="acd981c348c91449aa993c7b6ce3fb48b"></a>The connection is not encrypted.</p>
</td>
</tr>
<tr id="r15b0bce70c9d4ce59e6b02f444564f80"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="a6df7df4ee02244c38b4abc9ea80d8045"><a name="a6df7df4ee02244c38b4abc9ea80d8045"></a><a name="a6df7df4ee02244c38b4abc9ea80d8045"></a>allow</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="af8f93f3d5d4c4aa09a3050570e7257b0"><a name="af8f93f3d5d4c4aa09a3050570e7257b0"></a><a name="af8f93f3d5d4c4aa09a3050570e7257b0"></a>off</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="a5b46592dd85547ffa37dc596e8ca73b3"><a name="a5b46592dd85547ffa37dc596e8ca73b3"></a><a name="a5b46592dd85547ffa37dc596e8ca73b3"></a>The connection is not encrypted.</p>
</td>
</tr>
<tr id="rf856fcee2384400e8369f6d5b3f29354"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="a413b432138684c908d690a07787a5b30"><a name="a413b432138684c908d690a07787a5b30"></a><a name="a413b432138684c908d690a07787a5b30"></a>prefer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="a68ff17a105ea483ba651e118419773b9"><a name="a68ff17a105ea483ba651e118419773b9"></a><a name="a68ff17a105ea483ba651e118419773b9"></a>on</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="a734b295419b340e3af221fa6025fd9d1"><a name="a734b295419b340e3af221fa6025fd9d1"></a><a name="a734b295419b340e3af221fa6025fd9d1"></a>The connection is not encrypted.</p>
</td>
</tr>
<tr id="rfb4cf0dcda734b9ea8c4fd96c179f6e0"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="a0268e37b3e78499b826ce5a70f1b7b2d"><a name="a0268e37b3e78499b826ce5a70f1b7b2d"></a><a name="a0268e37b3e78499b826ce5a70f1b7b2d"></a>prefer</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="a794849ed15f64e618a3cf9bd6dc7cb3e"><a name="a794849ed15f64e618a3cf9bd6dc7cb3e"></a><a name="a794849ed15f64e618a3cf9bd6dc7cb3e"></a>off</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="af205c8628e8d4cdd8baabbf8ee53a7b7"><a name="af205c8628e8d4cdd8baabbf8ee53a7b7"></a><a name="af205c8628e8d4cdd8baabbf8ee53a7b7"></a>The connection is not encrypted.</p>
</td>
</tr>
<tr id="r714c483d796a486e8a3a618252e753b8"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="a7eb91819744b4cb38e3816f8fabd202f"><a name="a7eb91819744b4cb38e3816f8fabd202f"></a><a name="a7eb91819744b4cb38e3816f8fabd202f"></a>require</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="afa14b98251924375add8b152330f250f"><a name="afa14b98251924375add8b152330f250f"></a><a name="afa14b98251924375add8b152330f250f"></a>on</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="a6bc3403370d646cbb207191fcf6b4cde"><a name="a6bc3403370d646cbb207191fcf6b4cde"></a><a name="a6bc3403370d646cbb207191fcf6b4cde"></a>The client requires SSL, but SSL is disabled on the server. Therefore, the connection cannot be set up.</p>
</td>
</tr>
<tr id="rd33c90398d374e77865f99ddfdcd1517"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="a419be5cdb1b347cd9a707ac82c54a24b"><a name="a419be5cdb1b347cd9a707ac82c54a24b"></a><a name="a419be5cdb1b347cd9a707ac82c54a24b"></a>require</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="a53eff5bab0b74ecd9debde6018f1fae9"><a name="a53eff5bab0b74ecd9debde6018f1fae9"></a><a name="a53eff5bab0b74ecd9debde6018f1fae9"></a>off</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="a7fdde1b7073b479887ff91d365713e19"><a name="a7fdde1b7073b479887ff91d365713e19"></a><a name="a7fdde1b7073b479887ff91d365713e19"></a>The client requires SSL, but SSL is disabled on the server. Therefore, the connection cannot be set up.</p>
</td>
</tr>
<tr id="rcb3576ba1dd940c5870ea8751a7e16fb"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="aacc9f77ece6641dc8f85680c28d6cea1"><a name="aacc9f77ece6641dc8f85680c28d6cea1"></a><a name="aacc9f77ece6641dc8f85680c28d6cea1"></a>verify-ca</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="a802b5b2039ec45f0931480747b513b18"><a name="a802b5b2039ec45f0931480747b513b18"></a><a name="a802b5b2039ec45f0931480747b513b18"></a>on</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="a7ac23bcd08ee4c4ea1b3ed4a31b5abf9"><a name="a7ac23bcd08ee4c4ea1b3ed4a31b5abf9"></a><a name="a7ac23bcd08ee4c4ea1b3ed4a31b5abf9"></a>The client requires SSL, but SSL is disabled on the server. Therefore, the connection cannot be set up.</p>
</td>
</tr>
<tr id="r72609ade5c7a4ed5bfea1caa193afffa"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="a19612c3909eb4c14a1cff39bc19cda11"><a name="a19612c3909eb4c14a1cff39bc19cda11"></a><a name="a19612c3909eb4c14a1cff39bc19cda11"></a>verify-ca</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="aefd4050c11cb4a53839e24f8fdb9646c"><a name="aefd4050c11cb4a53839e24f8fdb9646c"></a><a name="aefd4050c11cb4a53839e24f8fdb9646c"></a>off</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="a1b024c996422424ca324c7adb28b1343"><a name="a1b024c996422424ca324c7adb28b1343"></a><a name="a1b024c996422424ca324c7adb28b1343"></a>The client requires SSL, but SSL is disabled on the server. Therefore, the connection cannot be set up.</p>
</td>
</tr>
</tbody>
</table>

