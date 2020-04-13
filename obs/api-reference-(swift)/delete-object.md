# Delete Object<a name="obs_03_0066"></a>

The  **DELETE** command is used to delete a specified object. After an object is deleted, any subsequent GET, HEAD, POST, or DELETE operations return a **404 Not Found**  error code.

For static large objects, you can add the  **multipart-manifest=delete**  query parameter. This operation deletes the segment objects and if all deletions succeed, this operation deletes the manifest object.

Normally the DELETE operation does not return a response body. However, with the  **multipart-manifest=delete**  query parameter, the response body contains a list of manifest and segment objects and the status of their delete operations.

## Method<a name="section39869956112928"></a>

**Table  1**  Method description

<a name="table36630378113016"></a>
<table><thead align="left"><tr id="row48730343113016"><th class="cellrowborder" valign="top" width="15.851585158515851%" id="mcps1.2.4.1.1"><p id="p5336715811413"><a name="p5336715811413"></a><a name="p5336715811413"></a>Method</p>
</th>
<th class="cellrowborder" valign="top" width="49.874987498749874%" id="mcps1.2.4.1.2"><p id="p51296332113016"><a name="p51296332113016"></a><a name="p51296332113016"></a><strong id="b39273688114629"><a name="b39273688114629"></a><a name="b39273688114629"></a>URI</strong></p>
</th>
<th class="cellrowborder" valign="top" width="34.27342734273427%" id="mcps1.2.4.1.3"><p id="p61362190113016"><a name="p61362190113016"></a><a name="p61362190113016"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15388804113016"><td class="cellrowborder" valign="top" width="15.851585158515851%" headers="mcps1.2.4.1.1 "><p id="p38533588113016"><a name="p38533588113016"></a><a name="p38533588113016"></a>DELETE</p>
</td>
<td class="cellrowborder" valign="top" width="49.874987498749874%" headers="mcps1.2.4.1.2 "><p id="p6978189171830"><a name="p6978189171830"></a><a name="p6978189171830"></a>/v1/{account}/{container}/{object}{?multipart-manifest}</p>
</td>
<td class="cellrowborder" valign="top" width="34.27342734273427%" headers="mcps1.2.4.1.3 "><p id="p19784190113016"><a name="p19784190113016"></a><a name="p19784190113016"></a>Permanently deletes an object from the OBS system.</p>
</td>
</tr>
</tbody>
</table>

**\{account\}**  indicates the name of an account.

**\{container\}**  indicates the name of a container.

**\{object\}**  indicates the name of an object.

This operation does not involve a request body.

## Example Request<a name="section16623225"></a>

Delete the  **helloworld** object from the **marktwain**  container.

```
curl -i $publicURL/
marktwain/helloworld -X DELETE -H "X-Auth-Token: $token"
```

## Request Query Parameters<a name="section5103708"></a>

<a name="table43935352172115"></a>
<table><thead align="left"><tr id="row62093530172115"><th class="cellrowborder" valign="top" width="36.54%" id="mcps1.1.4.1.1"><p id="p63520014172115"><a name="p63520014172115"></a><a name="p63520014172115"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="16.939999999999998%" id="mcps1.1.4.1.2"><p id="p974343172115"><a name="p974343172115"></a><a name="p974343172115"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.52%" id="mcps1.1.4.1.3"><p id="p39207829172115"><a name="p39207829172115"></a><a name="p39207829172115"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row61240780172115"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.1.4.1.1 "><p id="p61556132172115"><a name="p61556132172115"></a><a name="p61556132172115"></a>multipart-manifest</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.1.4.1.2 "><p id="p19990772172115"><a name="p19990772172115"></a><a name="p19990772172115"></a>String</p>
<p id="p45699225172115"><a name="p45699225172115"></a><a name="p45699225172115"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.1.4.1.3 "><p id="p686972921135"><a name="p686972921135"></a><a name="p686972921135"></a>If you include the <strong id="b36410264"><a name="b36410264"></a><a name="b36410264"></a>multipart-manifest=delete</strong> query parameter and the object is a static large object, the segment objects and the manifest object are deleted.</p>
<p id="p6182756521135"><a name="p6182756521135"></a><a name="p6182756521135"></a>If you omit the <strong id="b63550304"><a name="b63550304"></a><a name="b63550304"></a>multipart-manifest=delete</strong> query parameter, the manifest object is deleted and the segment objects are not deleted.</p>
<p id="p1957717721135"><a name="p1957717721135"></a><a name="p1957717721135"></a>If this is a dynamic large object, do not specify <strong id="b9999457211452"><a name="b9999457211452"></a><a name="b9999457211452"></a>multipart-manifest=delete</strong> query parameter.</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section2186955"></a>

