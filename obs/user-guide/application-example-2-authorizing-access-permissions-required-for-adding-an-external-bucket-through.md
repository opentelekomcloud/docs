# Application Example 2: Authorizing Access Permissions Required for Adding an External Bucket Through the Standard Bucket Policy<a name="obs_03_0135"></a>

A standard bucket policy can be used to grant the read and write access to a bucket. The standard bucket policy grants the public read and write access to the bucket, that is, all users can access the bucket. Permissions controlled by a standard bucket policy are as follows:

**Table  1**  Permissions controlled by a standard bucket policy

<a name="table862416458164"></a>
<table><thead align="left"><tr id="obs_03_0434_row15249821152217"><th class="cellrowborder" valign="top" width="22.35%" id="mcps1.2.4.1.1"><p id="obs_03_0434_p122491621102215"><a name="obs_03_0434_p122491621102215"></a><a name="obs_03_0434_p122491621102215"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="37.65%" id="mcps1.2.4.1.2"><p id="obs_03_0434_p9249112142212"><a name="obs_03_0434_p9249112142212"></a><a name="obs_03_0434_p9249112142212"></a>Public Read</p>
</th>
<th class="cellrowborder" valign="top" width="40%" id="mcps1.2.4.1.3"><p id="obs_03_0434_p14249421172212"><a name="obs_03_0434_p14249421172212"></a><a name="obs_03_0434_p14249421172212"></a>Public Read and Write</p>
</th>
</tr>
</thead>
<tbody><tr id="obs_03_0434_row724919215226"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.4.1.1 "><p id="obs_03_0434_p102491321142216"><a name="obs_03_0434_p102491321142216"></a><a name="obs_03_0434_p102491321142216"></a>Effect</p>
</td>
<td class="cellrowborder" valign="top" width="37.65%" headers="mcps1.2.4.1.2 "><p id="obs_03_0434_p02496219224"><a name="obs_03_0434_p02496219224"></a><a name="obs_03_0434_p02496219224"></a>Allow</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="obs_03_0434_p424962162212"><a name="obs_03_0434_p424962162212"></a><a name="obs_03_0434_p424962162212"></a>Allow</p>
</td>
</tr>
<tr id="obs_03_0434_row1224915215221"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.4.1.1 "><p id="obs_03_0434_p824919216225"><a name="obs_03_0434_p824919216225"></a><a name="obs_03_0434_p824919216225"></a>Principal</p>
</td>
<td class="cellrowborder" valign="top" width="37.65%" headers="mcps1.2.4.1.2 "><p id="obs_03_0434_p12503210220"><a name="obs_03_0434_p12503210220"></a><a name="obs_03_0434_p12503210220"></a>* (Any user)</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="obs_03_0434_p132503214228"><a name="obs_03_0434_p132503214228"></a><a name="obs_03_0434_p132503214228"></a>* (Any user)</p>
</td>
</tr>
<tr id="obs_03_0434_row5250121102214"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.4.1.1 "><p id="obs_03_0434_p1625082192215"><a name="obs_03_0434_p1625082192215"></a><a name="obs_03_0434_p1625082192215"></a>Resources</p>
</td>
<td class="cellrowborder" valign="top" width="37.65%" headers="mcps1.2.4.1.2 "><p id="obs_03_0434_p125022172220"><a name="obs_03_0434_p125022172220"></a><a name="obs_03_0434_p125022172220"></a>* (All objects in a bucket)</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="obs_03_0434_p3250112172220"><a name="obs_03_0434_p3250112172220"></a><a name="obs_03_0434_p3250112172220"></a>* (All objects in a bucket)</p>
</td>
</tr>
<tr id="obs_03_0434_row14250821122214"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.4.1.1 "><p id="obs_03_0434_p1125052118223"><a name="obs_03_0434_p1125052118223"></a><a name="obs_03_0434_p1125052118223"></a>Actions</p>
</td>
<td class="cellrowborder" valign="top" width="37.65%" headers="mcps1.2.4.1.2 "><a name="obs_03_0434_ul1512955514"></a><a name="obs_03_0434_ul1512955514"></a><ul id="obs_03_0434_ul1512955514"><li>GetObject</li><li>GetObjectVersion</li><li>ListBucket</li></ul>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><a name="obs_03_0434_ul5350174995516"></a><a name="obs_03_0434_ul5350174995516"></a><ul id="obs_03_0434_ul5350174995516"><li>GetObject</li><li>GetObjectVersion</li><li>PutObject</li><li>DeleteObject</li><li>DeleteObjectVersion</li><li>ListBucket</li></ul>
</td>
</tr>
<tr id="obs_03_0434_row122501121162216"><td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.4.1.1 "><p id="obs_03_0434_p22501217226"><a name="obs_03_0434_p22501217226"></a><a name="obs_03_0434_p22501217226"></a>Conditions</p>
</td>
<td class="cellrowborder" valign="top" width="37.65%" headers="mcps1.2.4.1.2 "><p id="obs_03_0434_p132501521172219"><a name="obs_03_0434_p132501521172219"></a><a name="obs_03_0434_p132501521172219"></a>N/A</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="obs_03_0434_p1325042111223"><a name="obs_03_0434_p1325042111223"></a><a name="obs_03_0434_p1325042111223"></a>N/A</p>
</td>
</tr>
</tbody>
</table>

## Procedure<a name="section9799102151917"></a>

1.  Log in to OBS Console.
2.  In the bucket list, click the bucket to be operated. The  **Overview**  page of the bucket is displayed.
3.  In the navigation pane on the left, click  **Permissions**  to go to the permission management page.
4.  Select the  **Public Read and Write**  policy from the standard bucket policies that are pre-defined.
5.  In the dialog box that is displayed, click  **Yes**.

## Verification<a name="section88013218195"></a>

1.  Log in to OBS Browser.
2.  Click  **Add Bucket**  on the upper left corner of the page. The  **Add Bucket**  dialog box is displayed.
3.  Select  **Add external bucket**  and enter the bucket name.
4.  Click  **OK**. The external bucket is added successfully.
5.  Click the newly added external bucket to open the bucket.
6.  Click  **Upload Object**, and objects can be successfully uploaded to the bucket.
7.  Select an object in the bucket and click  **Delete**. The object can be deleted successfully.

