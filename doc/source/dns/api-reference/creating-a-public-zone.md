# Creating a Public Zone<a name="EN-US_TOPIC_0057310891"></a>

## Function<a name="section3569153217343"></a>

Create a public zone.

## URI<a name="section6163262617350"></a>

URI format:

POST /v2/zones

## Request<a name="section4207148117353"></a>

-   Parameter description

    **Table  1**  Parameters in the request

    <a name="table3720408817742"></a><table><thead align="left"><tr id="row6225671717742"><th class="cellrowborder" valign="top" width="16.16%" id="mcps1.2.5.1.1"><p id="p5153686617742"><a name="p5153686617742"></a><a name="p5153686617742"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.459999999999997%" id="mcps1.2.5.1.2"><p id="p473035017742"><a name="p473035017742"></a><a name="p473035017742"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.590000000000002%" id="mcps1.2.5.1.3"><p id="p386753717742"><a name="p386753717742"></a><a name="p386753717742"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="52.790000000000006%" id="mcps1.2.5.1.4"><p id="p5956810717742"><a name="p5956810717742"></a><a name="p5956810717742"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1329410717742"><td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.1 "><p id="p3414560317742"><a name="p3414560317742"></a><a name="p3414560317742"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.459999999999997%" headers="mcps1.2.5.1.2 "><p id="p6603174617742"><a name="p6603174617742"></a><a name="p6603174617742"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.590000000000002%" headers="mcps1.2.5.1.3 "><p id="p360216817742"><a name="p360216817742"></a><a name="p360216817742"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.790000000000006%" headers="mcps1.2.5.1.4 "><p id="p2651334817742"><a name="p2651334817742"></a><a name="p2651334817742"></a>Domain name registered with the domain name registrar</p>
    <a name="ul1677295557"></a><a name="ul1677295557"></a><ul id="ul1677295557"><li id="li167529125515"><a name="li167529125515"></a><a name="li167529125515"></a>If a domain name is ended with a dot (.), it cannot exceed 254 characters.</li><li id="li86713293557"><a name="li86713293557"></a><a name="li86713293557"></a>Otherwise, the domain name cannot exceed 253 characters.</li><li id="li3672029115515"><a name="li3672029115515"></a><a name="li3672029115515"></a>Labels of a domain name are separated by dot (.). Each label cannot exceed 63 characters.</li></ul>
    <p id="p3680010615524"><a name="p3680010615524"></a><a name="p3680010615524"></a>A domain name is case insensitive. Uppercase letters will also be converted into lowercase letters.</p>
    </td>
    </tr>
    <tr id="row1973909717742"><td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.1 "><p id="p5474826717742"><a name="p5474826717742"></a><a name="p5474826717742"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.459999999999997%" headers="mcps1.2.5.1.2 "><p id="p759162017742"><a name="p759162017742"></a><a name="p759162017742"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.590000000000002%" headers="mcps1.2.5.1.3 "><p id="p3220634117742"><a name="p3220634117742"></a><a name="p3220634117742"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.790000000000006%" headers="mcps1.2.5.1.4 "><p id="p6675950017742"><a name="p6675950017742"></a><a name="p6675950017742"></a>Description of the domain name, which cannot exceed 255 characters</p>
    </td>
    </tr>
    <tr id="row3526956217742"><td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.1 "><p id="p5656791917742"><a name="p5656791917742"></a><a name="p5656791917742"></a>zone_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.459999999999997%" headers="mcps1.2.5.1.2 "><p id="p2306625217742"><a name="p2306625217742"></a><a name="p2306625217742"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.590000000000002%" headers="mcps1.2.5.1.3 "><p id="p5927915117742"><a name="p5927915117742"></a><a name="p5927915117742"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.790000000000006%" headers="mcps1.2.5.1.4 "><p id="p1460824917742"><a name="p1460824917742"></a><a name="p1460824917742"></a>Zone type, the value of which can be <strong id="b842352706113548"><a name="b842352706113548"></a><a name="b842352706113548"></a>public</strong> or <strong id="b842352706113551"><a name="b842352706113551"></a><a name="b842352706113551"></a>private</strong></p>
    <a name="ul3411250511841"></a><a name="ul3411250511841"></a><ul id="ul3411250511841"><li id="li3430935611841"><a name="li3430935611841"></a><a name="li3430935611841"></a><strong id="b84235270691511"><a name="b84235270691511"></a><a name="b84235270691511"></a>public</strong>: public zones accessible to hosts on the Internet</li><li id="li2055999811841"><a name="li2055999811841"></a><a name="li2055999811841"></a><strong id="b8423527069166"><a name="b8423527069166"></a><a name="b8423527069166"></a>private</strong>: private zones accessible only to hosts in specified VPCs</li></ul>
    <p id="p5903182219130"><a name="p5903182219130"></a><a name="p5903182219130"></a>If the value is left blank, a public zone will be created. For details about creating a private zone, see section <a href="creating-a-private-zone.html">Creating a Private Zone</a>.</p>
    </td>
    </tr>
    <tr id="row4358988017742"><td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.1 "><p id="p6536976617742"><a name="p6536976617742"></a><a name="p6536976617742"></a>email</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.459999999999997%" headers="mcps1.2.5.1.2 "><p id="p650279617742"><a name="p650279617742"></a><a name="p650279617742"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.590000000000002%" headers="mcps1.2.5.1.3 "><p id="p2054573717742"><a name="p2054573717742"></a><a name="p2054573717742"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.790000000000006%" headers="mcps1.2.5.1.4 "><p id="p1997196517742"><a name="p1997196517742"></a><a name="p1997196517742"></a>Email address of the administrator managing the zone</p>
    </td>
    </tr>
    <tr id="row13489593141045"><td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.1 "><p id="p18915273141045"><a name="p18915273141045"></a><a name="p18915273141045"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.459999999999997%" headers="mcps1.2.5.1.2 "><p id="p55742162141045"><a name="p55742162141045"></a><a name="p55742162141045"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.590000000000002%" headers="mcps1.2.5.1.3 "><p id="p18821243141045"><a name="p18821243141045"></a><a name="p18821243141045"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.790000000000006%" headers="mcps1.2.5.1.4 "><p id="p3447255141334"><a name="p3447255141334"></a><a name="p3447255141334"></a>Caching period of the SOA record set (in seconds)</p>
    <p id="p54818170173211"><a name="p54818170173211"></a><a name="p54818170173211"></a>The default value is <strong id="b84235270615612"><a name="b84235270615612"></a><a name="b84235270615612"></a>300s</strong>.</p>
    <p id="p6035867719130"><a name="p6035867719130"></a><a name="p6035867719130"></a>The value range is 300–2147483647.</p>
    </td>
    </tr>
    <tr id="row964631312824"><td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.5.1.1 "><p id="p5754504312824"><a name="p5754504312824"></a><a name="p5754504312824"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.459999999999997%" headers="mcps1.2.5.1.2 "><p id="p3063693212824"><a name="p3063693212824"></a><a name="p3063693212824"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.590000000000002%" headers="mcps1.2.5.1.3 "><p id="p6567246612824"><a name="p6567246612824"></a><a name="p6567246612824"></a>List&lt;tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.790000000000006%" headers="mcps1.2.5.1.4 "><p id="p1786954012824"><a name="p1786954012824"></a><a name="p1786954012824"></a>Resource tag. For details, see <a href="#EN-US_TOPIC_0057310891__table19530794112436">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Description of the tag list

    <a name="table19530794112436"></a><table><thead align="left"><tr id="row15361836112436"><th class="cellrowborder" valign="top" width="17.28%" id="mcps1.2.5.1.1"><p id="p58707511112436"><a name="p58707511112436"></a><a name="p58707511112436"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.15%" id="mcps1.2.5.1.2"><p id="p57687928112436"><a name="p57687928112436"></a><a name="p57687928112436"></a><strong id="b593421527191713_1"><a name="b593421527191713_1"></a><a name="b593421527191713_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.77%" id="mcps1.2.5.1.3"><p id="p42210623112436"><a name="p42210623112436"></a><a name="p42210623112436"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.8%" id="mcps1.2.5.1.4"><p id="p63617265112436"><a name="p63617265112436"></a><a name="p63617265112436"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35684479112436"><td class="cellrowborder" valign="top" width="17.28%" headers="mcps1.2.5.1.1 "><p id="p13313439112530"><a name="p13313439112530"></a><a name="p13313439112530"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.15%" headers="mcps1.2.5.1.2 "><p id="p50150432112436"><a name="p50150432112436"></a><a name="p50150432112436"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.77%" headers="mcps1.2.5.1.3 "><p id="p35653193112436"><a name="p35653193112436"></a><a name="p35653193112436"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.8%" headers="mcps1.2.5.1.4 "><p id="p48921437201850"><a name="p48921437201850"></a><a name="p48921437201850"></a>Tag key. The key contains 36 Unicode characters at most and cannot be blank. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row20048002112436"><td class="cellrowborder" valign="top" width="17.28%" headers="mcps1.2.5.1.1 "><p id="p66095544112533"><a name="p66095544112533"></a><a name="p66095544112533"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.15%" headers="mcps1.2.5.1.2 "><p id="p1570770112436"><a name="p1570770112436"></a><a name="p1570770112436"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.77%" headers="mcps1.2.5.1.3 "><p id="p60123528112436"><a name="p60123528112436"></a><a name="p60123528112436"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.8%" headers="mcps1.2.5.1.4 "><p id="p61714725112922"><a name="p61714725112922"></a><a name="p61714725112922"></a>Tag value. Each value contains 43 Unicode characters at most and can be an empty string. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    {
        "name": "example.com.",
        "description": "This is an example zone.",
        "zone_type": "public",
        "email": "xx@example.org"
    }
    ```


## Response<a name="section2142173017358"></a>

-   Parameter description

    **Table  3**  Parameters in the response

    <a name="table54601120171039"></a><table><thead align="left"><tr id="row54125868171039"><th class="cellrowborder" valign="top" width="17.990000000000002%" id="mcps1.2.4.1.1"><p id="p46128019171039"><a name="p46128019171039"></a><a name="p46128019171039"></a><strong id="b162774213314533_2"><a name="b162774213314533_2"></a><a name="b162774213314533_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.77%" id="mcps1.2.4.1.2"><p id="p61288737171039"><a name="p61288737171039"></a><a name="p61288737171039"></a><strong id="b84235270619112_2"><a name="b84235270619112_2"></a><a name="b84235270619112_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.239999999999995%" id="mcps1.2.4.1.3"><p id="p39427830171039"><a name="p39427830171039"></a><a name="p39427830171039"></a><strong id="b842352706112423_2"><a name="b842352706112423_2"></a><a name="b842352706112423_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3275315171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="p13677558171039"><a name="p13677558171039"></a><a name="p13677558171039"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="p31480160171039"><a name="p31480160171039"></a><a name="p31480160171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p55186322171039"><a name="p55186322171039"></a><a name="p55186322171039"></a>Zone ID, which is a UUID used to identify the zone</p>
    </td>
    </tr>
    <tr id="row62038903171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="p21725743171039"><a name="p21725743171039"></a><a name="p21725743171039"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="p55078653171039"><a name="p55078653171039"></a><a name="p55078653171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p65545475171039"><a name="p65545475171039"></a><a name="p65545475171039"></a>Zone name</p>
    </td>
    </tr>
    <tr id="row24663709171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="p56112529171039"><a name="p56112529171039"></a><a name="p56112529171039"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="p46656524171039"><a name="p46656524171039"></a><a name="p46656524171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p31778607171039"><a name="p31778607171039"></a><a name="p31778607171039"></a>Zone description</p>
    </td>
    </tr>
    <tr id="row34212800171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="p51657401171039"><a name="p51657401171039"></a><a name="p51657401171039"></a>email</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="p336297171039"><a name="p336297171039"></a><a name="p336297171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p66322352171039"><a name="p66322352171039"></a><a name="p66322352171039"></a>Email address of the administrator managing the zone</p>
    </td>
    </tr>
    <tr id="row45341886171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="p22374403171039"><a name="p22374403171039"></a><a name="p22374403171039"></a>zone_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="p16323247171039"><a name="p16323247171039"></a><a name="p16323247171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p58527202171039"><a name="p58527202171039"></a><a name="p58527202171039"></a>Zone type, which can be <strong id="b842352706115152"><a name="b842352706115152"></a><a name="b842352706115152"></a>public</strong> or <strong id="b842352706115156"><a name="b842352706115156"></a><a name="b842352706115156"></a>private</strong></p>
    </td>
    </tr>
    <tr id="row36905265171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="p4888971171039"><a name="p4888971171039"></a><a name="p4888971171039"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="p16027579171039"><a name="p16027579171039"></a><a name="p16027579171039"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p41240291171039"><a name="p41240291171039"></a><a name="p41240291171039"></a>TTL value of the SOA record set in the zone</p>
    </td>
    </tr>
    <tr id="row29641334171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="p63311148171039"><a name="p63311148171039"></a><a name="p63311148171039"></a>serial</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="p26678057171039"><a name="p26678057171039"></a><a name="p26678057171039"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p7524749171039"><a name="p7524749171039"></a><a name="p7524749171039"></a>Serial number in the SOA record set in the zone, which identifies the change on the primary DNS server</p>
    </td>
    </tr>
    <tr id="row44990376171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="p30244483171039"><a name="p30244483171039"></a><a name="p30244483171039"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="p47406357171039"><a name="p47406357171039"></a><a name="p47406357171039"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p9822846171039"><a name="p9822846171039"></a><a name="p9822846171039"></a>Resource status</p>
    <p id="p36239781171039"><a name="p36239781171039"></a><a name="p36239781171039"></a>The value can be <strong id="b84235270695628"><a name="b84235270695628"></a><a name="b84235270695628"></a>PENDING_CREATE</strong>, <strong id="b84235270695635"><a name="b84235270695635"></a><a name="b84235270695635"></a>ACTIVE</strong>, <strong id="b84235270695643"><a name="b84235270695643"></a><a name="b84235270695643"></a>PENDING_DELETE</strong>, or <strong id="b84235270695650"><a name="b84235270695650"></a><a name="b84235270695650"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="row1454557171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="p51202644171039"><a name="p51202644171039"></a><a name="p51202644171039"></a>record_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="p32016130171039"><a name="p32016130171039"></a><a name="p32016130171039"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p53878535171039"><a name="p53878535171039"></a><a name="p53878535171039"></a>Number of record sets in the zone</p>
    </td>
    </tr>
    <tr id="row48476716171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="p54136527171039"><a name="p54136527171039"></a><a name="p54136527171039"></a>pool_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="p48020249171039"><a name="p48020249171039"></a><a name="p48020249171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p63987755171039"><a name="p63987755171039"></a><a name="p63987755171039"></a>Pool ID of the zone, which is assigned by the system</p>
    </td>
    </tr>
    <tr id="row49967872171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="p35791512171039"><a name="p35791512171039"></a><a name="p35791512171039"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="p10454086171039"><a name="p10454086171039"></a><a name="p10454086171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p8704812171039"><a name="p8704812171039"></a><a name="p8704812171039"></a>Project ID of the zone</p>
    </td>
    </tr>
    <tr id="row27690345171039"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="p48529730171039"><a name="p48529730171039"></a><a name="p48529730171039"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="p59988242171039"><a name="p59988242171039"></a><a name="p59988242171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p9292793171039"><a name="p9292793171039"></a><a name="p9292793171039"></a>Time when the zone was created</p>
    </td>
    </tr>
    <tr id="row4377608115654"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="p5844041115654"><a name="p5844041115654"></a><a name="p5844041115654"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="p3605288915654"><a name="p3605288915654"></a><a name="p3605288915654"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p3460290715654"><a name="p3460290715654"></a><a name="p3460290715654"></a>Time when the zone was updated</p>
    </td>
    </tr>
    <tr id="row384676871572"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="p288749251572"><a name="p288749251572"></a><a name="p288749251572"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="p571676251572"><a name="p571676251572"></a><a name="p571676251572"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p59736855103137"><a name="p59736855103137"></a><a name="p59736855103137"></a>Link of the current resource or other related resources</p>
    <p id="p5462345019130"><a name="p5462345019130"></a><a name="p5462345019130"></a>When a response is broken into pages, a <strong id="b84235270695245"><a name="b84235270695245"></a><a name="b84235270695245"></a>next</strong> link is provided to retrieve all results.</p>
    </td>
    </tr>
    <tr id="row177328815945"><td class="cellrowborder" valign="top" width="17.990000000000002%" headers="mcps1.2.4.1.1 "><p id="p1595959815945"><a name="p1595959815945"></a><a name="p1595959815945"></a>masters</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.4.1.2 "><p id="p1765902715945"><a name="p1765902715945"></a><a name="p1765902715945"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p2109506015945"><a name="p2109506015945"></a><a name="p2109506015945"></a>Master DNS servers, from which the slave servers get DNS information</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "id": "2c9eb155587194ec01587224c9f90149",
        "name": "example.com.",
        "description": "This is an example zone.",
        "email": "xx@example.com",
        "ttl": 300,
        "serial": 1,
        "masters": [],
        "status": "PENDING_CREATE",
        "links": {
            "self": "https://Endpoint/v2/zones/2c9eb155587194ec01587224c9f90149"
        },
        "pool_id": "00000000570e54ee01570e9939b20019",
        "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c",
        "zone_type": "public",
        "created_at": "2016-11-17T11:56:03.439",
        "updated_at": null,
        "record_num": 0
    }
    
    ```


## **Returned Value**<a name="section1917896317411"></a>

See  [General Request Return Code](general-request-return-code.md).

