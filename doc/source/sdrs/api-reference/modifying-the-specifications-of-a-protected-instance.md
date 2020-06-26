# Modifying the Specifications of a Protected Instance<a name="sdrs_05_0510"></a>

## Function<a name="section1490915283251"></a>

This API is used to modify the specifications of a server in a protected instance, including:

-   Modify the specifications of both the production and DR site servers.
-   Modify the specifications of only the production site server.
-   Modify the specifications of only the DR site server.

You can perform this operation only when the servers of which the specifications to be modified are stopped.

>![](/images/icon-note.gif) **NOTE:**   
>Servers of different specifications have different performance, which may affect applications running on the servers. To ensure the server performance after a planned failover or failover, you are recommended to use servers of specifications \(CPU and memory\) same or higher than the specifications of the production site servers at the DR site.  

## Constraints and Limitations<a name="section7196184015399"></a>

-   **status**  of the protection group must be  **available**  or  **protected**.
-   **status**  of the protected instance must be  **available**,  **protected**, or  **error-resizing**.
-   Servers of which the specifications to be modified are stopped.

## URI<a name="section1691352816254"></a>

-   URI format

    POST /v1/\{project\_id\}/protected-instances/\{protected\_instance\_id\}/resize

-   Parameter description

    <a name="table19201128132511"></a>
    <table><thead align="left"><tr id="row31342297258"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.5.1.1"><p id="p15134172915251"><a name="p15134172915251"></a><a name="p15134172915251"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.33%" id="mcps1.1.5.1.2"><p id="p1013442952511"><a name="p1013442952511"></a><a name="p1013442952511"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.39%" id="mcps1.1.5.1.3"><p id="p1913419291256"><a name="p1913419291256"></a><a name="p1913419291256"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="35.709999999999994%" id="mcps1.1.5.1.4"><p id="p17135152910253"><a name="p17135152910253"></a><a name="p17135152910253"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12135112962518"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.5.1.1 "><p id="p2013552952512"><a name="p2013552952512"></a><a name="p2013552952512"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.1.5.1.2 "><p id="p17135162912510"><a name="p17135162912510"></a><a name="p17135162912510"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p1913572992518"><a name="p1913572992518"></a><a name="p1913572992518"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.709999999999994%" headers="mcps1.1.5.1.4 "><p id="p9135172917257"><a name="p9135172917257"></a><a name="p9135172917257"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row413532917251"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.5.1.1 "><p id="p13135132982513"><a name="p13135132982513"></a><a name="p13135132982513"></a>protected_instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.1.5.1.2 "><p id="p413572962510"><a name="p413572962510"></a><a name="p413572962510"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.3 "><p id="p6135129152515"><a name="p6135129152515"></a><a name="p6135129152515"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.709999999999994%" headers="mcps1.1.5.1.4 "><p id="p2135202918251"><a name="p2135202918251"></a><a name="p2135202918251"></a>Specifies the ID of a protected instance.</p>
    <p id="p89531514145712"><a name="p89531514145712"></a><a name="p89531514145712"></a>You can obtain this value by calling the API described in <a href="querying-protected-instances.md">Querying Protected Instances</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section119421628182517"></a>

