# List of OBS Error Codes<a name="obs_03_0348"></a>

If a request fails to be processed due to errors, an error response is returned. An error response contains an error code and error details.  [Table 1](#table50167618173651)  lists some common error codes in OBS error responses.

**Table  1**  List of OBS error codes

<a name="table50167618173651"></a>
<table><thead align="left"><tr id="row52554525173651"><th class="cellrowborder" valign="top" width="28.76%" id="mcps1.2.3.1.1"><p id="p32578321173731"><a name="p32578321173731"></a><a name="p32578321173731"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="71.24000000000001%" id="mcps1.2.3.1.2"><p id="p21598326173731"><a name="p21598326173731"></a><a name="p21598326173731"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19851684173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p5601064419558"><a name="p5601064419558"></a><a name="p5601064419558"></a>Obs.0000</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p5653294417386"><a name="p5653294417386"></a><a name="p5653294417386"></a>Invalid parameter.</p>
</td>
</tr>
<tr id="row15993949173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p2957026719558"><a name="p2957026719558"></a><a name="p2957026719558"></a>Obs.0001</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p4301448617386"><a name="p4301448617386"></a><a name="p4301448617386"></a>All access requests for this object are invalid.</p>
</td>
</tr>
<tr id="row61412348173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p1477998319558"><a name="p1477998319558"></a><a name="p1477998319558"></a>Obs.0002</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p3541989817386"><a name="p3541989817386"></a><a name="p3541989817386"></a>The absolute path of a file cannot exceed 1023 characters. Please retry.</p>
</td>
</tr>
<tr id="row19222418173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p3718999419558"><a name="p3718999419558"></a><a name="p3718999419558"></a>Obs.0003</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p921254317386"><a name="p921254317386"></a><a name="p921254317386"></a>The connection timed out.</p>
</td>
</tr>
<tr id="row29140860173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p6663409619558"><a name="p6663409619558"></a><a name="p6663409619558"></a>Obs.0004</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p959903017386"><a name="p959903017386"></a><a name="p959903017386"></a>Time difference is longer than 15 minutes between the client and server. Correctly set the local time.</p>
</td>
</tr>
<tr id="row1621471173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p5654737019558"><a name="p5654737019558"></a><a name="p5654737019558"></a>Obs.0005</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p3822980017386"><a name="p3822980017386"></a><a name="p3822980017386"></a>The server load is too heavy. Try again later.</p>
</td>
</tr>
<tr id="row2461864173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p1819050819558"><a name="p1819050819558"></a><a name="p1819050819558"></a>Obs.0006</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p6222142917386"><a name="p6222142917386"></a><a name="p6222142917386"></a>The number of buckets has reached the upper limit.</p>
</td>
</tr>
<tr id="row11481991173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p4043470619558"><a name="p4043470619558"></a><a name="p4043470619558"></a>Obs.0007</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p2474072917386"><a name="p2474072917386"></a><a name="p2474072917386"></a>The target bucket does not exist or is not in the same region with the current bucket.</p>
</td>
</tr>
<tr id="row27427029171527"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p1610963019558"><a name="p1610963019558"></a><a name="p1610963019558"></a>Obs.0008</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p46696090171648"><a name="p46696090171648"></a><a name="p46696090171648"></a>The account has not been registered with the system. Only a registered account can be used.</p>
</td>
</tr>
<tr id="row36046441171557"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p6697794619558"><a name="p6697794619558"></a><a name="p6697794619558"></a>Obs.0009</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p55545500171648"><a name="p55545500171648"></a><a name="p55545500171648"></a>A conflicting operation is being performed on this resource. Please retry.</p>
</td>
</tr>
<tr id="row2110992717162"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p3877909919558"><a name="p3877909919558"></a><a name="p3877909919558"></a>Obs.0010</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p64178123171648"><a name="p64178123171648"></a><a name="p64178123171648"></a>Deletion failed. Check whether objects or objects of historical versions exist in the bucket.</p>
</td>
</tr>
<tr id="row3917222717164"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p1713196319558"><a name="p1713196319558"></a><a name="p1713196319558"></a>Obs.0011</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p16478426171648"><a name="p16478426171648"></a><a name="p16478426171648"></a>The bucket policy is invalid. Configure it again.</p>
</td>
</tr>
<tr id="row46347315171625"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p695289319558"><a name="p695289319558"></a><a name="p695289319558"></a>Obs.0012</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p23183687171648"><a name="p23183687171648"></a><a name="p23183687171648"></a>The requested bucket name already exists. Bucket namespace is shared by all users in the system. Enter a different name and try again.</p>
</td>
</tr>
<tr id="row42201452171630"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p3549489319558"><a name="p3549489319558"></a><a name="p3549489319558"></a>Obs.0013</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p19832727171648"><a name="p19832727171648"></a><a name="p19832727171648"></a>The requested folder name already exists. Enter a different name and try again.</p>
</td>
</tr>
<tr id="row1661362917168"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p3886454019558"><a name="p3886454019558"></a><a name="p3886454019558"></a>Obs.0014</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p30654632171648"><a name="p30654632171648"></a><a name="p30654632171648"></a>The file size has exceeded 50 MB. Use OBS Browser to upload it.</p>
</td>
</tr>
<tr id="row15434962171618"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p1230954319558"><a name="p1230954319558"></a><a name="p1230954319558"></a>Obs.0015</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p65092656171648"><a name="p65092656171648"></a><a name="p65092656171648"></a>The absolute path in the search criteria cannot exceed 1023 characters. Please retry.</p>
</td>
</tr>
<tr id="row24419871171620"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p4817809519558"><a name="p4817809519558"></a><a name="p4817809519558"></a>Obs.0016</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p11774179102245"><a name="p11774179102245"></a><a name="p11774179102245"></a>Upload failed. Possible causes:</p>
<a name="ol35293502114550"></a><a name="ol35293502114550"></a><ol id="ol35293502114550"><li>The network is abnormal.</li><li>You have incorrect or no permissions to write the bucket.</li></ol>
</td>
</tr>
<tr id="row19510255171615"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p2389603319558"><a name="p2389603319558"></a><a name="p2389603319558"></a>Obs.0017</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p24421024171648"><a name="p24421024171648"></a><a name="p24421024171648"></a>The end time of the new validity period must be later than that of the old validity period.</p>
</td>
</tr>
<tr id="row27402193171613"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p3901278319558"><a name="p3901278319558"></a><a name="p3901278319558"></a>Obs.0018</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p1787731171648"><a name="p1787731171648"></a><a name="p1787731171648"></a>The validity period cannot be shorter than the remaining period.</p>
</td>
</tr>
<tr id="row4739939717160"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p5326978019558"><a name="p5326978019558"></a><a name="p5326978019558"></a>Obs.0019</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p1485784171648"><a name="p1485784171648"></a><a name="p1485784171648"></a>Cannot determine whether the bucket has objects or fragments. Check whether you have the read permission for this bucket.</p>
</td>
</tr>
<tr id="row14775209113411"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p4474670719558"><a name="p4474670719558"></a><a name="p4474670719558"></a>Obs.0020</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p47424265163119"><a name="p47424265163119"></a><a name="p47424265163119"></a>TMS system error. Try again later.</p>
</td>
</tr>
<tr id="row36498530113435"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p544210419558"><a name="p544210419558"></a><a name="p544210419558"></a>Obs.0021</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p37615837113435"><a name="p37615837113435"></a><a name="p37615837113435"></a>You do not have permissions to access TMS. Use IAM to add the permission to access TMS.</p>
</td>
</tr>
<tr id="row11501159113437"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p787093219558"><a name="p787093219558"></a><a name="p787093219558"></a>Obs.0022</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p1698072113437"><a name="p1698072113437"></a><a name="p1698072113437"></a>The TMS system is busy. Try again later.</p>
</td>
</tr>
</tbody>
</table>

