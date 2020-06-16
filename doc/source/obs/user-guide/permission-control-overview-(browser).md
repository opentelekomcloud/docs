# Overview<a name="obs_03_0062"></a>

OBS Browser supports permission control based on bucket policies, bucket ACLs, and object ACLs.

-   Bucket policy: A bucket policy applies to the configured OBS bucket and objects in the bucket. An OBS bucket owner can use a bucket policy to grant permissions of buckets and objects in the buckets to IAM users or other accounts.
-   Access Control List \(ACL\): OBS provides ACL settings at bucket and object levels. Bucket and object ACLs are attached to accounts.

## Bucket Policy<a name="section1898792812813"></a>

A bucket owner can edit a bucket policy to implement fine-grained bucket access control.

A bucket policy can be used to control access to the bucket and objects in the bucket. Specifically, you can define the effect, authorized users, resources, actions, and conditions of a bucket policy. Permissions attached to a bucket apply to all the objects in the bucket. After a bucket policy is created, access requests to the bucket are controlled by the bucket policy. The bucket policy controls access requests by allowing or denying the requests.

## ACL<a name="section685651513912"></a>

A bucket or object ACL can assign the following users the read and write permissions to OBS resources:

**Table  1**  Users supported by OBS

<a name="table177445813209"></a>
<table><thead align="left"><tr id="row5236185882019"><th class="cellrowborder" valign="top" width="27%" id="mcps1.2.3.1.1"><p id="p4236185812209"><a name="p4236185812209"></a><a name="p4236185812209"></a>Principal</p>
</th>
<th class="cellrowborder" valign="top" width="73%" id="mcps1.2.3.1.2"><p id="p0236185811200"><a name="p0236185811200"></a><a name="p0236185811200"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14236115815207"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p4237195812018"><a name="p4237195812018"></a><a name="p4237195812018"></a>Owner</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p82371758102019"><a name="p82371758102019"></a><a name="p82371758102019"></a>The owner of a bucket is the account that created the bucket. The bucket owner has all bucket access permissions by default. The read and write permissions to the bucket ACL are permanently available to the bucket owner, and cannot be modified.</p>
<p id="p108801457143318"><a name="p108801457143318"></a><a name="p108801457143318"></a>The owner of an object is the account that uploads the object, who may not be the owner of the bucket to which the object belongs. The object owner has the read access to the object, as well as the read and write permission to the object ACL, and such access permissions cannot be modified.</p>
<div class="notice" id="note16704211185110"><a name="note16704211185110"></a><a name="note16704211185110"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p11704131114517"><a name="p11704131114517"></a><a name="p11704131114517"></a>Do not modify the bucket owner's read and write access permissions for the bucket.</p>
</div></div>
</td>
</tr>
<tr id="row0239105872015"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p2239658142016"><a name="p2239658142016"></a><a name="p2239658142016"></a>Anonymous User</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p112397589206"><a name="p112397589206"></a><a name="p112397589206"></a>Unregistered common users of cloud services. If the permissions to access a bucket or an object are granted to anonymous users, everyone can access the object or bucket without identity authentication.</p>
<div class="notice" id="note1437509296"><a name="note1437509296"></a><a name="note1437509296"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p122391580206"><a name="p122391580206"></a><a name="p122391580206"></a>If the permissions to access a bucket or an object are granted to anonymous users, everyone can access the object or bucket without identity authentication.</p>
</div></div>
</td>
</tr>
<tr id="row112391958122020"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p1123911582207"><a name="p1123911582207"></a><a name="p1123911582207"></a>Registered User</p>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p6239185816209"><a name="p6239185816209"></a><a name="p6239185816209"></a>A registered user refers to any account registered with the cloud services, excluding IAM users or user groups created by any account. To obtain access permissions, a registered user must be authenticated (AK and SK are used for the identity authentication). If the registered user group is granted with the write permission for a bucket, any registered and authenticated cloud service account can upload objects to the bucket, overwrite objects in the bucket, and delete objects from the bucket.</p>
</td>
</tr>
<tr id="row1123945814203"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.3.1.1 "><p id="p19239165817208"><a name="p19239165817208"></a><a name="p19239165817208"></a>Log Delivery User</p>
<div class="note" id="note0623203504215"><a name="note0623203504215"></a><a name="note0623203504215"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p12623113515421"><a name="p12623113515421"></a><a name="p12623113515421"></a>Only the bucket ACL supports authorizing permissions to the log delivery user.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="73%" headers="mcps1.2.3.1.2 "><p id="p11239175822012"><a name="p11239175822012"></a><a name="p11239175822012"></a>A log delivery user only delivers access logs of buckets and objects to the specified target bucket. OBS does not create or upload any file to a bucket automatically. Therefore, if you want to record bucket access logs, you need to grant the permission to the log delivery user who will deliver the access logs to your specified target bucket. The user only delivers logs within the service scope of OBS.</p>
<div class="notice" id="note71171158122010"><a name="note71171158122010"></a><a name="note71171158122010"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p7241158152013"><a name="p7241158152013"></a><a name="p7241158152013"></a>After logging is enabled, the bucket write permission, as well as the ACL read permission for the target bucket will be enabled automatically for the log delivery user. If you manually disable such permissions, bucket logging fails.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

