# Creating a DR Drill<a name="sdrs_05_0701"></a>

## Function<a name="section14779124510514"></a>

This API is used to create a disaster recovery \(DR\) drill.

## Constraints and Limitations<a name="section89885190818"></a>

-   **status**  of the protection group must be  **available**,  **protected**,  **failed-over**,  **error-starting**,  **error-stopping**,  **error-reversing**,  **error-reprotecting**, or  **error-failing-over**.
-   Do not perform a DR drill before the first time data synchronization completes. Otherwise, the drill server may not start properly.
-   If the DR site server of the protection group is added to Enterprise Project, the created DR drill server will not be automatically added to Enterprise Project. You need to manually add it to Enterprise Project if needed.
-   If  **drill\_vpc\_id**  is specified \(the system uses an existing drill VPC\), the drill VPC CIDR block must be consistent with that of the VPC for the protection group. If  **drill\_vpc\_id**  is not specified, the system automatically creates a drill VPC.
-   When you use a created drill VPC to create a drill, the subnet ACL rule of the drill VPC will be different from that of the VPC of the protection group. You need to manually set them to be the same one if needed.
-   When you create a DR drill, if the VPC of the protection group has a customized routing table and subnets configured, the corresponding routing table will not be automatically created for the drill VPC. You need to manually create it if needed.

## URI<a name="section153861316152517"></a>

-   URI format

    POST /v1/\{project\_id\}/disaster-recovery-drills


-   Parameter description

<a name="table626919772614"></a>
<table><thead align="left"><tr id="row029797192616"><th class="cellrowborder" valign="top" width="15.459999999999999%" id="mcps1.1.5.1.1"><p id="p829714714267"><a name="p829714714267"></a><a name="p829714714267"></a><strong id="b84235270615443"><a name="b84235270615443"></a><a name="b84235270615443"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.430000000000001%" id="mcps1.1.5.1.2"><p id="p132977712263"><a name="p132977712263"></a><a name="p132977712263"></a><strong id="b84235270615447"><a name="b84235270615447"></a><a name="b84235270615447"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.59%" id="mcps1.1.5.1.3"><p id="p429713742620"><a name="p429713742620"></a><a name="p429713742620"></a><strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50.519999999999996%" id="mcps1.1.5.1.4"><p id="p14297187162610"><a name="p14297187162610"></a><a name="p14297187162610"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row529717792618"><td class="cellrowborder" valign="top" width="15.459999999999999%" headers="mcps1.1.5.1.1 "><p id="p1129716762612"><a name="p1129716762612"></a><a name="p1129716762612"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.430000000000001%" headers="mcps1.1.5.1.2 "><p id="p17297147142615"><a name="p17297147142615"></a><a name="p17297147142615"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.1.5.1.3 "><p id="p172970718262"><a name="p172970718262"></a><a name="p172970718262"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.519999999999996%" headers="mcps1.1.5.1.4 "><p id="p122971676267"><a name="p122971676267"></a><a name="p122971676267"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section164743348267"></a>

