# Managing Public Zones<a name="en-us_topic_0035467702"></a>

> ![](/images/icon-note.gif) **NOTE:** 

> The ap-sg region does not support public zones.

## Viewing Details About a Public Zone<a name="section6318733510236"></a>

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  On the **Dashboard** page, click **Public Zones** under **My Resources** to query the public zone list.
4.  View the public zone details.

## Creating a Public Zone<a name="section52845971102319"></a>

Create a public zone if a new domain name is to be managed using the DNS service.

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, Choose **Public Zones**.

    The **Public Zones** page is displayed.

4.  Click **Create Public Zone**.

    **Figure 1** Create Public Zone<a name="en-us_topic_0035467699_fig554123819318"></a>
    ![](figures/create-public-zone.png "Create Public Zone")

5.  Configure the parameters according to [Table 1](#en-us_topic_0035467699_en-us_topic_0035467699_table2052132816642).**Table 1** Parameters required for creating a public zone

    <a name="en-us_topic_0035467699_en-us_topic_0035467699_table2052132816642"></a><table><thead align="left"><tr id="en-us_topic_0035467699_en-us_topic_0035467699_row5957484916642"><th class="cellrowborder" valign="top" width="18.11%" id="mcps1.2.4.1.1"><p id="en-us_topic_0035467699_en-us_topic_0035467699_p1063011916642"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p1063011916642"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p1063011916642"></a><strong id="en-us_topic_0035467699_b8423527069657"><a name="en-us_topic_0035467699_b8423527069657"></a><a name="en-us_topic_0035467699_b8423527069657"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.629999999999995%" id="mcps1.2.4.1.2"><p id="en-us_topic_0035467699_en-us_topic_0035467699_p5573330716642"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p5573330716642"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p5573330716642"></a><strong id="en-us_topic_0035467699_b842352706971"><a name="en-us_topic_0035467699_b842352706971"></a><a name="en-us_topic_0035467699_b842352706971"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.259999999999998%" id="mcps1.2.4.1.3"><p id="en-us_topic_0035467699_en-us_topic_0035467699_p1810404816642"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p1810404816642"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p1810404816642"></a><strong id="en-us_topic_0035467699_b842352706978"><a name="en-us_topic_0035467699_b842352706978"></a><a name="en-us_topic_0035467699_b842352706978"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0035467699_en-us_topic_0035467699_row2871871016642"><td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_en-us_topic_0035467699_p4451420716642"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p4451420716642"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p4451420716642"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467699_en-us_topic_0035467699_p41211101203154"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p41211101203154"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p41211101203154"></a>Domain name registered with the domain name registrar</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_en-us_topic_0035467699_p6704856616642"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p6704856616642"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p6704856616642"></a>example.com</p>
    </td>
    </tr>
    <tr id="en-us_topic_0035467699_en-us_topic_0035467699_row3925088716642"><td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_en-us_topic_0035467699_p2520529816642"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p2520529816642"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p2520529816642"></a>Email</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467699_p58502563174819"><a name="en-us_topic_0035467699_p58502563174819"></a><a name="en-us_topic_0035467699_p58502563174819"></a>(Optional) Email address of the administrator managing the public zone. It is recommended that you set the email address to <strong id="en-us_topic_0035467699_b842352706182128"><a name="en-us_topic_0035467699_b842352706182128"></a><a name="en-us_topic_0035467699_b842352706182128"></a>HOSTMASTER@<em id="en-us_topic_0035467699_i842352697182143"><a name="en-us_topic_0035467699_i842352697182143"></a><a name="en-us_topic_0035467699_i842352697182143"></a>Domain name</em></strong>.</p>
    <p id="en-us_topic_0035467699_p3894942320387"><a name="en-us_topic_0035467699_p3894942320387"></a><a name="en-us_topic_0035467699_p3894942320387"></a>For more details about the email address, see <a href="why-is-the-email-address-format-changed-in-the-soa-record.html">Why Is the Email Address Format Changed in the SOA Record?</a></p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_en-us_topic_0035467699_p1572349716642"><a name="en-us_topic_0035467699_en-us_topic_0035467699_p1572349716642"></a><a name="en-us_topic_0035467699_en-us_topic_0035467699_p1572349716642"></a>HOSTMASTER@example.com</p>
    </td>
    </tr>
    <tr id="en-us_topic_0035467699_row105410594141"><td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_p95595914146"><a name="en-us_topic_0035467699_p95595914146"></a><a name="en-us_topic_0035467699_p95595914146"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467699_p40394784174819"><a name="en-us_topic_0035467699_p40394784174819"></a><a name="en-us_topic_0035467699_p40394784174819"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a zone.</p>
    <p id="en-us_topic_0035467699_p1690771316155"><a name="en-us_topic_0035467699_p1690771316155"></a><a name="en-us_topic_0035467699_p1690771316155"></a>For details about tag key and value requirements, see <a href="#en-us_topic_0035467702__en-us_topic_0035467699_table18290035121711">Table 2</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_p15551259121412"><a name="en-us_topic_0035467699_p15551259121412"></a><a name="en-us_topic_0035467699_p15551259121412"></a>example_key1</p>
    <p id="en-us_topic_0035467699_p15031954131915"><a name="en-us_topic_0035467699_p15031954131915"></a><a name="en-us_topic_0035467699_p15031954131915"></a>example_value1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0035467699_row197267115553"><td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_p196195011562"><a name="en-us_topic_0035467699_p196195011562"></a><a name="en-us_topic_0035467699_p196195011562"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467699_p23257049174819"><a name="en-us_topic_0035467699_p23257049174819"></a><a name="en-us_topic_0035467699_p23257049174819"></a>(Optional) Description of the domain name, which cannot exceed 255 characters</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_p5775016011562"><a name="en-us_topic_0035467699_p5775016011562"></a><a name="en-us_topic_0035467699_p5775016011562"></a>This is a public zone.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table 2** Tag key and value requirements

    <a name="en-us_topic_0035467699_table18290035121711"></a><table><thead align="left"><tr id="en-us_topic_0035467699_row72901535141713"><th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.4.1.1"><p id="en-us_topic_0035467699_p132908358173"><a name="en-us_topic_0035467699_p132908358173"></a><a name="en-us_topic_0035467699_p132908358173"></a><strong id="en-us_topic_0035467699_b8423527069525"><a name="en-us_topic_0035467699_b8423527069525"></a><a name="en-us_topic_0035467699_b8423527069525"></a>Parameter</strong></p>
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

6.  Click **OK**.

    You can query information about the zone you created on the **Public Zones** page.

    > ![](/images/icon-note.gif) **NOTE:** 

    > Click the zone name to query detailed zone information. The system has created record sets of the SOA type and NS type in the zone.

    > -   The SOA record set determines the DNS server that is the authoritative information source for a particular domain name.
    > -   The NS record set defines authoritative DNS servers for a zone.

## Modifying a Public Zone<a name="section26081112215548"></a>

If the information of your public zone has changed, you can modify its email address or description.

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, Choose **Public Zones**.

    The **Public Zones** page is displayed.

4.  Locate the zone to be modified and click **Modify** under **Operation**.

    The **Modify Public Zone** box is displayed.

5.  Change the email address or description of the zone.
6.  Click **OK**.

## Deleting a Public Zone<a name="section34296412102339"></a>

A public zone can be deleted if you do not need to manage it using the DNS service. After the deletion, domain names included in this zone cannot be resolved.

> ![](/images/icon-notice.gif) **NOTICE:** 

> Before deleting a public zone, ensure that all record sets in this zone have been backed up.

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, Choose **Public Zones**.

    The **Public Zones** page is displayed.

4.  Locate the zone to be deleted and click **Delete** under **Operation**.
5.  Click **OK** to confirm the deletion.

