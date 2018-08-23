# Creating a Private Zone<a name="EN-US_TOPIC_0057311027"></a>

## Function<a name="section3569153217343"></a>

Create a private zone.

## URI<a name="section6163262617350"></a>

URI format:

POST /v2/zones

## Request<a name="section4207148117353"></a>

-   Parameter description

    **Table  1**  Parameters in the request

    <a name="table3720408817742"></a><table><thead align="left"><tr id="row6225671717742"><th class="cellrowborder" valign="top" width="18.970000000000002%" id="mcps1.2.5.1.1"><p id="p5153686617742"><a name="p5153686617742"></a><a name="p5153686617742"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.18%" id="mcps1.2.5.1.2"><p id="p473035017742"><a name="p473035017742"></a><a name="p473035017742"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.72%" id="mcps1.2.5.1.3"><p id="p386753717742"><a name="p386753717742"></a><a name="p386753717742"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.13%" id="mcps1.2.5.1.4"><p id="p5956810717742"><a name="p5956810717742"></a><a name="p5956810717742"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1329410717742"><td class="cellrowborder" valign="top" width="18.970000000000002%" headers="mcps1.2.5.1.1 "><p id="p3414560317742"><a name="p3414560317742"></a><a name="p3414560317742"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.18%" headers="mcps1.2.5.1.2 "><p id="p6603174617742"><a name="p6603174617742"></a><a name="p6603174617742"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.72%" headers="mcps1.2.5.1.3 "><p id="p360216817742"><a name="p360216817742"></a><a name="p360216817742"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.13%" headers="mcps1.2.5.1.4 "><p id="p2651334817742"><a name="p2651334817742"></a><a name="p2651334817742"></a>Domain name of the zone to be created</p>
    <a name="ul1536534155329"></a><a name="ul1536534155329"></a><ul id="ul1536534155329"><li id="li13093589155329"><a name="li13093589155329"></a><a name="li13093589155329"></a>If a domain name is ended with a dot (.), it cannot exceed 254 characters.</li><li id="li5289935151252"><a name="li5289935151252"></a><a name="li5289935151252"></a>Otherwise, the domain name cannot exceed 253 characters.</li><li id="li932560893722"><a name="li932560893722"></a><a name="li932560893722"></a>Labels of a domain name are separated by dot (.). Each label cannot exceed 63 characters.</li></ul>
    <p id="p61100872151329"><a name="p61100872151329"></a><a name="p61100872151329"></a>A domain name is case insensitive. Uppercase letters will also be converted into lowercase letters.</p>
    </td>
    </tr>
    <tr id="row1973909717742"><td class="cellrowborder" valign="top" width="18.970000000000002%" headers="mcps1.2.5.1.1 "><p id="p5474826717742"><a name="p5474826717742"></a><a name="p5474826717742"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.18%" headers="mcps1.2.5.1.2 "><p id="p759162017742"><a name="p759162017742"></a><a name="p759162017742"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.72%" headers="mcps1.2.5.1.3 "><p id="p3220634117742"><a name="p3220634117742"></a><a name="p3220634117742"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.13%" headers="mcps1.2.5.1.4 "><p id="p3586421511957"><a name="p3586421511957"></a><a name="p3586421511957"></a>Description of the domain name, which cannot exceed 255 characters</p>
    </td>
    </tr>
    <tr id="row3526956217742"><td class="cellrowborder" valign="top" width="18.970000000000002%" headers="mcps1.2.5.1.1 "><p id="p5656791917742"><a name="p5656791917742"></a><a name="p5656791917742"></a>zone_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.18%" headers="mcps1.2.5.1.2 "><p id="p2306625217742"><a name="p2306625217742"></a><a name="p2306625217742"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.72%" headers="mcps1.2.5.1.3 "><p id="p5927915117742"><a name="p5927915117742"></a><a name="p5927915117742"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.13%" headers="mcps1.2.5.1.4 "><p id="p92377632066"><a name="p92377632066"></a><a name="p92377632066"></a>Zone type</p>
    <p id="p59986333111018"><a name="p59986333111018"></a><a name="p59986333111018"></a>The value must be <strong id="b60062277144632"><a name="b60062277144632"></a><a name="b60062277144632"></a>private</strong>, indicating private zones accessible only to hosts in specified VPCs will be created.</p>
    <p id="p96596832066"><a name="p96596832066"></a><a name="p96596832066"></a>For details about creating a public zone, see section <a href="creating-a-public-zone.html">Creating a Public Zone</a>.</p>
    </td>
    </tr>
    <tr id="row4358988017742"><td class="cellrowborder" valign="top" width="18.970000000000002%" headers="mcps1.2.5.1.1 "><p id="p6536976617742"><a name="p6536976617742"></a><a name="p6536976617742"></a>email</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.18%" headers="mcps1.2.5.1.2 "><p id="p650279617742"><a name="p650279617742"></a><a name="p650279617742"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.72%" headers="mcps1.2.5.1.3 "><p id="p2054573717742"><a name="p2054573717742"></a><a name="p2054573717742"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.13%" headers="mcps1.2.5.1.4 "><p id="p1997196517742"><a name="p1997196517742"></a><a name="p1997196517742"></a>Email address of the administrator managing the zone</p>
    </td>
    </tr>
    <tr id="row13489593141045"><td class="cellrowborder" valign="top" width="18.970000000000002%" headers="mcps1.2.5.1.1 "><p id="p18915273141045"><a name="p18915273141045"></a><a name="p18915273141045"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.18%" headers="mcps1.2.5.1.2 "><p id="p55742162141045"><a name="p55742162141045"></a><a name="p55742162141045"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.72%" headers="mcps1.2.5.1.3 "><p id="p18821243141045"><a name="p18821243141045"></a><a name="p18821243141045"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.13%" headers="mcps1.2.5.1.4 "><p id="p3447255141334"><a name="p3447255141334"></a><a name="p3447255141334"></a>Caching period of the SOA record set (in seconds)</p>
    <p id="p54818170173211"><a name="p54818170173211"></a><a name="p54818170173211"></a>The default value is <strong id="b84235270615612"><a name="b84235270615612"></a><a name="b84235270615612"></a>300s</strong>.</p>
    <p id="p5335091141210"><a name="p5335091141210"></a><a name="p5335091141210"></a>The value range is 300–2147483647.</p>
    </td>
    </tr>
    <tr id="row18045881171648"><td class="cellrowborder" valign="top" width="18.970000000000002%" headers="mcps1.2.5.1.1 "><p id="p20204595171650"><a name="p20204595171650"></a><a name="p20204595171650"></a>router</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.18%" headers="mcps1.2.5.1.2 "><p id="p25959495171650"><a name="p25959495171650"></a><a name="p25959495171650"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.72%" headers="mcps1.2.5.1.3 "><p id="p22344380171650"><a name="p22344380171650"></a><a name="p22344380171650"></a>Router</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.13%" headers="mcps1.2.5.1.4 "><p id="p49598957105941"><a name="p49598957105941"></a><a name="p49598957105941"></a>Router information (VPC associated with the private zone)</p>
    <p id="p2202488111957"><a name="p2202488111957"></a><a name="p2202488111957"></a>For details, see <a href="#EN-US_TOPIC_0057311027__table4448008117179">Table 2</a>.</p>
    </td>
    </tr>
    <tr id="row3748545412107"><td class="cellrowborder" valign="top" width="18.970000000000002%" headers="mcps1.2.5.1.1 "><p id="p6123289312107"><a name="p6123289312107"></a><a name="p6123289312107"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.18%" headers="mcps1.2.5.1.2 "><p id="p6091732812107"><a name="p6091732812107"></a><a name="p6091732812107"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.72%" headers="mcps1.2.5.1.3 "><p id="p3535651512107"><a name="p3535651512107"></a><a name="p3535651512107"></a>tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.13%" headers="mcps1.2.5.1.4 "><p id="p4530543812107"><a name="p4530543812107"></a><a name="p4530543812107"></a>Resource tag. For details, see <a href="#EN-US_TOPIC_0057311027__table19530794112436">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Description of the  **router**  field

    <a name="table4448008117179"></a><table><thead align="left"><tr id="row6132935617179"><th class="cellrowborder" valign="top" width="17.34%" id="mcps1.2.5.1.1"><p id="p36588677171719"><a name="p36588677171719"></a><a name="p36588677171719"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.439999999999998%" id="mcps1.2.5.1.2"><p id="p10892865171719"><a name="p10892865171719"></a><a name="p10892865171719"></a><strong id="b593421527191713_1"><a name="b593421527191713_1"></a><a name="b593421527191713_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.969999999999999%" id="mcps1.2.5.1.3"><p id="p9906869171719"><a name="p9906869171719"></a><a name="p9906869171719"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.25%" id="mcps1.2.5.1.4"><p id="p64258954171719"><a name="p64258954171719"></a><a name="p64258954171719"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row266872817179"><td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.5.1.1 "><p id="p25118582171719"><a name="p25118582171719"></a><a name="p25118582171719"></a>router_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.2.5.1.2 "><p id="p21339228171719"><a name="p21339228171719"></a><a name="p21339228171719"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.5.1.3 "><p id="p50755907171719"><a name="p50755907171719"></a><a name="p50755907171719"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.25%" headers="mcps1.2.5.1.4 "><p id="p17587794171719"><a name="p17587794171719"></a><a name="p17587794171719"></a>Router ID (VPC ID)</p>
    </td>
    </tr>
    <tr id="row6657832817179"><td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.2.5.1.1 "><p id="p3709384171719"><a name="p3709384171719"></a><a name="p3709384171719"></a>router_region</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.2.5.1.2 "><p id="p32024676171719"><a name="p32024676171719"></a><a name="p32024676171719"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.5.1.3 "><p id="p43861924171719"><a name="p43861924171719"></a><a name="p43861924171719"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.25%" headers="mcps1.2.5.1.4 "><p id="p63154928171719"><a name="p63154928171719"></a><a name="p63154928171719"></a>Region of the router (VPC)</p>
    <p id="p38645142171939"><a name="p38645142171939"></a><a name="p38645142171939"></a>If it is left blank, the region of the project in the token takes effect by default.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the tag list

    <a name="table19530794112436"></a><table><thead align="left"><tr id="en-us_topic_0057310891_row15361836112436"><th class="cellrowborder" valign="top" width="17.28%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057310891_p58707511112436"><a name="en-us_topic_0057310891_p58707511112436"></a><a name="en-us_topic_0057310891_p58707511112436"></a><strong id="en-us_topic_0057310891_b162774213314533"><a name="en-us_topic_0057310891_b162774213314533"></a><a name="en-us_topic_0057310891_b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.15%" id="mcps1.2.5.1.2"><p id="en-us_topic_0057310891_p57687928112436"><a name="en-us_topic_0057310891_p57687928112436"></a><a name="en-us_topic_0057310891_p57687928112436"></a><strong id="en-us_topic_0057310891_b593421527191713"><a name="en-us_topic_0057310891_b593421527191713"></a><a name="en-us_topic_0057310891_b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.77%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057310891_p42210623112436"><a name="en-us_topic_0057310891_p42210623112436"></a><a name="en-us_topic_0057310891_p42210623112436"></a><strong id="en-us_topic_0057310891_b84235270619112"><a name="en-us_topic_0057310891_b84235270619112"></a><a name="en-us_topic_0057310891_b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.8%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057310891_p63617265112436"><a name="en-us_topic_0057310891_p63617265112436"></a><a name="en-us_topic_0057310891_p63617265112436"></a><strong id="en-us_topic_0057310891_b842352706112423"><a name="en-us_topic_0057310891_b842352706112423"></a><a name="en-us_topic_0057310891_b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0057310891_row35684479112436"><td class="cellrowborder" valign="top" width="17.28%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057310891_p13313439112530"><a name="en-us_topic_0057310891_p13313439112530"></a><a name="en-us_topic_0057310891_p13313439112530"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057310891_p50150432112436"><a name="en-us_topic_0057310891_p50150432112436"></a><a name="en-us_topic_0057310891_p50150432112436"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.77%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057310891_p35653193112436"><a name="en-us_topic_0057310891_p35653193112436"></a><a name="en-us_topic_0057310891_p35653193112436"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.8%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057310891_p48921437201850"><a name="en-us_topic_0057310891_p48921437201850"></a><a name="en-us_topic_0057310891_p48921437201850"></a>Tag key. The key contains 36 Unicode characters at most and cannot be blank. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057310891_row20048002112436"><td class="cellrowborder" valign="top" width="17.28%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057310891_p66095544112533"><a name="en-us_topic_0057310891_p66095544112533"></a><a name="en-us_topic_0057310891_p66095544112533"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.15%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057310891_p1570770112436"><a name="en-us_topic_0057310891_p1570770112436"></a><a name="en-us_topic_0057310891_p1570770112436"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.77%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057310891_p60123528112436"><a name="en-us_topic_0057310891_p60123528112436"></a><a name="en-us_topic_0057310891_p60123528112436"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.8%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057310891_p61714725112922"><a name="en-us_topic_0057310891_p61714725112922"></a><a name="en-us_topic_0057310891_p61714725112922"></a>Tag value. Each value contains 43 Unicode characters at most and can be an empty string. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    {
        "name": "example.com.",
        "description": "This is an example zone.",
        "zone_type": "private",
        "email": "xx@example.org",
        "router": {
            "router_id": "19664294-0bf6-4271-ad3a-94b8c79c6558",
            "router_region": "xx"
        }
    }
    ```


## Response<a name="section2142173017358"></a>

-   Parameter description

    **Table  4**  Parameters in the response

    <a name="table54601120171039"></a><table><thead align="left"><tr id="row54125868171039"><th class="cellrowborder" valign="top" width="18.37%" id="mcps1.2.4.1.1"><p id="p46128019171039"><a name="p46128019171039"></a><a name="p46128019171039"></a><strong id="b162774213314533_2"><a name="b162774213314533_2"></a><a name="b162774213314533_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.32%" id="mcps1.2.4.1.2"><p id="p61288737171039"><a name="p61288737171039"></a><a name="p61288737171039"></a><strong id="b84235270619112_2"><a name="b84235270619112_2"></a><a name="b84235270619112_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="64.31%" id="mcps1.2.4.1.3"><p id="p39427830171039"><a name="p39427830171039"></a><a name="p39427830171039"></a><strong id="b842352706112423_2"><a name="b842352706112423_2"></a><a name="b842352706112423_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3275315171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p13677558171039"><a name="p13677558171039"></a><a name="p13677558171039"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p31480160171039"><a name="p31480160171039"></a><a name="p31480160171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="p55186322171039"><a name="p55186322171039"></a><a name="p55186322171039"></a>Zone ID, which is a UUID used to identify the zone</p>
    </td>
    </tr>
    <tr id="row62038903171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p21725743171039"><a name="p21725743171039"></a><a name="p21725743171039"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p55078653171039"><a name="p55078653171039"></a><a name="p55078653171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="p65545475171039"><a name="p65545475171039"></a><a name="p65545475171039"></a>Zone name</p>
    </td>
    </tr>
    <tr id="row24663709171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p56112529171039"><a name="p56112529171039"></a><a name="p56112529171039"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p46656524171039"><a name="p46656524171039"></a><a name="p46656524171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="p31778607171039"><a name="p31778607171039"></a><a name="p31778607171039"></a>Zone description</p>
    </td>
    </tr>
    <tr id="row34212800171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p51657401171039"><a name="p51657401171039"></a><a name="p51657401171039"></a>email</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p336297171039"><a name="p336297171039"></a><a name="p336297171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="p66322352171039"><a name="p66322352171039"></a><a name="p66322352171039"></a>Email address of the administrator managing the zone</p>
    </td>
    </tr>
    <tr id="row45341886171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p22374403171039"><a name="p22374403171039"></a><a name="p22374403171039"></a>zone_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p16323247171039"><a name="p16323247171039"></a><a name="p16323247171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="p58527202171039"><a name="p58527202171039"></a><a name="p58527202171039"></a>Zone type, which can be <strong id="b842352706115152"><a name="b842352706115152"></a><a name="b842352706115152"></a>public</strong> or <strong id="b842352706115156"><a name="b842352706115156"></a><a name="b842352706115156"></a>private</strong></p>
    </td>
    </tr>
    <tr id="row36905265171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p4888971171039"><a name="p4888971171039"></a><a name="p4888971171039"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p16027579171039"><a name="p16027579171039"></a><a name="p16027579171039"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="p41240291171039"><a name="p41240291171039"></a><a name="p41240291171039"></a>TTL value of the SOA record set in the zone</p>
    </td>
    </tr>
    <tr id="row29641334171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p63311148171039"><a name="p63311148171039"></a><a name="p63311148171039"></a>serial</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p26678057171039"><a name="p26678057171039"></a><a name="p26678057171039"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="p7524749171039"><a name="p7524749171039"></a><a name="p7524749171039"></a>Serial number in the SOA record set in the zone, which identifies the change on the primary DNS server</p>
    </td>
    </tr>
    <tr id="row44990376171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p30244483171039"><a name="p30244483171039"></a><a name="p30244483171039"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p47406357171039"><a name="p47406357171039"></a><a name="p47406357171039"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="p9822846171039"><a name="p9822846171039"></a><a name="p9822846171039"></a>Resource status</p>
    <p id="p36239781171039"><a name="p36239781171039"></a><a name="p36239781171039"></a>The value can be <strong id="b84235270695628"><a name="b84235270695628"></a><a name="b84235270695628"></a>PENDING_CREATE</strong>,&nbsp;<strong id="b84235270695635"><a name="b84235270695635"></a><a name="b84235270695635"></a>ACTIVE</strong>,&nbsp;<strong id="b84235270695643"><a name="b84235270695643"></a><a name="b84235270695643"></a>PENDING_DELETE</strong>, or&nbsp;<strong id="b84235270695650"><a name="b84235270695650"></a><a name="b84235270695650"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="row1454557171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p51202644171039"><a name="p51202644171039"></a><a name="p51202644171039"></a>record_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p32016130171039"><a name="p32016130171039"></a><a name="p32016130171039"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="p53878535171039"><a name="p53878535171039"></a><a name="p53878535171039"></a>Number of record sets in the zone</p>
    </td>
    </tr>
    <tr id="row48476716171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p54136527171039"><a name="p54136527171039"></a><a name="p54136527171039"></a>pool_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p48020249171039"><a name="p48020249171039"></a><a name="p48020249171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="p63987755171039"><a name="p63987755171039"></a><a name="p63987755171039"></a>Pool ID of the zone, which is assigned by the system</p>
    </td>
    </tr>
    <tr id="row49967872171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p35791512171039"><a name="p35791512171039"></a><a name="p35791512171039"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p10454086171039"><a name="p10454086171039"></a><a name="p10454086171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="p8704812171039"><a name="p8704812171039"></a><a name="p8704812171039"></a>Project ID of the zone</p>
    </td>
    </tr>
    <tr id="row27690345171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p48529730171039"><a name="p48529730171039"></a><a name="p48529730171039"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p59988242171039"><a name="p59988242171039"></a><a name="p59988242171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="p9292793171039"><a name="p9292793171039"></a><a name="p9292793171039"></a>Time when the zone was created</p>
    </td>
    </tr>
    <tr id="row4377608115654"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p5844041115654"><a name="p5844041115654"></a><a name="p5844041115654"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p3605288915654"><a name="p3605288915654"></a><a name="p3605288915654"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="p3460290715654"><a name="p3460290715654"></a><a name="p3460290715654"></a>Time when the zone was updated</p>
    </td>
    </tr>
    <tr id="row384676871572"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p288749251572"><a name="p288749251572"></a><a name="p288749251572"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p571676251572"><a name="p571676251572"></a><a name="p571676251572"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="p50014989155938"><a name="p50014989155938"></a><a name="p50014989155938"></a>Link of the current resource or other related resources</p>
    <p id="p660161572"><a name="p660161572"></a><a name="p660161572"></a>When a response is broken into pages, a <strong id="b84235270695245"><a name="b84235270695245"></a><a name="b84235270695245"></a>next</strong> link is provided to retrieve all results.</p>
    </td>
    </tr>
    <tr id="row177328815945"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p1595959815945"><a name="p1595959815945"></a><a name="p1595959815945"></a>masters</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p1765902715945"><a name="p1765902715945"></a><a name="p1765902715945"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="p2109506015945"><a name="p2109506015945"></a><a name="p2109506015945"></a>Master DNS servers, from which the slave servers get DNS information</p>
    </td>
    </tr>
    <tr id="row57448667171910"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p3560499171932"><a name="p3560499171932"></a><a name="p3560499171932"></a>router</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p19965041171932"><a name="p19965041171932"></a><a name="p19965041171932"></a>Router</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="p6555635171932"><a name="p6555635171932"></a><a name="p6555635171932"></a>Router information (VPC associated with the zone)</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "id": "ff8080825b8fc86c015b94bc6f8712c3",
        "name": "example.com.",
        "description": "This is an example zone.",
        "email": "xx@example.com",
        "ttl": 300,
        "serial": 1,
        "masters": [],
        "status": "PENDING_CREATE",
        "links": {
            "self": "https://Endpoint/v2/zones/ff8080825b8fc86c015b94bc6f8712c3"
        },
        "pool_id": "ff8080825ab738f4015ab7513298010e",
        "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c",
        "zone_type": "private",
        "created_at": "2017-04-22T08:17:08.997",
        "updated_at": null,
        "record_num": 0,
        "router": {
            "status": "PENDING_CREATE",
            "router_id": "19664294-0bf6-4271-ad3a-94b8c79c6558",
            "router_region": "xx"
        }
    }
    ```


## **Returned Value**<a name="section1917896317411"></a>

See  [General Request Return Code](general-request-return-code.md).

