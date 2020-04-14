# ACL<a name="EN-US_TOPIC_0125560406"></a>

A default ACL is generated during the creation of a bucket or an object. The entries in an ACL define permission granted to accounts. You can use PUT Bucket/Object acl to create a new ACL for a bucket or an object.

-   [Table 1](#table49181932)  gives a description of each Grantee and their access permission.

**Table  1**  Grantees in OBS

<a name="table49181932"></a>
<table><thead align="left"><tr id="row11473484"><th class="cellrowborder" valign="top" width="34.77%" id="mcps1.2.3.1.1"><p id="p56936981"><a name="p56936981"></a><a name="p56936981"></a>Grantee</p>
</th>
<th class="cellrowborder" valign="top" width="65.23%" id="mcps1.2.3.1.2"><p id="p48492710"><a name="p48492710"></a><a name="p48492710"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row35595432"><td class="cellrowborder" valign="top" width="34.77%" headers="mcps1.2.3.1.1 "><p id="p64657730"><a name="p64657730"></a><a name="p64657730"></a>OBS user</p>
</td>
<td class="cellrowborder" valign="top" width="65.23%" headers="mcps1.2.3.1.2 "><p id="p2784797"><a name="p2784797"></a><a name="p2784797"></a>The permission to access a bucket or object can be granted to any OBS user. An OBS user can access the bucket or object in OBS using its AK and SK.</p>
</td>
</tr>
<tr id="row25063178"><td class="cellrowborder" valign="top" width="34.77%" headers="mcps1.2.3.1.1 "><p id="p16851561"><a name="p16851561"></a><a name="p16851561"></a>Registered user group user</p>
</td>
<td class="cellrowborder" valign="top" width="65.23%" headers="mcps1.2.3.1.2 "><p id="p22799196"><a name="p22799196"></a><a name="p22799196"></a>The permission to access a bucket or object can be granted to all users in a registered user group. A user in a registered user group can access the bucket or object in OBS using its AK and SK. This group represents all OBS accounts.</p>
</td>
</tr>
<tr id="row3866177"><td class="cellrowborder" valign="top" width="34.77%" headers="mcps1.2.3.1.1 "><p id="p44724910"><a name="p44724910"></a><a name="p44724910"></a>Anonymous user</p>
</td>
<td class="cellrowborder" valign="top" width="65.23%" headers="mcps1.2.3.1.2 "><p id="p65947939"><a name="p65947939"></a><a name="p65947939"></a>The permission to access a bucket or object can be granted to anonymous users. After the permission is granted, all users can access the bucket or object.</p>
</td>
</tr>
<tr id="row56660545"><td class="cellrowborder" valign="top" width="34.77%" headers="mcps1.2.3.1.1 "><p id="p26101398"><a name="p26101398"></a><a name="p26101398"></a>Log delivery user group</p>
</td>
<td class="cellrowborder" valign="top" width="65.23%" headers="mcps1.2.3.1.2 "><p id="p33838471"><a name="p33838471"></a><a name="p33838471"></a>The permission to access a bucket can be granted to all users in a log delivery user group. A user in a log delivery user group can access the bucket. The permission is mainly used in log management.</p>
</td>
</tr>
</tbody>
</table>

-   ACL syntax

The request for modifying or setting the ACL of a bucket or object must contain an ACL in the following syntax:

```
<AccessControlPolicy> 
 <Owner>
 <ID>id</ID>
 <DisplayName>displayname</DisplayName>
 </Owner>
 <AccessControlList>
 <Grant>
 <Grantee>grantee</Grantee>
 <Permission>permission</Permission>
 </Grant>
 <Grant>…………</Grant>
 </AccessControlList>
 </AccessControlPolicy>
```

In the preceding ACL,  **permission** indicates one of the five permission types supported by OBS. For details about the permission, see [Table 2](#table39984204). The format of content in **Grantee**  varies with the grantee.

1.  An OBS user as the grantee

    ```
    <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
     <ID>DomainId</ID>
     <DisplayName>displayname</DisplayName>
     </Grantee>
    ```

2.  A registered user group user as the grantee

    ```
    <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Group">
     <URI>http://acs.amazonaws.com/groups/global/AuthenticatedUsers</URI>
     </Grantee>
    ```

3.  An anonymous user as the grantee

    ```
    <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Group">
     <URI>http://acs.amazonaws.com/groups/global/AllUsers</URI>
     </Grantee>
    ```

4.  Log delivery user group user as the grantee

    ```
    <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Group">   <URI>http://acs.amazonaws.com/groups/s3/LogDelivery</URI>   </Grantee>
    ```


**Table  2**  Permission on an OBS bucket or object

<a name="table39984204"></a>
<table><thead align="left"><tr id="row59544593"><th class="cellrowborder" valign="top" width="31.019999999999996%" id="mcps1.2.3.1.1"><p id="p58382711"><a name="p58382711"></a><a name="p58382711"></a>Permission</p>
</th>
<th class="cellrowborder" valign="top" width="68.97999999999999%" id="mcps1.2.3.1.2"><p id="p31379187"><a name="p31379187"></a><a name="p31379187"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row58686186"><td class="cellrowborder" valign="top" width="31.019999999999996%" headers="mcps1.2.3.1.1 "><p id="p55960646"><a name="p55960646"></a><a name="p55960646"></a>READ</p>
</td>
<td class="cellrowborder" valign="top" width="68.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p36518511"><a name="p36518511"></a><a name="p36518511"></a>A grantee with such permission for a bucket can obtain the list of objects in the bucket and its metadata.</p>
<p id="p60231148"><a name="p60231148"></a><a name="p60231148"></a>A grantee with such permission for an object can obtain the object content and metadata.</p>
</td>
</tr>
<tr id="row5209420"><td class="cellrowborder" valign="top" width="31.019999999999996%" headers="mcps1.2.3.1.1 "><p id="p19309894"><a name="p19309894"></a><a name="p19309894"></a>WRITE</p>
</td>
<td class="cellrowborder" valign="top" width="68.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p20597572"><a name="p20597572"></a><a name="p20597572"></a>A grantee with such permission for a bucket can upload, overwrite, and delete any object in the bucket.</p>
<p id="p3877837163357"><a name="p3877837163357"></a><a name="p3877837163357"></a>Such permission for an object is <strong id="b4909618205558"><a name="b4909618205558"></a><a name="b4909618205558"></a>NOT</strong> applicable.</p>
</td>
</tr>
<tr id="row51160424"><td class="cellrowborder" valign="top" width="31.019999999999996%" headers="mcps1.2.3.1.1 "><p id="p50353704"><a name="p50353704"></a><a name="p50353704"></a>READ_ACP</p>
</td>
<td class="cellrowborder" valign="top" width="68.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p52118241"><a name="p52118241"></a><a name="p52118241"></a>A grantee with such permission can obtain the ACL of a bucket or object. A bucket or object owner has such permission permanently.</p>
</td>
</tr>
<tr id="row66410986"><td class="cellrowborder" valign="top" width="31.019999999999996%" headers="mcps1.2.3.1.1 "><p id="p10580746"><a name="p10580746"></a><a name="p10580746"></a>WRITE_ACP</p>
</td>
<td class="cellrowborder" valign="top" width="68.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p51734070"><a name="p51734070"></a><a name="p51734070"></a>A grantee with such permission can update the ACL of a bucket or object. A bucket or object owner has such permission permanently.</p>
<p id="p62953453"><a name="p62953453"></a><a name="p62953453"></a>A grantee with such permission can modify the access control policy to obtain desired access permission.</p>
</td>
</tr>
<tr id="row29710167"><td class="cellrowborder" valign="top" width="31.019999999999996%" headers="mcps1.2.3.1.1 "><p id="p57713365"><a name="p57713365"></a><a name="p57713365"></a>FULL_CONTROL</p>
</td>
<td class="cellrowborder" valign="top" width="68.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p44270999"><a name="p44270999"></a><a name="p44270999"></a>A grantee with such permission for a bucket has <strong id="b62894678"><a name="b62894678"></a><a name="b62894678"></a>READ</strong>,&nbsp;<strong id="b29181190"><a name="b29181190"></a><a name="b29181190"></a>WRITE</strong>,&nbsp;<strong id="b61304121"><a name="b61304121"></a><a name="b61304121"></a>READ_ACP</strong>, and&nbsp;<strong id="b14866185"><a name="b14866185"></a><a name="b14866185"></a>WRITE_ACP</strong> permission.</p>
<p id="p23402560163625"><a name="p23402560163625"></a><a name="p23402560163625"></a>A grantee with such permission for an object has <strong id="b39840676163625"><a name="b39840676163625"></a><a name="b39840676163625"></a>READ</strong>,&nbsp;<strong id="b5652634163625"><a name="b5652634163625"></a><a name="b5652634163625"></a>READ_ACP</strong>, and&nbsp;<strong id="b55210187163625"><a name="b55210187163625"></a><a name="b55210187163625"></a>WRITE_ACP</strong> permission.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>1.  A request can contain a maximum of 100 grants.  
>2.  The ACL of a bucket or object is overwritten after permission associated with the bucket or object is granted  

The following table shows how each of the ACL permissions maps to the corresponding access policy permissions. As you can see, access policy allows more permissions than ACL does, you use ACL to primarily grant basic read/write permissions.

**Table  3**  ACL permissions map

<a name="table26278030164431"></a>
<table><thead align="left"><tr id="row19828033164431"><th class="cellrowborder" valign="top" width="23.23767623237676%" id="mcps1.2.4.1.1"><p id="p4020331165425"><a name="p4020331165425"></a><a name="p4020331165425"></a>ACL</p>
<p id="p4573853016536"><a name="p4573853016536"></a><a name="p4573853016536"></a>Permission</p>
</th>
<th class="cellrowborder" valign="top" width="38.92610738926107%" id="mcps1.2.4.1.2"><p id="p5138300165347"><a name="p5138300165347"></a><a name="p5138300165347"></a>Corresponding access policy permissions when the ACL permission is granted on a bucket</p>
</th>
<th class="cellrowborder" valign="top" width="37.83621637836217%" id="mcps1.2.4.1.3"><p id="p38839699165411"><a name="p38839699165411"></a><a name="p38839699165411"></a>Corresponding access policy permissions when the ACL permission is granted on an object</p>
</th>
</tr>
</thead>
<tbody><tr id="row8381768164431"><td class="cellrowborder" valign="top" width="23.23767623237676%" headers="mcps1.2.4.1.1 "><p id="p7834633164431"><a name="p7834633164431"></a><a name="p7834633164431"></a>READ</p>
</td>
<td class="cellrowborder" valign="top" width="38.92610738926107%" headers="mcps1.2.4.1.2 "><p id="p27306801165459"><a name="p27306801165459"></a><a name="p27306801165459"></a>s3:ListBucket, s3:ListBucketVersions, and s3:ListBucketMultipartUploads</p>
</td>
<td class="cellrowborder" valign="top" width="37.83621637836217%" headers="mcps1.2.4.1.3 "><p id="p19239774165512"><a name="p19239774165512"></a><a name="p19239774165512"></a>s3:GetObject and s3:GetObjectVersion</p>
</td>
</tr>
<tr id="row45901784164431"><td class="cellrowborder" valign="top" width="23.23767623237676%" headers="mcps1.2.4.1.1 "><p id="p27056987164431"><a name="p27056987164431"></a><a name="p27056987164431"></a>WRITE</p>
</td>
<td class="cellrowborder" valign="top" width="38.92610738926107%" headers="mcps1.2.4.1.2 "><p id="p322918416569"><a name="p322918416569"></a><a name="p322918416569"></a>s3:PutObject and s3:DeleteObject.</p>
<p id="p6023735816569"><a name="p6023735816569"></a><a name="p6023735816569"></a>In addition, when the grantee is the bucket owner, granting WRITE permission in a bucket ACL allows the s3:DeleteObjectVersion action to be performed on any version in that bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="37.83621637836217%" headers="mcps1.2.4.1.3 "><p id="p17952693164431"><a name="p17952693164431"></a><a name="p17952693164431"></a>Not applicable</p>
</td>
</tr>
<tr id="row27356511164431"><td class="cellrowborder" valign="top" width="23.23767623237676%" headers="mcps1.2.4.1.1 "><p id="p1284912164431"><a name="p1284912164431"></a><a name="p1284912164431"></a>READ_ACP</p>
</td>
<td class="cellrowborder" valign="top" width="38.92610738926107%" headers="mcps1.2.4.1.2 "><p id="p36969013164431"><a name="p36969013164431"></a><a name="p36969013164431"></a>s3:GetBucketAcl</p>
</td>
<td class="cellrowborder" valign="top" width="37.83621637836217%" headers="mcps1.2.4.1.3 "><p id="p32992663165752"><a name="p32992663165752"></a><a name="p32992663165752"></a>s3:GetObjectAcl and s3:GetObjectVersionAcl</p>
</td>
</tr>
<tr id="row39756173164431"><td class="cellrowborder" valign="top" width="23.23767623237676%" headers="mcps1.2.4.1.1 "><p id="p66133477164431"><a name="p66133477164431"></a><a name="p66133477164431"></a>WRITE_ACP</p>
</td>
<td class="cellrowborder" valign="top" width="38.92610738926107%" headers="mcps1.2.4.1.2 "><p id="p55211405164431"><a name="p55211405164431"></a><a name="p55211405164431"></a>s3:PutBucketAcl</p>
</td>
<td class="cellrowborder" valign="top" width="37.83621637836217%" headers="mcps1.2.4.1.3 "><p id="p6058706165840"><a name="p6058706165840"></a><a name="p6058706165840"></a>s3:PutObjectAcl and s3:PutObjectVersionAcl</p>
</td>
</tr>
<tr id="row50904858164431"><td class="cellrowborder" valign="top" width="23.23767623237676%" headers="mcps1.2.4.1.1 "><p id="p29652834164431"><a name="p29652834164431"></a><a name="p29652834164431"></a>FULL_CONTROL</p>
</td>
<td class="cellrowborder" valign="top" width="38.92610738926107%" headers="mcps1.2.4.1.2 "><p id="p18109623165858"><a name="p18109623165858"></a><a name="p18109623165858"></a>It is equivalent to granting READ, WRITE, READ_ACP, and WRITE_ACP ACL permissions. Accordingly, this ACL permission maps to combination of corresponding access policy permissions.</p>
</td>
<td class="cellrowborder" valign="top" width="37.83621637836217%" headers="mcps1.2.4.1.3 "><p id="p3197895517036"><a name="p3197895517036"></a><a name="p3197895517036"></a>It is equivalent to granting READ, READ_ACP, and WRITE_ACP ACL permissions. Accordingly, this ACL permission maps to combination of corresponding access policy permissions.</p>
</td>
</tr>
</tbody>
</table>

## Access Control Policies<a name="section37008167"></a>

You can set an access control policy in  **x-amz-acl** HTTP header when creating a bucket or uploading an object. Available access control policies are predefined in OBS, as described in [Table 4](#table40200743).

**Table  4**  Predefined access control policies

<a name="table40200743"></a>
<table><thead align="left"><tr id="row23604067"><th class="cellrowborder" valign="top" width="31.019999999999996%" id="mcps1.2.3.1.1"><p id="p32881259"><a name="p32881259"></a><a name="p32881259"></a>Policy</p>
</th>
<th class="cellrowborder" valign="top" width="68.97999999999999%" id="mcps1.2.3.1.2"><p id="p46136299"><a name="p46136299"></a><a name="p46136299"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row46052748"><td class="cellrowborder" valign="top" width="31.019999999999996%" headers="mcps1.2.3.1.1 "><p id="p39285109"><a name="p39285109"></a><a name="p39285109"></a>private</p>
</td>
<td class="cellrowborder" valign="top" width="68.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p27977295"><a name="p27977295"></a><a name="p27977295"></a>Indicates that the owner of a bucket or object has <strong id="b2101653195420"><a name="b2101653195420"></a><a name="b2101653195420"></a>FULL_CONTROL</strong> permission for the bucket or object. Other users have no permission to access the bucket or object.</p>
</td>
</tr>
<tr id="row51568450"><td class="cellrowborder" valign="top" width="31.019999999999996%" headers="mcps1.2.3.1.1 "><p id="p16294901"><a name="p16294901"></a><a name="p16294901"></a>public-read</p>
</td>
<td class="cellrowborder" valign="top" width="68.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p44818576"><a name="p44818576"></a><a name="p44818576"></a>Indicates that the owner of a bucket or object has <strong id="b714004"><a name="b714004"></a><a name="b714004"></a>FULL_CONTROL</strong>&nbsp;permission for the bucket or object. Other users including anonymous users have&nbsp;<strong id="b6426044"><a name="b6426044"></a><a name="b6426044"></a>READ</strong> permission.</p>
</td>
</tr>
<tr id="row57834400"><td class="cellrowborder" valign="top" width="31.019999999999996%" headers="mcps1.2.3.1.1 "><p id="p54074791"><a name="p54074791"></a><a name="p54074791"></a>public-read-write</p>
</td>
<td class="cellrowborder" valign="top" width="68.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p17981971"><a name="p17981971"></a><a name="p17981971"></a>Indicates that the owner of a bucket or object has <strong id="b27620019"><a name="b27620019"></a><a name="b27620019"></a>FULL_CONTROL</strong>&nbsp;permission for the bucket or object. Other users including anonymous users have&nbsp;<strong id="b47253580"><a name="b47253580"></a><a name="b47253580"></a>READ</strong>&nbsp;and&nbsp;<strong id="b22629041"><a name="b22629041"></a><a name="b22629041"></a>WRITE</strong> permission.</p>
</td>
</tr>
<tr id="row2334777"><td class="cellrowborder" valign="top" width="31.019999999999996%" headers="mcps1.2.3.1.1 "><p id="p54899267"><a name="p54899267"></a><a name="p54899267"></a>authenticated-read</p>
</td>
<td class="cellrowborder" valign="top" width="68.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p17655633"><a name="p17655633"></a><a name="p17655633"></a>Indicates that the owner of a bucket or object has <strong id="b24682973"><a name="b24682973"></a><a name="b24682973"></a>FULL_CONTROL</strong>&nbsp;permission for the bucket or object. Other OBS users have&nbsp;<strong id="b20820172"><a name="b20820172"></a><a name="b20820172"></a>READ</strong> permission.</p>
</td>
</tr>
<tr id="row53163821"><td class="cellrowborder" valign="top" width="31.019999999999996%" headers="mcps1.2.3.1.1 "><p id="p11302262"><a name="p11302262"></a><a name="p11302262"></a>bucket-owner-read</p>
</td>
<td class="cellrowborder" valign="top" width="68.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p43067999"><a name="p43067999"></a><a name="p43067999"></a>Indicates that the owner of an object has <strong id="b52067671"><a name="b52067671"></a><a name="b52067671"></a>FULL_CONTROL</strong>&nbsp;permission for the object and the owner of the bucket where the object resides has&nbsp;<strong id="b65955856"><a name="b65955856"></a><a name="b65955856"></a>READ</strong> permission.</p>
</td>
</tr>
<tr id="row56731795"><td class="cellrowborder" valign="top" width="31.019999999999996%" headers="mcps1.2.3.1.1 "><p id="p31872708"><a name="p31872708"></a><a name="p31872708"></a>bucket-owner-full-control</p>
</td>
<td class="cellrowborder" valign="top" width="68.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p31552594"><a name="p31552594"></a><a name="p31552594"></a>Indicates that the owner of an object has <strong id="b15537895"><a name="b15537895"></a><a name="b15537895"></a>FULL_CONTROL</strong>&nbsp;permission for the object and the owner of the bucket where the object resides has&nbsp;<strong id="b5623332"><a name="b5623332"></a><a name="b5623332"></a>FULL_CONTROL</strong> permission for the object.</p>
</td>
</tr>
<tr id="row50609995"><td class="cellrowborder" valign="top" width="31.019999999999996%" headers="mcps1.2.3.1.1 "><p id="p5768894"><a name="p5768894"></a><a name="p5768894"></a>log-delivery-write</p>
</td>
<td class="cellrowborder" valign="top" width="68.97999999999999%" headers="mcps1.2.3.1.2 "><p id="p64627307"><a name="p64627307"></a><a name="p64627307"></a>Indicates that a log delivery group has <strong id="b64191727172224"><a name="b64191727172224"></a><a name="b64191727172224"></a>WRITE</strong>&nbsp;and&nbsp;<strong id="b320504"><a name="b320504"></a><a name="b320504"></a>READ_ACP</strong> permission for buckets.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>By default, the access control policy is  **private**.  

