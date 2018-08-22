# Updating Subnet Information<a name="EN-US_TOPIC_0020090593"></a>

## Function<a name="section52667802"></a>

This interface is used to update information about a subnet.

## URI<a name="section4248175"></a>

-   PUT /v1/\{tenant\_id\}/vpcs/\{vpc\_id\}/subnets/\{subnet\_id\}
-   Parameter description

    <a name="table27806533"></a><table><thead align="left"><tr id="row25717600"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p2750866"><a name="p2750866"></a><a name="p2750866"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p21493617"><a name="p21493617"></a><a name="p21493617"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p63261412"><a name="p63261412"></a><a name="p63261412"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23900756"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p56913064"><a name="p56913064"></a><a name="p56913064"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p46555465"><a name="p46555465"></a><a name="p46555465"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p12896286"><a name="p12896286"></a><a name="p12896286"></a>Specifies the tenant ID of the operator.</p>
    </td>
    </tr>
    <tr id="row41240337122055"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p52133024122055"><a name="p52133024122055"></a><a name="p52133024122055"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p4532040312214"><a name="p4532040312214"></a><a name="p4532040312214"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p58002403122055"><a name="p58002403122055"></a><a name="p58002403122055"></a>Specifies the ID of the subnet VPC.</p>
    </td>
    </tr>
    <tr id="row48957711"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p6151694"><a name="p6151694"></a><a name="p6151694"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p28525238"><a name="p28525238"></a><a name="p28525238"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p28842926"><a name="p28842926"></a><a name="p28842926"></a>Specifies the subnet ID, which uniquely identifies the subnet.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section38233575"></a>

