# MRS Manager APIs<a name="EN-US_TOPIC_0220024719"></a>

MRS Manager APIs are provided for you to query basic information about MRS clusters and monitoring status, as well as start and stop services.

MRS Manager APIs can be accessed only by nodes in the same VPC as the cluster.

Clusters with Kerberos authentication disabled can directly call MRS Manager APIs in the same VPC for access. However, clusters with Kerberos authentication enabled must obtain authentication information before calling MRS Manager APIs.

An MRS Manager API request or response consists of the following six parts:

-   [Request URI](#en-us_topic_0125376273_section181761234145413)
-   [Request method](#en-us_topic_0125376273_section1437511065519)
-   [Request Header](#en-us_topic_0125376273_section559515309552)
-   [Request body](#en-us_topic_0125376273_section1692615591277)
-   [Response Header](#en-us_topic_0125376273_section33899391911)
-   [Response Body](#en-us_topic_0125376273_section186021620141012)

## Request URI<a name="en-us_topic_0125376273_section181761234145413"></a>

A request URI consists of the following parts:

**\{URI-scheme\} :// \{_Floating IP address of MRS Manager_\}**:\{_MRS Manager port_\}**  / \{resource-path\} ? \{query-string\}**

Although the request URI is included in the request header, most languages or frameworks require that it be transmitted separately from the request message. Therefore, the request URI is listed independently.

**Table  1**  Parameters in a URI

<a name="en-us_topic_0125376273_t85220210b39647cf81d6a6d96190b3f4"></a>
<table><thead align="left"><tr id="en-us_topic_0125376273_re65b80dc13aa433687077590004f8f31"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="en-us_topic_0125376273_abe4e57c399174c5fbff74084162f1e8b"><a name="en-us_topic_0125376273_abe4e57c399174c5fbff74084162f1e8b"></a><a name="en-us_topic_0125376273_abe4e57c399174c5fbff74084162f1e8b"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="en-us_topic_0125376273_ab9cddd12f37b40979f76eb56011032e5"><a name="en-us_topic_0125376273_ab9cddd12f37b40979f76eb56011032e5"></a><a name="en-us_topic_0125376273_ab9cddd12f37b40979f76eb56011032e5"></a><strong id="en-us_topic_0125376273_a8da163a420114c2ca0bd4b83fac21aa8"><a name="en-us_topic_0125376273_a8da163a420114c2ca0bd4b83fac21aa8"></a><a name="en-us_topic_0125376273_a8da163a420114c2ca0bd4b83fac21aa8"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376273_rda9d445b3100462aac07fcb6ec45b563"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0125376273_a54b4acac0c9740b1adf56b7af78d4db7"><a name="en-us_topic_0125376273_a54b4acac0c9740b1adf56b7af78d4db7"></a><a name="en-us_topic_0125376273_a54b4acac0c9740b1adf56b7af78d4db7"></a>URI-scheme</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0125376273_ad4b25d7b521c40868fe7852f95b100e8"><a name="en-us_topic_0125376273_ad4b25d7b521c40868fe7852f95b100e8"></a><a name="en-us_topic_0125376273_ad4b25d7b521c40868fe7852f95b100e8"></a>Specifies the protocol used for transmitting requests. HTTPS must be used in MRS APIs.</p>
</td>
</tr>
<tr id="en-us_topic_0125376273_ra308b02302184d10ad75a581194c47a2"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0125376273_p26272051435"><a name="en-us_topic_0125376273_p26272051435"></a><a name="en-us_topic_0125376273_p26272051435"></a><span>Floating IP address of MRS Manager</span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0125376273_p174328111143"><a name="en-us_topic_0125376273_p174328111143"></a><a name="en-us_topic_0125376273_p174328111143"></a>IP address for logging in to MRS Manager</p>
<p id="en-us_topic_0125376273_p1432911949"><a name="en-us_topic_0125376273_p1432911949"></a><a name="en-us_topic_0125376273_p1432911949"></a>For a security cluster that supports Kerberos authentication, you can view the floating IP address in <strong id="en-us_topic_0125376273_b339982264314"><a name="en-us_topic_0125376273_b339982264314"></a><a name="en-us_topic_0125376273_b339982264314"></a>Cluster Manager IP Address</strong> on the basic cluster information page.</p>
<p id="en-us_topic_0125376273_p34491546114210"><a name="en-us_topic_0125376273_p34491546114210"></a><a name="en-us_topic_0125376273_p34491546114210"></a><span>For a non-security cluster that does not support Kerberos authentication, you can log in to the Master2 node of the cluster using VNC and run the </span><strong id="en-us_topic_0125376273_b2409192211439"><a name="en-us_topic_0125376273_b2409192211439"></a><a name="en-us_topic_0125376273_b2409192211439"></a>ifconfig</strong><span> command to view the floating IP address of the cluster. </span><strong id="en-us_topic_0125376273_b74091422124311"><a name="en-us_topic_0125376273_b74091422124311"></a><a name="en-us_topic_0125376273_b74091422124311"></a>eth0:wsom</strong><span> indicates the floating IP address of MRS Manager. The value of the </span><strong id="en-us_topic_0125376273_b740914229437"><a name="en-us_topic_0125376273_b740914229437"></a><a name="en-us_topic_0125376273_b740914229437"></a>inet</strong><span> parameter is the floating IP address.</span></p>
<div class="note" id="en-us_topic_0125376273_note1885312353418"><a name="en-us_topic_0125376273_note1885312353418"></a><a name="en-us_topic_0125376273_note1885312353418"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0125376273_p208546356415"><a name="en-us_topic_0125376273_p208546356415"></a><a name="en-us_topic_0125376273_p208546356415"></a>If the floating IP address of MRS Manager cannot be queried on the Master2 node, switch to the Master1 node to query and record the floating IP address.</p>
</div></div>
</td>
</tr>
<tr id="en-us_topic_0125376273_row432302413411"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0125376273_p832416241411"><a name="en-us_topic_0125376273_p832416241411"></a><a name="en-us_topic_0125376273_p832416241411"></a>MRS Manager port</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0125376273_p1032402414420"><a name="en-us_topic_0125376273_p1032402414420"></a><a name="en-us_topic_0125376273_p1032402414420"></a>Port for logging in to MRS Manager. The default value is 28443.</p>
</td>
</tr>
<tr id="en-us_topic_0125376273_r9025f4bb60c24d2895d4abf942f61f95"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0125376273_a15ff34de37184f04856ba021a6d96f89"><a name="en-us_topic_0125376273_a15ff34de37184f04856ba021a6d96f89"></a><a name="en-us_topic_0125376273_a15ff34de37184f04856ba021a6d96f89"></a>resource-path</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0125376273_a35f85cbdd89b4e95bf243bd51cf3aefa"><a name="en-us_topic_0125376273_a35f85cbdd89b4e95bf243bd51cf3aefa"></a><a name="en-us_topic_0125376273_a35f85cbdd89b4e95bf243bd51cf3aefa"></a>Specifies a resource path, that is, an API access path. Obtain this value from the URI of a specific API, for example, <strong id="en-us_topic_0125376273_a862cb86e0f8f434080be9a5ac31d71f2"><a name="en-us_topic_0125376273_a862cb86e0f8f434080be9a5ac31d71f2"></a><a name="en-us_topic_0125376273_a862cb86e0f8f434080be9a5ac31d71f2"></a>v3/auth/tokens</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0125376273_r2d8c4aa44a1647e9b5e33f9c307699d5"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0125376273_ab838f891ab5c492daf9c565ba0eaf91d"><a name="en-us_topic_0125376273_ab838f891ab5c492daf9c565ba0eaf91d"></a><a name="en-us_topic_0125376273_ab838f891ab5c492daf9c565ba0eaf91d"></a>Query string</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0125376273_af7c1f60a9272459f9da3b3840c6d9835"><a name="en-us_topic_0125376273_af7c1f60a9272459f9da3b3840c6d9835"></a><a name="en-us_topic_0125376273_af7c1f60a9272459f9da3b3840c6d9835"></a>This parameter is optional. For example, you can set it to API version or resource selection criteria.</p>
</td>
</tr>
</tbody>
</table>

## Request Methods<a name="en-us_topic_0125376273_section1437511065519"></a>

HTTP methods, which are also called operations or actions, specify the type of operations that you are requesting.

**Table  2**  HTTP methods

<a name="en-us_topic_0125376273_t918bb5e59b134a739192f8838a37b071"></a>
<table><thead align="left"><tr id="en-us_topic_0125376273_r93e35e0d6bc74d99b6a63f509792c214"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.3.1.1"><p id="en-us_topic_0125376273_a4f5d6e9c022a42b0bd1fe3ef73b88372"><a name="en-us_topic_0125376273_a4f5d6e9c022a42b0bd1fe3ef73b88372"></a><a name="en-us_topic_0125376273_a4f5d6e9c022a42b0bd1fe3ef73b88372"></a>Method</p>
</th>
<th class="cellrowborder" valign="top" width="82%" id="mcps1.2.3.1.2"><p id="en-us_topic_0125376273_a320567a925b74bb5b677cb12c2ad9933"><a name="en-us_topic_0125376273_a320567a925b74bb5b677cb12c2ad9933"></a><a name="en-us_topic_0125376273_a320567a925b74bb5b677cb12c2ad9933"></a><strong id="en-us_topic_0125376273_en-us_topic_0110581851_b842352706134712"><a name="en-us_topic_0125376273_en-us_topic_0110581851_b842352706134712"></a><a name="en-us_topic_0125376273_en-us_topic_0110581851_b842352706134712"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376273_r67e6bb4864e747528497c8256034803c"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0125376273_ab4f8d722d29c431cb33cc9edd77c7f78"><a name="en-us_topic_0125376273_ab4f8d722d29c431cb33cc9edd77c7f78"></a><a name="en-us_topic_0125376273_ab4f8d722d29c431cb33cc9edd77c7f78"></a>GET</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0125376273_a762afdfc07ae4639a252c46e1197a442"><a name="en-us_topic_0125376273_a762afdfc07ae4639a252c46e1197a442"></a><a name="en-us_topic_0125376273_a762afdfc07ae4639a252c46e1197a442"></a>Requests a server to return the specified resources.</p>
</td>
</tr>
<tr id="en-us_topic_0125376273_r0ca064b7961348b183edf354cac8f1ce"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0125376273_a7367944bac5a4e81b99773b5938a8434"><a name="en-us_topic_0125376273_a7367944bac5a4e81b99773b5938a8434"></a><a name="en-us_topic_0125376273_a7367944bac5a4e81b99773b5938a8434"></a>PUT</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0125376273_a626f067da1e34c109f38ee6e642ac4d0"><a name="en-us_topic_0125376273_a626f067da1e34c109f38ee6e642ac4d0"></a><a name="en-us_topic_0125376273_a626f067da1e34c109f38ee6e642ac4d0"></a>Requests a server to update the specified resources.</p>
</td>
</tr>
<tr id="en-us_topic_0125376273_r60c6a5fbb933424da2c292f5457325a5"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0125376273_ac8c9934549344144b06bf2466a1b7437"><a name="en-us_topic_0125376273_ac8c9934549344144b06bf2466a1b7437"></a><a name="en-us_topic_0125376273_ac8c9934549344144b06bf2466a1b7437"></a>POST</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0125376273_a85ca21ab62db4ff38d18ae02611507e8"><a name="en-us_topic_0125376273_a85ca21ab62db4ff38d18ae02611507e8"></a><a name="en-us_topic_0125376273_a85ca21ab62db4ff38d18ae02611507e8"></a>Requests a server to add resources or perform special operations.</p>
</td>
</tr>
<tr id="en-us_topic_0125376273_rd3ad4679acb3476e89e8e5183d330008"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0125376273_aeda3833ce0d444d1a19b6aa15759c356"><a name="en-us_topic_0125376273_aeda3833ce0d444d1a19b6aa15759c356"></a><a name="en-us_topic_0125376273_aeda3833ce0d444d1a19b6aa15759c356"></a>DELETE</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0125376273_a26bf4ce5b4414338a67aac5e639e5c69"><a name="en-us_topic_0125376273_a26bf4ce5b4414338a67aac5e639e5c69"></a><a name="en-us_topic_0125376273_a26bf4ce5b4414338a67aac5e639e5c69"></a>Requests a server to delete specified resources, for example, an object.</p>
</td>
</tr>
<tr id="en-us_topic_0125376273_rebfda88fee954bc2b14c8d59cd490d80"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0125376273_a6a250d64328c4a3bb7972fd24654fd76"><a name="en-us_topic_0125376273_a6a250d64328c4a3bb7972fd24654fd76"></a><a name="en-us_topic_0125376273_a6a250d64328c4a3bb7972fd24654fd76"></a>HEAD</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0125376273_a849d9e541ecc42d39325707e7fc447ef"><a name="en-us_topic_0125376273_a849d9e541ecc42d39325707e7fc447ef"></a><a name="en-us_topic_0125376273_a849d9e541ecc42d39325707e7fc447ef"></a>Requests a server resource header.</p>
</td>
</tr>
<tr id="en-us_topic_0125376273_r531bd60ebe934ca7b358c8559ff2d68e"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0125376273_a3ddbfe77ed05471db32a101167690c2f"><a name="en-us_topic_0125376273_a3ddbfe77ed05471db32a101167690c2f"></a><a name="en-us_topic_0125376273_a3ddbfe77ed05471db32a101167690c2f"></a>PATCH</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0125376273_a7817e14c4815436dbde219726c16cb63"><a name="en-us_topic_0125376273_a7817e14c4815436dbde219726c16cb63"></a><a name="en-us_topic_0125376273_a7817e14c4815436dbde219726c16cb63"></a>Requests a server to update the partial content of the specified resource.</p>
<p id="en-us_topic_0125376273_aeaddfbe2d7904c3bba28c2b4b3825702"><a name="en-us_topic_0125376273_aeaddfbe2d7904c3bba28c2b4b3825702"></a><a name="en-us_topic_0125376273_aeaddfbe2d7904c3bba28c2b4b3825702"></a>If the resource does not exist, the PATCH method may create a resource.</p>
</td>
</tr>
</tbody>
</table>

## Request Header<a name="en-us_topic_0125376273_section559515309552"></a>

A request header consists of several header fields. Each header field consists of a field name, a colon \(:\), and a field value.

You can also add additional fields to the request header, for example, the fields required by a specified URI and an HTTP method. For details about common request headers, see  [Table 3](#en-us_topic_0125376273_tb3f5c5f3dfb84fce8aa08057e60545ac). For details about the request authentication information, see [Authentication](authentication.md).

**Table  3**  Common request headers

<a name="en-us_topic_0125376273_tb3f5c5f3dfb84fce8aa08057e60545ac"></a>
<table><thead align="left"><tr id="en-us_topic_0125376273_rb849972ee8c74d759f6fc8b86a8a57e6"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376273_a5c386b98502a4beda950b89d96464acb"><a name="en-us_topic_0125376273_a5c386b98502a4beda950b89d96464acb"></a><a name="en-us_topic_0125376273_a5c386b98502a4beda950b89d96464acb"></a><strong id="en-us_topic_0125376273_a662640af392749868e6b1d159b1c7118"><a name="en-us_topic_0125376273_a662640af392749868e6b1d159b1c7118"></a><a name="en-us_topic_0125376273_a662640af392749868e6b1d159b1c7118"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376273_a138f26b2335841e7ae1fad7e1d2de58b"><a name="en-us_topic_0125376273_a138f26b2335841e7ae1fad7e1d2de58b"></a><a name="en-us_topic_0125376273_a138f26b2335841e7ae1fad7e1d2de58b"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376273_aade48220e5ef4b9bafbbdcc325a5ff7e"><a name="en-us_topic_0125376273_aade48220e5ef4b9bafbbdcc325a5ff7e"></a><a name="en-us_topic_0125376273_aade48220e5ef4b9bafbbdcc325a5ff7e"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="30%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376273_aaefeba1a15d540dfadb3af89c308d430"><a name="en-us_topic_0125376273_aaefeba1a15d540dfadb3af89c308d430"></a><a name="en-us_topic_0125376273_aaefeba1a15d540dfadb3af89c308d430"></a>Example</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376273_r501d9bd22d71407084ad2a83519c07a0"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376273_a6819cb341451482d91da271099efbbe5"><a name="en-us_topic_0125376273_a6819cb341451482d91da271099efbbe5"></a><a name="en-us_topic_0125376273_a6819cb341451482d91da271099efbbe5"></a>Content-type</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376273_a18121bc2f94b4a29b6380ec935976930"><a name="en-us_topic_0125376273_a18121bc2f94b4a29b6380ec935976930"></a><a name="en-us_topic_0125376273_a18121bc2f94b4a29b6380ec935976930"></a>MIME type of the sent request body</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376273_a46beafbd500e4fa58eed8e5001bfb4e1"><a name="en-us_topic_0125376273_a46beafbd500e4fa58eed8e5001bfb4e1"></a><a name="en-us_topic_0125376273_a46beafbd500e4fa58eed8e5001bfb4e1"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376273_a4fbe73e0b8ab4566afe028afe4b086e4"><a name="en-us_topic_0125376273_a4fbe73e0b8ab4566afe028afe4b086e4"></a><a name="en-us_topic_0125376273_a4fbe73e0b8ab4566afe028afe4b086e4"></a>application/json</p>
</td>
</tr>
<tr id="en-us_topic_0125376273_r62435759348941618d567c93e0bd8e05"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376273_a0635f1e462f34d5aa097fc8d31f98b71"><a name="en-us_topic_0125376273_a0635f1e462f34d5aa097fc8d31f98b71"></a><a name="en-us_topic_0125376273_a0635f1e462f34d5aa097fc8d31f98b71"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376273_a70178e8313944911997e5789736c231a"><a name="en-us_topic_0125376273_a70178e8313944911997e5789736c231a"></a><a name="en-us_topic_0125376273_a70178e8313944911997e5789736c231a"></a>Length of the request body. The unit is byte.</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376273_a7be62605f4254a53b504c35f19f99385"><a name="en-us_topic_0125376273_a7be62605f4254a53b504c35f19f99385"></a><a name="en-us_topic_0125376273_a7be62605f4254a53b504c35f19f99385"></a>This parameter is mandatory for POST and PUT requests but must be left blank for GET requests.</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376273_aba00e8e59f394f0397ab067e18a6ed64"><a name="en-us_topic_0125376273_aba00e8e59f394f0397ab067e18a6ed64"></a><a name="en-us_topic_0125376273_aba00e8e59f394f0397ab067e18a6ed64"></a>3495</p>
</td>
</tr>
<tr id="en-us_topic_0125376273_rf226614952f44dc3bf8dca12e52b6003"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376273_a0bdd89f7dc6342699176779e2dc28605"><a name="en-us_topic_0125376273_a0bdd89f7dc6342699176779e2dc28605"></a><a name="en-us_topic_0125376273_a0bdd89f7dc6342699176779e2dc28605"></a>X-Language</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376273_a75295e940ff74f35a18f170341929c21"><a name="en-us_topic_0125376273_a75295e940ff74f35a18f170341929c21"></a><a name="en-us_topic_0125376273_a75295e940ff74f35a18f170341929c21"></a>Request language. Values include:</p>
<a name="en-us_topic_0125376273_ube3c929c82e64cc8932db34e8518729e"></a><a name="en-us_topic_0125376273_ube3c929c82e64cc8932db34e8518729e"></a><ul id="en-us_topic_0125376273_ube3c929c82e64cc8932db34e8518729e"><li><strong id="en-us_topic_0125376273_ab722d3cbfe2742e4a4e908be93514c18"><a name="en-us_topic_0125376273_ab722d3cbfe2742e4a4e908be93514c18"></a><a name="en-us_topic_0125376273_ab722d3cbfe2742e4a4e908be93514c18"></a>zh-cn</strong>: Chinese</li><li><strong id="en-us_topic_0125376273_b51152427185931"><a name="en-us_topic_0125376273_b51152427185931"></a><a name="en-us_topic_0125376273_b51152427185931"></a>en-us</strong>: English</li></ul>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376273_a3422981cd66b4db08489b0b7b5d9dc25"><a name="en-us_topic_0125376273_a3422981cd66b4db08489b0b7b5d9dc25"></a><a name="en-us_topic_0125376273_a3422981cd66b4db08489b0b7b5d9dc25"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376273_a1983da4704c44a4ca611ccba526868a2"><a name="en-us_topic_0125376273_a1983da4704c44a4ca611ccba526868a2"></a><a name="en-us_topic_0125376273_a1983da4704c44a4ca611ccba526868a2"></a>en-us</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>For details about other parameters in the header, see the HTTP protocol documentation.  

## Request Body<a name="en-us_topic_0125376273_section1692615591277"></a>

A request body is generally sent in a structured format \(for example, JSON or XML\), corresponding to  **Content-type**  in the request header, and is used to transfer content other than the request header.

## Response Header<a name="en-us_topic_0125376273_section33899391911"></a>

A response header consists of the following two parts:

-   An HTTP status code, from 2_xx_ success code to 4_xx_ or 5_xx_  error code, or status code that can return the service definition, as shown in the API document
-   Additional fields in the response header required by a specified response, for example, the  **Content-type** response header. For details about common response headers, see [Table 4](#en-us_topic_0125376273_ta1929fc30fc14e1ebf1cf848648c76d8).

    **Table  4**  Common response headers

    <a name="en-us_topic_0125376273_ta1929fc30fc14e1ebf1cf848648c76d8"></a>
    <table><thead align="left"><tr id="en-us_topic_0125376273_re807ee13e4a14507ae7eb50ee27e6243"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.5.1.1"><p id="en-us_topic_0125376273_a41658ca83f064ebfb02c33c5be0e703e"><a name="en-us_topic_0125376273_a41658ca83f064ebfb02c33c5be0e703e"></a><a name="en-us_topic_0125376273_a41658ca83f064ebfb02c33c5be0e703e"></a><strong id="en-us_topic_0125376273_a04df1db6deef423485642cbd7282e4a4"><a name="en-us_topic_0125376273_a04df1db6deef423485642cbd7282e4a4"></a><a name="en-us_topic_0125376273_a04df1db6deef423485642cbd7282e4a4"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36%" id="mcps1.2.5.1.2"><p id="en-us_topic_0125376273_ae358ccf6b18542ab9bbc4e296d2ac355"><a name="en-us_topic_0125376273_ae358ccf6b18542ab9bbc4e296d2ac355"></a><a name="en-us_topic_0125376273_ae358ccf6b18542ab9bbc4e296d2ac355"></a><strong id="en-us_topic_0125376273_b31481387185931"><a name="en-us_topic_0125376273_b31481387185931"></a><a name="en-us_topic_0125376273_b31481387185931"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="9%" id="mcps1.2.5.1.3"><p id="en-us_topic_0125376273_p88717713613"><a name="en-us_topic_0125376273_p88717713613"></a><a name="en-us_topic_0125376273_p88717713613"></a>Mandatory or Not</p>
    </th>
    <th class="cellrowborder" valign="top" width="31%" id="mcps1.2.5.1.4"><p id="en-us_topic_0125376273_ab90bc0aeea65400689bcf5116c65b5a0"><a name="en-us_topic_0125376273_ab90bc0aeea65400689bcf5116c65b5a0"></a><a name="en-us_topic_0125376273_ab90bc0aeea65400689bcf5116c65b5a0"></a>Example</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0125376273_re2211cb0f9e14e8599f835744a3f5a4f"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376273_aa8cc5be1a1994ae9af561f4cf4345478"><a name="en-us_topic_0125376273_aa8cc5be1a1994ae9af561f4cf4345478"></a><a name="en-us_topic_0125376273_aa8cc5be1a1994ae9af561f4cf4345478"></a>Date</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376273_a6e285d2b752f4170bcd72ee8c33c6e9c"><a name="en-us_topic_0125376273_a6e285d2b752f4170bcd72ee8c33c6e9c"></a><a name="en-us_topic_0125376273_a6e285d2b752f4170bcd72ee8c33c6e9c"></a>Standard HTTP header, which specifies the date and time at which the message was sent. The format is defined by RFC 822.</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376273_p5871876614"><a name="en-us_topic_0125376273_p5871876614"></a><a name="en-us_topic_0125376273_p5871876614"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376273_ae93a6c395cbd4826b64e6a9827cd6b0e"><a name="en-us_topic_0125376273_ae93a6c395cbd4826b64e6a9827cd6b0e"></a><a name="en-us_topic_0125376273_ae93a6c395cbd4826b64e6a9827cd6b0e"></a>Mon, 12 Nov 2007 15:55:01 GMT</p>
    </td>
    </tr>
    <tr id="en-us_topic_0125376273_r8d9260b7191f4f6c9930201ee3101392"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376273_a651a11db80104697b6c3c30c95bc263d"><a name="en-us_topic_0125376273_a651a11db80104697b6c3c30c95bc263d"></a><a name="en-us_topic_0125376273_a651a11db80104697b6c3c30c95bc263d"></a>Server</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376273_ad99f967ef9ca48a9aa9087694af86a8e"><a name="en-us_topic_0125376273_ad99f967ef9ca48a9aa9087694af86a8e"></a><a name="en-us_topic_0125376273_ad99f967ef9ca48a9aa9087694af86a8e"></a>Standard HTTP header, which includes the software information that the server uses to process the request.</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376273_p158737868"><a name="en-us_topic_0125376273_p158737868"></a><a name="en-us_topic_0125376273_p158737868"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376273_a37374b1afb104a2a9cc43931bc9c5cca"><a name="en-us_topic_0125376273_a37374b1afb104a2a9cc43931bc9c5cca"></a><a name="en-us_topic_0125376273_a37374b1afb104a2a9cc43931bc9c5cca"></a>Apache</p>
    </td>
    </tr>
    <tr id="en-us_topic_0125376273_rbe41f12a5f26406eb43cd43e5ced0e88"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376273_ade016caaf4954370b7f53b48540d365b"><a name="en-us_topic_0125376273_ade016caaf4954370b7f53b48540d365b"></a><a name="en-us_topic_0125376273_ade016caaf4954370b7f53b48540d365b"></a>Content-Length</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376273_a523d3a520c104dc694a5bbc70056d308"><a name="en-us_topic_0125376273_a523d3a520c104dc694a5bbc70056d308"></a><a name="en-us_topic_0125376273_a523d3a520c104dc694a5bbc70056d308"></a>Standard HTTP header, which specifies the size of the entity body, in decimal number of bytes, sent to the recipient.</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376273_p1187167461"><a name="en-us_topic_0125376273_p1187167461"></a><a name="en-us_topic_0125376273_p1187167461"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376273_ae65ca61be58e4e0a94e6d02fc9234468"><a name="en-us_topic_0125376273_ae65ca61be58e4e0a94e6d02fc9234468"></a><a name="en-us_topic_0125376273_ae65ca61be58e4e0a94e6d02fc9234468"></a>xxx</p>
    </td>
    </tr>
    <tr id="en-us_topic_0125376273_rb698600904774d098bde430fa0e484c5"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0125376273_a916851eb6c8d4b1fb5507470a678180a"><a name="en-us_topic_0125376273_a916851eb6c8d4b1fb5507470a678180a"></a><a name="en-us_topic_0125376273_a916851eb6c8d4b1fb5507470a678180a"></a>Content-type</p>
    </td>
    <td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0125376273_a2176f3a4392247d0a68ab4c59bb60a61"><a name="en-us_topic_0125376273_a2176f3a4392247d0a68ab4c59bb60a61"></a><a name="en-us_topic_0125376273_a2176f3a4392247d0a68ab4c59bb60a61"></a>Standard HTTP header, which specifies the media type of the entity body sent to the recipient.</p>
    </td>
    <td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0125376273_p118715716613"><a name="en-us_topic_0125376273_p118715716613"></a><a name="en-us_topic_0125376273_p118715716613"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0125376273_a8301f9bb0b9248da88e5ce4ee91fb092"><a name="en-us_topic_0125376273_a8301f9bb0b9248da88e5ce4ee91fb092"></a><a name="en-us_topic_0125376273_a8301f9bb0b9248da88e5ce4ee91fb092"></a>application/json</p>
    </td>
    </tr>
    </tbody>
    </table>


## Response Body<a name="en-us_topic_0125376273_section186021620141012"></a>

A response body is generally returned in a structured format \(for example, JSON or XML\), corresponding to  **Content-type**  in the response header, and is used to transfer content other than the response header.

## Sending a Request<a name="en-us_topic_0125376273_section17323144941019"></a>

You can send a request based on the constructed request body using any of the following three methods:

-   cURL

    cURL is a command-line tool used to perform URL operations and transfer information. cURL acts as an HTTP client that can send HTTP requests to the server and receive response messages. It is applicable to API debugging. For more information about cURL, visit  [https://curl.haxx.se/](https://curl.haxx.se/).

-   Code

    You can call APIs using code to assemble, send, and process request messages.

-   REST clients

    Both Mozilla Firefox and Google Chrome provide a graphical browser plug-in, that is, REST client, to send and process requests. For Mozilla Firefox, see  [Firefox REST Client](https://addons.mozilla.org/en-US/firefox/addon/restclient/). For Google Chrome, see [Postman Interceptor](https://chrome.google.com/webstore/detail/postman-interceptor/aicmkgpgakddgnaphhhpliifpcfhicfo/).


