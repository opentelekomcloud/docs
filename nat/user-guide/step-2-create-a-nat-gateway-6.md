# Step 2: Create a NAT Gateway<a name="nat_qs_0016"></a>

## Scenarios<a name="nat_qs_0003_section141051954102215"></a>

This section guides you on how to create a NAT gateway to enable your servers to access the Internet or to provide services for external networks.

## **Prerequisites**<a name="nat_qs_0003_section1825861973713"></a>

-   When creating a NAT gateway, you must specify its VPC, subnet, and type.
-   Ensure that the VPC does not have a default route.

## Procedure<a name="nat_qs_0003_section82633199366"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Network**, click  **NAT Gateway**.
4.  On the displayed page, click  **Create NAT Gateway**.

    **Figure  1**  Create NAT Gateway<a name="nat_qs_0003_fig1753371912428"></a>  
    ![](figures/create-nat-gateway.png "create-nat-gateway")

5.  Set the parameters as prompted. For details, see  [Table 1](#nat_qs_0003_table27487005195751).

    **Table  1**  Parameter description

    <a name="nat_qs_0003_table27487005195751"></a>
    <table><thead align="left"><tr id="nat_qs_0003_row9940336195751"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="nat_qs_0003_p5995559819588"><a name="nat_qs_0003_p5995559819588"></a><a name="nat_qs_0003_p5995559819588"></a><strong id="nat_qs_0003_b24725868162658"><a name="nat_qs_0003_b24725868162658"></a><a name="nat_qs_0003_b24725868162658"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="nat_qs_0003_p2456526519588"><a name="nat_qs_0003_p2456526519588"></a><a name="nat_qs_0003_p2456526519588"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="nat_qs_0003_row11053428162048"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="nat_qs_0003_p22912486162048"><a name="nat_qs_0003_p22912486162048"></a><a name="nat_qs_0003_p22912486162048"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="nat_qs_0003_p43972101162048"><a name="nat_qs_0003_p43972101162048"></a><a name="nat_qs_0003_p43972101162048"></a>Specifies the region where the NAT gateway is located.</p>
    </td>
    </tr>
    <tr id="nat_qs_0003_row32613315195751"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="nat_qs_0003_p2832836319588"><a name="nat_qs_0003_p2832836319588"></a><a name="nat_qs_0003_p2832836319588"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="nat_qs_0003_p1289605119588"><a name="nat_qs_0003_p1289605119588"></a><a name="nat_qs_0003_p1289605119588"></a>Specifies the name of the NAT gateway. The value is a string of 1 to 64 characters consisting of digits, letters, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="nat_qs_0003_row27553870195751"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="nat_qs_0003_p1464780019588"><a name="nat_qs_0003_p1464780019588"></a><a name="nat_qs_0003_p1464780019588"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="nat_qs_0003_p4562116519588"><a name="nat_qs_0003_p4562116519588"></a><a name="nat_qs_0003_p4562116519588"></a>Specifies the VPC to which the NAT gateway belongs. You can select the VPC which is not used by other NAT gateways and has no default route. </p>
    </td>
    </tr>
    <tr id="nat_qs_0003_row47407746195751"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="nat_qs_0003_p17196519588"><a name="nat_qs_0003_p17196519588"></a><a name="nat_qs_0003_p17196519588"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="nat_qs_0003_p980412105420"><a name="nat_qs_0003_p980412105420"></a><a name="nat_qs_0003_p980412105420"></a>Specifies the VPC subnet to which the NAT gateway belongs.</p>
    <p id="nat_qs_0003_p1392917619588"><a name="nat_qs_0003_p1392917619588"></a><a name="nat_qs_0003_p1392917619588"></a>The subnet has at least one available IP address.</p>
    </td>
    </tr>
    <tr id="nat_qs_0003_row3011590195751"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="nat_qs_0003_p1770884719588"><a name="nat_qs_0003_p1770884719588"></a><a name="nat_qs_0003_p1770884719588"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="nat_qs_0003_p156313256519"><a name="nat_qs_0003_p156313256519"></a><a name="nat_qs_0003_p156313256519"></a>Specifies the type of the NAT gateway.</p>
    <p id="nat_qs_0003_p03201316191210"><a name="nat_qs_0003_p03201316191210"></a><a name="nat_qs_0003_p03201316191210"></a>The value can be <strong id="nat_qs_0003_b842352706152120"><a name="nat_qs_0003_b842352706152120"></a><a name="nat_qs_0003_b842352706152120"></a>Small</strong>, <strong id="nat_qs_0003_b842352706152124"><a name="nat_qs_0003_b842352706152124"></a><a name="nat_qs_0003_b842352706152124"></a>Medium</strong>, <strong id="nat_qs_0003_b842352706152128"><a name="nat_qs_0003_b842352706152128"></a><a name="nat_qs_0003_b842352706152128"></a>Large</strong>, and <strong id="nat_qs_0003_b842352706152132"><a name="nat_qs_0003_b842352706152132"></a><a name="nat_qs_0003_b842352706152132"></a>Extra-large</strong>. You can click <strong id="nat_qs_0003_b842352706152252"><a name="nat_qs_0003_b842352706152252"></a><a name="nat_qs_0003_b842352706152252"></a>Learn more</strong> on the page to view details about each type.</p>
    </td>
    </tr>
    <tr id="nat_qs_0003_row2219225792544"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="nat_qs_0003_p5274235692544"><a name="nat_qs_0003_p5274235692544"></a><a name="nat_qs_0003_p5274235692544"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="nat_qs_0003_p4427248192544"><a name="nat_qs_0003_p4427248192544"></a><a name="nat_qs_0003_p4427248192544"></a>Provides supplementary information about the NAT gateway. The description can contain a maximum of 255 characters.</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **Create Now**. The page for you to confirm the NAT gateway specifications is displayed.
7.  If you do not need to modify the information, click  **Submit**.

    It takes 1 to 5 minutes to create a NAT gateway.

8.  On the  **NAT Gateway**  homepage, check the NAT gateway status. For details about the NAT gateway status, see  [Table 2](#nat_qs_0003_table1213025114317).

    **Table  2**  NAT gateway status

    <a name="nat_qs_0003_table1213025114317"></a>
    <table><thead align="left"><tr id="nat_qs_0003_row9131125119310"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="nat_qs_0003_p41311951532"><a name="nat_qs_0003_p41311951532"></a><a name="nat_qs_0003_p41311951532"></a><strong id="nat_qs_0003_b8423527062072"><a name="nat_qs_0003_b8423527062072"></a><a name="nat_qs_0003_b8423527062072"></a>Status</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="nat_qs_0003_p313185110315"><a name="nat_qs_0003_p313185110315"></a><a name="nat_qs_0003_p313185110315"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="nat_qs_0003_row1713115114315"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="nat_qs_0003_p41311351433"><a name="nat_qs_0003_p41311351433"></a><a name="nat_qs_0003_p41311351433"></a>Running</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="nat_qs_0003_p1513185113314"><a name="nat_qs_0003_p1513185113314"></a><a name="nat_qs_0003_p1513185113314"></a>The resource is normal.</p>
    </td>
    </tr>
    <tr id="nat_qs_0003_row1013115115314"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="nat_qs_0003_p613155112317"><a name="nat_qs_0003_p613155112317"></a><a name="nat_qs_0003_p613155112317"></a>Creating</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="nat_qs_0003_p1713175110310"><a name="nat_qs_0003_p1713175110310"></a><a name="nat_qs_0003_p1713175110310"></a>The resource is being created.</p>
    </td>
    </tr>
    <tr id="nat_qs_0003_row101312514318"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="nat_qs_0003_p5131165115319"><a name="nat_qs_0003_p5131165115319"></a><a name="nat_qs_0003_p5131165115319"></a>Updating</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="nat_qs_0003_p6131951338"><a name="nat_qs_0003_p6131951338"></a><a name="nat_qs_0003_p6131951338"></a>The resource is being updated.</p>
    </td>
    </tr>
    <tr id="nat_qs_0003_row1913115514318"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="nat_qs_0003_p666512504613"><a name="nat_qs_0003_p666512504613"></a><a name="nat_qs_0003_p666512504613"></a>Deleting</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="nat_qs_0003_p3131351739"><a name="nat_qs_0003_p3131351739"></a><a name="nat_qs_0003_p3131351739"></a>The resource is being deleted.</p>
    </td>
    </tr>
    <tr id="nat_qs_0003_row1613155110316"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="nat_qs_0003_p1813155111316"><a name="nat_qs_0003_p1813155111316"></a><a name="nat_qs_0003_p1813155111316"></a>Frozen</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="nat_qs_0003_p8131105111315"><a name="nat_qs_0003_p8131105111315"></a><a name="nat_qs_0003_p8131105111315"></a>The resource has been frozen.</p>
    </td>
    </tr>
    <tr id="nat_qs_0003_row101318515313"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="nat_qs_0003_p384018216717"><a name="nat_qs_0003_p384018216717"></a><a name="nat_qs_0003_p384018216717"></a>Abnormal</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="nat_qs_0003_p213110511539"><a name="nat_qs_0003_p213110511539"></a><a name="nat_qs_0003_p213110511539"></a>The resource is abnormal.</p>
    </td>
    </tr>
    </tbody>
    </table>


