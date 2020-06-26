# Updating a Subnet Pool<a name="vpc_subnetpools_0004"></a>

## Function<a name="section10267951"></a>

This API is used to update a subnet pool.

## URI<a name="section25302698"></a>

PUT /v2.0/subnetpools/\{subnetpool\_id\}

## Request Message<a name="section36252627"></a>

**Table  1**  Request parameter

<a name="table40701910"></a>
<table><thead align="left"><tr id="row5914937"><th class="cellrowborder" valign="top" width="14.29%" id="mcps1.2.5.1.1"><p id="p9347893"><a name="p9347893"></a><a name="p9347893"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="8.16%" id="mcps1.2.5.1.2"><p id="p18981865"><a name="p18981865"></a><a name="p18981865"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="10.2%" id="mcps1.2.5.1.3"><p id="p61136126"><a name="p61136126"></a><a name="p61136126"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="67.35%" id="mcps1.2.5.1.4"><p id="p53079196"><a name="p53079196"></a><a name="p53079196"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4447594"><td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.2.5.1.1 "><p id="p24710800"><a name="p24710800"></a><a name="p24710800"></a>subnetpool</p>
</td>
<td class="cellrowborder" valign="top" width="8.16%" headers="mcps1.2.5.1.2 "><p id="p55417783"><a name="p55417783"></a><a name="p55417783"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="10.2%" headers="mcps1.2.5.1.3 "><p id="p59655430"><a name="p59655430"></a><a name="p59655430"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="67.35%" headers="mcps1.2.5.1.4 "><p id="p37955333"><a name="p37955333"></a><a name="p37955333"></a>Specifies the subnet pool list. For details, see <a href="#table12211980105515">Table 2</a>.</p>
<p id="p2265180"><a name="p2265180"></a><a name="p2265180"></a>You must specify at least one attribute when updating the subnet pool.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **subnetpool**  objects

