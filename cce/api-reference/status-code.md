# Status Code<a name="cce_02_0084"></a>

[Table 1](#t20791fa3900d4d2d8289da35135eca33)  describes the status codes.

**Table  1**  Status code

<a name="t20791fa3900d4d2d8289da35135eca33"></a>
<table><thead align="left"><tr id="rbc76ad82de2047af81b473727c96ece4"><th class="cellrowborder" valign="top" width="15.120000000000001%" id="mcps1.2.4.1.1"><p id="a84aecb1a68754e5ca56899cf035d0ec7"><a name="a84aecb1a68754e5ca56899cf035d0ec7"></a><a name="a84aecb1a68754e5ca56899cf035d0ec7"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="24.88%" id="mcps1.2.4.1.2"><p id="ab2b95d1578ec488f8b624d39a222b500"><a name="ab2b95d1578ec488f8b624d39a222b500"></a><a name="ab2b95d1578ec488f8b624d39a222b500"></a>Code</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="abf289bbe6d3a423fac5f2ad975293b6a"><a name="abf289bbe6d3a423fac5f2ad975293b6a"></a><a name="abf289bbe6d3a423fac5f2ad975293b6a"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="re4f3d7062c0d4e90b5e77dc97a0f03d4"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="ab19e1853c71e4b2aa9c95d8449e98f35"><a name="ab19e1853c71e4b2aa9c95d8449e98f35"></a><a name="ab19e1853c71e4b2aa9c95d8449e98f35"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="aed4d7626f2c24a78b85eac834631d6bf"><a name="aed4d7626f2c24a78b85eac834631d6bf"></a><a name="aed4d7626f2c24a78b85eac834631d6bf"></a>Continue</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="af1654c6d13e542d4905d8fe538ac11d1"><a name="af1654c6d13e542d4905d8fe538ac11d1"></a><a name="af1654c6d13e542d4905d8fe538ac11d1"></a>The server has received the initial part of the request and the client should continue to send the remaining part.</p>
<p id="a509ade96f63047f3b4061c45d474157b"><a name="a509ade96f63047f3b4061c45d474157b"></a><a name="a509ade96f63047f3b4061c45d474157b"></a>It is issued on a provisional basis while request processing continues. It alerts the client to wait for a final response.</p>
</td>
</tr>
<tr id="r6a99ef6e489144e99ff1552d7d892504"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="abc5d56a5d57e4b52a76208ac758e229d"><a name="abc5d56a5d57e4b52a76208ac758e229d"></a><a name="abc5d56a5d57e4b52a76208ac758e229d"></a>101</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a41b573f0f7564a97a7e1ceed6514545b"><a name="a41b573f0f7564a97a7e1ceed6514545b"></a><a name="a41b573f0f7564a97a7e1ceed6514545b"></a>Switching Protocols</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="ac13b93ced28140d29172d47d76e79974"><a name="ac13b93ced28140d29172d47d76e79974"></a><a name="ac13b93ced28140d29172d47d76e79974"></a>The requester has asked the server to switch protocols and the server has agreed to do so. The target protocol must be more advanced than the source protocol.</p>
<p id="a8d39ff763e91475ca06c715071a7fcba"><a name="a8d39ff763e91475ca06c715071a7fcba"></a><a name="a8d39ff763e91475ca06c715071a7fcba"></a>For example, the current HTTP protocol is switched to a later version of HTTP.</p>
</td>
</tr>
<tr id="r20e4011a79c447199bc83428560acadc"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="afd634d3079f64f348300a3060c478984"><a name="afd634d3079f64f348300a3060c478984"></a><a name="afd634d3079f64f348300a3060c478984"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a52db7506e9f548ec8f224f60c1e4777a"><a name="a52db7506e9f548ec8f224f60c1e4777a"></a><a name="a52db7506e9f548ec8f224f60c1e4777a"></a>Created</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="af7f51be1fa7e44dcae2f2bec57baa1a2"><a name="af7f51be1fa7e44dcae2f2bec57baa1a2"></a><a name="af7f51be1fa7e44dcae2f2bec57baa1a2"></a>The request has been fulfilled, resulting in the creation of a new resource.</p>
</td>
</tr>
<tr id="r191c2bbf56fc450a846dbe0fd35bb5a5"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="ad10fe65750e3404491c2149c73b59834"><a name="ad10fe65750e3404491c2149c73b59834"></a><a name="ad10fe65750e3404491c2149c73b59834"></a>202</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="aedcf450fe29a4a369fb56fedd7dd1819"><a name="aedcf450fe29a4a369fb56fedd7dd1819"></a><a name="aedcf450fe29a4a369fb56fedd7dd1819"></a>Accepted</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="aee9aa60ac5bf40049b927e9015dd4570"><a name="aee9aa60ac5bf40049b927e9015dd4570"></a><a name="aee9aa60ac5bf40049b927e9015dd4570"></a>The request has been accepted for processing, but the processing has not been completed.</p>
</td>
</tr>
<tr id="r3960990364f54bc38789ef069bd9744b"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a23c45676007d46c4807585f84d9edba2"><a name="a23c45676007d46c4807585f84d9edba2"></a><a name="a23c45676007d46c4807585f84d9edba2"></a>203</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="abd9933d1be41469e9bd215ba0803814c"><a name="abd9933d1be41469e9bd215ba0803814c"></a><a name="abd9933d1be41469e9bd215ba0803814c"></a>Non-Authoritative Information</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="ae3733b684ca94e738c35d1abcfeb3da4"><a name="ae3733b684ca94e738c35d1abcfeb3da4"></a><a name="ae3733b684ca94e738c35d1abcfeb3da4"></a>The server successfully processed the request, but is returning information that may be from another source.</p>
</td>
</tr>
<tr id="r2a604d94067f4cbb8a69c8fbb77ada84"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a6439e35a331e404c99bd10232edc03bd"><a name="a6439e35a331e404c99bd10232edc03bd"></a><a name="a6439e35a331e404c99bd10232edc03bd"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a3b0d3e4dc1974880801205751547a473"><a name="a3b0d3e4dc1974880801205751547a473"></a><a name="a3b0d3e4dc1974880801205751547a473"></a>NoContent</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a485c52b011e447fc9c02ebffa9d97df0"><a name="a485c52b011e447fc9c02ebffa9d97df0"></a><a name="a485c52b011e447fc9c02ebffa9d97df0"></a>The server has successfully processed the request, but does not return any content.</p>
<p id="a2658cd62dd4147a18f74faffb1df56f9"><a name="a2658cd62dd4147a18f74faffb1df56f9"></a><a name="a2658cd62dd4147a18f74faffb1df56f9"></a>The status code is returned in response to an HTTP OPTIONS request.</p>
</td>
</tr>
<tr id="rd528da1291fe42a6b0ac5dd9eec9e3be"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="af51b305955a641c98ed8257e1aeadd98"><a name="af51b305955a641c98ed8257e1aeadd98"></a><a name="af51b305955a641c98ed8257e1aeadd98"></a>205</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a5f90f247e48f4ab087fba767a29b1f63"><a name="a5f90f247e48f4ab087fba767a29b1f63"></a><a name="a5f90f247e48f4ab087fba767a29b1f63"></a>Reset Content</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="af313c681e80e4335bb92f04aa4800b70"><a name="af313c681e80e4335bb92f04aa4800b70"></a><a name="af313c681e80e4335bb92f04aa4800b70"></a>The server has successfully processed the request, but does not return any content. Unlike a 204 response, this response requires that the requester reset the content.</p>
</td>
</tr>
<tr id="r5cfb4cb336bf4dd9b925a4abe4881ff2"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="afb23b89e3ac544c8805806ec90ab66a9"><a name="afb23b89e3ac544c8805806ec90ab66a9"></a><a name="afb23b89e3ac544c8805806ec90ab66a9"></a>206</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="aa0b14468438146489cbd5e75c176f349"><a name="aa0b14468438146489cbd5e75c176f349"></a><a name="aa0b14468438146489cbd5e75c176f349"></a>Partial Content</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a0aec02f0c2c64327a623e82076466116"><a name="a0aec02f0c2c64327a623e82076466116"></a><a name="a0aec02f0c2c64327a623e82076466116"></a>The server has successfully processed a part of the GET request.</p>
</td>
</tr>
<tr id="ra1c6521ca98e46c0919d43eaa9359e31"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a08aa4679868b443d8dab6798fa7b1e02"><a name="a08aa4679868b443d8dab6798fa7b1e02"></a><a name="a08aa4679868b443d8dab6798fa7b1e02"></a>300</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="aada629cd692a4f02a63a3d2950b2a08f"><a name="aada629cd692a4f02a63a3d2950b2a08f"></a><a name="aada629cd692a4f02a63a3d2950b2a08f"></a>Multiple Choices</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a177bb92a44c44cd5997eac006bbd41dd"><a name="a177bb92a44c44cd5997eac006bbd41dd"></a><a name="a177bb92a44c44cd5997eac006bbd41dd"></a>There are multiple options for the requested resource. For example, this code could be used to present a list of resource characteristics and addresses from which the client such as a browser may choose.</p>
</td>
</tr>
<tr id="r341c5b71e83e411eab3f9baaa285a919"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a43bd98a2a34b4350b56e138fa49f34c3"><a name="a43bd98a2a34b4350b56e138fa49f34c3"></a><a name="a43bd98a2a34b4350b56e138fa49f34c3"></a>301</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="ac283fa53eef54d4c89c19ca711cfc556"><a name="ac283fa53eef54d4c89c19ca711cfc556"></a><a name="ac283fa53eef54d4c89c19ca711cfc556"></a>Moved Permanently</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="ab751941751e843e2afaccf6feedc8d2b"><a name="ab751941751e843e2afaccf6feedc8d2b"></a><a name="ab751941751e843e2afaccf6feedc8d2b"></a>This and all future requests should be permanently directed to the given URI indicated in this response.</p>
</td>
</tr>
<tr id="rfe65ae38d89741098dd27cfa55301205"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a62c5111eee80465aa67ee89e550dea06"><a name="a62c5111eee80465aa67ee89e550dea06"></a><a name="a62c5111eee80465aa67ee89e550dea06"></a>302</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a3de7db914ce24e72acce438266f28ff7"><a name="a3de7db914ce24e72acce438266f28ff7"></a><a name="a3de7db914ce24e72acce438266f28ff7"></a>Found</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a5353a781e0584463920706e32806d344"><a name="a5353a781e0584463920706e32806d344"></a><a name="a5353a781e0584463920706e32806d344"></a>The requested resource was temporarily moved.</p>
</td>
</tr>
<tr id="r88f7b45cd0dc4e9084536f0a1817cb1d"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a2cc98f9d0d8942fd867857e888379afb"><a name="a2cc98f9d0d8942fd867857e888379afb"></a><a name="a2cc98f9d0d8942fd867857e888379afb"></a>303</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a0d1bba0045e24c1ea8208bf0a3a4ce5d"><a name="a0d1bba0045e24c1ea8208bf0a3a4ce5d"></a><a name="a0d1bba0045e24c1ea8208bf0a3a4ce5d"></a>See Other</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a3410938145ee4e09b4d7f75cf49c849d"><a name="a3410938145ee4e09b4d7f75cf49c849d"></a><a name="a3410938145ee4e09b4d7f75cf49c849d"></a>The response to the request can be found under a different URI, and should be retrieved using a GET or POST method.</p>
</td>
</tr>
<tr id="r55cf7b8a49dc4164851bb97466294286"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="aec0ff825b98449c2b0166372ae569085"><a name="aec0ff825b98449c2b0166372ae569085"></a><a name="aec0ff825b98449c2b0166372ae569085"></a>304</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a42116ee000194ce3a0a65af19c35bff2"><a name="a42116ee000194ce3a0a65af19c35bff2"></a><a name="a42116ee000194ce3a0a65af19c35bff2"></a>Not Modified</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a0ecb1a5d453e41ee8747b62afc224ef5"><a name="a0ecb1a5d453e41ee8747b62afc224ef5"></a><a name="a0ecb1a5d453e41ee8747b62afc224ef5"></a>The requested resource has not been modified. In such case, there is no need to retransmit the resource since the client still has a previously-downloaded copy.</p>
</td>
</tr>
<tr id="re9e57c52d4264722b89183ada2a254d9"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="ab1c90c108e804a949ebf4dd46ca52353"><a name="ab1c90c108e804a949ebf4dd46ca52353"></a><a name="ab1c90c108e804a949ebf4dd46ca52353"></a>305</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="ae473202c8807432b9709658e3a9ba1e0"><a name="ae473202c8807432b9709658e3a9ba1e0"></a><a name="ae473202c8807432b9709658e3a9ba1e0"></a>Use Proxy</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a77cc9864132d4555bc140590ac2a7291"><a name="a77cc9864132d4555bc140590ac2a7291"></a><a name="a77cc9864132d4555bc140590ac2a7291"></a>The requested resource is available only through a proxy.</p>
</td>
</tr>
<tr id="r606d011d131d42ebb95ce9400ddea364"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a0ab773f265644151840fa62722bfa760"><a name="a0ab773f265644151840fa62722bfa760"></a><a name="a0ab773f265644151840fa62722bfa760"></a>306</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="aebe024c88a484ed995280cb80339f4a3"><a name="aebe024c88a484ed995280cb80339f4a3"></a><a name="aebe024c88a484ed995280cb80339f4a3"></a>Unused</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a67cde7e6efe04e34824eeb8092fdca48"><a name="a67cde7e6efe04e34824eeb8092fdca48"></a><a name="a67cde7e6efe04e34824eeb8092fdca48"></a>This HTTP status code is no longer used.</p>
</td>
</tr>
<tr id="rb2dcbb1d93e448e5bd74d8015785d32d"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a7405d5feda82480b95460b06d9d9ab62"><a name="a7405d5feda82480b95460b06d9d9ab62"></a><a name="a7405d5feda82480b95460b06d9d9ab62"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a7dec5a8ee813472daf24f0438278090f"><a name="a7dec5a8ee813472daf24f0438278090f"></a><a name="a7dec5a8ee813472daf24f0438278090f"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a566cffbf340549129db8d0f74e468a28"><a name="a566cffbf340549129db8d0f74e468a28"></a><a name="a566cffbf340549129db8d0f74e468a28"></a>The request is invalid.</p>
<p id="a611fcf889d3945cd9560c318ae9da067"><a name="a611fcf889d3945cd9560c318ae9da067"></a><a name="a611fcf889d3945cd9560c318ae9da067"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="r9af167b643994504b80a78bce27d9eae"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="ae75dab347b5b453a8e5f8995412c91f0"><a name="ae75dab347b5b453a8e5f8995412c91f0"></a><a name="ae75dab347b5b453a8e5f8995412c91f0"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="abbf5f14e1ab24e9a8a0122eb60134917"><a name="abbf5f14e1ab24e9a8a0122eb60134917"></a><a name="abbf5f14e1ab24e9a8a0122eb60134917"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a2d2826ecc5104c8a9e38998f72a51f35"><a name="a2d2826ecc5104c8a9e38998f72a51f35"></a><a name="a2d2826ecc5104c8a9e38998f72a51f35"></a>The authorization information provided by the client is incorrect or invalid.</p>
</td>
</tr>
<tr id="r02caa56bd98642339d0fd7d6f4e24db2"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="abe0b820fd1e94a499679a52e92ac3884"><a name="abe0b820fd1e94a499679a52e92ac3884"></a><a name="abe0b820fd1e94a499679a52e92ac3884"></a>402</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="aa029174cf10247019ff6a97624238427"><a name="aa029174cf10247019ff6a97624238427"></a><a name="aa029174cf10247019ff6a97624238427"></a>Payment Required</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a995a9510740440bb8499077f67c1f49e"><a name="a995a9510740440bb8499077f67c1f49e"></a><a name="a995a9510740440bb8499077f67c1f49e"></a>This status code is reserved for future use.</p>
</td>
</tr>
<tr id="rc833d3ba51a04c43bdc74899046e97d3"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a919b6adc826849fcb7a39db838fe911a"><a name="a919b6adc826849fcb7a39db838fe911a"></a><a name="a919b6adc826849fcb7a39db838fe911a"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a1c7a1f59fd044f378b3d2af334a86191"><a name="a1c7a1f59fd044f378b3d2af334a86191"></a><a name="a1c7a1f59fd044f378b3d2af334a86191"></a>Forbidden</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a9620e1312a4046c0be2b16a6c5392493"><a name="a9620e1312a4046c0be2b16a6c5392493"></a><a name="a9620e1312a4046c0be2b16a6c5392493"></a>The server has received the request and understood it, but the server is refusing to respond to it.</p>
<p id="a24526889b88a482781b8dee97061b5ee"><a name="a24526889b88a482781b8dee97061b5ee"></a><a name="a24526889b88a482781b8dee97061b5ee"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="rcc240dad303c47caa16a2610dfb2b0a7"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="ac6e272275d8344b78aff7e90765ccf8c"><a name="ac6e272275d8344b78aff7e90765ccf8c"></a><a name="ac6e272275d8344b78aff7e90765ccf8c"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a30ee3a65b167493495889c32bf2e56e0"><a name="a30ee3a65b167493495889c32bf2e56e0"></a><a name="a30ee3a65b167493495889c32bf2e56e0"></a>NotFound</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a87ff3ba2ddd343eba394e0c94e77a818"><a name="a87ff3ba2ddd343eba394e0c94e77a818"></a><a name="a87ff3ba2ddd343eba394e0c94e77a818"></a>The requested resource cannot be found.</p>
<p id="a03279c803c9e499d88a44e7d8813b76a"><a name="a03279c803c9e499d88a44e7d8813b76a"></a><a name="a03279c803c9e499d88a44e7d8813b76a"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="r9513553e25694702b3671c7153949d65"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a7485264f5b5848839cebc39fb4fd0b2b"><a name="a7485264f5b5848839cebc39fb4fd0b2b"></a><a name="a7485264f5b5848839cebc39fb4fd0b2b"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="ac13abcc161a44727a622903cdeb9959f"><a name="ac13abcc161a44727a622903cdeb9959f"></a><a name="ac13abcc161a44727a622903cdeb9959f"></a>MethodNotAllowed</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="afe44da959f0f4f66b3d66f3fab7526f6"><a name="afe44da959f0f4f66b3d66f3fab7526f6"></a><a name="afe44da959f0f4f66b3d66f3fab7526f6"></a>A request method is not supported for the requested resource.</p>
<p id="a824f8bb01c9f4829bea8c4be4f36d9fc"><a name="a824f8bb01c9f4829bea8c4be4f36d9fc"></a><a name="a824f8bb01c9f4829bea8c4be4f36d9fc"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="r61b09bc1f6e44b5190befb3ef1e0bf29"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a0c9b78ce39a5465f82c158c15c9da57c"><a name="a0c9b78ce39a5465f82c158c15c9da57c"></a><a name="a0c9b78ce39a5465f82c158c15c9da57c"></a>406</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a37677cf7699e468ea4972a109cf3c9d7"><a name="a37677cf7699e468ea4972a109cf3c9d7"></a><a name="a37677cf7699e468ea4972a109cf3c9d7"></a>Not Acceptable</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a88440e07c4b640c79e60ae91f4fcee52"><a name="a88440e07c4b640c79e60ae91f4fcee52"></a><a name="a88440e07c4b640c79e60ae91f4fcee52"></a>The server cannot fulfill the request based on the content characteristics of the request.</p>
</td>
</tr>
<tr id="r3955dad94fa64770b632cdc1e590a017"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a7b10b53572134c3f93b57ace9dd842b8"><a name="a7b10b53572134c3f93b57ace9dd842b8"></a><a name="a7b10b53572134c3f93b57ace9dd842b8"></a>407</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a6a30ffd664874cda8ddf6ec9b9de375a"><a name="a6a30ffd664874cda8ddf6ec9b9de375a"></a><a name="a6a30ffd664874cda8ddf6ec9b9de375a"></a>Proxy Authentication Required</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a92bc4c85796e4c208bd55c752d4c876a"><a name="a92bc4c85796e4c208bd55c752d4c876a"></a><a name="a92bc4c85796e4c208bd55c752d4c876a"></a>This code is similar to 401, but indicates that the client must first authenticate itself with the proxy.</p>
</td>
</tr>
<tr id="r7255efeda91a4d54a9855bbd7c5a2db8"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a24bf9c6636ab4821a2ff2857f3a0d60e"><a name="a24bf9c6636ab4821a2ff2857f3a0d60e"></a><a name="a24bf9c6636ab4821a2ff2857f3a0d60e"></a>408</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a82afefc9940a4cf6bd03b57d6a8998fa"><a name="a82afefc9940a4cf6bd03b57d6a8998fa"></a><a name="a82afefc9940a4cf6bd03b57d6a8998fa"></a>Request Time-out</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a3330539776934ab8a8ed224632dfe3eb"><a name="a3330539776934ab8a8ed224632dfe3eb"></a><a name="a3330539776934ab8a8ed224632dfe3eb"></a>The server timed out waiting for the request.</p>
<p id="aa2ea199958e34f21aefb853851cb108d"><a name="aa2ea199958e34f21aefb853851cb108d"></a><a name="aa2ea199958e34f21aefb853851cb108d"></a>The client may re-initiate the request without modifications at any later time.</p>
</td>
</tr>
<tr id="r47f62ab6b9b14f9591a544ed91dddeec"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a8949119a934e4c7d849421c3bfcabe1a"><a name="a8949119a934e4c7d849421c3bfcabe1a"></a><a name="a8949119a934e4c7d849421c3bfcabe1a"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a23bdd0ced266497396ecf8660dd842e1"><a name="a23bdd0ced266497396ecf8660dd842e1"></a><a name="a23bdd0ced266497396ecf8660dd842e1"></a>Conflict</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="ae56f7918b6fe4f58a87b2177a8cdade5"><a name="ae56f7918b6fe4f58a87b2177a8cdade5"></a><a name="ae56f7918b6fe4f58a87b2177a8cdade5"></a>The request cannot be processed due to a conflict.</p>
<p id="a9dc9b6c27f8642fab2957c2daa1c7dd3"><a name="a9dc9b6c27f8642fab2957c2daa1c7dd3"></a><a name="a9dc9b6c27f8642fab2957c2daa1c7dd3"></a>This status code indicates that the resource that the client attempts to create already exits, or the request fails to be processed because of the update of the conflict request.</p>
</td>
</tr>
<tr id="r6d60af98286742ec93a6aaff8c208cee"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="ad074d120393c4132b887d6058fac1abd"><a name="ad074d120393c4132b887d6058fac1abd"></a><a name="ad074d120393c4132b887d6058fac1abd"></a>410</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="ab5bbb66b2d8f40ff9508a3ad4de01573"><a name="ab5bbb66b2d8f40ff9508a3ad4de01573"></a><a name="ab5bbb66b2d8f40ff9508a3ad4de01573"></a>Gone</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a98d2ef73b8fc4b42a89462edef8e972e"><a name="a98d2ef73b8fc4b42a89462edef8e972e"></a><a name="a98d2ef73b8fc4b42a89462edef8e972e"></a>The requested resource cannot be found.</p>
<p id="a1e5ffc8f31d4427292dcc470f50533e6"><a name="a1e5ffc8f31d4427292dcc470f50533e6"></a><a name="a1e5ffc8f31d4427292dcc470f50533e6"></a>The status code indicates that the requested resource has been deleted permanently.</p>
</td>
</tr>
<tr id="r5eec8fab32fb49a0ba294b2e873a085e"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="afaa9c532c0a242d1a5c74a14b724d316"><a name="afaa9c532c0a242d1a5c74a14b724d316"></a><a name="afaa9c532c0a242d1a5c74a14b724d316"></a>411</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a269e564e4fff431493e7c6e9ec46665b"><a name="a269e564e4fff431493e7c6e9ec46665b"></a><a name="a269e564e4fff431493e7c6e9ec46665b"></a>Length Required</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="af583cbb1b7d741ddb31c22bff9616cbd"><a name="af583cbb1b7d741ddb31c22bff9616cbd"></a><a name="af583cbb1b7d741ddb31c22bff9616cbd"></a>The server refused to process the request because the request does not specify the length of its content.</p>
</td>
</tr>
<tr id="rcae2021af30b4c65a73fb4f2e10e7850"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a9cec1bd2fc734a5cafab98e9a089c1ed"><a name="a9cec1bd2fc734a5cafab98e9a089c1ed"></a><a name="a9cec1bd2fc734a5cafab98e9a089c1ed"></a>412</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a5a647018557141a9ba9b631bc3af1233"><a name="a5a647018557141a9ba9b631bc3af1233"></a><a name="a5a647018557141a9ba9b631bc3af1233"></a>Precondition Failed</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a2effbf29858f4f34972837ab47a7f62f"><a name="a2effbf29858f4f34972837ab47a7f62f"></a><a name="a2effbf29858f4f34972837ab47a7f62f"></a>The server does not meet one of the preconditions that the requester puts on the request.</p>
</td>
</tr>
<tr id="rf2237d41356d42dab91450d17f6b6ea0"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a2273905bdec645a8847ca5644c7b0a94"><a name="a2273905bdec645a8847ca5644c7b0a94"></a><a name="a2273905bdec645a8847ca5644c7b0a94"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a02f39a141c604043af17c21fb16d4464"><a name="a02f39a141c604043af17c21fb16d4464"></a><a name="a02f39a141c604043af17c21fb16d4464"></a>Request Entity Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a8c4228577cae47d1870785384d56a05c"><a name="a8c4228577cae47d1870785384d56a05c"></a><a name="a8c4228577cae47d1870785384d56a05c"></a>The server refuses to process a request because the request entity is too large. The server may disable the connection to prevent the client from sending requests consecutively. If the server temporarily cannot process the request, the response will contain a Retry-After header field.</p>
</td>
</tr>
<tr id="r95624560275443bda2aba0fc7ec6d244"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a7fb439d359ba491bab86f29205148e7e"><a name="a7fb439d359ba491bab86f29205148e7e"></a><a name="a7fb439d359ba491bab86f29205148e7e"></a>414</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="ac260bc7ee9994c4badaa18a0763fd361"><a name="ac260bc7ee9994c4badaa18a0763fd361"></a><a name="ac260bc7ee9994c4badaa18a0763fd361"></a>Request-URI Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a24003774f6c2409aa9457370191b2e83"><a name="a24003774f6c2409aa9457370191b2e83"></a><a name="a24003774f6c2409aa9457370191b2e83"></a>The URI provided was too long for the server to process.</p>
</td>
</tr>
<tr id="rcfa31ac3b8d0452b959e4b5354329fca"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="aa4279e48b30842aba2c3233ab788f4b0"><a name="aa4279e48b30842aba2c3233ab788f4b0"></a><a name="aa4279e48b30842aba2c3233ab788f4b0"></a>415</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="af0db2d9ef823408fb4a827c2bdc3f27b"><a name="af0db2d9ef823408fb4a827c2bdc3f27b"></a><a name="af0db2d9ef823408fb4a827c2bdc3f27b"></a>Unsupported Media Type</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a5a578604b6a240a3b4bb567fb071a064"><a name="a5a578604b6a240a3b4bb567fb071a064"></a><a name="a5a578604b6a240a3b4bb567fb071a064"></a>The server does not support the media type in the request.</p>
</td>
</tr>
<tr id="raac8213d51b147bd80ed8dcdad0ac33e"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a7ed1f230ed6e42a089c884337464630b"><a name="a7ed1f230ed6e42a089c884337464630b"></a><a name="a7ed1f230ed6e42a089c884337464630b"></a>416</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a89ae0ac9e84b4f9db906a1ea2772a392"><a name="a89ae0ac9e84b4f9db906a1ea2772a392"></a><a name="a89ae0ac9e84b4f9db906a1ea2772a392"></a>Requested range not satisfiable</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a26df0c553883495eb675b988069156d6"><a name="a26df0c553883495eb675b988069156d6"></a><a name="a26df0c553883495eb675b988069156d6"></a>The requested range is invalid.</p>
</td>
</tr>
<tr id="rd0193d0870dc4776a5462962cbe18f7d"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a7288c46523414479b02651702a1dfad2"><a name="a7288c46523414479b02651702a1dfad2"></a><a name="a7288c46523414479b02651702a1dfad2"></a>417</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a2cd3fe564ad04b82bdf7629807d66bdc"><a name="a2cd3fe564ad04b82bdf7629807d66bdc"></a><a name="a2cd3fe564ad04b82bdf7629807d66bdc"></a>Expectation Failed</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="adb1c6d0389a34449a7eca22737302fa4"><a name="adb1c6d0389a34449a7eca22737302fa4"></a><a name="adb1c6d0389a34449a7eca22737302fa4"></a>The server fails to meet the requirements of the Expect request-header field.</p>
</td>
</tr>
<tr id="r2a786e322edc4ff2a44c5d2b39f60187"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a19c255b6ca7c40dd9631e5f6557d6799"><a name="a19c255b6ca7c40dd9631e5f6557d6799"></a><a name="a19c255b6ca7c40dd9631e5f6557d6799"></a>422</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a76bf20540ee74b80ba19ed515148cd00"><a name="a76bf20540ee74b80ba19ed515148cd00"></a><a name="a76bf20540ee74b80ba19ed515148cd00"></a>UnprocessableEntity</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a0e3b214780e6426abdc322a3d43a4245"><a name="a0e3b214780e6426abdc322a3d43a4245"></a><a name="a0e3b214780e6426abdc322a3d43a4245"></a>The request is well-formed but is unable to be processed due to semantic errors.</p>
</td>
</tr>
<tr id="r5da0f097d51a476c947dc84457dd57de"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a4a6666c8526b42c082785768b8fe4895"><a name="a4a6666c8526b42c082785768b8fe4895"></a><a name="a4a6666c8526b42c082785768b8fe4895"></a>429</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a77d660bce94f4478a5cd6ba4f1951f1d"><a name="a77d660bce94f4478a5cd6ba4f1951f1d"></a><a name="a77d660bce94f4478a5cd6ba4f1951f1d"></a>TooManyRequests</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="aa71dc3de3bca4a3e97c3ee6be3721f7d"><a name="aa71dc3de3bca4a3e97c3ee6be3721f7d"></a><a name="aa71dc3de3bca4a3e97c3ee6be3721f7d"></a>The client sends excessive requests to the server within a given time (exceeding the limit on the access frequency of the client), or the server receives excessive requests within a given time (beyond its processing capability). In this case, the client should repeat requests after the time specified in the Retry-After header of the response expires.</p>
</td>
</tr>
<tr id="r4fc00bbb9994435dae2f43d74bd95108"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a1c735411d36846d4b00242487f9e4f5f"><a name="a1c735411d36846d4b00242487f9e4f5f"></a><a name="a1c735411d36846d4b00242487f9e4f5f"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a5861766d33d94446b74c49103d681364"><a name="a5861766d33d94446b74c49103d681364"></a><a name="a5861766d33d94446b74c49103d681364"></a>InternalServerError</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a01c25870be78450d87488b35df5a0bf8"><a name="a01c25870be78450d87488b35df5a0bf8"></a><a name="a01c25870be78450d87488b35df5a0bf8"></a>The server is able to receive the request but it could not understand the request.</p>
</td>
</tr>
<tr id="rd33ef159958e4e22a853ba7ec55d12b3"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a55f265f082ab4550b14634e0ccbde6ef"><a name="a55f265f082ab4550b14634e0ccbde6ef"></a><a name="a55f265f082ab4550b14634e0ccbde6ef"></a>501</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="ac7a49ca89a0a402aab7d6e62ff7b99af"><a name="ac7a49ca89a0a402aab7d6e62ff7b99af"></a><a name="ac7a49ca89a0a402aab7d6e62ff7b99af"></a>Not Implemented</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a4aa84fcfa1b44ab89eb31806e1d35f3d"><a name="a4aa84fcfa1b44ab89eb31806e1d35f3d"></a><a name="a4aa84fcfa1b44ab89eb31806e1d35f3d"></a>The server does not support the requested function.</p>
</td>
</tr>
<tr id="r3f31d73d19c641a2b994776273cc56e9"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a25c4c2398c914a45a40134302ae7f139"><a name="a25c4c2398c914a45a40134302ae7f139"></a><a name="a25c4c2398c914a45a40134302ae7f139"></a>502</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="aa5ed5c3a15f74ac3a22411fd31a95f2a"><a name="aa5ed5c3a15f74ac3a22411fd31a95f2a"></a><a name="aa5ed5c3a15f74ac3a22411fd31a95f2a"></a>Bad Gateway</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a1950f6a6031649748df9482bcf952772"><a name="a1950f6a6031649748df9482bcf952772"></a><a name="a1950f6a6031649748df9482bcf952772"></a>The server acting as a gateway or proxy receives an invalid response from a remote server.</p>
</td>
</tr>
<tr id="r85cc3d19296d47b185a7330e9a8e7e03"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="a8ad37cc52e7244928183d625921d0118"><a name="a8ad37cc52e7244928183d625921d0118"></a><a name="a8ad37cc52e7244928183d625921d0118"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="ab92a103c0ad44eb39454c38ea1fef4af"><a name="ab92a103c0ad44eb39454c38ea1fef4af"></a><a name="ab92a103c0ad44eb39454c38ea1fef4af"></a>ServiceUnavailable</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a796ed830f4ca4816a5035bb44ba008d0"><a name="a796ed830f4ca4816a5035bb44ba008d0"></a><a name="a796ed830f4ca4816a5035bb44ba008d0"></a>The requested service is invalid.</p>
<p id="acd2d0be102004aac8109ab5e2fc32e6e"><a name="acd2d0be102004aac8109ab5e2fc32e6e"></a><a name="acd2d0be102004aac8109ab5e2fc32e6e"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="r4e2ab731793540349f6b8bba0d556db0"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="ab9afb6793fe8403e883d86515eb5136d"><a name="ab9afb6793fe8403e883d86515eb5136d"></a><a name="ab9afb6793fe8403e883d86515eb5136d"></a>504</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="a28c54f0f0fc8470a94b6e306a581deaa"><a name="a28c54f0f0fc8470a94b6e306a581deaa"></a><a name="a28c54f0f0fc8470a94b6e306a581deaa"></a>ServerTimeout</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="ac8379144fb9542baa57673a8af7a93fc"><a name="ac8379144fb9542baa57673a8af7a93fc"></a><a name="ac8379144fb9542baa57673a8af7a93fc"></a>The server could not return a timely response. The response will reach the client only if the request carries a timeout parameter.</p>
</td>
</tr>
<tr id="r8a02c404d2754fd884b9a333ec01a783"><td class="cellrowborder" valign="top" width="15.120000000000001%" headers="mcps1.2.4.1.1 "><p id="ad975953ef0a44ac6bbe1ed03982ec4f9"><a name="ad975953ef0a44ac6bbe1ed03982ec4f9"></a><a name="ad975953ef0a44ac6bbe1ed03982ec4f9"></a>505</p>
</td>
<td class="cellrowborder" valign="top" width="24.88%" headers="mcps1.2.4.1.2 "><p id="ab8e2b222b05c41cbbb9a7035a0aa72d9"><a name="ab8e2b222b05c41cbbb9a7035a0aa72d9"></a><a name="ab8e2b222b05c41cbbb9a7035a0aa72d9"></a>HTTP Version not supported</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a1a25cec109ae4b8eb8447433f47b65d9"><a name="a1a25cec109ae4b8eb8447433f47b65d9"></a><a name="a1a25cec109ae4b8eb8447433f47b65d9"></a>The server does not support the HTTP protocol version used in the request.</p>
</td>
</tr>
</tbody>
</table>

