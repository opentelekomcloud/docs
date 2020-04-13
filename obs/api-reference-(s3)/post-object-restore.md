# POST Object restore<a name="EN-US_TOPIC_0125560388"></a>

If you want to obtain the content of a Cold object, restore the object first. Then, you can download the object.

## Versioning<a name="section61930124204855"></a>

By default, the object of the latest version is restored. If the object has a delete marker, status code 404 is returned. To restore an object of a specified version, the  **versionId**  parameter can be used to specify the desired version.

## Request Syntax<a name="section16245225204959"></a>

```
POST /ObjectName?restore&versionId=VersionID HTTP/1.1  
User-Agent: agent
Host: bucketname.obs.example.com   
Accept: */*
Date: date   
Authorization: authorization string   
Content-MD5: MD5 

<RestoreRequest>
   <Days>NumberOfDays</Days>
   <GlacierJobParameters>
       <Tier>RetrievalOption</Tier>
   </GlacierJobParameters>
</RestoreRequest>
```

## Request Parameters<a name="section24286729205229"></a>

<a name="table63064893205318"></a>
<table><thead align="left"><tr id="row29419945205318"><th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.1.4.1.1"><p id="p34205369205318"><a name="p34205369205318"></a><a name="p34205369205318"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="62.629999999999995%" id="mcps1.1.4.1.2"><p id="p19171522205318"><a name="p19171522205318"></a><a name="p19171522205318"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="15.15%" id="mcps1.1.4.1.3"><p id="p9389419205318"><a name="p9389419205318"></a><a name="p9389419205318"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row22345436205318"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.1.4.1.1 "><p id="p65149886205318"><a name="p65149886205318"></a><a name="p65149886205318"></a>versionId</p>
</td>
<td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.1.4.1.2 "><p id="p42649400205318"><a name="p42649400205318"></a><a name="p42649400205318"></a>Version ID of the Cold object to be restored.</p>
<p id="p48300286205318"><a name="p48300286205318"></a><a name="p48300286205318"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.4.1.3 "><p id="p20009104205318"><a name="p20009104205318"></a><a name="p20009104205318"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section65131379205237"></a>

This request uses common headers. For details, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section0926151615554"></a>

**Table  1**  Request elements

