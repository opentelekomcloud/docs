# Querying Forwarding Policies<a name="EN-US_TOPIC_0136295315"></a>

## Function<a name="section169151579315"></a>

This API is used to query the forwarding policies. Filter query and pagination query are supported. Unless otherwise specified, exact match is applied.

## URI<a name="section1688113211"></a>

GET /v2.0/lbaas/l7policies

## Constraints<a name="section392752110538"></a>

Parameters  **marker**,  **limit**, and  **page\_reverse**  are used for pagination query. Parameters  **marker**  and  **page\_reverse**  take effect only when they are used together with parameter  **limit**.

## Request<a name="section64891616203820"></a>

**Table  1**  Request parameters

<a name="table151465453212"></a>
<table><thead align="left"><tr id="row3253115415323"><th class="cellrowborder" valign="top" id="mcps1.2.6.1.1"><p id="p4253554173213"><a name="p4253554173213"></a><a name="p4253554173213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.6.1.2"><p id="p0253854153215"><a name="p0253854153215"></a><a name="p0253854153215"></a><strong id="b842352706192244"><a name="b842352706192244"></a><a name="b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.6.1.3"><p id="p1225395413214"><a name="p1225395413214"></a><a name="p1225395413214"></a>Type</p>
</th>
<th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.6.1.4"><p id="p1525315543325"><a name="p1525315543325"></a><a name="p1525315543325"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16253154103210"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p7253115415321"><a name="p7253115415321"></a><a name="p7253115415321"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p425315483210"><a name="p425315483210"></a><a name="p425315483210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p11253185463216"><a name="p11253185463216"></a><a name="p11253185463216"></a>String</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.4 "><p id="p4235152211344"><a name="p4235152211344"></a><a name="p4235152211344"></a>Specifies the ID of the forwarding policy from which pagination query starts, that is, the ID of the last forwarding policy on the previous page.</p>
<p id="p06221826143418"><a name="p06221826143418"></a><a name="p06221826143418"></a>This parameter must be used together with <strong id="b183401465212"><a name="b183401465212"></a><a name="b183401465212"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row325345463216"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1225310547328"><a name="p1225310547328"></a><a name="p1225310547328"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p152531554163219"><a name="p152531554163219"></a><a name="p152531554163219"></a>No</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p15253175413326"><a name="p15253175413326"></a><a name="p15253175413326"></a>Integer</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.4 "><p id="p163282306342"><a name="p163282306342"></a><a name="p163282306342"></a>Specifies the number of forwarding policies on each page. </p>
<p id="p8300236113416"><a name="p8300236113416"></a><a name="p8300236113416"></a>The value ranges from <strong id="b0707191721"><a name="b0707191721"></a><a name="b0707191721"></a>0</strong> to <strong id="b11708169222"><a name="b11708169222"></a><a name="b11708169222"></a>intmax</strong>.</p>
</td>
</tr>
<tr id="row19253165414327"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p13253105453218"><a name="p13253105453218"></a><a name="p13253105453218"></a>page_reverse</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p142535545323"><a name="p142535545323"></a><a name="p142535545323"></a>No</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1425335418324"><a name="p1425335418324"></a><a name="p1425335418324"></a>Boolean</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.4 "><p id="p15227113913341"><a name="p15227113913341"></a><a name="p15227113913341"></a>Specifies the page direction. The value can be <strong id="b5899185233513"><a name="b5899185233513"></a><a name="b5899185233513"></a>true</strong> or <strong id="b59004521353"><a name="b59004521353"></a><a name="b59004521353"></a>false</strong>, and the default value is <strong id="b139007525351"><a name="b139007525351"></a><a name="b139007525351"></a>false</strong>. The last page in the list requested with <strong id="b1990195223510"><a name="b1990195223510"></a><a name="b1990195223510"></a>page_reverse</strong> set to <strong id="b59011652143519"><a name="b59011652143519"></a><a name="b59011652143519"></a>false</strong> will not contain the "next" link, and the last page in the list requested with <strong id="b11901185210357"><a name="b11901185210357"></a><a name="b11901185210357"></a>page_reverse</strong> set to <strong id="b1990217528356"><a name="b1990217528356"></a><a name="b1990217528356"></a>true</strong> will not contain the "previous" link.</p>
<p id="p5244104243413"><a name="p5244104243413"></a><a name="p5244104243413"></a>This parameter must be used together with <strong id="b1845618157218"><a name="b1845618157218"></a><a name="b1845618157218"></a>limit</strong>.</p>
</td>
</tr>
<tr id="row925316546325"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p92531154103212"><a name="p92531154103212"></a><a name="p92531154103212"></a>id</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1825345483211"><a name="p1825345483211"></a><a name="p1825345483211"></a>No</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p824318301048"><a name="p824318301048"></a><a name="p824318301048"></a>String</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.4 "><p id="p152531254193215"><a name="p152531254193215"></a><a name="p152531254193215"></a>Specifies the forwarding policy ID.</p>
</td>
</tr>
<tr id="row1425305453217"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p12491330111414"><a name="p12491330111414"></a><a name="p12491330111414"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1625310542329"><a name="p1625310542329"></a><a name="p1625310542329"></a>No</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p122531354203217"><a name="p122531354203217"></a><a name="p122531354203217"></a>String</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.4 "><p id="p5927193621418"><a name="p5927193621418"></a><a name="p5927193621418"></a>Specifies the ID of the project where the forwarding policy is used.</p>
<p id="p1264211013318"><a name="p1264211013318"></a><a name="p1264211013318"></a>The value contains a maximum of 255 characters.</p>
<p id="p8222164914610"><a name="p8222164914610"></a><a name="p8222164914610"></a></p>
</td>
</tr>
<tr id="row3253454183210"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p725375413210"><a name="p725375413210"></a><a name="p725375413210"></a>name</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p32545545325"><a name="p32545545325"></a><a name="p32545545325"></a>No</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1525355483214"><a name="p1525355483214"></a><a name="p1525355483214"></a>String</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.4 "><p id="p52541154133217"><a name="p52541154133217"></a><a name="p52541154133217"></a>Specifies the forwarding policy name.</p>
<p id="p7527181302013"><a name="p7527181302013"></a><a name="p7527181302013"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row725415548328"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p1525475410329"><a name="p1525475410329"></a><a name="p1525475410329"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p18254554123211"><a name="p18254554123211"></a><a name="p18254554123211"></a>No</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p102541254193213"><a name="p102541254193213"></a><a name="p102541254193213"></a>Boolean</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.4 "><p id="p189741017613"><a name="p189741017613"></a><a name="p189741017613"></a>Specifies the administrative status of the forwarding policy.</p>
<p id="p189052592020"><a name="p189052592020"></a><a name="p189052592020"></a>The value can be <strong id="b12895162519218"><a name="b12895162519218"></a><a name="b12895162519218"></a>true</strong> or <strong id="b589717251216"><a name="b589717251216"></a><a name="b589717251216"></a>false</strong>.</p>
<p id="p1421417231357"><a name="p1421417231357"></a><a name="p1421417231357"></a>This parameter is reserved. The default value is <strong id="b2721201919431"><a name="b2721201919431"></a><a name="b2721201919431"></a>true</strong>.</p>
</td>
</tr>
<tr id="row9254254163217"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p72545543326"><a name="p72545543326"></a><a name="p72545543326"></a>description</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p152541954133218"><a name="p152541954133218"></a><a name="p152541954133218"></a>No</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1254135493214"><a name="p1254135493214"></a><a name="p1254135493214"></a>String</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.4 "><p id="p1336061815356"><a name="p1336061815356"></a><a name="p1336061815356"></a>Provides supplementary information about the forwarding policy.</p>
<p id="p196507154201"><a name="p196507154201"></a><a name="p196507154201"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row725418541329"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p62540546329"><a name="p62540546329"></a><a name="p62540546329"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p625415419325"><a name="p625415419325"></a><a name="p625415419325"></a>No</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p480613491444"><a name="p480613491444"></a><a name="p480613491444"></a>String</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.4 "><p id="p960104714116"><a name="p960104714116"></a><a name="p960104714116"></a>Specifies the ID of the listener to which the forwarding policy is added.</p>
</td>
</tr>
<tr id="row325485433215"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p112541454163214"><a name="p112541454163214"></a><a name="p112541454163214"></a>action</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p1425465412326"><a name="p1425465412326"></a><a name="p1425465412326"></a>No</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1325475413219"><a name="p1325475413219"></a><a name="p1325475413219"></a>String</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.4 "><p id="p19912991832"><a name="p19912991832"></a><a name="p19912991832"></a>Specifies whether requests are forwarded to another backend server group or redirected to another HTTPS listener.</p>
<p id="p136925473311"><a name="p136925473311"></a><a name="p136925473311"></a>The value can be one of the following:</p>
<a name="ul1141318491933"></a><a name="ul1141318491933"></a><ul id="ul1141318491933"><li><strong id="b338118316246"><a name="b338118316246"></a><a name="b338118316246"></a>REDIRECT_TO_POOL</strong>: Requests are forwarded to the backend server group specified by <strong id="b123821133246"><a name="b123821133246"></a><a name="b123821133246"></a>redirect_pool_id</strong>.</li><li><strong id="b10570312247"><a name="b10570312247"></a><a name="b10570312247"></a>REDIRECT_TO_LISTENER</strong>: Requests are redirected from the HTTP listener specified by <strong id="b35815332413"><a name="b35815332413"></a><a name="b35815332413"></a>listener_id</strong> to the HTTPS listener specified by <strong id="b4595316247"><a name="b4595316247"></a><a name="b4595316247"></a>redirect_listener_id</strong>.</li></ul>
</td>
</tr>
<tr id="row18254554113212"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p182541254143211"><a name="p182541254143211"></a><a name="p182541254143211"></a>redirect_pool_id</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p3254154193210"><a name="p3254154193210"></a><a name="p3254154193210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p280810522041"><a name="p280810522041"></a><a name="p280810522041"></a>String</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.4 "><p id="p115216211498"><a name="p115216211498"></a><a name="p115216211498"></a>Specifies the ID of the backend server group to which traffic is forwarded.</p>
</td>
</tr>
<tr id="row125475423215"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p39832033132210"><a name="p39832033132210"></a><a name="p39832033132210"></a>redirect_listener_id</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p498393342218"><a name="p498393342218"></a><a name="p498393342218"></a>No</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p369215541841"><a name="p369215541841"></a><a name="p369215541841"></a>String</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.4 "><p id="p687911951310"><a name="p687911951310"></a><a name="p687911951310"></a>Specifies the ID of the listener that forwards the traffic.</p>
</td>
</tr>
<tr id="row1185810017224"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p116361415224"><a name="p116361415224"></a><a name="p116361415224"></a>redirect_url</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p18171121482213"><a name="p18171121482213"></a><a name="p18171121482213"></a>No</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p1316311432216"><a name="p1316311432216"></a><a name="p1316311432216"></a>String</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.4 "><p id="p1714910214509"><a name="p1714910214509"></a><a name="p1714910214509"></a>Specifies the URL to which traffic is redirected.</p>
<p id="p914972185020"><a name="p914972185020"></a><a name="p914972185020"></a>This parameter is reserved.</p>
<p id="p94472021122016"><a name="p94472021122016"></a><a name="p94472021122016"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row19255105443211"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p325520546323"><a name="p325520546323"></a><a name="p325520546323"></a>position</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p15255354103210"><a name="p15255354103210"></a><a name="p15255354103210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p625545410329"><a name="p625545410329"></a><a name="p625545410329"></a>Integer</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.4 "><p id="p0275145775019"><a name="p0275145775019"></a><a name="p0275145775019"></a>Specifies the forwarding priority. The value ranges from <strong id="b68911142412"><a name="b68911142412"></a><a name="b68911142412"></a>1</strong> to <strong id="b199141112245"><a name="b199141112245"></a><a name="b199141112245"></a>100</strong>. The default value is <strong id="b9621131352411"><a name="b9621131352411"></a><a name="b9621131352411"></a>100</strong>.</p>
<p id="p122771157115019"><a name="p122771157115019"></a><a name="p122771157115019"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="row1325505415327"><td class="cellrowborder" valign="top" headers="mcps1.2.6.1.1 "><p id="p12559548326"><a name="p12559548326"></a><a name="p12559548326"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.2 "><p id="p12255155417329"><a name="p12255155417329"></a><a name="p12255155417329"></a>No</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.6.1.3 "><p id="p132556540327"><a name="p132556540327"></a><a name="p132556540327"></a>String</p>
</td>
<td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.6.1.4 "><p id="p14704205693714"><a name="p14704205693714"></a><a name="p14704205693714"></a>Specifies the provisioning status of the forwarding policy. The value can be <strong id="b7302203720252"><a name="b7302203720252"></a><a name="b7302203720252"></a>ACTIVE</strong>, <strong id="b230413372255"><a name="b230413372255"></a><a name="b230413372255"></a>PENDING_CREATE</strong>, or <strong id="b8304037132520"><a name="b8304037132520"></a><a name="b8304037132520"></a>ERROR</strong>.</p>
<p id="p178421832011"><a name="p178421832011"></a><a name="p178421832011"></a>The default value is <strong id="b1745011392251"><a name="b1745011392251"></a><a name="b1745011392251"></a>ACTIVE</strong>.</p>
<p id="p210952312206"><a name="p210952312206"></a><a name="p210952312206"></a>This parameter is reserved.</p>
<p id="p207341733192010"><a name="p207341733192010"></a><a name="p207341733192010"></a>The value contains a maximum of 16 characters.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section1587922123913"></a>

