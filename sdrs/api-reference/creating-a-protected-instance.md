# Creating a Protected Instance<a name="sdrs_05_0501"></a>

## Function<a name="en-us_topic_0079693002_section34649765"></a>

This API is used to create a protected instance. When a protected instance is created, the default name of the server at the DR site is the same as that of the server at the production site, but their IDs are different. To modify a server name, click the server name on the protected instance details page to switch to the server details page and modify the server name. Alternatively, you can call the API in  [Changing the Name of a Protected Instance](changing-the-name-of-a-protected-instance.md)  to modify the name.

## Constraints and Limitations<a name="section15345162453414"></a>

-   **status**  of the protection group must be  **available**  or  **protected**.
-   No protected instance has been created using the server.
-   The server must be in the same VPC as the protection group.
-   If protection is enabled for servers created during capacity expansion of an Auto Scaling \(AS\) group, these servers cannot be deleted when the capacity of the AS group is reduced.
-   If the server at the production site runs Windows and you choose the key login mode, ensure that the key pair of the server exists when you create a protected instance. Otherwise, the server at the DR site may fail to create, causing the protected instance creation failure.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the key pair of the production site server has been deleted, create a key pair with the same name.  

-   If the production site server is added to Enterprise Project, the created DR site server will not be automatically added to Enterprise Project. You need to manually add it to Enterprise Project if needed.
-   After you create a protected instance and enable protection on servers at the production site, modifications to the  **Hostname**,  **Name**,  **Security Group**,  **Agency**,  **ECS Group**,  **Tags**, and  **Auto Recovery**  configurations of servers on the production site will not synchronize to the servers at the DR site. You can manually add the configuration items to the servers at the DR site on the management console.

## URI<a name="en-us_topic_0079693002_section39390935"></a>

-   URI format

    POST /v1/\{project\_id\}/protected-instances

-   Parameter description

    <a name="en-us_topic_0079693002_table63321005"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row37593218"><th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.1.5.1.1"><p id="p156610131613"><a name="p156610131613"></a><a name="p156610131613"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.1.5.1.2"><p id="p4668012162"><a name="p4668012162"></a><a name="p4668012162"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.1.5.1.3"><p id="p12661012161"><a name="p12661012161"></a><a name="p12661012161"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.504950495049506%" id="mcps1.1.5.1.4"><p id="p16620191615"><a name="p16620191615"></a><a name="p16620191615"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row29123463"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="p19663013163"><a name="p19663013163"></a><a name="p19663013163"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.5.1.2 "><p id="p46611011166"><a name="p46611011166"></a><a name="p46611011166"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.3 "><p id="p15672071610"><a name="p15672071610"></a><a name="p15672071610"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.1.5.1.4 "><p id="p76710011166"><a name="p76710011166"></a><a name="p76710011166"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079693002_section18974100"></a>

