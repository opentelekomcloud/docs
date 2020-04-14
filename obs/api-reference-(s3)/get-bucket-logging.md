# GET Bucket logging<a name="EN-US_TOPIC_0125560463"></a>

You can use this operation to query the logging status of a bucket. This GET operation uses the  **logging**  subresource to return the logging status of a bucket.

Only the bucket owner or users granted the  **s3:GetBucketLogging**  permission can query the bucket logging status.

## Request Syntax<a name="section26394946"></a>

```
GET /?logging HTTP/1.1 
 User-Agent: agent
 Host: bucketname.obs.example.com
 Accept: */* 
 Date: date 
 Authorization: authorization
```

## Request Parameters<a name="section36227930"></a>

This request involves no parameters.

## Request Headers<a name="section57615916"></a>

This request uses common headers. For details about common request headers, see section  [Common Request Headers](common-request-headers.md).

## Request Elements<a name="section48781203"></a>

This request involves no elements.

## Response Syntax<a name="section7008729"></a>

```
HTTP/1.1 status_code 
 Server: Server Name
 x-amz-request-id: request id
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
 x-amz-id-2: id
 Content-Type: type
 Date: date
 Content-Length:length

 <?xml version="1.0" encoding="UTF-8"?> 
 <BucketLoggingStatus xmlns="http://obs.example.com/doc/2006-03-01/">
 <LoggingEnabled> 
 <TargetBucket>bucketName</TargetBucket> 
 <TargetPrefix>prefix</TargetPrefix> 
 <TargetGrants> 
 <Grant> 
 <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser"> 
 <ID>id</ID> 
 <DisplayName>displayName</DisplayName> 
 </Grantee> 
 <Permission>permission</Permission> 
 </Grant> 
 </TargetGrants> 
 </LoggingEnabled> 
 </BucketLoggingStatus>
```

## Response Headers<a name="section63078563"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response Elements<a name="section30836156"></a>

