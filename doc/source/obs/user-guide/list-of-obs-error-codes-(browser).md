# List of OBS Error Codes<a name="obs_03_0445"></a>

If a request fails to be processed due to errors, an error response is returned. An error response contains an error code and error details.  [Table 1](#table50167618173651)  lists some common error codes in OBS error responses.

**Table  1**  List of OBS error codes

<a name="table50167618173651"></a>
<table><thead align="left"><tr id="row52554525173651"><th class="cellrowborder" valign="top" width="28.76%" id="mcps1.2.3.1.1"><p id="p32578321173731"><a name="p32578321173731"></a><a name="p32578321173731"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="71.24000000000001%" id="mcps1.2.3.1.2"><p id="p21598326173731"><a name="p21598326173731"></a><a name="p21598326173731"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row61432158173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p20919686195132"><a name="p20919686195132"></a><a name="p20919686195132"></a>Obs.0000</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p1866292217386"><a name="p1866292217386"></a><a name="p1866292217386"></a>Unauthorized gateway or proxy server. Enter the correct authentication information.</p>
</td>
</tr>
<tr id="row4967814173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p16739388195132"><a name="p16739388195132"></a><a name="p16739388195132"></a>Obs.0001</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p4927993017386"><a name="p4927993017386"></a><a name="p4927993017386"></a>Internal server error. Contact the customer service.</p>
</td>
</tr>
<tr id="row11635827173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p56310107195132"><a name="p56310107195132"></a><a name="p56310107195132"></a>Obs.0002</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p2182699317386"><a name="p2182699317386"></a><a name="p2182699317386"></a>Bad gateway or unable to connect to the proxy server. Contact the customer service.</p>
</td>
</tr>
<tr id="row23405464173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p46552316195132"><a name="p46552316195132"></a><a name="p46552316195132"></a>Obs.0003</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p707742617386"><a name="p707742617386"></a><a name="p707742617386"></a>The server is busy. Try again later.</p>
</td>
</tr>
<tr id="row3974808417636"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p46662660195132"><a name="p46662660195132"></a><a name="p46662660195132"></a>Obs.0004</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p213527317636"><a name="p213527317636"></a><a name="p213527317636"></a>The requested bucket name already exists. Bucket namespace is shared by all users in the system. Enter a different name and retry.</p>
</td>
</tr>
<tr id="row844593017344"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p59994333195132"><a name="p59994333195132"></a><a name="p59994333195132"></a>Obs.0005</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p4893773517344"><a name="p4893773517344"></a><a name="p4893773517344"></a>Deletion failed. Check whether objects exist in the bucket or log in to OBS Console to check whether objects of historical versions exist in the bucket.</p>
</td>
</tr>
<tr id="row11296810173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p47998522195132"><a name="p47998522195132"></a><a name="p47998522195132"></a>Obs.0006</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p6140570417386"><a name="p6140570417386"></a><a name="p6140570417386"></a>Access to the local file denied. Please retry.</p>
</td>
</tr>
<tr id="row3265318173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p27204566195132"><a name="p27204566195132"></a><a name="p27204566195132"></a>Obs.0007</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p314654417386"><a name="p314654417386"></a><a name="p314654417386"></a>Failed to upload the target file because it has been occupied. Check whether the file is accessible.</p>
</td>
</tr>
<tr id="row10048093173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p35013940195132"><a name="p35013940195132"></a><a name="p35013940195132"></a>Obs.0008</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p1212957717386"><a name="p1212957717386"></a><a name="p1212957717386"></a>Failed to read the file. Please retry.</p>
</td>
</tr>
<tr id="row19559764173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p23794271195132"><a name="p23794271195132"></a><a name="p23794271195132"></a>Obs.0009</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p1276605017386"><a name="p1276605017386"></a><a name="p1276605017386"></a>Insufficient local disk space. Delete unnecessary files to ensure that the disk space is sufficient.</p>
</td>
</tr>
<tr id="row35254551173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p31937195195132"><a name="p31937195195132"></a><a name="p31937195195132"></a>Obs.0010</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p3192247517386"><a name="p3192247517386"></a><a name="p3192247517386"></a>You do not have permission to read or write a local file. Apply for the required permissions.</p>
</td>
</tr>
<tr id="row29066043173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p62548337195132"><a name="p62548337195132"></a><a name="p62548337195132"></a>Obs.0011</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p5181787917386"><a name="p5181787917386"></a><a name="p5181787917386"></a>The account balance is in arrears or insufficient. Please top up and retry.</p>
</td>
</tr>
<tr id="row28371785173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p30819542195132"><a name="p30819542195132"></a><a name="p30819542195132"></a>Obs.0012</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p2318361817386"><a name="p2318361817386"></a><a name="p2318361817386"></a>Invalid access key ID or secret access key.</p>
</td>
</tr>
<tr id="row44049661173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p53085828195132"><a name="p53085828195132"></a><a name="p53085828195132"></a>Obs.0013</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p2417769117386"><a name="p2417769117386"></a><a name="p2417769117386"></a>Failed to upload the file in multiparts. Please cancel this task and retry.</p>
</td>
</tr>
<tr id="row15993949173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p44863086195132"><a name="p44863086195132"></a><a name="p44863086195132"></a>Obs.0014</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p62406315164022"><a name="p62406315164022"></a><a name="p62406315164022"></a>All access requests to this object are invalid.</p>
</td>
</tr>
<tr id="row15858547173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p23173007195132"><a name="p23173007195132"></a><a name="p23173007195132"></a>Obs.0015</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p11565767114749"><a name="p11565767114749"></a><a name="p11565767114749"></a>This operation cannot be performed because: The target bucket does not exist. The target bucket does not belong to you. You do not have the required permission. For this reason, ensure that the log delivery user has the <strong id="b15869173735714"><a name="b15869173735714"></a><a name="b15869173735714"></a>Bucket Write</strong> and <strong id="b3204545115717"><a name="b3204545115717"></a><a name="b3204545115717"></a>ACL View</strong> permissions for the target bucket. Configure the permissions in the Configure Permission dialog box.</p>
</td>
</tr>
<tr id="row26976423173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p48797354195132"><a name="p48797354195132"></a><a name="p48797354195132"></a>Obs.0016</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p1012906017386"><a name="p1012906017386"></a><a name="p1012906017386"></a>Your operation is conflicting with another user's operation. Try again later.</p>
</td>
</tr>
<tr id="row34841921173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p5573386195132"><a name="p5573386195132"></a><a name="p5573386195132"></a>Obs.0017</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p211036217386"><a name="p211036217386"></a><a name="p211036217386"></a>The bucket that you attempt to access is not found in this region. Select another bucket.</p>
</td>
</tr>
<tr id="row24168049173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p36467011195132"><a name="p36467011195132"></a><a name="p36467011195132"></a>Obs.0018</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p6205894817386"><a name="p6205894817386"></a><a name="p6205894817386"></a>Incorrect region. Enter a correct region.</p>
</td>
</tr>
<tr id="row29140860173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p9340910195132"><a name="p9340910195132"></a><a name="p9340910195132"></a>Obs.0019</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p959903017386"><a name="p959903017386"></a><a name="p959903017386"></a>Time difference is longer than 15 minutes between the client and server.</p>
</td>
</tr>
<tr id="row1621471173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p31528560195132"><a name="p31528560195132"></a><a name="p31528560195132"></a>Obs.0020</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p3822980017386"><a name="p3822980017386"></a><a name="p3822980017386"></a>The server load is too heavy. Try again later.</p>
</td>
</tr>
<tr id="row49023273173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p33088947195132"><a name="p33088947195132"></a><a name="p33088947195132"></a>Obs.0021</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p1934565217386"><a name="p1934565217386"></a><a name="p1934565217386"></a>Failed to delete some objects. Try again later.</p>
</td>
</tr>
<tr id="row34440371173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p29760233195132"><a name="p29760233195132"></a><a name="p29760233195132"></a>Obs.0022</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p1011946117386"><a name="p1011946117386"></a><a name="p1011946117386"></a>Failed to download some objects. Try again later.</p>
</td>
</tr>
<tr id="row2461864173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p19047504195132"><a name="p19047504195132"></a><a name="p19047504195132"></a>Obs.0023</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p6222142917386"><a name="p6222142917386"></a><a name="p6222142917386"></a>The number of buckets has reached the upper limit.</p>
</td>
</tr>
<tr id="row12851391173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p61204456195132"><a name="p61204456195132"></a><a name="p61204456195132"></a>Obs.0024</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p6093911117386"><a name="p6093911117386"></a><a name="p6093911117386"></a>Failed to process the request. Please retry.</p>
</td>
</tr>
<tr id="row12676108171851"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p57762877195132"><a name="p57762877195132"></a><a name="p57762877195132"></a>Obs.0025</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p20067333171851"><a name="p20067333171851"></a><a name="p20067333171851"></a>Invalid IP address or domain name. Try another one.</p>
</td>
</tr>
<tr id="row59761684173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p31879970195132"><a name="p31879970195132"></a><a name="p31879970195132"></a>Obs.0026</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p6264668917386"><a name="p6264668917386"></a><a name="p6264668917386"></a>The absolute path of a file cannot exceed 1023 characters. Please retry.</p>
</td>
</tr>
<tr id="row15191585173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p20831859195132"><a name="p20831859195132"></a><a name="p20831859195132"></a>Obs.0027</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p3540892117386"><a name="p3540892117386"></a><a name="p3540892117386"></a>Unable to connect to the proxy server. Check whether the network is normal and the authentication information about the proxy server is correct.</p>
</td>
</tr>
<tr id="row11481991173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p19822290195132"><a name="p19822290195132"></a><a name="p19822290195132"></a>Obs.0028</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p2474072917386"><a name="p2474072917386"></a><a name="p2474072917386"></a>The target bucket does not exist or is not in the same region with the source bucket.</p>
</td>
</tr>
<tr id="row66359153173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p22043753195132"><a name="p22043753195132"></a><a name="p22043753195132"></a>Obs.0029</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p5081633417386"><a name="p5081633417386"></a><a name="p5081633417386"></a>Incorrect signature. Contact the customer service.</p>
</td>
</tr>
<tr id="row3955647173651"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p30878125195132"><a name="p30878125195132"></a><a name="p30878125195132"></a>Obs.0030</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p176507417386"><a name="p176507417386"></a><a name="p176507417386"></a>Failed to find or create the path. Check whether the path exists or is too long.</p>
</td>
</tr>
<tr id="row27427029171527"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p28684312195132"><a name="p28684312195132"></a><a name="p28684312195132"></a>Obs.0031</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p46696090171648"><a name="p46696090171648"></a><a name="p46696090171648"></a>The account has not been registered with the system. Only a registered account can be used.</p>
</td>
</tr>
<tr id="row3917222717164"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p40007406195132"><a name="p40007406195132"></a><a name="p40007406195132"></a>Obs.0032</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p16478426171648"><a name="p16478426171648"></a><a name="p16478426171648"></a>The bucket policy is invalid. Configure it again.</p>
</td>
</tr>
<tr id="row46347315171625"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p40152056195132"><a name="p40152056195132"></a><a name="p40152056195132"></a>Obs.0033</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p23183687171648"><a name="p23183687171648"></a><a name="p23183687171648"></a>The requested bucket name already exists. Bucket namespace is shared by all users in the system. Enter a different name and retry.</p>
</td>
</tr>
<tr id="row19510255171615"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p11384394195132"><a name="p11384394195132"></a><a name="p11384394195132"></a>Obs.0034</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p24421024171648"><a name="p24421024171648"></a><a name="p24421024171648"></a>The end time of the new validity period must be later than that of the old validity period.</p>
</td>
</tr>
<tr id="row4739939717160"><td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.3.1.1 "><p id="p44833536195132"><a name="p44833536195132"></a><a name="p44833536195132"></a>Obs.0035</p>
</td>
<td class="cellrowborder" valign="top" width="71.24000000000001%" headers="mcps1.2.3.1.2 "><p id="p1485784171648"><a name="p1485784171648"></a><a name="p1485784171648"></a>Cannot determine whether the bucket has objects or fragments. Check whether you have the read permission for this bucket.</p>
</td>
</tr>
</tbody>
</table>

