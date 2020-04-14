# Querying Private IP Addresses<a name="vpc_privateip_0003"></a>

## Function<a name="section54434571"></a>

This API is used to query private IP addresses using search criteria and to display the private IP addresses in a list.

## URI<a name="section20149094"></a>

GET /v1/\{project\_id\}/subnets/\{subnet\_id\}/privateips

Example:

```
GET https://{Endpoint}/v1/{project_id}/subnets/{subnet_id}/privateips?limit=10&marker=4779ab1c-7c1a-44b1-a02e-93dfc361b32d
```

[Table 1](#table12098568)  describes the parameters.

**Table  1**  Parameter description

<a name="table12098568"></a>
<table><thead align="left"><tr id="row42283611"><th class="cellrowborder" valign="top" width="16.73%" id="mcps1.2.5.1.1"><p id="p2420499"><a name="p2420499"></a><a name="p2420499"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="16.54%" id="mcps1.2.5.1.2"><p id="p61842715"><a name="p61842715"></a><a name="p61842715"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.61%" id="mcps1.2.5.1.3"><p id="p18030025173211"><a name="p18030025173211"></a><a name="p18030025173211"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.120000000000005%" id="mcps1.2.5.1.4"><p id="p43203995"><a name="p43203995"></a><a name="p43203995"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9862716"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.1 "><p id="p60682533"><a name="p60682533"></a><a name="p60682533"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.5.1.2 "><p id="p16338175"><a name="p16338175"></a><a name="p16338175"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.3 "><p id="p51145882173211"><a name="p51145882173211"></a><a name="p51145882173211"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.120000000000005%" headers="mcps1.2.5.1.4 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row32261252"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.1 "><p id="p63024590"><a name="p63024590"></a><a name="p63024590"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.5.1.2 "><p id="p4718148"><a name="p4718148"></a><a name="p4718148"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.3 "><p id="p49175772173211"><a name="p49175772173211"></a><a name="p49175772173211"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.120000000000005%" headers="mcps1.2.5.1.4 "><p id="p44471500173244"><a name="p44471500173244"></a><a name="p44471500173244"></a>Specifies the unique ID of the subnet to which the private IP address belongs.</p>
</td>
</tr>
<tr id="row33082261"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.1 "><p id="p62417507"><a name="p62417507"></a><a name="p62417507"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.5.1.2 "><p id="p22653281"><a name="p22653281"></a><a name="p22653281"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.3 "><p id="p23814582173211"><a name="p23814582173211"></a><a name="p23814582173211"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.120000000000005%" headers="mcps1.2.5.1.4 "><p id="p49152270"><a name="p49152270"></a><a name="p49152270"></a>Specifies the start resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
</td>
</tr>
<tr id="row39717249"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.5.1.1 "><p id="p62980604"><a name="p62980604"></a><a name="p62980604"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.5.1.2 "><p id="p1155275"><a name="p1155275"></a><a name="p1155275"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.61%" headers="mcps1.2.5.1.3 "><p id="p49933009173211"><a name="p49933009173211"></a><a name="p49933009173211"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48.120000000000005%" headers="mcps1.2.5.1.4 "><a name="ul18965173516362"></a><a name="ul18965173516362"></a><ul id="ul18965173516362"><li>Specifies the number of records returned on each page.</li><li>The value ranges from 0 to intmax.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section47124125"></a>

-   Request parameter

    None

-   Example request

    ```
    GET https://{Endpoint}/v1/{project_id}/subnets/{subnet_id}/privateips
    ```


## Response Message<a name="section21463943"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="table16726122155915"></a>
    <table><thead align="left"><tr id="row50660459155915"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p9856497155915"><a name="p9856497155915"></a><a name="p9856497155915"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="p42646948155915"><a name="p42646948155915"></a><a name="p42646948155915"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="p31850784155915"><a name="p31850784155915"></a><a name="p31850784155915"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29776745155915"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p63106150155915"><a name="p63106150155915"></a><a name="p63106150155915"></a>privateips</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p44872862155915"><a name="p44872862155915"></a><a name="p44872862155915"></a>Array of <a href="#table21538022">privateip</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="p30300018155915"><a name="p30300018155915"></a><a name="p30300018155915"></a>Specifies the private IP address objects. For details, see <a href="#table21538022">Table 3</a>.</p>
    <p id="p15992181219214"><a name="p15992181219214"></a><a name="p15992181219214"></a>Private IP addresses reserved for system interfaces are not displayed. You can log in to the management console to view the IP addresses.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **privateip**  field

    <a name="table21538022"></a>
    <table><thead align="left"><tr id="row33313579"><th class="cellrowborder" valign="top" width="22.17778222177782%" id="mcps1.2.4.1.1"><p id="p14045344"><a name="p14045344"></a><a name="p14045344"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.477852214778522%" id="mcps1.2.4.1.2"><p id="p42744433173254"><a name="p42744433173254"></a><a name="p42744433173254"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.34436556344365%" id="mcps1.2.4.1.3"><p id="p11033160"><a name="p11033160"></a><a name="p11033160"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row21270730"><td class="cellrowborder" valign="top" width="22.17778222177782%" headers="mcps1.2.4.1.1 "><p id="p45207585"><a name="p45207585"></a><a name="p45207585"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.477852214778522%" headers="mcps1.2.4.1.2 "><p id="p39747058173254"><a name="p39747058173254"></a><a name="p39747058173254"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.34436556344365%" headers="mcps1.2.4.1.3 "><a name="ul13978236183119"></a><a name="ul13978236183119"></a><ul id="ul13978236183119"><li>Specifies the status of the private IP address.</li><li>Possible values are as follows:<a name="ul948092312377"></a><a name="ul948092312377"></a><ul id="ul948092312377"><li><strong id="b5445142382412"><a name="b5445142382412"></a><a name="b5445142382412"></a>ACTIVE</strong></li><li><strong id="b1250102492416"><a name="b1250102492416"></a><a name="b1250102492416"></a>DOWN</strong></li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row44135236"><td class="cellrowborder" valign="top" width="22.17778222177782%" headers="mcps1.2.4.1.1 "><p id="p18184391"><a name="p18184391"></a><a name="p18184391"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.477852214778522%" headers="mcps1.2.4.1.2 "><p id="p65395131173254"><a name="p65395131173254"></a><a name="p65395131173254"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.34436556344365%" headers="mcps1.2.4.1.3 "><p id="p47453675"><a name="p47453675"></a><a name="p47453675"></a>Specifies the ID of the private IP address, which uniquely identifies the private IP address.</p>
    </td>
    </tr>
    <tr id="row53320433"><td class="cellrowborder" valign="top" width="22.17778222177782%" headers="mcps1.2.4.1.1 "><p id="p23987813"><a name="p23987813"></a><a name="p23987813"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.477852214778522%" headers="mcps1.2.4.1.2 "><p id="p62514293173254"><a name="p62514293173254"></a><a name="p62514293173254"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.34436556344365%" headers="mcps1.2.4.1.3 "><p id="p26383427"><a name="p26383427"></a><a name="p26383427"></a>Specifies the ID of the subnet from which IP addresses are assigned.</p>
    </td>
    </tr>
    <tr id="row8629350181540"><td class="cellrowborder" valign="top" width="22.17778222177782%" headers="mcps1.2.4.1.1 "><p id="p22152840181542"><a name="p22152840181542"></a><a name="p22152840181542"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.477852214778522%" headers="mcps1.2.4.1.2 "><p id="p54098843181542"><a name="p54098843181542"></a><a name="p54098843181542"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.34436556344365%" headers="mcps1.2.4.1.3 "><p id="p126338192113"><a name="p126338192113"></a><a name="p126338192113"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row40871974"><td class="cellrowborder" valign="top" width="22.17778222177782%" headers="mcps1.2.4.1.1 "><p id="p22295564"><a name="p22295564"></a><a name="p22295564"></a>device_owner</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.477852214778522%" headers="mcps1.2.4.1.2 "><p id="p30493000173254"><a name="p30493000173254"></a><a name="p30493000173254"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.34436556344365%" headers="mcps1.2.4.1.3 "><a name="ul1878734133215"></a><a name="ul1878734133215"></a><ul id="ul1878734133215"><li>Specifies the resource using the private IP address. The parameter is left blank if it is not used.</li><li>The value can be <strong id="b167565012264"><a name="b167565012264"></a><a name="b167565012264"></a>network:dhcp</strong>, <strong id="b1067719503269"><a name="b1067719503269"></a><a name="b1067719503269"></a>network:router_interface_distributed</strong>, <strong id="b3679125016265"><a name="b3679125016265"></a><a name="b3679125016265"></a>compute:xxx</strong>, or <strong id="b168035018264"><a name="b168035018264"></a><a name="b168035018264"></a>neutron:VIP_PORT</strong>. (In value <strong id="b46821150122612"><a name="b46821150122612"></a><a name="b46821150122612"></a>compute:xxx</strong>, <strong id="b36841150182610"><a name="b36841150182610"></a><a name="b36841150182610"></a>xxx</strong> specifies the AZ name, for example, <strong id="b1768895062614"><a name="b1768895062614"></a><a name="b1768895062614"></a>compute:aa-bb-cc</strong> indicates that the private IP address is used by an ECS in the <strong id="b176904505262"><a name="b176904505262"></a><a name="b176904505262"></a>aa-bb-cc</strong> AZ).</li><li>The value range specifies only the type of private IP addresses supported by the current service.</li></ul>
    </td>
    </tr>
    <tr id="row35044283"><td class="cellrowborder" valign="top" width="22.17778222177782%" headers="mcps1.2.4.1.1 "><p id="p20014644"><a name="p20014644"></a><a name="p20014644"></a>ip_address</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.477852214778522%" headers="mcps1.2.4.1.2 "><p id="p54013915173254"><a name="p54013915173254"></a><a name="p54013915173254"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.34436556344365%" headers="mcps1.2.4.1.3 "><p id="p57619553"><a name="p57619553"></a><a name="p57619553"></a>Specifies the assigned private IP address.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "privateips": [
            {
                "status": "DOWN",
                "id": "d600542a-b231-45ed-af05-e9930cb14f78",
                "subnet_id": "531dec0f-3116-411b-a21b-e612e42349fd",
                "tenant_id": "8b7e35ad379141fc9df3e178bd64f55c",
                "device_owner": "",
                "ip_address": "192.168.1.11"
            },
            {
                "status": "DOWN",
                "id": "d600542a-b231-45ed-af05-e9930cb14f79",
                "subnet_id": "531dec0f-3116-411b-a21b-e612e42349fd",
                "tenant_id": "8b7e35ad379141fc9df3e178bd64f55c",
                "device_owner": "",
                "ip_address": "192.168.1.12"
            }
        ]
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

