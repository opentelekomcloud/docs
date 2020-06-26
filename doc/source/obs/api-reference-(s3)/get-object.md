# GET Object<a name="EN-US_TOPIC_0125560336"></a>

You can use this operation to obtain the content and metadata of an object, as long as you have  **READ**  permission for the object.

This operation makes server-side encryption available.

## Versioning<a name="section20062571"></a>

By default, the content of the object with the latest version ID is obtained. If the version ID of the object is a deletion mark,  **404** is returned. You can specify **versionId**  to obtain the content of an object of the desired version.

## Cold Objects<a name="section5921648520359"></a>

For Cold objects, the response varies with the restoration status of the objects. If the objects have been restored, then the  **x-amz-restore** header is returned indicating the expiry date of the objects when they are successfully downloaded. If you request to download Cold objects that are not restored or are being restored, a **403 Forbidden**  error is returned.

## Request Syntax<a name="section39480712"></a>

```
GET /ObjectName HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com 
 Accept: */* 
 Date: date 
 Authorization: authorization 
 Range:bytes=byte_range 
 <Optional Additional Header>
```

>![](/images/icon-note.gif) **NOTE:**   
>In this request, header  **Range**  is optional. If this header is not specified, all data of an object is returned.  

## Request Parameters<a name="section19782092"></a>

