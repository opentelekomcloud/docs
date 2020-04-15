# Error Code<a name="en-us_topic_0168602259"></a>

## Description<a name="section22042507"></a>

This section explains the meanings of error code returned by CTS APIs.

## Example of Returned Error Information<a name="en-us_topic_0024737081-chtext"></a>

\{"details":\{"details":"Create bucket failed","code":"cts.0036","obs\_details":\{"obs\_code":403, "obs\_error":"ClusterGroupExclusiveException","obs\_message":"The cluster groups are exclusively,you are not allowed to create bucket."\}\}\}

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The  **obs\_details**  field is only contained in the error message returned by the OBS bucket.  

## Error Code Description<a name="section60430213113222"></a>

**Table  1**  Error code description

<a name="table38580605104321"></a>
<table><thead align="left"><tr id="row1575457104321"><th class="cellrowborder" valign="top" width="9%" id="mcps1.2.6.1.1"><p id="p1782415589359"><a name="p1782415589359"></a><a name="p1782415589359"></a><strong id="b132034917466"><a name="b132034917466"></a><a name="b132034917466"></a>Response Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="9%" id="mcps1.2.6.1.2"><p id="p60503230104321"><a name="p60503230104321"></a><a name="p60503230104321"></a><strong id="b842352706115256"><a name="b842352706115256"></a><a name="b842352706115256"></a>Error Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.6.1.3"><p id="p18210194404111"><a name="p18210194404111"></a><a name="p18210194404111"></a><strong id="b842352706115259"><a name="b842352706115259"></a><a name="b842352706115259"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.5%" id="mcps1.2.6.1.4"><p id="p056934718416"><a name="p056934718416"></a><a name="p056934718416"></a>Error Message</p>
</th>
<th class="cellrowborder" valign="top" width="33.5%" id="mcps1.2.6.1.5"><p id="p2028219123429"><a name="p2028219123429"></a><a name="p2028219123429"></a>Description.</p>
</th>
</tr>
</thead>
<tbody><tr id="row12763840104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p178248589356"><a name="p178248589356"></a><a name="p178248589356"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p27238134104321"><a name="p27238134104321"></a><a name="p27238134104321"></a>cts.0001</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p172112448412"><a name="p172112448412"></a><a name="p172112448412"></a>The API version number is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p16991103712815"><a name="p16991103712815"></a><a name="p16991103712815"></a>Empty API version. Check whether you need to specify an API version.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p58805252104321"><a name="p58805252104321"></a><a name="p58805252104321"></a>The API version in the URL is empty. Check whether the API version information is specified.</p>
</td>
</tr>
<tr id="row59485228104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p1163362692218"><a name="p1163362692218"></a><a name="p1163362692218"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p53574195104321"><a name="p53574195104321"></a><a name="p53574195104321"></a>cts.0002</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p1321194418411"><a name="p1321194418411"></a><a name="p1321194418411"></a>The API version number is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p155691347154112"><a name="p155691347154112"></a><a name="p155691347154112"></a>Invalid API version. Check whether the API version is correct.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p44542501104321"><a name="p44542501104321"></a><a name="p44542501104321"></a>The API version information in the URL is invalid. Check whether the API version information is correct.</p>
</td>
</tr>
<tr id="row65338195104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p12214927152214"><a name="p12214927152214"></a><a name="p12214927152214"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p57902419104321"><a name="p57902419104321"></a><a name="p57902419104321"></a>cts.0003</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p821144434114"><a name="p821144434114"></a><a name="p821144434114"></a>The tenant ID does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p622553917325"><a name="p622553917325"></a><a name="p622553917325"></a>Empty project ID. Check whether you need to specify a project ID.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p59584372104321"><a name="p59584372104321"></a><a name="p59584372104321"></a>The project ID in the URL is empty. Check whether the project ID is specified.</p>
</td>
</tr>
<tr id="row66497304104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p20812162772217"><a name="p20812162772217"></a><a name="p20812162772217"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p17572557104321"><a name="p17572557104321"></a><a name="p17572557104321"></a>cts.0004</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p102117445417"><a name="p102117445417"></a><a name="p102117445417"></a>The tenant ID is incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p37155111337"><a name="p37155111337"></a><a name="p37155111337"></a>Invalid project ID. Check whether the project ID is correct.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p14090998104321"><a name="p14090998104321"></a><a name="p14090998104321"></a>The project ID in the URL is invalid. Check whether the project ID is correct.</p>
</td>
</tr>
<tr id="row59710122104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p49743017259"><a name="p49743017259"></a><a name="p49743017259"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p4681693104321"><a name="p4681693104321"></a><a name="p4681693104321"></a>cts.0005</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p121124417418"><a name="p121124417418"></a><a name="p121124417418"></a>The query parameters are incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p10314218113317"><a name="p10314218113317"></a><a name="p10314218113317"></a>Invalid query criteria. Check whether query criteria parameters are correct.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p43672824104321"><a name="p43672824104321"></a><a name="p43672824104321"></a>Invalid query criteria. Check whether query criteria parameters are correct. **** does not exist.</p>
</td>
</tr>
<tr id="row57511100104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p220623118256"><a name="p220623118256"></a><a name="p220623118256"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p27887560104321"><a name="p27887560104321"></a><a name="p27887560104321"></a>cts.0006</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p921119441412"><a name="p921119441412"></a><a name="p921119441412"></a>The request URL does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p1050811315332"><a name="p1050811315332"></a><a name="p1050811315332"></a>The URL does not exist. Check whether the URL meets requirements.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p44299855104321"><a name="p44299855104321"></a><a name="p44299855104321"></a>The URL does not exist. Check whether the URL is correct.</p>
</td>
</tr>
<tr id="row63154381104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p1595553182518"><a name="p1595553182518"></a><a name="p1595553182518"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p15231259104321"><a name="p15231259104321"></a><a name="p15231259104321"></a>cts.0007</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p52111244194114"><a name="p52111244194114"></a><a name="p52111244194114"></a>Request parameters are incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p95695473411"><a name="p95695473411"></a><a name="p95695473411"></a>Invalid message body. Different errors are returned according to different parameters.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p40817657103721"><a name="p40817657103721"></a><a name="p40817657103721"></a>Invalid message body. Check whether the message body format and content are correct.</p>
<p id="p60879828103817"><a name="p60879828103817"></a><a name="p60879828103817"></a>Invalid message body. The message body is not needed or not JSON.</p>
</td>
</tr>
<tr id="row30625377104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p18826195816351"><a name="p18826195816351"></a><a name="p18826195816351"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p64736491104321"><a name="p64736491104321"></a><a name="p64736491104321"></a>cts.0008</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p152111044154115"><a name="p152111044154115"></a><a name="p152111044154115"></a>Data reading error.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p1925085416332"><a name="p1925085416332"></a><a name="p1925085416332"></a>Data read exception. Contact O&amp;M personnel.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p9164409104321"><a name="p9164409104321"></a><a name="p9164409104321"></a>Data reading is abnormal. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row15370821104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p28268581353"><a name="p28268581353"></a><a name="p28268581353"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p37077013104321"><a name="p37077013104321"></a><a name="p37077013104321"></a>cts.0009</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p12211174414414"><a name="p12211174414414"></a><a name="p12211174414414"></a>Data writing error.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p13508101215342"><a name="p13508101215342"></a><a name="p13508101215342"></a>Data write exception. Contact O&amp;M personnel.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p50448094104321"><a name="p50448094104321"></a><a name="p50448094104321"></a>Data writing is abnormal. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row1457821220262"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p155783123266"><a name="p155783123266"></a><a name="p155783123266"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p1057841216269"><a name="p1057841216269"></a><a name="p1057841216269"></a>cts.0010</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p757813127265"><a name="p757813127265"></a><a name="p757813127265"></a>Repeated creation.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p17224830183414"><a name="p17224830183414"></a><a name="p17224830183414"></a>Tracker is existed already.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p185781012102612"><a name="p185781012102612"></a><a name="p185781012102612"></a>The tracker already exists. Modify the tracker name and create it again.</p>
</td>
</tr>
<tr id="row51379663104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p19826155893520"><a name="p19826155893520"></a><a name="p19826155893520"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p1003135104321"><a name="p1003135104321"></a><a name="p1003135104321"></a>cts.0011</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p92117440412"><a name="p92117440412"></a><a name="p92117440412"></a>The user does not have the permission to perform the operation.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p64444444349"><a name="p64444444349"></a><a name="p64444444349"></a>The user fails the authentication or does not have permission to this operation.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p14145083104321"><a name="p14145083104321"></a><a name="p14145083104321"></a>The authentication failed or you have no rights to perform the operation.</p>
</td>
</tr>
<tr id="row60196890104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p1782665812358"><a name="p1782665812358"></a><a name="p1782665812358"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p44109908104321"><a name="p44109908104321"></a><a name="p44109908104321"></a>cts.0012</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p721113447417"><a name="p721113447417"></a><a name="p721113447417"></a>The tracker does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p59551512113619"><a name="p59551512113619"></a><a name="p59551512113619"></a>The tracker does not exist. Check whether the tracker name is correct or CTS has been enabled.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p16132815104321"><a name="p16132815104321"></a><a name="p16132815104321"></a>The tracker does not exist. Check whether the tracker name is correct.</p>
</td>
</tr>
<tr id="row10977612104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p882665883517"><a name="p882665883517"></a><a name="p882665883517"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p16771403104321"><a name="p16771403104321"></a><a name="p16771403104321"></a>cts.0013</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p121134415419"><a name="p121134415419"></a><a name="p121134415419"></a>The trace does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p13474142943614"><a name="p13474142943614"></a><a name="p13474142943614"></a>The event does not exist. Check whether the trace ID is correct.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p16306398104321"><a name="p16306398104321"></a><a name="p16306398104321"></a>The trace does not exist. Check whether the trace ID is correct.</p>
</td>
</tr>
<tr id="row11167459192620"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p14167259112611"><a name="p14167259112611"></a><a name="p14167259112611"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p816718598260"><a name="p816718598260"></a><a name="p816718598260"></a>cts.0014</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p1167135942614"><a name="p1167135942614"></a><a name="p1167135942614"></a>The token is not found.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p0449104253613"><a name="p0449104253613"></a><a name="p0449104253613"></a>No valid token found.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p5167145912620"><a name="p5167145912620"></a><a name="p5167145912620"></a>The token is not found. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row12539859104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p20826165815356"><a name="p20826165815356"></a><a name="p20826165815356"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p9095648104321"><a name="p9095648104321"></a><a name="p9095648104321"></a>cts.0015</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p1021113445410"><a name="p1021113445410"></a><a name="p1021113445410"></a>Internal service error.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p6887104617301"><a name="p6887104617301"></a><a name="p6887104617301"></a>Internal server error. Contact the O&amp;M personnel.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p65658869104321"><a name="p65658869104321"></a><a name="p65658869104321"></a>An internal service error occurs. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row54058915104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p7826158113516"><a name="p7826158113516"></a><a name="p7826158113516"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p16695960104321"><a name="p16695960104321"></a><a name="p16695960104321"></a>cts.0016</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p1421114449411"><a name="p1421114449411"></a><a name="p1421114449411"></a>Failed to write data to the cache.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p119903215316"><a name="p119903215316"></a><a name="p119903215316"></a>Failed to write data into the cache. Contact O&amp;M personnel.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p10195497104321"><a name="p10195497104321"></a><a name="p10195497104321"></a>Cache writing failed. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row24650616104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p1682635873511"><a name="p1682635873511"></a><a name="p1682635873511"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p50542912104321"><a name="p50542912104321"></a><a name="p50542912104321"></a>cts.0017</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p1621164416411"><a name="p1621164416411"></a><a name="p1621164416411"></a>Token authentication failed.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p1248711810314"><a name="p1248711810314"></a><a name="p1248711810314"></a>The token does not exist or is invalid. Check whether the token information is correct.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p335192104321"><a name="p335192104321"></a><a name="p335192104321"></a>The token does not exist or is invalid. Check whether the token information is correct.</p>
</td>
</tr>
<tr id="row3016729104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p1182611585352"><a name="p1182611585352"></a><a name="p1182611585352"></a>202</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p43028525104321"><a name="p43028525104321"></a><a name="p43028525104321"></a>cts.0018</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p182111444194110"><a name="p182111444194110"></a><a name="p182111444194110"></a>O&amp;M query is not supported.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p16864144353116"><a name="p16864144353116"></a><a name="p16864144353116"></a>The current environment does not support the calling of O&amp;M interfaces. Check whether the URL is correct.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p62758501104321"><a name="p62758501104321"></a><a name="p62758501104321"></a>The system does not support invocation of O&amp;M APIs. Check whether the URL information is correct.</p>
</td>
</tr>
<tr id="row27955602104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p4826135813357"><a name="p4826135813357"></a><a name="p4826135813357"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p49811324104321"><a name="p49811324104321"></a><a name="p49811324104321"></a>cts.0019</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p162113442415"><a name="p162113442415"></a><a name="p162113442415"></a>The AK/SK fails to be obtained. </p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p14870123919552"><a name="p14870123919552"></a><a name="p14870123919552"></a>Failed to obtain the user AK and SK.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p8185471104321"><a name="p8185471104321"></a><a name="p8185471104321"></a>Failed to obtain the AK/SK of the current user. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row6560377104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p1282617582356"><a name="p1282617582356"></a><a name="p1282617582356"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p61628499104321"><a name="p61628499104321"></a><a name="p61628499104321"></a>cts.0020</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p82111442414"><a name="p82111442414"></a><a name="p82111442414"></a>Invalid AK/SK.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p1242415501558"><a name="p1242415501558"></a><a name="p1242415501558"></a>The user AK and SK are invalid.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p25852505104321"><a name="p25852505104321"></a><a name="p25852505104321"></a>The AK/SK of the current user is invalid.</p>
</td>
</tr>
<tr id="row31345961104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p082615813355"><a name="p082615813355"></a><a name="p082615813355"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p55994909104321"><a name="p55994909104321"></a><a name="p55994909104321"></a>cts.0021</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p1421104410413"><a name="p1421104410413"></a><a name="p1421104410413"></a>OBS authentication failed.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p437203205612"><a name="p437203205612"></a><a name="p437203205612"></a>Failed to authenticate the OBS bucket. Contact O&amp;M personnel.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p39293810104321"><a name="p39293810104321"></a><a name="p39293810104321"></a>The OBS bucket does not exist. Check whether the OBS bucket has been deleted.</p>
</td>
</tr>
<tr id="row18099976104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p208261158183511"><a name="p208261158183511"></a><a name="p208261158183511"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p56811985104321"><a name="p56811985104321"></a><a name="p56811985104321"></a>cts.0022</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p32111344144120"><a name="p32111344144120"></a><a name="p32111344144120"></a>Enabled.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p52751714175619"><a name="p52751714175619"></a><a name="p52751714175619"></a>CTS cannot be repeatedly enabled. Check whether CTS has been enabled.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p38368078104321"><a name="p38368078104321"></a><a name="p38368078104321"></a>The OBS bucket authentication failed. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row9768388104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p12826758183515"><a name="p12826758183515"></a><a name="p12826758183515"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p53041963104321"><a name="p53041963104321"></a><a name="p53041963104321"></a>cts.0023</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p62118448419"><a name="p62118448419"></a><a name="p62118448419"></a>The OBS bucket has been deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p238993065612"><a name="p238993065612"></a><a name="p238993065612"></a>The OBS bucket of the current user does not exist. Check whether the OBS bucket has been deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p1431738104321"><a name="p1431738104321"></a><a name="p1431738104321"></a>The requested OBS bucket does not exist. Check whether the OBS bucket has been deleted.</p>
</td>
</tr>
<tr id="row12885649104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p16826115813514"><a name="p16826115813514"></a><a name="p16826115813514"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p37104624104321"><a name="p37104624104321"></a><a name="p37104624104321"></a>cts.0024</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p0211144184113"><a name="p0211144184113"></a><a name="p0211144184113"></a>OBS authentication failed.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p563354614568"><a name="p563354614568"></a><a name="p563354614568"></a>CTS is not authorized by the current user's OBS bucket. Check whether CTS is successfully authorized.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p52684556104321"><a name="p52684556104321"></a><a name="p52684556104321"></a>CTS failed to obtain the permission to access the OBS bucket. Check whether CTS has been authorized.</p>
</td>
</tr>
<tr id="row50409811141734"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p19826058133515"><a name="p19826058133515"></a><a name="p19826058133515"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p62147097141754"><a name="p62147097141754"></a><a name="p62147097141754"></a>cts.0025</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p32111644124110"><a name="p32111644124110"></a><a name="p32111644124110"></a>Connecting to the database failed.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p7999707570"><a name="p7999707570"></a><a name="p7999707570"></a>The api service disconnect with db.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p6327150814182"><a name="p6327150814182"></a><a name="p6327150814182"></a>The API service failed to connect to the database.</p>
</td>
</tr>
<tr id="row17586969141734"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p118261358163516"><a name="p118261358163516"></a><a name="p118261358163516"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p6750856141754"><a name="p6750856141754"></a><a name="p6750856141754"></a>cts.0026</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p112111044184115"><a name="p112111044184115"></a><a name="p112111044184115"></a>Connecting to the cache failed.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p101846103572"><a name="p101846103572"></a><a name="p101846103572"></a>The api service disconnect with cache.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p2065291714182"><a name="p2065291714182"></a><a name="p2065291714182"></a>The API service failed to connect to the Cache node.</p>
</td>
</tr>
<tr id="row60311788141734"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p58266585353"><a name="p58266585353"></a><a name="p58266585353"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p22427055141754"><a name="p22427055141754"></a><a name="p22427055141754"></a>cts.0027</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p5211204414411"><a name="p5211204414411"></a><a name="p5211204414411"></a>Failed to obtain the bucket list.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p64521219195715"><a name="p64521219195715"></a><a name="p64521219195715"></a>Failed to obtain the OBS bucket list. Contact O&amp;M personnel.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p3544112914182"><a name="p3544112914182"></a><a name="p3544112914182"></a>Failed to obtain the list of OBS buckets. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row17064349141734"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p982675853512"><a name="p982675853512"></a><a name="p982675853512"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p41869827141754"><a name="p41869827141754"></a><a name="p41869827141754"></a>cts.0028</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p152116446412"><a name="p152116446412"></a><a name="p152116446412"></a>Failed to obtain the bucket location.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p1450112919571"><a name="p1450112919571"></a><a name="p1450112919571"></a>Failed to obtain the OBS bucket location. Contact O&amp;M personnel.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p1824466414182"><a name="p1824466414182"></a><a name="p1824466414182"></a>Failed to obtain the region of the OBS bucket. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row4398956104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p11826135814356"><a name="p11826135814356"></a><a name="p11826135814356"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p20771117104321"><a name="p20771117104321"></a><a name="p20771117104321"></a>cts.0029</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p1521124412416"><a name="p1521124412416"></a><a name="p1521124412416"></a>Failed to create a bucket policy.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p1810240105718"><a name="p1810240105718"></a><a name="p1810240105718"></a>Failed to create the OBS bucket policy. Contact O&amp;M personnel.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p4738911104321"><a name="p4738911104321"></a><a name="p4738911104321"></a>Failed to create an OBS bucket policy. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row42650201104321"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p58261258113514"><a name="p58261258113514"></a><a name="p58261258113514"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p32114295104321"><a name="p32114295104321"></a><a name="p32114295104321"></a>cts.0030</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p721104410410"><a name="p721104410410"></a><a name="p721104410410"></a>Failed to delete a bucket policy.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p8975451115719"><a name="p8975451115719"></a><a name="p8975451115719"></a>Failed to delete the OBS bucket policy. Contact O&amp;M personnel.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p51121113104321"><a name="p51121113104321"></a><a name="p51121113104321"></a>Failed to delete an OBS bucket policy. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row49585498141729"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p18826145820356"><a name="p18826145820356"></a><a name="p18826145820356"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p24531402141849"><a name="p24531402141849"></a><a name="p24531402141849"></a>cts.0032</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p12111444413"><a name="p12111444413"></a><a name="p12111444413"></a>Failed to authenticate the account information.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p1135319165810"><a name="p1135319165810"></a><a name="p1135319165810"></a>Failed to check the OBS bucket existence. Contact O&amp;M personnel.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p29907289141910"><a name="p29907289141910"></a><a name="p29907289141910"></a>The OBS account information is not updated, and you can try 15 minutes later.</p>
</td>
</tr>
<tr id="row3561477141729"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p382615811351"><a name="p382615811351"></a><a name="p382615811351"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p32434406141849"><a name="p32434406141849"></a><a name="p32434406141849"></a>cts.0033</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p1921154417417"><a name="p1921154417417"></a><a name="p1921154417417"></a>The OBS bucket does not belong to the current user.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p66161510135815"><a name="p66161510135815"></a><a name="p66161510135815"></a>Account information is not refresh in OBS. Please retry after 15 minutes.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p27818130141910"><a name="p27818130141910"></a><a name="p27818130141910"></a>The OBS bucket does not belong to the current user. Check whether the OBS bucket is correct.</p>
</td>
</tr>
<tr id="row17811202141729"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p5826105833518"><a name="p5826105833518"></a><a name="p5826105833518"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p22362052141849"><a name="p22362052141849"></a><a name="p22362052141849"></a>cts.0034</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p14211044144112"><a name="p14211044144112"></a><a name="p14211044144112"></a>Failed to obtain the central region from IAM.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p743022145812"><a name="p743022145812"></a><a name="p743022145812"></a>The OBS bucket does not belong to the current user. Check whether the OBS bucket is correct.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p8318528141910"><a name="p8318528141910"></a><a name="p8318528141910"></a>Failed to obtain the central area information from IAM.</p>
</td>
</tr>
<tr id="row60025461141723"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p13826058183511"><a name="p13826058183511"></a><a name="p13826058183511"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p4119611141849"><a name="p4119611141849"></a><a name="p4119611141849"></a>cts.0036</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p1211144414110"><a name="p1211144414110"></a><a name="p1211144414110"></a>Failed to create a bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p164134549013"><a name="p164134549013"></a><a name="p164134549013"></a>Create bucket failed.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p922106141910"><a name="p922106141910"></a><a name="p922106141910"></a>Failed to create a bucket.</p>
</td>
</tr>
<tr id="row50546609141723"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p20826195811352"><a name="p20826195811352"></a><a name="p20826195811352"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p50406529141849"><a name="p50406529141849"></a><a name="p50406529141849"></a>cts.0037</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p202131544164118"><a name="p202131544164118"></a><a name="p202131544164118"></a>Failed to check the bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p2018912371219"><a name="p2018912371219"></a><a name="p2018912371219"></a>Check bucket failed.The bucket is already exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p43077086141910"><a name="p43077086141910"></a><a name="p43077086141910"></a>Failed to check the bucket, and a bucket exists.</p>
</td>
</tr>
<tr id="row2048217581364"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p1048265819617"><a name="p1048265819617"></a><a name="p1048265819617"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p34821658768"><a name="p34821658768"></a><a name="p34821658768"></a>cts.0038</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p204831358460"><a name="p204831358460"></a><a name="p204831358460"></a>Failed to obtain the project ID.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p1418213501218"><a name="p1418213501218"></a><a name="p1418213501218"></a>Failed to obtain the project ID from IAM when the system is trying to obtain keys from KMS.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p114831658669"><a name="p114831658669"></a><a name="p114831658669"></a>Failed to obtain the project ID. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row5710471570"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p07101071579"><a name="p07101071579"></a><a name="p07101071579"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p57101672720"><a name="p57101672720"></a><a name="p57101672720"></a>cts.0039</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p1371017719716"><a name="p1371017719716"></a><a name="p1371017719716"></a>The key does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p88921173216"><a name="p88921173216"></a><a name="p88921173216"></a>The KMS key id of the current user does not exist. Check whether the KMS key id has been deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p20710171573"><a name="p20710171573"></a><a name="p20710171573"></a>The key does not exist. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row6593180670"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p35934015712"><a name="p35934015712"></a><a name="p35934015712"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p1593201671"><a name="p1593201671"></a><a name="p1593201671"></a>cts.0040</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p75931109719"><a name="p75931109719"></a><a name="p75931109719"></a>Failed to obtain the key.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p132521121128"><a name="p132521121128"></a><a name="p132521121128"></a>Failed to obtain key list from KMS.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p2593110372"><a name="p2593110372"></a><a name="p2593110372"></a>Failed to obtain the key. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row16293451677"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p112931551671"><a name="p112931551671"></a><a name="p112931551671"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p132931150713"><a name="p132931150713"></a><a name="p132931150713"></a>cts.0041</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p1229313516710"><a name="p1229313516710"></a><a name="p1229313516710"></a>Failed to create a log topic or group.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p8197193515213"><a name="p8197193515213"></a><a name="p8197193515213"></a>Create log group or log topic failed, create tracker failed, please try again.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p52931655714"><a name="p52931655714"></a><a name="p52931655714"></a>Failed to create a log topic or group. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row553322511834"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p178261158183513"><a name="p178261158183513"></a><a name="p178261158183513"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p4553805111834"><a name="p4553805111834"></a><a name="p4553805111834"></a>cts.0043</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p17213144174117"><a name="p17213144174117"></a><a name="p17213144174117"></a>Failed to check the bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p1370225813144"><a name="p1370225813144"></a><a name="p1370225813144"></a>Check bucket failed. Contact O&amp;M personnel.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p6470349711834"><a name="p6470349711834"></a><a name="p6470349711834"></a>Failed to query the bucket. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row4820900711929"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p13826258103513"><a name="p13826258103513"></a><a name="p13826258103513"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p1261552711929"><a name="p1261552711929"></a><a name="p1261552711929"></a>cts.0044</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p521310447418"><a name="p521310447418"></a><a name="p521310447418"></a>Failed to set the bucket lifecycle.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p11701198151518"><a name="p11701198151518"></a><a name="p11701198151518"></a>Set bucket life cycle failed. Contact O&amp;M personnel.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p1522475111929"><a name="p1522475111929"></a><a name="p1522475111929"></a>Failed to set the bucket lifecycle. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row56979938111253"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p10826175810359"><a name="p10826175810359"></a><a name="p10826175810359"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p51972250111253"><a name="p51972250111253"></a><a name="p51972250111253"></a>cts.0045</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p3213184484120"><a name="p3213184484120"></a><a name="p3213184484120"></a>Failed to obtain the bucket lifecycle.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p090619227154"><a name="p090619227154"></a><a name="p090619227154"></a>Get bucket life cycle failed. Contact O&amp;M personnel.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p49002698111253"><a name="p49002698111253"></a><a name="p49002698111253"></a>Failed to obtain the bucket lifecycle. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row47885434112027"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p1182635843511"><a name="p1182635843511"></a><a name="p1182635843511"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p53514923112027"><a name="p53514923112027"></a><a name="p53514923112027"></a>cts.0046</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p13213144410414"><a name="p13213144410414"></a><a name="p13213144410414"></a>The number of created trackers reaches the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p1890531201617"><a name="p1890531201617"></a><a name="p1890531201617"></a>The maximum number of trackers is: %s.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p39741538112027"><a name="p39741538112027"></a><a name="p39741538112027"></a>Failed to create the tracker. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row1628485994"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p92849517916"><a name="p92849517916"></a><a name="p92849517916"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p18284135694"><a name="p18284135694"></a><a name="p18284135694"></a>cts.0048</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p192841454919"><a name="p192841454919"></a><a name="p192841454919"></a>Failed to delete the data tracker.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p14160114101612"><a name="p14160114101612"></a><a name="p14160114101612"></a>Failed to delete the tracker, Please try again.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p1786611362913"><a name="p1786611362913"></a><a name="p1786611362913"></a>Failed to delete the tracker. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row462613161291"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p06261716997"><a name="p06261716997"></a><a name="p06261716997"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p116261161099"><a name="p116261161099"></a><a name="p116261161099"></a>cts.0049</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p116261716793"><a name="p116261716793"></a><a name="p116261716793"></a>A bucket cannot be used to create multiple trackers that record operations of the same type.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p1186743212163"><a name="p1186743212163"></a><a name="p1186743212163"></a>You cannot create different trackers to record the same type of operations on the same OBS bucket.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p1662611166916"><a name="p1662611166916"></a><a name="p1662611166916"></a>Failed to create the tracker. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row20626216198"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p18626121611916"><a name="p18626121611916"></a><a name="p18626121611916"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p1762615165914"><a name="p1762615165914"></a><a name="p1762615165914"></a>cts.0050</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p562651613916"><a name="p562651613916"></a><a name="p562651613916"></a>The tracked bucket cannot be modified.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p5402184917165"><a name="p5402184917165"></a><a name="p5402184917165"></a>The tracked OBS bucket can not be modify.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p1462614167912"><a name="p1462614167912"></a><a name="p1462614167912"></a>You are not allowed to modify the tracked OBS bucket.</p>
</td>
</tr>
<tr id="row206262016399"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p0626816692"><a name="p0626816692"></a><a name="p0626816692"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p1662611162917"><a name="p1662611162917"></a><a name="p1662611162917"></a>cts.0051</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p362615161092"><a name="p362615161092"></a><a name="p362615161092"></a>A bucket cannot be traced by multiple trackers.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p12117192181719"><a name="p12117192181719"></a><a name="p12117192181719"></a>Failed to configure the tracker because the new settings could not be applied to the log group or log topic. Try again later.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p1862631614912"><a name="p1862631614912"></a><a name="p1862631614912"></a>An OBS bucket can be tracked by only one tracker.</p>
</td>
</tr>
<tr id="row10626121615911"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p86269169911"><a name="p86269169911"></a><a name="p86269169911"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p1062661614911"><a name="p1062661614911"></a><a name="p1062661614911"></a>cts.0052</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p06265163917"><a name="p06265163917"></a><a name="p06265163917"></a>Failed to delete the log topic.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p2541929101713"><a name="p2541929101713"></a><a name="p2541929101713"></a>The topic in LTS deleted failed, tracker deleted failed. Please try again or delete the topic manually.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p116261116094"><a name="p116261116094"></a><a name="p116261116094"></a>Failed to delete the log topic. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row1362771612919"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p16627121617910"><a name="p16627121617910"></a><a name="p16627121617910"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p19627111610920"><a name="p19627111610920"></a><a name="p19627111610920"></a>cts.0054</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p062714161292"><a name="p062714161292"></a><a name="p062714161292"></a>The key operation notification already exists.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p62820191818"><a name="p62820191818"></a><a name="p62820191818"></a>Notification name is existed already.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p66271016895"><a name="p66271016895"></a><a name="p66271016895"></a>The key operation notification already exists and cannot be created repeatedly.</p>
</td>
</tr>
<tr id="row1662715161997"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p12627131618912"><a name="p12627131618912"></a><a name="p12627131618912"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p762751610918"><a name="p762751610918"></a><a name="p762751610918"></a>cts.0055</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p962741612915"><a name="p962741612915"></a><a name="p962741612915"></a>The key operation notification does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p573192619188"><a name="p573192619188"></a><a name="p573192619188"></a>The notification does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p106271616298"><a name="p106271616298"></a><a name="p106271616298"></a>The key operation notification does not exist. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row126279166919"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p1162719169910"><a name="p1162719169910"></a><a name="p1162719169910"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p18627161614918"><a name="p18627161614918"></a><a name="p18627161614918"></a>cts.0056</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p13627181610917"><a name="p13627181610917"></a><a name="p13627181610917"></a>The number of key operation notifications reaches the upper limit.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p12630335181813"><a name="p12630335181813"></a><a name="p12630335181813"></a>The quantity has exceeded the maximum quantity limit.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p176277167917"><a name="p176277167917"></a><a name="p176277167917"></a>Failed to create the key operation notification. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row106272161093"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p17627201615917"><a name="p17627201615917"></a><a name="p17627201615917"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p76275161095"><a name="p76275161095"></a><a name="p76275161095"></a>cts.0057</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p146279161592"><a name="p146279161592"></a><a name="p146279161592"></a>Failed to start or stop the key operation notification.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p852254516187"><a name="p852254516187"></a><a name="p852254516187"></a>State setting failed, check if topicId exists.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p1627916995"><a name="p1627916995"></a><a name="p1627916995"></a>Failed to start or stop the key operation notification. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row325111281099"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p7251028791"><a name="p7251028791"></a><a name="p7251028791"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p1325102817911"><a name="p1325102817911"></a><a name="p1325102817911"></a>cts.0058</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p725102817913"><a name="p725102817913"></a><a name="p725102817913"></a>Failed to obtain group users from IAM.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p296313313193"><a name="p296313313193"></a><a name="p296313313193"></a>Get group users failed from IAM.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p1925142810916"><a name="p1925142810916"></a><a name="p1925142810916"></a>Failed to obtain group users from IAM. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row225115281798"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p2251728599"><a name="p2251728599"></a><a name="p2251728599"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p1025192819910"><a name="p1025192819910"></a><a name="p1025192819910"></a>cts.0059</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p92511328997"><a name="p92511328997"></a><a name="p92511328997"></a>An error occurred when querying the <strong id="b1578831815416"><a name="b1578831815416"></a><a name="b1578831815416"></a>page_type</strong> parameter in the CDR.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p11491749102113"><a name="p11491749102113"></a><a name="p11491749102113"></a>Get meter data failed, the page_type parameter must be 2.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p19251228696"><a name="p19251228696"></a><a name="p19251228696"></a>The <strong id="b1090603214541"><a name="b1090603214541"></a><a name="b1090603214541"></a>page_type</strong> parameter must be set to <strong id="b1556712387540"><a name="b1556712387540"></a><a name="b1556712387540"></a>2</strong>.</p>
</td>
</tr>
<tr id="row1925115281496"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p172514289910"><a name="p172514289910"></a><a name="p172514289910"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p525219281913"><a name="p525219281913"></a><a name="p525219281913"></a>cts.0060</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p162526282913"><a name="p162526282913"></a><a name="p162526282913"></a>An error occurred when querying the <strong id="b1341333019552"><a name="b1341333019552"></a><a name="b1341333019552"></a>limit</strong> parameter in the CDR.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p19925180192214"><a name="p19925180192214"></a><a name="p19925180192214"></a>Get meter data failed, the limit parameter should be greater than 0 or equal to 1000.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p102521928593"><a name="p102521928593"></a><a name="p102521928593"></a>The <strong id="b1675054814554"><a name="b1675054814554"></a><a name="b1675054814554"></a>limit</strong> parameter must be set to <strong id="b1439181765618"><a name="b1439181765618"></a><a name="b1439181765618"></a>0-1000</strong>.</p>
</td>
</tr>
<tr id="row1525218281916"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p1325232810914"><a name="p1325232810914"></a><a name="p1325232810914"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p1425242820915"><a name="p1425242820915"></a><a name="p1425242820915"></a>cts.0061</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p1325262811910"><a name="p1325262811910"></a><a name="p1325262811910"></a>The project ID in the request does not match that in the token.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p154661714152215"><a name="p154661714152215"></a><a name="p154661714152215"></a>CSB update CTS status error, projectId in token is not equal projectId in body.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p14252172811914"><a name="p14252172811914"></a><a name="p14252172811914"></a>The project ID in the token is different from that in the request. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row18252528197"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p1252428798"><a name="p1252428798"></a><a name="p1252428798"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p15252728094"><a name="p15252728094"></a><a name="p15252728094"></a>cts.0062</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p62521281913"><a name="p62521281913"></a><a name="p62521281913"></a>The tracked bucket has been deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p2912123162216"><a name="p2912123162216"></a><a name="p2912123162216"></a>The OBS bucket of the current user does not exist. Check whether the tracked bucket has been deleted.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p42525281792"><a name="p42525281792"></a><a name="p42525281792"></a>Check whether the tracked bucket has been deleted.</p>
</td>
</tr>
<tr id="row62523289918"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p4252152817912"><a name="p4252152817912"></a><a name="p4252152817912"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p52529284916"><a name="p52529284916"></a><a name="p52529284916"></a>cts.0063</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p12252192814914"><a name="p12252192814914"></a><a name="p12252192814914"></a>The current version number cannot be queried.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p204561635132217"><a name="p204561635132217"></a><a name="p204561635132217"></a>CTS does not support API interface version query.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p18252192814918"><a name="p18252192814918"></a><a name="p18252192814918"></a>The current version number cannot be queried.</p>
</td>
</tr>
<tr id="row11252128198"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p122521128898"><a name="p122521128898"></a><a name="p122521128898"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p112521028993"><a name="p112521028993"></a><a name="p112521028993"></a>cts.0064</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p1525218281496"><a name="p1525218281496"></a><a name="p1525218281496"></a>The SMN topic does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p148074415228"><a name="p148074415228"></a><a name="p148074415228"></a>The SMN topic does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p1025222811920"><a name="p1025222811920"></a><a name="p1025222811920"></a>The SMN topic does not exist. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row102527281395"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p725202812914"><a name="p725202812914"></a><a name="p725202812914"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p425214281097"><a name="p425214281097"></a><a name="p425214281097"></a>cts.0065</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p142522028990"><a name="p142522028990"></a><a name="p142522028990"></a>The language and time zone obtained from the CBC are incorrect.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p18407801231"><a name="p18407801231"></a><a name="p18407801231"></a>Failed to get time zone and language from CBC.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p192522028795"><a name="p192522028795"></a><a name="p192522028795"></a>The language and time zone obtained from the CBC are incorrect. Contact O&amp;M personnel.</p>
</td>
</tr>
<tr id="row10252142817912"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.1 "><p id="p1252172815916"><a name="p1252172815916"></a><a name="p1252172815916"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.6.1.2 "><p id="p82529281996"><a name="p82529281996"></a><a name="p82529281996"></a>cts.0066</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="p9252112811919"><a name="p9252112811919"></a><a name="p9252112811919"></a>Failed to obtain AK/SK from IAM.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.4 "><p id="p97941594237"><a name="p97941594237"></a><a name="p97941594237"></a>Failed to get AK/SK from IAM.</p>
</td>
<td class="cellrowborder" valign="top" width="33.5%" headers="mcps1.2.6.1.5 "><p id="p22528285914"><a name="p22528285914"></a><a name="p22528285914"></a>Failed to obtain AK/SK from IAM. Contact O&amp;M personnel.</p>
</td>
</tr>
</tbody>
</table>