-   Parameter description

    <a name="table17813513277"></a>
    <table><thead align="left"><tr id="row787781112712"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p98771912276"><a name="p98771912276"></a><a name="p98771912276"></a><strong id="b1025355661"><a name="b1025355661"></a><a name="b1025355661"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.5.1.2"><p id="p58771012275"><a name="p58771012275"></a><a name="p58771012275"></a><strong id="b928589655"><a name="b928589655"></a><a name="b928589655"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.3"><p id="p98776132712"><a name="p98776132712"></a><a name="p98776132712"></a><strong id="b2088104378"><a name="b2088104378"></a><a name="b2088104378"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.1.5.1.4"><p id="p7877191162714"><a name="p7877191162714"></a><a name="p7877191162714"></a><strong id="b1271288693"><a name="b1271288693"></a><a name="b1271288693"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1787710162710"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p1824911633017"><a name="p1824911633017"></a><a name="p1824911633017"></a>disaster_recovery_drill</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p48771311278"><a name="p48771311278"></a><a name="p48771311278"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p128770192713"><a name="p128770192713"></a><a name="p128770192713"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p1887714116274"><a name="p1887714116274"></a><a name="p1887714116274"></a>Specifies the information about a DR drill.</p>
    <p id="p1595117334115"><a name="p1595117334115"></a><a name="p1595117334115"></a>For details, see <a href="#table592231164010">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **disaster\_recovery\_drill**  field description

    <a name="table592231164010"></a>
    <table><thead align="left"><tr id="row2103201244010"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p12104151214406"><a name="p12104151214406"></a><a name="p12104151214406"></a><strong id="b1958031934"><a name="b1958031934"></a><a name="b1958031934"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p110618124404"><a name="p110618124404"></a><a name="p110618124404"></a><strong id="b630005917"><a name="b630005917"></a><a name="b630005917"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p1010819128407"><a name="p1010819128407"></a><a name="p1010819128407"></a><strong id="b1919749780"><a name="b1919749780"></a><a name="b1919749780"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p14112141244014"><a name="p14112141244014"></a><a name="p14112141244014"></a><strong id="b213403512"><a name="b213403512"></a><a name="b213403512"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row141256121405"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p20127111224010"><a name="p20127111224010"></a><a name="p20127111224010"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p0128191224010"><a name="p0128191224010"></a><a name="p0128191224010"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1412991219404"><a name="p1412991219404"></a><a name="p1412991219404"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p1132112124012"><a name="p1132112124012"></a><a name="p1132112124012"></a>Specifies the ID of a protection group.</p>
    <p id="p1214719284341"><a name="p1214719284341"></a><a name="p1214719284341"></a>For details, see <a href="querying-protection-groups.md">Querying Protection Groups</a>.</p>
    </td>
    </tr>
    <tr id="row51331712144011"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p121349125404"><a name="p121349125404"></a><a name="p121349125404"></a>drill_vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p213431213402"><a name="p213431213402"></a><a name="p213431213402"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p17137412124012"><a name="p17137412124012"></a><a name="p17137412124012"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p91391612184015"><a name="p91391612184015"></a><a name="p91391612184015"></a>Specifies the drill VPC ID. If you do not specify this parameter, the system will automatically create a drill VPC.</p>
    </td>
    </tr>
    <tr id="row513910127407"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p201431412184016"><a name="p201431412184016"></a><a name="p201431412184016"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p1114514128409"><a name="p1114514128409"></a><a name="p1114514128409"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p5146191224010"><a name="p5146191224010"></a><a name="p5146191224010"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p1814871264019"><a name="p1814871264019"></a><a name="p1814871264019"></a>Specifies the name of a DR drill. The name can contain a maximum of 64 bytes. The value can contain only letters (a to z and A to Z), digits (0 to 9), decimal points (.), underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    POST https://\{Endpoint\}/v1/\{project\_id\}/disaster-recovery-drills

    ```
    {
             "disaster_recovery_drill": {
                      "name": "dr_drill_test",
                      "server_group_id":"c2aee29a-2959-4d01-9755-01cc76a4d17d",
                      "drill_vpc_id":"87d505be-e984-455e-ad84-588c73fb258b"
        }
    }
    ```


## Response<a name="section48391527302"></a>

