# PUT Bucket lifecycle<a name="EN-US_TOPIC_0125560423"></a>

OBS supports periodic transition and deletion of objects in a bucket based on a specified rule. This is implemented in lifecycle configuration. After the bucket lifecycle is set, OBS automatically deletes objects at the time specified in this operation. This operation can be used to delete:

-   Periodically uploaded files: Some periodically uploaded files need to be retained for only one week or one month.
-   Documents that are seldom accessed after a certain period of time. These documents may be archived for another period of time and be deleted then.
-   The minimum time for the transition of the bucket storage to Warm or to Cold can be configured. The value ranges from   **24** to **8640**.

This operation is used to create or update the lifecycle configuration of a bucket.

Only users granted the  **s3:PutLifecycleConfiguration**  permission can create or update the bucket lifecycle configuration. By default, only the bucket owner can set the bucket lifecycle configuration. The bucket owner can allow other users to set the bucket lifecycle configuration by granting them the permission.

The lifecycle configuration supports periodic deletion and transition of objects. If you want to prevent a user from deleting and transitioning objects, disable the following permissions:

-   s3:DeleteObject
-   s3:DeleteObjectVersion
-   s3:PutLifecycleConfiguration

If you want to prevent a user configuring a bucket lifecycle, revoke the  **s3:PutLifecycleConfiguration**  permission from the user.

## Request Syntax<a name="section66482253"></a>

