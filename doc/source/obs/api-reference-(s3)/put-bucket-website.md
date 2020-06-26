# PUT Bucket website<a name="EN-US_TOPIC_0125560321"></a>

You can use this operation to create or update the website configuration of a bucket.

OBS allows you to store static web page resources such as HTML web pages, flash files, video files, and audio files to a bucket. When a client accesses these resources from the website endpoint of the bucket, the browser can directly resolve and present the resources to the client. This operation can be used to:

-   Redirect all requests to a website endpoint.
-   Add routing rules that redirect specific requests.

Only users granted the  **s3:PutBucketWebsite**  permission can set the bucket website configuration. By default, only the bucket owner can set the bucket website configuration. The bucket owner can allow other users to set the bucket website configuration by granting them the permission. After the bucket website configuration is set, it will take effect within two minutes.

>![](/images/icon-note.gif) **NOTE:**   
>Avoid using periods \(.\) in the target bucket name. Otherwise, the client may fail to authenticate the certificate when you use HTTPS for access.  

## Request Syntax<a name="section8461910"></a>

```
 PUT /?website HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com
 Accept: */* 
 Content-Length: length 
 Date: date 
 Authorization: authorization 
 Expect: expect

 <WebsiteConfiguration> 
   <RedirectAllRequestsTo> 
     <HostName>hostName</HostName> 
   </RedirectAllRequestsTo> 
 </WebsiteConfiguration>
```

## Request Parameters<a name="section9048327"></a>

This request involves no parameters.

## Request Headers<a name="section14326087"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section73133455518"></a>

This request contains elements to specify the website configuration in the XML format. The elements differ for situations where users want to redirect all requests to a website endpoint and for when users want to add routing rules that redirect specific requests.

-   To redirect all websites requests sent to the bucket's website endpoint, add the elements as described in  [Table 1](#table5411655).

**Table  1**  Elements for redirecting all website requests

<a name="table5411655"></a>
<table><thead align="left"><tr id="row20599592"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p57954280"><a name="p57954280"></a><a name="p57954280"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p63785121"><a name="p63785121"></a><a name="p63785121"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p66321146"><a name="p66321146"></a><a name="p66321146"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row3303707"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p66273709"><a name="p66273709"></a><a name="p66273709"></a>WebsiteConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p66570199"><a name="p66570199"></a><a name="p66570199"></a>Indicates the root element for the website configuration.</p>
<p id="p62260885"><a name="p62260885"></a><a name="p62260885"></a>Type: Container</p>
<p id="p23477058"><a name="p23477058"></a><a name="p23477058"></a>Ancestor: None</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p22593558"><a name="p22593558"></a><a name="p22593558"></a>Mandatory</p>
</td>
</tr>
<tr id="row2015430"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p29032137"><a name="p29032137"></a><a name="p29032137"></a>RedirectAllRequestsTo</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2792905"><a name="p2792905"></a><a name="p2792905"></a>Describes the redirection behavior for every request to this bucket's website endpoint. If this element is present, no other siblings are allowed.</p>
<p id="p25136147"><a name="p25136147"></a><a name="p25136147"></a>Type: Container</p>
<p id="p24898733"><a name="p24898733"></a><a name="p24898733"></a>Ancestor: WebsiteConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p3531486"><a name="p3531486"></a><a name="p3531486"></a>Mandatory</p>
</td>
</tr>
<tr id="row31783374"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p24316508"><a name="p24316508"></a><a name="p24316508"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p23480171"><a name="p23480171"></a><a name="p23480171"></a>Indicates the name of the host where requests will be redirected.</p>
<p id="p9994955"><a name="p9994955"></a><a name="p9994955"></a>Type: String</p>
<p id="p22845731"><a name="p22845731"></a><a name="p22845731"></a>Ancestor: RedirectAllRequestsTo</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p38564907"><a name="p38564907"></a><a name="p38564907"></a>Mandatory</p>
</td>
</tr>
<tr id="row11539844"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p62312200"><a name="p62312200"></a><a name="p62312200"></a>Protocol</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p14123440"><a name="p14123440"></a><a name="p14123440"></a>Indicates the protocol (HTTP and HTTPS) used in redirecting requests. The default protocol is HTTP.</p>
<p id="p60002101"><a name="p60002101"></a><a name="p60002101"></a>Type: String</p>
<p id="p3148005"><a name="p3148005"></a><a name="p3148005"></a>Ancestor: RedirectAllRequestsTo</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p53661838"><a name="p53661838"></a><a name="p53661838"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

