# Modifying a Private Zone<a name="EN-US_TOPIC_0080996887"></a>

## Function<a name="section3569153217343"></a>

Modify a private zone.

## URI<a name="section6163262617350"></a>

-   URI format

    PATCH /v2/zones/\{zone\_id\}

-   Parameter description

    **Table  1**  Parameter in the URI

    <a name="en-us_topic_0080995382_table56746773172616"></a><table><thead align="left"><tr id="en-us_topic_0080995382_row12848229172616"><th class="cellrowborder" valign="top" width="19.598040195980403%" id="mcps1.2.5.1.1"><p id="en-us_topic_0080995382_p44975878172616"><a name="en-us_topic_0080995382_p44975878172616"></a><a name="en-us_topic_0080995382_p44975878172616"></a><strong id="en-us_topic_0080995382_b162774213314533"><a name="en-us_topic_0080995382_b162774213314533"></a><a name="en-us_topic_0080995382_b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.537946205379463%" id="mcps1.2.5.1.2"><p id="en-us_topic_0080995382_p46443918172616"><a name="en-us_topic_0080995382_p46443918172616"></a><a name="en-us_topic_0080995382_p46443918172616"></a><strong id="en-us_topic_0080995382_b593421527191713"><a name="en-us_topic_0080995382_b593421527191713"></a><a name="en-us_topic_0080995382_b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.958604139586042%" id="mcps1.2.5.1.3"><p id="en-us_topic_0080995382_p1368350172616"><a name="en-us_topic_0080995382_p1368350172616"></a><a name="en-us_topic_0080995382_p1368350172616"></a><strong id="en-us_topic_0080995382_b84235270619112"><a name="en-us_topic_0080995382_b84235270619112"></a><a name="en-us_topic_0080995382_b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.9054094590541%" id="mcps1.2.5.1.4"><p id="en-us_topic_0080995382_p24157908172616"><a name="en-us_topic_0080995382_p24157908172616"></a><a name="en-us_topic_0080995382_p24157908172616"></a><strong id="en-us_topic_0080995382_b842352706112423"><a name="en-us_topic_0080995382_b842352706112423"></a><a name="en-us_topic_0080995382_b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0080995382_row39993297172616"><td class="cellrowborder" valign="top" width="19.598040195980403%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0080995382_p43071797172616"><a name="en-us_topic_0080995382_p43071797172616"></a><a name="en-us_topic_0080995382_p43071797172616"></a>zone_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.537946205379463%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0080995382_p26647585172616"><a name="en-us_topic_0080995382_p26647585172616"></a><a name="en-us_topic_0080995382_p26647585172616"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.958604139586042%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0080995382_p21075379172616"><a name="en-us_topic_0080995382_p21075379172616"></a><a name="en-us_topic_0080995382_p21075379172616"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.9054094590541%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0080995382_p4976396172616"><a name="en-us_topic_0080995382_p4976396172616"></a><a name="en-us_topic_0080995382_p4976396172616"></a>ID of the zone to be modified</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section4207148117353"></a>

