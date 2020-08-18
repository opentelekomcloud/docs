# Step 2: Create a VPC Endpoint for Connecting to OBS<a name="vpcep_02_0303"></a>

## Scenarios<a name="section687815311387"></a>

This section describes how to create a VPC endpoint to access OBS from your local data center.

## Procedure<a name="section10562948920"></a>

1.  On the displayed page, click  **Create VPC Endpoint**.

    The  **Create VPC Endpoint**  page is displayed.

    **Figure  1**  Create VPC Endpoint<a name="fig1672316225376"></a>  
    ![](figures/create-vpc-endpoint-4.png "create-vpc-endpoint-4")

2.  Configure parameters by referring to  [Table 1](#table15408172022211).

    **Table  1**  Required parameters

    <a name="table15408172022211"></a>
    <table><thead align="left"><tr id="row1740572010223"><th class="cellrowborder" valign="top" width="22.830000000000002%" id="mcps1.2.3.1.1"><p id="p440582010229"><a name="p440582010229"></a><a name="p440582010229"></a><strong id="b79018283246"><a name="b79018283246"></a><a name="b79018283246"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="77.17%" id="mcps1.2.3.1.2"><p id="p6405112052219"><a name="p6405112052219"></a><a name="p6405112052219"></a><strong id="b89611528142420"><a name="b89611528142420"></a><a name="b89611528142420"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54061020172210"><td class="cellrowborder" valign="top" width="22.830000000000002%" headers="mcps1.2.3.1.1 "><p id="p1240542020228"><a name="p1240542020228"></a><a name="p1240542020228"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="77.17%" headers="mcps1.2.3.1.2 "><p id="p88021271489"><a name="p88021271489"></a><a name="p88021271489"></a>Specifies the region where the VPC endpoint is located.</p>
    <p id="p14406192012221"><a name="p14406192012221"></a><a name="p14406192012221"></a>Resources in different regions cannot communicate with each other over internal networks. For lower network latency and faster access to resources, select the nearest region.</p>
    </td>
    </tr>
    <tr id="row440662082215"><td class="cellrowborder" valign="top" width="22.830000000000002%" headers="mcps1.2.3.1.1 "><p id="p1540622002211"><a name="p1540622002211"></a><a name="p1540622002211"></a>Service Category</p>
    </td>
    <td class="cellrowborder" valign="top" width="77.17%" headers="mcps1.2.3.1.2 "><p id="p1757134220153"><a name="p1757134220153"></a><a name="p1757134220153"></a>There are two options: <strong id="b4151954711"><a name="b4151954711"></a><a name="b4151954711"></a>Cloud services</strong> or <strong id="b61611918472"><a name="b61611918472"></a><a name="b61611918472"></a>Find a service by name</strong>.</p>
    <a name="ul033017631615"></a><a name="ul033017631615"></a><ul id="ul033017631615"><li><strong id="b632519311142"><a name="b632519311142"></a><a name="b632519311142"></a>Cloud services</strong>: Select this value if the target VPC endpoint service is a cloud service.</li><li><strong id="b191701133201418"><a name="b191701133201418"></a><a name="b191701133201418"></a>Find a service by name</strong>: Select this value if the target VPC endpoint service is a private service of your own.</li></ul>
    <p id="p38293188598"><a name="p38293188598"></a><a name="p38293188598"></a>Example: <strong id="b2041324724719"><a name="b2041324724719"></a><a name="b2041324724719"></a>Cloud services</strong></p>
    </td>
    </tr>
    <tr id="row5406820172217"><td class="cellrowborder" valign="top" width="22.830000000000002%" headers="mcps1.2.3.1.1 "><p id="p3406520162211"><a name="p3406520162211"></a><a name="p3406520162211"></a>Service List</p>
    </td>
    <td class="cellrowborder" valign="top" width="77.17%" headers="mcps1.2.3.1.2 "><p id="p2077711451062"><a name="p2077711451062"></a><a name="p2077711451062"></a>This parameter is available only if you select <strong id="b1964814844713"><a name="b1964814844713"></a><a name="b1964814844713"></a>Cloud services</strong> for <strong id="b17649204884714"><a name="b17649204884714"></a><a name="b17649204884714"></a>Service Category</strong>.</p>
    <p id="p1483771241911"><a name="p1483771241911"></a><a name="p1483771241911"></a>The VPC endpoint service has been created by operations people and you can use it without having to perform the creation operation.</p>
    <p id="p15406182012226"><a name="p15406182012226"></a><a name="p15406182012226"></a>Example: <strong id="b1881412442288"><a name="b1881412442288"></a><a name="b1881412442288"></a>com.t-systems.otc.eu-de.obs</strong></p>
    </td>
    </tr>
    <tr id="row1407162072220"><td class="cellrowborder" valign="top" width="22.830000000000002%" headers="mcps1.2.3.1.1 "><p id="p15407162013221"><a name="p15407162013221"></a><a name="p15407162013221"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="77.17%" headers="mcps1.2.3.1.2 "><p id="p619041554012"><a name="p619041554012"></a><a name="p619041554012"></a>Specifies the VPC where the VPC endpoint is located.</p>
    </td>
    </tr>
    <tr id="row740752017228"><td class="cellrowborder" valign="top" width="22.830000000000002%" headers="mcps1.2.3.1.1 "><p id="p164071208226"><a name="p164071208226"></a><a name="p164071208226"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="77.17%" headers="mcps1.2.3.1.2 "><p id="p36711254125416"><a name="p36711254125416"></a><a name="p36711254125416"></a>This parameter is optional.</p>
    <p id="p14849415152412"><a name="p14849415152412"></a><a name="p14849415152412"></a>Specifies the VPC endpoint tag, which consists of a key and a value. You can add a maximum of 10 tags to each VPC endpoint.</p>
    <p id="p1140782017225"><a name="p1140782017225"></a><a name="p1140782017225"></a>Tag keys and values must meet requirements listed in <a href="#table1487920102215">Table 2</a>.</p>
    <div class="note" id="note1144911398210"><a name="note1144911398210"></a><a name="note1144911398210"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0131645182_p1697925218"><a name="en-us_topic_0131645182_p1697925218"></a><a name="en-us_topic_0131645182_p1697925218"></a>If a predefined tag has been created on TMS, you can directly select the corresponding tag key and value.</p>
    <p id="en-us_topic_0131645182_p6121182813506"><a name="en-us_topic_0131645182_p6121182813506"></a><a name="en-us_topic_0131645182_p6121182813506"></a>For details about predefined tags, see <a href="https://docs.otc.t-systems.com/usermanual/tms/en-us_topic_0056266269.html" target="_blank" rel="noopener noreferrer">Predefined Tag Overview</a>.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Tag requirements for VPC endpoints

    <a name="table1487920102215"></a>
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

3.  Confirm the specifications and click  **Create Now**.
    -   If all of the specifications are correct, click  **Submit**.
    -   If any of the specifications are incorrect, click  **Previous**  to return to the previous page and modify the parameters as needed, and then click  **Submit**.

4.  Click  **Back to VPC Endpoint List**  after the task is submitted.

    If the status of the VPC endpoint changes from  **Creating**  to  **Accepted**, the VPC endpoint for connecting to  **com.t-systems.otc.eu-de.obs**  is created.

5.  In the VPC endpoint list, locate the target VPC endpoint and click its ID to view the endpoint details.

    **Figure  2**  Summary of the VPC endpoint<a name="fig16953822181916"></a>  
    ![](figures/summary-of-the-vpc-endpoint-5.png "summary-of-the-vpc-endpoint-5")


