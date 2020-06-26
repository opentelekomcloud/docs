# Bucket Policy and Object Policy<a name="en-us_topic_0045853745"></a>

## Bucket Owner and Object Owner<a name="section4574154145010"></a>

The owner of a bucket is the account that created the bucket. If the bucket is created by an IAM user under the account, the bucket owner is the account instead of the IAM user.

The owner of an object is the account that uploads the object, who may not be the owner of the bucket to which the object belongs. For example, account  **B**  is granted the permission to access a bucket of account  **A**, and account  **B**  uploads a file to the bucket. In that case, instead of the bucket owner account  **A**, account  **B**  is the owner of the object.

## Bucket Policy<a name="section1825740772"></a>

A bucket policy is attached to a bucket and objects in the bucket. By leveraging bucket policies, the owner of a bucket can authorize IAM users or other accounts the permissions to operate the bucket and objects in the bucket.

**Bucket Policy Application Scenarios**:

-   If no  IAM policies  is used for access permission control and you want to authorize other accounts the permission to access your OBS resources, you can use bucket policies to authorize such permissions.
-   If you want to authorize IAM users different access permissions to different buckets, you can configure different bucket policies for buckets.
-   If you want to authorize other accounts the permission to access your buckets, you can use bucket policies to authorize such permissions.

**Standard Bucket Policies**:

There are three options for standard bucket policies.

-   **Private**: No access beyond the bucket ACL settings is granted.
-   **Public Read**: Any user can read objects in the bucket.
-   **Public Read and Write**: Any user can read, write, and delete objects in the bucket.

After a bucket is created, the default bucket policy is  **Private**. Only the bucket owner has the full control permissions over the bucket. To ensure data security, it is recommended that you do not use the  **Public Read**  or  **Public Read and Write**  policies.

**Table  1**  Standard bucket policies

<a name="table12248152111227"></a>
<table><thead align="left"><tr id="row15249821152217"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="p122491621102215"><a name="p122491621102215"></a><a name="p122491621102215"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p1249182111225"><a name="p1249182111225"></a><a name="p1249182111225"></a>Private</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.5.1.3"><p id="p9249112142212"><a name="p9249112142212"></a><a name="p9249112142212"></a>Public Read</p>
</th>
<th class="cellrowborder" valign="top" width="34%" id="mcps1.2.5.1.4"><p id="p14249421172212"><a name="p14249421172212"></a><a name="p14249421172212"></a>Public Read and Write</p>
</th>
</tr>
</thead>
<tbody><tr id="row724919215226"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p102491321142216"><a name="p102491321142216"></a><a name="p102491321142216"></a>Effect</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p13249112115225"><a name="p13249112115225"></a><a name="p13249112115225"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.5.1.3 "><p id="p02496219224"><a name="p02496219224"></a><a name="p02496219224"></a>Allow</p>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.5.1.4 "><p id="p424962162212"><a name="p424962162212"></a><a name="p424962162212"></a>Allow</p>
</td>
</tr>
<tr id="row1224915215221"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p824919216225"><a name="p824919216225"></a><a name="p824919216225"></a>Principal</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p913548162513"><a name="p913548162513"></a><a name="p913548162513"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.5.1.3 "><p id="p12503210220"><a name="p12503210220"></a><a name="p12503210220"></a>* (Any user)</p>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.5.1.4 "><p id="p132503214228"><a name="p132503214228"></a><a name="p132503214228"></a>* (Any user)</p>
</td>
</tr>
<tr id="row5250121102214"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p1625082192215"><a name="p1625082192215"></a><a name="p1625082192215"></a>Resources</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p92501212228"><a name="p92501212228"></a><a name="p92501212228"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.5.1.3 "><p id="p125022172220"><a name="p125022172220"></a><a name="p125022172220"></a>* (All objects in a bucket)</p>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.5.1.4 "><p id="p3250112172220"><a name="p3250112172220"></a><a name="p3250112172220"></a>* (All objects in a bucket)</p>
</td>
</tr>
<tr id="row14250821122214"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p1125052118223"><a name="p1125052118223"></a><a name="p1125052118223"></a>Actions</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p113541515304"><a name="p113541515304"></a><a name="p113541515304"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.5.1.3 "><a name="ul1512955514"></a><a name="ul1512955514"></a><ul id="ul1512955514"><li>GetObject</li><li>GetObjectVersion</li><li>ListBucket</li></ul>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.5.1.4 "><a name="ul5350174995516"></a><a name="ul5350174995516"></a><ul id="ul5350174995516"><li>GetObject</li><li>GetObjectVersion</li><li>PutObject</li><li>DeleteObject</li><li>DeleteObjectVersion</li><li>ListBucket</li></ul>
</td>
</tr>
<tr id="row122501121162216"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p22501217226"><a name="p22501217226"></a><a name="p22501217226"></a>Conditions</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p10924191511307"><a name="p10924191511307"></a><a name="p10924191511307"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.5.1.3 "><p id="p132501521172219"><a name="p132501521172219"></a><a name="p132501521172219"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.5.1.4 "><p id="p1325042111223"><a name="p1325042111223"></a><a name="p1325042111223"></a>N/A</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>For buckets whose version is 3.0, the default permissions of  **Public Read**  and  **Public Read and Write**  are updated to solve the problem that buckets fail to be added to OBS Browser due to permission limitations.  
>-   Added the ListBucket permission to the  **Public Read**  policy.  
>-   Added the ListBucket permission to the  **Public Read and Write**  policy.  
>-   If you want to add an external bucket to OBS Browser, manually update the configuration of standard bucket policies.  

**Custom Bucket Policy**:

The following three modes are provided to facilitate quick configuration:

-   **Read-only**: With the  **Read-only**  mode, you only need to specify the  **Principal**  \(authorized users\). Then the authorized users have the read permission for the bucket and objects in the bucket, and can perform all GET operations on these resources.
-   **Read and write**: With the  **Read and write**  mode, you only need to specify the  **Principal**  \(authorized users\). Then the authorized users have the full control permissions for the bucket and objects in the bucket, and can perform any operation on these resources.
-   **Customized**: With the  **Customized**  mode, you can define the specific operation permissions that you want to authorize to users and accounts by configuring the parameters of  **Effect**,  **Principal**,  **Resources**,  **Actions**, and  **Conditions**. 

>![](/images/icon-note.gif) **NOTE:**   
>On OBS Console, when you use the custom bucket policy to authorize other users with resource operation permissions, you also need to authorize the users with the bucket read permission  **ListBucket**  \(leave the resource name blank to indicate that the policy takes effect on the entire bucket\). Otherwise, the users have no permission to access the bucket.  

## Object Policy<a name="section0354920819"></a>

An object policy is a policy that applies to objects in a bucket. In a bucket policy, you can specify a set of objects as the resources to which the bucket policy applies, or you can use asterisk symbol \(\*\) to indicate all objects in the bucket. To configure an object policy, select an object, and then configure the object policy directly for the object.

