# Copy Object<a name="obs_03_0062"></a>

You can copy an object to a new object with the same name.

Two methods of copying an object are as follows:

1.  Use PUT method and add the  **X-Copy-From**  request header.
2.  Use the COPY method.

The preceding two methods have the same effect.

The COPY operation always creates a new object. If you use this operation on an existing object, replace the existing object and metadata.

If you use this operation to copy a manifest object, the new object is a normal object and not a copy of the manifest. Instead it is a concatenation of all the segment objects. This means that you cannot copy objects larger than 5 GB in size.

## Method<a name="section39869956112928"></a>

**Table  1**  Method description

<a name="table36630378113016"></a>
<table><thead align="left"><tr id="row48730343113016"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p5336715811413"><a name="p5336715811413"></a><a name="p5336715811413"></a>Method</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p51296332113016"><a name="p51296332113016"></a><a name="p51296332113016"></a><strong id="b39273688114629"><a name="b39273688114629"></a><a name="b39273688114629"></a>URI</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p61362190113016"><a name="p61362190113016"></a><a name="p61362190113016"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15388804113016"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p38533588113016"><a name="p38533588113016"></a><a name="p38533588113016"></a>COPY</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52757727113245"><a name="p52757727113245"></a><a name="p52757727113245"></a>/v1/{account}/{container}/{object}</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19784190113016"><a name="p19784190113016"></a><a name="p19784190113016"></a>Copies an object to another object in OBS (compatible with OpenStack Swift).</p>
</td>
</tr>
</tbody>
</table>

**\{account\}**  indicates the name of an account.

**\{container\}**  indicates the name of a container.

**\{object\}**  indicates the name of an object.

This operation does not involve a request body.

## Example Request<a name="section16623225"></a>

Copy the  **goodbye** object from the **marktwain** container to the **janeausten**  container:

```
curl -i $publicURL/marktwain/goodbye -X COPY -H "X-Auth-Token:
$token" -H "Destination: janeausten/goodbye"
```

```
curl -i $publicURL/janeausten/goodbye -X PUT -H "X-Auth-Token:
$token" -H "X-Copy-From: /marktwain/goodbye" -H "Content-Length:
0"
```

## Request Query Parameters<a name="section5103708"></a>

This operation does not include request query parameters.

## Request Headers<a name="section2186955"></a>

Request URI parameters

<a name="table22064127165949"></a>
<table><thead align="left"><tr id="row51611586165949"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p19788932165949"><a name="p19788932165949"></a><a name="p19788932165949"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p64834772165949"><a name="p64834772165949"></a><a name="p64834772165949"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p19908989165949"><a name="p19908989165949"></a><a name="p19908989165949"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18138392165949"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p59923656165949"><a name="p59923656165949"></a><a name="p59923656165949"></a>{account}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p21977948165949"><a name="p21977948165949"></a><a name="p21977948165949"></a>String</p>
<p id="p63583807165949"><a name="p63583807165949"></a><a name="p63583807165949"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p50014757165949"><a name="p50014757165949"></a><a name="p50014757165949"></a>Unique name of the account. In the current version, it indicates the unique ID of the account.</p>
</td>
</tr>
<tr id="row47479634165949"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p20645123165949"><a name="p20645123165949"></a><a name="p20645123165949"></a>{container}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p61642298165949"><a name="p61642298165949"></a><a name="p61642298165949"></a>String</p>
<p id="p17909770165949"><a name="p17909770165949"></a><a name="p17909770165949"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p41405250165949"><a name="p41405250165949"></a><a name="p41405250165949"></a>Unique name of the container.</p>
<p id="p37102931165949"><a name="p37102931165949"></a><a name="p37102931165949"></a>For details about container naming rules, see <a href="naming-rules.md">Naming Rules</a>.</p>
</td>
</tr>
<tr id="row52547463165949"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p28486111165949"><a name="p28486111165949"></a><a name="p28486111165949"></a>{object}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p25673668165949"><a name="p25673668165949"></a><a name="p25673668165949"></a>String</p>
<p id="p29736422165949"><a name="p29736422165949"></a><a name="p29736422165949"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p59840009165949"><a name="p59840009165949"></a><a name="p59840009165949"></a>Name of the object.</p>
<p id="p1689171165949"><a name="p1689171165949"></a><a name="p1689171165949"></a>For details about object naming rules, see <a href="naming-rules.md#section23579102">Object Naming Rules</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Request header parameters

