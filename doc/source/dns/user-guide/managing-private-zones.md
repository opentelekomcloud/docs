# Managing Private Zones<a name="en-us_topic_0057773658"></a>

## Viewing Details About a Private Zone<a name="section6093022701347"></a>

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  On the **Dashboard** page, click **Private Zones** under **My Resources**.
4.  Click on the upper left and select the desired region and project.
5.  View the private zone details.

## Creating a Private Zone<a name="section246499601514"></a>

Create a private zone if a new domain name is to be managed using the DNS service.

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, Choose **Private Zones**.

    The **Private Zones** page is displayed.

4.  Click on the upper left and select the desired region and project.
5.  Click **Create Private Zone**.

    **Figure 1** Create Private Zone<a name="en-us_topic_0057777026_fig176111710101018"></a>
    ![](figures/create-private-zone.png "Create Private Zone")

6.  Configure the parameters according to [Table 1](#en-us_topic_0057777026_en-us_topic_0035467699_table2052132816642).**Table 1** Parameters required for creating a private zone

    <a name="en-us_topic_0057777026_en-us_topic_0035467699_table2052132816642"></a><table><thead align="left"><tr id="en-us_topic_0057777026_en-us_topic_0035467699_row5957484916642"><th class="cellrowborder" valign="top" width="18.11%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057777026_en-us_topic_0035467699_p1063011916642"><a name="en-us_topic_0057777026_en-us_topic_0035467699_p1063011916642"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_p1063011916642"></a><strong id="en-us_topic_0057777026_b84235270695255"><a name="en-us_topic_0057777026_b84235270695255"></a><a name="en-us_topic_0057777026_b84235270695255"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.629999999999995%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057777026_en-us_topic_0035467699_p5573330716642"><a name="en-us_topic_0057777026_en-us_topic_0035467699_p5573330716642"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_p5573330716642"></a><strong id="en-us_topic_0057777026_en-us_topic_0035268497_b8423527061433"><a name="en-us_topic_0057777026_en-us_topic_0035268497_b8423527061433"></a><a name="en-us_topic_0057777026_en-us_topic_0035268497_b8423527061433"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.259999999999998%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057777026_en-us_topic_0035467699_p1810404816642"><a name="en-us_topic_0057777026_en-us_topic_0035467699_p1810404816642"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_p1810404816642"></a><strong id="en-us_topic_0057777026_b84235270617114"><a name="en-us_topic_0057777026_b84235270617114"></a><a name="en-us_topic_0057777026_b84235270617114"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0057777026_en-us_topic_0035467699_row2871871016642"><td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057777026_en-us_topic_0035467699_p4451420716642"><a name="en-us_topic_0057777026_en-us_topic_0035467699_p4451420716642"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_p4451420716642"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057777026_en-us_topic_0035467699_p41211101203154"><a name="en-us_topic_0057777026_en-us_topic_0035467699_p41211101203154"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_p41211101203154"></a>Private network domain name</p>
    <p id="en-us_topic_0057777026_p58045962204247"><a name="en-us_topic_0057777026_p58045962204247"></a><a name="en-us_topic_0057777026_p58045962204247"></a>You can customize any correctly formatted top-level domain names.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057777026_en-us_topic_0035467699_p6704856616642"><a name="en-us_topic_0057777026_en-us_topic_0035467699_p6704856616642"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_p6704856616642"></a>example.com</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057777026_row16069279235858"><td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057777026_p10405784235858"><a name="en-us_topic_0057777026_p10405784235858"></a><a name="en-us_topic_0057777026_p10405784235858"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057777026_p37562215235858"><a name="en-us_topic_0057777026_p37562215235858"></a><a name="en-us_topic_0057777026_p37562215235858"></a>VPC to be associated with the private zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057777026_p22640607235858"><a name="en-us_topic_0057777026_p22640607235858"></a><a name="en-us_topic_0057777026_p22640607235858"></a>-</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057777026_en-us_topic_0035467699_row3925088716642"><td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057777026_p13135064235829"><a name="en-us_topic_0057777026_p13135064235829"></a><a name="en-us_topic_0057777026_p13135064235829"></a>Email</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057777026_p32695006191040"><a name="en-us_topic_0057777026_p32695006191040"></a><a name="en-us_topic_0057777026_p32695006191040"></a>(Optional) Email address of the administrator managing the private zone</p>
    <p id="en-us_topic_0057777026_p34628599174928"><a name="en-us_topic_0057777026_p34628599174928"></a><a name="en-us_topic_0057777026_p34628599174928"></a>It is recommended that you set the email address to <strong id="en-us_topic_0057777026_b842352706182128"><a name="en-us_topic_0057777026_b842352706182128"></a><a name="en-us_topic_0057777026_b842352706182128"></a>HOSTMASTER@<em id="en-us_topic_0057777026_i842352697182143"><a name="en-us_topic_0057777026_i842352697182143"></a><a name="en-us_topic_0057777026_i842352697182143"></a>Domain name</em></strong>.</p>
    <p id="en-us_topic_0057777026_p3894942320387"><a name="en-us_topic_0057777026_p3894942320387"></a><a name="en-us_topic_0057777026_p3894942320387"></a>For more details about the email address, see <a href="why-is-the-email-address-format-changed-in-the-soa-record.html">Why Is the Email Address Format Changed in the SOA Record?</a></p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057777026_en-us_topic_0035467699_p1572349716642"><a name="en-us_topic_0057777026_en-us_topic_0035467699_p1572349716642"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_p1572349716642"></a>HOSTMASTER@example.com</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057777026_row648142632420"><td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057777026_p18481122652416"><a name="en-us_topic_0057777026_p18481122652416"></a><a name="en-us_topic_0057777026_p18481122652416"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057777026_p43647836174928"><a name="en-us_topic_0057777026_p43647836174928"></a><a name="en-us_topic_0057777026_p43647836174928"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a zone.</p>
    <p id="en-us_topic_0057777026_p1690771316155"><a name="en-us_topic_0057777026_p1690771316155"></a><a name="en-us_topic_0057777026_p1690771316155"></a>For details about tag key and value requirements, see <a href="#en-us_topic_0057773658__en-us_topic_0057777026_table1393932617253">Table 2</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057777026_p15551259121412"><a name="en-us_topic_0057777026_p15551259121412"></a><a name="en-us_topic_0057777026_p15551259121412"></a>example_key1</p>
    <p id="en-us_topic_0057777026_p15031954131915"><a name="en-us_topic_0057777026_p15031954131915"></a><a name="en-us_topic_0057777026_p15031954131915"></a>example_value1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057777026_row197267115553"><td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057777026_p196195011562"><a name="en-us_topic_0057777026_p196195011562"></a><a name="en-us_topic_0057777026_p196195011562"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057777026_p17251976174928"><a name="en-us_topic_0057777026_p17251976174928"></a><a name="en-us_topic_0057777026_p17251976174928"></a>(Optional) Description of the domain name, which cannot exceed 255 characters</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057777026_p5775016011562"><a name="en-us_topic_0057777026_p5775016011562"></a><a name="en-us_topic_0057777026_p5775016011562"></a>This is a private zone.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table 2** Tag key and value requirements

    <a name="en-us_topic_0057777026_table1393932617253"></a><table><thead align="left"><tr id="en-us_topic_0057777026_en-us_topic_0035467699_row72901535141713"><th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057777026_en-us_topic_0035467699_p132908358173"><a name="en-us_topic_0057777026_en-us_topic_0035467699_p132908358173"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_p132908358173"></a><strong id="en-us_topic_0057777026_en-us_topic_0035467699_b8423527069525"><a name="en-us_topic_0057777026_en-us_topic_0035467699_b8423527069525"></a><a name="en-us_topic_0057777026_en-us_topic_0035467699_b8423527069525"></a>Parameter</strong></p>
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

    > ![](/images/icon-note.gif) **NOTE:** 

    > Click the zone name to query detailed zone information. The system has created record sets of the SOA type and NS type in the zone.

    > -   The SOA record set determines the DNS server that is the authoritative information source for a particular domain name.
    > -   The NS record set defines authoritative DNS servers for a zone.

## Modifying a Private zone<a name="section10328742215619"></a>

If the information of your private zone has changed, you can modify its email address or description.

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, Choose **Private Zones**.

    The **Private Zones** page is displayed.

4.  Click on the upper left and select the desired region and project.
5.  Locate the zone to be modified and click **Modify** under **Operation**.

    The **Modify Private Zone** box is displayed.

6.  Change the email address or description of the zone.
7.  Click **OK**.

## Associating a VPC<a name="section3901082101738"></a>

You can associate a new VPC with the private zone on the DNS console.

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, Choose **Private Zones**.

    The **Private Zones** page is displayed.

4.  Click on the upper left and select the desired region and project.
5.  Locate the private zone to be associated with the VPC and click **Associate VPC** in the **Operation** column.

    **Figure 2** Associate VPC<a name="fig385519890242"></a>
    ![](figures/associate-vpc.png "Associate VPC")

6.  Configure the parameters according to [Table 3](#table2843771002454).**Table 3** Associating a VPC

    <a name="table2843771002454"></a><table><thead align="left"><tr id="row3835768902454"><th class="cellrowborder" valign="top" width="19.61%" id="mcps1.2.4.1.1"><p id="p225945050254"><a name="p225945050254"></a><a name="p225945050254"></a><strong id="b84235270695255"><a name="b84235270695255"></a><a name="b84235270695255"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.06%" id="mcps1.2.4.1.2"><p id="p182156250254"><a name="p182156250254"></a><a name="p182156250254"></a><strong id="en-us_topic_0035268497_b8423527061433"><a name="en-us_topic_0035268497_b8423527061433"></a><a name="en-us_topic_0035268497_b8423527061433"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p661795010254"><a name="p661795010254"></a><a name="p661795010254"></a><strong id="b84235270617114"><a name="b84235270617114"></a><a name="b84235270617114"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4962413602454"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.4.1.1 "><p id="p93586590254"><a name="p93586590254"></a><a name="p93586590254"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.06%" headers="mcps1.2.4.1.2 "><p id="p198538920254"><a name="p198538920254"></a><a name="p198538920254"></a>Private zone name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p646614510254"><a name="p646614510254"></a><a name="p646614510254"></a>example.com</p>
    </td>
    </tr>
    <tr id="row878042502454"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.4.1.1 "><p id="p428600050254"><a name="p428600050254"></a><a name="p428600050254"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.06%" headers="mcps1.2.4.1.2 "><p id="p491083660254"><a name="p491083660254"></a><a name="p491083660254"></a>VPC to be associated with the private zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p183547080254"><a name="p183547080254"></a><a name="p183547080254"></a>-</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click **OK**.

## Disassociating a VPC<a name="section4893792902612"></a>

If multiple VPCs are associated with a private zone, you can disassociate one of them on the console.

> ![](/images/icon-note.gif) **NOTE:** 

> If only one VPC is associated, you cannot disassociate it from the private zone. You can choose to delete the private zone.

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, Choose **Private Zones**.

    The **Private Zones** page is displayed.

4.  Click on the upper left and select the desired region and project.
5.  Locate the private zone to be disassociated with the VPC and click in the **Associated VPCs** column to disassociate a VPC.

    **Figure 3** Private Zone<a name="fig8261111312264"></a>
    ![](figures/private-zone.png "Private Zone")

6.  Click **OK**.

    **Figure 4** Disassociate VPC<a name="fig8783134443611"></a>
    ![](figures/disassociate-vpc.png "Disassociate VPC")


## Deleting a Private Zone<a name="section5576188803045"></a>

A private zone can be deleted if you do not need to manage it using the DNS service. After the deletion, domain names included in this zone cannot be resolved.

> ![](/images/icon-notice.gif) **NOTICE:** 

> Before deleting a private zone, ensure that all record sets in this zone have been backed up.

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, Choose **Private Zones**.

    The **Private Zones** page is displayed.

4.  Click on the upper left and select the desired region and project.
5.  Locate the private zone to be deleted and click **Delete** under **Operation**.
6.  Click **OK** to confirm the deletion.

