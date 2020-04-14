# Querying Cluster Details<a name="css_03_0026"></a>

## Function<a name="section31951730334"></a>

This API is used to query and display details about a cluster.

## URI<a name="section111957301639"></a>

```
GET /v1.0/{project_id}/clusters/{cluster_id}
```

**Table  1**  Parameter description

<a name="table721120301031"></a>
<table><thead align="left"><tr id="row439920301735"><th class="cellrowborder" valign="top" width="25.77%" id="mcps1.2.5.1.1"><p id="p18399103015317"><a name="p18399103015317"></a><a name="p18399103015317"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.740000000000002%" id="mcps1.2.5.1.2"><p id="p7399143017310"><a name="p7399143017310"></a><a name="p7399143017310"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.56%" id="mcps1.2.5.1.3"><p id="p1139910301639"><a name="p1139910301639"></a><a name="p1139910301639"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.5.1.4"><p id="p6399143019310"><a name="p6399143019310"></a><a name="p6399143019310"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1339913301636"><td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.1 "><p id="p1539993015315"><a name="p1539993015315"></a><a name="p1539993015315"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.2.5.1.2 "><p id="p1239911301737"><a name="p1239911301737"></a><a name="p1239911301737"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.2.5.1.3 "><p id="p193991630734"><a name="p193991630734"></a><a name="p193991630734"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.4 "><p id="p039918302317"><a name="p039918302317"></a><a name="p039918302317"></a>Project ID.</p>
</td>
</tr>
<tr id="row143991230731"><td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.1 "><p id="p1139918307319"><a name="p1139918307319"></a><a name="p1139918307319"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.2.5.1.2 "><p id="p33998308318"><a name="p33998308318"></a><a name="p33998308318"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.2.5.1.3 "><p id="p153994301318"><a name="p153994301318"></a><a name="p153994301318"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.4 "><p id="p539911301733"><a name="p539911301733"></a><a name="p539911301733"></a>ID of the cluster to be queried.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section142271830233"></a>

None

## Response<a name="section72271330831"></a>

