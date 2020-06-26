# Creating a Replication Pair<a name="sdrs_05_0601"></a>

## Function<a name="en-us_topic_0079693002_section34649765"></a>

This API is used to create a replication pair and add it to the specified protection group.

## Constraints and Limitations<a name="section17205506404"></a>

-   **status**  of the protection group must be  **available**  or  **protected**.
-   If  **server\_type**  of the protection group is set to  **ECS**, the disk status is  **Available**.

## URI<a name="en-us_topic_0079693002_section39390935"></a>

-   URI format

    POST /v1/\{project\_id\}/replications

-   Parameter description

    <a name="en-us_topic_0079693002_table63321005"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row37593218"><th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.1.5.1.1"><p id="en-us_topic_0079693002_p25151854"><a name="en-us_topic_0079693002_p25151854"></a><a name="en-us_topic_0079693002_p25151854"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.1.5.1.2"><p id="en-us_topic_0079693002_p1556805116115"><a name="en-us_topic_0079693002_p1556805116115"></a><a name="en-us_topic_0079693002_p1556805116115"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.1.5.1.3"><p id="p125951548183213"><a name="p125951548183213"></a><a name="p125951548183213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.504950495049506%" id="mcps1.1.5.1.4"><p id="en-us_topic_0079693002_p2565159161120"><a name="en-us_topic_0079693002_p2565159161120"></a><a name="en-us_topic_0079693002_p2565159161120"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row29123463"><td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.1 "><p id="p199411839185611"><a name="p199411839185611"></a><a name="p199411839185611"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.5.1.2 "><p id="p9945103985612"><a name="p9945103985612"></a><a name="p9945103985612"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.1.5.1.3 "><p id="p1359514883213"><a name="p1359514883213"></a><a name="p1359514883213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.1.5.1.4 "><p id="p17947113916566"><a name="p17947113916566"></a><a name="p17947113916566"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079693002_section18974100"></a>

-   Parameter description

    <a name="en-us_topic_0079693002_table54932709"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row41882373"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="en-us_topic_0079693002_p8696081161227"><a name="en-us_topic_0079693002_p8696081161227"></a><a name="en-us_topic_0079693002_p8696081161227"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.5.1.2"><p id="en-us_topic_0079693002_p33293980161227"><a name="en-us_topic_0079693002_p33293980161227"></a><a name="en-us_topic_0079693002_p33293980161227"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.3"><p id="en-us_topic_0079693002_p12457872161227"><a name="en-us_topic_0079693002_p12457872161227"></a><a name="en-us_topic_0079693002_p12457872161227"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.1.5.1.4"><p id="en-us_topic_0079693002_p2454675161227"><a name="en-us_topic_0079693002_p2454675161227"></a><a name="en-us_topic_0079693002_p2454675161227"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row27990155"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p15440132953312"><a name="p15440132953312"></a><a name="p15440132953312"></a>replication</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p17440129123310"><a name="p17440129123310"></a><a name="p17440129123310"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p1144022916333"><a name="p1144022916333"></a><a name="p1144022916333"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p444022903315"><a name="p444022903315"></a><a name="p444022903315"></a>Specifies the information about a replication pair.</p>
    <p id="p5612344144814"><a name="p5612344144814"></a><a name="p5612344144814"></a>For details, see <a href="#table1282085653515">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **replication**  field description

    <a name="table1282085653515"></a>
    <table><thead align="left"><tr id="row582505613517"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p16826185613357"><a name="p16826185613357"></a><a name="p16826185613357"></a><strong id="b84235270615443"><a name="b84235270615443"></a><a name="b84235270615443"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p14829185673511"><a name="p14829185673511"></a><a name="p14829185673511"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p198301356133510"><a name="p198301356133510"></a><a name="p198301356133510"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p188331456103511"><a name="p188331456103511"></a><a name="p188331456103511"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5840656143514"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p188421056133512"><a name="p188421056133512"></a><a name="p188421056133512"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p2084455683518"><a name="p2084455683518"></a><a name="p2084455683518"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p384545633512"><a name="p384545633512"></a><a name="p384545633512"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p184645617351"><a name="p184645617351"></a><a name="p184645617351"></a>Specifies the ID of a protection group.</p>
    <p id="p11751114151011"><a name="p11751114151011"></a><a name="p11751114151011"></a>You can obtain this value by calling the API described in <a href="querying-protection-groups.md">Querying Protection Groups</a>.</p>
    </td>
    </tr>
    <tr id="row19846956143515"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p16847205619353"><a name="p16847205619353"></a><a name="p16847205619353"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p08501756143520"><a name="p08501756143520"></a><a name="p08501756143520"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p18513562355"><a name="p18513562355"></a><a name="p18513562355"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p6851145633518"><a name="p6851145633518"></a><a name="p6851145633518"></a>Specifies the ID of the production site disk.</p>
    <div class="note" id="note1860019482814"><a name="note1860019482814"></a><a name="note1860019482814"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p206012411280"><a name="p206012411280"></a><a name="p206012411280"></a>When the API is successfully invoked, the DR site disk will be automatically created.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row8853115663519"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p17855356113518"><a name="p17855356113518"></a><a name="p17855356113518"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p14855165615350"><a name="p14855165615350"></a><a name="p14855165615350"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p108561056173516"><a name="p108561056173516"></a><a name="p108561056173516"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p178571856193515"><a name="p178571856193515"></a><a name="p178571856193515"></a>Specifies the name of a replication pair. The name can contain a maximum of 64 bytes. The value can contain only letters (a to z and A to Z), digits (0 to 9), decimal points (.), underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row1385965612357"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p16861556173519"><a name="p16861556173519"></a><a name="p16861556173519"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p6862165614354"><a name="p6862165614354"></a><a name="p6862165614354"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p9862185610359"><a name="p9862185610359"></a><a name="p9862185610359"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p086516561354"><a name="p086516561354"></a><a name="p086516561354"></a>Specifies the description of a replication pair. The value can contain a maximum of 64 bytes and cannot contain the left angle bracket (&lt;) or right angle bracket (&gt;).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    POST https://\{Endpoint\}/v1/\{project\_id\}/replications

    ```
    { 
        "replication": { 
           "server_group_id": "c79fba33-b165-4c69-80c1-d7e590691162", 
           "volume_id": "b6f71149-7b9c-4f36-8ff0-1c4809a6f2c2", 
           "name": "replication_name", 
           "description": "replication_description" 
       } 
     }
    ```


## Response<a name="en-us_topic_0079693002_section36549175"></a>

-   Parameter description

    <a name="table155991608555"></a>
    <table><thead align="left"><tr id="row460510055518"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p11759599336"><a name="p11759599336"></a><a name="p11759599336"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p67517591332"><a name="p67517591332"></a><a name="p67517591332"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p1875659103317"><a name="p1875659103317"></a><a name="p1875659103317"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row86164025512"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p775135943316"><a name="p775135943316"></a><a name="p775135943316"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p27675923314"><a name="p27675923314"></a><a name="p27675923314"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p276859193317"><a name="p276859193317"></a><a name="p276859193317"></a>Specifies the job ID.</p>
    <p id="p66521206545"><a name="p66521206545"></a><a name="p66521206545"></a>This is a returned parameter when the asynchronous API command is issued successfully. For details about the task execution result, see the description in <a href="querying-the-job-status.md">Querying the Job Status</a>.</p>
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


