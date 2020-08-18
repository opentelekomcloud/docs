# Step 2: Create a VPC Endpoint<a name="vpcep_02_02035"></a>

## Scenarios<a name="section5179152041320"></a>

This section describes how to create a VPC endpoint in another VPC of your own for connecting to the VPC endpoint service.

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>Select the same region and project as those of the VPC endpoint service.

## Procedure<a name="section71312811313"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Click  **Service List**  and choose  **VPC Endpoint**  under  **Network**.
4.  In the navigation pane on the left, choose  **VPC Endpoint**  \>  **VPC Endpoints**.
5.  On the  **VPC Endpoints**  page, click  **Create VPC Endpoint**.

    The  **Create VPC Endpoint**  page is displayed.

    **Figure  1**  Create VPC Endpoint<a name="fig3678226165614"></a>  
    ![](figures/create-vpc-endpoint-1.png "create-vpc-endpoint-1")

6.  Configure parameters by referring to  [Table 1](#table12737165517587).

    **Table  1**  Required parameters

    <a name="table12737165517587"></a>
    <table><thead align="left"><tr id="row573718559589"><th class="cellrowborder" valign="top" width="19.950000000000003%" id="mcps1.2.3.1.1"><p id="p19845468112"><a name="p19845468112"></a><a name="p19845468112"></a><strong id="b183661420173514"><a name="b183661420173514"></a><a name="b183661420173514"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="80.05%" id="mcps1.2.3.1.2"><p id="p8818151814596"><a name="p8818151814596"></a><a name="p8818151814596"></a><strong id="b114674219359"><a name="b114674219359"></a><a name="b114674219359"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row157371055185814"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p1582221875915"><a name="p1582221875915"></a><a name="p1582221875915"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p414694461010"><a name="p414694461010"></a><a name="p414694461010"></a>Specifies the region where the VPC endpoint is located. This region is the same as that of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row1173785555810"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p2829181875918"><a name="p2829181875918"></a><a name="p2829181875918"></a>Service Category</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p1757134220153"><a name="p1757134220153"></a><a name="p1757134220153"></a>There are two options: <strong id="b17409125544019"><a name="b17409125544019"></a><a name="b17409125544019"></a>Cloud services</strong> or <strong id="b941005513408"><a name="b941005513408"></a><a name="b941005513408"></a>Find a service by name</strong>.</p>
    <a name="ul033017631615"></a><a name="ul033017631615"></a><ul id="ul033017631615"><li><strong id="b1437152413131"><a name="b1437152413131"></a><a name="b1437152413131"></a>Cloud services</strong>: Select this value if the target VPC endpoint service is a cloud service.</li><li><strong id="b1240812260133"><a name="b1240812260133"></a><a name="b1240812260133"></a>Find a service by name</strong>: Select this value if the target VPC endpoint service is a private service of your own.</li></ul>
    <p id="p38293188598"><a name="p38293188598"></a><a name="p38293188598"></a>Example: <strong id="vpcep_02_02023_b1633955318321"><a name="vpcep_02_02023_b1633955318321"></a><a name="vpcep_02_02023_b1633955318321"></a>Find a service by name</strong></p>
    </td>
    </tr>
    <tr id="row1373945595814"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p183291814594"><a name="p183291814594"></a><a name="p183291814594"></a>VPC Endpoint Service Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p44541820122317"><a name="p44541820122317"></a><a name="p44541820122317"></a>This parameter is available only if you select <strong id="b8826197144118"><a name="b8826197144118"></a><a name="b8826197144118"></a>Find a service by name</strong> for <strong id="b9827971415"><a name="b9827971415"></a><a name="b9827971415"></a>Service Category</strong>.</p>
    <p id="p1934481283910"><a name="p1934481283910"></a><a name="p1934481283910"></a>Enter a VPC endpoint service name, for example, <strong id="b41416440567"><a name="b41416440567"></a><a name="b41416440567"></a>eu-de.69e93219-e3ad-43b9-8416-9d788319ac9f</strong>, and click <strong id="b363492845611"><a name="b363492845611"></a><a name="b363492845611"></a>Verify</strong>.</p>
    <a name="ul3480142813394"></a><a name="ul3480142813394"></a><ul id="ul3480142813394"><li>If <strong id="b52510075717"><a name="b52510075717"></a><a name="b52510075717"></a>Service name found</strong> is displayed, proceed with subsequent operations.</li><li>If <strong id="b1827512239431"><a name="b1827512239431"></a><a name="b1827512239431"></a>Service name not found</strong> is displayed, check whether the region is the same as that of the connected VPC endpoint service or whether the entered service name is correct.</li></ul>
    </td>
    </tr>
    <tr id="row1762717911591"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p583711186592"><a name="p583711186592"></a><a name="p583711186592"></a>Private Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p1592095318211"><a name="p1592095318211"></a><a name="p1592095318211"></a>If you want to access a VPC endpoint using a domain name, select <strong id="b841704135310"><a name="b841704135310"></a><a name="b841704135310"></a>Create a Private Domain Name</strong> when creating a VPC endpoint. After the VPC endpoint is created, you can access it using the domain name.</p>
    <a name="ul104371446506"></a><a name="ul104371446506"></a><ul id="ul104371446506"><li>For a target VPC endpoint service that is a gateway, this parameter is unavailable.</li><li>For a target VPC endpoint service that is an interface, this parameter is optional.</li></ul>
    </td>
    </tr>
    <tr id="row36294912590"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p4787227141811"><a name="p4787227141811"></a><a name="p4787227141811"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p1578952791814"><a name="p1578952791814"></a><a name="p1578952791814"></a>Specifies the VPC where the VPC endpoint is located.</p>
    </td>
    </tr>
    <tr id="row1062914915592"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p1284291815594"><a name="p1284291815594"></a><a name="p1284291815594"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p384231845919"><a name="p384231845919"></a><a name="p384231845919"></a>Specifies the subnet where the VPC endpoint is located.</p>
    </td>
    </tr>
    <tr id="row15944171661120"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p111652042164320"><a name="p111652042164320"></a><a name="p111652042164320"></a>Private IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p149917271918"><a name="p149917271918"></a><a name="p149917271918"></a>This parameter is available only if you create a VPC endpoint for connecting to an interface VPC endpoint service.</p>
    <p id="p111652426435"><a name="p111652426435"></a><a name="p111652426435"></a>Specifies the private IP address of the VPC endpoint. You can select <strong id="b172641514132610"><a name="b172641514132610"></a><a name="b172641514132610"></a>Automatic</strong> or <strong id="b152781014142619"><a name="b152781014142619"></a><a name="b152781014142619"></a>Manual</strong>.</p>
    </td>
    </tr>
    <tr id="row1164684404011"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p11841250101315"><a name="p11841250101315"></a><a name="p11841250101315"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p18120152565319"><a name="p18120152565319"></a><a name="p18120152565319"></a>This parameter is optional.</p>
    <p id="p1934918182710"><a name="p1934918182710"></a><a name="p1934918182710"></a>Specifies the VPC endpoint tag, which consists of a key and a value. You can add a maximum of 10 tags to each VPC endpoint.</p>
    <p id="p218515071317"><a name="p218515071317"></a><a name="p218515071317"></a>Tag keys and values must meet requirements listed in <a href="#table37259471306">Table 2</a>.</p>
    <div class="note" id="note135211732813"><a name="note135211732813"></a><a name="note135211732813"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0131645182_p1697925218"><a name="en-us_topic_0131645182_p1697925218"></a><a name="en-us_topic_0131645182_p1697925218"></a>If a predefined tag has been created on TMS, you can directly select the corresponding tag key and value.</p>
    <p id="en-us_topic_0131645182_p6121182813506"><a name="en-us_topic_0131645182_p6121182813506"></a><a name="en-us_topic_0131645182_p6121182813506"></a>For details about predefined tags, see <a href="https://docs.otc.t-systems.com/usermanual/tms/en-us_topic_0056266269.html" target="_blank" rel="noopener noreferrer">Predefined Tag Overview</a>.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Tag requirements for VPC endpoints

    <a name="table37259471306"></a>
    <table><thead align="left"><tr id="vpcep_02_0302_row1975492119112"><th class="cellrowborder" valign="top" width="42.63%" id="mcps1.2.3.1.1"><p id="vpcep_02_0302_p127543216114"><a name="vpcep_02_0302_p127543216114"></a><a name="vpcep_02_0302_p127543216114"></a><strong id="vpcep_02_0302_b116044234515"><a name="vpcep_02_0302_b116044234515"></a><a name="vpcep_02_0302_b116044234515"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.37%" id="mcps1.2.3.1.2"><p id="vpcep_02_0302_p187541211118"><a name="vpcep_02_0302_p187541211118"></a><a name="vpcep_02_0302_p187541211118"></a><strong id="vpcep_02_0302_b134861185457"><a name="vpcep_02_0302_b134861185457"></a><a name="vpcep_02_0302_b134861185457"></a>Requirement</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpcep_02_0302_row1375419211915"><td class="cellrowborder" valign="top" width="42.63%" headers="mcps1.2.3.1.1 "><p id="vpcep_02_0302_p15754421417"><a name="vpcep_02_0302_p15754421417"></a><a name="vpcep_02_0302_p15754421417"></a>Tag key</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.37%" headers="mcps1.2.3.1.2 "><a name="vpcep_02_0302_ul182248574315"></a><a name="vpcep_02_0302_ul182248574315"></a><ul id="vpcep_02_0302_ul182248574315"><li>Cannot be left blank.</li><li>Must be unique for the same VPC endpoint.</li><li>Contains a maximum of 36 characters and only allows the following characters:<a name="vpcep_02_0302_ul15224957937"></a><a name="vpcep_02_0302_ul15224957937"></a><ul id="vpcep_02_0302_ul15224957937"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="vpcep_02_0302_row97543211410"><td class="cellrowborder" valign="top" width="42.63%" headers="mcps1.2.3.1.1 "><p id="vpcep_02_0302_p97549211414"><a name="vpcep_02_0302_p97549211414"></a><a name="vpcep_02_0302_p97549211414"></a>Tag value</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.37%" headers="mcps1.2.3.1.2 "><div class="p" id="vpcep_02_0302_p20581523133713"><a name="vpcep_02_0302_p20581523133713"></a><a name="vpcep_02_0302_p20581523133713"></a>Contains a maximum of 43 characters and only allows the following characters:<a name="vpcep_02_0302_ul19120173116418"></a><a name="vpcep_02_0302_ul19120173116418"></a><ul id="vpcep_02_0302_ul19120173116418"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

7.  Confirm the specifications and click  **Create Now**.
    -   If all of the specifications are correct, click  **Submit**.
    -   If any of the specifications are incorrect, click  **Previous**  to return to the previous page and modify the parameters as needed, and then click  **Submit**.

8.  Manage the connection of the VPC endpoint.

    If the status of the VPC endpoint changes to  **Accepted**, the VPC endpoint is connected to the desired VPC endpoint service. If the status is  **Pending acceptance**, connection approval is enabled for the endpoint service and you need to contact the owner of the endpoint service and ask the owner to perform the following operations:

    1.  Log in to the management console.
    2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
    3.  Click  **Service List**  and choose  **VPC Endpoint**  under  **Network**.
    4.  In the navigation pane on the left, choose  **VPC Endpoint**  \>  **VPC Endpoint Services**.
    5.  In the VPC endpoint service list, locate the target VPC endpoint service and click its name.
    6.  On the displayed page, select the  **Connection Management**  tab.
        -   If you allow a VPC endpoint to connect to this VPC endpoint service, locate the target VPC endpoint and click  **Accept**  in the  **Operation**  column.
        -   If you refuse a VPC endpoint from connecting to this VPC endpoint service, click  **Reject**  in the  **Operation**  column.

    7.  Go back to the VPC endpoint list and check whether the status of the target VPC endpoint changes to  **Accepted**. If yes, the VPC endpoint is connected to the VPC endpoint service.

9.  In the VPC endpoint list, click the ID of the target VPC endpoint to view its details.

    After a VPC endpoint is created, a private IP address and a private domain name are generated if you select  **Create a Private Domain Name**  during creation.

    **Figure  2**  Summary of the VPC endpoint<a name="vpcep_02_02023_fig6750164113019"></a>  
    ![](figures/summary-of-the-vpc-endpoint.png "summary-of-the-vpc-endpoint")

    You can use the private IP address or private domain name to access the VPC endpoint service.


