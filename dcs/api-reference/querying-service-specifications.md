# Querying Service Specifications<a name="EN-US_TOPIC_0237964379"></a>

## Function<a name="section35039337"></a>

This API is used to query the specifications of the DCS service to which you can subscribe.

## URI<a name="section46918583"></a>

-   URI format:

    GET /v1.0/products

-   Parameter description:

    None.


## Request<a name="section19614067"></a>

None.

## Response<a name="section42308878"></a>

-   Status code:

    If status code "200 OK" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    [Table 1](#table11231275217)  describes the response parameters.


**Table  1**  Parameter description

<a name="table11231275217"></a>
<table><thead align="left"><tr id="row44696736"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p63665841"><a name="p63665841"></a><a name="p63665841"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p56659528"><a name="p56659528"></a><a name="p56659528"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p26019018"><a name="p26019018"></a><a name="p26019018"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row27165729"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p52940469"><a name="p52940469"></a><a name="p52940469"></a>products</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p60319597"><a name="p60319597"></a><a name="p60319597"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p54049202"><a name="p54049202"></a><a name="p54049202"></a>List of specifications of the DCS service to which you can subscribe.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  products parameter description

<a name="table16680772"></a>
<table><thead align="left"><tr id="row38416353"><th class="cellrowborder" valign="top" width="23.232323232323232%" id="mcps1.2.4.1.1"><p id="p24716925"><a name="p24716925"></a><a name="p24716925"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.4.1.2"><p id="p55913876"><a name="p55913876"></a><a name="p55913876"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60.60606060606061%" id="mcps1.2.4.1.3"><p id="p32730128"><a name="p32730128"></a><a name="p32730128"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row33894745"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p61119830"><a name="p61119830"></a><a name="p61119830"></a>details</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p51759216"><a name="p51759216"></a><a name="p51759216"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p31746958"><a name="p31746958"></a><a name="p31746958"></a>Details of the chosen DCS specification.</p>
</td>
</tr>
<tr id="row17287170"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p58083554"><a name="p58083554"></a><a name="p58083554"></a>engine</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p7147451"><a name="p7147451"></a><a name="p7147451"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p42072628"><a name="p42072628"></a><a name="p42072628"></a>Cache engine.</p>
</td>
</tr>
<tr id="row43109332"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p2194976"><a name="p2194976"></a><a name="p2194976"></a>price</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p43575393"><a name="p43575393"></a><a name="p43575393"></a>doubule</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p39945983"><a name="p39945983"></a><a name="p39945983"></a>Price of the DCS service to which you can subscribe. (This parameter has been abandoned.)</p>
</td>
</tr>
<tr id="row23969532"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p62483952"><a name="p62483952"></a><a name="p62483952"></a>currency</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p28035315"><a name="p28035315"></a><a name="p28035315"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p56268080"><a name="p56268080"></a><a name="p56268080"></a>Currency.</p>
</td>
</tr>
<tr id="row36650675"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p15914679"><a name="p15914679"></a><a name="p15914679"></a>flavors</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p14020616"><a name="p14020616"></a><a name="p14020616"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p61928077"><a name="p61928077"></a><a name="p61928077"></a>AZs with available resources.</p>
</td>
</tr>
<tr id="row20481782"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p48411685"><a name="p48411685"></a><a name="p48411685"></a>product_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p29032445"><a name="p29032445"></a><a name="p29032445"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p2817829"><a name="p2817829"></a><a name="p2817829"></a>Product ID of DCS.</p>
</td>
</tr>
<tr id="row25360462"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p40931570"><a name="p40931570"></a><a name="p40931570"></a>spec_code</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p27122874"><a name="p27122874"></a><a name="p27122874"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p49469199"><a name="p49469199"></a><a name="p49469199"></a>DCS specification ID.</p>
<p id="p42569609"><a name="p42569609"></a><a name="p42569609"></a>Options:</p>
<a name="ul47582168"></a><a name="ul47582168"></a><ul id="ul47582168"><li><strong id="b28950398"><a name="b28950398"></a><a name="b28950398"></a>dcs.single_node</strong></li><li><strong id="b63280872"><a name="b63280872"></a><a name="b63280872"></a>dcs.master_standby</strong></li><li><strong id="b25476990"><a name="b25476990"></a><a name="b25476990"></a>dcs.cluster</strong></li></ul>
</td>
</tr>
<tr id="row27966326"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p50679930"><a name="p50679930"></a><a name="p50679930"></a>cache_mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p11433695"><a name="p11433695"></a><a name="p11433695"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p53714125"><a name="p53714125"></a><a name="p53714125"></a>DCS instance type. Options:</p>
<a name="ul13665078"></a><a name="ul13665078"></a><ul id="ul13665078"><li><strong id="b33129539"><a name="b33129539"></a><a name="b33129539"></a>single</strong>: single-node</li><li><strong id="b66247021"><a name="b66247021"></a><a name="b66247021"></a>ha</strong>: master/standby</li><li><strong id="b64408475"><a name="b64408475"></a><a name="b64408475"></a>cluster</strong>: Redis Cluster</li></ul>
</td>
</tr>
<tr id="row42805367"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p44682727"><a name="p44682727"></a><a name="p44682727"></a>product_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p62531152"><a name="p62531152"></a><a name="p62531152"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p31858521"><a name="p31858521"></a><a name="p31858521"></a>Product type.</p>
<p id="p18291233"><a name="p18291233"></a><a name="p18291233"></a>Options: <strong id="b30403370"><a name="b30403370"></a><a name="b30403370"></a>generic</strong></p>
</td>
</tr>
<tr id="row5194877"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p18131918"><a name="p18131918"></a><a name="p18131918"></a>cpu_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p59399292"><a name="p59399292"></a><a name="p59399292"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p46613358"><a name="p46613358"></a><a name="p46613358"></a>CPU architecture.</p>
<p id="p16867045"><a name="p16867045"></a><a name="p16867045"></a>Options: <strong id="b17585677"><a name="b17585677"></a><a name="b17585677"></a>x86_64</strong></p>
</td>
</tr>
<tr id="row24053368"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p2165829"><a name="p2165829"></a><a name="p2165829"></a>storage_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p41214450"><a name="p41214450"></a><a name="p41214450"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p50036135"><a name="p50036135"></a><a name="p50036135"></a>Memory type.</p>
<p id="p47672037"><a name="p47672037"></a><a name="p47672037"></a>Options: <strong id="b26395149"><a name="b26395149"></a><a name="b26395149"></a>DRAM</strong></p>
</td>
</tr>
<tr id="row36229754"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p48928939"><a name="p48928939"></a><a name="p48928939"></a>engine_versions</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p3821154"><a name="p3821154"></a><a name="p3821154"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p41078020"><a name="p41078020"></a><a name="p41078020"></a>Supported cache engine versions.</p>
</td>
</tr>
<tr id="row34157866"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p15323738"><a name="p15323738"></a><a name="p15323738"></a>spec_details</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p33263275"><a name="p33263275"></a><a name="p33263275"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p9970756"><a name="p9970756"></a><a name="p9970756"></a>Details of DCS specification information, which is a character string in the JSON format.</p>
<a name="ul22627948"></a><a name="ul22627948"></a><ul id="ul22627948"><li>When <strong id="b20924485"><a name="b20924485"></a><a name="b20924485"></a>spec_code</strong> is <strong id="b54102641"><a name="b54102641"></a><a name="b54102641"></a>dcs.single_node</strong>, the value of <strong id="b17161723"><a name="b17161723"></a><a name="b17161723"></a>spec_details</strong> is <strong id="b20237780"><a name="b20237780"></a><a name="b20237780"></a>2,4,8,16,32,64</strong>.</li><li>When <strong id="b28647455"><a name="b28647455"></a><a name="b28647455"></a>spec_code</strong> is <strong id="b56500507"><a name="b56500507"></a><a name="b56500507"></a>dcs.master_standby</strong>, the value of <strong id="b38742523"><a name="b38742523"></a><a name="b38742523"></a>spec_details</strong> is <strong id="b13138391"><a name="b13138391"></a><a name="b13138391"></a>2,4,8,16,32,64</strong>.</li><li>When <strong id="b57576718"><a name="b57576718"></a><a name="b57576718"></a>spec_code</strong> is <strong id="b48428420"><a name="b48428420"></a><a name="b48428420"></a>dcs.cluster</strong>, the value of <strong id="b33202602"><a name="b33202602"></a><a name="b33202602"></a>spec_details</strong> is <strong id="b30387970"><a name="b30387970"></a><a name="b30387970"></a>64,128,256,512</strong>.</li></ul>
</td>
</tr>
<tr id="row5056275"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p6905136"><a name="p6905136"></a><a name="p6905136"></a>spec_details2</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p22445162"><a name="p22445162"></a><a name="p22445162"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p6118824"><a name="p6118824"></a><a name="p6118824"></a>Details of DCS specifications, including the maximum number of connections and maximum memory size.</p>
</td>
</tr>
<tr id="row55069420"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p31438060"><a name="p31438060"></a><a name="p31438060"></a>charging_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p63454949"><a name="p63454949"></a><a name="p63454949"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p39577214"><a name="p39577214"></a><a name="p39577214"></a>Billing mode.</p>
<p id="p20650606"><a name="p20650606"></a><a name="p20650606"></a>Value: <strong id="b51637727"><a name="b51637727"></a><a name="b51637727"></a>Hourly</strong>.</p>
<p id="p62086362"><a name="p62086362"></a><a name="p62086362"></a>Charging mode.</p>
</td>
</tr>
<tr id="row21906353"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p29584155"><a name="p29584155"></a><a name="p29584155"></a>prod_type</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p47506374"><a name="p47506374"></a><a name="p47506374"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p22811098"><a name="p22811098"></a><a name="p22811098"></a>Product type.</p>
<p id="p3973290"><a name="p3973290"></a><a name="p3973290"></a>Options: <strong id="b35759613"><a name="b35759613"></a><a name="b35759613"></a>instance</strong> and <strong id="b53401069"><a name="b53401069"></a><a name="b53401069"></a>obs_space</strong>.</p>
</td>
</tr>
<tr id="row10847578"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p6238615"><a name="p6238615"></a><a name="p6238615"></a>cloud_service_type_code</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p35565788"><a name="p35565788"></a><a name="p35565788"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p62256594"><a name="p62256594"></a><a name="p62256594"></a>Cloud service type code.</p>
</td>
</tr>
<tr id="row23438439"><td class="cellrowborder" valign="top" width="23.232323232323232%" headers="mcps1.2.4.1.1 "><p id="p19465384"><a name="p19465384"></a><a name="p19465384"></a>cloud_resource_type_code</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.4.1.2 "><p id="p33192303"><a name="p33192303"></a><a name="p33192303"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p4221985"><a name="p4221985"></a><a name="p4221985"></a>Cloud resource type code.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  details parameter description

<a name="table37997871"></a>
<table><thead align="left"><tr id="row25167817"><th class="cellrowborder" valign="top" width="23.46938775510204%" id="mcps1.2.4.1.1"><p id="p25327282"><a name="p25327282"></a><a name="p25327282"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="16.3265306122449%" id="mcps1.2.4.1.2"><p id="p38243960"><a name="p38243960"></a><a name="p38243960"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60.204081632653065%" id="mcps1.2.4.1.3"><p id="p10753026"><a name="p10753026"></a><a name="p10753026"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row65688760"><td class="cellrowborder" valign="top" width="23.46938775510204%" headers="mcps1.2.4.1.1 "><p id="p19189380"><a name="p19189380"></a><a name="p19189380"></a>capacity</p>
</td>
<td class="cellrowborder" valign="top" width="16.3265306122449%" headers="mcps1.2.4.1.2 "><p id="p10835915"><a name="p10835915"></a><a name="p10835915"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.204081632653065%" headers="mcps1.2.4.1.3 "><p id="p5293943"><a name="p5293943"></a><a name="p5293943"></a>Specification (total memory) of the DCS instance.</p>
</td>
</tr>
<tr id="row47645495"><td class="cellrowborder" valign="top" width="23.46938775510204%" headers="mcps1.2.4.1.1 "><p id="p34079861"><a name="p34079861"></a><a name="p34079861"></a>max_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="16.3265306122449%" headers="mcps1.2.4.1.2 "><p id="p9005323"><a name="p9005323"></a><a name="p9005323"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.204081632653065%" headers="mcps1.2.4.1.3 "><p id="p58342562"><a name="p58342562"></a><a name="p58342562"></a>Maximum bandwidth supported by the specification.</p>
</td>
</tr>
<tr id="row55321013"><td class="cellrowborder" valign="top" width="23.46938775510204%" headers="mcps1.2.4.1.1 "><p id="p51817072"><a name="p51817072"></a><a name="p51817072"></a>max_clients</p>
</td>
<td class="cellrowborder" valign="top" width="16.3265306122449%" headers="mcps1.2.4.1.2 "><p id="p36433279"><a name="p36433279"></a><a name="p36433279"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.204081632653065%" headers="mcps1.2.4.1.3 "><p id="p65414475"><a name="p65414475"></a><a name="p65414475"></a>Maximum number of clients supported by the specification, which is usually equal to the maximum number of connections.</p>
</td>
</tr>
<tr id="row51859363"><td class="cellrowborder" valign="top" width="23.46938775510204%" headers="mcps1.2.4.1.1 "><p id="p39858836"><a name="p39858836"></a><a name="p39858836"></a>max_connections</p>
</td>
<td class="cellrowborder" valign="top" width="16.3265306122449%" headers="mcps1.2.4.1.2 "><p id="p7340278"><a name="p7340278"></a><a name="p7340278"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.204081632653065%" headers="mcps1.2.4.1.3 "><p id="p57691632"><a name="p57691632"></a><a name="p57691632"></a>Maximum number of connections supported by the specification.</p>
</td>
</tr>
<tr id="row49462646"><td class="cellrowborder" valign="top" width="23.46938775510204%" headers="mcps1.2.4.1.1 "><p id="p47051400"><a name="p47051400"></a><a name="p47051400"></a>max_in_bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="16.3265306122449%" headers="mcps1.2.4.1.2 "><p id="p53067079"><a name="p53067079"></a><a name="p53067079"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.204081632653065%" headers="mcps1.2.4.1.3 "><p id="p3466138"><a name="p3466138"></a><a name="p3466138"></a>Maximum inbound bandwidth supported by the specification, which is usually equal to the maximum bandwidth.</p>
</td>
</tr>
<tr id="row31195247"><td class="cellrowborder" valign="top" width="23.46938775510204%" headers="mcps1.2.4.1.1 "><p id="p43787068"><a name="p43787068"></a><a name="p43787068"></a>max_memory</p>
</td>
<td class="cellrowborder" valign="top" width="16.3265306122449%" headers="mcps1.2.4.1.2 "><p id="p57091601"><a name="p57091601"></a><a name="p57091601"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.204081632653065%" headers="mcps1.2.4.1.3 "><p id="p61016983"><a name="p61016983"></a><a name="p61016983"></a>Maximum available memory.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  flavors parameter description

<a name="table12281940"></a>
<table><thead align="left"><tr id="row59688756"><th class="cellrowborder" valign="top" width="23.46938775510204%" id="mcps1.2.4.1.1"><p id="p2951044"><a name="p2951044"></a><a name="p2951044"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="16.3265306122449%" id="mcps1.2.4.1.2"><p id="p37708021"><a name="p37708021"></a><a name="p37708021"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60.204081632653065%" id="mcps1.2.4.1.3"><p id="p34450862"><a name="p34450862"></a><a name="p34450862"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row39056472"><td class="cellrowborder" valign="top" width="23.46938775510204%" headers="mcps1.2.4.1.1 "><p id="p9457691"><a name="p9457691"></a><a name="p9457691"></a>capacity</p>
</td>
<td class="cellrowborder" valign="top" width="16.3265306122449%" headers="mcps1.2.4.1.2 "><p id="p27875486"><a name="p27875486"></a><a name="p27875486"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.204081632653065%" headers="mcps1.2.4.1.3 "><p id="p43321865"><a name="p43321865"></a><a name="p43321865"></a>Specification (total memory) of the DCS instance.</p>
</td>
</tr>
<tr id="row54352469"><td class="cellrowborder" valign="top" width="23.46938775510204%" headers="mcps1.2.4.1.1 "><p id="p40473905"><a name="p40473905"></a><a name="p40473905"></a>unit</p>
</td>
<td class="cellrowborder" valign="top" width="16.3265306122449%" headers="mcps1.2.4.1.2 "><p id="p57160840"><a name="p57160840"></a><a name="p57160840"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.204081632653065%" headers="mcps1.2.4.1.3 "><p id="p66625348"><a name="p66625348"></a><a name="p66625348"></a>Capacity unit.</p>
</td>
</tr>
<tr id="row62757228"><td class="cellrowborder" valign="top" width="23.46938775510204%" headers="mcps1.2.4.1.1 "><p id="p50170682"><a name="p50170682"></a><a name="p50170682"></a>available_zones</p>
</td>
<td class="cellrowborder" valign="top" width="16.3265306122449%" headers="mcps1.2.4.1.2 "><p id="p37293408"><a name="p37293408"></a><a name="p37293408"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.204081632653065%" headers="mcps1.2.4.1.3 "><p id="p867207"><a name="p867207"></a><a name="p867207"></a>AZ ID.</p>
</td>
</tr>
</tbody>
</table>

Example response:

```
{ 
```

```
 "products": [ 
```

```
       { 
```

```
            "details": { 
```

```
                "capacity": 64, 
```

```
                "max_memory": 64, 
```

```
                "max_connections": 20000, 
```

```
                "max_clients": 80000, 
```

```
                "max_bandwidth": 2000, 
```

```
                "max_in_bandwidth": 600, 
```

```
                "proc_num": 8 
```

```
            }, 
```

```
            "engine": "redis", 
```

```
            "price": 0.04, 
```

```
            "currency": "1", 
```

```
            "flavors": [ 
```

```
                { 
```

```
                    "capacity": "64", 
```

```
                    "unit": "GB", 
```

```
                    "available_zones": [ 
```

```
                        "ae04cf9d61544df3806a3feeb401b204", 
```

```
                        "882f6e449e3245dbb8c1c0fafa494c89" 
```

```
                    ] 
```

```
                }, 
```

```
                { 
```

```
                    "capacity": "128", 
```

```
                    "unit": "GB", 
```

```
                    "available_zones": [ 
```

```
                        "ae04cf9d61544df3806a3feeb401b204", 
```

```
                        "882f6e449e3245dbb8c1c0fafa494c89" 
```

```
                    ] 
```

```
                }, 
```

```
                { 
```

```
                    "capacity": "256", 
```

```
                    "unit": "GB", 
```

```
                    "available_zones": [ 
```

```
                        "ae04cf9d61544df3806a3feeb401b204", 
```

```
                        "882f6e449e3245dbb8c1c0fafa494c89" 
```

```
                    ] 
```

```
                } 
```

```
            ], 
```

```
            "product_id": "00301-30112-0--0", 
```

```
            "spec_code": "dcs.cluster", 
```

```
            "cache_mode": "cluster", 
```

```
            "product_type": "generic", 
```

```
            "cpu_type": "x86_64", 
```

```
            "storage_type": "DRAM", 
```

```
            "engine_versions": "3.0.7", 
```

```
            "spec_details": "[{\"mem\":\"64,128,256\"}]", 
```

```
            "spec_details2": "[{\"capacity\": 64,\"max_memory\": 64,\"max_connections\": 20000,\"max_clients\":80000,\"max_bandwidth\": 2000,\"max_in_bandwidth\": 600,\"proc_num\":8},{\"capacity\": 128,\"max_memory\": 128,\"max_connections\": 20000,\"max_clients\":160000,\"max_bandwidth\": 2000,\"max_in_bandwidth\": 600,\"proc_num\":16},{\"capacity\": 256,\"max_memory\": 256,\"max_connections\": 20000,\"max_clients\":160000,\"max_bandwidth\": 2000,\"max_in_bandwidth\": 600,\"proc_num\":32},{\"capacity\": 512,\"max_memory\": 512,\"max_connections\": 20000,\"max_clients\":160000,\"max_bandwidth\": 2000,\"max_in_bandwidth\": 600,\"proc_num\":64},{\"capacity\": 1024,\"max_memory\": 1024,\"max_connections\": 20000,\"max_clients\":160000,\"max_bandwidth\": 2000,\"max_in_bandwidth\": 600,\"proc_num\":128}]", 
```

```
            "charging_type": "Hourly", 
```

```
            "prod_type": "instance", 
```

```
            "cloud_service_type_code": "otc.service.type.dcs", 
```

```
            "cloud_resource_type_code": "otc.resource.type.dcs" 
```

```
      }, 
```

```
}
```