**Table  2**  Response parameters

<a name="table158419166402"></a>
<table><thead align="left"><tr id="row19584716114011"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="a64927ab2aa97448982ed5b4e23d8f815"><a name="a64927ab2aa97448982ed5b4e23d8f815"></a><a name="a64927ab2aa97448982ed5b4e23d8f815"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="ab40573ee697e4318a8353d752926a303"><a name="ab40573ee697e4318a8353d752926a303"></a><a name="ab40573ee697e4318a8353d752926a303"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="aa29d0f322c0e4dee90c6d57d36ed4429"><a name="aa29d0f322c0e4dee90c6d57d36ed4429"></a><a name="aa29d0f322c0e4dee90c6d57d36ed4429"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3584201694018"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="affcef3ef00a341f2b96f6fcc2d42dcf3"><a name="affcef3ef00a341f2b96f6fcc2d42dcf3"></a><a name="affcef3ef00a341f2b96f6fcc2d42dcf3"></a>l7policies</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096561533_p422512115486"><a name="en-us_topic_0096561533_p422512115486"></a><a name="en-us_topic_0096561533_p422512115486"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="a5f3b9dc41ec44762b0e3259be85e3620"><a name="a5f3b9dc41ec44762b0e3259be85e3620"></a><a name="a5f3b9dc41ec44762b0e3259be85e3620"></a>Lists the forwarding policies. For details, see <a href="#table1921785733313">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **l7policy**  parameter description

