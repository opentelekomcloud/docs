# Querying Subnets<a name="vpc_subnet01_0003"></a>

## Function<a name="section49967061"></a>

This API is used to query subnets using search criteria and to display the subnets in a list.

## URI<a name="section47050372"></a>

GET /v1/\{project\_id\}/subnets

Example:

```
GET https://{Endpoint}/v1/{project_id}/subnets?limit=10&marker=4779ab1c-7c1a-44b1-a02e-93dfc361b32d&vpc_id=3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85
```

**Table  1**  Parameter description

<a name="table42526340"></a>
<table><thead align="left"><tr id="row55636561"><th class="cellrowborder" valign="top" width="20.11201120112011%" id="mcps1.2.5.1.1"><p id="p10267631"><a name="p10267631"></a><a name="p10267631"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="18.04180418041804%" id="mcps1.2.5.1.2"><p id="p26371793"><a name="p26371793"></a><a name="p26371793"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.72137213721372%" id="mcps1.2.5.1.3"><p id="p6814361175820"><a name="p6814361175820"></a><a name="p6814361175820"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.12481248124813%" id="mcps1.2.5.1.4"><p id="p55740512"><a name="p55740512"></a><a name="p55740512"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18687619"><td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.5.1.1 "><p id="p37302179"><a name="p37302179"></a><a name="p37302179"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.04180418041804%" headers="mcps1.2.5.1.2 "><p id="p1577639"><a name="p1577639"></a><a name="p1577639"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.72137213721372%" headers="mcps1.2.5.1.3 "><p id="p15092369175820"><a name="p15092369175820"></a><a name="p15092369175820"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.12481248124813%" headers="mcps1.2.5.1.4 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row9248440"><td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.5.1.1 "><p id="p10926182"><a name="p10926182"></a><a name="p10926182"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="18.04180418041804%" headers="mcps1.2.5.1.2 "><p id="p12605589"><a name="p12605589"></a><a name="p12605589"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.72137213721372%" headers="mcps1.2.5.1.3 "><p id="p14522390175820"><a name="p14522390175820"></a><a name="p14522390175820"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.12481248124813%" headers="mcps1.2.5.1.4 "><p id="p28526205175853"><a name="p28526205175853"></a><a name="p28526205175853"></a>Specifies the start resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
</td>
</tr>
<tr id="row43066942"><td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.5.1.1 "><p id="p65870306"><a name="p65870306"></a><a name="p65870306"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="18.04180418041804%" headers="mcps1.2.5.1.2 "><p id="p33894570"><a name="p33894570"></a><a name="p33894570"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.72137213721372%" headers="mcps1.2.5.1.3 "><p id="p35462927175820"><a name="p35462927175820"></a><a name="p35462927175820"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48.12481248124813%" headers="mcps1.2.5.1.4 "><a name="ul17419193531"></a><a name="ul17419193531"></a><ul id="ul17419193531"><li>Specifies the number of records returned on each page.</li><li>The value ranges from 0 to intmax.</li></ul>
</td>
</tr>
<tr id="row4071301142654"><td class="cellrowborder" valign="top" width="20.11201120112011%" headers="mcps1.2.5.1.1 "><p id="p61339955142654"><a name="p61339955142654"></a><a name="p61339955142654"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.04180418041804%" headers="mcps1.2.5.1.2 "><p id="p2480462142654"><a name="p2480462142654"></a><a name="p2480462142654"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.72137213721372%" headers="mcps1.2.5.1.3 "><p id="p66699709142654"><a name="p66699709142654"></a><a name="p66699709142654"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.12481248124813%" headers="mcps1.2.5.1.4 "><p id="p2678389014283"><a name="p2678389014283"></a><a name="p2678389014283"></a>Specifies that the VPC ID is used as the filtering condition.</p>
<p id="p13743141181413"><a name="p13743141181413"></a><a name="p13743141181413"></a>This field is mandatory in the fine-grained authorization scenario based on enterprise projects.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section20800170"></a>

-   Request parameter

    None

-   Example request

    ```
    GET https://{Endpoint}/v1/{project_id}/subnets
    ```


