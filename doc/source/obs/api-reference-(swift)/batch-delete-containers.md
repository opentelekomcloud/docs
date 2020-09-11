# Batch Delete Containers<a name="obs_03_0048"></a>

## Method<a name="section318016296718"></a>

<a name="table20186229072"></a>
<table><thead align="left"><tr id="row152544293714"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p13255192919710"><a name="p13255192919710"></a><a name="p13255192919710"></a>Method</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p5255122910718"><a name="p5255122910718"></a><a name="p5255122910718"></a><strong id="b11255729078"><a name="b11255729078"></a><a name="b11255729078"></a>URI</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p1425512299717"><a name="p1425512299717"></a><a name="p1425512299717"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row72556295713"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p1625519291715"><a name="p1625519291715"></a><a name="p1625519291715"></a>POST</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p92551291579"><a name="p92551291579"></a><a name="p92551291579"></a>/v1/{account}?bulk-delete</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p177641292166"><a name="p177641292166"></a><a name="p177641292166"></a>Batch deletes containers. A maximum of 10,000 empty containers can be deleted.</p>
</td>
</tr>
</tbody>
</table>

**\{account\}**  indicates the name of an account.

The request body is a text file that includes the containers to be deleted. Each line in the text file represents a container to be deleted.

## Example Request<a name="section1079761591017"></a>

Batch delete containers:

```
curl -i $publicURL?bulk-delete -XPOST -H "X-Auth-Token:$token" -T ./deletesample
```

## Request Query Parameters<a name="section138011151105"></a>

<a name="table080121521013"></a>
<table><thead align="left"><tr id="row1991151581020"><th class="cellrowborder" valign="top" width="20.407959204079592%" id="mcps1.1.4.1.1"><p id="p14911201520106"><a name="p14911201520106"></a><a name="p14911201520106"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.1.4.1.2"><p id="p59110153109"><a name="p59110153109"></a><a name="p59110153109"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.3034696530347%" id="mcps1.1.4.1.3"><p id="p1291118158108"><a name="p1291118158108"></a><a name="p1291118158108"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row991141551017"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.1.4.1.1 "><p id="p1591118157106"><a name="p1591118157106"></a><a name="p1591118157106"></a>bulk-delete</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.1.4.1.2 "><p id="p1391191551012"><a name="p1391191551012"></a><a name="p1391191551012"></a>String</p>
<p id="p1991161514104"><a name="p1991161514104"></a><a name="p1991161514104"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="65.3034696530347%" headers="mcps1.1.4.1.3 "><p id="p18911141517103"><a name="p18911141517103"></a><a name="p18911141517103"></a>Bulk-deletes containers. It is used together with the text file that includes the containers to be deleted.</p>
<p id="p139111815181015"><a name="p139111815181015"></a><a name="p139111815181015"></a>A maximum of 10,000 empty containers can be deleted.</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section11811171501013"></a>

Request URI parameters

<a name="table118171015141015"></a>
<table><thead align="left"><tr id="row1691415154104"><th class="cellrowborder" valign="top" width="20.407959204079592%" id="mcps1.1.4.1.1"><p id="p791417154108"><a name="p791417154108"></a><a name="p791417154108"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.1.4.1.2"><p id="p1191471571012"><a name="p1191471571012"></a><a name="p1191471571012"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.3034696530347%" id="mcps1.1.4.1.3"><p id="p14914915161017"><a name="p14914915161017"></a><a name="p14914915161017"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row09141915171019"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.1.4.1.1 "><p id="p791441520103"><a name="p791441520103"></a><a name="p791441520103"></a>{account}</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.1.4.1.2 "><p id="p291491515105"><a name="p291491515105"></a><a name="p291491515105"></a>String</p>
<p id="p209149154102"><a name="p209149154102"></a><a name="p209149154102"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="65.3034696530347%" headers="mcps1.1.4.1.3 "><p id="p1391481581010"><a name="p1391481581010"></a><a name="p1391481581010"></a>Unique name of the account. In the current version, it indicates the unique ID of the account.</p>
</td>
</tr>
</tbody>
</table>

Request header parameters

<a name="table781141518105"></a>
<table><thead align="left"><tr id="row79131015151012"><th class="cellrowborder" valign="top" width="20.407959204079592%" id="mcps1.1.4.1.1"><p id="p1591311517104"><a name="p1591311517104"></a><a name="p1591311517104"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.1.4.1.2"><p id="p11913171517106"><a name="p11913171517106"></a><a name="p11913171517106"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.3034696530347%" id="mcps1.1.4.1.3"><p id="p149131515141015"><a name="p149131515141015"></a><a name="p149131515141015"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17913121518102"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.1.4.1.1 "><p id="p1191341571017"><a name="p1191341571017"></a><a name="p1191341571017"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.1.4.1.2 "><p id="p491391521014"><a name="p491391521014"></a><a name="p491391521014"></a>String</p>
<p id="p11913101541017"><a name="p11913101541017"></a><a name="p11913101541017"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="65.3034696530347%" headers="mcps1.1.4.1.3 "><p id="p49131715161017"><a name="p49131715161017"></a><a name="p49131715161017"></a>Authentication token.</p>
</td>
</tr>
</tbody>
</table>

