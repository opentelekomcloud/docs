# Status Code<a name="EN-US_TOPIC_0128036883"></a>

[Table 1](#table5210141351517)  lists status codes.

**Table  1**  Status codes

<a name="table5210141351517"></a>
<table><thead align="left"><tr id="row15711913161515"><th class="cellrowborder" valign="top" width="14.14%" id="mcps1.2.4.1.1"><p id="p257261312159"><a name="p257261312159"></a><a name="p257261312159"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.2.4.1.2"><p id="p2057218133157"><a name="p2057218133157"></a><a name="p2057218133157"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="61.62%" id="mcps1.2.4.1.3"><p id="p457261311152"><a name="p457261311152"></a><a name="p457261311152"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row135722013141514"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1357261371516"><a name="p1357261371516"></a><a name="p1357261371516"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1657291319157"><a name="p1657291319157"></a><a name="p1657291319157"></a>Continue</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p20572141361517"><a name="p20572141361517"></a><a name="p20572141361517"></a>The server has received the initial part of the request and the client should continue to send the remaining part.</p>
</td>
</tr>
<tr id="row1357214138150"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p155726134152"><a name="p155726134152"></a><a name="p155726134152"></a>101</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p85721713121512"><a name="p85721713121512"></a><a name="p85721713121512"></a>Switching Protocols</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p45726139156"><a name="p45726139156"></a><a name="p45726139156"></a>The requester has asked the server to switch protocols and the server has agreed to do so. The target protocol must be more advanced than the source protocol.</p>
<p id="p95728136153"><a name="p95728136153"></a><a name="p95728136153"></a>For example, the current HTTP protocol is switched to a later version of HTTP.</p>
</td>
</tr>
<tr id="row7170152184816"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p19171102119481"><a name="p19171102119481"></a><a name="p19171102119481"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p6171162144811"><a name="p6171162144811"></a><a name="p6171162144811"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p17171162116486"><a name="p17171162116486"></a><a name="p17171162116486"></a>Request sent successfully.</p>
</td>
</tr>
<tr id="row45721139153"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p6572151316155"><a name="p6572151316155"></a><a name="p6572151316155"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p0573713191517"><a name="p0573713191517"></a><a name="p0573713191517"></a>Created</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p7573813181519"><a name="p7573813181519"></a><a name="p7573813181519"></a>The request has been fulfilled, resulting in the creation of a new resource.</p>
</td>
</tr>
<tr id="row85737134158"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p10573713161515"><a name="p10573713161515"></a><a name="p10573713161515"></a>202</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p15731213111517"><a name="p15731213111517"></a><a name="p15731213111517"></a>Accepted</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p957381310155"><a name="p957381310155"></a><a name="p957381310155"></a>The request has been accepted for processing, but the processing has not been completed.</p>
</td>
</tr>
<tr id="row195732139151"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p857391310155"><a name="p857391310155"></a><a name="p857391310155"></a>203</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p95731713141510"><a name="p95731713141510"></a><a name="p95731713141510"></a>Non-Authoritative Information</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1957361317158"><a name="p1957361317158"></a><a name="p1957361317158"></a>The request has been fulfilled.</p>
</td>
</tr>
<tr id="row16573101316152"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p6574101311155"><a name="p6574101311155"></a><a name="p6574101311155"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p65741613161513"><a name="p65741613161513"></a><a name="p65741613161513"></a>NoContent</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p957417130157"><a name="p957417130157"></a><a name="p957417130157"></a>The server has successfully processed the request, but is not returning any response body.</p>
<p id="p657481351516"><a name="p657481351516"></a><a name="p657481351516"></a>The status code is returned in response to an HTTP OPTIONS request.</p>
</td>
</tr>
<tr id="row1157417138159"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p7574111391512"><a name="p7574111391512"></a><a name="p7574111391512"></a>205</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p6574413171515"><a name="p6574413171515"></a><a name="p6574413171515"></a>Reset Content</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p9574171319159"><a name="p9574171319159"></a><a name="p9574171319159"></a>The server has fulfilled the request, but the requester is required to reset the content.</p>
</td>
</tr>
<tr id="row195741313131513"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p19574913201516"><a name="p19574913201516"></a><a name="p19574913201516"></a>206</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p19574201361514"><a name="p19574201361514"></a><a name="p19574201361514"></a>Partial Content</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p12575161321512"><a name="p12575161321512"></a><a name="p12575161321512"></a>The server has successfully processed a part of the GET request.</p>
</td>
</tr>
<tr id="row35751013151513"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p18575113181517"><a name="p18575113181517"></a><a name="p18575113181517"></a>300</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1457515131158"><a name="p1457515131158"></a><a name="p1457515131158"></a>Multiple Choices</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p125755138157"><a name="p125755138157"></a><a name="p125755138157"></a>There are multiple options for the requested resource. For example, this code could be used to present a list of resource characteristics and addresses from which the client such as a browser may choose.</p>
</td>
</tr>
<tr id="row057516133151"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p13575181381514"><a name="p13575181381514"></a><a name="p13575181381514"></a>301</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p9575151316153"><a name="p9575151316153"></a><a name="p9575151316153"></a>Moved Permanently</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p145751613151515"><a name="p145751613151515"></a><a name="p145751613151515"></a>This and all future requests have been permanently moved to the given URI indicated in this response.</p>
</td>
</tr>
<tr id="row4575181341512"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p13575413141519"><a name="p13575413141519"></a><a name="p13575413141519"></a>302</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1575121314159"><a name="p1575121314159"></a><a name="p1575121314159"></a>Found</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p115761813191513"><a name="p115761813191513"></a><a name="p115761813191513"></a>The requested resource was temporarily moved.</p>
</td>
</tr>
<tr id="row13576413171515"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p25761813101514"><a name="p25761813101514"></a><a name="p25761813101514"></a>303</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p2057661371513"><a name="p2057661371513"></a><a name="p2057661371513"></a>See Other</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p9576191319155"><a name="p9576191319155"></a><a name="p9576191319155"></a>The response to the request can be found under another URI using a GET or POST method.</p>
</td>
</tr>
<tr id="row1557651311516"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p19576613141515"><a name="p19576613141515"></a><a name="p19576613141515"></a>304</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p18576913161512"><a name="p18576913161512"></a><a name="p18576913161512"></a>Not Modified</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p19576181301510"><a name="p19576181301510"></a><a name="p19576181301510"></a>The requested resource has not been modified. When the server returns this status code, it does not return any resources.</p>
</td>
</tr>
<tr id="row14576161310152"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p13576201391511"><a name="p13576201391511"></a><a name="p13576201391511"></a>305</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1857713133154"><a name="p1857713133154"></a><a name="p1857713133154"></a>Use Proxy</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p3577101351510"><a name="p3577101351510"></a><a name="p3577101351510"></a>The requested resource is available only through a proxy.</p>
</td>
</tr>
<tr id="row15577101371510"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p557731341518"><a name="p557731341518"></a><a name="p557731341518"></a>306</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p16577131316152"><a name="p16577131316152"></a><a name="p16577131316152"></a>Unused</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p457731351519"><a name="p457731351519"></a><a name="p457731351519"></a>This HTTP status code is no longer used.</p>
</td>
</tr>
<tr id="row2577171341515"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p13577313161515"><a name="p13577313161515"></a><a name="p13577313161515"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p155773131154"><a name="p155773131154"></a><a name="p155773131154"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p357718136158"><a name="p357718136158"></a><a name="p357718136158"></a>Invalid request.</p>
<p id="p6577171331517"><a name="p6577171331517"></a><a name="p6577171331517"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="row1857831361512"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p2578313161516"><a name="p2578313161516"></a><a name="p2578313161516"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p357951361512"><a name="p357951361512"></a><a name="p357951361512"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p65791013141518"><a name="p65791013141518"></a><a name="p65791013141518"></a>The authorization information provided by the client is incorrect or invalid.</p>
</td>
</tr>
<tr id="row1957917137154"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1157941310159"><a name="p1157941310159"></a><a name="p1157941310159"></a>402</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p157981331517"><a name="p157981331517"></a><a name="p157981331517"></a>Payment Required</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1957931331510"><a name="p1957931331510"></a><a name="p1957931331510"></a>Reserved for future use.</p>
</td>
</tr>
<tr id="row2579111314152"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p13579013131517"><a name="p13579013131517"></a><a name="p13579013131517"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1458021316155"><a name="p1458021316155"></a><a name="p1458021316155"></a>Forbidden</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p28189154"><a name="p28189154"></a><a name="p28189154"></a>The server has received the request and understood it, but the server is refusing to respond to it.</p>
<p id="p52375797"><a name="p52375797"></a><a name="p52375797"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="row758018131154"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p125808134158"><a name="p125808134158"></a><a name="p125808134158"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p195806134154"><a name="p195806134154"></a><a name="p195806134154"></a>NotFound</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1258041361516"><a name="p1258041361516"></a><a name="p1258041361516"></a>The requested resource cannot be found.</p>
<p id="p358041351515"><a name="p358041351515"></a><a name="p358041351515"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="row115802131157"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p658051311519"><a name="p658051311519"></a><a name="p658051311519"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p6580151312157"><a name="p6580151312157"></a><a name="p6580151312157"></a>MethodNotAllowed</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p958081381514"><a name="p958081381514"></a><a name="p958081381514"></a>A request method is not supported for the requested resource.</p>
<p id="p11580513171514"><a name="p11580513171514"></a><a name="p11580513171514"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="row258061381519"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p0580131319158"><a name="p0580131319158"></a><a name="p0580131319158"></a>406</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p12580913161518"><a name="p12580913161518"></a><a name="p12580913161518"></a>Not Acceptable</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1580101351515"><a name="p1580101351515"></a><a name="p1580101351515"></a>The server cannot fulfill the request based on the content characteristics of the request.</p>
</td>
</tr>
<tr id="row3580161316159"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p258061371510"><a name="p258061371510"></a><a name="p258061371510"></a>407</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p45806134157"><a name="p45806134157"></a><a name="p45806134157"></a>Proxy Authentication Required</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p45802131156"><a name="p45802131156"></a><a name="p45802131156"></a>This code is similar to 401, but indicates that the client must first authenticate itself with the proxy.</p>
</td>
</tr>
<tr id="row1958081361515"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p14580213131514"><a name="p14580213131514"></a><a name="p14580213131514"></a>408</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p8581101361514"><a name="p8581101361514"></a><a name="p8581101361514"></a>Request Time-out</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p165817133154"><a name="p165817133154"></a><a name="p165817133154"></a>The server timed out when waiting for the request.</p>
<p id="p20581141321519"><a name="p20581141321519"></a><a name="p20581141321519"></a>The client may re-initiate the request without any modification at any time.</p>
</td>
</tr>
<tr id="row10581161311157"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p65812139153"><a name="p65812139153"></a><a name="p65812139153"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1058121331512"><a name="p1058121331512"></a><a name="p1058121331512"></a>Conflict</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p35818138152"><a name="p35818138152"></a><a name="p35818138152"></a>The request cannot be processed due to a conflict, such as an edit conflict between multiple simultaneous updates or the resource that the client attempts to create already exits.</p>
</td>
</tr>
<tr id="row1858191351518"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p958101321516"><a name="p958101321516"></a><a name="p958101321516"></a>410</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1581191381516"><a name="p1581191381516"></a><a name="p1581191381516"></a>Gone</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p35811213131512"><a name="p35811213131512"></a><a name="p35811213131512"></a>The requested resource has been deleted permanently and will not be available again.</p>
</td>
</tr>
<tr id="row258121381514"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1458171313157"><a name="p1458171313157"></a><a name="p1458171313157"></a>411</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p19581131371516"><a name="p19581131371516"></a><a name="p19581131371516"></a>Length Required</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p358118134153"><a name="p358118134153"></a><a name="p358118134153"></a>The server refused to process the request because the request does not specify the length of its content.</p>
</td>
</tr>
<tr id="row1958171361513"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p125811813141514"><a name="p125811813141514"></a><a name="p125811813141514"></a>412</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p658171316150"><a name="p658171316150"></a><a name="p658171316150"></a>Precondition Failed</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p13581181315155"><a name="p13581181315155"></a><a name="p13581181315155"></a>The server does not meet one of the preconditions that the requester puts on the request.</p>
</td>
</tr>
<tr id="row25811131157"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p45811813171518"><a name="p45811813171518"></a><a name="p45811813171518"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1581131331513"><a name="p1581131331513"></a><a name="p1581131331513"></a>Request Entity Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p11582171315151"><a name="p11582171315151"></a><a name="p11582171315151"></a>The server refuses to process a request because the request is too large. The server may close the connection to prevent the client from continuing the request. If the server cannot process the request temporarily, the response will contain a Retry-After field.</p>
</td>
</tr>
<tr id="row9582513141513"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p958221318152"><a name="p958221318152"></a><a name="p958221318152"></a>414</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p8582313111519"><a name="p8582313111519"></a><a name="p8582313111519"></a>Request-URI Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p7582213101517"><a name="p7582213101517"></a><a name="p7582213101517"></a>The URI provided was too long for the server to process.</p>
</td>
</tr>
<tr id="row258218136157"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p15582013171520"><a name="p15582013171520"></a><a name="p15582013171520"></a>415</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p55825137155"><a name="p55825137155"></a><a name="p55825137155"></a>Unsupported Media Type</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p958216137156"><a name="p958216137156"></a><a name="p958216137156"></a>The server does not support the media type in the request.</p>
</td>
</tr>
<tr id="row55820138153"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p11582161317151"><a name="p11582161317151"></a><a name="p11582161317151"></a>416</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p85821413181511"><a name="p85821413181511"></a><a name="p85821413181511"></a>Requested range not satisfiable</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p11582111313157"><a name="p11582111313157"></a><a name="p11582111313157"></a>The requested range is invalid.</p>
</td>
</tr>
<tr id="row185824134159"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p45827133151"><a name="p45827133151"></a><a name="p45827133151"></a>417</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p6582181371513"><a name="p6582181371513"></a><a name="p6582181371513"></a>Expectation Failed</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p358341320157"><a name="p358341320157"></a><a name="p358341320157"></a>The server fails to meet the requirements of the Expect request-header field.</p>
</td>
</tr>
<tr id="row175831913171511"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p13583161319157"><a name="p13583161319157"></a><a name="p13583161319157"></a>422</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p18583171371512"><a name="p18583171371512"></a><a name="p18583171371512"></a>UnprocessableEntity</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p05831213181518"><a name="p05831213181518"></a><a name="p05831213181518"></a>The request is well-formed but is unable to be processed due to semantic errors.</p>
</td>
</tr>
<tr id="row358351316150"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1958331301511"><a name="p1958331301511"></a><a name="p1958331301511"></a>429</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p11583713111515"><a name="p11583713111515"></a><a name="p11583713111515"></a>TooManyRequests</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p95831613201517"><a name="p95831613201517"></a><a name="p95831613201517"></a>The client has sent more requests than its rate limit is allowed within a given amount of time, or the server has received more requests than it is able to process within a given amount of time. In this case, the client should re-initiate requests after the time specified in the Retry-After header of the response expires.</p>
</td>
</tr>
<tr id="row16583213111519"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1858311133153"><a name="p1858311133153"></a><a name="p1858311133153"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p758351319153"><a name="p758351319153"></a><a name="p758351319153"></a>InternalServerError</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p4584201313157"><a name="p4584201313157"></a><a name="p4584201313157"></a>The server is able to receive the request but it could not understand the request.</p>
</td>
</tr>
<tr id="row458410135151"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p1158441351511"><a name="p1158441351511"></a><a name="p1158441351511"></a>501</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p4584191341512"><a name="p4584191341512"></a><a name="p4584191341512"></a>Not Implemented</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p2584101310152"><a name="p2584101310152"></a><a name="p2584101310152"></a>The server does not support the requested function.</p>
</td>
</tr>
<tr id="row115841713171516"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p4584111331511"><a name="p4584111331511"></a><a name="p4584111331511"></a>502</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p1558401313157"><a name="p1558401313157"></a><a name="p1558401313157"></a>Bad Gateway</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p058411331514"><a name="p058411331514"></a><a name="p058411331514"></a>The server was acting as a gateway or proxy and received an invalid request from a remote server.</p>
</td>
</tr>
<tr id="row258417134152"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p158511314153"><a name="p158511314153"></a><a name="p158511314153"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p135852139150"><a name="p135852139150"></a><a name="p135852139150"></a>ServiceUnavailable</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p158512134153"><a name="p158512134153"></a><a name="p158512134153"></a>The requested service is invalid.</p>
<p id="p155851138151"><a name="p155851138151"></a><a name="p155851138151"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="row185852138154"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p9585131319158"><a name="p9585131319158"></a><a name="p9585131319158"></a>504</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p10585141320156"><a name="p10585141320156"></a><a name="p10585141320156"></a>ServerTimeout</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p135854136159"><a name="p135854136159"></a><a name="p135854136159"></a>The request cannot be fulfilled within a given time. The response will reach the client only if the request carries the <strong id="b13860357193114"><a name="b13860357193114"></a><a name="b13860357193114"></a>timeout</strong> parameter.</p>
</td>
</tr>
<tr id="row165851513111519"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.4.1.1 "><p id="p18586111391518"><a name="p18586111391518"></a><a name="p18586111391518"></a>505</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p19586111381511"><a name="p19586111381511"></a><a name="p19586111381511"></a>HTTP Version not supported</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p15861113111520"><a name="p15861113111520"></a><a name="p15861113111520"></a>The server does not support the HTTP protocol version used in the request.</p>
</td>
</tr>
</tbody>
</table>