-   To add routing rules that describe conditions for redirecting requests, add the elements as described in  [Table 2](#table48704899).

**Table  2**  Elements for adding rules that redirect requests

<a name="table48704899"></a>
<table><thead align="left"><tr id="row16114131"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p30176268"><a name="p30176268"></a><a name="p30176268"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p28358649"><a name="p28358649"></a><a name="p28358649"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p15349251"><a name="p15349251"></a><a name="p15349251"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row35329809"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43142284"><a name="p43142284"></a><a name="p43142284"></a>WebsiteConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4864091"><a name="p4864091"></a><a name="p4864091"></a>Indicates the root element for the website configuration.</p>
<p id="p43776822"><a name="p43776822"></a><a name="p43776822"></a>Type: Container</p>
<p id="p58447079"><a name="p58447079"></a><a name="p58447079"></a>Ancestor: None</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p36592919"><a name="p36592919"></a><a name="p36592919"></a>Mandatory</p>
</td>
</tr>
<tr id="row60900816"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p34019058"><a name="p34019058"></a><a name="p34019058"></a>IndexDocument</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4080300"><a name="p4080300"></a><a name="p4080300"></a>Indicates the container for the <strong id="b36722706"><a name="b36722706"></a><a name="b36722706"></a>Suffix</strong> element.</p>
<p id="p62068903"><a name="p62068903"></a><a name="p62068903"></a>Type: Container</p>
<p id="p21749220"><a name="p21749220"></a><a name="p21749220"></a>Ancestor: WebsiteConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16856419"><a name="p16856419"></a><a name="p16856419"></a>Mandatory</p>
</td>
</tr>
<tr id="row17490046"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p7407659"><a name="p7407659"></a><a name="p7407659"></a>Suffix</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p63149496"><a name="p63149496"></a><a name="p63149496"></a>Indicates a suffix that is appended to a request initiated for a directory on the website endpoint. For example, if the suffix is <strong id="b71710451350"><a name="b71710451350"></a><a name="b71710451350"></a>index.html</strong>&nbsp;and you request for&nbsp;<strong id="b14835533"><a name="b14835533"></a><a name="b14835533"></a>samplebucket/images/</strong>, the data that is returned will be for the object with the key name&nbsp;<strong id="b66410939"><a name="b66410939"></a><a name="b66410939"></a>images/index.html</strong>&nbsp;in the&nbsp;<strong id="b60827539"><a name="b60827539"></a><a name="b60827539"></a>samplebucket</strong> bucket. The suffix cannot be empty or contain slashes (/).</p>
<p id="p10576944"><a name="p10576944"></a><a name="p10576944"></a>Type: String</p>
<p id="p28083633"><a name="p28083633"></a><a name="p28083633"></a>Ancestor: IndexDocument</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p60181840"><a name="p60181840"></a><a name="p60181840"></a>Mandatory</p>
</td>
</tr>
<tr id="row4765656"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p50473818"><a name="p50473818"></a><a name="p50473818"></a>ErrorDocument</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p61847473"><a name="p61847473"></a><a name="p61847473"></a>Indicates the container for the <strong id="b19756352"><a name="b19756352"></a><a name="b19756352"></a>Key</strong> element.</p>
<p id="p43589445"><a name="p43589445"></a><a name="p43589445"></a>Type: Container</p>
<p id="p56760689"><a name="p56760689"></a><a name="p56760689"></a>Ancestor: WebsiteConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p34213098"><a name="p34213098"></a><a name="p34213098"></a>Optional</p>
</td>
</tr>
<tr id="row39482434"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43960571"><a name="p43960571"></a><a name="p43960571"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4036497"><a name="p4036497"></a><a name="p4036497"></a>Indicates the object key that is used when a 4<em id="i06861825202213"><a name="i06861825202213"></a><a name="i06861825202213"></a>xx</em> error occurs. This element identifies the page that is returned when a 4<em id="i15591522122218"><a name="i15591522122218"></a><a name="i15591522122218"></a>xx</em> error occurs.</p>
<p id="p36328474"><a name="p36328474"></a><a name="p36328474"></a>Type: String</p>
<p id="p58520811"><a name="p58520811"></a><a name="p58520811"></a>Ancestor: ErrorDocument</p>
<p id="p56925253"><a name="p56925253"></a><a name="p56925253"></a>Condition: Required when <strong id="b149203537520"><a name="b149203537520"></a><a name="b149203537520"></a>ErrorDocument</strong> is specified.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p25231885"><a name="p25231885"></a><a name="p25231885"></a>Optional</p>
</td>
</tr>
<tr id="row25760373"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6215498"><a name="p6215498"></a><a name="p6215498"></a>RoutingRules</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p33693352"><a name="p33693352"></a><a name="p33693352"></a>Indicates the container for the <strong id="b34804713"><a name="b34804713"></a><a name="b34804713"></a>RoutingRule</strong> element.</p>
<p id="p44806966"><a name="p44806966"></a><a name="p44806966"></a>Type: Container</p>
<p id="p609510"><a name="p609510"></a><a name="p609510"></a>Ancestor: WebsiteConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p49370368"><a name="p49370368"></a><a name="p49370368"></a>Optional</p>
</td>
</tr>
<tr id="row41680131"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p20647442"><a name="p20647442"></a><a name="p20647442"></a>RoutingRule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p61830130"><a name="p61830130"></a><a name="p61830130"></a>Indicates the container for a routing rule that identifies a condition and a redirect applicable when the condition is met.</p>
<p id="p19600264"><a name="p19600264"></a><a name="p19600264"></a>Type: Container</p>
<p id="p42184651"><a name="p42184651"></a><a name="p42184651"></a>Ancestor: RoutingRules</p>
<p id="p44117540"><a name="p44117540"></a><a name="p44117540"></a>Condition: In a <strong id="b61513540"><a name="b61513540"></a><a name="b61513540"></a>RoutingRules</strong>&nbsp;container, there must be at least one&nbsp;<strong id="b16750948"><a name="b16750948"></a><a name="b16750948"></a>RoutingRule</strong> element.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14649520"><a name="p14649520"></a><a name="p14649520"></a>Mandatory</p>
</td>
</tr>
<tr id="row64736823"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p9191297"><a name="p9191297"></a><a name="p9191297"></a>Condition</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6297612"><a name="p6297612"></a><a name="p6297612"></a>Indicates the container for describing a condition that must be met for the specified redirect to apply.</p>
<p id="p56678513"><a name="p56678513"></a><a name="p56678513"></a>Type: Container</p>
<p id="p40344576"><a name="p40344576"></a><a name="p40344576"></a>Ancestor: RoutingRule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p46685187"><a name="p46685187"></a><a name="p46685187"></a>Optional</p>
</td>
</tr>
<tr id="row17513507"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p9307971"><a name="p9307971"></a><a name="p9307971"></a>KeyPrefixEquals</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15748167"><a name="p15748167"></a><a name="p15748167"></a>Indicates the object key name prefix when the redirection is applied.</p>
<p id="p7515778"><a name="p7515778"></a><a name="p7515778"></a>For example:</p>
<a name="ul533144"></a><a name="ul533144"></a><ul id="ul533144"><li>To redirect the request for object <strong id="b43184669"><a name="b43184669"></a><a name="b43184669"></a>ExamplePage.html</strong>, the key prefix is set to&nbsp;<strong id="b53117702"><a name="b53117702"></a><a name="b53117702"></a>ExamplePage.html</strong>.</li></ul>
<p id="p8297278"><a name="p8297278"></a><a name="p8297278"></a>Type: String</p>
<p id="p7566645"><a name="p7566645"></a><a name="p7566645"></a>Ancestor: Condition</p>
<p id="p990949"><a name="p990949"></a><a name="p990949"></a>Condition: Required when the parent element <strong id="b8918541"><a name="b8918541"></a><a name="b8918541"></a>HttpErrorCodeReturnedEquals</strong> is not specified. If two conditions are specified, both conditions must be true for the redirection to be applied.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p51313205"><a name="p51313205"></a><a name="p51313205"></a>Optional</p>
</td>
</tr>
<tr id="row59165662"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p27689346"><a name="p27689346"></a><a name="p27689346"></a>HttpErrorCodeReturnedEquals</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p28244554"><a name="p28244554"></a><a name="p28244554"></a>Indicates the HTTP error code returned when the redirection is applied. The specified redirect is applied only when the error code returned equals to this value.</p>
<p id="p52874399"><a name="p52874399"></a><a name="p52874399"></a>For example:</p>
<a name="ul6107551"></a><a name="ul6107551"></a><ul id="ul6107551"><li>If you want to redirect to <strong id="b24949608"><a name="b24949608"></a><a name="b24949608"></a>NotFound.html</strong>&nbsp;when HTTP error code&nbsp;<strong id="b23219884"><a name="b23219884"></a><a name="b23219884"></a>404</strong>&nbsp;is returned, set&nbsp;<strong id="b7652366"><a name="b7652366"></a><a name="b7652366"></a>HttpErrorCodeReturnedEquals</strong>&nbsp;to&nbsp;<strong id="b1762431"><a name="b1762431"></a><a name="b1762431"></a>404</strong>&nbsp;in&nbsp;<strong id="b15861880"><a name="b15861880"></a><a name="b15861880"></a>Condition</strong>&nbsp;and&nbsp;<strong id="b8539194"><a name="b8539194"></a><a name="b8539194"></a>ReplaceKeyWith</strong>&nbsp;to&nbsp;<strong id="b9743886"><a name="b9743886"></a><a name="b9743886"></a>NotFound.html</strong>&nbsp;in&nbsp;<strong id="b20586118"><a name="b20586118"></a><a name="b20586118"></a>Redirect</strong>.</li></ul>
<p id="p51057338"><a name="p51057338"></a><a name="p51057338"></a>Type: String</p>
<p id="p56862858"><a name="p56862858"></a><a name="p56862858"></a>Ancestor: Condition</p>
<p id="p42003681"><a name="p42003681"></a><a name="p42003681"></a>Condition: Required when parent element <strong id="b415387368"><a name="b415387368"></a><a name="b415387368"></a>Condition</strong> is specified and sibling&nbsp;<strong id="b46855021"><a name="b46855021"></a><a name="b46855021"></a>KeyPrefixEquals</strong> is not specified. If multiple conditions are specified, the redirection takes effect only after all conditions are met.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p37160390"><a name="p37160390"></a><a name="p37160390"></a>Optional</p>
</td>
</tr>
<tr id="row66008059"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p45052529"><a name="p45052529"></a><a name="p45052529"></a>Redirect</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p25376232"><a name="p25376232"></a><a name="p25376232"></a>Indicates the container for redirect information. You can redirect requests to another host, to another web page, or with another protocol. You can specify an error code to be returned after an error.</p>
<p id="p27059499"><a name="p27059499"></a><a name="p27059499"></a>Type: Container</p>
<p id="p42208903"><a name="p42208903"></a><a name="p42208903"></a>Ancestor: RoutingRule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p63478007"><a name="p63478007"></a><a name="p63478007"></a>Mandatory</p>
</td>
</tr>
<tr id="row34431157"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p37460321"><a name="p37460321"></a><a name="p37460321"></a>Protocol</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p14387121"><a name="p14387121"></a><a name="p14387121"></a>Indicates the protocol used in the redirection request.</p>
<p id="p62375226"><a name="p62375226"></a><a name="p62375226"></a>Type: String</p>
<p id="p24506125"><a name="p24506125"></a><a name="p24506125"></a>Ancestor: Redirect</p>
<p id="p19228540"><a name="p19228540"></a><a name="p19228540"></a>Valid Values: http, https</p>
<p id="p38839134"><a name="p38839134"></a><a name="p38839134"></a>Condition: Not required if one of the siblings is present.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p58962188"><a name="p58962188"></a><a name="p58962188"></a>Optional</p>
</td>
</tr>
<tr id="row60897649"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p33762549"><a name="p33762549"></a><a name="p33762549"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p50411912"><a name="p50411912"></a><a name="p50411912"></a>Indicates the host name used in the redirection request.</p>
<p id="p51054032"><a name="p51054032"></a><a name="p51054032"></a>Type: String</p>
<p id="p56833109"><a name="p56833109"></a><a name="p56833109"></a>Ancestor: Redirect</p>
<p id="p41735936"><a name="p41735936"></a><a name="p41735936"></a>Condition: Not required if one of the siblings is present.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p25167636"><a name="p25167636"></a><a name="p25167636"></a>Optional</p>
</td>
</tr>
<tr id="row25182135"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p26487069"><a name="p26487069"></a><a name="p26487069"></a>ReplaceKeyPrefixWith</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p65077851"><a name="p65077851"></a><a name="p65077851"></a>Indicates the object key prefix used in the redirection request.</p>
<p id="p48829755"><a name="p48829755"></a><a name="p48829755"></a>For example:</p>
<a name="ul36814618"></a><a name="ul36814618"></a><ul id="ul36814618"><li>To redirect all requests for (objects under) <strong id="b29194114"><a name="b29194114"></a><a name="b29194114"></a>docs</strong>&nbsp;to (objects under)&nbsp;<strong id="b61420436"><a name="b61420436"></a><a name="b61420436"></a>documents</strong>, set&nbsp;<strong id="b15913018"><a name="b15913018"></a><a name="b15913018"></a>KeyPrefixEquals</strong>&nbsp;to&nbsp;<strong id="b8999435"><a name="b8999435"></a><a name="b8999435"></a>docs</strong>&nbsp;in&nbsp;<strong id="b13886058"><a name="b13886058"></a><a name="b13886058"></a>Condition</strong>&nbsp;and&nbsp;<strong id="b57865663"><a name="b57865663"></a><a name="b57865663"></a>ReplaceKeyPrefixWith</strong>&nbsp;to&nbsp;<strong id="b51028923"><a name="b51028923"></a><a name="b51028923"></a>documents</strong>&nbsp;in&nbsp;<strong id="b56607127"><a name="b56607127"></a><a name="b56607127"></a>Redirect</strong>.</li></ul>
<p id="p39702100"><a name="p39702100"></a><a name="p39702100"></a>Type: String</p>
<p id="p21774588"><a name="p21774588"></a><a name="p21774588"></a>Ancestor: Redirect</p>
<p id="p61753566"><a name="p61753566"></a><a name="p61753566"></a>Condition: Not required if one of the siblings is present. Can be present only if <strong id="b18911189"><a name="b18911189"></a><a name="b18911189"></a>ReplaceKeyWith</strong> is not provided.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p28940004"><a name="p28940004"></a><a name="p28940004"></a>Optional</p>
</td>
</tr>
<tr id="row59133445"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p25079723"><a name="p25079723"></a><a name="p25079723"></a>ReplaceKeyWith</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p18191719"><a name="p18191719"></a><a name="p18191719"></a>Indicates the object key used in the redirection request. For example, redirect requests to <strong id="b29507743"><a name="b29507743"></a><a name="b29507743"></a>error.html</strong>.</p>
<p id="p64243102"><a name="p64243102"></a><a name="p64243102"></a>Type: String</p>
<p id="p41317012"><a name="p41317012"></a><a name="p41317012"></a>Ancestor: Redirect</p>
<p id="p36308794"><a name="p36308794"></a><a name="p36308794"></a>Condition: Not required if one of the siblings is present. Can be present only if <strong id="b58343698"><a name="b58343698"></a><a name="b58343698"></a>ReplaceKeyPrefixWith</strong>is not provided.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p52645056"><a name="p52645056"></a><a name="p52645056"></a>Optional</p>
</td>
</tr>
<tr id="row4043462"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p59085005"><a name="p59085005"></a><a name="p59085005"></a>HttpRedirectCode</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p21156092"><a name="p21156092"></a><a name="p21156092"></a>Indicates the HTTP status code returned after the redirection request.</p>
<p id="p56187107"><a name="p56187107"></a><a name="p56187107"></a>Type: String</p>
<p id="p35921916"><a name="p35921916"></a><a name="p35921916"></a>Ancestor: Redirect</p>
<p id="p54861794"><a name="p54861794"></a><a name="p54861794"></a>Condition: Not required if one of the siblings is present.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14620318"><a name="p14620318"></a><a name="p14620318"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Response Syntax<a name="section45559064"></a>

```
HTTP/1.1 status_code 
 Server: Server Name 
 x-amz-request-id: request id 
 x-amz-id-2: id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: date 
 Content-Length: length 
```

## Response Headers<a name="section7378398"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section66405588"></a>

This response involves no elements.

## Error Responses<a name="section60779388"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Example 1: Setting Website to Redirect All Requests<a name="section25151514"></a>

```
PUT /?website HTTP/1.1 
 User-Agent: curl/7.29.0
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Sat, 04 Jan 2014 06:22:20 +0000 
 Authorization: AWS C6630CD15B645CB8A3BA:NiQpK7VHqCx93B8k14LJMSZy8ng=
 Content-Length: 198 
 Expect: 100-continue

<WebsiteConfiguration> 
   <RedirectAllRequestsTo> 
     <HostName>www.example.com</HostName>
   </RedirectAllRequestsTo> 
 </WebsiteConfiguration>
```

## Example 2: Setting Website to Add Routing Rules that Redirect Requests<a name="section25037038"></a>

```
PUT /?website HTTP/1.1 
 User-Agent: curl/7.29.0
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Sat, 04 Jan 2014 06:22:20 +0000 
 Authorization: AWS C6630CD15B645CB8A3BA:NiQpK7VHqCx93B8k14LJMSZy8ng=
 Content-Length: 490 
 Expect: 100-continue

<WebsiteConfiguration> 
   <IndexDocument> 
     <Suffix>index.html</Suffix> 
   </IndexDocument> 
   <ErrorDocument> 
     <Key>Error.html</Key> 
   </ErrorDocument> 
   <RoutingRules> 
     <RoutingRule> 
       <Condition> 
         <KeyPrefixEquals>docs/</KeyPrefixEquals> 
       </Condition> 
       <Redirect> 
         <ReplaceKeyPrefixWith>documents/</ReplaceKeyPrefixWith> 
       </Redirect> 
     </RoutingRule> 
   </RoutingRules> 
 </WebsiteConfiguration>
```

## Sample Response<a name="section24006753"></a>

```
HTTP/1.1 200 OK 
 Date: Sat, 04 Jan 2014 06:24:31 GMT 
 Server: OBS 
 x-amz-request-id: 90E2BA0A420C00000140ED7A369007A2 
 x-amz-id-2: t35S98JCFKUMswCPZCk+UTi/VOoiSenzi5J6wnoKCIMfXUsKYGgU5+daiWAYiY/8 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: text/xml 
 Content-Length: 0
```

