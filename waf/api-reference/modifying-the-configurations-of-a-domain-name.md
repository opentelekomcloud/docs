# Modifying the Configurations of a Domain Name<a name="EN-US_TOPIC_0193630658"></a>

## Function Description<a name="section58977142"></a>

This API is used to modify basic configurations of a domain name.

## URI<a name="section61032237"></a>

-   URI format

    PUT  /v1/\{project\_id\}/waf/instance/\{instance\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table29810584"></a>
    <table><thead align="left"><tr id="row53142603"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p9583549"><a name="p9583549"></a><a name="p9583549"></a><strong id="b166311362714"><a name="b166311362714"></a><a name="b166311362714"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p38070020"><a name="p38070020"></a><a name="p38070020"></a><strong id="b101787140273"><a name="b101787140273"></a><a name="b101787140273"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p63772808"><a name="p63772808"></a><a name="p63772808"></a><strong id="b194612154278"><a name="b194612154278"></a><a name="b194612154278"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p65323824"><a name="p65323824"></a><a name="p65323824"></a><strong id="b8881515112712"><a name="b8881515112712"></a><a name="b8881515112712"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56738405"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p32408078"><a name="p32408078"></a><a name="p32408078"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p7808660"><a name="p7808660"></a><a name="p7808660"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p28521694"><a name="p28521694"></a><a name="p28521694"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p28555860"><a name="p28555860"></a><a name="p28555860"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row55676156"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p13474784"><a name="p13474784"></a><a name="p13474784"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p17715749"><a name="p17715749"></a><a name="p17715749"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p25689587"><a name="p25689587"></a><a name="p25689587"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p481777"><a name="p481777"></a><a name="p481777"></a>Specifies the instance ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section12419223"></a>

Request parameters

**Table  2**  Parameter description

<a name="table61405329"></a>
<table><thead align="left"><tr id="row58888607"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p5247824"><a name="p5247824"></a><a name="p5247824"></a><strong id="b147061432122716"><a name="b147061432122716"></a><a name="b147061432122716"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p22420594"><a name="p22420594"></a><a name="p22420594"></a><strong id="b1674612330272"><a name="b1674612330272"></a><a name="b1674612330272"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p4128812"><a name="p4128812"></a><a name="p4128812"></a><strong id="b4824173417273"><a name="b4824173417273"></a><a name="b4824173417273"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p65998375"><a name="p65998375"></a><a name="p65998375"></a><strong id="b169721035152715"><a name="b169721035152715"></a><a name="b169721035152715"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row44268171"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p28952062"><a name="p28952062"></a><a name="p28952062"></a>certificate_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p63415723"><a name="p63415723"></a><a name="p63415723"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p36399928"><a name="p36399928"></a><a name="p36399928"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p62713037"><a name="p62713037"></a><a name="p62713037"></a>Specifies the certificate ID. This parameter is not required when <span class="parmname" id="parmname97183673816"><a name="parmname97183673816"></a><a name="parmname97183673816"></a><b>client_protocol</b></span> is set to <strong id="b15739115919478"><a name="b15739115919478"></a><a name="b15739115919478"></a>HTTP</strong>.</p>
</td>
</tr>
<tr id="row27546427"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p16668080"><a name="p16668080"></a><a name="p16668080"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p7937217"><a name="p7937217"></a><a name="p7937217"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p38934872"><a name="p38934872"></a><a name="p38934872"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p12362191310286"><a name="p12362191310286"></a><a name="p12362191310286"></a>Specifies the origin server information, including the <strong id="b960413271392"><a name="b960413271392"></a><a name="b960413271392"></a>client_protocol</strong>, <strong id="b3605112723913"><a name="b3605112723913"></a><a name="b3605112723913"></a>server_protocol</strong>, <strong id="b5605627193911"><a name="b5605627193911"></a><a name="b5605627193911"></a>address</strong>, and <strong id="b116067278391"><a name="b116067278391"></a><a name="b116067278391"></a>port</strong> fields.</p>
<a name="ul5701341115010"></a><a name="ul5701341115010"></a><ul id="ul5701341115010"><li><span class="parmvalue" id="parmvalue5429103163913"><a name="parmvalue5429103163913"></a><a name="parmvalue5429103163913"></a><b>client_protocol</b></span>: protocol type of the client. The options are <strong id="b889454497"><a name="b889454497"></a><a name="b889454497"></a>HTTP</strong> and <strong id="b15891456494"><a name="b15891456494"></a><a name="b15891456494"></a>HTTPS</strong>.</li><li><strong id="b11892173915394"><a name="b11892173915394"></a><a name="b11892173915394"></a>server_protocol</strong>: protocol used by WAF to forward client requests to the server. The options are <strong id="b547169134910"><a name="b547169134910"></a><a name="b547169134910"></a>HTTP</strong> and <strong id="b94718934919"><a name="b94718934919"></a><a name="b94718934919"></a>HTTPS</strong>.</li><li><strong id="b916292921813"><a name="b916292921813"></a><a name="b916292921813"></a>address</strong>: public IP address or domain name of the web server that the client accesses</li><li><strong id="b56621433151810"><a name="b56621433151810"></a><a name="b56621433151810"></a>port</strong>: port number used by the web server. The value ranges from <strong id="b19662103318187"><a name="b19662103318187"></a><a name="b19662103318187"></a>0</strong> to <strong id="b1766293371815"><a name="b1766293371815"></a><a name="b1766293371815"></a>65535</strong>, for example, <strong id="b0662113317189"><a name="b0662113317189"></a><a name="b0662113317189"></a>8080</strong>.</li></ul>
</td>
</tr>
<tr id="row63581104"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p49795776"><a name="p49795776"></a><a name="p49795776"></a>proxy</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p6926065"><a name="p6926065"></a><a name="p6926065"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p24140394"><a name="p24140394"></a><a name="p24140394"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p9214932"><a name="p9214932"></a><a name="p9214932"></a>Specifies whether a proxy is configured.</p>
<a name="ul1189171615367"></a><a name="ul1189171615367"></a><ul id="ul1189171615367"><li><strong id="b19830161304918"><a name="b19830161304918"></a><a name="b19830161304918"></a>true</strong>: A proxy is configured.</li><li><strong id="b105678449496"><a name="b105678449496"></a><a name="b105678449496"></a>false</strong>: No proxy is configured.</li></ul>
</td>
</tr>
<tr id="row1631512311233"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p63151923102314"><a name="p63151923102314"></a><a name="p63151923102314"></a>sip_header_name</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p231572352318"><a name="p231572352318"></a><a name="p231572352318"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p1331572392314"><a name="p1331572392314"></a><a name="p1331572392314"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p8843143191518"><a name="p8843143191518"></a><a name="p8843143191518"></a>Specifies the type of the source IP header. This parameter is required only when <strong id="b15170142152310"><a name="b15170142152310"></a><a name="b15170142152310"></a>proxy</strong> is set to <strong id="b191708272312"><a name="b191708272312"></a><a name="b191708272312"></a>true</strong>.</p>
<p id="p122363442313"><a name="p122363442313"></a><a name="p122363442313"></a>The options are as follows: <strong id="b610714183495"><a name="b610714183495"></a><a name="b610714183495"></a>default</strong>, <strong id="b151221918144913"><a name="b151221918144913"></a><a name="b151221918144913"></a>cloudflare</strong>, <strong id="b8122218134910"><a name="b8122218134910"></a><a name="b8122218134910"></a>akamai</strong>, and <strong id="b20122161816491"><a name="b20122161816491"></a><a name="b20122161816491"></a>custom</strong>.</p>
</td>
</tr>
<tr id="row4830172582314"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p108311025182319"><a name="p108311025182319"></a><a name="p108311025182319"></a>sip_header_list</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p7831825122318"><a name="p7831825122318"></a><a name="p7831825122318"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p168311925182315"><a name="p168311925182315"></a><a name="p168311925182315"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p1962095241420"><a name="p1962095241420"></a><a name="p1962095241420"></a>Specifies the HTTP request header for identifying the real source IP address. This parameter is required only when <strong id="b13498178152318"><a name="b13498178152318"></a><a name="b13498178152318"></a>proxy</strong> is set to <strong id="b174985816238"><a name="b174985816238"></a><a name="b174985816238"></a>true</strong>.</p>
<a name="ul1757412912176"></a><a name="ul1757412912176"></a><ul id="ul1757412912176"><li>If <strong id="b423281072319"><a name="b423281072319"></a><a name="b423281072319"></a>sip_header_name</strong> is <strong id="b9232161032313"><a name="b9232161032313"></a><a name="b9232161032313"></a>default</strong>, <strong id="b13232710192314"><a name="b13232710192314"></a><a name="b13232710192314"></a>sip_header_list</strong> is <strong id="b223241092313"><a name="b223241092313"></a><a name="b223241092313"></a>["X-Forwarded-For"]</strong>.</li><li>If <strong id="b96434579549"><a name="b96434579549"></a><a name="b96434579549"></a>sip_header_name</strong> is <strong id="b264385795412"><a name="b264385795412"></a><a name="b264385795412"></a>cloudflare</strong>, <strong id="b6643125755419"><a name="b6643125755419"></a><a name="b6643125755419"></a>sip_header_list</strong> is <strong id="b16643145735419"><a name="b16643145735419"></a><a name="b16643145735419"></a>["CF-Connecting-IP", "X-Forwarded-For"]</strong>.</li><li>If <strong id="b11839195113117"><a name="b11839195113117"></a><a name="b11839195113117"></a>sip_header_name</strong> is <strong id="b15839951121113"><a name="b15839951121113"></a><a name="b15839951121113"></a>akamai</strong>, <strong id="b4839751131117"><a name="b4839751131117"></a><a name="b4839751131117"></a>sip_header_list</strong> is <strong id="b1083995110115"><a name="b1083995110115"></a><a name="b1083995110115"></a>["True-Client-IP"]</strong>.</li><li>If <strong id="b10521161712236"><a name="b10521161712236"></a><a name="b10521161712236"></a>sip_header_name</strong> is <strong id="b20521317132319"><a name="b20521317132319"></a><a name="b20521317132319"></a>custom</strong>, you can customize a value.</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section44664151"></a>

Response parameters

**Table  3**  Parameter description

<a name="table57985477"></a>
<table><thead align="left"><tr id="row6696138"><th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.4.1.1"><p id="p5516328"><a name="p5516328"></a><a name="p5516328"></a><strong id="b7739133422810"><a name="b7739133422810"></a><a name="b7739133422810"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.2"><p id="p44169398"><a name="p44169398"></a><a name="p44169398"></a><strong id="b9568735132819"><a name="b9568735132819"></a><a name="b9568735132819"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="58.160000000000004%" id="mcps1.2.4.1.3"><p id="p20951452"><a name="p20951452"></a><a name="p20951452"></a><strong id="b20310173622814"><a name="b20310173622814"></a><a name="b20310173622814"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row54345344"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p39896734"><a name="p39896734"></a><a name="p39896734"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p10410025"><a name="p10410025"></a><a name="p10410025"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p37905672"><a name="p37905672"></a><a name="p37905672"></a>Specifies the domain ID.</p>
</td>
</tr>
<tr id="row5606731"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p51492036"><a name="p51492036"></a><a name="p51492036"></a>hostname</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p10105349"><a name="p10105349"></a><a name="p10105349"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p8980385"><a name="p8980385"></a><a name="p8980385"></a>Specifies the domain name.</p>
</td>
</tr>
<tr id="row102041951183518"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p820435117357"><a name="p820435117357"></a><a name="p820435117357"></a>cname</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p12204151153517"><a name="p12204151153517"></a><a name="p12204151153517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p4371234161716"><a name="p4371234161716"></a><a name="p4371234161716"></a>Specifies the CNAME value. For example, <strong id="b171451387014"><a name="b171451387014"></a><a name="b171451387014"></a>efec1196267b41c399f2980ea4048517.waf.cloud.com</strong>.</p>
</td>
</tr>
<tr id="row122121655183513"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p421345518358"><a name="p421345518358"></a><a name="p421345518358"></a>txt_code</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p1021385519357"><a name="p1021385519357"></a><a name="p1021385519357"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p1549244121814"><a name="p1549244121814"></a><a name="p1549244121814"></a>Specifies the TXT record. This parameter is returned only when <strong id="b131621730145016"><a name="b131621730145016"></a><a name="b131621730145016"></a>proxy</strong> is set to <strong id="b716233019507"><a name="b716233019507"></a><a name="b716233019507"></a>true</strong>.</p>
</td>
</tr>
<tr id="row1129619073614"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p1129612011363"><a name="p1129612011363"></a><a name="p1129612011363"></a>sub_domain</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p1529620193613"><a name="p1529620193613"></a><a name="p1529620193613"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p673423131814"><a name="p673423131814"></a><a name="p673423131814"></a>Specifies the subdomain name. This parameter is returned only when <strong id="b7754126105112"><a name="b7754126105112"></a><a name="b7754126105112"></a>proxy</strong> is set to <strong id="b675410645114"><a name="b675410645114"></a><a name="b675410645114"></a>true</strong>.</p>
</td>
</tr>
<tr id="row30818691"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p13286080"><a name="p13286080"></a><a name="p13286080"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p2430685"><a name="p2430685"></a><a name="p2430685"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p62667778"><a name="p62667778"></a><a name="p62667778"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row27139096"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p50783133"><a name="p50783133"></a><a name="p50783133"></a>protect_status</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p19793086"><a name="p19793086"></a><a name="p19793086"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p8515133844011"><a name="p8515133844011"></a><a name="p8515133844011"></a>Specifies the WAF mode.</p>
<a name="ul137579456408"></a><a name="ul137579456408"></a><ul id="ul137579456408"><li><strong id="b65782041182"><a name="b65782041182"></a><a name="b65782041182"></a>0</strong>: disabled.</li><li><strong id="b1425419278555"><a name="b1425419278555"></a><a name="b1425419278555"></a>1</strong>: enabled.</li><li><span class="parmvalue" id="parmvalue1023875662014"><a name="parmvalue1023875662014"></a><a name="parmvalue1023875662014"></a><b>-1</b></span>: bypassed.</li></ul>
</td>
</tr>
<tr id="row754573"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p61120437"><a name="p61120437"></a><a name="p61120437"></a>access_status</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p51808341"><a name="p51808341"></a><a name="p51808341"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p19585656134117"><a name="p19585656134117"></a><a name="p19585656134117"></a>Specifies whether a domain name is connected to WAF.</p>
<a name="ul39582516425"></a><a name="ul39582516425"></a><ul id="ul39582516425"><li><strong id="b197744176015"><a name="b197744176015"></a><a name="b197744176015"></a>0</strong>: The domain name is not connected to WAF.</li><li><strong id="b73364211508"><a name="b73364211508"></a><a name="b73364211508"></a>1</strong>: The domain name is connected to WAF.</li></ul>
</td>
</tr>
<tr id="row53099466"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p6089503"><a name="p6089503"></a><a name="p6089503"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p23487720"><a name="p23487720"></a><a name="p23487720"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p23457166"><a name="p23457166"></a><a name="p23457166"></a>Specifies the protocol type. The options are <strong id="b2311174020112"><a name="b2311174020112"></a><a name="b2311174020112"></a>HTTP</strong>, <strong id="b153118401912"><a name="b153118401912"></a><a name="b153118401912"></a>HTTPS</strong>, and <span class="parmvalue" id="parmvalue13678161104010"><a name="parmvalue13678161104010"></a><a name="parmvalue13678161104010"></a><b>HTTP,HTTPS</b></span>.</p>
</td>
</tr>
<tr id="row9787903"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p54622650"><a name="p54622650"></a><a name="p54622650"></a>certificate_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p62358534"><a name="p62358534"></a><a name="p62358534"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p17876490"><a name="p17876490"></a><a name="p17876490"></a>Specifies the certificate ID. This parameter is returned only when <strong id="b192544511"><a name="b192544511"></a><a name="b192544511"></a>protocol</strong> is set to <strong id="b12926441617"><a name="b12926441617"></a><a name="b12926441617"></a>HTTPS</strong>.</p>
</td>
</tr>
<tr id="row26670689"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p12842221"><a name="p12842221"></a><a name="p12842221"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p33587014"><a name="p33587014"></a><a name="p33587014"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p36193619"><a name="p36193619"></a><a name="p36193619"></a>Specifies the origin server information, including the <strong id="b696551314212"><a name="b696551314212"></a><a name="b696551314212"></a>client_protocol</strong>, <strong id="b496541314217"><a name="b496541314217"></a><a name="b496541314217"></a>server_protocol</strong>, <strong id="b69652013126"><a name="b69652013126"></a><a name="b69652013126"></a>address</strong>, and <strong id="b1965181310219"><a name="b1965181310219"></a><a name="b1965181310219"></a>port</strong> fields.</p>
</td>
</tr>
<tr id="row57307121"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p11365224"><a name="p11365224"></a><a name="p11365224"></a>proxy</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p48167943"><a name="p48167943"></a><a name="p48167943"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p10924103854314"><a name="p10924103854314"></a><a name="p10924103854314"></a>Specifies whether a proxy is configured.</p>
<a name="ul16743155117444"></a><a name="ul16743155117444"></a><ul id="ul16743155117444"><li><strong id="b16618225135011"><a name="b16618225135011"></a><a name="b16618225135011"></a>true</strong>: A proxy is configured.</li><li><strong id="b163017298504"><a name="b163017298504"></a><a name="b163017298504"></a>false</strong>: No proxy is configured.</li></ul>
</td>
</tr>
<tr id="row46256269250"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p10626132613253"><a name="p10626132613253"></a><a name="p10626132613253"></a>sip_header_name</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p462652617256"><a name="p462652617256"></a><a name="p462652617256"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p6626926142515"><a name="p6626926142515"></a><a name="p6626926142515"></a>Specifies the type of the source IP header. This parameter is returned only when <strong id="b01631203239"><a name="b01631203239"></a><a name="b01631203239"></a>proxy</strong> is set to <strong id="b111701920112316"><a name="b111701920112316"></a><a name="b111701920112316"></a>true</strong>.</p>
<p id="p20672019124820"><a name="p20672019124820"></a><a name="p20672019124820"></a>The options are as follows: <strong id="b461813273385"><a name="b461813273385"></a><a name="b461813273385"></a>default</strong>, <strong id="b1161862716380"><a name="b1161862716380"></a><a name="b1161862716380"></a>cloudflare</strong>, <strong id="b761814274382"><a name="b761814274382"></a><a name="b761814274382"></a>akamai</strong>, and <strong id="b6618142733811"><a name="b6618142733811"></a><a name="b6618142733811"></a>custom</strong>.</p>
</td>
</tr>
<tr id="row1434123116252"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p1341123113252"><a name="p1341123113252"></a><a name="p1341123113252"></a>sip_header_list</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p17342183115258"><a name="p17342183115258"></a><a name="p17342183115258"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p123092211264"><a name="p123092211264"></a><a name="p123092211264"></a>Specifies the HTTP request header for identifying the real source IP address. This parameter is returned only when <strong id="b3179102612316"><a name="b3179102612316"></a><a name="b3179102612316"></a>proxy</strong> is set to <strong id="b13179726102316"><a name="b13179726102316"></a><a name="b13179726102316"></a>true</strong>.</p>
<a name="ul13577174214502"></a><a name="ul13577174214502"></a><ul id="ul13577174214502"><li>If <strong id="b940412814236"><a name="b940412814236"></a><a name="b940412814236"></a>sip_header_name</strong> is <strong id="b16404228112316"><a name="b16404228112316"></a><a name="b16404228112316"></a>default</strong>, <strong id="b13404102819233"><a name="b13404102819233"></a><a name="b13404102819233"></a>sip_header_list</strong> is <strong id="b1540442815236"><a name="b1540442815236"></a><a name="b1540442815236"></a>["X-Forwarded-For"]</strong>.</li><li>If <strong id="b194721914557"><a name="b194721914557"></a><a name="b194721914557"></a>sip_header_name</strong> is <strong id="b1847901195513"><a name="b1847901195513"></a><a name="b1847901195513"></a>cloudflare</strong>, <strong id="b44796195517"><a name="b44796195517"></a><a name="b44796195517"></a>sip_header_list</strong> is <strong id="b74795155510"><a name="b74795155510"></a><a name="b74795155510"></a>["CF-Connecting-IP", "X-Forwarded-For"]</strong>.</li><li>If <strong id="b317120651215"><a name="b317120651215"></a><a name="b317120651215"></a>sip_header_name</strong> is <strong id="b417196131220"><a name="b417196131220"></a><a name="b417196131220"></a>akamai</strong>, <strong id="b15179106201217"><a name="b15179106201217"></a><a name="b15179106201217"></a>sip_header_list</strong> is <strong id="b171793631218"><a name="b171793631218"></a><a name="b171793631218"></a>["True-Client-IP"]</strong>.</li><li>If <strong id="b1845535132317"><a name="b1845535132317"></a><a name="b1845535132317"></a>sip_header_name</strong> is <strong id="b84512351232"><a name="b84512351232"></a><a name="b84512351232"></a>custom</strong>, you can customize a value.</li></ul>
</td>
</tr>
<tr id="row16495157"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p61039329"><a name="p61039329"></a><a name="p61039329"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p45238577"><a name="p45238577"></a><a name="p45238577"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p40446093"><a name="p40446093"></a><a name="p40446093"></a>Specifies the time when a domain name is created.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section9725142733211"></a>

**www.a.com**  is used as an example.

-   Request example

    ```
    {
      "certificate_id": "07fb6809a89241fca86ac6f69e34963d", 
      "server": [
          {"client_protocol": "HTTPS","server_protocol": "HTTP", "address": "X.X.X.X","port": "8080"},
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
              "hostname": "www.a.com",
              
              "cname": "3249d21e5eb34d21be12fdc817fcb67d.wafcloud.com",
              "txt_code": "3249d21e5eb34d21be12fdc817fcb67d",
              "sub_domain": "3249d21e5eb34d21be12fdc817fcb67d.www.a.com",
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


## Status Code<a name="section66433045"></a>

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

