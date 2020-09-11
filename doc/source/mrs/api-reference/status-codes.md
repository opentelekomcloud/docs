# Status Codes<a name="EN-US_TOPIC_0172602529"></a>

[Table 1](#tbcc499a25f1a4cdcb3933a128e804ad8)  describes status codes.

**Table  1**  Status codes

<a name="tbcc499a25f1a4cdcb3933a128e804ad8"></a>
<table><thead align="left"><tr id="r1e72af18ed6b41269b993ef96d19a7f7"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="a97d6af6c69f3423487d7de41ed990f9b"><a name="a97d6af6c69f3423487d7de41ed990f9b"></a><a name="a97d6af6c69f3423487d7de41ed990f9b"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="a1d82889868ed480b901f0b54478253d2"><a name="a1d82889868ed480b901f0b54478253d2"></a><a name="a1d82889868ed480b901f0b54478253d2"></a>Message</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.4.1.3"><p id="a65d095ece8714e66a41688d85eace437"><a name="a65d095ece8714e66a41688d85eace437"></a><a name="a65d095ece8714e66a41688d85eace437"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r1ef6b934fbae4e1ab8a074f919eb6210"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a2b1ec72c8da044d2b6e86d429d2f2c34"><a name="a2b1ec72c8da044d2b6e86d429d2f2c34"></a><a name="a2b1ec72c8da044d2b6e86d429d2f2c34"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a7a45b15c635143a99b0e333fcf90b7e9"><a name="a7a45b15c635143a99b0e333fcf90b7e9"></a><a name="a7a45b15c635143a99b0e333fcf90b7e9"></a>Continue</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ac59960b82e7b46ebac9b3c3b8778e138"><a name="ac59960b82e7b46ebac9b3c3b8778e138"></a><a name="ac59960b82e7b46ebac9b3c3b8778e138"></a>The client should continue with its request.</p>
<p id="a51df030855e84ef68e4651a9496f1764"><a name="a51df030855e84ef68e4651a9496f1764"></a><a name="a51df030855e84ef68e4651a9496f1764"></a>This interim response is used to inform the client that the initial part of the request has been received and has not yet been rejected by the server.</p>
</td>
</tr>
<tr id="rc27f997bc89b422ca39491d5aa5a47ff"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ab06153e44f494c868ca26d081caaefd4"><a name="ab06153e44f494c868ca26d081caaefd4"></a><a name="ab06153e44f494c868ca26d081caaefd4"></a>101</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="af2c0bd1fde1f4f88a9805185597b06bb"><a name="af2c0bd1fde1f4f88a9805185597b06bb"></a><a name="af2c0bd1fde1f4f88a9805185597b06bb"></a>Switching Protocols</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a7bdc0bea6bf04d108f352d1b5044357d"><a name="a7bdc0bea6bf04d108f352d1b5044357d"></a><a name="a7bdc0bea6bf04d108f352d1b5044357d"></a>The protocol should be switched. The protocol can only be switched to a newer protocol.</p>
<p id="a98060c75e6e2495ebbfb578d62efe20e"><a name="a98060c75e6e2495ebbfb578d62efe20e"></a><a name="a98060c75e6e2495ebbfb578d62efe20e"></a>For example, the current HTTPS protocol is switched to a later version.</p>
</td>
</tr>
<tr id="row60081890161212"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p34794944161212"><a name="p34794944161212"></a><a name="p34794944161212"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p66927054161212"><a name="p66927054161212"></a><a name="p66927054161212"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="p63796653161236"><a name="p63796653161236"></a><a name="p63796653161236"></a>The request has been fulfilled.</p>
</td>
</tr>
<tr id="raf229a49ff74493b9c8b77864f057188"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="abe11a57c77c548ec9caee2bca1346a0d"><a name="abe11a57c77c548ec9caee2bca1346a0d"></a><a name="abe11a57c77c548ec9caee2bca1346a0d"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ae83ea0a9cc434bf181d40fe60cffefa3"><a name="ae83ea0a9cc434bf181d40fe60cffefa3"></a><a name="ae83ea0a9cc434bf181d40fe60cffefa3"></a>Created</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a7dbc4b1c6a0645ee90d9525f308e7c78"><a name="a7dbc4b1c6a0645ee90d9525f308e7c78"></a><a name="a7dbc4b1c6a0645ee90d9525f308e7c78"></a>The request has been fulfilled and a new resource has been created.</p>
</td>
</tr>
<tr id="r7a6b4083785d4dc19350ee8dd053a05b"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a50b4d60480a7431891a6fce3be2f4604"><a name="a50b4d60480a7431891a6fce3be2f4604"></a><a name="a50b4d60480a7431891a6fce3be2f4604"></a>202</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a9be604dbd70a47079eb04d149d228ae5"><a name="a9be604dbd70a47079eb04d149d228ae5"></a><a name="a9be604dbd70a47079eb04d149d228ae5"></a>Accepted</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a347055b166d4405dbf2270add04a4dee"><a name="a347055b166d4405dbf2270add04a4dee"></a><a name="a347055b166d4405dbf2270add04a4dee"></a>The request has been accepted, but the processing has not been completed.</p>
</td>
</tr>
<tr id="r9f9315986e1f4f09b25fac74d7cf65c4"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a9394fbdb89fe4620ae0ad893887b5db5"><a name="a9394fbdb89fe4620ae0ad893887b5db5"></a><a name="a9394fbdb89fe4620ae0ad893887b5db5"></a>203</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a4d790f165f134f47acfa4708be442a77"><a name="a4d790f165f134f47acfa4708be442a77"></a><a name="a4d790f165f134f47acfa4708be442a77"></a>Non-Authoritative Information</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a2d1d16ba06314e74a6fa6e7b5baa1bcf"><a name="a2d1d16ba06314e74a6fa6e7b5baa1bcf"></a><a name="a2d1d16ba06314e74a6fa6e7b5baa1bcf"></a>The server has successfully processed the request, but is returning information that may be from another source.</p>
</td>
</tr>
<tr id="re98b5775aae144a68567b3af4da4cca0"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aa9ef24cbcb7949b297033278c55bb1b4"><a name="aa9ef24cbcb7949b297033278c55bb1b4"></a><a name="aa9ef24cbcb7949b297033278c55bb1b4"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="af32f641b57214ea1a98b804e74100ad0"><a name="af32f641b57214ea1a98b804e74100ad0"></a><a name="af32f641b57214ea1a98b804e74100ad0"></a>NoContent</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ab6126c48b8664b83b888cad08e5b8245"><a name="ab6126c48b8664b83b888cad08e5b8245"></a><a name="ab6126c48b8664b83b888cad08e5b8245"></a>The request has been fulfilled, but the HTTPS response does not contain a response body.</p>
<p id="accebb585f8034a419511f7991d57de3f"><a name="accebb585f8034a419511f7991d57de3f"></a><a name="accebb585f8034a419511f7991d57de3f"></a>The status code is returned in response to an HTTPS OPTIONS request.</p>
</td>
</tr>
<tr id="rf4ff2a9d88a64116a5556cd04183c2b2"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a1a14428fde39421c99f78a5799cd6123"><a name="a1a14428fde39421c99f78a5799cd6123"></a><a name="a1a14428fde39421c99f78a5799cd6123"></a>205</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a435f61aa0ed24fdcb44062659641de6d"><a name="a435f61aa0ed24fdcb44062659641de6d"></a><a name="a435f61aa0ed24fdcb44062659641de6d"></a>Reset Content</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a9b3c9da69aa94827bfa275b566708e29"><a name="a9b3c9da69aa94827bfa275b566708e29"></a><a name="a9b3c9da69aa94827bfa275b566708e29"></a>The server has fulfilled the request, but the requester is required to reset the content.</p>
</td>
</tr>
<tr id="r169bb0e63e644cca9eea8487555cde16"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ace63fe2adcc047e9859e34d0c3f177e2"><a name="ace63fe2adcc047e9859e34d0c3f177e2"></a><a name="ace63fe2adcc047e9859e34d0c3f177e2"></a>206</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="aa4354efe9f954f6cb14cd6d8dbcb0c57"><a name="aa4354efe9f954f6cb14cd6d8dbcb0c57"></a><a name="aa4354efe9f954f6cb14cd6d8dbcb0c57"></a>Partial Content</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0037324641_p813455162537"><a name="en-us_topic_0037324641_p813455162537"></a><a name="en-us_topic_0037324641_p813455162537"></a>The server has successfully processed the partial GET request.</p>
</td>
</tr>
<tr id="rd005c4068a1440e483e9efaf6e19ebfa"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="acf802e09cb6f4cfaaed9ace8880c941b"><a name="acf802e09cb6f4cfaaed9ace8880c941b"></a><a name="acf802e09cb6f4cfaaed9ace8880c941b"></a>300</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a0937e22868eb4439a61aece2cbb5380f"><a name="a0937e22868eb4439a61aece2cbb5380f"></a><a name="a0937e22868eb4439a61aece2cbb5380f"></a>Multiple Choices</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ae30e35e51c3a4f3bb31c087d4b4842d1"><a name="ae30e35e51c3a4f3bb31c087d4b4842d1"></a><a name="ae30e35e51c3a4f3bb31c087d4b4842d1"></a>There are multiple options for the location of the requested resource. The response contains a list of resource characteristics and addresses from which a user terminal (such as a browser) can choose the most appropriate one.</p>
</td>
</tr>
<tr id="rdca895d732d1441992a52898d284206e"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a9db78897776a42038e479cb06eb5c32a"><a name="a9db78897776a42038e479cb06eb5c32a"></a><a name="a9db78897776a42038e479cb06eb5c32a"></a>301</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0037324641_p425112162537"><a name="en-us_topic_0037324641_p425112162537"></a><a name="en-us_topic_0037324641_p425112162537"></a>Moved Permanently</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a12e4795584fb44b696c90729e0a7db52"><a name="a12e4795584fb44b696c90729e0a7db52"></a><a name="a12e4795584fb44b696c90729e0a7db52"></a>The requested resource has been assigned a new permanent URI, and the new URI is contained in the response.</p>
</td>
</tr>
<tr id="r001a43807ca74237aaf9fc5b1ad54e33"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a3583f8fc180e45a3bbe021afa9b9a467"><a name="a3583f8fc180e45a3bbe021afa9b9a467"></a><a name="a3583f8fc180e45a3bbe021afa9b9a467"></a>302</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ae6b1420f4d6441aaa34378093dfcc8a2"><a name="ae6b1420f4d6441aaa34378093dfcc8a2"></a><a name="ae6b1420f4d6441aaa34378093dfcc8a2"></a>Found</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ad05f61160c6c4d528199075ef956c48e"><a name="ad05f61160c6c4d528199075ef956c48e"></a><a name="ad05f61160c6c4d528199075ef956c48e"></a>The requested resource resides temporarily under a different URI.</p>
</td>
</tr>
<tr id="r08fe483433694d1e8cd74f5e09db717e"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="af7d0d800ee4c4b05aca8c6dc3dcd7f81"><a name="af7d0d800ee4c4b05aca8c6dc3dcd7f81"></a><a name="af7d0d800ee4c4b05aca8c6dc3dcd7f81"></a>303</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="abd602d887dce4a4990f06aa60d0f997e"><a name="abd602d887dce4a4990f06aa60d0f997e"></a><a name="abd602d887dce4a4990f06aa60d0f997e"></a>See Other</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aeb26543a4323463797470f6247ba1fdf"><a name="aeb26543a4323463797470f6247ba1fdf"></a><a name="aeb26543a4323463797470f6247ba1fdf"></a>The response to the request can be found under a different URI.</p>
<p id="a0ce12a0e2af14701a2de80c10aad904f"><a name="a0ce12a0e2af14701a2de80c10aad904f"></a><a name="a0ce12a0e2af14701a2de80c10aad904f"></a>It can be retrieved by using a GET or POST method.</p>
</td>
</tr>
<tr id="ra74f835800194b3faeaad6e2df746390"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="adb7c51516aa14cec90f216381fe68416"><a name="adb7c51516aa14cec90f216381fe68416"></a><a name="adb7c51516aa14cec90f216381fe68416"></a>304</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ae680825c68844bf68a4a5439346198ca"><a name="ae680825c68844bf68a4a5439346198ca"></a><a name="ae680825c68844bf68a4a5439346198ca"></a>Not Modified</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ab9fb1e8e86ba40bda0ad8a7cfd9ec096"><a name="ab9fb1e8e86ba40bda0ad8a7cfd9ec096"></a><a name="ab9fb1e8e86ba40bda0ad8a7cfd9ec096"></a>The requested resource has not been modified. When the server returns this status code, it does not return any resources.</p>
</td>
</tr>
<tr id="r71dab9d58d694dd58f9f19c87a1c3988"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aa153f2cd7fd64c14893abda52eee579e"><a name="aa153f2cd7fd64c14893abda52eee579e"></a><a name="aa153f2cd7fd64c14893abda52eee579e"></a>305</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a39ce63c801e54363bd5d62dd8d36ee61"><a name="a39ce63c801e54363bd5d62dd8d36ee61"></a><a name="a39ce63c801e54363bd5d62dd8d36ee61"></a>Use Proxy</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a1f5617225dab44528218a050d01150a9"><a name="a1f5617225dab44528218a050d01150a9"></a><a name="a1f5617225dab44528218a050d01150a9"></a>The requested resource is available only through a proxy.</p>
</td>
</tr>
<tr id="re78d6922870141d3bca159894a5f361a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a1ff5456ce9514957839aec11653b436b"><a name="a1ff5456ce9514957839aec11653b436b"></a><a name="a1ff5456ce9514957839aec11653b436b"></a>306</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a2a5eb1cb63164740937036b33f65dfb4"><a name="a2a5eb1cb63164740937036b33f65dfb4"></a><a name="a2a5eb1cb63164740937036b33f65dfb4"></a>Unused</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a102f63107abc4d4c80a941f52e3f1f32"><a name="a102f63107abc4d4c80a941f52e3f1f32"></a><a name="a102f63107abc4d4c80a941f52e3f1f32"></a>The HTTPS status code is no longer used.</p>
</td>
</tr>
<tr id="racfdafb16b5040ef9d1e88d7663cf6e7"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a6a98dca9d2654b4a848b3c3a8b4ab693"><a name="a6a98dca9d2654b4a848b3c3a8b4ab693"></a><a name="a6a98dca9d2654b4a848b3c3a8b4ab693"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="acf3d0bec9a5e4a398336ca6fe7f2a1a2"><a name="acf3d0bec9a5e4a398336ca6fe7f2a1a2"></a><a name="acf3d0bec9a5e4a398336ca6fe7f2a1a2"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="adb93e2c9501c4e51bd30f137fff3b78c"><a name="adb93e2c9501c4e51bd30f137fff3b78c"></a><a name="adb93e2c9501c4e51bd30f137fff3b78c"></a>The request is invalid.</p>
<p id="a1e1599cb698c40de81f0a2fdf5ef4bbc"><a name="a1e1599cb698c40de81f0a2fdf5ef4bbc"></a><a name="a1e1599cb698c40de81f0a2fdf5ef4bbc"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="r293576a3bfe947b2bdd2215d42540f2b"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aa71f6e35880045ab9dab66989538ccf0"><a name="aa71f6e35880045ab9dab66989538ccf0"></a><a name="aa71f6e35880045ab9dab66989538ccf0"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a4334f458f96449a5ae4fa73776bfa01e"><a name="a4334f458f96449a5ae4fa73776bfa01e"></a><a name="a4334f458f96449a5ae4fa73776bfa01e"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a04f15b96c80b48fcb1e6a1293790c331"><a name="a04f15b96c80b48fcb1e6a1293790c331"></a><a name="a04f15b96c80b48fcb1e6a1293790c331"></a>This status code is returned after the client provides the authentication information, indicating that the authentication information is incorrect or invalid.</p>
</td>
</tr>
<tr id="r1d6a6c32239d4b4e9417d0209e7846e2"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ab186e3436b924bbf95c51be7d813e5f5"><a name="ab186e3436b924bbf95c51be7d813e5f5"></a><a name="ab186e3436b924bbf95c51be7d813e5f5"></a>402</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a2c1ed3d58ca04ad2a7c68beea4c226b2"><a name="a2c1ed3d58ca04ad2a7c68beea4c226b2"></a><a name="a2c1ed3d58ca04ad2a7c68beea4c226b2"></a>Payment Required</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a971ecc06f6e8465bae3d6bc56b2d2f45"><a name="a971ecc06f6e8465bae3d6bc56b2d2f45"></a><a name="a971ecc06f6e8465bae3d6bc56b2d2f45"></a>This status code is reserved for future use.</p>
</td>
</tr>
<tr id="rb5d180d711734e249c73c9f091063a69"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ae7400644cd2e458580f5cd722b254e7e"><a name="ae7400644cd2e458580f5cd722b254e7e"></a><a name="ae7400644cd2e458580f5cd722b254e7e"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ae99aa3a9d2e04ba6a5f400491f90181c"><a name="ae99aa3a9d2e04ba6a5f400491f90181c"></a><a name="ae99aa3a9d2e04ba6a5f400491f90181c"></a>Forbidden</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a104ca10dc86d457ca12219d9eecb5c16"><a name="a104ca10dc86d457ca12219d9eecb5c16"></a><a name="a104ca10dc86d457ca12219d9eecb5c16"></a>The server understood the request, but is refusing to fulfill it.</p>
<p id="a4eef4302c649414a95f5d2a7d4075a6b"><a name="a4eef4302c649414a95f5d2a7d4075a6b"></a><a name="a4eef4302c649414a95f5d2a7d4075a6b"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="r1ce941e745ad4b60a8be433a956917e3"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a8abe4e1c09c2432a98191538e6a445a5"><a name="a8abe4e1c09c2432a98191538e6a445a5"></a><a name="a8abe4e1c09c2432a98191538e6a445a5"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a637e80e7a9c74799979b1fd7c02205d7"><a name="a637e80e7a9c74799979b1fd7c02205d7"></a><a name="a637e80e7a9c74799979b1fd7c02205d7"></a>NotFound</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a989506cde3184b33b96b339d65d04620"><a name="a989506cde3184b33b96b339d65d04620"></a><a name="a989506cde3184b33b96b339d65d04620"></a>The requested resource cannot be found. </p>
<p id="a4580d570f2634ab4ac66042f600bcb2a"><a name="a4580d570f2634ab4ac66042f600bcb2a"></a><a name="a4580d570f2634ab4ac66042f600bcb2a"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="re053ad1595264069bb0a49f33d874f55"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aba8a05159c1c4c169566523f8a59dfce"><a name="aba8a05159c1c4c169566523f8a59dfce"></a><a name="aba8a05159c1c4c169566523f8a59dfce"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ace64a3fe279c425a868587a1a5114622"><a name="ace64a3fe279c425a868587a1a5114622"></a><a name="ace64a3fe279c425a868587a1a5114622"></a>MethodNotAllowed</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ad0bb7ce5e8c94d84a69de2002bad64f3"><a name="ad0bb7ce5e8c94d84a69de2002bad64f3"></a><a name="ad0bb7ce5e8c94d84a69de2002bad64f3"></a>A request method is not supported for the requested resource.</p>
<p id="a3b8606c304d04204885a4e6bee615b82"><a name="a3b8606c304d04204885a4e6bee615b82"></a><a name="a3b8606c304d04204885a4e6bee615b82"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="r3f827db5bc014ec6b5f7e912848970ce"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aee9f58c107a748569cc73ecbfefc8cf9"><a name="aee9f58c107a748569cc73ecbfefc8cf9"></a><a name="aee9f58c107a748569cc73ecbfefc8cf9"></a>406</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ab85eaa4408a34ebbbf31d97932ad1275"><a name="ab85eaa4408a34ebbbf31d97932ad1275"></a><a name="ab85eaa4408a34ebbbf31d97932ad1275"></a>Not Acceptable</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a1044394d9bb84613bd8ceacb4381f038"><a name="a1044394d9bb84613bd8ceacb4381f038"></a><a name="a1044394d9bb84613bd8ceacb4381f038"></a>The server cannot fulfill the request according to the content characteristics of the request.</p>
</td>
</tr>
<tr id="r63ce829f677145ebb6ee8cdb38905749"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="ade93e96156fa42dd96563174d80e32d7"><a name="ade93e96156fa42dd96563174d80e32d7"></a><a name="ade93e96156fa42dd96563174d80e32d7"></a>407</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a38af6bce9c674ac28d6b7fb4e3c1d557"><a name="a38af6bce9c674ac28d6b7fb4e3c1d557"></a><a name="a38af6bce9c674ac28d6b7fb4e3c1d557"></a>Proxy Authentication Required</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a7a4401d99be142f586e68b915c2235cc"><a name="a7a4401d99be142f586e68b915c2235cc"></a><a name="a7a4401d99be142f586e68b915c2235cc"></a>This status code is similar to 401, but indicates that the client must first authenticate itself with the proxy.</p>
</td>
</tr>
<tr id="r5908336b36e34222aa3adc413f33307d"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a9b7515c90c5a4d87832fcad24a281e98"><a name="a9b7515c90c5a4d87832fcad24a281e98"></a><a name="a9b7515c90c5a4d87832fcad24a281e98"></a>408</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a681c274f386b4386adf7175cb29866ab"><a name="a681c274f386b4386adf7175cb29866ab"></a><a name="a681c274f386b4386adf7175cb29866ab"></a>Request Time-out</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a9f88c15753784bc8b567c97918b2dac3"><a name="a9f88c15753784bc8b567c97918b2dac3"></a><a name="a9f88c15753784bc8b567c97918b2dac3"></a>The server has timed out waiting for the request.</p>
<p id="a9679ff4a15604fe9acd86586b74e4797"><a name="a9679ff4a15604fe9acd86586b74e4797"></a><a name="a9679ff4a15604fe9acd86586b74e4797"></a>The client may repeat the request without modifications at a later time.</p>
</td>
</tr>
<tr id="r2c47f3af2213469eaa43c9e6c333c9e1"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="abe216c508ca44e2eb1333a448b9722e4"><a name="abe216c508ca44e2eb1333a448b9722e4"></a><a name="abe216c508ca44e2eb1333a448b9722e4"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a540eb169400d45379e101a3c00500dbc"><a name="a540eb169400d45379e101a3c00500dbc"></a><a name="a540eb169400d45379e101a3c00500dbc"></a>Conflict</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ac724a894d2f547ecb01ec6bb2a07f9db"><a name="ac724a894d2f547ecb01ec6bb2a07f9db"></a><a name="ac724a894d2f547ecb01ec6bb2a07f9db"></a>The request could not be processed due to a conflict with the current state of the resource.</p>
<p id="ad1937bd33f4048ac962b123609917df8"><a name="ad1937bd33f4048ac962b123609917df8"></a><a name="ad1937bd33f4048ac962b123609917df8"></a>This status code indicates that the resource that the client is attempting to create already exists, or that the request has failed to be processed because of the update of the conflict request.</p>
</td>
</tr>
<tr id="r51dc89645bed4a1db9c537ca4bc8a88a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a590573bdbfa8476c8f9abe36311cdccc"><a name="a590573bdbfa8476c8f9abe36311cdccc"></a><a name="a590573bdbfa8476c8f9abe36311cdccc"></a>410</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a6fd5edf67a0d46ceaf28776b08388ca6"><a name="a6fd5edf67a0d46ceaf28776b08388ca6"></a><a name="a6fd5edf67a0d46ceaf28776b08388ca6"></a>Gone</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a41634b7103b74fa7b7e2602c5953e069"><a name="a41634b7103b74fa7b7e2602c5953e069"></a><a name="a41634b7103b74fa7b7e2602c5953e069"></a>The requested resource has been deleted permanently and is no longer available.</p>
<p id="a964edd0267014ab1aca7183157a99b63"><a name="a964edd0267014ab1aca7183157a99b63"></a><a name="a964edd0267014ab1aca7183157a99b63"></a> </p>
</td>
</tr>
<tr id="rb843292b16774a55b957f1a4a191b7ad"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a4857ec65b1134ce4b9396ef7150601dc"><a name="a4857ec65b1134ce4b9396ef7150601dc"></a><a name="a4857ec65b1134ce4b9396ef7150601dc"></a>411</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a7e5c7af3719141e0b8b10a6b8c1cbd21"><a name="a7e5c7af3719141e0b8b10a6b8c1cbd21"></a><a name="a7e5c7af3719141e0b8b10a6b8c1cbd21"></a>Length Required</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a9626fcf4bfb44d0893fabde87eaa1052"><a name="a9626fcf4bfb44d0893fabde87eaa1052"></a><a name="a9626fcf4bfb44d0893fabde87eaa1052"></a>The server is refusing to process the request without a defined <strong id="b579314021715"><a name="b579314021715"></a><a name="b579314021715"></a>Content-Length</strong>.</p>
</td>
</tr>
<tr id="rec441d3142cb408cbd71f04476a46d98"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a753f5e5d48314713ad7a1307ebd47528"><a name="a753f5e5d48314713ad7a1307ebd47528"></a><a name="a753f5e5d48314713ad7a1307ebd47528"></a>412</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="aefd47c50fe3c44df9d925000470cb356"><a name="aefd47c50fe3c44df9d925000470cb356"></a><a name="aefd47c50fe3c44df9d925000470cb356"></a>Precondition Failed</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aadf285f6a7b349078a6b18aa35a62ee6"><a name="aadf285f6a7b349078a6b18aa35a62ee6"></a><a name="aadf285f6a7b349078a6b18aa35a62ee6"></a>The server did not meet one of the preconditions that the requester put on the request.</p>
</td>
</tr>
<tr id="r00943feed116444791dc4e79a788b916"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aa14c4c1b2835466aa792b34ceabcbb7b"><a name="aa14c4c1b2835466aa792b34ceabcbb7b"></a><a name="aa14c4c1b2835466aa792b34ceabcbb7b"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a33ede2b1c1c643dd9abf13b18383d9bf"><a name="a33ede2b1c1c643dd9abf13b18383d9bf"></a><a name="a33ede2b1c1c643dd9abf13b18383d9bf"></a>Request Entity Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a9356882896ab4741a887a8550d76f383"><a name="a9356882896ab4741a887a8550d76f383"></a><a name="a9356882896ab4741a887a8550d76f383"></a>The server is refusing to process a request because the request entity is too large for the server to process. The server may close the connection to prevent the client from continuing the request. If the server is only temporarily unable to process the request, the response will contain a <strong id="b8494111232411"><a name="b8494111232411"></a><a name="b8494111232411"></a>Retry-After</strong> header field.</p>
</td>
</tr>
<tr id="r783ca91dcbd642e9a5155bfbe6422cc9"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a9926ea4e60f64a9ea79efcd94f443686"><a name="a9926ea4e60f64a9ea79efcd94f443686"></a><a name="a9926ea4e60f64a9ea79efcd94f443686"></a>414</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="adf527081905143e389fad95e4d1e984b"><a name="adf527081905143e389fad95e4d1e984b"></a><a name="adf527081905143e389fad95e4d1e984b"></a>Request-URI Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a937ac6280ef54e6f9eacdf0456d8a68a"><a name="a937ac6280ef54e6f9eacdf0456d8a68a"></a><a name="a937ac6280ef54e6f9eacdf0456d8a68a"></a>The Request-URI is too long for the server to process.</p>
</td>
</tr>
<tr id="r57b4dd50a698481aba6e438c30523dac"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a8c11fa5a29314f1ca302f0eb1a8e277d"><a name="a8c11fa5a29314f1ca302f0eb1a8e277d"></a><a name="a8c11fa5a29314f1ca302f0eb1a8e277d"></a>415</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a9d6f6aae6b694726808f6416bc5453a7"><a name="a9d6f6aae6b694726808f6416bc5453a7"></a><a name="a9d6f6aae6b694726808f6416bc5453a7"></a>Unsupported Media Type</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aa81d47c885a846f183841aaf9eacce8e"><a name="aa81d47c885a846f183841aaf9eacce8e"></a><a name="aa81d47c885a846f183841aaf9eacce8e"></a>The server is unable to process the media format in the request.</p>
</td>
</tr>
<tr id="r264374a5d60c473c8ea643a43c035cc4"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a379feef831e444389f8ab69bee33b215"><a name="a379feef831e444389f8ab69bee33b215"></a><a name="a379feef831e444389f8ab69bee33b215"></a>416</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="aa3d258afa4a3475b83373bbe958e5e81"><a name="aa3d258afa4a3475b83373bbe958e5e81"></a><a name="aa3d258afa4a3475b83373bbe958e5e81"></a>Requested range not satisfiable</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="abb8fd626e8694f06a802ae6e39a247a7"><a name="abb8fd626e8694f06a802ae6e39a247a7"></a><a name="abb8fd626e8694f06a802ae6e39a247a7"></a>The requested range is invalid.</p>
</td>
</tr>
<tr id="refb11b28fb724d13b0a154301bd6ee68"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a758f0007de334bb99abbbede991cc915"><a name="a758f0007de334bb99abbbede991cc915"></a><a name="a758f0007de334bb99abbbede991cc915"></a>417</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a0f102f8197de4aeea2c1da2021609152"><a name="a0f102f8197de4aeea2c1da2021609152"></a><a name="a0f102f8197de4aeea2c1da2021609152"></a>Expectation Failed</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="af3ed2ad15e4541b3a5fa16d11b4adf6c"><a name="af3ed2ad15e4541b3a5fa16d11b4adf6c"></a><a name="af3ed2ad15e4541b3a5fa16d11b4adf6c"></a>The server has failed to meet the requirements of the <strong id="b14890224182814"><a name="b14890224182814"></a><a name="b14890224182814"></a>Expect</strong> request-header field.</p>
</td>
</tr>
<tr id="r2fb4848f52f347fc85fe79db6bfc8eaa"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a75ac0309980446f7b53dfb239ce27f65"><a name="a75ac0309980446f7b53dfb239ce27f65"></a><a name="a75ac0309980446f7b53dfb239ce27f65"></a>422</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a014363768c0043efba5cf977ab077887"><a name="a014363768c0043efba5cf977ab077887"></a><a name="a014363768c0043efba5cf977ab077887"></a>UnprocessableEntity</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a13dedd2195754b2baf8afdd24972834b"><a name="a13dedd2195754b2baf8afdd24972834b"></a><a name="a13dedd2195754b2baf8afdd24972834b"></a>The request is well-formed but is unable to be processed due to semantic errors. </p>
</td>
</tr>
<tr id="r293dd8e837ef44119a48b60c3a219eee"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a3517b9b513f44dad9379f781b9455e46"><a name="a3517b9b513f44dad9379f781b9455e46"></a><a name="a3517b9b513f44dad9379f781b9455e46"></a>429</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a590752cc681744bb9cf706e95c46ce2e"><a name="a590752cc681744bb9cf706e95c46ce2e"></a><a name="a590752cc681744bb9cf706e95c46ce2e"></a>TooManyRequests</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a2c76f245fc7b406db82948918b4ab83d"><a name="a2c76f245fc7b406db82948918b4ab83d"></a><a name="a2c76f245fc7b406db82948918b4ab83d"></a>The client has sent excessive number of requests to the server within a given time (exceeding the limit on the access frequency of the client), or the server has received an excessive number of requests within a given time (beyond its processing capability). In this case, the client should resend the request after the time specified in the <strong id="b1987730142919"><a name="b1987730142919"></a><a name="b1987730142919"></a>Retry-After</strong> header of the response has elapsed. </p>
</td>
</tr>
<tr id="r479f5b12efa14c5e968ce8bd45790b69"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a959e8c2b536541d0b98a85cf491e04ef"><a name="a959e8c2b536541d0b98a85cf491e04ef"></a><a name="a959e8c2b536541d0b98a85cf491e04ef"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a7f2ea84d1b4949c6b35030d720c3c6eb"><a name="a7f2ea84d1b4949c6b35030d720c3c6eb"></a><a name="a7f2ea84d1b4949c6b35030d720c3c6eb"></a>InternalServerError</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="aaf6f51c7596445fc998d5eaf00d04ed0"><a name="aaf6f51c7596445fc998d5eaf00d04ed0"></a><a name="aaf6f51c7596445fc998d5eaf00d04ed0"></a>The server is able to receive the request but unable to understand it.</p>
</td>
</tr>
<tr id="rd67e70242f2f4f029169ae588d39bb32"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a09a64366f498425ea245df920ea3d2c6"><a name="a09a64366f498425ea245df920ea3d2c6"></a><a name="a09a64366f498425ea245df920ea3d2c6"></a>501</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a1a6c46ce59b2497198d54219ddf5fa39"><a name="a1a6c46ce59b2497198d54219ddf5fa39"></a><a name="a1a6c46ce59b2497198d54219ddf5fa39"></a>Not Implemented</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a290caff8aebc46d28c9356eb1aef495a"><a name="a290caff8aebc46d28c9356eb1aef495a"></a><a name="a290caff8aebc46d28c9356eb1aef495a"></a>The server does not support the function required to fulfill the request.</p>
</td>
</tr>
<tr id="rd7158a9c76514dd18eedd3aee57b02a9"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a7b881d9816224af8988591f27a14b245"><a name="a7b881d9816224af8988591f27a14b245"></a><a name="a7b881d9816224af8988591f27a14b245"></a>502</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a6aa928969e2d44878079c8337c99ceac"><a name="a6aa928969e2d44878079c8337c99ceac"></a><a name="a6aa928969e2d44878079c8337c99ceac"></a>Bad Gateway</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a1e8cbe354f4c41c4883ba7fb79c4702c"><a name="a1e8cbe354f4c41c4883ba7fb79c4702c"></a><a name="a1e8cbe354f4c41c4883ba7fb79c4702c"></a>The server was acting as a gateway or proxy and received an invalid request from the remote server.</p>
</td>
</tr>
<tr id="r630780f841c744bcac72a935e4a8ae66"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0037324641_p313675162537"><a name="en-us_topic_0037324641_p313675162537"></a><a name="en-us_topic_0037324641_p313675162537"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="ac57749afb9d24b32ac02b2e19236d0e6"><a name="ac57749afb9d24b32ac02b2e19236d0e6"></a><a name="ac57749afb9d24b32ac02b2e19236d0e6"></a>ServiceUnavailable</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="afe155c784cba456da387fc11a34e157b"><a name="afe155c784cba456da387fc11a34e157b"></a><a name="afe155c784cba456da387fc11a34e157b"></a>The requested service is invalid.</p>
<p id="en-us_topic_0037324641_p166256162537"><a name="en-us_topic_0037324641_p166256162537"></a><a name="en-us_topic_0037324641_p166256162537"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="r744f055a9dc24b27ab59944fff3656cb"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="aa556406dd421474085fdff9925fca6d5"><a name="aa556406dd421474085fdff9925fca6d5"></a><a name="aa556406dd421474085fdff9925fca6d5"></a>504</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="aa55315835e8f4543ab514df9aeb8f573"><a name="aa55315835e8f4543ab514df9aeb8f573"></a><a name="aa55315835e8f4543ab514df9aeb8f573"></a>ServerTimeout</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="ac4a4cc1324a14e91bf7453912cc6b50e"><a name="ac4a4cc1324a14e91bf7453912cc6b50e"></a><a name="ac4a4cc1324a14e91bf7453912cc6b50e"></a>The request cannot be fulfilled within a given time. This status code is returned to the client only if the <strong id="b12187153764513"><a name="b12187153764513"></a><a name="b12187153764513"></a>Timeout</strong> parameter is specified in the request.</p>
</td>
</tr>
<tr id="rf67b6f8ac3cd4feca4a323f3fbef5f56"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="a58b7a64339e24750a1c472e33f1b3820"><a name="a58b7a64339e24750a1c472e33f1b3820"></a><a name="a58b7a64339e24750a1c472e33f1b3820"></a>505</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="abfad2a39532647538f5a113132e95c00"><a name="abfad2a39532647538f5a113132e95c00"></a><a name="abfad2a39532647538f5a113132e95c00"></a>HTTPS Version not supported</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.4.1.3 "><p id="a92026b374204427d954e8ae3e3b012b8"><a name="a92026b374204427d954e8ae3e3b012b8"></a><a name="a92026b374204427d954e8ae3e3b012b8"></a>The server does not support the HTTPS protocol version used in the request.</p>
</td>
</tr>
</tbody>
</table>

