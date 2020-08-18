# Creating a VPC Endpoint<a name="en-us_topic_0131645189"></a>

## Scenarios<a name="section158984274016"></a>

This section describes how to create a VPC endpoint as needed.

## Procedure<a name="section339372615535"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Click  **Service List**  and choose  **VPC Endpoint**  under  **Network**.
4.  On the displayed page, click  **Create VPC Endpoint**.
5.  On the  **Create VPC Endpoint**  page, set the parameters as prompted.

    **Figure  1**  Create VPC Endpoint \(select  **Cloud services**  for  **Service Category**\)<a name="fig1647103210203"></a>  
    ![](figures/create-vpc-endpoint-(select-cloud-services-for-service-category).png "create-vpc-endpoint-(select-cloud-services-for-service-category)")

    **Figure  2**  Create VPC Endpoint \(select  **Find a service by name**  for  **Service Category**\)<a name="fig3678226165614"></a>  
    ![](figures/create-vpc-endpoint-(select-find-a-service-by-name-for-service-category).png "create-vpc-endpoint-(select-find-a-service-by-name-for-service-category)")

    For parameters for creating a VPC endpoint, see  [Table 1](#table12737165517587).

    **Table  1**  Required parameters

    <a name="table12737165517587"></a>
    <table><thead align="left"><tr id="row573718559589"><th class="cellrowborder" valign="top" width="19.950000000000003%" id="mcps1.2.3.1.1"><p id="p19845468112"><a name="p19845468112"></a><a name="p19845468112"></a><strong id="b1616019131713"><a name="b1616019131713"></a><a name="b1616019131713"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="80.05%" id="mcps1.2.3.1.2"><p id="p8818151814596"><a name="p8818151814596"></a><a name="p8818151814596"></a><strong id="b143116141418"><a name="b143116141418"></a><a name="b143116141418"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row157371055185814"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p1582221875915"><a name="p1582221875915"></a><a name="p1582221875915"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p217793964314"><a name="p217793964314"></a><a name="p217793964314"></a>Specifies the region where the VPC endpoint is located. Resources in different regions cannot communicate with each other over internal networks. For lower network latency and faster access to resources, select the nearest region.</p>
    </td>
    </tr>
    <tr id="row1173785555810"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p2829181875918"><a name="p2829181875918"></a><a name="p2829181875918"></a>Service Category</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p1756510618442"><a name="p1756510618442"></a><a name="p1756510618442"></a>There are two options: <strong id="b860411441112"><a name="b860411441112"></a><a name="b860411441112"></a>Cloud services</strong> or <strong id="b66051144201115"><a name="b66051144201115"></a><a name="b66051144201115"></a>Find a service by name</strong>.</p>
    <a name="ul462316111449"></a><a name="ul462316111449"></a><ul id="ul462316111449"><li><strong id="b2946171641210"><a name="b2946171641210"></a><a name="b2946171641210"></a>Cloud services</strong>: Select this value if the target VPC endpoint service is a cloud service.</li><li><strong id="b6447113393819"><a name="b6447113393819"></a><a name="b6447113393819"></a>Find a service by name</strong>: Select this value if the target VPC endpoint service is a private service of your own.</li></ul>
    </td>
    </tr>
    <tr id="row680485252415"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p183291814594"><a name="p183291814594"></a><a name="p183291814594"></a>Service List</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p2077711451062"><a name="p2077711451062"></a><a name="p2077711451062"></a>This parameter is available only when you select <strong id="b58867426386"><a name="b58867426386"></a><a name="b58867426386"></a>Cloud services</strong> for <strong id="b11887194216385"><a name="b11887194216385"></a><a name="b11887194216385"></a>Service Category</strong>.</p>
    <p id="p1483771241911"><a name="p1483771241911"></a><a name="p1483771241911"></a>The VPC endpoint service has been created by operations people and you can use it without having to perform the creation operation.</p>
    </td>
    </tr>
    <tr id="row181111619152517"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p9489125217215"><a name="p9489125217215"></a><a name="p9489125217215"></a>VPC Endpoint Service Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p44541820122317"><a name="p44541820122317"></a><a name="p44541820122317"></a>This parameter is available only when you select <strong id="b1342605818389"><a name="b1342605818389"></a><a name="b1342605818389"></a>Find a service by name</strong> for <strong id="b242715817385"><a name="b242715817385"></a><a name="b242715817385"></a>Service Category</strong>.</p>
    <p id="p2765151952514"><a name="p2765151952514"></a><a name="p2765151952514"></a>Enter the VPC endpoint service name recorded in <a href="step-1-create-a-vpc-endpoint-service.md#li837613314320">8</a> and click <strong id="b89822022104112"><a name="b89822022104112"></a><a name="b89822022104112"></a>Verify</strong>.</p>
    <a name="ul2413202710255"></a><a name="ul2413202710255"></a><ul id="ul2413202710255"><li>If <strong id="b13884143395"><a name="b13884143395"></a><a name="b13884143395"></a>Service name found</strong> is displayed, proceed with subsequent operations.</li><li>If <strong id="b75211716173917"><a name="b75211716173917"></a><a name="b75211716173917"></a>Service name not found</strong> is displayed, check whether the region is the same as that of the connected VPC endpoint service or whether the entered service name is correct.</li></ul>
    </td>
    </tr>
    <tr id="row1762717911591"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p583711186592"><a name="p583711186592"></a><a name="p583711186592"></a>Private Domain Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p158760812914"><a name="p158760812914"></a><a name="p158760812914"></a>If you want to access a VPC endpoint using a domain name, select <strong id="vpcep_02_0302_b1382213276236"><a name="vpcep_02_0302_b1382213276236"></a><a name="vpcep_02_0302_b1382213276236"></a>Create a Private Domain Name</strong> when creating a VPC endpoint. After the VPC endpoint is created, you can access it using the domain name.</p>
    <p id="p1203944195919"><a name="p1203944195919"></a><a name="p1203944195919"></a>This parameter can only be configured for VPC endpoints of the interface type.</p>
    <a name="ul48541540116"></a><a name="ul48541540116"></a><ul id="ul48541540116"><li>For a target VPC endpoint service that is a gateway, this parameter is unavailable.</li><li>For a target VPC endpoint service that is an interface, this parameter is optional.</li></ul>
    </td>
    </tr>
    <tr id="row36294912590"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p4787227141811"><a name="p4787227141811"></a><a name="p4787227141811"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p619041554012"><a name="p619041554012"></a><a name="p619041554012"></a>Specifies the VPC where the VPC endpoint is located.</p>
    </td>
    </tr>
    <tr id="row1062914915592"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p1284291815594"><a name="p1284291815594"></a><a name="p1284291815594"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p1220520210222"><a name="p1220520210222"></a><a name="p1220520210222"></a>This parameter is available only when you create a VPC endpoint for connecting to an interface VPC endpoint service.</p>
    <p id="p874574018102"><a name="p874574018102"></a><a name="p874574018102"></a>Specifies the subnet where the VPC endpoint is located.</p>
    </td>
    </tr>
    <tr id="row9984356166"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p111652042164320"><a name="p111652042164320"></a><a name="p111652042164320"></a>Private IP Address</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p7275101111817"><a name="p7275101111817"></a><a name="p7275101111817"></a>This parameter is available only when you create a VPC endpoint for connecting to an interface VPC endpoint service.</p>
    <p id="p111652426435"><a name="p111652426435"></a><a name="p111652426435"></a>Specifies the private IP address of the VPC endpoint. You can select <strong id="b14641637102711"><a name="b14641637102711"></a><a name="b14641637102711"></a>Automatic</strong> or <strong id="b1146493712270"><a name="b1146493712270"></a><a name="b1146493712270"></a>Manual</strong>.</p>
    </td>
    </tr>
    <tr id="row1164684404011"><td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.3.1.1 "><p id="p11841250101315"><a name="p11841250101315"></a><a name="p11841250101315"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.05%" headers="mcps1.2.3.1.2 "><p id="p6659101317541"><a name="p6659101317541"></a><a name="p6659101317541"></a>This parameter is optional.</p>
    <p id="p7440181811445"><a name="p7440181811445"></a><a name="p7440181811445"></a>Specifies the VPC endpoint tag, which consists of a key and a value. You can add a maximum of 10 tags to each VPC endpoint.</p>
    <p id="p218515071317"><a name="p218515071317"></a><a name="p218515071317"></a>Tag keys and values must meet requirements listed in <a href="#table37259471306">Table 2</a>.</p>
    <div class="note" id="note242016251043"><a name="note242016251043"></a><a name="note242016251043"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0131645182_p1697925218"><a name="en-us_topic_0131645182_p1697925218"></a><a name="en-us_topic_0131645182_p1697925218"></a>If a predefined tag has been created on TMS, you can directly select the corresponding tag key and value.</p>
    <p id="en-us_topic_0131645182_p6121182813506"><a name="en-us_topic_0131645182_p6121182813506"></a><a name="en-us_topic_0131645182_p6121182813506"></a>For details about predefined tags, see <a href="https://docs.otc.t-systems.com/usermanual/tms/en-us_topic_0056266269.html" target="_blank" rel="noopener noreferrer">Predefined Tag Overview</a>.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Tag requirements for VPC endpoints

    <a name="table37259471306"></a>
    <table><thead align="left"><tr id="en-us_topic_0162785419_row1975492119112"><th class="cellrowborder" valign="top" width="42.63%" id="mcps1.2.3.1.1"><p id="en-us_topic_0162785419_p127543216114"><a name="en-us_topic_0162785419_p127543216114"></a><a name="en-us_topic_0162785419_p127543216114"></a><strong id="b11248632114012"><a name="b11248632114012"></a><a name="b11248632114012"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.37%" id="mcps1.2.3.1.2"><p id="en-us_topic_0162785419_p187541211118"><a name="en-us_topic_0162785419_p187541211118"></a><a name="en-us_topic_0162785419_p187541211118"></a><strong id="b153342338408"><a name="b153342338408"></a><a name="b153342338408"></a>Requirement</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0162785419_row1375419211915"><td class="cellrowborder" valign="top" width="42.63%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0162785419_p15754421417"><a name="en-us_topic_0162785419_p15754421417"></a><a name="en-us_topic_0162785419_p15754421417"></a>Tag key</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.37%" headers="mcps1.2.3.1.2 "><a name="en-us_topic_0162785419_ul182248574315"></a><a name="en-us_topic_0162785419_ul182248574315"></a><ul id="en-us_topic_0162785419_ul182248574315"><li>Cannot be left blank.</li><li>Must be unique for the same VPC endpoint.</li><li>Contains a maximum of 36 characters and only allows the following characters:<a name="en-us_topic_0162785419_ul15224957937"></a><a name="en-us_topic_0162785419_ul15224957937"></a><ul id="en-us_topic_0162785419_ul15224957937"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0162785419_row97543211410"><td class="cellrowborder" valign="top" width="42.63%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0162785419_p97549211414"><a name="en-us_topic_0162785419_p97549211414"></a><a name="en-us_topic_0162785419_p97549211414"></a>Tag value</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.37%" headers="mcps1.2.3.1.2 "><div class="p" id="en-us_topic_0162785419_p20581523133713"><a name="en-us_topic_0162785419_p20581523133713"></a><a name="en-us_topic_0162785419_p20581523133713"></a>Contains a maximum of 43 characters and only allows the following characters:<a name="en-us_topic_0162785419_ul19120173116418"></a><a name="en-us_topic_0162785419_ul19120173116418"></a><ul id="en-us_topic_0162785419_ul19120173116418"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

6.  Confirm the specifications and click  **Create Now**.
    -   If all of the specifications are correct, click  **Submit**.
    -   If any of the specifications are incorrect, click  **Previous**  to return to the previous page and modify the parameters as needed, and then click  **Submit**.