<a name="table2605133165949"></a>
<table><thead align="left"><tr id="row34737820165949"><th class="cellrowborder" valign="top" width="36.54%" id="mcps1.2.4.1.1"><p id="p62300058165949"><a name="p62300058165949"></a><a name="p62300058165949"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="16.939999999999998%" id="mcps1.2.4.1.2"><p id="p51150344165949"><a name="p51150344165949"></a><a name="p51150344165949"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.52%" id="mcps1.2.4.1.3"><p id="p43181781165949"><a name="p43181781165949"></a><a name="p43181781165949"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5461419165949"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p39721770165949"><a name="p39721770165949"></a><a name="p39721770165949"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p63346790165949"><a name="p63346790165949"></a><a name="p63346790165949"></a>String</p>
<p id="p33250198165949"><a name="p33250198165949"></a><a name="p33250198165949"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p8911479165949"><a name="p8911479165949"></a><a name="p8911479165949"></a>Authentication token. If you omit this header, your request fails unless the account owner has granted you access through an ACL.</p>
</td>
</tr>
<tr id="row6199553317024"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p2108888817024"><a name="p2108888817024"></a><a name="p2108888817024"></a>Destination</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p4885976117040"><a name="p4885976117040"></a><a name="p4885976117040"></a>String</p>
<p id="p3708466617040"><a name="p3708466617040"></a><a name="p3708466617040"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p5282619417024"><a name="p5282619417024"></a><a name="p5282619417024"></a>The container and object name of the destination object in the form of <strong id="b54702703"><a name="b54702703"></a><a name="b54702703"></a>/container/object</strong>.</p>
</td>
</tr>
<tr id="row13094450165949"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p54017555165949"><a name="p54017555165949"></a><a name="p54017555165949"></a>X-Object-Meta-name</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p13345873165949"><a name="p13345873165949"></a><a name="p13345873165949"></a>String</p>
<p id="p53003998165949"><a name="p53003998165949"></a><a name="p53003998165949"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p65465458165949"><a name="p65465458165949"></a><a name="p65465458165949"></a>Object metadata, where <strong id="b2150722715140"><a name="b2150722715140"></a><a name="b2150722715140"></a>{name}</strong>&nbsp;is the name of the metadata item. You must specify an&nbsp;<strong id="b1327692239145812"><a name="b1327692239145812"></a><a name="b1327692239145812"></a>X-Object-Meta-{name}</strong>&nbsp;header for each metadata item (for each&nbsp;<strong id="b1639042642145812"><a name="b1639042642145812"></a><a name="b1639042642145812"></a>{name}</strong>) that you want to add or update.</p>
</td>
</tr>
<tr id="row52318210165949"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p9916613165949"><a name="p9916613165949"></a><a name="p9916613165949"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p65048197165949"><a name="p65048197165949"></a><a name="p65048197165949"></a>String</p>
<p id="p48562863165949"><a name="p48562863165949"></a><a name="p48562863165949"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p41277812165949"><a name="p41277812165949"></a><a name="p41277812165949"></a>Sets the MIME type of the object.</p>
</td>
</tr>
<tr id="row42990608165949"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p59687260165949"><a name="p59687260165949"></a><a name="p59687260165949"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p2829859165949"><a name="p2829859165949"></a><a name="p2829859165949"></a>String</p>
<p id="p25468737165949"><a name="p25468737165949"></a><a name="p25468737165949"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p49701839165949"><a name="p49701839165949"></a><a name="p49701839165949"></a>Object length.</p>
</td>
</tr>
<tr id="row49988103165949"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p22504532165949"><a name="p22504532165949"></a><a name="p22504532165949"></a>Content-Disposition</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p10927785165949"><a name="p10927785165949"></a><a name="p10927785165949"></a>String</p>
<p id="p31241207165949"><a name="p31241207165949"></a><a name="p31241207165949"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p47509804165949"><a name="p47509804165949"></a><a name="p47509804165949"></a>When the header is set to <strong id="b6222962"><a name="b6222962"></a><a name="b6222962"></a>{newname}</strong>&nbsp;and an object is downloaded through a browser, the default object name&nbsp;<strong id="b56006663"><a name="b56006663"></a><a name="b56006663"></a>{newname}</strong> is returned.</p>
</td>
</tr>
<tr id="row24935053165949"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p6473452165949"><a name="p6473452165949"></a><a name="p6473452165949"></a>Content-Encoding</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p54587636165949"><a name="p54587636165949"></a><a name="p54587636165949"></a>String</p>
<p id="p21526678165949"><a name="p21526678165949"></a><a name="p21526678165949"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p65939373165949"><a name="p65939373165949"></a><a name="p65939373165949"></a>If this header is set, the value is the encoding format used when an object is downloaded through a browser.</p>
</td>
</tr>
<tr id="row4458523217727"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p5463404017727"><a name="p5463404017727"></a><a name="p5463404017727"></a>X-Copy-From</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p4911470617738"><a name="p4911470617738"></a><a name="p4911470617738"></a>String</p>
<p id="p3937917417738"><a name="p3937917417738"></a><a name="p3937917417738"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p2549813417727"><a name="p2549813417727"></a><a name="p2549813417727"></a>Container and object name of the source object in the form of <strong id="b49251786"><a name="b49251786"></a><a name="b49251786"></a>/container/object</strong>.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If the  **X-Copy-From** or **Destination** header is used to specify the name of a source or destination object, only the **/container/object**  format is supported. OpenStack Swift supports the name of a source or destination object with a URL.  

