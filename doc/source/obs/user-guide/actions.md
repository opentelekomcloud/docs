# Actions<a name="obs_03_0051"></a>

Actions are related to resources. When the resource is the current bucket, actions configured in the bucket policy must be bucket related actions. When objects are specified as resources, actions configured in the bucket policy must be object related actions.

Actions can be specified in either of the following ways:

-   **Include**: Specifies the actions on which the bucket policy takes effect.
-   **Exclude**: Specifies that on all except the specified actions the bucket policy takes effect.

## Actions Related to Buckets<a name="section88267409555"></a>

**Table  1**  Actions related to buckets

<a name="table13827194016555"></a>
<table><thead align="left"><tr id="row85334118557"><th class="cellrowborder" valign="top" width="16.16%" id="mcps1.2.4.1.1"><p id="p195334120552"><a name="p195334120552"></a><a name="p195334120552"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="30.3%" id="mcps1.2.4.1.2"><p id="p175354120557"><a name="p175354120557"></a><a name="p175354120557"></a>Value</p>
</th>
<th class="cellrowborder" valign="top" width="53.54%" id="mcps1.2.4.1.3"><p id="p1453144125511"><a name="p1453144125511"></a><a name="p1453144125511"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row453184117553"><td class="cellrowborder" rowspan="4" valign="top" width="16.16%" headers="mcps1.2.4.1.1 "><p id="p5531411558"><a name="p5531411558"></a><a name="p5531411558"></a>General</p>
</td>
<td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.4.1.2 "><p id="p453174113553"><a name="p453174113553"></a><a name="p453174113553"></a>*</p>
</td>
<td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.4.1.3 "><p id="p135334117553"><a name="p135334117553"></a><a name="p135334117553"></a>The value supports a wildcard character (*) that indicates all operations can be performed.</p>
</td>
</tr>
<tr id="row1453124118553"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p15334135514"><a name="p15334135514"></a><a name="p15334135514"></a>Get*</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1153041155513"><a name="p1153041155513"></a><a name="p1153041155513"></a>The value supports a wildcard character (*) that indicates all GET operations can be performed.</p>
</td>
</tr>
<tr id="row55304185517"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1553124165517"><a name="p1553124165517"></a><a name="p1553124165517"></a>Put*</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p13535414553"><a name="p13535414553"></a><a name="p13535414553"></a>The value supports a wildcard character (*) that indicates all PUT operations can be performed.</p>
</td>
</tr>
<tr id="row1053184119554"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p853741105510"><a name="p853741105510"></a><a name="p853741105510"></a>List*</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p653441185516"><a name="p653441185516"></a><a name="p653441185516"></a>The value supports a wildcard character (*) that indicates all LIST operations can be performed.</p>
</td>
</tr>
<tr id="row6531441135518"><td class="cellrowborder" rowspan="18" valign="top" width="16.16%" headers="mcps1.2.4.1.1 "><p id="p13531541105510"><a name="p13531541105510"></a><a name="p13531541105510"></a>Bucket</p>
</td>
<td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.4.1.2 "><p id="p19531141125518"><a name="p19531141125518"></a><a name="p19531141125518"></a>DeleteBucket</p>
</td>
<td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.4.1.3 "><p id="p175384145515"><a name="p175384145515"></a><a name="p175384145515"></a>Deletes the bucket.</p>
</td>
</tr>
<tr id="row1154041115519"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p9541741175510"><a name="p9541741175510"></a><a name="p9541741175510"></a>ListBucket</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1154134112551"><a name="p1154134112551"></a><a name="p1154134112551"></a>Lists objects in the bucket, and gets the bucket metadata.</p>
</td>
</tr>
<tr id="row95474110559"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p20541041185513"><a name="p20541041185513"></a><a name="p20541041185513"></a>ListBucketVersions</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1254144145510"><a name="p1254144145510"></a><a name="p1254144145510"></a>Lists object versions in the bucket.</p>
</td>
</tr>
<tr id="row12542041195514"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p135413411555"><a name="p135413411555"></a><a name="p135413411555"></a>ListBucketMultipartUploads</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p954184135510"><a name="p954184135510"></a><a name="p954184135510"></a>Lists multipart upload tasks.</p>
</td>
</tr>
<tr id="row3541541155515"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p45474113559"><a name="p45474113559"></a><a name="p45474113559"></a>GetBucketAcl</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1545412557"><a name="p1545412557"></a><a name="p1545412557"></a>Obtains the ACL information of the bucket.</p>
</td>
</tr>
<tr id="row1541541125517"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1854144125519"><a name="p1854144125519"></a><a name="p1854144125519"></a>PutBucketAcl</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p185424175514"><a name="p185424175514"></a><a name="p185424175514"></a>Configures the ACL for the bucket.</p>
</td>
</tr>
<tr id="row19548412556"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p17546419559"><a name="p17546419559"></a><a name="p17546419559"></a>GetBucketCORS</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p17545414556"><a name="p17545414556"></a><a name="p17545414556"></a>Obtains the CORS configuration of the bucket.</p>
</td>
</tr>
<tr id="row154174165511"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p13545418559"><a name="p13545418559"></a><a name="p13545418559"></a>PutBucketCORS</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1554341195517"><a name="p1554341195517"></a><a name="p1554341195517"></a>Configures CORS for the bucket.</p>
</td>
</tr>
<tr id="row18541541155513"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p35424175510"><a name="p35424175510"></a><a name="p35424175510"></a>GetBucketVersioning</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p25694120558"><a name="p25694120558"></a><a name="p25694120558"></a>Obtains the versioning information of the bucket.</p>
</td>
</tr>
<tr id="row1556124110550"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p256114114557"><a name="p256114114557"></a><a name="p256114114557"></a>PutBucketVersioning</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p8561041165514"><a name="p8561041165514"></a><a name="p8561041165514"></a>Configures versioning for the bucket.</p>
</td>
</tr>
<tr id="row1956174175518"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p105616414553"><a name="p105616414553"></a><a name="p105616414553"></a>GetBucketLocation</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p65684195517"><a name="p65684195517"></a><a name="p65684195517"></a>Obtains the bucket location.</p>
</td>
</tr>
<tr id="row65694112559"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p19567419551"><a name="p19567419551"></a><a name="p19567419551"></a>GetBucketLogging</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p20561941195520"><a name="p20561941195520"></a><a name="p20561941195520"></a>Obtains the bucket logging information.</p>
</td>
</tr>
<tr id="row25624135520"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p8576412557"><a name="p8576412557"></a><a name="p8576412557"></a>PutBucketLogging</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p65794105515"><a name="p65794105515"></a><a name="p65794105515"></a>Configures logging for the bucket.</p>
</td>
</tr>
<tr id="row1457341125512"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p125714418556"><a name="p125714418556"></a><a name="p125714418556"></a>GetBucketWebsite</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p145710418554"><a name="p145710418554"></a><a name="p145710418554"></a>Obtains the static website configuration information about the bucket.</p>
</td>
</tr>
<tr id="row135744120554"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p957184112553"><a name="p957184112553"></a><a name="p957184112553"></a>PutBucketWebsite</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1457154115555"><a name="p1457154115555"></a><a name="p1457154115555"></a>Configures the static website hosting for the bucket.</p>
</td>
</tr>
<tr id="row8571941185515"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p757164111551"><a name="p757164111551"></a><a name="p757164111551"></a>DeleteBucketWebsite</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p11573417559"><a name="p11573417559"></a><a name="p11573417559"></a>Cancels the static website hosting configuration of the bucket.</p>
</td>
</tr>
<tr id="row165719411553"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1357104117554"><a name="p1357104117554"></a><a name="p1357104117554"></a>GetLifecycleConfiguration</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p5581441145518"><a name="p5581441145518"></a><a name="p5581441145518"></a>Obtains the lifecycle rules of the bucket.</p>
</td>
</tr>
<tr id="row658341115520"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1358124115511"><a name="p1358124115511"></a><a name="p1358124115511"></a>PutLifecycleConfiguration</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1558941115516"><a name="p1558941115516"></a><a name="p1558941115516"></a>Configures a lifecycle rule for the bucket.</p>
</td>
</tr>
</tbody>
</table>

