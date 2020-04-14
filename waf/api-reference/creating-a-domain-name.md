# Creating a Domain Name<a name="EN-US_TOPIC_0193631107"></a>

## Function Description<a name="section14920754"></a>

This API is used to create a domain name.

## URI<a name="section69063"></a>

-   URI format

    POST  /v1/\{project\_id\}/waf/instance

-   Parameter description

    **Table  1**  Path parameters

    <a name="table12964649"></a>
    <table><thead align="left"><tr id="row53015668"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p66410720"><a name="p66410720"></a><a name="p66410720"></a><strong id="b4737184915504"><a name="b4737184915504"></a><a name="b4737184915504"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p10559236"><a name="p10559236"></a><a name="p10559236"></a><strong id="b12972155075013"><a name="b12972155075013"></a><a name="b12972155075013"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p49991817"><a name="p49991817"></a><a name="p49991817"></a><strong id="b1526185213508"><a name="b1526185213508"></a><a name="b1526185213508"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p22805399"><a name="p22805399"></a><a name="p22805399"></a><strong id="b129716536502"><a name="b129716536502"></a><a name="b129716536502"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35298005"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p40566123"><a name="p40566123"></a><a name="p40566123"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p64630530"><a name="p64630530"></a><a name="p64630530"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p581569"><a name="p581569"></a><a name="p581569"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p47107153"><a name="p47107153"></a><a name="p47107153"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section621568"></a>

Request parameters

**Table  2**  Parameter description