## Response Headers<a name="section30570743"></a>

The following table describes response header parameters:

<a name="table1908395917540"></a>
<table><thead align="left"><tr id="row3722364517540"><th class="cellrowborder" valign="top" width="26.810000000000002%" id="mcps1.1.4.1.1"><p id="p6232528617540"><a name="p6232528617540"></a><a name="p6232528617540"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="20.86%" id="mcps1.1.4.1.2"><p id="p1518337517540"><a name="p1518337517540"></a><a name="p1518337517540"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.33%" id="mcps1.1.4.1.3"><p id="p2189382417540"><a name="p2189382417540"></a><a name="p2189382417540"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2856931417540"><td class="cellrowborder" valign="top" width="26.810000000000002%" headers="mcps1.1.4.1.1 "><p id="p3241308417540"><a name="p3241308417540"></a><a name="p3241308417540"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.1.4.1.2 "><p id="p821416717540"><a name="p821416717540"></a><a name="p821416717540"></a>String</p>
<p id="p681864417540"><a name="p681864417540"></a><a name="p681864417540"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.4.1.3 "><p id="p1543931517540"><a name="p1543931517540"></a><a name="p1543931517540"></a>If the operation succeeds, this value is 0.</p>
<p id="p473611017540"><a name="p473611017540"></a><a name="p473611017540"></a>If the operation fails, this value is the length of the error text in the response body.</p>
</td>
</tr>
<tr id="row20759256539"><td class="cellrowborder" valign="top" width="26.810000000000002%" headers="mcps1.1.4.1.1 "><p id="p10759155115313"><a name="p10759155115313"></a><a name="p10759155115313"></a>Last-Modified</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.1.4.1.2 "><p id="p52071110135312"><a name="p52071110135312"></a><a name="p52071110135312"></a>String</p>
<p id="p172071310185315"><a name="p172071310185315"></a><a name="p172071310185315"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.4.1.3 "><p id="p167596511539"><a name="p167596511539"></a><a name="p167596511539"></a>Date and time that the object was created or the last time that the metadata was changed.</p>
</td>
</tr>
<tr id="row658857581762"><td class="cellrowborder" valign="top" width="26.810000000000002%" headers="mcps1.1.4.1.1 "><p id="p561009131762"><a name="p561009131762"></a><a name="p561009131762"></a>X-Copied-From-Last-Modified</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.1.4.1.2 "><p id="p4782068117615"><a name="p4782068117615"></a><a name="p4782068117615"></a>String</p>
<p id="p2773294617615"><a name="p2773294617615"></a><a name="p2773294617615"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.4.1.3 "><p id="p530853601762"><a name="p530853601762"></a><a name="p530853601762"></a>For a copied object, it shows the last modified date and time.</p>
</td>
</tr>
<tr id="row1864933617944"><td class="cellrowborder" valign="top" width="26.810000000000002%" headers="mcps1.1.4.1.1 "><p id="p3362630417944"><a name="p3362630417944"></a><a name="p3362630417944"></a>X-Copied-From</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.1.4.1.2 "><p id="p6418171017954"><a name="p6418171017954"></a><a name="p6418171017954"></a>String</p>
<p id="p4076448517954"><a name="p4076448517954"></a><a name="p4076448517954"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.4.1.3 "><p id="p3535032917944"><a name="p3535032917944"></a><a name="p3535032917944"></a>For a copied object, it shows the container name and object name in the form of <strong id="b14382484815358"><a name="b14382484815358"></a><a name="b14382484815358"></a>{container}/{object}</strong>.</p>
</td>
</tr>
<tr id="row597919561508"><td class="cellrowborder" valign="top" width="26.810000000000002%" headers="mcps1.1.4.1.1 "><p id="p14980135625015"><a name="p14980135625015"></a><a name="p14980135625015"></a>X-Copied-From-Account</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.1.4.1.2 "><p id="p126136152511"><a name="p126136152511"></a><a name="p126136152511"></a>String</p>
<p id="p126141615105117"><a name="p126141615105117"></a><a name="p126141615105117"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.4.1.3 "><p id="p6980056185018"><a name="p6980056185018"></a><a name="p6980056185018"></a>Account ID of the user who owns the object to be copied.</p>
</td>
</tr>
<tr id="row4262499817540"><td class="cellrowborder" valign="top" width="26.810000000000002%" headers="mcps1.1.4.1.1 "><p id="p3007282217540"><a name="p3007282217540"></a><a name="p3007282217540"></a>Etag</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.1.4.1.2 "><p id="p1997949817540"><a name="p1997949817540"></a><a name="p1997949817540"></a>String</p>
<p id="p4559775717540"><a name="p4559775717540"></a><a name="p4559775717540"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.4.1.3 "><p id="p243085117540"><a name="p243085117540"></a><a name="p243085117540"></a>For ordinary objects, this value is the MD5 checksum of the uploaded object content.</p>
<p id="p2187766417540"><a name="p2187766417540"></a><a name="p2187766417540"></a>For static large objects, this value is the MD5 checksum of the concatenated string of MD5 checksums for each of the segments.</p>
<p id="p6268124917540"><a name="p6268124917540"></a><a name="p6268124917540"></a>For dynamic large objects, the value is the MD5 checksum of the manifest file.</p>
</td>
</tr>
<tr id="row1506052417122"><td class="cellrowborder" valign="top" width="26.810000000000002%" headers="mcps1.1.4.1.1 "><p id="p132699117122"><a name="p132699117122"></a><a name="p132699117122"></a>X-Object-Meta-name</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.1.4.1.2 "><p id="p37441973171216"><a name="p37441973171216"></a><a name="p37441973171216"></a>String</p>
<p id="p1433437171216"><a name="p1433437171216"></a><a name="p1433437171216"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.4.1.3 "><p id="p55468529171320"><a name="p55468529171320"></a><a name="p55468529171320"></a>The custom object metadata item.</p>
<p id="p4934983817122"><a name="p4934983817122"></a><a name="p4934983817122"></a><strong id="b50884809"><a name="b50884809"></a><a name="b50884809"></a>{name}</strong> is the name of the metadata item.</p>
</td>
</tr>
<tr id="row2726033717540"><td class="cellrowborder" valign="top" width="26.810000000000002%" headers="mcps1.1.4.1.1 "><p id="p6060372017540"><a name="p6060372017540"></a><a name="p6060372017540"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.1.4.1.2 "><p id="p995425017540"><a name="p995425017540"></a><a name="p995425017540"></a>String</p>
<p id="p2247939217540"><a name="p2247939217540"></a><a name="p2247939217540"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.4.1.3 "><p id="p889144017540"><a name="p889144017540"></a><a name="p889144017540"></a>MIME type of the object.</p>
</td>
</tr>
<tr id="row1291410117540"><td class="cellrowborder" valign="top" width="26.810000000000002%" headers="mcps1.1.4.1.1 "><p id="p3940926117540"><a name="p3940926117540"></a><a name="p3940926117540"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.1.4.1.2 "><p id="p3803358617540"><a name="p3803358617540"></a><a name="p3803358617540"></a>String</p>
<p id="p675795617540"><a name="p675795617540"></a><a name="p675795617540"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.4.1.3 "><p id="p1052359117540"><a name="p1052359117540"></a><a name="p1052359117540"></a>Transaction date and time.</p>
</td>
</tr>
<tr id="row2760345717540"><td class="cellrowborder" valign="top" width="26.810000000000002%" headers="mcps1.1.4.1.1 "><p id="p2128751517540"><a name="p2128751517540"></a><a name="p2128751517540"></a>X-Trans-Id</p>
</td>
<td class="cellrowborder" valign="top" width="20.86%" headers="mcps1.1.4.1.2 "><p id="p4656713717540"><a name="p4656713717540"></a><a name="p4656713717540"></a>Uuid</p>
<p id="p1645105717540"><a name="p1645105717540"></a><a name="p1645105717540"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="52.33%" headers="mcps1.1.4.1.3 "><p id="p5746723717540"><a name="p5746723717540"></a><a name="p5746723717540"></a>Unique transaction identifier.</p>
<p id="p4744309217540"><a name="p4744309217540"></a><a name="p4744309217540"></a></p>
</td>
</tr>
</tbody>
</table>