<a name="table12211980105515"></a>
<table><thead align="left"><tr id="row32722637105515"><th class="cellrowborder" valign="top" width="24.86%" id="mcps1.2.5.1.1"><p id="p60075710105815"><a name="p60075710105815"></a><a name="p60075710105815"></a><strong id="b117161146205610"><a name="b117161146205610"></a><a name="b117161146205610"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.13%" id="mcps1.2.5.1.2"><p id="p15964952144115"><a name="p15964952144115"></a><a name="p15964952144115"></a><strong id="b161051427113710"><a name="b161051427113710"></a><a name="b161051427113710"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.389999999999999%" id="mcps1.2.5.1.3"><p id="p34294369105815"><a name="p34294369105815"></a><a name="p34294369105815"></a><strong id="b2469232133717"><a name="b2469232133717"></a><a name="b2469232133717"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.62%" id="mcps1.2.5.1.4"><p id="p25203839105815"><a name="p25203839105815"></a><a name="p25203839105815"></a><strong id="b143311033103718"><a name="b143311033103718"></a><a name="b143311033103718"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row43081158105515"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p54833166105624"><a name="p54833166105624"></a><a name="p54833166105624"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p179641252184115"><a name="p179641252184115"></a><a name="p179641252184115"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.389999999999999%" headers="mcps1.2.5.1.3 "><p id="p12301465105624"><a name="p12301465105624"></a><a name="p12301465105624"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.62%" headers="mcps1.2.5.1.4 "><p id="p14797472105624"><a name="p14797472105624"></a><a name="p14797472105624"></a>Specifies the subnet pool name.</p>
</td>
</tr>
<tr id="row49397935105515"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p23027912105624"><a name="p23027912105624"></a><a name="p23027912105624"></a>default_quota</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p7964152134116"><a name="p7964152134116"></a><a name="p7964152134116"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.389999999999999%" headers="mcps1.2.5.1.3 "><p id="p6099296144650"><a name="p6099296144650"></a><a name="p6099296144650"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.62%" headers="mcps1.2.5.1.4 "><p id="p2365807714488"><a name="p2365807714488"></a><a name="p2365807714488"></a>Specifies the upper limit of the prefix space that can be allocated from the subnet pool to the subnet. For IPv4 subnet pools, default_quota is measured in units of /32. For IPv6 subnet pools, default_quota is measured in units of /64.</p>
</td>
</tr>
<tr id="row62757710105647"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p5097986810577"><a name="p5097986810577"></a><a name="p5097986810577"></a>prefixes</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p139641652184112"><a name="p139641652184112"></a><a name="p139641652184112"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.389999999999999%" headers="mcps1.2.5.1.3 "><p id="p3572863210577"><a name="p3572863210577"></a><a name="p3572863210577"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="49.62%" headers="mcps1.2.5.1.4 "><p id="p1242857210116"><a name="p1242857210116"></a><a name="p1242857210116"></a>Specifies a list of subnet prefixes that are assigned to the subnet pool. The adjacent prefixes are merged and treated as a single prefix. Each subnet prefix must be unique.</p>
</td>
</tr>
<tr id="row2545218105647"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p1395064410577"><a name="p1395064410577"></a><a name="p1395064410577"></a>min_prefixlen</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p7964552174112"><a name="p7964552174112"></a><a name="p7964552174112"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.389999999999999%" headers="mcps1.2.5.1.3 "><p id="p5626034310577"><a name="p5626034310577"></a><a name="p5626034310577"></a>Integer</p>
<p id="p3658104710577"><a name="p3658104710577"></a><a name="p3658104710577"></a></p>
</td>
<td class="cellrowborder" valign="top" width="49.62%" headers="mcps1.2.5.1.4 "><p id="p3725182415446"><a name="p3725182415446"></a><a name="p3725182415446"></a>Specifies the minimum prefix that can be allocated from the subnet pool. Instructions:</p>
<p id="p793283773517"><a name="p793283773517"></a><a name="p793283773517"></a>min_prefixlen =&lt; default_prefixlen =&lt; max_prefixlen</p>
</td>
</tr>
<tr id="row21625046105653"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p4495318510577"><a name="p4495318510577"></a><a name="p4495318510577"></a>default_prefixlen</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p39641652114112"><a name="p39641652114112"></a><a name="p39641652114112"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.389999999999999%" headers="mcps1.2.5.1.3 "><p id="p1732939410577"><a name="p1732939410577"></a><a name="p1732939410577"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.62%" headers="mcps1.2.5.1.4 "><p id="p5482176910577"><a name="p5482176910577"></a><a name="p5482176910577"></a>Specifies the length of the prefix to allocate when the CIDR or prefixlen attributes are omitted when creating a subnet.</p>
<p id="p37814568346"><a name="p37814568346"></a><a name="p37814568346"></a>Instructions:</p>
<p id="p15995203519"><a name="p15995203519"></a><a name="p15995203519"></a>min_prefixlen =&lt; default_prefixlen =&lt; max_prefixlen</p>
</td>
</tr>
<tr id="row18053024151048"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p53008854151048"><a name="p53008854151048"></a><a name="p53008854151048"></a>max_prefixlen</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p1796525214415"><a name="p1796525214415"></a><a name="p1796525214415"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.389999999999999%" headers="mcps1.2.5.1.3 "><p id="p65858788151048"><a name="p65858788151048"></a><a name="p65858788151048"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.62%" headers="mcps1.2.5.1.4 "><p id="p14908979151048"><a name="p14908979151048"></a><a name="p14908979151048"></a>Specifies the maximum prefix length that can be allocated from the subnet pool.</p>
<p id="p179716319354"><a name="p179716319354"></a><a name="p179716319354"></a>Instructions:</p>
<p id="p979793119358"><a name="p979793119358"></a><a name="p979793119358"></a>min_prefixlen =&lt; default_prefixlen =&lt; max_prefixlen</p>
</td>
</tr>
<tr id="row8351286151053"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p5365552151053"><a name="p5365552151053"></a><a name="p5365552151053"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p129651752124116"><a name="p129651752124116"></a><a name="p129651752124116"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.389999999999999%" headers="mcps1.2.5.1.3 "><p id="p31956587151053"><a name="p31956587151053"></a><a name="p31956587151053"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.62%" headers="mcps1.2.5.1.4 "><p id="p28387452151053"><a name="p28387452151053"></a><a name="p28387452151053"></a>Provides supplementary information about the subnet pool.</p>
</td>
</tr>
<tr id="row3921595115167"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p2237545215167"><a name="p2237545215167"></a><a name="p2237545215167"></a>is_default</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p89651952104117"><a name="p89651952104117"></a><a name="p89651952104117"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.389999999999999%" headers="mcps1.2.5.1.3 "><p id="p47230515167"><a name="p47230515167"></a><a name="p47230515167"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="49.62%" headers="mcps1.2.5.1.4 "><p id="p4334828415167"><a name="p4334828415167"></a><a name="p4334828415167"></a>Specifies whether this is the default subnet pool.</p>
</td>
</tr>
<tr id="row21006459151647"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p23801595151647"><a name="p23801595151647"></a><a name="p23801595151647"></a>revision_number</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p10965195219417"><a name="p10965195219417"></a><a name="p10965195219417"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.389999999999999%" headers="mcps1.2.5.1.3 "><p id="p48881052151647"><a name="p48881052151647"></a><a name="p48881052151647"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="49.62%" headers="mcps1.2.5.1.4 "><p id="p59981829151647"><a name="p59981829151647"></a><a name="p59981829151647"></a>Specifies the revision number of the subnet pool.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="section57838187"></a>

