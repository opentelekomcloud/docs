# PUT Bucket Notification<a name="EN-US_TOPIC_0125560248"></a>

When the notification function is enabled, you will be notified of all the specified operations on your bucket. 

By default, the notification function of your bucket is not enabled. Namely, the NotificationConfiguration element is null. If you want to disable the function, set the NotificationConfiguration element to null.

After receiving the notification request, OBS verifies whether the specified Simple Message Notification \(SMN\) topic exists and whether the topic is authorized to OBS. If the topic exists and is authorized to OBS, OBS sends a test notification to the topic.

The  **s3:PutBucketNotification**  permission is required to configure the notification function. By default, the permission is granted to the bucket owner only. However, it can be granted to other users by configuring the bucket policy.

>![](/images/icon-note.gif) **NOTE:**   
>For details about how to authorize topics to OBS, see the  _SMN User Guide_  

## Request Syntax<a name="section35786508144743"></a>

```
PUT /?notification HTTP/1.1
User-Agent: agent 
Host: bucketname.obs.example.com
Accept: */* 
Date: date 
Authorization: authorization
Content-Length: length
Expect: expect
 
<NotificationConfiguration> 
 <TopicConfiguration> 
  <Id>ConfigurationId</Id>
  <Filter>
   <S3Key>
    <FilterRule>
     <Name>prefix</Name>
     <Value>prefix-value</Value>
    </FilterRule>
    <FilterRule>
     <Name>suffix</Name>
     <Value>suffix-value</Value>
    </FilterRule>
   </S3Key>
  </Filter>
  <Topic>TopicARN</Topic>
  <Event>event-type</Event>
  <Event>event-type</Event>
  ...
 </TopicConfiguration>
</NotificationConfiguration>
```

## Request Parameters<a name="section27343126145027"></a>

This request contains no parameter.

## Request Headers<a name="section1806247145027"></a>

This request uses common headers. For details, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section41685955145027"></a>

This request contains elements to specify the notification configuration for the bucket in XML format. The following table lists the request elements.

**Table  1**  Request elements of notification function configuration

