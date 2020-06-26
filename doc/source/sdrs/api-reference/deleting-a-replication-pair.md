# Deleting a Replication Pair<a name="sdrs_05_0602"></a>

## Function<a name="en-us_topic_0079693002_section34649765"></a>

This API is used to delete a specified replication pair.

## Constraints and Limitations<a name="section7484742581"></a>

-   **status**  of the protection group must be  **available**,  **protected**,  **failed-over**,  **error-starting**,  **error-stopping**,  **error-reversing**, or  **error-failing-over**,  **error-deleting**, or  **error-reprotecting**.
-   **status**  of the replication pair must be  **available**,  **protected**,  **failed-over**,  **error**,  **error-starting**,  **error-stopping**,  **error-reversing**,  **error-failing-over**,  **error-deleting**,  **error-reprotecting**,  **error-attaching**,  **error-extending**,  **invalid**, or  **fault**.
-   The replication pair has not been attached to a protected instance.

## URI<a name="en-us_topic_0079693002_section39390935"></a>

-   URI format

    DELETE /v1/\{project\_id\}/replications/\{replication\_id\}

-   Parameter description

    <a name="en-us_topic_0079693002_table63321005"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row37593218"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.5.1.1"><p id="p1194811468343"><a name="p1194811468343"></a><a name="p1194811468343"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.1.5.1.2"><p id="p13948164617349"><a name="p13948164617349"></a><a name="p13948164617349"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.1.5.1.3"><p id="p179481446123414"><a name="p179481446123414"></a><a name="p179481446123414"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.1.5.1.4"><p id="p8948246133413"><a name="p8948246133413"></a><a name="p8948246133413"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row29123463"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p294819466347"><a name="p294819466347"></a><a name="p294819466347"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p13948104613413"><a name="p13948104613413"></a><a name="p13948104613413"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.3 "><p id="p10948124623419"><a name="p10948124623419"></a><a name="p10948124623419"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="p694894613345"><a name="p694894613345"></a><a name="p694894613345"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row96111753145510"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p1894813464348"><a name="p1894813464348"></a><a name="p1894813464348"></a>replication_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.5.1.2 "><p id="p6948104673412"><a name="p6948104673412"></a><a name="p6948104673412"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.3 "><p id="p199488468342"><a name="p199488468342"></a><a name="p199488468342"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="p1394974603418"><a name="p1394974603418"></a><a name="p1394974603418"></a>Specifies the ID of a replication pair.</p>
    <p id="p19001919195714"><a name="p19001919195714"></a><a name="p19001919195714"></a>You can obtain this value by calling the API described in <a href="querying-replication-pairs.md">Querying Replication Pairs</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079693002_section18974100"></a>

-   Parameter description

    <a name="en-us_topic_0079693002_table54932709"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row41882373"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p16380711183510"><a name="p16380711183510"></a><a name="p16380711183510"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.5.1.2"><p id="p16380111113358"><a name="p16380111113358"></a><a name="p16380111113358"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.3"><p id="p238019115351"><a name="p238019115351"></a><a name="p238019115351"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.1.5.1.4"><p id="p19380151113352"><a name="p19380151113352"></a><a name="p19380151113352"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row434005863411"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p19380171113510"><a name="p19380171113510"></a><a name="p19380171113510"></a>replication</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p7380131183514"><a name="p7380131183514"></a><a name="p7380131183514"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p1038021117355"><a name="p1038021117355"></a><a name="p1038021117355"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p8380191113353"><a name="p8380191113353"></a><a name="p8380191113353"></a>Specifies the information about a replication pair.</p>
    <p id="p44108366012"><a name="p44108366012"></a><a name="p44108366012"></a>For details, see <a href="#table38261646898">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **replication**  field description

    <a name="table38261646898"></a>
    <table><thead align="left"><tr id="row482618461597"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p14827154612911"><a name="p14827154612911"></a><a name="p14827154612911"></a><strong id="b040162210214"><a name="b040162210214"></a><a name="b040162210214"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.180000000000001%" id="mcps1.2.5.1.2"><p id="p1582714461919"><a name="p1582714461919"></a><a name="p1582714461919"></a><strong id="b204482271210"><a name="b204482271210"></a><a name="b204482271210"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.84%" id="mcps1.2.5.1.3"><p id="p188272461913"><a name="p188272461913"></a><a name="p188272461913"></a><strong id="b10500122815216"><a name="b10500122815216"></a><a name="b10500122815216"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.98%" id="mcps1.2.5.1.4"><p id="p9827446891"><a name="p9827446891"></a><a name="p9827446891"></a><strong id="b4952030723"><a name="b4952030723"></a><a name="b4952030723"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row148278465912"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p13827446897"><a name="p13827446897"></a><a name="p13827446897"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.180000000000001%" headers="mcps1.2.5.1.2 "><p id="p1882744618920"><a name="p1882744618920"></a><a name="p1882744618920"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.84%" headers="mcps1.2.5.1.3 "><p id="p1282714461193"><a name="p1282714461193"></a><a name="p1282714461193"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.98%" headers="mcps1.2.5.1.4 "><p id="p88273468917"><a name="p88273468917"></a><a name="p88273468917"></a>Specifies the ID of a protection group.</p>
    </td>
    </tr>
    <tr id="row98276461796"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p349675119210"><a name="p349675119210"></a><a name="p349675119210"></a>delete_target_volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.180000000000001%" headers="mcps1.2.5.1.2 "><p id="p168272046695"><a name="p168272046695"></a><a name="p168272046695"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.84%" headers="mcps1.2.5.1.3 "><p id="p1182710462918"><a name="p1182710462918"></a><a name="p1182710462918"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.98%" headers="mcps1.2.5.1.4 "><p id="p68279467911"><a name="p68279467911"></a><a name="p68279467911"></a>Specifies whether to delete the DR site disk. The default value is <strong id="b11313455566"><a name="b11313455566"></a><a name="b11313455566"></a>false</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    DELETE https://\{Endpoint\}/v1/\{project\_id\}/replications/b93bc1c4-67ee-45a1-bc8a-d022fdd28811

    ```
    { 
       "replication": {
           "server_group_id": "c79fba33-b165-4c69-80c1-d7e590691162",
            "delete_target_volume": false
       }
     }
    ```


## Response<a name="en-us_topic_0079693002_section36549175"></a>

-   Parameter description

    <a name="table155991608555"></a>
    <table><thead align="left"><tr id="row460510055518"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p1551112117368"><a name="p1551112117368"></a><a name="p1551112117368"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p13512122116363"><a name="p13512122116363"></a><a name="p13512122116363"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p051212218364"><a name="p051212218364"></a><a name="p051212218364"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row86164025512"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p4512321153612"><a name="p4512321153612"></a><a name="p4512321153612"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p3512421123616"><a name="p3512421123616"></a><a name="p3512421123616"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p165121121133615"><a name="p165121121133615"></a><a name="p165121121133615"></a>Specifies the job ID.</p>
    <p id="p6861199954"><a name="p6861199954"></a><a name="p6861199954"></a>This is a returned parameter when the asynchronous API command is issued successfully. For details about the task execution result, see the description in <a href="querying-the-job-status.md">Querying the Job Status</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    { 
       "job_id": "0000000011db92d34587db9d20df32ch" 
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


