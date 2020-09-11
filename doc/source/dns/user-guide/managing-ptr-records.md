# Managing PTR Records<a name="en-us_topic_0077500015"></a>

> ![](/images/icon-note.gif) **NOTE:** 

> The ap-sg region does not support PTR records.

## Viewing Details About a PTR Record<a name="section6318733510236"></a>

You can query information about the PTR record you created on the **PTR Records** page.

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  Choose **Dashboard** and click **PTR Records** under **My Resources**.
4.  In the PTR record list, check the record details.

## Creating a PTR Record<a name="section52845971102319"></a>

If you have assigned a new EIP in your public cloud services \(for example, ECS\), you can create a PTR record for the EIP.

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, choose **PTR Records**.

    The **PTR Records** page is displayed.

4.  Click **Create PTR Record**.

    **Figure 1** Create PTR Record<a name="en-us_topic_0040322596_fig1279516245216"></a>
    ![](figures/create-ptr-record.png "Create PTR Record")

5.  Configure the parameters according to [Table 1](#en-us_topic_0040322596_en-us_topic_0035467699_table2052132816642).**Table 1** Parameters required for creating a PTR record

    <a name="en-us_topic_0040322596_en-us_topic_0035467699_table2052132816642"></a><table><thead align="left"><tr id="en-us_topic_0040322596_en-us_topic_0035467699_row5957484916642"><th class="cellrowborder" valign="top" width="19.99%" id="mcps1.2.4.1.1"><p id="en-us_topic_0040322596_en-us_topic_0035467699_p1063011916642"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p1063011916642"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p1063011916642"></a><strong id="en-us_topic_0040322596_b84235270695255"><a name="en-us_topic_0040322596_b84235270695255"></a><a name="en-us_topic_0040322596_b84235270695255"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.75%" id="mcps1.2.4.1.2"><p id="en-us_topic_0040322596_en-us_topic_0035467699_p5573330716642"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p5573330716642"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p5573330716642"></a><strong id="en-us_topic_0040322596_en-us_topic_0035268497_b8423527061433"><a name="en-us_topic_0040322596_en-us_topic_0035268497_b8423527061433"></a><a name="en-us_topic_0040322596_en-us_topic_0035268497_b8423527061433"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.259999999999998%" id="mcps1.2.4.1.3"><p id="en-us_topic_0040322596_en-us_topic_0035467699_p1810404816642"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p1810404816642"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p1810404816642"></a><strong id="en-us_topic_0040322596_b84235270617114"><a name="en-us_topic_0040322596_b84235270617114"></a><a name="en-us_topic_0040322596_b84235270617114"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0040322596_en-us_topic_0035467699_row2871871016642"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0040322596_en-us_topic_0035467699_p4451420716642"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p4451420716642"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p4451420716642"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.75%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0040322596_p19766855214631"><a name="en-us_topic_0040322596_p19766855214631"></a><a name="en-us_topic_0040322596_p19766855214631"></a>EIP obtained from another cloud service (for example, ECS)</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0040322596_en-us_topic_0035467699_p6704856616642"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p6704856616642"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p6704856616642"></a>XX.XX.XX.XX</p>
    </td>
    </tr>
    <tr id="en-us_topic_0040322596_en-us_topic_0035467699_row6656618516642"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0040322596_en-us_topic_0035467699_p2315189616642"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p2315189616642"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p2315189616642"></a>Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.75%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0040322596_en-us_topic_0035467699_p4185944320320"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p4185944320320"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p4185944320320"></a>Domain name mapped to the EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0040322596_en-us_topic_0035467699_p3223566516642"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p3223566516642"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p3223566516642"></a>www.example.com</p>
    </td>
    </tr>
    <tr id="en-us_topic_0040322596_en-us_topic_0035467699_row2168553016642"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0040322596_en-us_topic_0035467699_p1169746616642"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p1169746616642"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p1169746616642"></a>TTL (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.75%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0040322596_en-us_topic_0035467699_p12484891202715"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p12484891202715"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p12484891202715"></a>Caching period of the PTR record (in seconds)</p>
    <p id="en-us_topic_0040322596_p57181144162444"><a name="en-us_topic_0040322596_p57181144162444"></a><a name="en-us_topic_0040322596_p57181144162444"></a>The default value is 300s, that is, <strong id="en-us_topic_0040322596_b842352706183837"><a name="en-us_topic_0040322596_b842352706183837"></a><a name="en-us_topic_0040322596_b842352706183837"></a>5 min</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0040322596_en-us_topic_0035467699_p4164391116642"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p4164391116642"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p4164391116642"></a>300</p>
    </td>
    </tr>
    <tr id="en-us_topic_0040322596_row273617193297"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0040322596_p5738419102911"><a name="en-us_topic_0040322596_p5738419102911"></a><a name="en-us_topic_0040322596_p5738419102911"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.75%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0040322596_p1839961732214"><a name="en-us_topic_0040322596_p1839961732214"></a><a name="en-us_topic_0040322596_p1839961732214"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a PTR record.</p>
    <p id="en-us_topic_0040322596_p8401121711229"><a name="en-us_topic_0040322596_p8401121711229"></a><a name="en-us_topic_0040322596_p8401121711229"></a>For details about tag key and value requirements, see <a href="#en-us_topic_0077500015__en-us_topic_0040322596_table1393932617253">Table 2</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0040322596_p94761455155619"><a name="en-us_topic_0040322596_p94761455155619"></a><a name="en-us_topic_0040322596_p94761455155619"></a>example_key1</p>
    <p id="en-us_topic_0040322596_p165896220231"><a name="en-us_topic_0040322596_p165896220231"></a><a name="en-us_topic_0040322596_p165896220231"></a>example_value1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0040322596_en-us_topic_0035467699_row3925088716642"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0040322596_en-us_topic_0035467699_p2520529816642"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p2520529816642"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p2520529816642"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.75%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0040322596_p2953836818442"><a name="en-us_topic_0040322596_p2953836818442"></a><a name="en-us_topic_0040322596_p2953836818442"></a>(Optional) Description of the PTR record</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0040322596_en-us_topic_0035467699_p1572349716642"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p1572349716642"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p1572349716642"></a>The PTR record is for reverse resolution.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table 2** Tag key and value requirements

    <a name="en-us_topic_0040322596_table1393932617253"></a><table><thead align="left"><tr id="en-us_topic_0040322596_en-us_topic_0035467699_row72901535141713"><th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.4.1.1"><p id="en-us_topic_0040322596_en-us_topic_0035467699_p132908358173"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p132908358173"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p132908358173"></a><strong id="en-us_topic_0040322596_en-us_topic_0035467699_b8423527069525"><a name="en-us_topic_0040322596_en-us_topic_0035467699_b8423527069525"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_b8423527069525"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.505050505050505%" id="mcps1.2.4.1.2"><p id="en-us_topic_0040322596_en-us_topic_0035467699_p1629093517175"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p1629093517175"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p1629093517175"></a><strong id="en-us_topic_0040322596_en-us_topic_0035467699_b842352706171418"><a name="en-us_topic_0040322596_en-us_topic_0035467699_b842352706171418"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_b842352706171418"></a>Requirement</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.313131313131315%" id="mcps1.2.4.1.3"><p id="en-us_topic_0040322596_en-us_topic_0035467699_p32901635141714"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p32901635141714"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p32901635141714"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0040322596_en-us_topic_0035467699_row52906354176"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0040322596_en-us_topic_0035467699_p122901235111715"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p122901235111715"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p122901235111715"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.505050505050505%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0040322596_en-us_topic_0035467699_ul46253231183"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_ul46253231183"></a><ul id="en-us_topic_0040322596_en-us_topic_0035467699_ul46253231183"><li id="en-us_topic_0040322596_en-us_topic_0035467699_li176251123141812"><a name="en-us_topic_0040322596_en-us_topic_0035467699_li176251123141812"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_li176251123141812"></a>Cannot be left blank.</li><li id="en-us_topic_0040322596_en-us_topic_0035467699_li86261923201810"><a name="en-us_topic_0040322596_en-us_topic_0035467699_li86261923201810"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_li86261923201810"></a>Must be unique for each resource.</li><li id="en-us_topic_0040322596_en-us_topic_0035467699_li162620231180"><a name="en-us_topic_0040322596_en-us_topic_0035467699_li162620231180"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_li162620231180"></a>Consists of at most 36 characters.</li><li id="en-us_topic_0040322596_en-us_topic_0035467699_li5389246102911"><a name="en-us_topic_0040322596_en-us_topic_0035467699_li5389246102911"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_li5389246102911"></a>Contains only letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="31.313131313131315%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0040322596_en-us_topic_0035467699_p12290163511720"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p12290163511720"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p12290163511720"></a>example_key1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0040322596_en-us_topic_0035467699_row132900355172"><td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0040322596_en-us_topic_0035467699_p152901635181712"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p152901635181712"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p152901635181712"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.505050505050505%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0040322596_en-us_topic_0035467699_ul19648123161815"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_ul19648123161815"></a><ul id="en-us_topic_0040322596_en-us_topic_0035467699_ul19648123161815"><li id="en-us_topic_0040322596_en-us_topic_0035467699_li15648193110182"><a name="en-us_topic_0040322596_en-us_topic_0035467699_li15648193110182"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_li15648193110182"></a>Cannot be left blank.</li><li id="en-us_topic_0040322596_en-us_topic_0035467699_li3648143181813"><a name="en-us_topic_0040322596_en-us_topic_0035467699_li3648143181813"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_li3648143181813"></a>Consists of at most 43 characters.</li><li id="en-us_topic_0040322596_en-us_topic_0035467699_li64561823123015"><a name="en-us_topic_0040322596_en-us_topic_0035467699_li64561823123015"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_li64561823123015"></a>Contains only letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="31.313131313131315%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0040322596_en-us_topic_0035467699_p62904352179"><a name="en-us_topic_0040322596_en-us_topic_0035467699_p62904352179"></a><a name="en-us_topic_0040322596_en-us_topic_0035467699_p62904352179"></a>example_value1</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click **OK**.

    You can query information about the PTR record you created on the **PTR Records** page.

    **Figure 2** PTR record<a name="en-us_topic_0040322596_fig2608187413419"></a>
    ![](figures/ptr-record.png "PTR record")

    > ![](/images/icon-note.gif) **NOTE:** 

    > If the domain name, for example, example.com, is mapped to multiple EIPs, you need to create a PTR record for each EIP.


## Modifying a PTR Record<a name="section32986191105210"></a>

If the domain name mapped to the EIP has changed or you want to change the TTL and description of a PTR record, you can modify the required PTR record.

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, choose **PTR Records**.

    The **PTR Records** page is displayed.

4.  Locate the PTR record to be modified and click **Modify** under **Operation**.

    The **Modify PTR Record** box is displayed.

5.  Change the domain name, TTL, or description as needed.
6.  Click **OK** to save the change.

## Deleting a PTR Record<a name="section34296412102339"></a>

You can delete a PTR record if it is needed any more. After the deletion, the domain name mapped to your EIP will change to the default.

1.  Log in to the management console.
2.  In the **Network** category, click **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, choose **PTR Records**.

    The **PTR Records** page is displayed.

4.  Locate the PTR record to be deleted and click **Delete** under **Operation**.
5.  Click **OK**.

