# API Overview<a name="obs_03_0003"></a>

REST APIs support standard HTTP headers and status codes. IAM is used to implement authentication for access security.

APIs provided by OBS \(compatible with OpenStack Swift\) comply with the REST specifications \(HTTP 1.1\). Based on REST APIs provided by OBS \(compatible with OpenStack Swift\), users can send standard HTTP requests to perform operations such as creating, querying, and deleting containers or objects. Users can use any tools that support REST requests to send requests to OBS \(compatible with OpenStack Swift\).

REST APIs provided by OBS \(compatible with OpenStack Swift\) are compatible with most OpenStack Swift APIs.  [Table 1](#table5871188311518)  describes the compatibility between REST APIs provided by OBS \(compatible with OpenStack Swift\) and OpenStack Swift APIs \(Version v1.0, Kilo\).

**Table  1**  Compatibility between REST APIs provided by OBS \(compatible with OpenStack Swift\) and OpenStack Swift APIs

<a name="table5871188311518"></a>
<table><thead align="left"><tr id="row6710120511518"><th class="cellrowborder" valign="top" width="22.73%" id="mcps1.2.5.1.1"><p id="p5423421611518"><a name="p5423421611518"></a><a name="p5423421611518"></a>OpenStack Swift API</p>
</th>
<th class="cellrowborder" valign="top" width="26.61%" id="mcps1.2.5.1.2"><p id="p3388143911518"><a name="p3388143911518"></a><a name="p3388143911518"></a>Function</p>
</th>
<th class="cellrowborder" valign="top" width="24.169999999999998%" id="mcps1.2.5.1.3"><p id="p4638294411518"><a name="p4638294411518"></a><a name="p4638294411518"></a>Whether Implemented by OBS (Compatible with OpenStack Swift)</p>
</th>
<th class="cellrowborder" valign="top" width="26.490000000000002%" id="mcps1.2.5.1.4"><p id="p5633825911518"><a name="p5633825911518"></a><a name="p5633825911518"></a>Difference</p>
</th>
</tr>
</thead>
<tbody><tr id="row1400745711518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p21468608161526"><a name="p21468608161526"></a><a name="p21468608161526"></a>GET Account</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p4702039611518"><a name="p4702039611518"></a><a name="p4702039611518"></a>Obtains account information and the container list.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p5415429811518"><a name="p5415429811518"></a><a name="p5415429811518"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p3375590611518"><a name="p3375590611518"></a><a name="p3375590611518"></a>None</p>
</td>
</tr>
<tr id="row4181487511518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p2782531811518"><a name="p2782531811518"></a><a name="p2782531811518"></a>POST Account</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p6659068711518"><a name="p6659068711518"></a><a name="p6659068711518"></a>Creates, updates, or deletes account metadata.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p136043111518"><a name="p136043111518"></a><a name="p136043111518"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p518329311518"><a name="p518329311518"></a><a name="p518329311518"></a>None</p>
</td>
</tr>
<tr id="row1118843111518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p1727103811518"><a name="p1727103811518"></a><a name="p1727103811518"></a>HEAD Account</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p8854419163345"><a name="p8854419163345"></a><a name="p8854419163345"></a>Obtains account metadata.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p4560338711518"><a name="p4560338711518"></a><a name="p4560338711518"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p2097167311518"><a name="p2097167311518"></a><a name="p2097167311518"></a>None</p>
</td>
</tr>
<tr id="row5453226111518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p5593365016357"><a name="p5593365016357"></a><a name="p5593365016357"></a>GET Container</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p48682831163536"><a name="p48682831163536"></a><a name="p48682831163536"></a>Obtains container information and the object list.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p3465068011518"><a name="p3465068011518"></a><a name="p3465068011518"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p6440883311518"><a name="p6440883311518"></a><a name="p6440883311518"></a>None</p>
</td>
</tr>
<tr id="row2351646311518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p405411611518"><a name="p405411611518"></a><a name="p405411611518"></a>PUT Container</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p3697512411518"><a name="p3697512411518"></a><a name="p3697512411518"></a>Creates a container.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p1237661511518"><a name="p1237661511518"></a><a name="p1237661511518"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p134221211518"><a name="p134221211518"></a><a name="p134221211518"></a>None</p>
</td>
</tr>
<tr id="row5503069311518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p3058191711518"><a name="p3058191711518"></a><a name="p3058191711518"></a>DELETE Container</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p281365111518"><a name="p281365111518"></a><a name="p281365111518"></a>Deletes an empty container.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p3212811211518"><a name="p3212811211518"></a><a name="p3212811211518"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p5183029911518"><a name="p5183029911518"></a><a name="p5183029911518"></a>None</p>
</td>
</tr>
<tr id="row4466749811518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p5835431711518"><a name="p5835431711518"></a><a name="p5835431711518"></a>POST Container</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p7873902164437"><a name="p7873902164437"></a><a name="p7873902164437"></a>Creates, updates, or deletes container metadata.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p1872490111518"><a name="p1872490111518"></a><a name="p1872490111518"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p250186411518"><a name="p250186411518"></a><a name="p250186411518"></a>None</p>
</td>
</tr>
<tr id="row3546758811518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p2834561511518"><a name="p2834561511518"></a><a name="p2834561511518"></a>HEAD Container</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p27267574164541"><a name="p27267574164541"></a><a name="p27267574164541"></a>Obtains container metadata.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p1454419011518"><a name="p1454419011518"></a><a name="p1454419011518"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p2115826011518"><a name="p2115826011518"></a><a name="p2115826011518"></a>None</p>
</td>
</tr>
<tr id="row53408695143552"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p10916210143552"><a name="p10916210143552"></a><a name="p10916210143552"></a>BULK DELETE Container</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p11797798143552"><a name="p11797798143552"></a><a name="p11797798143552"></a>Batch deletes containers.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p16097575143552"><a name="p16097575143552"></a><a name="p16097575143552"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p56776280145845"><a name="p56776280145845"></a><a name="p56776280145845"></a>In a response, the <strong id="b5432205"><a name="b5432205"></a><a name="b5432205"></a>Content-Type</strong> header contains charset information.</p>
</td>
</tr>
<tr id="row35926525143735"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p54903270143735"><a name="p54903270143735"></a><a name="p54903270143735"></a>POST Container Static WebSite</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p17979846143735"><a name="p17979846143735"></a><a name="p17979846143735"></a>Configures container static websites.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p49354822143831"><a name="p49354822143831"></a><a name="p49354822143831"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p18849175145845"><a name="p18849175145845"></a><a name="p18849175145845"></a>None</p>
</td>
</tr>
<tr id="row50251614143913"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p49611348143913"><a name="p49611348143913"></a><a name="p49611348143913"></a>POST Container Cross domain policy</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p59096251143913"><a name="p59096251143913"></a><a name="p59096251143913"></a>Configures container cross-domain access policies.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p22067018143913"><a name="p22067018143913"></a><a name="p22067018143913"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p61702725145845"><a name="p61702725145845"></a><a name="p61702725145845"></a>None</p>
</td>
</tr>
<tr id="row63095002145755"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p30984112145755"><a name="p30984112145755"></a><a name="p30984112145755"></a>POST container to container Synchronization</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p26685132145755"><a name="p26685132145755"></a><a name="p26685132145755"></a>Configures container synchronization.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p14012044145755"><a name="p14012044145755"></a><a name="p14012044145755"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p1742804515639"><a name="p1742804515639"></a><a name="p1742804515639"></a>This function is not supported.</p>
</td>
</tr>
<tr id="row123493812910"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p1335118802915"><a name="p1335118802915"></a><a name="p1335118802915"></a>POST Container Quota</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p20352138162920"><a name="p20352138162920"></a><a name="p20352138162920"></a>Configures the bucket quota.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p1235214817296"><a name="p1235214817296"></a><a name="p1235214817296"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p113522087298"><a name="p113522087298"></a><a name="p113522087298"></a>This function is not supported.</p>
</td>
</tr>
<tr id="row6218231111518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p3996393711518"><a name="p3996393711518"></a><a name="p3996393711518"></a>GET Object</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p340631011518"><a name="p340631011518"></a><a name="p340631011518"></a>Obtains an object's content and metadata.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p2175458911518"><a name="p2175458911518"></a><a name="p2175458911518"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p6224369511518"><a name="p6224369511518"></a><a name="p6224369511518"></a>None</p>
</td>
</tr>
<tr id="row6653180163918"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p2036669163918"><a name="p2036669163918"></a><a name="p2036669163918"></a>PUT Object</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p30752495163918"><a name="p30752495163918"></a><a name="p30752495163918"></a>Creates or replaces an object.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p7924153163918"><a name="p7924153163918"></a><a name="p7924153163918"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p37876676163918"><a name="p37876676163918"></a><a name="p37876676163918"></a>None</p>
</td>
</tr>
<tr id="row185469811518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p3074001411518"><a name="p3074001411518"></a><a name="p3074001411518"></a>COPY Object</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p13977811518"><a name="p13977811518"></a><a name="p13977811518"></a>Copies an object.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p3364033111518"><a name="p3364033111518"></a><a name="p3364033111518"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p4373413111518"><a name="p4373413111518"></a><a name="p4373413111518"></a>None</p>
</td>
</tr>
<tr id="row4826894211518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p547642311518"><a name="p547642311518"></a><a name="p547642311518"></a>DELETE Object</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p1195403511518"><a name="p1195403511518"></a><a name="p1195403511518"></a>Deletes an object.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p2918284111518"><a name="p2918284111518"></a><a name="p2918284111518"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p5793804611518"><a name="p5793804611518"></a><a name="p5793804611518"></a>None</p>
</td>
</tr>
<tr id="row2664965211518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p3645343311518"><a name="p3645343311518"></a><a name="p3645343311518"></a>HEAD Object</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p782943311518"><a name="p782943311518"></a><a name="p782943311518"></a>Obtains object metadata.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p794076411518"><a name="p794076411518"></a><a name="p794076411518"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p1261944211518"><a name="p1261944211518"></a><a name="p1261944211518"></a>None</p>
</td>
</tr>
<tr id="row4763511211518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p1374928211518"><a name="p1374928211518"></a><a name="p1374928211518"></a>POST Object</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p2709443011518"><a name="p2709443011518"></a><a name="p2709443011518"></a>Creates or updates object metadata.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p4592832511518"><a name="p4592832511518"></a><a name="p4592832511518"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p3032185511518"><a name="p3032185511518"></a><a name="p3032185511518"></a>None</p>
</td>
</tr>
<tr id="row3523650611518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p65818149171859"><a name="p65818149171859"></a><a name="p65818149171859"></a>Object Version</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p56122160171859"><a name="p56122160171859"></a><a name="p56122160171859"></a>Supports operations corresponding to object versioning.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p57763930171859"><a name="p57763930171859"></a><a name="p57763930171859"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p19333355171859"><a name="p19333355171859"></a><a name="p19333355171859"></a>Object versioning is not supported.</p>
</td>
</tr>
<tr id="row1950244311518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p869802171842"><a name="p869802171842"></a><a name="p869802171842"></a>GET Large Object</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p32270649171842"><a name="p32270649171842"></a><a name="p32270649171842"></a>Gets large objects.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p4922374171842"><a name="p4922374171842"></a><a name="p4922374171842"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p11172443171842"><a name="p11172443171842"></a><a name="p11172443171842"></a>None</p>
</td>
</tr>
<tr id="row3718200511518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p45556706171847"><a name="p45556706171847"></a><a name="p45556706171847"></a>PUT Archive Auto Extraction</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p17319428171847"><a name="p17319428171847"></a><a name="p17319428171847"></a>Automatically decompresses uploaded objects.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p61363649171847"><a name="p61363649171847"></a><a name="p61363649171847"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p4353235171847"><a name="p4353235171847"></a><a name="p4353235171847"></a>This function is not supported.</p>
</td>
</tr>
<tr id="row1009772111518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p2085406171852"><a name="p2085406171852"></a><a name="p2085406171852"></a>PUT Large Object</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p14675125171852"><a name="p14675125171852"></a><a name="p14675125171852"></a>Puts large objects.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p1135304171852"><a name="p1135304171852"></a><a name="p1135304171852"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p44168862171852"><a name="p44168862171852"></a><a name="p44168862171852"></a>A static large object has a maximum of 1000 parts.</p>
</td>
</tr>
<tr id="row2020022311518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p4204380115043"><a name="p4204380115043"></a><a name="p4204380115043"></a>COPY Large Object</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p150935915043"><a name="p150935915043"></a><a name="p150935915043"></a>Copies large objects.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p3769726515043"><a name="p3769726515043"></a><a name="p3769726515043"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p5636566815043"><a name="p5636566815043"></a><a name="p5636566815043"></a>None</p>
</td>
</tr>
<tr id="row6417541711518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p2482556015043"><a name="p2482556015043"></a><a name="p2482556015043"></a>BULK DELETE Object</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p893629315043"><a name="p893629315043"></a><a name="p893629315043"></a>Batch deletes objects.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p3719716115043"><a name="p3719716115043"></a><a name="p3719716115043"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p1871828315043"><a name="p1871828315043"></a><a name="p1871828315043"></a>None</p>
</td>
</tr>
<tr id="row4798969511518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p3075359415043"><a name="p3075359415043"></a><a name="p3075359415043"></a>Delete Large Object</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p648164515043"><a name="p648164515043"></a><a name="p648164515043"></a>Deletes large objects.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p1198422715043"><a name="p1198422715043"></a><a name="p1198422715043"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p1970422715043"><a name="p1970422715043"></a><a name="p1970422715043"></a>None</p>
</td>
</tr>
<tr id="row2956930011518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p3998041315043"><a name="p3998041315043"></a><a name="p3998041315043"></a>Expiring Object Support</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p1424467815043"><a name="p1424467815043"></a><a name="p1424467815043"></a>Deletes objects as scheduled.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p2824438315043"><a name="p2824438315043"></a><a name="p2824438315043"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p3948779015043"><a name="p3948779015043"></a><a name="p3948779015043"></a>This function is not supported.</p>
</td>
</tr>
<tr id="row363135811518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p1891440215043"><a name="p1891440215043"></a><a name="p1891440215043"></a>Object TempURL</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p1064581015043"><a name="p1064581015043"></a><a name="p1064581015043"></a>Performs object TempURL operations.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p6695241315043"><a name="p6695241315043"></a><a name="p6695241315043"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p511837915043"><a name="p511837915043"></a><a name="p511837915043"></a>When <strong id="b8713795"><a name="b8713795"></a><a name="b8713795"></a>outgoing_allow_head</strong> is set in TempURL, the content of the <strong id="b11315292"><a name="b11315292"></a><a name="b11315292"></a>Content-Type</strong> header cannot be removed.</p>
</td>
</tr>
<tr id="row5481752111518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p2107972115043"><a name="p2107972115043"></a><a name="p2107972115043"></a>Storage Policy</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p1493643215043"><a name="p1493643215043"></a><a name="p1493643215043"></a>Configures storage policies.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p3350575815043"><a name="p3350575815043"></a><a name="p3350575815043"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p4186108115043"><a name="p4186108115043"></a><a name="p4186108115043"></a>OpenStack Swift's storage policy configuration is not supported. None of the APIs allow the <strong id="b108721710015316"><a name="b108721710015316"></a><a name="b108721710015316"></a>X-Newest</strong> header to be carried.</p>
</td>
</tr>
<tr id="row5839418011518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p2163790615043"><a name="p2163790615043"></a><a name="p2163790615043"></a>Rate limiting</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p2081094415043"><a name="p2081094415043"></a><a name="p2081094415043"></a>Allows a configuration file to limit the rate.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p433648015043"><a name="p433648015043"></a><a name="p433648015043"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p520409015043"><a name="p520409015043"></a><a name="p520409015043"></a>A configuration file is not allowed to limit the rate.</p>
</td>
</tr>
<tr id="row2002546411518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p2244207815043"><a name="p2244207815043"></a><a name="p2244207815043"></a>Erasure Code Support</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p4955644915043"><a name="p4955644915043"></a><a name="p4955644915043"></a>Supports the Erasure Code algorithm at the underlying layer.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p3941277215043"><a name="p3941277215043"></a><a name="p3941277215043"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p3837345315043"><a name="p3837345315043"></a><a name="p3837345315043"></a>This function is not supported.</p>
</td>
</tr>
<tr id="row4677068711518"><td class="cellrowborder" valign="top" width="22.73%" headers="mcps1.2.5.1.1 "><p id="p2497057115043"><a name="p2497057115043"></a><a name="p2497057115043"></a>TempAuth</p>
</td>
<td class="cellrowborder" valign="top" width="26.61%" headers="mcps1.2.5.1.2 "><p id="p5430466115043"><a name="p5430466115043"></a><a name="p5430466115043"></a>Supports simple authentication provided by OpenStack Swift.</p>
</td>
<td class="cellrowborder" valign="top" width="24.169999999999998%" headers="mcps1.2.5.1.3 "><p id="p3039204215043"><a name="p3039204215043"></a><a name="p3039204215043"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="26.490000000000002%" headers="mcps1.2.5.1.4 "><p id="p5557718415172"><a name="p5557718415172"></a><a name="p5557718415172"></a>Only IAM is supported.</p>
</td>
</tr>
</tbody>
</table>

The REST specifications of OBS \(compatible with OpenStack Swift\) are compatible with most specifications of OpenStack Swift.  [Table 2](#table43308771142121)  describes the differences between the REST specifications of OBS \(compatible with OpenStack Swift\) and the OpenStack Swift specifications.

**Table  2**  Differences between the REST specifications of OBS \(compatible with OpenStack Swift\) and the OpenStack Swift specifications

<a name="table43308771142121"></a>
<table><thead align="left"><tr id="row51298310142121"><th class="cellrowborder" valign="top" width="40.550000000000004%" id="mcps1.2.4.1.1"><p id="p16831085142121"><a name="p16831085142121"></a><a name="p16831085142121"></a>Item</p>
</th>
<th class="cellrowborder" valign="top" width="30.69%" id="mcps1.2.4.1.2"><p id="p21140616142121"><a name="p21140616142121"></a><a name="p21140616142121"></a><strong id="b39476331142524"><a name="b39476331142524"></a><a name="b39476331142524"></a>OpenStack Swift</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.76%" id="mcps1.2.4.1.3"><p id="p34668340142121"><a name="p34668340142121"></a><a name="p34668340142121"></a>REST Specifications of OBS (Compatible with OpenStack Swift)</p>
</th>
</tr>
</thead>
<tbody><tr id="row42627204142121"><td class="cellrowborder" valign="top" width="40.550000000000004%" headers="mcps1.2.4.1.1 "><p id="p4491259916220"><a name="p4491259916220"></a><a name="p4491259916220"></a>Maximum number of containers under an account</p>
</td>
<td class="cellrowborder" valign="top" width="30.69%" headers="mcps1.2.4.1.2 "><p id="p1404187316220"><a name="p1404187316220"></a><a name="p1404187316220"></a>None</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.3 "><p id="p6364991116220"><a name="p6364991116220"></a><a name="p6364991116220"></a>100</p>
</td>
</tr>
<tr id="row15625736142121"><td class="cellrowborder" valign="top" width="40.550000000000004%" headers="mcps1.2.4.1.1 "><p id="p57725098142121"><a name="p57725098142121"></a><a name="p57725098142121"></a>Maximum number of objects under a container</p>
</td>
<td class="cellrowborder" valign="top" width="30.69%" headers="mcps1.2.4.1.2 "><p id="p45221348142121"><a name="p45221348142121"></a><a name="p45221348142121"></a>None</p>
</td>
<td class="cellrowborder" valign="top" width="28.76%" headers="mcps1.2.4.1.3 "><p id="p39050591142121"><a name="p39050591142121"></a><a name="p39050591142121"></a>50 million</p>
</td>
</tr>
</tbody>
</table>