<a name="table33716739"></a>
<table><thead align="left"><tr id="row27649238"><th class="cellrowborder" valign="top" width="26.52734726527347%" id="mcps1.2.5.1.1"><p id="p24995816"><a name="p24995816"></a><a name="p24995816"></a><strong id="b843315113517"><a name="b843315113517"></a><a name="b843315113517"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.2"><p id="p11395239"><a name="p11395239"></a><a name="p11395239"></a><strong id="b16519222511"><a name="b16519222511"></a><a name="b16519222511"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.418558144185582%" id="mcps1.2.5.1.3"><p id="p50599162"><a name="p50599162"></a><a name="p50599162"></a><strong id="b8409858513"><a name="b8409858513"></a><a name="b8409858513"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.725727427257276%" id="mcps1.2.5.1.4"><p id="p4891466"><a name="p4891466"></a><a name="p4891466"></a><strong id="b66760685113"><a name="b66760685113"></a><a name="b66760685113"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row60664446"><td class="cellrowborder" valign="top" width="26.52734726527347%" headers="mcps1.2.5.1.1 "><p id="p14873087"><a name="p14873087"></a><a name="p14873087"></a>hostname</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p63869364"><a name="p63869364"></a><a name="p63869364"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.418558144185582%" headers="mcps1.2.5.1.3 "><p id="p6035973"><a name="p6035973"></a><a name="p6035973"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.725727427257276%" headers="mcps1.2.5.1.4 "><p id="p19151836"><a name="p19151836"></a><a name="p19151836"></a>Specifies the domain name.</p>
<p id="p78431657145217"><a name="p78431657145217"></a><a name="p78431657145217"></a>For example, <strong id="b311114474614"><a name="b311114474614"></a><a name="b311114474614"></a>www.example.com</strong> or <strong id="b15504164713466"><a name="b15504164713466"></a><a name="b15504164713466"></a>*.example.com</strong>.</p>
</td>
</tr>
<tr id="row38148796"><td class="cellrowborder" valign="top" width="26.52734726527347%" headers="mcps1.2.5.1.1 "><p id="p3044756"><a name="p3044756"></a><a name="p3044756"></a>certificate_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p45298660"><a name="p45298660"></a><a name="p45298660"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.418558144185582%" headers="mcps1.2.5.1.3 "><p id="p45312853"><a name="p45312853"></a><a name="p45312853"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.725727427257276%" headers="mcps1.2.5.1.4 "><p id="p46462478"><a name="p46462478"></a><a name="p46462478"></a>Specifies the certificate ID. This parameter is mandatory when <strong id="b96208415244"><a name="b96208415244"></a><a name="b96208415244"></a>client_protocol</strong> is set to <strong id="b7989984247"><a name="b7989984247"></a><a name="b7989984247"></a>HTTPS</strong>.</p>
</td>
</tr>
<tr id="row15509126"><td class="cellrowborder" valign="top" width="26.52734726527347%" headers="mcps1.2.5.1.1 "><p id="p48279679"><a name="p48279679"></a><a name="p48279679"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p18339925"><a name="p18339925"></a><a name="p18339925"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.418558144185582%" headers="mcps1.2.5.1.3 "><p id="p9138927"><a name="p9138927"></a><a name="p9138927"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="42.725727427257276%" headers="mcps1.2.5.1.4 "><p id="p2055605"><a name="p2055605"></a><a name="p2055605"></a>Specifies the origin server information, including the <strong id="b2440569499"><a name="b2440569499"></a><a name="b2440569499"></a>client_protocol</strong>, <strong id="b144475611496"><a name="b144475611496"></a><a name="b144475611496"></a>server_protocol</strong>, <strong id="b744145618493"><a name="b744145618493"></a><a name="b744145618493"></a>address</strong>, and <strong id="b165115664913"><a name="b165115664913"></a><a name="b165115664913"></a>port</strong> fields.</p>
<a name="ul5701341115010"></a><a name="ul5701341115010"></a><ul id="ul5701341115010"><li><span class="parmvalue" id="parmvalue179100402277"><a name="parmvalue179100402277"></a><a name="parmvalue179100402277"></a><b>client_protocol</b></span>: protocol type of the client. The options are <strong id="b890725042413"><a name="b890725042413"></a><a name="b890725042413"></a>HTTP</strong> and <strong id="b3852454162414"><a name="b3852454162414"></a><a name="b3852454162414"></a>HTTPS</strong>.</li><li><strong id="b842352706201043"><a name="b842352706201043"></a><a name="b842352706201043"></a>server_protocol</strong>: protocol used by WAF to forward client requests to the server. The options are <strong id="b9279513192520"><a name="b9279513192520"></a><a name="b9279513192520"></a>HTTP</strong> and <strong id="b3279313162513"><a name="b3279313162513"></a><a name="b3279313162513"></a>HTTPS</strong>.</li><li><strong id="b1316614526555"><a name="b1316614526555"></a><a name="b1316614526555"></a>address</strong>: public IP address or domain name of the web server that the client accesses</li><li><strong id="b1953817195815"><a name="b1953817195815"></a><a name="b1953817195815"></a>port</strong>: port number used by the web server. The value ranges from <strong id="b25341720586"><a name="b25341720586"></a><a name="b25341720586"></a>0</strong> to <strong id="b10531417165818"><a name="b10531417165818"></a><a name="b10531417165818"></a>65535</strong>, for example, <strong id="b195381717583"><a name="b195381717583"></a><a name="b195381717583"></a>8080</strong>.</li></ul>
</td>
</tr>
<tr id="row18500453"><td class="cellrowborder" valign="top" width="26.52734726527347%" headers="mcps1.2.5.1.1 "><p id="p22141721"><a name="p22141721"></a><a name="p22141721"></a>proxy</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p48649006"><a name="p48649006"></a><a name="p48649006"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.418558144185582%" headers="mcps1.2.5.1.3 "><p id="p48255436"><a name="p48255436"></a><a name="p48255436"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="42.725727427257276%" headers="mcps1.2.5.1.4 "><p id="p181572050193818"><a name="p181572050193818"></a><a name="p181572050193818"></a>Specifies whether a proxy is configured.</p>
<a name="ul125775813386"></a><a name="ul125775813386"></a><ul id="ul125775813386"><li><strong id="b18191715278"><a name="b18191715278"></a><a name="b18191715278"></a>true</strong>: A proxy is configured.</li><li><strong id="b19821111882714"><a name="b19821111882714"></a><a name="b19821111882714"></a>false</strong>: No proxy is configured.</li></ul>
</td>
</tr>
<tr id="row8400175801319"><td class="cellrowborder" valign="top" width="26.52734726527347%" headers="mcps1.2.5.1.1 "><p id="p104001658141317"><a name="p104001658141317"></a><a name="p104001658141317"></a>sip_header_name</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p44001058101316"><a name="p44001058101316"></a><a name="p44001058101316"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.418558144185582%" headers="mcps1.2.5.1.3 "><p id="p1840010585132"><a name="p1840010585132"></a><a name="p1840010585132"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.725727427257276%" headers="mcps1.2.5.1.4 "><p id="p3687155611489"><a name="p3687155611489"></a><a name="p3687155611489"></a>Specifies the type of the source IP header. This parameter is required only when <strong id="b2013517415615"><a name="b2013517415615"></a><a name="b2013517415615"></a>proxy</strong> is set to <strong id="b1854277613"><a name="b1854277613"></a><a name="b1854277613"></a>true</strong>.</p>
<p id="p63761813186"><a name="p63761813186"></a><a name="p63761813186"></a>The options are as follows: <strong id="b135841836236"><a name="b135841836236"></a><a name="b135841836236"></a>default</strong>, <strong id="b358416313237"><a name="b358416313237"></a><a name="b358416313237"></a>cloudflare</strong>, <strong id="b1758423132314"><a name="b1758423132314"></a><a name="b1758423132314"></a>akamai</strong>, and <strong id="b058410316239"><a name="b058410316239"></a><a name="b058410316239"></a>custom</strong>.</p>
</td>
</tr>
<tr id="row1797718111419"><td class="cellrowborder" valign="top" width="26.52734726527347%" headers="mcps1.2.5.1.1 "><p id="p29774120143"><a name="p29774120143"></a><a name="p29774120143"></a>sip_header_list</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p997712118143"><a name="p997712118143"></a><a name="p997712118143"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.418558144185582%" headers="mcps1.2.5.1.3 "><p id="p149779141420"><a name="p149779141420"></a><a name="p149779141420"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="42.725727427257276%" headers="mcps1.2.5.1.4 "><p id="p197771191414"><a name="p197771191414"></a><a name="p197771191414"></a>Specifies the HTTP request header for identifying the real source IP address. This parameter is required only when <strong id="b944019187618"><a name="b944019187618"></a><a name="b944019187618"></a>proxy</strong> is set to <strong id="b134481182613"><a name="b134481182613"></a><a name="b134481182613"></a>true</strong>.</p>
<a name="ul1757412912176"></a><a name="ul1757412912176"></a><ul id="ul1757412912176"><li>If <strong id="b1368922419617"><a name="b1368922419617"></a><a name="b1368922419617"></a>sip_header_name</strong> is <strong id="b36891224269"><a name="b36891224269"></a><a name="b36891224269"></a>default</strong>, <strong id="b18689024465"><a name="b18689024465"></a><a name="b18689024465"></a>sip_header_list</strong> is <strong id="b0689192413613"><a name="b0689192413613"></a><a name="b0689192413613"></a>["X-Forwarded-For"]</strong>.</li><li>If <strong id="b9555161313548"><a name="b9555161313548"></a><a name="b9555161313548"></a>sip_header_name</strong> is <strong id="b6555181316544"><a name="b6555181316544"></a><a name="b6555181316544"></a>cloudflare</strong>, <strong id="b10555111325415"><a name="b10555111325415"></a><a name="b10555111325415"></a>sip_header_list</strong> is <strong id="b3555813145418"><a name="b3555813145418"></a><a name="b3555813145418"></a>["CF-Connecting-IP", "X-Forwarded-For"]</strong>.</li><li>If <strong id="b1779810355109"><a name="b1779810355109"></a><a name="b1779810355109"></a>sip_header_name</strong> is <strong id="b18806535151010"><a name="b18806535151010"></a><a name="b18806535151010"></a>akamai</strong>, <strong id="b108061135161015"><a name="b108061135161015"></a><a name="b108061135161015"></a>sip_header_list</strong> is <strong id="b480613357108"><a name="b480613357108"></a><a name="b480613357108"></a>["True-Client-IP"]</strong>.</li><li>If <strong id="b8261133520617"><a name="b8261133520617"></a><a name="b8261133520617"></a>sip_header_name</strong> is <strong id="b112616351610"><a name="b112616351610"></a><a name="b112616351610"></a>custom</strong>, you can customize a value.</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section5594120"></a>

