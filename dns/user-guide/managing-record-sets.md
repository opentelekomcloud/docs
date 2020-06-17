# Managing Record Sets<a name="en-us_topic_0035467703"></a>

## Querying Record Set Details<a name="section42501200102359"></a>

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  On the **Dashboard** page, click **Public Zones** or **Private Zones** under **My Resources**.

    The zone list is displayed.

4.  \(Optional\) If you have selected **Private Zones**, click ![](figures/en-us_image_0079592430.png) on the upper left to select the region and project.
5.  Click a zone name.

    The record set page is displayed.

6.  View the record set details.

## Adding a Record Set<a name="section17307186102417"></a>

The DNS service supports multiple types of record sets. Each record set type applies to a specified application scenario. You can choose the record set types as needed. For details, see section [Record Set](record-set.md).

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, click **Public Zones** or **Private Zones**.

    The zone list is displayed.

4.  \(Optional\) If you have selected **Private Zones**, click ![](figures/en-us_image_0079623919.png) on the upper left to select the region and project.
5.  Click the name of a zone.
6.  Click **Add Record Set**.

    The **Add Record Set** box is displayed.

    **Figure 1** Add Record Set<a name="en-us_topic_0035467699_fig86510231718"></a>
    ![](figures/add-record-set.png "Add Record Set")