[Table 2](#table372832271213)  describes the response parameters.

**Table  2**  Parameter description

<a name="table372832271213"></a>
<table><thead align="left"><tr id="row172822201216"><th class="cellrowborder" valign="top" width="16.333333333333336%" id="mcps1.2.4.1.1"><p id="p102799549123"><a name="p102799549123"></a><a name="p102799549123"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.070707070707073%" id="mcps1.2.4.1.2"><p id="p1927965418126"><a name="p1927965418126"></a><a name="p1927965418126"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="59.59595959595959%" id="mcps1.2.4.1.3"><p id="p8279254121216"><a name="p8279254121216"></a><a name="p8279254121216"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1728172231215"><td class="cellrowborder" valign="top" width="16.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1027935418122"><a name="p1027935418122"></a><a name="p1027935418122"></a>datastore</p>
</td>
<td class="cellrowborder" valign="top" width="24.070707070707073%" headers="mcps1.2.4.1.2 "><p id="p1527915415128"><a name="p1527915415128"></a><a name="p1527915415128"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p027905411219"><a name="p027905411219"></a><a name="p027905411219"></a>Type of the data search engine. For details, see <a href="#table1060833515712">Table 3</a>.</p>
</td>
</tr>
<tr id="row1172862211210"><td class="cellrowborder" valign="top" width="16.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p18279754161220"><a name="p18279754161220"></a><a name="p18279754161220"></a>instances</p>
</td>
<td class="cellrowborder" valign="top" width="24.070707070707073%" headers="mcps1.2.4.1.2 "><p id="p16279105461215"><a name="p16279105461215"></a><a name="p16279105461215"></a>Array of instance objects</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p02791054121213"><a name="p02791054121213"></a><a name="p02791054121213"></a>List of node objects. For details, see <a href="#table6945141813">Table 4</a>.</p>
</td>
</tr>
<tr id="row187284223121"><td class="cellrowborder" valign="top" width="16.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p10279115419121"><a name="p10279115419121"></a><a name="p10279115419121"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="24.070707070707073%" headers="mcps1.2.4.1.2 "><p id="p4279145481214"><a name="p4279145481214"></a><a name="p4279145481214"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p227915411211"><a name="p227915411211"></a><a name="p227915411211"></a>Last modification time of a cluster. The format is <strong id="b44132588322"><a name="b44132588322"></a><a name="b44132588322"></a>ISO8601: CCYY-MM-DDThh:mm:ss</strong>.</p>
</td>
</tr>
<tr id="row18728132241214"><td class="cellrowborder" valign="top" width="16.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1427916545123"><a name="p1427916545123"></a><a name="p1427916545123"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="24.070707070707073%" headers="mcps1.2.4.1.2 "><p id="p8279145431210"><a name="p8279145431210"></a><a name="p8279145431210"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p8279454101215"><a name="p8279454101215"></a><a name="p8279454101215"></a>Cluster name.</p>
</td>
</tr>
<tr id="row2728192231218"><td class="cellrowborder" valign="top" width="16.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p22791654121214"><a name="p22791654121214"></a><a name="p22791654121214"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="24.070707070707073%" headers="mcps1.2.4.1.2 "><p id="p12279154121213"><a name="p12279154121213"></a><a name="p12279154121213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p13279154111211"><a name="p13279154111211"></a><a name="p13279154111211"></a>Time when a cluster is created. The format is <strong id="b11101013311"><a name="b11101013311"></a><a name="b11101013311"></a>ISO8601: CCYY-MM-DDThh:mm:ss</strong>.</p>
</td>
</tr>
<tr id="row772812225127"><td class="cellrowborder" valign="top" width="16.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p727955491216"><a name="p727955491216"></a><a name="p727955491216"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="24.070707070707073%" headers="mcps1.2.4.1.2 "><p id="p82792054181216"><a name="p82792054181216"></a><a name="p82792054181216"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p527985417129"><a name="p527985417129"></a><a name="p527985417129"></a>Cluster ID.</p>
</td>
</tr>
<tr id="row16728152271215"><td class="cellrowborder" valign="top" width="16.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1927985410124"><a name="p1927985410124"></a><a name="p1927985410124"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="24.070707070707073%" headers="mcps1.2.4.1.2 "><p id="p1927955401216"><a name="p1927955401216"></a><a name="p1927955401216"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p02795545129"><a name="p02795545129"></a><a name="p02795545129"></a>Return value.</p>
<a name="ul72793548129"></a><a name="ul72793548129"></a><ul id="ul72793548129"><li><strong id="b842352706152659"><a name="b842352706152659"></a><a name="b842352706152659"></a>100</strong>: The operation, such as instance creation, is in progress.</li><li><strong id="b842352706103933"><a name="b842352706103933"></a><a name="b842352706103933"></a>200</strong>: The cluster is available.</li><li><strong id="b842352706103945"><a name="b842352706103945"></a><a name="b842352706103945"></a>303</strong>: The cluster is unavailable.</li></ul>
</td>
</tr>
<tr id="row151501130181220"><td class="cellrowborder" valign="top" width="16.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p202791654161213"><a name="p202791654161213"></a><a name="p202791654161213"></a>endpoint</p>
</td>
<td class="cellrowborder" valign="top" width="24.070707070707073%" headers="mcps1.2.4.1.2 "><p id="p427919549123"><a name="p427919549123"></a><a name="p427919549123"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p16279155415123"><a name="p16279155415123"></a><a name="p16279155415123"></a>Indicates the IP address and port number of the user used to access the VPC.</p>
</td>
</tr>
<tr id="row274411333129"><td class="cellrowborder" valign="top" width="16.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p32791054151216"><a name="p32791054151216"></a><a name="p32791054151216"></a>actionProgress</p>
</td>
<td class="cellrowborder" valign="top" width="24.070707070707073%" headers="mcps1.2.4.1.2 "><p id="p727914545121"><a name="p727914545121"></a><a name="p727914545121"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p72796543128"><a name="p72796543128"></a><a name="p72796543128"></a>Cluster operation progress, which indicates the progress of cluster creation and expansion in percentage.</p>
</td>
</tr>
<tr id="row852519374124"><td class="cellrowborder" valign="top" width="16.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p18279185413120"><a name="p18279185413120"></a><a name="p18279185413120"></a>actions</p>
</td>
<td class="cellrowborder" valign="top" width="24.070707070707073%" headers="mcps1.2.4.1.2 "><p id="p827905481211"><a name="p827905481211"></a><a name="p827905481211"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p7481181175918"><a name="p7481181175918"></a><a name="p7481181175918"></a>Current behavior on a cluster. Value <strong id="b4252206554"><a name="b4252206554"></a><a name="b4252206554"></a>REBOOTING</strong> indicates that the cluster is being restarted, <strong id="b1826320115510"><a name="b1826320115510"></a><a name="b1826320115510"></a>GROWING</strong> indicates that capacity expansion is being performed on the cluster, <strong id="b162612203557"><a name="b162612203557"></a><a name="b162612203557"></a>RESTORING</strong> indicates that the cluster is being restored, and <strong id="b17271520185511"><a name="b17271520185511"></a><a name="b17271520185511"></a>SNAPSHOTTING</strong> indicates that the snapshot is being created.</p>
</td>
</tr>
<tr id="row165951256111516"><td class="cellrowborder" valign="top" width="16.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p145956566157"><a name="p145956566157"></a><a name="p145956566157"></a>failed_reasons</p>
</td>
<td class="cellrowborder" valign="top" width="24.070707070707073%" headers="mcps1.2.4.1.2 "><p id="p11595656151513"><a name="p11595656151513"></a><a name="p11595656151513"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p35952056121518"><a name="p35952056121518"></a><a name="p35952056121518"></a>Failure cause. If the cluster is in the Available state, this parameter is not returned. For details, see <a href="#table57969612189">Table 5</a>.</p>
</td>
</tr>
<tr id="row65960327244"><td class="cellrowborder" valign="top" width="16.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p159683215247"><a name="p159683215247"></a><a name="p159683215247"></a>httpsEnable</p>
</td>
<td class="cellrowborder" valign="top" width="24.070707070707073%" headers="mcps1.2.4.1.2 "><p id="p259612323242"><a name="p259612323242"></a><a name="p259612323242"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p1059663272410"><a name="p1059663272410"></a><a name="p1059663272410"></a>Communication encryption status.</p>
<a name="ul10157125063914"></a><a name="ul10157125063914"></a><ul id="ul10157125063914"><li>Value <strong id="b5552192553419"><a name="b5552192553419"></a><a name="b5552192553419"></a>false</strong> indicates that communication encryption is not enabled.</li><li>Value <strong id="b1860542718347"><a name="b1860542718347"></a><a name="b1860542718347"></a>true</strong> indicates that communication encryption has been enabled.</li></ul>
</td>
</tr>
<tr id="row13734141262113"><td class="cellrowborder" valign="top" width="16.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p18734512202119"><a name="p18734512202119"></a><a name="p18734512202119"></a>diskEncrypted</p>
</td>
<td class="cellrowborder" valign="top" width="24.070707070707073%" headers="mcps1.2.4.1.2 "><p id="p18734141211217"><a name="p18734141211217"></a><a name="p18734141211217"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p5734111215212"><a name="p5734111215212"></a><a name="p5734111215212"></a>Whether disks are encrypted.</p>
<a name="ul197793115619"></a><a name="ul197793115619"></a><ul id="ul197793115619"><li>Value <strong id="b4529123813425"><a name="b4529123813425"></a><a name="b4529123813425"></a>true</strong> indicates that disks are encrypted.</li><li>Value <strong id="b1221263913429"><a name="b1221263913429"></a><a name="b1221263913429"></a>false</strong> indicates that disks are not encrypted.</li></ul>
</td>
</tr>
<tr id="row17352242317"><td class="cellrowborder" valign="top" width="16.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p127353218233"><a name="p127353218233"></a><a name="p127353218233"></a>cmkId</p>
</td>
<td class="cellrowborder" valign="top" width="24.070707070707073%" headers="mcps1.2.4.1.2 "><p id="p4735112122314"><a name="p4735112122314"></a><a name="p4735112122314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p1673517202311"><a name="p1673517202311"></a><a name="p1673517202311"></a>Key ID used for disk encryption.</p>
</td>
</tr>
<tr id="row19613203673517"><td class="cellrowborder" valign="top" width="16.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p7613113615359"><a name="p7613113615359"></a><a name="p7613113615359"></a>vpcId</p>
</td>
<td class="cellrowborder" valign="top" width="24.070707070707073%" headers="mcps1.2.4.1.2 "><p id="p19613436173520"><a name="p19613436173520"></a><a name="p19613436173520"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p86131936203512"><a name="p86131936203512"></a><a name="p86131936203512"></a>VPC ID.</p>
</td>
</tr>
<tr id="row3602724360"><td class="cellrowborder" valign="top" width="16.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p560272173611"><a name="p560272173611"></a><a name="p560272173611"></a>subnetId</p>
</td>
<td class="cellrowborder" valign="top" width="24.070707070707073%" headers="mcps1.2.4.1.2 "><p id="p156028233619"><a name="p156028233619"></a><a name="p156028233619"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p14602192143615"><a name="p14602192143615"></a><a name="p14602192143615"></a>Subnet ID.</p>
</td>
</tr>
<tr id="row73171419163619"><td class="cellrowborder" valign="top" width="16.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1431791914365"><a name="p1431791914365"></a><a name="p1431791914365"></a>securityGroupId</p>
</td>
<td class="cellrowborder" valign="top" width="24.070707070707073%" headers="mcps1.2.4.1.2 "><p id="p23171194363"><a name="p23171194363"></a><a name="p23171194363"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="59.59595959595959%" headers="mcps1.2.4.1.3 "><p id="p123171219203612"><a name="p123171219203612"></a><a name="p123171219203612"></a>Security group ID.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **datastore**  field data structure description

<a name="table1060833515712"></a>
<table><thead align="left"><tr id="row560820358713"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p84144301433"><a name="p84144301433"></a><a name="p84144301433"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.5%" id="mcps1.2.4.1.2"><p id="p18414930739"><a name="p18414930739"></a><a name="p18414930739"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.50000000000001%" id="mcps1.2.4.1.3"><p id="p341423015314"><a name="p341423015314"></a><a name="p341423015314"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row46081935873"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p841420301030"><a name="p841420301030"></a><a name="p841420301030"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="21.5%" headers="mcps1.2.4.1.2 "><p id="p1141416308313"><a name="p1141416308313"></a><a name="p1141416308313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.50000000000001%" headers="mcps1.2.4.1.3 "><p id="p154144301833"><a name="p154144301833"></a><a name="p154144301833"></a>Supported type: elasticsearch</p>
</td>
</tr>
<tr id="row2608103518711"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p1941493017319"><a name="p1941493017319"></a><a name="p1941493017319"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="21.5%" headers="mcps1.2.4.1.2 "><p id="p241412301836"><a name="p241412301836"></a><a name="p241412301836"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.50000000000001%" headers="mcps1.2.4.1.3 "><p id="p941413305319"><a name="p941413305319"></a><a name="p941413305319"></a>Engine version number. The current engine version is 6.2.3.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **instances**  field data structure description

<a name="table6945141813"></a>
<table><thead align="left"><tr id="row169419141184"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p34142301319"><a name="p34142301319"></a><a name="p34142301319"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.2"><p id="p541410301436"><a name="p541410301436"></a><a name="p541410301436"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52%" id="mcps1.2.4.1.3"><p id="p2414330339"><a name="p2414330339"></a><a name="p2414330339"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19944141083"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p4414203015312"><a name="p4414203015312"></a><a name="p4414203015312"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p841415303315"><a name="p841415303315"></a><a name="p841415303315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p144141030137"><a name="p144141030137"></a><a name="p144141030137"></a>Supported type: ess (indicating the Elasticsearch node)</p>
</td>
</tr>
<tr id="row6949141182"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p941410301316"><a name="p941410301316"></a><a name="p941410301316"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p841413308313"><a name="p841413308313"></a><a name="p841413308313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p1141410300312"><a name="p1141410300312"></a><a name="p1141410300312"></a>Instance ID.</p>
</td>
</tr>
<tr id="row13941214985"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p241412302032"><a name="p241412302032"></a><a name="p241412302032"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p2414230038"><a name="p2414230038"></a><a name="p2414230038"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p194142301934"><a name="p194142301934"></a><a name="p194142301934"></a>Instance name.</p>
</td>
</tr>
<tr id="row109417148815"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p1541416301036"><a name="p1541416301036"></a><a name="p1541416301036"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.2 "><p id="p34141330836"><a name="p34141330836"></a><a name="p34141330836"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p1241414301531"><a name="p1241414301531"></a><a name="p1241414301531"></a>Instance status.</p>
<a name="ul1641411301333"></a><a name="ul1641411301333"></a><ul id="ul1641411301333"><li><strong id="b283582344"><a name="b283582344"></a><a name="b283582344"></a>100</strong>: The operation, such as instance creation, is in progress.</li><li><strong id="b1583751011"><a name="b1583751011"></a><a name="b1583751011"></a>200</strong>: The instance is available.</li><li><strong id="b1620046781"><a name="b1620046781"></a><a name="b1620046781"></a>303</strong>: The instance is unavailable.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  5** **failed\_reasons**  field data structure description

<a name="table57969612189"></a>
<table><thead align="left"><tr id="row13802166151810"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p128041560187"><a name="p128041560187"></a><a name="p128041560187"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="p20806116101810"><a name="p20806116101810"></a><a name="p20806116101810"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44%" id="mcps1.2.4.1.3"><p id="p880720616185"><a name="p880720616185"></a><a name="p880720616185"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row108081469182"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p680916661820"><a name="p680916661820"></a><a name="p680916661820"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p1781046131813"><a name="p1781046131813"></a><a name="p1781046131813"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.3 "><p id="p13335142981118"><a name="p13335142981118"></a><a name="p13335142981118"></a>Error code.</p>
<a name="ul83351829161110"></a><a name="ul83351829161110"></a><ul id="ul83351829161110"><li>CSS.6000: indicates that a cluster fails to be created.</li><li>CSS.6001: indicates that capacity expansion of a cluster fails.</li><li>CSS.6002: indicates that a cluster fails to be restarted.</li><li>CSS.6004: indicates that a node fails to be created in a cluster.</li><li>CSS.6005: indicates that the service fails to be initialized.</li></ul>
</td>
</tr>
<tr id="row88153612185"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p681614661811"><a name="p681614661811"></a><a name="p681614661811"></a>error_msg</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p681756191816"><a name="p681756191816"></a><a name="p681756191816"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.3 "><p id="p65415487814"><a name="p65415487814"></a><a name="p65415487814"></a>Detailed error information.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section19991837172616"></a>

Example request

```
GET /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/5c77b71c-5b35-4f50-8984-76387e42451a
```

Example response

```
{
  "datastore": {
    "type": "elasticsearch",
    "version": "6.2.3"
  },
  "instances": [
    {
      "status": "200",
      "type": "ess",
      "id": "3c7fe582-a9f6-46fd-9d01-956bed4a8bbc",
      "name": "ES-1-16-test17-ess-esn-1-1"
    }
  ],
  "updated": "2018-01-16T08:37:18",
  "name": "ES-1-16-test17",
  "created": "2018-01-16T08:37:18",
  "id": "5c77b71c-5b35-4f50-8984-76387e42451a",
  "status": "200",
  "endpoint": "192.168.0.8:9200",
  "httpsEnable": false,
  "diskEncrypted" : true,
  "cmkId" : "42546bb1-8025-4ad1-868f-600729c341ae",
  "vpcId": "07761987-bb61-4bbf-9d14-a7e6b6909224",
  "subnetId": "675ae21c-cc1c-4fc5-9cb4-4c07fce79648",
  "securityGroupId": "e9e098c8-2116-4b92-823c-036f0f17360b",
  "actionProgress": {},
  "actions": []
}
```

## Status Code<a name="section87962546391"></a>

[Table 6](#table10194172917151)  describes the status code.

**Table  6**  Status code

<a name="table10194172917151"></a>
<table><thead align="left"><tr id="css_03_0018_row1972183521418"><th class="cellrowborder" valign="top" width="15.939999999999998%" id="mcps1.2.4.1.1"><p id="css_03_0018_p14560134151414"><a name="css_03_0018_p14560134151414"></a><a name="css_03_0018_p14560134151414"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="31.04%" id="mcps1.2.4.1.2"><p id="css_03_0018_p5563194141411"><a name="css_03_0018_p5563194141411"></a><a name="css_03_0018_p5563194141411"></a>Code</p>
</th>
<th class="cellrowborder" valign="top" width="53.02%" id="mcps1.2.4.1.3"><p id="css_03_0018_p256616411143"><a name="css_03_0018_p256616411143"></a><a name="css_03_0018_p256616411143"></a>Status Code Description</p>
</th>
</tr>
</thead>
<tbody><tr id="css_03_0018_row129720356144"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="css_03_0018_p1957004131410"><a name="css_03_0018_p1957004131410"></a><a name="css_03_0018_p1957004131410"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="css_03_0018_p165731141171419"><a name="css_03_0018_p165731141171419"></a><a name="css_03_0018_p165731141171419"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="css_03_0018_p65778413148"><a name="css_03_0018_p65778413148"></a><a name="css_03_0018_p65778413148"></a>Invalid request.</p>
<p id="css_03_0018_p1557974171415"><a name="css_03_0018_p1557974171415"></a><a name="css_03_0018_p1557974171415"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="css_03_0018_row8972103517147"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="css_03_0018_p75841441191410"><a name="css_03_0018_p75841441191410"></a><a name="css_03_0018_p75841441191410"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="css_03_0018_p258716416142"><a name="css_03_0018_p258716416142"></a><a name="css_03_0018_p258716416142"></a>NotFound</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="css_03_0018_p15589154118141"><a name="css_03_0018_p15589154118141"></a><a name="css_03_0018_p15589154118141"></a>The requested resource cannot be found.</p>
<p id="css_03_0018_p14590164151410"><a name="css_03_0018_p14590164151410"></a><a name="css_03_0018_p14590164151410"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="css_03_0018_row297223511416"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="css_03_0018_p13595164131416"><a name="css_03_0018_p13595164131416"></a><a name="css_03_0018_p13595164131416"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="css_03_0018_p9598741131416"><a name="css_03_0018_p9598741131416"></a><a name="css_03_0018_p9598741131416"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="css_03_0018_p659994115146"><a name="css_03_0018_p659994115146"></a><a name="css_03_0018_p659994115146"></a>The request is processed successfully.</p>
</td>
</tr>
</tbody>
</table>

