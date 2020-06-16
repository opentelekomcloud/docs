# Performing a Failover for a Protection Group<a name="sdrs_05_0408"></a>

## Function<a name="en-us_topic_0079693002_section34649765"></a>

When the production site of a protection group becomes faulty, services of the protection group are switched over to the DR site, and servers and disks at the DR site start. After a failover is performed, the current production site of the protection group will become the DR site before the failover. Data synchronization between the production and DR sites will stop. To resume the data synchronization, you need to perform steps provided in  [Enabling Protection or Enabling Protection Again for a Protection Group](enabling-protection-or-enabling-protection-again-for-a-protection-group.md)  to enable protection.

## Constraints and Limitations<a name="section162571021113217"></a>

-   The protection group must have replication pairs.
-   **status**  of the protection group must be  **protected**,  **error-failing-over**, or  **error-reversing**.
-   If the server at the production site or DR site in a protected instance is deleted using the native interface, no operations can be performed on the protected instance or the protection group of the protected instance.

## Restrictions on Logging In to a Server After You Perform a Planned Failover, Failover, or DR Drill for the First Time<a name="section330514140125"></a>

-   For servers with Cloud-Init/Cloudbase-Init installed, after you perform a planned failover, failover, or DR drill for the first time, Cloud-Init/Cloudbase-Init will start when the servers start for the first time to inject the initial data. The password or key pair for logging in to the production site server, DR site server, or DR drill server will change.
-   For servers without Cloud-Init/Cloudbase-Init installed, the password or key pair for logging in to the production site, DR site server, or DR drill server will not change after you perform a planned failover or failover for the first time.

The following describes an example of server login restrictions after you perform a planned failover or failover for the first time. For details about the login restrictions for the DR drill server, see the login restrictions for the DR site server in this scenario.

Server A and server B are deployed. After the first time planned failover or failover, the production site server and DR site server are listed as follows.

**Table  1**  Production site and DR site servers after a planned failover or failover

<a name="en-us_topic_0110981899_table92017496206"></a>
<table><thead align="left"><tr id="en-us_topic_0110981899_row92016497207"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0110981899_p22014982019"><a name="en-us_topic_0110981899_p22014982019"></a><a name="en-us_topic_0110981899_p22014982019"></a>-</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0110981899_p12201349182012"><a name="en-us_topic_0110981899_p12201349182012"></a><a name="en-us_topic_0110981899_p12201349182012"></a>Production Site Server</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0110981899_p721184962020"><a name="en-us_topic_0110981899_p721184962020"></a><a name="en-us_topic_0110981899_p721184962020"></a>DR Site Server</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0110981899_row19211749182018"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110981899_p142194942018"><a name="en-us_topic_0110981899_p142194942018"></a><a name="en-us_topic_0110981899_p142194942018"></a>Before</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0110981899_p5219498200"><a name="en-us_topic_0110981899_p5219498200"></a><a name="en-us_topic_0110981899_p5219498200"></a>A</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110981899_p16219493202"><a name="en-us_topic_0110981899_p16219493202"></a><a name="en-us_topic_0110981899_p16219493202"></a>B</p>
</td>
</tr>
<tr id="en-us_topic_0110981899_row1221114972012"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0110981899_p102184942014"><a name="en-us_topic_0110981899_p102184942014"></a><a name="en-us_topic_0110981899_p102184942014"></a>After</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0110981899_p421849152011"><a name="en-us_topic_0110981899_p421849152011"></a><a name="en-us_topic_0110981899_p421849152011"></a>B</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0110981899_p82104942011"><a name="en-us_topic_0110981899_p82104942011"></a><a name="en-us_topic_0110981899_p82104942011"></a>A</p>
</td>
</tr>
</tbody>
</table>

In this case, the detailed login restrictions are as follows:

Scenario 1: Server A runs Windows and does not have Cloudbase-Init installed. After the first time planned failover or failover:

-   If you choose to use a password for the server login, use the password of server A to log in to the production site server B or DR site server A.
-   If you choose to use a key pair for the server login, use the password obtained from server A to log in to the production site server B or DR site server A.