<a name="table38605968205415"></a>
<table><thead align="left"><tr id="row38119865205415"><th class="cellrowborder" valign="top" width="26.25262526252625%" id="mcps1.2.4.1.1"><p id="p701350205415"><a name="p701350205415"></a><a name="p701350205415"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="49.56495649564957%" id="mcps1.2.4.1.2"><p id="p56809371205415"><a name="p56809371205415"></a><a name="p56809371205415"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="24.18241824182418%" id="mcps1.2.4.1.3"><p id="p38156353205415"><a name="p38156353205415"></a><a name="p38156353205415"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row45698087191234"><td class="cellrowborder" valign="top" width="26.25262526252625%" headers="mcps1.2.4.1.1 "><p id="p8629607191234"><a name="p8629607191234"></a><a name="p8629607191234"></a>RestoreRequest</p>
</td>
<td class="cellrowborder" valign="top" width="49.56495649564957%" headers="mcps1.2.4.1.2 "><p id="p6395843719133"><a name="p6395843719133"></a><a name="p6395843719133"></a>Container for restore information.</p>
<p id="p1325091519133"><a name="p1325091519133"></a><a name="p1325091519133"></a>Type: Container</p>
</td>
<td class="cellrowborder" valign="top" width="24.18241824182418%" headers="mcps1.2.4.1.3 "><p id="p46083083191234"><a name="p46083083191234"></a><a name="p46083083191234"></a>Mandatory</p>
</td>
</tr>
<tr id="row3656895205415"><td class="cellrowborder" valign="top" width="26.25262526252625%" headers="mcps1.2.4.1.1 "><p id="p27773118205415"><a name="p27773118205415"></a><a name="p27773118205415"></a>Days</p>
</td>
<td class="cellrowborder" valign="top" width="49.56495649564957%" headers="mcps1.2.4.1.2 "><p id="p35030118205415"><a name="p35030118205415"></a><a name="p35030118205415"></a>Indicates the retention period of the restored object. The value is an integer ranging from 1 to 30.</p>
<p id="p46835608205415"><a name="p46835608205415"></a><a name="p46835608205415"></a>Type: Positive integer</p>
</td>
<td class="cellrowborder" valign="top" width="24.18241824182418%" headers="mcps1.2.4.1.3 "><p id="p35587919205415"><a name="p35587919205415"></a><a name="p35587919205415"></a>Mandatory</p>
</td>
</tr>
<tr id="row42995031191243"><td class="cellrowborder" valign="top" width="26.25262526252625%" headers="mcps1.2.4.1.1 "><p id="p51410962191243"><a name="p51410962191243"></a><a name="p51410962191243"></a>GlacierJobParameters</p>
</td>
<td class="cellrowborder" valign="top" width="49.56495649564957%" headers="mcps1.2.4.1.2 "><p id="p3538385191243"><a name="p3538385191243"></a><a name="p3538385191243"></a>Container for Glacier job parameters.</p>
<p id="p44331211191345"><a name="p44331211191345"></a><a name="p44331211191345"></a>Type: Container</p>
</td>
<td class="cellrowborder" valign="top" width="24.18241824182418%" headers="mcps1.2.4.1.3 "><p id="p18173793191243"><a name="p18173793191243"></a><a name="p18173793191243"></a>Optional</p>
</td>
</tr>
<tr id="row51855822205415"><td class="cellrowborder" valign="top" width="26.25262526252625%" headers="mcps1.2.4.1.1 "><p id="p39572063205415"><a name="p39572063205415"></a><a name="p39572063205415"></a>Tier</p>
</td>
<td class="cellrowborder" valign="top" width="49.56495649564957%" headers="mcps1.2.4.1.2 "><p id="p51220536205415"><a name="p51220536205415"></a><a name="p51220536205415"></a>Indicates the retrieval option used when restoring a Cold object.</p>
<p id="p58331648205415"><a name="p58331648205415"></a><a name="p58331648205415"></a>Valid Values: <strong id="b55222786205415"><a name="b55222786205415"></a><a name="b55222786205415"></a>Expedited</strong>,&nbsp;<strong id="b27243033205415"><a name="b27243033205415"></a><a name="b27243033205415"></a>Standard</strong>, and&nbsp;<strong id="b43860709205415"><a name="b43860709205415"></a><a name="b43860709205415"></a>Bulk</strong></p>
<a name="ul59202063205415"></a><a name="ul59202063205415"></a><ul id="ul59202063205415"><li><strong id="b30637769205415"><a name="b30637769205415"></a><a name="b30637769205415"></a>Expedited</strong>: indicates that data can be restored within 1 to 5 minutes.</li></ul>
<a name="ul65740207205415"></a><a name="ul65740207205415"></a><ul id="ul65740207205415"><li><strong id="b23356587205415"><a name="b23356587205415"></a><a name="b23356587205415"></a>Standard</strong>: indicates that data can be restored within 3 to 5 hours.</li></ul>
<a name="ul12835362205415"></a><a name="ul12835362205415"></a><ul id="ul12835362205415"><li><strong id="b33031422205415"><a name="b33031422205415"></a><a name="b33031422205415"></a>Bulk</strong>: indicates that data can be restored within 5 to 12 hours.</li></ul>
<p id="p10203123231015"><a name="p10203123231015"></a><a name="p10203123231015"></a>The default value is&nbsp;<strong id="b28847350205415"><a name="b28847350205415"></a><a name="b28847350205415"></a>Standard</strong>.</p>
<p id="p58299559205415"><a name="p58299559205415"></a><a name="p58299559205415"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="24.18241824182418%" headers="mcps1.2.4.1.3 "><p id="p24643844205415"><a name="p24643844205415"></a><a name="p24643844205415"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Response Syntax<a name="section6423315205511"></a>

```
HTTP/1.1 status_code 
Server: server
x-amz-request-id: request id   
x-amz-id-2: id   
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc   
Date: date
```

## Response Headers<a name="section52085441205511"></a>

This response uses common headers. For details, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section53778968205511"></a>

This response involves no elements.

## Error Responses<a name="section63796171205525"></a>

**Table  2**  List of OBS error codes

