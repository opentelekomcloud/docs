# Configuring a Public Zone<a name="en-us_topic_0035467699"></a>

## **Scenarios**<a name="section788725015149"></a>

To use the DNS service to manage domain names, you need to configure the service on the management console.

> ![](/images/icon-note.gif) **NOTE:** 

> The ap-sg region does not support public zones.

## **Prerequisites**<a name="section6577675115583"></a>

You have registered a domain name with the domain name registrar.

For details about how to register a domain name, contact the domain name registrar.

## Configuration Process<a name="section7987195861919"></a>

**Figure 1** Process to configure a public zone<a name="fe4910c96160749349abf31cb88cfe52b"></a>
![](figures/process-to-configure-a-public-zone.png "Process to configure a public zone")

You need to perform operations in [Figure 1](#fe4910c96160749349abf31cb88cfe52b) in different places:

-   "Register a domain name" and "Update the NS addresses" are conducted by your domain name registrar.
-   "Create a public zone" and "Create record sets" are performed on the DNS console.

## **Procedure**<a name="section6593003511349"></a>

**Creating a public zone**

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, Choose **Public Zones**.

    The **Public Zones** page is displayed.

4.  Click **Create Public Zone**.

    **Figure 2** Create Public Zone<a name="fig554123819318"></a>
    ![](figures/add-record-set-for-public-zone.png "Create Public Zone")

5.  Configure the parameters according to [Table 1](#en-us_topic_0035467699_table2052132816642).**Table 1** Parameters required for creating a public zone

    <a name="en-us_topic_0035467699_table2052132816642"></a><table><thead align="left"><tr id="en-us_topic_0035467699_row5957484916642"><th class="cellrowborder" valign="top" width="18.11%" id="mcps1.2.4.1.1"><p id="en-us_topic_0035467699_p1063011916642"><a name="en-us_topic_0035467699_p1063011916642"></a><a name="en-us_topic_0035467699_p1063011916642"></a><strong id="b8423527069657"><a name="b8423527069657"></a><a name="b8423527069657"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.629999999999995%" id="mcps1.2.4.1.2"><p id="en-us_topic_0035467699_p5573330716642"><a name="en-us_topic_0035467699_p5573330716642"></a><a name="en-us_topic_0035467699_p5573330716642"></a><strong id="b842352706971"><a name="b842352706971"></a><a name="b842352706971"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.259999999999998%" id="mcps1.2.4.1.3"><p id="en-us_topic_0035467699_p1810404816642"><a name="en-us_topic_0035467699_p1810404816642"></a><a name="en-us_topic_0035467699_p1810404816642"></a><strong id="b842352706978"><a name="b842352706978"></a><a name="b842352706978"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0035467699_row2871871016642"><td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_p4451420716642"><a name="en-us_topic_0035467699_p4451420716642"></a><a name="en-us_topic_0035467699_p4451420716642"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467699_p41211101203154"><a name="en-us_topic_0035467699_p41211101203154"></a><a name="en-us_topic_0035467699_p41211101203154"></a>Domain name registered with the domain name registrar</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_p6704856616642"><a name="en-us_topic_0035467699_p6704856616642"></a><a name="en-us_topic_0035467699_p6704856616642"></a>example.com</p>
    </td>
    </tr>
    <tr id="en-us_topic_0035467699_row3925088716642"><td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_p2520529816642"><a name="en-us_topic_0035467699_p2520529816642"></a><a name="en-us_topic_0035467699_p2520529816642"></a>Email</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.2 "><p id="p58502563174819"><a name="p58502563174819"></a><a name="p58502563174819"></a>(Optional) Email address of the administrator managing the public zone. It is recommended that you set the email address to <strong id="b842352706182128"><a name="b842352706182128"></a><a name="b842352706182128"></a>HOSTMASTER@<em id="i842352697182143"><a name="i842352697182143"></a><a name="i842352697182143"></a>Domain name</em></strong>.</p>
    <p id="p3894942320387"><a name="p3894942320387"></a><a name="p3894942320387"></a>For more details about the email address, see <a href="why-is-the-email-address-format-changed-in-the-soa-record.html">Why Is the Email Address Format Changed in the SOA Record?</a></p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_p1572349716642"><a name="en-us_topic_0035467699_p1572349716642"></a><a name="en-us_topic_0035467699_p1572349716642"></a>HOSTMASTER@example.com</p>
    </td>
    </tr>
    <tr id="row105410594141"><td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.1 "><p id="p95595914146"><a name="p95595914146"></a><a name="p95595914146"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.2 "><p id="p40394784174819"><a name="p40394784174819"></a><a name="p40394784174819"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a zone.</p>
    <p id="p1690771316155"><a name="p1690771316155"></a><a name="p1690771316155"></a>For details about tag key and value requirements, see <a href="#en-us_topic_0035467699__table18290035121711">Table 2</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="p15551259121412"><a name="p15551259121412"></a><a name="p15551259121412"></a>example_key1</p>
    <p id="p15031954131915"><a name="p15031954131915"></a><a name="p15031954131915"></a>example_value1</p>
    </td>
    </tr>
    <tr id="row197267115553"><td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.1 "><p id="p196195011562"><a name="p196195011562"></a><a name="p196195011562"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.2 "><p id="p23257049174819"><a name="p23257049174819"></a><a name="p23257049174819"></a>(Optional) Description of the domain name, which cannot exceed 255 characters</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="p5775016011562"><a name="p5775016011562"></a><a name="p5775016011562"></a>This is a public zone.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table 2** Tag key and value requirements

    <a name="table18290035121711"></a><table><thead align="left"><tr id="row72901535141713"><th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.4.1.1"><p id="p132908358173"><a name="p132908358173"></a><a name="p132908358173"></a><strong id="b8423527069525"><a name="b8423527069525"></a><a name="b8423527069525"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.505050505050505%" id="mcps1.2.4.1.2"><p id="p1629093517175"><a name="p1629093517175"></a><a name="p1629093517175"></a><strong id="b842352706171418"><a name="b842352706171418"></a><a name="b842352706171418"></a>Requirement</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.313131313131315%" id="mcps1.2.4.1.3"><p id="p32901635141714"><a name="p32901635141714"></a><a name="p32901635141714"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52906354176"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.1 "><p id="p122901235111715"><a name="p122901235111715"></a><a name="p122901235111715"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.505050505050505%" headers="mcps1.2.4.1.2 "><a name="ul46253231183"></a><a name="ul46253231183"></a><ul id="ul46253231183"><li id="li176251123141812"><a name="li176251123141812"></a><a name="li176251123141812"></a>Cannot be left blank.</li><li id="li86261923201810"><a name="li86261923201810"></a><a name="li86261923201810"></a>Must be unique for each resource.</li><li id="li162620231180"><a name="li162620231180"></a><a name="li162620231180"></a>Consists of at most 36 characters.</li><li id="li5389246102911"><a name="li5389246102911"></a><a name="li5389246102911"></a>Contains only letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="31.313131313131315%" headers="mcps1.2.4.1.3 "><p id="p12290163511720"><a name="p12290163511720"></a><a name="p12290163511720"></a>example_key1</p>
    </td>
    </tr>
    <tr id="row132900355172"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.1 "><p id="p152901635181712"><a name="p152901635181712"></a><a name="p152901635181712"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.505050505050505%" headers="mcps1.2.4.1.2 "><a name="ul19648123161815"></a><a name="ul19648123161815"></a><ul id="ul19648123161815"><li id="li15648193110182"><a name="li15648193110182"></a><a name="li15648193110182"></a>Cannot be left blank.</li><li id="li3648143181813"><a name="li3648143181813"></a><a name="li3648143181813"></a>Consists of at most 43 characters.</li><li id="li64561823123015"><a name="li64561823123015"></a><a name="li64561823123015"></a>Contains only letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="31.313131313131315%" headers="mcps1.2.4.1.3 "><p id="p62904352179"><a name="p62904352179"></a><a name="p62904352179"></a>example_value1</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click **OK**.

    You can query information about the zone you created on the **Public Zones** page.

    > ![](/images/icon-note.gif) **NOTE:** 

    > Click the zone name to query detailed zone information. The system has created record sets of the SOA type and NS type in the zone.

    > -   The SOA record set determines the DNS server that is the authoritative information source for a particular domain name.
    > -   The NS record set defines authoritative DNS servers for a zone.

**Adding a record set of the A type**

1.  In the zone list on the **Public Zones** page, click the name of the public zone you created.

    The record set page is displayed.

2.  Click **Add Record Set**.

    The **Add Record Set** box is displayed.

    **Figure 3** Add Record Set<a name="fig86510231718"></a>
    ![](figures/add-record-set.png "Add Record Set")

3.  Configure the parameters according to [Table 3](#en-us_topic_0035467699_table6239446395216).**Table 3** Parameters required for adding a record set of the A type

    <a name="en-us_topic_0035467699_table6239446395216"></a><table><thead align="left"><tr id="en-us_topic_0035467699_row1754572995216"><th class="cellrowborder" valign="top" width="20.549999999999997%" id="mcps1.2.4.1.1"><p id="en-us_topic_0035467699_p4015297795216"><a name="en-us_topic_0035467699_p4015297795216"></a><a name="en-us_topic_0035467699_p4015297795216"></a><strong id="b8423527069657_1"><a name="b8423527069657_1"></a><a name="b8423527069657_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.12%" id="mcps1.2.4.1.2"><p id="en-us_topic_0035467699_p270124995329"><a name="en-us_topic_0035467699_p270124995329"></a><a name="en-us_topic_0035467699_p270124995329"></a><strong id="b842352706971_1"><a name="b842352706971_1"></a><a name="b842352706971_1"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="en-us_topic_0035467699_p4139255095216"><a name="en-us_topic_0035467699_p4139255095216"></a><a name="en-us_topic_0035467699_p4139255095216"></a><strong id="b842352706978_1"><a name="b842352706978_1"></a><a name="b842352706978_1"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0035467699_row3698863095216"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p5689226291944"><a name="p5689226291944"></a><a name="p5689226291944"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p3294717143513"><a name="p3294717143513"></a><a name="p3294717143513"></a>Domain name (You do not need to manually add the suffix.)</p>
    <p id="p29652461143513"><a name="p29652461143513"></a><a name="p29652461143513"></a>The default value is the zone name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_p1481668395216"><a name="en-us_topic_0035467699_p1481668395216"></a><a name="en-us_topic_0035467699_p1481668395216"></a>www</p>
    </td>
    </tr>
    <tr id="en-us_topic_0035467699_row933215795216"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_p1770728795216"><a name="en-us_topic_0035467699_p1770728795216"></a><a name="en-us_topic_0035467699_p1770728795216"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467699_p2500417095216"><a name="en-us_topic_0035467699_p2500417095216"></a><a name="en-us_topic_0035467699_p2500417095216"></a>Type of the record set</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_p1207186995216"><a name="en-us_topic_0035467699_p1207186995216"></a><a name="en-us_topic_0035467699_p1207186995216"></a></p>
    <p id="p177315541502"><a name="p177315541502"></a><a name="p177315541502"></a>A – Map domains to IPv4 addresses</p>
    </td>
    </tr>
    <tr id="en-us_topic_0035467699_row2395117795431"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_p1423400295431"><a name="en-us_topic_0035467699_p1423400295431"></a><a name="en-us_topic_0035467699_p1423400295431"></a>TTL (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467699_p300850919591"><a name="en-us_topic_0035467699_p300850919591"></a><a name="en-us_topic_0035467699_p300850919591"></a>Caching period of the record set (in seconds)</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_p4085731095431"><a name="en-us_topic_0035467699_p4085731095431"></a><a name="en-us_topic_0035467699_p4085731095431"></a>The default value is 300s, that is, <strong id="b8423527061593"><a name="b8423527061593"></a><a name="b8423527061593"></a>5 min</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0035467699_row3388081495431"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_p3649187395431"><a name="en-us_topic_0035467699_p3649187395431"></a><a name="en-us_topic_0035467699_p3649187395431"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p5257204895334"><a name="p5257204895334"></a><a name="p5257204895334"></a>IPv4 addresses mapped to the domain name</p>
    <p id="en-us_topic_0035467699_p3889841410035"><a name="en-us_topic_0035467699_p3889841410035"></a><a name="en-us_topic_0035467699_p3889841410035"></a>Every two IPv4 addresses are separated using a line break.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p65885051152545"><a name="p65885051152545"></a><a name="p65885051152545"></a>192.168.12.2</p>
    <p id="p56094551152545"><a name="p56094551152545"></a><a name="p56094551152545"></a>192.168.12.3</p>
    </td>
    </tr>
    <tr id="row947495585616"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p1947655513565"><a name="p1947655513565"></a><a name="p1947655513565"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p77793111515"><a name="p77793111515"></a><a name="p77793111515"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a record set.</p>
    <p id="p8401121711229"><a name="p8401121711229"></a><a name="p8401121711229"></a>For details about tag key and value requirements, see <a href="#en-us_topic_0035467699__table18290035121711">Table 2</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p94761455155619"><a name="p94761455155619"></a><a name="p94761455155619"></a>example_key1</p>
    <p id="p165896220231"><a name="p165896220231"></a><a name="p165896220231"></a>example_value1</p>
    </td>
    </tr>
    <tr id="row21944507132325"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p64541931132333"><a name="p64541931132333"></a><a name="p64541931132333"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p60513903132333"><a name="p60513903132333"></a><a name="p60513903132333"></a>(Optional) Description of the domain name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p2679104132333"><a name="p2679104132333"></a><a name="p2679104132333"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click **OK**.

**Updating the NS addresses**

To resolve the domain name on the Internet, you need to change your domain name registrar's NS record addresses. Specifically, you need to change the domain name resolution addresses in the NS record of the zone to the authoritative DNS server domain names provided by the DNS service.

After you create a zone, the system automatically creates an NS record set, which specifies the DNS servers used to resolve public network domain names.

> ![](/images/icon-note.gif) **NOTE:** 

> Generally, the update takes effect within 48 hours, but the time may vary depending on domain name registrars.

You can perform the following operations to query the NS addresses provided for you:

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, Choose **Public Zones**.

    The **Public Zones** page is displayed.

4.  In the zone list, click the name of the public zone you created.

    Query the NS record set. The information under **Value** is the NS addresses provided by the DNS service.

    **Figure 4** NS record set<a name="fig527759133123"></a>
    ![](figures/ns-record-set.png "NS record set")


