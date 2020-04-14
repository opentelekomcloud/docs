# Status Codes<a name="css_03_0012"></a>

[Table 1](#en-us_topic_0171139321_en-us_topic_0122640420_table62859252)  describes status codes.

**Table  1**  Status code description

<a name="en-us_topic_0171139321_en-us_topic_0122640420_table62859252"></a>
<table><thead align="left"><tr id="en-us_topic_0171139321_en-us_topic_0122640420_row38747780"><th class="cellrowborder" valign="top" width="14.14%" id="mcps1.2.4.1.1"><p id="en-us_topic_0171139321_en-us_topic_0122640420_p51562446"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p51562446"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p51562446"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0171139321_en-us_topic_0122640420_p15808580"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p15808580"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p15808580"></a>Message</p>
</th>
<th class="cellrowborder" valign="top" width="61.62%" id="mcps1.2.4.1.3"><p id="en-us_topic_0171139321_en-us_topic_0122640420_p5426640"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p5426640"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p5426640"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0171139321_en-us_topic_0122640420_row36904663"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p36487747"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p36487747"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p36487747"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p2717564"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p2717564"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p2717564"></a>Continue</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p18796137"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p18796137"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p18796137"></a>The client should continue sending the request.</p>
<p id="en-us_topic_0171139321_en-us_topic_0122640420_p34947511"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p34947511"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p34947511"></a>This interim response is used to inform the client that the initial part of the request has been received and has not yet been rejected by the server.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row46092147"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p42476417"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p42476417"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p42476417"></a>101</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p18037756"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p18037756"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p18037756"></a>Switching Protocols</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p51772107"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p51772107"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p51772107"></a>Switching protocols. The target protocol must be later than the source protocol.</p>
<p id="en-us_topic_0171139321_en-us_topic_0122640420_p63295782"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p63295782"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p63295782"></a>For example, the current HTTPS protocol is switched to a later version.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_row641324316518"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_p341311431758"><a name="en-us_topic_0171139321_p341311431758"></a><a name="en-us_topic_0171139321_p341311431758"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_p134136431055"><a name="en-us_topic_0171139321_p134136431055"></a><a name="en-us_topic_0171139321_p134136431055"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_p134136431458"><a name="en-us_topic_0171139321_p134136431458"></a><a name="en-us_topic_0171139321_p134136431458"></a>The request is processed successfully.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row32791127"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p38835591"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p38835591"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p38835591"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p58675139"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p58675139"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p58675139"></a>Created</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p55065844"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p55065844"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p55065844"></a>The request for creating a resource has been fulfilled.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row25830556"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p11900311"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p11900311"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p11900311"></a>202</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p24401147"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p24401147"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p24401147"></a>Accepted</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p30335854"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p30335854"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p30335854"></a>The request has been accepted, but the processing has not been completed.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row4587238"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p36022006"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p36022006"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p36022006"></a>203</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p32101354"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p32101354"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p32101354"></a>Non-Authoritative Information</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p50072875"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p50072875"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p50072875"></a>Unauthorized information. The request is successful.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row48002691"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p63012769"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p63012769"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p63012769"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p3760704"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p3760704"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p3760704"></a>NoContent</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p36181640"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p36181640"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p36181640"></a>The server has successfully processed the request, but has not returned any content.</p>
<p id="en-us_topic_0171139321_en-us_topic_0122640420_p57199306"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p57199306"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p57199306"></a>The status code is returned in response to an HTTPS OPTIONS request.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row45031712"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p23690032"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p23690032"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p23690032"></a>205</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p39844449"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p39844449"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p39844449"></a>Reset Content</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p6174938"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p6174938"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p6174938"></a>The server has fulfilled the request, but the requester is required to reset the content.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row55574450"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p5236587"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p5236587"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p5236587"></a>206</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p21510401"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p21510401"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p21510401"></a>Partial Content</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p64620891"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p64620891"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p64620891"></a>The server has successfully processed a part of the GET request.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row44717109"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p65316081"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p65316081"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p65316081"></a>300</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p56111205"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p56111205"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p56111205"></a>Multiple Choices</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p48713786"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p48713786"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p48713786"></a>There are multiple options for the location of the requested resource. The response contains a list of resource characteristics and addresses from which the user or user agent (such as a browser) can choose the most appropriate one.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row35770896"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p11761497"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p11761497"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p11761497"></a>301</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p13157206"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p13157206"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p13157206"></a>Moved Permanently</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p59100784"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p59100784"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p59100784"></a>The requested resource has been assigned a new permanent URI, and the new URI is contained in the response.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row62145011"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p581122"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p581122"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p581122"></a>302</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p47070946"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p47070946"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p47070946"></a>Found</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p54650299"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p54650299"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p54650299"></a>The requested resource was temporarily moved.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row22090644"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p44511700"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p44511700"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p44511700"></a>303</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p48677920"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p48677920"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p48677920"></a>See Other</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p50597473"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p50597473"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p50597473"></a>Retrieve a location. </p>
<p id="en-us_topic_0171139321_en-us_topic_0122640420_p52724081"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p52724081"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p52724081"></a>The response to the request can be found under a different URI, and should be retrieved using a GET or POST method.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row4754687"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p49585377"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p49585377"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p49585377"></a>304</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p56992624"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p56992624"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p56992624"></a>Not Modified</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p52999827"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p52999827"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p52999827"></a>The requested resource has not been modified. In such case, there is no need to retransmit the resource since the client still has a previously-downloaded copy.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row7236400"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p49277517"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p49277517"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p49277517"></a>305</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p32055922"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p32055922"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p32055922"></a>Use Proxy</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p46392904"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p46392904"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p46392904"></a>The requested resource must be accessed through a proxy.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row14882957"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p64668846"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p64668846"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p64668846"></a>306</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p3685205"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p3685205"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p3685205"></a>Unused</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p30066151"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p30066151"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p30066151"></a>The HTTPS status code is no longer used.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row2159909"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p40734917"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p40734917"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p40734917"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p11193990"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p11193990"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p11193990"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p34297999"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p34297999"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p34297999"></a>Invalid request.</p>
<p id="en-us_topic_0171139321_en-us_topic_0122640420_p40246543"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p40246543"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p40246543"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row26674569"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p13156508"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p13156508"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p13156508"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p59044207"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p59044207"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p59044207"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p17851434"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p17851434"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p17851434"></a>The status code is returned after the client provides the authentication information, indicating that the authentication information provided by the client is incorrect or invalid.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row26445182"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p61685034"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p61685034"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p61685034"></a>402</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p30431825"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p30431825"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p30431825"></a>Payment Required</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p49058781"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p49058781"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p49058781"></a>Reserved for future use.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row38875853"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p61936363"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p61936363"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p61936363"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p50789473"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p50789473"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p50789473"></a>Forbidden</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p20306648"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p20306648"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p20306648"></a>The request has been rejected.</p>
<p id="en-us_topic_0171139321_en-us_topic_0122640420_p48542107"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p48542107"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p48542107"></a>The server has received and understood the request; yet it refused to respond, because the request is set to deny access. Do not retry the request before modification.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row34225783"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p20825063"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p20825063"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p20825063"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p9108560"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p9108560"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p9108560"></a>NotFound</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p66704729"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p66704729"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p66704729"></a>The requested resource cannot be found.</p>
<p id="en-us_topic_0171139321_en-us_topic_0122640420_p63471649"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p63471649"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p63471649"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row34373930"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p32824940"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p32824940"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p32824940"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p41574470"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p41574470"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p41574470"></a>MethodNotAllowed</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p12088929"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p12088929"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p12088929"></a>The method specified in the request is not supported for the requested resource.</p>
<p id="en-us_topic_0171139321_en-us_topic_0122640420_p41691502"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p41691502"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p41691502"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row39679205"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p59899000"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p59899000"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p59899000"></a>406</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p19980869"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p19980869"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p19980869"></a>Not Acceptable</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p7837682"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p7837682"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p7837682"></a>The server cannot fulfill the request according to the content characteristics of the request.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row3430276"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p9416933"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p9416933"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p9416933"></a>407</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p24574074"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p24574074"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p24574074"></a>Proxy Authentication Required</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p44342955"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p44342955"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p44342955"></a>This status code is similar to 401, but indicates that the client must first authenticate itself with the proxy.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row63542282"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p46651250"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p46651250"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p46651250"></a>408</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p20654890"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p20654890"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p20654890"></a>Request Time-out</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p62433370"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p62433370"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p62433370"></a>The request timed out.</p>
<p id="en-us_topic_0171139321_en-us_topic_0122640420_p25029423"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p25029423"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p25029423"></a>The client may repeat the request without modifications at any time later.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row23938219"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p59947588"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p59947588"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p59947588"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p23916494"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p23916494"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p23916494"></a>Conflict</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p58187889"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p58187889"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p58187889"></a>The request could not be processed due to a conflict.</p>
<p id="en-us_topic_0171139321_en-us_topic_0122640420_p53928955"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p53928955"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p53928955"></a>This status code indicates that the resource that the client attempts to create already exits, or the request fails to be processed because of the update of the conflict request.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row15598548"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p55522847"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p55522847"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p55522847"></a>410</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p1056763"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p1056763"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p1056763"></a>Gone</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p18488975"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p18488975"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p18488975"></a>The requested resource is no longer available.</p>
<p id="en-us_topic_0171139321_en-us_topic_0122640420_p32183054"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p32183054"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p32183054"></a>The status code indicates that the requested resource has been deleted.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row21212036"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p40453378"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p40453378"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p40453378"></a>411</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p55498160"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p55498160"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p55498160"></a>Length Required</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p66165942"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p66165942"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p66165942"></a>The server refuses to process the request without a defined <strong id="b7813104844218"><a name="b7813104844218"></a><a name="b7813104844218"></a>Content-Length</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row58622570"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p50807720"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p50807720"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p50807720"></a>412</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p21784659"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p21784659"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p21784659"></a>Precondition Failed</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p19726930"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p19726930"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p19726930"></a>The server does not meet one of the preconditions that the requester puts on the request.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row43324645"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p19635326"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p19635326"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p19635326"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p46957535"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p46957535"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p46957535"></a>Request Entity Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p45463985"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p45463985"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p45463985"></a>The server is refusing to process a request because the request entity is too large for the server to process. The server may disable the connection to prevent the client from sending requests consecutively. If the server is only temporarily unable to process the request, the response will contain a <strong id="b1762872214319"><a name="b1762872214319"></a><a name="b1762872214319"></a>Retry-After</strong> header field.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row6522683"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p58575353"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p58575353"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p58575353"></a>414</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p46983163"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p46983163"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p46983163"></a>Request-URI Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p47539882"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p47539882"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p47539882"></a>The URI provided was too long for the server to process.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row25205757"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p28400474"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p28400474"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p28400474"></a>415</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p18737047"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p18737047"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p18737047"></a>Unsupported Media Type</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p41305820"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p41305820"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p41305820"></a>The server does not support the media type in the request.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row36208066"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p47172199"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p47172199"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p47172199"></a>416</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p62851752"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p62851752"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p62851752"></a>Requested range not satisfiable</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p57827183"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p57827183"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p57827183"></a>The requested range is invalid.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row50682599"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p11649839"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p11649839"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p11649839"></a>417</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p4112879"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p4112879"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p4112879"></a>Expectation Failed</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p64707792"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p64707792"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p64707792"></a>The server fails to meet the requirements of the <strong id="b147175795920"><a name="b147175795920"></a><a name="b147175795920"></a>Expect</strong> request-header field.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row45499220"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p61558217"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p61558217"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p61558217"></a>422</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p20159666"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p20159666"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p20159666"></a>UnprocessableEntity</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p22320248"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p22320248"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p22320248"></a>The request is well-formed but is unable to be processed due to semantic errors.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row66664505"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p31115796"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p31115796"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p31115796"></a>429</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p37351552"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p37351552"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p37351552"></a>TooManyRequests</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p5576868"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p5576868"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p5576868"></a>The client has sent more requests than its rate limit is allowed within a given amount of time, or the server has received more requests than it is able to process within a given amount of time. In this case, the client should resend the request after the time specified in the <strong id="b7790181012442"><a name="b7790181012442"></a><a name="b7790181012442"></a>Retry-After</strong> header of the response has elapsed. </p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row50191819"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p39005559"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p39005559"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p39005559"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p5333744"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p5333744"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p5333744"></a>InternalServerError</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p29380125"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p29380125"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p29380125"></a>The server is able to receive but unable to understand the request.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row63094539"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p10384034"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p10384034"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p10384034"></a>501</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p35800417"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p35800417"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p35800417"></a>Not Implemented</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p14152689"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p14152689"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p14152689"></a>The server does not support the requested function.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row60265343"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p49654603"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p49654603"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p49654603"></a>502</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p62599867"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p62599867"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p62599867"></a>Bad Gateway</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p37424439"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p37424439"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p37424439"></a>The server is acting as a gateway or proxy and receives an invalid request from a remote server.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row1275638"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p36217840"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p36217840"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p36217840"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p47963947"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p47963947"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p47963947"></a>ServiceUnavailable</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p59874511"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p59874511"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p59874511"></a>The requested service is invalid.</p>
<p id="en-us_topic_0171139321_en-us_topic_0122640420_p1999687"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p1999687"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p1999687"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row17997186"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p48485999"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p48485999"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p48485999"></a>504</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p35051836"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p35051836"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p35051836"></a>ServerTimeout</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p20626449"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p20626449"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p20626449"></a>The request cannot be fulfilled within a given time. This status code is returned to the client only when the <strong id="en-us_topic_0171139321_b842352706162338"><a name="en-us_topic_0171139321_b842352706162338"></a><a name="en-us_topic_0171139321_b842352706162338"></a>Timeout</strong> parameter is specified in the request.</p>
</td>
</tr>
<tr id="en-us_topic_0171139321_en-us_topic_0122640420_row51420319"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p4296276"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p4296276"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p4296276"></a>505</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p12454053"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p12454053"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p12454053"></a>HTTP Version not supported</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0171139321_en-us_topic_0122640420_p2145404"><a name="en-us_topic_0171139321_en-us_topic_0122640420_p2145404"></a><a name="en-us_topic_0171139321_en-us_topic_0122640420_p2145404"></a>The server does not support the HTTPS protocol version used in the request.</p>
</td>
</tr>
</tbody>
</table>

