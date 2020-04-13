# External Buckets Overview<a name="obs_03_0434"></a>

The bucket owner can authorize other accounts the read and write access to the bucket. If you are authorized with such permissions, you can add the bucket on OBS Browser as an external bucket. After the external bucket is added successfully, you can operate the bucket on OBS Browser. For details about what actions you can perform on the external bucket, check the permission settings.

## Authorizing Permissions Required for Adding a Bucket as an External Bucket on OBS Browser<a name="section1914573815229"></a>

The read and write access to a bucket can be granted through the bucket ACL or bucket policy.

Permissions controlled by a bucket ACL are as follows:

**Table  1**  Permissions controlled by a bucket ACL

<a name="table183716545593"></a>
<table><thead align="left"><tr id="row10426205416593"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.4.1.1"><p id="p6426165418599"><a name="p6426165418599"></a><a name="p6426165418599"></a>Bucket ACL</p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.4.1.2"><p id="p1842615544595"><a name="p1842615544595"></a><a name="p1842615544595"></a>Option</p>
</th>
<th class="cellrowborder" valign="top" width="66.66666666666667%" id="mcps1.2.4.1.3"><p id="p8428125435912"><a name="p8428125435912"></a><a name="p8428125435912"></a>Mapped Action in a Custom Bucket Policy</p>
</th>
</tr>
</thead>
<tbody><tr id="row942885416596"><td class="cellrowborder" rowspan="2" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.1 "><p id="p184281354195919"><a name="p184281354195919"></a><a name="p184281354195919"></a>Access to Bucket</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="p54287547598"><a name="p54287547598"></a><a name="p54287547598"></a>Read</p>
</td>
<td class="cellrowborder" valign="top" width="66.66666666666667%" headers="mcps1.2.4.1.3 "><a name="ul1242814546590"></a><a name="ul1242814546590"></a><ul id="ul1242814546590"><li>ListBucket</li><li>ListBucketVersions</li><li>ListBucketMultipartUploads</li></ul>
</td>
</tr>
<tr id="row1242885414593"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p134281454115913"><a name="p134281454115913"></a><a name="p134281454115913"></a>Write</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><a name="ul84281154125913"></a><a name="ul84281154125913"></a><ul id="ul84281154125913"><li>PutObject</li><li>DeleteObject</li><li>DeleteObjectVersion</li></ul>
</td>
</tr>
<tr id="row17428135413591"><td class="cellrowborder" rowspan="2" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.1 "><p id="p174281154105920"><a name="p174281154105920"></a><a name="p174281154105920"></a>Access to ACL</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="p1142885415597"><a name="p1142885415597"></a><a name="p1142885415597"></a>Read</p>
</td>
<td class="cellrowborder" valign="top" width="66.66666666666667%" headers="mcps1.2.4.1.3 "><p id="p1842815542599"><a name="p1842815542599"></a><a name="p1842815542599"></a>GetBucketAcl</p>
</td>
</tr>
<tr id="row15428654125911"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1742825465912"><a name="p1742825465912"></a><a name="p1742825465912"></a>Write</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p2429554125918"><a name="p2429554125918"></a><a name="p2429554125918"></a>PutBucketAcl</p>
</td>
</tr>
</tbody>
</table>

Permissions controlled by a standard bucket policy are as follows:

**Table  2**  Permissions controlled by a standard bucket policy