```
PUT /?lifecycle HTTP/1.1
User-Agent: user-agent
Host: bucketname.obs.example.com
Content-Length: length
Date: date
Authorization: authorization
Content-MD5: MD5
Expect: expect

<?xml version="1.0" encoding="UTF-8"?>
<LifecycleConfiguration>
 <Rule>
  <ID>id</ID>
  <Prefix>prefix</Prefix>
  <Status>status</Status>
  <Expiration>
   <Days>365</Days>
  </Expiration>
  <NoncurrentVersionExpiration>
   <NoncurrentDays>365</NoncurrentDays>
  </NoncurrentVersionExpiration>
  <Transition> 
   <Days>30</Days> 
   <StorageClass>STANDARD_IA</StorageClass> 
  </Transition> 
  <Transition> 
   <Days>60</Days> 
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

## Request Parameters<a name="section61469371"></a>

This request involves no parameters.

## Request Headers<a name="section16353430"></a>

The request uses one header, as described in  [Table 1](#table16725372).

**Table  1**  Request header

<a name="table16725372"></a>
<table><thead align="left"><tr id="row2055005"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p32237730"><a name="p32237730"></a><a name="p32237730"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p61119323"><a name="p61119323"></a><a name="p61119323"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p51718129"><a name="p51718129"></a><a name="p51718129"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row28418891"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p20228817"><a name="p20228817"></a><a name="p20228817"></a>Content-MD5</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p27921517"><a name="p27921517"></a><a name="p27921517"></a>The MD5 digest string of the message body is calculated according to the RFC 1864 standard. That is, calculate the 128-bit binary array (the message header data encrypted with MD5) first, and then use Base 64 encoding to convert the binary data to a character string.</p>
<p id="p49967061"><a name="p49967061"></a><a name="p49967061"></a>Type: String</p>
<p id="p47050372"><a name="p47050372"></a><a name="p47050372"></a>Example: n58IG6hfM7vqI4K0vnWpog==</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p52983808"><a name="p52983808"></a><a name="p52983808"></a>Mandatory</p>
</td>
</tr>
<tr id="row45891858237"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p862519620235"><a name="p862519620235"></a><a name="p862519620235"></a>x-amz-security-token</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3625168237"><a name="p3625168237"></a><a name="p3625168237"></a>Header field used to identify the request of a federated user. When the federal authentication function is enabled, users sending such requests are identified as federated users.</p>
<p id="p10625268232"><a name="p10625268232"></a><a name="p10625268232"></a>Type: string</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p9625186202320"><a name="p9625186202320"></a><a name="p9625186202320"></a>Optional. This parameter must be carried in the request sent by federated users.</p>
</td>
</tr>
</tbody>
</table>

## Request Elements<a name="section12963143"></a>

In this request, you need to specify the lifecycle configuration in the request body using the elements described in  [Table 2](#table26371793).

**Table  2**  Request elements for lifecycle configuration

<a name="table26371793"></a>
<table><thead align="left"><tr id="row175293"><th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.1"><p id="p14198754"><a name="p14198754"></a><a name="p14198754"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.2"><p id="p9248440"><a name="p9248440"></a><a name="p9248440"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.3"><p id="p10926182"><a name="p10926182"></a><a name="p10926182"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row12605589"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p14419821"><a name="p14419821"></a><a name="p14419821"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p26479335418"><a name="p26479335418"></a><a name="p26479335418"></a>Indicates when the specified rule takes effect (applicable to the latest object version).</p>
<p id="p43066942"><a name="p43066942"></a><a name="p43066942"></a>The date value must conform to ISO 8601 format. The time is always midnight UTC.</p>
<p id="p52058165"><a name="p52058165"></a><a name="p52058165"></a>Type: String</p>
<p id="p65870306"><a name="p65870306"></a><a name="p65870306"></a>Ancestor: Expiration, Transition</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p33894570"><a name="p33894570"></a><a name="p33894570"></a>Mandatory if the <strong id="b2295423126"><a name="b2295423126"></a><a name="b2295423126"></a>Days</strong> parameter is absent.</p>
</td>
</tr>
<tr id="row61105663"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p50611656"><a name="p50611656"></a><a name="p50611656"></a>Days</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p5903470"><a name="p5903470"></a><a name="p5903470"></a>Indicates the number of days after object creation when the specified rule takes effect.</p>
<p id="p53131231"><a name="p53131231"></a><a name="p53131231"></a>Type: Positive integer</p>
<p id="p8419032"><a name="p8419032"></a><a name="p8419032"></a>Ancestor: Expiration, Transition</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p10852974"><a name="p10852974"></a><a name="p10852974"></a>Mandatory if the <strong id="b528416411634"><a name="b528416411634"></a><a name="b528416411634"></a>Date</strong> parameter is absent.</p>
</td>
</tr>
<tr id="row109861831211"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1273253835015"><a name="p1273253835015"></a><a name="p1273253835015"></a>StorageClass</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p128511633219"><a name="p128511633219"></a><a name="p128511633219"></a>Indicates the new storage class of the object.</p>
<p id="p7851103314118"><a name="p7851103314118"></a><a name="p7851103314118"></a>Type: <strong id="b98516331414"><a name="b98516331414"></a><a name="b98516331414"></a>STANDARD_IA</strong> or <strong id="b785115331216"><a name="b785115331216"></a><a name="b785115331216"></a>GLACIER</strong></p>
<p id="p138515331111"><a name="p138515331111"></a><a name="p138515331111"></a>Ancestor: <strong id="b2085123316117"><a name="b2085123316117"></a><a name="b2085123316117"></a>Transition, NoncurrentVersionTransition</strong></p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p1485113336115"><a name="p1485113336115"></a><a name="p1485113336115"></a>Mandatory if <strong id="b168511333212"><a name="b168511333212"></a><a name="b168511333212"></a>Transition</strong> or <strong id="b1885103312112"><a name="b1885103312112"></a><a name="b1885103312112"></a>NoncurrentVersionTransition</strong> is present.</p>
</td>
</tr>
<tr id="row1445819212128"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p128181506518"><a name="p128181506518"></a><a name="p128181506518"></a>Transition</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p194647501519"><a name="p194647501519"></a><a name="p194647501519"></a>Indicates the element of the transition time and new storage class (applicable to the latest version of the object) in the lifecycle configuration.</p>
<p id="p94640503114"><a name="p94640503114"></a><a name="p94640503114"></a>Type: XML</p>
<p id="p846465011119"><a name="p846465011119"></a><a name="p846465011119"></a>Children: Date or Days, StorageClass</p>
<p id="p11464350317"><a name="p11464350317"></a><a name="p11464350317"></a>Ancestor: Rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p1946417501118"><a name="p1946417501118"></a><a name="p1946417501118"></a>Mandatory if <strong id="b546413501214"><a name="b546413501214"></a><a name="b546413501214"></a>NoncurrentVersionTransition</strong>, <strong id="b11464175010117"><a name="b11464175010117"></a><a name="b11464175010117"></a>Expiration</strong>, and <strong id="b24649501917"><a name="b24649501917"></a><a name="b24649501917"></a>NoncurrentVersionExpiration</strong> are absent.</p>
</td>
</tr>
<tr id="row6675738"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p3863873"><a name="p3863873"></a><a name="p3863873"></a>Expiration</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p44538317"><a name="p44538317"></a><a name="p44538317"></a>Indicates the container for the object expiration rule.</p>
<p id="p65300541"><a name="p65300541"></a><a name="p65300541"></a>Type: XML</p>
<p id="p50833958"><a name="p50833958"></a><a name="p50833958"></a>Children: Date or Days</p>
<p id="p54852443"><a name="p54852443"></a><a name="p54852443"></a>Ancestor: Rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p13862865"><a name="p13862865"></a><a name="p13862865"></a>Mandatory if <strong id="b3757191629"><a name="b3757191629"></a><a name="b3757191629"></a>Transition</strong>, <strong id="b137571918213"><a name="b137571918213"></a><a name="b137571918213"></a>NoncurrentVersionTransition</strong>, and <strong id="b157574110216"><a name="b157574110216"></a><a name="b157574110216"></a>NoncurrentVersionExpiration</strong> are absent.</p>
</td>
</tr>
<tr id="row57656925"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p39699339"><a name="p39699339"></a><a name="p39699339"></a>ID</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p61529894"><a name="p61529894"></a><a name="p61529894"></a>Indicates the unique identifier of a rule. The value can contain a maximum of 255 characters.</p>
<p id="p16898135"><a name="p16898135"></a><a name="p16898135"></a>Type: String</p>
<p id="p17865493"><a name="p17865493"></a><a name="p17865493"></a>Ancestor: Rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p37818817"><a name="p37818817"></a><a name="p37818817"></a>Optional</p>
</td>
</tr>
<tr id="row4825033"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p55283354"><a name="p55283354"></a><a name="p55283354"></a>LifecycleConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p48766684"><a name="p48766684"></a><a name="p48766684"></a>Indicates the container for lifecycle rules. You can add multiple rules. The total size of the rules cannot exceed 20 KB.</p>
<p id="p36246974"><a name="p36246974"></a><a name="p36246974"></a>Type: XML</p>
<p id="p57787318"><a name="p57787318"></a><a name="p57787318"></a>Children: Rule</p>
<p id="p50323820"><a name="p50323820"></a><a name="p50323820"></a>Ancestor: None</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p49697630"><a name="p49697630"></a><a name="p49697630"></a>Mandatory</p>
</td>
</tr>
<tr id="row15752738173915"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p903368173915"><a name="p903368173915"></a><a name="p903368173915"></a>NoncurrentDays</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p1780571618050"><a name="p1780571618050"></a><a name="p1780571618050"></a>Indicates the number of days after object is noncurrent when the specified rule takes effect.</p>
<p id="p1687068218050"><a name="p1687068218050"></a><a name="p1687068218050"></a>Type: Positive integer</p>
<p id="p1178684417544"><a name="p1178684417544"></a><a name="p1178684417544"></a>Ancestor: NoncurrentVersionExpiration, NoncurrentVersionTransition</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p21420606173915"><a name="p21420606173915"></a><a name="p21420606173915"></a>Mandatory if the <strong id="b1598111525312"><a name="b1598111525312"></a><a name="b1598111525312"></a>NoncurrentVersionExpiration</strong> or <strong id="b17992301044"><a name="b17992301044"></a><a name="b17992301044"></a>NoncurrentVersionTransition</strong> parameter is present.</p>
</td>
</tr>
<tr id="row81345881514"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p356918547576"><a name="p356918547576"></a><a name="p356918547576"></a>NoncurrentVersionTransition</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p1670512161921"><a name="p1670512161921"></a><a name="p1670512161921"></a>Indicates the element of the transition time and new storage class (applicable to historical versions) in the lifecycle configuration.</p>
<p id="p4705416421"><a name="p4705416421"></a><a name="p4705416421"></a>Type: XML</p>
<p id="p770520161926"><a name="p770520161926"></a><a name="p770520161926"></a>Children: NoncurrentDays, StorageClass</p>
<p id="p47062162220"><a name="p47062162220"></a><a name="p47062162220"></a>Ancestor: Rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p11706816329"><a name="p11706816329"></a><a name="p11706816329"></a>Mandatory if <strong id="b670691617215"><a name="b670691617215"></a><a name="b670691617215"></a>Transition</strong>, <strong id="b0706111619216"><a name="b0706111619216"></a><a name="b0706111619216"></a>Expiration</strong>, and <strong id="b170613169211"><a name="b170613169211"></a><a name="b170613169211"></a>NoncurrentVersionExpiration</strong> are absent.</p>
</td>
</tr>
<tr id="row38960720173947"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1701766173947"><a name="p1701766173947"></a><a name="p1701766173947"></a>NoncurrentVersionExpiration</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p411104918235"><a name="p411104918235"></a><a name="p411104918235"></a>Indicates the container for the noncurrent object expiration rule. You set this lifecycle configuration action on a bucket that has versioning enabled (or suspended) to request that OBS delete noncurrent object versions which meet the expiration rule.</p>
<p id="p35167743115110"><a name="p35167743115110"></a><a name="p35167743115110"></a>Type: XML</p>
<p id="p48074236115110"><a name="p48074236115110"></a><a name="p48074236115110"></a>Children: NoncurrentDays</p>
<p id="p30014947115110"><a name="p30014947115110"></a><a name="p30014947115110"></a>Ancestor: Rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p114457812915"><a name="p114457812915"></a><a name="p114457812915"></a>Mandatory if <strong id="b12739225526"><a name="b12739225526"></a><a name="b12739225526"></a>Transition</strong>, <strong id="b47397251021"><a name="b47397251021"></a><a name="b47397251021"></a>Expiration</strong>, and <strong id="b1873916251429"><a name="b1873916251429"></a><a name="b1873916251429"></a>NoncurrentVersionTransition</strong> are absent.</p>
</td>
</tr>
<tr id="row44625493"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p57895144"><a name="p57895144"></a><a name="p57895144"></a>Prefix</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p58995125"><a name="p58995125"></a><a name="p58995125"></a>Indicates the object key prefix identifying one or more objects to which the rule applies.</p>
<p id="p61194080"><a name="p61194080"></a><a name="p61194080"></a>Type: String</p>
<p id="p13875810"><a name="p13875810"></a><a name="p13875810"></a>Ancestor: Rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p50198807"><a name="p50198807"></a><a name="p50198807"></a>Mandatory</p>
</td>
</tr>
<tr id="row49136085"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p20599914"><a name="p20599914"></a><a name="p20599914"></a>Rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p57980315"><a name="p57980315"></a><a name="p57980315"></a>Indicates the container for lifecycle rules.</p>
<p id="p52060794"><a name="p52060794"></a><a name="p52060794"></a>Type: Container</p>
<p id="p65893970"><a name="p65893970"></a><a name="p65893970"></a>Ancestor: LifecycleConfiguration</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p35811316"><a name="p35811316"></a><a name="p35811316"></a>Mandatory</p>
</td>
</tr>
<tr id="row53866394"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1101770"><a name="p1101770"></a><a name="p1101770"></a>Status</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p22134555"><a name="p22134555"></a><a name="p22134555"></a>Indicates whether the rule is enabled.</p>
<p id="p64993271"><a name="p64993271"></a><a name="p64993271"></a>Type: String</p>
<p id="p48068532"><a name="p48068532"></a><a name="p48068532"></a>Ancestor: Rule</p>
<p id="p29963612"><a name="p29963612"></a><a name="p29963612"></a>Valid Values: Enabled, Disabled</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p11133493"><a name="p11133493"></a><a name="p11133493"></a>Mandatory</p>
</td>
</tr>
</tbody>
</table>

If the multi-version of a bucket is enabled or suspended, you can set  **NoncurrentVersionExpiration**  or  **NoncurrentVersionTransition**  to control the lifecycle of historical object versions. The lifecycle of a historical version depends on the time when the version becomes a historical one, that is, the version is overwritten by a new version \(**NoncurrentDays**\).

In deletion circumstances, if  **NoncurrentDays**  is 1, a version can only be deleted one day after it has become a historical version. For example, the V1 version of object A is created on the first day of a month, and its new version V2 is uploaded on the fifth day of the month. Then V1 becomes a historical version. One day later, that is, when the 0 o'clock of the seventh day comes, V1 expires. If an object version does not meet the deletion conditions,  **NoncurrentDays**  is 1, and  **StorageClass**  is  **STANDARD\_IA**, a version transitions to the Warm storage class one day after it has become a historical version. For example, the V1 version of object A is created on the first day of a month, and its new version V2 is uploaded on the fifth day of the month. Then V1 becomes a historical version. One day later, that is, when the 0 o'clock of the seventh day comes, V1 transitions to the Warm storage class. \(Remarks: There is a delay of less than 48 hours for such a deletion or transition upon object expiration.\)

The following lists the background processing for when the multi-version of a bucket is enabled or suspended and the object of the latest version meets expiration rules:

-   The multi-version of the bucket is enabled:
    -   If the object of the latest version is not  **deletemarker**, a new  **deletemarker**  is generated for the object.
    -   If the object of the latest version is  **deletemarker**  and the object has this version only, the version will be deleted.
    -   If the object of the latest version is  **deletemarker**  and the object has other versions, all versions of the object remain unchanged.


-   The multi-version of the bucket is suspended:
    -   If the latest version is not null,  **deletemarker**  of a null version will be generated.
    -   If the latest version is null, the null version will be overwritten by  **deletemarker**  of a new null version.


If the bucket versioning is  **Enabled**  or  **Suspended**  and the latest version of the object meets the transition rule:

-   If the latest version is  **deletemarker**, this version will not transition to another storage class.
-   If the latest version is  **deletemarker**  and the object meets the transition conditions, this version will transition to another storage class.

## Response Syntax<a name="section10857028"></a>

```
HTTP/1.1 status_code 
Server: Server Name 
x-amz-request-id: request id 
x-amz-id-2: id 
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
Date: date 
Content-Length: length 
```

## Response Headers<a name="section30604389"></a>

This response uses common headers. For details about common response headers, see section  [Common Response Headers](common-response-headers.md).

## Response elements<a name="section7004053"></a>

This response involves no elements.

## Error Responses<a name="section63036484"></a>

No special error responses are returned. For details about error responses, see  [Table 1](error-codes.md#table30733758).

## Sample Request 1<a name="section28842926"></a>

```
PUT /?lifecycle HTTP/1.1
 User-Agent: curl/7.29.0
 Host: bucketname.obs.example.com
 Date: Thu, 05 Sep 2013 09:35:44 +0000 
 Authorization: AWS B9A70C60A39C4D551A16:MOO0dUPmAAEXEe0/z+Q9LCx1Vzc= 
 Content-MD5: Sa2ttwkV/+XRCwEHg4N8ow== 
 Content-Length: 423
 Expect: 100-continue

