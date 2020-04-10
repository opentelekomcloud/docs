# Status Code<a name="dws_02_0038"></a>

[Table 1](#t086f984f5caa4d1da9258d7d871e1e62)  describes the status code.

**Table  1**  Status code

<a name="t086f984f5caa4d1da9258d7d871e1e62"></a>
<table><thead align="left"><tr id="r162a4f76e44b4cc0a00e22073652ead3"><th class="cellrowborder" valign="top" width="13.530000000000001%" id="mcps1.2.4.1.1"><p id="aada45cfe054243abbbf98d2205eac9cd"><a name="aada45cfe054243abbbf98d2205eac9cd"></a><a name="aada45cfe054243abbbf98d2205eac9cd"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="26.5%" id="mcps1.2.4.1.2"><p id="a4461c3b635d0427aaf6127094c8e24a4"><a name="a4461c3b635d0427aaf6127094c8e24a4"></a><a name="a4461c3b635d0427aaf6127094c8e24a4"></a>Code</p>
</th>
<th class="cellrowborder" valign="top" width="59.97%" id="mcps1.2.4.1.3"><p id="aa68b0f2f89cb40f480bb177bf33af24a"><a name="aa68b0f2f89cb40f480bb177bf33af24a"></a><a name="aa68b0f2f89cb40f480bb177bf33af24a"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r0a8b062685a6456ab1bdec32442f4e5c"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a40c35adc1f1244759283ea52bd4d7e55"><a name="a40c35adc1f1244759283ea52bd4d7e55"></a><a name="a40c35adc1f1244759283ea52bd4d7e55"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a87089e11bd1d409eaebd7e3b902d3ff6"><a name="a87089e11bd1d409eaebd7e3b902d3ff6"></a><a name="a87089e11bd1d409eaebd7e3b902d3ff6"></a>Continue</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="ad756d34df6ec49228b271c85154ff0b7"><a name="ad756d34df6ec49228b271c85154ff0b7"></a><a name="ad756d34df6ec49228b271c85154ff0b7"></a>The client continues sending the request.</p>
<p id="a6ba98d5024c2455cb4f24d4b89bff89a"><a name="a6ba98d5024c2455cb4f24d4b89bff89a"></a><a name="a6ba98d5024c2455cb4f24d4b89bff89a"></a>This interim response is used to inform the client that the initial part of the request has been received and has not yet been rejected by the server.</p>
</td>
</tr>
<tr id="re99892cd19574010a88913dacf3e24c9"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a7a0315214e5d4ad6823958f4967c3dd2"><a name="a7a0315214e5d4ad6823958f4967c3dd2"></a><a name="a7a0315214e5d4ad6823958f4967c3dd2"></a>101</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a49652d390054445687da1712a2baa086"><a name="a49652d390054445687da1712a2baa086"></a><a name="a49652d390054445687da1712a2baa086"></a>Switching Protocols</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a0827f66487194ce09177ac6ca701ef8b"><a name="a0827f66487194ce09177ac6ca701ef8b"></a><a name="a0827f66487194ce09177ac6ca701ef8b"></a>Switching protocols. The target protocol must be more advanced than the source protocol.</p>
<p id="a1dc018f65502431bb72d7259bd37f78d"><a name="a1dc018f65502431bb72d7259bd37f78d"></a><a name="a1dc018f65502431bb72d7259bd37f78d"></a>For example, the current HTTP protocol is switched to a later version.</p>
</td>
</tr>
<tr id="r6785af6943e8456f85957a2b1a6fe2c6"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="aaf03595d336147519822581628825b2a"><a name="aaf03595d336147519822581628825b2a"></a><a name="aaf03595d336147519822581628825b2a"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a8a098258f2d345a6bd5bcecb87054c96"><a name="a8a098258f2d345a6bd5bcecb87054c96"></a><a name="a8a098258f2d345a6bd5bcecb87054c96"></a>Created</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a890f4eee57e7457ea4f59401efcad8f5"><a name="a890f4eee57e7457ea4f59401efcad8f5"></a><a name="a890f4eee57e7457ea4f59401efcad8f5"></a>The request for creating a resource has been fulfilled. </p>
</td>
</tr>
<tr id="r4c76d286d93b4d829aad85050c2ce0a2"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="ae89d384200864adaab424994a0dba4fe"><a name="ae89d384200864adaab424994a0dba4fe"></a><a name="ae89d384200864adaab424994a0dba4fe"></a>202</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="ac5c040025f7e4c52892fffaf2330ef9b"><a name="ac5c040025f7e4c52892fffaf2330ef9b"></a><a name="ac5c040025f7e4c52892fffaf2330ef9b"></a>Accepted</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a3ae2e34a7e4d423e8a7603810173f42b"><a name="a3ae2e34a7e4d423e8a7603810173f42b"></a><a name="a3ae2e34a7e4d423e8a7603810173f42b"></a>The request has been accepted, but the processing has not been completed.</p>
</td>
</tr>
<tr id="ra85f84d4df60497dae3e33a6fe59408c"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a96a5ac545a8041f3bf81428b40262b85"><a name="a96a5ac545a8041f3bf81428b40262b85"></a><a name="a96a5ac545a8041f3bf81428b40262b85"></a>203</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a01ddb3f004e542df9a9d237a19ca175b"><a name="a01ddb3f004e542df9a9d237a19ca175b"></a><a name="a01ddb3f004e542df9a9d237a19ca175b"></a>Non-Authoritative Information</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="ad73d6bd874084e36b8bb0169719b08f9"><a name="ad73d6bd874084e36b8bb0169719b08f9"></a><a name="ad73d6bd874084e36b8bb0169719b08f9"></a>The server successfully processed the request, but is returning information that may be from another source.</p>
</td>
</tr>
<tr id="r7cdb00bdce894c2ebc3d9c9de65d1c29"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a5414f6f3cec54efaa3c1a385f0e6f53d"><a name="a5414f6f3cec54efaa3c1a385f0e6f53d"></a><a name="a5414f6f3cec54efaa3c1a385f0e6f53d"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="aa9094f36b12840c1ada623743108ef69"><a name="aa9094f36b12840c1ada623743108ef69"></a><a name="aa9094f36b12840c1ada623743108ef69"></a>NoContent</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a6d23edbb093145c3a9ac52aff158033c"><a name="a6d23edbb093145c3a9ac52aff158033c"></a><a name="a6d23edbb093145c3a9ac52aff158033c"></a>The server has successfully processed the request, but has not returned any content.</p>
<p id="a2f221c2bc8f740b1aace4517bcab6e6f"><a name="a2f221c2bc8f740b1aace4517bcab6e6f"></a><a name="a2f221c2bc8f740b1aace4517bcab6e6f"></a>The status code is returned in response to an HTTP OPTIONS request.</p>
</td>
</tr>
<tr id="r2b19455d5595444eb35eb1867be36cb6"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a73981ec970124b6795617426a1660858"><a name="a73981ec970124b6795617426a1660858"></a><a name="a73981ec970124b6795617426a1660858"></a>205</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="abd6f5e573b1743de8976f2a00fa2465a"><a name="abd6f5e573b1743de8976f2a00fa2465a"></a><a name="abd6f5e573b1743de8976f2a00fa2465a"></a>Reset Content</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a78a369c844b144feb369e6792dac8c16"><a name="a78a369c844b144feb369e6792dac8c16"></a><a name="a78a369c844b144feb369e6792dac8c16"></a>The server has fulfilled the request, but the requester is required to reset the content.</p>
</td>
</tr>
<tr id="rbbc8c417611b4b7d9d046ed87323dc19"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="abf2250a9e8024c488cd6a159abd0d80e"><a name="abf2250a9e8024c488cd6a159abd0d80e"></a><a name="abf2250a9e8024c488cd6a159abd0d80e"></a>206</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="ad0db868d7b0b47c1bc1930bec0a8cfbe"><a name="ad0db868d7b0b47c1bc1930bec0a8cfbe"></a><a name="ad0db868d7b0b47c1bc1930bec0a8cfbe"></a>Partial Content</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="ade2d76c356f143dca440fc73eac38698"><a name="ade2d76c356f143dca440fc73eac38698"></a><a name="ade2d76c356f143dca440fc73eac38698"></a>The server has processed certain GET requests.</p>
</td>
</tr>
<tr id="r63a14852b889427fb65f1b78de970af5"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a15fefd5e6e6a434f92f6f5e79b4eb6b6"><a name="a15fefd5e6e6a434f92f6f5e79b4eb6b6"></a><a name="a15fefd5e6e6a434f92f6f5e79b4eb6b6"></a>300</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a759d741d0c444fd3874fe860bd63648d"><a name="a759d741d0c444fd3874fe860bd63648d"></a><a name="a759d741d0c444fd3874fe860bd63648d"></a>Multiple Choices</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="afc03f22a6a09470a9682e87fa516ffc4"><a name="afc03f22a6a09470a9682e87fa516ffc4"></a><a name="afc03f22a6a09470a9682e87fa516ffc4"></a>There are multiple options for the location of the requested resource. The response contains a list of resource characteristics and addresses from which the user or user agent (such as a browser) can choose the most appropriate one.</p>
</td>
</tr>
<tr id="rcac1aad617994a78999175d174c6908c"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a579915a462094885b88947643cdef003"><a name="a579915a462094885b88947643cdef003"></a><a name="a579915a462094885b88947643cdef003"></a>301</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a4326a25695ce40fe8233b4d26239ba49"><a name="a4326a25695ce40fe8233b4d26239ba49"></a><a name="a4326a25695ce40fe8233b4d26239ba49"></a>Moved Permanently</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="abd93f7545a1641fe97e84f77c394b187"><a name="abd93f7545a1641fe97e84f77c394b187"></a><a name="abd93f7545a1641fe97e84f77c394b187"></a>The requested resource has been assigned a new permanent URI, and the new URI is contained in the response.</p>
</td>
</tr>
<tr id="r8fde9b3065ab41938601ed83d07d089b"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="ae45e9c0b7f194d998bcf237ea8da0319"><a name="ae45e9c0b7f194d998bcf237ea8da0319"></a><a name="ae45e9c0b7f194d998bcf237ea8da0319"></a>302</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a14f9b1d094e94a7388df2662cdccd49a"><a name="a14f9b1d094e94a7388df2662cdccd49a"></a><a name="a14f9b1d094e94a7388df2662cdccd49a"></a>Found</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a869ebe4e0a40496ba908072389246c52"><a name="a869ebe4e0a40496ba908072389246c52"></a><a name="a869ebe4e0a40496ba908072389246c52"></a>The requested resource resides temporarily under a different URI.</p>
</td>
</tr>
<tr id="rd3cdc4ce4a704a2e8c30fe605a64beb8"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a9f531c3875134e8aa53a4012ad637e3e"><a name="a9f531c3875134e8aa53a4012ad637e3e"></a><a name="a9f531c3875134e8aa53a4012ad637e3e"></a>303</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="afe6949574bd94451bfe3c9f3dcd985cc"><a name="afe6949574bd94451bfe3c9f3dcd985cc"></a><a name="afe6949574bd94451bfe3c9f3dcd985cc"></a>See Other</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a3fbcce4a49f24fe79fd9511e2eea2b9c"><a name="a3fbcce4a49f24fe79fd9511e2eea2b9c"></a><a name="a3fbcce4a49f24fe79fd9511e2eea2b9c"></a>Retrieve a location.</p>
<p id="a7786732ced524b12bf587d44ce1807ad"><a name="a7786732ced524b12bf587d44ce1807ad"></a><a name="a7786732ced524b12bf587d44ce1807ad"></a>The response to the request can be found under a different URI and should be retrieved using a GET or POST method.</p>
</td>
</tr>
<tr id="r7c5c6e871f644f3d8a5ee7650bd03844"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="af77cd5306ae1408daca73ae2df0a3673"><a name="af77cd5306ae1408daca73ae2df0a3673"></a><a name="af77cd5306ae1408daca73ae2df0a3673"></a>304</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a4050355cdd414396a932871de7846cc1"><a name="a4050355cdd414396a932871de7846cc1"></a><a name="a4050355cdd414396a932871de7846cc1"></a>Not Modified</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="aece67fb95f9c4414b68a6732bb3d300e"><a name="aece67fb95f9c4414b68a6732bb3d300e"></a><a name="aece67fb95f9c4414b68a6732bb3d300e"></a>The requested resource has not been modified. When the server returns this status code, it does not return any resources.</p>
</td>
</tr>
<tr id="r09527273ee234fd1b53687c4d6b5117c"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="ac6e84627e0e84c2c8690a135f5384236"><a name="ac6e84627e0e84c2c8690a135f5384236"></a><a name="ac6e84627e0e84c2c8690a135f5384236"></a>305</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a7946f82bd7ff4764a8de7155e4ecc0c2"><a name="a7946f82bd7ff4764a8de7155e4ecc0c2"></a><a name="a7946f82bd7ff4764a8de7155e4ecc0c2"></a>Use Proxy</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="af34162d1f67b4f048adc19f2baedf7de"><a name="af34162d1f67b4f048adc19f2baedf7de"></a><a name="af34162d1f67b4f048adc19f2baedf7de"></a>The requested resource must be accessed through a proxy.</p>
</td>
</tr>
<tr id="r2539d3da4684439f9d0755d5fb99fafe"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a9e4039a453b94740a01783c3eafee3fb"><a name="a9e4039a453b94740a01783c3eafee3fb"></a><a name="a9e4039a453b94740a01783c3eafee3fb"></a>306</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a546b4b18155d40afb0cfc6d132100b4f"><a name="a546b4b18155d40afb0cfc6d132100b4f"></a><a name="a546b4b18155d40afb0cfc6d132100b4f"></a>Unused</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="aa4a7ec1a652442c2bf3ad8b9df5e1f3a"><a name="aa4a7ec1a652442c2bf3ad8b9df5e1f3a"></a><a name="aa4a7ec1a652442c2bf3ad8b9df5e1f3a"></a>The HTTP status code is no longer used.</p>
</td>
</tr>
<tr id="r7cbbb7fcb90e449f949046b2e8ea5b00"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a8af0f4ebfb514e16b6e1009565b6dcd2"><a name="a8af0f4ebfb514e16b6e1009565b6dcd2"></a><a name="a8af0f4ebfb514e16b6e1009565b6dcd2"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a91b0623ab3784acc94881811ad8da8ea"><a name="a91b0623ab3784acc94881811ad8da8ea"></a><a name="a91b0623ab3784acc94881811ad8da8ea"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="afbaaa89f9388470a87cd9205775beba5"><a name="afbaaa89f9388470a87cd9205775beba5"></a><a name="afbaaa89f9388470a87cd9205775beba5"></a>Invalid request.</p>
<p id="a3e5262ae14504bfe9735ac5a4f6ed832"><a name="a3e5262ae14504bfe9735ac5a4f6ed832"></a><a name="a3e5262ae14504bfe9735ac5a4f6ed832"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="ra509c21948db492289c4e92f912d230a"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="ad903ef945f9e4a6396a94ea2524010fb"><a name="ad903ef945f9e4a6396a94ea2524010fb"></a><a name="ad903ef945f9e4a6396a94ea2524010fb"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a62db3f1ecc2f486badbec94921410301"><a name="a62db3f1ecc2f486badbec94921410301"></a><a name="a62db3f1ecc2f486badbec94921410301"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="ae1da71d475404736986d95e3629646c3"><a name="ae1da71d475404736986d95e3629646c3"></a><a name="ae1da71d475404736986d95e3629646c3"></a>The status code is returned after the client provides the authentication information, indicating that the authentication information is incorrect or invalid.</p>
</td>
</tr>
<tr id="r85ca63fe7d3a413392a3dad5fd5f69e2"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a87b31fc382a743eb857e0e41d35d3c12"><a name="a87b31fc382a743eb857e0e41d35d3c12"></a><a name="a87b31fc382a743eb857e0e41d35d3c12"></a>402</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a6e661d959dd9483dafb12fac77a4faae"><a name="a6e661d959dd9483dafb12fac77a4faae"></a><a name="a6e661d959dd9483dafb12fac77a4faae"></a>Payment Required</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a6b1995fe5dd34fd4aafcf7a82dc02d6f"><a name="a6b1995fe5dd34fd4aafcf7a82dc02d6f"></a><a name="a6b1995fe5dd34fd4aafcf7a82dc02d6f"></a>This status code is reserved for future use.</p>
</td>
</tr>
<tr id="r4b0c7f94a2ee48e18fdbf3145aab6eab"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a85a4c60b21ed4795beedfa1ba9c96b8d"><a name="a85a4c60b21ed4795beedfa1ba9c96b8d"></a><a name="a85a4c60b21ed4795beedfa1ba9c96b8d"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a8cadcbed279d4427b24621dd2adcfe66"><a name="a8cadcbed279d4427b24621dd2adcfe66"></a><a name="a8cadcbed279d4427b24621dd2adcfe66"></a>Forbidden</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a04eed0db24434b498b620fdfe5fa9aab"><a name="a04eed0db24434b498b620fdfe5fa9aab"></a><a name="a04eed0db24434b498b620fdfe5fa9aab"></a>The server understood the request, but is refusing to fulfill it.</p>
<p id="ae5a332deb981414098f4d7b07578c510"><a name="ae5a332deb981414098f4d7b07578c510"></a><a name="ae5a332deb981414098f4d7b07578c510"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="r434feff721754be387bae9f429bcdbcb"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a1c4a2c10adda45d09d91b977c55fa7b1"><a name="a1c4a2c10adda45d09d91b977c55fa7b1"></a><a name="a1c4a2c10adda45d09d91b977c55fa7b1"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a4ee08c5b924d4833a6175f81fd9bfb48"><a name="a4ee08c5b924d4833a6175f81fd9bfb48"></a><a name="a4ee08c5b924d4833a6175f81fd9bfb48"></a>NotFound</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a4e74057f79424d8b8efb9bd6a3f4b730"><a name="a4e74057f79424d8b8efb9bd6a3f4b730"></a><a name="a4e74057f79424d8b8efb9bd6a3f4b730"></a>The requested resource cannot be found.</p>
<p id="a65fd0adce76d40ab89034e8b2a97d550"><a name="a65fd0adce76d40ab89034e8b2a97d550"></a><a name="a65fd0adce76d40ab89034e8b2a97d550"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="rd4c0b4a1dfde4c5d873291169b956e71"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a955e79b0b6a540ab9897774d8f4d445b"><a name="a955e79b0b6a540ab9897774d8f4d445b"></a><a name="a955e79b0b6a540ab9897774d8f4d445b"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a51e54e40dad348aeab38f91aab196838"><a name="a51e54e40dad348aeab38f91aab196838"></a><a name="a51e54e40dad348aeab38f91aab196838"></a>MethodNotAllowed</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="afecffffef2e641bcb370d2e6b96bf2b8"><a name="afecffffef2e641bcb370d2e6b96bf2b8"></a><a name="afecffffef2e641bcb370d2e6b96bf2b8"></a>The method specified in the request is not supported for the requested resource.</p>
<p id="a270182983fff4f18939160a72c331425"><a name="a270182983fff4f18939160a72c331425"></a><a name="a270182983fff4f18939160a72c331425"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="r9d1d52cf1f5641ccae2358893624b38b"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a3b3bb265bbc44f44a64d1b381f211d87"><a name="a3b3bb265bbc44f44a64d1b381f211d87"></a><a name="a3b3bb265bbc44f44a64d1b381f211d87"></a>406</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="abe7dbccc6ba3495da29e70881509ea37"><a name="abe7dbccc6ba3495da29e70881509ea37"></a><a name="abe7dbccc6ba3495da29e70881509ea37"></a>Not Acceptable</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a66eb017c5dcd4bbeb50bc78bfb5b3256"><a name="a66eb017c5dcd4bbeb50bc78bfb5b3256"></a><a name="a66eb017c5dcd4bbeb50bc78bfb5b3256"></a>The server cannot fulfill the request according to the content characteristics of the request.</p>
</td>
</tr>
<tr id="r0367e2cfd1574d378298eee8f49ede56"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a485ca01f2d7e41c883501e7544aa6ba0"><a name="a485ca01f2d7e41c883501e7544aa6ba0"></a><a name="a485ca01f2d7e41c883501e7544aa6ba0"></a>407</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a92f2d4ec27fc4a478724733244c61055"><a name="a92f2d4ec27fc4a478724733244c61055"></a><a name="a92f2d4ec27fc4a478724733244c61055"></a>Proxy Authentication Required</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a4f2780df63424efabdd5861d538c17d0"><a name="a4f2780df63424efabdd5861d538c17d0"></a><a name="a4f2780df63424efabdd5861d538c17d0"></a>This status code is similar to 401, but indicates that the client must first authenticate itself with the proxy.</p>
</td>
</tr>
<tr id="r7c07a404cf23467fa48f71625afdd0b1"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a673d796a29cd489890a3183de89ef602"><a name="a673d796a29cd489890a3183de89ef602"></a><a name="a673d796a29cd489890a3183de89ef602"></a>408</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="aa3c74a0e9f97444da67139a5edf74a34"><a name="aa3c74a0e9f97444da67139a5edf74a34"></a><a name="aa3c74a0e9f97444da67139a5edf74a34"></a>Request Time-out</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a78bfcc247c98439fb55dfe101821a3d0"><a name="a78bfcc247c98439fb55dfe101821a3d0"></a><a name="a78bfcc247c98439fb55dfe101821a3d0"></a>The request timed out.</p>
<p id="ae64b7a9dfbdb41708c70f98bdae4f92f"><a name="ae64b7a9dfbdb41708c70f98bdae4f92f"></a><a name="ae64b7a9dfbdb41708c70f98bdae4f92f"></a>The client may repeat the request without modifications at any later time.</p>
</td>
</tr>
<tr id="r5d8e87a18a71408cb42e27d924b48103"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a2d467f82122c4be28a1832037da599a1"><a name="a2d467f82122c4be28a1832037da599a1"></a><a name="a2d467f82122c4be28a1832037da599a1"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a23ff91be80454230a8c143c718316e8a"><a name="a23ff91be80454230a8c143c718316e8a"></a><a name="a23ff91be80454230a8c143c718316e8a"></a>Conflict</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a7b71d365692045bc9c7483bb0c030c4b"><a name="a7b71d365692045bc9c7483bb0c030c4b"></a><a name="a7b71d365692045bc9c7483bb0c030c4b"></a>The request could not be completed due to a conflict with the current state of the resource. </p>
<p id="a67bf154992f849c3b74affface21edac"><a name="a67bf154992f849c3b74affface21edac"></a><a name="a67bf154992f849c3b74affface21edac"></a>This status code indicates that the resource that the client attempts to create already exits, or the request fails to be processed because of the update of the conflict request.</p>
</td>
</tr>
<tr id="r128bed14acd64b8ea4819c3630d11b82"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="aae567681bcd34d2aaec52a72f46041dc"><a name="aae567681bcd34d2aaec52a72f46041dc"></a><a name="aae567681bcd34d2aaec52a72f46041dc"></a>410</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a316fa75bd95f4d22a64edefe9f75f5c2"><a name="a316fa75bd95f4d22a64edefe9f75f5c2"></a><a name="a316fa75bd95f4d22a64edefe9f75f5c2"></a>Gone</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a732a4541cf3c4469bc9acad68170109b"><a name="a732a4541cf3c4469bc9acad68170109b"></a><a name="a732a4541cf3c4469bc9acad68170109b"></a>The requested resource is no longer available.</p>
<p id="ad6acf7463f264427bc3e1138e9635a56"><a name="ad6acf7463f264427bc3e1138e9635a56"></a><a name="ad6acf7463f264427bc3e1138e9635a56"></a>The status code indicates that the requested resource has been deleted permanently. </p>
</td>
</tr>
<tr id="r23352b5483a4467dbf849467cb2a768a"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="ade099ef9069645339535eeb86c98c58c"><a name="ade099ef9069645339535eeb86c98c58c"></a><a name="ade099ef9069645339535eeb86c98c58c"></a>411</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a4265a186430548008ddff1092a17c163"><a name="a4265a186430548008ddff1092a17c163"></a><a name="a4265a186430548008ddff1092a17c163"></a>Length Required</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="ad2bdd3cb3d7240bb82928fbb1b902fa4"><a name="ad2bdd3cb3d7240bb82928fbb1b902fa4"></a><a name="ad2bdd3cb3d7240bb82928fbb1b902fa4"></a>The server refuses to process the request without a defined Content-Length.</p>
</td>
</tr>
<tr id="r585acc64ccce4201a5832a6acf0324a3"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a6e423d350e994f94b1ea1c5ccbd98f1e"><a name="a6e423d350e994f94b1ea1c5ccbd98f1e"></a><a name="a6e423d350e994f94b1ea1c5ccbd98f1e"></a>412</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a3a7ae39f69d746ac9a955645857c60a1"><a name="a3a7ae39f69d746ac9a955645857c60a1"></a><a name="a3a7ae39f69d746ac9a955645857c60a1"></a>Precondition Failed</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a7c523d24713c459eb167028b4f154113"><a name="a7c523d24713c459eb167028b4f154113"></a><a name="a7c523d24713c459eb167028b4f154113"></a>The server does not meet one of the preconditions that the requester puts on the request.</p>
</td>
</tr>
<tr id="r114f65f16ff4480db76f0f95525ee8ce"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="ae45692711e2144059a5cc2a68d6103d5"><a name="ae45692711e2144059a5cc2a68d6103d5"></a><a name="ae45692711e2144059a5cc2a68d6103d5"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a53dba5b2fb574e87b1b3b940ff0cd250"><a name="a53dba5b2fb574e87b1b3b940ff0cd250"></a><a name="a53dba5b2fb574e87b1b3b940ff0cd250"></a>Request Entity Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a4b35e1969ff648349acce195ba2f1128"><a name="a4b35e1969ff648349acce195ba2f1128"></a><a name="a4b35e1969ff648349acce195ba2f1128"></a>The request is larger than that a server is able to process. The server may close the connection to prevent the client from continuing the request. If the server cannot process the request temporarily, the response will contain a Retry-After header field.</p>
</td>
</tr>
<tr id="r5dc84b339bf3409ca09f5963cfabcd2c"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="aaa1fed9a2d744e44be3a75db30dde51e"><a name="aaa1fed9a2d744e44be3a75db30dde51e"></a><a name="aaa1fed9a2d744e44be3a75db30dde51e"></a>414</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="ae14a7b4ce00c48049889b5afd1ea641b"><a name="ae14a7b4ce00c48049889b5afd1ea641b"></a><a name="ae14a7b4ce00c48049889b5afd1ea641b"></a>Request-URI Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a00b22a30be834a1f99940f4b83202c16"><a name="a00b22a30be834a1f99940f4b83202c16"></a><a name="a00b22a30be834a1f99940f4b83202c16"></a>The URI provided was too long for the server to process.</p>
</td>
</tr>
<tr id="r11542ca9e8d741979fa37dd241c104a7"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a325c4b4e0b4b4dd9b39a4dc882ada3c3"><a name="a325c4b4e0b4b4dd9b39a4dc882ada3c3"></a><a name="a325c4b4e0b4b4dd9b39a4dc882ada3c3"></a>415</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="ac80abe84aa16476ba378e0decd4c29a8"><a name="ac80abe84aa16476ba378e0decd4c29a8"></a><a name="ac80abe84aa16476ba378e0decd4c29a8"></a>Unsupported Media Type</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a977bc47446e44be0b45471af10a163fd"><a name="a977bc47446e44be0b45471af10a163fd"></a><a name="a977bc47446e44be0b45471af10a163fd"></a>The server is unable to process the media format in the request.</p>
</td>
</tr>
<tr id="r5d8b1b2d47bd429f96dfaa1edb739037"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a96092a705d2c48c689f722b9fbb47f48"><a name="a96092a705d2c48c689f722b9fbb47f48"></a><a name="a96092a705d2c48c689f722b9fbb47f48"></a>416</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a13a6c0a3e73248639ca41da6a86345f7"><a name="a13a6c0a3e73248639ca41da6a86345f7"></a><a name="a13a6c0a3e73248639ca41da6a86345f7"></a>Requested range not satisfiable</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="ad08674ab29824d119e489807eebb5d84"><a name="ad08674ab29824d119e489807eebb5d84"></a><a name="ad08674ab29824d119e489807eebb5d84"></a>The requested range is invalid.</p>
</td>
</tr>
<tr id="r560b8176231747c28f3f3dce78c40667"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a0cb2336dc5984fde809049f5190ecfa5"><a name="a0cb2336dc5984fde809049f5190ecfa5"></a><a name="a0cb2336dc5984fde809049f5190ecfa5"></a>417</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a4d1de880f54344bba61b84a69908e882"><a name="a4d1de880f54344bba61b84a69908e882"></a><a name="a4d1de880f54344bba61b84a69908e882"></a>Expectation Failed</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a35043611412e4fa597ec4e71b71e90a6"><a name="a35043611412e4fa597ec4e71b71e90a6"></a><a name="a35043611412e4fa597ec4e71b71e90a6"></a>The server fails to meet the requirements of the Expect request-header field.</p>
</td>
</tr>
<tr id="r91eae8b9d05148a6968a17c1b9a815fc"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a9e0c65cc3630438784352727895f9006"><a name="a9e0c65cc3630438784352727895f9006"></a><a name="a9e0c65cc3630438784352727895f9006"></a>422</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a2e5a68fce1b64794824c9e225ae5c806"><a name="a2e5a68fce1b64794824c9e225ae5c806"></a><a name="a2e5a68fce1b64794824c9e225ae5c806"></a>UnprocessableEntity</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a7fdb1e9694984b2c8ac9ce2fac6486aa"><a name="a7fdb1e9694984b2c8ac9ce2fac6486aa"></a><a name="a7fdb1e9694984b2c8ac9ce2fac6486aa"></a>The request is well-formed but is unable to be processed due to semantic errors.</p>
</td>
</tr>
<tr id="r7443b7dca04f4adc945d1448898fbfd7"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a52ff15a9d5f34326bff4d9ee157c3d18"><a name="a52ff15a9d5f34326bff4d9ee157c3d18"></a><a name="a52ff15a9d5f34326bff4d9ee157c3d18"></a>429</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="ae514e3ffe5264adca5d9f6571c73078b"><a name="ae514e3ffe5264adca5d9f6571c73078b"></a><a name="ae514e3ffe5264adca5d9f6571c73078b"></a>TooManyRequests</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="abb1b91c2a1314d32ac9770f2623ae043"><a name="abb1b91c2a1314d32ac9770f2623ae043"></a><a name="abb1b91c2a1314d32ac9770f2623ae043"></a>The client has sent more requests than its rate limit is allowed within a given amount of time, or the server has received more requests than it is able to process within a given amount of time. In this case, it is advisable for the client to re-initiate requests after the time specified in the Retry-After header of the response expires.</p>
</td>
</tr>
<tr id="r7900976b57ca4172adb5b79bd1185446"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a74710e4987b14c8a942e23edc00311e5"><a name="a74710e4987b14c8a942e23edc00311e5"></a><a name="a74710e4987b14c8a942e23edc00311e5"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a8eecf8898ca447bcbe74274b1dc19d4f"><a name="a8eecf8898ca447bcbe74274b1dc19d4f"></a><a name="a8eecf8898ca447bcbe74274b1dc19d4f"></a>InternalServerError</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a1e8ab391f7ed4566b04a86f05d0f47bb"><a name="a1e8ab391f7ed4566b04a86f05d0f47bb"></a><a name="a1e8ab391f7ed4566b04a86f05d0f47bb"></a>The server is able to receive the request but it could not understand the request.</p>
</td>
</tr>
<tr id="r1101fcc1970d44f1b5a449080a6d2f7a"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a802042cc977a4257a8533135832ab524"><a name="a802042cc977a4257a8533135832ab524"></a><a name="a802042cc977a4257a8533135832ab524"></a>501</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a3e4f74ba04c54225ae97905ebca4b701"><a name="a3e4f74ba04c54225ae97905ebca4b701"></a><a name="a3e4f74ba04c54225ae97905ebca4b701"></a>Not Implemented</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a7dbbdd4299e9440eabf8e52035d59c17"><a name="a7dbbdd4299e9440eabf8e52035d59c17"></a><a name="a7dbbdd4299e9440eabf8e52035d59c17"></a>The server does not support the requested function.</p>
</td>
</tr>
<tr id="r87ec10ab6aba42f5928f383dfebee44d"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="ae00f45f2d43b4033a29333785ed3ac83"><a name="ae00f45f2d43b4033a29333785ed3ac83"></a><a name="ae00f45f2d43b4033a29333785ed3ac83"></a>502</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="ac638009b4e4c489992bf4c03ea5b12d0"><a name="ac638009b4e4c489992bf4c03ea5b12d0"></a><a name="ac638009b4e4c489992bf4c03ea5b12d0"></a>Bad Gateway</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a7df30e2c0249428c9e802f3bf900ee02"><a name="a7df30e2c0249428c9e802f3bf900ee02"></a><a name="a7df30e2c0249428c9e802f3bf900ee02"></a>The server is acting as a gateway or proxy and receives an invalid request from a remote server.</p>
</td>
</tr>
<tr id="ra5b872b5d3c94c109ae5f041a0e0a6ed"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a3e4150216f3242009333ee371dcedaa6"><a name="a3e4150216f3242009333ee371dcedaa6"></a><a name="a3e4150216f3242009333ee371dcedaa6"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="abbcdc28e2aec43ac976f10c4a9430133"><a name="abbcdc28e2aec43ac976f10c4a9430133"></a><a name="abbcdc28e2aec43ac976f10c4a9430133"></a>ServiceUnavailable</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="af80f1cdf06714c51a477884cb678f0b4"><a name="af80f1cdf06714c51a477884cb678f0b4"></a><a name="af80f1cdf06714c51a477884cb678f0b4"></a>The requested service is invalid.</p>
<p id="a0bb3dc8b0f1c4eb3a1238b0d3643cb14"><a name="a0bb3dc8b0f1c4eb3a1238b0d3643cb14"></a><a name="a0bb3dc8b0f1c4eb3a1238b0d3643cb14"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="r9e5a69d883f146f2a0c698bb7b244b66"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="aa3db92b14c6441389a03ee8c47774eaa"><a name="aa3db92b14c6441389a03ee8c47774eaa"></a><a name="aa3db92b14c6441389a03ee8c47774eaa"></a>504</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="aab377e3751844ec0b187099015e767a7"><a name="aab377e3751844ec0b187099015e767a7"></a><a name="aab377e3751844ec0b187099015e767a7"></a>ServerTimeout</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="a854ac172d5a040f18a36e29b041e622d"><a name="a854ac172d5a040f18a36e29b041e622d"></a><a name="a854ac172d5a040f18a36e29b041e622d"></a>The request cannot be fulfilled within a given time. This status code is returned to the client only when the <strong id="b842352706162338"><a name="b842352706162338"></a><a name="b842352706162338"></a>Timeout</strong> parameter is specified in the request.</p>
</td>
</tr>
<tr id="r44a5a336bf024424aec1bacbc38e1699"><td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.4.1.1 "><p id="a05e25aaaba324b8b841502b9a870428b"><a name="a05e25aaaba324b8b841502b9a870428b"></a><a name="a05e25aaaba324b8b841502b9a870428b"></a>505</p>
</td>
<td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.4.1.2 "><p id="a6169fec01b6447e28898e7b505b2b4d5"><a name="a6169fec01b6447e28898e7b505b2b4d5"></a><a name="a6169fec01b6447e28898e7b505b2b4d5"></a>HTTP Version not supported</p>
</td>
<td class="cellrowborder" valign="top" width="59.97%" headers="mcps1.2.4.1.3 "><p id="ae1b12533c7914e39965b447fb01d2ee6"><a name="ae1b12533c7914e39965b447fb01d2ee6"></a><a name="ae1b12533c7914e39965b447fb01d2ee6"></a>The server does not support the HTTP protocol version used in the request.</p>
</td>
</tr>
</tbody>
</table>