>![](/images/icon-note.gif) **NOTE:**   
>From the second time planned failover or failover, the login password or key pair of the server without Cloudbase-Init installed will remain the same. Take servers listed in  [Table 1](#en-us_topic_0110981899_table92017496206)  as an example.  
>You can use the password of server A to log in to the production site server or DR site server.  

Scenario 2: Server A runs Windows and already has Cloudbase-Init installed. After the first time planned failover or failover:

-   If you choose to use a password for the server login, check whether Cloudbase-Init is started.

    If Cloudbase-Init is not started \(normally within three to five minutes after the production site server starts\), you can use the password of server B for the login.

    After the Cloudbase-Init is started, the login password of server B set before the planned failover or failover becomes invalid. You need to reset the login password of server B and then use the new password to log in to server B.

-   If you choose to use a key pair for the server login, check whether Cloudbase-Init is started.

    If Cloudbase-Init is not started \(normally within three to five minutes after the production site server starts\), you can use the password of server B for the login.

    After the Cloudbase-Init is started, the login password of server B obtained before the planned failover or failover becomes invalid. You need to obtain the login password of server B again.


>![](/images/icon-note.gif) **NOTE:**   
>From the second time planned failover or failover, the login password or key pair of the server with Cloudbase-Init installed will remain the same. Take servers listed in  [Table 1](#en-us_topic_0110981899_table92017496206)  as an example.  
>-   Login using a password: Reset the password of server B and use the new password to log in to server B after the first time planned failover or failover.  
>-   Login using a key pair: Obtain the password of server B and use the obtained password to log in to server B after the first time planned failover or failover.  

Scenario 3: Server A runs Linux. After the first time planned failover or failover:

-   If you choose to use a password for the server login, use the password of server A to log in to the production site server B or DR site server A. 

    If the login password of server A is not changed before the planned failover or failover, use the login password configured when server A is created after the planned failover or failover. 

    If the login password of server A is changed before the planned failover or failover, use the new login password after the planned failover or failover.

    >![](/images/icon-note.gif) **NOTE:**   
    >For ECSs running OSs other than CoreOS, the login password does not change after the first-time planned failover or failover.  
    >For ECSs running CoreOS, the login password of server A will restore to the initial one after the first-time planned failover or failover. Therefore, you need to use the login password configured when server A is created to log in to production site server A or DR site server B.  

-   If you choose to use a key pair for the server login, use the key pair of server A to log in to the production site server B or DR site server A in SSH mode. 

## URI<a name="en-us_topic_0079693002_section39390935"></a>

-   URI format

    POST /v1/\{project\_id\}/server-groups/\{server\_group\_id\}/action

-   Parameter description

    <a name="en-us_topic_0079693002_table63321005"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row37593218"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.5.1.1"><p id="p14696181410125"><a name="p14696181410125"></a><a name="p14696181410125"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.2"><p id="p46961114101214"><a name="p46961114101214"></a><a name="p46961114101214"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.3"><p id="p9696514111215"><a name="p9696514111215"></a><a name="p9696514111215"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.1.5.1.4"><p id="p186961514171212"><a name="p186961514171212"></a><a name="p186961514171212"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row29123463"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.1 "><p id="p196961814121213"><a name="p196961814121213"></a><a name="p196961814121213"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.2 "><p id="p8696141431217"><a name="p8696141431217"></a><a name="p8696141431217"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p1069651451215"><a name="p1069651451215"></a><a name="p1069651451215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="p969612149122"><a name="p969612149122"></a><a name="p969612149122"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row89481211122513"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.5.1.1 "><p id="p4696114101218"><a name="p4696114101218"></a><a name="p4696114101218"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.2 "><p id="p17696814141216"><a name="p17696814141216"></a><a name="p17696814141216"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p126963149120"><a name="p126963149120"></a><a name="p126963149120"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="p469614149123"><a name="p469614149123"></a><a name="p469614149123"></a>Specifies the ID of a protection group.</p>
    <p id="p1789515183119"><a name="p1789515183119"></a><a name="p1789515183119"></a>For details, see <a href="querying-protection-groups.md">Querying Protection Groups</a>.</p>
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
    <tbody><tr id="en-us_topic_0079693002_row27990155"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p1597715414259"><a name="p1597715414259"></a><a name="p1597715414259"></a>failover-server-group</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p14977641152511"><a name="p14977641152511"></a><a name="p14977641152511"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p119772041162510"><a name="p119772041162510"></a><a name="p119772041162510"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p1697715415254"><a name="p1697715415254"></a><a name="p1697715415254"></a>Performs a failover for a protection group.</p>
    <p id="p1519412563318"><a name="p1519412563318"></a><a name="p1519412563318"></a>This parameter is left empty by default.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    POST https://\{Endpoint\}/v1/\{project\_id\}/server-groups/40df180b-9fe2-471a-8c64-1b758dc84189/action

    ```
    {
        "failover-server-group": {}
    }
    ```


## Response<a name="en-us_topic_0079693002_section36549175"></a>

-   Parameter description

    <a name="table155991608555"></a>
    <table><thead align="left"><tr id="row460510055518"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p125611510173"><a name="p125611510173"></a><a name="p125611510173"></a><strong id="b842352706151210"><a name="b842352706151210"></a><a name="b842352706151210"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p1456195171718"><a name="p1456195171718"></a><a name="p1456195171718"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p12561651177"><a name="p12561651177"></a><a name="p12561651177"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row86164025512"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p4561551711"><a name="p4561551711"></a><a name="p4561551711"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p35635121719"><a name="p35635121719"></a><a name="p35635121719"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p15561951175"><a name="p15561951175"></a><a name="p15561951175"></a>Specifies the returned parameter when the asynchronous API command is issued successfully. For details about the task execution result, see the description in <a href="querying-the-job-status.md">Querying the Job Status</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "job_id": "ff8080826adfae02016ae2d123fc05ed"
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