<a name="table5865346121044"></a>
<table><thead align="left"><tr id="row2030149621044"><th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.1"><p id="p3380844921044"><a name="p3380844921044"></a><a name="p3380844921044"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="53.059999999999995%" id="mcps1.2.4.1.2"><p id="p5412981021044"><a name="p5412981021044"></a><a name="p5412981021044"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.4.1.3"><p id="p2243848421044"><a name="p2243848421044"></a><a name="p2243848421044"></a>HTTP Status Code</p>
</th>
</tr>
</thead>
<tbody><tr id="row543128521044"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p3728094721044"><a name="p3728094721044"></a><a name="p3728094721044"></a>RestoreAlreadyInProgress</p>
</td>
<td class="cellrowborder" valign="top" width="53.059999999999995%" headers="mcps1.2.4.1.2 "><p id="p6696677021044"><a name="p6696677021044"></a><a name="p6696677021044"></a>The object is being restored. The request conflicts with another.</p>
<p id="p6583002621044"><a name="p6583002621044"></a><a name="p6583002621044"></a>ErrorMessage: Object restore is already in progress</p>
</td>
<td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.4.1.3 "><p id="p3063185221044"><a name="p3063185221044"></a><a name="p3063185221044"></a>409 Conflict</p>
</td>
</tr>
<tr id="row725121821044"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p5047776221044"><a name="p5047776221044"></a><a name="p5047776221044"></a>ObjectHasAlreadyRestored</p>
</td>
<td class="cellrowborder" valign="top" width="53.059999999999995%" headers="mcps1.2.4.1.2 "><p id="p6216693121044"><a name="p6216693121044"></a><a name="p6216693121044"></a>The object has been restored and the retention period of the restored object is not allowed to be shortened.</p>
<p id="p2263147121044"><a name="p2263147121044"></a><a name="p2263147121044"></a>ErrorMessage: After restoring a Cold object, you cannot shorten the restoration period of the Cold object</p>
</td>
<td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.4.1.3 "><p id="p2120987621044"><a name="p2120987621044"></a><a name="p2120987621044"></a>409 Conflict</p>
</td>
</tr>
<tr id="row5667115821044"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p2696111321044"><a name="p2696111321044"></a><a name="p2696111321044"></a>MalformedXML</p>
</td>
<td class="cellrowborder" valign="top" width="53.059999999999995%" headers="mcps1.2.4.1.2 "><p id="p3636652421044"><a name="p3636652421044"></a><a name="p3636652421044"></a>Invalid value for the <strong id="b5886326121044"><a name="b5886326121044"></a><a name="b5886326121044"></a>Days</strong> field (not an integer)</p>
<p id="p6000730321044"><a name="p6000730321044"></a><a name="p6000730321044"></a>ErrorMessage: The XML you provided was not well-formed or did not validate against our published schema</p>
</td>
<td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.4.1.3 "><p id="p2875337921044"><a name="p2875337921044"></a><a name="p2875337921044"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row5745382321044"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p2324805421044"><a name="p2324805421044"></a><a name="p2324805421044"></a>InvalidArgument</p>
</td>
<td class="cellrowborder" valign="top" width="53.059999999999995%" headers="mcps1.2.4.1.2 "><p id="p404424221044"><a name="p404424221044"></a><a name="p404424221044"></a>The value of the <strong id="b3639818621044"><a name="b3639818621044"></a><a name="b3639818621044"></a>Days</strong> field is not within the range of 1to 30.</p>
<p id="p5914821921044"><a name="p5914821921044"></a><a name="p5914821921044"></a>ErrorMessage: restoration days should be at least 1 and at most 30</p>
</td>
<td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.4.1.3 "><p id="p2627644021044"><a name="p2627644021044"></a><a name="p2627644021044"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row3516137421044"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p2949904521044"><a name="p2949904521044"></a><a name="p2949904521044"></a>MalformedXML</p>
</td>
<td class="cellrowborder" valign="top" width="53.059999999999995%" headers="mcps1.2.4.1.2 "><p id="p4061243621044"><a name="p4061243621044"></a><a name="p4061243621044"></a>Invalid value for the <strong id="b2996761121044"><a name="b2996761121044"></a><a name="b2996761121044"></a>Tier</strong> field.</p>
<p id="p127304421044"><a name="p127304421044"></a><a name="p127304421044"></a>ErrorMessage: The XML you provided was not well-formed or did not validate against our published schema</p>
</td>
<td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.4.1.3 "><p id="p3600775721044"><a name="p3600775721044"></a><a name="p3600775721044"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row5563435821044"><td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.1 "><p id="p1008911021044"><a name="p1008911021044"></a><a name="p1008911021044"></a>InvalidObjectState</p>
</td>
<td class="cellrowborder" valign="top" width="53.059999999999995%" headers="mcps1.2.4.1.2 "><p id="p1191155421044"><a name="p1191155421044"></a><a name="p1191155421044"></a>The restored object is not a Cold object.</p>
<p id="p4009512921044"><a name="p4009512921044"></a><a name="p4009512921044"></a>ErrorMessage: Restore is not allowed, as object's storage class is not GLACIER</p>
</td>
<td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.4.1.3 "><p id="p2648000321044"><a name="p2648000321044"></a><a name="p2648000321044"></a>403 Forbidden</p>
</td>
</tr>
</tbody>
</table>

## Sample Request<a name="section1893604921116"></a>

```
POST /object?restore HTTP/1.1   
User-Agent: curl/7.19.7 (x86_64-suse-linux-gnu) libcurl/7.19.7 OpenSSL/0.9.8j zlib/1.2.7 libidn/1.10   
Host: bucketname.obs.example.com   
Accept: */*   
Date: Tue, 07 Mar 2017 08:54:09 +0000   
Authorization: AWS UDSIAMSTUBTEST000002:kaEwOixnSVuS6If3Q0Lnd6kxm5A=   
Content-Length: 183   
Expect: 100-continue     
<RestoreRequest xmlns="http://s3.amazonaws.com/doc/2006-3-01">      <Days>3</Days>      
<GlacierJobParameters>         
 <Tier>Expedited</Tier>     
 </GlacierJobParameters>   
</RestoreRequest>
```

## Sample Response<a name="section4706316021116"></a>

```
HTTP/1.1 100 Continue   
HTTP/1.1 202 Accepted  
Server: OBS 
x-amz-request-id: 00013235600000015AA7FE74DCAE68RC   
x-amz-id-2: W5NZYb1KhRt+updrvY4OCgmESg7R1lsdR3CMA450Gq2jtrc07YAThUJmV8mPg9D4   x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc   
Content-Length: 0   
Date: Tue, 07 Mar 2017 08:59:15 GMT
```

