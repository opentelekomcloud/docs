# Configuring a PTR Record<a name="EN-US_TOPIC_0042318613"></a>

## Function<a name="section2763065016101"></a>

Configure the PTR record for an elastic IP address \(EIP\).

## URI<a name="section53701671161015"></a>

-   URI format

    PATCH /v2/reverse/floatingips/\{region\}:\{floatingip\_id\}

-   Parameter description

    **Table  1**  Parameters in the URI

    <a name="table6099729418149"></a><table><thead align="left"><tr id="row3442661918149"><th class="cellrowborder" valign="top" width="20.380000000000003%" id="mcps1.2.5.1.1"><p id="p3709279118149"><a name="p3709279118149"></a><a name="p3709279118149"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.439999999999998%" id="mcps1.2.5.1.2"><p id="p5172606218149"><a name="p5172606218149"></a><a name="p5172606218149"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.59%" id="mcps1.2.5.1.3"><p id="p2906151418149"><a name="p2906151418149"></a><a name="p2906151418149"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.589999999999996%" id="mcps1.2.5.1.4"><p id="p517246718149"><a name="p517246718149"></a><a name="p517246718149"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1631668818149"><td class="cellrowborder" valign="top" width="20.380000000000003%" headers="mcps1.2.5.1.1 "><p id="p4658337018149"><a name="p4658337018149"></a><a name="p4658337018149"></a>region</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.2.5.1.2 "><p id="p1515661618149"><a name="p1515661618149"></a><a name="p1515661618149"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.59%" headers="mcps1.2.5.1.3 "><p id="p1972638718149"><a name="p1972638718149"></a><a name="p1972638718149"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.589999999999996%" headers="mcps1.2.5.1.4 "><p id="p5433349018149"><a name="p5433349018149"></a><a name="p5433349018149"></a>Region of the tenant</p>
    </td>
    </tr>
    <tr id="row1923936518149"><td class="cellrowborder" valign="top" width="20.380000000000003%" headers="mcps1.2.5.1.1 "><p id="p1488470218149"><a name="p1488470218149"></a><a name="p1488470218149"></a>floatingip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.2.5.1.2 "><p id="p6481017518149"><a name="p6481017518149"></a><a name="p6481017518149"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.59%" headers="mcps1.2.5.1.3 "><p id="p1513281718149"><a name="p1513281718149"></a><a name="p1513281718149"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.589999999999996%" headers="mcps1.2.5.1.4 "><p id="p1779865118149"><a name="p1779865118149"></a><a name="p1779865118149"></a>EIP ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section44958995161021"></a>