<a name="table1921785733313"></a>
<table><thead align="left"><tr id="row10701165673714"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.4.1.1"><p id="p1470214562375"><a name="p1470214562375"></a><a name="p1470214562375"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.4.1.2"><p id="p2702105618372"><a name="p2702105618372"></a><a name="p2702105618372"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60.60606060606061%" id="mcps1.2.4.1.3"><p id="p770265613371"><a name="p770265613371"></a><a name="p770265613371"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1170211562375"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p37021956163715"><a name="p37021956163715"></a><a name="p37021956163715"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p9101532352"><a name="p9101532352"></a><a name="p9101532352"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p87022056103715"><a name="p87022056103715"></a><a name="p87022056103715"></a>Specifies the forwarding policy ID.</p>
</td>
</tr>
<tr id="row5702175643718"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p423345441210"><a name="p423345441210"></a><a name="p423345441210"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p1949510305143"><a name="p1949510305143"></a><a name="p1949510305143"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p923755481211"><a name="p923755481211"></a><a name="p923755481211"></a>Specifies the ID of the project where the forwarding policy is used.</p>
<p id="p189295742214"><a name="p189295742214"></a><a name="p189295742214"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row67026562371"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p97021056173713"><a name="p97021056173713"></a><a name="p97021056173713"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p9702105619373"><a name="p9702105619373"></a><a name="p9702105619373"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p57021564370"><a name="p57021564370"></a><a name="p57021564370"></a>Specifies the forwarding policy name.</p>
<p id="p1532011232"><a name="p1532011232"></a><a name="p1532011232"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row17021156193714"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p1570220562375"><a name="p1570220562375"></a><a name="p1570220562375"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p270220563373"><a name="p270220563373"></a><a name="p270220563373"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p935075494818"><a name="p935075494818"></a><a name="p935075494818"></a>Specifies the administrative status of the forwarding policy.</p>
<p id="p535095417489"><a name="p535095417489"></a><a name="p535095417489"></a>The value can be <strong id="b1329576025"><a name="b1329576025"></a><a name="b1329576025"></a>true</strong> or <strong id="b1262032845"><a name="b1262032845"></a><a name="b1262032845"></a>false</strong>.</p>
<p id="p18576435690"><a name="p18576435690"></a><a name="p18576435690"></a>This parameter is reserved. The default value is <strong id="b1265618259431"><a name="b1265618259431"></a><a name="b1265618259431"></a>true</strong>.</p>
</td>
</tr>
<tr id="row87021656103712"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p147021156163720"><a name="p147021156163720"></a><a name="p147021156163720"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p2702105663711"><a name="p2702105663711"></a><a name="p2702105663711"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p163501654104816"><a name="p163501654104816"></a><a name="p163501654104816"></a>Provides supplementary information about the forwarding policy.</p>
<p id="p1241002122314"><a name="p1241002122314"></a><a name="p1241002122314"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row1970325673717"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p207031656133714"><a name="p207031656133714"></a><a name="p207031656133714"></a>listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p1637154512510"><a name="p1637154512510"></a><a name="p1637154512510"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p183501454194816"><a name="p183501454194816"></a><a name="p183501454194816"></a>Specifies the ID of the listener to which the forwarding policy is added.</p>
</td>
</tr>
<tr id="row1970317567371"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p17703115614375"><a name="p17703115614375"></a><a name="p17703115614375"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p1170365623715"><a name="p1170365623715"></a><a name="p1170365623715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p2351954164814"><a name="p2351954164814"></a><a name="p2351954164814"></a>Specifies whether requests are forwarded to another backend server group or redirected to another HTTPS listener.</p>
<p id="p13351145412483"><a name="p13351145412483"></a><a name="p13351145412483"></a>The value can be one of the following:</p>
<a name="ul203511354204814"></a><a name="ul203511354204814"></a><ul id="ul203511354204814"><li><strong id="b336143162616"><a name="b336143162616"></a><a name="b336143162616"></a>REDIRECT_TO_POOL</strong>: Requests are forwarded to the backend server group specified by <strong id="b437231267"><a name="b437231267"></a><a name="b437231267"></a>redirect_pool_id</strong>.</li><li><strong id="b255419412266"><a name="b255419412266"></a><a name="b255419412266"></a>REDIRECT_TO_LISTENER</strong>: Requests are redirected to the HTTPS listener specified by <strong id="b105568411269"><a name="b105568411269"></a><a name="b105568411269"></a>listener_id</strong> to the HTTPS listener specified by <strong id="b555724142614"><a name="b555724142614"></a><a name="b555724142614"></a>redirect_listener_id</strong>.</li></ul>
</td>
</tr>
<tr id="row77039560374"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p6703195611375"><a name="p6703195611375"></a><a name="p6703195611375"></a>redirect_pool_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p1250115531251"><a name="p1250115531251"></a><a name="p1250115531251"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p142211521194918"><a name="p142211521194918"></a><a name="p142211521194918"></a>Specifies the ID of the backend server group to which traffic is forwarded.</p>
</td>
</tr>
<tr id="row461412820402"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p35992015134018"><a name="p35992015134018"></a><a name="p35992015134018"></a>redirect_listener_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p1422311551851"><a name="p1422311551851"></a><a name="p1422311551851"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p722113215492"><a name="p722113215492"></a><a name="p722113215492"></a>Specifies the ID of the listener that forwards the traffic.</p>
</td>
</tr>
<tr id="row9703135610377"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p18703195613712"><a name="p18703195613712"></a><a name="p18703195613712"></a>redirect_url</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p18703155693720"><a name="p18703155693720"></a><a name="p18703155693720"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p832245451219"><a name="p832245451219"></a><a name="p832245451219"></a>Specifies the URL to which traffic is redirected.</p>
<p id="p132355414127"><a name="p132355414127"></a><a name="p132355414127"></a>This parameter is reserved.</p>
<p id="p1873163917238"><a name="p1873163917238"></a><a name="p1873163917238"></a>The value contains a maximum of 255 characters.</p>
</td>
</tr>
<tr id="row5703956183715"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p18703155613719"><a name="p18703155613719"></a><a name="p18703155613719"></a>rules</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p1970375611378"><a name="p1970375611378"></a><a name="p1970375611378"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p17125144555018"><a name="p17125144555018"></a><a name="p17125144555018"></a>Lists the forwarding rules of the forwarding policy.</p>
</td>
</tr>
<tr id="row1970312566375"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p770375663720"><a name="p770375663720"></a><a name="p770375663720"></a>position</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p1870319564378"><a name="p1870319564378"></a><a name="p1870319564378"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p18338205419126"><a name="p18338205419126"></a><a name="p18338205419126"></a>Specifies the forwarding priority. The value ranges from <strong id="b3954121115267"><a name="b3954121115267"></a><a name="b3954121115267"></a>1</strong> to <strong id="b149541113263"><a name="b149541113263"></a><a name="b149541113263"></a>100</strong>. The default value is <strong id="b9234151312612"><a name="b9234151312612"></a><a name="b9234151312612"></a>100</strong>.</p>
<p id="p133915461210"><a name="p133915461210"></a><a name="p133915461210"></a>This parameter is reserved.</p>
</td>
</tr>
<tr id="row870395643716"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p6704256183713"><a name="p6704256183713"></a><a name="p6704256183713"></a>provisioning_status</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p170405683718"><a name="p170405683718"></a><a name="p170405683718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p934715461215"><a name="p934715461215"></a><a name="p934715461215"></a>Specifies the provisioning status of the forwarding policy. The value can be <strong id="b1508816122614"><a name="b1508816122614"></a><a name="b1508816122614"></a>ACTIVE</strong>, <strong id="b1050981622617"><a name="b1050981622617"></a><a name="b1050981622617"></a>PENDING_CREATE</strong>, or <strong id="b9510131618263"><a name="b9510131618263"></a><a name="b9510131618263"></a>ERROR</strong>.</p>
<p id="p1111194711237"><a name="p1111194711237"></a><a name="p1111194711237"></a>The value contains a maximum of 16 characters.</p>
<div class="note" id="note1950762816420"><a name="note1950762816420"></a><a name="note1950762816420"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p550922834216"><a name="p550922834216"></a><a name="p550922834216"></a>This parameter has no actual meaning. The default value is <strong id="b842352706175433"><a name="b842352706175433"></a><a name="b842352706175433"></a>ACTIVE</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row1190111551316"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096561531_p11729026152811"><a name="en-us_topic_0096561531_p11729026152811"></a><a name="en-us_topic_0096561531_p11729026152811"></a>l7policies_links</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.4.1.2 "><p id="p215116463169"><a name="p215116463169"></a><a name="p215116463169"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="60.60606060606061%" headers="mcps1.2.4.1.3 "><p id="p5542991616"><a name="p5542991616"></a><a name="p5542991616"></a>Provides links to the previous or next page during pagination query, respectively.</p>
<p id="p165764116119"><a name="p165764116119"></a><a name="p165764116119"></a>This parameter exists only in the response body of pagination query.</p>
<p id="p53635145114"><a name="p53635145114"></a><a name="p53635145114"></a>For details, see <a href="#table164602247259">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **l7policies\_links**  parameter description

