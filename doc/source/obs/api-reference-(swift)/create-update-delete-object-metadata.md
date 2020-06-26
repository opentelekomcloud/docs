# Create/Update/Delete Object Metadata<a name="obs_03_0074"></a>

Users can send requests to create, update, or delete object metadata.

## Method<a name="section2546628103434"></a>

**Table  1**  Method description

<a name="table4950298103434"></a>
<table><thead align="left"><tr id="row45407113103434"><th class="cellrowborder" valign="top" width="12.280000000000001%" id="mcps1.2.4.1.1"><p id="p54097511103434"><a name="p54097511103434"></a><a name="p54097511103434"></a>Method</p>
</th>
<th class="cellrowborder" valign="top" width="44.42%" id="mcps1.2.4.1.2"><p id="p44182409103434"><a name="p44182409103434"></a><a name="p44182409103434"></a><strong id="b62097364103434"><a name="b62097364103434"></a><a name="b62097364103434"></a>URI</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43.3%" id="mcps1.2.4.1.3"><p id="p63830579103434"><a name="p63830579103434"></a><a name="p63830579103434"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row26049921103434"><td class="cellrowborder" valign="top" width="12.280000000000001%" headers="mcps1.2.4.1.1 "><p id="p29668845103434"><a name="p29668845103434"></a><a name="p29668845103434"></a>POST</p>
</td>
<td class="cellrowborder" valign="top" width="44.42%" headers="mcps1.2.4.1.2 "><p id="p54366205103434"><a name="p54366205103434"></a><a name="p54366205103434"></a>/v1/{account}/{container}/{object}</p>
</td>
<td class="cellrowborder" valign="top" width="43.3%" headers="mcps1.2.4.1.3 "><p id="p41586457103434"><a name="p41586457103434"></a><a name="p41586457103434"></a>Creates, updates, or deletes object metadata.</p>
</td>
</tr>
</tbody>
</table>

**\{account\}**  indicates the name of an account.

**\{container\}**  indicates the name of a container.

**\{object\}**  indicates the name of an object.

A POST request deletes all existing user metadata.

Metadata creation or update depends on whether the specified metadata exists. Metadata is created if it does not exist. Metadata is updated if it exists.

This operation does not involve a request body.

## Example Request<a name="section5807786810479"></a>

Create or update metadata:

```
curl -i $publicURL/marktwain/goodbye  -X POST -H "X-Auth-Token:$token" -H "X-Object-Meta-name:value"
```

Delete metadata:

```
curl -i $publicURL/marktwain/goodbye -X POST -H "X-Auth-Token:$token" -H "X-Object-Meta-name:"
```

## Request Query Parameters<a name="section5058163010479"></a>

This request does not include query parameters.

## Request Headers<a name="section3124263010479"></a>

Request URI parameters

<a name="table51767760175113"></a>
<table><thead align="left"><tr id="row30376867175113"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p44607195175113"><a name="p44607195175113"></a><a name="p44607195175113"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p37955196175113"><a name="p37955196175113"></a><a name="p37955196175113"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p20486532175113"><a name="p20486532175113"></a><a name="p20486532175113"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row36514397175113"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p4876166175113"><a name="p4876166175113"></a><a name="p4876166175113"></a>{account}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p59425164175113"><a name="p59425164175113"></a><a name="p59425164175113"></a>String</p>
<p id="p65064429175113"><a name="p65064429175113"></a><a name="p65064429175113"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p35727368175113"><a name="p35727368175113"></a><a name="p35727368175113"></a>Unique name of the account. In the current version, it indicates the unique ID of the account.</p>
</td>
</tr>
<tr id="row53110860175113"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p7012440175113"><a name="p7012440175113"></a><a name="p7012440175113"></a>{container}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p31136735175113"><a name="p31136735175113"></a><a name="p31136735175113"></a>String</p>
<p id="p11795165175113"><a name="p11795165175113"></a><a name="p11795165175113"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p15884331175113"><a name="p15884331175113"></a><a name="p15884331175113"></a>Unique name of the container.</p>
<p id="p8741252175113"><a name="p8741252175113"></a><a name="p8741252175113"></a>For details about container naming rules, see <a href="naming-rules.md">Naming Rules</a>.</p>
</td>
</tr>
<tr id="row36952817175113"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p40388219175113"><a name="p40388219175113"></a><a name="p40388219175113"></a>{object}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p50220297175113"><a name="p50220297175113"></a><a name="p50220297175113"></a>String</p>
<p id="p49329493175113"><a name="p49329493175113"></a><a name="p49329493175113"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p36266021175113"><a name="p36266021175113"></a><a name="p36266021175113"></a>Name of the object.</p>
<p id="p57958739175113"><a name="p57958739175113"></a><a name="p57958739175113"></a>For details about object naming rules, see <a href="naming-rules.md#section23579102">Object Naming Rules</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Request header parameters

