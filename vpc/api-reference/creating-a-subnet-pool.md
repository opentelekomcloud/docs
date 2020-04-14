# Creating a Subnet Pool<a name="vpc_subnetpools_0001"></a>

## Function<a name="section54540374"></a>

This API is used to create a subnet pool.

## URI<a name="section21101319"></a>

POST /v2.0/subnetpools

## Request Message<a name="section31485239"></a>

**Table  1**  Request parameter

<a name="table26517876"></a>
<table><thead align="left"><tr id="row40476817"><th class="cellrowborder" valign="top" width="22.509999999999998%" id="mcps1.2.5.1.1"><p id="p57396781"><a name="p57396781"></a><a name="p57396781"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.700000000000001%" id="mcps1.2.5.1.2"><p id="p18627652"><a name="p18627652"></a><a name="p18627652"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="22.35%" id="mcps1.2.5.1.3"><p id="p32444864"><a name="p32444864"></a><a name="p32444864"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="41.44%" id="mcps1.2.5.1.4"><p id="p10788361"><a name="p10788361"></a><a name="p10788361"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1442054"><td class="cellrowborder" valign="top" width="22.509999999999998%" headers="mcps1.2.5.1.1 "><p id="p49697568"><a name="p49697568"></a><a name="p49697568"></a>subnetpool</p>
</td>
<td class="cellrowborder" valign="top" width="13.700000000000001%" headers="mcps1.2.5.1.2 "><p id="p66080062"><a name="p66080062"></a><a name="p66080062"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="22.35%" headers="mcps1.2.5.1.3 "><p id="p50884809"><a name="p50884809"></a><a name="p50884809"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="41.44%" headers="mcps1.2.5.1.4 "><p id="p19248251"><a name="p19248251"></a><a name="p19248251"></a>Specifies the subnet pool list. For details, see <a href="#table12211980105515">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2** **subnetpool**  objects

