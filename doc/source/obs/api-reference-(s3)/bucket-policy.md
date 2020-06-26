# Bucket Policy<a name="EN-US_TOPIC_0125560422"></a>

Bucket policies provide centralized, access control to buckets and objects based on a variety of conditions, including OBS operations, requesters, resources, and aspects of the request \(e.g., IP address\). The permissions attached to a bucket apply to all of the objects in that bucket.

Individuals as well as companies can use bucket policies. When companies register with OBS they create an  _account_. Thereafter, the company becomes synonymous with the account. Accounts are financially responsible for the resources they \(and their employees\) create. Accounts have the power to grant bucket policy permissions and assign employees permissions based on a variety of conditions. For example, an account could create a policy that gives a user write access:

To a particular bucket

From an account's corporate network

From an account's custom application

Unlike access control lists \(ACL\), which can add \(grant\) permissions only on individual objects, policies can either add or deny permissions across all \(or a subset\) of objects within a bucket. With one request an account can set the permissions of any number of objects in a bucket. An account can use wildcards \(similar to regular expression operators\) on Amazon resource names \(ARNs\) and other values, so that an account can control access to groups of objects.

A bucket owner can perform the PUT Bucket policy operation to set a bucket access policy. However, a new policy will overwrite the existing one. A bucket owner can also perform the Get Bucket policy or DELETE Bucket policy operation to obtain or delete a bucket policy. After a policy is set for a bucket, all subsequent access to the bucket is controlled by the policy. Requests for accessing the bucket are accepted or denied according to the policy.

In the following example bucket policy, accounts  **783fc6652cf246c096ea836694f71855** \(Domain ID\) and **219d520ceac84c5a98b237431a2cf4c2** \(Domain ID\) are granted the **GetObject** permission for all objects in **mybucket**.

```
{ 
   "Version":"2008-10-17", 
   "Id":"aaaa-bbbb-cccc-dddd", 
   "Statement" : [ 
      { 
       "Effect":"Allow", 
       "Sid":"1",  
       "Principal" : { 
         "AWS":["arn:aws:iam::783fc6652cf246c096ea836694f71855:root","arn:aws:iam::219d520ceac84c5a98b237431a2cf4c2:root"] 
       }, 
       "Action":["s3:GetObject"], 
       "Resource":"arn:aws:s3:::mybucket/*" 
      } 
   ]  
 }
```

## Policy Format<a name="section39017818"></a>

A policy is described in the JSON format, as shown in the following syntax:

```
{ 
 "Version" : "version", 
 "Id" : "id", 
 "Statement" : [statement] 
 }
```

The  **Id**  and **Version**  parameters are optional.

**Table  1**  Policy

<a name="table22453715"></a>
<table><thead align="left"><tr id="row60715486"><th class="cellrowborder" valign="top" width="19.05%" id="mcps1.2.4.1.1"><p id="p19007354"><a name="p19007354"></a><a name="p19007354"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="63.78%" id="mcps1.2.4.1.2"><p id="p63200739"><a name="p63200739"></a><a name="p63200739"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.3"><p id="p18986240"><a name="p18986240"></a><a name="p18986240"></a>Required</p>
</th>
</tr>
</thead>
<tbody><tr id="row61490490"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="p14673784"><a name="p14673784"></a><a name="p14673784"></a>Id</p>
</td>
<td class="cellrowborder" valign="top" width="63.78%" headers="mcps1.2.4.1.2 "><p id="p47725859"><a name="p47725859"></a><a name="p47725859"></a>Indicates the ID of a policy. The value is a string that describes the policy.</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.3 "><p id="p40589346"><a name="p40589346"></a><a name="p40589346"></a>No</p>
</td>
</tr>
<tr id="row29759797"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="p61733326"><a name="p61733326"></a><a name="p61733326"></a>Version</p>
</td>
<td class="cellrowborder" valign="top" width="63.78%" headers="mcps1.2.4.1.2 "><p id="p56311059193618"><a name="p56311059193618"></a><a name="p56311059193618"></a>Possible values are <strong id="b22584573193647"><a name="b22584573193647"></a><a name="b22584573193647"></a>2008-10-17</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.3 "><p id="p30357761"><a name="p30357761"></a><a name="p30357761"></a>No</p>
</td>
</tr>
</tbody>
</table>

A policy can contain multiple statements and each statement contains the following elements:

**Table  2**  statement elements

