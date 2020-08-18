# Step 1: Create a VPC Endpoint for Connecting to DNS<a name="vpcep_02_0302"></a>

## Scenarios<a name="section999595611370"></a>

This section describes how to create a VPC endpoint for accessing a DNS server, in order to forward requests of resolving OBS domain names.

## Procedure<a name="section433119486438"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Click  **Service List**  and choose  **VPC Endpoint**  under  **Network**.

1.  On the  **VPC Endpoints**  page, click  **Create VPC Endpoint**.

    The  **Create VPC Endpoint**  page is displayed.

    **Figure  1**  Create VPC Endpoint<a name="fig1672316225376"></a>  
    ![](figures/create-vpc-endpoint-2.png "create-vpc-endpoint-2")

2.  Configure parameters by referring to  [Table 1](#table85139343530).

    **Table  1**  Required parameters

    <a name="table85139343530"></a>
    <table><thead align="left"><tr id="row573718559589"><th class="cellrowborder" valign="top" width="22.97%" id="mcps1.2.3.1.1"><p id="p19845468112"><a name="p19845468112"></a><a name="p19845468112"></a><strong id="b12298310334"><a name="b12298310334"></a><a name="b12298310334"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="77.03%" id="mcps1.2.3.1.2"><p id="p8818151814596"><a name="p8818151814596"></a><a name="p8818151814596"></a><strong id="b823454183318"><a name="b823454183318"></a><a name="b823454183318"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row157371055185814"><td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.2.3.1.1 "><p id="p1582221875915"><a name="p1582221875915"></a><a name="p1582221875915"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="77.03%" headers="mcps1.2.3.1.2 "><p id="p142402511421"><a name="p142402511421"></a><a name="p142402511421"></a>Specifies the region where the VPC endpoint is located.</p>
    <p id="p18823101819598"><a name="p18823101819598"></a><a name="p18823101819598"></a>Resources in different regions cannot communicate with each other over internal networks. For lower network latency and faster access to resources, select the nearest region.</p>
    </td>
    </tr>
    <tr id="row1173785555810"><td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.2.3.1.1 "><p id="p2829181875918"><a name="p2829181875918"></a><a name="p2829181875918"></a>Service Category</p>
    </td>
    <td class="cellrowborder" valign="top" width="77.03%" headers="mcps1.2.3.1.2 "><p id="p1757134220153"><a name="p1757134220153"></a><a name="p1757134220153"></a>There are two options: <strong id="b797416261823"><a name="b797416261823"></a><a name="b797416261823"></a>Cloud services</strong> or <strong id="b14976192920215"><a name="b14976192920215"></a><a name="b14976192920215"></a>Find a service by name</strong>.</p>
    <a name="ul033017631615"></a><a name="ul033017631615"></a><ul id="ul033017631615"><li><strong id="b611016901413"><a name="b611016901413"></a><a name="b611016901413"></a>Cloud services</strong>: Select this value if the target VPC endpoint service is a cloud service.</li><li><strong id="b97471910111417"><a name="b97471910111417"></a><a name="b97471910111417"></a>Find a service by name</strong>: Select this value if the target VPC endpoint service is a private service of your own.</li></ul>
    <p id="p38293188598"><a name="p38293188598"></a><a name="p38293188598"></a>Example: <strong id="b842352706163023"><a name="b842352706163023"></a><a name="b842352706163023"></a>Cloud services</strong></p>
    </td>
    </tr>
    <tr id="row1373945595814"><td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.2.3.1.1 "><p id="p183291814594"><a name="p183291814594"></a><a name="p183291814594"></a>Service List</p>
    </td>
    <td class="cellrowborder" valign="top" width="77.03%" headers="mcps1.2.3.1.2 "><p id="p2077711451062"><a name="p2077711451062"></a><a name="p2077711451062"></a>This parameter is available only if you select <strong id="b84235270617153"><a name="b84235270617153"></a><a name="b84235270617153"></a>Cloud services</strong> for <strong id="b8423527061721"><a name="b8423527061721"></a><a name="b8423527061721"></a>Service Category</strong>.</p>
    <p id="p136925222284"><a name="p136925222284"></a><a name="p136925222284"></a>The VPC endpoint service has been created by operations people and you can use it without having to perform the creation operation.</p>
    <p id="p178331418165914"><a name="p178331418165914"></a><a name="p178331418165914"></a>Example: <strong id="b1939710151420"><a name="b1939710151420"></a><a name="b1939710151420"></a>com.t-systems.otc.eu-de.dns</strong></p>
    </td>
    </tr>
    <tr id="row1762717911591"><td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.2.3.1.1 "><p id="p583711186592"><a name="p583711186592"></a><a name="p583711186592"></a>Private Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="77.03%" headers="mcps1.2.3.1.2 "><p id="p946796123317"><a name="p946796123317"></a><a name="p946796123317"></a>If you want to access a VPC endpoint using a domain name, select <strong id="b1382213276236"><a name="b1382213276236"></a><a name="b1382213276236"></a>Create a Private Domain Name</strong> when creating a VPC endpoint. After the VPC endpoint is created, you can access it using the domain name.</p>
    <p id="p13794391474"><a name="p13794391474"></a><a name="p13794391474"></a>This parameter can only be configured for VPC endpoints of the interface type.</p>
    <a name="ul4120659195320"></a><a name="ul4120659195320"></a><ul id="ul4120659195320"><li>For a target VPC endpoint service that is a gateway, this parameter is unavailable.</li><li>For a target VPC endpoint service that is an interface, this parameter is optional.</li></ul>
    </td>
    </tr>
    <tr id="row36294912590"><td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.2.3.1.1 "><p id="p33591328191713"><a name="p33591328191713"></a><a name="p33591328191713"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="77.03%" headers="mcps1.2.3.1.2 "><p id="p619041554012"><a name="p619041554012"></a><a name="p619041554012"></a>Specifies the VPC where the VPC endpoint is located.</p>
    </td>
    </tr>
    <tr id="row1062914915592"><td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.2.3.1.1 "><p id="p1284291815594"><a name="p1284291815594"></a><a name="p1284291815594"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="77.03%" headers="mcps1.2.3.1.2 "><p id="p1220520210222"><a name="p1220520210222"></a><a name="p1220520210222"></a>This parameter is available only if you create a VPC endpoint for connecting to an interface VPC endpoint service.</p>
    <p id="p874574018102"><a name="p874574018102"></a><a name="p874574018102"></a>Specifies the subnet where the VPC endpoint is located.</p>
    </td>
    </tr>
    <tr id="row1631222142818"><td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.2.3.1.1 "><p id="p111652042164320"><a name="p111652042164320"></a><a name="p111652042164320"></a>Private IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="77.03%" headers="mcps1.2.3.1.2 "><p id="p217097596"><a name="p217097596"></a><a name="p217097596"></a>This parameter is available only if you create a VPC endpoint for connecting to an interface VPC endpoint service.</p>
    <p id="p111652426435"><a name="p111652426435"></a><a name="p111652426435"></a>Specifies the private IP address of the VPC endpoint. You can select <strong id="b3930506403"><a name="b3930506403"></a><a name="b3930506403"></a>Automatic</strong> or <strong id="b39311505406"><a name="b39311505406"></a><a name="b39311505406"></a>Manual</strong>.</p>
    </td>
    </tr>
    <tr id="row65523491313"><td class="cellrowborder" valign="top" width="22.97%" headers="mcps1.2.3.1.1 "><p id="p12722155817313"><a name="p12722155817313"></a><a name="p12722155817313"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="77.03%" headers="mcps1.2.3.1.2 "><p id="p189201436125417"><a name="p189201436125417"></a><a name="p189201436125417"></a>This parameter is optional.</p>
    <p id="p16439102412198"><a name="p16439102412198"></a><a name="p16439102412198"></a>Specifies the VPC endpoint tag, which consists of a key and a value. You can add a maximum of 10 tags to each VPC endpoint.</p>
    <p id="p117231558153114"><a name="p117231558153114"></a><a name="p117231558153114"></a>Tag keys and values must meet requirements listed in <a href="#table775312110110">Table 2</a>.</p>
    <div class="note" id="note81245517210"><a name="note81245517210"></a><a name="note81245517210"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0131645182_p1697925218"><a name="en-us_topic_0131645182_p1697925218"></a><a name="en-us_topic_0131645182_p1697925218"></a>If a predefined tag has been created on TMS, you can directly select the corresponding tag key and value.</p>
    <p id="en-us_topic_0131645182_p6121182813506"><a name="en-us_topic_0131645182_p6121182813506"></a><a name="en-us_topic_0131645182_p6121182813506"></a>For details about predefined tags, see <a href="https://docs.otc.t-systems.com/usermanual/tms/en-us_topic_0056266269.html" target="_blank" rel="noopener noreferrer">Predefined Tag Overview</a>.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Tag requirements for VPC endpoints

    <a name="table775312110110"></a>
    <table><thead align="left"><tr id="row1975492119112"><th class="cellrowborder" valign="top" width="42.63%" id="mcps1.2.3.1.1"><p id="p127543216114"><a name="p127543216114"></a><a name="p127543216114"></a><strong id="b116044234515"><a name="b116044234515"></a><a name="b116044234515"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.37%" id="mcps1.2.3.1.2"><p id="p187541211118"><a name="p187541211118"></a><a name="p187541211118"></a><strong id="b134861185457"><a name="b134861185457"></a><a name="b134861185457"></a>Requirement</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1375419211915"><td class="cellrowborder" valign="top" width="42.63%" headers="mcps1.2.3.1.1 "><p id="p15754421417"><a name="p15754421417"></a><a name="p15754421417"></a>Tag key</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.37%" headers="mcps1.2.3.1.2 "><a name="ul182248574315"></a><a name="ul182248574315"></a><ul id="ul182248574315"><li>Cannot be left blank.</li><li>Must be unique for the same VPC endpoint.</li><li>Contains a maximum of 36 characters and only allows the following characters:<a name="ul15224957937"></a><a name="ul15224957937"></a><ul id="ul15224957937"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row97543211410"><td class="cellrowborder" valign="top" width="42.63%" headers="mcps1.2.3.1.1 "><p id="p97549211414"><a name="p97549211414"></a><a name="p97549211414"></a>Tag value</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.37%" headers="mcps1.2.3.1.2 "><div class="p" id="p20581523133713"><a name="p20581523133713"></a><a name="p20581523133713"></a>Contains a maximum of 43 characters and only allows the following characters:<a name="ul19120173116418"></a><a name="ul19120173116418"></a><ul id="ul19120173116418"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

3.  Confirm the specifications and click  **Create Now**.
    -   If all of the specifications are correct, click  **Submit**.
    -   If any of the specifications are incorrect, click  **Previous**  to return to the previous page and modify the parameters as needed, and then click  **Submit**.

4.  Click  **Back to VPC Endpoint List**  after the task is submitted.

    If the status of the VPC endpoint changes to  **Accepted**, the VPC endpoint for connecting to  **com.t-systems.otc.eu-de.dns**  is created.

5.  In the VPC endpoint list, locate the target VPC endpoint and click its ID to view the endpoint details.

    After an interface VPC endpoint is created, a private IP address and a private domain name are generated if you select  **Create a Private Domain Name**  during creation.

    **Figure  2**  Summary of the VPC endpoint<a name="fig1234818262310"></a>  
    ![](figures/summary-of-the-vpc-endpoint-3.png "summary-of-the-vpc-endpoint-3")


