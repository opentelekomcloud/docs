# Application Example 1: Authorizing Access Permissions Required for Adding an External Bucket Through the Bucket ACL<a name="obs_03_0134"></a>

A bucket ACL can be used to grant the read and write access to a bucket. If only the read access to the bucket is granted, the authorized user can only add the bucket and list objects in the bucket, but cannot upload objects to the bucket. If the read and write access to the bucket is granted, the authorized user can upload objects to the bucket. Permissions controlled by a bucket ACL are as follows:

**Table  1**  Permissions controlled by a bucket ACL

<a name="table862416458164"></a>
<table><thead align="left"><tr id="obs_03_0434_row10426205416593"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.4.1.1"><p id="obs_03_0434_p6426165418599"><a name="obs_03_0434_p6426165418599"></a><a name="obs_03_0434_p6426165418599"></a>Bucket ACL</p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.4.1.2"><p id="obs_03_0434_p1842615544595"><a name="obs_03_0434_p1842615544595"></a><a name="obs_03_0434_p1842615544595"></a>Option</p>
</th>
<th class="cellrowborder" valign="top" width="66.66666666666667%" id="mcps1.2.4.1.3"><p id="obs_03_0434_p8428125435912"><a name="obs_03_0434_p8428125435912"></a><a name="obs_03_0434_p8428125435912"></a>Mapped Action in a Custom Bucket Policy</p>
</th>
</tr>
</thead>
<tbody><tr id="obs_03_0434_row942885416596"><td class="cellrowborder" rowspan="2" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.1 "><p id="obs_03_0434_p184281354195919"><a name="obs_03_0434_p184281354195919"></a><a name="obs_03_0434_p184281354195919"></a>Access to Bucket</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="obs_03_0434_p54287547598"><a name="obs_03_0434_p54287547598"></a><a name="obs_03_0434_p54287547598"></a>Read</p>
</td>
<td class="cellrowborder" valign="top" width="66.66666666666667%" headers="mcps1.2.4.1.3 "><a name="obs_03_0434_ul1242814546590"></a><a name="obs_03_0434_ul1242814546590"></a><ul id="obs_03_0434_ul1242814546590"><li>ListBucket</li><li>ListBucketVersions</li><li>ListBucketMultipartUploads</li></ul>
</td>
</tr>
<tr id="obs_03_0434_row1242885414593"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="obs_03_0434_p134281454115913"><a name="obs_03_0434_p134281454115913"></a><a name="obs_03_0434_p134281454115913"></a>Write</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><a name="obs_03_0434_ul84281154125913"></a><a name="obs_03_0434_ul84281154125913"></a><ul id="obs_03_0434_ul84281154125913"><li>PutObject</li><li>DeleteObject</li><li>DeleteObjectVersion</li></ul>
</td>
</tr>
<tr id="obs_03_0434_row17428135413591"><td class="cellrowborder" rowspan="2" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.1 "><p id="obs_03_0434_p174281154105920"><a name="obs_03_0434_p174281154105920"></a><a name="obs_03_0434_p174281154105920"></a>Access to ACL</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.4.1.2 "><p id="obs_03_0434_p1142885415597"><a name="obs_03_0434_p1142885415597"></a><a name="obs_03_0434_p1142885415597"></a>Read</p>
</td>
<td class="cellrowborder" valign="top" width="66.66666666666667%" headers="mcps1.2.4.1.3 "><p id="obs_03_0434_p1842815542599"><a name="obs_03_0434_p1842815542599"></a><a name="obs_03_0434_p1842815542599"></a>GetBucketAcl</p>
</td>
</tr>
<tr id="obs_03_0434_row15428654125911"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="obs_03_0434_p1742825465912"><a name="obs_03_0434_p1742825465912"></a><a name="obs_03_0434_p1742825465912"></a>Write</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="obs_03_0434_p2429554125918"><a name="obs_03_0434_p2429554125918"></a><a name="obs_03_0434_p2429554125918"></a>PutBucketAcl</p>
</td>
</tr>
</tbody>
</table>

## Procedure<a name="section207491196166"></a>

1.  Log in to OBS Console.
2.  In the bucket list, click the bucket to be operated. The  **Summary**  page of the bucket is displayed.
3.  In the navigation pane on the left, click  **Permissions**  to go to the permission management page.
4.  Click  **Bucket ACL**. The  **Bucket ACL**  page is displayed.
5.  Click  **Add**, enter the account ID of the user that will add the bucket to OBS Browser, and select the read and write access to the bucket.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If you want to authorize such access to all users, in the  **Public Permissions**  area, authorize the  **Anonymous User**  the read and write access to the bucket.  
    >**Account ID**  corresponds to  **Domain ID**  on the  **My Credential**  page.  

6.  Click  **Save**.

## Verification<a name="section682292355915"></a>

1.  Log in to OBS Browser.
2.  Click  **Add Bucket**  on the upper left corner of the page. The  **Add Bucket**  dialog box is displayed.
3.  Select  **Add external bucket**  and enter the bucket name.
4.  Click  **OK**. The external bucket is added successfully.
5.  Click the newly added external bucket to open the bucket.
6.  Click  **Upload Object**, and objects can be successfully uploaded to the bucket.
7.  Select an object in the bucket and click  **Delete**. The object can be deleted successfully.

