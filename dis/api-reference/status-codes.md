# Status Codes<a name="dis_02_0022"></a>

A status code is an HTTPS response issued by DIS to indicate whether an API request has been successfully completed.

<a name="taf9f8a6088834dda8e32665ce7c84d6b"></a>
<table><thead align="left"><tr id="rf95d58bdebd344fe88befe2510e79f0b"><th class="cellrowborder" valign="top" width="14.469999999999999%" id="mcps1.1.4.1.1"><p id="ac9a6fa9217a34e5aace28b03e5c93fc4"><a name="ac9a6fa9217a34e5aace28b03e5c93fc4"></a><a name="ac9a6fa9217a34e5aace28b03e5c93fc4"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="25.56%" id="mcps1.1.4.1.2"><p id="a8e44676ca7a94b8a851bb49183b844af"><a name="a8e44676ca7a94b8a851bb49183b844af"></a><a name="a8e44676ca7a94b8a851bb49183b844af"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="59.97%" id="mcps1.1.4.1.3"><p id="aef1d25a29a7547c48bd5a74d3b006c6d"><a name="aef1d25a29a7547c48bd5a74d3b006c6d"></a><a name="aef1d25a29a7547c48bd5a74d3b006c6d"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r747c79762e3047099ca1de43328f90be"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a4bdd50dfd4a54df6a39775dcd821949d"><a name="a4bdd50dfd4a54df6a39775dcd821949d"></a><a name="a4bdd50dfd4a54df6a39775dcd821949d"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a65295cb79f254b559450a6c48ade6b9c"><a name="a65295cb79f254b559450a6c48ade6b9c"></a><a name="a65295cb79f254b559450a6c48ade6b9c"></a>Continue</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="aca2b95ab32d449aba6de06eda31c4f90"><a name="aca2b95ab32d449aba6de06eda31c4f90"></a><a name="aca2b95ab32d449aba6de06eda31c4f90"></a>The server has received the initial part of the request and the client should continue to send the remaining part.</p>
<p id="a6c51a1cb05e34478a1d033b011f81551"><a name="a6c51a1cb05e34478a1d033b011f81551"></a><a name="a6c51a1cb05e34478a1d033b011f81551"></a>It is issued on a provisional basis while request processing continues. It alerts the client to wait for a final response.</p>
</td>
</tr>
<tr id="rda47b369bf564fbe8b5885f0bb447540"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="aa65379260fd448bfa75af442d73a84fb"><a name="aa65379260fd448bfa75af442d73a84fb"></a><a name="aa65379260fd448bfa75af442d73a84fb"></a>101</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a23763fac1e5c411f9a94b06c86b7a878"><a name="a23763fac1e5c411f9a94b06c86b7a878"></a><a name="a23763fac1e5c411f9a94b06c86b7a878"></a>Switching Protocols</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="afc6995ef11994a18bc6ce883e4d9b9fc"><a name="afc6995ef11994a18bc6ce883e4d9b9fc"></a><a name="afc6995ef11994a18bc6ce883e4d9b9fc"></a>The requester has asked the server to switch protocols and the server has agreed to do so. The target protocol must be more advanced than the source protocol.</p>
<p id="ad2f82b477cd94d1fa6e6c6d9408b7dca"><a name="ad2f82b477cd94d1fa6e6c6d9408b7dca"></a><a name="ad2f82b477cd94d1fa6e6c6d9408b7dca"></a>For example, the current HTTP protocol is switched to a later version of HTTP.</p>
</td>
</tr>
<tr id="row60081890161212"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="p34794944161212"><a name="p34794944161212"></a><a name="p34794944161212"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="p66927054161212"><a name="p66927054161212"></a><a name="p66927054161212"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="p63796653161236"><a name="p63796653161236"></a><a name="p63796653161236"></a>The server has successfully processed the request.</p>
</td>
</tr>
<tr id="r4dfc69425e2d4da481727ac79c0c70e2"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a551816bb5ff2413f9c70185503e407ea"><a name="a551816bb5ff2413f9c70185503e407ea"></a><a name="a551816bb5ff2413f9c70185503e407ea"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a7353a6f9f2a24fb9a7a809c2b5b1736c"><a name="a7353a6f9f2a24fb9a7a809c2b5b1736c"></a><a name="a7353a6f9f2a24fb9a7a809c2b5b1736c"></a>Created</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a37a9b75ed932495399220f0cfe1f4ecc"><a name="a37a9b75ed932495399220f0cfe1f4ecc"></a><a name="a37a9b75ed932495399220f0cfe1f4ecc"></a>The request has been fulfilled, resulting in the creation of a new resource.</p>
</td>
</tr>
<tr id="r1f968f9012634457b5f7a79179123c88"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a89a8fa96b39a4878bc58842289a94ca8"><a name="a89a8fa96b39a4878bc58842289a94ca8"></a><a name="a89a8fa96b39a4878bc58842289a94ca8"></a>202</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a1105514e59bd420e85ef81d6d2dff6fa"><a name="a1105514e59bd420e85ef81d6d2dff6fa"></a><a name="a1105514e59bd420e85ef81d6d2dff6fa"></a>Accepted</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a7ea9c3242da14ec0a324739a50d9b0c5"><a name="a7ea9c3242da14ec0a324739a50d9b0c5"></a><a name="a7ea9c3242da14ec0a324739a50d9b0c5"></a>The request has been accepted for processing, but the processing has not been completed.</p>
</td>
</tr>
<tr id="r1d383d7e59ce4d799fff21fac378fa19"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a503ea728a0c94221b2236a9afc2eb807"><a name="a503ea728a0c94221b2236a9afc2eb807"></a><a name="a503ea728a0c94221b2236a9afc2eb807"></a>203</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="ab863e12f2285414797b69b6ef0698ad3"><a name="ab863e12f2285414797b69b6ef0698ad3"></a><a name="ab863e12f2285414797b69b6ef0698ad3"></a>Non-Authoritative Information</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a5f36df975499442e8661687067cd1ef1"><a name="a5f36df975499442e8661687067cd1ef1"></a><a name="a5f36df975499442e8661687067cd1ef1"></a>The server successfully processed the request, but is returning information that may be from another source.</p>
</td>
</tr>
<tr id="rc66c76180d0e4a5295138ba4a9e5b1b0"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="ae1a1d81cdf4c42f286d283e2d4f08aa4"><a name="ae1a1d81cdf4c42f286d283e2d4f08aa4"></a><a name="ae1a1d81cdf4c42f286d283e2d4f08aa4"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a8199685c57c6472c8569892e3c975d5d"><a name="a8199685c57c6472c8569892e3c975d5d"></a><a name="a8199685c57c6472c8569892e3c975d5d"></a>NoContent</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="ad3d8be4cda654d838e1fb6c3789658bc"><a name="ad3d8be4cda654d838e1fb6c3789658bc"></a><a name="ad3d8be4cda654d838e1fb6c3789658bc"></a>The server has successfully processed the request, but does not return any content.</p>
<p id="ad5b0167adee7468e9d4ae55694277435"><a name="ad5b0167adee7468e9d4ae55694277435"></a><a name="ad5b0167adee7468e9d4ae55694277435"></a>The status code is returned in response to an HTTPS OPTIONS request.</p>
</td>
</tr>
<tr id="r1e2ff8d26e2d4e9d9295e91e8be844d1"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a1df2195f12ea49e084a766b551058aa4"><a name="a1df2195f12ea49e084a766b551058aa4"></a><a name="a1df2195f12ea49e084a766b551058aa4"></a>205</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="aeb762b27779041499545fcb674581496"><a name="aeb762b27779041499545fcb674581496"></a><a name="aeb762b27779041499545fcb674581496"></a>Reset Content</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a0203d403b8724adc8a4f91d9d538c2db"><a name="a0203d403b8724adc8a4f91d9d538c2db"></a><a name="a0203d403b8724adc8a4f91d9d538c2db"></a>The server has successfully processed the request, but does not return any content. Unlike a 204 response, this response requires that the requester reset the content.</p>
</td>
</tr>
<tr id="r36722ffd1087412195fb5f3c15023e65"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a1ef6e929f6f049058edca92a18b8b8b8"><a name="a1ef6e929f6f049058edca92a18b8b8b8"></a><a name="a1ef6e929f6f049058edca92a18b8b8b8"></a>206</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="adba01eb079a643f4af559a36b1a9368d"><a name="adba01eb079a643f4af559a36b1a9368d"></a><a name="adba01eb079a643f4af559a36b1a9368d"></a>Partial Content</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0037324641_p813455162537"><a name="en-us_topic_0037324641_p813455162537"></a><a name="en-us_topic_0037324641_p813455162537"></a>The server has successfully processed a part of the GET request.</p>
</td>
</tr>
<tr id="rbd781bf50f5344f0b6df20ffb5a0d2c9"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="ac072c48184c34bd48a7f49b87690cf61"><a name="ac072c48184c34bd48a7f49b87690cf61"></a><a name="ac072c48184c34bd48a7f49b87690cf61"></a>300</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a3a5e56d95adb4977a8ab75c7a3150e81"><a name="a3a5e56d95adb4977a8ab75c7a3150e81"></a><a name="a3a5e56d95adb4977a8ab75c7a3150e81"></a>Multiple Choices</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="aa756d59fc6974b3cafa73f8b5e8f8141"><a name="aa756d59fc6974b3cafa73f8b5e8f8141"></a><a name="aa756d59fc6974b3cafa73f8b5e8f8141"></a>There are multiple options for the requested resource. For example, this code could be used to present a list of resource characteristics and addresses from which the client such as a browser may choose.</p>
</td>
</tr>
<tr id="rfe61ce734fc14a289a9af50683a55737"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a3a5f8dd35b804e0487a0e3ededc202e1"><a name="a3a5f8dd35b804e0487a0e3ededc202e1"></a><a name="a3a5f8dd35b804e0487a0e3ededc202e1"></a>301</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0037324641_p425112162537"><a name="en-us_topic_0037324641_p425112162537"></a><a name="en-us_topic_0037324641_p425112162537"></a>Moved Permanently</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a97b17283ff994999add2278c95040d52"><a name="a97b17283ff994999add2278c95040d52"></a><a name="a97b17283ff994999add2278c95040d52"></a>This and all future requests should be permanently directed to the given URI indicated in this response.</p>
</td>
</tr>
<tr id="r85062c96396c4e89a131ec3f90b39681"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a84b97c97226540138feb9bfbc338b3a0"><a name="a84b97c97226540138feb9bfbc338b3a0"></a><a name="a84b97c97226540138feb9bfbc338b3a0"></a>302</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a2a2abedf0763459fb3b7cad0d2a59ac7"><a name="a2a2abedf0763459fb3b7cad0d2a59ac7"></a><a name="a2a2abedf0763459fb3b7cad0d2a59ac7"></a>Found</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a83819bbdff98446abc33012d31d38c9a"><a name="a83819bbdff98446abc33012d31d38c9a"></a><a name="a83819bbdff98446abc33012d31d38c9a"></a>The requested resource was temporarily moved.</p>
</td>
</tr>
<tr id="r52af6b2a78f24672bc6254309377c078"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="abe96558cf830436a9fc3a864b801349c"><a name="abe96558cf830436a9fc3a864b801349c"></a><a name="abe96558cf830436a9fc3a864b801349c"></a>303</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a9d5791c37ee140969c82a354cb635fcb"><a name="a9d5791c37ee140969c82a354cb635fcb"></a><a name="a9d5791c37ee140969c82a354cb635fcb"></a>See Other</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a61a3164be0854ab0987cc2591a1fe619"><a name="a61a3164be0854ab0987cc2591a1fe619"></a><a name="a61a3164be0854ab0987cc2591a1fe619"></a>The response to the request can be found under another URI using a GET or POST method.</p>
</td>
</tr>
<tr id="r024a9ba3a46f431689ef7baead1921b3"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="abfe4b40c0ffb473086f8657ffca44972"><a name="abfe4b40c0ffb473086f8657ffca44972"></a><a name="abfe4b40c0ffb473086f8657ffca44972"></a>304</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a99d6f6df45c646aa9d2d7ec290bdc06b"><a name="a99d6f6df45c646aa9d2d7ec290bdc06b"></a><a name="a99d6f6df45c646aa9d2d7ec290bdc06b"></a>Not Modified</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a22b284adc6354cfdb8bc30f6ed7a7539"><a name="a22b284adc6354cfdb8bc30f6ed7a7539"></a><a name="a22b284adc6354cfdb8bc30f6ed7a7539"></a>The requested resource has not been modified. In such a case, there is no need to retransmit the resource since the client still has a previously-downloaded copy.</p>
</td>
</tr>
<tr id="r73d20f5056d642b098e0b6a788c7a68f"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a4250b3d397d74bc69a39c7119433582c"><a name="a4250b3d397d74bc69a39c7119433582c"></a><a name="a4250b3d397d74bc69a39c7119433582c"></a>305</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a5f545b5c3044497890fc8c77bb76d19f"><a name="a5f545b5c3044497890fc8c77bb76d19f"></a><a name="a5f545b5c3044497890fc8c77bb76d19f"></a>Use Proxy</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="ab883338804e649f4a1f2974482a562d7"><a name="ab883338804e649f4a1f2974482a562d7"></a><a name="ab883338804e649f4a1f2974482a562d7"></a>The requested resource is available only through a proxy.</p>
</td>
</tr>
<tr id="re62340d9872b41cab34168340b92a62d"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a402eb8e193d34c2eb24ff9e10cbe92b0"><a name="a402eb8e193d34c2eb24ff9e10cbe92b0"></a><a name="a402eb8e193d34c2eb24ff9e10cbe92b0"></a>306</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a485e350e9a41460296a7d553c582ba1a"><a name="a485e350e9a41460296a7d553c582ba1a"></a><a name="a485e350e9a41460296a7d553c582ba1a"></a>Unused</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a8255119086674a03a36bb08191ac4b35"><a name="a8255119086674a03a36bb08191ac4b35"></a><a name="a8255119086674a03a36bb08191ac4b35"></a>This HTTP status code is no longer used.</p>
</td>
</tr>
<tr id="r07b56c4524024267955fd0045918f11f"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a9195a4dfd5b44aad9a2e06efb3a8aabd"><a name="a9195a4dfd5b44aad9a2e06efb3a8aabd"></a><a name="a9195a4dfd5b44aad9a2e06efb3a8aabd"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="ad780e34fc217491eaad4e5849850e31d"><a name="ad780e34fc217491eaad4e5849850e31d"></a><a name="ad780e34fc217491eaad4e5849850e31d"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="ad8820ab2810341f89887df5a79bdd7b9"><a name="ad8820ab2810341f89887df5a79bdd7b9"></a><a name="ad8820ab2810341f89887df5a79bdd7b9"></a>The request is invalid.</p>
<p id="a0cdc0b290d8d4be7bc4cc9466fd39a74"><a name="a0cdc0b290d8d4be7bc4cc9466fd39a74"></a><a name="a0cdc0b290d8d4be7bc4cc9466fd39a74"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="rb90c73d56bb245f28f9834fc4c6ed6dc"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a1e713e6ad6654da8a401aca0d9f0b070"><a name="a1e713e6ad6654da8a401aca0d9f0b070"></a><a name="a1e713e6ad6654da8a401aca0d9f0b070"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="aabb070e76e9d467eba87a3366affcb0a"><a name="aabb070e76e9d467eba87a3366affcb0a"></a><a name="aabb070e76e9d467eba87a3366affcb0a"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a8afa37cf876a4f97b6bfa2fad76b078d"><a name="a8afa37cf876a4f97b6bfa2fad76b078d"></a><a name="a8afa37cf876a4f97b6bfa2fad76b078d"></a>The authentication information provided by the client is incorrect or invalid.</p>
</td>
</tr>
<tr id="r1e32089cb4f9455499a01e76d5ee204a"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a9b3e643721c146d79351a1110ecf41a2"><a name="a9b3e643721c146d79351a1110ecf41a2"></a><a name="a9b3e643721c146d79351a1110ecf41a2"></a>402</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a8e62da471e5648ab81352df656083d58"><a name="a8e62da471e5648ab81352df656083d58"></a><a name="a8e62da471e5648ab81352df656083d58"></a>Payment Required</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a993bb8c99ac74db6a9c1f6d35df70fbd"><a name="a993bb8c99ac74db6a9c1f6d35df70fbd"></a><a name="a993bb8c99ac74db6a9c1f6d35df70fbd"></a>Reserved for future use.</p>
</td>
</tr>
<tr id="r0a8d55acffcf4ae3b6149d52b0dafdc9"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="ab6f4ffff2c8a4984b820f518d4a2281f"><a name="ab6f4ffff2c8a4984b820f518d4a2281f"></a><a name="ab6f4ffff2c8a4984b820f518d4a2281f"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a5578bb537c13478eb5a04889a492c806"><a name="a5578bb537c13478eb5a04889a492c806"></a><a name="a5578bb537c13478eb5a04889a492c806"></a>Forbidden</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="af5945d1c926c4c30b8c1b0a82772b711"><a name="af5945d1c926c4c30b8c1b0a82772b711"></a><a name="af5945d1c926c4c30b8c1b0a82772b711"></a>The server has received the request and understood it, but the server is refusing to respond to it.</p>
<p id="a9a9e6610a9df41d6922ab673e0256a77"><a name="a9a9e6610a9df41d6922ab673e0256a77"></a><a name="a9a9e6610a9df41d6922ab673e0256a77"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="r425c11a0907e495bb027022e2de5d374"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a6dc391900b5b4847938a487417aa8c93"><a name="a6dc391900b5b4847938a487417aa8c93"></a><a name="a6dc391900b5b4847938a487417aa8c93"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a87d3ad3755e24923a79e284c157463ac"><a name="a87d3ad3755e24923a79e284c157463ac"></a><a name="a87d3ad3755e24923a79e284c157463ac"></a>NotFound</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="af6abcf49ca7143ebaa58a710fdaca492"><a name="af6abcf49ca7143ebaa58a710fdaca492"></a><a name="af6abcf49ca7143ebaa58a710fdaca492"></a>The requested resource could not be found.</p>
<p id="ab3a503aa32494b9e8a5fb16d18c6686c"><a name="ab3a503aa32494b9e8a5fb16d18c6686c"></a><a name="ab3a503aa32494b9e8a5fb16d18c6686c"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="r6052897dcfe84edcb351fabccc307dc4"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a81d09efa514b4a339cf39e0646f659d0"><a name="a81d09efa514b4a339cf39e0646f659d0"></a><a name="a81d09efa514b4a339cf39e0646f659d0"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a6a297b7884214830976821ea813f844b"><a name="a6a297b7884214830976821ea813f844b"></a><a name="a6a297b7884214830976821ea813f844b"></a>MethodNotAllowed</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a35113661e6b548ad8d17b731890552e8"><a name="a35113661e6b548ad8d17b731890552e8"></a><a name="a35113661e6b548ad8d17b731890552e8"></a>A request method is not supported for the requested resource.</p>
<p id="a99fe886e926045d9872e22bc61bcbf5f"><a name="a99fe886e926045d9872e22bc61bcbf5f"></a><a name="a99fe886e926045d9872e22bc61bcbf5f"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="r1dfac6a1561f4533963f2ee28cdd08c3"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a595c1f86685048309ec9282860acdbdd"><a name="a595c1f86685048309ec9282860acdbdd"></a><a name="a595c1f86685048309ec9282860acdbdd"></a>406</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a43a2d181147643cbaa166c61d35f5b74"><a name="a43a2d181147643cbaa166c61d35f5b74"></a><a name="a43a2d181147643cbaa166c61d35f5b74"></a>Not Acceptable</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a93dee349f5504d77b43bb658c506452a"><a name="a93dee349f5504d77b43bb658c506452a"></a><a name="a93dee349f5504d77b43bb658c506452a"></a>The server could not fulfill the request according to the content characteristics of the request.</p>
</td>
</tr>
<tr id="r398b11ea63a14532b175abc0e48b4243"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a071d28ad94734d8690866658de5d18ef"><a name="a071d28ad94734d8690866658de5d18ef"></a><a name="a071d28ad94734d8690866658de5d18ef"></a>407</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="ad8c4486720934bf1863bc17734cab37b"><a name="ad8c4486720934bf1863bc17734cab37b"></a><a name="ad8c4486720934bf1863bc17734cab37b"></a>Proxy Authentication Required</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a690f6ceda3d1407f8052576802f31e69"><a name="a690f6ceda3d1407f8052576802f31e69"></a><a name="a690f6ceda3d1407f8052576802f31e69"></a>This code is similar to 401, but indicates that the client must first authenticate itself with the proxy.</p>
</td>
</tr>
<tr id="r9055946522a94071978ba28cbf296fcf"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a6614102423994522ab9c5bb0a93e104a"><a name="a6614102423994522ab9c5bb0a93e104a"></a><a name="a6614102423994522ab9c5bb0a93e104a"></a>408</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a454144ece267474582c79a9144cd0892"><a name="a454144ece267474582c79a9144cd0892"></a><a name="a454144ece267474582c79a9144cd0892"></a>Request Time-out</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="ae76a4723e5424780ae928345b16efe77"><a name="ae76a4723e5424780ae928345b16efe77"></a><a name="ae76a4723e5424780ae928345b16efe77"></a>The server timed out waiting for the request.</p>
<p id="ae54f8a3008c64d4280756b18f31abcda"><a name="ae54f8a3008c64d4280756b18f31abcda"></a><a name="ae54f8a3008c64d4280756b18f31abcda"></a>The client may re-initiate the request without modifications at any later time.</p>
</td>
</tr>
<tr id="r63aecfc4eace445bb648872c599d1a12"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a63008f292ba24ad5ba86155511b28abd"><a name="a63008f292ba24ad5ba86155511b28abd"></a><a name="a63008f292ba24ad5ba86155511b28abd"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a6d515cb644c14da887a6895bec0ddcb6"><a name="a6d515cb644c14da887a6895bec0ddcb6"></a><a name="a6d515cb644c14da887a6895bec0ddcb6"></a>Conflict</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="aa34871cf779e43a7ab41423d5df2dc12"><a name="aa34871cf779e43a7ab41423d5df2dc12"></a><a name="aa34871cf779e43a7ab41423d5df2dc12"></a>The request could not be processed due to a conflict in the request.</p>
<p id="acae6c8fe48854af4abaf4e0d0ebfed4c"><a name="acae6c8fe48854af4abaf4e0d0ebfed4c"></a><a name="acae6c8fe48854af4abaf4e0d0ebfed4c"></a>For example, an edit conflict between multiple simultaneous updates or the resource that the client attempts to create already exists.</p>
</td>
</tr>
<tr id="rf988ca1bcbd241c888aec3cbcf8d351c"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a00fb6b2bcdc84f9181fbc2ff067f69bd"><a name="a00fb6b2bcdc84f9181fbc2ff067f69bd"></a><a name="a00fb6b2bcdc84f9181fbc2ff067f69bd"></a>410</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a96fa258e7a594cf4b0368d025874aad2"><a name="a96fa258e7a594cf4b0368d025874aad2"></a><a name="a96fa258e7a594cf4b0368d025874aad2"></a>Gone</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a0f51914b3a394977b43f74033862ee0b"><a name="a0f51914b3a394977b43f74033862ee0b"></a><a name="a0f51914b3a394977b43f74033862ee0b"></a>The requested resource has been deleted permanently and will not be available again.</p>
<p id="a3f5e679bc1e34e778416ec28ccb31f46"><a name="a3f5e679bc1e34e778416ec28ccb31f46"></a><a name="a3f5e679bc1e34e778416ec28ccb31f46"></a>The status code indicates that the requested resource has been deleted permanently.</p>
</td>
</tr>
<tr id="ra056058b044b4e228b1dee966993e591"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a14513fe6544c40b4a7535178d6c33626"><a name="a14513fe6544c40b4a7535178d6c33626"></a><a name="a14513fe6544c40b4a7535178d6c33626"></a>411</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a0cd35affb83044958478dd089087b794"><a name="a0cd35affb83044958478dd089087b794"></a><a name="a0cd35affb83044958478dd089087b794"></a>Length Required</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="ad1ed5731f65146cba3f3ce25e802cf6a"><a name="ad1ed5731f65146cba3f3ce25e802cf6a"></a><a name="ad1ed5731f65146cba3f3ce25e802cf6a"></a>The server refused to process the request because the request does not specify the length of its content.</p>
</td>
</tr>
<tr id="r00964069da0f45b8a684e893b4ffb77a"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="ad72736e850414a87b4cacb960c8b20a3"><a name="ad72736e850414a87b4cacb960c8b20a3"></a><a name="ad72736e850414a87b4cacb960c8b20a3"></a>412</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a8e98b261ea644f1f8baf976f27e7e71c"><a name="a8e98b261ea644f1f8baf976f27e7e71c"></a><a name="a8e98b261ea644f1f8baf976f27e7e71c"></a>Precondition Failed</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="ad26391c25a994f6b9287058a365c3333"><a name="ad26391c25a994f6b9287058a365c3333"></a><a name="ad26391c25a994f6b9287058a365c3333"></a>The server does not meet one of the preconditions that the requester puts on the request.</p>
</td>
</tr>
<tr id="r6df890fb1b634fa3870a43d083529b95"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="ad32a6d092f0b4ffdaa7447cdb6328948"><a name="ad32a6d092f0b4ffdaa7447cdb6328948"></a><a name="ad32a6d092f0b4ffdaa7447cdb6328948"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="aa3d29646e6c2476e9271265e5c51df7a"><a name="aa3d29646e6c2476e9271265e5c51df7a"></a><a name="aa3d29646e6c2476e9271265e5c51df7a"></a>Request Entity Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a071dd8a8ed884d6f97bb7dddf13a910e"><a name="a071dd8a8ed884d6f97bb7dddf13a910e"></a><a name="a071dd8a8ed884d6f97bb7dddf13a910e"></a>The request is larger than the server is willing or able to process. The server may close the connection to prevent the client from continuing the request. If the server temporarily cannot process the request, the response will contain a Retry-After header field.</p>
</td>
</tr>
<tr id="r05e6f8fff821444796fd56e92290e805"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a7e822d4719ef40a98c70de541cf793dc"><a name="a7e822d4719ef40a98c70de541cf793dc"></a><a name="a7e822d4719ef40a98c70de541cf793dc"></a>414</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a4e9f0e70801d4ca68d4e894906b29107"><a name="a4e9f0e70801d4ca68d4e894906b29107"></a><a name="a4e9f0e70801d4ca68d4e894906b29107"></a>Request-URI Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="ad9f837a33fb0405e9e0e5502fcb64b4a"><a name="ad9f837a33fb0405e9e0e5502fcb64b4a"></a><a name="ad9f837a33fb0405e9e0e5502fcb64b4a"></a>The URI provided was too long for the server to process.</p>
</td>
</tr>
<tr id="r38d861da868145f6b2397cbd700b37f4"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a9eecdeaf99b04d70abfa3c4a2dd205d0"><a name="a9eecdeaf99b04d70abfa3c4a2dd205d0"></a><a name="a9eecdeaf99b04d70abfa3c4a2dd205d0"></a>415</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="aaee7175204844df092c08b06bcb5a796"><a name="aaee7175204844df092c08b06bcb5a796"></a><a name="aaee7175204844df092c08b06bcb5a796"></a>Unsupported Media Type</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a3256b588a5564bffa890a8ded265ce49"><a name="a3256b588a5564bffa890a8ded265ce49"></a><a name="a3256b588a5564bffa890a8ded265ce49"></a>The server does not support the media type in the request.</p>
</td>
</tr>
<tr id="r5ac83bcd20e0441aa63131eabf09146a"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a915f52e55b4442499b43fa7202dbd3dc"><a name="a915f52e55b4442499b43fa7202dbd3dc"></a><a name="a915f52e55b4442499b43fa7202dbd3dc"></a>416</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="ad6374a691bff4bc7b83d809c6ae6a96c"><a name="ad6374a691bff4bc7b83d809c6ae6a96c"></a><a name="ad6374a691bff4bc7b83d809c6ae6a96c"></a>Requested range not satisfiable</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a5f6fc5b242584a0dbe6c1d684a2aab9e"><a name="a5f6fc5b242584a0dbe6c1d684a2aab9e"></a><a name="a5f6fc5b242584a0dbe6c1d684a2aab9e"></a>The requested range is invalid.</p>
</td>
</tr>
<tr id="rf348028cb9c94d0b95f21079dcb23b7c"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a07c303660a874311b2dc653ec29a2edd"><a name="a07c303660a874311b2dc653ec29a2edd"></a><a name="a07c303660a874311b2dc653ec29a2edd"></a>417</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="ad954afa69d574e269f9698bb06ae1070"><a name="ad954afa69d574e269f9698bb06ae1070"></a><a name="ad954afa69d574e269f9698bb06ae1070"></a>Expectation Failed</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a6225f24cce8f4efb95b92396925f4d43"><a name="a6225f24cce8f4efb95b92396925f4d43"></a><a name="a6225f24cce8f4efb95b92396925f4d43"></a>The server fails to meet the requirements of the Expect request-header field.</p>
</td>
</tr>
<tr id="rc04930b5ecb140a68d35a53ae75cd6f0"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="ae434248f76224f068e4d50762591b290"><a name="ae434248f76224f068e4d50762591b290"></a><a name="ae434248f76224f068e4d50762591b290"></a>422</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="ab3cc1251cc2542398c7b7bd2821deb42"><a name="ab3cc1251cc2542398c7b7bd2821deb42"></a><a name="ab3cc1251cc2542398c7b7bd2821deb42"></a>UnprocessableEntity</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a5f9b322bd5f848fc91eda2bed3ae9991"><a name="a5f9b322bd5f848fc91eda2bed3ae9991"></a><a name="a5f9b322bd5f848fc91eda2bed3ae9991"></a>The request was well-formed but was unable to be followed due to semantic errors.</p>
</td>
</tr>
<tr id="rc7cd0beef14a42efbecbd0b0ebad450a"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a56dab92ef9a84e8c9722dc4f8216c693"><a name="a56dab92ef9a84e8c9722dc4f8216c693"></a><a name="a56dab92ef9a84e8c9722dc4f8216c693"></a>429</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a24d4093485fd44b0953b4ab5500f0962"><a name="a24d4093485fd44b0953b4ab5500f0962"></a><a name="a24d4093485fd44b0953b4ab5500f0962"></a>TooManyRequests</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="afe34150b692a44c4a970f6ee11984cc2"><a name="afe34150b692a44c4a970f6ee11984cc2"></a><a name="afe34150b692a44c4a970f6ee11984cc2"></a>The client has sent more requests than its rate limit is allowed within a given amount of time, or the server has received more requests than it is able to process within a given amount of time. In this case, it is advisable for the client to re-initiate requests after the time specified in the Retry-After header of the response expires.</p>
</td>
</tr>
<tr id="row06301931182817"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="p063017316285"><a name="p063017316285"></a><a name="p063017316285"></a>441</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="p19116333153015"><a name="p19116333153015"></a><a name="p19116333153015"></a>Authentication Error</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="p1563014317287"><a name="p1563014317287"></a><a name="p1563014317287"></a>Authentication fails.</p>
</td>
</tr>
<tr id="r41d1e8c2253948eaa0650dc89febb1cf"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="aad2a8d8f354943ef871c598f38916167"><a name="aad2a8d8f354943ef871c598f38916167"></a><a name="aad2a8d8f354943ef871c598f38916167"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="ae9f934e133274754817301869fbd2721"><a name="ae9f934e133274754817301869fbd2721"></a><a name="ae9f934e133274754817301869fbd2721"></a>InternalServerError</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="acb56cc5bb4154c2da8ba39d9f01e79ce"><a name="acb56cc5bb4154c2da8ba39d9f01e79ce"></a><a name="acb56cc5bb4154c2da8ba39d9f01e79ce"></a>The server is able to receive the request but it could not understand the request.</p>
</td>
</tr>
<tr id="r52cf80f1e781491fa7916228f48bf62f"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="ae4f4686ec08b4d69bf6bec3483757c8f"><a name="ae4f4686ec08b4d69bf6bec3483757c8f"></a><a name="ae4f4686ec08b4d69bf6bec3483757c8f"></a>501</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="afdef08f9ecb64e51a2269527271dc852"><a name="afdef08f9ecb64e51a2269527271dc852"></a><a name="afdef08f9ecb64e51a2269527271dc852"></a>Not Implemented</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="abe8eff64fe064814a17387c2d7fd3931"><a name="abe8eff64fe064814a17387c2d7fd3931"></a><a name="abe8eff64fe064814a17387c2d7fd3931"></a>The server does not support the requested function.</p>
</td>
</tr>
<tr id="r163f7a3bcbb444b3a30239311e82ab3e"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="aafe3c72106b44f94b9c155d1bcb13206"><a name="aafe3c72106b44f94b9c155d1bcb13206"></a><a name="aafe3c72106b44f94b9c155d1bcb13206"></a>502</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a4955e9621ae24de4a8ebeb7a24e0aa25"><a name="a4955e9621ae24de4a8ebeb7a24e0aa25"></a><a name="a4955e9621ae24de4a8ebeb7a24e0aa25"></a>Bad Gateway</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a2b7a4d8cfee04f1e83122a292c8569af"><a name="a2b7a4d8cfee04f1e83122a292c8569af"></a><a name="a2b7a4d8cfee04f1e83122a292c8569af"></a>The server was acting as a gateway or proxy and received an invalid request from a remote server.</p>
</td>
</tr>
<tr id="r7fa9d06db5f44763bae08e58c225e67a"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0037324641_p313675162537"><a name="en-us_topic_0037324641_p313675162537"></a><a name="en-us_topic_0037324641_p313675162537"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="aadbef27e0bea498eb2e0ea0c0e82e1e1"><a name="aadbef27e0bea498eb2e0ea0c0e82e1e1"></a><a name="aadbef27e0bea498eb2e0ea0c0e82e1e1"></a>ServiceUnavailable</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a2175a4d692d141b2af83332f27eb5e49"><a name="a2175a4d692d141b2af83332f27eb5e49"></a><a name="a2175a4d692d141b2af83332f27eb5e49"></a>The requested service is invalid.</p>
<p id="en-us_topic_0037324641_p166256162537"><a name="en-us_topic_0037324641_p166256162537"></a><a name="en-us_topic_0037324641_p166256162537"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="re7436f7aa99946cebad6877a4e5088cd"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="a46b2b1758461476dbf4e3b65e3bd2dfc"><a name="a46b2b1758461476dbf4e3b65e3bd2dfc"></a><a name="a46b2b1758461476dbf4e3b65e3bd2dfc"></a>504</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="a1e2fc20b7afe41a980cdb3c196f937bf"><a name="a1e2fc20b7afe41a980cdb3c196f937bf"></a><a name="a1e2fc20b7afe41a980cdb3c196f937bf"></a>ServerTimeout</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="ac9b931941ee2493bae9fc6cb82fef73c"><a name="ac9b931941ee2493bae9fc6cb82fef73c"></a><a name="ac9b931941ee2493bae9fc6cb82fef73c"></a>The server could not return a timely response. The response will reach the client only if the request carries a timeout parameter.</p>
</td>
</tr>
<tr id="rcef6a18e552c4e57ac6fa10f84c8f0cb"><td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.1.4.1.1 "><p id="adba437c4b9534472b3187cca39c80112"><a name="adba437c4b9534472b3187cca39c80112"></a><a name="adba437c4b9534472b3187cca39c80112"></a>505</p>
</td>
<td class="cellrowborder" valign="top" width="25.56%" headers="mcps1.1.4.1.2 "><p id="aa4c2cd6f76d24a489db00f5c357a3b67"><a name="aa4c2cd6f76d24a489db00f5c357a3b67"></a><a name="aa4c2cd6f76d24a489db00f5c357a3b67"></a>HTTP Version not supported</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.1.4.1.3 "><p id="a6a7d5f3a8374482381893378336cb39d"><a name="a6a7d5f3a8374482381893378336cb39d"></a><a name="a6a7d5f3a8374482381893378336cb39d"></a>The server does not support the HTTP protocol version used in the request.</p>
</td>
</tr>
</tbody>
</table>

