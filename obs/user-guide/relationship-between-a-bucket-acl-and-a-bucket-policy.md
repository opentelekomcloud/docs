# Relationship Between a Bucket ACL and a Bucket Policy<a name="obs_03_0325"></a>

## Mapping Relationship Between Bucket ACLs and Bucket Policies<a name="section9370125413594"></a>

Bucket ACLs are used to control basic read and write access permissions for buckets. Custom settings of bucket policies support more actions that can be performed on buckets. Bucket policies are supplements to bucket ACLs. Despite granting permissions to the log delivery user, bucket policies can replace the bucket ACL to manage the access permissions of a bucket.  [Table 1](#table183716545593)  shows the mapping between bucket ACL access permissions and bucket policy actions.

**Table  1**  Mapping relationship between bucket ACLs and bucket policies

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

## Mapping Relationship Between Object ACLs and Bucket Policies<a name="section816016146119"></a>

Object ACLs are used to control basic read and write access permissions for objects. The custom settings of bucket policies support more actions that can be performed on objects.  [Table 2](#table4160714016)  describes the mapping relationship between object ACL access permissions and bucket policy actions.

**Table  2**  Mapping relationship between object ACLs and bucket policies

<a name="table4160714016"></a>
<table><thead align="left"><tr id="row122474141815"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.4.1.1"><p id="p92471614310"><a name="p92471614310"></a><a name="p92471614310"></a>Object ACL</p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.4.1.2"><p id="p1024713142118"><a name="p1024713142118"></a><a name="p1024713142118"></a>Option</p>
</th>
<th class="cellrowborder" valign="top" width="66.32336766323368%" id="mcps1.2.4.1.3"><p id="p62479146116"><a name="p62479146116"></a><a name="p62479146116"></a>Mapped Action in a Custom Bucket Policy</p>
</th>
</tr>
</thead>
<tbody><tr id="row1724718148112"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.4.1.1 "><p id="p102479141019"><a name="p102479141019"></a><a name="p102479141019"></a>Access to Object</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.4.1.2 "><p id="p724781411118"><a name="p724781411118"></a><a name="p724781411118"></a>Read</p>
</td>
<td class="cellrowborder" valign="top" width="66.32336766323368%" headers="mcps1.2.4.1.3 "><a name="ul1424715141914"></a><a name="ul1424715141914"></a><ul id="ul1424715141914"><li>GetObject</li><li>GetObjectVersion</li></ul>
</td>
</tr>
<tr id="row12247101419112"><td class="cellrowborder" rowspan="2" valign="top" width="19.388061193880613%" headers="mcps1.2.4.1.1 "><p id="p62471514814"><a name="p62471514814"></a><a name="p62471514814"></a>Access to ACL</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.4.1.2 "><p id="p72471314311"><a name="p72471314311"></a><a name="p72471314311"></a>Read</p>
</td>
<td class="cellrowborder" valign="top" width="66.32336766323368%" headers="mcps1.2.4.1.3 "><a name="ul324718149119"></a><a name="ul324718149119"></a><ul id="ul324718149119"><li>GetObjectAcl</li><li>GetObjectVersionAcl</li></ul>
</td>
</tr>
<tr id="row122478141116"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p8247614513"><a name="p8247614513"></a><a name="p8247614513"></a>Write</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><a name="ul122471014113"></a><a name="ul122471014113"></a><ul id="ul122471014113"><li>PutObjectAcl</li><li>PutObjectVersionAcl</li></ul>
</td>
</tr>
</tbody>
</table>

## Does Bucket Policy Change Effect on the ACL Setting?<a name="section8941172018353"></a>

When objects are uploaded to a bucket, object ACLs are set for those objects. When the bucket policy is modified, ACLs of the objects do not change. However, ACLs of newly uploaded objects will be the default setting, and will not inherit the object ACL rule set by existing objects.