-   Parameter description

    <a name="en-us_topic_0079693002_table54932709"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row41882373"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p1192132112168"><a name="p1192132112168"></a><a name="p1192132112168"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.5.1.2"><p id="p129232191617"><a name="p129232191617"></a><a name="p129232191617"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.3"><p id="p12921521131614"><a name="p12921521131614"></a><a name="p12921521131614"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.1.5.1.4"><p id="p49242101620"><a name="p49242101620"></a><a name="p49242101620"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row27990155"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p1492121181613"><a name="p1492121181613"></a><a name="p1492121181613"></a>protected_instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p109232171617"><a name="p109232171617"></a><a name="p109232171617"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p492821111618"><a name="p492821111618"></a><a name="p492821111618"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p1292102118162"><a name="p1292102118162"></a><a name="p1292102118162"></a>Specifies the information about a protected instance.</p>
    <p id="p7520116143819"><a name="p7520116143819"></a><a name="p7520116143819"></a>For details, see <a href="#table1632215113348">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **protected\_instance**  field description

    <a name="table1632215113348"></a>
    <table><thead align="left"><tr id="row63289116346"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p13330111193413"><a name="p13330111193413"></a><a name="p13330111193413"></a><strong id="b842352706151210"><a name="b842352706151210"></a><a name="b842352706151210"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p33321118343"><a name="p33321118343"></a><a name="p33321118343"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p12333161173420"><a name="p12333161173420"></a><a name="p12333161173420"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p1033516115345"><a name="p1033516115345"></a><a name="p1033516115345"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1234501173411"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p11346141203410"><a name="p11346141203410"></a><a name="p11346141203410"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p834712113341"><a name="p834712113341"></a><a name="p834712113341"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p19348101163410"><a name="p19348101163410"></a><a name="p19348101163410"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p234913153415"><a name="p234913153415"></a><a name="p234913153415"></a>Specifies the ID of the protection group where a protected instance is added.</p>
    <p id="p13736203513581"><a name="p13736203513581"></a><a name="p13736203513581"></a>For details, see <a href="querying-protection-groups.md">Querying Protection Groups</a>.</p>
    </td>
    </tr>
    <tr id="row235010113341"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1035181183412"><a name="p1035181183412"></a><a name="p1035181183412"></a>server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p73521815349"><a name="p73521815349"></a><a name="p73521815349"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p935411113346"><a name="p935411113346"></a><a name="p935411113346"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p13559113412"><a name="p13559113412"></a><a name="p13559113412"></a>Specifies the ID of the production site server.</p>
    <div class="note" id="note78991219226"><a name="note78991219226"></a><a name="note78991219226"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p862281812212"><a name="p862281812212"></a><a name="p862281812212"></a>When the API is successfully invoked, the DR site server will be automatically created.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row835613113341"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p153585112349"><a name="p153585112349"></a><a name="p153585112349"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p735916133419"><a name="p735916133419"></a><a name="p735916133419"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p193611811345"><a name="p193611811345"></a><a name="p193611811345"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p136417153412"><a name="p136417153412"></a><a name="p136417153412"></a>Specifies the name of a protected instance. The name can contain a maximum of 64 bytes. The value can contain only letters (a to z and A to Z), digits (0 to 9), decimal points (.), underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row11364815343"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1636591143417"><a name="p1636591143417"></a><a name="p1636591143417"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p536717143419"><a name="p536717143419"></a><a name="p536717143419"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p136891163411"><a name="p136891163411"></a><a name="p136891163411"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p03692163416"><a name="p03692163416"></a><a name="p03692163416"></a>Specifies the description of a protected instance. The description can contain a maximum of 64 bytes. The value cannot contain the left angle bracket (&lt;) or right angle bracket (&gt;).</p>
    </td>
    </tr>
    <tr id="row1237721103415"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p63800123416"><a name="p63800123416"></a><a name="p63800123416"></a>primary_subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p53811214347"><a name="p53811214347"></a><a name="p53811214347"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p2381151143415"><a name="p2381151143415"></a><a name="p2381151143415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p550919197411"><a name="p550919197411"></a><a name="p550919197411"></a>Specifies the network ID of the subnet for the primary NIC on the DR site server. The value is the same as that of <strong id="b114542831019"><a name="b114542831019"></a><a name="b114542831019"></a>neutron_network_id</strong> obtained using the VPC API.</p>
    <p id="p182814201018"><a name="p182814201018"></a><a name="p182814201018"></a>For details about how to query the subnets, see <a href="https://docs.otc.t-systems.com/en-us/api/vpc/en-us_topic_0020090592.html" target="_blank" rel="noopener noreferrer">Querying Subnets</a>.</p>
    </td>
    </tr>
    <tr id="row103848183415"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1238791143415"><a name="p1238791143415"></a><a name="p1238791143415"></a>primary_ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p1038710173418"><a name="p1038710173418"></a><a name="p1038710173418"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p123871412348"><a name="p123871412348"></a><a name="p123871412348"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p8444753191215"><a name="p8444753191215"></a><a name="p8444753191215"></a>Specifies the IP address of the primary NIC on the DR site server.</p>
    <p id="p73901117342"><a name="p73901117342"></a><a name="p73901117342"></a>This parameter is valid only when <strong id="b157849402302"><a name="b157849402302"></a><a name="b157849402302"></a>primary_subnet_id</strong> is specified.</p>
    <p id="p1374413142388"><a name="p1374413142388"></a><a name="p1374413142388"></a>If this parameter is not specified when <strong id="b153603593307"><a name="b153603593307"></a><a name="b153603593307"></a>primary_subnet_id</strong> is specified, the system automatically assigns an IP address to the primary NIC on the DR site server</p>
    </td>
    </tr>
    <tr id="row15411161381118"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1313715294258"><a name="p1313715294258"></a><a name="p1313715294258"></a>flavorRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p1741214132116"><a name="p1741214132116"></a><a name="p1741214132116"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p94126134118"><a name="p94126134118"></a><a name="p94126134118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p20413113161111"><a name="p20413113161111"></a><a name="p20413113161111"></a>Specifies the flavor ID of the DR site server</p>
    <div class="note" id="note34243124143"><a name="note34243124143"></a><a name="note34243124143"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul1367484801310"></a><a name="ul1367484801310"></a><ul id="ul1367484801310"><li>If this parameter is not specified, the flavor ID of the DR site server is the same as that of the production site server by default.</li><li>Servers of different specifications have different performance, which may affect applications running on the servers. To ensure the server performance after a planned failover or failover, you are recommended to use servers of specifications (CPU and memory) same or higher than the specifications of the production site servers at the DR site.</li></ul>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    POST https://\{Endpoint\}/v1/\{project\_id\}/protected-instances

    ```
    {  
             "protected_instance":{  
                   "server_group_id": "523ab8ad-3759-4933-9436-4cf4ebb20867",  
                   "server_id": "403b603d-1d91-42cc-a357-81f3c2daf43f",  
                   "name": "test_protected_instance_name",  
                   "description": "my description",
                   "primary_subnet_id": "a32217fh-3413-c313-6342-3124d3491502", 
                   "primary_ip_address": "192.168.0.5",
                   "flavorRef": "s3.large.2", 
                   "tenancy": "dedicated", 
                   "dedicated_host_id": "0bc41598-1b5a-4bd2-872a-82e6abb82e68", 
                   "tags": [ 
                      { 
                          "key": "key1", 
                          "value":"value1" 
                      },
                      {
                           "key": "key",
                           "value": "value3" 
                      }
                   ]
             }  
      }
    ```