-   Parameter description

    <a name="table1281112383010"></a>
    <table><thead align="left"><tr id="row61051923123013"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p1010582316301"><a name="p1010582316301"></a><a name="p1010582316301"></a><strong id="b842352706151210"><a name="b842352706151210"></a><a name="b842352706151210"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p21053237309"><a name="p21053237309"></a><a name="p21053237309"></a><strong id="b1587130705"><a name="b1587130705"></a><a name="b1587130705"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p161051235309"><a name="p161051235309"></a><a name="p161051235309"></a><strong id="b479966456"><a name="b479966456"></a><a name="b479966456"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1310542312301"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p1210517237301"><a name="p1210517237301"></a><a name="p1210517237301"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p12105523123013"><a name="p12105523123013"></a><a name="p12105523123013"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p6105723123012"><a name="p6105723123012"></a><a name="p6105723123012"></a>Specifies the job ID.</p>
    <p id="p184441948155510"><a name="p184441948155510"></a><a name="p184441948155510"></a>This is a returned parameter when the asynchronous API command is issued successfully. For details about the task execution result, see the description in <a href="querying-the-job-status.md">Querying the Job Status</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {  
        "job_id": "0000000011db92d36662db9d20df32ch"  
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


## Returned Values<a name="section35552115310"></a>

-   Normal

    <a name="table295713516312"></a>
    <table><thead align="left"><tr id="row498075163118"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p1398012516314"><a name="p1398012516314"></a><a name="p1398012516314"></a><strong id="b842352706175024"><a name="b842352706175024"></a><a name="b842352706175024"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p39804510315"><a name="p39804510315"></a><a name="p39804510315"></a><strong id="b1670551419"><a name="b1670551419"></a><a name="b1670551419"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1998013519312"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p13980195114319"><a name="p13980195114319"></a><a name="p13980195114319"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p14980151113111"><a name="p14980151113111"></a><a name="p14980151113111"></a>The server has accepted the request.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table1023081113216"></a>
    <table><thead align="left"><tr id="row18293711173212"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="p9293131112322"><a name="p9293131112322"></a><a name="p9293131112322"></a><strong id="b1167302089"><a name="b1167302089"></a><a name="b1167302089"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="p1729314118324"><a name="p1729314118324"></a><a name="p1729314118324"></a><strong id="b1039122294"><a name="b1039122294"></a><a name="b1039122294"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row82931711153217"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p329312119323"><a name="p329312119323"></a><a name="p329312119323"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p9293411193220"><a name="p9293411193220"></a><a name="p9293411193220"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row1829361113218"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p72936112326"><a name="p72936112326"></a><a name="p72936112326"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p1293161123219"><a name="p1293161123219"></a><a name="p1293161123219"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row192939114324"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p152941411143214"><a name="p152941411143214"></a><a name="p152941411143214"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p132941711173219"><a name="p132941711173219"></a><a name="p132941711173219"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row17294121103215"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p42941611103214"><a name="p42941611103214"></a><a name="p42941611103214"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p19294201115326"><a name="p19294201115326"></a><a name="p19294201115326"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row162941411133212"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p8294911173213"><a name="p8294911173213"></a><a name="p8294911173213"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p13294101113216"><a name="p13294101113216"></a><a name="p13294101113216"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row42948113329"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p112942011113211"><a name="p112942011113211"></a><a name="p112942011113211"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p1729481123216"><a name="p1729481123216"></a><a name="p1729481123216"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row029414110325"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p202941911193217"><a name="p202941911193217"></a><a name="p202941911193217"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p1329413112323"><a name="p1329413112323"></a><a name="p1329413112323"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row3294101118325"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p20294191110322"><a name="p20294191110322"></a><a name="p20294191110322"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p52943114327"><a name="p52943114327"></a><a name="p52943114327"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row1829491120320"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1729441111326"><a name="p1729441111326"></a><a name="p1729441111326"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p329481183219"><a name="p329481183219"></a><a name="p329481183219"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row12294111173219"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1929419118322"><a name="p1929419118322"></a><a name="p1929419118322"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p1229417114323"><a name="p1229417114323"></a><a name="p1229417114323"></a>Failed to complete the request because of a service error.</p>
    </td>
    </tr>
    <tr id="row8294101120326"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p929401163215"><a name="p929401163215"></a><a name="p929401163215"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p192941311103217"><a name="p192941311103217"></a><a name="p192941311103217"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row13294151117322"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p329413115325"><a name="p329413115325"></a><a name="p329413115325"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p4295131153216"><a name="p4295131153216"></a><a name="p4295131153216"></a>Failed to complete the request because the server receives an invalid response from an upstream server.</p>
    </td>
    </tr>
    <tr id="row1929571163210"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1295711193212"><a name="p1295711193212"></a><a name="p1295711193212"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p1129520112327"><a name="p1129520112327"></a><a name="p1129520112327"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row629516117328"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p9295711153217"><a name="p9295711153217"></a><a name="p9295711153217"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p2295121113210"><a name="p2295121113210"></a><a name="p2295121113210"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