This response contains elements to specify the bucket logging status.  [Table 1](#table56643352)  describes the elements.

**Table  1**  Response elements

<a name="table56643352"></a>
<table><thead align="left"><tr id="row24846201"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p66385258"><a name="p66385258"></a><a name="p66385258"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p8496783"><a name="p8496783"></a><a name="p8496783"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p17150800"><a name="p17150800"></a><a name="p17150800"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row47037591"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p51948489"><a name="p51948489"></a><a name="p51948489"></a>BucketLoggingStatus</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p47078096"><a name="p47078096"></a><a name="p47078096"></a>Indicates the container for logging status information.</p>
<p id="p21049687"><a name="p21049687"></a><a name="p21049687"></a>Type: Container</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p27303096"><a name="p27303096"></a><a name="p27303096"></a>Mandatory</p>
</td>
</tr>
<tr id="row44401276"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p39733617"><a name="p39733617"></a><a name="p39733617"></a>LoggingEnabled</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p64306394"><a name="p64306394"></a><a name="p64306394"></a>Indicates the container for logging information. This element is present when you are enabling logging (and not present when you are disabling logging).</p>
<p id="p41886638"><a name="p41886638"></a><a name="p41886638"></a>Type: Container</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p37374497"><a name="p37374497"></a><a name="p37374497"></a>Optional</p>
</td>
</tr>
<tr id="row826154"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p66918496"><a name="p66918496"></a><a name="p66918496"></a>Grant</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p51689132"><a name="p51689132"></a><a name="p51689132"></a>Indicates the container for the grantee and the grantee's logging permission.</p>
<p id="p62549004"><a name="p62549004"></a><a name="p62549004"></a>Type: Container</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p33304593"><a name="p33304593"></a><a name="p33304593"></a>Optional</p>
</td>
</tr>
<tr id="row31305887"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p52748952"><a name="p52748952"></a><a name="p52748952"></a>Grantee</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p44806725"><a name="p44806725"></a><a name="p44806725"></a>Indicates the container for users granted logging permission.</p>
<p id="p607347"><a name="p607347"></a><a name="p607347"></a>Type: Container</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p49195146"><a name="p49195146"></a><a name="p49195146"></a>Optional</p>
</td>
</tr>
<tr id="row40103133"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p27128344"><a name="p27128344"></a><a name="p27128344"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p49912231"><a name="p49912231"></a><a name="p49912231"></a>DomainId of the grantee, Indicates the globally unique ID.</p>
<p id="p46556898"><a name="p46556898"></a><a name="p46556898"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p13012363"><a name="p13012363"></a><a name="p13012363"></a>Optional</p>
</td>
</tr>
<tr id="row50002403"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p23662815"><a name="p23662815"></a><a name="p23662815"></a>DisplayName</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p37639888"><a name="p37639888"></a><a name="p37639888"></a>Indicates the name of the grantee. This element is not globally unique but a user ID corresponds to only one name.</p>
<p id="p3214680"><a name="p3214680"></a><a name="p3214680"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p59062547"><a name="p59062547"></a><a name="p59062547"></a>Optional</p>
</td>
</tr>
<tr id="row61800880"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p39815407"><a name="p39815407"></a><a name="p39815407"></a>Permission</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3822530"><a name="p3822530"></a><a name="p3822530"></a>Indicates the logging permission granted to the grantee for a bucket. The bucket owner is automatically granted the <strong id="b17279181819116"><a name="b17279181819116"></a><a name="b17279181819116"></a>FULL_CONTROL</strong> permission when creating the bucket. Logging permission control access to different logs.</p>
<p id="p41189522"><a name="p41189522"></a><a name="p41189522"></a>Type: String</p>
<p id="p35161380"><a name="p35161380"></a><a name="p35161380"></a>Valid Values: FULL_CONTROL | READ | WRITE</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p29499513"><a name="p29499513"></a><a name="p29499513"></a>Optional</p>
</td>
</tr>
<tr id="row64169031"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p30308988"><a name="p30308988"></a><a name="p30308988"></a>TargetBucket</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p39108941"><a name="p39108941"></a><a name="p39108941"></a>Specifies the target bucket where bucket logs are stored. In OBS, logs of multiple buckets can be stored in the same target bucket. In this case, you need to use different <strong id="b16436156"><a name="b16436156"></a><a name="b16436156"></a>TargetPrefix</strong> to distinguish the logs.</p>
<p id="p13707684"><a name="p13707684"></a><a name="p13707684"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p36580582"><a name="p36580582"></a><a name="p36580582"></a>Optional</p>
</td>
</tr>
<tr id="row60789788"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p25025772"><a name="p25025772"></a><a name="p25025772"></a>TargetPrefix</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p13821661"><a name="p13821661"></a><a name="p13821661"></a>Specifies a prefix for keys of logs to be stored.</p>
<p id="p57286089"><a name="p57286089"></a><a name="p57286089"></a>Type: String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p9661646"><a name="p9661646"></a><a name="p9661646"></a>Optional</p>
</td>
</tr>
<tr id="row19845952"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p64018307"><a name="p64018307"></a><a name="p64018307"></a>TargetGrants</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p18100358"><a name="p18100358"></a><a name="p18100358"></a>Indicates the container for granting information.</p>
<p id="p28685495"><a name="p28685495"></a><a name="p28685495"></a>Type: Container</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p41823741"><a name="p41823741"></a><a name="p41823741"></a>Optional</p>
</td>
</tr>
</tbody>
</table>

## Error Responses<a name="section9089949"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request<a name="section4666767"></a>

```
GET /?logging HTTP/1.1 
 User-Agent: curl/7.19.0
 Host: bucketname.obs.example.com
 Accept: */*
 Date: Wed, 25 Nov 2009 12:00:00 GMT 
 Authorization: AWS UDSIAMSTUBTEST000002:IuWiXuyanEXDOKUMdUnyZ2J83sA=
```

## Sample Response<a name="section42000908"></a>

```
HTTP/1.1 200 OK 
 Server: OBS
 x-amz-request-id: 0000016594648286822DDF9487214C88
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
 x-amz-id-2: 32AAAQAAEAABAAAQAAEAABAAAQAAEAABCSWVP7N5CZQGJzkZXBosuFJjC7XFsYQq
 Date: Wed, 25 Nov 2009 12:00:00 GMT 
 Content_Length:277

 <?xml version="1.0" encoding="UTF-8"?> 
 <BucketLoggingStatus xmlns="http://obs.example.com/doc/2006-03-01/">
 <LoggingEnabled> 
 <TargetBucket>logging.bucket1</TargetBucket> 
 <TargetPrefix>access_log</TargetPrefix> 
 <TargetGrants> 
 <Grant> 
 <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser"> 
 <ID>af258a3a0a1c2cd93011f75c1e031c043f47a25048490c8742f2f942464794e0</ID> 
 <DisplayName>user</DisplayName> 
 </Grantee> 
 <Permission>FULL_CONTROL</Permission> 
 </Grant> 
 </TargetGrants> 
 </LoggingEnabled> 
 </BucketLoggingStatus>
```

