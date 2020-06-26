# List Multipart Uploads<a name="EN-US_TOPIC_0125560292"></a>

You can use this operation to query all in-progress multipart uploads that have been initiated but not been combined or aborted.

## Request Syntax<a name="section56778103"></a>

```
GET /?uploads&max-uploads=max HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: Mon, 1 Nov 2010 20:34:56 GMT 
 Authorization: auth
```

## Request Parameters<a name="section41240880"></a>

This request uses parameters to specify the query range for multipart uploads.  [Table 1](#table25002124)  describes the parameters.

**Table  1**  Request parameters

<a name="table25002124"></a>
<table><thead align="left"><tr id="row20781721"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p5597801"><a name="p5597801"></a><a name="p5597801"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p50768709"><a name="p50768709"></a><a name="p50768709"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p18624790"><a name="p18624790"></a><a name="p18624790"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row33405390"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p21482089"><a name="p21482089"></a><a name="p21482089"></a>delimiter</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p62327661"><a name="p62327661"></a><a name="p62327661"></a>Character used to group object keys.</p>
<p id="p24078037"><a name="p24078037"></a><a name="p24078037"></a>All keys that contain the same string between <strong id="b15375744"><a name="b15375744"></a><a name="b15375744"></a>prefix</strong>, if specified, and the first occurrence of the delimiter after&nbsp;<strong id="b4163976"><a name="b4163976"></a><a name="b4163976"></a>prefix</strong>&nbsp;are grouped under a single result element&nbsp;<strong id="b37475789"><a name="b37475789"></a><a name="b37475789"></a>CommonPrefixes</strong>.&nbsp;<strong id="b1737784"><a name="b1737784"></a><a name="b1737784"></a>CommonPrefix</strong> contains no information about any multipart upload. It is only used for informing users of the following: multipart uploads are contained in this group.</p>
<p id="p15640058"><a name="p15640058"></a><a name="p15640058"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p58885167"><a name="p58885167"></a><a name="p58885167"></a>Optional</p>
</td>
</tr>
<tr id="row60204461"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p44723138"><a name="p44723138"></a><a name="p44723138"></a>prefix</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p65804403"><a name="p65804403"></a><a name="p65804403"></a>Lists in-progress uploads only for those object keys that begin with the specified prefix.</p>
<p id="p55368722"><a name="p55368722"></a><a name="p55368722"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p55681530"><a name="p55681530"></a><a name="p55681530"></a>Optional</p>
</td>
</tr>
<tr id="row31371724"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p58081731"><a name="p58081731"></a><a name="p58081731"></a>max-uploads</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6999799"><a name="p6999799"></a><a name="p6999799"></a>Sets the maximum number (ranging from 1 to 1000) of multipart uploads to be returned in the response body. If the value is not in this range, 1000 is returned by default.</p>
<p id="p62998195"><a name="p62998195"></a><a name="p62998195"></a>Type: Integer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2580172"><a name="p2580172"></a><a name="p2580172"></a>Optional</p>
</td>
</tr>
<tr id="row23221556"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1897869"><a name="p1897869"></a><a name="p1897869"></a>key-marker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p19509699"><a name="p19509699"></a><a name="p19509699"></a>Indicates the multipart upload after which the listing begins.</p>
<p id="p41369564"><a name="p41369564"></a><a name="p41369564"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p62600359"><a name="p62600359"></a><a name="p62600359"></a>Optional</p>
</td>
</tr>
<tr id="row26532323"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1634591"><a name="p1634591"></a><a name="p1634591"></a>upload-id-marker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p65293014"><a name="p65293014"></a><a name="p65293014"></a>Indicates the multipart upload after which the listing begins. This parameter is used together with <strong id="b50766220"><a name="b50766220"></a><a name="b50766220"></a>key-marker</strong>.</p>
<p id="p54242802"><a name="p54242802"></a><a name="p54242802"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p31590875"><a name="p31590875"></a><a name="p31590875"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section35623602"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section52176966"></a>

This request involves no elements.

## Response Syntax<a name="section32948183"></a>

```
HTTP/1.1 status_code 
 Server: OBS
 x-amz-request-id: request id 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: id2 
 Content-Length: length 
 Date: date 
 Connection: connect state

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <ListMultipartUploadsResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Bucket>bucket</Bucket> 
 <KeyMarker></KeyMarker> 
 <UploadIdMarker></UploadIdMarker> 
 <NextKeyMarker>nextMarker</NextKeyMarker> 
 <NextUploadIdMarker>idMarker</NextUploadIdMarker> 
 <MaxUploads>maxUploads</MaxUploads> 
 <IsTruncated>true</IsTruncated> 
 <Upload> 
 <Key>key</Key> 
 <UploadId>uploadID</UploadId> 
 <Initiator> 
 <ID>id</ID> 
 <DisplayName>name</DisplayName> 
 </Initiator> 
 <Owner> 
 <ID>ownerID</ID> 
 <DisplayName>OwnerDisplayName</DisplayName> 
 </Owner> 
 <StorageClass>STANDARD</StorageClass> 
 <Initiated>initiatedDate</Initiated>  
 </Upload> 
 </ListMultipartUploadsResult>
```

## Response Headers<a name="section28098193"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section51557149"></a>

This response contains elements to provide details about the listed multipart uploads.  [Table 2](#table36296664)  describes the elements.

**Table  2**  Response elements

<a name="table36296664"></a>
<table><thead align="left"><tr id="row62252322"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p9273323"><a name="p9273323"></a><a name="p9273323"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p12941733"><a name="p12941733"></a><a name="p12941733"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p41647480"><a name="p41647480"></a><a name="p41647480"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row39283002"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p27806564"><a name="p27806564"></a><a name="p27806564"></a>ListMultipartUploads Result</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p37739194"><a name="p37739194"></a><a name="p37739194"></a>Container for the response</p>
<p id="p4108434"><a name="p4108434"></a><a name="p4108434"></a>Type: Container</p>
<p id="p36975910"><a name="p36975910"></a><a name="p36975910"></a>Children: <strong id="b64347734"><a name="b64347734"></a><a name="b64347734"></a>Bucket</strong>,&nbsp;<strong id="b42258701"><a name="b42258701"></a><a name="b42258701"></a>KeyMarker</strong>,&nbsp;<strong id="b44783995"><a name="b44783995"></a><a name="b44783995"></a>UploadIdMarker</strong>,&nbsp;<strong id="b402777"><a name="b402777"></a><a name="b402777"></a>NextKeyMarker</strong>,&nbsp;<strong id="b3625001"><a name="b3625001"></a><a name="b3625001"></a>NextUploadIdMarker</strong>,&nbsp;<strong id="b32625010"><a name="b32625010"></a><a name="b32625010"></a>Delimiter</strong>,&nbsp;<strong id="b25189639"><a name="b25189639"></a><a name="b25189639"></a>Prefix</strong>,&nbsp;<strong id="b25380159"><a name="b25380159"></a><a name="b25380159"></a>MaxUploads</strong>,&nbsp;<strong id="b27094845"><a name="b27094845"></a><a name="b27094845"></a>IsTruncated</strong>,&nbsp;<strong id="b42527017"><a name="b42527017"></a><a name="b42527017"></a>Upload</strong>, and&nbsp;<strong id="b47198836"><a name="b47198836"></a><a name="b47198836"></a>CommonPrefixes</strong></p>
<p id="p22136343"><a name="p22136343"></a><a name="p22136343"></a>Ancestor: None</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p48213362"><a name="p48213362"></a><a name="p48213362"></a>Mandatory</p>
</td>
</tr>
<tr id="row31267075"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p49605164"><a name="p49605164"></a><a name="p49605164"></a>Bucket</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p58595317"><a name="p58595317"></a><a name="p58595317"></a>Name of the bucket to which the multipart upload was initiated</p>
<p id="p57595805"><a name="p57595805"></a><a name="p57595805"></a>Type: String</p>
<p id="p48600198"><a name="p48600198"></a><a name="p48600198"></a>Ancestor: <strong id="b34748601"><a name="b34748601"></a><a name="b34748601"></a>ListMultipartUploadsResult</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p63173322"><a name="p63173322"></a><a name="p63173322"></a>Mandatory</p>
</td>
</tr>
<tr id="row31688994"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16671741"><a name="p16671741"></a><a name="p16671741"></a>KeyMarker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p8233793"><a name="p8233793"></a><a name="p8233793"></a>Object keys at or after which the multipart upload listing begins</p>
<p id="p6995273"><a name="p6995273"></a><a name="p6995273"></a>Type: String</p>
<p id="p62957460"><a name="p62957460"></a><a name="p62957460"></a>Ancestor: <strong id="b29746236"><a name="b29746236"></a><a name="b29746236"></a>ListMultipartUploadsResult</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p60634924"><a name="p60634924"></a><a name="p60634924"></a>Mandatory</p>
</td>
</tr>
<tr id="row8843406"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p45227267"><a name="p45227267"></a><a name="p45227267"></a>UploadIdMarker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p39530025"><a name="p39530025"></a><a name="p39530025"></a>Upload ID after which the multipart upload listing begins</p>
<p id="p20225910"><a name="p20225910"></a><a name="p20225910"></a>Type: String</p>
<p id="p47815463"><a name="p47815463"></a><a name="p47815463"></a>Ancestor: <strong id="b27685991"><a name="b27685991"></a><a name="b27685991"></a>ListMultipartUploadsResult</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p27972830"><a name="p27972830"></a><a name="p27972830"></a>Mandatory</p>
</td>
</tr>
<tr id="row50428878"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p58207302"><a name="p58207302"></a><a name="p58207302"></a>NextKeyMarker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p17170998"><a name="p17170998"></a><a name="p17170998"></a>Value of <strong id="b20321259"><a name="b20321259"></a><a name="b20321259"></a>KeyMarker</strong> in a subsequent request after a multipart upload list is truncated</p>
<p id="p48673607"><a name="p48673607"></a><a name="p48673607"></a>Type: String</p>
<p id="p35409283"><a name="p35409283"></a><a name="p35409283"></a>Ancestor: <strong id="b50248096"><a name="b50248096"></a><a name="b50248096"></a>ListMultipartUploadsResult</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p43564010"><a name="p43564010"></a><a name="p43564010"></a>Mandatory</p>
</td>
</tr>
<tr id="row56531777"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15671223"><a name="p15671223"></a><a name="p15671223"></a>NextUploadIdMarker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p61409521"><a name="p61409521"></a><a name="p61409521"></a>Value of <strong id="b15814779"><a name="b15814779"></a><a name="b15814779"></a>UploadMarker</strong> in a subsequent request after a multipart upload list is truncated</p>
<p id="p8115287"><a name="p8115287"></a><a name="p8115287"></a>Type: String</p>
<p id="p5928727"><a name="p5928727"></a><a name="p5928727"></a>Ancestor: <strong id="b53358547"><a name="b53358547"></a><a name="b53358547"></a>ListMultipartUploadsResult</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p27075018"><a name="p27075018"></a><a name="p27075018"></a>Mandatory</p>
</td>
</tr>
<tr id="row42348576"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p7682654"><a name="p7682654"></a><a name="p7682654"></a>MaxUploads</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p18315212"><a name="p18315212"></a><a name="p18315212"></a>Maximum of multipart uploads to be returned in the response</p>
<p id="p30619180"><a name="p30619180"></a><a name="p30619180"></a>Type: Integer</p>
<p id="p7137170"><a name="p7137170"></a><a name="p7137170"></a>Ancestor: <strong id="b64234534"><a name="b64234534"></a><a name="b64234534"></a>ListMultipartUploadsResult</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p35614756"><a name="p35614756"></a><a name="p35614756"></a>Mandatory</p>
</td>
</tr>
<tr id="row52097352"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p59136008"><a name="p59136008"></a><a name="p59136008"></a>IsTruncated</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p25287361"><a name="p25287361"></a><a name="p25287361"></a>Indicates whether the returned list of multipart uploads is truncated. <strong id="b26259658"><a name="b26259658"></a><a name="b26259658"></a>true</strong>&nbsp;indicates that the list was truncated and&nbsp;<strong id="b35010330"><a name="b35010330"></a><a name="b35010330"></a>false</strong> indicates that the list was not truncated.</p>
<p id="p46657514"><a name="p46657514"></a><a name="p46657514"></a>Type: Boolean</p>
<p id="p17264443"><a name="p17264443"></a><a name="p17264443"></a>Ancestor: <strong id="b21162262"><a name="b21162262"></a><a name="b21162262"></a>ListMultipartUploadsResult</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p36421687"><a name="p36421687"></a><a name="p36421687"></a>Mandatory</p>
</td>
</tr>
<tr id="row59359735"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43409250"><a name="p43409250"></a><a name="p43409250"></a>Upload</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p26488374"><a name="p26488374"></a><a name="p26488374"></a>Container for elements related to a specific multipart upload</p>
<p id="p37068774"><a name="p37068774"></a><a name="p37068774"></a>Type: Container</p>
<p id="p65183513"><a name="p65183513"></a><a name="p65183513"></a>Children: <strong id="b49780713"><a name="b49780713"></a><a name="b49780713"></a>Key</strong>,&nbsp;<strong id="b45373238"><a name="b45373238"></a><a name="b45373238"></a>UploadId</strong>,&nbsp;<strong id="b5705961"><a name="b5705961"></a><a name="b5705961"></a>InitiatorOwner</strong>,&nbsp;<strong id="b51353651"><a name="b51353651"></a><a name="b51353651"></a>StorageClass</strong>,&nbsp;<strong id="b59529677"><a name="b59529677"></a><a name="b59529677"></a>Initiated</strong></p>
<p id="p66005048"><a name="p66005048"></a><a name="p66005048"></a>Ancestor: <strong id="b57174526"><a name="b57174526"></a><a name="b57174526"></a>ListMultipartUploadsResult</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p624995"><a name="p624995"></a><a name="p624995"></a>Mandatory</p>
</td>
</tr>
<tr id="row5624956"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p52968331"><a name="p52968331"></a><a name="p52968331"></a>Key</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p62576451"><a name="p62576451"></a><a name="p62576451"></a>Key of the object for which the multipart upload was initiated</p>
<p id="p26317149"><a name="p26317149"></a><a name="p26317149"></a>Type: String</p>
<p id="p35527755"><a name="p35527755"></a><a name="p35527755"></a>Ancestor: <strong id="b51314340"><a name="b51314340"></a><a name="b51314340"></a>Upload</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p62820904"><a name="p62820904"></a><a name="p62820904"></a>Mandatory</p>
</td>
</tr>
<tr id="row28517228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p28194133"><a name="p28194133"></a><a name="p28194133"></a>UploadId</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2023471"><a name="p2023471"></a><a name="p2023471"></a>ID of the multipart upload</p>
<p id="p18211246"><a name="p18211246"></a><a name="p18211246"></a>Type: String</p>
<p id="p29683490"><a name="p29683490"></a><a name="p29683490"></a>Ancestor: <strong id="b65824820"><a name="b65824820"></a><a name="b65824820"></a>Upload</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p30210174"><a name="p30210174"></a><a name="p30210174"></a>Mandatory</p>
</td>
</tr>
<tr id="row3456112"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p11509660"><a name="p11509660"></a><a name="p11509660"></a>Initiator</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p59867264"><a name="p59867264"></a><a name="p59867264"></a>Container element that identifies who initiated the multipart upload</p>
<p id="p1934471"><a name="p1934471"></a><a name="p1934471"></a>Children: <strong id="b17410245"><a name="b17410245"></a><a name="b17410245"></a>ID</strong>,&nbsp;<strong id="b22474483"><a name="b22474483"></a><a name="b22474483"></a>DisplayName</strong></p>
<p id="p943763"><a name="p943763"></a><a name="p943763"></a>Type: Container</p>
<p id="p8493868"><a name="p8493868"></a><a name="p8493868"></a>Ancestor: <strong id="b9335953"><a name="b9335953"></a><a name="b9335953"></a>Upload</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18014695"><a name="p18014695"></a><a name="p18014695"></a>Mandatory</p>
</td>
</tr>
<tr id="row27914531"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p46484529"><a name="p46484529"></a><a name="p46484529"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p7150508"><a name="p7150508"></a><a name="p7150508"></a>DomainId of the user.</p>
<p id="p64354573"><a name="p64354573"></a><a name="p64354573"></a>Type: String</p>
<p id="p42320251"><a name="p42320251"></a><a name="p42320251"></a>Ancestor: <strong id="b45337942"><a name="b45337942"></a><a name="b45337942"></a>Initiator</strong>,&nbsp;<strong id="b5388295"><a name="b5388295"></a><a name="b5388295"></a>Owner</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p33798711"><a name="p33798711"></a><a name="p33798711"></a>Mandatory</p>
</td>
</tr>
<tr id="row35752944"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p10307346"><a name="p10307346"></a><a name="p10307346"></a>DisplayName</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p29588684"><a name="p29588684"></a><a name="p29588684"></a>Initiator name</p>
<p id="p64971570"><a name="p64971570"></a><a name="p64971570"></a>Type: String</p>
<p id="p47873223"><a name="p47873223"></a><a name="p47873223"></a>Ancestor: <strong id="b28205828"><a name="b28205828"></a><a name="b28205828"></a>Initiator</strong>,&nbsp;<strong id="b52525867"><a name="b52525867"></a><a name="b52525867"></a>Owner</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p26736798"><a name="p26736798"></a><a name="p26736798"></a>Mandatory</p>
</td>
</tr>
<tr id="row39304598"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p29555878"><a name="p29555878"></a><a name="p29555878"></a>Owner</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p45215898"><a name="p45215898"></a><a name="p45215898"></a>Container element that identifies the object owner. This element is the same as <strong id="b4289901"><a name="b4289901"></a><a name="b4289901"></a>Initiator</strong>&nbsp;and compatible with Amazon S3. In S3, if a multipart upload is initiated by an IAM user,&nbsp;<strong id="b38609115"><a name="b38609115"></a><a name="b38609115"></a>Initiator</strong>&nbsp;may differ from&nbsp;<strong id="b11937715"><a name="b11937715"></a><a name="b11937715"></a>Owner</strong>.</p>
<p id="p40330576"><a name="p40330576"></a><a name="p40330576"></a>Type: Container</p>
<p id="p27430865"><a name="p27430865"></a><a name="p27430865"></a>Children: <strong id="b45551201"><a name="b45551201"></a><a name="b45551201"></a>ID</strong>,&nbsp;<strong id="b7307632"><a name="b7307632"></a><a name="b7307632"></a>DisplayName</strong></p>
<p id="p65768696"><a name="p65768696"></a><a name="p65768696"></a>Ancestor: <strong id="b55047352"><a name="b55047352"></a><a name="b55047352"></a>Upload</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p29650512"><a name="p29650512"></a><a name="p29650512"></a>Mandatory</p>
</td>
</tr>
<tr id="row65528017"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6169189"><a name="p6169189"></a><a name="p6169189"></a>StorageClass</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p29942301"><a name="p29942301"></a><a name="p29942301"></a>Type of storage that will be used for storing objects after the multipart upload is complete.</p>
<p id="p1045258"><a name="p1045258"></a><a name="p1045258"></a>Type: Enumeration</p>
<p id="p9407330"><a name="p9407330"></a><a name="p9407330"></a>Ancestor: <strong id="b17557108"><a name="b17557108"></a><a name="b17557108"></a>Upload</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p12839671"><a name="p12839671"></a><a name="p12839671"></a>Mandatory</p>
</td>
</tr>
<tr id="row48448177"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p31988235"><a name="p31988235"></a><a name="p31988235"></a>Initiated</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p40910225"><a name="p40910225"></a><a name="p40910225"></a>Date and time at which the multipart upload was initiated</p>
<p id="p32647713"><a name="p32647713"></a><a name="p32647713"></a>Type: Date</p>
<p id="p25393965"><a name="p25393965"></a><a name="p25393965"></a>Ancestor: <strong id="b27219093"><a name="b27219093"></a><a name="b27219093"></a>Upload</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p57262954"><a name="p57262954"></a><a name="p57262954"></a>Mandatory</p>
</td>
</tr>
<tr id="row45604544"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2980617"><a name="p2980617"></a><a name="p2980617"></a>ListMultipartUploadsResult.Prefix</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p40103430"><a name="p40103430"></a><a name="p40103430"></a>Contains the prefix specified in the request.</p>
<p id="p25386556"><a name="p25386556"></a><a name="p25386556"></a>Type: String</p>
<p id="p27152416"><a name="p27152416"></a><a name="p27152416"></a>Ancestor: <strong id="b43045155"><a name="b43045155"></a><a name="b43045155"></a>ListMultipartUploadsResult</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p64105522"><a name="p64105522"></a><a name="p64105522"></a>Mandatory</p>
</td>
</tr>
<tr id="row40078793"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p25156776"><a name="p25156776"></a><a name="p25156776"></a>Delimiter</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p24432964"><a name="p24432964"></a><a name="p24432964"></a>Contains the delimiter specified in the request.</p>
<p id="p18570084"><a name="p18570084"></a><a name="p18570084"></a>Type: String</p>
<p id="p32913028"><a name="p32913028"></a><a name="p32913028"></a>Ancestor: <strong id="b27781797"><a name="b27781797"></a><a name="b27781797"></a>ListMultipartUploadsResult</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p35733079"><a name="p35733079"></a><a name="p35733079"></a>Mandatory</p>
</td>
</tr>
<tr id="row53162257"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p11175599"><a name="p11175599"></a><a name="p11175599"></a>CommonPrefixes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p32808337"><a name="p32808337"></a><a name="p32808337"></a>If you specify a delimiter in the request, the result returns each distinct key prefix containing the delimiter in a <strong id="b5531242155811"><a name="b5531242155811"></a><a name="b5531242155811"></a>CommonPrefixes</strong> element.</p>
<p id="p40229664"><a name="p40229664"></a><a name="p40229664"></a>Type: Container</p>
<p id="p26522659"><a name="p26522659"></a><a name="p26522659"></a>Ancestor: <strong id="b37377347"><a name="b37377347"></a><a name="b37377347"></a>ListMultipartUploadsResult</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p7666275"><a name="p7666275"></a><a name="p7666275"></a>Mandatory</p>
</td>
</tr>
<tr id="row1887613"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p18678946"><a name="p18678946"></a><a name="p18678946"></a>CommonPrefixes. Prefix</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p36599672"><a name="p36599672"></a><a name="p36599672"></a>Prefix contained in a <strong id="b365945245812"><a name="b365945245812"></a><a name="b365945245812"></a>CommonPrefix</strong> element</p>
<p id="p11783462"><a name="p11783462"></a><a name="p11783462"></a>Type: String</p>
<p id="p38942302"><a name="p38942302"></a><a name="p38942302"></a>Ancestor: <strong id="b14936405"><a name="b14936405"></a><a name="b14936405"></a>CommonPrefixes</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1889325"><a name="p1889325"></a><a name="p1889325"></a>Mandatory</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section61361165"></a>

1.  If an AK or signature is invalid, OBS returns status code  **403 Forbidden** and error code **AccessDenied**.
2.  If the requested bucket does not exist, OBS returns status code  **404 Not Found** and error code **NoSuchBucket**.
3.  If the requester does not have  **READ** permission for the requested bucket, OBS returns status code **403 Forbidden** and error code **AccessDenied**.
4.  If the value of  **maxUploads** is a non-integer or smaller than 0, OBS returns status code **400 Bad Request**.

For details about other error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section48013777"></a>

```
GET /?uploads&max-uploads=3 HTTP/1.1 
 User-Agent: curl/7.19.0
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Mon, 1 Nov 2010 20:34:56 GMT 
 Authorization: AWS AKIAIOSFODNN7EXAMPLE:0RQf4/cRonhpaBX5sCYVf1bNRuU=
```

## Sample Response<a name="section29470815"></a>

```
HTTP/1.1 200 OK 
 Server: OBS 
 x-amz-request-id: 656c76696e6727732072657175657374 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 x-amz-id-2: Uuag1LuByRx9e6j5Onimru9pO4ZVKnJ2Qz7/C1NPcfTWAtRPfTaOFg== 
 Date: Mon, 1 Nov 2010 20:34:56 GMT 
 Content-Length: 1330 
 Connection: keep-alive 

 <?xml version="1.0" encoding="UTF-8" standalone="yes"?> 
 <ListMultipartUploadsResult xmlns="http://obs.example.com/doc/2015-06-30/"> 
 <Bucket>bucket</Bucket> 
 <KeyMarker></KeyMarker> 
 <UploadIdMarker></UploadIdMarker> 
 <NextKeyMarker>my-movie.m2ts</NextKeyMarker> 
 <NextUploadIdMarker>YW55gd2h5IGVsdmluZydzIHVwbG9hZCBmYWlsZWQ</NextUploadIdMarker> 
 <MaxUploads>3</MaxUploads> 
 <IsTruncated>true</IsTruncated> 
 <Upload> 
 <Key>my-divisor</Key> 
 <UploadId>XMgbGlrZSBlbHZpbmcncyBub3QgaGF2aW5nIG11Y2ggbHVjaw</UploadId> 
 <Initiator> 
 <ID>b1d16700c70b0b05597d7acd6a3f92be</ID> 
 <DisplayName>InitiatorDisplayName</DisplayName> 
 </Initiator> 
 <Owner> 
 <ID>75aa57f09aa0c8caeab4f84e99d10f8e</ID> 
 <DisplayName>OwnerDisplayName</DisplayName> 
 </Owner> 
 <StorageClass>STANDARD</StorageClass> 
 <Initiated>2010-11-10T20:48:33.000Z</Initiated>  
 </Upload> 
 <Upload> 
 <Key>my-movie.m2ts</Key> 
 <UploadId>VXBsb2FkIElEIGZvciBlbHZpbmcncyBteS1tb3ZpZS5tMnRzIHVwbG9hZA</UploadId> 
 <Initiator> 
 <ID>b1d16700c70b0b05597d7acd6a3f92be</ID> 
 <DisplayName>InitiatorDisplayName</DisplayName> 
 </Initiator> 
 <Owner> 
 <ID>b1d16700c70b0b05597d7acd6a3f92be</ID> 
 <DisplayName>InitiatorDisplayName</DisplayName> 
 </Owner> 
 <StorageClass>STANDARD</StorageClass> 
 <Initiated>2010-11-10T20:48:33.000Z</Initiated> 
 </Upload> 
 <Upload> 
 <Key>my-movie.m2ts</Key> 
 <UploadId>YW55IGlkZWEgd2h5IGVsdmluZydzIHVwbG9hZCBmYWlsZWQ</UploadId> 
 <Initiator> 
 <ID>75aa57f09aa0c8caeab4f84e99d10f8e</ID> 
 <DisplayName>OwnerDisplayName</DisplayName> 
 </Initiator> 
 <Owner> 
 <ID>b1d16700c70b0b05597d7acd6a3f92be</ID> 
 <DisplayName>InitiatorDisplayName</DisplayName> 
 </Owner> 
 <StorageClass>STANDARD</StorageClass> 
 <Initiated>2010-11-10T20:49:33.000Z</Initiated> 
 </Upload> 
 </ListMultipartUploadsResult>
```

