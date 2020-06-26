# Creating a Protection Group<a name="sdrs_05_0401"></a>

## Function<a name="en-us_topic_0079693002_section34649765"></a>

This API is used to create a protection group.

>![](/images/icon-note.gif) **NOTE:**   
>This API is an asynchronous interface. If this API is invoked successfully, the request is issued. To query the creation result, invoke the API described in  [Querying the Job Status](querying-the-job-status.md).  

## Constraints and Limitations<a name="section192520370189"></a>

None

## URI<a name="en-us_topic_0079693002_section39390935"></a>

-   URI format

    POST /v1/\{project\_id\}/server-groups

-   Parameter description

    <a name="en-us_topic_0079693002_table63321005"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row37593218"><th class="cellrowborder" valign="top" width="24%" id="mcps1.1.5.1.1"><p id="en-us_topic_0079693002_p25151854"><a name="en-us_topic_0079693002_p25151854"></a><a name="en-us_topic_0079693002_p25151854"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="12%" id="mcps1.1.5.1.2"><p id="en-us_topic_0079693002_p1556805116115"><a name="en-us_topic_0079693002_p1556805116115"></a><a name="en-us_topic_0079693002_p1556805116115"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.5.1.3"><p id="p696973018520"><a name="p696973018520"></a><a name="p696973018520"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.1.5.1.4"><p id="en-us_topic_0079693002_p2565159161120"><a name="en-us_topic_0079693002_p2565159161120"></a><a name="en-us_topic_0079693002_p2565159161120"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row29123463"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.5.1.1 "><p id="p199411839185611"><a name="p199411839185611"></a><a name="p199411839185611"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.1.5.1.2 "><p id="p9945103985612"><a name="p9945103985612"></a><a name="p9945103985612"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.3 "><p id="p15969153075211"><a name="p15969153075211"></a><a name="p15969153075211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.5.1.4 "><p id="p17947113916566"><a name="p17947113916566"></a><a name="p17947113916566"></a>Specifies the project ID.</p>
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
    <tbody><tr id="en-us_topic_0079693002_row27990155"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p2614164612462"><a name="p2614164612462"></a><a name="p2614164612462"></a>server_group</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p106141846134615"><a name="p106141846134615"></a><a name="p106141846134615"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p89495395316"><a name="p89495395316"></a><a name="p89495395316"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p894185316533"><a name="p894185316533"></a><a name="p894185316533"></a>Specifies the information about a protection group.</p>
    <p id="p2576163019326"><a name="p2576163019326"></a><a name="p2576163019326"></a>For details, see <a href="#table5487195132418">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **server\_group**  field description

    <a name="table5487195132418"></a>
    <table><thead align="left"><tr id="row1349405112411"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p17496165192412"><a name="p17496165192412"></a><a name="p17496165192412"></a><strong id="b842352706151210"><a name="b842352706151210"></a><a name="b842352706151210"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p8497135116244"><a name="p8497135116244"></a><a name="p8497135116244"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p1649995172418"><a name="p1649995172418"></a><a name="p1649995172418"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p155011151122411"><a name="p155011151122411"></a><a name="p155011151122411"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5510351172420"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p851015142419"><a name="p851015142419"></a><a name="p851015142419"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p1951385152415"><a name="p1951385152415"></a><a name="p1951385152415"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p115154512243"><a name="p115154512243"></a><a name="p115154512243"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p15171251182415"><a name="p15171251182415"></a><a name="p15171251182415"></a>Specifies the name of a protection group. The name can contain a maximum of 64 bytes. The value can contain only letters (a to z and A to Z), digits (0 to 9), decimal points (.), underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row25181951172411"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p451945152411"><a name="p451945152411"></a><a name="p451945152411"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p1252112511242"><a name="p1252112511242"></a><a name="p1252112511242"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p152395110240"><a name="p152395110240"></a><a name="p152395110240"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p1352415182413"><a name="p1352415182413"></a><a name="p1352415182413"></a>Specifies the description of a protection group. The description can contain a maximum of 64 bytes. The value cannot contain the left angle bracket (&lt;) or right angle bracket (&gt;).</p>
    </td>
    </tr>
    <tr id="row1652455152410"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p145261351182420"><a name="p145261351182420"></a><a name="p145261351182420"></a>source_availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p135272510240"><a name="p135272510240"></a><a name="p135272510240"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p1252817518244"><a name="p1252817518244"></a><a name="p1252817518244"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p15301951192418"><a name="p15301951192418"></a><a name="p15301951192418"></a>Specifies the production site AZ of a protection group.</p>
    <p id="p490217144311"><a name="p490217144311"></a><a name="p490217144311"></a>You can obtain this value by calling the API described in <a href="active_active_domain.rst">Active-Active Domain</a>.</p>
    </td>
    </tr>
    <tr id="row115308519246"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p2053265113249"><a name="p2053265113249"></a><a name="p2053265113249"></a>target_availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p3532105110246"><a name="p3532105110246"></a><a name="p3532105110246"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p12534115152413"><a name="p12534115152413"></a><a name="p12534115152413"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p17536851192414"><a name="p17536851192414"></a><a name="p17536851192414"></a>Specifies the DR site AZ of a protection group.</p>
    <p id="p34672113453"><a name="p34672113453"></a><a name="p34672113453"></a>You can obtain this value by calling the API described in <a href="active_active_domain.rst">Active-Active Domain</a>.</p>
    </td>
    </tr>
    <tr id="row5536125132413"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p45381051132420"><a name="p45381051132420"></a><a name="p45381051132420"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p14539195118243"><a name="p14539195118243"></a><a name="p14539195118243"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p35411751142414"><a name="p35411751142414"></a><a name="p35411751142414"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p17543165119241"><a name="p17543165119241"></a><a name="p17543165119241"></a>Specifies the ID of an active-active domain.</p>
    <p id="p42271928194513"><a name="p42271928194513"></a><a name="p42271928194513"></a>You can obtain this value by calling the API described in <a href="active_active_domain.rst">Active-Active Domain</a>.</p>
    </td>
    </tr>
    <tr id="row25431851192415"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p14545175152419"><a name="p14545175152419"></a><a name="p14545175152419"></a>source_vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p25462517241"><a name="p25462517241"></a><a name="p25462517241"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p5547105132412"><a name="p5547105132412"></a><a name="p5547105132412"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p55471251112412"><a name="p55471251112412"></a><a name="p55471251112412"></a>Specifies the ID of the VPC for the production site.</p>
    </td>
    </tr>
    <tr id="row9547175111245"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1755013511245"><a name="p1755013511245"></a><a name="p1755013511245"></a>dr_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p1155225111244"><a name="p1155225111244"></a><a name="p1155225111244"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p25531951172417"><a name="p25531951172417"></a><a name="p25531951172417"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p2554155162415"><a name="p2554155162415"></a><a name="p2554155162415"></a>Specifies the deployment model. The default value is <strong id="b1963647298"><a name="b1963647298"></a><a name="b1963647298"></a>migration</strong>, indicating migration within a VPC.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    POST https://\{endpoint\}/v1/\{project\_id\}/server-groups

    ```
    { 
    	"server_group":
    	{ 
    		"name":"testname", 
    		"description":"description", 
    		"source_availability_zone":"eu-de-01", 
    		"target_availability_zone":"eu-de-02", 
    		"domain_id":"fb4bb8e3-a574-4437-a156-78c916aeea4d",
    		"source_vpc_id":"046852ef-c49d-409b-8389-546aaaa5701f",
    		"dr_type":"migration",
                    
    	} 
    }
    ```


## Response<a name="en-us_topic_0079693002_section36549175"></a>

-   Parameter description

    <a name="table155991608555"></a>
    <table><thead align="left"><tr id="row460510055518"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p56078010555"><a name="p56078010555"></a><a name="p56078010555"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p961219016552"><a name="p961219016552"></a><a name="p961219016552"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p186139012557"><a name="p186139012557"></a><a name="p186139012557"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row86164025512"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p174529129479"><a name="p174529129479"></a><a name="p174529129479"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p12452812124712"><a name="p12452812124712"></a><a name="p12452812124712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p1545221254712"><a name="p1545221254712"></a><a name="p1545221254712"></a>Specifies the job ID.</p>
    <p id="p1169357114917"><a name="p1169357114917"></a><a name="p1169357114917"></a>Specifies the returned parameter when the asynchronous API command is issued successfully. For details about the task execution result, see the description in <a href="querying-the-job-status.md">Querying the Job Status</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    { 
       "job_id": "0000000062db92d70162db9d200f000a" 
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