<a name="table164602247259"></a>
<table><thead align="left"><tr id="row850752492520"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p950782413257"><a name="p950782413257"></a><a name="p950782413257"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p75071724202519"><a name="p75071724202519"></a><a name="p75071724202519"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p95070246259"><a name="p95070246259"></a><a name="p95070246259"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row050718241255"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p115071024142516"><a name="p115071024142516"></a><a name="p115071024142516"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p175071724112514"><a name="p175071724112514"></a><a name="p175071724112514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096561531_p1653852193312"><a name="en-us_topic_0096561531_p1653852193312"></a><a name="en-us_topic_0096561531_p1653852193312"></a>Provides links to the previous or next page during pagination query, respectively.</p>
</td>
</tr>
<tr id="row165074249253"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p155071124112518"><a name="p155071124112518"></a><a name="p155071124112518"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p550762417253"><a name="p550762417253"></a><a name="p550762417253"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p1772113411218"><a name="p1772113411218"></a><a name="p1772113411218"></a>Specifies the prompt of the previous or next page.</p>
<p id="p422510443113"><a name="p422510443113"></a><a name="p422510443113"></a>The value can be <strong id="b1536213910262"><a name="b1536213910262"></a><a name="b1536213910262"></a>next</strong> or <strong id="b5363123962614"><a name="b5363123962614"></a><a name="b5363123962614"></a>previous</strong>. The value <strong id="b2155104182610"><a name="b2155104182610"></a><a name="b2155104182610"></a>next</strong> indicates the href containing the URL of the next page, and <strong id="b3156841102616"><a name="b3156841102616"></a><a name="b3156841102616"></a>previous</strong> indicates the href containing the URL of the previous page.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section098062617334"></a>

