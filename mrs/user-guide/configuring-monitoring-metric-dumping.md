# Configuring Monitoring Metric Dumping<a name="EN-US_TOPIC_0125375619"></a>

## Scenario<a name="section4158655012154"></a>

You can configure interconnection parameters on MRS Manager to save monitoring indicator data to a specified FTP server using the FTP or SFTP protocol. In this way, MRS clusters can interconnect with third-party systems. The FTP protocol does not encrypt data, which creates potential security risks. The SFTP protocol is recommended.

MRS Manager supports the collecting of all monitoring indicator data in managed clusters. The collection period can be 30 seconds, 60 seconds, or 300 seconds. Depending on the collection period, the data is stored in different monitoring files on the FTP server. To name a monitoring file, adhere to the following pattern: Cluster name\_metric\_Monitoring indicator data collection period\_File saving time.log.

## Prerequisites<a name="section6134247712556"></a>

-   The corresponding ECS of the dump server and the Master node of the MRS cluster are deployed on the same VPC.
-   The Master node can access the IP address and specific ports of the dump server.
-   The FTP service of the dump server is running properly.

## Procedure<a name="section906741412237"></a>

1.  On MRS Manager, click  **System**.
2.  In  **Configuration**, click **Configure Monitoring Metric Dump** under **Monitoring and Alarm**.
3.  [Table 1](#table6396292112414)  describes dump parameters.

    **Table  1**  Dump parameters

    <a name="table6396292112414"></a>
    <table><thead align="left"><tr id="row5968953912414"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="p301448212414"><a name="p301448212414"></a><a name="p301448212414"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="p4284651412414"><a name="p4284651412414"></a><a name="p4284651412414"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54004614193153"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p12297579193153"><a name="p12297579193153"></a><a name="p12297579193153"></a>Dump Monitoring Metric</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p56579820193153"><a name="p56579820193153"></a><a name="p56579820193153"></a>Mandatory.</p>
    <p id="p33830997193450"><a name="p33830997193450"></a><a name="p33830997193450"></a>Specifies whether to enable the audit log export function.</p>
    <a name="ul1089276919373"></a><a name="ul1089276919373"></a><ul id="ul1089276919373"><li><a name="image1220780219327"></a><a name="image1220780219327"></a><span><img id="image1220780219327" src="figures/wwx437827-中软基础平台部-datasight-image-8602897a-b990-4838-8c30-36b5459e48ff.png"></span> : Enabled</li><li><a name="image2579164419228"></a><a name="image2579164419228"></a><span><img id="image2579164419228" src="figures/wwx437827-中软基础平台部-datasight-image-dcd81e5f-3df4-40ac-a2e7-fe1afef5102f.png"></span> : Disabled</li></ul>
    </td>
    </tr>
    <tr id="row4801562712414"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p6406054812414"><a name="p6406054812414"></a><a name="p6406054812414"></a>FTP IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p2152186112414"><a name="p2152186112414"></a><a name="p2152186112414"></a>Mandatory.</p>
    <p id="p5947902412414"><a name="p5947902412414"></a><a name="p5947902412414"></a>Specifies the IP address of the FTP server for storing monitoring files after the interconnection of monitoring indicator data is enabled.</p>
    </td>
    </tr>
    <tr id="row6554917512414"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p788294512414"><a name="p788294512414"></a><a name="p788294512414"></a>FTP Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p3453882812414"><a name="p3453882812414"></a><a name="p3453882812414"></a>Mandatory.</p>
    <p id="p4241400112414"><a name="p4241400112414"></a><a name="p4241400112414"></a>Specifies the port for connecting to the FTP server.</p>
    </td>
    </tr>
    <tr id="row4618169612414"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p4972985912414"><a name="p4972985912414"></a><a name="p4972985912414"></a>FTP Username</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p158681612414"><a name="p158681612414"></a><a name="p158681612414"></a>Mandatory.</p>
    <p id="p1428134712414"><a name="p1428134712414"></a><a name="p1428134712414"></a>Specifies the username for logging in to the FTP server.</p>
    </td>
    </tr>
    <tr id="row6142326112414"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p922822612414"><a name="p922822612414"></a><a name="p922822612414"></a>FTP Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p928885612414"><a name="p928885612414"></a><a name="p928885612414"></a>Mandatory.</p>
    <p id="p1649084512414"><a name="p1649084512414"></a><a name="p1649084512414"></a>Specifies the password for logging in to the FTP server.</p>
    </td>
    </tr>
    <tr id="row1419987812414"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p933950912414"><a name="p933950912414"></a><a name="p933950912414"></a>Save Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1830279712414"><a name="p1830279712414"></a><a name="p1830279712414"></a>Mandatory.</p>
    <p id="p3050744712414"><a name="p3050744712414"></a><a name="p3050744712414"></a>Specifies the save path of monitoring files on the FTP server.</p>
    </td>
    </tr>
    <tr id="row613157312414"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p2689538112414"><a name="p2689538112414"></a><a name="p2689538112414"></a>Dump Interval (s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p3104226212414"><a name="p3104226212414"></a><a name="p3104226212414"></a>Mandatory.</p>
    <p id="p1094490612414"><a name="p1094490612414"></a><a name="p1094490612414"></a>Specifies the interval for saving monitoring files to the FTP server, in seconds.</p>
    </td>
    </tr>
    <tr id="row3139529512414"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p5999100112414"><a name="p5999100112414"></a><a name="p5999100112414"></a>Dump Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p2743294012414"><a name="p2743294012414"></a><a name="p2743294012414"></a>Mandatory.</p>
    <p id="p4556987012414"><a name="p4556987012414"></a><a name="p4556987012414"></a>Specifies the protocol used to send monitoring files. The options include <strong id="b17196012414"><a name="b17196012414"></a><a name="b17196012414"></a>FTP</strong>&nbsp;and&nbsp;<strong id="b5825018212414"><a name="b5825018212414"></a><a name="b5825018212414"></a>SFTP</strong>.</p>
    </td>
    </tr>
    <tr id="row2064429812414"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p6157547112414"><a name="p6157547112414"></a><a name="p6157547112414"></a>SFTP Public Key</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p2155727712414"><a name="p2155727712414"></a><a name="p2155727712414"></a>Optional.</p>
    <p id="p5979776612414"><a name="p5979776612414"></a><a name="p5979776612414"></a>Specifies the public key of the FTP server. This parameter is valid after <strong id="b1618383211232"><a name="b1618383211232"></a><a name="b1618383211232"></a>Dump Mode</strong> is set to&nbsp;<strong id="b6543850412414"><a name="b6543850412414"></a><a name="b6543850412414"></a>SFTP</strong>. You are advised to set this parameter. If not, security risks may exist.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **OK**. The parameters are set.