## Response Message<a name="section52983808"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table162269121588"></a>
    <table><thead align="left"><tr id="row95582811588"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p360232861588"><a name="p360232861588"></a><a name="p360232861588"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.15%" id="mcps1.2.4.1.2"><p id="p584710571588"><a name="p584710571588"></a><a name="p584710571588"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59.51%" id="mcps1.2.4.1.3"><p id="p385351831588"><a name="p385351831588"></a><a name="p385351831588"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row343421581588"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p302514461588"><a name="p302514461588"></a><a name="p302514461588"></a>subnets</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.15%" headers="mcps1.2.4.1.2 "><p id="p26395826172022"><a name="p26395826172022"></a><a name="p26395826172022"></a>Array of <a href="#table946390317596">subnets</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="59.51%" headers="mcps1.2.4.1.3 "><p id="p530125231588"><a name="p530125231588"></a><a name="p530125231588"></a>Specifies the <a href="#table946390317596">subnets objects</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **subnets**  objects

    <a name="table946390317596"></a>
    <table><thead align="left"><tr id="row2260217717596"><th class="cellrowborder" valign="top" width="29.017098290170978%" id="mcps1.2.4.1.1"><p id="p1883706917596"><a name="p1883706917596"></a><a name="p1883706917596"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.6983301669833%" id="mcps1.2.4.1.2"><p id="p4259704317596"><a name="p4259704317596"></a><a name="p4259704317596"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.284571542845704%" id="mcps1.2.4.1.3"><p id="p2780847717596"><a name="p2780847717596"></a><a name="p2780847717596"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3789415517596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.2.4.1.1 "><p id="p4952771817596"><a name="p4952771817596"></a><a name="p4952771817596"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.2.4.1.2 "><p id="p1023955317596"><a name="p1023955317596"></a><a name="p1023955317596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.2.4.1.3 "><p id="p2409742517596"><a name="p2409742517596"></a><a name="p2409742517596"></a>Specifies a resource ID in UUID format.</p>
    </td>
    </tr>
    <tr id="row1555023417596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.2.4.1.1 "><p id="p5160943617596"><a name="p5160943617596"></a><a name="p5160943617596"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.2.4.1.2 "><p id="p4529288117596"><a name="p4529288117596"></a><a name="p4529288117596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.2.4.1.3 "><a name="ul23311559134110"></a><a name="ul23311559134110"></a><ul id="ul23311559134110"><li>Specifies the subnet name.</li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li></ul>
    </td>
    </tr>
    <tr id="row6838204320315"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.2.4.1.1 "><p id="p541524553114"><a name="p541524553114"></a><a name="p541524553114"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.2.4.1.2 "><p id="p0415745133114"><a name="p0415745133114"></a><a name="p0415745133114"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.2.4.1.3 "><a name="ul237215542179"></a><a name="ul237215542179"></a><ul id="ul237215542179"><li>Provides supplementary information about the subnet.</li><li>The value is a string of no more than 255 characters and cannot contain angle brackets (&lt; or &gt;).</li></ul>
    </td>
    </tr>
    <tr id="row94962917596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.2.4.1.1 "><p id="p981112017596"><a name="p981112017596"></a><a name="p981112017596"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.2.4.1.2 "><p id="p1336165217596"><a name="p1336165217596"></a><a name="p1336165217596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.2.4.1.3 "><p id="p855202117596"><a name="p855202117596"></a><a name="p855202117596"></a>Specifies the subnet CIDR block.</p>
    </td>
    </tr>
    <tr id="row985932517596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.2.4.1.1 "><p id="p6040786717596"><a name="p6040786717596"></a><a name="p6040786717596"></a>gateway_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.2.4.1.2 "><p id="p5817993817596"><a name="p5817993817596"></a><a name="p5817993817596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.2.4.1.3 "><p id="p1495452217596"><a name="p1495452217596"></a><a name="p1495452217596"></a>Specifies the subnet gateway address.</p>
    </td>
    </tr>
    <tr id="row37297117596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.2.4.1.1 "><p id="p3021071917596"><a name="p3021071917596"></a><a name="p3021071917596"></a>dhcp_enable</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.2.4.1.2 "><p id="p4005526017596"><a name="p4005526017596"></a><a name="p4005526017596"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.2.4.1.3 "><p id="p2325061317596"><a name="p2325061317596"></a><a name="p2325061317596"></a>Specifies whether the DHCP function is enabled for the subnet.</p>
    </td>
    </tr>
    <tr id="row792892917596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.2.4.1.1 "><p id="p3826349217596"><a name="p3826349217596"></a><a name="p3826349217596"></a>primary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.2.4.1.2 "><p id="p5962058717596"><a name="p5962058717596"></a><a name="p5962058717596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.2.4.1.3 "><p id="p6453823917596"><a name="p6453823917596"></a><a name="p6453823917596"></a>Specifies the IP address of DNS server 1 on the subnet.</p>
    </td>
    </tr>
    <tr id="row4397324617596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.2.4.1.1 "><p id="p506319417596"><a name="p506319417596"></a><a name="p506319417596"></a>secondary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.2.4.1.2 "><p id="p73411217596"><a name="p73411217596"></a><a name="p73411217596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.2.4.1.3 "><p id="p5946313017596"><a name="p5946313017596"></a><a name="p5946313017596"></a>Specifies the IP address of DNS server 2 on the subnet.</p>
    </td>
    </tr>
    <tr id="row545834911143"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.2.4.1.1 "><p id="p591866701143"><a name="p591866701143"></a><a name="p591866701143"></a>dnsList</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.2.4.1.2 "><p id="p318589811143"><a name="p318589811143"></a><a name="p318589811143"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.2.4.1.3 "><p id="p304407061143"><a name="p304407061143"></a><a name="p304407061143"></a>Specifies the IP address list of DNS servers on the subnet.</p>
    </td>
    </tr>
    <tr id="row6540612517596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.2.4.1.1 "><p id="p6340476417596"><a name="p6340476417596"></a><a name="p6340476417596"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.2.4.1.2 "><p id="p5792277317596"><a name="p5792277317596"></a><a name="p5792277317596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.2.4.1.3 "><p id="p6123300617596"><a name="p6123300617596"></a><a name="p6123300617596"></a>Identifies the AZ to which the subnet belongs.</p>
    </td>
    </tr>
    <tr id="row1422614217596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.2.4.1.1 "><p id="p1146682617596"><a name="p1146682617596"></a><a name="p1146682617596"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.2.4.1.2 "><p id="p481418517596"><a name="p481418517596"></a><a name="p481418517596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.2.4.1.3 "><p id="p5440471517596"><a name="p5440471517596"></a><a name="p5440471517596"></a>Specifies the ID of the VPC to which the subnet belongs.</p>
    </td>
    </tr>
    <tr id="row1988039417596"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.2.4.1.1 "><p id="p6680804517596"><a name="p6680804517596"></a><a name="p6680804517596"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.2.4.1.2 "><p id="p3959872717596"><a name="p3959872717596"></a><a name="p3959872717596"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.2.4.1.3 "><a name="ul1290083685410"></a><a name="ul1290083685410"></a><ul id="ul1290083685410"><li>Specifies the status of the subnet.</li><li>The value can be <strong>ACTIVE</strong>, <strong>UNKNOWN</strong>, or <strong>ERROR</strong>.<a name="ul83391032184614"></a><a name="ul83391032184614"></a><ul id="ul83391032184614"><li><strong>ACTIVE</strong>: indicates that the subnet has been associated with the router.</li><li><strong id="b842352706151633"><a name="b842352706151633"></a><a name="b842352706151633"></a>UNKNOWN</strong>: indicates that the subnet has not been associated with the router.</li><li><strong id="b842352706151734"><a name="b842352706151734"></a><a name="b842352706151734"></a>ERROR</strong>: indicates that the subnet is abnormal.</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row6437766611027"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.2.4.1.1 "><p id="p2150517711033"><a name="p2150517711033"></a><a name="p2150517711033"></a>neutron_network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.2.4.1.2 "><p id="p3263900011033"><a name="p3263900011033"></a><a name="p3263900011033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.2.4.1.3 "><p id="p2651330711033"><a name="p2651330711033"></a><a name="p2651330711033"></a>Specifies the ID of the corresponding network (OpenStack Neutron API).</p>
    </td>
    </tr>
    <tr id="row2552805011031"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.2.4.1.1 "><p id="p84866711033"><a name="p84866711033"></a><a name="p84866711033"></a>neutron_subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.2.4.1.2 "><p id="p6517899211033"><a name="p6517899211033"></a><a name="p6517899211033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.2.4.1.3 "><p id="p4500696511033"><a name="p4500696511033"></a><a name="p4500696511033"></a>Specifies the ID of the corresponding subnet (OpenStack Neutron API).</p>
    </td>
    </tr>
    <tr id="row147527203715"><td class="cellrowborder" valign="top" width="29.017098290170978%" headers="mcps1.2.4.1.1 "><p id="p5714303263"><a name="p5714303263"></a><a name="p5714303263"></a>extra_dhcp_opts</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.6983301669833%" headers="mcps1.2.4.1.2 "><p id="p01223042610"><a name="p01223042610"></a><a name="p01223042610"></a>Array of <a href="#table019517383270">extra_dhcp_opt</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.284571542845704%" headers="mcps1.2.4.1.3 "><p id="p111573015263"><a name="p111573015263"></a><a name="p111573015263"></a>Specifies the NTP server address configured for the subnet. For details, see the <a href="#table019517383270">extra_dhcp_opt object</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **extra\_dhcp\_opt**  object

    <a name="table019517383270"></a>
    <table><thead align="left"><tr id="vpc_subnet01_0001_row1806141418109"><th class="cellrowborder" valign="top" width="21.740000000000002%" id="mcps1.2.5.1.1"><p id="vpc_subnet01_0001_p1948182811017"><a name="vpc_subnet01_0001_p1948182811017"></a><a name="vpc_subnet01_0001_p1948182811017"></a><strong id="vpc_subnet01_0001_b842352706195711"><a name="vpc_subnet01_0001_b842352706195711"></a><a name="vpc_subnet01_0001_b842352706195711"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.17%" id="mcps1.2.5.1.2"><p id="vpc_subnet01_0001_p19515288107"><a name="vpc_subnet01_0001_p19515288107"></a><a name="vpc_subnet01_0001_p19515288107"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.619999999999997%" id="mcps1.2.5.1.3"><p id="vpc_subnet01_0001_p755202861014"><a name="vpc_subnet01_0001_p755202861014"></a><a name="vpc_subnet01_0001_p755202861014"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.47%" id="mcps1.2.5.1.4"><p id="vpc_subnet01_0001_p66018281105"><a name="vpc_subnet01_0001_p66018281105"></a><a name="vpc_subnet01_0001_p66018281105"></a><strong id="vpc_subnet01_0001_b1716215324573"><a name="vpc_subnet01_0001_b1716215324573"></a><a name="vpc_subnet01_0001_b1716215324573"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpc_subnet01_0001_row19806161420105"><td class="cellrowborder" valign="top" width="21.740000000000002%" headers="mcps1.2.5.1.1 "><p id="vpc_subnet01_0001_p1834323611017"><a name="vpc_subnet01_0001_p1834323611017"></a><a name="vpc_subnet01_0001_p1834323611017"></a>opt_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.2.5.1.2 "><p id="vpc_subnet01_0001_p1034310368108"><a name="vpc_subnet01_0001_p1034310368108"></a><a name="vpc_subnet01_0001_p1034310368108"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.619999999999997%" headers="mcps1.2.5.1.3 "><p id="vpc_subnet01_0001_p15343163651014"><a name="vpc_subnet01_0001_p15343163651014"></a><a name="vpc_subnet01_0001_p15343163651014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.47%" headers="mcps1.2.5.1.4 "><a name="vpc_subnet01_0001_ul1734314363102"></a><a name="vpc_subnet01_0001_ul1734314363102"></a><ul id="vpc_subnet01_0001_ul1734314363102"><li>Specifies the NTP server address configured for the subnet.</li><li>Constraints:<p id="vpc_subnet01_0001_p1984274292214"><a name="vpc_subnet01_0001_p1984274292214"></a><a name="vpc_subnet01_0001_p1984274292214"></a>The option <strong id="vpc_subnet01_0001_b18312174218176"><a name="vpc_subnet01_0001_b18312174218176"></a><a name="vpc_subnet01_0001_b18312174218176"></a>ntp</strong> for <strong id="vpc_subnet01_0001_b2456833191713"><a name="vpc_subnet01_0001_b2456833191713"></a><a name="vpc_subnet01_0001_b2456833191713"></a>opt_name</strong> indicates the NTP server configured for the subnet. Currently, only IPv4 addresses are supported. A maximum of four IP addresses can be configured, and each address must be unique. Multiple IP addresses must be separated using commas (,). The option <strong id="vpc_subnet01_0001_b1973813315213"><a name="vpc_subnet01_0001_b1973813315213"></a><a name="vpc_subnet01_0001_b1973813315213"></a>null</strong> for <strong id="vpc_subnet01_0001_b9368121819213"><a name="vpc_subnet01_0001_b9368121819213"></a><a name="vpc_subnet01_0001_b9368121819213"></a>opt_name</strong> indicates that no NTP server is configured for the subnet. The parameter value cannot be an empty string.</p>
    </li></ul>
    </td>
    </tr>
    <tr id="vpc_subnet01_0001_row48061714191011"><td class="cellrowborder" valign="top" width="21.740000000000002%" headers="mcps1.2.5.1.1 "><p id="vpc_subnet01_0001_p33437363104"><a name="vpc_subnet01_0001_p33437363104"></a><a name="vpc_subnet01_0001_p33437363104"></a>opt_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.2.5.1.2 "><p id="vpc_subnet01_0001_p1634393613106"><a name="vpc_subnet01_0001_p1634393613106"></a><a name="vpc_subnet01_0001_p1634393613106"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.619999999999997%" headers="mcps1.2.5.1.3 "><p id="vpc_subnet01_0001_p14343113613104"><a name="vpc_subnet01_0001_p14343113613104"></a><a name="vpc_subnet01_0001_p14343113613104"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.47%" headers="mcps1.2.5.1.4 "><a name="vpc_subnet01_0001_ul1934353641010"></a><a name="vpc_subnet01_0001_ul1934353641010"></a><ul id="vpc_subnet01_0001_ul1934353641010"><li>Specifies the NTP server address name configured for the subnet.</li><li>Currently, the value can only be set to <strong id="vpc_subnet01_0001_b185618261310"><a name="vpc_subnet01_0001_b185618261310"></a><a name="vpc_subnet01_0001_b185618261310"></a>ntp</strong>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "subnets": [
            {
                "id": "4779ab1c-7c1a-44b1-a02e-93dfc361b32d",
                "name": "subnet",
                "cidr": "192.168.20.0/24",
                "dnsList": [
                    "114.xx.xx.114",
                    "114.xx.xx.115"
                ],
                "status": "ACTIVE",
                "vpc_id": "3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85",
                "gateway_ip": "192.168.20.1",
                "dhcp_enable": true,
                "primary_dns": "114.xx.xx.114",
                "secondary_dns": "114.xx.xx.115",
            "availability_zone": "aa-bb-cc",//For example, the AZ is aa-bb-cc.
                "neutron_network_id": "4779ab1c-7c1a-44b1-a02e-93dfc361b32d",
                "neutron_subnet_id": "213cb9d-3122-2ac1-1a29-91ffc1231a12"
                "extra_dhcp_opts": [
                  {
                    "opt_value": "10.100.0.33,10.100.0.34",
                    "opt_name": "ntp"
                  }
               ]
            },
            {
                "id": "531dec0f-3116-411b-a21b-e612e42349fd",
                "name": "Subnet1",
                "description": "",
                "cidr": "192.168.1.0/24",
                "dnsList": [
                    "114.xx.xx.114",
                    "114.xx.xx.115"
                ],
                "status": "ACTIVE",
                "vpc_id": "3ec3b33f-ac1c-4630-ad1c-7dba1ed79d85",
                "gateway_ip": "192.168.1.1",
                "dhcp_enable": true,
                "primary_dns": "114.xx.xx.114",
                "secondary_dns": "114.xx.xx.115",
            "availability_zone": "aa-bb-cc",//For example, the AZ is aa-bb-cc.
                "neutron_network_id": "531dec0f-3116-411b-a21b-e612e42349fd",
                "neutron_subnet_id": "1aac193-a2ad-f153-d122-12d64c2c1d78",
                "extra_dhcp_opts": [
                  {
                    "opt_value": "10.100.0.33,10.100.0.34",
                    "opt_name": "ntp"
                  }
               ]
            }
        ]
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

