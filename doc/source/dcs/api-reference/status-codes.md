# Status Codes<a name="dcs-api-0312043"></a>

[Table 1](#table5210141351517)  describes status codes.

**Table  1**  Status codes

<a name="table5210141351517"></a>
<table><thead align="left"><tr id="row9601199"><th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.4.1.1"><p id="p39499626"><a name="p39499626"></a><a name="p39499626"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="22.81%" id="mcps1.2.4.1.2"><p id="p45353142"><a name="p45353142"></a><a name="p45353142"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="59.830000000000005%" id="mcps1.2.4.1.3"><p id="p49725882"><a name="p49725882"></a><a name="p49725882"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1264671"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p35329549"><a name="p35329549"></a><a name="p35329549"></a>100</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p43121195"><a name="p43121195"></a><a name="p43121195"></a>Continue</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p28402861"><a name="p28402861"></a><a name="p28402861"></a>The server has received the initial part of the request and the client should continue to send the remaining part.</p>
</td>
</tr>
<tr id="row54299160"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p36155831"><a name="p36155831"></a><a name="p36155831"></a>101</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p42941223"><a name="p42941223"></a><a name="p42941223"></a>Switching Protocols</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p34788224155715"><a name="p34788224155715"></a><a name="p34788224155715"></a>The requester has asked the server to switch protocols and the server has agreed to do so.</p>
<p id="p55687056"><a name="p55687056"></a><a name="p55687056"></a>The target protocol must be more advanced than the source protocol.</p>
<p id="p31421457"><a name="p31421457"></a><a name="p31421457"></a>For example, the current HTTP protocol is switched to a later version of HTTP.</p>
</td>
</tr>
<tr id="row28986342162053"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p66192337162053"><a name="p66192337162053"></a><a name="p66192337162053"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p59979085162053"><a name="p59979085162053"></a><a name="p59979085162053"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p14733219124120"><a name="p14733219124120"></a><a name="p14733219124120"></a>The server successfully processed the request.</p>
</td>
</tr>
<tr id="row14357657"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p22119530"><a name="p22119530"></a><a name="p22119530"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p46851500"><a name="p46851500"></a><a name="p46851500"></a>Created</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p36875142"><a name="p36875142"></a><a name="p36875142"></a>The request has been fulfilled, resulting in the creation of a new resource.</p>
</td>
</tr>
<tr id="row63440828"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p38433454"><a name="p38433454"></a><a name="p38433454"></a>202</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p26102093"><a name="p26102093"></a><a name="p26102093"></a>Accepted</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p33894784"><a name="p33894784"></a><a name="p33894784"></a>The request has been accepted for processing, but the processing has not been completed.</p>
</td>
</tr>
<tr id="row36617605"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p13236018"><a name="p13236018"></a><a name="p13236018"></a>203</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p65484519"><a name="p65484519"></a><a name="p65484519"></a>Non-Authoritative Information</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p2645837"><a name="p2645837"></a><a name="p2645837"></a>The request has been fulfilled.</p>
</td>
</tr>
<tr id="row23812538"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p49767403"><a name="p49767403"></a><a name="p49767403"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p4627874"><a name="p4627874"></a><a name="p4627874"></a>NoContent</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p39313476"><a name="p39313476"></a><a name="p39313476"></a>The server has successfully processed the request, but is not returning any content.</p>
<p id="p18276970"><a name="p18276970"></a><a name="p18276970"></a>The status code is returned in response to an HTTP OPTIONS request.</p>
</td>
</tr>
<tr id="row30275003"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p36356207"><a name="p36356207"></a><a name="p36356207"></a>205</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p59171655"><a name="p59171655"></a><a name="p59171655"></a>Reset Content</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p28174764"><a name="p28174764"></a><a name="p28174764"></a>The server has successfully processed the request, but is not returning any content. Unlike a 204 response, this response requires that the requester reset the content.</p>
</td>
</tr>
<tr id="row52246286"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p4090801"><a name="p4090801"></a><a name="p4090801"></a>206</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p62919444"><a name="p62919444"></a><a name="p62919444"></a>Partial Content</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p63310175"><a name="p63310175"></a><a name="p63310175"></a>The server has successfully processed a part of the GET request.</p>
</td>
</tr>
<tr id="row32920667"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p49328407"><a name="p49328407"></a><a name="p49328407"></a>300</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p36177998"><a name="p36177998"></a><a name="p36177998"></a>Multiple Choices</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p44736746"><a name="p44736746"></a><a name="p44736746"></a>There are multiple options for the requested resource. For example, this code could be used to present a list of resource characteristics and addresses from which the client such as a browser may choose.</p>
</td>
</tr>
<tr id="row67086402"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p65289456"><a name="p65289456"></a><a name="p65289456"></a>301</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p53954550"><a name="p53954550"></a><a name="p53954550"></a>Moved Permanently</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p8242429"><a name="p8242429"></a><a name="p8242429"></a>This and all future requests should be permanently directed to the given URI indicated in this response.</p>
</td>
</tr>
<tr id="row7073000"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p36042131"><a name="p36042131"></a><a name="p36042131"></a>302</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p33731474"><a name="p33731474"></a><a name="p33731474"></a>Found</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p47894862"><a name="p47894862"></a><a name="p47894862"></a>The requested resource was temporarily moved.</p>
</td>
</tr>
<tr id="row28400574"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p18745119"><a name="p18745119"></a><a name="p18745119"></a>303</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p41959665"><a name="p41959665"></a><a name="p41959665"></a>See Other</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p43289691"><a name="p43289691"></a><a name="p43289691"></a>The response to the request can be found under another URI using a GET or POST method.</p>
</td>
</tr>
<tr id="row54062905"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p17019195"><a name="p17019195"></a><a name="p17019195"></a>304</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p36377578"><a name="p36377578"></a><a name="p36377578"></a>Not Modified</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p60902701"><a name="p60902701"></a><a name="p60902701"></a>The requested resource has not been modified. In such case, there is no need to retransmit the resource since the client still has a previously-downloaded copy.</p>
</td>
</tr>
<tr id="row11253402"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p39110359"><a name="p39110359"></a><a name="p39110359"></a>305</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p13822492"><a name="p13822492"></a><a name="p13822492"></a>Use Proxy</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p45880082"><a name="p45880082"></a><a name="p45880082"></a>The requested resource is available only through a proxy.</p>
</td>
</tr>
<tr id="row10267559"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p26365928"><a name="p26365928"></a><a name="p26365928"></a>306</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p55265455"><a name="p55265455"></a><a name="p55265455"></a>Unused</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p47316833"><a name="p47316833"></a><a name="p47316833"></a>This HTTP status code is no longer used.</p>
</td>
</tr>
<tr id="row23198319"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p15663"><a name="p15663"></a><a name="p15663"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p1268752"><a name="p1268752"></a><a name="p1268752"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p35660089"><a name="p35660089"></a><a name="p35660089"></a>The request is invalid.</p>
<p id="p52505353"><a name="p52505353"></a><a name="p52505353"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="row2786131"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p24350086"><a name="p24350086"></a><a name="p24350086"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p26199929"><a name="p26199929"></a><a name="p26199929"></a>Unauthorized</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p41819476"><a name="p41819476"></a><a name="p41819476"></a>The authentication information provided by the client is incorrect or invalid.</p>
</td>
</tr>
<tr id="row40830968"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p18974148"><a name="p18974148"></a><a name="p18974148"></a>402</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p60510987"><a name="p60510987"></a><a name="p60510987"></a>Payment Required</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p2442935"><a name="p2442935"></a><a name="p2442935"></a>Reserved for future use.</p>
</td>
</tr>
<tr id="row21986423"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p36069813"><a name="p36069813"></a><a name="p36069813"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p35973707"><a name="p35973707"></a><a name="p35973707"></a>Forbidden</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p28189154"><a name="p28189154"></a><a name="p28189154"></a>The server has received the request and understood it, but the server is refusing to respond to it.</p>
<p id="p52375797"><a name="p52375797"></a><a name="p52375797"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="row1620129"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p64121649"><a name="p64121649"></a><a name="p64121649"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p26471098"><a name="p26471098"></a><a name="p26471098"></a>NotFound</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p63784163"><a name="p63784163"></a><a name="p63784163"></a>The requested resource could not be found.</p>
<p id="p37186555"><a name="p37186555"></a><a name="p37186555"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="row66243540"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p64126518"><a name="p64126518"></a><a name="p64126518"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p26865456"><a name="p26865456"></a><a name="p26865456"></a>MethodNotAllowed</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p28618347"><a name="p28618347"></a><a name="p28618347"></a>A request method is not supported for the requested resource.</p>
<p id="p56238536"><a name="p56238536"></a><a name="p56238536"></a>The client should modify the request instead of re-initiating it.</p>
</td>
</tr>
<tr id="row36384783"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p61486274"><a name="p61486274"></a><a name="p61486274"></a>406</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p14332335"><a name="p14332335"></a><a name="p14332335"></a>Not Acceptable</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p20068476"><a name="p20068476"></a><a name="p20068476"></a>The server could not fulfill the request according to the content characteristics of the request.</p>
</td>
</tr>
<tr id="row46398558"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p186847"><a name="p186847"></a><a name="p186847"></a>407</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p15134612"><a name="p15134612"></a><a name="p15134612"></a>Proxy Authentication Required</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p17944037"><a name="p17944037"></a><a name="p17944037"></a>This code is similar to 401, but indicates that the client must first authenticate itself with the proxy.</p>
</td>
</tr>
<tr id="row27278612"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p62083996"><a name="p62083996"></a><a name="p62083996"></a>408</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p62747764"><a name="p62747764"></a><a name="p62747764"></a>Request Time-out</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p49404100"><a name="p49404100"></a><a name="p49404100"></a>The server timed out waiting for the request.</p>
<p id="p41983721"><a name="p41983721"></a><a name="p41983721"></a>The client may re-initiate the request without modifications at any later time.</p>
</td>
</tr>
<tr id="row42309173"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p4490990"><a name="p4490990"></a><a name="p4490990"></a>409</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p28225944"><a name="p28225944"></a><a name="p28225944"></a>Conflict</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p4600155"><a name="p4600155"></a><a name="p4600155"></a>The request could not be processed due to a conflict in the request, such as an edit conflict between multiple simultaneous updates or the resource that the client attempts to create already exits.</p>
</td>
</tr>
<tr id="row37068254"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p49738569"><a name="p49738569"></a><a name="p49738569"></a>410</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p2292293"><a name="p2292293"></a><a name="p2292293"></a>Gone</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p51458041"><a name="p51458041"></a><a name="p51458041"></a>The requested resource has been deleted permanently and will not be available again.</p>
</td>
</tr>
<tr id="row60469192"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p66166404"><a name="p66166404"></a><a name="p66166404"></a>411</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p57878541"><a name="p57878541"></a><a name="p57878541"></a>Length Required</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p57650250"><a name="p57650250"></a><a name="p57650250"></a>The server refused to process the request because the request does not specify the length of its content.</p>
</td>
</tr>
<tr id="row49090208"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p16883911"><a name="p16883911"></a><a name="p16883911"></a>412</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p25419542"><a name="p25419542"></a><a name="p25419542"></a>Precondition Failed</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p45717046"><a name="p45717046"></a><a name="p45717046"></a>The server does not meet one of the preconditions that the requester puts on the request.</p>
</td>
</tr>
<tr id="row8800236"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p41730504"><a name="p41730504"></a><a name="p41730504"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p24727624"><a name="p24727624"></a><a name="p24727624"></a>Request Entity Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p9505134164228"><a name="p9505134164228"></a><a name="p9505134164228"></a>The request is larger than the server is willing or able to process.</p>
<p id="p56780500"><a name="p56780500"></a><a name="p56780500"></a>The server may close the connection to prevent the client from continuing the request. If the server temporarily cannot process the request, the response will contain a Retry-After header field.</p>
</td>
</tr>
<tr id="row41262459"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p53924869"><a name="p53924869"></a><a name="p53924869"></a>414</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p5838288"><a name="p5838288"></a><a name="p5838288"></a>Request-URI Too Large</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p3139332"><a name="p3139332"></a><a name="p3139332"></a>The URI provided was too long for the server to process.</p>
</td>
</tr>
<tr id="row28253988"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p6871687"><a name="p6871687"></a><a name="p6871687"></a>415</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p19735783"><a name="p19735783"></a><a name="p19735783"></a>Unsupported Media Type</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p55094571"><a name="p55094571"></a><a name="p55094571"></a>The server does not support the media type in the request.</p>
</td>
</tr>
<tr id="row26089094"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p32841884"><a name="p32841884"></a><a name="p32841884"></a>416</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p42946954"><a name="p42946954"></a><a name="p42946954"></a>Requested range not satisfiable</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p56151289"><a name="p56151289"></a><a name="p56151289"></a>The requested range is invalid.</p>
</td>
</tr>
<tr id="row35599561"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p64992155"><a name="p64992155"></a><a name="p64992155"></a>417</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p29873218"><a name="p29873218"></a><a name="p29873218"></a>Expectation Failed</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p3811622"><a name="p3811622"></a><a name="p3811622"></a>The server fails to meet the requirements of the Expect request-header field.</p>
</td>
</tr>
<tr id="row34304602"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p27209379"><a name="p27209379"></a><a name="p27209379"></a>422</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p56476125"><a name="p56476125"></a><a name="p56476125"></a>UnprocessableEntity</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p11163440"><a name="p11163440"></a><a name="p11163440"></a>The request was well-formed but was unable to be followed due to semantic errors.</p>
</td>
</tr>
<tr id="row33362098"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p17975388"><a name="p17975388"></a><a name="p17975388"></a>429</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p46720306"><a name="p46720306"></a><a name="p46720306"></a>TooManyRequests</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p26248478"><a name="p26248478"></a><a name="p26248478"></a>The client has sent more requests than its rate limit is allowed within a given amount of time, or the server has received more requests than it is able to process within a given amount of time. In this case, it is advisable for the client to re-initiate requests after the time specified in the Retry-After header of the response expires.</p>
</td>
</tr>
<tr id="row34909710"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p9114291"><a name="p9114291"></a><a name="p9114291"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p60129"><a name="p60129"></a><a name="p60129"></a>InternalServerError</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p4870463"><a name="p4870463"></a><a name="p4870463"></a>The server is able to receive the request but it could not understand the request.</p>
</td>
</tr>
<tr id="row43834167"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p60906657"><a name="p60906657"></a><a name="p60906657"></a>501</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p34492175"><a name="p34492175"></a><a name="p34492175"></a>Not Implemented</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p42402794"><a name="p42402794"></a><a name="p42402794"></a>The server does not support the requested function.</p>
</td>
</tr>
<tr id="row46080827"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p41559524"><a name="p41559524"></a><a name="p41559524"></a>502</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p10878253"><a name="p10878253"></a><a name="p10878253"></a>Bad Gateway</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p8723262"><a name="p8723262"></a><a name="p8723262"></a>The server was acting as a gateway or proxy and received an invalid request from a remote server.</p>
</td>
</tr>
<tr id="row11400497"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p51025090"><a name="p51025090"></a><a name="p51025090"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p39391664"><a name="p39391664"></a><a name="p39391664"></a>ServiceUnavailable</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p36608226"><a name="p36608226"></a><a name="p36608226"></a>The requested service is invalid.</p>
<p id="p61038585"><a name="p61038585"></a><a name="p61038585"></a>It is advisable for the client to modify the request instead of re-initiating the request.</p>
</td>
</tr>
<tr id="row12476353"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p3951668"><a name="p3951668"></a><a name="p3951668"></a>504</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p51649700"><a name="p51649700"></a><a name="p51649700"></a>ServerTimeout</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p22876152"><a name="p22876152"></a><a name="p22876152"></a>The server could not return a timely response. The response will reach the client only if the request carries a timeout parameter.</p>
</td>
</tr>
<tr id="row4558779"><td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.1 "><p id="p33716833"><a name="p33716833"></a><a name="p33716833"></a>505</p>
</td>
<td class="cellrowborder" valign="top" width="22.81%" headers="mcps1.2.4.1.2 "><p id="p46708959"><a name="p46708959"></a><a name="p46708959"></a>HTTP Version not supported</p>
</td>
<td class="cellrowborder" valign="top" width="59.830000000000005%" headers="mcps1.2.4.1.3 "><p id="p25329374"><a name="p25329374"></a><a name="p25329374"></a>The server does not support the HTTP protocol version used in the request.</p>
</td>
</tr>
</tbody>
</table>