<a name="table12211980105515"></a>
<table><thead align="left"><tr id="row32722637105515"><th class="cellrowborder" valign="top" width="24.86%" id="mcps1.2.5.1.1"><p id="p60075710105815"><a name="p60075710105815"></a><a name="p60075710105815"></a><strong id="b136971748143716"><a name="b136971748143716"></a><a name="b136971748143716"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12.13%" id="mcps1.2.5.1.2"><p id="p15964952144115"><a name="p15964952144115"></a><a name="p15964952144115"></a><strong id="b204001849173713"><a name="b204001849173713"></a><a name="b204001849173713"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.86%" id="mcps1.2.5.1.3"><p id="p34294369105815"><a name="p34294369105815"></a><a name="p34294369105815"></a><strong id="b10280450153713"><a name="b10280450153713"></a><a name="b10280450153713"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="38.15%" id="mcps1.2.5.1.4"><p id="p25203839105815"><a name="p25203839105815"></a><a name="p25203839105815"></a><strong id="b593745043711"><a name="b593745043711"></a><a name="b593745043711"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row43081158105515"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p54833166105624"><a name="p54833166105624"></a><a name="p54833166105624"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p179641252184115"><a name="p179641252184115"></a><a name="p179641252184115"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.3 "><p id="p12301465105624"><a name="p12301465105624"></a><a name="p12301465105624"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.2.5.1.4 "><p id="p14797472105624"><a name="p14797472105624"></a><a name="p14797472105624"></a>Specifies the subnet pool name.</p>
</td>
</tr>
<tr id="row49397935105515"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p23027912105624"><a name="p23027912105624"></a><a name="p23027912105624"></a>default_quota</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p7964152134116"><a name="p7964152134116"></a><a name="p7964152134116"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.3 "><p id="p6099296144650"><a name="p6099296144650"></a><a name="p6099296144650"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.2.5.1.4 "><p id="p2365807714488"><a name="p2365807714488"></a><a name="p2365807714488"></a>Specifies the upper limit of the prefix space that can be allocated from the subnet pool to the subnet. For IPv4 subnet pools, default_quota is measured in units of /32. For IPv6 subnet pools, default_quota is measured in units of /64.</p>
</td>
</tr>
<tr id="row62757710105647"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p5097986810577"><a name="p5097986810577"></a><a name="p5097986810577"></a>prefixes</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p139641652184112"><a name="p139641652184112"></a><a name="p139641652184112"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.3 "><p id="p118841747111416"><a name="p118841747111416"></a><a name="p118841747111416"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.2.5.1.4 "><p id="p1242857210116"><a name="p1242857210116"></a><a name="p1242857210116"></a>Specifies a list of subnet prefixes that are assigned to the subnet pool. The adjacent prefixes are merged and treated as a single prefix. Each subnet prefix must be unique.</p>
</td>
</tr>
<tr id="row2545218105647"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p1395064410577"><a name="p1395064410577"></a><a name="p1395064410577"></a>min_prefixlen</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p7964552174112"><a name="p7964552174112"></a><a name="p7964552174112"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.3 "><p id="p5626034310577"><a name="p5626034310577"></a><a name="p5626034310577"></a>Integer</p>
<p id="p3658104710577"><a name="p3658104710577"></a><a name="p3658104710577"></a></p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.2.5.1.4 "><p id="p3725182415446"><a name="p3725182415446"></a><a name="p3725182415446"></a>Specifies the minimum prefix that can be allocated from the subnet pool.</p>
<p id="p37814568346"><a name="p37814568346"></a><a name="p37814568346"></a>Instructions:</p>
<p id="p15995203519"><a name="p15995203519"></a><a name="p15995203519"></a>min_prefixlen =&lt; default_prefixlen =&lt; max_prefixlen</p>
</td>
</tr>
<tr id="row21625046105653"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p4495318510577"><a name="p4495318510577"></a><a name="p4495318510577"></a>default_prefixlen</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p39641652114112"><a name="p39641652114112"></a><a name="p39641652114112"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.3 "><p id="p1732939410577"><a name="p1732939410577"></a><a name="p1732939410577"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.2.5.1.4 "><p id="p5482176910577"><a name="p5482176910577"></a><a name="p5482176910577"></a>Specifies the length of the prefix to allocate when the CIDR or prefixlen attributes are omitted when creating a subnet.</p>
<p id="p195431012103514"><a name="p195431012103514"></a><a name="p195431012103514"></a>Instructions:</p>
<p id="p45431512133516"><a name="p45431512133516"></a><a name="p45431512133516"></a>min_prefixlen =&lt; default_prefixlen =&lt; max_prefixlen</p>
</td>
</tr>
<tr id="row18053024151048"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p53008854151048"><a name="p53008854151048"></a><a name="p53008854151048"></a>max_prefixlen</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p1796525214415"><a name="p1796525214415"></a><a name="p1796525214415"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.3 "><p id="p65858788151048"><a name="p65858788151048"></a><a name="p65858788151048"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.2.5.1.4 "><p id="p14908979151048"><a name="p14908979151048"></a><a name="p14908979151048"></a>Specifies the maximum prefix length that can be allocated from the subnet pool.</p>
<p id="p757517149356"><a name="p757517149356"></a><a name="p757517149356"></a>Instructions:</p>
<p id="p135753142358"><a name="p135753142358"></a><a name="p135753142358"></a>min_prefixlen =&lt; default_prefixlen =&lt; max_prefixlen</p>
</td>
</tr>
<tr id="row8351286151053"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p5365552151053"><a name="p5365552151053"></a><a name="p5365552151053"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p129651752124116"><a name="p129651752124116"></a><a name="p129651752124116"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.3 "><p id="p31956587151053"><a name="p31956587151053"></a><a name="p31956587151053"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.2.5.1.4 "><p id="p28387452151053"><a name="p28387452151053"></a><a name="p28387452151053"></a>Provides supplementary information about the subnet pool.</p>
</td>
</tr>
<tr id="row3921595115167"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p2237545215167"><a name="p2237545215167"></a><a name="p2237545215167"></a>is_default</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p89651952104117"><a name="p89651952104117"></a><a name="p89651952104117"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.3 "><p id="p47230515167"><a name="p47230515167"></a><a name="p47230515167"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.2.5.1.4 "><p id="p4334828415167"><a name="p4334828415167"></a><a name="p4334828415167"></a>Specifies whether this is the default subnet pool.</p>
</td>
</tr>
<tr id="row21006459151647"><td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.1 "><p id="p23801595151647"><a name="p23801595151647"></a><a name="p23801595151647"></a>revision_number</p>
</td>
<td class="cellrowborder" valign="top" width="12.13%" headers="mcps1.2.5.1.2 "><p id="p10965195219417"><a name="p10965195219417"></a><a name="p10965195219417"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="24.86%" headers="mcps1.2.5.1.3 "><p id="p48881052151647"><a name="p48881052151647"></a><a name="p48881052151647"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="38.15%" headers="mcps1.2.5.1.4 "><p id="p59981829151647"><a name="p59981829151647"></a><a name="p59981829151647"></a>Specifies the revision number of the subnet pool.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="section14931696"></a>