Response parameters

**Table  3**  Parameter description

<a name="table27490285"></a>
<table><thead align="left"><tr id="row66285160"><th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.4.1.1"><p id="p388852"><a name="p388852"></a><a name="p388852"></a><strong id="b1136721055510"><a name="b1136721055510"></a><a name="b1136721055510"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.2"><p id="p31497077"><a name="p31497077"></a><a name="p31497077"></a><strong id="b8515711205511"><a name="b8515711205511"></a><a name="b8515711205511"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="58.160000000000004%" id="mcps1.2.4.1.3"><p id="p1126483"><a name="p1126483"></a><a name="p1126483"></a><strong id="b332961215552"><a name="b332961215552"></a><a name="b332961215552"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row10138352"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p15900196"><a name="p15900196"></a><a name="p15900196"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p12847463"><a name="p12847463"></a><a name="p12847463"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p34011620"><a name="p34011620"></a><a name="p34011620"></a>Specifies the instance ID.</p>
</td>
</tr>
<tr id="row37669127"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p31300427"><a name="p31300427"></a><a name="p31300427"></a>hostname</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p52306652"><a name="p52306652"></a><a name="p52306652"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p8980385"><a name="p8980385"></a><a name="p8980385"></a>Specifies the domain name.</p>
</td>
</tr>
<tr id="row2371534191710"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p237173411719"><a name="p237173411719"></a><a name="p237173411719"></a>cname</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p4371834191710"><a name="p4371834191710"></a><a name="p4371834191710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p4371234161716"><a name="p4371234161716"></a><a name="p4371234161716"></a>Specifies the CNAME value. For example, <strong id="b1398922619566"><a name="b1398922619566"></a><a name="b1398922619566"></a>efec1196267b41c399f2980ea4048517.waf.cloud.com</strong>.</p>
</td>
</tr>
<tr id="row18492244185"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p1649294151819"><a name="p1649294151819"></a><a name="p1649294151819"></a>txt_code</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p3492164151820"><a name="p3492164151820"></a><a name="p3492164151820"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p1549244121814"><a name="p1549244121814"></a><a name="p1549244121814"></a>Specifies the TXT record. This parameter is returned only when <strong id="b20853175115288"><a name="b20853175115288"></a><a name="b20853175115288"></a>proxy</strong> is set to <strong id="b198535512287"><a name="b198535512287"></a><a name="b198535512287"></a>true</strong>.</p>
</td>
</tr>
<tr id="row6734163120182"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p37341531101820"><a name="p37341531101820"></a><a name="p37341531101820"></a>sub_domain</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p177343313184"><a name="p177343313184"></a><a name="p177343313184"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p673423131814"><a name="p673423131814"></a><a name="p673423131814"></a>Specifies the subdomain name. This parameter is returned only when <strong id="b895610102919"><a name="b895610102919"></a><a name="b895610102919"></a>proxy</strong> is set to <strong id="b199641419299"><a name="b199641419299"></a><a name="b199641419299"></a>true</strong>.</p>
</td>
</tr>
<tr id="row22290018"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p60661062"><a name="p60661062"></a><a name="p60661062"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p14598990"><a name="p14598990"></a><a name="p14598990"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p41667555"><a name="p41667555"></a><a name="p41667555"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row39463677"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p42441296"><a name="p42441296"></a><a name="p42441296"></a>protect_status</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p15192931"><a name="p15192931"></a><a name="p15192931"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p18949775417"><a name="p18949775417"></a><a name="p18949775417"></a>Specifies the WAF mode.</p>
<a name="ul1029811519417"></a><a name="ul1029811519417"></a><ul id="ul1029811519417"><li><span class="parmvalue" id="parmvalue4702153915193"><a name="parmvalue4702153915193"></a><a name="parmvalue4702153915193"></a><b>-1</b></span>: bypassed.</li><li><strong id="b18764195091912"><a name="b18764195091912"></a><a name="b18764195091912"></a>0</strong>: disabled.</li><li><strong id="b552521212290"><a name="b552521212290"></a><a name="b552521212290"></a>1</strong>: enabled.</li></ul>
</td>
</tr>
<tr id="row2684242"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p16097086"><a name="p16097086"></a><a name="p16097086"></a>access_status</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p28795557"><a name="p28795557"></a><a name="p28795557"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p12249113014412"><a name="p12249113014412"></a><a name="p12249113014412"></a>Specifies whether a domain name is connected to WAF.</p>
<a name="ul45972388415"></a><a name="ul45972388415"></a><ul id="ul45972388415"><li><strong id="b12135202082919"><a name="b12135202082919"></a><a name="b12135202082919"></a>0</strong>: The domain name is not connected to WAF.</li><li><strong id="b159792116291"><a name="b159792116291"></a><a name="b159792116291"></a>1</strong>: The domain name is connected to WAF.</li></ul>
</td>
</tr>
<tr id="row53996033"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p11602527"><a name="p11602527"></a><a name="p11602527"></a>proxy</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p280597"><a name="p280597"></a><a name="p280597"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p53262117423"><a name="p53262117423"></a><a name="p53262117423"></a>Specifies whether a proxy is configured.</p>
<a name="ul18351173214216"></a><a name="ul18351173214216"></a><ul id="ul18351173214216"><li><strong id="b169061431142915"><a name="b169061431142915"></a><a name="b169061431142915"></a>true</strong>: A proxy is configured.</li><li><strong id="b588319329291"><a name="b588319329291"></a><a name="b588319329291"></a>false</strong>: No proxy is configured.</li></ul>
</td>
</tr>
<tr id="row3228975"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p60220426"><a name="p60220426"></a><a name="p60220426"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p46016313"><a name="p46016313"></a><a name="p46016313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p36333861"><a name="p36333861"></a><a name="p36333861"></a>Specifies the protocol type of the client. The options are <strong id="b54781426308"><a name="b54781426308"></a><a name="b54781426308"></a>HTTP</strong>, <strong id="b16781165163013"><a name="b16781165163013"></a><a name="b16781165163013"></a>HTTPS</strong>, and <strong id="b17867089302"><a name="b17867089302"></a><a name="b17867089302"></a>HTTP,HTTPS</strong>.</p>
</td>
</tr>
<tr id="row58569293"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p46492254"><a name="p46492254"></a><a name="p46492254"></a>certificate_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p7776224"><a name="p7776224"></a><a name="p7776224"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p653394019291"><a name="p653394019291"></a><a name="p653394019291"></a>Specifies the certificate ID. This parameter is mandatory when <strong id="b114852013113016"><a name="b114852013113016"></a><a name="b114852013113016"></a>client_protocol</strong> is set to <strong id="b1548541343019"><a name="b1548541343019"></a><a name="b1548541343019"></a>HTTPS</strong>.</p>
</td>
</tr>
<tr id="row31722960"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p19422978"><a name="p19422978"></a><a name="p19422978"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p29757409"><a name="p29757409"></a><a name="p29757409"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p61539924"><a name="p61539924"></a><a name="p61539924"></a>Specifies the origin server information, including the <strong id="b16453827103012"><a name="b16453827103012"></a><a name="b16453827103012"></a>client_protocol</strong>, <strong id="b16461112710305"><a name="b16461112710305"></a><a name="b16461112710305"></a>server_protocol</strong>, <strong id="b164611827123010"><a name="b164611827123010"></a><a name="b164611827123010"></a>address</strong>, and <strong id="b7461627153012"><a name="b7461627153012"></a><a name="b7461627153012"></a>port</strong> fields.</p>
</td>
</tr>
<tr id="row984303131517"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p1284393110156"><a name="p1284393110156"></a><a name="p1284393110156"></a>sip_header_name</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p3843193112155"><a name="p3843193112155"></a><a name="p3843193112155"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p8843143191518"><a name="p8843143191518"></a><a name="p8843143191518"></a>Specifies the type of the source IP header. This parameter is returned only when <strong id="b2369538269"><a name="b2369538269"></a><a name="b2369538269"></a>proxy</strong> is set to <strong id="b133691938462"><a name="b133691938462"></a><a name="b133691938462"></a>true</strong>.</p>
<p id="p122363442313"><a name="p122363442313"></a><a name="p122363442313"></a>The options are as follows: <strong id="b12673154918103"><a name="b12673154918103"></a><a name="b12673154918103"></a>default</strong>, <strong id="b8673649121017"><a name="b8673649121017"></a><a name="b8673649121017"></a>cloudflare</strong>, <strong id="b1267304971019"><a name="b1267304971019"></a><a name="b1267304971019"></a>akamai</strong>, and <strong id="b8673149181012"><a name="b8673149181012"></a><a name="b8673149181012"></a>custom</strong>.</p>
</td>
</tr>
<tr id="row1774735191513"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p127483531514"><a name="p127483531514"></a><a name="p127483531514"></a>sip_header_list</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p174133521513"><a name="p174133521513"></a><a name="p174133521513"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p756019408495"><a name="p756019408495"></a><a name="p756019408495"></a>Specifies the HTTP request header for identifying the real source IP address. This parameter is returned only when <strong id="b56564410615"><a name="b56564410615"></a><a name="b56564410615"></a>proxy</strong> is set to <strong id="b2651844969"><a name="b2651844969"></a><a name="b2651844969"></a>true</strong>.</p>
<a name="ul2880124694920"></a><a name="ul2880124694920"></a><ul id="ul2880124694920"><li>If <strong id="b141718451262"><a name="b141718451262"></a><a name="b141718451262"></a>sip_header_name</strong> is <strong id="b84174453618"><a name="b84174453618"></a><a name="b84174453618"></a>default</strong>, <strong id="b14249451465"><a name="b14249451465"></a><a name="b14249451465"></a>sip_header_list</strong> is <strong id="b19424164516610"><a name="b19424164516610"></a><a name="b19424164516610"></a>["X-Forwarded-For"]</strong>.</li><li>If <strong id="b152968222540"><a name="b152968222540"></a><a name="b152968222540"></a>sip_header_name</strong> is <strong id="b14296122125412"><a name="b14296122125412"></a><a name="b14296122125412"></a>cloudflare</strong>, <strong id="b1229612219544"><a name="b1229612219544"></a><a name="b1229612219544"></a>sip_header_list</strong> is <strong id="b830418224545"><a name="b830418224545"></a><a name="b830418224545"></a>["CF-Connecting-IP", "X-Forwarded-For"]</strong>.</li><li>If <strong id="b17901058161016"><a name="b17901058161016"></a><a name="b17901058161016"></a>sip_header_name</strong> is <strong id="b879065861011"><a name="b879065861011"></a><a name="b879065861011"></a>akamai</strong>, <strong id="b13790205820103"><a name="b13790205820103"></a><a name="b13790205820103"></a>sip_header_list</strong> is <strong id="b479014582102"><a name="b479014582102"></a><a name="b479014582102"></a>["True-Client-IP"]</strong>.</li><li>If <strong id="b1697113511769"><a name="b1697113511769"></a><a name="b1697113511769"></a>sip_header_name</strong> is <strong id="b0978165120616"><a name="b0978165120616"></a><a name="b0978165120616"></a>custom</strong>, you can customize a value.</li></ul>
</td>
</tr>
<tr id="row16988409"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p33883878"><a name="p33883878"></a><a name="p33883878"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p60239579"><a name="p60239579"></a><a name="p60239579"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p47567745"><a name="p47567745"></a><a name="p47567745"></a>Specifies the time when a domain name is created.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section19913183183016"></a>

