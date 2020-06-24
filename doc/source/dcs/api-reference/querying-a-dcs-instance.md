# Querying a DCS Instance<a name="EN-US_TOPIC_0237964386"></a>

## Function<a name="section13385627"></a>

This API is used to query the details about a specified DCS instance.

## URI<a name="section53361782"></a>

-   URI format:

    GET /v1.0/\{project\_id\}/instances/\{instance\_id\}

-   Parameter description:

    [Table 1](#table43643771)  describes the parameters of this API.


**Table  1**  Parameter description

<a name="table43643771"></a>
<table><thead align="left"><tr id="row18091079"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p56091274"><a name="p56091274"></a><a name="p56091274"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p47099317"><a name="p47099317"></a><a name="p47099317"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p56948337"><a name="p56948337"></a><a name="p56948337"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p49412581"><a name="p49412581"></a><a name="p49412581"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row42996154"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p60136472"><a name="p60136472"></a><a name="p60136472"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p39216038"><a name="p39216038"></a><a name="p39216038"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p22382476"><a name="p22382476"></a><a name="p22382476"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1041267"><a name="p1041267"></a><a name="p1041267"></a>Project ID.</p>
</td>
</tr>
<tr id="row9371406"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p20886425"><a name="p20886425"></a><a name="p20886425"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p14078840"><a name="p14078840"></a><a name="p14078840"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p66644244"><a name="p66644244"></a><a name="p66644244"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p29474644"><a name="p29474644"></a><a name="p29474644"></a>DCS instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section10493992"></a>

None.

## Response<a name="section27337066"></a>

-   Status code:

    If status code "200 OK" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    [Table 2](#ref478561811)  describes the response parameters.


**Table  2**  Parameter description

<a name="ref478561811"></a>
<table><thead align="left"><tr id="row13679496"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p34297357"><a name="p34297357"></a><a name="p34297357"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="p26622510"><a name="p26622510"></a><a name="p26622510"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="62%" id="mcps1.2.4.1.3"><p id="p8939733"><a name="p8939733"></a><a name="p8939733"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53029735"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p441294"><a name="p441294"></a><a name="p441294"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p35744882"><a name="p35744882"></a><a name="p35744882"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p9654330"><a name="p9654330"></a><a name="p9654330"></a>DCS instance name.</p>
</td>
</tr>
<tr id="row19780111"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p58685193"><a name="p58685193"></a><a name="p58685193"></a>engine</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p55880220"><a name="p55880220"></a><a name="p55880220"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p30003951"><a name="p30003951"></a><a name="p30003951"></a>Cache engine.</p>
</td>
</tr>
<tr id="row1600104"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p62499582"><a name="p62499582"></a><a name="p62499582"></a>capacity</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p29301418"><a name="p29301418"></a><a name="p29301418"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p24604625"><a name="p24604625"></a><a name="p24604625"></a>Cache capacity.</p>
<p id="p20115039"><a name="p20115039"></a><a name="p20115039"></a>Unit: GB.</p>
</td>
</tr>
<tr id="row46817629"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p34131638"><a name="p34131638"></a><a name="p34131638"></a>ip</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p13199299"><a name="p13199299"></a><a name="p13199299"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p62510317"><a name="p62510317"></a><a name="p62510317"></a>Cache node's IP address in tenant's VPC.</p>
</td>
</tr>
<tr id="row25721944"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p3102711"><a name="p3102711"></a><a name="p3102711"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p49993063"><a name="p49993063"></a><a name="p49993063"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p22906320"><a name="p22906320"></a><a name="p22906320"></a>Port of the cache node.</p>
</td>
</tr>
<tr id="row4830289"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p55709089"><a name="p55709089"></a><a name="p55709089"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p16142333"><a name="p16142333"></a><a name="p16142333"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p32460622"><a name="p32460622"></a><a name="p32460622"></a>Cache instance status. For details about status, see <a href="dcs-instance-statuses.md">DCS Instance Statuses</a>.</p>
</td>
</tr>
<tr id="row12064764"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p37721838"><a name="p37721838"></a><a name="p37721838"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p35570061"><a name="p35570061"></a><a name="p35570061"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p62602688"><a name="p62602688"></a><a name="p62602688"></a>Brief description of the DCS instance.</p>
</td>
</tr>
<tr id="row26553285"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p3332466"><a name="p3332466"></a><a name="p3332466"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p1494311"><a name="p1494311"></a><a name="p1494311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p53930381"><a name="p53930381"></a><a name="p53930381"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row15611386"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p56562731"><a name="p56562731"></a><a name="p56562731"></a>resource_spec_code</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p18178530"><a name="p18178530"></a><a name="p18178530"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p63174788"><a name="p63174788"></a><a name="p63174788"></a>Resource specifications.</p>
<a name="ul31702186"></a><a name="ul31702186"></a><ul id="ul31702186"><li><strong id="b17740250"><a name="b17740250"></a><a name="b17740250"></a>dcs.single_node</strong>: indicates a DCS instance in single-node mode.</li><li><strong id="b27674155"><a name="b27674155"></a><a name="b27674155"></a>dcs.master_standby</strong>: indicates a DCS instance in master/standby mode.</li><li><strong id="b27014084"><a name="b27014084"></a><a name="b27014084"></a>dcs.cluster</strong>: indicates a DCS instance in cluster mode.</li></ul>
</td>
</tr>
<tr id="row41800172"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p30370757"><a name="p30370757"></a><a name="p30370757"></a>engine_version</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p44112251"><a name="p44112251"></a><a name="p44112251"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p16322549"><a name="p16322549"></a><a name="p16322549"></a>Cache engine version.</p>
</td>
</tr>
<tr id="row12685215"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p20869499"><a name="p20869499"></a><a name="p20869499"></a>internal_version</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p12707855"><a name="p12707855"></a><a name="p12707855"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p22703364"><a name="p22703364"></a><a name="p22703364"></a>Internal DCS version.</p>
</td>
</tr>
<tr id="row3003690"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p41972371"><a name="p41972371"></a><a name="p41972371"></a>charging_mode</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p44318896"><a name="p44318896"></a><a name="p44318896"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p33060842"><a name="p33060842"></a><a name="p33060842"></a>Billing mode.</p>
<p id="p29112125"><a name="p29112125"></a><a name="p29112125"></a><strong id="b60682536"><a name="b60682536"></a><a name="b60682536"></a>0</strong> indicates that users pay only for what they use.</p>
</td>
</tr>
<tr id="row9271916"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p12827756"><a name="p12827756"></a><a name="p12827756"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p32415333"><a name="p32415333"></a><a name="p32415333"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p8396286"><a name="p8396286"></a><a name="p8396286"></a>VPC ID.</p>
</td>
</tr>
<tr id="row8457710"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p13985882"><a name="p13985882"></a><a name="p13985882"></a>vpc_name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p59114683"><a name="p59114683"></a><a name="p59114683"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p23560057"><a name="p23560057"></a><a name="p23560057"></a>VPC name.</p>
</td>
</tr>
<tr id="row10713926"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p62521690"><a name="p62521690"></a><a name="p62521690"></a>created_at</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p31092093"><a name="p31092093"></a><a name="p31092093"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p35431642"><a name="p35431642"></a><a name="p35431642"></a>Time at which the DCS instance is created.</p>
<p id="p50449325"><a name="p50449325"></a><a name="p50449325"></a>For example, 2017-03-31<strong id="b51390743"><a name="b51390743"></a><a name="b51390743"></a>T</strong>12:24:46.297<strong id="b59863505"><a name="b59863505"></a><a name="b59863505"></a>Z</strong>.</p>
</td>
</tr>
<tr id="row1900636"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p19733842"><a name="p19733842"></a><a name="p19733842"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p54937376"><a name="p54937376"></a><a name="p54937376"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p20742511"><a name="p20742511"></a><a name="p20742511"></a>Error code returned when the DCS instance fails to be created or is in abnormal status.</p>
<p id="p52464879"><a name="p52464879"></a><a name="p52464879"></a>For details about error codes, see <a href="#table45484537">Table 3</a>.</p>
</td>
</tr>
<tr id="row21796769"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p20707880"><a name="p20707880"></a><a name="p20707880"></a>product_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p66725612"><a name="p66725612"></a><a name="p66725612"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p36065492"><a name="p36065492"></a><a name="p36065492"></a>Product ID used to differentiate DCS instance types.</p>
<a name="ul56153977"></a><a name="ul56153977"></a><ul id="ul56153977"><li>OTC_DCS_SINGLE: indicates a single-node DCS instance.</li><li>OTC_DCS_MS: indicates a master/standby DCS instance.</li><li>OTC_DCS_CL: indicates a DCS instance in cluster mode.</li></ul>
</td>
</tr>
<tr id="row65694662"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p19667385"><a name="p19667385"></a><a name="p19667385"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p49554324"><a name="p49554324"></a><a name="p49554324"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p54477312"><a name="p54477312"></a><a name="p54477312"></a>Security group ID.</p>
</td>
</tr>
<tr id="row20533764"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p52622155"><a name="p52622155"></a><a name="p52622155"></a>security_group_name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p34536183"><a name="p34536183"></a><a name="p34536183"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p45967472"><a name="p45967472"></a><a name="p45967472"></a>Security group name.</p>
</td>
</tr>
<tr id="row11054069"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p22964363"><a name="p22964363"></a><a name="p22964363"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p48174114"><a name="p48174114"></a><a name="p48174114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p9789153"><a name="p9789153"></a><a name="p9789153"></a>Subnet ID.</p>
</td>
</tr>
<tr id="row20993520"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p22753535"><a name="p22753535"></a><a name="p22753535"></a>subnet_name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p31097035"><a name="p31097035"></a><a name="p31097035"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p35831867"><a name="p35831867"></a><a name="p35831867"></a>Subnet name.</p>
</td>
</tr>
<tr id="row54051348"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p16083062"><a name="p16083062"></a><a name="p16083062"></a>subnet_cidr</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p27659632"><a name="p27659632"></a><a name="p27659632"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p25837739"><a name="p25837739"></a><a name="p25837739"></a>Subnet segment.</p>
</td>
</tr>
<tr id="row31213064"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p45230279"><a name="p45230279"></a><a name="p45230279"></a>available_zones</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p39773978"><a name="p39773978"></a><a name="p39773978"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p466794"><a name="p466794"></a><a name="p466794"></a>AZ where a cache node resides.</p>
<p id="p4201148"><a name="p4201148"></a><a name="p4201148"></a>The value of this parameter in the response contains an AZ ID.</p>
</td>
</tr>
<tr id="row37810334"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p42738207"><a name="p42738207"></a><a name="p42738207"></a>max_memory</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p39242708"><a name="p39242708"></a><a name="p39242708"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p24542757"><a name="p24542757"></a><a name="p24542757"></a>Overall memory size.</p>
<p id="p19558228"><a name="p19558228"></a><a name="p19558228"></a>Unit: MB.</p>
</td>
</tr>
<tr id="row41806332"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p30869694"><a name="p30869694"></a><a name="p30869694"></a>used_memory</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p17417301"><a name="p17417301"></a><a name="p17417301"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p1515305"><a name="p1515305"></a><a name="p1515305"></a>Size of the used memory.</p>
<p id="p13637749"><a name="p13637749"></a><a name="p13637749"></a>Unit: MB.</p>
</td>
</tr>
<tr id="row55630881"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p9807526"><a name="p9807526"></a><a name="p9807526"></a>instance_backup_policy</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p56212127"><a name="p56212127"></a><a name="p56212127"></a>JSON</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p56888437"><a name="p56888437"></a><a name="p56888437"></a>Backup policy.</p>
<p id="p42233886"><a name="p42233886"></a><a name="p42233886"></a>This parameter is available for master/standby DCS instances. For details, see <a href="creating-a-dcs-instance.md#table17319656205111">Table 3</a> and <a href="creating-a-dcs-instance.md#table1322175615513">Table 4</a>.</p>
</td>
</tr>
<tr id="row52643285"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p36247729"><a name="p36247729"></a><a name="p36247729"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p50384904"><a name="p50384904"></a><a name="p50384904"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p54645444"><a name="p54645444"></a><a name="p54645444"></a>User ID.</p>
</td>
</tr>
<tr id="row22046956"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p40972986"><a name="p40972986"></a><a name="p40972986"></a>user_name</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p30477536"><a name="p30477536"></a><a name="p30477536"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p52761351"><a name="p52761351"></a><a name="p52761351"></a>Username.</p>
</td>
</tr>
<tr id="row5090114"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p9646093"><a name="p9646093"></a><a name="p9646093"></a>order_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p43136044"><a name="p43136044"></a><a name="p43136044"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p4358664"><a name="p4358664"></a><a name="p4358664"></a>Order ID.</p>
<p id="p39227976"><a name="p39227976"></a><a name="p39227976"></a>An order ID is generated only in the monthly or yearly billing mode. In other billing modes, no value is returned for this parameter.</p>
</td>
</tr>
<tr id="row17507464"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p8818452"><a name="p8818452"></a><a name="p8818452"></a>maintain_begin</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p43206037"><a name="p43206037"></a><a name="p43206037"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p10028147"><a name="p10028147"></a><a name="p10028147"></a>Time at which the maintenance time window starts.</p>
<p id="p23144464"><a name="p23144464"></a><a name="p23144464"></a>Format: HH:mm:ss.</p>
</td>
</tr>
<tr id="row6973589"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p27989860"><a name="p27989860"></a><a name="p27989860"></a>maintain_end</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p52586183"><a name="p52586183"></a><a name="p52586183"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="p31622439"><a name="p31622439"></a><a name="p31622439"></a>Time at which the maintenance time window ends.</p>
<p id="p16166497"><a name="p16166497"></a><a name="p16166497"></a>Format: HH:mm:ss.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Error code description

<a name="table45484537"></a>
<table><thead align="left"><tr id="row15535650"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.3.1.1"><p id="p50428169"><a name="p50428169"></a><a name="p50428169"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="82%" id="mcps1.2.3.1.2"><p id="p58149851"><a name="p58149851"></a><a name="p58149851"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12517506"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p7285094"><a name="p7285094"></a><a name="p7285094"></a>dcs.01.0001</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p53221742"><a name="p53221742"></a><a name="p53221742"></a>Internal service error.</p>
</td>
</tr>
<tr id="row9233635"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p9727005"><a name="p9727005"></a><a name="p9727005"></a>dcs.01.0002</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p49689968"><a name="p49689968"></a><a name="p49689968"></a>Internal service error.</p>
</td>
</tr>
<tr id="row44556530"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p52309148"><a name="p52309148"></a><a name="p52309148"></a>dcs.01.0003</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p9182578"><a name="p9182578"></a><a name="p9182578"></a>Internal service error.</p>
</td>
</tr>
<tr id="row15534346"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p50322510"><a name="p50322510"></a><a name="p50322510"></a>dcs.02.0001</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p49591539"><a name="p49591539"></a><a name="p49591539"></a>Failed to create VPC.</p>
</td>
</tr>
<tr id="row43670673"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p47663658"><a name="p47663658"></a><a name="p47663658"></a>dcs.02.0002</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p35551095"><a name="p35551095"></a><a name="p35551095"></a>Failed to create VPC.</p>
</td>
</tr>
<tr id="row51524405"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p12727276"><a name="p12727276"></a><a name="p12727276"></a>dcs.02.0003</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p24276427"><a name="p24276427"></a><a name="p24276427"></a>Failed to create security group.</p>
</td>
</tr>
<tr id="row17161258"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p47884633"><a name="p47884633"></a><a name="p47884633"></a>dcs.02.0004</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p53450053"><a name="p53450053"></a><a name="p53450053"></a>Failed to create subnet.</p>
</td>
</tr>
<tr id="row11288429"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p41947518"><a name="p41947518"></a><a name="p41947518"></a>dcs.02.0005</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p42305792"><a name="p42305792"></a><a name="p42305792"></a>Subnet status abnormal.</p>
</td>
</tr>
<tr id="row45207810"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p37954032"><a name="p37954032"></a><a name="p37954032"></a>dcs.03.0001</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p54377762"><a name="p54377762"></a><a name="p54377762"></a>Failed to create ECS.</p>
</td>
</tr>
<tr id="row19637817"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p47159308"><a name="p47159308"></a><a name="p47159308"></a>dcs.03.0002</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p61807641"><a name="p61807641"></a><a name="p61807641"></a>Failed to create ECS.</p>
</td>
</tr>
<tr id="row19397860"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p27722808"><a name="p27722808"></a><a name="p27722808"></a>dcs.03.0003</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p30954969"><a name="p30954969"></a><a name="p30954969"></a>Failed to create ECS.</p>
</td>
</tr>
<tr id="row10159265"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p17594143"><a name="p17594143"></a><a name="p17594143"></a>dcs.03.0004</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p15839518"><a name="p15839518"></a><a name="p15839518"></a>Failed to create ECS.</p>
</td>
</tr>
<tr id="row8337942"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p4284664"><a name="p4284664"></a><a name="p4284664"></a>dcs.03.0005</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p11513519"><a name="p11513519"></a><a name="p11513519"></a>Failed to bind NIC to the ECS.</p>
</td>
</tr>
<tr id="row36512814"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p4747967"><a name="p4747967"></a><a name="p4747967"></a>dcs.03.0007</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p49041048"><a name="p49041048"></a><a name="p49041048"></a>Failed to start ECS.</p>
</td>
</tr>
<tr id="row38716256"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p49009017"><a name="p49009017"></a><a name="p49009017"></a>dcs.03.0008</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p10307439"><a name="p10307439"></a><a name="p10307439"></a>Failed to start ECS.</p>
</td>
</tr>
<tr id="row25658088"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p65039219"><a name="p65039219"></a><a name="p65039219"></a>dcs.03.0009</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p33685391"><a name="p33685391"></a><a name="p33685391"></a>Failed to stop ECS.</p>
</td>
</tr>
<tr id="row34733067"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p61915010"><a name="p61915010"></a><a name="p61915010"></a>dcs.04.0002</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p49059934"><a name="p49059934"></a><a name="p49059934"></a>Failed to deploy instance.</p>
</td>
</tr>
<tr id="row38886230"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p62776900"><a name="p62776900"></a><a name="p62776900"></a>dcs.04.0003</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p51764106"><a name="p51764106"></a><a name="p51764106"></a>Failed to connect to the instance.</p>
</td>
</tr>
<tr id="row63223774"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p20852060"><a name="p20852060"></a><a name="p20852060"></a>dcs.04.0004</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p11295303"><a name="p11295303"></a><a name="p11295303"></a>Both cache nodes are in the master state. A network connection error may occur between the master and standby nodes.</p>
</td>
</tr>
</tbody>
</table>

-   Example response:

    ```
    { 
     "name" : "dcs-a11e", 
     "engine" : "Redis", 
     "capacity" : 2, 
     "ip" : "192.168.3.100", 
     "port" : 6379, 
     "status" : "RUNNING", 
     "description" : "Create a instance", 
     "instance_id" : "68d5745e-6af2-40e4-945d-fe449be00148", 
     "resource_spec_code" : "dcs.single_node", 
     "engine_version" : "3.0.7", 
     "internal_version" : null, 
     "charging_mode" : 0, 
     "vpc_id" : "27d99e17-42f2-4751-818f-5c8c6c03ff15", 
     "vpc_name" : "vpc_4944a40e-ac57-4f08-9d38-9786e2759458_192", 
     "created_at" : "2017-03-31T12:24:46.297Z", 
     "error_code" : null, 
     "product_id" : "XXXXXX", 
     "security_group_id" : "60ea2db8-1a51-4ab6-9e11-65b418c24583", 
     "security_group_name" : "sg_6379_4944a40e-ac57-4f08-9d38-9786e2759458", 
     "subnet_id" : "ec2f34b9-20eb-4872-85bd-bea9fc943128", 
      "subnet_name" : "subnet_az_7f336767-10ec-48a5-9ae8-9cacde119318", 
     "available_zones" : "XXXXXX", 
     "max_memory" : 460, 
     "used_memory" : 56, 
     "user_id": "6d0977e4c9b74ae7b5a083a8d0d8fafa", 
     "user_name": "liutao02", 
     "order_id": "XXXXXXXXX", 
     "maintain_begin" : "22:00:00", 
     "maintain_end" : "02:00:00" 
    }
    ```


