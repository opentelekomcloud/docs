# Querying Product Specifications<a name="EN-US_TOPIC_0128036912"></a>

## Function<a name="section15275849309"></a>

This API is used to query the product specifications to configure the product ID.

## URI<a name="section651445311597"></a>

GET /v1.0/products?engine=\{engine\}

[Table 1](#table0211262515)  describes the parameter.

**Table  1**  Parameter description

<a name="table0211262515"></a>
<table><thead align="left"><tr id="row2031516262518"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="p631522182516"><a name="p631522182516"></a><a name="p631522182516"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p731516272513"><a name="p731516272513"></a><a name="p731516272513"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="p15315124252"><a name="p15315124252"></a><a name="p15315124252"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.5.1.4"><p id="p183155252514"><a name="p183155252514"></a><a name="p183155252514"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row183151820257"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p731542202515"><a name="p731542202515"></a><a name="p731542202515"></a>engine</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p14315028257"><a name="p14315028257"></a><a name="p14315028257"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p43151224252"><a name="p43151224252"></a><a name="p43151224252"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p2564113813111"><a name="p2564113813111"></a><a name="p2564113813111"></a>Indicates a message engine type.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section145141653175910"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section11526162120234"></a>

**Response parameters**

[Table 2](#table18238145151512)  describes the response parameters.

**Table  2**  Parameter description

<a name="table18238145151512"></a>
<table><thead align="left"><tr id="row8238951171516"><th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.1"><p id="p723895120156"><a name="p723895120156"></a><a name="p723895120156"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.669999999999998%" id="mcps1.2.4.1.2"><p id="p1238951131512"><a name="p1238951131512"></a><a name="p1238951131512"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p22385511154"><a name="p22385511154"></a><a name="p22385511154"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row35312151710"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p17605185517134"><a name="p17605185517134"></a><a name="p17605185517134"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p9605185513138"><a name="p9605185513138"></a><a name="p9605185513138"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p15605165511135"><a name="p15605165511135"></a><a name="p15605165511135"></a>Indicates the name of a message engine.</p>
</td>
</tr>
<tr id="row1825012201673"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p13604855101315"><a name="p13604855101315"></a><a name="p13604855101315"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p7603145512134"><a name="p7603145512134"></a><a name="p7603145512134"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1060385581311"><a name="p1060385581311"></a><a name="p1060385581311"></a>Indicates the version of the message engine.</p>
</td>
</tr>
<tr id="row1223815161515"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p3601555131319"><a name="p3601555131319"></a><a name="p3601555131319"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p660165516139"><a name="p660165516139"></a><a name="p660165516139"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p16600115541314"><a name="p16600115541314"></a><a name="p16600115541314"></a>Indicates product specifications. For details, see <a href="#table1380164413184">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  values parameter description

<a name="table1380164413184"></a>
<table><thead align="left"><tr id="row638510448187"><th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.1"><p id="p838664410183"><a name="p838664410183"></a><a name="p838664410183"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.669999999999998%" id="mcps1.2.4.1.2"><p id="p11387344141815"><a name="p11387344141815"></a><a name="p11387344141815"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p193901344121812"><a name="p193901344121812"></a><a name="p193901344121812"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5406644181813"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p15406644101819"><a name="p15406644101819"></a><a name="p15406644101819"></a>detail</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p11406114410181"><a name="p11406114410181"></a><a name="p11406114410181"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p84072447189"><a name="p84072447189"></a><a name="p84072447189"></a>Indicates the details of specifications. For details, see <a href="#table131863331362">Table 4</a>.</p>
</td>
</tr>
<tr id="row845716343197"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p84571341196"><a name="p84571341196"></a><a name="p84571341196"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p1041913917219"><a name="p1041913917219"></a><a name="p1041913917219"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p164571234151915"><a name="p164571234151915"></a><a name="p164571234151915"></a>Indicates an instance type.</p>
</td>
</tr>
<tr id="row1938162612911"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p869017313297"><a name="p869017313297"></a><a name="p869017313297"></a>unavailable_zones</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p5381172616290"><a name="p5381172616290"></a><a name="p5381172616290"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p53811526172920"><a name="p53811526172920"></a><a name="p53811526172920"></a>Indicates AZs where resources are sold out.</p>
</td>
</tr>
<tr id="row53817269292"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p469110311297"><a name="p469110311297"></a><a name="p469110311297"></a>available_zones</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p1638132622911"><a name="p1638132622911"></a><a name="p1638132622911"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p438132612912"><a name="p438132612912"></a><a name="p438132612912"></a>Indicates AZs where there are available resources.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  detail parameter description of Kafka instances

<a name="table131863331362"></a>
<table><thead align="left"><tr id="row1221713335369"><th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.1"><p id="p19217203373616"><a name="p19217203373616"></a><a name="p19217203373616"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.669999999999998%" id="mcps1.2.4.1.2"><p id="p122331733193611"><a name="p122331733193611"></a><a name="p122331733193611"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p1924993317367"><a name="p1924993317367"></a><a name="p1924993317367"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row132491133143618"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p624953343620"><a name="p624953343620"></a><a name="p624953343620"></a>tps</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p3264143317362"><a name="p3264143317362"></a><a name="p3264143317362"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p428183393613"><a name="p428183393613"></a><a name="p428183393613"></a>Indicates the maximum number of messages per unit time.</p>
</td>
</tr>
<tr id="row19281183343619"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p142961533193611"><a name="p142961533193611"></a><a name="p142961533193611"></a>storage</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p129618331367"><a name="p129618331367"></a><a name="p129618331367"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1296203383615"><a name="p1296203383615"></a><a name="p1296203383615"></a>Indicates the message storage space.</p>
</td>
</tr>
<tr id="row885716414319"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p124201933173610"><a name="p124201933173610"></a><a name="p124201933173610"></a>partition_num</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p943619337365"><a name="p943619337365"></a><a name="p943619337365"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p0453533103617"><a name="p0453533103617"></a><a name="p0453533103617"></a>Indicates the maximum number of topics in a Kafka instance.</p>
</td>
</tr>
<tr id="row11344202612318"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p4467163343610"><a name="p4467163343610"></a><a name="p4467163343610"></a>product_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p5467433143614"><a name="p5467433143614"></a><a name="p5467433143614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p3483433183610"><a name="p3483433183610"></a><a name="p3483433183610"></a>Indicates the product ID.</p>
</td>
</tr>
<tr id="row7514403319"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p15500433193611"><a name="p15500433193611"></a><a name="p15500433193611"></a>spec_code</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p11500633123618"><a name="p11500633123618"></a><a name="p11500633123618"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p15500203319369"><a name="p15500203319369"></a><a name="p15500203319369"></a>Indicates the specification ID.</p>
</td>
</tr>
<tr id="row18311193313369"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p15311133312365"><a name="p15311133312365"></a><a name="p15311133312365"></a>io</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p3327133313362"><a name="p3327133313362"></a><a name="p3327133313362"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p8342173393611"><a name="p8342173393611"></a><a name="p8342173393611"></a>Indicates the I/O information. For details, see <a href="#table1132314152265">Table 5</a>.</p>
</td>
</tr>
<tr id="row11374143311369"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p2037453393614"><a name="p2037453393614"></a><a name="p2037453393614"></a>bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p6389133373620"><a name="p6389133373620"></a><a name="p6389133373620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p154201133183619"><a name="p154201133183619"></a><a name="p154201133183619"></a>Indicates the bandwidth of a Kafka instance.</p>
</td>
</tr>
<tr id="row442053315369"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p1799611161319"><a name="p1799611161319"></a><a name="p1799611161319"></a>available_zones</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p49952164318"><a name="p49952164318"></a><a name="p49952164318"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p69893166319"><a name="p69893166319"></a><a name="p69893166319"></a>Indicates AZs where there are available resources.</p>
</td>
</tr>
<tr id="row1745313335362"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p361218301318"><a name="p361218301318"></a><a name="p361218301318"></a>ecs_flavor_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p1461083013110"><a name="p1461083013110"></a><a name="p1461083013110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p3609130103111"><a name="p3609130103111"></a><a name="p3609130103111"></a>Indicates the VM specifications of the instance resources.</p>
</td>
</tr>
<tr id="row20483173317360"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p572714493311"><a name="p572714493311"></a><a name="p572714493311"></a>arch_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p10726949143113"><a name="p10726949143113"></a><a name="p10726949143113"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p18724949143119"><a name="p18724949143119"></a><a name="p18724949143119"></a>Indicates the instance architecture type. Currently, only x86 is supported.</p>
</td>
</tr>
</tbody>
</table>

**Table  5**  io parameter description

<a name="table1132314152265"></a>
<table><thead align="left"><tr id="row73551615202613"><th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.1"><p id="p1937011510262"><a name="p1937011510262"></a><a name="p1937011510262"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.669999999999998%" id="mcps1.2.4.1.2"><p id="p11370131520264"><a name="p11370131520264"></a><a name="p11370131520264"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p73862157263"><a name="p73862157263"></a><a name="p73862157263"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12386131542612"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p1740110156264"><a name="p1740110156264"></a><a name="p1740110156264"></a>io_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p840131502615"><a name="p840131502615"></a><a name="p840131502615"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p8417121572617"><a name="p8417121572617"></a><a name="p8417121572617"></a>Indicates the I/O type.</p>
</td>
</tr>
<tr id="row941781532612"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p54253862613"><a name="p54253862613"></a><a name="p54253862613"></a>storage_spec_code</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p34481152265"><a name="p34481152265"></a><a name="p34481152265"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p194481158263"><a name="p194481158263"></a><a name="p194481158263"></a>Indicates the I/O specification.</p>
</td>
</tr>
<tr id="row1175725115333"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p167571951113311"><a name="p167571951113311"></a><a name="p167571951113311"></a>available_zones</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p5757851193317"><a name="p5757851193317"></a><a name="p5757851193317"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1775795111335"><a name="p1775795111335"></a><a name="p1775795111335"></a>Indicates AZs where there are available I/O resources.</p>
</td>
</tr>
<tr id="row1175765183316"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p3757751163315"><a name="p3757751163315"></a><a name="p3757751163315"></a>volume_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.2.4.1.2 "><p id="p1975714519335"><a name="p1975714519335"></a><a name="p1975714519335"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p127571151103311"><a name="p127571151103311"></a><a name="p127571151103311"></a>Indicates the disk type.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
	"Hourly": [{
		"name": "kafka",
		"version": "2.3.0",
		"values": [{
			"detail": [{
				"tps": "50000",
				"storage": "600",
				"partition_num": "300",
				"product_id": "00300-30308-0--0",
				"spec_code": "dms.instance.kafka.cluster.c3.mini",
				"io": [{
					"io_type": "high",
					"storage_spec_code": "dms.physical.storage.high",
					"available_zones": ["eu-de-02",
					"eu-de-01"],
					"volume_type": "SAS"
				},
				{
					"io_type": "ultra",
					"storage_spec_code": "dms.physical.storage.ultra",
					"available_zones": ["eu-de-02",
					"eu-de-01"],
					"volume_type": "SSD"
				}],
				"bandwidth": "100MB",
				"unavailable_zones": ["eu-de-02"],
				"available_zones": ["eu-de-01"],
				"ecs_flavor_id": "c4.large.2",
				"arch_type": "X86"
			},
			{
				"tps": "100000",
				"storage": "1200",
				"partition_num": "900",
				"product_id": "00300-30310-0--0",
				"spec_code": "dms.instance.kafka.cluster.c3.small.2",
				"io": [{
					"io_type": "high",
					"storage_spec_code": "dms.physical.storage.high",
					"available_zones": ["eu-de-02",
					"eu-de-01"],
					"volume_type": "SAS"
				},
				{
					"io_type": "ultra",
					"storage_spec_code": "dms.physical.storage.ultra",
					"available_zones": ["eu-de-02",
					"eu-de-01"],
					"volume_type": "SSD"
				}],
				"bandwidth": "300MB",
				"unavailable_zones": ["eu-de-02"],
				"available_zones": ["eu-de-01"],
				"ecs_flavor_id": "c4.xlarge.2",
				"arch_type": "X86"
			},
			{
				"tps": "200000",
				"storage": "2400",
				"partition_num": "1800",
				"product_id": "00300-30312-0--0",
				"spec_code": "dms.instance.kafka.cluster.c3.middle.2",
				"io": [{
					"io_type": "ultra",
					"storage_spec_code": "dms.physical.storage.ultra",
					"available_zones": ["eu-de-02",
					"eu-de-01"],
					"volume_type": "SSD"
				}],
				"bandwidth": "600MB",
				"unavailable_zones": ["eu-de-02"],
				"available_zones": ["eu-de-01"],
				"ecs_flavor_id": "c4.2xlarge.2",
				"arch_type": "X86"
			},
			{
				"tps": "300000",
				"storage": "4800",
				"partition_num": "1800",
				"product_id": "00300-30314-0--0",
				"spec_code": "dms.instance.kafka.cluster.c3.high.2",
				"io": [{
					"io_type": "ultra",
					"storage_spec_code": "dms.physical.storage.ultra",
					"available_zones": ["eu-de-02",
					"eu-de-01"],
					"volume_type": "SSD"
				}],
				"bandwidth": "1200MB",
				"unavailable_zones": ["eu-de-02"],
				"available_zones": ["eu-de-01"],
				"ecs_flavor_id": "c4.2xlarge.2",
				"arch_type": "X86"
			}],
			"name": "cluster",
			"unavailable_zones": ["eu-de-02"],
			"available_zones": ["eu-de-01"]
		}]
	}]
}
```

## Status Code<a name="section1557653155920"></a>

[Table 6](#table2557155375912)  describes the status code of successful operations. For details about other status codes, see  [Status Code](status-code.md).

**Table  6**  Status code

<a name="table2557155375912"></a>
<table><thead align="left"><tr id="row963675310593"><th class="cellrowborder" valign="top" width="15.15%" id="mcps1.2.3.1.1"><p id="p146361353155914"><a name="p146361353155914"></a><a name="p146361353155914"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.85000000000001%" id="mcps1.2.3.1.2"><p id="p1363655375910"><a name="p1363655375910"></a><a name="p1363655375910"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8636185325919"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.3.1.1 "><p id="p1063635325912"><a name="p1063635325912"></a><a name="p1063635325912"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.85000000000001%" headers="mcps1.2.3.1.2 "><p id="p46360535595"><a name="p46360535595"></a><a name="p46360535595"></a>Product specifications queried successfully.</p>
</td>
</tr>
</tbody>
</table>

