# Creating a Wildcard DNS Record Set<a name="en-us_topic_0049960991"></a>

## **Scenarios**<a name="section5192411916229"></a>

A wildcard DNS record set is used to match requests for all subdomains in a zone. You specify the host name in a domain name to an asterisk \(\*\) when creating a record set so that the DNS service can map subdomains to the specified IP address.

This section describes how you can create a wildcard DNS record set.

## Restrictions and Limitations<a name="section65793739162214"></a>

Wildcard DNS resolution does not support NS record sets.

## **Procedure**<a name="section44418024162230"></a>

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, click **Public Zones** or **Private Zones**.

    The zone list is displayed.

4.  \(Optional\) If you have selected **Private Zones**, click on the upper left to select the region and project.
5.  Click the name of the zone to which the wildcard DNS record set is to be added.
6.  Click **Add Record Set** to create a wildcard DNS record set.
7.  Configure the parameters according to [Table 1](#en-us_topic_0035467699_en-us_topic_0035467699_table6239446395216).**Table 1** Parameters required for adding a wildcard DNS record set.

    <a name="en-us_topic_0035467699_en-us_topic_0035467699_table6239446395216"></a><table><thead align="left"><tr id="en-us_topic_0035467699_en-us_topic_0035467699_row1754572995216"><th class="cellrowborder" valign="top" width="20.549999999999997%" id="mcps1.2.4.1.1"><p id="en-us_topic_0035467699_en-us_topic_0035467699_p4015297795216"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p4015297795216"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p4015297795216"></a><strong id="b84235270695255"><a name="b84235270695255"></a><a name="b84235270695255"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.12%" id="mcps1.2.4.1.2"><p id="en-us_topic_0035467699_en-us_topic_0035467699_p270124995329"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p270124995329"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p270124995329"></a><strong id="en-us_topic_0035268497_b8423527061433"><a name="en-us_topic_0035268497_b8423527061433"></a><a name="en-us_topic_0035268497_b8423527061433"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="en-us_topic_0035467699_en-us_topic_0035467699_p4139255095216"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p4139255095216"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p4139255095216"></a><strong id="b84235270617114"><a name="b84235270617114"></a><a name="b84235270617114"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0035467699_en-us_topic_0035467699_row3698863095216"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_en-us_topic_0035467699_p4328906095216"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p4328906095216"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p4328906095216"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p13372480173245"><a name="p13372480173245"></a><a name="p13372480173245"></a>Public (or private) domain name</p>
    <p id="en-us_topic_0035467699_p3294717143513"><a name="en-us_topic_0035467699_p3294717143513"></a><a name="en-us_topic_0035467699_p3294717143513"></a>To configure a wildcard DNS record set, enter an asterisk (*) as the leftmost label of the domain name, for example, <strong id="b842352706161950"><a name="b842352706161950"></a><a name="b842352706161950"></a>*.example.com</strong>.</p>
    <div class="note" id="note5710651175326"><a name="note5710651175326"></a><a name="note5710651175326"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p51395859175326"><a name="p51395859175326"></a><a name="p51395859175326"></a>When creating a wildcard record set of the TXT type, you can enter an asterisk (*) in the domain name, but only the leftmost asterisk is treated as a wildcard character. Asterisks in other places of the domain name are used as common text characters.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_en-us_topic_0035467699_p1481668395216"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p1481668395216"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p1481668395216"></a>*.abc</p>
    </td>
    </tr>
    <tr id="en-us_topic_0035467699_en-us_topic_0035467699_row933215795216"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_en-us_topic_0035467699_p1770728795216"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p1770728795216"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p1770728795216"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467699_en-us_topic_0035467699_p2500417095216"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p2500417095216"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p2500417095216"></a>Record set type</p>
    <p id="p24720447174230"><a name="p24720447174230"></a><a name="p24720447174230"></a>Wildcard DNS resolution does not support NS record sets.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_en-us_topic_0035467699_p1207186995216"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p1207186995216"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p1207186995216"></a></p>
    <p id="p16334345161916"><a name="p16334345161916"></a><a name="p16334345161916"></a>A – Map domains to IPv4 addresses</p>
    </td>
    </tr>
    <tr id="en-us_topic_0035467699_en-us_topic_0035467699_row2395117795431"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_en-us_topic_0035467699_p1423400295431"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p1423400295431"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p1423400295431"></a>TTL (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467699_en-us_topic_0035467699_p300850919591"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p300850919591"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p300850919591"></a>Caching period of the record set (in seconds)</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_en-us_topic_0035467699_p4085731095431"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p4085731095431"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p4085731095431"></a>The default value is 300s, that is, <strong id="b842352706183837"><a name="b842352706183837"></a><a name="b842352706183837"></a>5 min</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0035467699_en-us_topic_0035467699_row3388081495431"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_en-us_topic_0035467699_p3649187395431"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p3649187395431"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p3649187395431"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467699_p5257204895334"><a name="en-us_topic_0035467699_p5257204895334"></a><a name="en-us_topic_0035467699_p5257204895334"></a>Record set value</p>
    <p id="p5557923693143"><a name="p5557923693143"></a><a name="p5557923693143"></a>For more information, see section <a href="managing-record-sets.html">Managing Record Sets</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p6519983393616"><a name="p6519983393616"></a><a name="p6519983393616"></a>If it is an A record set, the value is the IPv4 addresses mapped to the domain name. For example:</p>
    <p id="en-us_topic_0035467699_p65885051152545"><a name="en-us_topic_0035467699_p65885051152545"></a><a name="en-us_topic_0035467699_p65885051152545"></a>192.168.12.2</p>
    <p id="en-us_topic_0035467699_p56094551152545"><a name="en-us_topic_0035467699_p56094551152545"></a><a name="en-us_topic_0035467699_p56094551152545"></a>192.168.12.3</p>
    </td>
    </tr>
    <tr id="row934550113116"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p1481158112914"><a name="p1481158112914"></a><a name="p1481158112914"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p18487135819293"><a name="p18487135819293"></a><a name="p18487135819293"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a record set.</p>
    <p id="p1849145832914"><a name="p1849145832914"></a><a name="p1849145832914"></a>For details about tag key and value requirements, see <a href="#en-us_topic_0049960991__table865604093219">Table 2</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p205017586294"><a name="p205017586294"></a><a name="p205017586294"></a>example_key1</p>
    <p id="p11507158172920"><a name="p11507158172920"></a><a name="p11507158172920"></a>example_value1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0035467699_row21944507132325"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_p64541931132333"><a name="en-us_topic_0035467699_p64541931132333"></a><a name="en-us_topic_0035467699_p64541931132333"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467699_p60513903132333"><a name="en-us_topic_0035467699_p60513903132333"></a><a name="en-us_topic_0035467699_p60513903132333"></a>(Optional) Description of the domain name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_p2679104132333"><a name="en-us_topic_0035467699_p2679104132333"></a><a name="en-us_topic_0035467699_p2679104132333"></a>This is a wildcard DNS record set.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table 2** Tag key and value requirements

    <a name="table865604093219"></a><table><thead align="left"><tr id="en-us_topic_0035467699_row72901535141713"><th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.4.1.1"><p id="en-us_topic_0035467699_p132908358173"><a name="en-us_topic_0035467699_p132908358173"></a><a name="en-us_topic_0035467699_p132908358173"></a><strong id="en-us_topic_0035467699_b8423527069525"><a name="en-us_topic_0035467699_b8423527069525"></a><a name="en-us_topic_0035467699_b8423527069525"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.505050505050505%" id="mcps1.2.4.1.2"><p id="en-us_topic_0035467699_p1629093517175"><a name="en-us_topic_0035467699_p1629093517175"></a><a name="en-us_topic_0035467699_p1629093517175"></a><strong id="en-us_topic_0035467699_b842352706171418"><a name="en-us_topic_0035467699_b842352706171418"></a><a name="en-us_topic_0035467699_b842352706171418"></a>Requirement</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.313131313131315%" id="mcps1.2.4.1.3"><p id="en-us_topic_0035467699_p32901635141714"><a name="en-us_topic_0035467699_p32901635141714"></a><a name="en-us_topic_0035467699_p32901635141714"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0035467699_row52906354176"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_p122901235111715"><a name="en-us_topic_0035467699_p122901235111715"></a><a name="en-us_topic_0035467699_p122901235111715"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.505050505050505%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0035467699_ul46253231183"></a><a name="en-us_topic_0035467699_ul46253231183"></a><ul id="en-us_topic_0035467699_ul46253231183"><li id="en-us_topic_0035467699_li176251123141812"><a name="en-us_topic_0035467699_li176251123141812"></a><a name="en-us_topic_0035467699_li176251123141812"></a>Cannot be left blank.</li><li id="en-us_topic_0035467699_li86261923201810"><a name="en-us_topic_0035467699_li86261923201810"></a><a name="en-us_topic_0035467699_li86261923201810"></a>Must be unique for each resource.</li><li id="en-us_topic_0035467699_li162620231180"><a name="en-us_topic_0035467699_li162620231180"></a><a name="en-us_topic_0035467699_li162620231180"></a>Consists of at most 36 characters.</li><li id="en-us_topic_0035467699_li5389246102911"><a name="en-us_topic_0035467699_li5389246102911"></a><a name="en-us_topic_0035467699_li5389246102911"></a>Contains only letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="31.313131313131315%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_p12290163511720"><a name="en-us_topic_0035467699_p12290163511720"></a><a name="en-us_topic_0035467699_p12290163511720"></a>example_key1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0035467699_row132900355172"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_p152901635181712"><a name="en-us_topic_0035467699_p152901635181712"></a><a name="en-us_topic_0035467699_p152901635181712"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.505050505050505%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0035467699_ul19648123161815"></a><a name="en-us_topic_0035467699_ul19648123161815"></a><ul id="en-us_topic_0035467699_ul19648123161815"><li id="en-us_topic_0035467699_li15648193110182"><a name="en-us_topic_0035467699_li15648193110182"></a><a name="en-us_topic_0035467699_li15648193110182"></a>Cannot be left blank.</li><li id="en-us_topic_0035467699_li3648143181813"><a name="en-us_topic_0035467699_li3648143181813"></a><a name="en-us_topic_0035467699_li3648143181813"></a>Consists of at most 43 characters.</li><li id="en-us_topic_0035467699_li64561823123015"><a name="en-us_topic_0035467699_li64561823123015"></a><a name="en-us_topic_0035467699_li64561823123015"></a>Contains only letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="31.313131313131315%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_p62904352179"><a name="en-us_topic_0035467699_p62904352179"></a><a name="en-us_topic_0035467699_p62904352179"></a>example_value1</p>
    </td>
    </tr>
    </tbody>
    </table>

8.  Click **OK**.

