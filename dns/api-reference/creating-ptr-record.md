# Creating PTR Record<a name="dns_api_66002"></a>

## Function<a name="section2763065016101"></a>

Create a PTR record for an elastic IP address \(EIP\).

## URI<a name="section53701671161015"></a>

PATCH /v2/reverse/floatingips/\{region\}:\{floatingip\_id\}

For details, see  [Table 1](#table6099729418149).

**Table  1**  Parameters in the URI

<a name="table6099729418149"></a>
<table><thead align="left"><tr id="row3442661918149"><th class="cellrowborder" valign="top" width="20.380000000000003%" id="mcps1.2.5.1.1"><p id="p3709279118149"><a name="p3709279118149"></a><a name="p3709279118149"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
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
<td class="cellrowborder" valign="top" width="13.59%" headers="mcps1.2.5.1.3 "><p id="p1972638718149"><a name="p1972638718149"></a><a name="p1972638718149"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.589999999999996%" headers="mcps1.2.5.1.4 "><p id="p5433349018149"><a name="p5433349018149"></a><a name="p5433349018149"></a>Region of the tenant. </p>
</td>
</tr>
<tr id="row1923936518149"><td class="cellrowborder" valign="top" width="20.380000000000003%" headers="mcps1.2.5.1.1 "><p id="p1488470218149"><a name="p1488470218149"></a><a name="p1488470218149"></a>floatingip_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.2.5.1.2 "><p id="p6481017518149"><a name="p6481017518149"></a><a name="p6481017518149"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.59%" headers="mcps1.2.5.1.3 "><p id="p1513281718149"><a name="p1513281718149"></a><a name="p1513281718149"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.589999999999996%" headers="mcps1.2.5.1.4 "><p id="p1779865118149"><a name="p1779865118149"></a><a name="p1779865118149"></a>EIP ID</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section44958995161021"></a>

-   Parameter description

    **Table  2**  Parameters in the request

    <a name="table239794161830"></a>
    <table><thead align="left"><tr id="row654560711830"><th class="cellrowborder" valign="top" width="19.251925192519252%" id="mcps1.2.5.1.1"><p id="p3415211830"><a name="p3415211830"></a><a name="p3415211830"></a><strong id="b41677924"><a name="b41677924"></a><a name="b41677924"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.23182318231823%" id="mcps1.2.5.1.2"><p id="p276632601830"><a name="p276632601830"></a><a name="p276632601830"></a><strong id="b53247500142936"><a name="b53247500142936"></a><a name="b53247500142936"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.151415141514152%" id="mcps1.2.5.1.3"><p id="p261316001830"><a name="p261316001830"></a><a name="p261316001830"></a><strong id="b1084351182"><a name="b1084351182"></a><a name="b1084351182"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.36483648364836%" id="mcps1.2.5.1.4"><p id="p362848191830"><a name="p362848191830"></a><a name="p362848191830"></a><strong id="b938122000"><a name="b938122000"></a><a name="b938122000"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row533892641830"><td class="cellrowborder" valign="top" width="19.251925192519252%" headers="mcps1.2.5.1.1 "><p id="p295631171830"><a name="p295631171830"></a><a name="p295631171830"></a>ptrdname</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.2 "><p id="p458022581830"><a name="p458022581830"></a><a name="p458022581830"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.151415141514152%" headers="mcps1.2.5.1.3 "><p id="p189954321830"><a name="p189954321830"></a><a name="p189954321830"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.36483648364836%" headers="mcps1.2.5.1.4 "><p id="p622350301830"><a name="p622350301830"></a><a name="p622350301830"></a>Domain name of the PTR record</p>
    <p id="p27471407151355"><a name="p27471407151355"></a><a name="p27471407151355"></a>A domain name is case insensitive. Uppercase letters will also be converted into lowercase letters.</p>
    </td>
    </tr>
    <tr id="row232443661830"><td class="cellrowborder" valign="top" width="19.251925192519252%" headers="mcps1.2.5.1.1 "><p id="p37455251830"><a name="p37455251830"></a><a name="p37455251830"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.2 "><p id="p349520711830"><a name="p349520711830"></a><a name="p349520711830"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.151415141514152%" headers="mcps1.2.5.1.3 "><p id="p125455181830"><a name="p125455181830"></a><a name="p125455181830"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.36483648364836%" headers="mcps1.2.5.1.4 "><p id="p95540661830"><a name="p95540661830"></a><a name="p95540661830"></a>PTR record description</p>
    <p id="p14845539143311"><a name="p14845539143311"></a><a name="p14845539143311"></a>The value is left blank by default.</p>
    </td>
    </tr>
    <tr id="row356818821830"><td class="cellrowborder" valign="top" width="19.251925192519252%" headers="mcps1.2.5.1.1 "><p id="p45513431830"><a name="p45513431830"></a><a name="p45513431830"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.2 "><p id="p331144881830"><a name="p331144881830"></a><a name="p331144881830"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.151415141514152%" headers="mcps1.2.5.1.3 "><p id="p650278701830"><a name="p650278701830"></a><a name="p650278701830"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.36483648364836%" headers="mcps1.2.5.1.4 "><p id="p123031523174010"><a name="p123031523174010"></a><a name="p123031523174010"></a>PTR record cache duration (in second) on a local DNS server. The longer the duration is, the slower the update takes effect.</p>
    <p id="p1030317233408"><a name="p1030317233408"></a><a name="p1030317233408"></a>If your service address is frequently changed, set TTL to a smaller value.</p>
    <p id="p368074541830"><a name="p368074541830"></a><a name="p368074541830"></a>The value ranges from <strong id="b8393910205320"><a name="b8393910205320"></a><a name="b8393910205320"></a>1</strong> to <strong id="b10699013125317"><a name="b10699013125317"></a><a name="b10699013125317"></a>2147483647</strong>.</p>
    <p id="p1339417482339"><a name="p1339417482339"></a><a name="p1339417482339"></a>The default value is <strong id="b998224515116"><a name="b998224515116"></a><a name="b998224515116"></a>300</strong>.</p>
    </td>
    </tr>
    <tr id="row13969437195229"><td class="cellrowborder" valign="top" width="19.251925192519252%" headers="mcps1.2.5.1.1 "><p id="p42211177195229"><a name="p42211177195229"></a><a name="p42211177195229"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.23182318231823%" headers="mcps1.2.5.1.2 "><p id="p63662158195229"><a name="p63662158195229"></a><a name="p63662158195229"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.151415141514152%" headers="mcps1.2.5.1.3 "><p id="p56361188195229"><a name="p56361188195229"></a><a name="p56361188195229"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.36483648364836%" headers="mcps1.2.5.1.4 "><p id="p1853522195229"><a name="p1853522195229"></a><a name="p1853522195229"></a>Resource tag. For details, see <a href="data-structure.md#table19530794112436">Table 2</a>.</p>
    <p id="p15941338343"><a name="p15941338343"></a><a name="p15941338343"></a>The value is left blank by default.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    Create a PTR record for the EIP whose ID is  _Region ID_:c5504932-bf23-4171-b655-b87a6bc59334:

    ```
    PATCH https://{DNS_Endpoint}/v2/reverse/floatingips/region_id:c5504932-bf23-4171-b655-b87a6bc59334
    ```

    ```
    {
        "ptrdname": "www.example.com",
        "description": "Description for this PTR record",
        "ttl": 300,
        "tags": [ 
            { 
              "key": "key1", 
              "value": "value1" 
            } 
        ] 
    }
    ```


## Response<a name="section40090803161031"></a>

-   Parameter description

    **Table  3**  Parameters in the response

    <a name="table6558745818456"></a>
    <table><thead align="left"><tr id="row5725206118456"><th class="cellrowborder" valign="top" width="18.37%" id="mcps1.2.4.1.1"><p id="p690539418456"><a name="p690539418456"></a><a name="p690539418456"></a><strong id="b1958727690"><a name="b1958727690"></a><a name="b1958727690"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.87%" id="mcps1.2.4.1.2"><p id="p2246606418456"><a name="p2246606418456"></a><a name="p2246606418456"></a><strong id="b1057399781"><a name="b1057399781"></a><a name="b1057399781"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="66.75999999999999%" id="mcps1.2.4.1.3"><p id="p781187018456"><a name="p781187018456"></a><a name="p781187018456"></a><strong id="b972289688"><a name="b972289688"></a><a name="b972289688"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2878170018456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p4961636318456"><a name="p4961636318456"></a><a name="p4961636318456"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="p5950245818456"><a name="p5950245818456"></a><a name="p5950245818456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="p5496981818456"><a name="p5496981818456"></a><a name="p5496981818456"></a>PTR record ID, which is in <strong id="b842352706151833"><a name="b842352706151833"></a><a name="b842352706151833"></a>{region}:{floatingip_id}</strong> format</p>
    </td>
    </tr>
    <tr id="row3274940018456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p3545576918456"><a name="p3545576918456"></a><a name="p3545576918456"></a>ptrdname</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="p5334507918456"><a name="p5334507918456"></a><a name="p5334507918456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="p2598415318456"><a name="p2598415318456"></a><a name="p2598415318456"></a>Domain name of the PTR record</p>
    </td>
    </tr>
    <tr id="row3253079218456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p1774845918456"><a name="p1774845918456"></a><a name="p1774845918456"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="p2833911218456"><a name="p2833911218456"></a><a name="p2833911218456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="p1376672518456"><a name="p1376672518456"></a><a name="p1376672518456"></a>PTR record description</p>
    </td>
    </tr>
    <tr id="row5679166318456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p3672198418456"><a name="p3672198418456"></a><a name="p3672198418456"></a>ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="p2169069318456"><a name="p2169069318456"></a><a name="p2169069318456"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="p73714549431"><a name="p73714549431"></a><a name="p73714549431"></a>PTR record cache duration (in second) on a local DNS server. The longer the duration is, the slower the update takes effect.</p>
    <p id="p1837175484310"><a name="p1837175484310"></a><a name="p1837175484310"></a>If your service address is frequently changed, set TTL to a smaller value.</p>
    <p id="p4184654118456"><a name="p4184654118456"></a><a name="p4184654118456"></a>The value ranges from <strong id="b14395111215615"><a name="b14395111215615"></a><a name="b14395111215615"></a>1</strong> to <strong id="b9824181610567"><a name="b9824181610567"></a><a name="b9824181610567"></a>2147483647</strong>.</p>
    <p id="p8320130104412"><a name="p8320130104412"></a><a name="p8320130104412"></a>The default value is <strong id="b11241724579"><a name="b11241724579"></a><a name="b11241724579"></a>300</strong>.</p>
    </td>
    </tr>
    <tr id="row3412662318456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p1279309418456"><a name="p1279309418456"></a><a name="p1279309418456"></a>address</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="p2960772218456"><a name="p2960772218456"></a><a name="p2960772218456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="p4941528218456"><a name="p4941528218456"></a><a name="p4941528218456"></a>EIP</p>
    </td>
    </tr>
    <tr id="row4208435918456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p5338995318456"><a name="p5338995318456"></a><a name="p5338995318456"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="p2961896418456"><a name="p2961896418456"></a><a name="p2961896418456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="p5032586318456"><a name="p5032586318456"></a><a name="p5032586318456"></a>Resource status</p>
    <p id="p55966391353"><a name="p55966391353"></a><a name="p55966391353"></a>For details, see <a href="enumeration-values.md#section33673592114748">Resource Status</a>.</p>
    </td>
    </tr>
    <tr id="row4986307418456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p1237719818456"><a name="p1237719818456"></a><a name="p1237719818456"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="p6302897818456"><a name="p6302897818456"></a><a name="p6302897818456"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="p507362318456"><a name="p507362318456"></a><a name="p507362318456"></a>Requested operation on the resource</p>
    <p id="p13931119183618"><a name="p13931119183618"></a><a name="p13931119183618"></a>The value can be <strong id="b842352706141356"><a name="b842352706141356"></a><a name="b842352706141356"></a>CREATE</strong>, <strong id="b84235270614144"><a name="b84235270614144"></a><a name="b84235270614144"></a>UPDATE</strong>, <strong id="b84235270614146"><a name="b84235270614146"></a><a name="b84235270614146"></a>DELETE</strong>, or <strong id="b23344111882"><a name="b23344111882"></a><a name="b23344111882"></a>NONE</strong>.</p>
    <p id="p178601911399"><a name="p178601911399"></a><a name="p178601911399"></a><strong id="b4481648153717"><a name="b4481648153717"></a><a name="b4481648153717"></a>NONE</strong> indicates that no operation will be performed.</p>
    </td>
    </tr>
    <tr id="row831034118456"><td class="cellrowborder" valign="top" width="18.37%" headers="mcps1.2.4.1.1 "><p id="p204899518456"><a name="p204899518456"></a><a name="p204899518456"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.87%" headers="mcps1.2.4.1.2 "><p id="p3175087318456"><a name="p3175087318456"></a><a name="p3175087318456"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.75999999999999%" headers="mcps1.2.4.1.3 "><p id="p2168392018456"><a name="p2168392018456"></a><a name="p2168392018456"></a>Link to the current resource or other related resources</p>
    <p id="p6093755518456"><a name="p6093755518456"></a><a name="p6093755518456"></a>When a response is broken into pages, a <strong id="b84235270695245"><a name="b84235270695245"></a><a name="b84235270695245"></a>next</strong> link is provided to retrieve all results. For details, see <a href="#table354521744216">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Parameters in the  **links**  field

    <a name="table354521744216"></a>
    <table><thead align="left"><tr id="row954518179427"><th class="cellrowborder" valign="top" width="18.3018301830183%" id="mcps1.2.4.1.1"><p id="p654513173424"><a name="p654513173424"></a><a name="p654513173424"></a><strong id="b589611720127"><a name="b589611720127"></a><a name="b589611720127"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.591959195919593%" id="mcps1.2.4.1.2"><p id="p654551714212"><a name="p654551714212"></a><a name="p654551714212"></a><strong id="b1783669993"><a name="b1783669993"></a><a name="b1783669993"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.10621062106211%" id="mcps1.2.4.1.3"><p id="p1545141717427"><a name="p1545141717427"></a><a name="p1545141717427"></a><strong id="b1984681812125"><a name="b1984681812125"></a><a name="b1984681812125"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3545101710429"><td class="cellrowborder" valign="top" width="18.3018301830183%" headers="mcps1.2.4.1.1 "><p id="p115467171428"><a name="p115467171428"></a><a name="p115467171428"></a>self</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.591959195919593%" headers="mcps1.2.4.1.2 "><p id="p254611713427"><a name="p254611713427"></a><a name="p254611713427"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.10621062106211%" headers="mcps1.2.4.1.3 "><p id="p5546171744214"><a name="p5546171744214"></a><a name="p5546171744214"></a>Link to the current resource</p>
    </td>
    </tr>
    <tr id="row62371226175119"><td class="cellrowborder" valign="top" width="18.3018301830183%" headers="mcps1.2.4.1.1 "><p id="p136561245153620"><a name="p136561245153620"></a><a name="p136561245153620"></a>next</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.591959195919593%" headers="mcps1.2.4.1.2 "><p id="p19656144517367"><a name="p19656144517367"></a><a name="p19656144517367"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.10621062106211%" headers="mcps1.2.4.1.3 "><p id="p76567451365"><a name="p76567451365"></a><a name="p76567451365"></a>Link to the next page</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "id": "region_id:c5504932-bf23-4171-b655-b87a6bc59334",
        "ptrdname": "www.example.com.",
        "description": "Description for this PTR record",
        "address": "10.154.52.138",
        "action": "CREATE",
        "ttl": 300,
        "status": "PENDING_CREATE",
        "links": {
            "self": "https://Endpoint/v2/reverse/floatingips/region_id:c5504932-bf23-4171-b655-b87a6bc59334"
        }
    }
    ```


## Returned Value<a name="section9249181042119"></a>

If the API call returns a code of 2_xx_, for example, 200, 202, or 204, the request is successful.

For details, see  [Status Code](status-code.md).