## Response Headers<a name="section116681545231"></a>

<a name="table16670115410233"></a>
<table><thead align="left"><tr id="row11742185419235"><th class="cellrowborder" valign="top" width="20.407959204079592%" id="mcps1.1.4.1.1"><p id="p1774265432312"><a name="p1774265432312"></a><a name="p1774265432312"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="13.268673132686734%" id="mcps1.1.4.1.2"><p id="p1474214548238"><a name="p1474214548238"></a><a name="p1474214548238"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.32336766323368%" id="mcps1.1.4.1.3"><p id="p16742454202316"><a name="p16742454202316"></a><a name="p16742454202316"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16742105413236"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.1.4.1.1 "><p id="p157427545234"><a name="p157427545234"></a><a name="p157427545234"></a>Transfer-Encoding</p>
</td>
<td class="cellrowborder" valign="top" width="13.268673132686734%" headers="mcps1.1.4.1.2 "><p id="p1674217540234"><a name="p1674217540234"></a><a name="p1674217540234"></a>String</p>
<p id="p1874285422310"><a name="p1874285422310"></a><a name="p1874285422310"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="66.32336766323368%" headers="mcps1.1.4.1.3 "><p id="p147428547234"><a name="p147428547234"></a><a name="p147428547234"></a>Enables chunked transfer.</p>
</td>
</tr>
<tr id="row1174215492312"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.1.4.1.1 "><p id="p0742854162314"><a name="p0742854162314"></a><a name="p0742854162314"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="13.268673132686734%" headers="mcps1.1.4.1.2 "><p id="p11743135418231"><a name="p11743135418231"></a><a name="p11743135418231"></a>String</p>
<p id="p10743145410236"><a name="p10743145410236"></a><a name="p10743145410236"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="66.32336766323368%" headers="mcps1.1.4.1.3 "><p id="p2074311548237"><a name="p2074311548237"></a><a name="p2074311548237"></a>MIME type of the text in the response body.</p>
</td>
</tr>
<tr id="row1574317546234"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.1.4.1.1 "><p id="p1474335452311"><a name="p1474335452311"></a><a name="p1474335452311"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="13.268673132686734%" headers="mcps1.1.4.1.2 "><p id="p1774355418233"><a name="p1774355418233"></a><a name="p1774355418233"></a>Datetime</p>
<p id="p157431554142318"><a name="p157431554142318"></a><a name="p157431554142318"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="66.32336766323368%" headers="mcps1.1.4.1.3 "><p id="p1874316540233"><a name="p1874316540233"></a><a name="p1874316540233"></a>Transaction date and time.</p>
</td>
</tr>
<tr id="row8744125492317"><td class="cellrowborder" valign="top" width="20.407959204079592%" headers="mcps1.1.4.1.1 "><p id="p12744165413232"><a name="p12744165413232"></a><a name="p12744165413232"></a>X-Trans-Id</p>
</td>
<td class="cellrowborder" valign="top" width="13.268673132686734%" headers="mcps1.1.4.1.2 "><p id="p97441054102313"><a name="p97441054102313"></a><a name="p97441054102313"></a>Uuid</p>
<p id="p67441454162314"><a name="p67441454162314"></a><a name="p67441454162314"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="66.32336766323368%" headers="mcps1.1.4.1.3 "><p id="p10744554142317"><a name="p10744554142317"></a><a name="p10744554142317"></a>Unique transaction identifier.</p>
</td>
</tr>
</tbody>
</table>

## Delete Empty Containers<a name="section2201390"></a>

Delete two empty containers:  **8projectidprojectidproject000023.bucket.test6.0**  and  **8projectidprojectidproject000023.bucket.test6.1**, and delete the container text file  **deletesample**:

```
/8projectidprojectidproject000023.bucket.test6.0
/8projectidprojectidproject000023.bucket.test6.1
```

Execute the deletion:

```
curl -i -H "X-auth-token:b85044aa87eb46b88552f1dcbae411e3" http://172.28.5.31:80/v1/AUTH_09ijuyhgt675432wert56yt789i0o98u?bulk-delete -XPOST -T ./deletesample
```

```
HTTP/1.1 100 Continue

HTTP/1.1 200 OK
X-Trans-Id: tx0000015f80c43411770b1-a2dbb9e7c9
Date: Fri, 03 Nov 2017 07:24:22 GMT
Content-Type: text/plain;charset=ISO-8859-1
Transfer-Encoding: chunked

Number Deleted: 2
Number Not Found: 0
Response Body: 
Response Status: 200 OK
Errors:
```