## Actions Related to Objects<a name="section387654045518"></a>

**Table  2**  Actions related to objects

<a name="table1020518423242"></a>
<table><thead align="left"><tr id="row1620644218243"><th class="cellrowborder" valign="top" width="16.16%" id="mcps1.2.4.1.1"><p id="p120612421243"><a name="p120612421243"></a><a name="p120612421243"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="30.3%" id="mcps1.2.4.1.2"><p id="p1920614217245"><a name="p1920614217245"></a><a name="p1920614217245"></a>Value</p>
</th>
<th class="cellrowborder" valign="top" width="53.54%" id="mcps1.2.4.1.3"><p id="p4206442152416"><a name="p4206442152416"></a><a name="p4206442152416"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5206204282412"><td class="cellrowborder" rowspan="4" valign="top" width="16.16%" headers="mcps1.2.4.1.1 "><p id="p112069421244"><a name="p112069421244"></a><a name="p112069421244"></a>General</p>
</td>
<td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.4.1.2 "><p id="p17206342142415"><a name="p17206342142415"></a><a name="p17206342142415"></a>*</p>
</td>
<td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.4.1.3 "><p id="p320664292412"><a name="p320664292412"></a><a name="p320664292412"></a>The value supports a wildcard character (*) that indicates all operations can be performed.</p>
</td>
</tr>
<tr id="row620624218240"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1720611423245"><a name="p1720611423245"></a><a name="p1720611423245"></a>Get*</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1320617422244"><a name="p1320617422244"></a><a name="p1320617422244"></a>The value supports a wildcard character (*) that indicates all GET operations can be performed.</p>
</td>
</tr>
<tr id="row1220634216241"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p7206134202415"><a name="p7206134202415"></a><a name="p7206134202415"></a>Put*</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p620616420248"><a name="p620616420248"></a><a name="p620616420248"></a>The value supports a wildcard character (*) that indicates all PUT operations can be performed.</p>
</td>
</tr>
<tr id="row5206164262415"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p19206144252410"><a name="p19206144252410"></a><a name="p19206144252410"></a>List*</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p152061042112416"><a name="p152061042112416"></a><a name="p152061042112416"></a>The value supports a wildcard character (*) that indicates all LIST operations can be performed.</p>
</td>
</tr>
<tr id="row13206342192416"><td class="cellrowborder" rowspan="11" valign="top" width="16.16%" headers="mcps1.2.4.1.1 "><p id="p9206144211241"><a name="p9206144211241"></a><a name="p9206144211241"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="30.3%" headers="mcps1.2.4.1.2 "><p id="p7206134213245"><a name="p7206134213245"></a><a name="p7206134213245"></a>GetObject</p>
</td>
<td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.2.4.1.3 "><p id="p8206242122419"><a name="p8206242122419"></a><a name="p8206242122419"></a>Obtains the object and its metadata.</p>
</td>
</tr>
<tr id="row120674272415"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p162069427248"><a name="p162069427248"></a><a name="p162069427248"></a>GetObjectVersion</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p620684210243"><a name="p620684210243"></a><a name="p620684210243"></a>Obtains the object of a specified version and its metadata.</p>
</td>
</tr>
<tr id="row17207842192410"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p142073426242"><a name="p142073426242"></a><a name="p142073426242"></a>PutObject</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p220794282413"><a name="p220794282413"></a><a name="p220794282413"></a>Performs PUT upload, POST upload, multipart upload, initialization of uploaded parts, and merging of parts.</p>
</td>
</tr>
<tr id="row3207144232415"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p132071542162416"><a name="p132071542162416"></a><a name="p132071542162416"></a>GetObjectAcl</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p120704242415"><a name="p120704242415"></a><a name="p120704242415"></a>Obtains the object ACL information.</p>
</td>
</tr>
<tr id="row3207144272419"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p8207194212243"><a name="p8207194212243"></a><a name="p8207194212243"></a>GetObjectVersionAcl</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p172071042192415"><a name="p172071042192415"></a><a name="p172071042192415"></a>Obtains the ACL information of a specified object version.</p>
</td>
</tr>
<tr id="row202072042172419"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p52071642162419"><a name="p52071642162419"></a><a name="p52071642162419"></a>PutObjectAcl</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p420704222419"><a name="p420704222419"></a><a name="p420704222419"></a>Configures the ACL for an object.</p>
</td>
</tr>
<tr id="row720715423242"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p12071942182413"><a name="p12071942182413"></a><a name="p12071942182413"></a>PutObjectVersionAcl</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p120744282411"><a name="p120744282411"></a><a name="p120744282411"></a>Configures the ACL for a specified object version.</p>
</td>
</tr>
<tr id="row1120704216242"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p520716423242"><a name="p520716423242"></a><a name="p520716423242"></a>DeleteObject</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p142071342192417"><a name="p142071342192417"></a><a name="p142071342192417"></a>Deletes an object.</p>
</td>
</tr>
<tr id="row1320714423244"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p10207842172412"><a name="p10207842172412"></a><a name="p10207842172412"></a>DeleteObjectVersion</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1120794212240"><a name="p1120794212240"></a><a name="p1120794212240"></a>Deletes a specified object version.</p>
</td>
</tr>
<tr id="row92071342112420"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1620711424248"><a name="p1620711424248"></a><a name="p1620711424248"></a>ListMultipartUploadParts</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1208164202420"><a name="p1208164202420"></a><a name="p1208164202420"></a>Lists uploaded parts.</p>
</td>
</tr>
<tr id="row1420864214247"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p2208184292413"><a name="p2208184292413"></a><a name="p2208184292413"></a>AbortMultipartUpload</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p5208174242416"><a name="p5208174242416"></a><a name="p5208174242416"></a>Cancels a multipart upload task.</p>
</td>
</tr>
</tbody>
</table>

