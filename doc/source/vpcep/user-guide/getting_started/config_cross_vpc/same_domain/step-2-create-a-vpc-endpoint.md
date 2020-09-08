# Step 2: Create a VPC Endpoint<a name="vpcep_02_02023"></a>

## Scenarios<a name="section1207820191216"></a>

This section describes how to create a VPC endpoint in another VPC of your own for connecting to the VPC endpoint service.

## Procedure<a name="section49178302126"></a>

1.  In the navigation pane on the left, choose  **VPC Endpoint**  \>  **VPC Endpoints**.
2.  On the displayed page, click  **Create VPC Endpoint**.

    **Figure  1**  Create VPC Endpoint<a name="fig3678226165614"></a>  
    ![](/vpcep/user-guide/figures/create-vpc-endpoint.png "create-vpc-endpoint")

3.  Configure parameters by referring to  [Table 1](#table1449016525218).

    **Table  1**  Required parameters

    <a name="table1449016525218"></a>
    <table><thead align="left"><tr id="row448845216214"><th class="cellrowborder" valign="top" width="19.950000000000003%" id="mcps1.2.3.1.1"><p id="p648810528211"><a name="p648810528211"></a><a name="p648810528211"></a><strong id="b142371120101315"><a name="b142371120101315"></a><a name="b142371120101315"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="80.05%" id="mcps1.2.3.1.2"><p id="p7488115219220"><a name="p7488115219220"></a><a name="p7488115219220"></a><strong id="b427715218136"><a name="b427715218136"></a><a name="b427715218136"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row74887527213"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p164888522219"><a name="p164888522219"></a><a name="p164888522219"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p1348817522217"><a name="p1348817522217"></a><a name="p1348817522217"></a>Specifies the region where the VPC endpoint is located. This region is the same as that of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row13489105218217"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p19488205213212"><a name="p19488205213212"></a><a name="p19488205213212"></a>Service Category</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p1757134220153"><a name="p1757134220153"></a><a name="p1757134220153"></a>There are two options: <strong id="b48876464323"><a name="b48876464323"></a><a name="b48876464323"></a>Cloud services</strong> or <strong id="b48882046133212"><a name="b48882046133212"></a><a name="b48882046133212"></a>Find a service by name</strong>.</p>
    <a name="ul033017631615"></a><a name="ul033017631615"></a><ul id="ul033017631615"><li><strong id="b132155102155"><a name="b132155102155"></a><a name="b132155102155"></a>Cloud services</strong>: Select this value if the target VPC endpoint service is a cloud service.</li><li><strong id="b1574221311159"><a name="b1574221311159"></a><a name="b1574221311159"></a>Find a service by name</strong>: Select this value if the target VPC endpoint service is a private service of your own.</li></ul>
    <p id="p748845214218"><a name="p748845214218"></a><a name="p748845214218"></a>Example: <strong id="b1633955318321"><a name="b1633955318321"></a><a name="b1633955318321"></a>Find a service by name</strong></p>
    </td>
    </tr>
    <tr id="row1148995216218"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p9489125217215"><a name="p9489125217215"></a><a name="p9489125217215"></a>VPC Endpoint Service Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p44541820122317"><a name="p44541820122317"></a><a name="p44541820122317"></a>This parameter is available only if you select <strong id="b151101933280"><a name="b151101933280"></a><a name="b151101933280"></a>Find a service by name</strong> for <strong id="b8111638289"><a name="b8111638289"></a><a name="b8111638289"></a>Service Category</strong>.</p>
    <p id="p2765151952514"><a name="p2765151952514"></a><a name="p2765151952514"></a>Enter the VPC endpoint service name recorded in step <a href="step-1-create-a-vpc-endpoint-service.md#li837613314320">8</a>, for example, <strong id="b152951244733"><a name="b152951244733"></a><a name="b152951244733"></a>eu-de.69e93219-e3ad-43b9-8416-9d788319ac9f</strong> and click <strong id="b1833816415591"><a name="b1833816415591"></a><a name="b1833816415591"></a>Verify</strong>.</p>
    <a name="ul2413202710255"></a><a name="ul2413202710255"></a><ul id="ul2413202710255"><li>If <strong id="b12495239125617"><a name="b12495239125617"></a><a name="b12495239125617"></a>Service name found</strong> is displayed, proceed with subsequent operations.</li><li>If <strong id="b79601041205611"><a name="b79601041205611"></a><a name="b79601041205611"></a>Service name not found</strong> is displayed, check whether the region is the same as that of the connected VPC endpoint service or whether the entered service name is correct.</li></ul>
    </td>
    </tr>
    <tr id="row24891452828"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p248915212210"><a name="p248915212210"></a><a name="p248915212210"></a>Private Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p428517225213"><a name="p428517225213"></a><a name="p428517225213"></a>If you want to access a VPC endpoint using a domain name, select <strong id="b136998229533"><a name="b136998229533"></a><a name="b136998229533"></a>Create a Private Domain Name</strong> when creating a VPC endpoint. After the VPC endpoint is created, you can access it using the domain name.</p>
    <a name="ul102191581715"></a><a name="ul102191581715"></a><ul id="ul102191581715"><li>For a target VPC endpoint service that is a gateway, this parameter is unavailable.</li><li>For a target VPC endpoint service that is an interface, this parameter is optional.</li></ul>
    </td>
    </tr>
    <tr id="row16489145215218"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p1489352922"><a name="p1489352922"></a><a name="p1489352922"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p174891152428"><a name="p174891152428"></a><a name="p174891152428"></a>Specifies the VPC where the VPC endpoint is located.</p>
    </td>
    </tr>
    <tr id="row20490115211211"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p1948915529217"><a name="p1948915529217"></a><a name="p1948915529217"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p1490135214214"><a name="p1490135214214"></a><a name="p1490135214214"></a>Specifies the subnet where the VPC endpoint is located.</p>
    </td>
    </tr>
    <tr id="row149146382217"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p111652042164320"><a name="p111652042164320"></a><a name="p111652042164320"></a>Private IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p1230717432095"><a name="p1230717432095"></a><a name="p1230717432095"></a>This parameter is available only if you create a VPC endpoint for connecting to an interface VPC endpoint service.</p>
    <p id="p111652426435"><a name="p111652426435"></a><a name="p111652426435"></a>Specifies the private IP address of the VPC endpoint. You can select <strong id="b55051336144910"><a name="b55051336144910"></a><a name="b55051336144910"></a>Automatic</strong> or <strong id="b1151983617499"><a name="b1151983617499"></a><a name="b1151983617499"></a>Manual</strong>.</p>
    </td>
    </tr>
    <tr id="row74909521922"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p10490152321"><a name="p10490152321"></a><a name="p10490152321"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p1636001755219"><a name="p1636001755219"></a><a name="p1636001755219"></a>This parameter is optional.</p>
    <p id="p1490175220216"><a name="p1490175220216"></a><a name="p1490175220216"></a>Specifies the VPC endpoint tag, which consists of a key and a value. You can add a maximum of 10 tags to each VPC endpoint.</p>
    <p id="p74903522027"><a name="p74903522027"></a><a name="p74903522027"></a>Tag keys and values must meet requirements listed in <a href="#table1349117521628">Table 2</a>.</p>
    <div class="note" id="note5846751155719"><a name="note5846751155719"></a><a name="note5846751155719"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0131645182_p1697925218"><a name="en-us_topic_0131645182_p1697925218"></a><a name="en-us_topic_0131645182_p1697925218"></a>If a predefined tag has been created on TMS, you can directly select the corresponding tag key and value.</p>
    <p id="en-us_topic_0131645182_p6121182813506"><a name="en-us_topic_0131645182_p6121182813506"></a><a name="en-us_topic_0131645182_p6121182813506"></a>For details about predefined tags, see <a href="https://docs.otc.t-systems.com/usermanual/tms/en-us_topic_0056266269.html" target="_blank" rel="noopener noreferrer">Predefined Tag Overview</a>.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Tag requirements for VPC endpoints

    <a name="table1349117521628"></a>
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

4.  Confirm the specifications and click  **Create Now**.
    -   If all of the specifications are correct, click  **Submit**.
    -   If any of the specifications are incorrect, click  **Previous**  to return to the previous page and modify the parameters as needed, and then click  **Submit**.

5.  Manage the connection of the VPC endpoint.

    If the status of the VPC endpoint changes to  **Accepted**, the VPC endpoint is connected to the desired VPC endpoint service. If the status is  **Pending acceptance**, connection approval is enabled for the endpoint service and you need to contact the owner of the endpoint service and ask the owner to perform the following operations:

    1.  In the navigation pane on the left, choose  **VPC Endpoint**  \>  **VPC Endpoint Services**.
    2.  In the VPC endpoint service list, locate the target VPC endpoint service and click its name.
    3.  On the displayed page, select the  **Connection Management**  tab.
        -   If you allow a VPC endpoint to connect to this VPC endpoint service, locate the target VPC endpoint and click  **Accept**  in the  **Operation**  column.
        -   If you refuse a VPC endpoint from connecting to this VPC endpoint service, click  **Reject**  in the  **Operation**  column.

    4.  Go back to the VPC endpoint list and check whether the status of the target VPC endpoint changes to  **Accepted**. If yes, the VPC endpoint is connected to the VPC endpoint service.

6.  In the VPC endpoint list, click the ID of the target VPC endpoint to view its details.

    After a VPC endpoint is created, a private IP address and a private domain name are generated if you select  **Create a Private Domain Name**  during creation.

    **Figure  2**  Summary of the VPC endpoint<a name="fig6750164113019"></a>  
    ![](/vpcep/user-guide/figures/summary-of-the-vpc-endpoint.png "summary-of-the-vpc-endpoint")

    You can use the private IP address or private domain name to access the VPC endpoint service.


## Configuration Verification<a name="section179521348182011"></a>

Log in to an ECS in VPC1 in remote mode and access the VPC endpoint using its private IP address or private domain name.

**Figure  3**  Logging in to the ECS to access the VPC endpoint<a name="fig470954135415"></a>  
![](/vpcep/user-guide/figures/logging-in-to-the-ecs-to-access-the-vpc-endpoint.png "logging-in-to-the-ecs-to-access-the-vpc-endpoint")