In a  **GET** request, you can override values for a set of response headers using the request parameters listed in [Table 1](#table63181911). Response headers that you can override are **Content-Type**, **Content-Language**, **Expires**, **Cache-Control**, **Content-Disposition**, and **Content-Encoding**.

**Table  1**  Request parameters

<a name="table63181911"></a>
<table><thead align="left"><tr id="row6292375"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p39920339"><a name="p39920339"></a><a name="p39920339"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p12322052"><a name="p12322052"></a><a name="p12322052"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p58562194"><a name="p58562194"></a><a name="p58562194"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row45917284"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p28312547"><a name="p28312547"></a><a name="p28312547"></a>response-content-type</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p11614966"><a name="p11614966"></a><a name="p11614966"></a>Overrides the <strong id="b37425835"><a name="b37425835"></a><a name="b37425835"></a>Content-Type</strong> header in the response.</p>
<p id="p1288198"><a name="p1288198"></a><a name="p1288198"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p37235194"><a name="p37235194"></a><a name="p37235194"></a>Optional</p>
</td>
</tr>
<tr id="row66681293"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p32475667"><a name="p32475667"></a><a name="p32475667"></a>response-content-language</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p13283377"><a name="p13283377"></a><a name="p13283377"></a>Overrides the <strong id="b52441537"><a name="b52441537"></a><a name="b52441537"></a>Content-Language</strong> header in the response.</p>
<p id="p2211792"><a name="p2211792"></a><a name="p2211792"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p44937496"><a name="p44937496"></a><a name="p44937496"></a>Optional</p>
</td>
</tr>
<tr id="row1784282"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p10309169"><a name="p10309169"></a><a name="p10309169"></a>response-expires</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p29736389"><a name="p29736389"></a><a name="p29736389"></a>Overrides the <strong id="b66300913"><a name="b66300913"></a><a name="b66300913"></a>Expires</strong> header in the response.</p>
<p id="p59837309"><a name="p59837309"></a><a name="p59837309"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14983874"><a name="p14983874"></a><a name="p14983874"></a>Optional</p>
</td>
</tr>
<tr id="row637140"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p51608407"><a name="p51608407"></a><a name="p51608407"></a>response-cache-control</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p19531418"><a name="p19531418"></a><a name="p19531418"></a>Overrides the <strong id="b41565035"><a name="b41565035"></a><a name="b41565035"></a>Cache-Control</strong> header in the response.</p>
<p id="p38540997"><a name="p38540997"></a><a name="p38540997"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p34813057"><a name="p34813057"></a><a name="p34813057"></a>Optional</p>
</td>
</tr>
<tr id="row44882061"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p11568292"><a name="p11568292"></a><a name="p11568292"></a>response-content-disposition</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p64616480"><a name="p64616480"></a><a name="p64616480"></a>Overrides the <strong id="b44677416"><a name="b44677416"></a><a name="b44677416"></a>Content-Disposition</strong> header in the response.</p>
<p id="p66552425"><a name="p66552425"></a><a name="p66552425"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p22037350"><a name="p22037350"></a><a name="p22037350"></a>Optional</p>
</td>
</tr>
<tr id="row64118428"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p26210179"><a name="p26210179"></a><a name="p26210179"></a>response-content-encoding</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p42649746"><a name="p42649746"></a><a name="p42649746"></a>Overrides the <strong id="b48303401"><a name="b48303401"></a><a name="b48303401"></a>Content-Encoding</strong> header in the response.</p>
<p id="p32077426"><a name="p32077426"></a><a name="p32077426"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p48134731"><a name="p48134731"></a><a name="p48134731"></a>Optional</p>
</td>
</tr>
<tr id="row30559396"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p59391972"><a name="p59391972"></a><a name="p59391972"></a>versionId</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p46020400"><a name="p46020400"></a><a name="p46020400"></a>Specifies the version ID of the object whose content is obtained.</p>
<p id="p11530423"><a name="p11530423"></a><a name="p11530423"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p61549057"><a name="p61549057"></a><a name="p61549057"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section43821104"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md). In addition, you can add optional headers to this request.  [Table 2](#table54982876)  describes the optional headers.

**Table  2**  Optional request headers

<a name="table54982876"></a>
<table><thead align="left"><tr id="row19581186"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p42572248"><a name="p42572248"></a><a name="p42572248"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p25800070"><a name="p25800070"></a><a name="p25800070"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p9430965"><a name="p9430965"></a><a name="p9430965"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row25710733"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2194613"><a name="p2194613"></a><a name="p2194613"></a>Range</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p43545941"><a name="p43545941"></a><a name="p43545941"></a>Obtains the specified range bytes of an object. The value is a range starting from 0 to maximum object length minus one. If the range is invalid, all object data is returned.</p>
<p id="p56369154"><a name="p56369154"></a><a name="p56369154"></a>Type: String</p>
<p id="p37560342"><a name="p37560342"></a><a name="p37560342"></a>Note:</p>
<p id="p2498762"><a name="p2498762"></a><a name="p2498762"></a>The header format for a single range is <em id="i22488863"><a name="i22488863"></a><a name="i22488863"></a>bytes=byte_range</em>, for example, <strong id="b126647117125"><a name="b126647117125"></a><a name="b126647117125"></a>bytes=0-4</strong> or&nbsp;<strong id="b101236412409"><a name="b101236412409"></a><a name="b101236412409"></a>bytes=512-1024</strong>. The header format for multiple ranges is, for example, <strong id="b393316216446"><a name="b393316216446"></a><a name="b393316216446"></a>bytes=10-20,30-40</strong>. If there are multiple ranges, the output is as follows:</p>
<p id="p57272696212419"><a name="p57272696212419"></a><a name="p57272696212419"></a>--5926640d-5ca3-4e56-a9e9-5493dab2da66</p>
<p id="p45692217212419"><a name="p45692217212419"></a><a name="p45692217212419"></a>Content-type: binary/octet-stream</p>
<p id="p8576776212419"><a name="p8576776212419"></a><a name="p8576776212419"></a>Content-range: bytes 10-20/7279</p>
<p id="p23630265212419"><a name="p23630265212419"></a><a name="p23630265212419"></a>xxxx</p>
<p id="p11345797212419"><a name="p11345797212419"></a><a name="p11345797212419"></a>--5926640d-5ca3-4e56-a9e9-5493dab2da66</p>
<p id="p35003314212419"><a name="p35003314212419"></a><a name="p35003314212419"></a>Content-type: binary/octet-stream</p>
<p id="p46594378212419"><a name="p46594378212419"></a><a name="p46594378212419"></a>Content-range: bytes 30-40/7279</p>
<p id="p16048259212419"><a name="p16048259212419"></a><a name="p16048259212419"></a>yyyy</p>
<div class="note" id="note149731316529"><a name="note149731316529"></a><a name="note149731316529"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1718914112571"><a name="p1718914112571"></a><a name="p1718914112571"></a><strong id="b141897115713"><a name="b141897115713"></a><a name="b141897115713"></a>--5926640d-5ca3-4e56-a9e9-5493dab2da66--</strong> is a randomly generated character string and functions as a separator.</p>
<p id="p1749711135529"><a name="p1749711135529"></a><a name="p1749711135529"></a><strong id="b152971157125711"><a name="b152971157125711"></a><a name="b152971157125711"></a>Content-type</strong> indicates the type of the range data.</p>
<p id="p144891575718"><a name="p144891575718"></a><a name="p144891575718"></a><strong id="b14730163175818"><a name="b14730163175818"></a><a name="b14730163175818"></a>Content-range</strong> indicates the data range or the total object size.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p44153132"><a name="p44153132"></a><a name="p44153132"></a>Optional</p>
</td>
</tr>
<tr id="row61833870"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p42487544"><a name="p42487544"></a><a name="p42487544"></a>If-Modified-Since</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p18939022"><a name="p18939022"></a><a name="p18939022"></a>Returns the object only if it has been modified since the time specified by this header, otherwise <strong id="b24247951212"><a name="b24247951212"></a><a name="b24247951212"></a>304 Not Modified</strong> is returned.</p>
<p id="p57665850"><a name="p57665850"></a><a name="p57665850"></a>Type: HTTP time string complying with the format specified in http://www.ietf.org/rfc/rfc2616.txt.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p40422241"><a name="p40422241"></a><a name="p40422241"></a>Optional</p>
</td>
</tr>
<tr id="row28255855"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p7022941"><a name="p7022941"></a><a name="p7022941"></a>If-Unmodified-Since</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p31987323"><a name="p31987323"></a><a name="p31987323"></a>Returns the object only if it has not been modified since the time specified by this header, otherwise <strong id="b1127351891211"><a name="b1127351891211"></a><a name="b1127351891211"></a>412 Precondition Failed</strong> is returned.</p>
<p id="p40836337"><a name="p40836337"></a><a name="p40836337"></a>Type: HTTP time string complying with the format specified in http://www.ietf.org/rfc/rfc2616.txt.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19409000"><a name="p19409000"></a><a name="p19409000"></a>Optional</p>
</td>
</tr>
<tr id="row40463275"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p56299846"><a name="p56299846"></a><a name="p56299846"></a>If-Match</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p63993653"><a name="p63993653"></a><a name="p63993653"></a>Returns the object only if its ETag is the same as the one specified by this header, otherwise <strong id="b454719261122"><a name="b454719261122"></a><a name="b454719261122"></a>412 Precondition Failed</strong> is returned.</p>
<p id="p16103393"><a name="p16103393"></a><a name="p16103393"></a>Type: String</p>
<p id="p10712809"><a name="p10712809"></a><a name="p10712809"></a>Note:</p>
<p id="p29306417"><a name="p29306417"></a><a name="p29306417"></a>An example ETag value is <strong id="b62431162"><a name="b62431162"></a><a name="b62431162"></a>0f64741bf7cb1089e988e4585d0d3434</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p23759356"><a name="p23759356"></a><a name="p23759356"></a>Optional</p>
</td>
</tr>
<tr id="row12507614"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6483852"><a name="p6483852"></a><a name="p6483852"></a>If-None-Match</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p55430014"><a name="p55430014"></a><a name="p55430014"></a>Returns the object only if its ETag is different from the one specified by this header, otherwise <strong id="b5663163301213"><a name="b5663163301213"></a><a name="b5663163301213"></a>304 Not Modified</strong> is returned.</p>
<p id="p60646173"><a name="p60646173"></a><a name="p60646173"></a>Type: String</p>
<p id="p8944648"><a name="p8944648"></a><a name="p8944648"></a>Note:</p>
<p id="p13392976"><a name="p13392976"></a><a name="p13392976"></a>An example ETag value is <strong id="b53427925"><a name="b53427925"></a><a name="b53427925"></a>0f64741bf7cb1089e988e4585d0d3434</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p32694658"><a name="p32694658"></a><a name="p32694658"></a>Optional</p>
</td>
</tr>
<tr id="row65701914165449"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p20254821165449"><a name="p20254821165449"></a><a name="p20254821165449"></a>Origin</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p34982523165521"><a name="p34982523165521"></a><a name="p34982523165521"></a>Indicates an origin specified by a pre-request. Generally, it is a domain name.</p>
<p id="p46407251165521"><a name="p46407251165521"></a><a name="p46407251165521"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16331104165449"><a name="p16331104165449"></a><a name="p16331104165449"></a>Optional. If you want to obtain the CORs configuration, this item is mandatory.</p>
</td>
</tr>
<tr id="row506837165454"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p41053798165454"><a name="p41053798165454"></a><a name="p41053798165454"></a>Access-Control-Request-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p21484200165529"><a name="p21484200165529"></a><a name="p21484200165529"></a>Indicates the HTTP headers of a request. The request can use multiple HTTP headers.</p>
<p id="p59140076165529"><a name="p59140076165529"></a><a name="p59140076165529"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p46100226165454"><a name="p46100226165454"></a><a name="p46100226165454"></a>Optional</p>
</td>
</tr>
<tr id="row2545979102559"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p18680844165828"><a name="p18680844165828"></a><a name="p18680844165828"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p36753425165828"><a name="p36753425165828"></a><a name="p36753425165828"></a>Indicates an encryption algorithm. The header is used in SSE-C mode.</p>
<p id="p62345375165828"><a name="p62345375165828"></a><a name="p62345375165828"></a>Type: string</p>
<p id="p24237471165828"><a name="p24237471165828"></a><a name="p24237471165828"></a>Example: x-amz-server-side-encryption-customer-algorithm:AES256</p>
<p id="p16810648165828"><a name="p16810648165828"></a><a name="p16810648165828"></a>Constraints: This header must be used together with <strong id="b17078109165828"><a name="b17078109165828"></a><a name="b17078109165828"></a>x-amz-server-side-encryption-customer-key</strong>&nbsp;and&nbsp;<strong id="b19485253165828"><a name="b19485253165828"></a><a name="b19485253165828"></a>x-amz-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p34801679165828"><a name="p34801679165828"></a><a name="p34801679165828"></a>Optional. This header is mandatory when SSE-C is used.</p>
</td>
</tr>
<tr id="row1200923010266"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p3273673165828"><a name="p3273673165828"></a><a name="p3273673165828"></a>x-amz-server-side-encryption-customer-key</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p63840985165828"><a name="p63840985165828"></a><a name="p63840985165828"></a>Indicates a key used to decrypt objects. The header is used in SSE-C mode.</p>
<p id="p37697959165828"><a name="p37697959165828"></a><a name="p37697959165828"></a>Type: string</p>
<p id="p3737314165828"><a name="p3737314165828"></a><a name="p3737314165828"></a>Example: x-amz-server-side-encryption-customer-key:K7QkYpBkM5+hcs27fsNkUnNVaobncnLht/rCB2o/9Cw=</p>
<p id="p33635827165828"><a name="p33635827165828"></a><a name="p33635827165828"></a>Constraints: This header is a base64-encoded 256-bit or 512-bit key and must be used together with <strong id="b34286987165828"><a name="b34286987165828"></a><a name="b34286987165828"></a>x-amz-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b40147427165828"><a name="b40147427165828"></a><a name="b40147427165828"></a>x-amz-server-side-encryption-customer-key-MD5</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p30716127165828"><a name="p30716127165828"></a><a name="p30716127165828"></a>Optional. This header is mandatory when SSE-C is used.</p>
</td>
</tr>
<tr id="row21277310263"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p44805464165828"><a name="p44805464165828"></a><a name="p44805464165828"></a>x-amz-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5363987165828"><a name="p5363987165828"></a><a name="p5363987165828"></a>Indicates the MD5 value of a key used to encrypt objects. The header is used in SSE-C mode. The MD5 value is used to check whether any error occurs during the transmission of the key.</p>
<p id="p48275888165828"><a name="p48275888165828"></a><a name="p48275888165828"></a>Type: string</p>
<p id="p31829815165828"><a name="p31829815165828"></a><a name="p31829815165828"></a>Example: x-amz-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
<p id="p18032879165828"><a name="p18032879165828"></a><a name="p18032879165828"></a>Constraints: This header is a base64-encoded 128-bit MD5 value and must be used together with <strong id="b28078186165828"><a name="b28078186165828"></a><a name="b28078186165828"></a>x-amz-server-side-encryption-customer-algorithm</strong>&nbsp;and&nbsp;<strong id="b51377090165828"><a name="b51377090165828"></a><a name="b51377090165828"></a>x-amz-server-side-encryption-customer-key</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p794770165828"><a name="p794770165828"></a><a name="p794770165828"></a>Optional. This header is mandatory when SSE-C is used.</p>
</td>
</tr>
<tr id="row76475653817"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p93771257143819"><a name="p93771257143819"></a><a name="p93771257143819"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1377175714384"><a name="p1377175714384"></a><a name="p1377175714384"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p123771157103813"><a name="p123771157103813"></a><a name="p123771157103813"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1937711572389"><a name="p1937711572389"></a><a name="p1937711572389"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

## Request Elements<a name="section58845621"></a>

This request involves no elements.

## Response Syntax<a name="section41115719"></a>

```
HTTP/1.1 status_code 
 Server: bucketname.obs.example.com 
 x-amz-request-id: request id 
 x-amz-id-2: id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: type 
 Date: date 
 Content-Length: length 
 Etag: etag 
 Last-Modified: time 
 <Object Content>
```

## Response Headers<a name="section34497158"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

This response can also include optional headers.  [Table 3](#table29723549)  describes these headers.

**Table  3**  Optional response headers

<a name="table29723549"></a>
<table><thead align="left"><tr id="row58585662"><th class="cellrowborder" valign="top" width="32.74%" id="mcps1.2.3.1.1"><p id="p47818216"><a name="p47818216"></a><a name="p47818216"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="67.25999999999999%" id="mcps1.2.3.1.2"><p id="p48070315"><a name="p48070315"></a><a name="p48070315"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1381422"><td class="cellrowborder" valign="top" width="32.74%" headers="mcps1.2.3.1.1 "><p id="p44786329"><a name="p44786329"></a><a name="p44786329"></a>x-amz-expiration</p>
</td>
<td class="cellrowborder" valign="top" width="67.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p3814037"><a name="p3814037"></a><a name="p3814037"></a>This header is included in the response if the object expiration is configured. This header includes <strong id="b229714281211"><a name="b229714281211"></a><a name="b229714281211"></a>expiry-date</strong> and&nbsp;<strong id="b130195001217"><a name="b130195001217"></a><a name="b130195001217"></a>rule-id</strong> key value pairs to provide object expiration information.</p>
<p id="p28969880"><a name="p28969880"></a><a name="p28969880"></a>Type: String</p>
</td>
</tr>
<tr id="row59402334"><td class="cellrowborder" valign="top" width="32.74%" headers="mcps1.2.3.1.1 "><p id="p46859772"><a name="p46859772"></a><a name="p46859772"></a>x-amz-website-redirect-location</p>
</td>
<td class="cellrowborder" valign="top" width="67.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p37545162"><a name="p37545162"></a><a name="p37545162"></a>When a bucket is configured as a website, you can set this metadata for the object so that the website endpoint will evaluate the request for the object as a 301 redirect to another object in the same bucket or an external URL.</p>
<p id="p2362138"><a name="p2362138"></a><a name="p2362138"></a>Type: String</p>
</td>
</tr>
<tr id="row21259248"><td class="cellrowborder" valign="top" width="32.74%" headers="mcps1.2.3.1.1 "><p id="p44277527"><a name="p44277527"></a><a name="p44277527"></a>x-amz-delete-marker</p>
</td>
<td class="cellrowborder" valign="top" width="67.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p29709926"><a name="p29709926"></a><a name="p29709926"></a>Indicates whether an object is marked as deleted. If an object is not marked as deleted, the header is not returned.</p>
<p id="p66062749"><a name="p66062749"></a><a name="p66062749"></a>Type: Boolean</p>
<p id="p57693830"><a name="p57693830"></a><a name="p57693830"></a>Valid values: true|false</p>
<p id="p49482428"><a name="p49482428"></a><a name="p49482428"></a>Default: false</p>
</td>
</tr>
<tr id="row42688671"><td class="cellrowborder" valign="top" width="32.74%" headers="mcps1.2.3.1.1 "><p id="p35230296"><a name="p35230296"></a><a name="p35230296"></a>x-amz-version-id</p>
</td>
<td class="cellrowborder" valign="top" width="67.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p35081689"><a name="p35081689"></a><a name="p35081689"></a>Indicates the version ID of an object. If an object has no version ID specified, this header is not returned.</p>
<p id="p47299748"><a name="p47299748"></a><a name="p47299748"></a>Valid values: String</p>
<p id="p23044555"><a name="p23044555"></a><a name="p23044555"></a>Default: None</p>
</td>
</tr>
<tr id="row18613230163532"><td class="cellrowborder" valign="top" width="32.74%" headers="mcps1.2.3.1.1 "><p id="p18376122163614"><a name="p18376122163614"></a><a name="p18376122163614"></a>Access-Control-Allow-Origin</p>
</td>
<td class="cellrowborder" valign="top" width="67.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p12070905163614"><a name="p12070905163614"></a><a name="p12070905163614"></a>CORS is configured for buckets. If <strong id="b41529288163614"><a name="b41529288163614"></a><a name="b41529288163614"></a>Origin</strong>&nbsp;in the request meets the CORS configuration requirements,&nbsp;<strong id="b38219273163614"><a name="b38219273163614"></a><a name="b38219273163614"></a>Origin</strong> is included in the response.</p>
<p id="p8429143163614"><a name="p8429143163614"></a><a name="p8429143163614"></a>Type: String</p>
</td>
</tr>
<tr id="row38006271163539"><td class="cellrowborder" valign="top" width="32.74%" headers="mcps1.2.3.1.1 "><p id="p37938875163614"><a name="p37938875163614"></a><a name="p37938875163614"></a>Access-Control-Allow-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="67.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p53149996163614"><a name="p53149996163614"></a><a name="p53149996163614"></a>CORS is configured for buckets. If <strong id="b8587919163614"><a name="b8587919163614"></a><a name="b8587919163614"></a>headers</strong>&nbsp;in the request meet the CORS configuration requirements,&nbsp;<strong id="b10182414163614"><a name="b10182414163614"></a><a name="b10182414163614"></a>headers</strong> are included in the response.</p>
<p id="p24532864163614"><a name="p24532864163614"></a><a name="p24532864163614"></a>Type: String</p>
</td>
</tr>
<tr id="row22290404163545"><td class="cellrowborder" valign="top" width="32.74%" headers="mcps1.2.3.1.1 "><p id="p33500739163614"><a name="p33500739163614"></a><a name="p33500739163614"></a>Access-Control-Max-Age</p>
</td>
<td class="cellrowborder" valign="top" width="67.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p29205351163614"><a name="p29205351163614"></a><a name="p29205351163614"></a>Indicates <strong id="b61521567163614"><a name="b61521567163614"></a><a name="b61521567163614"></a>MaxAgeSeconds</strong> in the CORS configuration of a server when CORS is configured for buckets.</p>
<p id="p16823194163614"><a name="p16823194163614"></a><a name="p16823194163614"></a>Type: Integer</p>
</td>
</tr>
<tr id="row58327138163550"><td class="cellrowborder" valign="top" width="32.74%" headers="mcps1.2.3.1.1 "><p id="p50295874163614"><a name="p50295874163614"></a><a name="p50295874163614"></a>Access-Control-Allow-Methods</p>
</td>
<td class="cellrowborder" valign="top" width="67.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p47433974163614"><a name="p47433974163614"></a><a name="p47433974163614"></a>CORS is configured for buckets. If <strong id="b24252585163614"><a name="b24252585163614"></a><a name="b24252585163614"></a>Access-Control-Request-Method</strong> in the request meets the CORS configuration requirements, methods in the rule are included in the response.</p>
<p id="p16946679163614"><a name="p16946679163614"></a><a name="p16946679163614"></a>Type: String</p>
<p id="p18302383163614"><a name="p18302383163614"></a><a name="p18302383163614"></a>Valid values: <strong id="b30503724163614"><a name="b30503724163614"></a><a name="b30503724163614"></a>GET</strong>,&nbsp;<strong id="b6098061163614"><a name="b6098061163614"></a><a name="b6098061163614"></a>PUT</strong>,&nbsp;<strong id="b54882557163614"><a name="b54882557163614"></a><a name="b54882557163614"></a>HEAD</strong>,&nbsp;<strong id="b24180972163614"><a name="b24180972163614"></a><a name="b24180972163614"></a>POST</strong>, and&nbsp;<strong id="b16302164163614"><a name="b16302164163614"></a><a name="b16302164163614"></a>DELETE</strong></p>
</td>
</tr>
<tr id="row18597873163557"><td class="cellrowborder" valign="top" width="32.74%" headers="mcps1.2.3.1.1 "><p id="p6008652163614"><a name="p6008652163614"></a><a name="p6008652163614"></a>Access-Control-Expose-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="67.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p16938780163614"><a name="p16938780163614"></a><a name="p16938780163614"></a>Indicates <strong id="b1948145618124"><a name="b1948145618124"></a><a name="b1948145618124"></a>ExposeHeader</strong> in the CORS configuration of a server when CORS is configured for buckets.</p>
<p id="p29863949163614"><a name="p29863949163614"></a><a name="p29863949163614"></a>Type: String</p>
</td>
</tr>
<tr id="row32966838102639"><td class="cellrowborder" valign="top" width="32.74%" headers="mcps1.2.3.1.1 "><p id="p24935902165856"><a name="p24935902165856"></a><a name="p24935902165856"></a>x-amz-server-side-encryption</p>
</td>
<td class="cellrowborder" valign="top" width="67.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p6542148165856"><a name="p6542148165856"></a><a name="p6542148165856"></a>This header is included in a response if SSE-KMS is used.</p>
<p id="p58879336165856"><a name="p58879336165856"></a><a name="p58879336165856"></a>Type: string</p>
<p id="p60151979165856"><a name="p60151979165856"></a><a name="p60151979165856"></a>Example: x-amz-server-side-encryption:aws:kms</p>
</td>
</tr>
<tr id="row63160593102649"><td class="cellrowborder" valign="top" width="32.74%" headers="mcps1.2.3.1.1 "><p id="p28704785165856"><a name="p28704785165856"></a><a name="p28704785165856"></a>x-amz-server-side-encryption-aws-kms-key-id</p>
</td>
<td class="cellrowborder" valign="top" width="67.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p43386224165856"><a name="p43386224165856"></a><a name="p43386224165856"></a>Indicates the master key ID. This header is included in a response if SSE-KMS is used.</p>
<p id="p12218175034910"><a name="p12218175034910"></a><a name="p12218175034910"></a>Example: x-amz-server-side-encryption-aws-kms-key-id:arn:aws:kms:sichuan:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0</p>
</td>
</tr>
<tr id="row20211970102653"><td class="cellrowborder" valign="top" width="32.74%" headers="mcps1.2.3.1.1 "><p id="p48325708165856"><a name="p48325708165856"></a><a name="p48325708165856"></a>x-amz-server-side-encryption-customer-algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="67.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p22068248165856"><a name="p22068248165856"></a><a name="p22068248165856"></a>Indicates a decryption algorithm. This header is included in a response if SSE-C is used.</p>
<p id="p64396511165856"><a name="p64396511165856"></a><a name="p64396511165856"></a>Type: string</p>
<p id="p42697689165856"><a name="p42697689165856"></a><a name="p42697689165856"></a>Example: x-amz-server-side-encryption-customer-algorithm:AES256</p>
</td>
</tr>
<tr id="row7749226102645"><td class="cellrowborder" valign="top" width="32.74%" headers="mcps1.2.3.1.1 "><p id="p55211956165856"><a name="p55211956165856"></a><a name="p55211956165856"></a>x-amz-server-side-encryption-customer-key-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="67.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p42983464165856"><a name="p42983464165856"></a><a name="p42983464165856"></a>Indicates the MD5 value of a key used to decrypt objects. This header is included in a response if SSE-C is used.</p>
<p id="p51306856165856"><a name="p51306856165856"></a><a name="p51306856165856"></a>Type: string</p>
<p id="p59108523165856"><a name="p59108523165856"></a><a name="p59108523165856"></a>Example: x-amz-server-side-encryption-customer-key-MD5:4XvB3tbNTN+tIEVa0/fGaQ==</p>
</td>
</tr>
<tr id="row4625798110051"><td class="cellrowborder" valign="top" width="32.74%" headers="mcps1.2.3.1.1 "><p id="p88555201010"><a name="p88555201010"></a><a name="p88555201010"></a>x-amz-storage-class</p>
</td>
<td class="cellrowborder" valign="top" width="67.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p462085421010"><a name="p462085421010"></a><a name="p462085421010"></a>This header is returned when the storage class of an object is not Standard.</p>
<p id="p132236951010"><a name="p132236951010"></a><a name="p132236951010"></a>Type: String</p>
<p id="p519043961010"><a name="p519043961010"></a><a name="p519043961010"></a>Valid values: <strong id="b644863801010"><a name="b644863801010"></a><a name="b644863801010"></a>STANDARD_IA</strong>&nbsp;and&nbsp;<strong id="b435065141010"><a name="b435065141010"></a><a name="b435065141010"></a>GLACIER</strong></p>
</td>
</tr>
<tr id="row66187865174528"><td class="cellrowborder" valign="top" width="32.74%" headers="mcps1.2.3.1.1 "><p id="p20200022174531"><a name="p20200022174531"></a><a name="p20200022174531"></a>x-amz-restore</p>
</td>
<td class="cellrowborder" valign="top" width="67.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p34523931174642"><a name="p34523931174642"></a><a name="p34523931174642"></a>This header is returned when the storage class of an object is OBS Cold and the object has been restored.</p>
<p id="p34829944174712"><a name="p34829944174712"></a><a name="p34829944174712"></a>Example:</p>
<p id="p30536175174721"><a name="p30536175174721"></a><a name="p30536175174721"></a>x-amz-restore:ongoing-request="false", expiry-date="Wed, 07 Nov 2012 00:00:00 GMT"</p>
<a name="ul37302768174938"></a><a name="ul37302768174938"></a><ul id="ul37302768174938"><li><strong id="b2808422520407"><a name="b2808422520407"></a><a name="b2808422520407"></a>ongoing-request="false"</strong>indicates that the object has been restored.</li><li>In <strong id="b6022971520407"><a name="b6022971520407"></a><a name="b6022971520407"></a>expiry-date="Wed, 07 Nov 2012 00:00:00 GMT"</strong>,&nbsp;<strong id="b519652920407"><a name="b519652920407"></a><a name="b519652920407"></a>expiry-date</strong> indicates the expiry date of the restored object.</li></ul>
<p id="p33755437174531"><a name="p33755437174531"></a><a name="p33755437174531"></a>Type: String</p>
</td>
</tr>
</tbody>
</table>

## Response Elements<a name="section42038968"></a>

This response involves no elements.

## Error Responses<a name="section42806400"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request for Not Overriding Response Headers<a name="section19552748"></a>

```
GET /test HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com 
 Accept: */* 
 Date: Sat, 03 Dec 2011 08:28:02 +0000 
 Authorization: AWS BF6C09F302931425E9A7:tQ+A280jUgPCAdSTuUis35T9gWI=
```

## Sample Response for Not Overriding Response Headers<a name="section41757008"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 001B21A61C6C0000013403098535528C 
 x-amz-id-2: MDAxQjIxQTYxQzZDMDAwMDAxMzQwMzA5ODUzNTUyOENBQUFBQUFBQWJiYmJiYmJi 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 ETag: "507e3fff69b69bf57d303e807448560b" 
 Last-Modified: Sat, 03 Dec 2011 08:25:46 GMT 
 Accept-Ranges: bytes 
 Content-Length: 30 
 Content-Type: binary/octet-stream 
 Date: Sat, 03 Dec 2011 08:28:02 GMT 
```

## Sample Request for Overriding Headers<a name="section40268759"></a>

```
GET /test?response-cache-control=No-cache&response-content-disposition=attachment%3B%20filename%3Dtesting.txt&response-content-encoding=x-gzip&response-content-language=mi%2C%20en&response-expires=Thu%2C%2001%20Dec%201994%2016:00:00%20GMT HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com 
 Accept: */* 
 Date: Sat, 03 Dec 2011 08:28:02 +0000 
 Authorization: AWS BF6C09F302931425E9A7: aaStE6nKnw8ihhiIdReoXYlMamW=
```

## Sample Response for Overriding Headers<a name="section26874512"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 001B21A61C6C0000013403098535528C 
 x-amz-id-2: MDAxQjIxQTYxQzZDMDAwMDAxMzQwMzA5ODUzNTUyOENBQUFBQUFBQWJiYmJiYmJi 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 ETag: "507e3fff69b69bf57d303e807448560b" 
 Last-Modified: Sat, 03 Dec 2011 08:25:46 GMT 
 Accept-Ranges: bytes 
 Content-Length: 30 
 Cache-Control: No-cache 
 Content-Language: mi, en 
 Expires: Thu, 01 Dec 1994 16:00:00 GMT 
 Content-Disposition: attachment; filename=testing.txt 
 Content-Encoding: x-gzip 
 Content-Type: binary/octet-stream 
 Date: Sat, 03 Dec 2011 08:28:02 GMT 
```

## Sample Request for Getting an Object with Version ID Specified<a name="section40544022"></a>

```
GET /object?versionId=AAABQ47OMnbc0vycq3gAAAANVURTRkha HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com 
 Accept: */* 
 Date: Tue, 14 Jan 2014 06:11:49 +0000 
 Authorization: AWS C9590CEB8EC051BDEC9D:kpuA5lb+IoEOglV5824R4Yb18RE=
```

## Sample Response for Getting an Object with Version ID Specified<a name="section29351881"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB78000001438F609AD59896 
 x-amz-id-2: nz0bi6ru2wS4OvhkCS1OQ2FwyxjvYwuGv1EI5JVeDpuGwX6weBoX7MRxJwhuXJu9 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Accept-Ranges: bytes 
 ETag: "ba1f2511fc30423bdbb183fe33f3dd0f" 
 Last-Modified: Tue, 14 Jan 2014 03:31:54 GMT 
 Content-Length: 4 
 x-amz-version-id: AAABQ47OMnbc0vycq3gAAAANVURTRkha 
 Content-Type: binary/octet-stream 
 Date: Tue, 14 Jan 2014 06:11:49 GMT 

 [4 bytes of object data]
```

## Sample Request for Getting an Object Whose Latest Version ID Is a Deletion Mark<a name="section62840338"></a>

```
GET /object HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1 
 Host: bucketname.obs.example.com 
 Accept: */* 
 Date: Tue, 14 Jan 2014 06:17:59 +0000 
 Authorization: AWS C9590CEB8EC051BDEC9D:MsZcBz1QOULDOhPP1gx1+4hbh4A=
```

## Sample Response for Getting an Object Whose Latest Version ID Is a Deletion Mark<a name="section28692130"></a>

```
HTTP/1.1 404 Not Found 
 Server: OBS 
 x-amz-request-id: DCD2FC9CAB78000001438F6640529BA9 
 x-amz-id-2: /BdlSJIqa5Gkl3yEoEgmJKUUak0xjtgCTn9LhbsyJwqG5OVqrkfiateRxF8Gg4AU 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml 
 x-amz-version-id: AAABQ49lNT_c0vycq3gAAAAOVURTRkha 
 x-amz-delete-marker: true 
 Date: Tue, 14 Jan 2014 06:17:59 GMT 
 Content-Length: 297

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <Error> 
 <Code>NoSuchKey</Code> 
 <Message>The specified key does not exist.</Message> 
 <RequestId>DCD2FC9CAB78000001438F6640529BA9</RequestId> 
 <HostId>nkbX5Pw7vRd26kP6gRwQQ4AxiN446dN608LMf4/9h/NMdhrWsc17Vnlva6VS23dq</HostId> 
 <Key>object</Key> 
 </Error>
```

## Sample Request for Getting an Object and CORS Configuration when CORS is properly configured<a name="section3311378921371"></a>

```
GET /object HTTP/1.1
User-Agent: curl/7.19.0 (x86_64-suse-linux-gnu) libcurl/7.19.0 OpenSSL/0.9.8{ zlib/1.2.3 libidn/1.10
Host: bucketname.obs.example.com
Accept: */*
Date: Tue, 28 Apr 2015 13:36:06 +0000
Authorization: AWS D13E0C94E722DD69423C:9PzAsaQnzJfMb2pcUNzaYpxgtSE=
Origin:www.example.com
Access-Control-Request-Headers:acc_header_1
```

## Sample Response for Getting an Object and CORS Configuration when CORS is properly configured<a name="section36796706143443"></a>

```
HTTP/1.1 200 OK
x-amz-request-id: 0B2B8A2B224F067CB15E4203ABF583F4
x-amz-id-2: PI5ZL3VEM6LnENYPchIQLKDfMlHanhkCz+CgmqCmyN0AniJZMGKBij9bj7fm4sve
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
Access-Control-Allow-Origin: www.example.com
Access-Control-Allow-Methods: POST,GET,HEAD,PUT
Access-Control-Allow-Headers: acc_header_01
Access-Control-Max-Age: 100
Access-Control-Expose-Headers: exp_header_01
Accept-Ranges: bytes
ETag: "6bcb16084a88ae550811429c0c1e8bc7"
Last-Modified: Tue, 28 Apr 2015 13:38:05 GMT
Content-Length: 264
Content-Type: binary/octet-stream
Date: Tue, 28 Apr 2015 13:38:17 GMTa
```

