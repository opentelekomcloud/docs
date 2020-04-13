# Step 2: Create a NAT Gateway<a name="nat_qs_0003"></a>

## Scenarios<a name="section141051954102215"></a>

This section guides you on how to create a NAT gateway to enable your servers to access the Internet or to provide services for external networks.

## **Prerequisites**<a name="section1825861973713"></a>

-   When creating a NAT gateway, you must specify its VPC, subnet, and type.
-   Ensure that the VPC does not have a default route.

## Procedure<a name="section82633199366"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Network**, click  **NAT Gateway**.
4.  On the displayed page, click  **Create NAT Gateway**.

    **Figure  1**  Create NAT Gateway<a name="fig1753371912428"></a>  
    ![](figures/create-nat-gateway.png "create-nat-gateway")

5.  Set the parameters as prompted. For details, see  [Table 1](#table27487005195751).

    **Table  1**  Parameter description

    <a name="table27487005195751"></a>
    <table><thead align="left"><tr id="row9940336195751"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="p5995559819588"><a name="p5995559819588"></a><a name="p5995559819588"></a><strong id="b24725868162658"><a name="b24725868162658"></a><a name="b24725868162658"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="p2456526519588"><a name="p2456526519588"></a><a name="p2456526519588"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11053428162048"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p22912486162048"><a name="p22912486162048"></a><a name="p22912486162048"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p43972101162048"><a name="p43972101162048"></a><a name="p43972101162048"></a>Specifies the region where the NAT gateway is located.</p>
    </td>
    </tr>
    <tr id="row32613315195751"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p2832836319588"><a name="p2832836319588"></a><a name="p2832836319588"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p1289605119588"><a name="p1289605119588"></a><a name="p1289605119588"></a>Specifies the name of the NAT gateway. The value is a string of 1 to 64 characters consisting of digits, letters, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row27553870195751"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p1464780019588"><a name="p1464780019588"></a><a name="p1464780019588"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p4562116519588"><a name="p4562116519588"></a><a name="p4562116519588"></a>Specifies the VPC to which the NAT gateway belongs. You can select the VPC which is not used by other NAT gateways and has no default route. </p>
    </td>
    </tr>
    <tr id="row47407746195751"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p17196519588"><a name="p17196519588"></a><a name="p17196519588"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p980412105420"><a name="p980412105420"></a><a name="p980412105420"></a>Specifies the VPC subnet to which the NAT gateway belongs.</p>
    <p id="p1392917619588"><a name="p1392917619588"></a><a name="p1392917619588"></a>The subnet has at least one available IP address.</p>
    </td>
    </tr>
    <tr id="row3011590195751"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p1770884719588"><a name="p1770884719588"></a><a name="p1770884719588"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p156313256519"><a name="p156313256519"></a><a name="p156313256519"></a>Specifies the type of the NAT gateway.</p>
    <p id="p03201316191210"><a name="p03201316191210"></a><a name="p03201316191210"></a>The value can be <strong id="b842352706152120"><a name="b842352706152120"></a><a name="b842352706152120"></a>Small</strong>, <strong id="b842352706152124"><a name="b842352706152124"></a><a name="b842352706152124"></a>Medium</strong>, <strong id="b842352706152128"><a name="b842352706152128"></a><a name="b842352706152128"></a>Large</strong>, and <strong id="b842352706152132"><a name="b842352706152132"></a><a name="b842352706152132"></a>Extra-large</strong>. You can click <strong id="b842352706152252"><a name="b842352706152252"></a><a name="b842352706152252"></a>Learn more</strong> on the page to view details about each type.</p>
    </td>
    </tr>
    <tr id="row2219225792544"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p5274235692544"><a name="p5274235692544"></a><a name="p5274235692544"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p4427248192544"><a name="p4427248192544"></a><a name="p4427248192544"></a>Provides supplementary information about the NAT gateway. The description can contain a maximum of 255 characters.</p>
    </td>
    </tr>
    </tbody>
    </table>

6.  Click  **Create Now**. The page for you to confirm the NAT gateway specifications is displayed.
7.  If you do not need to modify the information, click  **Submit**.

    It takes 1 to 5 minutes to create a NAT gateway.

8.  On the  **NAT Gateway**  homepage, check the NAT gateway status. For details about the NAT gateway status, see  [Table 2](#table1213025114317).

    **Table  2**  NAT gateway status

    <a name="table1213025114317"></a>
    <table><thead align="left"><tr id="row9131125119310"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p41311951532"><a name="p41311951532"></a><a name="p41311951532"></a><strong id="b8423527062072"><a name="b8423527062072"></a><a name="b8423527062072"></a>Status</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p313185110315"><a name="p313185110315"></a><a name="p313185110315"></a><strong>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1713115114315"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p41311351433"><a name="p41311351433"></a><a name="p41311351433"></a>Running</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p1513185113314"><a name="p1513185113314"></a><a name="p1513185113314"></a>The resource is normal.</p>
    </td>
    </tr>
    <tr id="row1013115115314"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p613155112317"><a name="p613155112317"></a><a name="p613155112317"></a>Creating</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p1713175110310"><a name="p1713175110310"></a><a name="p1713175110310"></a>The resource is being created.</p>
    </td>
    </tr>
    <tr id="row101312514318"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p5131165115319"><a name="p5131165115319"></a><a name="p5131165115319"></a>Updating</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p6131951338"><a name="p6131951338"></a><a name="p6131951338"></a>The resource is being updated.</p>
    </td>
    </tr>
    <tr id="row1913115514318"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p666512504613"><a name="p666512504613"></a><a name="p666512504613"></a>Deleting</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p3131351739"><a name="p3131351739"></a><a name="p3131351739"></a>The resource is being deleted.</p>
    </td>
    </tr>
    <tr id="row1613155110316"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1813155111316"><a name="p1813155111316"></a><a name="p1813155111316"></a>Frozen</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p8131105111315"><a name="p8131105111315"></a><a name="p8131105111315"></a>The resource has been frozen.</p>
    </td>
    </tr>
    <tr id="row101318515313"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p384018216717"><a name="p384018216717"></a><a name="p384018216717"></a>Abnormal</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p213110511539"><a name="p213110511539"></a><a name="p213110511539"></a>The resource is abnormal.</p>
    </td>
    </tr>
    </tbody>
    </table>


