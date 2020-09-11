# Querying a Domain Name<a name="EN-US_TOPIC_0193631166"></a>

## Function Description<a name="section15255239"></a>

This API is used to query details about a domain name.

## URI<a name="section3079425"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/instance/\{instance\_id\}

-   Parameter description

    **Table  1**  Path parameters

    <a name="table24910021"></a>
    <table><thead align="left"><tr id="row56986579"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p52510190"><a name="p52510190"></a><a name="p52510190"></a><strong id="b86911019172"><a name="b86911019172"></a><a name="b86911019172"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p25466973"><a name="p25466973"></a><a name="p25466973"></a><strong id="b194711121715"><a name="b194711121715"></a><a name="b194711121715"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p49558921"><a name="p49558921"></a><a name="p49558921"></a><strong id="b99841119179"><a name="b99841119179"></a><a name="b99841119179"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p54849625"><a name="p54849625"></a><a name="p54849625"></a><strong id="b1394502161718"><a name="b1394502161718"></a><a name="b1394502161718"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13634613"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p30661894"><a name="p30661894"></a><a name="p30661894"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p585524"><a name="p585524"></a><a name="p585524"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p47427494"><a name="p47427494"></a><a name="p47427494"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p16421829"><a name="p16421829"></a><a name="p16421829"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row13578736"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p26135869"><a name="p26135869"></a><a name="p26135869"></a>instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p36630634"><a name="p36630634"></a><a name="p36630634"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p14291359"><a name="p14291359"></a><a name="p14291359"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p16749445"><a name="p16749445"></a><a name="p16749445"></a>Specifies the instance ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section27714832"></a>

Request parameters

None

## Response<a name="section48106900"></a>

Response parameters

**Table  2**  Parameter description