## Use COPY Command to Copy Object<a name="section2201390"></a>

Use the COPY command to copy an object. The source object is  **janeausten/goodby**  and the destination object is  **marketwain/goodbye**.

```
curl -i http://172.28.54.12:80/v1/AUTH_4b34aa268d8c45879cf4da16443d3f95/marketwain/goodbye -H "X-Auth-Token:74565091b56b4783818430cecb283e7f"  -XCOPY -H "Destination:janeausten/goodbye"
```

```
HTTP/1.1 201 Created
X-Trans-Id: tx000001513c9e87a1370c0-144543b5de
Content-Type: text/html;charset=UTF-8
Date: Wed, 25 Nov 2015 03:10:01 GMT
ETag: e85f5c28b588fa64a379ba876e3591d2
Last-Modified: Wed, 25 Nov 2015 03:10:01 GMT
X-Copied-From: marketwain/goodbye
X-Copied-From-Account: AUTH_4b34aa268d8c45879cf4da16443d3f95
X-Copied-From-Last-Modified: Wed, 25 Nov 2015 03:04:55 GMT
Content-Length: 0
```

## Use PUT Command to Copy Object<a name="section60098234144536"></a>

Use the PUT command to copy an object. The source object is  **janeausten/goodby**  and the destination object is  **marketwain/goodbye**.

```
curl -i http://172.28.54.12:80/v1/AUTH_4b34aa268d8c45879cf4da16443d3f95/janeausten/goodbye -H "X-Auth-Token:74565091b56b4783818430cecb283e7f" -H "X-Copy-from:/marketwain/goodbye" -XPUT -H "Content-Length:0"
```

```
HTTP/1.1 201 Created
X-Trans-Id: tx000001513ca34816370c1-16ea772e65
Content-Type: text/html;charset=UTF-8
Date: Wed, 25 Nov 2015 03:15:12 GMT
ETag: e85f5c28b588fa64a379ba876e3591d2
Last-Modified: Wed, 25 Nov 2015 03:15:12 GMT
X-Copied-From: marketwain/goodbye
X-Copied-From-Account: AUTH_4b34aa268d8c45879cf4da16443d3f95
X-Copied-From-Last-Modified: Wed, 25 Nov 2015 03:04:55 GMT
Content-Length: 0
```

