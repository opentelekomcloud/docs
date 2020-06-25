# Creating a PTR Record<a name="en-us_topic_0040322596"></a>

## **Scenarios**<a name="section788725015149"></a>

PTR records are used to prove the credibility of IP addresses and domain names of email servers. Most spam senders use email servers whose IP addresses are dynamically allocated or not mapped to registered domain names to avoid being tracked. If you do not want emails sent from your email server to be considered as spam, you need to add a PTR record to map the email server IP address to a domain name. In this way, the email recipient can obtain the domain name by IP address and will know that the email server is trustworthy.

By creating a PTR record, you can map an EIP of another cloud service, for example, ECS, to a domain name.

>![](/images/icon-note.gif) **NOTE:**   
>After an ECS is successfully created and assigned with an EIP, a PTR record will be generated for the EIP by default in format of  **ecs-xx-xx-xx-xx.compute.xxx.com**, where  **xx-xx-xx-xx**  is the EIP and  **xxx**  the domain name provided by the cloud platform.  
>You can use one of the following methods to query the default PTR record of an EIP:  
>-   ping -a  _EIP_  
>-   nslookup \[-qt=ptr\]  _EIP_  
>-   dig -x  _EIP_  
>The default PTR record of the EIP may not be applicable in some scenarios. For example, it cannot be used as the domain name of an email server. In this case, you need to create a new PTR record for the EIP.  
>After you create a new PTR record, the default record will be overwritten.  

This section describes how to create a PTR record for reverse domain name resolution.

## Restrictions and Limitations<a name="section66901242223741"></a>

Currently, you can configure a PTR record only for IP addresses with a 32-bit subnet mask.

## **Procedure**<a name="section6593003511349"></a>

1.  Log in to the management console.
2.  In the  **Network**  category, click  **Domain Name Service**.

    The DNS console is displayed.

3.  In the navigation pane, choose  **PTR Records**.

    The  **PTR Records**  page is displayed.

4.  Click  ![](figures/icon-region.png)  on the upper left and select the desired region and project.
5.  Click  **Create PTR Record**.

    **Figure  1**  Create PTR Record<a name="fig1279516245216"></a>  
    ![](figures/create-ptr-record.png "create-ptr-record")