<a name="table756848"></a>
<table><thead align="left"><tr id="row30402474"><th class="cellrowborder" valign="top" width="19.05%" id="mcps1.2.4.1.1"><p id="p46681319"><a name="p46681319"></a><a name="p46681319"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="63.970000000000006%" id="mcps1.2.4.1.2"><p id="p23090476"><a name="p23090476"></a><a name="p23090476"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.3"><p id="p58389282"><a name="p58389282"></a><a name="p58389282"></a>Required</p>
</th>
</tr>
</thead>
<tbody><tr id="row31911408"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="p34687295"><a name="p34687295"></a><a name="p34687295"></a>Sid</p>
</td>
<td class="cellrowborder" valign="top" width="63.970000000000006%" headers="mcps1.2.4.1.2 "><p id="p58207543"><a name="p58207543"></a><a name="p58207543"></a>Indicates the ID of a statement. The value is a string that describes the statement.</p>
</td>
<td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.3 "><p id="p17190527"><a name="p17190527"></a><a name="p17190527"></a>No</p>
</td>
</tr>
<tr id="row20497016"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="p49645628"><a name="p49645628"></a><a name="p49645628"></a>Principal</p>
</td>
<td class="cellrowborder" valign="top" width="63.970000000000006%" headers="mcps1.2.4.1.2 "><p id="p1694205"><a name="p1694205"></a><a name="p1694205"></a>Indicates the grantee of a statement. The value can be a wildcard character (*) that indicates all users. When the grantee is a domain, <strong id="b15247851"><a name="b15247851"></a><a name="b15247851"></a>Principal</strong>&nbsp;is in the&nbsp;<strong id="b842352706172349"><a name="b842352706172349"></a><a name="b842352706172349"></a>AWS:domainid</strong>,&nbsp;<strong id="b84235270617242"><a name="b84235270617242"></a><a name="b84235270617242"></a>AWS:arn:aws:iam::domainid:root</strong>, or&nbsp;<strong id="b842352706102541"><a name="b842352706102541"></a><a name="b842352706102541"></a>CanonicalUser:</strong>&nbsp;format. When the grantee is a user,&nbsp;<strong id="b93562175616120"><a name="b93562175616120"></a><a name="b93562175616120"></a>Principal</strong>&nbsp;is in the&nbsp;<strong id="b173439141516120"><a name="b173439141516120"></a><a name="b173439141516120"></a>AWS:arn:aws:iam::domainid:user/userId</strong>&nbsp;or&nbsp;<strong id="b842352706171843"><a name="b842352706171843"></a><a name="b842352706171843"></a>AWS:arn:aws:iam::domainid:user/userName</strong> format.</p>
<p id="p47015489143336"><a name="p47015489143336"></a><a name="p47015489143336"></a>A statement grantee can specify whether the statement grantors are agency users or federated users. For agency users, the principal format is <strong id="b32826017145418"><a name="b32826017145418"></a><a name="b32826017145418"></a>AWS:arn:aws:iam::domainid:agency/agencyName</strong>. For federated users, the principal format is&nbsp;<strong id="b19159022145418"><a name="b19159022145418"></a><a name="b19159022145418"></a>Federated:arn:aws:iam::domainid:identity-provider/providername</strong>&nbsp;or&nbsp;<strong id="b38213472145418"><a name="b38213472145418"></a><a name="b38213472145418"></a>Federated:arn:aws:iam::domainid:group/groupname</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.3 "><p id="p61135510"><a name="p61135510"></a><a name="p61135510"></a>No, Choose either Principal or NotPrincipal</p>
</td>
</tr>
<tr id="row13348680"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="p7501266"><a name="p7501266"></a><a name="p7501266"></a>NotPrincipal</p>
</td>
<td class="cellrowborder" valign="top" width="63.970000000000006%" headers="mcps1.2.4.1.2 "><p id="p3622792"><a name="p3622792"></a><a name="p3622792"></a>Specifies an exception to a list of principals in the statement. You can deny access to all principals except the one named in the <strong id="b32605136"><a name="b32605136"></a><a name="b32605136"></a>NotPrincipal</strong>&nbsp;element. The value of this element is similar to that of&nbsp;<strong id="b25010772"><a name="b25010772"></a><a name="b25010772"></a>Principal</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.3 "><p id="p12606619"><a name="p12606619"></a><a name="p12606619"></a>No, Choose either Principal or NotPrincipal</p>
</td>
</tr>
<tr id="row46350713"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="p63420295"><a name="p63420295"></a><a name="p63420295"></a>Action</p>
</td>
<td class="cellrowborder" valign="top" width="63.970000000000006%" headers="mcps1.2.4.1.2 "><p id="p36770245"><a name="p36770245"></a><a name="p36770245"></a>Specifies operations that a grantee can perform. The value is a case-insensitive string consisting of a set of operations supported by OBS.</p>
<p id="p62496749"><a name="p62496749"></a><a name="p62496749"></a>The value can be a wildcard character (*) that indicates all operations.</p>
<p id="p25599835"><a name="p25599835"></a><a name="p25599835"></a>Example:</p>
<p id="p29071927"><a name="p29071927"></a><a name="p29071927"></a>"Action":["s3:List*", "s3:Get*"]</p>
</td>
<td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.3 "><p id="p6015877"><a name="p6015877"></a><a name="p6015877"></a>No, Choose either Action or NotAction</p>
</td>
</tr>
<tr id="row54142897"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="p23498561"><a name="p23498561"></a><a name="p23498561"></a>NotAction</p>
</td>
<td class="cellrowborder" valign="top" width="63.970000000000006%" headers="mcps1.2.4.1.2 "><p id="p24335306"><a name="p24335306"></a><a name="p24335306"></a>Specifies an exception to a list of actions in the statement. All actions are performed except the one specified in <strong id="b17691163"><a name="b17691163"></a><a name="b17691163"></a>NotAction</strong>. The value of this element is similar to&nbsp;<strong id="b25002739"><a name="b25002739"></a><a name="b25002739"></a>Action</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.3 "><p id="p11955940"><a name="p11955940"></a><a name="p11955940"></a>No, Choose either Action or NotAction</p>
</td>
</tr>
<tr id="row40494599"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="p58837112"><a name="p58837112"></a><a name="p58837112"></a>Effect</p>
</td>
<td class="cellrowborder" valign="top" width="63.970000000000006%" headers="mcps1.2.4.1.2 "><p id="p1076806"><a name="p1076806"></a><a name="p1076806"></a>Indicates whether permission in a statement is allowed or denied. The value is <strong id="b33804765518"><a name="b33804765518"></a><a name="b33804765518"></a>Allow</strong> or&nbsp;<strong id="b17535142994213"><a name="b17535142994213"></a><a name="b17535142994213"></a>Deny</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.3 "><p id="p20112472"><a name="p20112472"></a><a name="p20112472"></a>Yes</p>
</td>
</tr>
<tr id="row46794527"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="p32260306"><a name="p32260306"></a><a name="p32260306"></a>Resource</p>
</td>
<td class="cellrowborder" valign="top" width="63.970000000000006%" headers="mcps1.2.4.1.2 "><p id="p62948031"><a name="p62948031"></a><a name="p62948031"></a>Specifies resources that the statement covers. A resource is defined in the Amazon Resource Name (ARN) format. You can use a wildcard character (*) to represent all resources.</p>
</td>
<td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.3 "><p id="p65625740"><a name="p65625740"></a><a name="p65625740"></a>No, Choose either Resource or NotResource</p>
</td>
</tr>
<tr id="row53760750"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="p59653487"><a name="p59653487"></a><a name="p59653487"></a>NotResource</p>
</td>
<td class="cellrowborder" valign="top" width="63.970000000000006%" headers="mcps1.2.4.1.2 "><p id="p94244"><a name="p94244"></a><a name="p94244"></a>Specifies an exception to a list of resources in the statement. A policy is not applied to resources specified in <strong id="b848197"><a name="b848197"></a><a name="b848197"></a>NotResource</strong>. The value of this parameter is similar to that of&nbsp;<strong id="b7633781"><a name="b7633781"></a><a name="b7633781"></a>Resource</strong>.</p>
</td>
<td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.3 "><p id="p14356556"><a name="p14356556"></a><a name="p14356556"></a>No, Choose either Resource or NotResource</p>
</td>
</tr>
<tr id="row62100140"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="p64055428"><a name="p64055428"></a><a name="p64055428"></a>Condition</p>
</td>
<td class="cellrowborder" valign="top" width="63.970000000000006%" headers="mcps1.2.4.1.2 "><p id="p21107156"><a name="p21107156"></a><a name="p21107156"></a>Indicates the conditions for a statement to take effect.</p>
</td>
<td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.3 "><p id="p31958085"><a name="p31958085"></a><a name="p31958085"></a>No</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>A statement contains either:  
>-   **Action** or **NotAction**  
>-   **Resource** or **NotResource**  
>-   **Principal** or **NotPrincipal**  

