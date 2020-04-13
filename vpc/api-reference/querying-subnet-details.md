# Querying Subnet Details<a name="vpc_subnet01_0002"></a>

## Function<a name="section6925935"></a>

This API is used to query details about a subnet.

## URI<a name="section62333418"></a>

GET /v1/\{project\_id\}/subnets/\{subnet\_id\}

[Table 1](#table61566768)  describes the parameters.

**Table  1**  Parameter description

<a name="table61566768"></a>
<table><thead align="left"><tr id="row44407631"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p40248354"><a name="p40248354"></a><a name="p40248354"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p38891250"><a name="p38891250"></a><a name="p38891250"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p63183526"><a name="p63183526"></a><a name="p63183526"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17591975"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15663836"><a name="p15663836"></a><a name="p15663836"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p60811181"><a name="p60811181"></a><a name="p60811181"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row39501348"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p45492604"><a name="p45492604"></a><a name="p45492604"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p61022284"><a name="p61022284"></a><a name="p61022284"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p43857981"><a name="p43857981"></a><a name="p43857981"></a>Specifies the subnet ID, which uniquely identifies the subnet. If you use the management console, the value of this parameter is the <strong id="b195522519461"><a name="b195522519461"></a><a name="b195522519461"></a>Network ID</strong> value.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section24129853"></a>

-   Request parameter

    None

-   Example request

    ```
    GET https://{Endpoint}/v1/{project_id}/subnets/4779ab1c-7c1a-44b1-a02e-93dfc361b32d
    ```


## Response Message<a name="section15842089"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table6005374015751"></a>
    <table><thead align="left"><tr id="row4874046215751"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p5566332215751"><a name="p5566332215751"></a><a name="p5566332215751"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.84%" id="mcps1.2.4.1.2"><p id="p62309715751"><a name="p62309715751"></a><a name="p62309715751"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.82000000000001%" id="mcps1.2.4.1.3"><p id="p5047090715751"><a name="p5047090715751"></a><a name="p5047090715751"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6161169015751"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p2449098915751"><a name="p2449098915751"></a><a name="p2449098915751"></a>subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.84%" headers="mcps1.2.4.1.2 "><p id="p2676232115751"><a name="p2676232115751"></a><a name="p2676232115751"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.82000000000001%" headers="mcps1.2.4.1.3 "><p id="p4816174615751"><a name="p4816174615751"></a><a name="p4816174615751"></a>Specifies the <a href="#table6614597017585">subnet objects</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **subnet**  objects

    <a name="table6614597017585"></a>
    <table><thead align="left"><tr id="row5931021317585"><th class="cellrowborder" valign="top" width="28.95%" id="mcps1.2.4.1.1"><p id="p3939794017585"><a name="p3939794017585"></a><a name="p3939794017585"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.950000000000003%" id="mcps1.2.4.1.2"><p id="p5365431717585"><a name="p5365431717585"></a><a name="p5365431717585"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.1%" id="mcps1.2.4.1.3"><p id="p5103239017585"><a name="p5103239017585"></a><a name="p5103239017585"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3998288717585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.2.4.1.1 "><p id="p1738840917585"><a name="p1738840917585"></a><a name="p1738840917585"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p28481417585"><a name="p28481417585"></a><a name="p28481417585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.2.4.1.3 "><p id="p2306998617585"><a name="p2306998617585"></a><a name="p2306998617585"></a>Specifies a resource ID in UUID format.</p>
    </td>
    </tr>
    <tr id="row630328217585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.2.4.1.1 "><p id="p4080382917585"><a name="p4080382917585"></a><a name="p4080382917585"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p1666748117585"><a name="p1666748117585"></a><a name="p1666748117585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.2.4.1.3 "><a name="ul23311559134110"></a><a name="ul23311559134110"></a><ul id="ul23311559134110"><li>Specifies the subnet name.</li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li></ul>
    </td>
    </tr>
    <tr id="row098813447294"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.2.4.1.1 "><p id="p6644346112914"><a name="p6644346112914"></a><a name="p6644346112914"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p1964416468296"><a name="p1964416468296"></a><a name="p1964416468296"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.2.4.1.3 "><a name="ul237215542179"></a><a name="ul237215542179"></a><ul id="ul237215542179"><li>Provides supplementary information about the subnet.</li><li>The value is a string of no more than 255 characters and cannot contain angle brackets (&lt; or &gt;).</li></ul>
    </td>
    </tr>
    <tr id="row388956217585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.2.4.1.1 "><p id="p4661911217585"><a name="p4661911217585"></a><a name="p4661911217585"></a>cidr</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p5290705517585"><a name="p5290705517585"></a><a name="p5290705517585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.2.4.1.3 "><p id="p5761304717585"><a name="p5761304717585"></a><a name="p5761304717585"></a>Specifies the subnet CIDR block.</p>
    </td>
    </tr>
    <tr id="row4875537617585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.2.4.1.1 "><p id="p5687141217585"><a name="p5687141217585"></a><a name="p5687141217585"></a>gateway_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p805358517585"><a name="p805358517585"></a><a name="p805358517585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.2.4.1.3 "><p id="p4836063417585"><a name="p4836063417585"></a><a name="p4836063417585"></a>Specifies the subnet gateway address.</p>
    </td>
    </tr>
    <tr id="row3259252617585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.2.4.1.1 "><p id="p2274892917585"><a name="p2274892917585"></a><a name="p2274892917585"></a>dhcp_enable</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p561056817585"><a name="p561056817585"></a><a name="p561056817585"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.2.4.1.3 "><p id="p5180286017585"><a name="p5180286017585"></a><a name="p5180286017585"></a>Specifies whether DHCP is enabled for the subnet.</p>
    </td>
    </tr>
    <tr id="row6357256317585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.2.4.1.1 "><p id="p4910399917585"><a name="p4910399917585"></a><a name="p4910399917585"></a>primary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p4879619717585"><a name="p4879619717585"></a><a name="p4879619717585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.2.4.1.3 "><p id="p6017790317585"><a name="p6017790317585"></a><a name="p6017790317585"></a>Specifies the IP address of DNS server 1 on the subnet.</p>
    </td>
    </tr>
    <tr id="row473021817585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.2.4.1.1 "><p id="p4760336917585"><a name="p4760336917585"></a><a name="p4760336917585"></a>secondary_dns</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p105619417585"><a name="p105619417585"></a><a name="p105619417585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.2.4.1.3 "><p id="p1844285917585"><a name="p1844285917585"></a><a name="p1844285917585"></a>Specifies the IP address of DNS server 2 on the subnet.</p>
    </td>
    </tr>
    <tr id="row5602880311213"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.2.4.1.1 "><p id="p4203922911213"><a name="p4203922911213"></a><a name="p4203922911213"></a>dnsList</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p195587511213"><a name="p195587511213"></a><a name="p195587511213"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.2.4.1.3 "><p id="p2420815811213"><a name="p2420815811213"></a><a name="p2420815811213"></a>Specifies the IP address list of DNS servers on the subnet.</p>
    </td>
    </tr>
    <tr id="row3176800317585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.2.4.1.1 "><p id="p2307142317585"><a name="p2307142317585"></a><a name="p2307142317585"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p4112332617585"><a name="p4112332617585"></a><a name="p4112332617585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.2.4.1.3 "><p id="p4265512017585"><a name="p4265512017585"></a><a name="p4265512017585"></a>Identifies the AZ to which the subnet belongs.</p>
    </td>
    </tr>
    <tr id="row4835176717585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.2.4.1.1 "><p id="p2417901817585"><a name="p2417901817585"></a><a name="p2417901817585"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p6029773217585"><a name="p6029773217585"></a><a name="p6029773217585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.2.4.1.3 "><p id="p5227810517585"><a name="p5227810517585"></a><a name="p5227810517585"></a>Specifies the ID of the VPC to which the subnet belongs.</p>
    </td>
    </tr>
    <tr id="row74090317585"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.2.4.1.1 "><p id="p6001314817585"><a name="p6001314817585"></a><a name="p6001314817585"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p1856038817585"><a name="p1856038817585"></a><a name="p1856038817585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.2.4.1.3 "><a name="ul756817571315"></a><a name="ul756817571315"></a><ul id="ul756817571315"><li>Specifies the status of the subnet.</li><li>The value can be <strong>ACTIVE</strong>, <strong>UNKNOWN</strong>, or <strong>ERROR</strong>.<a name="ul83391032184614"></a><a name="ul83391032184614"></a><ul id="ul83391032184614"><li><strong>ACTIVE</strong>: indicates that the subnet has been associated with the router.</li><li><strong id="b842352706151633"><a name="b842352706151633"></a><a name="b842352706151633"></a>UNKNOWN</strong>: indicates that the subnet has not been associated with the router.</li><li><strong id="b842352706151734"><a name="b842352706151734"></a><a name="b842352706151734"></a>ERROR</strong>: indicates that the subnet is abnormal.</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row21291622105956"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.2.4.1.1 "><p id="p442246351103"><a name="p442246351103"></a><a name="p442246351103"></a>neutron_network_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p462170191103"><a name="p462170191103"></a><a name="p462170191103"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.2.4.1.3 "><p id="p525910351103"><a name="p525910351103"></a><a name="p525910351103"></a>Specifies the ID of the corresponding network (OpenStack Neutron API).</p>
    </td>
    </tr>
    <tr id="row136513311102"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.2.4.1.1 "><p id="p197036161103"><a name="p197036161103"></a><a name="p197036161103"></a>neutron_subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p237568301103"><a name="p237568301103"></a><a name="p237568301103"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.2.4.1.3 "><p id="p452550761103"><a name="p452550761103"></a><a name="p452550761103"></a>Specifies the ID of the corresponding subnet (OpenStack Neutron API).</p>
    </td>
    </tr>
    <tr id="row776211348365"><td class="cellrowborder" valign="top" width="28.95%" headers="mcps1.2.4.1.1 "><p id="p5714303263"><a name="p5714303263"></a><a name="p5714303263"></a>extra_dhcp_opts</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.950000000000003%" headers="mcps1.2.4.1.2 "><p id="p01223042610"><a name="p01223042610"></a><a name="p01223042610"></a>Array of <a href="#table019517383270">extra_dhcp_opt</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.1%" headers="mcps1.2.4.1.3 "><p id="p111573015263"><a name="p111573015263"></a><a name="p111573015263"></a>Specifies the NTP server address configured for the subnet. For details, see the <a href="#table019517383270">extra_dhcp_opt object</a>.</p>
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
        "subnet": {
            "id": "4779ab1c-7c1a-44b1-a02e-93dfc361b32d",
            "name": "subnet",
            "description": "",
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
            "neutron_subnet_id": "213cb9d-3122-2ac1-1a29-91ffc1231a12",
            "extra_dhcp_opts": [
                {
                    "opt_value": "10.100.0.33,10.100.0.34",
                    "opt_name": "ntp"
                }
            ]
        }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