**Table  3**  Response parameter

<a name="table49261880"></a>
<table><thead align="left"><tr id="row31386613"><th class="cellrowborder" valign="top" width="31.7%" id="mcps1.2.4.1.1"><p id="p59287744"><a name="p59287744"></a><a name="p59287744"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.080000000000002%" id="mcps1.2.4.1.2"><p id="p37577972"><a name="p37577972"></a><a name="p37577972"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="p58217140"><a name="p58217140"></a><a name="p58217140"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17967889"><td class="cellrowborder" valign="top" width="31.7%" headers="mcps1.2.4.1.1 "><p id="p46112886"><a name="p46112886"></a><a name="p46112886"></a>subnetpool</p>
</td>
<td class="cellrowborder" valign="top" width="17.080000000000002%" headers="mcps1.2.4.1.2 "><p id="p44156300"><a name="p44156300"></a><a name="p44156300"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p522217"><a name="p522217"></a><a name="p522217"></a>Specifies the subnet pool list. For details, see <a href="#table149662441462">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **subnetpool**  objects

<a name="table149662441462"></a>
<table><thead align="left"><tr id="row496617442612"><th class="cellrowborder" valign="top" width="24.33%" id="mcps1.2.4.1.1"><p id="p1596613445611"><a name="p1596613445611"></a><a name="p1596613445611"></a><strong id="b1269113154415"><a name="b1269113154415"></a><a name="b1269113154415"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.03%" id="mcps1.2.4.1.2"><p id="p49667449616"><a name="p49667449616"></a><a name="p49667449616"></a><strong id="b6130151714114"><a name="b6130151714114"></a><a name="b6130151714114"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="55.64%" id="mcps1.2.4.1.3"><p id="p8966144413616"><a name="p8966144413616"></a><a name="p8966144413616"></a><strong id="b5249118144114"><a name="b5249118144114"></a><a name="b5249118144114"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row28303131105515"><td class="cellrowborder" valign="top" width="24.33%" headers="mcps1.2.4.1.1 "><p id="p2014344105614"><a name="p2014344105614"></a><a name="p2014344105614"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p28944191105614"><a name="p28944191105614"></a><a name="p28944191105614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.2.4.1.3 "><p id="p53796361105614"><a name="p53796361105614"></a><a name="p53796361105614"></a>Specifies the subnet pool ID.</p>
<p id="p1089535311426"><a name="p1089535311426"></a><a name="p1089535311426"></a>This parameter is not mandatory when you query subnet pools.</p>
</td>
</tr>
<tr id="row1196634410618"><td class="cellrowborder" valign="top" width="24.33%" headers="mcps1.2.4.1.1 "><p id="p696615445611"><a name="p696615445611"></a><a name="p696615445611"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p3966104412620"><a name="p3966104412620"></a><a name="p3966104412620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.2.4.1.3 "><p id="p89666442613"><a name="p89666442613"></a><a name="p89666442613"></a>Specifies the subnet pool name.</p>
</td>
</tr>
<tr id="row9772661105515"><td class="cellrowborder" valign="top" width="24.33%" headers="mcps1.2.4.1.1 "><p id="p49939441105624"><a name="p49939441105624"></a><a name="p49939441105624"></a>ip_version</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p18562940105624"><a name="p18562940105624"></a><a name="p18562940105624"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.2.4.1.3 "><p id="p682749310257"><a name="p682749310257"></a><a name="p682749310257"></a>Specifies the IP address version.</p>
<p id="p33352482102727"><a name="p33352482102727"></a><a name="p33352482102727"></a>Only IPv4 address is supported.</p>
</td>
</tr>
<tr id="row89665441569"><td class="cellrowborder" valign="top" width="24.33%" headers="mcps1.2.4.1.1 "><p id="p79664442613"><a name="p79664442613"></a><a name="p79664442613"></a>default_quota</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p496616449616"><a name="p496616449616"></a><a name="p496616449616"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.2.4.1.3 "><p id="p7968244361"><a name="p7968244361"></a><a name="p7968244361"></a>Specifies the upper limit of the prefix space that can be allocated from the subnet pool to the subnet. For IPv4 subnet pools, default_quota is measured in units of /32. For IPv6 subnet pools, default_quota is measured in units of /64.</p>
</td>
</tr>
<tr id="row157121839115912"><td class="cellrowborder" valign="top" width="24.33%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p15700614790"><a name="p15700614790"></a><a name="p15700614790"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row2067783695917"><td class="cellrowborder" valign="top" width="24.33%" headers="mcps1.2.4.1.1 "><p id="p11508184345913"><a name="p11508184345913"></a><a name="p11508184345913"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p1651534311599"><a name="p1651534311599"></a><a name="p1651534311599"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.2.4.1.3 "><p id="p552334314592"><a name="p552334314592"></a><a name="p552334314592"></a>Specifies the time (UTC) when the subnet pool is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i895045134412"><a name="i895045134412"></a><a name="i895045134412"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row1428916334597"><td class="cellrowborder" valign="top" width="24.33%" headers="mcps1.2.4.1.1 "><p id="p15531114325914"><a name="p15531114325914"></a><a name="p15531114325914"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p853513432597"><a name="p853513432597"></a><a name="p853513432597"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.2.4.1.3 "><p id="p1954364325913"><a name="p1954364325913"></a><a name="p1954364325913"></a>Specifies the time (UTC) when the subnet pool rule is updated.</p>
<p id="p1876431451910"><a name="p1876431451910"></a><a name="p1876431451910"></a>Format: <em id="i13677855124417"><a name="i13677855124417"></a><a name="i13677855124417"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row1796820448610"><td class="cellrowborder" valign="top" width="24.33%" headers="mcps1.2.4.1.1 "><p id="p296834417616"><a name="p296834417616"></a><a name="p296834417616"></a>prefixes</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p209681244961"><a name="p209681244961"></a><a name="p209681244961"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.2.4.1.3 "><p id="p1496884418618"><a name="p1496884418618"></a><a name="p1496884418618"></a>Specifies a list of subnet prefixes that are assigned to the subnet pool. The adjacent prefixes are merged and treated as a single prefix. Each subnet prefix must be unique.</p>
</td>
</tr>
<tr id="row14968744267"><td class="cellrowborder" valign="top" width="24.33%" headers="mcps1.2.4.1.1 "><p id="p199681944763"><a name="p199681944763"></a><a name="p199681944763"></a>min_prefixlen</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p49682044566"><a name="p49682044566"></a><a name="p49682044566"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.2.4.1.3 "><p id="p397084410616"><a name="p397084410616"></a><a name="p397084410616"></a>Specifies the minimum prefix that can be allocated from the subnet pool.</p>
</td>
</tr>
<tr id="row22360302105653"><td class="cellrowborder" valign="top" width="24.33%" headers="mcps1.2.4.1.1 "><p id="p1404384110577"><a name="p1404384110577"></a><a name="p1404384110577"></a>address_scope_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p930111615640"><a name="p930111615640"></a><a name="p930111615640"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.2.4.1.3 "><p id="p2924364410577"><a name="p2924364410577"></a><a name="p2924364410577"></a>Specifies the ID of the address range allocated to the subnet pool.</p>
<p id="p62544866102532"><a name="p62544866102532"></a><a name="p62544866102532"></a>Only the administrator can specify this attribute.</p>
</td>
</tr>
<tr id="row1597013444615"><td class="cellrowborder" valign="top" width="24.33%" headers="mcps1.2.4.1.1 "><p id="p19970184415616"><a name="p19970184415616"></a><a name="p19970184415616"></a>shared</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p597044417614"><a name="p597044417614"></a><a name="p597044417614"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.2.4.1.3 "><p id="p159708444612"><a name="p159708444612"></a><a name="p159708444612"></a>Specifies whether the network can be shared to all projects. </p>
</td>
</tr>
<tr id="row99704441966"><td class="cellrowborder" valign="top" width="24.33%" headers="mcps1.2.4.1.1 "><p id="p3970744162"><a name="p3970744162"></a><a name="p3970744162"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p597014415620"><a name="p597014415620"></a><a name="p597014415620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.2.4.1.3 "><p id="p03241213320"><a name="p03241213320"></a><a name="p03241213320"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row139702441463"><td class="cellrowborder" valign="top" width="24.33%" headers="mcps1.2.4.1.1 "><p id="p4970154418614"><a name="p4970154418614"></a><a name="p4970154418614"></a>default_prefixlen</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p397018441063"><a name="p397018441063"></a><a name="p397018441063"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.2.4.1.3 "><p id="p3970044567"><a name="p3970044567"></a><a name="p3970044567"></a>Specifies the length of the prefix to allocate when the CIDR or prefixlen attributes are omitted when creating a subnet.</p>
</td>
</tr>
<tr id="row197118445620"><td class="cellrowborder" valign="top" width="24.33%" headers="mcps1.2.4.1.1 "><p id="p1297110441967"><a name="p1297110441967"></a><a name="p1297110441967"></a>max_prefixlen</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p697184412610"><a name="p697184412610"></a><a name="p697184412610"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.2.4.1.3 "><p id="p497164414613"><a name="p497164414613"></a><a name="p497164414613"></a>Specifies the maximum prefix length that can be allocated from the subnet pool.</p>
</td>
</tr>
<tr id="row1597174413610"><td class="cellrowborder" valign="top" width="24.33%" headers="mcps1.2.4.1.1 "><p id="p397114441268"><a name="p397114441268"></a><a name="p397114441268"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p5971104410613"><a name="p5971104410613"></a><a name="p5971104410613"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.2.4.1.3 "><p id="p097164411616"><a name="p097164411616"></a><a name="p097164411616"></a>Provides supplementary information about the subnet pool.</p>
</td>
</tr>
<tr id="row129712441610"><td class="cellrowborder" valign="top" width="24.33%" headers="mcps1.2.4.1.1 "><p id="p1971174417613"><a name="p1971174417613"></a><a name="p1971174417613"></a>is_default</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p1597254413618"><a name="p1597254413618"></a><a name="p1597254413618"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.2.4.1.3 "><p id="p17972114418620"><a name="p17972114418620"></a><a name="p17972114418620"></a>Specifies whether this is the default subnet pool.</p>
</td>
</tr>
<tr id="row129724441264"><td class="cellrowborder" valign="top" width="24.33%" headers="mcps1.2.4.1.1 "><p id="p12972144415618"><a name="p12972144415618"></a><a name="p12972144415618"></a>revision_number</p>
</td>
<td class="cellrowborder" valign="top" width="20.03%" headers="mcps1.2.4.1.2 "><p id="p179721944765"><a name="p179721944765"></a><a name="p179721944765"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="55.64%" headers="mcps1.2.4.1.3 "><p id="p19724441061"><a name="p19724441061"></a><a name="p19724441061"></a>Specifies the revision number of the subnet pool.</p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section5055526711495"></a>

