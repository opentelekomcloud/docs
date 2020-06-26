# GET Bucket lifecycle<a name="EN-US_TOPIC_0125560497"></a>

You can use this operation to get the bucket lifecycle configuration.

Only users granted the  **s3:GetLifecycleConfiguration**  permission can view the bucket lifecycle configuration. By default, only the bucket owner can get the bucket lifecycle configuration. The bucket owner can allow other users to get the bucket lifecycle configuration by granting them the permission.

## Request Syntax<a name="section52483186"></a>

```
GET /?lifecycle HTTP/1.1
User-Agent: agnet
 Host: bucketname.obs.example.com
Accept: */*
Date: date
 Authorization: authorization
```

## Request Parameters<a name="section2586631"></a>

This request involves no parameters.

## Request Headers<a name="section23279683"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section8190559"></a>

This request involves no elements.

## Response Syntax<a name="section59061958"></a>

```
HTTP/1.1 200 OK
Server: Server Name
x-amz-request-id: 90E2BA0A420C00000140ED9939AF099E
x-amz-id-2: UHQoAKndcsk628TszydX75G/Q2+I5MwYJ3IJYqzEkNInMkBMn96hunAVsoiMCHZh
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
Content-Type: application/xml
Date: Thu, 05 Sep 2015 10:09:36 GMT
Content-Length: 425

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<LifecycleConfiguration xmlns="http://obs.example.com/doc/2015-06-30/">
<Rule>
<ID>id</ID>
<Prefix>prefix</Prefix>
<Status>status</Status>
<Expiration>
<Date>date</Date>
</Expiration>
<NoncurrentVersionExpiration>
<NoncurrentDays>365</NoncurrentDays>
</NoncurrentVersionExpiration>
<Transition> 
<Date>date</Date> 
<StorageClass>STANDARD_IA</StorageClass> 
</Transition> 
<Transition> 
<Date>date</Date> 
<StorageClass>GLACIER</StorageClass> 
</Transition> 
<NoncurrentVersionTransition> 
<NoncurrentDays>30</NoncurrentDays> 
<StorageClass>STANDARD_IA</StorageClass> 
</NoncurrentVersionTransition> 
<NoncurrentVersionTransition> 
<NoncurrentDays>60</NoncurrentDays> 
<StorageClass>GLACIER</StorageClass> 
</NoncurrentVersionTransition>
</Rule>
</LifecycleConfiguration>
```

## Response Headers<a name="section61795582"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section19289328"></a>