<a name="table55855374145027"></a>
<table><thead align="left"><tr id="row43394869145027"><th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.2.4.1.1"><p id="p25323481145027"><a name="p25323481145027"></a><a name="p25323481145027"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="60.61%" id="mcps1.2.4.1.2"><p id="p37936074145027"><a name="p37936074145027"></a><a name="p37936074145027"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="19.189999999999998%" id="mcps1.2.4.1.3"><p id="p52923119145027"><a name="p52923119145027"></a><a name="p52923119145027"></a>Mandatory or Not</p>
</th>
</tr>
</thead>
<tbody><tr id="row58914224145027"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p7322871145027"><a name="p7322871145027"></a><a name="p7322871145027"></a>NotificationConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.2 "><p id="p56281641145027"><a name="p56281641145027"></a><a name="p56281641145027"></a>Container for configuring the event notification function of a bucket. If this element is null, the function is disabled.</p>
<p id="p36772727145027"><a name="p36772727145027"></a><a name="p36772727145027"></a>Type: Container</p>
<p id="p62519088145027"><a name="p62519088145027"></a><a name="p62519088145027"></a>Ancestor: None</p>
<p id="p25800887145027"><a name="p25800887145027"></a><a name="p25800887145027"></a>Children: zero TopicConfiguration, one TopicConfiguration, or TopicConfigurations</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.3 "><p id="p9497112145027"><a name="p9497112145027"></a><a name="p9497112145027"></a>Yes</p>
</td>
</tr>
<tr id="row18365148145027"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p11182033145027"><a name="p11182033145027"></a><a name="p11182033145027"></a>TopicConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.2 "><p id="p33329466145027"><a name="p33329466145027"></a><a name="p33329466145027"></a>Container for configuring the event notification topic</p>
<p id="p31529742145027"><a name="p31529742145027"></a><a name="p31529742145027"></a>Type: Container</p>
<p id="p15332224145027"><a name="p15332224145027"></a><a name="p15332224145027"></a>Ancestor: NotificationConfiguration</p>
<p id="p3772289145027"><a name="p3772289145027"></a><a name="p3772289145027"></a>Children: Id, Filter, Topic, Event or Events</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.3 "><p id="p37119964145027"><a name="p37119964145027"></a><a name="p37119964145027"></a>No</p>
</td>
</tr>
<tr id="row65644224145027"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p15581964145027"><a name="p15581964145027"></a><a name="p15581964145027"></a>Topic</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.2 "><p id="p54179539145027"><a name="p54179539145027"></a><a name="p54179539145027"></a>URN of the event notification topic. After detecting a specific event, OBS sends a message to the topic.</p>
<p id="p17853809145027"><a name="p17853809145027"></a><a name="p17853809145027"></a>Type: String</p>
<p id="p26466559145027"><a name="p26466559145027"></a><a name="p26466559145027"></a>Ancestor: TopicConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.3 "><p id="p63416568145027"><a name="p63416568145027"></a><a name="p63416568145027"></a>Yes if ancestor TopicConfiguration is added</p>
</td>
</tr>
<tr id="row33878205145027"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p59780051145027"><a name="p59780051145027"></a><a name="p59780051145027"></a>Id</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.2 "><p id="p10345962145027"><a name="p10345962145027"></a><a name="p10345962145027"></a>Unique ID of each event notification. If the user does not specify an ID, the system assigns an ID automatically.</p>
<p id="p26004797145027"><a name="p26004797145027"></a><a name="p26004797145027"></a>Type: String</p>
<p id="p32716585145027"><a name="p32716585145027"></a><a name="p32716585145027"></a>Ancestor: TopicConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.3 "><p id="p32797753145027"><a name="p32797753145027"></a><a name="p32797753145027"></a>No</p>
</td>
</tr>
<tr id="row26744327145027"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p18806867145027"><a name="p18806867145027"></a><a name="p18806867145027"></a>Filter</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.2 "><p id="p46961219145027"><a name="p46961219145027"></a><a name="p46961219145027"></a>Container of S3Key used to store rules of filtering object names</p>
<p id="p19997788145027"><a name="p19997788145027"></a><a name="p19997788145027"></a>Type: Container</p>
<p id="p45762367145027"><a name="p45762367145027"></a><a name="p45762367145027"></a>Ancestor: TopicConfiguration</p>
<p id="p9208126145027"><a name="p9208126145027"></a><a name="p9208126145027"></a>Children: S3Key</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.3 "><p id="p7660728145027"><a name="p7660728145027"></a><a name="p7660728145027"></a>No</p>
</td>
</tr>
<tr id="row1837694145027"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p14635536145027"><a name="p14635536145027"></a><a name="p14635536145027"></a>S3Key</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.2 "><p id="p44627791145027"><a name="p44627791145027"></a><a name="p44627791145027"></a>Container that defines filtering rules. The rules filter objects based on the prefixes and suffixes of object names.</p>
<p id="p66105802145027"><a name="p66105802145027"></a><a name="p66105802145027"></a>Type: Container</p>
<p id="p58081314145027"><a name="p58081314145027"></a><a name="p58081314145027"></a>Ancestor: Filter</p>
<p id="p52969783145027"><a name="p52969783145027"></a><a name="p52969783145027"></a>Children: One FilterRule or FilterRules</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.3 "><p id="p62694020145027"><a name="p62694020145027"></a><a name="p62694020145027"></a>No</p>
</td>
</tr>
<tr id="row27375270145027"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p2804391145027"><a name="p2804391145027"></a><a name="p2804391145027"></a>FilterRule</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.2 "><p id="p25829084145027"><a name="p25829084145027"></a><a name="p25829084145027"></a>Container that defines key-value pairs of filtering rules</p>
<p id="p31135165145027"><a name="p31135165145027"></a><a name="p31135165145027"></a>Type: Container</p>
<p id="p11781037145027"><a name="p11781037145027"></a><a name="p11781037145027"></a>Ancestor: S3Key</p>
<p id="p38920476145027"><a name="p38920476145027"></a><a name="p38920476145027"></a>Children: Name, Value</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.3 "><p id="p65550884145027"><a name="p65550884145027"></a><a name="p65550884145027"></a>No</p>
</td>
</tr>
<tr id="row53087046145027"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p5083485145027"><a name="p5083485145027"></a><a name="p5083485145027"></a>Name</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.2 "><p id="p9109169145027"><a name="p9109169145027"></a><a name="p9109169145027"></a>Specifies the prefix or suffix of object names for filtering.</p>
<p id="p14873661145027"><a name="p14873661145027"></a><a name="p14873661145027"></a>Type: String</p>
<p id="p66754089145027"><a name="p66754089145027"></a><a name="p66754089145027"></a>Ancestor: FilterRule</p>
<p id="p63915894145027"><a name="p63915894145027"></a><a name="p63915894145027"></a>Legal value: prefix or suffix</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.3 "><p id="p9804960145027"><a name="p9804960145027"></a><a name="p9804960145027"></a>No</p>
</td>
</tr>
<tr id="row21135783145027"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p34276861145027"><a name="p34276861145027"></a><a name="p34276861145027"></a>Value</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.2 "><p id="p24962327145027"><a name="p24962327145027"></a><a name="p24962327145027"></a>Specifies keywords of object names so that objects can be filtered based on the prefixes or suffixes. The value contains a maximum of 1024 characters.</p>
<p id="p23334353145027"><a name="p23334353145027"></a><a name="p23334353145027"></a>Type: String</p>
<p id="p8682589145027"><a name="p8682589145027"></a><a name="p8682589145027"></a>Ancestor: FilterRule</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.3 "><p id="p32201145145027"><a name="p32201145145027"></a><a name="p32201145145027"></a>No</p>
</td>
</tr>
<tr id="row21374849145027"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p53641238145027"><a name="p53641238145027"></a><a name="p53641238145027"></a>Event</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.2 "><p id="p49973044145027"><a name="p49973044145027"></a><a name="p49973044145027"></a>Type of events that need to be notified</p>
<div class="note" id="note47104213145027"><a name="note47104213145027"></a><a name="note47104213145027"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p class="textintable" id="p21284738145027"><a name="p21284738145027"></a><a name="p21284738145027"></a>Multiple event types can be added in one TopicConfiguration configuration item.<em id="i57344914145027"><a name="i57344914145027"></a><a name="i57344914145027"></a></em></p>
</div></div>
<p id="p46342184145027"><a name="p46342184145027"></a><a name="p46342184145027"></a>Type: String</p>
<p id="p27693898145027"><a name="p27693898145027"></a><a name="p27693898145027"></a>Ancestor: TopicConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.2.4.1.3 "><p id="p28613269145027"><a name="p28613269145027"></a><a name="p28613269145027"></a>Yes if ancestor TopicConfiguration is added</p>
</td>
</tr>
</tbody>
</table>