7.  Set the required parameters.
    -   [Table 1](#table298011311249) lists the parameters required for adding a record set of the A type.**Table 1** Parameters required for adding a record set of the A type

        <a name="table298011311249"></a><table><thead align="left"><tr id="row798141382414"><th class="cellrowborder" valign="top" width="20.549999999999997%" id="mcps1.2.4.1.1"><p id="p59811413122415"><a name="p59811413122415"></a><a name="p59811413122415"></a><strong id="b8423527069525"><a name="b8423527069525"></a><a name="b8423527069525"></a>Parameter</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="46.12%" id="mcps1.2.4.1.2"><p id="p4981151311242"><a name="p4981151311242"></a><a name="p4981151311242"></a><strong id="en-us_topic_0035268497_b8423527061433"><a name="en-us_topic_0035268497_b8423527061433"></a><a name="en-us_topic_0035268497_b8423527061433"></a>Description</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p8981161312249"><a name="p8981161312249"></a><a name="p8981161312249"></a><strong id="b84235270617114"><a name="b84235270617114"></a><a name="b84235270617114"></a>Example Value</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row3986161312249"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p1998661319243"><a name="p1998661319243"></a><a name="p1998661319243"></a>Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p179861613132418"><a name="p179861613132418"></a><a name="p179861613132418"></a>Domain name (You do not need to manually add the suffix.)</p>
        <p id="p1698641342415"><a name="p1698641342415"></a><a name="p1698641342415"></a>The default value is the zone name.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p298891312414"><a name="p298891312414"></a><a name="p298891312414"></a>www</p>
        </td>
        </tr>
        <tr id="row1098871317246"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p2098819138244"><a name="p2098819138244"></a><a name="p2098819138244"></a>Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p29883133248"><a name="p29883133248"></a><a name="p29883133248"></a>Type of the record set</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p09881613172416"><a name="p09881613172416"></a><a name="p09881613172416"></a></p>
        <p id="p27761650663"><a name="p27761650663"></a><a name="p27761650663"></a>A – Map domains to IPv4 addresses</p>
        </td>
        </tr>
        <tr id="row1699071313249"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p1399021315241"><a name="p1399021315241"></a><a name="p1399021315241"></a>TTL (s)</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p1799017131249"><a name="p1799017131249"></a><a name="p1799017131249"></a>Caching period of the record set (in seconds)</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p399081372415"><a name="p399081372415"></a><a name="p399081372415"></a>The default value is 300s, that is, <strong id="b842352706183837"><a name="b842352706183837"></a><a name="b842352706183837"></a>5 min</strong>.</p>
        </td>
        </tr>
        <tr id="row2990513122419"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p19991213182418"><a name="p19991213182418"></a><a name="p19991213182418"></a>Value</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p15991141313246"><a name="p15991141313246"></a><a name="p15991141313246"></a>IPv4 addresses mapped to the domain name</p>
        <p id="p1099115138244"><a name="p1099115138244"></a><a name="p1099115138244"></a>Every two IPv4 addresses are separated using a line break.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p15992813172419"><a name="p15992813172419"></a><a name="p15992813172419"></a>192.168.12.2</p>
        <p id="p16992121318241"><a name="p16992121318241"></a><a name="p16992121318241"></a>192.168.12.3</p>
        </td>
        </tr>
        <tr id="row59921913132420"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p8992121382414"><a name="p8992121382414"></a><a name="p8992121382414"></a>Tag</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p1399412133244"><a name="p1399412133244"></a><a name="p1399412133244"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a record set.</p>
        <p id="p1699410132244"><a name="p1699410132244"></a><a name="p1699410132244"></a>For details about tag key and value requirements, see <a href="#en-us_topic_0035467703__table26050509163">Table 2</a>.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p59941113182414"><a name="p59941113182414"></a><a name="p59941113182414"></a>example_key1</p>
        <p id="p1499431342413"><a name="p1499431342413"></a><a name="p1499431342413"></a>example_value1</p>
        </td>
        </tr>
        <tr id="row799419131241"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p69946136245"><a name="p69946136245"></a><a name="p69946136245"></a>Description</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p59951113182412"><a name="p59951113182412"></a><a name="p59951113182412"></a>(Optional) Description of the domain name</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p49951713112413"><a name="p49951713112413"></a><a name="p49951713112413"></a>-</p>
        </td>
        </tr>
        </tbody>
        </table>

        **Table 2** Tag key and value requirements

        <a name="table26050509163"></a><table><thead align="left"><tr id="en-us_topic_0035467699_row72901535141713"><th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.4.1.1"><p id="en-us_topic_0035467699_p132908358173"><a name="en-us_topic_0035467699_p132908358173"></a><a name="en-us_topic_0035467699_p132908358173"></a><strong id="en-us_topic_0035467699_b8423527069525"><a name="en-us_topic_0035467699_b8423527069525"></a><a name="en-us_topic_0035467699_b8423527069525"></a>Parameter</strong></p>
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

    -   [Table 3](#table3171006112739) lists the parameters required for adding a record set of the AAAA type.**Table 3** Parameters required for adding a record set of the AAAA type

        <a name="table3171006112739"></a><table><thead align="left"><tr id="row3069844212739"><th class="cellrowborder" valign="top" width="20.549999999999997%" id="mcps1.2.4.1.1"><p id="p2387414512739"><a name="p2387414512739"></a><a name="p2387414512739"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="46.12%" id="mcps1.2.4.1.2"><p id="p5475757412739"><a name="p5475757412739"></a><a name="p5475757412739"></a>Description</p>
        </th>
        <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p617852412739"><a name="p617852412739"></a><a name="p617852412739"></a>Example Value</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row2712386512739"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p57077793115735"><a name="p57077793115735"></a><a name="p57077793115735"></a>Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p498991411924"><a name="p498991411924"></a><a name="p498991411924"></a>Domain name (You do not need to manually add the suffix.)</p>
        <p id="p4490923311924"><a name="p4490923311924"></a><a name="p4490923311924"></a>The default value is the zone name.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p28898697122810"><a name="p28898697122810"></a><a name="p28898697122810"></a>www</p>
        </td>
        </tr>
        <tr id="row3782375412739"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p3932606412739"><a name="p3932606412739"></a><a name="p3932606412739"></a>Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p3129459512739"><a name="p3129459512739"></a><a name="p3129459512739"></a>Type of the record set</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p5183423812739"><a name="p5183423812739"></a><a name="p5183423812739"></a></p>
        <p id="p5595396711"><a name="p5595396711"></a><a name="p5595396711"></a>AAAA – Map domains to IPv6 addresses</p>
        </td>
        </tr>
        <tr id="row5115242612739"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p486947012739"><a name="p486947012739"></a><a name="p486947012739"></a>TTL (s)</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p5888275712739"><a name="p5888275712739"></a><a name="p5888275712739"></a>Caching period of the record set (in seconds)</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p477403312739"><a name="p477403312739"></a><a name="p477403312739"></a>The default value is 300s, that is, <strong id="b842352706183837_1"><a name="b842352706183837_1"></a><a name="b842352706183837_1"></a>5 min</strong>.</p>
        </td>
        </tr>
        <tr id="row3916732112739"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p5771865512739"><a name="p5771865512739"></a><a name="p5771865512739"></a>Value</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p4469944512739"><a name="p4469944512739"></a><a name="p4469944512739"></a>IPv6 addresses mapped to the domain name</p>
        <p id="p6675068912739"><a name="p6675068912739"></a><a name="p6675068912739"></a>Every two IPv6 addresses are separated using a line break.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p6593540212739"><a name="p6593540212739"></a><a name="p6593540212739"></a>ff03:0db8:85a3:0:0:8a2e:0370:7334</p>
        </td>
        </tr>
        <tr id="row158111406234"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p174971657162412"><a name="p174971657162412"></a><a name="p174971657162412"></a>Tag</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p8505957152412"><a name="p8505957152412"></a><a name="p8505957152412"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a record set.</p>
        <p id="p7512155710249"><a name="p7512155710249"></a><a name="p7512155710249"></a>For details about tag key and value requirements, see <a href="#en-us_topic_0035467703__table26050509163">Table 2</a>.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p19522657162412"><a name="p19522657162412"></a><a name="p19522657162412"></a>example_key1</p>
        <p id="p05253572248"><a name="p05253572248"></a><a name="p05253572248"></a>example_value1</p>
        </td>
        </tr>
        <tr id="row5602640133247"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p48629108133253"><a name="p48629108133253"></a><a name="p48629108133253"></a>Description</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p46643703133253"><a name="p46643703133253"></a><a name="p46643703133253"></a>(Optional) Description of the domain name, which cannot exceed 255 characters</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p46174475133253"><a name="p46174475133253"></a><a name="p46174475133253"></a>The description of the hostname.</p>
        </td>
        </tr>
        </tbody>
        </table>

    -   [Table 4](#table51864159122254) lists the parameters required for adding a record set of the NS type.

        > ![](/images/icon-note.gif) **NOTE:** 

        > You can create NS record sets only in public zones.

        **Table 4** Parameters required for adding a record set of the NS type

        <a name="table51864159122254"></a><table><thead align="left"><tr id="en-us_topic_0035467703_row3069844212739"><th class="cellrowborder" valign="top" width="20.549999999999997%" id="mcps1.2.4.1.1"><p id="en-us_topic_0035467703_p2387414512739"><a name="en-us_topic_0035467703_p2387414512739"></a><a name="en-us_topic_0035467703_p2387414512739"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="46.12%" id="mcps1.2.4.1.2"><p id="en-us_topic_0035467703_p5475757412739"><a name="en-us_topic_0035467703_p5475757412739"></a><a name="en-us_topic_0035467703_p5475757412739"></a>Description</p>
        </th>
        <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="en-us_topic_0035467703_p617852412739"><a name="en-us_topic_0035467703_p617852412739"></a><a name="en-us_topic_0035467703_p617852412739"></a>Example Value</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="en-us_topic_0035467703_row2712386512739"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467703_p354591312739"><a name="en-us_topic_0035467703_p354591312739"></a><a name="en-us_topic_0035467703_p354591312739"></a>Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p2606520411934"><a name="p2606520411934"></a><a name="p2606520411934"></a>Domain name (You do not need to manually add the suffix.)</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p5691184212286"><a name="p5691184212286"></a><a name="p5691184212286"></a>abc</p>
        </td>
        </tr>
        <tr id="en-us_topic_0035467703_row3782375412739"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467703_p3932606412739"><a name="en-us_topic_0035467703_p3932606412739"></a><a name="en-us_topic_0035467703_p3932606412739"></a>Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467703_p3129459512739"><a name="en-us_topic_0035467703_p3129459512739"></a><a name="en-us_topic_0035467703_p3129459512739"></a>Type of the record set</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p214011191388"><a name="p214011191388"></a><a name="p214011191388"></a>NS – Delegate subdomains to other name servers</p>
        </td>
        </tr>
        <tr id="en-us_topic_0035467703_row5115242612739"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467703_p486947012739"><a name="en-us_topic_0035467703_p486947012739"></a><a name="en-us_topic_0035467703_p486947012739"></a>TTL (s)</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467703_p5888275712739"><a name="en-us_topic_0035467703_p5888275712739"></a><a name="en-us_topic_0035467703_p5888275712739"></a>Caching period of the record set (in seconds)</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467703_p477403312739"><a name="en-us_topic_0035467703_p477403312739"></a><a name="en-us_topic_0035467703_p477403312739"></a>The default value is 300s, that is, <strong id="b842352706183837_2"><a name="b842352706183837_2"></a><a name="b842352706183837_2"></a>5 min</strong>.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0035467703_row3916732112739"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467703_p5771865512739"><a name="en-us_topic_0035467703_p5771865512739"></a><a name="en-us_topic_0035467703_p5771865512739"></a>Value</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467703_p6675068912739"><a name="en-us_topic_0035467703_p6675068912739"></a><a name="en-us_topic_0035467703_p6675068912739"></a>NS address (DNS server domain name)</p>
        <p id="p56933877122524"><a name="p56933877122524"></a><a name="p56933877122524"></a>Two domain names are separated using a line break.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p49423069122512"><a name="p49423069122512"></a><a name="p49423069122512"></a>ns1.example.net</p>
        <p id="p42154445122512"><a name="p42154445122512"></a><a name="p42154445122512"></a>ns2.example.net</p>
        </td>
        </tr>
        <tr id="row097221322518"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p12194133218255"><a name="p12194133218255"></a><a name="p12194133218255"></a>Tag</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p181991932132510"><a name="p181991932132510"></a><a name="p181991932132510"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a record set.</p>
        <p id="p1820510326251"><a name="p1820510326251"></a><a name="p1820510326251"></a>For details about tag key and value requirements, see <a href="#en-us_topic_0035467703__table26050509163">Table 2</a>.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p521214327252"><a name="p521214327252"></a><a name="p521214327252"></a>example_key1</p>
        <p id="p17215143210256"><a name="p17215143210256"></a><a name="p17215143210256"></a>example_value1</p>
        </td>
        </tr>
        <tr id="row21315254133345"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p51175951133351"><a name="p51175951133351"></a><a name="p51175951133351"></a>Description</p>
        </td>
        <td class="cellrowborder" valign="top" width="46.12%" headers="mcps1.2.4.1.2 "><p id="p51611365133351"><a name="p51611365133351"></a><a name="p51611365133351"></a>(Optional) Description of the domain name, which cannot exceed 255 characters</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p43721337133351"><a name="p43721337133351"></a><a name="p43721337133351"></a>The description of the hostname.</p>
        </td>
        </tr>
        </tbody>
        </table>

    -   [Table 5](#en-us_topic_0035467703_table51864159122254) lists the parameters required for adding a record set of the CNAME type.**Table 5** Parameters required for adding a record set of the CNAME type

        <a name="en-us_topic_0035467703_table51864159122254"></a><table><thead align="left"><tr id="en-us_topic_0035467703_en-us_topic_0035467703_row3069844212739"><th class="cellrowborder" valign="top" width="20.549999999999997%" id="mcps1.2.4.1.1"><p id="en-us_topic_0035467703_en-us_topic_0035467703_p2387414512739"><a name="en-us_topic_0035467703_en-us_topic_0035467703_p2387414512739"></a><a name="en-us_topic_0035467703_en-us_topic_0035467703_p2387414512739"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="44.99%" id="mcps1.2.4.1.2"><p id="en-us_topic_0035467703_en-us_topic_0035467703_p5475757412739"><a name="en-us_topic_0035467703_en-us_topic_0035467703_p5475757412739"></a><a name="en-us_topic_0035467703_en-us_topic_0035467703_p5475757412739"></a>Description</p>
        </th>
        <th class="cellrowborder" valign="top" width="34.46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0035467703_en-us_topic_0035467703_p617852412739"><a name="en-us_topic_0035467703_en-us_topic_0035467703_p617852412739"></a><a name="en-us_topic_0035467703_en-us_topic_0035467703_p617852412739"></a>Example Value</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="en-us_topic_0035467703_en-us_topic_0035467703_row2712386512739"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467703_en-us_topic_0035467703_p354591312739"><a name="en-us_topic_0035467703_en-us_topic_0035467703_p354591312739"></a><a name="en-us_topic_0035467703_en-us_topic_0035467703_p354591312739"></a>Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="44.99%" headers="mcps1.2.4.1.2 "><p id="p5964432911942"><a name="p5964432911942"></a><a name="p5964432911942"></a>Domain name alias (You do not need to manually add the suffix.)</p>
        </td>
        <td class="cellrowborder" valign="top" width="34.46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467703_en-us_topic_0035467703_p4507410512739"><a name="en-us_topic_0035467703_en-us_topic_0035467703_p4507410512739"></a><a name="en-us_topic_0035467703_en-us_topic_0035467703_p4507410512739"></a>alias</p>
        </td>
        </tr>
        <tr id="en-us_topic_0035467703_en-us_topic_0035467703_row3782375412739"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467703_en-us_topic_0035467703_p3932606412739"><a name="en-us_topic_0035467703_en-us_topic_0035467703_p3932606412739"></a><a name="en-us_topic_0035467703_en-us_topic_0035467703_p3932606412739"></a>Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="44.99%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467703_en-us_topic_0035467703_p3129459512739"><a name="en-us_topic_0035467703_en-us_topic_0035467703_p3129459512739"></a><a name="en-us_topic_0035467703_en-us_topic_0035467703_p3129459512739"></a>Type of the record set</p>
        </td>
        <td class="cellrowborder" valign="top" width="34.46%" headers="mcps1.2.4.1.3 "><p id="p7252454291"><a name="p7252454291"></a><a name="p7252454291"></a>CNAME – Map one domain to another</p>
        </td>
        </tr>
        <tr id="en-us_topic_0035467703_en-us_topic_0035467703_row5115242612739"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467703_en-us_topic_0035467703_p486947012739"><a name="en-us_topic_0035467703_en-us_topic_0035467703_p486947012739"></a><a name="en-us_topic_0035467703_en-us_topic_0035467703_p486947012739"></a>TTL (s)</p>
        </td>
        <td class="cellrowborder" valign="top" width="44.99%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467703_en-us_topic_0035467703_p5888275712739"><a name="en-us_topic_0035467703_en-us_topic_0035467703_p5888275712739"></a><a name="en-us_topic_0035467703_en-us_topic_0035467703_p5888275712739"></a>Caching period of the record set (in seconds)</p>
        </td>
        <td class="cellrowborder" valign="top" width="34.46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467703_en-us_topic_0035467703_p477403312739"><a name="en-us_topic_0035467703_en-us_topic_0035467703_p477403312739"></a><a name="en-us_topic_0035467703_en-us_topic_0035467703_p477403312739"></a>The default value is 300s, that is, <strong id="b842352706183837_3"><a name="b842352706183837_3"></a><a name="b842352706183837_3"></a>5 min</strong>.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0035467703_en-us_topic_0035467703_row3916732112739"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467703_en-us_topic_0035467703_p5771865512739"><a name="en-us_topic_0035467703_en-us_topic_0035467703_p5771865512739"></a><a name="en-us_topic_0035467703_en-us_topic_0035467703_p5771865512739"></a>Value</p>
        </td>
        <td class="cellrowborder" valign="top" width="44.99%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467703_p56933877122524"><a name="en-us_topic_0035467703_p56933877122524"></a><a name="en-us_topic_0035467703_p56933877122524"></a>Domain name mapped to the alias</p>
        </td>
        <td class="cellrowborder" valign="top" width="34.46%" headers="mcps1.2.4.1.3 "><p id="p1396527123037"><a name="p1396527123037"></a><a name="p1396527123037"></a>webserver01.example.com</p>
        </td>
        </tr>
        <tr id="row14781155652511"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p1079616472617"><a name="p1079616472617"></a><a name="p1079616472617"></a>Tag</p>
        </td>
        <td class="cellrowborder" valign="top" width="44.99%" headers="mcps1.2.4.1.2 "><p id="p1380164152613"><a name="p1380164152613"></a><a name="p1380164152613"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a record set.</p>
        <p id="p1480614410262"><a name="p1480614410262"></a><a name="p1480614410262"></a>For details about tag key and value requirements, see <a href="#en-us_topic_0035467703__table26050509163">Table 2</a>.</p>
        </td>
        <td class="cellrowborder" valign="top" width="34.46%" headers="mcps1.2.4.1.3 "><p id="p168174416269"><a name="p168174416269"></a><a name="p168174416269"></a>example_key1</p>
        <p id="p58186442618"><a name="p58186442618"></a><a name="p58186442618"></a>example_value1</p>
        </td>
        </tr>
        <tr id="row17850451133421"><td class="cellrowborder" valign="top" width="20.549999999999997%" headers="mcps1.2.4.1.1 "><p id="p42407063133426"><a name="p42407063133426"></a><a name="p42407063133426"></a>Description</p>
        </td>
        <td class="cellrowborder" valign="top" width="44.99%" headers="mcps1.2.4.1.2 "><p id="p12420091133426"><a name="p12420091133426"></a><a name="p12420091133426"></a>(Optional) Description of the domain name, which cannot exceed 255 characters</p>
        </td>
        <td class="cellrowborder" valign="top" width="34.46%" headers="mcps1.2.4.1.3 "><p id="p61658598133426"><a name="p61658598133426"></a><a name="p61658598133426"></a>The description of the alias name.</p>
        </td>
        </tr>
        </tbody>
        </table>

    -   [Table 6](#en-us_topic_0035467703_table3171006112739) lists the parameters required for adding a record set of the MX type.**Table 6** Parameters required for adding a record set of the MX type

        <a name="en-us_topic_0035467703_table3171006112739"></a><table><thead align="left"><tr id="row40985647123146"><th class="cellrowborder" valign="top" width="19.05%" id="mcps1.2.4.1.1"><p id="p31503124123146"><a name="p31503124123146"></a><a name="p31503124123146"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="47.620000000000005%" id="mcps1.2.4.1.2"><p id="p1616237123146"><a name="p1616237123146"></a><a name="p1616237123146"></a>Description</p>
        </th>
        <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p63806371123146"><a name="p63806371123146"></a><a name="p63806371123146"></a>Example Value</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row933533123146"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="p8507331123146"><a name="p8507331123146"></a><a name="p8507331123146"></a>Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.620000000000005%" headers="mcps1.2.4.1.2 "><p id="p16846400111050"><a name="p16846400111050"></a><a name="p16846400111050"></a>Domain name (You do not need to manually add the suffix.)</p>
        <p id="p17399874111050"><a name="p17399874111050"></a><a name="p17399874111050"></a>The default value is the zone name.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p1195486695028"><a name="p1195486695028"></a><a name="p1195486695028"></a>Usually, the value is blank.</p>
        </td>
        </tr>
        <tr id="row26983954123146"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="p38216656123146"><a name="p38216656123146"></a><a name="p38216656123146"></a>Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.620000000000005%" headers="mcps1.2.4.1.2 "><p id="p8541435123146"><a name="p8541435123146"></a><a name="p8541435123146"></a>Type of the record set</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p1410795417116"><a name="p1410795417116"></a><a name="p1410795417116"></a>MX – Map domains to email servers</p>
        </td>
        </tr>
        <tr id="row52690765123146"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="p40093542123146"><a name="p40093542123146"></a><a name="p40093542123146"></a>TTL (s)</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.620000000000005%" headers="mcps1.2.4.1.2 "><p id="p26351431123146"><a name="p26351431123146"></a><a name="p26351431123146"></a>Caching period of the record set (in seconds)</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p54091161123146"><a name="p54091161123146"></a><a name="p54091161123146"></a>The default value is 300s, that is, <strong id="b842352706183837_4"><a name="b842352706183837_4"></a><a name="b842352706183837_4"></a>5 min</strong>.</p>
        </td>
        </tr>
        <tr id="row17058403123146"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="p39553441123146"><a name="p39553441123146"></a><a name="p39553441123146"></a>Value</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.620000000000005%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467703_p4469944512739"><a name="en-us_topic_0035467703_p4469944512739"></a><a name="en-us_topic_0035467703_p4469944512739"></a>Mail server domain name</p>
        <p id="p8498594123410"><a name="p8498594123410"></a><a name="p8498594123410"></a>Format: <strong id="b842352706185121"><a name="b842352706185121"></a><a name="b842352706185121"></a>[priority] [mail server host name]</strong></p>
        <p id="p9378486123410"><a name="p9378486123410"></a><a name="p9378486123410"></a><strong id="b842352706185127"><a name="b842352706185127"></a><a name="b842352706185127"></a>priority</strong> specifies the priority for a mail server to receive emails. A smaller value indicates a higher priority.</p>
        <p id="p17297517123410"><a name="p17297517123410"></a><a name="p17297517123410"></a>Set this parameter to the domain name provided by the email service provider.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467703_p6593540212739"><a name="en-us_topic_0035467703_p6593540212739"></a><a name="en-us_topic_0035467703_p6593540212739"></a>10 mailserver.example.com</p>
        </td>
        </tr>
        <tr id="row17185193111276"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="p10406539102715"><a name="p10406539102715"></a><a name="p10406539102715"></a>Tag</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.620000000000005%" headers="mcps1.2.4.1.2 "><p id="p0411239132716"><a name="p0411239132716"></a><a name="p0411239132716"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a record set.</p>
        <p id="p74162039142714"><a name="p74162039142714"></a><a name="p74162039142714"></a>For details about tag key and value requirements, see <a href="#en-us_topic_0035467703__table26050509163">Table 2</a>.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p7423139192714"><a name="p7423139192714"></a><a name="p7423139192714"></a>example_key1</p>
        <p id="p1428103913279"><a name="p1428103913279"></a><a name="p1428103913279"></a>example_value1</p>
        </td>
        </tr>
        <tr id="row31966209133453"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.1 "><p id="p3764367133458"><a name="p3764367133458"></a><a name="p3764367133458"></a>Description</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.620000000000005%" headers="mcps1.2.4.1.2 "><p id="p36478336133458"><a name="p36478336133458"></a><a name="p36478336133458"></a>(Optional) Description of the domain name, which cannot exceed 255 characters</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p17597507133458"><a name="p17597507133458"></a><a name="p17597507133458"></a>The description of the hostname.</p>
        </td>
        </tr>
        </tbody>
        </table>

    -   [Table 7](#table5740910174810) lists the parameters required for adding a record set of the TXT type.**Table 7** Parameters required for adding a record set of the TXT type

        <a name="table5740910174810"></a><table><thead align="left"><tr id="row118734174810"><th class="cellrowborder" valign="top" width="18.86%" id="mcps1.2.4.1.1"><p id="p9617457174810"><a name="p9617457174810"></a><a name="p9617457174810"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="47.81%" id="mcps1.2.4.1.2"><p id="p40816590174810"><a name="p40816590174810"></a><a name="p40816590174810"></a>Description</p>
        </th>
        <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p17809483174810"><a name="p17809483174810"></a><a name="p17809483174810"></a>Example Value</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row33282000174810"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p11487494174810"><a name="p11487494174810"></a><a name="p11487494174810"></a>Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p2885765511112"><a name="p2885765511112"></a><a name="p2885765511112"></a>Domain name (You do not need to manually add the suffix.)</p>
        <p id="p5839230411112"><a name="p5839230411112"></a><a name="p5839230411112"></a>The default value is the zone name.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467703_p5691184212286"><a name="en-us_topic_0035467703_p5691184212286"></a><a name="en-us_topic_0035467703_p5691184212286"></a>abc</p>
        </td>
        </tr>
        <tr id="row5056388174810"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p6914285174810"><a name="p6914285174810"></a><a name="p6914285174810"></a>Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p23186247174810"><a name="p23186247174810"></a><a name="p23186247174810"></a>Type of the record set</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p1031317712158"><a name="p1031317712158"></a><a name="p1031317712158"></a>TXT – Specify text records</p>
        </td>
        </tr>
        <tr id="row58449804174810"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p36813654174810"><a name="p36813654174810"></a><a name="p36813654174810"></a>TTL (s)</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p29115980174810"><a name="p29115980174810"></a><a name="p29115980174810"></a>Caching period of the record set (in seconds)</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p9584216174810"><a name="p9584216174810"></a><a name="p9584216174810"></a>The default value is 300s, that is, <strong id="b842352706183837_5"><a name="b842352706183837_5"></a><a name="b842352706183837_5"></a>5 min</strong>.</p>
        </td>
        </tr>
        <tr id="row19149080174810"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p7571677174810"><a name="p7571677174810"></a><a name="p7571677174810"></a>Value</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p9326123174810"><a name="p9326123174810"></a><a name="p9326123174810"></a>Enter the text content based on requirements:</p>
        <a name="ul32037609181232"></a><a name="ul32037609181232"></a><ul id="ul32037609181232"><li id="li58018380101436"><a name="li58018380101436"></a><a name="li58018380101436"></a>One or more text records are supported. Every two text records are separated with a line break.</li><li id="li63305313203922"><a name="li63305313203922"></a><a name="li63305313203922"></a>A single text record can contain multiple text character strings, each of which is double quoted and separated from others using a space.</li><li id="li5689491181232"><a name="li5689491181232"></a><a name="li5689491181232"></a>Each text character string within a pair of double quotation marks contains a maximum of 255 characters.</li><li id="li37390633181239"><a name="li37390633181239"></a><a name="li37390633181239"></a>One text record must not exceed 4096 characters.</li><li id="li2600389318132"><a name="li2600389318132"></a><a name="li2600389318132"></a>The text value cannot be left empty.</li><li id="li51504955181315"><a name="li51504955181315"></a><a name="li51504955181315"></a>The text cannot contain a backslash (\).</li><li id="li39026303103757"><a name="li39026303103757"></a><a name="li39026303103757"></a>The text only supports English characters.</li></ul>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p66533616181420"><a name="p66533616181420"></a><a name="p66533616181420"></a>"aaa"</p>
        <p id="p24045512155350"><a name="p24045512155350"></a><a name="p24045512155350"></a>"bbb" "ccc" "ddd"</p>
        <p id="p49045257204059"><a name="p49045257204059"></a><a name="p49045257204059"></a><strong id="b842352706194848"><a name="b842352706194848"></a><a name="b842352706194848"></a>"bbb" "ccc" "ddd"</strong>&nbsp;indicates a text record, and&nbsp;<strong id="b842352706194913"><a name="b842352706194913"></a><a name="b842352706194913"></a>"bbb"</strong> is a text character string.</p>
        </td>
        </tr>
        <tr id="row168631717132812"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p20610172802814"><a name="p20610172802814"></a><a name="p20610172802814"></a>Tag</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p1261813285288"><a name="p1261813285288"></a><a name="p1261813285288"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a record set.</p>
        <p id="p5622122811281"><a name="p5622122811281"></a><a name="p5622122811281"></a>For details about tag key and value requirements, see <a href="#en-us_topic_0035467703__table26050509163">Table 2</a>.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p18633928192814"><a name="p18633928192814"></a><a name="p18633928192814"></a>example_key1</p>
        <p id="p1763732818281"><a name="p1763732818281"></a><a name="p1763732818281"></a>example_value1</p>
        </td>
        </tr>
        <tr id="row54183889133522"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p65190159133528"><a name="p65190159133528"></a><a name="p65190159133528"></a>Description</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p45911501133528"><a name="p45911501133528"></a><a name="p45911501133528"></a>(Optional) Description of the domain name, which cannot exceed 255 characters</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p49270015133528"><a name="p49270015133528"></a><a name="p49270015133528"></a>The description of the hostname.</p>
        </td>
        </tr>
        </tbody>
        </table>

    -   [Table 8](#table28439303171815) lists the parameters required for adding a record set of the SRV type.**Table 8** Parameters required for adding a record set of the SRV type

        <a name="table28439303171815"></a><table><thead align="left"><tr id="row7964149171815"><th class="cellrowborder" valign="top" width="18.86%" id="mcps1.2.4.1.1"><p id="p34502967171815"><a name="p34502967171815"></a><a name="p34502967171815"></a><strong id="b84235270695255"><a name="b84235270695255"></a><a name="b84235270695255"></a>Parameter</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="47.81%" id="mcps1.2.4.1.2"><p id="p43276958171815"><a name="p43276958171815"></a><a name="p43276958171815"></a>Description</p>
        </th>
        <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p15772738171815"><a name="p15772738171815"></a><a name="p15772738171815"></a>Example Value</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row7736918171815"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p22710623171815"><a name="p22710623171815"></a><a name="p22710623171815"></a>Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p27785896213757"><a name="p27785896213757"></a><a name="p27785896213757"></a>Service (for example, FTP, SSH, or SIP) provided over the specified protocol (for example, TCP or UDP) on a host</p>
        <p id="p27621209171815"><a name="p27621209171815"></a><a name="p27621209171815"></a>The format is _<em id="i61518104214227"><a name="i61518104214227"></a><a name="i61518104214227"></a>Service name</em>._<em id="i48790082214232"><a name="i48790082214232"></a><a name="i48790082214232"></a>Protocol</em>.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p28796317213955"><a name="p28796317213955"></a><a name="p28796317213955"></a><strong id="b84235270612936"><a name="b84235270612936"></a><a name="b84235270612936"></a>_ftp._tcp</strong>: indicates that the host provides the FTP service over TCP.</p>
        </td>
        </tr>
        <tr id="row3202766171815"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p58097464171815"><a name="p58097464171815"></a><a name="p58097464171815"></a>Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p8274126171815"><a name="p8274126171815"></a><a name="p8274126171815"></a>Type of the record set</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p4791154914158"><a name="p4791154914158"></a><a name="p4791154914158"></a>SRV – Record servers providing specific services</p>
        </td>
        </tr>
        <tr id="row59149642171815"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p26391727171815"><a name="p26391727171815"></a><a name="p26391727171815"></a>TTL (s)</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p9431650214151"><a name="p9431650214151"></a><a name="p9431650214151"></a>Caching period of the record set (in seconds)</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p25766181214151"><a name="p25766181214151"></a><a name="p25766181214151"></a>The default value is 300s, that is, <strong id="b842352706183837_6"><a name="b842352706183837_6"></a><a name="b842352706183837_6"></a>5 min</strong>.</p>
        </td>
        </tr>
        <tr id="row3093139171815"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p49217725171815"><a name="p49217725171815"></a><a name="p49217725171815"></a>Value</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p27212779171815"><a name="p27212779171815"></a><a name="p27212779171815"></a>The value is composed of the priority, weight, port number, and host domain name.</p>
        <a name="ul61715031214652"></a><a name="ul61715031214652"></a><ul id="ul61715031214652"><li id="li13383858214652"><a name="li13383858214652"></a><a name="li13383858214652"></a>The priority, weight, and port number are a digit ranging from 0 to 65535.</li><li id="li4365262921482"><a name="li4365262921482"></a><a name="li4365262921482"></a>The system checks the priority first. Only when the priority values are the same does the system check the weight values.</li><li id="li60047294214834"><a name="li60047294214834"></a><a name="li60047294214834"></a>A smaller priority value indicates a higher priority.</li><li id="li3933924821491"><a name="li3933924821491"></a><a name="li3933924821491"></a>The larger weight value indicates a larger weight.</li><li id="li44091146214942"><a name="li44091146214942"></a><a name="li44091146214942"></a>The host domain name must be mapped to a functional host.</li></ul>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p56751494171815"><a name="p56751494171815"></a><a name="p56751494171815"></a>2 1 2355 example_server.test.com</p>
        </td>
        </tr>
        <tr id="row126157642916"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p104991515162919"><a name="p104991515162919"></a><a name="p104991515162919"></a>Tag</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p16504315102920"><a name="p16504315102920"></a><a name="p16504315102920"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a record set.</p>
        <p id="p55151615192914"><a name="p55151615192914"></a><a name="p55151615192914"></a>For details about tag key and value requirements, see <a href="#en-us_topic_0035467703__table26050509163">Table 2</a>.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p15524415162910"><a name="p15524415162910"></a><a name="p15524415162910"></a>example_key1</p>
        <p id="p152817154291"><a name="p152817154291"></a><a name="p152817154291"></a>example_value1</p>
        </td>
        </tr>
        <tr id="row41001399171815"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p32779040171815"><a name="p32779040171815"></a><a name="p32779040171815"></a>Description</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p37856553171815"><a name="p37856553171815"></a><a name="p37856553171815"></a>(Optional) Description of the SRV record set</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p46481914171815"><a name="p46481914171815"></a><a name="p46481914171815"></a>The description of SRV Server.</p>
        </td>
        </tr>
        </tbody>
        </table>

    -   [Table 9](#table676063732817) lists the parameters required for adding a record set of the CAA type.

        > ![](/images/icon-note.gif) **NOTE:** 

        > You can create CAA record sets only in public zones.

        **Table 9** Parameters required for adding a record set of the CAA type

        <a name="table676063732817"></a><table><thead align="left"><tr id="row5778037182810"><th class="cellrowborder" valign="top" width="18.86%" id="mcps1.2.4.1.1"><p id="p7782133732811"><a name="p7782133732811"></a><a name="p7782133732811"></a><strong id="b84235270695255_1"><a name="b84235270695255_1"></a><a name="b84235270695255_1"></a>Parameter</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="47.81%" id="mcps1.2.4.1.2"><p id="p12788153715287"><a name="p12788153715287"></a><a name="p12788153715287"></a><strong id="en-us_topic_0035268497_b8423527061433_1"><a name="en-us_topic_0035268497_b8423527061433_1"></a><a name="en-us_topic_0035268497_b8423527061433_1"></a>Description</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p15792153719289"><a name="p15792153719289"></a><a name="p15792153719289"></a><strong id="b84235270617114_1"><a name="b84235270617114_1"></a><a name="b84235270617114_1"></a>Example Value</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row207951137172810"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p8798203752820"><a name="p8798203752820"></a><a name="p8798203752820"></a>Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p1651552314301"><a name="p1651552314301"></a><a name="p1651552314301"></a>Domain name (You do not need to manually add the suffix.)</p>
        <p id="p551572315301"><a name="p551572315301"></a><a name="p551572315301"></a>The default value is the zone name.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p78160372285"><a name="p78160372285"></a><a name="p78160372285"></a>Usually, the value is blank.</p>
        </td>
        </tr>
        <tr id="row13819837192816"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p982663713288"><a name="p982663713288"></a><a name="p982663713288"></a>Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p1383173742816"><a name="p1383173742816"></a><a name="p1383173742816"></a>Type of the record</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p115317413182"><a name="p115317413182"></a><a name="p115317413182"></a>CAA – Grant certificate issuing permissions to CAs</p>
        </td>
        </tr>
        <tr id="row3866173712813"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p9874163714287"><a name="p9874163714287"></a><a name="p9874163714287"></a>TTL (s)</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p1887933714285"><a name="p1887933714285"></a><a name="p1887933714285"></a>Caching period of the record set (in seconds)</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p68863371284"><a name="p68863371284"></a><a name="p68863371284"></a>The default value is 300s, that is, <strong id="b842352706183837_7"><a name="b842352706183837_7"></a><a name="b842352706183837_7"></a>5 min</strong>.</p>
        </td>
        </tr>
        <tr id="row9887737162813"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p689116371284"><a name="p689116371284"></a><a name="p689116371284"></a>Value</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p19128114815389"><a name="p19128114815389"></a><a name="p19128114815389"></a>Format: <strong id="b84235270615728"><a name="b84235270615728"></a><a name="b84235270615728"></a>[flag] [tag] [value]</strong></p>
        <a name="ul4929101919515"></a><a name="ul4929101919515"></a><ul id="ul4929101919515"><li id="li119293195518"><a name="li119293195518"></a><a name="li119293195518"></a><strong id="b84235270615756"><a name="b84235270615756"></a><a name="b84235270615756"></a>Flag</strong>: certificate authority (CA) identifier, which is an unsigned character ranging from 0 to 255. Usually, it is specified to&nbsp;<strong id="b842352706105143"><a name="b842352706105143"></a><a name="b842352706105143"></a>0</strong>.</li><li id="li1649132215511"><a name="li1649132215511"></a><a name="li1649132215511"></a><strong id="b8423527061587"><a name="b8423527061587"></a><a name="b8423527061587"></a>Tag</strong>: a string of 1 to 15 characters composed of upper- and lower-case letters and digits from 0 to 9. The tag can be the following:<a name="ul359754482613"></a><a name="ul359754482613"></a><ul id="ul359754482613"><li id="li959784482616"><a name="li959784482616"></a><a name="li959784482616"></a><strong id="b84235270695322"><a name="b84235270695322"></a><a name="b84235270695322"></a>issue</strong>: authorizes a CA to issue all types of certificates.</li><li id="li959734418266"><a name="li959734418266"></a><a name="li959734418266"></a><strong id="b84235270695328"><a name="b84235270695328"></a><a name="b84235270695328"></a>issuewild</strong>: authorizes a CA to issue a wildcard certificate.</li><li id="li7597114418262"><a name="li7597114418262"></a><a name="li7597114418262"></a><strong id="b84235270695332"><a name="b84235270695332"></a><a name="b84235270695332"></a>iodef</strong>: requests notification once the CA receives invalid certificate requests.</li></ul>
        </li></ul>
        <a name="ul445910264513"></a><a name="ul445910264513"></a><ul id="ul445910264513"><li id="li124587266518"><a name="li124587266518"></a><a name="li124587266518"></a><strong id="b84235270615101"><a name="b84235270615101"></a><a name="b84235270615101"></a>Value</strong>: authorized CA or email address/URL for notification once the CA receives an invalid certificate request, depending on the setting of the tag. The value must be enclosed in quotation marks (""). It is a string of 1 to 255 characters, including letters, digits, spaces, and special characters -#*?&amp;_~=:;.@+^/!%.</li></ul>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p9310164811125"><a name="p9310164811125"></a><a name="p9310164811125"></a>domain.com. CAA 0 issue "ca.abc.com"</p>
        <p id="p183101948161220"><a name="p183101948161220"></a><a name="p183101948161220"></a>domain.com. CAA 0 issuewild "ca.def.com"</p>
        <p id="p831014831214"><a name="p831014831214"></a><a name="p831014831214"></a>domain.com. CAA 0 iodef "mailto:admin@domain.com"</p>
        <p id="p143101248181211"><a name="p143101248181211"></a><a name="p143101248181211"></a>domain.com. CAA 0 iodef "http:// domain.com/log/"</p>
        </td>
        </tr>
        <tr id="row1844134819292"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p1481158112914"><a name="p1481158112914"></a><a name="p1481158112914"></a>Tag</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p18487135819293"><a name="p18487135819293"></a><a name="p18487135819293"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a record set.</p>
        <p id="p1849145832914"><a name="p1849145832914"></a><a name="p1849145832914"></a>For details about tag key and value requirements, see <a href="#en-us_topic_0035467703__table26050509163">Table 2</a>.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p205017586294"><a name="p205017586294"></a><a name="p205017586294"></a>example_key1</p>
        <p id="p11507158172920"><a name="p11507158172920"></a><a name="p11507158172920"></a>example_value1</p>
        </td>
        </tr>
        <tr id="row179379378281"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p094143782818"><a name="p094143782818"></a><a name="p094143782818"></a>Description</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p3400191253413"><a name="p3400191253413"></a><a name="p3400191253413"></a>(Optional) Description of the domain name</p>
        <p id="p16402112133418"><a name="p16402112133418"></a><a name="p16402112133418"></a>The value cannot exceed 255 characters.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p8951437162817"><a name="p8951437162817"></a><a name="p8951437162817"></a>Description of the CAA record set</p>
        </td>
        </tr>
        </tbody>
        </table>

    -   [Table 10](#table6260239895544) lists the parameters required for adding a record set of the PTR type.

        > ![](/images/icon-note.gif) **NOTE:** 

        > PTR records sets take effect only in a private zone whose top-level domain name is **in-addr.arpa**. For details about how to add a PTR record in a public zone, see section [Managing PTR Records](managing-ptr-records.md).

        **Table 10** Parameters required for adding a record set of the PTR type

        <a name="table6260239895544"></a><table><thead align="left"><tr id="row897191795544"><th class="cellrowborder" valign="top" width="18.86%" id="mcps1.2.4.1.1"><p id="p5563669295544"><a name="p5563669295544"></a><a name="p5563669295544"></a><strong id="b84235270695255_2"><a name="b84235270695255_2"></a><a name="b84235270695255_2"></a>Parameter</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="47.81%" id="mcps1.2.4.1.2"><p id="p1027823295544"><a name="p1027823295544"></a><a name="p1027823295544"></a>Description</p>
        </th>
        <th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p2723046495544"><a name="p2723046495544"></a><a name="p2723046495544"></a><strong id="b84235270617114_2"><a name="b84235270617114_2"></a><a name="b84235270617114_2"></a>Example Value</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row5818398995544"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p1528265495544"><a name="p1528265495544"></a><a name="p1528265495544"></a>Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p2993546095544"><a name="p2993546095544"></a><a name="p2993546095544"></a>Name of the PTR record</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p1150727695544"><a name="p1150727695544"></a><a name="p1150727695544"></a>10.1.168</p>
        <p id="p3645662495544"><a name="p3645662495544"></a><a name="p3645662495544"></a>For example, if the IP address is <strong id="b842352706145136"><a name="b842352706145136"></a><a name="b842352706145136"></a>192.168.1.10</strong>, the name of the PTR record is&nbsp;<strong id="b84235270615344"><a name="b84235270615344"></a><a name="b84235270615344"></a>10.1.168.192.in-addr.arpa</strong>.</p>
        <a name="ul772510438411"></a><a name="ul772510438411"></a><ul id="ul772510438411"><li id="li16725124312418"><a name="li16725124312418"></a><a name="li16725124312418"></a>If the private zone name is <strong id="b84235270615732"><a name="b84235270615732"></a><a name="b84235270615732"></a>192.in-addr.arpa</strong>, enter&nbsp;<strong id="b84235270615827"><a name="b84235270615827"></a><a name="b84235270615827"></a>10.1.168</strong> in the box.</li><li id="li16272201077"><a name="li16272201077"></a><a name="li16272201077"></a>If the private zone name is <strong id="b84235270615732_1"><a name="b84235270615732_1"></a><a name="b84235270615732_1"></a>1.168.192.in-addr.arpa</strong>, enter&nbsp;<strong id="b84235270615827_1"><a name="b84235270615827_1"></a><a name="b84235270615827_1"></a>10</strong> in the box.</li></ul>
        </td>
        </tr>
        <tr id="row5967416095544"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p176882195544"><a name="p176882195544"></a><a name="p176882195544"></a>Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p905683595544"><a name="p905683595544"></a><a name="p905683595544"></a>Type of the record</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p6251500995544"><a name="p6251500995544"></a><a name="p6251500995544"></a></p>
        <p id="p10646172511818"><a name="p10646172511818"></a><a name="p10646172511818"></a>PTR – Map IP addresses to domains</p>
        </td>
        </tr>
        <tr id="row2576416995544"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p652296395544"><a name="p652296395544"></a><a name="p652296395544"></a>TTL (s)</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p5859798595544"><a name="p5859798595544"></a><a name="p5859798595544"></a>Caching period of the record set (in seconds)</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p4881634895544"><a name="p4881634895544"></a><a name="p4881634895544"></a>The default value is 300s, that is, <strong id="b842352706183837_8"><a name="b842352706183837_8"></a><a name="b842352706183837_8"></a>5 min</strong>.</p>
        </td>
        </tr>
        <tr id="row3669394995544"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p1941991095544"><a name="p1941991095544"></a><a name="p1941991095544"></a>Value</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p2950884795544"><a name="p2950884795544"></a><a name="p2950884795544"></a>Domain name mapped to the host name</p>
        <p id="p21053573102030"><a name="p21053573102030"></a><a name="p21053573102030"></a>You can enter only one name at a time.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p4833148395544"><a name="p4833148395544"></a><a name="p4833148395544"></a>host.example.com.</p>
        </td>
        </tr>
        <tr id="row257814332309"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p125271425301"><a name="p125271425301"></a><a name="p125271425301"></a>Tag</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p85331642133013"><a name="p85331642133013"></a><a name="p85331642133013"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a record set.</p>
        <p id="p1353994283013"><a name="p1353994283013"></a><a name="p1353994283013"></a>For details about tag key and value requirements, see <a href="#en-us_topic_0035467703__table26050509163">Table 2</a>.</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p165498428308"><a name="p165498428308"></a><a name="p165498428308"></a>example_key1</p>
        <p id="p14553184210305"><a name="p14553184210305"></a><a name="p14553184210305"></a>example_value1</p>
        </td>
        </tr>
        <tr id="row3233016395544"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p149754295544"><a name="p149754295544"></a><a name="p149754295544"></a>Description</p>
        </td>
        <td class="cellrowborder" valign="top" width="47.81%" headers="mcps1.2.4.1.2 "><p id="p17364672101947"><a name="p17364672101947"></a><a name="p17364672101947"></a>(Optional) Description of the PTR record</p>
        </td>
        <td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p2748282695544"><a name="p2748282695544"></a><a name="p2748282695544"></a>The description of PTR record.</p>
        </td>
        </tr>
        </tbody>
        </table>


## Modifying a Record Set<a name="section2233355694352"></a>

If you find that the original configuration of a record set does not meet your service requirements, you can adjust its TTL, value, and description as needed.

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  On the **Dashboard** page, click **Public Zones** or **Private Zones** under **My Resources**.

    The zone list is displayed.

4.  \(Optional\) If you have selected **Private Zones**, click ![](figures/en-us_image_0079623919.png) on the upper left to select the region and project.
5.  Click a zone name.

    The record set page is displayed.

6.  Locate the record set to be modified and click **Modify** under **Operation**.

    The **Modify Record Set** page is displayed.

7.  Change the TTL, value, and description of the record set as required.
8.  Click **OK** to save the change.

## Deleting a Record Set<a name="section6770436102428"></a>

A record set can be deleted if it is not required. After the record set is deleted, the function of this type of record set will become invalid. For example, if a record set of the A type is deleted, the specified domain name cannot be resolved into an IPv4 address. If a record set of the CNAME type is deleted, the domain alias cannot be mapped to the specified domain name.

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  On the **Dashboard** page, click **Public Zones** or **Private Zones** under **My Resources**.

    The zone list is displayed.

4.  \(Optional\) If you have selected **Private Zones**, click ![](figures/en-us_image_0079592430.png) on the upper left to select the region and project.
5.  Click a zone name.

    The record set page is displayed.

6.  Locate the record set to be deleted and click **Delete** under **Operation**.
7.  Click **OK**.

