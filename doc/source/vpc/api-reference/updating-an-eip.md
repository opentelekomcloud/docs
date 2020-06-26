# Updating an EIP<a name="vpc_eip_0004"></a>

## Function<a name="section43589445"></a>

This API is used to update an EIP, for example, binding an EIP to a NIC, unbinding an EIP from a NIC, or converting the IP address version.

## URI<a name="section56760689"></a>

PUT /v1/\{project\_id\}/publicips/\{publicip\_id\}

[Table 1](#table25231885)  describes the parameters.

**Table  1**  Parameter description

<a name="table25231885"></a>
<table><thead align="left"><tr id="row34804713"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p609510"><a name="p609510"></a><a name="p609510"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p49370368"><a name="p49370368"></a><a name="p49370368"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p39576862"><a name="p39576862"></a><a name="p39576862"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row51609257"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p19600264"><a name="p19600264"></a><a name="p19600264"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p44117540"><a name="p44117540"></a><a name="p44117540"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row16540805"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p64736823"><a name="p64736823"></a><a name="p64736823"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p9191297"><a name="p9191297"></a><a name="p9191297"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p6297612"><a name="p6297612"></a><a name="p6297612"></a>Specifies the unique identifier of the EIP.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section41084157"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="table46814673152226"></a>
    <table><thead align="left"><tr id="row46264343152226"><th class="cellrowborder" valign="top" width="12.4%" id="mcps1.2.5.1.1"><p id="p56424328152226"><a name="p56424328152226"></a><a name="p56424328152226"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.990000000000002%" id="mcps1.2.5.1.2"><p id="p6967894152226"><a name="p6967894152226"></a><a name="p6967894152226"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.3"><p id="p27528552152226"><a name="p27528552152226"></a><a name="p27528552152226"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.18%" id="mcps1.2.5.1.4"><p id="p15220263152226"><a name="p15220263152226"></a><a name="p15220263152226"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row24881786152226"><td class="cellrowborder" valign="top" width="12.4%" headers="mcps1.2.5.1.1 "><p id="p2158794152226"><a name="p2158794152226"></a><a name="p2158794152226"></a>publicip</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.2.5.1.2 "><p id="p40644606152226"><a name="p40644606152226"></a><a name="p40644606152226"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.3 "><p id="p3878783152226"><a name="p3878783152226"></a><a name="p3878783152226"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.2.5.1.4 "><p id="p9060565152226"><a name="p9060565152226"></a><a name="p9060565152226"></a>Specifies the EIP objects. For details, see <a href="#table23403840">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **publicip**  field

    <a name="table23403840"></a>
    <table><thead align="left"><tr id="row4798296"><th class="cellrowborder" valign="top" width="30.830000000000002%" id="mcps1.2.5.1.1"><p id="p53117702"><a name="p53117702"></a><a name="p53117702"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.05%" id="mcps1.2.5.1.2"><p id="p7566645"><a name="p7566645"></a><a name="p7566645"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.3"><p id="p3809944218819"><a name="p3809944218819"></a><a name="p3809944218819"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.830000000000002%" id="mcps1.2.5.1.4"><p id="p8918541"><a name="p8918541"></a><a name="p8918541"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51313205"><td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.5.1.1 "><p id="p62728917"><a name="p62728917"></a><a name="p62728917"></a>port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.5.1.2 "><p id="p47877526"><a name="p47877526"></a><a name="p47877526"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.3 "><p id="p6615596018819"><a name="p6615596018819"></a><a name="p6615596018819"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.5.1.4 "><a name="ul1580299162914"></a><a name="ul1580299162914"></a><ul id="ul1580299162914"><li>Specifies the port ID.</li><li>The value must be an existing port ID. If this parameter is not included or the parameter value is left blank, the EIP is unbound. If the specified port ID does not exist or has already been bound with an EIP, an error message will be displayed. </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request 1 \(Binding an EIP to a NIC\)

    ```
    PUT https://{Endpoint}/v1/{project_id}/publicips/{publicip_id}
    
    {
        "publicip": {
            "port_id": "f588ccfa-8750-4d7c-bf5d-2ede24414706"
        }
    }
    ```


## Response Message<a name="section34213098"></a>

-   Response parameter

    **Table  4**  Response parameter

    <a name="table32985183152250"></a>
    <table><thead align="left"><tr id="row10178394152250"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p19143548152250"><a name="p19143548152250"></a><a name="p19143548152250"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="p40138407152250"><a name="p40138407152250"></a><a name="p40138407152250"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="p29985535152250"><a name="p29985535152250"></a><a name="p29985535152250"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12909284152250"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p39019069152250"><a name="p39019069152250"></a><a name="p39019069152250"></a>publicip</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p50907501152250"><a name="p50907501152250"></a><a name="p50907501152250"></a><em id="i1810218131512"><a name="i1810218131512"></a><a name="i1810218131512"></a>Object</em></p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="p366643152250"><a name="p366643152250"></a><a name="p366643152250"></a>Specifies the EIP objects. For details, see <a href="#table83964341880">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Description of the  **publicips**  field

    <a name="table83964341880"></a>
    <table><thead align="left"><tr id="row608739661880"><th class="cellrowborder" valign="top" width="36.046395360463954%" id="mcps1.2.4.1.1"><p id="p318442431880"><a name="p318442431880"></a><a name="p318442431880"></a><strong id="b1969533113447"><a name="b1969533113447"></a><a name="b1969533113447"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="27.90720927907209%" id="mcps1.2.4.1.2"><p id="p201897271880"><a name="p201897271880"></a><a name="p201897271880"></a><strong id="b0745256174410"><a name="b0745256174410"></a><a name="b0745256174410"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="36.046395360463954%" id="mcps1.2.4.1.3"><p id="p247551571880"><a name="p247551571880"></a><a name="p247551571880"></a><strong id="b19198155994410"><a name="b19198155994410"></a><a name="b19198155994410"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row590107001880"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="p151373871880"><a name="p151373871880"></a><a name="p151373871880"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="p623914921880"><a name="p623914921880"></a><a name="p623914921880"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><p id="p205460611880"><a name="p205460611880"></a><a name="p205460611880"></a>Specifies the unique identifier of the EIP.</p>
    </td>
    </tr>
    <tr id="row506968211880"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="p128018091880"><a name="p128018091880"></a><a name="p128018091880"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="p394853281880"><a name="p394853281880"></a><a name="p394853281880"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><a name="ul263945115243"></a><a name="ul263945115243"></a><ul id="ul263945115243"><li>Specifies the EIP status.</li><li>Possible values are as follows:<a name="ul7905205815810"></a><a name="ul7905205815810"></a><ul id="ul7905205815810"><li><strong id="b84235270610153"><a name="b84235270610153"></a><a name="b84235270610153"></a>FREEZED</strong> (Frozen)</li><li><strong id="b842352706181622"><a name="b842352706181622"></a><a name="b842352706181622"></a>BIND_ERROR</strong> (Binding failed)</li><li><strong id="b842352706181646"><a name="b842352706181646"></a><a name="b842352706181646"></a>BINDING</strong> (Binding)</li><li><strong id="b84235270618176"><a name="b84235270618176"></a><a name="b84235270618176"></a>PENDING_DELETE</strong> (Releasing)</li><li><strong id="b842352706181716"><a name="b842352706181716"></a><a name="b842352706181716"></a>PENDING_CREATE</strong> (Assigning)</li><li><strong id="b842352706181818"><a name="b842352706181818"></a><a name="b842352706181818"></a>PENDING_UPDATE</strong> (Updating)</li><li><strong id="b842352706181834"><a name="b842352706181834"></a><a name="b842352706181834"></a>DOWN</strong> (Unbound)</li><li><strong id="b84235270610164"><a name="b84235270610164"></a><a name="b84235270610164"></a>ACTIVE</strong> (Bound)</li><li><strong id="b842352706181859"><a name="b842352706181859"></a><a name="b842352706181859"></a>ELB</strong> (Bound to a load balancer)</li><li><strong id="b842352706103022"><a name="b842352706103022"></a><a name="b842352706103022"></a>ERROR</strong> (Exceptions)</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row230260811880"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="p30749271"><a name="p30749271"></a><a name="p30749271"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="p379401841880"><a name="p379401841880"></a><a name="p379401841880"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><a name="ul7176216121014"></a><a name="ul7176216121014"></a><ul id="ul7176216121014"><li>Specifies the EIP type.</li><li>Constraints:<a name="ul9738153015499"></a><a name="ul9738153015499"></a><ul id="ul9738153015499"><li>The configured value must be supported by the system. </li><li><strong id="b131616456452"><a name="b131616456452"></a><a name="b131616456452"></a>publicip_id</strong> is an IPv4 port. If <strong id="b21764516456"><a name="b21764516456"></a><a name="b21764516456"></a>publicip_type</strong> is not specified, the default value is <strong id="b11201245154510"><a name="b11201245154510"></a><a name="b11201245154510"></a>5_bgp</strong>.</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row389218135338"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="p3576115214619"><a name="p3576115214619"></a><a name="p3576115214619"></a>public_ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="p35761552124618"><a name="p35761552124618"></a><a name="p35761552124618"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><p id="p19576252174619"><a name="p19576252174619"></a><a name="p19576252174619"></a>Specifies the obtained EIP if only IPv4 EIPs are available. </p>
    </td>
    </tr>
    <tr id="row283940631880"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="p182177951880"><a name="p182177951880"></a><a name="p182177951880"></a>private_ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="p60695041880"><a name="p60695041880"></a><a name="p60695041880"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><a name="ul1693412582014"></a><a name="ul1693412582014"></a><ul id="ul1693412582014"><li>Specifies the private IP address bound with the EIP.</li><li>This parameter is returned only when a private IP address is bound with the EIP.</li></ul>
    </td>
    </tr>
    <tr id="row264614551880"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="p630030811880"><a name="p630030811880"></a><a name="p630030811880"></a>port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="p397229231880"><a name="p397229231880"></a><a name="p397229231880"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><a name="ul420471472010"></a><a name="ul420471472010"></a><ul id="ul420471472010"><li>Specifies the port ID.</li><li>This parameter is returned only when a private IP address is bound with the EIP.</li></ul>
    </td>
    </tr>
    <tr id="row340905521880"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="p98713501880"><a name="p98713501880"></a><a name="p98713501880"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="p58747301880"><a name="p58747301880"></a><a name="p58747301880"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><p id="p269114516312"><a name="p269114516312"></a><a name="p269114516312"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row548200921880"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="p112424711880"><a name="p112424711880"></a><a name="p112424711880"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="p92119381880"><a name="p92119381880"></a><a name="p92119381880"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><p id="p36292894"><a name="p36292894"></a><a name="p36292894"></a>Specifies the time (UTC time) when the EIP was assigned.</p>
    </td>
    </tr>
    <tr id="row46164031880"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="p383843571880"><a name="p383843571880"></a><a name="p383843571880"></a>bandwidth_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="p473107141880"><a name="p473107141880"></a><a name="p473107141880"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><p id="p3934181618641"><a name="p3934181618641"></a><a name="p3934181618641"></a>Specifies the ID of the bandwidth associated with the EIP.</p>
    </td>
    </tr>
    <tr id="row626637421880"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="p425983371880"><a name="p425983371880"></a><a name="p425983371880"></a>bandwidth_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="p463832691880"><a name="p463832691880"></a><a name="p463832691880"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><p id="p2365466"><a name="p2365466"></a><a name="p2365466"></a>Specifies the bandwidth (Mbit/s).</p>
    </td>
    </tr>
    <tr id="row576448061880"><td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.1 "><p id="p387177161880"><a name="p387177161880"></a><a name="p387177161880"></a>bandwidth_share_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="27.90720927907209%" headers="mcps1.2.4.1.2 "><p id="p21369006155933"><a name="p21369006155933"></a><a name="p21369006155933"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.046395360463954%" headers="mcps1.2.4.1.3 "><a name="ul2255712095"></a><a name="ul2255712095"></a><ul id="ul2255712095"><li>Specifies the EIP bandwidth type.</li><li>The value can be <strong id="b65771539121116"><a name="b65771539121116"></a><a name="b65771539121116"></a>PER</strong> or <strong id="b057811393110"><a name="b057811393110"></a><a name="b057811393110"></a>WHOLE</strong>.<a name="ul729412507220"></a><a name="ul729412507220"></a><ul id="ul729412507220"><li><strong id="b130813427114"><a name="b130813427114"></a><a name="b130813427114"></a>PER</strong>: Dedicated bandwidth</li><li><strong id="b20211104617117"><a name="b20211104617117"></a><a name="b20211104617117"></a>WHOLE</strong>: Shared bandwidth</li></ul>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response 1 \(Binding an EIP to a NIC\)

    ```
    {
      "publicip": {
        "id": "f6318bef-6508-4ea5-a48f-6152b6b1a8fb",
        "status": "ACTIVE",
        "type": "5_bgp",
        "port_id": "a135e9b8-1630-40d2-a6c5-eb534a61efbe",
        "public_ip_address": "10.xx.xx.162",
        "private_ip_address": "192.168.1.131",
        "tenant_id": "26ae5181a416420998eb2093aaed84d9",
        "create_time": "2019-03-27 01:33:18",
        "bandwidth_size": 7,
        "ip_version": 4
      }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

