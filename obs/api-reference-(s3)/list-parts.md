# List Parts<a name="EN-US_TOPIC_0125560266"></a>

You can use this operation to query all parts associated to a multipart upload.

## Request Syntax<a name="section54014227"></a>

```
GET /ObjectName?uploadId=uploadid&max-parts=max&part-number-marker=marker HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com 
 Accept: */*
 Date: date 
 Authorization: auth
```

## Request Parameters<a name="section16365997"></a>

This request uses parameters to specify associated parts to be listed.  [Table 1](#table43496416)  describes the parameters.

**Table  1**  Request parameters

<a name="table43496416"></a>
<table><thead align="left"><tr id="row12855810"><th class="cellrowborder" valign="top" width="23.99239923992399%" id="mcps1.2.4.1.1"><p id="p34687669"><a name="p34687669"></a><a name="p34687669"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50.645064506450645%" id="mcps1.2.4.1.2"><p id="p58237776"><a name="p58237776"></a><a name="p58237776"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="25.36253625362536%" id="mcps1.2.4.1.3"><p id="p19639420"><a name="p19639420"></a><a name="p19639420"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row42537056"><td class="cellrowborder" valign="top" width="23.99239923992399%" headers="mcps1.2.4.1.1 "><p id="p22949479"><a name="p22949479"></a><a name="p22949479"></a>uploadId</p>
</td>
<td class="cellrowborder" valign="top" width="50.645064506450645%" headers="mcps1.2.4.1.2 "><p id="p46968531"><a name="p46968531"></a><a name="p46968531"></a>Indicates the ID of the multipart upload whose parts are to be listed.</p>
<p id="p20063603"><a name="p20063603"></a><a name="p20063603"></a>Type: String</p>
<p id="p46354700"><a name="p46354700"></a><a name="p46354700"></a>Default value: None</p>
</td>
<td class="cellrowborder" valign="top" width="25.36253625362536%" headers="mcps1.2.4.1.3 "><p id="p63743225"><a name="p63743225"></a><a name="p63743225"></a>Mandatory</p>
</td>
</tr>
<tr id="row36818119"><td class="cellrowborder" valign="top" width="23.99239923992399%" headers="mcps1.2.4.1.1 "><p id="p29477662"><a name="p29477662"></a><a name="p29477662"></a>max-parts</p>
</td>
<td class="cellrowborder" valign="top" width="50.645064506450645%" headers="mcps1.2.4.1.2 "><p id="p38880413"><a name="p38880413"></a><a name="p38880413"></a>Sets the maximum number of parts to be listed.</p>
<p id="p14379404"><a name="p14379404"></a><a name="p14379404"></a>Type: String</p>
<p id="p62305773"><a name="p62305773"></a><a name="p62305773"></a>Default: 1000</p>
</td>
<td class="cellrowborder" valign="top" width="25.36253625362536%" headers="mcps1.2.4.1.3 "><p id="p13602870"><a name="p13602870"></a><a name="p13602870"></a>Optional</p>
</td>
</tr>
<tr id="row55316967"><td class="cellrowborder" valign="top" width="23.99239923992399%" headers="mcps1.2.4.1.1 "><p id="p51489303"><a name="p51489303"></a><a name="p51489303"></a>part-number</p>
<p id="p60750544"><a name="p60750544"></a><a name="p60750544"></a>-marker</p>
</td>
<td class="cellrowborder" valign="top" width="50.645064506450645%" headers="mcps1.2.4.1.2 "><p id="p21847026"><a name="p21847026"></a><a name="p21847026"></a>Specifies the part after which the part listing begins. The OBS lists only parts with greater numbers than that specified by this parameter.</p>
<p id="p62405508"><a name="p62405508"></a><a name="p62405508"></a>Type: String</p>
<p id="p24778668"><a name="p24778668"></a><a name="p24778668"></a>Default: None</p>
</td>
<td class="cellrowborder" valign="top" width="25.36253625362536%" headers="mcps1.2.4.1.3 "><p id="p60915111"><a name="p60915111"></a><a name="p60915111"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section13076248"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section50577374"></a>

This request involves no elements.

## Response Syntax<a name="section45087584"></a>

```
HTTP/1.1 status_code 
 x-amz-id-2: id 
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Date: date 
 Content-Type: type
 Content-Length: length 
 Connection: state 
 Server: server 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <ListPartsResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Bucket>BucketName</Bucket> 
 <Key>ObjectName </Key> 
 <UploadId>uploadid</UploadId> 
 <Initiator> 
 <ID>initiatorid</ID>  
 <DisplayName>displayname</DisplayName> 
 </Initiator> 
 <Owner> 
 <ID>ownerid</ID> 
 <DisplayName>ownername</DisplayName> 
 </Owner> 
 <StorageClass>STANDARD</StorageClass> 
 <PartNumberMarker>partNmebermarker</PartNumberMarker> 
 <NextPartNumberMarker>nextpartnumbermarker</NextPartNumberMarker> 
 <MaxParts>2</MaxParts> 
 <IsTruncated>true</IsTruncated> 
 <Part> 
 <PartNumber>partnumber</PartNumber> 
 <LastModified>modifieddate</LastModified> 
 <ETag>etag</ETag> 
 <Size>etag</Size> 
 </Part> 
 ..  
 </ListPartsResult>
```

## Response Headers<a name="section3135073"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section28215657"></a>

This response uses elements to provide details about the listed parts.  [Table 2](#table33229135)  describes the elements.

**Table  2**  Response elements

<a name="table33229135"></a>
<table><thead align="left"><tr id="row12519366"><th class="cellrowborder" valign="top" width="26.55%" id="mcps1.2.3.1.1"><p id="p7435725"><a name="p7435725"></a><a name="p7435725"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="73.45%" id="mcps1.2.3.1.2"><p id="p65422844"><a name="p65422844"></a><a name="p65422844"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row51934691"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p45960418"><a name="p45960418"></a><a name="p45960418"></a>ListPartsResult</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p31806366"><a name="p31806366"></a><a name="p31806366"></a>Container for the response</p>
<p id="p17821838"><a name="p17821838"></a><a name="p17821838"></a>Type: Container</p>
<p id="p26178814"><a name="p26178814"></a><a name="p26178814"></a>Children: <strong id="b34282735"><a name="b34282735"></a><a name="b34282735"></a>Bucket</strong>,&nbsp;<strong id="b40109162"><a name="b40109162"></a><a name="b40109162"></a>Key</strong>,&nbsp;<strong id="b25438145"><a name="b25438145"></a><a name="b25438145"></a>UploadId</strong>,&nbsp;<strong id="b27616715"><a name="b27616715"></a><a name="b27616715"></a>PartNumberMarker</strong>,&nbsp;<strong id="b47223851"><a name="b47223851"></a><a name="b47223851"></a><em id="i22361481"><a name="i22361481"></a><a name="i22361481"></a>NextPartNumberMarker</em></strong>,&nbsp;<strong id="b67035606"><a name="b67035606"></a><a name="b67035606"></a>MaxParts</strong>,&nbsp;<strong id="b66449547"><a name="b66449547"></a><a name="b66449547"></a>IsTruncated</strong>,&nbsp;<strong id="b61175018"><a name="b61175018"></a><a name="b61175018"></a>Part</strong></p>
<p id="p13704250"><a name="p13704250"></a><a name="p13704250"></a>Ancestor: None</p>
</td>
</tr>
<tr id="row56229389"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p58286698"><a name="p58286698"></a><a name="p58286698"></a>Bucket</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p23602087"><a name="p23602087"></a><a name="p23602087"></a>Name of the bucket to which the multipart upload was initiated</p>
<p id="p11092193"><a name="p11092193"></a><a name="p11092193"></a>Type: String</p>
<p id="p32720876"><a name="p32720876"></a><a name="p32720876"></a>Ancestor: <strong id="b26052434"><a name="b26052434"></a><a name="b26052434"></a>ListPartsResult</strong></p>
</td>
</tr>
<tr id="row33145314"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p415920"><a name="p415920"></a><a name="p415920"></a>Key</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p33689599"><a name="p33689599"></a><a name="p33689599"></a>Key of the object for which the multipart upload was initiated</p>
<p id="p34770943"><a name="p34770943"></a><a name="p34770943"></a>Type: String</p>
<p id="p44503031"><a name="p44503031"></a><a name="p44503031"></a>Ancestor: <strong id="b64982961"><a name="b64982961"></a><a name="b64982961"></a>ListPartsResult</strong></p>
</td>
</tr>
<tr id="row47975743"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p60829951"><a name="p60829951"></a><a name="p60829951"></a>UploadId</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p28279008"><a name="p28279008"></a><a name="p28279008"></a>ID that identifies the multipart upload whose parts are listed</p>
<p id="p53184484"><a name="p53184484"></a><a name="p53184484"></a>Type: String</p>
<p id="p8898313"><a name="p8898313"></a><a name="p8898313"></a>Ancestor: <strong id="b12975961"><a name="b12975961"></a><a name="b12975961"></a>ListPartsResult</strong></p>
</td>
</tr>
<tr id="row49674787"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p64234838"><a name="p64234838"></a><a name="p64234838"></a>Initiator</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p35639369"><a name="p35639369"></a><a name="p35639369"></a>Container element that identifies who initiated the multipart upload</p>
<p id="p52318866"><a name="p52318866"></a><a name="p52318866"></a>Type: Container</p>
<p id="p1107748"><a name="p1107748"></a><a name="p1107748"></a>Children: <strong id="b9969736"><a name="b9969736"></a><a name="b9969736"></a>ID</strong>,&nbsp;<strong id="b22618768"><a name="b22618768"></a><a name="b22618768"></a>DisplayName</strong></p>
<p id="p2242324"><a name="p2242324"></a><a name="p2242324"></a>Ancestor: <strong id="b20180916"><a name="b20180916"></a><a name="b20180916"></a>ListPartsResult</strong></p>
</td>
</tr>
<tr id="row47410523"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p15047175"><a name="p15047175"></a><a name="p15047175"></a>Owner</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p10861696"><a name="p10861696"></a><a name="p10861696"></a>Container element that identifies the object owner. This element is the same as <strong id="b30646405"><a name="b30646405"></a><a name="b30646405"></a>Initiator</strong>&nbsp;and compatible with Amazon S3. In S3, if a multipart upload is initiated by an IAM user,&nbsp;<strong id="b7382189"><a name="b7382189"></a><a name="b7382189"></a>Initiator</strong>&nbsp;may differ from&nbsp;<strong id="b66439707"><a name="b66439707"></a><a name="b66439707"></a>Owner</strong>.</p>
<p id="p61086455"><a name="p61086455"></a><a name="p61086455"></a>Children: <strong id="b12907186"><a name="b12907186"></a><a name="b12907186"></a>ID</strong>,&nbsp;<strong id="b49055813"><a name="b49055813"></a><a name="b49055813"></a>DisplayName</strong></p>
<p id="p38849137"><a name="p38849137"></a><a name="p38849137"></a>Ancestor: <strong id="b14097920"><a name="b14097920"></a><a name="b14097920"></a>ListPartsResult</strong></p>
</td>
</tr>
<tr id="row59772417"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p9727626"><a name="p9727626"></a><a name="p9727626"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p49740211"><a name="p49740211"></a><a name="p49740211"></a>DomainId of initiator or owner.</p>
<p id="p45008715"><a name="p45008715"></a><a name="p45008715"></a>Type: String</p>
<p id="p2425252"><a name="p2425252"></a><a name="p2425252"></a>Ancestor: <strong id="b21827271"><a name="b21827271"></a><a name="b21827271"></a>Initiator</strong>&nbsp;or&nbsp;<strong id="b62227718"><a name="b62227718"></a><a name="b62227718"></a>Owner</strong></p>
</td>
</tr>
<tr id="row23178552"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p65523462"><a name="p65523462"></a><a name="p65523462"></a>DisplayName</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p5800216"><a name="p5800216"></a><a name="p5800216"></a>Initiator name</p>
<p id="p52201951"><a name="p52201951"></a><a name="p52201951"></a>Type: String</p>
<p id="p55511"><a name="p55511"></a><a name="p55511"></a>Ancestor: <strong id="b499602"><a name="b499602"></a><a name="b499602"></a>Initiator</strong>&nbsp;or&nbsp;<strong id="b4496426"><a name="b4496426"></a><a name="b4496426"></a>Owner</strong></p>
</td>
</tr>
<tr id="row57246233154424"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p196162555511"><a name="p196162555511"></a><a name="p196162555511"></a>StorageClass</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p92561642384"><a name="p92561642384"></a><a name="p92561642384"></a>Storage class.</p>
<p id="p10256842388"><a name="p10256842388"></a><a name="p10256842388"></a>Type: Enumeration</p>
<p id="p42561042688"><a name="p42561042688"></a><a name="p42561042688"></a>Valid values: STANDARD | STANDARD_IA |GLACIER</p>
<p id="p1925618421087"><a name="p1925618421087"></a><a name="p1925618421087"></a>Ancestor: ListPartsResult</p>
</td>
</tr>
<tr id="row40467839"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p56669516"><a name="p56669516"></a><a name="p56669516"></a>PartNumberMarker</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p26828065"><a name="p26828065"></a><a name="p26828065"></a>Part number after which the part listing begins</p>
<p id="p40125999"><a name="p40125999"></a><a name="p40125999"></a>Type: Integer</p>
<p id="p25589671"><a name="p25589671"></a><a name="p25589671"></a>Ancestor: <strong id="b28980452"><a name="b28980452"></a><a name="b28980452"></a>ListPartsResult</strong></p>
</td>
</tr>
<tr id="row59497477"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p54566372"><a name="p54566372"></a><a name="p54566372"></a>NextPartNumber Marker</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p57800044"><a name="p57800044"></a><a name="p57800044"></a>Value of <strong id="b50438350"><a name="b50438350"></a><a name="b50438350"></a>PartNumberMarker</strong> in a subsequent request after a part list is truncated.</p>
<p id="p51291972"><a name="p51291972"></a><a name="p51291972"></a>Type: Integer</p>
<p id="p58974565"><a name="p58974565"></a><a name="p58974565"></a>Ancestor: <strong id="b61009044"><a name="b61009044"></a><a name="b61009044"></a>ListPartsResult</strong></p>
</td>
</tr>
<tr id="row12210489"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p49525553"><a name="p49525553"></a><a name="p49525553"></a>MaxParts</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p52146870"><a name="p52146870"></a><a name="p52146870"></a>Maximum number of parts that are returned</p>
<p id="p66668648"><a name="p66668648"></a><a name="p66668648"></a>Type: Integer</p>
<p id="p63146927"><a name="p63146927"></a><a name="p63146927"></a>Ancestor: <strong id="b31451435"><a name="b31451435"></a><a name="b31451435"></a>ListPartsResult</strong></p>
</td>
</tr>
<tr id="row14627461"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p43973663"><a name="p43973663"></a><a name="p43973663"></a>IsTruncated</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p5096933"><a name="p5096933"></a><a name="p5096933"></a>Indicates whether the returned part list is truncated. <strong id="b45872405"><a name="b45872405"></a><a name="b45872405"></a>true</strong>&nbsp;indicates that the list was truncated and&nbsp;<strong id="b10198465"><a name="b10198465"></a><a name="b10198465"></a>false</strong> indicates that the list was not truncated.</p>
<p id="p24677321"><a name="p24677321"></a><a name="p24677321"></a>Type: Boolean</p>
<p id="p20769304"><a name="p20769304"></a><a name="p20769304"></a>Ancestor: <strong id="b52706014"><a name="b52706014"></a><a name="b52706014"></a>ListPartsResult</strong></p>
</td>
</tr>
<tr id="row4592084"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p36414557"><a name="p36414557"></a><a name="p36414557"></a>Part</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p63898010"><a name="p63898010"></a><a name="p63898010"></a>Container for elements related to a particular part</p>
<p id="p38211184"><a name="p38211184"></a><a name="p38211184"></a>Type: String</p>
<p id="p8356340"><a name="p8356340"></a><a name="p8356340"></a>Children: <strong id="b8098199"><a name="b8098199"></a><a name="b8098199"></a>PartNumber</strong>,&nbsp;<strong id="b5774930"><a name="b5774930"></a><a name="b5774930"></a>LastModified</strong>,&nbsp;<strong id="b51974374"><a name="b51974374"></a><a name="b51974374"></a>ETag</strong>,&nbsp;<strong id="b65116189"><a name="b65116189"></a><a name="b65116189"></a>Size</strong></p>
<p id="p49174790"><a name="p49174790"></a><a name="p49174790"></a>Ancestor: <strong id="b39919932"><a name="b39919932"></a><a name="b39919932"></a>ListPartsResult</strong></p>
</td>
</tr>
<tr id="row23735071"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p43492568"><a name="p43492568"></a><a name="p43492568"></a>PartNumber</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p33237081"><a name="p33237081"></a><a name="p33237081"></a>Number that identifies a part</p>
<p id="p30698276"><a name="p30698276"></a><a name="p30698276"></a>Type: Integer</p>
<p id="p7849035"><a name="p7849035"></a><a name="p7849035"></a>Ancestor: <strong id="b3532453"><a name="b3532453"></a><a name="b3532453"></a>ListPartsResult.Part</strong></p>
</td>
</tr>
<tr id="row31792085"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p25022112"><a name="p25022112"></a><a name="p25022112"></a>LastModified</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p13525204"><a name="p13525204"></a><a name="p13525204"></a>Date and time at which a part was uploaded</p>
<p id="p54617972"><a name="p54617972"></a><a name="p54617972"></a>Type: Date</p>
<p id="p21799703"><a name="p21799703"></a><a name="p21799703"></a>Ancestor: <strong id="b61979607"><a name="b61979607"></a><a name="b61979607"></a>ListPartsResult.Part</strong></p>
</td>
</tr>
<tr id="row20945556"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p18868465"><a name="p18868465"></a><a name="p18868465"></a>ETag</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p51950678"><a name="p51950678"></a><a name="p51950678"></a>ETag of an uploaded part.</p>
<p id="p64902924"><a name="p64902924"></a><a name="p64902924"></a>Type: String</p>
<p id="p47255404"><a name="p47255404"></a><a name="p47255404"></a>Ancestor: <strong id="b22645457"><a name="b22645457"></a><a name="b22645457"></a>ListPartsResult.Part</strong></p>
</td>
</tr>
<tr id="row2482522"><td class="cellrowborder" valign="top" width="26.55%" headers="mcps1.2.3.1.1 "><p id="p66866633"><a name="p66866633"></a><a name="p66866633"></a>Size</p>
</td>
<td class="cellrowborder" valign="top" width="73.45%" headers="mcps1.2.3.1.2 "><p id="p47488225"><a name="p47488225"></a><a name="p47488225"></a>Size of an uploaded part</p>
<p id="p24740843"><a name="p24740843"></a><a name="p24740843"></a>Type: Integer</p>
<p id="p21341001"><a name="p21341001"></a><a name="p21341001"></a>Ancestor: <strong id="b57851282"><a name="b57851282"></a><a name="b57851282"></a>ListPartsResult.Part</strong></p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section52614321"></a>

-   If an AccessKey or signature is invalid, OBS returns status code  **403 Forbidden** and error code **AccessDenied**.
-   If the requested bucket does not exist, OBS returns status code  **404 Not Found** and error code **NoSuchBucket**.
-   If the requested multipart upload does not exist, OBS returns status code  **404 Not Found** and error code **NoSuchUpload**.
-   If the requester does not have  **READ** permission for the requested bucket, OBS returns status code **403 Forbidden** and error code **AccessDenied**.

For details about other error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section63777619"></a>

```
GET /example-object?uploadId=XXBsb2FkIElEIGZvciBlbHZpbmcncyVcdS1tb3ZpZS5tMnRzEEEwbG9hZA&max-parts=2&part-number-marker=1 HTTP/1.1 
 User-Agent: Jakarta Commons-HttpClient/3.1
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Mon, 1 Nov 2010 20:34:56 GMT 
 Authorization: AWS AKIAIOSFODNN7EXAMPLE:0RQf4/cRonhpaBX5sCYVf1bNRuU=
```

## Sample Response<a name="section37127664"></a>

```
HTTP/1.1 200 OK 
 x-amz-id-2: Uuag1LuByRx9e6j5Onimru9pO4ZVKnJ2Qz7/C1NPcfTWAtRPfTaOFg== 
 x-amz-request-id: 656c76696e6727732072657175657374 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Type: application/xml
 Date: Mon, 1 Nov 2010 20:34:56 GMT 
 Content-Length: 985 
 Connection: keep-alive 
 Server: OBS 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <ListPartsResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Bucket>example-bucket</Bucket> 
 <Key>example-object</Key> 
 <UploadId>XXBsb2FkIElEIGZvciBlbHZpbmcncyVcdS1tb3ZpZS5tMnRzEEEwbG9hZA</UploadId> 
 <Initiator> 
 <ID> 11116a31-17b5-4fb7-9df5-b288870f11xx</ID>  
 <DisplayName>umat-user-11116a31-17b5-4fb7-9df5-b288870f11xx</DisplayName> 
 </Initiator> 
 <Owner> 
 <ID>75aa57f09aa0c8caeab4f8c24e99d10f8e7faeebf76c078efc7c6caea54ba06a</ID> 
 <DisplayName>someName</DisplayName> 
 </Owner> 
 <StorageClass>STANDARD</StorageClass> 
 <PartNumberMarker>1</PartNumberMarker> 
 <NextPartNumberMarker>3</NextPartNumberMarker> 
 <MaxParts>2</MaxParts> 
 <IsTruncated>true</IsTruncated> 
 <Part> 
 <PartNumber>2</PartNumber> 
 <LastModified>2010-11-10T20:48:34.000Z</LastModified> 
 <ETag>"7778aef83f66abc1fa1e8477f296d394"</ETag> 
 <Size>10485760</Size> 
 </Part> 
 <Part> 
 <PartNumber>3</PartNumber> 
 <LastModified>2010-11-10T20:48:33.000Z</LastModified> 
 <ETag>"aaaa18db4cc2f85cedef654fccc4a4x8"</ETag> 
 <Size>10485760</Size> 
 </Part> 
 </ListPartsResult>
```

