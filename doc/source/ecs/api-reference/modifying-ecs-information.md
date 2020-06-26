# Modifying ECS Information<a name="EN-US_TOPIC_0020212692"></a>

## Function<a name="section15039321"></a>

This API is used to modify ECS information. Only the name and description of an ECS can be modified.

## URI<a name="section1136168"></a>

PUT /v2/\{project\_id\}/servers/\{server\_id\}

PUT /v2.1/\{project\_id\}/servers/\{server\_id\}

[Table 1](#table44564854)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table44564854"></a>
<table><thead align="left"><tr id="row553045"><th class="cellrowborder" valign="top" width="16.41%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.61%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.98%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10515475"><td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.4.1.1 "><p id="p46447150"><a name="p46447150"></a><a name="p46447150"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.4.1.2 "><p id="p4122781"><a name="p4122781"></a><a name="p4122781"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.98%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row26436338165316"><td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.4.1.1 "><p id="p31999978165316"><a name="p31999978165316"></a><a name="p31999978165316"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.61%" headers="mcps1.2.4.1.2 "><p id="p41861457165316"><a name="p41861457165316"></a><a name="p41861457165316"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.98%" headers="mcps1.2.4.1.3 "><p id="p35334819165316"><a name="p35334819165316"></a><a name="p35334819165316"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section10225512"></a>

[Table 2](#table13100926)  describes the request parameters.

**Table  2**  Request parameters

<a name="table13100926"></a>
<table><thead align="left"><tr id="row35303864"><th class="cellrowborder" valign="top" width="16.35%" id="mcps1.2.5.1.1"><p id="p41040744"><a name="p41040744"></a><a name="p41040744"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.48%" id="mcps1.2.5.1.2"><p id="p35965948"><a name="p35965948"></a><a name="p35965948"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.989999999999998%" id="mcps1.2.5.1.3"><p id="p27560669"><a name="p27560669"></a><a name="p27560669"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.18%" id="mcps1.2.5.1.4"><p id="p17821682"><a name="p17821682"></a><a name="p17821682"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row34270115"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.5.1.1 "><p id="p24415962"><a name="p24415962"></a><a name="p24415962"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.2 "><p id="p31535868"><a name="p31535868"></a><a name="p31535868"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.989999999999998%" headers="mcps1.2.5.1.3 "><p id="p4268531"><a name="p4268531"></a><a name="p4268531"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50.18%" headers="mcps1.2.5.1.4 "><p id="p24751971"><a name="p24751971"></a><a name="p24751971"></a>Specifies the ECS data structure. For details, see <a href="#table26827213163326">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **server**  field description

<a name="table26827213163326"></a>
<table><thead align="left"><tr id="row36672866163326"><th class="cellrowborder" valign="top" width="16.35%" id="mcps1.2.5.1.1"><p id="p128484161419"><a name="p128484161419"></a><a name="p128484161419"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.11%" id="mcps1.2.5.1.2"><p id="p98416417142"><a name="p98416417142"></a><a name="p98416417142"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.36%" id="mcps1.2.5.1.3"><p id="p118418421415"><a name="p118418421415"></a><a name="p118418421415"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.18%" id="mcps1.2.5.1.4"><p id="p010104141410"><a name="p010104141410"></a><a name="p010104141410"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row31760590163326"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.5.1.1 "><p id="p22470979163326"><a name="p22470979163326"></a><a name="p22470979163326"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.5.1.2 "><p id="p8210025163326"><a name="p8210025163326"></a><a name="p8210025163326"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.2.5.1.3 "><p id="p61032295163326"><a name="p61032295163326"></a><a name="p61032295163326"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.18%" headers="mcps1.2.5.1.4 "><p id="p66475806163326"><a name="p66475806163326"></a><a name="p66475806163326"></a>Specifies the name of the modified ECS.</p>
<p id="p56398165141344"><a name="p56398165141344"></a><a name="p56398165141344"></a>The length is greater than 0 and less than 256</p>
</td>
</tr>
<tr id="row1590615702514"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.5.1.1 "><p id="p185271320121118"><a name="p185271320121118"></a><a name="p185271320121118"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.5.1.2 "><p id="p75277203114"><a name="p75277203114"></a><a name="p75277203114"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.36%" headers="mcps1.2.5.1.3 "><p id="p195271620111110"><a name="p195271620111110"></a><a name="p195271620111110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.18%" headers="mcps1.2.5.1.4 "><p id="p165273207113"><a name="p165273207113"></a><a name="p165273207113"></a>Describes the ECS. The value contains a maximum of 255 bytes.</p>
<p id="p5471142121113"><a name="p5471142121113"></a><a name="p5471142121113"></a>This field is newly added in version 2.19.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section24920747"></a>

[Table 4](#table44736746)  describes the response parameters.

**Table  4**  Response parameters

<a name="table44736746"></a>
<table><thead align="left"><tr id="row8242429"><th class="cellrowborder" valign="top" width="16.6%" id="mcps1.2.4.1.1"><p id="p63657004"><a name="p63657004"></a><a name="p63657004"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.04%" id="mcps1.2.4.1.2"><p id="p35147813"><a name="p35147813"></a><a name="p35147813"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.36%" id="mcps1.2.4.1.3"><p id="p28400574"><a name="p28400574"></a><a name="p28400574"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18745119"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p41959665"><a name="p41959665"></a><a name="p41959665"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="16.04%" headers="mcps1.2.4.1.2 "><p id="p16804102"><a name="p16804102"></a><a name="p16804102"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="67.36%" headers="mcps1.2.4.1.3 "><p id="p36377578"><a name="p36377578"></a><a name="p36377578"></a>Specifies an ECS.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **server**  field description

<a name="table11253402"></a>
<table><thead align="left"><tr id="row10267559"><th class="cellrowborder" valign="top" width="16.470000000000002%" id="mcps1.2.4.1.1"><p id="p49911341191514"><a name="p49911341191514"></a><a name="p49911341191514"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.32%" id="mcps1.2.4.1.2"><p id="p157164271511"><a name="p157164271511"></a><a name="p157164271511"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.21000000000001%" id="mcps1.2.4.1.3"><p id="p187164216157"><a name="p187164216157"></a><a name="p187164216157"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15663"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p1268752"><a name="p1268752"></a><a name="p1268752"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p2786131"><a name="p2786131"></a><a name="p2786131"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p24350086"><a name="p24350086"></a><a name="p24350086"></a>Specifies the tenant or project ID.</p>
</td>
</tr>
<tr id="row17824184"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p34472770"><a name="p34472770"></a><a name="p34472770"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p18974148"><a name="p18974148"></a><a name="p18974148"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p1146019416233"><a name="p1146019416233"></a><a name="p1146019416233"></a>Specifies the image ID.</p>
</td>
</tr>
<tr id="row7727977"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p21986423"><a name="p21986423"></a><a name="p21986423"></a>accessIPv4</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p1266224310514"><a name="p1266224310514"></a><a name="p1266224310514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p449319209247"><a name="p449319209247"></a><a name="p449319209247"></a>Reserved</p>
</td>
</tr>
<tr id="row17881104563115"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p148814457312"><a name="p148814457312"></a><a name="p148814457312"></a>addresses</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p1830765712513"><a name="p1830765712513"></a><a name="p1830765712513"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p188114593120"><a name="p188114593120"></a><a name="p188114593120"></a>Specifies the network addresses of an ECS. For details, see <a href="#table3730161">Table 6</a>.</p>
</td>
</tr>
<tr id="row12379948143212"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p337954823220"><a name="p337954823220"></a><a name="p337954823220"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p53791648203212"><a name="p53791648203212"></a><a name="p53791648203212"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p12379154816322"><a name="p12379154816322"></a><a name="p12379154816322"></a>Specifies the ECS metadata.</p>
</td>
</tr>
<tr id="row157021310336"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p2070231193310"><a name="p2070231193310"></a><a name="p2070231193310"></a>accessIPv6</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p107026111331"><a name="p107026111331"></a><a name="p107026111331"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p2702610337"><a name="p2702610337"></a><a name="p2702610337"></a>Reserved</p>
</td>
</tr>
<tr id="row1357051111330"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p10571121123317"><a name="p10571121123317"></a><a name="p10571121123317"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p1057181153310"><a name="p1057181153310"></a><a name="p1057181153310"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p145717115334"><a name="p145717115334"></a><a name="p145717115334"></a>Specifies the time when the ECS was created. The time is in the format of "2019-05-22T03:19:19Z".</p>
</td>
</tr>
<tr id="row44021729173312"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p1040292913331"><a name="p1040292913331"></a><a name="p1040292913331"></a>hostId</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p7403122973316"><a name="p7403122973316"></a><a name="p7403122973316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p15403729103310"><a name="p15403729103310"></a><a name="p15403729103310"></a>Specifies the host ID of the ECS.</p>
</td>
</tr>
<tr id="row1687495133318"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p1874145116332"><a name="p1874145116332"></a><a name="p1874145116332"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p1834114812515"><a name="p1834114812515"></a><a name="p1834114812515"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p1487435113336"><a name="p1487435113336"></a><a name="p1487435113336"></a>Specifies the ECS flavor.</p>
</td>
</tr>
<tr id="row64807110488"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p248041174813"><a name="p248041174813"></a><a name="p248041174813"></a>OS-DCF:diskConfig</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p1848012164812"><a name="p1848012164812"></a><a name="p1848012164812"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p2048819204245"><a name="p2048819204245"></a><a name="p2048819204245"></a>Specifies the disk configuration mode. This is an extended attribute. This field is valid for the ECS started using an image.</p>
</td>
</tr>
<tr id="row1625113556487"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p1025111555484"><a name="p1025111555484"></a><a name="p1025111555484"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p125175594818"><a name="p125175594818"></a><a name="p125175594818"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p192511555114814"><a name="p192511555114814"></a><a name="p192511555114814"></a>Specifies the ID of the user to which an ECS belongs.</p>
</td>
</tr>
<tr id="row1696711163499"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p9968141624920"><a name="p9968141624920"></a><a name="p9968141624920"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p19968716144915"><a name="p19968716144915"></a><a name="p19968716144915"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p12968111615495"><a name="p12968111615495"></a><a name="p12968111615495"></a>Specifies the name of the modified ECS.</p>
</td>
</tr>
<tr id="row6518308499"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p13519301498"><a name="p13519301498"></a><a name="p13519301498"></a>progress</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p13523018490"><a name="p13523018490"></a><a name="p13523018490"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p15730134916"><a name="p15730134916"></a><a name="p15730134916"></a>Reserved</p>
</td>
</tr>
<tr id="row9985124116491"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p498534117495"><a name="p498534117495"></a><a name="p498534117495"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p35973707"><a name="p35973707"></a><a name="p35973707"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p169324165111"><a name="p169324165111"></a><a name="p169324165111"></a>Specifies ECS shortcut links. For details, see <a href="#table64121649">Table 9</a>.</p>
</td>
</tr>
<tr id="row1833531795016"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p3335417195015"><a name="p3335417195015"></a><a name="p3335417195015"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p93353179506"><a name="p93353179506"></a><a name="p93353179506"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p16335121765010"><a name="p16335121765010"></a><a name="p16335121765010"></a>Specifies the unique ID of an ECS.</p>
</td>
</tr>
<tr id="row19934421115017"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p1934192114503"><a name="p1934192114503"></a><a name="p1934192114503"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p5466712110"><a name="p5466712110"></a><a name="p5466712110"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p3934721115015"><a name="p3934721115015"></a><a name="p3934721115015"></a>Specifies the time when the ECS was updated last time.</p>
<p id="p79461929272"><a name="p79461929272"></a><a name="p79461929272"></a>The time is in the format of "2019-05-22T03:19:19Z".</p>
</td>
</tr>
<tr id="row43315475142"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p1253710242210"><a name="p1253710242210"></a><a name="p1253710242210"></a>locked</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p1653720241521"><a name="p1653720241521"></a><a name="p1653720241521"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p18537624422"><a name="p18537624422"></a><a name="p18537624422"></a>Specifies the ECS lock status, which is <strong id="b842352706142719"><a name="b842352706142719"></a><a name="b842352706142719"></a>True</strong> when the ECS is locked and <strong id="b842352706142722"><a name="b842352706142722"></a><a name="b842352706142722"></a>False</strong> when the ECS is unlocked.</p>
<p id="p13993454402"><a name="p13993454402"></a><a name="p13993454402"></a>This field is supported in microversions later than 2.9.</p>
</td>
</tr>
<tr id="row2806910181520"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972887_p57463526"><a name="en-us_topic_0057972887_p57463526"></a><a name="en-us_topic_0057972887_p57463526"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972887_p24034004"><a name="en-us_topic_0057972887_p24034004"></a><a name="en-us_topic_0057972887_p24034004"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972887_p48379233"><a name="en-us_topic_0057972887_p48379233"></a><a name="en-us_topic_0057972887_p48379233"></a>Specifies the description of the ECS.</p>
<p id="p28201545155518"><a name="p28201545155518"></a><a name="p28201545155518"></a>This field is supported in microversions later than 2.19.</p>
</td>
</tr>
<tr id="row8354844101514"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p749372082418"><a name="p749372082418"></a><a name="p749372082418"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p14493420142420"><a name="p14493420142420"></a><a name="p14493420142420"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p1620274611333"><a name="p1620274611333"></a><a name="p1620274611333"></a>Specifies ECS tags.</p>
<p id="p1149310203247"><a name="p1149310203247"></a><a name="p1149310203247"></a>This field is supported in microversions later than 2.26. If the microversion is not used for query, the response does not contain the <strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>tags</strong> field.</p>
<div class="p" id="p7300949059"><a name="p7300949059"></a><a name="p7300949059"></a>Tag functions have been upgraded on the public cloud. After the upgrade, the tag values returned by the system comply with the following rules:<a name="en-us_topic_0020212689_ul871515496611"></a><a name="en-us_topic_0020212689_ul871515496611"></a><ul id="en-us_topic_0020212689_ul871515496611"><li>The key and value of a tag are connected using an equal sign (=), for example, key=value.</li><li>If the value is empty, only the key is returned.</li></ul>
</div>
<a name="en-us_topic_0020212689_ul871515496611_1"></a><a name="en-us_topic_0020212689_ul871515496611_1"></a><ul id="en-us_topic_0020212689_ul871515496611_1"><li>The key and value of a tag are connected using an equal sign (=), for example, key=value.</li><li>If the value is empty, only the key is returned.</li></ul>
<p id="p141334271371"><a name="p141334271371"></a><a name="p141334271371"></a>For more details about upgraded tag functions, see <a href="tag-types(openstack).md">Tag Types</a>.</p>
</td>
</tr>
<tr id="row61813343508"><td class="cellrowborder" valign="top" width="16.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p131883455011"><a name="p131883455011"></a><a name="p131883455011"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="16.32%" headers="mcps1.2.4.1.2 "><p id="p518143415010"><a name="p518143415010"></a><a name="p518143415010"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.21000000000001%" headers="mcps1.2.4.1.3 "><p id="p2018153465013"><a name="p2018153465013"></a><a name="p2018153465013"></a>Specifies the ECS status.</p>
<p id="p3162102155817"><a name="p3162102155817"></a><a name="p3162102155817"></a>Options:</p>
<p id="p10449173112588"><a name="p10449173112588"></a><a name="p10449173112588"></a><strong id="b84235270614233"><a name="b84235270614233"></a><a name="b84235270614233"></a>ACTIVE</strong>, <strong id="b84235270614237"><a name="b84235270614237"></a><a name="b84235270614237"></a>BUILD</strong>, <strong id="b842352706142313"><a name="b842352706142313"></a><a name="b842352706142313"></a>ERROR</strong>, <strong id="b842352706142317"><a name="b842352706142317"></a><a name="b842352706142317"></a>HARD_REBOOT</strong>, <strong id="b842352706142321"><a name="b842352706142321"></a><a name="b842352706142321"></a>MIGRATING</strong>, <strong id="b842352706142326"><a name="b842352706142326"></a><a name="b842352706142326"></a>REBOOT</strong>, <strong id="b842352706142330"><a name="b842352706142330"></a><a name="b842352706142330"></a>RESIZE</strong>, <strong id="b842352706142333"><a name="b842352706142333"></a><a name="b842352706142333"></a>REVERT_RESIZE</strong>, <strong id="b842352706142337"><a name="b842352706142337"></a><a name="b842352706142337"></a>SHELVED</strong>, <strong id="b842352706142340"><a name="b842352706142340"></a><a name="b842352706142340"></a>SHELVED_OFFLOADED</strong>, <strong id="b842352706142345"><a name="b842352706142345"></a><a name="b842352706142345"></a>SHUTOFF</strong>, <strong id="b842352706142347"><a name="b842352706142347"></a><a name="b842352706142347"></a>UNKNOWN</strong>, and <strong id="b842352706142350"><a name="b842352706142350"></a><a name="b842352706142350"></a>VERIFY_RESIZE</strong></p>
<p id="p19518218542"><a name="p19518218542"></a><a name="p19518218542"></a>For details, see <a href="ecs-statuses.md">ECS Statuses</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **addresses**  field description

<a name="table3730161"></a>
<table><thead align="left"><tr id="row20014316"><th class="cellrowborder" valign="top" width="16.61%" id="mcps1.2.4.1.1"><p id="p1191618499157"><a name="p1191618499157"></a><a name="p1191618499157"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.04%" id="mcps1.2.4.1.2"><p id="p9916194916152"><a name="p9916194916152"></a><a name="p9916194916152"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.35%" id="mcps1.2.4.1.3"><p id="p391614915151"><a name="p391614915151"></a><a name="p391614915151"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row57432766"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.4.1.1 "><p id="p2057412833316"><a name="p2057412833316"></a><a name="p2057412833316"></a>Name of the network where the ECS accesses</p>
</td>
<td class="cellrowborder" valign="top" width="16.04%" headers="mcps1.2.4.1.2 "><p id="p4439518115623"><a name="p4439518115623"></a><a name="p4439518115623"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="67.35%" headers="mcps1.2.4.1.3 "><p id="p19891184119819"><a name="p19891184119819"></a><a name="p19891184119819"></a>Specifies the network information of the ECS.</p>
<a name="ul1197110522819"></a><a name="ul1197110522819"></a><ul id="ul1197110522819"><li><strong id="b842352706214237"><a name="b842352706214237"></a><a name="b842352706214237"></a>key</strong> indicates the network name, for example, <strong id="b842352706214248"><a name="b842352706214248"></a><a name="b842352706214248"></a>demo_net</strong>.</li><li><strong id="b84235270621435"><a name="b84235270621435"></a><a name="b84235270621435"></a>value</strong> indicates the detailed network information.</li></ul>
<p id="p204137567134"><a name="p204137567134"></a><a name="p204137567134"></a>For details, see <a href="#table1656029015527">Table 7</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  7**  Data structure of the network which an ECS accesses

<a name="table1656029015527"></a>
<table><thead align="left"><tr id="row2645284715527"><th class="cellrowborder" valign="top" width="16.57%" id="mcps1.2.4.1.1"><p id="p1986420536154"><a name="p1986420536154"></a><a name="p1986420536154"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.11%" id="mcps1.2.4.1.2"><p id="p148649536156"><a name="p148649536156"></a><a name="p148649536156"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.32000000000001%" id="mcps1.2.4.1.3"><p id="p486414537159"><a name="p486414537159"></a><a name="p486414537159"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row5009697415527"><td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.2.4.1.1 "><p id="p3132311415527"><a name="p3132311415527"></a><a name="p3132311415527"></a>addr</p>
</td>
<td class="cellrowborder" valign="top" width="16.11%" headers="mcps1.2.4.1.2 "><p id="p5414433915527"><a name="p5414433915527"></a><a name="p5414433915527"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p2361534415527"><a name="p2361534415527"></a><a name="p2361534415527"></a>Specifies the IP address.</p>
</td>
</tr>
<tr id="row1121151015527"><td class="cellrowborder" valign="top" width="16.57%" headers="mcps1.2.4.1.1 "><p id="p3571711715527"><a name="p3571711715527"></a><a name="p3571711715527"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="16.11%" headers="mcps1.2.4.1.2 "><p id="p740535615527"><a name="p740535615527"></a><a name="p740535615527"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67.32000000000001%" headers="mcps1.2.4.1.3 "><p id="p6296298815527"><a name="p6296298815527"></a><a name="p6296298815527"></a>Specifies the type of an IP address. The value of this parameter can be <strong id="b84235270614154"><a name="b84235270614154"></a><a name="b84235270614154"></a>4</strong> or <strong id="b842352706141510"><a name="b842352706141510"></a><a name="b842352706141510"></a>6</strong>.</p>
<a name="ul2979598615527"></a><a name="ul2979598615527"></a><ul id="ul2979598615527"><li><strong id="b84235270614151"><a name="b84235270614151"></a><a name="b84235270614151"></a>4</strong>: The type of the IP address is IPv4.</li><li><strong id="b842352706141518"><a name="b842352706141518"></a><a name="b842352706141518"></a>6</strong>: The type of the IP address is IPv6.</li></ul>
</td>
</tr>
</tbody>
</table>

**Table  8** **flavor**  field description

<a name="table19588408"></a>
<table><thead align="left"><tr id="row65668512"><th class="cellrowborder" valign="top" width="16.48%" id="mcps1.2.4.1.1"><p id="p445185741513"><a name="p445185741513"></a><a name="p445185741513"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.29%" id="mcps1.2.4.1.2"><p id="p6466185761518"><a name="p6466185761518"></a><a name="p6466185761518"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.23%" id="mcps1.2.4.1.3"><p id="p1546645715151"><a name="p1546645715151"></a><a name="p1546645715151"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row54114449"><td class="cellrowborder" valign="top" width="16.48%" headers="mcps1.2.4.1.1 "><p id="p21194271"><a name="p21194271"></a><a name="p21194271"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.2.4.1.2 "><p id="p6046963"><a name="p6046963"></a><a name="p6046963"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.23%" headers="mcps1.2.4.1.3 "><p id="p20041994"><a name="p20041994"></a><a name="p20041994"></a>Specifies the ECS ID.</p>
</td>
</tr>
<tr id="row46160221"><td class="cellrowborder" valign="top" width="16.48%" headers="mcps1.2.4.1.1 "><p id="p47990424"><a name="p47990424"></a><a name="p47990424"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.2.4.1.2 "><p id="p57492083"><a name="p57492083"></a><a name="p57492083"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="67.23%" headers="mcps1.2.4.1.3 "><p id="p35797372"><a name="p35797372"></a><a name="p35797372"></a>Specifies shortcut links for ECS types. For details, see <a href="#table64121649">Table 9</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  9** **links**  field description

<a name="table64121649"></a>
<table><thead align="left"><tr id="row59320951"><th class="cellrowborder" valign="top" width="16.48%" id="mcps1.2.4.1.1"><p id="p19525409166"><a name="p19525409166"></a><a name="p19525409166"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.29%" id="mcps1.2.4.1.2"><p id="p15255041613"><a name="p15255041613"></a><a name="p15255041613"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.23%" id="mcps1.2.4.1.3"><p id="p452516061611"><a name="p452516061611"></a><a name="p452516061611"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row61486274"><td class="cellrowborder" valign="top" width="16.48%" headers="mcps1.2.4.1.1 "><p id="p14332335"><a name="p14332335"></a><a name="p14332335"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.2.4.1.2 "><p id="p14933841"><a name="p14933841"></a><a name="p14933841"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.23%" headers="mcps1.2.4.1.3 "><p id="p1681623"><a name="p1681623"></a><a name="p1681623"></a>Specifies the shortcut link marker name.</p>
</td>
</tr>
<tr id="row15134612"><td class="cellrowborder" valign="top" width="16.48%" headers="mcps1.2.4.1.1 "><p id="p17944037"><a name="p17944037"></a><a name="p17944037"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.2.4.1.2 "><p id="p21885054"><a name="p21885054"></a><a name="p21885054"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.23%" headers="mcps1.2.4.1.3 "><p id="p27858965"><a name="p27858965"></a><a name="p27858965"></a>Specifies the shortcut link.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section191304136165"></a>

```
PUT https://{endpoint}/v2/{project_id}/servers/{server_id}
PUT https://{endpoint}/v2.1/{project_id}/servers/{server_id}
```

```
{
    "server": {
        "name": "new-server-test"
    }
}
```

## Example Response<a name="section1845702716524"></a>

```
{
  "server": {
    "tenant_id": "7910a6e50b80402ba028c8d96c1b31fe",
    "image": "",
    "accessIPv4": "",
    "addresses": {
      "03be5c1e-e05d-4905-a105-c3bd9b730bdc": [
        {
          "addr": "192.168.0.72",
          "version": 4
        }
      ]
    },
    "metadata": {},
    "accessIPv6": "",
    "created": "2018-05-17T03:15:48Z",
    "hostId": "7dc82f6b1d406200fc63e395cf4829cbffcb49de0e9c75c5773f201f",
    "flavor": {
      "links": [
        {
          "rel": "bookmark",
          "href": "https://None/7910a6e50b80402ba028c8d96c1b31fe/flavors/c3.1U1G"
        }
      ],
      "id": "c3.1U1G"
    },
    "OS-DCF:diskConfig": "MANUAL",
    "user_id": "d698a78532ca430f8daec1858f2b500e",
    "name": "new-server-test",
    "progress": 0,
    "links": [
      {
        "rel": "self",
        "href": "https://None/v2/7910a6e50b80402ba028c8d96c1b31fe/servers/1a19ef4f-be0a-4526-bf2f-14b4464d536a"
      },
      {
        "rel": "bookmark",
        "href": "https://None/7910a6e50b80402ba028c8d96c1b31fe/servers/1a19ef4f-be0a-4526-bf2f-14b4464d536a"
      }
    ],
    "id": "1a19ef4f-be0a-4526-bf2f-14b4464d536a",
    "updated": "2018-05-21T00:36:27Z",
    "status": "ACTIVE"
  }
}
```

## Returned Values<a name="section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

