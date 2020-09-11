# Show Account Metadata<a name="obs_03_0024"></a>

Users can send requests to obtain account metadata. This operation is similar to a sub-function of  [5.1 Show Container Details and List Objects](show-account-details-and-list-containers.md). Only account details are shown, whereas containers are not listed.

## Method<a name="section3855846091844"></a>

**Table  1**  Method description

<a name="table3622757091844"></a>
<table><thead align="left"><tr id="row5885523391844"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p254458491844"><a name="p254458491844"></a><a name="p254458491844"></a>Method</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p4306302491844"><a name="p4306302491844"></a><a name="p4306302491844"></a><strong id="b5202290091844"><a name="b5202290091844"></a><a name="b5202290091844"></a>URI</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p5310538591844"><a name="p5310538591844"></a><a name="p5310538591844"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5912023091844"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2400930591844"><a name="p2400930591844"></a><a name="p2400930591844"></a>HEAD</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6570552491844"><a name="p6570552491844"></a><a name="p6570552491844"></a>/v1/{account}</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2054723291844"><a name="p2054723291844"></a><a name="p2054723291844"></a>Shows metadata of a specified account.</p>
</td>
</tr>
</tbody>
</table>

**\{account\}**  indicates the name of an account. Metadata of an account includes the number of containers, number of objects, and total number of bytes that are stored in OBS for the account.

This operation does not involve a request body.

## Example Request<a name="section1365578791844"></a>

```
curl -i $publicURL -X HEAD -H "X-Auth-Token:$token"
```

## Request Query Parameters<a name="section529000091844"></a>

This operation does not include request query parameters.

## Request Headers<a name="section187973291844"></a>

Request URI parameters

<a name="table50212566154423"></a>
<table><thead align="left"><tr id="row49025617154423"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p11652032154423"><a name="p11652032154423"></a><a name="p11652032154423"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p38615046154423"><a name="p38615046154423"></a><a name="p38615046154423"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p31754770154423"><a name="p31754770154423"></a><a name="p31754770154423"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row63778126154423"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p65754607154423"><a name="p65754607154423"></a><a name="p65754607154423"></a>{account}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p24522989154423"><a name="p24522989154423"></a><a name="p24522989154423"></a>String</p>
<p id="p19380314154423"><a name="p19380314154423"></a><a name="p19380314154423"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p26301614154423"><a name="p26301614154423"></a><a name="p26301614154423"></a>Unique name of the account. In the current version, it indicates the unique ID of the account.</p>
</td>
</tr>
</tbody>
</table>

Request header parameters

<a name="table24420230154423"></a>
<table><thead align="left"><tr id="row63928991154423"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p10865822154423"><a name="p10865822154423"></a><a name="p10865822154423"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p2338936154423"><a name="p2338936154423"></a><a name="p2338936154423"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p27363246154423"><a name="p27363246154423"></a><a name="p27363246154423"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16474171154423"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p59339488154423"><a name="p59339488154423"></a><a name="p59339488154423"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p41769209154423"><a name="p41769209154423"></a><a name="p41769209154423"></a>String</p>
<p id="p40378565154423"><a name="p40378565154423"></a><a name="p40378565154423"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p49438312154423"><a name="p49438312154423"></a><a name="p49438312154423"></a>Authentication token.</p>
</td>
</tr>
</tbody>
</table>

## Response Headers<a name="section569761409197"></a>

The following table describes the response headers:

**Table  2**  Response header parameters

