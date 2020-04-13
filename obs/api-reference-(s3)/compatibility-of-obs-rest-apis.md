# Compatibility of OBS REST APIs<a name="EN-US_TOPIC_0125560315"></a>

REST APIs support standard HTTP headers and status codes. In order to enhance security, OBS supports different types of user permission by adding authentication information to headers.

OBS REST APIs comply with REST \(HTTP 1.1\). With REST APIs, you can create, obtain, and delete buckets or objects by sending standard HTTP requests using any tool that supports REST requests.

OBS REST APIs are compatible with most Amazon S3 APIs.  [Table 1](#table6666716114028)  describes the compatibility between OBS REST APIs and Amazon S3 APIs.

**Table  1**  Compatibility between OBS REST APIs and Amazon S3 APIs

<a name="table6666716114028"></a>
<table><thead align="left"><tr id="row9894549"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p63260989"><a name="p63260989"></a><a name="p63260989"></a>S3 Operation</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p23866461"><a name="p23866461"></a><a name="p23866461"></a>Function</p>
</th>
<th class="cellrowborder" valign="top" width="16.73%" id="mcps1.2.5.1.3"><p id="p54135198"><a name="p54135198"></a><a name="p54135198"></a>Supported by OBS</p>
</th>
<th class="cellrowborder" valign="top" width="33.269999999999996%" id="mcps1.2.5.1.4"><p id="p22874919"><a name="p22874919"></a><a name="p22874919"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row40929185"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p26929716"><a name="p26929716"></a><a name="p26929716"></a>Abort Multipart Upload</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p33823367"><a name="p33823367"></a><a name="p33823367"></a>Aborts a multipart upload.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p55338178"><a name="p55338178"></a><a name="p55338178"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p53207438"><a name="p53207438"></a><a name="p53207438"></a>None</p>
</td>
</tr>
<tr id="row9104898"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p66408105"><a name="p66408105"></a><a name="p66408105"></a>Complete Multipart Upload</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p10347445"><a name="p10347445"></a><a name="p10347445"></a>Completes a multipart upload by assembling previously uploaded parts.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p32836750"><a name="p32836750"></a><a name="p32836750"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p42531099"><a name="p42531099"></a><a name="p42531099"></a>None</p>
</td>
</tr>
<tr id="row47235577"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p876528"><a name="p876528"></a><a name="p876528"></a>DELETE Bucket</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p3889935"><a name="p3889935"></a><a name="p3889935"></a>Deletes a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p46649343"><a name="p46649343"></a><a name="p46649343"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p20500456"><a name="p20500456"></a><a name="p20500456"></a>None</p>
</td>
</tr>
<tr id="row50286377"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p46664697"><a name="p46664697"></a><a name="p46664697"></a>DELETE Bucket lifecycle</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p21744085"><a name="p21744085"></a><a name="p21744085"></a>Deletes the lifecycle configuration of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p16440486"><a name="p16440486"></a><a name="p16440486"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p56611028"><a name="p56611028"></a><a name="p56611028"></a>None</p>
</td>
</tr>
<tr id="row39737209"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p64597373"><a name="p64597373"></a><a name="p64597373"></a>DELETE Bucket policy</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p65004688"><a name="p65004688"></a><a name="p65004688"></a>Deletes the policy of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p30888413"><a name="p30888413"></a><a name="p30888413"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p18933514"><a name="p18933514"></a><a name="p18933514"></a>None</p>
</td>
</tr>
<tr id="row36183900"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p45214781"><a name="p45214781"></a><a name="p45214781"></a>DELETE Bucket website</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p38518610"><a name="p38518610"></a><a name="p38518610"></a>Deletes the website configuration of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p32999683"><a name="p32999683"></a><a name="p32999683"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p55728698"><a name="p55728698"></a><a name="p55728698"></a>None</p>
</td>
</tr>
<tr id="row31796234"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p25358146"><a name="p25358146"></a><a name="p25358146"></a>DELETE Multiple Objects</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p40743922"><a name="p40743922"></a><a name="p40743922"></a>Deletes multiple objects from a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p136741026105718"><a name="p136741026105718"></a><a name="p136741026105718"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p36772261571"><a name="p36772261571"></a><a name="p36772261571"></a>None</p>
</td>
</tr>
<tr id="row35111876"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p25489693"><a name="p25489693"></a><a name="p25489693"></a>DELETE Object</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p51399251"><a name="p51399251"></a><a name="p51399251"></a>Deletes an object.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p2589773"><a name="p2589773"></a><a name="p2589773"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p8445043"><a name="p8445043"></a><a name="p8445043"></a>None</p>
</td>
</tr>
<tr id="row8896531"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p49530407"><a name="p49530407"></a><a name="p49530407"></a>GET Bucket acl</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p52540060"><a name="p52540060"></a><a name="p52540060"></a>Obtains the ACL (access control list) of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="ole_link1"><a name="ole_link1"></a><a name="ole_link1"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p44213192"><a name="p44213192"></a><a name="p44213192"></a>None</p>
</td>
</tr>
<tr id="row62374408"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p19162306"><a name="p19162306"></a><a name="p19162306"></a>GET Bucket CORS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p8642944"><a name="p8642944"></a><a name="p8642944"></a>Obtains the CORS configuration of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p28989867"><a name="p28989867"></a><a name="p28989867"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p66477866"><a name="p66477866"></a><a name="p66477866"></a>None</p>
</td>
</tr>
<tr id="row61429885"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p9764758"><a name="p9764758"></a><a name="p9764758"></a>GET Bucket lifecycle</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p52747895"><a name="p52747895"></a><a name="p52747895"></a>Obtains the lifecycle configuration of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p44721097"><a name="p44721097"></a><a name="p44721097"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p65639091"><a name="p65639091"></a><a name="p65639091"></a>None</p>
</td>
</tr>
<tr id="row53880913"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p2277843"><a name="p2277843"></a><a name="p2277843"></a>GET Bucket (List Objects)</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p50287618"><a name="p50287618"></a><a name="p50287618"></a>Lists objects in a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p46765253"><a name="p46765253"></a><a name="p46765253"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="ole_link11"><a name="ole_link11"></a><a name="ole_link11"></a>None</p>
</td>
</tr>
<tr id="row5102633"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p10660122"><a name="p10660122"></a><a name="p10660122"></a>GET Bucket location</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p58163519"><a name="p58163519"></a><a name="p58163519"></a>Obtains the Region (data center) where a bucket is located.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p13624576"><a name="p13624576"></a><a name="p13624576"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p29848903"><a name="p29848903"></a><a name="p29848903"></a>None</p>
</td>
</tr>
<tr id="row204671"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p16578375"><a name="p16578375"></a><a name="p16578375"></a>GET Bucket logging</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p671111"><a name="p671111"></a><a name="p671111"></a>Obtains the logging status of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p54360040"><a name="p54360040"></a><a name="p54360040"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p41087121"><a name="p41087121"></a><a name="p41087121"></a>None</p>
</td>
</tr>
<tr id="row34239777"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p21958538"><a name="p21958538"></a><a name="p21958538"></a>GET Bucket notification</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p33811152"><a name="p33811152"></a><a name="p33811152"></a>Obtains the notification configuration of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p54348762"><a name="p54348762"></a><a name="p54348762"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p40173584"><a name="p40173584"></a><a name="p40173584"></a>None</p>
</td>
</tr>
<tr id="row26017944"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p27078716"><a name="p27078716"></a><a name="p27078716"></a>GET Bucket Object versions</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p45892417"><a name="p45892417"></a><a name="p45892417"></a>Obtains information about all versions of objects in a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p26298319"><a name="p26298319"></a><a name="p26298319"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p49789069"><a name="p49789069"></a><a name="p49789069"></a>None</p>
</td>
</tr>
<tr id="row45448437"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p57444799"><a name="p57444799"></a><a name="p57444799"></a>GET Bucket policy</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p22517133"><a name="p22517133"></a><a name="p22517133"></a>Obtains the policy of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p11948488"><a name="p11948488"></a><a name="p11948488"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p28303447"><a name="p28303447"></a><a name="p28303447"></a>None</p>
</td>
</tr>
<tr id="row53404434"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p30791867"><a name="p30791867"></a><a name="p30791867"></a>GET Bucket requestPayment</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p11113260"><a name="p11113260"></a><a name="p11113260"></a>Obtains the request payment configuration of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p27758862"><a name="p27758862"></a><a name="p27758862"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p33875336"><a name="p33875336"></a><a name="p33875336"></a>None</p>
</td>
</tr>
<tr id="row36442574"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p66167392"><a name="p66167392"></a><a name="p66167392"></a>GET Bucket versioning</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p57958559"><a name="p57958559"></a><a name="p57958559"></a>Obtains the versioning state of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p64131698"><a name="p64131698"></a><a name="p64131698"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p27285058"><a name="p27285058"></a><a name="p27285058"></a>None</p>
</td>
</tr>
<tr id="row44238932"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p26583721"><a name="p26583721"></a><a name="p26583721"></a>GET Bucket website</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p5797807"><a name="p5797807"></a><a name="p5797807"></a>Obtains the website configuration of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p66969229"><a name="p66969229"></a><a name="p66969229"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p55798508"><a name="p55798508"></a><a name="p55798508"></a>None</p>
</td>
</tr>
<tr id="row32424532"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p9141398"><a name="p9141398"></a><a name="p9141398"></a>GET Object</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p2255789"><a name="p2255789"></a><a name="p2255789"></a>Obtains an object.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p48501249"><a name="p48501249"></a><a name="p48501249"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p36287097"><a name="p36287097"></a><a name="p36287097"></a>OBS does not support server-side encryption with S3-managed keys (SSE-S3).</p>
<p id="p18610136143216"><a name="p18610136143216"></a><a name="p18610136143216"></a>If the master key of a KMS-encrypted object is deleted, OBS returns status code <strong id="b6597843194812"><a name="b6597843194812"></a><a name="b6597843194812"></a>400 Bad Request</strong> while downloading the object, not compatible with Amazon (returns&nbsp;<strong id="b5610143643218"><a name="b5610143643218"></a><a name="b5610143643218"></a>500</strong>)<span>.</span></p>
<p id="p1610153610327"><a name="p1610153610327"></a><a name="p1610153610327"></a>OBS does not support object download with the <strong id="b18610536113218"><a name="b18610536113218"></a><a name="b18610536113218"></a>if-range</strong> header.</p>
</td>
</tr>
<tr id="row58148422"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p12401776"><a name="p12401776"></a><a name="p12401776"></a>GET Object acl</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p65019827"><a name="p65019827"></a><a name="p65019827"></a>Obtains the ACL of an object.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p32114614"><a name="p32114614"></a><a name="p32114614"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p51146913"><a name="p51146913"></a><a name="p51146913"></a>None</p>
</td>
</tr>
<tr id="row57669037"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p40680457"><a name="p40680457"></a><a name="p40680457"></a>GET Object torrent</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p6782688"><a name="p6782688"></a><a name="p6782688"></a>Obtains torrent files of an object.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p12526876"><a name="p12526876"></a><a name="p12526876"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p8044069"><a name="p8044069"></a><a name="p8044069"></a>None</p>
</td>
</tr>
<tr id="row5287762"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p25655544"><a name="p25655544"></a><a name="p25655544"></a>GET Service</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p64833183"><a name="p64833183"></a><a name="p64833183"></a>Lists all buckets of a user.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p16996462"><a name="p16996462"></a><a name="p16996462"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p34536206"><a name="p34536206"></a><a name="p34536206"></a>None</p>
</td>
</tr>
<tr id="row42390404"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p11070688"><a name="p11070688"></a><a name="p11070688"></a>HEAD Bucket</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p24310496"><a name="p24310496"></a><a name="p24310496"></a>Retrieves the metadata of a bucket and checks its access permission.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p22993132"><a name="p22993132"></a><a name="p22993132"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p50504429"><a name="p50504429"></a><a name="p50504429"></a>None</p>
</td>
</tr>
<tr id="row51886685"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p42071976"><a name="p42071976"></a><a name="p42071976"></a>HEAD Object</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p52386908"><a name="p52386908"></a><a name="p52386908"></a>Retrieves the metadata of an object.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p15481119"><a name="p15481119"></a><a name="p15481119"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p221517015012"><a name="p221517015012"></a><a name="p221517015012"></a>If the returned user-defined metadata contains non-ASCII or other unprintable characters, the metadata is encoded based on the number of returned ACSII and UTF characters in Amazon S3. However, the metadata is Base64 encoded in the OBS.</p>
<p id="p46011164"><a name="p46011164"></a><a name="p46011164"></a>OBS does not support server-side encryption with S3-managed keys (SSE-S3).</p>
</td>
</tr>
<tr id="row11447295"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p54815683"><a name="p54815683"></a><a name="p54815683"></a>Initiate Multipart Upload</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p10885332"><a name="p10885332"></a><a name="p10885332"></a>Creates a multipart upload.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="ole_link2"><a name="ole_link2"></a><a name="ole_link2"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p14832378"><a name="p14832378"></a><a name="p14832378"></a>OBS does not support server-side encryption with S3-managed keys (SSE-S3).</p>
</td>
</tr>
<tr id="row66382545"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p8277097"><a name="p8277097"></a><a name="p8277097"></a>List Multipart Uploads</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p66465105"><a name="p66465105"></a><a name="p66465105"></a>Lists multipart uploads.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p14964401"><a name="p14964401"></a><a name="p14964401"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p4156978"><a name="p4156978"></a><a name="p4156978"></a>None</p>
</td>
</tr>
<tr id="row37412806"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p10538459"><a name="p10538459"></a><a name="p10538459"></a>List Parts</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p48308836"><a name="p48308836"></a><a name="p48308836"></a>Lists parts.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p20701642"><a name="p20701642"></a><a name="p20701642"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p66220276"><a name="p66220276"></a><a name="p66220276"></a>None</p>
</td>
</tr>
<tr id="row59111574"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p23308194"><a name="p23308194"></a><a name="p23308194"></a>POST Object</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p8915558"><a name="p8915558"></a><a name="p8915558"></a>Uploads an object using HTML forms.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p51071627"><a name="p51071627"></a><a name="p51071627"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p43161145"><a name="p43161145"></a><a name="p43161145"></a>OBS does not support server-side encryption with S3-managed keys (SSE-S3).</p>
</td>
</tr>
<tr id="row52905986"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p57526479"><a name="p57526479"></a><a name="p57526479"></a>PUT Bucket</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p29133241"><a name="p29133241"></a><a name="p29133241"></a>Creates a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p10982311"><a name="p10982311"></a><a name="p10982311"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p17152002"><a name="p17152002"></a><a name="p17152002"></a>In contrast to OBS, Amazon S3 supports more complex bucket names and different bucket naming rules based on regions.</p>
<p id="p20150291"><a name="p20150291"></a><a name="p20150291"></a>Users can create a maximum of 101 (officially 100) buckets in Amazon S3 and a maximum of 100 buckets in OBS.</p>
</td>
</tr>
<tr id="row47134897"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p59830301"><a name="p59830301"></a><a name="p59830301"></a>PUT Bucket acl</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p14416173"><a name="p14416173"></a><a name="p14416173"></a>Sets the ACL of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p26859337"><a name="p26859337"></a><a name="p26859337"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p18631859919"><a name="p18631859919"></a><a name="p18631859919"></a>In OBS, permission cannot be granted to users identified by email address.</p>
<p id="p88631591210"><a name="p88631591210"></a><a name="p88631591210"></a>The <strong id="b1586325913113"><a name="b1586325913113"></a><a name="b1586325913113"></a>x-amz-grant-*</strong>&nbsp;header cannot be used to set ACLs, and the&nbsp;<strong id="b2387165894815"><a name="b2387165894815"></a><a name="b2387165894815"></a>x-amz-acl</strong> header cannot be used to modify existing bucket ACLs.</p>
</td>
</tr>
<tr id="row63347400"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p30865786"><a name="p30865786"></a><a name="p30865786"></a>PUT Bucket CORS</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p17100761"><a name="p17100761"></a><a name="p17100761"></a>Sets the CORS of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p42984396"><a name="p42984396"></a><a name="p42984396"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p59184060"><a name="p59184060"></a><a name="p59184060"></a>None</p>
</td>
</tr>
<tr id="row62894494"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p61289235"><a name="p61289235"></a><a name="p61289235"></a>PUT Bucket lifecycle</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p65481017"><a name="p65481017"></a><a name="p65481017"></a>Sets the lifecycle configuration of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p2362167"><a name="p2362167"></a><a name="p2362167"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p163656553192"><a name="p163656553192"></a><a name="p163656553192"></a>In OBS, expired objects can be deleted or transitioned to another storage class.</p>
</td>
</tr>
<tr id="row44298862"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p31438032"><a name="p31438032"></a><a name="p31438032"></a>PUT Bucket logging</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p63452679"><a name="p63452679"></a><a name="p63452679"></a>Sets the logging state of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p39393403"><a name="p39393403"></a><a name="p39393403"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p36749075"><a name="p36749075"></a><a name="p36749075"></a>None</p>
</td>
</tr>
<tr id="row62306224"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p13639418"><a name="p13639418"></a><a name="p13639418"></a>PUT Bucket notification</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p31051101"><a name="p31051101"></a><a name="p31051101"></a>Sets the notification configuration of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p32111232"><a name="p32111232"></a><a name="p32111232"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p50872971"><a name="p50872971"></a><a name="p50872971"></a>The restrictions are inconsistent with those of AWS. AWS supports up to 100 configuration items. However, OBS supports up to 100 configuration items only when the configuration file is not larger than 100 KB.</p>
</td>
</tr>
<tr id="row55203559"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p42303331"><a name="p42303331"></a><a name="p42303331"></a>PUT Bucket policy</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p4017754"><a name="p4017754"></a><a name="p4017754"></a>Sets the policy of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p57002678"><a name="p57002678"></a><a name="p57002678"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p53814239"><a name="p53814239"></a><a name="p53814239"></a>OBS supports only some conditions. For details, see section <a href="bucket-policy.md">Bucket Policy</a>.</p>
</td>
</tr>
<tr id="row39004066"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p5212777"><a name="p5212777"></a><a name="p5212777"></a>PUT Bucket requestPayment</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p19581784"><a name="p19581784"></a><a name="p19581784"></a>Sets the request payment configuration of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p42620696"><a name="p42620696"></a><a name="p42620696"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p29724369"><a name="p29724369"></a><a name="p29724369"></a>None</p>
</td>
</tr>
<tr id="row66192730"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p60010874"><a name="p60010874"></a><a name="p60010874"></a>PUT Bucket versioning</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p29042598"><a name="p29042598"></a><a name="p29042598"></a>Sets the versioning state of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p3640263"><a name="p3640263"></a><a name="p3640263"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p1899574015214"><a name="p1899574015214"></a><a name="p1899574015214"></a>OBS does not support the MfaDelete function. Using the MfaDelete element in XML will respond <strong id="b2995340724"><a name="b2995340724"></a><a name="b2995340724"></a>200</strong>, but the setting does not take effect.</p>
<p id="p199951403218"><a name="p199951403218"></a><a name="p199951403218"></a>The <strong id="b185814914490"><a name="b185814914490"></a><a name="b185814914490"></a>x-amz-mfa</strong> header is not supported in OBS.</p>
</td>
</tr>
<tr id="row36506738"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p4255814"><a name="p4255814"></a><a name="p4255814"></a>PUT Bucket website</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p9176617"><a name="p9176617"></a><a name="p9176617"></a>Sets the website configuration of a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p5108550"><a name="p5108550"></a><a name="p5108550"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p11139395"><a name="p11139395"></a><a name="p11139395"></a>None</p>
</td>
</tr>
<tr id="row33145693"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p446606"><a name="p446606"></a><a name="p446606"></a>PUT Object</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p36175091"><a name="p36175091"></a><a name="p36175091"></a>Uploads an object to a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p44501236"><a name="p44501236"></a><a name="p44501236"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p22484853164549"><a name="p22484853164549"></a><a name="p22484853164549"></a>OBS does not support server-side encryption with S3-managed keys (SSE-S3) and storage type setting.</p>
<p id="p94002038204910"><a name="p94002038204910"></a><a name="p94002038204910"></a>OBS supports three storage classes for the <strong id="b1721720103516"><a name="b1721720103516"></a><a name="b1721720103516"></a>x-amz-storage-class</strong> header: STANDARD|STANDARD_IA|GLACIER</p>
</td>
</tr>
<tr id="row27820371"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p38857563"><a name="p38857563"></a><a name="p38857563"></a>PUT Object acl</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p60454875"><a name="p60454875"></a><a name="p60454875"></a>Sets the ACL of an object.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p65006716"><a name="p65006716"></a><a name="p65006716"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p31052645"><a name="p31052645"></a><a name="p31052645"></a>In OBS, permission cannot be granted to users identified by email address.</p>
<p id="p46240203211242"><a name="p46240203211242"></a><a name="p46240203211242"></a>The OBS does not support <strong id="b13045125211610"><a name="b13045125211610"></a><a name="b13045125211610"></a>x-amz-grant-*</strong> headers.</p>
</td>
</tr>
<tr id="row32236351"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p61007666"><a name="p61007666"></a><a name="p61007666"></a>PUT Object - Copy</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p42673893"><a name="p42673893"></a><a name="p42673893"></a>Copies an object.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p34033280"><a name="p34033280"></a><a name="p34033280"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="ole_link3"><a name="ole_link3"></a><a name="ole_link3"></a>OBS processes field <strong id="b47090704"><a name="b47090704"></a><a name="b47090704"></a>x-amz-copy-source-if-*</strong>&nbsp;added to request headers but reserves HTTP-defined fields&nbsp;<strong id="b21163152"><a name="b21163152"></a><a name="b21163152"></a>if-unmodified-since</strong>,&nbsp;<strong id="b56250647"><a name="b56250647"></a><a name="b56250647"></a>if-modified-since</strong>,&nbsp;<strong id="b36493781"><a name="b36493781"></a><a name="b36493781"></a>if-match</strong>, and&nbsp;<strong id="b60008579"><a name="b60008579"></a><a name="b60008579"></a>if-none-match</strong>.</p>
<p id="p4263477412174"><a name="p4263477412174"></a><a name="p4263477412174"></a>OBS does not support server-side encryption with S3-managed keys (SSE-S3).</p>
<p id="p7313235508"><a name="p7313235508"></a><a name="p7313235508"></a>If the master key of a KMS-encrypted object is deleted and the object is the source object of a copy operation, status code <strong id="b1872921854913"><a name="b1872921854913"></a><a name="b1872921854913"></a>400 Bad Request</strong> while copying the object, not compatible with Amazon (returns&nbsp;<strong id="b103741049203517"><a name="b103741049203517"></a><a name="b103741049203517"></a>500</strong>)<span>.</span></p>
</td>
</tr>
<tr id="row3206307"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p58384289"><a name="p58384289"></a><a name="p58384289"></a>Upload Part</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p31506935"><a name="p31506935"></a><a name="p31506935"></a>Uploads a part to a multipart upload.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p1924942"><a name="p1924942"></a><a name="p1924942"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p21702605"><a name="p21702605"></a><a name="p21702605"></a>OBS does not support server-side encryption with S3-managed keys (SSE-S3). If the KMS CMK used by Initiate Multipart Upload is deleted, OBS returns status code <strong id="b146666336497"><a name="b146666336497"></a><a name="b146666336497"></a>400 Bad Request</strong> while uploading parts, not compatible with Amazon (returns <strong id="b6344785810298"><a name="b6344785810298"></a><a name="b6344785810298"></a>500</strong>).</p>
</td>
</tr>
<tr id="row61105724"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p50616587"><a name="p50616587"></a><a name="p50616587"></a>Upload Part - Copy</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p6302871"><a name="p6302871"></a><a name="p6302871"></a>Uploads a part by copying data from an existing object as data source.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p40770503"><a name="p40770503"></a><a name="p40770503"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p14076419"><a name="p14076419"></a><a name="p14076419"></a>OBS does not support server-side encryption with S3-managed keys (SSE-S3). If the KMS CMK used by Initiate Multipart Upload is deleted, OBS returns status code <strong id="b1761164364912"><a name="b1761164364912"></a><a name="b1761164364912"></a>400 Bad Request</strong> while copying parts, not compatible with Amazon (returns <strong id="b4481402910293"><a name="b4481402910293"></a><a name="b4481402910293"></a>500</strong>).</p>
</td>
</tr>
<tr id="row59578914"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p61162716"><a name="p61162716"></a><a name="p61162716"></a>OPTIONS Bucket</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p55232983"><a name="p55232983"></a><a name="p55232983"></a>Pre-processes a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p44686651"><a name="p44686651"></a><a name="p44686651"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p62848942"><a name="p62848942"></a><a name="p62848942"></a>Amazon does not support this API.</p>
</td>
</tr>
<tr id="row28769574"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p48634166"><a name="p48634166"></a><a name="p48634166"></a>OPTIONS Object</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p47053354"><a name="p47053354"></a><a name="p47053354"></a>Pre-processes an object.</p>
</td>
<td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.3 "><p id="p53225323"><a name="p53225323"></a><a name="p53225323"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.269999999999996%" headers="mcps1.2.5.1.4 "><p id="p16283872"><a name="p16283872"></a><a name="p16283872"></a>None</p>
</td>
</tr>
</tbody>
</table>