-   Parameter description

    **Table  2**  Parameters in the request

    <a name="en-us_topic_0080995382_table3720408817742"></a><table><thead align="left"><tr id="en-us_topic_0080995382_row6225671717742"><th class="cellrowborder" valign="top" width="18.208179182081793%" id="mcps1.2.5.1.1"><p id="en-us_topic_0080995382_p5153686617742"><a name="en-us_topic_0080995382_p5153686617742"></a><a name="en-us_topic_0080995382_p5153686617742"></a><strong id="en-us_topic_0080995382_b162774213314533_1"><a name="en-us_topic_0080995382_b162774213314533_1"></a><a name="en-us_topic_0080995382_b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.948005199480054%" id="mcps1.2.5.1.2"><p id="en-us_topic_0080995382_p473035017742"><a name="en-us_topic_0080995382_p473035017742"></a><a name="en-us_topic_0080995382_p473035017742"></a><strong id="en-us_topic_0080995382_b593421527191713_1"><a name="en-us_topic_0080995382_b593421527191713_1"></a><a name="en-us_topic_0080995382_b593421527191713_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.108689131086889%" id="mcps1.2.5.1.3"><p id="en-us_topic_0080995382_p386753717742"><a name="en-us_topic_0080995382_p386753717742"></a><a name="en-us_topic_0080995382_p386753717742"></a><strong id="en-us_topic_0080995382_b84235270619112_1"><a name="en-us_topic_0080995382_b84235270619112_1"></a><a name="en-us_topic_0080995382_b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.735126487351266%" id="mcps1.2.5.1.4"><p id="en-us_topic_0080995382_p5956810717742"><a name="en-us_topic_0080995382_p5956810717742"></a><a name="en-us_topic_0080995382_p5956810717742"></a><strong id="en-us_topic_0080995382_b842352706112423_1"><a name="en-us_topic_0080995382_b842352706112423_1"></a><a name="en-us_topic_0080995382_b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0080995382_row1973909717742"><td class="cellrowborder" valign="top" width="18.208179182081793%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0080995382_p5474826717742"><a name="en-us_topic_0080995382_p5474826717742"></a><a name="en-us_topic_0080995382_p5474826717742"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.948005199480054%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0080995382_p759162017742"><a name="en-us_topic_0080995382_p759162017742"></a><a name="en-us_topic_0080995382_p759162017742"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.108689131086889%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0080995382_p3220634117742"><a name="en-us_topic_0080995382_p3220634117742"></a><a name="en-us_topic_0080995382_p3220634117742"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.735126487351266%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0080995382_p6675950017742"><a name="en-us_topic_0080995382_p6675950017742"></a><a name="en-us_topic_0080995382_p6675950017742"></a>Description of the domain name, which cannot exceed 255 characters</p>
    </td>
    </tr>
    <tr id="en-us_topic_0080995382_row4358988017742"><td class="cellrowborder" valign="top" width="18.208179182081793%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0080995382_p6536976617742"><a name="en-us_topic_0080995382_p6536976617742"></a><a name="en-us_topic_0080995382_p6536976617742"></a>email</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.948005199480054%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0080995382_p650279617742"><a name="en-us_topic_0080995382_p650279617742"></a><a name="en-us_topic_0080995382_p650279617742"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.108689131086889%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0080995382_p2054573717742"><a name="en-us_topic_0080995382_p2054573717742"></a><a name="en-us_topic_0080995382_p2054573717742"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.735126487351266%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0080995382_p1997196517742"><a name="en-us_topic_0080995382_p1997196517742"></a><a name="en-us_topic_0080995382_p1997196517742"></a>Email address of the administrator managing the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0080995382_row13489593141045"><td class="cellrowborder" valign="top" width="18.208179182081793%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0080995382_p18915273141045"><a name="en-us_topic_0080995382_p18915273141045"></a><a name="en-us_topic_0080995382_p18915273141045"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.948005199480054%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0080995382_p55742162141045"><a name="en-us_topic_0080995382_p55742162141045"></a><a name="en-us_topic_0080995382_p55742162141045"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.108689131086889%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0080995382_p18821243141045"><a name="en-us_topic_0080995382_p18821243141045"></a><a name="en-us_topic_0080995382_p18821243141045"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.735126487351266%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0080995382_p3447255141334"><a name="en-us_topic_0080995382_p3447255141334"></a><a name="en-us_topic_0080995382_p3447255141334"></a>Caching period of the SOA record set (in seconds)</p>
    <p id="en-us_topic_0080995382_p54818170173211"><a name="en-us_topic_0080995382_p54818170173211"></a><a name="en-us_topic_0080995382_p54818170173211"></a>The default value is <strong id="en-us_topic_0080995382_b84235270615612"><a name="en-us_topic_0080995382_b84235270615612"></a><a name="en-us_topic_0080995382_b84235270615612"></a>300s</strong>.</p>
    <p id="en-us_topic_0080995382_p11670607161834"><a name="en-us_topic_0080995382_p11670607161834"></a><a name="en-us_topic_0080995382_p11670607161834"></a>The value range is 300–2147483647.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request example

    ```
    {
        "description": "This is an example zone.",
        "email": "xx@example.org",
        "ttl": 300
    }
    ```


## Response<a name="section2142173017358"></a>

