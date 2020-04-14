# IAM Policy<a name="EN-US_TOPIC_0125560389"></a>

An administrator account can configure permission policies for user groups in IAM.  [Table 1](#table19525872143042)  lists the default permission policies.

On the console homepage, select  **Identity and Access Management**, and click  **User Groups**  in the navigation pane on the left. Locate the user group that you want to authorize permissions. Click  **Modify**  under the  **Operation**  column. In the  **User Group Permissions**  area, find the  **OBS \(S3\)**  project and click  **Modify**  to authorize permissions to the user group.

**Table  1**  Default IAM policies

<a name="table19525872143042"></a>
<table><thead align="left"><tr id="row52940627143042"><th class="cellrowborder" valign="top" width="24.08%" id="mcps1.2.3.1.1"><p id="p454423162614"><a name="p454423162614"></a><a name="p454423162614"></a>Policy</p>
</th>
<th class="cellrowborder" valign="top" width="75.92%" id="mcps1.2.3.1.2"><p id="p554122352617"><a name="p554122352617"></a><a name="p554122352617"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19477932143042"><td class="cellrowborder" valign="top" width="24.08%" headers="mcps1.2.3.1.1 "><p id="p144411465223"><a name="p144411465223"></a><a name="p144411465223"></a>Tenant Administrator</p>
</td>
<td class="cellrowborder" valign="top" width="75.92%" headers="mcps1.2.3.1.2 "><p id="p8441206192213"><a name="p8441206192213"></a><a name="p8441206192213"></a>Users with this permission can perform any operation on OBS resources.</p>
</td>
</tr>
<tr id="row40737992143042"><td class="cellrowborder" valign="top" width="24.08%" headers="mcps1.2.3.1.1 "><p id="p1244120682210"><a name="p1244120682210"></a><a name="p1244120682210"></a>Tenant Guest</p>
</td>
<td class="cellrowborder" valign="top" width="75.92%" headers="mcps1.2.3.1.2 "><p id="p244186102220"><a name="p244186102220"></a><a name="p244186102220"></a>Users with this permission can query the usage of OBS resources, in other words, this is the read permission to OBS resources.</p>
</td>
</tr>
<tr id="row51969103296"><td class="cellrowborder" valign="top" width="24.08%" headers="mcps1.2.3.1.1 "><p id="p6441146162212"><a name="p6441146162212"></a><a name="p6441146162212"></a>OBS Buckets Viewer</p>
</td>
<td class="cellrowborder" valign="top" width="75.92%" headers="mcps1.2.3.1.2 "><p id="p444136102211"><a name="p444136102211"></a><a name="p444136102211"></a>A user with this permission can list buckets, obtain basic bucket information, obtain bucket metadata, and list objects.</p>
</td>
</tr>
</tbody>
</table>

[Table 2](#table129395482338)  lists the operations that can be performed on OBS resources after a user has the required permissions.

**Table  2**  Permissions and the allowed operations on OBS resources

<a name="table129395482338"></a>
<table><thead align="left"><tr id="row6220124963316"><th class="cellrowborder" valign="top" width="22.45%" id="mcps1.2.5.1.1"><p id="p1220049133315"><a name="p1220049133315"></a><a name="p1220049133315"></a><strong id="b148525115319"><a name="b148525115319"></a><a name="b148525115319"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.55%" id="mcps1.2.5.1.2"><p id="p15220204913314"><a name="p15220204913314"></a><a name="p15220204913314"></a><strong id="b151312578317"><a name="b151312578317"></a><a name="b151312578317"></a>Tenant Administrator Permission</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.5.1.3"><p id="p1822044933312"><a name="p1822044933312"></a><a name="p1822044933312"></a><strong id="b10746542043"><a name="b10746542043"></a><a name="b10746542043"></a>Tenant Guest Permission</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.5.1.4"><p id="p162201849143315"><a name="p162201849143315"></a><a name="p162201849143315"></a><strong id="b991416262151"><a name="b991416262151"></a><a name="b991416262151"></a>OBS Buckets Viewer Permission</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row222194923314"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p11221164933319"><a name="p11221164933319"></a><a name="p11221164933319"></a>Listing buckets</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p19221104933317"><a name="p19221104933317"></a><a name="p19221104933317"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p4221194910334"><a name="p4221194910334"></a><a name="p4221194910334"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p822104963316"><a name="p822104963316"></a><a name="p822104963316"></a>Yes</p>
</td>
</tr>
<tr id="row4221114917335"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p16221104933319"><a name="p16221104933319"></a><a name="p16221104933319"></a>Creating buckets</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p1922110491332"><a name="p1922110491332"></a><a name="p1922110491332"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p17221549163313"><a name="p17221549163313"></a><a name="p17221549163313"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p3222114973313"><a name="p3222114973313"></a><a name="p3222114973313"></a>No</p>
</td>
</tr>
<tr id="row62221949103314"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p92223494338"><a name="p92223494338"></a><a name="p92223494338"></a>Deleting buckets</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p82223491336"><a name="p82223491336"></a><a name="p82223491336"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p122213490335"><a name="p122213490335"></a><a name="p122213490335"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p722234911330"><a name="p722234911330"></a><a name="p722234911330"></a>No</p>
</td>
</tr>
<tr id="row13222194917331"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p19222149153317"><a name="p19222149153317"></a><a name="p19222149153317"></a>Obtaining basic bucket information</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p4222134919339"><a name="p4222134919339"></a><a name="p4222134919339"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p15222449103317"><a name="p15222449103317"></a><a name="p15222449103317"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p1522254993314"><a name="p1522254993314"></a><a name="p1522254993314"></a>Yes</p>
<div class="note" id="note12984151716450"><a name="note12984151716450"></a><a name="note12984151716450"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p17651727124514"><a name="p17651727124514"></a><a name="p17651727124514"></a>The statistics of used storage space and number of objects cannot be obtained.</p>
</div></div>
</td>
</tr>
<tr id="row62221249173316"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p8222164915339"><a name="p8222164915339"></a><a name="p8222164915339"></a>Bucket access control</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p82238496331"><a name="p82238496331"></a><a name="p82238496331"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p15223144963317"><a name="p15223144963317"></a><a name="p15223144963317"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p122239496333"><a name="p122239496333"></a><a name="p122239496333"></a>No</p>
</td>
</tr>
<tr id="row20573135993312"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p1957418596331"><a name="p1957418596331"></a><a name="p1957418596331"></a>Bucket policies</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p757425953310"><a name="p757425953310"></a><a name="p757425953310"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p32515244348"><a name="p32515244348"></a><a name="p32515244348"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p152614245344"><a name="p152614245344"></a><a name="p152614245344"></a>No</p>
</td>
</tr>
<tr id="row20223144917334"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p1322313498336"><a name="p1322313498336"></a><a name="p1322313498336"></a>Modifying bucket storage classes</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p102233494338"><a name="p102233494338"></a><a name="p102233494338"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p12231249113318"><a name="p12231249113318"></a><a name="p12231249113318"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p0223154943311"><a name="p0223154943311"></a><a name="p0223154943311"></a>No</p>
</td>
</tr>
<tr id="row1322317491333"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p1022312491333"><a name="p1022312491333"></a><a name="p1022312491333"></a>Listing objects</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p10223124943319"><a name="p10223124943319"></a><a name="p10223124943319"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p1622424912339"><a name="p1622424912339"></a><a name="p1622424912339"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p1522494913333"><a name="p1522494913333"></a><a name="p1522494913333"></a>Yes</p>
</td>
</tr>
<tr id="row119091435114514"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p16910335164511"><a name="p16910335164511"></a><a name="p16910335164511"></a>Listing objects with multiple versions</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p12910735124513"><a name="p12910735124513"></a><a name="p12910735124513"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p1191073517451"><a name="p1191073517451"></a><a name="p1191073517451"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p109106352455"><a name="p109106352455"></a><a name="p109106352455"></a>No</p>
</td>
</tr>
<tr id="row82241349103313"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p162241049203320"><a name="p162241049203320"></a><a name="p162241049203320"></a>Uploading files</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p17224154918332"><a name="p17224154918332"></a><a name="p17224154918332"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p1222417498333"><a name="p1222417498333"></a><a name="p1222417498333"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p922464963311"><a name="p922464963311"></a><a name="p922464963311"></a>No</p>
</td>
</tr>
<tr id="row3224164913310"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p1224134914333"><a name="p1224134914333"></a><a name="p1224134914333"></a>Creating folders</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p3224104983319"><a name="p3224104983319"></a><a name="p3224104983319"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p7224114953311"><a name="p7224114953311"></a><a name="p7224114953311"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p7224124913320"><a name="p7224124913320"></a><a name="p7224124913320"></a>No</p>
</td>
</tr>
<tr id="row5224149183317"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p1122404953315"><a name="p1122404953315"></a><a name="p1122404953315"></a>Deleting files</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p10224124915337"><a name="p10224124915337"></a><a name="p10224124915337"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p822674918332"><a name="p822674918332"></a><a name="p822674918332"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p2022614497333"><a name="p2022614497333"></a><a name="p2022614497333"></a>No</p>
</td>
</tr>
<tr id="row1722694993311"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p12226134919334"><a name="p12226134919334"></a><a name="p12226134919334"></a>Deleting folders</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p1822611498331"><a name="p1822611498331"></a><a name="p1822611498331"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p82261949193311"><a name="p82261949193311"></a><a name="p82261949193311"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p522624983314"><a name="p522624983314"></a><a name="p522624983314"></a>No</p>
</td>
</tr>
<tr id="row722674919335"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p72266498333"><a name="p72266498333"></a><a name="p72266498333"></a>Downloading files</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p18226124963312"><a name="p18226124963312"></a><a name="p18226124963312"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p20226104918339"><a name="p20226104918339"></a><a name="p20226104918339"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p14226134917339"><a name="p14226134917339"></a><a name="p14226134917339"></a>No</p>
</td>
</tr>
<tr id="row36561642193515"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p7656204212355"><a name="p7656204212355"></a><a name="p7656204212355"></a>Deleting files with multiple versions</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p206952197369"><a name="p206952197369"></a><a name="p206952197369"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p06995198362"><a name="p06995198362"></a><a name="p06995198362"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p10702201903614"><a name="p10702201903614"></a><a name="p10702201903614"></a>No</p>
</td>
</tr>
<tr id="row935422143615"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p835922163620"><a name="p835922163620"></a><a name="p835922163620"></a>Downloading files with multiple versions</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p123993370364"><a name="p123993370364"></a><a name="p123993370364"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p11611522757"><a name="p11611522757"></a><a name="p11611522757"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p1140310379367"><a name="p1140310379367"></a><a name="p1140310379367"></a>No</p>
</td>
</tr>
<tr id="row1022604933312"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p82261849133313"><a name="p82261849133313"></a><a name="p82261849133313"></a>Modifying object storage classes</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p72264494339"><a name="p72264494339"></a><a name="p72264494339"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p82261249183310"><a name="p82261249183310"></a><a name="p82261249183310"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p192261149143313"><a name="p192261149143313"></a><a name="p192261149143313"></a>No</p>
</td>
</tr>
<tr id="row1422664914335"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p1022604912335"><a name="p1022604912335"></a><a name="p1022604912335"></a>Restoring files</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p422624919334"><a name="p422624919334"></a><a name="p422624919334"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p822644914331"><a name="p822644914331"></a><a name="p822644914331"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p17226154933313"><a name="p17226154933313"></a><a name="p17226154933313"></a>No</p>
</td>
</tr>
<tr id="row132274497334"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p152271449123314"><a name="p152271449123314"></a><a name="p152271449123314"></a>Canceling the deletion of files</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p1822764910333"><a name="p1822764910333"></a><a name="p1822764910333"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p022704983317"><a name="p022704983317"></a><a name="p022704983317"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p422784914331"><a name="p422784914331"></a><a name="p422784914331"></a>No</p>
</td>
</tr>
<tr id="row17227204923316"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p132271949103313"><a name="p132271949103313"></a><a name="p132271949103313"></a>Deleting fragments</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p12227184915334"><a name="p12227184915334"></a><a name="p12227184915334"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p15227144973315"><a name="p15227144973315"></a><a name="p15227144973315"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p172272491335"><a name="p172272491335"></a><a name="p172272491335"></a>No</p>
</td>
</tr>
<tr id="row422744915332"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p5227134920336"><a name="p5227134920336"></a><a name="p5227134920336"></a>Object access control</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p122274498336"><a name="p122274498336"></a><a name="p122274498336"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p1722713490338"><a name="p1722713490338"></a><a name="p1722713490338"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p142278496331"><a name="p142278496331"></a><a name="p142278496331"></a>No</p>
</td>
</tr>
<tr id="row122814993316"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p12228249173319"><a name="p12228249173319"></a><a name="p12228249173319"></a>Configuring object metadata</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p102281249163313"><a name="p102281249163313"></a><a name="p102281249163313"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p1222854914337"><a name="p1222854914337"></a><a name="p1222854914337"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p622814903313"><a name="p622814903313"></a><a name="p622814903313"></a>No</p>
</td>
</tr>
<tr id="row13228149103315"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p1322810491337"><a name="p1322810491337"></a><a name="p1322810491337"></a>Managing versioning</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p18228194917333"><a name="p18228194917333"></a><a name="p18228194917333"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p12281349143318"><a name="p12281349143318"></a><a name="p12281349143318"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p522864903310"><a name="p522864903310"></a><a name="p522864903310"></a>No</p>
</td>
</tr>
<tr id="row02281749183318"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p92288490331"><a name="p92288490331"></a><a name="p92288490331"></a>Managing logging</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p15228249163320"><a name="p15228249163320"></a><a name="p15228249163320"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p10228549183318"><a name="p10228549183318"></a><a name="p10228549183318"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p13228194983313"><a name="p13228194983313"></a><a name="p13228194983313"></a>No</p>
</td>
</tr>
<tr id="row1722810499332"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p6228749133313"><a name="p6228749133313"></a><a name="p6228749133313"></a>Managing event notifications</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p20228194963318"><a name="p20228194963318"></a><a name="p20228194963318"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p9228204963318"><a name="p9228204963318"></a><a name="p9228204963318"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p152281149163314"><a name="p152281149163314"></a><a name="p152281149163314"></a>No</p>
</td>
</tr>
<tr id="row182282049183311"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p72301149113311"><a name="p72301149113311"></a><a name="p72301149113311"></a>Managing tags</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p1323016491339"><a name="p1323016491339"></a><a name="p1323016491339"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p1223034993314"><a name="p1223034993314"></a><a name="p1223034993314"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p5230549183313"><a name="p5230549183313"></a><a name="p5230549183313"></a>No</p>
</td>
</tr>
<tr id="row10230154910330"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p5230134953312"><a name="p5230134953312"></a><a name="p5230134953312"></a>Managing lifecycle rules</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p20230174953312"><a name="p20230174953312"></a><a name="p20230174953312"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p5230449113316"><a name="p5230449113316"></a><a name="p5230449113316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p12230124920337"><a name="p12230124920337"></a><a name="p12230124920337"></a>No</p>
</td>
</tr>
<tr id="row1623013494337"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p1823054919336"><a name="p1823054919336"></a><a name="p1823054919336"></a>Managing static website hosting</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p192307496331"><a name="p192307496331"></a><a name="p192307496331"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p15230144943313"><a name="p15230144943313"></a><a name="p15230144943313"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p62309496336"><a name="p62309496336"></a><a name="p62309496336"></a>No</p>
</td>
</tr>
<tr id="row67541923203711"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p46041028203714"><a name="p46041028203714"></a><a name="p46041028203714"></a>Managing CORS rules</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p15689203663720"><a name="p15689203663720"></a><a name="p15689203663720"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p136928361375"><a name="p136928361375"></a><a name="p136928361375"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p36947369371"><a name="p36947369371"></a><a name="p36947369371"></a>No</p>
</td>
</tr>
<tr id="row384417262372"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.5.1.1 "><p id="p160412863720"><a name="p160412863720"></a><a name="p160412863720"></a>Managing URL validation</p>
</td>
<td class="cellrowborder" valign="top" width="27.55%" headers="mcps1.2.5.1.2 "><p id="p15375133714373"><a name="p15375133714373"></a><a name="p15375133714373"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p237733717373"><a name="p237733717373"></a><a name="p237733717373"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p14379123715376"><a name="p14379123715376"></a><a name="p14379123715376"></a>No</p>
</td>
</tr>
</tbody>
</table>