Request URI parameters

<a name="table40884152172046"></a>
<table><thead align="left"><tr id="row13719513172046"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p37538754172046"><a name="p37538754172046"></a><a name="p37538754172046"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p52444361172046"><a name="p52444361172046"></a><a name="p52444361172046"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p46995656172046"><a name="p46995656172046"></a><a name="p46995656172046"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row34313268172046"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p27911353172046"><a name="p27911353172046"></a><a name="p27911353172046"></a>{account}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p46227143172046"><a name="p46227143172046"></a><a name="p46227143172046"></a>String</p>
<p id="p13391104172046"><a name="p13391104172046"></a><a name="p13391104172046"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p10937645172046"><a name="p10937645172046"></a><a name="p10937645172046"></a>Unique name of the account. In the current version, it indicates the unique ID of the account.</p>
</td>
</tr>
<tr id="row31329947172046"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p54697778172046"><a name="p54697778172046"></a><a name="p54697778172046"></a>{container}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p1335025172046"><a name="p1335025172046"></a><a name="p1335025172046"></a>String</p>
<p id="p12015232172046"><a name="p12015232172046"></a><a name="p12015232172046"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p33709711172046"><a name="p33709711172046"></a><a name="p33709711172046"></a>Unique name of the container.</p>
<p id="p34951946172046"><a name="p34951946172046"></a><a name="p34951946172046"></a>For details about container naming rules, see <a href="naming-rules.md">Naming Rules</a>.</p>
</td>
</tr>
<tr id="row12535347172046"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p8730148172046"><a name="p8730148172046"></a><a name="p8730148172046"></a>{object}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p36053382172046"><a name="p36053382172046"></a><a name="p36053382172046"></a>String</p>
<p id="p56044984172046"><a name="p56044984172046"></a><a name="p56044984172046"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p43349894172046"><a name="p43349894172046"></a><a name="p43349894172046"></a>Name of the object.</p>
<p id="p54604731172046"><a name="p54604731172046"></a><a name="p54604731172046"></a>For details about object naming rules, see <a href="naming-rules.md#section23579102">Object Naming Rules</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Request header parameters

<a name="table60907103172046"></a>
<table><thead align="left"><tr id="row25710638172046"><th class="cellrowborder" valign="top" width="36.54%" id="mcps1.2.4.1.1"><p id="p2186927172046"><a name="p2186927172046"></a><a name="p2186927172046"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="16.939999999999998%" id="mcps1.2.4.1.2"><p id="p50765957172046"><a name="p50765957172046"></a><a name="p50765957172046"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.52%" id="mcps1.2.4.1.3"><p id="p31399308172046"><a name="p31399308172046"></a><a name="p31399308172046"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5972932172046"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p14045460172046"><a name="p14045460172046"></a><a name="p14045460172046"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p63940485172046"><a name="p63940485172046"></a><a name="p63940485172046"></a>String</p>
<p id="p38593457172046"><a name="p38593457172046"></a><a name="p38593457172046"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p39062326172046"><a name="p39062326172046"></a><a name="p39062326172046"></a>Authentication token. If you omit this header, your request fails unless the account owner has granted you access through an ACL.</p>
</td>
</tr>
</tbody>
</table>

## Response Headers<a name="section30570743"></a>

The following table describes response header parameters:

<a name="table11410414172611"></a>
<table><thead align="left"><tr id="row5217026172611"><th class="cellrowborder" valign="top" width="24.740000000000002%" id="mcps1.1.4.1.1"><p id="p19925951172611"><a name="p19925951172611"></a><a name="p19925951172611"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="21.05%" id="mcps1.1.4.1.2"><p id="p3389316172611"><a name="p3389316172611"></a><a name="p3389316172611"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.21%" id="mcps1.1.4.1.3"><p id="p6099194172611"><a name="p6099194172611"></a><a name="p6099194172611"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row24272712172611"><td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.1.4.1.1 "><p id="p19932695172611"><a name="p19932695172611"></a><a name="p19932695172611"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.1.4.1.2 "><p id="p3935631172611"><a name="p3935631172611"></a><a name="p3935631172611"></a>String</p>
<p id="p35420681172611"><a name="p35420681172611"></a><a name="p35420681172611"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="54.21%" headers="mcps1.1.4.1.3 "><p id="p50502928172611"><a name="p50502928172611"></a><a name="p50502928172611"></a>If the operation succeeds, this value is 0.</p>
<p id="p51873175172611"><a name="p51873175172611"></a><a name="p51873175172611"></a>If the operation fails, this value is the length of the error text in the response body.</p>
</td>
</tr>
<tr id="row30623036172611"><td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.1.4.1.1 "><p id="p64546846172611"><a name="p64546846172611"></a><a name="p64546846172611"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.1.4.1.2 "><p id="p60912024172611"><a name="p60912024172611"></a><a name="p60912024172611"></a>String</p>
<p id="p11337310172611"><a name="p11337310172611"></a><a name="p11337310172611"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="54.21%" headers="mcps1.1.4.1.3 "><p id="p45906928172611"><a name="p45906928172611"></a><a name="p45906928172611"></a>MIME type of the object.</p>
</td>
</tr>
<tr id="row10509175172611"><td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.1.4.1.1 "><p id="p45936810172611"><a name="p45936810172611"></a><a name="p45936810172611"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.1.4.1.2 "><p id="p29894167172611"><a name="p29894167172611"></a><a name="p29894167172611"></a>String</p>
<p id="p612050172611"><a name="p612050172611"></a><a name="p612050172611"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="54.21%" headers="mcps1.1.4.1.3 "><p id="p49576070172611"><a name="p49576070172611"></a><a name="p49576070172611"></a>Transaction date and time.</p>
</td>
</tr>
<tr id="row43531449172611"><td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.1.4.1.1 "><p id="p36386495172611"><a name="p36386495172611"></a><a name="p36386495172611"></a>X-Trans-Id</p>
</td>
<td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.1.4.1.2 "><p id="p61624989172611"><a name="p61624989172611"></a><a name="p61624989172611"></a>Uuid</p>
<p id="p17753997172611"><a name="p17753997172611"></a><a name="p17753997172611"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="54.21%" headers="mcps1.1.4.1.3 "><p id="p28787684172611"><a name="p28787684172611"></a><a name="p28787684172611"></a>Unique transaction identifier.</p>
<p id="p57762564172611"><a name="p57762564172611"></a><a name="p57762564172611"></a></p>
</td>
</tr>
</tbody>
</table>

## Delete Object<a name="section2201390"></a>

Delete the  **goodbye**  object from the  **janeausten**  container:

```
curl -i http://172.28.54.12:80/v1/AUTH_4b34aa268d8c45879cf4da16443d3f95/janeausten/goodbye -H "X-Auth-Token:74565091b56b4783818430cecb283e7f"  -X DELETE
```

```
HTTP/1.1 204 No Content
X-Trans-Id: tx000001513cb0b434370c1-82374dd941
Content-Length: 0
Content-Type: text/html;charset=UTF-8
Date: Wed, 25 Nov 2015 03:29:52 GMT
```

## Delete Non-Existing Object<a name="section60098234144536"></a>

Delete the non-existing  **goodbye**  object from the  **janeausten**  container:

```
curl -i http://172.28.54.12:80/v1/AUTH_4b34aa268d8c45879cf4da16443d3f95/janeausten/goodbye -H "X-Auth-Token:74565091b56b4783818430cecb283e7f"  -X DELETE
```

```
HTTP/1.1 404 Not Found
X-Trans-Id: tx000001513cb1e9c6370c1-4c3eaf057d
Content-Type: text/html;charset=UTF-8
Date: Wed, 25 Nov 2015 03:31:11 GMT
Content-Length: 70

<html><h1>Not Found</h1><p>The resource could not be found.</p></html>
```

