# Creating a VPC Peering Connection with a VPC in Another Account<a name="en-us_topic_0046655038"></a>

## Scenarios<a name="s824032c0a83f4a57ad1a297330c193a8"></a>

The VPC service also allows you to create a VPC peering connection with a VPC in another account. The two VPCs must be in the same region. If you request a VPC peering connection with a VPC in another account in the same region, the owner of the peer account must accept the request to activate the connection.

## Creating a VPC Peering Connection<a name="section14616192294815"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, click  **VPC Peering**.
5.  In the right pane displayed, click  **Create VPC Peering Connection**.
6.  Configure parameters as prompted. You must select  **Another account**  for  **Account**.

    **Figure  1**  Create VPC Peering Connection<a name="fig10423142382612"></a>  
    ![](figures/create-vpc-peering-connection-5.png "create-vpc-peering-connection-5")

    **Table  1**  Parameter description

    <a name="table13425162318260"></a>
    <table><thead align="left"><tr id="row154231823162613"><th class="cellrowborder" valign="top" width="21.482148214821482%" id="mcps1.2.4.1.1"><p id="p1423182315268"><a name="p1423182315268"></a><a name="p1423182315268"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.18451845184518%" id="mcps1.2.4.1.2"><p id="p17423162317261"><a name="p17423162317261"></a><a name="p17423162317261"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p16423162320263"><a name="p16423162320263"></a><a name="p16423162320263"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64247230268"><td class="cellrowborder" valign="top" width="21.482148214821482%" headers="mcps1.2.4.1.1 "><p id="p11423623162616"><a name="p11423623162616"></a><a name="p11423623162616"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.18451845184518%" headers="mcps1.2.4.1.2 "><p id="p7423323132614"><a name="p7423323132614"></a><a name="p7423323132614"></a>Specifies the name of the VPC peering connection.</p>
    <p id="p642313233262"><a name="p642313233262"></a><a name="p642313233262"></a>The name contains a maximum of 64 characters, which consist of letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p84248236269"><a name="p84248236269"></a><a name="p84248236269"></a>peering-001</p>
    </td>
    </tr>
    <tr id="row84241823122615"><td class="cellrowborder" valign="top" width="21.482148214821482%" headers="mcps1.2.4.1.1 "><p id="p8424172362618"><a name="p8424172362618"></a><a name="p8424172362618"></a>Local VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.18451845184518%" headers="mcps1.2.4.1.2 "><p id="p44244232264"><a name="p44244232264"></a><a name="p44244232264"></a>Specifies the local VPC. You can select one from the drop-down list.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p12424192312616"><a name="p12424192312616"></a><a name="p12424192312616"></a>vpc_002</p>
    </td>
    </tr>
    <tr id="row1942432332613"><td class="cellrowborder" valign="top" width="21.482148214821482%" headers="mcps1.2.4.1.1 "><p id="p194241823202610"><a name="p194241823202610"></a><a name="p194241823202610"></a>Account</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.18451845184518%" headers="mcps1.2.4.1.2 "><p id="p6424112332615"><a name="p6424112332615"></a><a name="p6424112332615"></a>Specifies the account to which the VPC to peer with belongs.</p>
    <a name="ul1542462322614"></a><a name="ul1542462322614"></a><ul id="ul1542462322614"><li><strong id="b17610165611213"><a name="b17610165611213"></a><a name="b17610165611213"></a>My account</strong>: The VPC peering connection will be created between two VPCs, in the same region, in your account.</li><li><strong id="b15925111118224"><a name="b15925111118224"></a><a name="b15925111118224"></a>Another account</strong>: The VPC peering connection will be created between your VPC and a VPC in another account, in the same region.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p8424152322615"><a name="p8424152322615"></a><a name="p8424152322615"></a>Another account</p>
    </td>
    </tr>
    <tr id="row3424202312612"><td class="cellrowborder" valign="top" width="21.482148214821482%" headers="mcps1.2.4.1.1 "><p id="p16424112342616"><a name="p16424112342616"></a><a name="p16424112342616"></a>Peer Project ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.18451845184518%" headers="mcps1.2.4.1.2 "><p id="p144241323122613"><a name="p144241323122613"></a><a name="p144241323122613"></a>This parameter is available only when <strong id="b842352706191927"><a name="b842352706191927"></a><a name="b842352706191927"></a>Another account</strong> is selected.</p>
    <p id="p1842422342610"><a name="p1842422342610"></a><a name="p1842422342610"></a>For details about how to obtain the peer project ID, see <a href="#section41291933224121">Obtaining the Peer Project ID</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p17424182362613"><a name="p17424182362613"></a><a name="p17424182362613"></a>N/A</p>
    </td>
    </tr>
    <tr id="row10425192313261"><td class="cellrowborder" valign="top" width="21.482148214821482%" headers="mcps1.2.4.1.1 "><p id="p16424423102613"><a name="p16424423102613"></a><a name="p16424423102613"></a>Peer VPC ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.18451845184518%" headers="mcps1.2.4.1.2 "><p id="p144254233264"><a name="p144254233264"></a><a name="p144254233264"></a>This parameter is available only when <strong id="b447721302313"><a name="b447721302313"></a><a name="b447721302313"></a>Another account</strong> is selected.</p>
    <p id="p4425102372618"><a name="p4425102372618"></a><a name="p4425102372618"></a>For details about how to obtain the peer VPC ID, see <a href="#section19734314164713">Obtaining the Peer VPC ID</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p18425123162615"><a name="p18425123162615"></a><a name="p18425123162615"></a>65d062b3-40fa-4204-8181-3538f527d2ab</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