6.  Configure the parameters according to  [Table 1](#en-us_topic_0035467699_table2052132816642).

    **Table  1**  Parameters required for creating a PTR record

    <a name="en-us_topic_0035467699_table2052132816642"></a>
    <table><thead align="left"><tr id="en-us_topic_0035467699_row5957484916642"><th class="cellrowborder" valign="top" width="19.99%" id="mcps1.2.4.1.1"><p id="en-us_topic_0035467699_p1063011916642"><a name="en-us_topic_0035467699_p1063011916642"></a><a name="en-us_topic_0035467699_p1063011916642"></a><strong id="b84235270695255"><a name="b84235270695255"></a><a name="b84235270695255"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.75%" id="mcps1.2.4.1.2"><p id="en-us_topic_0035467699_p5573330716642"><a name="en-us_topic_0035467699_p5573330716642"></a><a name="en-us_topic_0035467699_p5573330716642"></a><strong id="en-us_topic_0035268497_b8423527061433"><a name="en-us_topic_0035268497_b8423527061433"></a><a name="en-us_topic_0035268497_b8423527061433"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.259999999999998%" id="mcps1.2.4.1.3"><p id="en-us_topic_0035467699_p1810404816642"><a name="en-us_topic_0035467699_p1810404816642"></a><a name="en-us_topic_0035467699_p1810404816642"></a><strong id="b84235270617114"><a name="b84235270617114"></a><a name="b84235270617114"></a>Example Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0035467699_row2871871016642"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_p4451420716642"><a name="en-us_topic_0035467699_p4451420716642"></a><a name="en-us_topic_0035467699_p4451420716642"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.75%" headers="mcps1.2.4.1.2 "><p id="p19766855214631"><a name="p19766855214631"></a><a name="p19766855214631"></a>EIP obtained from another cloud service (for example, ECS)</p>
    <p id="p2086314992410"><a name="p2086314992410"></a><a name="p2086314992410"></a>You can select an EIP from the drop-down list.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_p6704856616642"><a name="en-us_topic_0035467699_p6704856616642"></a><a name="en-us_topic_0035467699_p6704856616642"></a>XX.XX.XX.XX</p>
    </td>
    </tr>
    <tr id="en-us_topic_0035467699_row6656618516642"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_p2315189616642"><a name="en-us_topic_0035467699_p2315189616642"></a><a name="en-us_topic_0035467699_p2315189616642"></a>Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.75%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467699_p4185944320320"><a name="en-us_topic_0035467699_p4185944320320"></a><a name="en-us_topic_0035467699_p4185944320320"></a>Domain name mapped to the EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_p3223566516642"><a name="en-us_topic_0035467699_p3223566516642"></a><a name="en-us_topic_0035467699_p3223566516642"></a>www.example.com</p>
    </td>
    </tr>
    <tr id="en-us_topic_0035467699_row2168553016642"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_p1169746616642"><a name="en-us_topic_0035467699_p1169746616642"></a><a name="en-us_topic_0035467699_p1169746616642"></a>TTL (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.75%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0035467699_p12484891202715"><a name="en-us_topic_0035467699_p12484891202715"></a><a name="en-us_topic_0035467699_p12484891202715"></a>Caching period of the PTR record (in seconds)</p>
    <p id="p57181144162444"><a name="p57181144162444"></a><a name="p57181144162444"></a>The default value is 300s, that is, <strong id="b842352706183837"><a name="b842352706183837"></a><a name="b842352706183837"></a>5 min</strong>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_p4164391116642"><a name="en-us_topic_0035467699_p4164391116642"></a><a name="en-us_topic_0035467699_p4164391116642"></a>300</p>
    </td>
    </tr>
    <tr id="row273617193297"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="p5738419102911"><a name="p5738419102911"></a><a name="p5738419102911"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.75%" headers="mcps1.2.4.1.2 "><p id="p640091716224"><a name="p640091716224"></a><a name="p640091716224"></a>(Optional) Identifier of a resource. Each tag contains a key and a value. You can add 10 tags at most to a PTR record.</p>
    <p id="p8401121711229"><a name="p8401121711229"></a><a name="p8401121711229"></a>For details about tag key and value requirements, see <a href="#table1393932617253">Table 2</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="p94761455155619"><a name="p94761455155619"></a><a name="p94761455155619"></a>example_key1</p>
    <p id="p165896220231"><a name="p165896220231"></a><a name="p165896220231"></a>example_value1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0035467699_row3925088716642"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_p2520529816642"><a name="en-us_topic_0035467699_p2520529816642"></a><a name="en-us_topic_0035467699_p2520529816642"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.75%" headers="mcps1.2.4.1.2 "><p id="p2953836818442"><a name="p2953836818442"></a><a name="p2953836818442"></a>(Optional) Description of the PTR record</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.259999999999998%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_p1572349716642"><a name="en-us_topic_0035467699_p1572349716642"></a><a name="en-us_topic_0035467699_p1572349716642"></a>The PTR record is for reverse resolution.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Tag key and value requirements

    <a name="table1393932617253"></a>
    <table><thead align="left"><tr id="en-us_topic_0035467699_row72901535141713"><th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.1"><p id="en-us_topic_0035467699_p132908358173"><a name="en-us_topic_0035467699_p132908358173"></a><a name="en-us_topic_0035467699_p132908358173"></a><strong id="en-us_topic_0035467699_b8423527069525"><a name="en-us_topic_0035467699_b8423527069525"></a><a name="en-us_topic_0035467699_b8423527069525"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.51%" id="mcps1.2.4.1.2"><p id="en-us_topic_0035467699_p1629093517175"><a name="en-us_topic_0035467699_p1629093517175"></a><a name="en-us_topic_0035467699_p1629093517175"></a><strong id="en-us_topic_0035467699_b842352706171418"><a name="en-us_topic_0035467699_b842352706171418"></a><a name="en-us_topic_0035467699_b842352706171418"></a>Requirement</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.31%" id="mcps1.2.4.1.3"><p id="en-us_topic_0035467699_p32901635141714"><a name="en-us_topic_0035467699_p32901635141714"></a><a name="en-us_topic_0035467699_p32901635141714"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0035467699_row52906354176"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_p122901235111715"><a name="en-us_topic_0035467699_p122901235111715"></a><a name="en-us_topic_0035467699_p122901235111715"></a>Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0035467699_ul46253231183"></a><a name="en-us_topic_0035467699_ul46253231183"></a><ul id="en-us_topic_0035467699_ul46253231183"><li>Cannot be left blank.</li><li>Must be unique for each resource.</li><li>Consists of at most 36 characters.</li><li>Contains only letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="31.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_p12290163511720"><a name="en-us_topic_0035467699_p12290163511720"></a><a name="en-us_topic_0035467699_p12290163511720"></a>example_key1</p>
    </td>
    </tr>
    <tr id="en-us_topic_0035467699_row132900355172"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0035467699_p152901635181712"><a name="en-us_topic_0035467699_p152901635181712"></a><a name="en-us_topic_0035467699_p152901635181712"></a>Value</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.2.4.1.2 "><a name="en-us_topic_0035467699_ul19648123161815"></a><a name="en-us_topic_0035467699_ul19648123161815"></a><ul id="en-us_topic_0035467699_ul19648123161815"><li>Cannot be left blank.</li><li>Consists of at most 43 characters.</li><li>Contains only letters, digits, hyphens (-), and underscores (_).</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="31.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0035467699_p62904352179"><a name="en-us_topic_0035467699_p62904352179"></a><a name="en-us_topic_0035467699_p62904352179"></a>example_value1</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

    You can query information about the PTR record you created on the  **PTR Records**  page.

    **Figure  2**  PTR Records<a name="fig2608187413419"></a>  
    ![](figures/ptr-records.png "ptr-records")

    >![](/images/icon-note.gif) **NOTE:**   
    >If the domain name, for example, example.com, is mapped to multiple EIPs, you need to create a PTR record for each EIP.  