-   Parameter description

    <a name="table42592295151022"></a><table><thead align="left"><tr id="row13964015151022"><th class="cellrowborder" valign="top" width="12.4%" id="mcps1.1.5.1.1"><p id="p57343407151022"><a name="p57343407151022"></a><a name="p57343407151022"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.990000000000002%" id="mcps1.1.5.1.2"><p id="p14304400151022"><a name="p14304400151022"></a><a name="p14304400151022"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.5.1.3"><p id="p17805753151022"><a name="p17805753151022"></a><a name="p17805753151022"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.18%" id="mcps1.1.5.1.4"><p id="p32979923151022"><a name="p32979923151022"></a><a name="p32979923151022"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54128134151022"><td class="cellrowborder" valign="top" width="12.4%" headers="mcps1.1.5.1.1 "><p id="p22302713151022"><a name="p22302713151022"></a><a name="p22302713151022"></a>subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.5.1.2 "><p id="p61689300151022"><a name="p61689300151022"></a><a name="p61689300151022"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.5.1.3 "><p id="p30777408151022"><a name="p30777408151022"></a><a name="p30777408151022"></a><em id="i8561220151022"><a name="i8561220151022"></a><a name="i8561220151022"></a>Dictionary data structure</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.1.5.1.4 "><p id="p22370187151022"><a name="p22370187151022"></a><a name="p22370187151022"></a>Specifies the subnet objects.</p>
    </td>
    </tr>
    </tbody>
    </table>

    Descriptions of  **subnet**  fields

    <a name="table45027976"></a><table><thead align="left"><tr id="row34359256"><th class="cellrowborder" valign="top" width="20.862086208620862%" id="mcps1.1.5.1.1"><p id="p31636323"><a name="p31636323"></a><a name="p31636323"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.11201120112011%" id="mcps1.1.5.1.2"><p id="p12405375"><a name="p12405375"></a><a name="p12405375"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.661466146614663%" id="mcps1.1.5.1.3"><p id="p3774167175923"><a name="p3774167175923"></a><a name="p3774167175923"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.364436443644365%" id="mcps1.1.5.1.4"><p id="p65311315"><a name="p65311315"></a><a name="p65311315"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55725192"><td class="cellrowborder" valign="top" width="20.862086208620862%" headers="mcps1.1.5.1.1 "><p id="p17446726"><a name="p17446726"></a><a name="p17446726"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.1.5.1.2 "><p id="p3898676"><a name="p3898676"></a><a name="p3898676"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.661466146614663%" headers="mcps1.1.5.1.3 "><p id="p37272111175923"><a name="p37272111175923"></a><a name="p37272111175923"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.364436443644365%" headers="mcps1.1.5.1.4 "><p id="p47357306"><a name="p47357306"></a><a name="p47357306"></a>Specifies the subnet name.</p>
    <p id="p10736577"><a name="p10736577"></a><a name="p10736577"></a>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</p>
    </td>
    </tr>
    <tr id="row64356400"><td class="cellrowborder" valign="top" width="20.862086208620862%" headers="mcps1.1.5.1.1 "><p id="p45485936"><a name="p45485936"></a><a name="p45485936"></a>dhcp_enable</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.1.5.1.2 "><p id="p60482217"><a name="p60482217"></a><a name="p60482217"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.661466146614663%" headers="mcps1.1.5.1.3 "><p id="p66251028175923"><a name="p66251028175923"></a><a name="p66251028175923"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.364436443644365%" headers="mcps1.1.5.1.4 "><p id="p648261621802"><a name="p648261621802"></a><a name="p648261621802"></a>Specifies whether the DHCP function is enabled for the subnet.</p>
    <p id="p14913854"><a name="p14913854"></a><a name="p14913854"></a>The value can be <strong>true</strong>&nbsp;or&nbsp;<strong>false</strong>.</p>
    <p id="p6965"><a name="p6965"></a><a name="p6965"></a>If this parameter is left blank, it is set to <strong>true</strong> by default.</p>
    </td>
    </tr>
    <tr id="row62687"><td class="cellrowborder" valign="top" width="20.862086208620862%" headers="mcps1.1.5.1.1 "><p id="p5077725"><a name="p5077725"></a><a name="p5077725"></a>primary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.1.5.1.2 "><p id="p8642591"><a name="p8642591"></a><a name="p8642591"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.661466146614663%" headers="mcps1.1.5.1.3 "><p id="p64733037175923"><a name="p64733037175923"></a><a name="p64733037175923"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.364436443644365%" headers="mcps1.1.5.1.4 "><p id="p59325057"><a name="p59325057"></a><a name="p59325057"></a>Specifies the IP address of DNS server 1 on the subnet.</p>
    <p id="p64163473"><a name="p64163473"></a><a name="p64163473"></a>The value must be a valid IP address.</p>
    </td>
    </tr>
    <tr id="row40600350"><td class="cellrowborder" valign="top" width="20.862086208620862%" headers="mcps1.1.5.1.1 "><p id="p294043"><a name="p294043"></a><a name="p294043"></a>secondary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.1.5.1.2 "><p id="p23817504"><a name="p23817504"></a><a name="p23817504"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.661466146614663%" headers="mcps1.1.5.1.3 "><p id="p8884643175923"><a name="p8884643175923"></a><a name="p8884643175923"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.364436443644365%" headers="mcps1.1.5.1.4 "><p id="p48873995"><a name="p48873995"></a><a name="p48873995"></a>Specifies the IP address of DNS server 2 on the subnet.</p>
    <p id="p37212772"><a name="p37212772"></a><a name="p37212772"></a>The value must be a valid IP address.</p>
    </td>
    </tr>
    <tr id="row4104651911530"><td class="cellrowborder" valign="top" width="20.862086208620862%" headers="mcps1.1.5.1.1 "><p id="p3643375711530"><a name="p3643375711530"></a><a name="p3643375711530"></a>dnsList</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.1.5.1.2 "><p id="p787474711538"><a name="p787474711538"></a><a name="p787474711538"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.661466146614663%" headers="mcps1.1.5.1.3 "><p id="p10991411530"><a name="p10991411530"></a><a name="p10991411530"></a>List</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.364436443644365%" headers="mcps1.1.5.1.4 "><p id="p890310611530"><a name="p890310611530"></a><a name="p890310611530"></a>Specifies the DNS server address list of a subnet. This field is required if you need to use more than two DNS servers.</p>
    <p id="p199198691169"><a name="p199198691169"></a><a name="p199198691169"></a>This parameter value is the superset of both DNS server address 1 and DNS server address 2.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
      "subnet":
             {
              "name": "subnetqq",
              "dhcp_enable": "false",
              "primary_dns": "114.xx.xx.115",
              "secondary_dns": "114.xx.xx.116"
              }
    }
    ```


## Response<a name="section8557861"></a>

-   Parameter description

    <a name="table55739938151015"></a><table><thead align="left"><tr id="row19341165151015"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.1.4.1.1"><p id="p23130572151015"><a name="p23130572151015"></a><a name="p23130572151015"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.1.4.1.2"><p id="p26547244151015"><a name="p26547244151015"></a><a name="p26547244151015"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.1.4.1.3"><p id="p2843132151015"><a name="p2843132151015"></a><a name="p2843132151015"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row28967149151015"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.1.4.1.1 "><p id="p64637734151015"><a name="p64637734151015"></a><a name="p64637734151015"></a>subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.1.4.1.2 "><p id="p27267219151015"><a name="p27267219151015"></a><a name="p27267219151015"></a><em id="i8561220151022_1"><a name="i8561220151022_1"></a><a name="i8561220151022_1"></a>Dictionary data structure</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.1.4.1.3 "><p id="p13579079151015"><a name="p13579079151015"></a><a name="p13579079151015"></a>Specifies the subnet objects.</p>
    </td>
    </tr>
    </tbody>
    </table>

    Descriptions of  **subnet**  fields

    <a name="table1210700"></a><table><thead align="left"><tr id="row43388973"><th class="cellrowborder" valign="top" width="24.57%" id="mcps1.1.4.1.1"><p id="p24845910"><a name="p24845910"></a><a name="p24845910"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.68%" id="mcps1.1.4.1.2"><p id="p697309418033"><a name="p697309418033"></a><a name="p697309418033"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.74999999999999%" id="mcps1.1.4.1.3"><p id="p6587942"><a name="p6587942"></a><a name="p6587942"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63861276"><td class="cellrowborder" valign="top" width="24.57%" headers="mcps1.1.4.1.1 "><p id="p5380904"><a name="p5380904"></a><a name="p5380904"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.68%" headers="mcps1.1.4.1.2 "><p id="p2794974018033"><a name="p2794974018033"></a><a name="p2794974018033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.74999999999999%" headers="mcps1.1.4.1.3 "><p id="p4849307"><a name="p4849307"></a><a name="p4849307"></a>Specifies a resource ID in UUID format.</p>
    </td>
    </tr>
    <tr id="row43643771"><td class="cellrowborder" valign="top" width="24.57%" headers="mcps1.1.4.1.1 "><p id="p45484537"><a name="p45484537"></a><a name="p45484537"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.68%" headers="mcps1.1.4.1.2 "><p id="p4933643818033"><a name="p4933643818033"></a><a name="p4933643818033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.74999999999999%" headers="mcps1.1.4.1.3 "><p id="p52583897"><a name="p52583897"></a><a name="p52583897"></a>Specifies the status of the subnet.</p>
    <p id="p3493029"><a name="p3493029"></a><a name="p3493029"></a>The value can be <strong>ACTIVE</strong>,&nbsp;<strong>DOWN</strong>,&nbsp;<strong>UNKNOWN</strong>, or&nbsp;<strong>ERROR</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "subnet": {
            "id": "4779ab1c-7c1a-44b1-a02e-93dfc361b32d",
            "status": "ACTIVE"
        }
    }
    ```


