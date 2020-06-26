# Show Object Metadata<a name="obs_03_0070"></a>

This operation shows object metadata.

If the  **Content-Length**  response header is not 0, the cURL command stalls after it prints the response headers because it is waiting for a response body. However, OBS does not return a response body.

## Method<a name="section42203044114811"></a>

**Table  1**  Method description

<a name="table63003397114811"></a>
<table><thead align="left"><tr id="row958610114811"><th class="cellrowborder" valign="top" width="13.969999999999999%" id="mcps1.2.4.1.1"><p id="p10538570114811"><a name="p10538570114811"></a><a name="p10538570114811"></a>Method</p>
</th>
<th class="cellrowborder" valign="top" width="52.7%" id="mcps1.2.4.1.2"><p id="p32207183114811"><a name="p32207183114811"></a><a name="p32207183114811"></a><strong id="b21429195114811"><a name="b21429195114811"></a><a name="b21429195114811"></a>URI</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p58043236114811"><a name="p58043236114811"></a><a name="p58043236114811"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row34935397114811"><td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.1 "><p id="p11194907114811"><a name="p11194907114811"></a><a name="p11194907114811"></a>HEAD</p>
</td>
<td class="cellrowborder" valign="top" width="52.7%" headers="mcps1.2.4.1.2 "><p id="p3700552617321"><a name="p3700552617321"></a><a name="p3700552617321"></a>/v1/{account}/{container}/{object}{?temp_url_sig,temp_url_expires}</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p32688443114811"><a name="p32688443114811"></a><a name="p32688443114811"></a>Shows object metadata.</p>
</td>
</tr>
</tbody>
</table>

**\{account\}**  indicates the name of an account.

**\{container\}**  indicates the name of a container.

**\{object\}**  indicates the name of an object.

This operation does not involve a request body.

## Example Request<a name="section56060206114811"></a>

Show object metadata:

```
curl -i $publicURL/marktwain/goodbye -X HEAD -H "X-Auth-Token:$token"
```

## Request Query Parameters<a name="section47707984114811"></a>

<a name="table39845527173423"></a>
<table><thead align="left"><tr id="row7926438173423"><th class="cellrowborder" valign="top" width="22.68%" id="mcps1.1.4.1.1"><p id="p38061735173423"><a name="p38061735173423"></a><a name="p38061735173423"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.29%" id="mcps1.1.4.1.2"><p id="p31044029173423"><a name="p31044029173423"></a><a name="p31044029173423"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60.029999999999994%" id="mcps1.1.4.1.3"><p id="p15410692173423"><a name="p15410692173423"></a><a name="p15410692173423"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row42039985173423"><td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.1.4.1.1 "><p id="p49795625173423"><a name="p49795625173423"></a><a name="p49795625173423"></a>temp_url_sig</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.1.4.1.2 "><p id="p6913838173423"><a name="p6913838173423"></a><a name="p6913838173423"></a>String</p>
<p id="p56399519173444"><a name="p56399519173444"></a><a name="p56399519173444"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="60.029999999999994%" headers="mcps1.1.4.1.3 "><p id="p23149991173423"><a name="p23149991173423"></a><a name="p23149991173423"></a>Used with TempURL to sign the request.</p>
</td>
</tr>
<tr id="row32018918173423"><td class="cellrowborder" valign="top" width="22.68%" headers="mcps1.1.4.1.1 "><p id="p43395537173423"><a name="p43395537173423"></a><a name="p43395537173423"></a>temp_url_expires</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.1.4.1.2 "><p id="p25377613173423"><a name="p25377613173423"></a><a name="p25377613173423"></a>String</p>
<p id="p61076842173454"><a name="p61076842173454"></a><a name="p61076842173454"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="60.029999999999994%" headers="mcps1.1.4.1.3 "><p id="p42320769173423"><a name="p42320769173423"></a><a name="p42320769173423"></a>Used with TempURL to specify the expiry time of the signature.</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section16729309114811"></a>

Request URI parameters