**www.b.com**  is used as an example.

-   Request example

    ```
    {
      "hostname": "www.b.com",
      "certificate_id": "07fb6809a89241fca86ac6f69e34963d",
      "server": [
          {"client_protocol": "HTTPS", "server_protocol": "HTTP", "address": "X.X.X.X", "port": "8080"},
          {"client_protocol": "HTTP", "server_protocol": "HTTP", "address": "X.X.X.X", "port": "80"}
       ],
      "proxy": true,
      "sip_header_name": "default",
      "sip_header_list": ["X-Forwarded-For"]
    }
    ```


-   Response example

    ```
    {
              "id": "388a7789d55b41d1918b3088a8f1e7f3",
              "hostname": "www.b.com",
              "cname": "3249d21e5eb34d21be12fdc817fcb67d.waf.cloud.com",
              "txt_code": "3249d21e5eb34d21be12fdc817fcb67d",
              "sub_domain": "3249d21e5eb34d21be12fdc817fcb67d.www.b.com",
              "policy_id": "xxxxxxxxxxxxxx",
              "certificate_id": "xxxxxxxxxxxxxxxxxxx",
              "protect_status": 0,
              "access_status": 0,
              "protocol": "HTTP,HTTPS",
              "server": [
                 {"client_protocol": "HTTPS", "server_protocol":"HTTP", "address":"X.X.X.X", "port":443},
                 {"client_protocol": "HTTP", "server_protocol":"HTTP", "address":"X.X.X.X", "port":80}
              ],
             "proxy": true,
             "sip_header_name": "default",
             "sip_header_list": ["X-Forwarded-For"],
             "timestamp": 1499817600
    }
    ```


## Status Code<a name="section50347087"></a>

[Table 4](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  4**  Status code

<a name="en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0"></a>
<table><thead align="left"><tr id="en-us_topic_0193631139_r3d6e2f205c444705bdbb9daaac74e575"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"><a name="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"></a><a name="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="19.41%" id="mcps1.2.4.1.2"><p id="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"><a name="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"></a><a name="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"></a>Meaning</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0193631139_rc7b2adc390904a1ba79e303017797786"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"><a name="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"></a><a name="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="19.41%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"></a>The request has succeeded.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).