-   Parameter description

    <a name="table3944628102518"></a>
    <table><thead align="left"><tr id="row1513618295254"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p151361729152511"><a name="p151361729152511"></a><a name="p151361729152511"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.5.1.2"><p id="p111362296253"><a name="p111362296253"></a><a name="p111362296253"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.3"><p id="p0136152912515"><a name="p0136152912515"></a><a name="p0136152912515"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.1.5.1.4"><p id="p191365290255"><a name="p191365290255"></a><a name="p191365290255"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8136122914252"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p3136229132519"><a name="p3136229132519"></a><a name="p3136229132519"></a>resize</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p2136162917253"><a name="p2136162917253"></a><a name="p2136162917253"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p19137429162515"><a name="p19137429162515"></a><a name="p19137429162515"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p6137132913253"><a name="p6137132913253"></a><a name="p6137132913253"></a>Modifies the specifications of a protected instance.</p>
    <p id="p1416017218478"><a name="p1416017218478"></a><a name="p1416017218478"></a>The target server flavors to which a flavor can be changed are the same as those for ECS. You can use the ECS API to query these flavors. For details, see section "Querying the Target ECS Flavors to Which a Flavor Can Be Changed" in <a href="https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0020805967.html" target="_blank" rel="noopener noreferrer">Elastic Cloud Server API Reference</a>.</p>
    <p id="p560813118486"><a name="p560813118486"></a><a name="p560813118486"></a>For details, see <a href="#table0953028102515">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **resize**  field description

    <a name="table0953028102515"></a>
    <table><thead align="left"><tr id="row713752912259"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p613792911257"><a name="p613792911257"></a><a name="p613792911257"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p61371029192519"><a name="p61371029192519"></a><a name="p61371029192519"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p13137129192510"><a name="p13137129192510"></a><a name="p13137129192510"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p1413717293255"><a name="p1413717293255"></a><a name="p1413717293255"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15137529112519"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1313715294258"><a name="p1313715294258"></a><a name="p1313715294258"></a>flavorRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p1713816298251"><a name="p1713816298251"></a><a name="p1713816298251"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p4138182942513"><a name="p4138182942513"></a><a name="p4138182942513"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p61381429182519"><a name="p61381429182519"></a><a name="p61381429182519"></a>Specifies the flavor ID of the production and DR site servers after the modification.</p>
    <div class="note" id="note20185132583617"><a name="note20185132583617"></a><a name="note20185132583617"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p151871425123613"><a name="p151871425123613"></a><a name="p151871425123613"></a>If you specify this parameter, the system modifies the specifications of both the production and DR site servers. After the modification, the production site server and DR site server use the same specifications.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1472613612382"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p16727163618382"><a name="p16727163618382"></a><a name="p16727163618382"></a>production_flavorRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p197271236203812"><a name="p197271236203812"></a><a name="p197271236203812"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p772753683818"><a name="p772753683818"></a><a name="p772753683818"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p13727236133816"><a name="p13727236133816"></a><a name="p13727236133816"></a>Specifies the flavor ID of the production site server after the modification.</p>
    <div class="note" id="note8741115215411"><a name="note8741115215411"></a><a name="note8741115215411"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul185161342204318"></a><a name="ul185161342204318"></a><ul id="ul185161342204318"><li>If you specify this parameter, the system modifies the specifications of only the production site server.</li><li>If <strong id="b163371219713"><a name="b163371219713"></a><a name="b163371219713"></a>flavorRef</strong> is specified, <strong id="b395017441375"><a name="b395017441375"></a><a name="b395017441375"></a>production_flavorRef</strong> does not take effect.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row938593910388"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p03851939153820"><a name="p03851939153820"></a><a name="p03851939153820"></a>dr_flavorRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p13386103911385"><a name="p13386103911385"></a><a name="p13386103911385"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1386173911388"><a name="p1386173911388"></a><a name="p1386173911388"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p193861939173811"><a name="p193861939173811"></a><a name="p193861939173811"></a>Specifies the flavor ID of the DR site server after the modification.</p>
    <div class="note" id="note1957918126426"><a name="note1957918126426"></a><a name="note1957918126426"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul947565364317"></a><a name="ul947565364317"></a><ul id="ul947565364317"><li>If you specify this parameter, the system modifies the specifications of only the DR site server.</li><li>If <strong id="b198151620189"><a name="b198151620189"></a><a name="b198151620189"></a>flavorRef</strong> is specified, <strong id="b158163201180"><a name="b158163201180"></a><a name="b158163201180"></a>dr_flavorRef</strong> does not take effect.</li></ul>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    POST https://\{Endpoint\}/v1/\{project\_id\}/protected-instances/00000000632302f501632305f63c000e/resize

    Example 1: Modify the specifications of the production and DR site servers to e2.small. Example request:

    ```
    {   
          "resize": {   
               "flavorRef": "e2.small"
           }   
     }
    ```

    Example 2: Modify the specifications of the production and DR site serves to s3.small.1 and s3.large.2 respectively. Example request:

    ```
    {   
          "resize": {   
               "production_flavorRef": "s3.small.1",
               "dr_flavorRef": "s3.large.2"
           }   
     }
    ```

    Example 3: Modify the specifications of the production site server to e2.small, and retain the DR site server specifications. Example request:

    ```
    {   
          "resize": {   
               "production_flavorRef": "e2.small"
           }   
     }
    ```

    Example 4: Modify the specifications of the DR site server to e2.small, and retain the production site server specifications. Example request:

    ```
    {   
          "resize": {   
               "dr_flavorRef": "e2.small"
           }   
     }
    ```


## Response<a name="section8961102832514"></a>

-   Parameter description

    <a name="table1696412852512"></a>
    <table><thead align="left"><tr id="row213972918255"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p1413912298259"><a name="p1413912298259"></a><a name="p1413912298259"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p9139192912512"><a name="p9139192912512"></a><a name="p9139192912512"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p1313919295253"><a name="p1313919295253"></a><a name="p1313919295253"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row31391329132519"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p1613942918252"><a name="p1613942918252"></a><a name="p1613942918252"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p131391229172514"><a name="p131391229172514"></a><a name="p131391229172514"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p15139629152515"><a name="p15139629152515"></a><a name="p15139629152515"></a>Specifies the job ID.</p>
    <p id="p11406939144312"><a name="p11406939144312"></a><a name="p11406939144312"></a>This is a returned parameter when the asynchronous API command is issued successfully. For details about the task execution result, see the description in <a href="querying-the-job-status.md">Querying the Job Status</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {  
        "job_id": "0000000011db92d70162db9d20df32ch"  
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


## Returned Values<a name="section159741628152511"></a>

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