<a name="table12248152111227"></a>
<table><thead align="left"><tr id="row15249821152217"><th class="cellrowborder" valign="top" width="22.35%" id="mcps1.2.4.1.1"><p id="p122491621102215"><a name="p122491621102215"></a><a name="p122491621102215"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="37.65%" id="mcps1.2.4.1.2"><p id="p9249112142212"><a name="p9249112142212"></a><a name="p9249112142212"></a>Public Read</p>
</th>
<th class="cellrowborder" valign="top" width="40%" id="mcps1.2.4.1.3"><p id="p14249421172212"><a name="p14249421172212"></a><a name="p14249421172212"></a>Public Read and Write</p>
</th>
</tr>
</thead>
<tbody><tr id="row724919215226"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.4.1.1 "><p id="p102491321142216"><a name="p102491321142216"></a><a name="p102491321142216"></a>Effect</p>
</td>
<td class="cellrowborder" valign="top" width="37.65%" headers="mcps1.2.4.1.2 "><p id="p02496219224"><a name="p02496219224"></a><a name="p02496219224"></a>Allow</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p424962162212"><a name="p424962162212"></a><a name="p424962162212"></a>Allow</p>
</td>
</tr>
<tr id="row1224915215221"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.4.1.1 "><p id="p824919216225"><a name="p824919216225"></a><a name="p824919216225"></a>Principal</p>
</td>
<td class="cellrowborder" valign="top" width="37.65%" headers="mcps1.2.4.1.2 "><p id="p12503210220"><a name="p12503210220"></a><a name="p12503210220"></a>* (Any user)</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p132503214228"><a name="p132503214228"></a><a name="p132503214228"></a>* (Any user)</p>
</td>
</tr>
<tr id="row5250121102214"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.4.1.1 "><p id="p1625082192215"><a name="p1625082192215"></a><a name="p1625082192215"></a>Resources</p>
</td>
<td class="cellrowborder" valign="top" width="37.65%" headers="mcps1.2.4.1.2 "><p id="p125022172220"><a name="p125022172220"></a><a name="p125022172220"></a>* (All objects in a bucket)</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p3250112172220"><a name="p3250112172220"></a><a name="p3250112172220"></a>* (All objects in a bucket)</p>
</td>
</tr>
<tr id="row14250821122214"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.4.1.1 "><p id="p1125052118223"><a name="p1125052118223"></a><a name="p1125052118223"></a>Actions</p>
</td>
<td class="cellrowborder" valign="top" width="37.65%" headers="mcps1.2.4.1.2 "><a name="ul1512955514"></a><a name="ul1512955514"></a><ul id="ul1512955514"><li>GetObject</li><li>GetObjectVersion</li><li>ListBucket</li></ul>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><a name="ul5350174995516"></a><a name="ul5350174995516"></a><ul id="ul5350174995516"><li>GetObject</li><li>GetObjectVersion</li><li>PutObject</li><li>DeleteObject</li><li>DeleteObjectVersion</li><li>ListBucket</li></ul>
</td>
</tr>
<tr id="row122501121162216"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.4.1.1 "><p id="p22501217226"><a name="p22501217226"></a><a name="p22501217226"></a>Conditions</p>
</td>
<td class="cellrowborder" valign="top" width="37.65%" headers="mcps1.2.4.1.2 "><p id="p132501521172219"><a name="p132501521172219"></a><a name="p132501521172219"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p1325042111223"><a name="p1325042111223"></a><a name="p1325042111223"></a>N/A</p>
</td>
</tr>
</tbody>
</table>

If a custom bucket policy is used to authorize such permissions, the ListBucket, GetObject, and GetObjectVersion actions must be allowed. More actions can be allowed according to your actual needs.

## Operations That Can Be Performed on the External Bucket<a name="section7143122229"></a>

Operations that can be performed by the authorized user on the external bucket:

-   You can add an external bucket but cannot restore objects from the Cold storage class in the bucket. You can view the object restoration status only when the owner of those objects authorizes you the permission to read the objects.
-   You \(the user who adds the bucket\) can perform only authorized actions on original objects in the bucket. If you want to have additional operation permissions for objects in the bucket, you need to have the permissions authorized by the object owner.
-   If you upload an object to the added external bucket, the read access to the object and the object ACL will be automatically authorized to the bucket owner and configured in the object ACL settings.
-   If you upload an encrypted object to the added external bucket, the bucket owner cannot access the object because the bucket owner does not have the key.
-   To download an object from the external bucket, the user who adds the bucket must be authorized the permission to read the object, and encrypted objects cannot be downloaded.