## Response<a name="en-us_topic_0079693002_section36549175"></a>

-   Parameter description

    <a name="table155991608555"></a>
    <table><thead align="left"><tr id="row460510055518"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p125611510173"><a name="p125611510173"></a><a name="p125611510173"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p1456195171718"><a name="p1456195171718"></a><a name="p1456195171718"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p12561651177"><a name="p12561651177"></a><a name="p12561651177"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row86164025512"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p4561551711"><a name="p4561551711"></a><a name="p4561551711"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p35635121719"><a name="p35635121719"></a><a name="p35635121719"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p538173714408"><a name="p538173714408"></a><a name="p538173714408"></a>Specifies the returned parameter when the asynchronous API command is issued successfully. For details about the task execution result, see the description in <a href="querying-the-job-status.md">Querying the Job Status</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    { 
       "job_id": "0000000062db92d70162db9d200f00bb" 
     }
    ```

    Or

    ```
    { 
         "error": { 
             "message": "XXXX",  
             "code": "XXX" 
         } 
     }
    ```

    In this example,  **error**  represents a general error, including  **badrequest**  \(shown below\) and  **itemNotFound**.

    ```
    { 
         "badrequest": { 
             "message": "XXXX",  
             "code": "XXX" 
         } 
     }
    ```


## Returned Values<a name="en-us_topic_0079693002_section60507121"></a>

-   Normal

    <a name="sdrs_05_0101_table4315991194956"></a>
    <table><thead align="left"><tr id="sdrs_05_0101_row2336641294956"><th class="cellrowborder" valign="top" width="42.59%" id="mcps1.1.3.1.1"><p id="sdrs_05_0101_p1363125894956"><a name="sdrs_05_0101_p1363125894956"></a><a name="sdrs_05_0101_p1363125894956"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.410000000000004%" id="mcps1.1.3.1.2"><p id="sdrs_05_0101_p3039012494956"><a name="sdrs_05_0101_p3039012494956"></a><a name="sdrs_05_0101_p3039012494956"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="sdrs_05_0101_row507566794956"><td class="cellrowborder" valign="top" width="42.59%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p847584694956"><a name="sdrs_05_0101_p847584694956"></a><a name="sdrs_05_0101_p847584694956"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.410000000000004%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p1545496394956"><a name="sdrs_05_0101_p1545496394956"></a><a name="sdrs_05_0101_p1545496394956"></a>The server has accepted the request.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="sdrs_05_0101_table22458872203835"></a>
    <table><thead align="left"><tr id="sdrs_05_0101_row35704554203835"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="sdrs_05_0101_p6387753203835"><a name="sdrs_05_0101_p6387753203835"></a><a name="sdrs_05_0101_p6387753203835"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="sdrs_05_0101_p47646009203835"><a name="sdrs_05_0101_p47646009203835"></a><a name="sdrs_05_0101_p47646009203835"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="sdrs_05_0101_row34121538203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p12381163203835"><a name="sdrs_05_0101_p12381163203835"></a><a name="sdrs_05_0101_p12381163203835"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p63350108203835"><a name="sdrs_05_0101_p63350108203835"></a><a name="sdrs_05_0101_p63350108203835"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row33280063203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p11330608203835"><a name="sdrs_05_0101_p11330608203835"></a><a name="sdrs_05_0101_p11330608203835"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p45364094203835"><a name="sdrs_05_0101_p45364094203835"></a><a name="sdrs_05_0101_p45364094203835"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row5623667203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p52863895203835"><a name="sdrs_05_0101_p52863895203835"></a><a name="sdrs_05_0101_p52863895203835"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p54117066203835"><a name="sdrs_05_0101_p54117066203835"></a><a name="sdrs_05_0101_p54117066203835"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row17291554203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p58438642203835"><a name="sdrs_05_0101_p58438642203835"></a><a name="sdrs_05_0101_p58438642203835"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p35909542203835"><a name="sdrs_05_0101_p35909542203835"></a><a name="sdrs_05_0101_p35909542203835"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row54750425203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p5599455203835"><a name="sdrs_05_0101_p5599455203835"></a><a name="sdrs_05_0101_p5599455203835"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p50902717203835"><a name="sdrs_05_0101_p50902717203835"></a><a name="sdrs_05_0101_p50902717203835"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row55471277203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p63988484203835"><a name="sdrs_05_0101_p63988484203835"></a><a name="sdrs_05_0101_p63988484203835"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p15684678203835"><a name="sdrs_05_0101_p15684678203835"></a><a name="sdrs_05_0101_p15684678203835"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row6944380203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p25623884203835"><a name="sdrs_05_0101_p25623884203835"></a><a name="sdrs_05_0101_p25623884203835"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p62268733203835"><a name="sdrs_05_0101_p62268733203835"></a><a name="sdrs_05_0101_p62268733203835"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row23547689203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p28314670203835"><a name="sdrs_05_0101_p28314670203835"></a><a name="sdrs_05_0101_p28314670203835"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p11786919203835"><a name="sdrs_05_0101_p11786919203835"></a><a name="sdrs_05_0101_p11786919203835"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row38973411203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p2729702203835"><a name="sdrs_05_0101_p2729702203835"></a><a name="sdrs_05_0101_p2729702203835"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p19779281203835"><a name="sdrs_05_0101_p19779281203835"></a><a name="sdrs_05_0101_p19779281203835"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row43795805203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p57799353203835"><a name="sdrs_05_0101_p57799353203835"></a><a name="sdrs_05_0101_p57799353203835"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p51235984203835"><a name="sdrs_05_0101_p51235984203835"></a><a name="sdrs_05_0101_p51235984203835"></a>Failed to complete the request because of a service error.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row58470678203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p38504500203835"><a name="sdrs_05_0101_p38504500203835"></a><a name="sdrs_05_0101_p38504500203835"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p31856770203835"><a name="sdrs_05_0101_p31856770203835"></a><a name="sdrs_05_0101_p31856770203835"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row18275474203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p3918444203835"><a name="sdrs_05_0101_p3918444203835"></a><a name="sdrs_05_0101_p3918444203835"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p48958538203835"><a name="sdrs_05_0101_p48958538203835"></a><a name="sdrs_05_0101_p48958538203835"></a>Failed to complete the request because the server receives an invalid response from an upstream server.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row37973662203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p55967806203835"><a name="sdrs_05_0101_p55967806203835"></a><a name="sdrs_05_0101_p55967806203835"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p37098455203835"><a name="sdrs_05_0101_p37098455203835"></a><a name="sdrs_05_0101_p37098455203835"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row65450640203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p67010448203835"><a name="sdrs_05_0101_p67010448203835"></a><a name="sdrs_05_0101_p67010448203835"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p59137180203835"><a name="sdrs_05_0101_p59137180203835"></a><a name="sdrs_05_0101_p59137180203835"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