<a name="table64146271175113"></a>
<table><thead align="left"><tr id="row46164324175113"><th class="cellrowborder" valign="top" width="36.54%" id="mcps1.2.4.1.1"><p id="p48322783175113"><a name="p48322783175113"></a><a name="p48322783175113"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="16.939999999999998%" id="mcps1.2.4.1.2"><p id="p62264539175113"><a name="p62264539175113"></a><a name="p62264539175113"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.52%" id="mcps1.2.4.1.3"><p id="p25257187175113"><a name="p25257187175113"></a><a name="p25257187175113"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row24660850175113"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p51371827175113"><a name="p51371827175113"></a><a name="p51371827175113"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p368424175113"><a name="p368424175113"></a><a name="p368424175113"></a>String</p>
<p id="p3315817175113"><a name="p3315817175113"></a><a name="p3315817175113"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p145800175113"><a name="p145800175113"></a><a name="p145800175113"></a>Authentication token. If you omit this header, your request fails unless the account owner has granted you access through an ACL.</p>
</td>
</tr>
<tr id="row1312208175113"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p39179986175113"><a name="p39179986175113"></a><a name="p39179986175113"></a>X-Object-Meta-name</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p19462313175113"><a name="p19462313175113"></a><a name="p19462313175113"></a>String</p>
<p id="p40943096175113"><a name="p40943096175113"></a><a name="p40943096175113"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p28056489175113"><a name="p28056489175113"></a><a name="p28056489175113"></a>Object metadata, where <strong id="b851820542154254"><a name="b851820542154254"></a><a name="b851820542154254"></a>{name}</strong>&nbsp;is the name of the metadata item. To delete this item, send an empty value in this header. You must specify an&nbsp;<strong id="b44007985"><a name="b44007985"></a><a name="b44007985"></a>X-Object-Meta-{name}</strong>&nbsp;header for each metadata item (for each&nbsp;<strong id="b60527552"><a name="b60527552"></a><a name="b60527552"></a>{name}</strong>) that you want to add or update.</p>
</td>
</tr>
<tr id="row51181813175113"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p52086202175113"><a name="p52086202175113"></a><a name="p52086202175113"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p58232819175113"><a name="p58232819175113"></a><a name="p58232819175113"></a>String</p>
<p id="p54333327175113"><a name="p54333327175113"></a><a name="p54333327175113"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p38923346175113"><a name="p38923346175113"></a><a name="p38923346175113"></a>Sets the MIME type of the object.</p>
</td>
</tr>
<tr id="row14765795175113"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p55178729175113"><a name="p55178729175113"></a><a name="p55178729175113"></a>X-Detect-Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p40292101175113"><a name="p40292101175113"></a><a name="p40292101175113"></a>Boolean</p>
<p id="p27084589175113"><a name="p27084589175113"></a><a name="p27084589175113"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p46368130175113"><a name="p46368130175113"></a><a name="p46368130175113"></a>If it is set to <strong id="b66837559"><a name="b66837559"></a><a name="b66837559"></a>true</strong>, OBS guesses the content type based on the file name extension and ignores the value sent in the&nbsp;<strong id="b64667125"><a name="b64667125"></a><a name="b64667125"></a>Content-Type</strong> header, if present.</p>
</td>
</tr>
<tr id="row40355164175113"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p47542824175113"><a name="p47542824175113"></a><a name="p47542824175113"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p25763561175113"><a name="p25763561175113"></a><a name="p25763561175113"></a>String</p>
<p id="p30545465175113"><a name="p30545465175113"></a><a name="p30545465175113"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p58263620175113"><a name="p58263620175113"></a><a name="p58263620175113"></a>Set to the length of the object content. Do not set if chunked transfer encoding is being used.</p>
</td>
</tr>
<tr id="row46549969175113"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p12451172175113"><a name="p12451172175113"></a><a name="p12451172175113"></a>Content-Disposition</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p1911991175113"><a name="p1911991175113"></a><a name="p1911991175113"></a>String</p>
<p id="p17207920175113"><a name="p17207920175113"></a><a name="p17207920175113"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p51664262175113"><a name="p51664262175113"></a><a name="p51664262175113"></a>When the header is set to <strong id="b5395578"><a name="b5395578"></a><a name="b5395578"></a>{newname}</strong>&nbsp;and an object is downloaded through a browser, the default object name&nbsp;<strong id="b48560202"><a name="b48560202"></a><a name="b48560202"></a>{newname}</strong> is returned.</p>
</td>
</tr>
<tr id="row62325182175113"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p15174978175113"><a name="p15174978175113"></a><a name="p15174978175113"></a>Content-Encoding</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p21213735175113"><a name="p21213735175113"></a><a name="p21213735175113"></a>String</p>
<p id="p56705893175113"><a name="p56705893175113"></a><a name="p56705893175113"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p29774654175113"><a name="p29774654175113"></a><a name="p29774654175113"></a>If this header is set, the value is the encoding format used when an object is downloaded through a browser.</p>
</td>
</tr>
</tbody>
</table>

## Response Headers<a name="section59311107103522"></a>

The following table describes response header parameters:

<a name="table27894677175355"></a>
<table><thead align="left"><tr id="row27090943175355"><th class="cellrowborder" valign="top" width="23.43%" id="mcps1.1.4.1.1"><p id="p46882809175355"><a name="p46882809175355"></a><a name="p46882809175355"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="21.05%" id="mcps1.1.4.1.2"><p id="p39411212175355"><a name="p39411212175355"></a><a name="p39411212175355"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.52%" id="mcps1.1.4.1.3"><p id="p38191583175355"><a name="p38191583175355"></a><a name="p38191583175355"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6510490175355"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p57587686175355"><a name="p57587686175355"></a><a name="p57587686175355"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.1.4.1.2 "><p id="p34090986175355"><a name="p34090986175355"></a><a name="p34090986175355"></a>String</p>
<p id="p38383425175355"><a name="p38383425175355"></a><a name="p38383425175355"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="55.52%" headers="mcps1.1.4.1.3 "><p id="p22049741175355"><a name="p22049741175355"></a><a name="p22049741175355"></a>If the operation succeeds, the value is the length of the response body.</p>
<p id="p64229949175355"><a name="p64229949175355"></a><a name="p64229949175355"></a>If the operation fails, this value is the length of the error text in the response body.</p>
</td>
</tr>
<tr id="row41198630175355"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p48754739175355"><a name="p48754739175355"></a><a name="p48754739175355"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.1.4.1.2 "><p id="p56819805175355"><a name="p56819805175355"></a><a name="p56819805175355"></a>String</p>
<p id="p41616200175355"><a name="p41616200175355"></a><a name="p41616200175355"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="55.52%" headers="mcps1.1.4.1.3 "><p id="p15469031175355"><a name="p15469031175355"></a><a name="p15469031175355"></a>MIME type of the object.</p>
</td>
</tr>
<tr id="row5003558175355"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p2635029175355"><a name="p2635029175355"></a><a name="p2635029175355"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.1.4.1.2 "><p id="p12110785175355"><a name="p12110785175355"></a><a name="p12110785175355"></a>String</p>
<p id="p41888201175355"><a name="p41888201175355"></a><a name="p41888201175355"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="55.52%" headers="mcps1.1.4.1.3 "><p id="p37501082175355"><a name="p37501082175355"></a><a name="p37501082175355"></a>Transaction date and time.</p>
</td>
</tr>
<tr id="row1965421175355"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p24981438175355"><a name="p24981438175355"></a><a name="p24981438175355"></a>X-Trans-Id</p>
</td>
<td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.1.4.1.2 "><p id="p10230636175355"><a name="p10230636175355"></a><a name="p10230636175355"></a>Uuid</p>
<p id="p24966865175355"><a name="p24966865175355"></a><a name="p24966865175355"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="55.52%" headers="mcps1.1.4.1.3 "><p id="p9050197175355"><a name="p9050197175355"></a><a name="p9050197175355"></a>Unique transaction identifier.</p>
</td>
</tr>
</tbody>
</table>

## Create Object Metadata<a name="section63148656103541"></a>

Create object metadata  **Author** with the value set to **other**:

```
curl -i http://172.28.54.12:80/v1/AUTH_4b34aa268d8c45879cf4da16443d3f95/marketwain/goodbye -H "X-Auth-Token:74565091b56b4783818430cecb283e7f"  -XPOST  -H "X-Object-Meta-author:other"
```

```
HTTP/1.1 202 Accepted
X-Trans-Id: tx000001513cba7176370c1-adee95a013
Content-Type: text/html;charset=UTF-8
Date: Wed, 25 Nov 2015 03:40:30 GMT
Content-Length: 76

<html><h1>Accepted</h1><p>The request is accepted for processing.</p></html>
```

## Update Object Metadata<a name="section59441921103541"></a>

Update object metadata  **Author** with the value set to **marktwain**:

```
curl -i http://172.28.54.12:80/v1/AUTH_4b34aa268d8c45879cf4da16443d3f95/marketwain/goodbye -H "X-Auth-Token:74565091b56b4783818430cecb283e7f"  -XPOST  -H "X-Object-Meta-author:marktwain"
```

```
HTTP/1.1 202 Accepted
X-Trans-Id: tx000001513cbfbf2f370c2-f9e7f1cf40
Content-Type: text/html;charset=UTF-8
Date: Wed, 25 Nov 2015 03:46:18 GMT
Content-Length: 76

<html><h1>Accepted</h1><p>The request is accepted for processing.</p></html>
```

## Delete Object Metadata<a name="section54329679114246"></a>

Delete the metadata author, and leave the value blank.

```
curl -i http://172.28.54.12:80/v1/AUTH_4b34aa268d8c45879cf4da16443d3f95/marketwain/goodbye -H "X-Auth-Token:74565091b56b4783818430cecb283e7f"  -XPOST  -H "X-Object-Meta-author:"
```

```
HTTP/1.1 202 Accepted
X-Trans-Id: tx000001513cc10d85370c2-cddc60cba5
Content-Type: text/html;charset=UTF-8
Date: Wed, 25 Nov 2015 03:47:43 GMT
Content-Length: 76

<html><h1>Accepted</h1><p>The request is accepted for processing.</p></html>
```

