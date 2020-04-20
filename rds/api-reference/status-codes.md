# Status Codes<a name="en-us_topic_0032488240"></a>

[Table 1](#table6516105501617)  describes status codes.

**Table  1**  Status codes

<a name="table6516105501617"></a>
<table><thead align="left"><tr id="row74075611167"><th class="cellrowborder" valign="top" width="14.14%" id="mcps1.2.4.1.1"><p id="p104055617169"><a name="p104055617169"></a><a name="p104055617169"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.2.4.1.2"><p id="p10401456181617"><a name="p10401456181617"></a><a name="p10401456181617"></a>Message</p>
</th>
<th class="cellrowborder" valign="top" width="61.62%" id="mcps1.2.4.1.3"><p id="p3407562164"><a name="p3407562164"></a><a name="p3407562164"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row54095618167"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p194014568167"><a name="p194014568167"></a><a name="p194014568167"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1240175620168"><a name="p1240175620168"></a><a name="p1240175620168"></a>Continue</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p134035691619"><a name="p134035691619"></a><a name="p134035691619"></a>The client should continue with its request.</p>
<p id="p1640155617161"><a name="p1640155617161"></a><a name="p1640155617161"></a>This interim response is used to inform the client that the initial part of the request has been received and has not yet been rejected by the server.</p>
</td>
</tr>
<tr id="row1341175641620"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p144117567164"><a name="p144117567164"></a><a name="p144117567164"></a>101</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p14419561169"><a name="p14419561169"></a><a name="p14419561169"></a>Switching Protocols</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1341356141617"><a name="p1341356141617"></a><a name="p1341356141617"></a>The protocol should be switched. The protocol can only be switched to a more advanced protocol.</p>
<p id="p141185619161"><a name="p141185619161"></a><a name="p141185619161"></a>For example, the current HTTP protocol is switched to a later version.</p>
</td>
</tr>
<tr id="row197941150132211"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p37957507220"><a name="p37957507220"></a><a name="p37957507220"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1079535082211"><a name="p1079535082211"></a><a name="p1079535082211"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1979525062212"><a name="p1979525062212"></a><a name="p1979525062212"></a>Request succeeded.</p>
</td>
</tr>
<tr id="row24175671615"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p184115651618"><a name="p184115651618"></a><a name="p184115651618"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p64165621612"><a name="p64165621612"></a><a name="p64165621612"></a>Created</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1941756181614"><a name="p1941756181614"></a><a name="p1941756181614"></a>The request for creating a resource or task has been fulfilled.</p>
</td>
</tr>
<tr id="row1541145621612"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p13411156131611"><a name="p13411156131611"></a><a name="p13411156131611"></a>202</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1441185615162"><a name="p1441185615162"></a><a name="p1441185615162"></a>Accepted</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p14114565169"><a name="p14114565169"></a><a name="p14114565169"></a>The request has been accepted, but the processing has not been completed.</p>
</td>
</tr>
<tr id="row2419565161"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p20411156131613"><a name="p20411156131613"></a><a name="p20411156131613"></a>203</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1441115671615"><a name="p1441115671615"></a><a name="p1441115671615"></a>Non-Authoritative Information</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p64165681610"><a name="p64165681610"></a><a name="p64165681610"></a>Unauthorized information. The request is successful.</p>
</td>
</tr>
<tr id="row74185615167"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p124113563168"><a name="p124113563168"></a><a name="p124113563168"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p144105611169"><a name="p144105611169"></a><a name="p144105611169"></a>NoContent</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1441105619163"><a name="p1441105619163"></a><a name="p1441105619163"></a>The server has successfully processed the request, but has not returned any content.</p>
<p id="p841165631610"><a name="p841165631610"></a><a name="p841165631610"></a>The status code is returned in response to an HTTP OPTIONS request.</p>
</td>
</tr>
<tr id="row441156191612"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p142356161616"><a name="p142356161616"></a><a name="p142356161616"></a>205</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1142165614169"><a name="p1142165614169"></a><a name="p1142165614169"></a>Reset Content</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p13421056191616"><a name="p13421056191616"></a><a name="p13421056191616"></a>The server has fulfilled the request, but the requester is required to reset the content.</p>
</td>
</tr>
<tr id="row1542105611162"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1042185613162"><a name="p1042185613162"></a><a name="p1042185613162"></a>206</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1342656171611"><a name="p1342656171611"></a><a name="p1342656171611"></a>Partial Content</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p114255618163"><a name="p114255618163"></a><a name="p114255618163"></a>The server has processed certain GET requests.</p>
</td>
</tr>
<tr id="row1842656161613"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p194245601619"><a name="p194245601619"></a><a name="p194245601619"></a>300</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p164216565162"><a name="p164216565162"></a><a name="p164216565162"></a>Multiple Choices</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p84235661610"><a name="p84235661610"></a><a name="p84235661610"></a>There are multiple options for the location of the requested resource. The response contains a list of resource characteristics and addresses from which the user or user agent (such as a browser) can choose the most appropriate one.</p>
</td>
</tr>
<tr id="row542956171617"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p16425565164"><a name="p16425565164"></a><a name="p16425565164"></a>301</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p742145661617"><a name="p742145661617"></a><a name="p742145661617"></a>Moved Permanently</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p9428566164"><a name="p9428566164"></a><a name="p9428566164"></a>The requested resource has been assigned a new permanent URI, and the new URI is contained in the response.</p>
</td>
</tr>
<tr id="row34211569160"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p64295681619"><a name="p64295681619"></a><a name="p64295681619"></a>302</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p542105681616"><a name="p542105681616"></a><a name="p542105681616"></a>Found</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p14235601611"><a name="p14235601611"></a><a name="p14235601611"></a>The requested resource was temporarily moved.</p>
</td>
</tr>
<tr id="row5421156131612"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p15421556111618"><a name="p15421556111618"></a><a name="p15421556111618"></a>303</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p7422565164"><a name="p7422565164"></a><a name="p7422565164"></a>See Other</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1743135671616"><a name="p1743135671616"></a><a name="p1743135671616"></a>The response to the request can be found under a different URI and should be retrieved using a GET or POST method.</p>
</td>
</tr>
<tr id="row4433561165"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p2043135661616"><a name="p2043135661616"></a><a name="p2043135661616"></a>304</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p17432568165"><a name="p17432568165"></a><a name="p17432568165"></a>Not Modified</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1743155621611"><a name="p1743155621611"></a><a name="p1743155621611"></a>The requested resource has not been modified. In such a case, there is no need to retransmit the resource since the client still has a previously-downloaded copy.</p>
</td>
</tr>
<tr id="row14318560165"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1943756141611"><a name="p1943756141611"></a><a name="p1943756141611"></a>305</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p543856161612"><a name="p543856161612"></a><a name="p543856161612"></a>Use Proxy</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1343356131611"><a name="p1343356131611"></a><a name="p1343356131611"></a>The requested resource must be accessed through a proxy.</p>
</td>
</tr>
<tr id="row1343556191618"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1343105611613"><a name="p1343105611613"></a><a name="p1343105611613"></a>306</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p54320561165"><a name="p54320561165"></a><a name="p54320561165"></a>Unused</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p15434561168"><a name="p15434561168"></a><a name="p15434561168"></a>The HTTP status code is no longer used.</p>
</td>
</tr>
<tr id="row144313569161"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1243156161619"><a name="p1243156161619"></a><a name="p1243156161619"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p194310566162"><a name="p194310566162"></a><a name="p194310566162"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p543155691617"><a name="p543155691617"></a><a name="p543155691617"></a>Invalid request.</p>
<p id="p18431256131614"><a name="p18431256131614"></a><a name="p18431256131614"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="row114325612162"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p543135691611"><a name="p543135691611"></a><a name="p543135691611"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p243155620166"><a name="p243155620166"></a><a name="p243155620166"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p164315610167"><a name="p164315610167"></a><a name="p164315610167"></a>The status code is returned after the client provides the authentication information, indicating that the authentication information is incorrect or invalid.</p>
</td>
</tr>
<tr id="row164435615168"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p84475618162"><a name="p84475618162"></a><a name="p84475618162"></a>402</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1644145671615"><a name="p1644145671615"></a><a name="p1644145671615"></a>Payment Required</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p544256181617"><a name="p544256181617"></a><a name="p544256181617"></a>This status code is reserved for future use.</p>
</td>
</tr>
<tr id="row20442056201613"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p144205611619"><a name="p144205611619"></a><a name="p144205611619"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p944205613169"><a name="p944205613169"></a><a name="p944205613169"></a>Forbidden</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p134415681611"><a name="p134415681611"></a><a name="p134415681611"></a>The server understood the request, but is refusing to fulfill it.</p>
<p id="p74414563168"><a name="p74414563168"></a><a name="p74414563168"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="row124475618164"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1244056141614"><a name="p1244056141614"></a><a name="p1244056141614"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p194415661619"><a name="p194415661619"></a><a name="p194415661619"></a>NotFound</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p9447562169"><a name="p9447562169"></a><a name="p9447562169"></a>The requested resource cannot be found.</p>
<p id="p94495613162"><a name="p94495613162"></a><a name="p94495613162"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="row18441356171619"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1344356201616"><a name="p1344356201616"></a><a name="p1344356201616"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p134475631614"><a name="p134475631614"></a><a name="p134475631614"></a>MethodNotAllowed</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p544105641612"><a name="p544105641612"></a><a name="p544105641612"></a>The method specified in the request is not supported for the requested resource.</p>
<p id="p164465612162"><a name="p164465612162"></a><a name="p164465612162"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="row174419565161"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p34425681610"><a name="p34425681610"></a><a name="p34425681610"></a>406</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p644195621611"><a name="p644195621611"></a><a name="p644195621611"></a>Not Acceptable</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p12441656161616"><a name="p12441656161616"></a><a name="p12441656161616"></a>The server cannot fulfill the request according to the content characteristics of the request.</p>
</td>
</tr>
<tr id="row194515568164"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p84515614162"><a name="p84515614162"></a><a name="p84515614162"></a>407</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p164505691619"><a name="p164505691619"></a><a name="p164505691619"></a>Proxy Authentication Required</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1445115671617"><a name="p1445115671617"></a><a name="p1445115671617"></a>This status code is similar to 401, but indicates that the client must first authenticate itself with the proxy.</p>
</td>
</tr>
<tr id="row1045456131610"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1945556181618"><a name="p1945556181618"></a><a name="p1945556181618"></a>408</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p11451156131610"><a name="p11451156131610"></a><a name="p11451156131610"></a>Request Time-out</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1345155614166"><a name="p1345155614166"></a><a name="p1345155614166"></a>The server timed out waiting for the request.</p>
<p id="p64575613166"><a name="p64575613166"></a><a name="p64575613166"></a>The client may repeat the request without modifications at any later time.</p>
</td>
</tr>
<tr id="row1445185681615"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p04515612168"><a name="p04515612168"></a><a name="p04515612168"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1458563163"><a name="p1458563163"></a><a name="p1458563163"></a>Conflict</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p745456161612"><a name="p745456161612"></a><a name="p745456161612"></a>The request could not be processed due to a conflict.</p>
<p id="p174515612163"><a name="p174515612163"></a><a name="p174515612163"></a>This status code indicates that the resource that the client attempts to create already exits, or the request fails to be processed because of the update of the conflict request.</p>
</td>
</tr>
<tr id="row74511561167"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p445135616167"><a name="p445135616167"></a><a name="p445135616167"></a>410</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p445175619164"><a name="p445175619164"></a><a name="p445175619164"></a>Gone</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p154535618162"><a name="p154535618162"></a><a name="p154535618162"></a>The requested resource is no longer available.</p>
<p id="p1645115621617"><a name="p1645115621617"></a><a name="p1645115621617"></a>The requested resource has been deleted permanently.</p>
</td>
</tr>
<tr id="row10451856141616"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p12451756151619"><a name="p12451756151619"></a><a name="p12451756151619"></a>411</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1045105612163"><a name="p1045105612163"></a><a name="p1045105612163"></a>Length Required</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p3452563165"><a name="p3452563165"></a><a name="p3452563165"></a>The server refuses to process the request without a defined Content-Length.</p>
</td>
</tr>
<tr id="row19461256161612"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p2461561166"><a name="p2461561166"></a><a name="p2461561166"></a>412</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p114665631619"><a name="p114665631619"></a><a name="p114665631619"></a>Precondition Failed</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p194615616168"><a name="p194615616168"></a><a name="p194615616168"></a>The server does not meet one of the preconditions that the requester puts on the request.</p>
</td>
</tr>
<tr id="row1946195610168"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1046115612161"><a name="p1046115612161"></a><a name="p1046115612161"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p44611565161"><a name="p44611565161"></a><a name="p44611565161"></a>Request Entity Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p12461563166"><a name="p12461563166"></a><a name="p12461563166"></a>The request is larger than that a server is able to process. The server may close the connection to prevent the client from continuing the request. If the server temporarily cannot process the request, the response will contain a Retry-After header field.</p>
</td>
</tr>
<tr id="row1446456161619"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p194645618169"><a name="p194645618169"></a><a name="p194645618169"></a>414</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p19462569164"><a name="p19462569164"></a><a name="p19462569164"></a>Request-URI Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p204675641612"><a name="p204675641612"></a><a name="p204675641612"></a>The URI provided was too long for the server to process.</p>
</td>
</tr>
<tr id="row1446956111612"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p15461556181612"><a name="p15461556181612"></a><a name="p15461556181612"></a>415</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p134614562167"><a name="p134614562167"></a><a name="p134614562167"></a>Unsupported Media Type</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p94695661614"><a name="p94695661614"></a><a name="p94695661614"></a>The server is unable to process the media format in the request.</p>
</td>
</tr>
<tr id="row646145611168"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p8469565167"><a name="p8469565167"></a><a name="p8469565167"></a>416</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p204611569167"><a name="p204611569167"></a><a name="p204611569167"></a>Requested range not satisfied</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1246256151615"><a name="p1246256151615"></a><a name="p1246256151615"></a>The requested range is invalid.</p>
</td>
</tr>
<tr id="row546165619163"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1468563162"><a name="p1468563162"></a><a name="p1468563162"></a>417</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p3476563161"><a name="p3476563161"></a><a name="p3476563161"></a>Expectation Failed</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p114714566164"><a name="p114714566164"></a><a name="p114714566164"></a>The server fails to meet the requirements of the Expect request-header field.</p>
</td>
</tr>
<tr id="row9471562163"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1047125615163"><a name="p1047125615163"></a><a name="p1047125615163"></a>422</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1847145681613"><a name="p1847145681613"></a><a name="p1847145681613"></a>UnprocessableEntity</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p747125610168"><a name="p747125610168"></a><a name="p747125610168"></a>The request is well-formed but is unable to be processed due to semantic errors.</p>
</td>
</tr>
<tr id="row1047145618163"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p94725611618"><a name="p94725611618"></a><a name="p94725611618"></a>429</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p647165671611"><a name="p647165671611"></a><a name="p647165671611"></a>TooManyRequests</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p74715614165"><a name="p74715614165"></a><a name="p74715614165"></a>The client has sent more requests than its rate limit is allowed within a given amount of time, or the server has received more requests than it is able to process within a given amount of time. In this case, it is advisable for the client to re-initiate requests after the time specified in the Retry-After header of the response expires.</p>
</td>
</tr>
<tr id="row134720562168"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1147155617166"><a name="p1147155617166"></a><a name="p1147155617166"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p84712566167"><a name="p84712566167"></a><a name="p84712566167"></a>InternalServerError</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1547185681616"><a name="p1547185681616"></a><a name="p1547185681616"></a>The server is able to receive the request but it could not understand the request.</p>
</td>
</tr>
<tr id="row1947105661617"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p174785614169"><a name="p174785614169"></a><a name="p174785614169"></a>501</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p194755618167"><a name="p194755618167"></a><a name="p194755618167"></a>Not Implemented</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p2471564167"><a name="p2471564167"></a><a name="p2471564167"></a>The server does not support the requested function.</p>
</td>
</tr>
<tr id="row24714564164"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p447145681618"><a name="p447145681618"></a><a name="p447145681618"></a>502</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1748156191612"><a name="p1748156191612"></a><a name="p1748156191612"></a>Bad Gateway</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1048195617169"><a name="p1048195617169"></a><a name="p1048195617169"></a>The server acting as a gateway or proxy receives an invalid response from a remote server.</p>
</td>
</tr>
<tr id="row8481656161613"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p348956201618"><a name="p348956201618"></a><a name="p348956201618"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p54845611160"><a name="p54845611160"></a><a name="p54845611160"></a>ServiceUnavailable</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1048256161618"><a name="p1048256161618"></a><a name="p1048256161618"></a>The requested service is invalid.</p>
<p id="p048165651617"><a name="p048165651617"></a><a name="p048165651617"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="row748175671615"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p194865661616"><a name="p194865661616"></a><a name="p194865661616"></a>504</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1748105616169"><a name="p1748105616169"></a><a name="p1748105616169"></a>ServerTimeout</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p64825691614"><a name="p64825691614"></a><a name="p64825691614"></a>The request cannot be fulfilled within a given time. The response will reach the client only if the request carries a timeout parameter.</p>
</td>
</tr>
<tr id="row94812562164"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p124855621610"><a name="p124855621610"></a><a name="p124855621610"></a>505</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1748956161618"><a name="p1748956161618"></a><a name="p1748956161618"></a>HTTP Version not supported</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p448115617163"><a name="p448115617163"></a><a name="p448115617163"></a>The server does not support the HTTP protocol version used in the request.</p>
</td>
</tr>
</tbody>
</table>