In OBS,  **Action**  can be the following operations on buckets:

-   s3:DeleteBucket
-   s3:ListBucket
-   s3:ListBucketVersions
-   s3:ListBucketMultipartUploads
-   s3:GetBucketAcl
-   s3:PutBucketAcl
-   s3:GetBucketCORS
-   s3:PutBucketCORS
-   s3:GetBucketVersioning
-   s3:PutBucketVersioning
-   s3:GetBucketLocation
-   s3:GetBucketLogging
-   s3:PutBucketLogging
-   s3:GetBucketWebsite
-   s3:PutBucketWebsite
-   s3:DeleteBucketWebsite
-   s3:GetLifecycleConfiguration
-   s3:PutLifecycleConfiguration
-   s3:GetBucketNotification
-   s3:PutBucketNotification
-   s3:PutBucketPolicy
-   s3:GetBucketPolicy
-   s3:DeleteBucketPolicy
-   s3:PutBucketQuota
-   s3:GetBucketQuota
-   s3:PutBucketStoragePolicy
-   s3:GetBucketStoragePolicy
-   s3:GetBucketStorage
-   s3:PutBucketTagging
-   s3:GetBucketTagging

In OBS,  **Action**  can be the following operations on objects:

-   s3:GetObject \(applies to GET Object and HEAD Object\)
-   s3:GetObjectVersion
-   s3:PutObject \(applies to PUT Object, POST Object, Initiate Multipart Upload, Upload Part, and Complete Multipart Upload\)
-   s3:GetObjectAcl
-   s3:GetObjectVersionAcl
-   s3:PutObjectAcl
-   s3:PutObjectVersionAcl
-   s3:DeleteObject
-   s3:DeleteObjectVersion
-   s3:ListMultipartUploadParts
-   s3:AbortMultipartUpload
-   s3:RestoreObject

OBS supports S3 resources in the ARN format:

-   arn:aws:s3:::bucketname \(operations on buckets\)
-   arn:aws:s3:::bucketname/path/objectname \(operations on objects\)

The following policy grants all permissions \(including bucket and object operations\) for bucket  **examplebucket** to **71f3901173514e6988115ea2c26d1999** \(user ID\) in **b4bf1b36d9ca43d984fbcb9491b6fce9**  \(domain ID\).

```
{
    "Statement":[
    {
      "Sid":"test",
      "Effect":"Allow",
      "Principal": {"AWS": ["arn:aws:iam::b4bf1b36d9ca43d984fbcb9491b6fce9:user/71f3901173514e6988115ea2c26d1999"]},
      "Action":["s3:*"],
      "Resource":[
        "arn:aws:s3:::examplebucket/*",
        "arn:aws:s3:::examplebucket"
      ]
    }
  ]
}
```

or

```
{ 
    "Statement":[ 
    { 
      "Sid":"test", 
      "Effect":"Allow", 
      "Principal": {"AWS": ["arn:aws:iam::b4bf1b36d9ca43d984fbcb9491b6fce9:user/user1"]}, 
      "Action":["s3:*"], 
      "Resource":[ 
        "arn:aws:s3:::examplebucket/*", 
        "arn:aws:s3:::examplebucket" 
      ] 
    } 
  ] 
}
```

>![](/images/icon-note.gif) **NOTE:**   
>If you do not specify a path when uploading an object, omit  **/path**  in the ARN.  