This response contains elements to detail bucket lifecycle configuration.  [Table 1](#table28619802)  describes the elements.

**Table  1**  Response elements for lifecycle configuration

<a name="table28619802"></a>
<table><thead align="left"><tr id="row6648223"><th class="cellrowborder" valign="top" width="27.43%" id="mcps1.2.3.1.1"><p id="p1635228"><a name="p1635228"></a><a name="p1635228"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="72.57000000000001%" id="mcps1.2.3.1.2"><p id="p65344633"><a name="p65344633"></a><a name="p65344633"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row58423902"><td class="cellrowborder" valign="top" width="27.43%" headers="mcps1.2.3.1.1 "><p id="p34715636"><a name="p34715636"></a><a name="p34715636"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="72.57000000000001%" headers="mcps1.2.3.1.2 "><p id="p60503138"><a name="p60503138"></a><a name="p60503138"></a>Indicates when the specified rule takes effect.</p>
<p id="p7657338"><a name="p7657338"></a><a name="p7657338"></a>The date value must conform to ISO 8601 format. The time is always midnight UTC.</p>
<p id="p1807185"><a name="p1807185"></a><a name="p1807185"></a>Type: String</p>
<p id="p16264673"><a name="p16264673"></a><a name="p16264673"></a>Ancestor: Expiration, Transition</p>
</td>
</tr>
<tr id="row12164329"><td class="cellrowborder" valign="top" width="27.43%" headers="mcps1.2.3.1.1 "><p id="p45786577"><a name="p45786577"></a><a name="p45786577"></a>Days</p>
</td>
<td class="cellrowborder" valign="top" width="72.57000000000001%" headers="mcps1.2.3.1.2 "><p id="p17725233"><a name="p17725233"></a><a name="p17725233"></a>Indicates the number of days after object creation when the specified rule takes effect.</p>
<p id="p25309374"><a name="p25309374"></a><a name="p25309374"></a>Type: Positive integer</p>
<p id="p26457778"><a name="p26457778"></a><a name="p26457778"></a>Ancestor: Expiration, Transition</p>
</td>
</tr>
<tr id="row12445183271813"><td class="cellrowborder" valign="top" width="27.43%" headers="mcps1.2.3.1.1 "><p id="p1559772016109"><a name="p1559772016109"></a><a name="p1559772016109"></a>StorageClass</p>
</td>
<td class="cellrowborder" valign="top" width="72.57000000000001%" headers="mcps1.2.3.1.2 "><p id="p1771716481439"><a name="p1771716481439"></a><a name="p1771716481439"></a>Indicates the new storage class of the object.</p>
<p id="p2071734816320"><a name="p2071734816320"></a><a name="p2071734816320"></a>Type: <strong id="b6718848032"><a name="b6718848032"></a><a name="b6718848032"></a>STANDARD_IA</strong> or <strong id="b107181548930"><a name="b107181548930"></a><a name="b107181548930"></a>GLACIER</strong></p>
<p id="p271864812316"><a name="p271864812316"></a><a name="p271864812316"></a>Ancestor: <strong id="b1171814816316"><a name="b1171814816316"></a><a name="b1171814816316"></a>Transition, NoncurrentVersionTransition</strong></p>
</td>
</tr>
<tr id="row96191830111812"><td class="cellrowborder" valign="top" width="27.43%" headers="mcps1.2.3.1.1 "><p id="p39863719110"><a name="p39863719110"></a><a name="p39863719110"></a>Transition</p>
</td>
<td class="cellrowborder" valign="top" width="72.57000000000001%" headers="mcps1.2.3.1.2 "><p id="p18718948338"><a name="p18718948338"></a><a name="p18718948338"></a>Indicates the element of the transition time and new storage class (applicable to the latest version of the object) in the lifecycle configuration.</p>
<p id="p371811481310"><a name="p371811481310"></a><a name="p371811481310"></a>Type: XML</p>
<p id="p1371874813317"><a name="p1371874813317"></a><a name="p1371874813317"></a>Children: <strong id="b7718448831"><a name="b7718448831"></a><a name="b7718448831"></a>Date</strong> or <strong id="b3718174813318"><a name="b3718174813318"></a><a name="b3718174813318"></a>Days</strong></p>
<p id="p171812481331"><a name="p171812481331"></a><a name="p171812481331"></a>Ancestor: <strong id="b47185482317"><a name="b47185482317"></a><a name="b47185482317"></a>Rule</strong></p>
</td>
</tr>
<tr id="row36793414"><td class="cellrowborder" valign="top" width="27.43%" headers="mcps1.2.3.1.1 "><p id="p27476571"><a name="p27476571"></a><a name="p27476571"></a>Expiration</p>
</td>
<td class="cellrowborder" valign="top" width="72.57000000000001%" headers="mcps1.2.3.1.2 "><p id="p11009764"><a name="p11009764"></a><a name="p11009764"></a>Indicates the container for the object expiration rule.</p>
<p id="p31979016"><a name="p31979016"></a><a name="p31979016"></a>Type: XML</p>
<p id="p19375690"><a name="p19375690"></a><a name="p19375690"></a>Children: Date or Days</p>
<p id="p40163483"><a name="p40163483"></a><a name="p40163483"></a>Ancestor: Rule</p>
</td>
</tr>
<tr id="row25927028"><td class="cellrowborder" valign="top" width="27.43%" headers="mcps1.2.3.1.1 "><p id="p19714506"><a name="p19714506"></a><a name="p19714506"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="72.57000000000001%" headers="mcps1.2.3.1.2 "><p id="p53371190"><a name="p53371190"></a><a name="p53371190"></a>Indicates the unique identifier of a rule. The value can contain a maximum of 255 characters.</p>
<p id="p10578662"><a name="p10578662"></a><a name="p10578662"></a>Type: String</p>
<p id="p28099101"><a name="p28099101"></a><a name="p28099101"></a>Ancestor: Rule</p>
</td>
</tr>
<tr id="row51565323"><td class="cellrowborder" valign="top" width="27.43%" headers="mcps1.2.3.1.1 "><p id="p16041657"><a name="p16041657"></a><a name="p16041657"></a>LifecycleConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="72.57000000000001%" headers="mcps1.2.3.1.2 "><p id="p24305815"><a name="p24305815"></a><a name="p24305815"></a>Indicates the container for lifecycle rules. You can add multiple rules. The total size of the rules cannot exceed 20 KB.</p>
<p id="p17425743"><a name="p17425743"></a><a name="p17425743"></a>Type: XML</p>
<p id="p22613965"><a name="p22613965"></a><a name="p22613965"></a>Children: Rule</p>
<p id="p2199097"><a name="p2199097"></a><a name="p2199097"></a>Ancestor: None</p>
</td>
</tr>
<tr id="row58895873173852"><td class="cellrowborder" valign="top" width="27.43%" headers="mcps1.2.3.1.1 "><p id="p5836421173852"><a name="p5836421173852"></a><a name="p5836421173852"></a>NoncurrentDays</p>
</td>
<td class="cellrowborder" valign="top" width="72.57000000000001%" headers="mcps1.2.3.1.2 "><p id="p1780571618050"><a name="p1780571618050"></a><a name="p1780571618050"></a>Indicates the number of days after object is noncurrent when the specified rule takes effect.</p>
<p id="p1687068218050"><a name="p1687068218050"></a><a name="p1687068218050"></a>Type: Positive integer</p>
<p id="p1178684417544"><a name="p1178684417544"></a><a name="p1178684417544"></a>Ancestor: NoncurrentVersionExpiration, NoncurrentVersionTransition</p>
</td>
</tr>
<tr id="row157415549188"><td class="cellrowborder" valign="top" width="27.43%" headers="mcps1.2.3.1.1 "><p id="p1532415515136"><a name="p1532415515136"></a><a name="p1532415515136"></a>NoncurrentVersionTransition</p>
</td>
<td class="cellrowborder" valign="top" width="72.57000000000001%" headers="mcps1.2.3.1.2 "><p id="p6653003413"><a name="p6653003413"></a><a name="p6653003413"></a>Indicates the element of the transition time and new storage class (applicable to historical versions) in the lifecycle configuration.</p>
<p id="p6653001543"><a name="p6653001543"></a><a name="p6653001543"></a>Type: XML</p>
<p id="p7653501449"><a name="p7653501449"></a><a name="p7653501449"></a>Children: NoncurrentDays, StorageClass</p>
<p id="p565310049"><a name="p565310049"></a><a name="p565310049"></a>Ancestor: Rule</p>
</td>
</tr>
<tr id="row36811052185022"><td class="cellrowborder" valign="top" width="27.43%" headers="mcps1.2.3.1.1 "><p id="p28905267185022"><a name="p28905267185022"></a><a name="p28905267185022"></a>NoncurrentVersionExpiration</p>
</td>
<td class="cellrowborder" valign="top" width="72.57000000000001%" headers="mcps1.2.3.1.2 "><p id="p411104918235"><a name="p411104918235"></a><a name="p411104918235"></a>Indicates the container for the noncurrent object expiration rule. You set this lifecycle configuration action on a bucket that has versioning enabled (or suspended) to request that OBS delete noncurrent object versions which meet the expiration rule.</p>
<p id="p35167743115110"><a name="p35167743115110"></a><a name="p35167743115110"></a>Type: XML</p>
<p id="p48074236115110"><a name="p48074236115110"></a><a name="p48074236115110"></a>Children: NoncurrentDays</p>
<p id="p30014947115110"><a name="p30014947115110"></a><a name="p30014947115110"></a>Ancestor: Rule</p>
</td>
</tr>
<tr id="row19791876"><td class="cellrowborder" valign="top" width="27.43%" headers="mcps1.2.3.1.1 "><p id="p59638115"><a name="p59638115"></a><a name="p59638115"></a>Prefix</p>
</td>
<td class="cellrowborder" valign="top" width="72.57000000000001%" headers="mcps1.2.3.1.2 "><p id="p65958035"><a name="p65958035"></a><a name="p65958035"></a>Indicates the object key prefix identifying one or more objects to which the rule applies.</p>
<p id="p56751409"><a name="p56751409"></a><a name="p56751409"></a>Type: String</p>
<p id="p41000636"><a name="p41000636"></a><a name="p41000636"></a>Ancestor: Rule</p>
</td>
</tr>
<tr id="row33461405"><td class="cellrowborder" valign="top" width="27.43%" headers="mcps1.2.3.1.1 "><p id="p26019245"><a name="p26019245"></a><a name="p26019245"></a>Rule</p>
</td>
<td class="cellrowborder" valign="top" width="72.57000000000001%" headers="mcps1.2.3.1.2 "><p id="p27184073"><a name="p27184073"></a><a name="p27184073"></a>Indicates the container for lifecycle rules.</p>
<p id="p43330072"><a name="p43330072"></a><a name="p43330072"></a>Type: Container</p>
<p id="p54426330"><a name="p54426330"></a><a name="p54426330"></a>Ancestor: LifecycleConfiguration</p>
</td>
</tr>
<tr id="row20074930"><td class="cellrowborder" valign="top" width="27.43%" headers="mcps1.2.3.1.1 "><p id="p15456653"><a name="p15456653"></a><a name="p15456653"></a>Status</p>
</td>
<td class="cellrowborder" valign="top" width="72.57000000000001%" headers="mcps1.2.3.1.2 "><p id="p44029393"><a name="p44029393"></a><a name="p44029393"></a>Indicates whether the rule is enabled.</p>
<p id="p60720217"><a name="p60720217"></a><a name="p60720217"></a>Type: String</p>
<p id="p9611044"><a name="p9611044"></a><a name="p9611044"></a>Ancestor: Rule</p>
<p id="p19390540"><a name="p19390540"></a><a name="p19390540"></a>Valid Values: Enabled, Disabled</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section39386231"></a>

This response contains common errors. For details, see  [Table 1](error-codes.md#table30733758). In addition, this response contains one special error, as described in [Table 2](#table56251627).

**Table  2**  Special error

<a name="table56251627"></a>
<table><thead align="left"><tr id="row28630766"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p37390672"><a name="p37390672"></a><a name="p37390672"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p8745607"><a name="p8745607"></a><a name="p8745607"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p37305595"><a name="p37305595"></a><a name="p37305595"></a>HTTP Status Code</p>
</th>
</tr>
</thead>
<tbody><tr id="row1854355"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15985080"><a name="p15985080"></a><a name="p15985080"></a>NoSuchLifecycleConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p19723089"><a name="p19723089"></a><a name="p19723089"></a>Indicates that the bucket lifecycle configuration does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p54066375"><a name="p54066375"></a><a name="p54066375"></a>404 Not Found</p>
</td>
</tr>
</tbody>
</table>

## Sample Request<a name="section34097968"></a>

```
GET /?lifecycle HTTP/1.1
User-Agent: curl/7.29.0 
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Thu, 05 Sep 2013 10:09:36 +0000 
 Authorization: AWS B9A70C60A39C4D551A16:oNFuFZV8JLUqxsaFPI1Gs/HPRKg=
```

## Sample Response<a name="section38446258"></a>

```
HTTP/1.1 200 OK
Server: OBS
x-amz-request-id: 90E2BA0A420C00000140ED9939AF099E
x-amz-id-2: UHQoAKndcsk628TszydX75G/Q2+I5MwYJ3IJYqzEkNInMkBMn96hunAVsoiMCHZh
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
Content-Type: application/xml
Date: Thu, 05 Sep 2015 10:09:36 GMT
Content-Length: 425

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<LifecycleConfiguration xmlns="http://obs.example.com/doc/2015-06-30/">
<Rule>
<ID>delete-test/-1-day</ID>
<Prefix>test/</Prefix>
<Status>Enabled</Status>
<Expiration>
<Date>2015-07-12T00:00:00.000Z</Date>
</Expiration>
<NoncurrentVersionExpiration>
<NoncurrentDays>365</NoncurrentDays>
</NoncurrentVersionExpiration>
<Transition> 
<Date>2015-07-10T00:00:00.000Z</Date> 
<StorageClass>STANDARD_IA</StorageClass> 
</Transition> 
<Transition> 
<Date>2015-07-11T00:00:00.000Z</Date> 
<StorageClass>GLACIER</StorageClass> 
</Transition> 
<NoncurrentVersionTransition> 
<NoncurrentDays>30</NoncurrentDays> 
<StorageClass>STANDARD_IA</StorageClass> 
</NoncurrentVersionTransition> 
<NoncurrentVersionTransition> 
<NoncurrentDays>60</NoncurrentDays> 
<StorageClass>GLACIER</StorageClass> 
</NoncurrentVersionTransition>
</Rule>
</LifecycleConfiguration>
```