## Response Syntax<a name="section5866353914519"></a>

```
HTTP/1.1 status_code 
x-amz-request-id: request id 
x-amz-id-2: id 
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
Date: date 
Content-Length: length 
```

## Response Headers<a name="section1737390614519"></a>

This response uses common headers. For details, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section4911114514519"></a>

This response involves no elements.

## Error Responses<a name="section3300087714519"></a>

When the user invokes the interface, the system checks whether the NotificationConfiguration element and the configuration are valid. The following table lists common errors and possible causes.

**Table  2**  Error codes and possible causes

<a name="table3266664814519"></a>
<table><thead align="left"><tr id="row4080837914519"><th class="cellrowborder" valign="top" width="22.45%" id="mcps1.2.4.1.1"><p id="p1714439414519"><a name="p1714439414519"></a><a name="p1714439414519"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="59.18%" id="mcps1.2.4.1.2"><p id="p4651869814519"><a name="p4651869814519"></a><a name="p4651869814519"></a>Possible Cause</p>
</th>
<th class="cellrowborder" valign="top" width="18.37%" id="mcps1.2.4.1.3"><p id="p991821114519"><a name="p991821114519"></a><a name="p991821114519"></a>HTTP Status Code</p>
</th>
</tr>
</thead>
<tbody><tr id="row6517759614519"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p4489388514519"><a name="p4489388514519"></a><a name="p4489388514519"></a>InvalidArgument</p>
</td>
<td class="cellrowborder" valign="top" width="59.18%" headers="mcps1.2.4.1.2 "><a name="ul1252606314519"></a><a name="ul1252606314519"></a><ul id="ul1252606314519"><li>Unsupported events were specified.</li><li>The specified URN does not exist or is incorrect.</li><li>The specified region in the URN is different as the region where the bucket resides.</li><li>The specified filtering rules overlap.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.3 "><p id="p6696658414519"><a name="p6696658414519"></a><a name="p6696658414519"></a>400 Bad Request</p>
</td>
</tr>
<tr id="row6582834414519"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p3049564314519"><a name="p3049564314519"></a><a name="p3049564314519"></a>AccessDenied</p>
</td>
<td class="cellrowborder" valign="top" width="59.18%" headers="mcps1.2.4.1.2 "><p id="p5422802714519"><a name="p5422802714519"></a><a name="p5422802714519"></a>The operator is not the bucket owner and not granted with the s3:PutBucketNotification permission.</p>
</td>
<td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.3 "><p id="p3039404714519"><a name="p3039404714519"></a><a name="p3039404714519"></a>403 Forbidden</p>
</td>
</tr>
</tbody>
</table>

## Sample Request<a name="section21401127145254"></a>

```
PUT /?notification HTTP/1.1 
User-Agent: curl/7.19.0 (x86_64-suse-linux-gnu) libcurl/7.19.0
OpenSSL/0.9.8{ zlib/1.2.3 libidn/1.10
Host: bucketname.obs.example.com 
Pragma: no-cache 
Accept: */*Date: Tue, 28 Apr 2015 08:56:07 +0000 
Authorization:AWS D13E0C94E722DD69423C:QhHpU6Amg/2r6wIYdU3RXIx7Tlc=
Content-Length: 468 [request body]
Expect: 100-continue
<NotificationConfiguration>
 <TopicConfiguration>
  <Id>Id001</Id>
  <Topic>urn:smn:example:35667523564:topic001</Topic>
  <Event>s3:ObjectCreated:*</Event>
  <Filter>
   <S3Key>
    <FilterRule>
     <Name>prefix</Name>
     <Value>smn/</Value>
    </FilterRule>
    <FilterRule>
     <Name>suffix</Name>
     <Value>.jpg</Value>
    </FilterRule>
   </S3Key>
  </Filter>
 </TopicConfiguration> 
</NotificationConfiguration>
```

## Sample Response<a name="section32165774145254"></a>

```
HTTP/1.1 200 OK 
x-amz-request-id: C2D2F581B3C5AF6C6698322AB56836F6 
x-amz-id-2: lDGZAj4h+A33eYauDCTsPvFSHzBXEtZon6Eg1idIZl18/2/odotyqJUJ/lTh80uA
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
Content-Type: text/xml 
Date: Tue, 28 Apr 2015 08:56:07 GMT 
Content-Length: 0
```