-   Parameter description

    **Table  2**  Parameters in the request

    <a name="table239794161830"></a><table><thead align="left"><tr id="row654560711830"><th class="cellrowborder" valign="top" width="19.251925192519252%" id="mcps1.2.5.1.1"><p id="p3415211830"><a name="p3415211830"></a><a name="p3415211830"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.23182318231823%" id="mcps1.2.5.1.2"><p id="p276632601830"><a name="p276632601830"></a><a name="p276632601830"></a><strong id="b53247500142936"><a name="b53247500142936"></a><a name="b53247500142936"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.151415141514152%" id="mcps1.2.5.1.3"><p id="p261316001830"><a name="p261316001830"></a><a name="p261316001830"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.36483648364836%" id="mcps1.2.5.1.4"><p id="p362848191830"><a name="p362848191830"></a><a name="p362848191830"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row533892641830"><td class="cellrowborder" valign="top" width="19.251925192519252%" headers="mcps1.2.5.1.1 "><p id="p295631171830"><a name="p295631171830"></a><a name="p295631171830"></a>ptrdname</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.2 "><p id="p458022581830"><a name="p458022581830"></a><a name="p458022581830"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.151415141514152%" headers="mcps1.2.5.1.3 "><p id="p189954321830"><a name="p189954321830"></a><a name="p189954321830"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.36483648364836%" headers="mcps1.2.5.1.4 "><p id="p622350301830"><a name="p622350301830"></a><a name="p622350301830"></a>Domain name of the PTR record</p>
    <p id="p27471407151355"><a name="p27471407151355"></a><a name="p27471407151355"></a>A domain name is case insensitive. Uppercase letters will also be converted into lowercase letters.</p>
    </td>
    </tr>
    <tr id="row232443661830"><td class="cellrowborder" valign="top" width="19.251925192519252%" headers="mcps1.2.5.1.1 "><p id="p37455251830"><a name="p37455251830"></a><a name="p37455251830"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.2 "><p id="p349520711830"><a name="p349520711830"></a><a name="p349520711830"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.151415141514152%" headers="mcps1.2.5.1.3 "><p id="p125455181830"><a name="p125455181830"></a><a name="p125455181830"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.36483648364836%" headers="mcps1.2.5.1.4 "><p id="p95540661830"><a name="p95540661830"></a><a name="p95540661830"></a>PTR record description</p>
    </td>
    </tr>
    <tr id="row356818821830"><td class="cellrowborder" valign="top" width="19.251925192519252%" headers="mcps1.2.5.1.1 "><p id="p45513431830"><a name="p45513431830"></a><a name="p45513431830"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.2 "><p id="p331144881830"><a name="p331144881830"></a><a name="p331144881830"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.151415141514152%" headers="mcps1.2.5.1.3 "><p id="p650278701830"><a name="p650278701830"></a><a name="p650278701830"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.36483648364836%" headers="mcps1.2.5.1.4 "><p id="p2245129014581"><a name="p2245129014581"></a><a name="p2245129014581"></a>Caching period of a PTR record (in seconds)</p>
    <p id="p327660881830"><a name="p327660881830"></a><a name="p327660881830"></a>The default value is <strong id="b2896613691415"><a name="b2896613691415"></a><a name="b2896613691415"></a>300s</strong>.</p>
    <p id="p368074541830"><a name="p368074541830"></a><a name="p368074541830"></a>The value range is 300–2147483647.</p>
    </td>
    </tr>
    <tr id="row13969437195229"><td class="cellrowborder" valign="top" width="19.251925192519252%" headers="mcps1.2.5.1.1 "><p id="p42211177195229"><a name="p42211177195229"></a><a name="p42211177195229"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.2 "><p id="p63662158195229"><a name="p63662158195229"></a><a name="p63662158195229"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.151415141514152%" headers="mcps1.2.5.1.3 "><p id="p56361188195229"><a name="p56361188195229"></a><a name="p56361188195229"></a>List&lt;tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.36483648364836%" headers="mcps1.2.5.1.4 "><p id="p1853522195229"><a name="p1853522195229"></a><a name="p1853522195229"></a>Resource tag. </p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the tag list

    <a name="table9752964195025"></a><table><thead align="left"><tr id="en-us_topic_0057310891_row15361836112436"><th class="cellrowborder" valign="top" width="17.28%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057310891_p58707511112436"><a name="en-us_topic_0057310891_p58707511112436"></a><a name="en-us_topic_0057310891_p58707511112436"></a><strong id="en-us_topic_0057310891_b162774213314533"><a name="en-us_topic_0057310891_b162774213314533"></a><a name="en-us_topic_0057310891_b162774213314533"></a>Parameter</strong></p>
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
        "ptrdname": "www.example.com",
        "description": "Description for this PTR record",
        "ttl": 300
    }
    ```


## Response<a name="section40090803161031"></a>

-   Parameter description

    **Table  4**  Parameters in the response

    <a name="table6558745818456"></a><table><thead align="left"><tr id="row5725206118456"><th class="cellrowborder" valign="top" width="18.37%" id="mcps1.2.4.1.1"><p id="p690539418456"><a name="p690539418456"></a><a name="p690539418456"></a><strong id="b162774213314533_2"><a name="b162774213314533_2"></a><a name="b162774213314533_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.87%" id="mcps1.2.4.1.2"><p id="p2246606418456"><a name="p2246606418456"></a><a name="p2246606418456"></a><strong id="b84235270619112_2"><a name="b84235270619112_2"></a><a name="b84235270619112_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="66.75999999999999%" id="mcps1.2.4.1.3"><p id="p781187018456"><a name="p781187018456"></a><a name="p781187018456"></a><strong id="b842352706112423_2"><a name="b842352706112423_2"></a><a name="b842352706112423_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2878170018456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p4961636318456"><a name="p4961636318456"></a><a name="p4961636318456"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="p5950245818456"><a name="p5950245818456"></a><a name="p5950245818456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="p5496981818456"><a name="p5496981818456"></a><a name="p5496981818456"></a>PTR record ID, which is in <strong id="b842352706151833"><a name="b842352706151833"></a><a name="b842352706151833"></a>{region}:{floatingip_id}</strong> format</p>
    </td>
    </tr>
    <tr id="row3274940018456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p3545576918456"><a name="p3545576918456"></a><a name="p3545576918456"></a>ptrdname</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="p5334507918456"><a name="p5334507918456"></a><a name="p5334507918456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="p2598415318456"><a name="p2598415318456"></a><a name="p2598415318456"></a>Domain name of the PTR record</p>
    </td>
    </tr>
    <tr id="row3253079218456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p1774845918456"><a name="p1774845918456"></a><a name="p1774845918456"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="p2833911218456"><a name="p2833911218456"></a><a name="p2833911218456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="p1376672518456"><a name="p1376672518456"></a><a name="p1376672518456"></a>PTR record description</p>
    </td>
    </tr>
    <tr id="row5679166318456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p3672198418456"><a name="p3672198418456"></a><a name="p3672198418456"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="p2169069318456"><a name="p2169069318456"></a><a name="p2169069318456"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="p65120323151724"><a name="p65120323151724"></a><a name="p65120323151724"></a>Caching period of a PTR record (in seconds)</p>
    <p id="p1211568618456"><a name="p1211568618456"></a><a name="p1211568618456"></a>The default value is <strong id="b766716615417"><a name="b766716615417"></a><a name="b766716615417"></a>300s</strong>.</p>
    <p id="p4184654118456"><a name="p4184654118456"></a><a name="p4184654118456"></a>The value range is 300–2147483647.</p>
    </td>
    </tr>
    <tr id="row3412662318456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p1279309418456"><a name="p1279309418456"></a><a name="p1279309418456"></a>address</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="p2960772218456"><a name="p2960772218456"></a><a name="p2960772218456"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="p4941528218456"><a name="p4941528218456"></a><a name="p4941528218456"></a>EIP</p>
    </td>
    </tr>
    <tr id="row4208435918456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p5338995318456"><a name="p5338995318456"></a><a name="p5338995318456"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="p2961896418456"><a name="p2961896418456"></a><a name="p2961896418456"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="p5032586318456"><a name="p5032586318456"></a><a name="p5032586318456"></a>Resource status</p>
    <p id="p55721846144628"><a name="p55721846144628"></a><a name="p55721846144628"></a>The value can be <strong id="b84235270695628"><a name="b84235270695628"></a><a name="b84235270695628"></a>PENDING_CREATE</strong>, <strong id="b84235270695635"><a name="b84235270695635"></a><a name="b84235270695635"></a>ACTIVE</strong>, <strong id="b84235270695643"><a name="b84235270695643"></a><a name="b84235270695643"></a>PENDING_DELETE</strong>, <strong id="b842352706141041"><a name="b842352706141041"></a><a name="b842352706141041"></a>PENDING_UPDATE</strong>, or <strong id="b84235270695650"><a name="b84235270695650"></a><a name="b84235270695650"></a>ERROR</strong>.</p>
    </td>
    </tr>
    <tr id="row4986307418456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p1237719818456"><a name="p1237719818456"></a><a name="p1237719818456"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="p6302897818456"><a name="p6302897818456"></a><a name="p6302897818456"></a>enum</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="p507362318456"><a name="p507362318456"></a><a name="p507362318456"></a>Requested operation on the resource</p>
    <p id="p9217462145017"><a name="p9217462145017"></a><a name="p9217462145017"></a>The value can be <strong id="b842352706141356"><a name="b842352706141356"></a><a name="b842352706141356"></a>CREATE</strong>, <strong id="b84235270614144"><a name="b84235270614144"></a><a name="b84235270614144"></a>UPDATE</strong>, or <strong id="b84235270614146"><a name="b84235270614146"></a><a name="b84235270614146"></a>DELETE</strong>.</p>
    </td>
    </tr>
    <tr id="row831034118456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p204899518456"><a name="p204899518456"></a><a name="p204899518456"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="p3175087318456"><a name="p3175087318456"></a><a name="p3175087318456"></a>object</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="p2168392018456"><a name="p2168392018456"></a><a name="p2168392018456"></a>Link of the current resource or other related resources</p>
    <p id="p6093755518456"><a name="p6093755518456"></a><a name="p6093755518456"></a>When a response is broken into pages, a <strong id="b84235270695245"><a name="b84235270695245"></a><a name="b84235270695245"></a>next</strong> link is provided to retrieve all results.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "id": "region\_id:c5504932-bf23-4171-b655-b87a6bc59334",
        "ptrdname": "www.example.com.",
        "description": "Description for this PTR record",
        "address": "10.154.52.138",
        "action": "CREATE",
        "ttl": 300,
        "status": "PENDING_CREATE",
        "links": {
            "self": "https://Endpoint/v2/reverse/floatingips/region\_id:c5504932-bf23-4171-b655-b87a6bc59334"
        }
    }
    ```


## **Returned Value**<a name="section42637797161043"></a>

See  [General Request Return Code](general-request-return-code.md).