## Accepting a VPC Peering Connection Request<a name="section497322311429"></a>

To request a VPC peering connection with a VPC in another account, the owner of the peer account must accept the request to activate the connection.

1.  The owner of the peer account logs in to the management console.
2.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
3.  In the navigation pane on the left, click  **VPC Peering**.
4.  Locate the row that contains the target VPC peering connection in the connection list, and click  **Accept Request**  in the  **Operation**  column.

    **Figure  2**  VPC peering connection list<a name="fig16224165117555"></a>  
    ![](figures/vpc-peering-connection-list-6.png "vpc-peering-connection-list-6")

5.  Click  **Yes**  in the displayed dialog box.

## Refusing a VPC Peering Connection<a name="section1152263810435"></a>

The owner of the peer account can reject any VPC peering connection request that they receive. If a VPC peering connection request is rejected, the connection will not be established. You must delete the rejected VPC peering connection request before creating a VPC peering connection between the same VPCs as those in the rejected request.

1.  The owner of the peer account logs in to the management console.
2.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
3.  In the navigation pane on the left, click  **VPC Peering**.
4.  Locate the row that contains the target VPC peering connection in the connection list, and click  **Reject Request**  in the  **Operation**  column.
5.  Click  **Yes**  in the displayed dialog box.

## Adding Routes for a VPC Peering Connection <a name="section2772659154320"></a>

If you request a VPC peering connection with a VPC in another account, the owner of the peer account must accept the request. To enable communication between the two VPCs, you need to add routes for the VPC peering connection. The owner of the local account can add only the local route because the owner does not have the required permission to perform operations on the peer VPC. The owner of the peer account must add the peer route. The procedure for adding a local route and a peer route is the same.

1.  Log in to the management console.
2.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
3.  In the navigation pane on the left, click  **VPC Peering**.
4.  Locate the target VPC peering connection in the connection list.
5.  Click the name of the VPC peering connection to switch to the page showing details about the connection.
6.  On the displayed page, click the  **Local Routes**  tab.
7.  In the displayed  **Local Routes**  area, click  **Add Local Route**. In the displayed dialog box, add a local route.  [Table 2](#en-us_topic_0118498960_table1626072032518)  lists the parameters to be configured.

    **Figure  3**  Add Local Route<a name="en-us_topic_0118498960_fig125922016257"></a>  
    ![](figures/add-local-route-7.png "add-local-route-7")

    **Table  2**  Route parameter description

    <a name="en-us_topic_0118498960_table1626072032518"></a>
    <table><thead align="left"><tr id="en-us_topic_0118498960_row1260520192515"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0118498960_p192601220202510"><a name="en-us_topic_0118498960_p192601220202510"></a><a name="en-us_topic_0118498960_p192601220202510"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0118498960_p16260202012252"><a name="en-us_topic_0118498960_p16260202012252"></a><a name="en-us_topic_0118498960_p16260202012252"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0118498960_p142601420172518"><a name="en-us_topic_0118498960_p142601420172518"></a><a name="en-us_topic_0118498960_p142601420172518"></a>Example Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0118498960_row92601620142520"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118498960_p2026032017259"><a name="en-us_topic_0118498960_p2026032017259"></a><a name="en-us_topic_0118498960_p2026032017259"></a>Destination</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118498960_p1226011201251"><a name="en-us_topic_0118498960_p1226011201251"></a><a name="en-us_topic_0118498960_p1226011201251"></a>Specifies the destination address. Set it to the peer VPC or subnet CIDR block. </p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118498960_p3260172012258"><a name="en-us_topic_0118498960_p3260172012258"></a><a name="en-us_topic_0118498960_p3260172012258"></a>192.168.2.0/24</p>
    </td>
    </tr>
    <tr id="en-us_topic_0118498960_row19260102012518"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0118498960_p126012092511"><a name="en-us_topic_0118498960_p126012092511"></a><a name="en-us_topic_0118498960_p126012092511"></a>Next Hop</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0118498960_p4260220142514"><a name="en-us_topic_0118498960_p4260220142514"></a><a name="en-us_topic_0118498960_p4260220142514"></a>Specifies the next hop address. The default value is the VPC peering connection ID. Keep the default value.</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0118498960_p1260112010256"><a name="en-us_topic_0118498960_p1260112010256"></a><a name="en-us_topic_0118498960_p1260112010256"></a>d1a7863b-9d5e-4d27-8eaf-ab14d2a9148b</p>
    </td>
    </tr>
    </tbody>
    </table>

8.  Click  **OK**.

    The routes are added for the VPC peering connection.


After a VPC peering connection is created, the two VPCs can communicate with each other through private IP addresses. You can run the  **ping**  command to check whether the two VPCs can communicate with each other. 

If two VPCs cannot communicate with each other, check the configuration by following the instructions provided in  [What Can I Do If VPCs in a VPC Peering Connection Cannot Communicate with Each Other?](what-can-i-do-if-vpcs-in-a-vpc-peering-connection-cannot-communicate-with-each-other.md).

## Obtaining the Peer Project ID<a name="section41291933224121"></a>

1.  The owner of the peer account logs in to the management console.
2.  Select  **My Credentials**  from the username drop-down list.
3.  On the  **Project List**  tab, obtain the required project ID.

## Obtaining the Peer VPC ID<a name="section19734314164713"></a>

1.  The owner of the peer account logs in to the management console.
2.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
3.  In the navigation pane on the left, click  **Virtual Private Cloud**.
4.  Click the target VPC name and view VPC ID on the VPC details page.