## Returned Value<a name="section9911889"></a>

-   Normal

    200

-   Abnormal

    <a name="table1344289395411"></a><table><thead align="left"><tr id="row2578423195411"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="p814794695411"><a name="p814794695411"></a><a name="p814794695411"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="p5600386195411"><a name="p5600386195411"></a><a name="p5600386195411"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4001889795411"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p2030522195411"><a name="p2030522195411"></a><a name="p2030522195411"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3411023495411"><a name="p3411023495411"></a><a name="p3411023495411"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row3855665695411"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3608146595411"><a name="p3608146595411"></a><a name="p3608146595411"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p3691755895411"><a name="p3691755895411"></a><a name="p3691755895411"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row6382257295411"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p224584395411"><a name="p224584395411"></a><a name="p224584395411"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p4769558695411"><a name="p4769558695411"></a><a name="p4769558695411"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row2660709795411"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p769122495411"><a name="p769122495411"></a><a name="p769122495411"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p1900939695411"><a name="p1900939695411"></a><a name="p1900939695411"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row3686683695411"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3342370195411"><a name="p3342370195411"></a><a name="p3342370195411"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2296525595411"><a name="p2296525595411"></a><a name="p2296525595411"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row536070595411"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3156399995411"><a name="p3156399995411"></a><a name="p3156399995411"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p654713795411"><a name="p654713795411"></a><a name="p654713795411"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row5892424095411"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p813409995411"><a name="p813409995411"></a><a name="p813409995411"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5488232095411"><a name="p5488232095411"></a><a name="p5488232095411"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row2417883595411"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1232859995411"><a name="p1232859995411"></a><a name="p1232859995411"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5909245695411"><a name="p5909245695411"></a><a name="p5909245695411"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row6207005695411"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p6161864695411"><a name="p6161864695411"></a><a name="p6161864695411"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2505446995411"><a name="p2505446995411"></a><a name="p2505446995411"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row2416363795411"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1109754395411"><a name="p1109754395411"></a><a name="p1109754395411"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2648580695411"><a name="p2648580695411"></a><a name="p2648580695411"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row3704566995411"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p4790922295411"><a name="p4790922295411"></a><a name="p4790922295411"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p5544177595411"><a name="p5544177595411"></a><a name="p5544177595411"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row2921393595411"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p1751852095411"><a name="p1751852095411"></a><a name="p1751852095411"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p971401495411"><a name="p971401495411"></a><a name="p971401495411"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row2031726395411"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p3508557895411"><a name="p3508557895411"></a><a name="p3508557895411"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p2335957495411"><a name="p2335957495411"></a><a name="p2335957495411"></a>Failed to complete the request because the service is unavailable.</p>
    </td>
    </tr>
    <tr id="row890957895411"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="p5058718595411"><a name="p5058718595411"></a><a name="p5058718595411"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="p392134195411"><a name="p392134195411"></a><a name="p392134195411"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section85821649202813"></a>

For details, see section  [Error Codes](error-codes-27.md).