-   Example request 1: Querying all forwarding policies

    ```
    GET https://{Endpoint}/v2.0/lbaas/l7policies
    ```

-   Example response 1

    ```
    {
        "l7policies": [
            {
                "redirect_pool_id": "431a03eb-81bb-408e-ae37-7ce19023692b", 
                "redirect_listener_id": null,  
                "description": "", 
                "admin_state_up": true, 
                "rules": [
                    {
                        "id": "67d8a8fa-b0dd-4bd4-a85b-671db19b2ef3"
                    }, 
                    {
                        "id": "f02b3bca-69d2-4335-a3fa-a8054e996213"
                    }
                ], 
                "tenant_id": "a31d2bdcf7604c0faaddb058e1e08819",
     
                "listener_id": "26058b64-6185-4e06-874e-4bd68b7633d0", 
                "redirect_url": null, 
                "action": "REDIRECT_TO_POOL", 
                "position": 2,
                "provisioning_status": "ACTIVE", 
                "id": "5ae0e1e7-5f0f-47a1-b39f-5d4c428a1586", 
                "name": ""
            }, 
            {
                "redirect_pool_id": "59eebd7b-c68f-4f8a-aa7f-e062e84c0690", 
                "redirect_listener_id": null,  
                "description": "", 
                "admin_state_up": true, 
                "rules": [
                    {
                        "id": "f4499f48-de3d-4efe-926d-926aa4d6aaf5"
                    }
                ], 
                "tenant_id": "a31d2bdcf7604c0faaddb058e1e08819",
                "listener_id": "e1310063-00de-4867-ab55-ccac4d9db364", 
                "redirect_url": null, 
                "action": "REDIRECT_TO_POOL", 
                "position": 1, 
                "provisioning_status": "ACTIVE",
                "id": "6cfd9d89-1d7e-4d84-ae1f-a8c5ff126f72", 
                "name": ""
            }
        ]
    }
    ```

