# How Can I Configure a PTR Record for an ECS Private IP Address?<a name="dns_faq_031"></a>

PTR records enable visitors to query domain names based on IP addresses.

On the **PTR Records** page on the DNS console, you can configure PTR records for EIPs. If you want to add PTR records for ECS private IP addresses, create a private zone and create PTR records in the zone.

The domain name in a PTR record is specified in the ***x.x.x.x*.in-addr.arpa** format.

> ![](public_sys-resources/icon-note.gif) **NOTE:** 

> **in-addr.arpa** is the top-level domain for reverse resolution.

> For example, if the private IP address is **192.168.1.10**, its domain name in the PTR record is **10.1.168.192.in-addr.arpa**.

> In this case, you need to create a private zone **192.in-addr.arpa** and add a PTR record **10.1.168.192.in-addr.arpa**.

## Creating a Private Zone<a name="section75811117181517"></a>

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, Choose **Private Zones**.

    The **Private Zones** page is displayed.

4.  Click ![](figures/en-us_image_0073591874.png) on the upper left and select the desired region and project.
5.  Click **Create Private Zone**.

    **Figure 1** Create Private Zone<a name="fig339815012595"></a>
    ![](figures/create-a-private-zone.png "Create Private Zone")

6.  Configure the parameters according to [Table 1](#table12455154165118).**Table 1** Parameters required for creating a private zone

    <a name="table12455154165118"></a><table><thead align="left"><tr id="row54556485113"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p44551945516"><a name="p44551945516"></a><a name="p44551945516"></a><strong id="b84235270695255"><a name="b84235270695255"></a><a name="b84235270695255"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p44553411510"><a name="p44553411510"></a><a name="p44553411510"></a><strong id="en-us_topic_0035268497_b8423527061433"><a name="en-us_topic_0035268497_b8423527061433"></a><a name="en-us_topic_0035268497_b8423527061433"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p10455154125113"><a name="p10455154125113"></a><a name="p10455154125113"></a><strong id="b84235270617114"><a name="b84235270617114"></a><a name="b84235270617114"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row144553495114"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p645619414517"><a name="p645619414517"></a><a name="p645619414517"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p51968545220"><a name="p51968545220"></a><a name="p51968545220"></a>Domain name</p>
    <p id="p151961957522"><a name="p151961957522"></a><a name="p151961957522"></a>Set the top-level domain to <strong id="b84235270692248"><a name="b84235270692248"></a><a name="b84235270692248"></a>in-addr.arpa</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p174562418510"><a name="p174562418510"></a><a name="p174562418510"></a>192.in-addr.arpa</p>
    </td>
    </tr>
    <tr id="row5456845517"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p84561645514"><a name="p84561645514"></a><a name="p84561645514"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1645674145115"><a name="p1645674145115"></a><a name="p1645674145115"></a>VPC to be associated with the private zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p104567425119"><a name="p104567425119"></a><a name="p104567425119"></a>-</p>
    </td>
    </tr>
    <tr id="row145614175118"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p174561745510"><a name="p174561745510"></a><a name="p174561745510"></a>Email</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1071157192158"><a name="p1071157192158"></a><a name="p1071157192158"></a>(Optional) Email address of the administrator managing the private zone</p>
    <p id="p126950408523"><a name="p126950408523"></a><a name="p126950408523"></a>It is recommended that you set the email address to <strong id="b842352706182128"><a name="b842352706182128"></a><a name="b842352706182128"></a>HOSTMASTER@<em id="i842352697182143"><a name="i842352697182143"></a><a name="i842352697182143"></a>Domain name</em></strong>.</p>
    <p id="p1069694012522"><a name="p1069694012522"></a><a name="p1069694012522"></a>For more details about the email address, see <a href="why-is-the-email-address-format-changed-in-the-soa-record.html">Why Is the Email Address Format Changed in the SOA Record?</a></p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p345613435118"><a name="p345613435118"></a><a name="p345613435118"></a>HOSTMASTER@example.com</p>
    </td>
    </tr>
    <tr id="row18748159183818"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p18481122652416"><a name="p18481122652416"></a><a name="p18481122652416"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p18551159141412"><a name="p18551159141412"></a><a name="p18551159141412"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a zone.</p>
    <p id="p1690771316155"><a name="p1690771316155"></a><a name="p1690771316155"></a>For details about tag key and value requirements, see <a href="#dns_faq_031__table114584301390">Table 2</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p15551259121412"><a name="p15551259121412"></a><a name="p15551259121412"></a>example_key1</p>
    <p id="p15031954131915"><a name="p15031954131915"></a><a name="p15031954131915"></a>example_value1</p>
    </td>
    </tr>
    <tr id="row64563417519"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p545619418517"><a name="p545619418517"></a><a name="p545619418517"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p6836195285214"><a name="p6836195285214"></a><a name="p6836195285214"></a>(Optional) Description of the domain name, which cannot exceed 255 characters</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p84561846519"><a name="p84561846519"></a><a name="p84561846519"></a>This is a private zone.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table 2** Tag key and value requirements

    <a name="table114584301390"></a><table><thead align="left"><tr id="en-us_topic_0057777026_en-us_topic_0035467699_row72901535141713"><th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057777026_en-us_topic_0035467699_p132908358173"><a name="en-us_topic_0057777026_en-us_topic_0035467699_p132908358173"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_p132908358173"></a><strong id="en-us_topic_0057777026_en-us_topic_0035467699_b8423527069525"><a name="en-us_topic_0057777026_en-us_topic_0035467699_b8423527069525"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_b8423527069525"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.505050505050505%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057777026_en-us_topic_0035467699_p1629093517175"><a name="en-us_topic_0057777026_en-us_topic_0035467699_p1629093517175"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_p1629093517175"></a><strong id="en-us_topic_0057777026_en-us_topic_0035467699_b842352706171418"><a name="en-us_topic_0057777026_en-us_topic_0035467699_b842352706171418"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_b842352706171418"></a>Requirement</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.313131313131315%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057777026_en-us_topic_0035467699_p32901635141714"><a name="en-us_topic_0057777026_en-us_topic_0035467699_p32901635141714"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_p32901635141714"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0057777026_en-us_topic_0035467699_row52906354176"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057777026_en-us_topic_0035467699_p122901235111715"><a name="en-us_topic_0057777026_en-us_topic_0035467699_p122901235111715"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_p122901235111715"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.505050505050505%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0057777026_en-us_topic_0035467699_ul46253231183"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_ul46253231183"></a><ul id="en-us_topic_0057777026_en-us_topic_0035467699_ul46253231183"><li id="en-us_topic_0057777026_en-us_topic_0035467699_li176251123141812"><a name="en-us_topic_0057777026_en-us_topic_0035467699_li176251123141812"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_li176251123141812"></a>Cannot be left blank.</li><li id="en-us_topic_0057777026_en-us_topic_0035467699_li86261923201810"><a name="en-us_topic_0057777026_en-us_topic_0035467699_li86261923201810"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_li86261923201810"></a>Must be unique for each resource.</li><li id="en-us_topic_0057777026_en-us_topic_0035467699_li162620231180"><a name="en-us_topic_0057777026_en-us_topic_0035467699_li162620231180"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_li162620231180"></a>Consists of at most 36 characters.</li><li id="en-us_topic_0057777026_en-us_topic_0035467699_li5389246102911"><a name="en-us_topic_0057777026_en-us_topic_0035467699_li5389246102911"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_li5389246102911"></a>Contains only letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="31.313131313131315%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057777026_en-us_topic_0035467699_p12290163511720"><a name="en-us_topic_0057777026_en-us_topic_0035467699_p12290163511720"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_p12290163511720"></a>example_key1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057777026_en-us_topic_0035467699_row132900355172"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057777026_en-us_topic_0035467699_p152901635181712"><a name="en-us_topic_0057777026_en-us_topic_0035467699_p152901635181712"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_p152901635181712"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.505050505050505%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0057777026_en-us_topic_0035467699_ul19648123161815"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_ul19648123161815"></a><ul id="en-us_topic_0057777026_en-us_topic_0035467699_ul19648123161815"><li id="en-us_topic_0057777026_en-us_topic_0035467699_li15648193110182"><a name="en-us_topic_0057777026_en-us_topic_0035467699_li15648193110182"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_li15648193110182"></a>Cannot be left blank.</li><li id="en-us_topic_0057777026_en-us_topic_0035467699_li3648143181813"><a name="en-us_topic_0057777026_en-us_topic_0035467699_li3648143181813"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_li3648143181813"></a>Consists of at most 43 characters.</li><li id="en-us_topic_0057777026_en-us_topic_0035467699_li64561823123015"><a name="en-us_topic_0057777026_en-us_topic_0035467699_li64561823123015"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_li64561823123015"></a>Contains only letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="31.313131313131315%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057777026_en-us_topic_0035467699_p62904352179"><a name="en-us_topic_0057777026_en-us_topic_0035467699_p62904352179"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_p62904352179"></a>example_value1</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click **OK**.

    You can query information about the private zone you created on the **Private Zones** page.

    > ![](public_sys-resources/icon-note.gif) **NOTE:** 

    > Click the zone name to query detailed zone information. The system has created record sets of the SOA type and NS type in the zone.

    > -   The SOA record set determines the DNS server that is the authoritative information source for a particular domain name.
    > -   The NS record set defines authoritative DNS servers for a zone.

## Adding a PTR Record<a name="section59204303151"></a>

1.  In the zone list on the **Private Zones** page, click the name of the private zone you created.

    The record set page is displayed.

2.  Click **Add Record Set**.

    The **Add Record Set** box is displayed.

    **Figure 2** Add Record Set<a name="fig14326143110479"></a>
    ![](figures/add-record-set-for-faq.png "Add Record Set")

3.  Configure the parameters according to [Table 3](#table2068616914271).**Table 3** Parameters required for adding a record set of the PTR type

    <a name="table2068616914271"></a><table><thead align="left"><tr id="row14687398277"><th class="cellrowborder" valign="top" width="18.18181818181818%" id="mcps1.2.4.1.1"><p id="p56871894279"><a name="p56871894279"></a><a name="p56871894279"></a><strong id="b84235270695255_1"><a name="b84235270695255_1"></a><a name="b84235270695255_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.2.4.1.2"><p id="p46871191279"><a name="p46871191279"></a><a name="p46871191279"></a><strong id="en-us_topic_0035268497_b8423527061433_1"><a name="en-us_topic_0035268497_b8423527061433_1"></a><a name="en-us_topic_0035268497_b8423527061433_1"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p1568749132716"><a name="p1568749132716"></a><a name="p1568749132716"></a><strong id="b84235270617114_1"><a name="b84235270617114_1"></a><a name="b84235270617114_1"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46871799274"><td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.4.1.1 "><p id="p368713912271"><a name="p368713912271"></a><a name="p368713912271"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.4.1.2 "><p id="p172536599323"><a name="p172536599323"></a><a name="p172536599323"></a>IP address in the PTR record (typed in reverse order)</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p166871919278"><a name="p166871919278"></a><a name="p166871919278"></a>10.1.168</p>
    <p id="p3645662495544"><a name="p3645662495544"></a><a name="p3645662495544"></a>For example, if the IP address is <strong id="b842352706145136"><a name="b842352706145136"></a><a name="b842352706145136"></a>192.168.1.10</strong>, the name of the PTR record is <strong id="b84235270615344"><a name="b84235270615344"></a><a name="b84235270615344"></a>10.1.168.192.in-addr.arpa</strong>.</p>
    <a name="ul772510438411"></a><a name="ul772510438411"></a><ul id="ul772510438411"><li id="li16725124312418"><a name="li16725124312418"></a><a name="li16725124312418"></a>If the private zone name is <strong id="b84235270615732"><a name="b84235270615732"></a><a name="b84235270615732"></a>192.in-addr.arpa</strong>, enter <strong id="b84235270615827"><a name="b84235270615827"></a><a name="b84235270615827"></a>10.1.168</strong> in the box.</li><li id="li16272201077"><a name="li16272201077"></a><a name="li16272201077"></a>If the private zone name is <strong id="b84235270615732_1"><a name="b84235270615732_1"></a><a name="b84235270615732_1"></a>1.168.192.in-addr.arpa</strong>, enter <strong id="b84235270615827_1"><a name="b84235270615827_1"></a><a name="b84235270615827_1"></a>10</strong> in the box.</li></ul>
    </td>
    </tr>
    <tr id="row186872093277"><td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.4.1.1 "><p id="p176871792270"><a name="p176871792270"></a><a name="p176871792270"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.4.1.2 "><p id="p068716910279"><a name="p068716910279"></a><a name="p068716910279"></a>Type of the record</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1868718982720"><a name="p1868718982720"></a><a name="p1868718982720"></a></p>
    <p id="p182891339162315"><a name="p182891339162315"></a><a name="p182891339162315"></a>PTR – Map IP addresses to domains</p>
    </td>
    </tr>
    <tr id="row17687395279"><td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.4.1.1 "><p id="p1268849122712"><a name="p1268849122712"></a><a name="p1268849122712"></a>TTL (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.4.1.2 "><p id="p206881395275"><a name="p206881395275"></a><a name="p206881395275"></a>Caching period of the record set (in seconds)</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1068811962718"><a name="p1068811962718"></a><a name="p1068811962718"></a>The default value is 300s, that is, <strong id="b842352706183837"><a name="b842352706183837"></a><a name="b842352706183837"></a>5 min</strong>.</p>
    </td>
    </tr>
    <tr id="row176881399271"><td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.4.1.1 "><p id="p166882914277"><a name="p166882914277"></a><a name="p166882914277"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.4.1.2 "><p id="p51576321316"><a name="p51576321316"></a><a name="p51576321316"></a>Domain name mapped to the IP address</p>
    <p id="p715713223114"><a name="p715713223114"></a><a name="p715713223114"></a>You can enter only one name at a time.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p36883972711"><a name="p36883972711"></a><a name="p36883972711"></a>mail.example.com</p>
    </td>
    </tr>
    <tr id="row10389125919409"><td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.4.1.1 "><p id="p183901516412"><a name="p183901516412"></a><a name="p183901516412"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.4.1.2 "><p id="p16392191164119"><a name="p16392191164119"></a><a name="p16392191164119"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a record set.</p>
    <p id="p339421184117"><a name="p339421184117"></a><a name="p339421184117"></a>For details about tag key and value requirements, see <a href="#dns_faq_031__table114584301390">Table 2</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p9399117417"><a name="p9399117417"></a><a name="p9399117417"></a>example_key1</p>
    <p id="p1140011110414"><a name="p1140011110414"></a><a name="p1140011110414"></a>example_value1</p>
    </td>
    </tr>
    <tr id="row17688109192713"><td class="cellrowborder" valign="top" width="18.18181818181818%" headers="mcps1.2.4.1.1 "><p id="p968899202716"><a name="p968899202716"></a><a name="p968899202716"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.4.1.2 "><p id="p1468889182713"><a name="p1468889182713"></a><a name="p1468889182713"></a>(Optional) Description of the PTR record</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p11688159152710"><a name="p11688159152710"></a><a name="p11688159152710"></a>The PTR record is for reverse resolution.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click **OK**.