<a name="table22387562"></a>
<table><thead align="left"><tr id="row5105955"><th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.4.1.1"><p id="p10929212"><a name="p10929212"></a><a name="p10929212"></a><strong id="b6281112421713"><a name="b6281112421713"></a><a name="b6281112421713"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.2"><p id="p12851014"><a name="p12851014"></a><a name="p12851014"></a><strong id="b1312112591713"><a name="b1312112591713"></a><a name="b1312112591713"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="58.160000000000004%" id="mcps1.2.4.1.3"><p id="p34299241"><a name="p34299241"></a><a name="p34299241"></a><strong id="b33110268173"><a name="b33110268173"></a><a name="b33110268173"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row40257715"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p39649453"><a name="p39649453"></a><a name="p39649453"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p57489107"><a name="p57489107"></a><a name="p57489107"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p26106127"><a name="p26106127"></a><a name="p26106127"></a>Specifies the instance ID.</p>
</td>
</tr>
<tr id="row33628551"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p39558140"><a name="p39558140"></a><a name="p39558140"></a>hostname</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p50092794"><a name="p50092794"></a><a name="p50092794"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p30984488"><a name="p30984488"></a><a name="p30984488"></a>Specifies the domain name.</p>
</td>
</tr>
<tr id="row13252189236"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p6325518202315"><a name="p6325518202315"></a><a name="p6325518202315"></a>cname</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p5325101817231"><a name="p5325101817231"></a><a name="p5325101817231"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p4371234161716"><a name="p4371234161716"></a><a name="p4371234161716"></a>Specifies the CNAME value. For example, <strong id="b84254427588"><a name="b84254427588"></a><a name="b84254427588"></a>efec1196267b41c399f2980ea4048517.waf.cloud.com</strong>.</p>
</td>
</tr>
<tr id="row1061123613237"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p76111836172320"><a name="p76111836172320"></a><a name="p76111836172320"></a>txt_code</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p186113367236"><a name="p186113367236"></a><a name="p186113367236"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p1549244121814"><a name="p1549244121814"></a><a name="p1549244121814"></a>Specifies the TXT record. This parameter is returned only when <strong id="b16886185603417"><a name="b16886185603417"></a><a name="b16886185603417"></a>proxy</strong> is set to <strong id="b1688613562344"><a name="b1688613562344"></a><a name="b1688613562344"></a>true</strong>.</p>
</td>
</tr>
<tr id="row13187202562410"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p618772592414"><a name="p618772592414"></a><a name="p618772592414"></a>sub_domain</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p6187112511242"><a name="p6187112511242"></a><a name="p6187112511242"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p673423131814"><a name="p673423131814"></a><a name="p673423131814"></a>Specifies the subdomain name. This parameter is returned only when <strong id="b1896310417351"><a name="b1896310417351"></a><a name="b1896310417351"></a>proxy</strong> is set to <strong id="b8972646353"><a name="b8972646353"></a><a name="b8972646353"></a>true</strong>.</p>
</td>
</tr>
<tr id="row61883492"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p46506973"><a name="p46506973"></a><a name="p46506973"></a>policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p8968438"><a name="p8968438"></a><a name="p8968438"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p55354839"><a name="p55354839"></a><a name="p55354839"></a>Specifies the policy ID.</p>
</td>
</tr>
<tr id="row28431506"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p21250675"><a name="p21250675"></a><a name="p21250675"></a>protect_status</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p43583153"><a name="p43583153"></a><a name="p43583153"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p357818332332"><a name="p357818332332"></a><a name="p357818332332"></a>Specifies the WAF mode.</p>
<a name="ul1373411430338"></a><a name="ul1373411430338"></a><ul id="ul1373411430338"><li><strong id="b157181631132019"><a name="b157181631132019"></a><a name="b157181631132019"></a>0</strong>: disabled.</li><li><strong id="b8191614133514"><a name="b8191614133514"></a><a name="b8191614133514"></a>1</strong>: enabled.</li><li><span class="parmvalue" id="parmvalue144051534142011"><a name="parmvalue144051534142011"></a><a name="parmvalue144051534142011"></a><b>-1</b></span>: bypassed.</li></ul>
</td>
</tr>
<tr id="row29626322"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p50921845"><a name="p50921845"></a><a name="p50921845"></a>access_status</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p31028818"><a name="p31028818"></a><a name="p31028818"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p78861505348"><a name="p78861505348"></a><a name="p78861505348"></a>Specifies whether a domain name is connected to WAF.</p>
<a name="ul74320843410"></a><a name="ul74320843410"></a><ul id="ul74320843410"><li><strong id="b501859155819"><a name="b501859155819"></a><a name="b501859155819"></a>0</strong>: The domain name is not connected to WAF.</li><li><strong id="b1425715320595"><a name="b1425715320595"></a><a name="b1425715320595"></a>1</strong>: The domain name is connected to WAF.</li></ul>
</td>
</tr>
<tr id="row4321417"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p14490490"><a name="p14490490"></a><a name="p14490490"></a>protocol</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p32879007"><a name="p32879007"></a><a name="p32879007"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p45953888"><a name="p45953888"></a><a name="p45953888"></a>Specifies the protocol type. The options are <strong id="b7379610181819"><a name="b7379610181819"></a><a name="b7379610181819"></a>HTTP</strong>, <strong id="b81341314171816"><a name="b81341314171816"></a><a name="b81341314171816"></a>HTTPS</strong>, and <span class="parmvalue" id="parmvalue13678161104010"><a name="parmvalue13678161104010"></a><a name="parmvalue13678161104010"></a><b>HTTP,HTTPS</b></span>.</p>
</td>
</tr>
<tr id="row10931815"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p13061855"><a name="p13061855"></a><a name="p13061855"></a>certificate_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p51377319"><a name="p51377319"></a><a name="p51377319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p813287"><a name="p813287"></a><a name="p813287"></a>Specifies the certificate ID. This parameter is returned only when <span class="parmname" id="parmname8201329183410"><a name="parmname8201329183410"></a><a name="parmname8201329183410"></a><b>client_protocol</b></span> is set to <strong id="b106561718732"><a name="b106561718732"></a><a name="b106561718732"></a>HTTPS</strong>.</p>
</td>
</tr>
<tr id="row7319588"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p56015756"><a name="p56015756"></a><a name="p56015756"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p40982401"><a name="p40982401"></a><a name="p40982401"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p2055605"><a name="p2055605"></a><a name="p2055605"></a>Specifies the origin server information, including the <strong id="b31981217203812"><a name="b31981217203812"></a><a name="b31981217203812"></a>client_protocol</strong>, <strong id="b1519871711380"><a name="b1519871711380"></a><a name="b1519871711380"></a>server_protocol</strong>, <strong id="b121991175384"><a name="b121991175384"></a><a name="b121991175384"></a>address</strong>, and <strong id="b1199161783816"><a name="b1199161783816"></a><a name="b1199161783816"></a>port</strong> fields.</p>
<a name="ul5701341115010"></a><a name="ul5701341115010"></a><ul id="ul5701341115010"><li><span class="parmvalue" id="parmvalue19392228383"><a name="parmvalue19392228383"></a><a name="parmvalue19392228383"></a><b>client_protocol</b></span>: protocol type of the client. The options are <strong id="b756418155367"><a name="b756418155367"></a><a name="b756418155367"></a>HTTP</strong> and <strong id="b756411154364"><a name="b756411154364"></a><a name="b756411154364"></a>HTTPS</strong>.</li><li><strong id="b486515125010"><a name="b486515125010"></a><a name="b486515125010"></a>server_protocol</strong>: protocol used by WAF to forward client requests to the server. The options are <strong id="b1951782273611"><a name="b1951782273611"></a><a name="b1951782273611"></a>HTTP</strong> and <strong id="b851772203610"><a name="b851772203610"></a><a name="b851772203610"></a>HTTPS</strong>.</li><li><strong id="b1535137181713"><a name="b1535137181713"></a><a name="b1535137181713"></a>address</strong>: public IP address or domain name of the web server that the client accesses</li><li><strong id="b132544453177"><a name="b132544453177"></a><a name="b132544453177"></a>port</strong>: port number used by the web server. The value ranges from <strong id="b825414451176"><a name="b825414451176"></a><a name="b825414451176"></a>0</strong> to <strong id="b172541459179"><a name="b172541459179"></a><a name="b172541459179"></a>65535</strong>, for example, <strong id="b112548451173"><a name="b112548451173"></a><a name="b112548451173"></a>8080</strong>.</li></ul>
</td>
</tr>
<tr id="row12726078"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p24179377"><a name="p24179377"></a><a name="p24179377"></a>proxy</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p12372492"><a name="p12372492"></a><a name="p12372492"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p32316963618"><a name="p32316963618"></a><a name="p32316963618"></a>Specifies whether a proxy is configured.</p>
<a name="ul1189171615367"></a><a name="ul1189171615367"></a><ul id="ul1189171615367"><li><strong id="b31813819205"><a name="b31813819205"></a><a name="b31813819205"></a>true</strong>: A proxy is configured.</li><li><strong id="b19631822200"><a name="b19631822200"></a><a name="b19631822200"></a>false</strong>: No proxy is configured.</li></ul>
</td>
</tr>
<tr id="row9980155952118"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p19980459162112"><a name="p19980459162112"></a><a name="p19980459162112"></a>sip_header_name</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p39804595216"><a name="p39804595216"></a><a name="p39804595216"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p18980135915210"><a name="p18980135915210"></a><a name="p18980135915210"></a>Specifies the type of the source IP header. This parameter is returned only when <strong id="b758185915216"><a name="b758185915216"></a><a name="b758185915216"></a>proxy</strong> is set to <strong id="b1758114599217"><a name="b1758114599217"></a><a name="b1758114599217"></a>true</strong>.</p>
<p id="p122363442313"><a name="p122363442313"></a><a name="p122363442313"></a>The options are as follows: <strong id="b434311116417"><a name="b434311116417"></a><a name="b434311116417"></a>default</strong>, <strong id="b1634317112414"><a name="b1634317112414"></a><a name="b1634317112414"></a>cloudflare</strong>, <strong id="b173511111743"><a name="b173511111743"></a><a name="b173511111743"></a>akamai</strong>, and <strong id="b835110111845"><a name="b835110111845"></a><a name="b835110111845"></a>custom</strong>.</p>
</td>
</tr>
<tr id="row49071420222"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p59076222211"><a name="p59076222211"></a><a name="p59076222211"></a>sip_header_list</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p7907228225"><a name="p7907228225"></a><a name="p7907228225"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p1962095241420"><a name="p1962095241420"></a><a name="p1962095241420"></a>Specifies the HTTP request header for identifying the real source IP address. This parameter is returned only when <strong id="b1339271422219"><a name="b1339271422219"></a><a name="b1339271422219"></a>proxy</strong> is set to <strong id="b14011914162213"><a name="b14011914162213"></a><a name="b14011914162213"></a>true</strong>.</p>
<a name="ul1757412912176"></a><a name="ul1757412912176"></a><ul id="ul1757412912176"><li>If <strong id="b156811118172213"><a name="b156811118172213"></a><a name="b156811118172213"></a>sip_header_name</strong> is <strong id="b1668111842211"><a name="b1668111842211"></a><a name="b1668111842211"></a>default</strong>, <strong id="b1669019188229"><a name="b1669019188229"></a><a name="b1669019188229"></a>sip_header_list</strong> is <strong id="b126901318192214"><a name="b126901318192214"></a><a name="b126901318192214"></a>["X-Forwarded-For"]</strong>.</li><li>If <strong id="b169704012541"><a name="b169704012541"></a><a name="b169704012541"></a>sip_header_name</strong> is <strong id="b397194010544"><a name="b397194010544"></a><a name="b397194010544"></a>cloudflare</strong>, <strong id="b1597240135414"><a name="b1597240135414"></a><a name="b1597240135414"></a>sip_header_list</strong> is <strong id="b3978408545"><a name="b3978408545"></a><a name="b3978408545"></a>["CF-Connecting-IP", "X-Forwarded-For"]</strong>.</li><li>If <strong id="b192561721141111"><a name="b192561721141111"></a><a name="b192561721141111"></a>sip_header_name</strong> is <strong id="b12256521111114"><a name="b12256521111114"></a><a name="b12256521111114"></a>akamai</strong>, <strong id="b11256821201114"><a name="b11256821201114"></a><a name="b11256821201114"></a>sip_header_list</strong> is <strong id="b025652113115"><a name="b025652113115"></a><a name="b025652113115"></a>["True-Client-IP"]</strong>.</li><li>If <strong id="b1212824272213"><a name="b1212824272213"></a><a name="b1212824272213"></a>sip_header_name</strong> is <strong id="b312864219224"><a name="b312864219224"></a><a name="b312864219224"></a>custom</strong>, you can customize a value.</li></ul>
</td>
</tr>
<tr id="row26959292"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p36219011"><a name="p36219011"></a><a name="p36219011"></a>timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p48058799"><a name="p48058799"></a><a name="p48058799"></a>Long</p>
</td>
<td class="cellrowborder" valign="top" width="58.160000000000004%" headers="mcps1.2.4.1.3 "><p id="p448680"><a name="p448680"></a><a name="p448680"></a>Specifies the time when a domain name is created.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section15404202913319"></a>

**www.a.com**  is used as an example.

Response example

```
{
          "id": "388a7789d55b41d1918b3088a8f1e7f3",
          "hostname": "www.a.com",
          
          "cname": "3249d21e5eb34d21be12fdc817fcb67d.waf.cloud.com",
          "txt_code": "3249d21e5eb34d21be12fdc817fcb67d",
          "sub_domain": "3249d21e5eb34d21be12fdc817fcb67d.www.a.com",
          "policy_id": "xxxxxxxxxxxxxx",
          "certificate_id": "xxxxxxxxxxxxxxxxxxx",
          "protect_status": 0,
          "access_status": 0,
          "protocol": "HTTP,HTTPS",

          "server": [
             {"client_protocol": "HTTPS", "server_protocol":"HTTP", "address":"X.X.X.X.", "port":443},
             {"client_protocol": "HTTP", "server_protocol":"HTTP", "address":"X.X.X.X", "port":80}
          ],
         "proxy": true,
         "sip_header_name": "default",
         "sip_header_list": ["X-Forwarded-For"],
         "timestamp": 1499817600
}
```

## Status Code<a name="section30308918"></a>

[Table 3](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  3**  Status code

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