-   Parameter description

    **Table  3**  Parameters in the response

    <a name="table54601120171039"></a><table><thead align="left"><tr id="en-us_topic_0057311027_row54125868171039"><th class="cellrowborder" valign="top" width="18.37%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057311027_p46128019171039"><a name="en-us_topic_0057311027_p46128019171039"></a><a name="en-us_topic_0057311027_p46128019171039"></a><strong id="en-us_topic_0057311027_b162774213314533"><a name="en-us_topic_0057311027_b162774213314533"></a><a name="en-us_topic_0057311027_b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057311027_p61288737171039"><a name="en-us_topic_0057311027_p61288737171039"></a><a name="en-us_topic_0057311027_p61288737171039"></a><strong id="en-us_topic_0057311027_b84235270619112"><a name="en-us_topic_0057311027_b84235270619112"></a><a name="en-us_topic_0057311027_b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="64.31%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057311027_p39427830171039"><a name="en-us_topic_0057311027_p39427830171039"></a><a name="en-us_topic_0057311027_p39427830171039"></a><strong id="en-us_topic_0057311027_b842352706112423"><a name="en-us_topic_0057311027_b842352706112423"></a><a name="en-us_topic_0057311027_b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0057311027_row3275315171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311027_p13677558171039"><a name="en-us_topic_0057311027_p13677558171039"></a><a name="en-us_topic_0057311027_p13677558171039"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311027_p31480160171039"><a name="en-us_topic_0057311027_p31480160171039"></a><a name="en-us_topic_0057311027_p31480160171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311027_p55186322171039"><a name="en-us_topic_0057311027_p55186322171039"></a><a name="en-us_topic_0057311027_p55186322171039"></a>Zone ID, which is a UUID used to identify the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311027_row62038903171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311027_p21725743171039"><a name="en-us_topic_0057311027_p21725743171039"></a><a name="en-us_topic_0057311027_p21725743171039"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311027_p55078653171039"><a name="en-us_topic_0057311027_p55078653171039"></a><a name="en-us_topic_0057311027_p55078653171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311027_p65545475171039"><a name="en-us_topic_0057311027_p65545475171039"></a><a name="en-us_topic_0057311027_p65545475171039"></a>Zone name</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311027_row24663709171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311027_p56112529171039"><a name="en-us_topic_0057311027_p56112529171039"></a><a name="en-us_topic_0057311027_p56112529171039"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311027_p46656524171039"><a name="en-us_topic_0057311027_p46656524171039"></a><a name="en-us_topic_0057311027_p46656524171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311027_p31778607171039"><a name="en-us_topic_0057311027_p31778607171039"></a><a name="en-us_topic_0057311027_p31778607171039"></a>Zone description</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311027_row34212800171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311027_p51657401171039"><a name="en-us_topic_0057311027_p51657401171039"></a><a name="en-us_topic_0057311027_p51657401171039"></a>email</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311027_p336297171039"><a name="en-us_topic_0057311027_p336297171039"></a><a name="en-us_topic_0057311027_p336297171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311027_p66322352171039"><a name="en-us_topic_0057311027_p66322352171039"></a><a name="en-us_topic_0057311027_p66322352171039"></a>Email address of the administrator managing the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311027_row45341886171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311027_p22374403171039"><a name="en-us_topic_0057311027_p22374403171039"></a><a name="en-us_topic_0057311027_p22374403171039"></a>zone_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311027_p16323247171039"><a name="en-us_topic_0057311027_p16323247171039"></a><a name="en-us_topic_0057311027_p16323247171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311027_p58527202171039"><a name="en-us_topic_0057311027_p58527202171039"></a><a name="en-us_topic_0057311027_p58527202171039"></a>Zone type, which can be <strong id="en-us_topic_0057311027_b842352706115152"><a name="en-us_topic_0057311027_b842352706115152"></a><a name="en-us_topic_0057311027_b842352706115152"></a>public</strong> or <strong id="en-us_topic_0057311027_b842352706115156"><a name="en-us_topic_0057311027_b842352706115156"></a><a name="en-us_topic_0057311027_b842352706115156"></a>private</strong></p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311027_row36905265171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311027_p4888971171039"><a name="en-us_topic_0057311027_p4888971171039"></a><a name="en-us_topic_0057311027_p4888971171039"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311027_p16027579171039"><a name="en-us_topic_0057311027_p16027579171039"></a><a name="en-us_topic_0057311027_p16027579171039"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311027_p41240291171039"><a name="en-us_topic_0057311027_p41240291171039"></a><a name="en-us_topic_0057311027_p41240291171039"></a>TTL value of the SOA record set in the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311027_row29641334171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311027_p63311148171039"><a name="en-us_topic_0057311027_p63311148171039"></a><a name="en-us_topic_0057311027_p63311148171039"></a>serial</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311027_p26678057171039"><a name="en-us_topic_0057311027_p26678057171039"></a><a name="en-us_topic_0057311027_p26678057171039"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311027_p7524749171039"><a name="en-us_topic_0057311027_p7524749171039"></a><a name="en-us_topic_0057311027_p7524749171039"></a>Serial number in the SOA record set in the zone, which identifies the change on the primary DNS server</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311027_row44990376171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311027_p30244483171039"><a name="en-us_topic_0057311027_p30244483171039"></a><a name="en-us_topic_0057311027_p30244483171039"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311027_p47406357171039"><a name="en-us_topic_0057311027_p47406357171039"></a><a name="en-us_topic_0057311027_p47406357171039"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311027_p9822846171039"><a name="en-us_topic_0057311027_p9822846171039"></a><a name="en-us_topic_0057311027_p9822846171039"></a>Resource status</p>
    <p id="en-us_topic_0057311027_p36239781171039"><a name="en-us_topic_0057311027_p36239781171039"></a><a name="en-us_topic_0057311027_p36239781171039"></a>The value can be <strong id="en-us_topic_0057311027_b84235270695628"><a name="en-us_topic_0057311027_b84235270695628"></a><a name="en-us_topic_0057311027_b84235270695628"></a>PENDING_CREATE</strong>,&nbsp;<strong id="en-us_topic_0057311027_b84235270695635"><a name="en-us_topic_0057311027_b84235270695635"></a><a name="en-us_topic_0057311027_b84235270695635"></a>ACTIVE</strong>,&nbsp;<strong id="en-us_topic_0057311027_b84235270695643"><a name="en-us_topic_0057311027_b84235270695643"></a><a name="en-us_topic_0057311027_b84235270695643"></a>PENDING_DELETE</strong>, or&nbsp;<strong id="en-us_topic_0057311027_b84235270695650"><a name="en-us_topic_0057311027_b84235270695650"></a><a name="en-us_topic_0057311027_b84235270695650"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311027_row1454557171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311027_p51202644171039"><a name="en-us_topic_0057311027_p51202644171039"></a><a name="en-us_topic_0057311027_p51202644171039"></a>record_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311027_p32016130171039"><a name="en-us_topic_0057311027_p32016130171039"></a><a name="en-us_topic_0057311027_p32016130171039"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311027_p53878535171039"><a name="en-us_topic_0057311027_p53878535171039"></a><a name="en-us_topic_0057311027_p53878535171039"></a>Number of record sets in the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311027_row48476716171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311027_p54136527171039"><a name="en-us_topic_0057311027_p54136527171039"></a><a name="en-us_topic_0057311027_p54136527171039"></a>pool_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311027_p48020249171039"><a name="en-us_topic_0057311027_p48020249171039"></a><a name="en-us_topic_0057311027_p48020249171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311027_p63987755171039"><a name="en-us_topic_0057311027_p63987755171039"></a><a name="en-us_topic_0057311027_p63987755171039"></a>Pool ID of the zone, which is assigned by the system</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311027_row49967872171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311027_p35791512171039"><a name="en-us_topic_0057311027_p35791512171039"></a><a name="en-us_topic_0057311027_p35791512171039"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311027_p10454086171039"><a name="en-us_topic_0057311027_p10454086171039"></a><a name="en-us_topic_0057311027_p10454086171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311027_p8704812171039"><a name="en-us_topic_0057311027_p8704812171039"></a><a name="en-us_topic_0057311027_p8704812171039"></a>Project ID of the zone</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311027_row27690345171039"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311027_p48529730171039"><a name="en-us_topic_0057311027_p48529730171039"></a><a name="en-us_topic_0057311027_p48529730171039"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311027_p59988242171039"><a name="en-us_topic_0057311027_p59988242171039"></a><a name="en-us_topic_0057311027_p59988242171039"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311027_p9292793171039"><a name="en-us_topic_0057311027_p9292793171039"></a><a name="en-us_topic_0057311027_p9292793171039"></a>Time when the zone was created</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311027_row4377608115654"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311027_p5844041115654"><a name="en-us_topic_0057311027_p5844041115654"></a><a name="en-us_topic_0057311027_p5844041115654"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311027_p3605288915654"><a name="en-us_topic_0057311027_p3605288915654"></a><a name="en-us_topic_0057311027_p3605288915654"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311027_p3460290715654"><a name="en-us_topic_0057311027_p3460290715654"></a><a name="en-us_topic_0057311027_p3460290715654"></a>Time when the zone was updated</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311027_row384676871572"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311027_p288749251572"><a name="en-us_topic_0057311027_p288749251572"></a><a name="en-us_topic_0057311027_p288749251572"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311027_p571676251572"><a name="en-us_topic_0057311027_p571676251572"></a><a name="en-us_topic_0057311027_p571676251572"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311027_p50014989155938"><a name="en-us_topic_0057311027_p50014989155938"></a><a name="en-us_topic_0057311027_p50014989155938"></a>Link of the current resource or other related resources</p>
    <p id="en-us_topic_0057311027_p660161572"><a name="en-us_topic_0057311027_p660161572"></a><a name="en-us_topic_0057311027_p660161572"></a>When a response is broken into pages, a <strong id="en-us_topic_0057311027_b84235270695245"><a name="en-us_topic_0057311027_b84235270695245"></a><a name="en-us_topic_0057311027_b84235270695245"></a>next</strong> link is provided to retrieve all results.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311027_row177328815945"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311027_p1595959815945"><a name="en-us_topic_0057311027_p1595959815945"></a><a name="en-us_topic_0057311027_p1595959815945"></a>masters</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311027_p1765902715945"><a name="en-us_topic_0057311027_p1765902715945"></a><a name="en-us_topic_0057311027_p1765902715945"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311027_p2109506015945"><a name="en-us_topic_0057311027_p2109506015945"></a><a name="en-us_topic_0057311027_p2109506015945"></a>Master DNS servers, from which the slave servers get DNS information</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057311027_row57448667171910"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057311027_p3560499171932"><a name="en-us_topic_0057311027_p3560499171932"></a><a name="en-us_topic_0057311027_p3560499171932"></a>router</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057311027_p19965041171932"><a name="en-us_topic_0057311027_p19965041171932"></a><a name="en-us_topic_0057311027_p19965041171932"></a>Router</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057311027_p6555635171932"><a name="en-us_topic_0057311027_p6555635171932"></a><a name="en-us_topic_0057311027_p6555635171932"></a>Router information (VPC associated with the zone)</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Response example

    ```
    {
        "id": "ff8080825b8fc86c015b94bc6f8712c3",
        "name": "example.com.",
        "description": "This is an example zone.",
        "email": "xx@example.com",
        "ttl": 300,
        "serial": 1,
        "masters": [],
        "status": "ACTIVE",
        "links": {
            "self": "https://Endpoint/v2/zones/ff8080825b8fc86c015b94bc6f8712c3"
        },
        "pool_id": "ff8080825ab738f4015ab7513298010e",
        "project_id": "e55c6f3dc4e34c9f86353b664ae0e70c",
        "zone_type": "private",
        "created_at": "2017-04-22T08:17:08.997",
        "updated_at": "2017-04-22T08:17:10.849",
        "record_num": 2,
        "routers": {
            "status": "PENDING_CREATE",
            "router_id": "19664294-0bf6-4271-ad3a-94b8c79c6558",
            "router_region": "xx"
        }
    }
    
    ```


## **Returned Value**<a name="section1917896317411"></a>

See  [General Request Return Code](general-request-return-code.md).