<a name="table8826958173112"></a>
<table><thead align="left"><tr id="row31050417173112"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p32055862173112"><a name="p32055862173112"></a><a name="p32055862173112"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p14838955173112"><a name="p14838955173112"></a><a name="p14838955173112"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p13071263173112"><a name="p13071263173112"></a><a name="p13071263173112"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row66601109173112"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p25980745173112"><a name="p25980745173112"></a><a name="p25980745173112"></a>{account}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p24065630173112"><a name="p24065630173112"></a><a name="p24065630173112"></a>String</p>
<p id="p15264084173112"><a name="p15264084173112"></a><a name="p15264084173112"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p28431325173112"><a name="p28431325173112"></a><a name="p28431325173112"></a>Unique name of the account. In the current version, it indicates the unique ID of the account.</p>
</td>
</tr>
<tr id="row54555338173112"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p56906224173112"><a name="p56906224173112"></a><a name="p56906224173112"></a>{container}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p46001431173112"><a name="p46001431173112"></a><a name="p46001431173112"></a>String</p>
<p id="p11359698173112"><a name="p11359698173112"></a><a name="p11359698173112"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p47720349173112"><a name="p47720349173112"></a><a name="p47720349173112"></a>Unique name of the container.</p>
<p id="p26829958173112"><a name="p26829958173112"></a><a name="p26829958173112"></a>For details about container naming rules, see <a href="naming-rules.md">Naming Rules</a>.</p>
</td>
</tr>
<tr id="row25743007173112"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p4808792173112"><a name="p4808792173112"></a><a name="p4808792173112"></a>{object}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p53967833173112"><a name="p53967833173112"></a><a name="p53967833173112"></a>String</p>
<p id="p15948452173112"><a name="p15948452173112"></a><a name="p15948452173112"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p16756261173112"><a name="p16756261173112"></a><a name="p16756261173112"></a>Name of the object.</p>
<p id="p16588629173112"><a name="p16588629173112"></a><a name="p16588629173112"></a>For details about object naming rules, see <a href="naming-rules.md#section23579102">Object Naming Rules</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Request header parameters

<a name="table1501728173112"></a>
<table><thead align="left"><tr id="row59829943173112"><th class="cellrowborder" valign="top" width="36.54%" id="mcps1.2.4.1.1"><p id="p14387195173112"><a name="p14387195173112"></a><a name="p14387195173112"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="16.939999999999998%" id="mcps1.2.4.1.2"><p id="p19282668173112"><a name="p19282668173112"></a><a name="p19282668173112"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.52%" id="mcps1.2.4.1.3"><p id="p31312818173112"><a name="p31312818173112"></a><a name="p31312818173112"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10031201173112"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p7220937173112"><a name="p7220937173112"></a><a name="p7220937173112"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p48025001173112"><a name="p48025001173112"></a><a name="p48025001173112"></a>String</p>
<p id="p29571830173112"><a name="p29571830173112"></a><a name="p29571830173112"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p46508030173112"><a name="p46508030173112"></a><a name="p46508030173112"></a>Authentication token.</p>
</td>
</tr>
</tbody>
</table>

## Response Headers<a name="section84586421267"></a>

The following table describes response header parameters:

<a name="table58398915173738"></a>
<table><thead align="left"><tr id="row10138041173738"><th class="cellrowborder" valign="top" width="23.43%" id="mcps1.1.4.1.1"><p id="p15875029173738"><a name="p15875029173738"></a><a name="p15875029173738"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="20.669999999999998%" id="mcps1.1.4.1.2"><p id="p10808940173738"><a name="p10808940173738"></a><a name="p10808940173738"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.900000000000006%" id="mcps1.1.4.1.3"><p id="p3108968173738"><a name="p3108968173738"></a><a name="p3108968173738"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row27511085173747"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p13805384173747"><a name="p13805384173747"></a><a name="p13805384173747"></a>Last-Modified</p>
</td>
<td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p1809815717386"><a name="p1809815717386"></a><a name="p1809815717386"></a>String</p>
<p id="p2866569117386"><a name="p2866569117386"></a><a name="p2866569117386"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="55.900000000000006%" headers="mcps1.1.4.1.3 "><p id="p47270488173747"><a name="p47270488173747"></a><a name="p47270488173747"></a>Date and time that the object was created or the last time that the metadata was changed.</p>
</td>
</tr>
<tr id="row50499889173738"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p63959214173738"><a name="p63959214173738"></a><a name="p63959214173738"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p13313864173738"><a name="p13313864173738"></a><a name="p13313864173738"></a>String</p>
<p id="p52715915173738"><a name="p52715915173738"></a><a name="p52715915173738"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="55.900000000000006%" headers="mcps1.1.4.1.3 "><p id="p43632113173738"><a name="p43632113173738"></a><a name="p43632113173738"></a>Length of the object content in the response body, in bytes.</p>
</td>
</tr>
<tr id="row1085835173738"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p20843848173738"><a name="p20843848173738"></a><a name="p20843848173738"></a>Etag</p>
</td>
<td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p10630117173738"><a name="p10630117173738"></a><a name="p10630117173738"></a>String</p>
<p id="p28562191173738"><a name="p28562191173738"></a><a name="p28562191173738"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="55.900000000000006%" headers="mcps1.1.4.1.3 "><p id="p31836128173738"><a name="p31836128173738"></a><a name="p31836128173738"></a>For ordinary objects, this value is the MD5 checksum of the uploaded object content.</p>
<p id="p18089696173738"><a name="p18089696173738"></a><a name="p18089696173738"></a>For static large objects, this value is the MD5 checksum of the concatenated string of MD5 checksums for each of the segments.</p>
<p id="p28589541173738"><a name="p28589541173738"></a><a name="p28589541173738"></a>For dynamic large objects, the value is the MD5 checksum of the manifest file.</p>
</td>
</tr>
<tr id="row55979278173738"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p38027709173738"><a name="p38027709173738"></a><a name="p38027709173738"></a>X-Object-Meta-name</p>
</td>
<td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p60345621173738"><a name="p60345621173738"></a><a name="p60345621173738"></a>String</p>
<p id="p6239679173738"><a name="p6239679173738"></a><a name="p6239679173738"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="55.900000000000006%" headers="mcps1.1.4.1.3 "><p id="p35652006173738"><a name="p35652006173738"></a><a name="p35652006173738"></a>Custom object metadata item.</p>
<p id="p52432605173738"><a name="p52432605173738"></a><a name="p52432605173738"></a><strong id="b12347023"><a name="b12347023"></a><a name="b12347023"></a>{name}</strong> is the name of the metadata item.</p>
</td>
</tr>
<tr id="row2131402173738"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p38425874173738"><a name="p38425874173738"></a><a name="p38425874173738"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p25488103173738"><a name="p25488103173738"></a><a name="p25488103173738"></a>String</p>
<p id="p28066337173738"><a name="p28066337173738"></a><a name="p28066337173738"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="55.900000000000006%" headers="mcps1.1.4.1.3 "><p id="p58780852173738"><a name="p58780852173738"></a><a name="p58780852173738"></a>MIME type of the object.</p>
</td>
</tr>
<tr id="row59265622173738"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p35786048173738"><a name="p35786048173738"></a><a name="p35786048173738"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p12988758173738"><a name="p12988758173738"></a><a name="p12988758173738"></a>String</p>
<p id="p49789966173738"><a name="p49789966173738"></a><a name="p49789966173738"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="55.900000000000006%" headers="mcps1.1.4.1.3 "><p id="p6455442173738"><a name="p6455442173738"></a><a name="p6455442173738"></a>Transaction date and time.</p>
</td>
</tr>
<tr id="row58098985173738"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p8397365173738"><a name="p8397365173738"></a><a name="p8397365173738"></a>X-Trans-Id</p>
</td>
<td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p9097998173738"><a name="p9097998173738"></a><a name="p9097998173738"></a>Uuid</p>
<p id="p14773123173738"><a name="p14773123173738"></a><a name="p14773123173738"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="55.900000000000006%" headers="mcps1.1.4.1.3 "><p id="p55772281173738"><a name="p55772281173738"></a><a name="p55772281173738"></a>Unique transaction identifier.</p>
<p id="p32188485173738"><a name="p32188485173738"></a><a name="p32188485173738"></a></p>
</td>
</tr>
<tr id="row21260912173738"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p44412303173738"><a name="p44412303173738"></a><a name="p44412303173738"></a>X-Timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p40626815173738"><a name="p40626815173738"></a><a name="p40626815173738"></a>Datetime</p>
<p id="p30097021173738"><a name="p30097021173738"></a><a name="p30097021173738"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="55.900000000000006%" headers="mcps1.1.4.1.3 "><p id="p63238897173738"><a name="p63238897173738"></a><a name="p63238897173738"></a>Object creation time and date, in UNIX Epoch timestamp format.</p>
</td>
</tr>
<tr id="row20359477174132"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p1569659817420"><a name="p1569659817420"></a><a name="p1569659817420"></a>Content-Encoding</p>
</td>
<td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p6346490617420"><a name="p6346490617420"></a><a name="p6346490617420"></a>String</p>
<p id="p3431324517420"><a name="p3431324517420"></a><a name="p3431324517420"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="55.900000000000006%" headers="mcps1.1.4.1.3 "><p id="p2790947517420"><a name="p2790947517420"></a><a name="p2790947517420"></a>Code used when an object is downloaded through a browser.</p>
</td>
</tr>
<tr id="row26152510174133"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p1202190517420"><a name="p1202190517420"></a><a name="p1202190517420"></a>Content-Disposition</p>
</td>
<td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p3425028017420"><a name="p3425028017420"></a><a name="p3425028017420"></a>String</p>
<p id="p3981706417420"><a name="p3981706417420"></a><a name="p3981706417420"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="55.900000000000006%" headers="mcps1.1.4.1.3 "><p id="p395673617420"><a name="p395673617420"></a><a name="p395673617420"></a>When an object is downloaded through a browser, the default object name is <strong id="b49409500"><a name="b49409500"></a><a name="b49409500"></a>newname</strong>.</p>
</td>
</tr>
<tr id="row46767608174213"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p1872657917436"><a name="p1872657917436"></a><a name="p1872657917436"></a>X-Object-Manifest</p>
</td>
<td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p4045795317436"><a name="p4045795317436"></a><a name="p4045795317436"></a>String</p>
<p id="p2857725817436"><a name="p2857725817436"></a><a name="p2857725817436"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="55.900000000000006%" headers="mcps1.1.4.1.3 "><p id="p3305656717436"><a name="p3305656717436"></a><a name="p3305656717436"></a>This is the identifier of a dynamic large object. The value is the container and object name prefix of the segment objects in the form of <em id="i269219602153723"><a name="i269219602153723"></a><a name="i269219602153723"></a>container/prefix</em>.</p>
</td>
</tr>
<tr id="row51546946174214"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p615569217436"><a name="p615569217436"></a><a name="p615569217436"></a>X-Static-Large-Object</p>
</td>
<td class="cellrowborder" valign="top" width="20.669999999999998%" headers="mcps1.1.4.1.2 "><p id="p2884903517436"><a name="p2884903517436"></a><a name="p2884903517436"></a>String</p>
<p id="p5831473017436"><a name="p5831473017436"></a><a name="p5831473017436"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="55.900000000000006%" headers="mcps1.1.4.1.3 "><p id="p2587266517436"><a name="p2587266517436"></a><a name="p2587266517436"></a>Set to <strong id="b2105663"><a name="b2105663"></a><a name="b2105663"></a>True</strong> if this object is a static large object manifest object.</p>
</td>
</tr>
</tbody>
</table>

## Show Object Metadata<a name="section42277158"></a>

Show metadata of the  **goodbye**  object in the  **marketwain**  container:

```
curl -i http://172.28.54.12:80/v1/AUTH_4b34aa268d8c45879cf4da16443d3f95/marketwain/goodbye -H "X-Auth-Token:74565091b56b4783818430cecb283e7f"  -XHEAD
```

```
HTTP/1.1 200 OK
X-Trans-Id: tx000001513cbab7ca370c1-d95dee8729
Accept-Ranges: bytes
Content-Length: 15
Content-Type: application/octet-stream
Date: Wed, 25 Nov 2015 03:40:48 GMT
ETag: e85f5c28b588fa64a379ba876e3591d2
Last-Modified: Wed, 25 Nov 2015 03:40:30 GMT
X-Object-Meta-Author: other
X-Timestamp: 1448422830.47760
```