Example request

```
PUT https://{Endpoint}/v2.0/subnetpools/03f761e6-eee0-43fc-a921-8acf64c14988

{
    "subnetpool": {
        "name": "my-new-subnetpool-name",
        "prefixes": [
            "2001:db8::/64",
            "2001:db8:0:1::/64",
            "2001:db8:0:2::/64"
        ],
        "min_prefixlen": 64,
        "default_prefixlen": 64,
        "max_prefixlen": 64
    }
}
```

Example response

```
{
    "subnetpool": {
        "name": "my-new-subnetpool-name",
        "default_quota": null,
        "is_default": false,
        "project_id": "9fadcee8aa7c40cdb2114fff7d569c08",
        "tenant_id": "9fadcee8aa7c40cdb2114fff7d569c08",
        "prefixes": [
            "2001:db8::/63",
            "2001:db8:0:2::/64"
        ],
        "min_prefixlen": 64,
        "address_scope_id": null,
        "ip_version": 6,
        "shared": false,
        "default_prefixlen": 64,
        "id": "03f761e6-eee0-43fc-a921-8acf64c14988",
        "max_prefixlen": 64,
        "description": "",
        "revision_number": 2,
        "created_at": "2018-09-20T02:15:34",
        "updated_at": "2018-09-20T02:15:34"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