[Table 3](#table6811633) lists the general types of **Condition**  that you can specify.

**Table  3**  Condition

<a name="table6811633"></a>
<table><thead align="left"><tr id="row14369203"><th class="cellrowborder" valign="top" width="16.6%" id="mcps1.2.4.1.1"><p id="p23054829"><a name="p23054829"></a><a name="p23054829"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="32.96%" id="mcps1.2.4.1.2"><p id="p55501888"><a name="p55501888"></a><a name="p55501888"></a>Element</p>
</th>
<th class="cellrowborder" valign="top" width="50.44%" id="mcps1.2.4.1.3"><p id="p66467923"><a name="p66467923"></a><a name="p66467923"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15192654"><td class="cellrowborder" rowspan="6" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p22645466"><a name="p22645466"></a><a name="p22645466"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="32.96%" headers="mcps1.2.4.1.2 "><p id="p22343454"><a name="p22343454"></a><a name="p22343454"></a>StringEquals</p>
</td>
<td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.4.1.3 "><p id="p64989379"><a name="p64989379"></a><a name="p64989379"></a>Strict matching</p>
<p id="p48033505"><a name="p48033505"></a><a name="p48033505"></a>Short version: streq</p>
</td>
</tr>
<tr id="row29648369"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p52707663"><a name="p52707663"></a><a name="p52707663"></a>StringNotEquals</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p41462277"><a name="p41462277"></a><a name="p41462277"></a>Strict negated matching</p>
<p id="p37616177"><a name="p37616177"></a><a name="p37616177"></a>Short version: strneq</p>
</td>
</tr>
<tr id="row3001276"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p41776795"><a name="p41776795"></a><a name="p41776795"></a>StringEqualsIgnoreCase</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p28477259"><a name="p28477259"></a><a name="p28477259"></a>Strict matching, ignoring case</p>
<p id="p54968745"><a name="p54968745"></a><a name="p54968745"></a>Short version: streqi</p>
</td>
</tr>
<tr id="row24956660"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="ole_link41"><a name="ole_link41"></a><a name="ole_link41"></a>StringNotEqualsIgnoreCase</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p62127694"><a name="p62127694"></a><a name="p62127694"></a>Strict negated matching, ignoring case</p>
<p id="p22278337"><a name="p22278337"></a><a name="p22278337"></a>Short version: strneqi</p>
</td>
</tr>
<tr id="row66287312"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p563178"><a name="p563178"></a><a name="p563178"></a>StringLike</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p533911500313"><a name="p533911500313"></a><a name="p533911500313"></a>Loose case-insensitive matching. The values can include a multi-character match wildcard (*) or a single-character match wildcard (?) anywhere in the string.</p>
<p id="p45617477"><a name="p45617477"></a><a name="p45617477"></a>Short version: strl</p>
</td>
</tr>
<tr id="row7904114"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p36253521"><a name="p36253521"></a><a name="p36253521"></a>StringNotLike</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p50854084"><a name="p50854084"></a><a name="p50854084"></a>Negated loose case-insensitive matching. The values can include a multi-character match wildcard (*) or a single-character match wildcard (?) anywhere in the string.</p>
<p id="p55033577"><a name="p55033577"></a><a name="p55033577"></a>Short version: strnl</p>
</td>
</tr>
<tr id="row25540148"><td class="cellrowborder" rowspan="6" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p55486088"><a name="p55486088"></a><a name="p55486088"></a>Numeric</p>
</td>
<td class="cellrowborder" valign="top" width="32.96%" headers="mcps1.2.4.1.2 "><p id="p65188137"><a name="p65188137"></a><a name="p65188137"></a>NumericEquals</p>
</td>
<td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.4.1.3 "><p id="p45747710"><a name="p45747710"></a><a name="p45747710"></a>Strict matching</p>
<p id="p9076207"><a name="p9076207"></a><a name="p9076207"></a>Short version: numeq</p>
</td>
</tr>
<tr id="row14577007"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p39886950"><a name="p39886950"></a><a name="p39886950"></a>NumericNotEquals</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p9617480"><a name="p9617480"></a><a name="p9617480"></a>Strict negated matching</p>
<p id="p19448462"><a name="p19448462"></a><a name="p19448462"></a>Short version: numneq</p>
</td>
</tr>
<tr id="row40818431"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p17958643"><a name="p17958643"></a><a name="p17958643"></a>NumericLessThan</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p45363979"><a name="p45363979"></a><a name="p45363979"></a>"Less than" matching</p>
<p id="p5622632"><a name="p5622632"></a><a name="p5622632"></a>Short version: numlt</p>
</td>
</tr>
<tr id="row50603696"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p5258697"><a name="p5258697"></a><a name="p5258697"></a>NumericLessThanEquals</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p23301311"><a name="p23301311"></a><a name="p23301311"></a>"Less than or equals" matching</p>
<p id="p8385208"><a name="p8385208"></a><a name="p8385208"></a>Short version: numlteq</p>
</td>
</tr>
<tr id="row8358009"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p5910111"><a name="p5910111"></a><a name="p5910111"></a>NumericGreaterThan</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p8957019"><a name="p8957019"></a><a name="p8957019"></a>"Greater than" matching</p>
<p id="p13504307"><a name="p13504307"></a><a name="p13504307"></a>Short version: numgt</p>
</td>
</tr>
<tr id="row54429906"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p46746286"><a name="p46746286"></a><a name="p46746286"></a>NumericGreaterThanEquals</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p28352855"><a name="p28352855"></a><a name="p28352855"></a>"Greater than or equals" matching</p>
<p id="p53849108"><a name="p53849108"></a><a name="p53849108"></a>Short version: numgteq</p>
</td>
</tr>
<tr id="row14879924"><td class="cellrowborder" rowspan="6" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p64423214"><a name="p64423214"></a><a name="p64423214"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="32.96%" headers="mcps1.2.4.1.2 "><p id="p50897836"><a name="p50897836"></a><a name="p50897836"></a>DateEquals</p>
</td>
<td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.4.1.3 "><p id="p29084055"><a name="p29084055"></a><a name="p29084055"></a>Strict matching</p>
<p id="p60429904"><a name="p60429904"></a><a name="p60429904"></a>Short version: dateeq</p>
</td>
</tr>
<tr id="row6998230"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p29985746"><a name="p29985746"></a><a name="p29985746"></a>DateNotEquals</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p12926322"><a name="p12926322"></a><a name="p12926322"></a>Strict negated matching</p>
<p id="p49228035"><a name="p49228035"></a><a name="p49228035"></a>Short version: dateneq</p>
</td>
</tr>
<tr id="row40399134"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p51104447"><a name="p51104447"></a><a name="p51104447"></a>DateLessThan</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p45819581"><a name="p45819581"></a><a name="p45819581"></a>A point in time at which a key stops taking effect</p>
<p id="p9723050"><a name="p9723050"></a><a name="p9723050"></a>Short version: datelt</p>
</td>
</tr>
<tr id="row20398591"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p41673198"><a name="p41673198"></a><a name="p41673198"></a>DateLessThanEquals</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p20085873"><a name="p20085873"></a><a name="p20085873"></a>A point in time at which a key stops taking effect</p>
<p id="p46555134"><a name="p46555134"></a><a name="p46555134"></a>Short version: datelteq</p>
</td>
</tr>
<tr id="row16343025"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p48716629"><a name="p48716629"></a><a name="p48716629"></a>DateGreaterThan</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p53732870"><a name="p53732870"></a><a name="p53732870"></a>A point in time at which a key starts to take effect</p>
<p id="p13833782"><a name="p13833782"></a><a name="p13833782"></a>Short version: dategt</p>
</td>
</tr>
<tr id="row57395179"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p18497900"><a name="p18497900"></a><a name="p18497900"></a>DateGreaterThanEquals</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p21934963"><a name="p21934963"></a><a name="p21934963"></a>A point in time at which a key starts to take effect</p>
<p id="p63196939"><a name="p63196939"></a><a name="p63196939"></a>Short version: dategteq</p>
</td>
</tr>
<tr id="row31901541"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p33888044"><a name="p33888044"></a><a name="p33888044"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="32.96%" headers="mcps1.2.4.1.2 "><p id="p60577072"><a name="p60577072"></a><a name="p60577072"></a>Bool</p>
</td>
<td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.4.1.3 "><p id="p7795800"><a name="p7795800"></a><a name="p7795800"></a>Strict Boolean matching</p>
</td>
</tr>
<tr id="row3053341"><td class="cellrowborder" rowspan="2" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p45994103"><a name="p45994103"></a><a name="p45994103"></a>IP address</p>
</td>
<td class="cellrowborder" valign="top" width="32.96%" headers="mcps1.2.4.1.2 "><p id="p34534890"><a name="p34534890"></a><a name="p34534890"></a>IpAddress</p>
</td>
<td class="cellrowborder" valign="top" width="50.44%" headers="mcps1.2.4.1.3 "><p id="p45862685"><a name="p45862685"></a><a name="p45862685"></a>Approved based on the IP address or range</p>
</td>
</tr>
<tr id="row10110982"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p13683196"><a name="p13683196"></a><a name="p13683196"></a>NotIpAddress</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p34597128"><a name="p34597128"></a><a name="p34597128"></a>Denial based on the IP address or range</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>Elements in  **Condition**  are case-sensitive. Date conditions must be in the ISO 8601 format. For details, see [http://www.w3.org/TR/NOTE-datetime](http://www.w3.org/TR/NOTE-datetime).  

A  **Condition**  block \(element\) can contain multiple key value pairs. The following example **Condition**  block specifies requests initiated between 2009-04-16T12:00:00Z and 2009-04-16T15:00:00Z from IP addresses on network segment 192.168.176.0/24 or 192.168.143.0/24:

```
"Condition" : { 
   "DateGreaterThan" : { 
   "aws:CurrentTime" : "2009-04-16T12:00:00Z" 
   },
   "DateLessThan": { 
   "aws:CurrentTime" : "2009-04-16T15:00:00Z" 
   },
   "IpAddress" : { 
   "aws:SourceIp" : ["192.168.176.0/24","192.168.143.0/24"] 
   } 
 }
```

A  **Condition**  block can contain two types of keys:

-   General keys that have nothing to do with  **Action**.
-   S3 service-specific keys associated with  **Action**.

[Table 4](#table61304705)  lists the general keys.

**Table  4**  Common Condition Key

<a name="table61304705"></a>
<table><thead align="left"><tr id="row43801132"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p58230842"><a name="p58230842"></a><a name="p58230842"></a>Condition Key</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p19077772"><a name="p19077772"></a><a name="p19077772"></a>Condition Type</p>
</th>
</tr>
</thead>
<tbody><tr id="row1795723"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p11235870"><a name="p11235870"></a><a name="p11235870"></a>aws:CurrentTime</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p37690286"><a name="p37690286"></a><a name="p37690286"></a>Date</p>
</td>
</tr>
<tr id="row3668256"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p28693301"><a name="p28693301"></a><a name="p28693301"></a>aws:EpochTime</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p42456059"><a name="p42456059"></a><a name="p42456059"></a>Numeric</p>
</td>
</tr>
<tr id="row46560216"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p13281129"><a name="p13281129"></a><a name="p13281129"></a>aws:SecureTransport</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p2029696"><a name="p2029696"></a><a name="p2029696"></a>Boolean</p>
</td>
</tr>
<tr id="row18267264"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p3253400"><a name="p3253400"></a><a name="p3253400"></a>aws:SourceIp</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p62198824"><a name="p62198824"></a><a name="p62198824"></a>IP address</p>
</td>
</tr>
<tr id="row22918509"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p44459941"><a name="p44459941"></a><a name="p44459941"></a>aws:UserAgent</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p44485482"><a name="p44485482"></a><a name="p44485482"></a>String</p>
</td>
</tr>
<tr id="row64825020"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p16335295"><a name="p16335295"></a><a name="p16335295"></a>aws:Referer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p48090498"><a name="p48090498"></a><a name="p48090498"></a>String</p>
</td>
</tr>
</tbody>
</table>

[Table 5](#table14871440)  lists the OBS service-specific keys.

**Table  5**  OBS Action Condition Key

<a name="table14871440"></a>
<table><thead align="left"><tr id="row5680913"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p57500814"><a name="p57500814"></a><a name="p57500814"></a>Action</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p27054376"><a name="p27054376"></a><a name="p27054376"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p43920838"><a name="p43920838"></a><a name="p43920838"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row818129"><td class="cellrowborder" rowspan="3" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p66268464"><a name="p66268464"></a><a name="p66268464"></a>s3:CreateBucket</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p66145356"><a name="p66145356"></a><a name="p66145356"></a>s3:x-amz-acl</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p56173580"><a name="p56173580"></a><a name="p56173580"></a><strong id="b431374214362"><a name="b431374214362"></a><a name="b431374214362"></a>x-amz-acl</strong> can contain the canned ACL.</p>
<p id="p35800173"><a name="p35800173"></a><a name="p35800173"></a>Valid values: private| public-read| public-read-write|authenticated-read|bucket-owner-read|bucket-owner-full-control|log-delivery-write</p>
</td>
</tr>
<tr id="row25664850115252"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p13354193115316"><a name="p13354193115316"></a><a name="p13354193115316"></a>s3:x-amz-grant-permission</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p7947833115316"><a name="p7947833115316"></a><a name="p7947833115316"></a>Not supported</p>
</td>
</tr>
<tr id="row25039621115256"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p22608102115316"><a name="p22608102115316"></a><a name="p22608102115316"></a>s3:LocationConstraint</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p19316974115316"><a name="p19316974115316"></a><a name="p19316974115316"></a>Not supported</p>
</td>
</tr>
<tr id="row53766104"><td class="cellrowborder" rowspan="3" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p60087193"><a name="p60087193"></a><a name="p60087193"></a>s3:ListBucket</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p35224503"><a name="p35224503"></a><a name="p35224503"></a>s3:prefix</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p34612505"><a name="p34612505"></a><a name="p34612505"></a>String</p>
</td>
</tr>
<tr id="row43077096"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p66692715"><a name="p66692715"></a><a name="p66692715"></a>s3:delimiter</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p33400872"><a name="p33400872"></a><a name="p33400872"></a>String</p>
</td>
</tr>
<tr id="row32172395"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p55827183"><a name="p55827183"></a><a name="p55827183"></a>s3:max-keys</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p25707968"><a name="p25707968"></a><a name="p25707968"></a>Numeric</p>
</td>
</tr>
<tr id="row30045120"><td class="cellrowborder" rowspan="3" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p17735662"><a name="p17735662"></a><a name="p17735662"></a>s3:ListBucketVersions</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p27302557"><a name="p27302557"></a><a name="p27302557"></a>s3:prefix</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p64023541"><a name="p64023541"></a><a name="p64023541"></a>String</p>
</td>
</tr>
<tr id="row39340959"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p32501126"><a name="p32501126"></a><a name="p32501126"></a>s3:delimiter</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p15345578"><a name="p15345578"></a><a name="p15345578"></a>String</p>
</td>
</tr>
<tr id="row3892478"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p46855303"><a name="p46855303"></a><a name="p46855303"></a>s3:max-keys</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p37183233"><a name="p37183233"></a><a name="p37183233"></a>Numeric</p>
</td>
</tr>
<tr id="row66213648"><td class="cellrowborder" rowspan="2" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p61705270"><a name="p61705270"></a><a name="p61705270"></a>s3:PutBucketAcl</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p32070944"><a name="p32070944"></a><a name="p32070944"></a>s3:x-amz-acl</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p47609654"><a name="p47609654"></a><a name="p47609654"></a><strong id="b42193815562"><a name="b42193815562"></a><a name="b42193815562"></a>x-amz-acl</strong> can contain the canned ACL.</p>
<p id="p25833710"><a name="p25833710"></a><a name="p25833710"></a>Valid values: private| public-read| public-read-write|authenticated-read|bucket-owner-read|bucket-owner-full-control|log-delivery-write</p>
</td>
</tr>
<tr id="row32406958115327"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p20161470115344"><a name="p20161470115344"></a><a name="p20161470115344"></a>s3:x-amz-grant-permission</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p22466403115344"><a name="p22466403115344"></a><a name="p22466403115344"></a>Not supported</p>
</td>
</tr>
<tr id="row31176802"><td class="cellrowborder" rowspan="5" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p42293001"><a name="p42293001"></a><a name="p42293001"></a>s3:PutObject</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3181077"><a name="p3181077"></a><a name="p3181077"></a>s3:x-amz-acl</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p56340718"><a name="p56340718"></a><a name="p56340718"></a><strong id="b1851016250567"><a name="b1851016250567"></a><a name="b1851016250567"></a>x-amz-acl</strong> can contain the canned ACL.</p>
<p id="p37304419"><a name="p37304419"></a><a name="p37304419"></a>Valid values: private| public-read| public-read-write|authenticated-read|bucket-owner-read|bucket-owner-full-control|log-delivery-write</p>
</td>
</tr>
<tr id="row195451"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p15831589"><a name="p15831589"></a><a name="p15831589"></a>s3:x-amz-copy-source</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p4815152883710"><a name="p4815152883710"></a><a name="p4815152883710"></a>String</p>
<p id="p516273613372"><a name="p516273613372"></a><a name="p516273613372"></a>Example format:</p>
<p id="p7290323"><a name="p7290323"></a><a name="p7290323"></a><strong id="b17192438378"><a name="b17192438378"></a><a name="b17192438378"></a>/bucketname/keyname</strong></p>
</td>
</tr>
<tr id="row65612911"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p13045599"><a name="p13045599"></a><a name="p13045599"></a>s3:x-amz-metadata-di</p>
<p id="p50301533"><a name="p50301533"></a><a name="p50301533"></a>rective</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p47892361"><a name="p47892361"></a><a name="p47892361"></a>Valid values: COPY| REPLACE</p>
</td>
</tr>
<tr id="row1640328811547"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p35667538115436"><a name="p35667538115436"></a><a name="p35667538115436"></a>s3:x-amz-grant-permission</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p3389448115436"><a name="p3389448115436"></a><a name="p3389448115436"></a>Not supported</p>
</td>
</tr>
<tr id="row4607717611542"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p57997724115442"><a name="p57997724115442"></a><a name="p57997724115442"></a>s3:x-amz-storage-class</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p195166115442"><a name="p195166115442"></a><a name="p195166115442"></a>Not supported</p>
</td>
</tr>
<tr id="row28378065"><td class="cellrowborder" rowspan="2" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16921890"><a name="p16921890"></a><a name="p16921890"></a>s3:PutObjectAcl</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p28495844"><a name="p28495844"></a><a name="p28495844"></a>s3:x-amz-acl</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p26462014"><a name="p26462014"></a><a name="p26462014"></a><strong id="b2653173485619"><a name="b2653173485619"></a><a name="b2653173485619"></a>x-amz-acl</strong> can contain the canned ACL.</p>
<p id="p36831540"><a name="p36831540"></a><a name="p36831540"></a>Valid values: private| public-read| public-read-write|authenticated-read|bucket-owner-read|bucket-owner-full-control|log-delivery-write</p>
</td>
</tr>
<tr id="row17061708115450"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p3304895115457"><a name="p3304895115457"></a><a name="p3304895115457"></a>s3:x-amz-grant-permission</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p66369966115457"><a name="p66369966115457"></a><a name="p66369966115457"></a>Not supported</p>
</td>
</tr>
<tr id="row63048409"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6647517"><a name="p6647517"></a><a name="p6647517"></a>s3:GetObjectVersion</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1577968"><a name="p1577968"></a><a name="p1577968"></a>s3:VersionId</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p60706621"><a name="p60706621"></a><a name="p60706621"></a>String</p>
</td>
</tr>
<tr id="row9488680"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p30385596"><a name="p30385596"></a><a name="p30385596"></a>s3:GetObjectVersionAcl</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p45314205"><a name="p45314205"></a><a name="p45314205"></a>s3:VersionId</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p46571954"><a name="p46571954"></a><a name="p46571954"></a>String</p>
</td>
</tr>
<tr id="row16494403"><td class="cellrowborder" rowspan="3" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p60978306"><a name="p60978306"></a><a name="p60978306"></a>s3:PutObjectVersionAcl</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p40295786"><a name="p40295786"></a><a name="p40295786"></a>s3:VersionId</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p42733218"><a name="p42733218"></a><a name="p42733218"></a>String</p>
</td>
</tr>
<tr id="row49054643"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p14003175"><a name="p14003175"></a><a name="p14003175"></a>s3:x-amz-acl</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p60515391"><a name="p60515391"></a><a name="p60515391"></a><strong id="b5496340175617"><a name="b5496340175617"></a><a name="b5496340175617"></a>x-amz-acl</strong> can contain the canned ACL.</p>
<p id="p7767612"><a name="p7767612"></a><a name="p7767612"></a>Valid values: private| public-read| public-read-write|authenticated-read|bucket-owner-read|bucket-owner-full-control|log-delivery-write</p>
</td>
</tr>
<tr id="row13860262115516"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p64419481115532"><a name="p64419481115532"></a><a name="p64419481115532"></a>s3:x-amz-grant-permission</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p50595509115532"><a name="p50595509115532"></a><a name="p50595509115532"></a>Not supported</p>
</td>
</tr>
<tr id="row2799652"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p25445245"><a name="p25445245"></a><a name="p25445245"></a>s3:DeleteObjectVersion</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p47798963"><a name="p47798963"></a><a name="p47798963"></a>s3:VersionId</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p46510765"><a name="p46510765"></a><a name="p46510765"></a>String</p>
</td>
</tr>
<tr id="row24023584115536"><td class="cellrowborder" rowspan="4" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1754097111565"><a name="p1754097111565"></a><a name="p1754097111565"></a>s3:*</p>
<p id="p2365101111565"><a name="p2365101111565"></a><a name="p2365101111565"></a>(Actions or any of the S3 Actions)</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p5745940911560"><a name="p5745940911560"></a><a name="p5745940911560"></a>s3:signatureversion</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2370054711560"><a name="p2370054711560"></a><a name="p2370054711560"></a>Not supported</p>
</td>
</tr>
<tr id="row26068960115540"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p3072095511560"><a name="p3072095511560"></a><a name="p3072095511560"></a>s3:authType</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p536943711560"><a name="p536943711560"></a><a name="p536943711560"></a>Not supported</p>
</td>
</tr>
<tr id="row30617701115544"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p2200603111560"><a name="p2200603111560"></a><a name="p2200603111560"></a>s3:signatureAge</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p3765812411560"><a name="p3765812411560"></a><a name="p3765812411560"></a>Not supported</p>
</td>
</tr>
<tr id="row6883371115548"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p524728311560"><a name="p524728311560"></a><a name="p524728311560"></a>s3:x-amz-content-sha256</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p2237677211560"><a name="p2237677211560"></a><a name="p2237677211560"></a>Not supported</p>
</td>
</tr>
</tbody>
</table>

## Policy Permission Judgment Logic<a name="section15616050"></a>

A policy results in a default deny if conditions in any statement of the policy are not met. If all conditions in statements are met, the policy results in either an allow or an explicit deny. If a bucket policy contains multiple statements, the policy determines which statement prevails according to the following rules:

1. If conditions in any statement of a policy are not met, the policy results in a default deny.

2. An explicit deny overrides allows.

3. An allow overrides default denies.

4. Statements can be in any order in a policy.

**Table  6**  Statement results

<a name="table66734104"></a>
<table><thead align="left"><tr id="row44885282"><th class="cellrowborder" valign="top" width="23.5%" id="mcps1.2.3.1.1"><p id="p11829216"><a name="p11829216"></a><a name="p11829216"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="76.5%" id="mcps1.2.3.1.2"><p id="p18642443"><a name="p18642443"></a><a name="p18642443"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row33642890"><td class="cellrowborder" valign="top" width="23.5%" headers="mcps1.2.3.1.1 "><p id="p40719558"><a name="p40719558"></a><a name="p40719558"></a>explicit deny</p>
</td>
<td class="cellrowborder" valign="top" width="76.5%" headers="mcps1.2.3.1.2 "><p id="p1458616568388"><a name="p1458616568388"></a><a name="p1458616568388"></a>A statement defines effect="deny".</p>
<p id="p9949862"><a name="p9949862"></a><a name="p9949862"></a>All requests for resources to which the statement applies are denied. No permission is returned.</p>
</td>
</tr>
<tr id="row22439895"><td class="cellrowborder" valign="top" width="23.5%" headers="mcps1.2.3.1.1 "><p id="p5692201"><a name="p5692201"></a><a name="p5692201"></a>allow</p>
</td>
<td class="cellrowborder" valign="top" width="76.5%" headers="mcps1.2.3.1.2 "><p id="p1519515073913"><a name="p1519515073913"></a><a name="p1519515073913"></a>A statement defines effect="allow".</p>
<p id="p58415123"><a name="p58415123"></a><a name="p58415123"></a>All requests for resources to which the statement applies are allowed.</p>
</td>
</tr>
<tr id="row55974065"><td class="cellrowborder" valign="top" width="23.5%" headers="mcps1.2.3.1.1 "><p id="p37605427"><a name="p37605427"></a><a name="p37605427"></a>default deny</p>
</td>
<td class="cellrowborder" valign="top" width="76.5%" headers="mcps1.2.3.1.2 "><p id="p26140770"><a name="p26140770"></a><a name="p26140770"></a>Conditions defined in a statement are not met. Requests are denied.</p>
</td>
</tr>
</tbody>
</table>

## URL Validation Settings<a name="ole_link35"></a>

OBS is charged based on the services that you use. To prevent user data from being stolen, OBS supports URL validation based on HTTP headers. OBS also supports both whitelist and blacklist settings.

-   Whitelist settings

    Users can set a whitelist to allow requests from the websites added in the whitelist and deny requests from any other website.

    For the requests that are initialized from browsers' address boxes, that is, those HTTP requests with a blank  **referer**, users can add the **$\{null\}** field to **"aws:Referer"** of **Condition** to specify whether to allow the requests with a blank **referer**.

    Set a whitelist based on the following policy setting:

    ```
    "Statement":[
        {"Sid": "1",
         "Effect": "Allow",
         "Principal": {"CanonicalUser":["*"]},
         "Action": "s3:*",
         "Resource":["arn:aws:s3:::bucket/*"],
        },
        {"Sid":"2",
         "Effect":"Deny",
         "Principal":{"CanonicalUser":["*"]},
         "Action":["s3:*"],
         "Resource":["arn:aws:s3:::bucket/*"],                             "Condition":{
             "StringNotEquals":
             {"aws:Referer":["www.example01.com","${null}"]}
          }
        }
    ]
    ```

    If you set a whitelist in this way, you can perform operations on resources in buckets only when the value of the  **referer** parameter is **www.example01.com**  or is blank.


-   Blacklist settings

    You can refer to the following policy settings to set a blacklist for access.

    ```
    "Statement":[ 
         {"Sid":"1", 
          "Effect":"Deny", 
          "Principal":{"CanonicalUser":["*"]}, 
          "Action":["s3:*"], 
          "Resource":["arn:aws:s3:::bucket/*"],                             "Condition":{ 
              "StringEquals": 
              {"aws:Referer":["www.example01.com","www.example02.com"]} 
           } 
         } 
     ]
    ```

    If you set a blacklist in this way, you cannot perform operations on resources in buckets when the value of the  **referer** parameter is **www.example01.com** or **www.example02.com**.


