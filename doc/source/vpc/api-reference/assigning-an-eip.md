# Assigning an EIP<a name="en-us_topic_0020090596"></a>

## Function<a name="section12153337"></a>

This API is used to assign an EIP. 

The EIP service provides independent public IP addresses and bandwidth for Internet access. EIPs can be bound to or unbound from ECSs, BMSs, virtual IP addresses, load balancers, and NAT gateways. 

## URI<a name="section42271171"></a>

POST /v1/\{project\_id\}/publicips

[Table 1](#table57311924)  describes the parameters.

**Table  1**  Parameter description

<a name="table57311924"></a>
<table><thead align="left"><tr id="row11854613"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p20699582"><a name="p20699582"></a><a name="p20699582"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p66053444"><a name="p66053444"></a><a name="p66053444"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p48728718"><a name="p48728718"></a><a name="p48728718"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row54712068"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2492560"><a name="p2492560"></a><a name="p2492560"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p570775"><a name="p570775"></a><a name="p570775"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section44896221"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="table62031189151043"></a>
    <table><thead align="left"><tr id="row4339910151043"><th class="cellrowborder" valign="top" width="14.280000000000001%" id="mcps1.2.5.1.1"><p id="p15988448151043"><a name="p15988448151043"></a><a name="p15988448151043"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.61%" id="mcps1.2.5.1.2"><p id="p19995902151043"><a name="p19995902151043"></a><a name="p19995902151043"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.93%" id="mcps1.2.5.1.3"><p id="p9055369151043"><a name="p9055369151043"></a><a name="p9055369151043"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.18%" id="mcps1.2.5.1.4"><p id="p62396264151043"><a name="p62396264151043"></a><a name="p62396264151043"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20932612151043"><td class="cellrowborder" valign="top" width="14.280000000000001%" headers="mcps1.2.5.1.1 "><p id="p17819972151043"><a name="p17819972151043"></a><a name="p17819972151043"></a>publicip</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p34131600151043"><a name="p34131600151043"></a><a name="p34131600151043"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.93%" headers="mcps1.2.5.1.3 "><p id="p13196241151043"><a name="p13196241151043"></a><a name="p13196241151043"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.2.5.1.4 "><p id="p23492844151043"><a name="p23492844151043"></a><a name="p23492844151043"></a>Specifies the EIP objects. For details, see <a href="#table4491214">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row13560713151050"><td class="cellrowborder" valign="top" width="14.280000000000001%" headers="mcps1.2.5.1.1 "><p id="p24675975151050"><a name="p24675975151050"></a><a name="p24675975151050"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.2 "><p id="p52596998151050"><a name="p52596998151050"></a><a name="p52596998151050"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.93%" headers="mcps1.2.5.1.3 "><p id="p12429959151120"><a name="p12429959151120"></a><a name="p12429959151120"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.2.5.1.4 "><p id="p1744019151120"><a name="p1744019151120"></a><a name="p1744019151120"></a>Specifies the bandwidth objects. For details, see <a href="#table11041789">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **publicip**  field

    <a name="table4491214"></a>
    <table><thead align="left"><tr id="row21610982"><th class="cellrowborder" valign="top" width="30.830000000000002%" id="mcps1.2.5.1.1"><p id="p5659087"><a name="p5659087"></a><a name="p5659087"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.2"><p id="p55732864"><a name="p55732864"></a><a name="p55732864"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.05%" id="mcps1.2.5.1.3"><p id="p4226242618129"><a name="p4226242618129"></a><a name="p4226242618129"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.830000000000002%" id="mcps1.2.5.1.4"><p id="p18068130"><a name="p18068130"></a><a name="p18068130"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54232412"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.5.1.1 "><p id="p30749271"><a name="p30749271"></a><a name="p30749271"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p7663035"><a name="p7663035"></a><a name="p7663035"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.5.1.3 "><p id="p70444218129"><a name="p70444218129"></a><a name="p70444218129"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.5.1.4 "><a name="ul29589093174724"></a><a name="ul29589093174724"></a><ul id="ul29589093174724"><li>Specifies the EIP type.</li><li>The value can be <strong id="b610775542514"><a name="b610775542514"></a><a name="b610775542514"></a>5_bgp</strong> and <strong id="b15441185113256"><a name="b15441185113256"></a><a name="b15441185113256"></a>5_mailbgp</strong>.</li><li>Constraints:<a name="ul9738153015499"></a><a name="ul9738153015499"></a><ul id="ul9738153015499"><li>The configured value must be supported by the system. </li><li><strong id="b1719710451843"><a name="b1719710451843"></a><a name="b1719710451843"></a>publicip_id</strong> is an IPv4 port. If <strong id="b128290317518"><a name="b128290317518"></a><a name="b128290317518"></a>publicip_type</strong> is not specified, the default value is <strong id="b2471543767"><a name="b2471543767"></a><a name="b2471543767"></a>5_bgp</strong>.</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row116305209446"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.5.1.1 "><p id="p25480789446"><a name="p25480789446"></a><a name="p25480789446"></a>ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p50677729446"><a name="p50677729446"></a><a name="p50677729446"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.5.1.3 "><p id="p78364279446"><a name="p78364279446"></a><a name="p78364279446"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.5.1.4 "><a name="ul3888143018611"></a><a name="ul3888143018611"></a><ul id="ul3888143018611"><li>Specifies the EIP to be assigned. The system automatically assigns an EIP if you do not specify it.</li><li>The value must be a valid IPv4 address in the available IP address range.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Description of the  **bandwidth**  field

    <a name="table11041789"></a>
    <table><thead align="left"><tr id="row60677888"><th class="cellrowborder" valign="top" width="30.826917308269174%" id="mcps1.2.5.1.1"><p id="p15961928"><a name="p15961928"></a><a name="p15961928"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.10828917108289%" id="mcps1.2.5.1.2"><p id="p17847776"><a name="p17847776"></a><a name="p17847776"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.2.5.1.3"><p id="p3784029918155"><a name="p3784029918155"></a><a name="p3784029918155"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.886911308869113%" id="mcps1.2.5.1.4"><p id="p36383728"><a name="p36383728"></a><a name="p36383728"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61400865"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="p7414170"><a name="p7414170"></a><a name="p7414170"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.10828917108289%" headers="mcps1.2.5.1.2 "><p id="p63676932"><a name="p63676932"></a><a name="p63676932"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.2.5.1.3 "><p id="p4516535118155"><a name="p4516535118155"></a><a name="p4516535118155"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.886911308869113%" headers="mcps1.2.5.1.4 "><a name="ul518119181073"></a><a name="ul518119181073"></a><ul id="ul518119181073"><li>Specifies the bandwidth name.</li><li>The value is a string of 1 to 64 characters that can contain letters, digits, underscores (_), hyphens (-), and periods (.).</li><li>This parameter is mandatory when <strong id="b276165742195527"><a name="b276165742195527"></a><a name="b276165742195527"></a>share_type</strong> is set to <strong id="b1379441107195527"><a name="b1379441107195527"></a><a name="b1379441107195527"></a>PER</strong>. This parameter will be ignored when <strong id="b1701699234195527"><a name="b1701699234195527"></a><a name="b1701699234195527"></a>share_type</strong> is set to <strong id="b1218397550195527"><a name="b1218397550195527"></a><a name="b1218397550195527"></a>WHOLE</strong> with an ID specified.</li></ul>
    </td>
    </tr>
    <tr id="row15772917"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="p2537905"><a name="p2537905"></a><a name="p2537905"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.10828917108289%" headers="mcps1.2.5.1.2 "><p id="p4243749"><a name="p4243749"></a><a name="p4243749"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.2.5.1.3 "><p id="p3451484018155"><a name="p3451484018155"></a><a name="p3451484018155"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.886911308869113%" headers="mcps1.2.5.1.4 "><a name="ul194366475712"></a><a name="ul194366475712"></a><ul id="ul194366475712"><li>Specifies the bandwidth size.</li><li>The value ranges from 1 Mbit/s to 1000 Mbit/s by default. (The specific range may vary depending on the configuration in each region. You can see the bandwidth range of each region on the management console.)</li><li>This parameter is mandatory when <strong id="b1269381197"><a name="b1269381197"></a><a name="b1269381197"></a>share_type</strong> is set to <strong id="b1412280890"><a name="b1412280890"></a><a name="b1412280890"></a>PER</strong>. This parameter will be ignored when <strong id="b2109803823"><a name="b2109803823"></a><a name="b2109803823"></a>share_type</strong> is set to <strong id="b152335900"><a name="b152335900"></a><a name="b152335900"></a>WHOLE</strong> with an ID specified.</li><li>The minimum unit for bandwidth adjustment varies depending on the bandwidth range. The details are as follows:<a name="ul9790510185"></a><a name="ul9790510185"></a><ul id="ul9790510185"><li>The minimum unit is 1 Mbit/s if the allowed bandwidth size ranges from 0 to 300 Mbit/s (with 300 Mbit/s included).</li><li>The minimum unit is 50 Mbit/s if the allowed bandwidth size ranges 300 Mbit/s to 1000 Mbit/s (with 1000 Mbit/s included).</li><li>The minimum unit is 500 Mbit/s if the allowed bandwidth size is greater than 1000 Mbit/s.</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row33642107"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="p40656116"><a name="p40656116"></a><a name="p40656116"></a>share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.10828917108289%" headers="mcps1.2.5.1.2 "><p id="p4811061"><a name="p4811061"></a><a name="p4811061"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.2.5.1.3 "><p id="p2656447218155"><a name="p2656447218155"></a><a name="p2656447218155"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.886911308869113%" headers="mcps1.2.5.1.4 "><a name="ul2255712095"></a><a name="ul2255712095"></a><ul id="ul2255712095"><li>Specifies the bandwidth type.</li><li>The value is <strong id="b25288513165924"><a name="b25288513165924"></a><a name="b25288513165924"></a>PER</strong>, indicating that the bandwidth is dedicated.</li></ul>
    </td>
    </tr>
    <tr id="row17737188172319"><td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.1 "><p id="p27426113172319"><a name="p27426113172319"></a><a name="p27426113172319"></a>charge_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.10828917108289%" headers="mcps1.2.5.1.2 "><p id="p55776100172330"><a name="p55776100172330"></a><a name="p55776100172330"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.2.5.1.3 "><p id="p23864764172319"><a name="p23864764172319"></a><a name="p23864764172319"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.886911308869113%" headers="mcps1.2.5.1.4 "><a name="ul152417331215"></a><a name="ul152417331215"></a><ul id="ul152417331215"><li>The value is <strong id="b842352706173820"><a name="b842352706173820"></a><a name="b842352706173820"></a>traffic</strong>, indicating that the billing is based on traffic.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request 1 \(IPv4 EIP with dedicated bandwidth\)

    ```
    POST https://{Endpoint}/v1/{project_id}/publicips
    
    {
        "publicip": {
            "type": "5_bgp",
            "ip_version": 4
        },
        "bandwidth": {
            "name": "bandwidth123",
            "size": 10,
            "share_type": "PER"
        }
    }
    ```


## Response Message<a name="section1412808"></a>

-   Response parameter

    **Table  5**  Response parameter

    <a name="table32663367152049"></a>
    <table><thead align="left"><tr id="row49418185152049"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p43450028152049"><a name="p43450028152049"></a><a name="p43450028152049"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="p64289235152049"><a name="p64289235152049"></a><a name="p64289235152049"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="p40045543152049"><a name="p40045543152049"></a><a name="p40045543152049"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row22463580152049"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p7610714152049"><a name="p7610714152049"></a><a name="p7610714152049"></a>publicip</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p4900878152049"><a name="p4900878152049"></a><a name="p4900878152049"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="p15970624152049"><a name="p15970624152049"></a><a name="p15970624152049"></a>Specifies the EIP objects. For details, see <a href="#table44471219">Table 6</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  Description of the  **publicip**  field

    <a name="table44471219"></a>
    <table><thead align="left"><tr id="row33860402"><th class="cellrowborder" valign="top" width="37.96379637963796%" id="mcps1.2.4.1.1"><p id="p58338056"><a name="p58338056"></a><a name="p58338056"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="24.072407240724072%" id="mcps1.2.4.1.2"><p id="p4133121218330"><a name="p4133121218330"></a><a name="p4133121218330"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="37.96379637963796%" id="mcps1.2.4.1.3"><p id="p34137829"><a name="p34137829"></a><a name="p34137829"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13700797"><td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.1 "><p id="p36022757"><a name="p36022757"></a><a name="p36022757"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.2.4.1.2 "><p id="p5949386218330"><a name="p5949386218330"></a><a name="p5949386218330"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.3 "><p id="p25236858"><a name="p25236858"></a><a name="p25236858"></a>Specifies the unique identifier of the EIP.</p>
    </td>
    </tr>
    <tr id="row25805135"><td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.1 "><p id="p9841225"><a name="p9841225"></a><a name="p9841225"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.2.4.1.2 "><p id="p5427353718330"><a name="p5427353718330"></a><a name="p5427353718330"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.3 "><a name="ul052132731516"></a><a name="ul052132731516"></a><ul id="ul052132731516"><li>Specifies the EIP status.</li><li>Possible values are as follows:<a name="ul10603143175810"></a><a name="ul10603143175810"></a><ul id="ul10603143175810"><li><strong id="b84235270610153"><a name="b84235270610153"></a><a name="b84235270610153"></a>FREEZED</strong> (Frozen)</li><li><strong id="b842352706181622"><a name="b842352706181622"></a><a name="b842352706181622"></a>BIND_ERROR</strong> (Binding failed)</li><li><strong id="b842352706181646"><a name="b842352706181646"></a><a name="b842352706181646"></a>BINDING</strong> (Binding)</li><li><strong id="b84235270618176"><a name="b84235270618176"></a><a name="b84235270618176"></a>PENDING_DELETE</strong> (Releasing)</li><li><strong id="b842352706181716"><a name="b842352706181716"></a><a name="b842352706181716"></a>PENDING_CREATE</strong> (Assigning)</li><li><strong id="b842352706181818"><a name="b842352706181818"></a><a name="b842352706181818"></a>PENDING_UPDATE</strong> (Updating)</li><li><strong id="b842352706181834"><a name="b842352706181834"></a><a name="b842352706181834"></a>DOWN</strong> (Unbound)</li><li><strong id="b84235270610164"><a name="b84235270610164"></a><a name="b84235270610164"></a>ACTIVE</strong> (Bound)</li><li><strong id="b842352706181859"><a name="b842352706181859"></a><a name="b842352706181859"></a>ELB</strong> (Bound to a load balancer)</li><li><strong id="b842352706103022"><a name="b842352706103022"></a><a name="b842352706103022"></a>ERROR</strong> (Exceptions)</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row66476022"><td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.1 "><p id="p1332417268438"><a name="p1332417268438"></a><a name="p1332417268438"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.2.4.1.2 "><p id="p3408038918330"><a name="p3408038918330"></a><a name="p3408038918330"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.3 "><a name="ul61069400416"></a><a name="ul61069400416"></a><ul id="ul61069400416"><li>Specifies the EIP type.</li><li>Constraints:<a name="ul1010714409416"></a><a name="ul1010714409416"></a><ul id="ul1010714409416"><li>The configured value must be supported by the system. </li><li><strong id="b1030218389543"><a name="b1030218389543"></a><a name="b1030218389543"></a>publicip_id</strong> is an IPv4 port. If <strong id="b103031389542"><a name="b103031389542"></a><a name="b103031389542"></a>publicip_type</strong> is not specified, the default value is <strong id="b030323835419"><a name="b030323835419"></a><a name="b030323835419"></a>5_bgp</strong>.</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row53754023"><td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.1 "><p id="p59108624"><a name="p59108624"></a><a name="p59108624"></a>public_ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.2.4.1.2 "><p id="p904808818330"><a name="p904808818330"></a><a name="p904808818330"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.3 "><p id="p40237373"><a name="p40237373"></a><a name="p40237373"></a>Specifies the obtained EIP if only IPv4 EIPs are available. </p>
    </td>
    </tr>
    <tr id="row26592044"><td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.1 "><p id="p6471942"><a name="p6471942"></a><a name="p6471942"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.2.4.1.2 "><p id="p6180656518330"><a name="p6180656518330"></a><a name="p6180656518330"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.3 "><p id="p17634333267"><a name="p17634333267"></a><a name="p17634333267"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row43875021"><td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.1 "><p id="p64215808"><a name="p64215808"></a><a name="p64215808"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.2.4.1.2 "><p id="p4027585818330"><a name="p4027585818330"></a><a name="p4027585818330"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.3 "><p id="p27139175"><a name="p27139175"></a><a name="p27139175"></a>Specifies the time (UTC time) when the EIP was assigned.</p>
    </td>
    </tr>
    <tr id="row42925989"><td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.1 "><p id="p54453050"><a name="p54453050"></a><a name="p54453050"></a>bandwidth_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.072407240724072%" headers="mcps1.2.4.1.2 "><p id="p4111904718330"><a name="p4111904718330"></a><a name="p4111904718330"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.96379637963796%" headers="mcps1.2.4.1.3 "><p id="p11161650"><a name="p11161650"></a><a name="p11161650"></a>Specifies the bandwidth (Mbit/s).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response 1 \(IPv4 EIP with dedicated bandwidth\)

    ```
    {
        "publicip": {
            "id": "f588ccfa-8750-4d7c-bf5d-2ede24414706",
            "status": "PENDING_CREATE",
            "type": "5_bgp",
            "public_ip_address": "161.xx.xx.7",
            "tenant_id": "8b7e35ad379141fc9df3e178bd64f55c",
            "ip_version": 4,
            "create_time": "2015-07-16 04:10:52",
            "bandwidth_size": 0
            
        }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