<LifecycleConfiguration>
<Rule>
<ID>delete-2-days</ID>
<Prefix>test/</Prefix>
<Status>Enabled</Status>
<Expiration>
<Days>365</Days>
</Expiration>
<NoncurrentVersionExpiration>
<NoncurrentDays>365</NoncurrentDays>
</NoncurrentVersionExpiration>
<Transition> 
<Days>30</Days> 
<StorageClass>STANDARD_IA</StorageClass> 
</Transition> 
<Transition> 
<Days>60</Days> 
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

## Sample Response 1<a name="section58259743"></a>

```
HTTP/1.1 200 OK 
 Date: Thu, 05 Sep 2013 09:35:44 GMT 
 Server: OBS 
 x-amz-request-id: 90E2BA0A420C00000140ED7A369007A2 
 x-amz-id-2: t35S98JCFKUMswCPZCk+UTi/VOoiSenzi5J6wnoKCIMfXUsKYGgU5+daiWAYiY/8 
 x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc 
 Content-Length: 0
```

## Sample Request 2<a name="section165812054676"></a>

```
PUT /?lifecycle HTTP/1.1
User-Agent: curl/7.29.0
Host: bucketname.obs.example.comDate: Thu, 05 Sep 2015 09:35:44 +0000
Authorization: AWS B9A70C60A39C4D551A16:MOO0dUPmAAEXEe0/z+Q9LCx1Vzc=
Content-MD5: Sa2ttwkV/+XRCwEHg4N8ow==
Content-Length: 423
Expect: 100-continue
<LifecycleConfiguration>
<Rule>
<ID>delete-2-days</ID>
<Prefix>test/</Prefix>
<Status>Enabled</Status>
<Expiration>
<Days>365</Days>
</Expiration>
<Transition> 
<Days>30</Days> 
<StorageClass>STANDARD_IA</StorageClass> 
</Transition> 
<Transition> 
<Days>60</Days> 
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

## Sample Response 2<a name="section8484163419817"></a>

```
HTTP/1.1 200 OK
Date: Thu, 05 Sep 2015 09:35:44 GMT
x-amz-request-id: 90E2BA0A420C00000140ED7A369007A2
x-amz-id-2: t35S98JCFKUMswCPZCk+UTi/VOoiSenzi5J6wnoKCIMfXUsKYGgU5+daiWAYiY/8
x-reserved: amazon, aws and amazon web services are trademarks or registered trademarks of Amazon Technologies, Inc
Content-Length: 0
```