-   Example request 2: Filtering forwarding policies through which requests are forwarded to the backend server group

    ```
    GET https://{Endpoint}/v2.0/lbaas/l7policies?action=REDIRECT_TO_POOL
    ```

-   Example response 2

    ```
    {
        "l7policies": [
            {
                "redirect_pool_id": "431a03eb-81bb-408e-ae37-7ce19023692b", 
                "redirect_listener_id": null,  
                "description": "", 
                "admin_state_up": true, 
                "rules": [
                    {
                        "id": "67d8a8fa-b0dd-4bd4-a85b-671db19b2ef3"
                    }, 
                    {
                        "id": "f02b3bca-69d2-4335-a3fa-a8054e996213"
                    }
                ], 
                "tenant_id": "a31d2bdcf7604c0faaddb058e1e08819",
      
                "listener_id": "26058b64-6185-4e06-874e-4bd68b7633d0", 
                "redirect_url": null, 
                "action": "REDIRECT_TO_POOL", 
                "position": 2,
                "provisioning_status": "ACTIVE", 
                "id": "5ae0e1e7-5f0f-47a1-b39f-5d4c428a1586", 
                "name": ""
            }, 
            {
                "redirect_pool_id": "59eebd7b-c68f-4f8a-aa7f-e062e84c0690", 
                "redirect_listener_id": null,  
                "description": "", 
                "admin_state_up": true, 
                "rules": [
                    {
                        "id": "f4499f48-de3d-4efe-926d-926aa4d6aaf5"
                    }
                ], 
                "tenant_id": "a31d2bdcf7604c0faaddb058e1e08819",
     
                "listener_id": "e1310063-00de-4867-ab55-ccac4d9db364", 
                "redirect_url": null, 
                "action": "REDIRECT_TO_POOL", 
                "position": 1, 
                "provisioning_status": "ACTIVE",
                "id": "6cfd9d89-1d7e-4d84-ae1f-a8c5ff126f72", 
                "name": ""
            }
        ]
    }
    ```


## Status Code<a name="section18652115813401"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).