[Table 2](#table28226836)  lists the access permissions controlled by a bucket ACL.

**Table  2**  Access permissions controlled by a bucket ACL

<a name="table28226836"></a>
<table><thead align="left"><tr id="row61083978"><th class="cellrowborder" valign="top" width="19.55%" id="mcps1.2.4.1.1"><p id="p55592582172343"><a name="p55592582172343"></a><a name="p55592582172343"></a>Permission</p>
</th>
<th class="cellrowborder" valign="top" width="14.97%" id="mcps1.2.4.1.2"><p id="p48855171"><a name="p48855171"></a><a name="p48855171"></a>Option</p>
</th>
<th class="cellrowborder" valign="top" width="65.48%" id="mcps1.2.4.1.3"><p id="p64954777"><a name="p64954777"></a><a name="p64954777"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row26845555"><td class="cellrowborder" rowspan="2" valign="top" width="19.55%" headers="mcps1.2.4.1.1 "><p id="p6705326172343"><a name="p6705326172343"></a><a name="p6705326172343"></a>Access to Bucket</p>
</td>
<td class="cellrowborder" valign="top" width="14.97%" headers="mcps1.2.4.1.2 "><p id="p27006329"><a name="p27006329"></a><a name="p27006329"></a>Read</p>
</td>
<td class="cellrowborder" valign="top" width="65.48%" headers="mcps1.2.4.1.3 "><p id="p40029077"><a name="p40029077"></a><a name="p40029077"></a>A grantee with the read access to a bucket can obtain the list of objects in the bucket and the metadata of the bucket.</p>
</td>
</tr>
<tr id="row21129772"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p33789992"><a name="p33789992"></a><a name="p33789992"></a>Write</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p52634865"><a name="p52634865"></a><a name="p52634865"></a>A grantee with the write access to a bucket can upload, overwrite, and delete any object in the bucket.</p>
</td>
</tr>
<tr id="row35565678"><td class="cellrowborder" rowspan="2" valign="top" width="19.55%" headers="mcps1.2.4.1.1 "><p id="p46542350172415"><a name="p46542350172415"></a><a name="p46542350172415"></a>Access to ACL</p>
</td>
<td class="cellrowborder" valign="top" width="14.97%" headers="mcps1.2.4.1.2 "><p id="p62247688"><a name="p62247688"></a><a name="p62247688"></a>Read</p>
</td>
<td class="cellrowborder" valign="top" width="65.48%" headers="mcps1.2.4.1.3 "><p id="p8897958"><a name="p8897958"></a><a name="p8897958"></a>A grantee with the read access to a bucket ACL can obtain the ACL of the bucket.</p>
<p id="p12972762"><a name="p12972762"></a><a name="p12972762"></a>The bucket owner has this permission permanently by default.</p>
</td>
</tr>
<tr id="row49646001"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p61903120"><a name="p61903120"></a><a name="p61903120"></a>Write</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p48096812"><a name="p48096812"></a><a name="p48096812"></a>A grantee with the write access to a bucket ACL can update the ACL of the bucket.</p>
<p id="p30218124"><a name="p30218124"></a><a name="p30218124"></a>The bucket owner has this permission permanently by default.</p>
</td>
</tr>
</tbody>
</table>

[Table 3](#table63381242464)  lists the access permissions of an object ACL.

**Table  3**  Access permissions controlled by an object ACL

<a name="table63381242464"></a>
<table><thead align="left"><tr id="en-us_topic_0071293615_row61083978"><th class="cellrowborder" valign="top" width="19.55%" id="mcps1.2.4.1.1"><p id="p3671603217261"><a name="p3671603217261"></a><a name="p3671603217261"></a>Permission</p>
</th>
<th class="cellrowborder" valign="top" width="14.97%" id="mcps1.2.4.1.2"><p id="en-us_topic_0071293615_p48855171"><a name="en-us_topic_0071293615_p48855171"></a><a name="en-us_topic_0071293615_p48855171"></a>Option</p>
</th>
<th class="cellrowborder" valign="top" width="65.48%" id="mcps1.2.4.1.3"><p id="en-us_topic_0071293615_p64954777"><a name="en-us_topic_0071293615_p64954777"></a><a name="en-us_topic_0071293615_p64954777"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0071293615_row26845555"><td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.2.4.1.1 "><p id="p2120863117261"><a name="p2120863117261"></a><a name="p2120863117261"></a>Access to Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.97%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0071293615_p27006329"><a name="en-us_topic_0071293615_p27006329"></a><a name="en-us_topic_0071293615_p27006329"></a>Read</p>
</td>
<td class="cellrowborder" valign="top" width="65.48%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0071293615_p40029077"><a name="en-us_topic_0071293615_p40029077"></a><a name="en-us_topic_0071293615_p40029077"></a>A grantee with the read access to an object can obtain the content of the object and the metadata of the object.</p>
</td>
</tr>
<tr id="en-us_topic_0071293615_row35565678"><td class="cellrowborder" rowspan="2" valign="top" width="19.55%" headers="mcps1.2.4.1.1 "><p id="p3315846717261"><a name="p3315846717261"></a><a name="p3315846717261"></a>Access to ACL</p>
</td>
<td class="cellrowborder" valign="top" width="14.97%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0071293615_p62247688"><a name="en-us_topic_0071293615_p62247688"></a><a name="en-us_topic_0071293615_p62247688"></a>Read</p>
</td>
<td class="cellrowborder" valign="top" width="65.48%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0071293615_p8897958"><a name="en-us_topic_0071293615_p8897958"></a><a name="en-us_topic_0071293615_p8897958"></a>A grantee with the read access to an object ACL can obtain the ACL of the object.</p>
<p id="en-us_topic_0071293615_p12972762"><a name="en-us_topic_0071293615_p12972762"></a><a name="en-us_topic_0071293615_p12972762"></a>The object owner has this permission permanently by default.</p>
</td>
</tr>
<tr id="en-us_topic_0071293615_row49646001"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0071293615_p61903120"><a name="en-us_topic_0071293615_p61903120"></a><a name="en-us_topic_0071293615_p61903120"></a>Write</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0071293615_p48096812"><a name="en-us_topic_0071293615_p48096812"></a><a name="en-us_topic_0071293615_p48096812"></a>A grantee with the write access to an object ACL can update the ACL of the object.</p>
<p id="en-us_topic_0071293615_p30218124"><a name="en-us_topic_0071293615_p30218124"></a><a name="en-us_topic_0071293615_p30218124"></a>The object owner has this permission permanently by default.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>Every time you change the bucket or object access permission setting in an ACL, it overwrites the existing setting instead of adding a new access permission to the bucket or object.  
>Fragment management refers to the deletion of fragments. For the bucket owner and users who have the permission to initiate multipart tasks, deleting fragments is not restricted by bucket ACL settings. If a user has the permission to write, the user also has the permission to initiate multipart tasks.  