**Table  3**  Response parameter

<a name="table31929956"></a>
<table><thead align="left"><tr id="row12454319"><th class="cellrowborder" valign="top" width="23.810000000000002%" id="mcps1.2.4.1.1"><p id="p2166929"><a name="p2166929"></a><a name="p2166929"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.89%" id="mcps1.2.4.1.2"><p id="p41303584"><a name="p41303584"></a><a name="p41303584"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.3%" id="mcps1.2.4.1.3"><p id="p7224675"><a name="p7224675"></a><a name="p7224675"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row48327783"><td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.2.4.1.1 "><p id="p22236344"><a name="p22236344"></a><a name="p22236344"></a>subnetpool</p>
</td>
<td class="cellrowborder" valign="top" width="19.89%" headers="mcps1.2.4.1.2 "><p id="p56313405"><a name="p56313405"></a><a name="p56313405"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="56.3%" headers="mcps1.2.4.1.3 "><p id="p37955333"><a name="p37955333"></a><a name="p37955333"></a>Specifies the subnet pool list. For details, see <a href="#table149662441462">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **subnetpool**  objects

<a name="table149662441462"></a>
<table><thead align="left"><tr id="row496617442612"><th class="cellrowborder" valign="top" width="28.29%" id="mcps1.2.4.1.1"><p id="p1596613445611"><a name="p1596613445611"></a><a name="p1596613445611"></a><strong id="b137320516546"><a name="b137320516546"></a><a name="b137320516546"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.29%" id="mcps1.2.4.1.2"><p id="p49667449616"><a name="p49667449616"></a><a name="p49667449616"></a><strong id="b131642052205413"><a name="b131642052205413"></a><a name="b131642052205413"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.2.4.1.3"><p id="p8966144413616"><a name="p8966144413616"></a><a name="p8966144413616"></a><strong id="b1594318521541"><a name="b1594318521541"></a><a name="b1594318521541"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row28303131105515"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p2014344105614"><a name="p2014344105614"></a><a name="p2014344105614"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.2 "><p id="p28944191105614"><a name="p28944191105614"></a><a name="p28944191105614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.4.1.3 "><p id="p53796361105614"><a name="p53796361105614"></a><a name="p53796361105614"></a>Specifies the subnet pool ID.</p>
<p id="p1089535311426"><a name="p1089535311426"></a><a name="p1089535311426"></a>This parameter is not mandatory when you query subnet pools.</p>
</td>
</tr>
<tr id="row1196634410618"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p696615445611"><a name="p696615445611"></a><a name="p696615445611"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.2 "><p id="p3966104412620"><a name="p3966104412620"></a><a name="p3966104412620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.4.1.3 "><p id="p89666442613"><a name="p89666442613"></a><a name="p89666442613"></a>Specifies the subnet pool name.</p>
</td>
</tr>
<tr id="row9772661105515"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p49939441105624"><a name="p49939441105624"></a><a name="p49939441105624"></a>ip_version</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.2 "><p id="p18562940105624"><a name="p18562940105624"></a><a name="p18562940105624"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.4.1.3 "><p id="p682749310257"><a name="p682749310257"></a><a name="p682749310257"></a>Specifies the IP address version.</p>
<p id="p33352482102727"><a name="p33352482102727"></a><a name="p33352482102727"></a>Only IPv4 address is supported.</p>
</td>
</tr>
<tr id="row89665441569"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p79664442613"><a name="p79664442613"></a><a name="p79664442613"></a>default_quota</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.2 "><p id="p496616449616"><a name="p496616449616"></a><a name="p496616449616"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.4.1.3 "><p id="p7968244361"><a name="p7968244361"></a><a name="p7968244361"></a>Specifies the upper limit of the prefix space that can be allocated from the subnet pool to the subnet. For IPv4 subnet pools, default_quota is measured in units of /32. For IPv6 subnet pools, default_quota is measured in units of /64.</p>
</td>
</tr>
<tr id="row157121839115912"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p870051413911"><a name="p870051413911"></a><a name="p870051413911"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.2 "><p id="p15700614790"><a name="p15700614790"></a><a name="p15700614790"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row2067783695917"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p11508184345913"><a name="p11508184345913"></a><a name="p11508184345913"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.2 "><p id="p1651534311599"><a name="p1651534311599"></a><a name="p1651534311599"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.4.1.3 "><p id="p552334314592"><a name="p552334314592"></a><a name="p552334314592"></a>Specifies the time (UTC) when the subnet pool is created.</p>
<p id="p65980291419"><a name="p65980291419"></a><a name="p65980291419"></a>Format: <em id="i134613016619"><a name="i134613016619"></a><a name="i134613016619"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row1428916334597"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p15531114325914"><a name="p15531114325914"></a><a name="p15531114325914"></a>updated_at</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.2 "><p id="p853513432597"><a name="p853513432597"></a><a name="p853513432597"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.4.1.3 "><p id="p1954364325913"><a name="p1954364325913"></a><a name="p1954364325913"></a>Specifies the time (UTC) when the subnet pool rule is updated.</p>
<p id="p04198487169"><a name="p04198487169"></a><a name="p04198487169"></a>Format: <em id="i103381752814"><a name="i103381752814"></a><a name="i103381752814"></a>yyyy-MM-ddTHH:mm:ss</em></p>
</td>
</tr>
<tr id="row1796820448610"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p296834417616"><a name="p296834417616"></a><a name="p296834417616"></a>prefixes</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.2 "><p id="p209681244961"><a name="p209681244961"></a><a name="p209681244961"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.4.1.3 "><p id="p1496884418618"><a name="p1496884418618"></a><a name="p1496884418618"></a>Specifies a list of subnet prefixes that are assigned to the subnet pool. The adjacent prefixes are merged and treated as a single prefix. Each subnet prefix must be unique.</p>
</td>
</tr>
<tr id="row14968744267"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p199681944763"><a name="p199681944763"></a><a name="p199681944763"></a>min_prefixlen</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.2 "><p id="p49682044566"><a name="p49682044566"></a><a name="p49682044566"></a>Integer</p>
<p id="p896894413611"><a name="p896894413611"></a><a name="p896894413611"></a></p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.4.1.3 "><p id="p397084410616"><a name="p397084410616"></a><a name="p397084410616"></a>Specifies the minimum prefix that can be allocated from the subnet pool.</p>
</td>
</tr>
<tr id="row22360302105653"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p1404384110577"><a name="p1404384110577"></a><a name="p1404384110577"></a>address_scope_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.2 "><p id="p930111615640"><a name="p930111615640"></a><a name="p930111615640"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.4.1.3 "><p id="p2924364410577"><a name="p2924364410577"></a><a name="p2924364410577"></a>Specifies the ID of the address range allocated to the subnet pool.</p>
<p id="p62544866102532"><a name="p62544866102532"></a><a name="p62544866102532"></a>Only the administrator can specify this attribute.</p>
</td>
</tr>
<tr id="row1597013444615"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p19970184415616"><a name="p19970184415616"></a><a name="p19970184415616"></a>shared</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.2 "><p id="p597044417614"><a name="p597044417614"></a><a name="p597044417614"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.4.1.3 "><p id="p159708444612"><a name="p159708444612"></a><a name="p159708444612"></a>Specifies whether the network can be shared to all projects. </p>
</td>
</tr>
<tr id="row99704441966"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p3970744162"><a name="p3970744162"></a><a name="p3970744162"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.2 "><p id="p597014415620"><a name="p597014415620"></a><a name="p597014415620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.4.1.3 "><p id="p534413014313"><a name="p534413014313"></a><a name="p534413014313"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row139702441463"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p4970154418614"><a name="p4970154418614"></a><a name="p4970154418614"></a>default_prefixlen</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.2 "><p id="p397018441063"><a name="p397018441063"></a><a name="p397018441063"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.4.1.3 "><p id="p3970044567"><a name="p3970044567"></a><a name="p3970044567"></a>Specifies the length of the prefix to allocate when the CIDR or prefixlen attributes are omitted when creating a subnet.</p>
</td>
</tr>
<tr id="row197118445620"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p1297110441967"><a name="p1297110441967"></a><a name="p1297110441967"></a>max_prefixlen</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.2 "><p id="p697184412610"><a name="p697184412610"></a><a name="p697184412610"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.4.1.3 "><p id="p497164414613"><a name="p497164414613"></a><a name="p497164414613"></a>Specifies the maximum prefix length that can be allocated from the subnet pool.</p>
</td>
</tr>
<tr id="row1597174413610"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p397114441268"><a name="p397114441268"></a><a name="p397114441268"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.2 "><p id="p5971104410613"><a name="p5971104410613"></a><a name="p5971104410613"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.4.1.3 "><p id="p097164411616"><a name="p097164411616"></a><a name="p097164411616"></a>Provides supplementary information about the subnet pool.</p>
</td>
</tr>
<tr id="row129712441610"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p1971174417613"><a name="p1971174417613"></a><a name="p1971174417613"></a>is_default</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.2 "><p id="p1597254413618"><a name="p1597254413618"></a><a name="p1597254413618"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.4.1.3 "><p id="p17972114418620"><a name="p17972114418620"></a><a name="p17972114418620"></a>Specifies whether this is the default subnet pool.</p>
</td>
</tr>
<tr id="row129724441264"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p12972144415618"><a name="p12972144415618"></a><a name="p12972144415618"></a>revision_number</p>
</td>
<td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.2 "><p id="p179721944765"><a name="p179721944765"></a><a name="p179721944765"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.2.4.1.3 "><p id="p19724441061"><a name="p19724441061"></a><a name="p19724441061"></a>Specifies the revision number of the subnet pool.</p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section38241653113834"></a>

Example request

```
POST https://{Endpoint}/v2.0/subnetpools

{
    "subnetpool": {
        "name": "my-subnet-pool",
        "prefixes": [
            "192.168.0.0/16",
            "10.10.0.0/21"
        ],
        "default_prefixlen": 25,
        "min_prefixlen": 24,
        "max_prefixlen": 30,
        "shared": false
    }
}
```

Example response

```
{
    "subnetpool": {
        "address_scope_id": null,
        "default_prefixlen": 25,
        "default_quota": null,
        "description": "",
        "id": "f49a1319-423a-4ee6-ba54-1d95a4f6cc68",
        "ip_version": 4,
        "is_default": false,
        "max_prefixlen": 30,
        "min_prefixlen": 24,
        "name": "my-subnet-pool",
        "prefixes": [
            "10.10.0.0/21",
            "192.168.0.0/16"
        ],
        "project_id": "9fadcee8aa7c40cdb2114fff7d569c08",
        "revision_number": 1,
        "shared": false,
        "tenant_id": "9fadcee8aa7c40cdb2114fff7d569c08",
        "created_at": "2018-09-20T02:15:34",
        "updated_at": "2018-09-20T02:15:34"
    }
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