<a name="table36256464105935"></a>
<table><thead align="left"><tr id="row12655405105935"><th class="cellrowborder" valign="top" width="38.279999999999994%" id="mcps1.2.4.1.1"><p id="p18454862105935"><a name="p18454862105935"></a><a name="p18454862105935"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.509999999999998%" id="mcps1.2.4.1.2"><p id="p31822237105935"><a name="p31822237105935"></a><a name="p31822237105935"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.21%" id="mcps1.2.4.1.3"><p id="p45852910105935"><a name="p45852910105935"></a><a name="p45852910105935"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6557734105935"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.2.4.1.1 "><p id="p61414447105935"><a name="p61414447105935"></a><a name="p61414447105935"></a>Accept-Ranges</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p8514345105935"><a name="p8514345105935"></a><a name="p8514345105935"></a>String</p>
<p id="p4237564419328"><a name="p4237564419328"></a><a name="p4237564419328"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p18573372105935"><a name="p18573372105935"></a><a name="p18573372105935"></a>Acceptable range type, for example, bytes.</p>
</td>
</tr>
<tr id="row32942622105935"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.2.4.1.1 "><p id="p51106696105935"><a name="p51106696105935"></a><a name="p51106696105935"></a>X-Account-Bytes-Used</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p46001694105935"><a name="p46001694105935"></a><a name="p46001694105935"></a>Int</p>
<p id="p5358594193145"><a name="p5358594193145"></a><a name="p5358594193145"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p35149770105935"><a name="p35149770105935"></a><a name="p35149770105935"></a>Total number of bytes that are stored in OBS for the account.</p>
</td>
</tr>
<tr id="row47912474105935"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.2.4.1.1 "><p id="p55705215105935"><a name="p55705215105935"></a><a name="p55705215105935"></a>X-Account-Container-Count</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p15828589105935"><a name="p15828589105935"></a><a name="p15828589105935"></a>Int</p>
<p id="p51680976193218"><a name="p51680976193218"></a><a name="p51680976193218"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p7047307105935"><a name="p7047307105935"></a><a name="p7047307105935"></a>Number of containers in the account.</p>
</td>
</tr>
<tr id="row63425763105935"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.2.4.1.1 "><p id="p37213197105935"><a name="p37213197105935"></a><a name="p37213197105935"></a>X-Account-Object-Count</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p61478971105935"><a name="p61478971105935"></a><a name="p61478971105935"></a>Int</p>
<p id="p23266699193220"><a name="p23266699193220"></a><a name="p23266699193220"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p13740758105935"><a name="p13740758105935"></a><a name="p13740758105935"></a>Number of objects in the account.</p>
</td>
</tr>
<tr id="row56557959105935"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.2.4.1.1 "><p id="p17791984105935"><a name="p17791984105935"></a><a name="p17791984105935"></a>X-Account-Meta-name</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p31864569105935"><a name="p31864569105935"></a><a name="p31864569105935"></a>String</p>
<p id="p6244537193222"><a name="p6244537193222"></a><a name="p6244537193222"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p30893258105935"><a name="p30893258105935"></a><a name="p30893258105935"></a>Custom account metadata item, where <strong id="b54273197"><a name="b54273197"></a><a name="b54273197"></a>{name}</strong> is the name of the metadata item.</p>
</td>
</tr>
<tr id="row14705161202056"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.2.4.1.1 "><p id="p50267403202056"><a name="p50267403202056"></a><a name="p50267403202056"></a>X-Account-Meta-Quota-Bytes</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p1109620620218"><a name="p1109620620218"></a><a name="p1109620620218"></a>Int</p>
<p id="p3275699220218"><a name="p3275699220218"></a><a name="p3275699220218"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p31478525202056"><a name="p31478525202056"></a><a name="p31478525202056"></a>Quota of account.</p>
</td>
</tr>
<tr id="row9603869105935"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.2.4.1.1 "><p id="p39715950105935"><a name="p39715950105935"></a><a name="p39715950105935"></a>X-Account-Meta-Temp-URL-Key</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p62875420105935"><a name="p62875420105935"></a><a name="p62875420105935"></a>String</p>
<p id="p60300411193226"><a name="p60300411193226"></a><a name="p60300411193226"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p59744270105935"><a name="p59744270105935"></a><a name="p59744270105935"></a>Secret key value for TempURL.</p>
</td>
</tr>
<tr id="row827525105935"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.2.4.1.1 "><p id="p67029528105935"><a name="p67029528105935"></a><a name="p67029528105935"></a>X-Account-Meta-Temp-URL-Key-2</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p60682725105935"><a name="p60682725105935"></a><a name="p60682725105935"></a>String</p>
<p id="p23657714193245"><a name="p23657714193245"></a><a name="p23657714193245"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p16353682105935"><a name="p16353682105935"></a><a name="p16353682105935"></a>A second secret key value for TempURL.</p>
</td>
</tr>
<tr id="row12965412105935"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.2.4.1.1 "><p id="p43565445105935"><a name="p43565445105935"></a><a name="p43565445105935"></a>X-Account-Project-Domain-Id</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p39140122105935"><a name="p39140122105935"></a><a name="p39140122105935"></a>String</p>
<p id="p25474958193238"><a name="p25474958193238"></a><a name="p25474958193238"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p16233291105935"><a name="p16233291105935"></a><a name="p16233291105935"></a>ID of the domain to which the account belongs.</p>
</td>
</tr>
<tr id="row38329479193252"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.2.4.1.1 "><p id="p38252292193551"><a name="p38252292193551"></a><a name="p38252292193551"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p11427942193551"><a name="p11427942193551"></a><a name="p11427942193551"></a>String</p>
<p id="p35742616193551"><a name="p35742616193551"></a><a name="p35742616193551"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p9470822193551"><a name="p9470822193551"></a><a name="p9470822193551"></a>If the operation succeeds, this value is 0.</p>
<p id="p18128539193551"><a name="p18128539193551"></a><a name="p18128539193551"></a>If the operation fails, this value is the length of the error text in the response body.</p>
</td>
</tr>
<tr id="row53804509193253"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.2.4.1.1 "><p id="p62368055193551"><a name="p62368055193551"></a><a name="p62368055193551"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p18647690193551"><a name="p18647690193551"></a><a name="p18647690193551"></a>String</p>
<p id="p33611487193551"><a name="p33611487193551"></a><a name="p33611487193551"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p38175916193551"><a name="p38175916193551"></a><a name="p38175916193551"></a>MIME type of the text in the response body.</p>
</td>
</tr>
<tr id="row51485756193253"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.2.4.1.1 "><p id="p47173263193551"><a name="p47173263193551"></a><a name="p47173263193551"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p62937924193551"><a name="p62937924193551"></a><a name="p62937924193551"></a>Datetime</p>
<p id="p29570405193551"><a name="p29570405193551"></a><a name="p29570405193551"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p46392644193551"><a name="p46392644193551"></a><a name="p46392644193551"></a>Transaction date and time.</p>
</td>
</tr>
<tr id="row14784897193254"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.2.4.1.1 "><p id="p64479534193551"><a name="p64479534193551"></a><a name="p64479534193551"></a>X-Trans-Id</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p55459781193551"><a name="p55459781193551"></a><a name="p55459781193551"></a>Uuid</p>
<p id="p29375988193551"><a name="p29375988193551"></a><a name="p29375988193551"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p30644837193551"><a name="p30644837193551"></a><a name="p30644837193551"></a>Unique transaction identifier.</p>
<p id="p7368081193551"><a name="p7368081193551"></a><a name="p7368081193551"></a></p>
</td>
</tr>
<tr id="row6689059193254"><td class="cellrowborder" valign="top" width="38.279999999999994%" headers="mcps1.2.4.1.1 "><p id="p2622408193551"><a name="p2622408193551"></a><a name="p2622408193551"></a>X-Timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="15.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p11088523193551"><a name="p11088523193551"></a><a name="p11088523193551"></a>Datetime</p>
<p id="p32687845193551"><a name="p32687845193551"></a><a name="p32687845193551"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p30469759193551"><a name="p30469759193551"></a><a name="p30469759193551"></a>Object creation time and date, in UNIX Epoch timestamp format.</p>
</td>
</tr>
</tbody>
</table>

## Show Account Metadata<a name="section42277158"></a>

Show account metadata.

```
curl -i -H "X-Auth-token:9d6c288edff8434ea23108e6516ae5a5" "http://172.28.5.30:80/v1/AUTH_0ce042a9be6140769b12c1001d41bcf9" -X HEAD
```

```
HTTP/1.1 204 No Content
X-Trans-Id: tx000001513970d65e370c0-0480bf0ace
Accept-Ranges: bytes
Content-Length: 0
Content-Type: text/plain;charset=UTF-8
Date: Tue, 24 Nov 2015 12:21:14 GMT
X-Account-Bytes-Used: 0
X-Account-Container-Count: 0
X-Account-Meta-Book: firstbook
X-Account-Object-Count: 0
X-Account-Project-Domain-Id: default
X-Timestamp: 1448367617.422
```

