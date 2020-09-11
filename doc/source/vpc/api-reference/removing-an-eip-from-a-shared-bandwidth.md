# Removing an EIP from a Shared Bandwidth<a name="vpc_sharebandwidth_0005"></a>

## Function<a name="section16581154"></a>

This API is used to remove an EIP from a shared bandwidth.

## URI<a name="section15012662"></a>

POST /v2.0/\{project\_id\}/bandwidths/\{bandwidth\_id\}/remove

[Table 1](#table25281875)  describes the parameters.

**Table  1**  Parameter description

<a name="table25281875"></a>
<table><thead align="left"><tr id="row26712487"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p16227847"><a name="p16227847"></a><a name="p16227847"></a><strong id="b842352706195711"><a name="b842352706195711"></a><a name="b842352706195711"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p39387211"><a name="p39387211"></a><a name="p39387211"></a><strong id="b84235270615219"><a name="b84235270615219"></a><a name="b84235270615219"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p36247516"><a name="p36247516"></a><a name="p36247516"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row50367649"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p53247746"><a name="p53247746"></a><a name="p53247746"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p18100201"><a name="p18100201"></a><a name="p18100201"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row41709209"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p23002745"><a name="p23002745"></a><a name="p23002745"></a>bandwidth_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p51283066"><a name="p51283066"></a><a name="p51283066"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p60287683"><a name="p60287683"></a><a name="p60287683"></a>Specifies the bandwidth ID, which uniquely identifies the bandwidth.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section896237"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="table3057854815556"></a>
    <table><thead align="left"><tr id="row6286666315556"><th class="cellrowborder" valign="top" width="15.409999999999998%" id="mcps1.2.5.1.1"><p id="p5903494715556"><a name="p5903494715556"></a><a name="p5903494715556"></a><strong id="b191459121"><a name="b191459121"></a><a name="b191459121"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.5.1.2"><p id="p1710139915556"><a name="p1710139915556"></a><a name="p1710139915556"></a><strong id="b37618596"><a name="b37618596"></a><a name="b37618596"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.2.5.1.3"><p id="p4303610815556"><a name="p4303610815556"></a><a name="p4303610815556"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.18%" id="mcps1.2.5.1.4"><p id="p6337274615556"><a name="p6337274615556"></a><a name="p6337274615556"></a><strong id="b376567515"><a name="b376567515"></a><a name="b376567515"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3291877615556"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.2.5.1.1 "><p id="p4917516615556"><a name="p4917516615556"></a><a name="p4917516615556"></a>bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.5.1.2 "><p id="p2376550915556"><a name="p2376550915556"></a><a name="p2376550915556"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.2.5.1.3 "><p id="p4595806815556"><a name="p4595806815556"></a><a name="p4595806815556"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.2.5.1.4 "><p id="p1610901815556"><a name="p1610901815556"></a><a name="p1610901815556"></a>Specifies the bandwidth objects. For details, see <a href="#table31854691">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **bandwidth**  field

    <a name="table31854691"></a>
    <table><thead align="left"><tr id="row6882862"><th class="cellrowborder" valign="top" width="13.350000000000001%" id="mcps1.2.5.1.1"><p id="p20640979"><a name="p20640979"></a><a name="p20640979"></a><strong id="b49957805"><a name="b49957805"></a><a name="b49957805"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.91%" id="mcps1.2.5.1.2"><p id="p61306625"><a name="p61306625"></a><a name="p61306625"></a><strong id="b1855646529"><a name="b1855646529"></a><a name="b1855646529"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.91%" id="mcps1.2.5.1.3"><p id="p5200653172316"><a name="p5200653172316"></a><a name="p5200653172316"></a><strong id="b308813508"><a name="b308813508"></a><a name="b308813508"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="58.830000000000005%" id="mcps1.2.5.1.4"><p id="p66889567"><a name="p66889567"></a><a name="p66889567"></a><strong id="b1511764873"><a name="b1511764873"></a><a name="b1511764873"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49345813"><td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.2.5.1.1 "><p id="p37587916"><a name="p37587916"></a><a name="p37587916"></a>publicip_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.2.5.1.2 "><p id="p24722347"><a name="p24722347"></a><a name="p24722347"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.2.5.1.3 "><p id="p18599757172316"><a name="p18599757172316"></a><a name="p18599757172316"></a>Array of <a href="#table30936422">publicip_info</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.830000000000005%" headers="mcps1.2.5.1.4 "><a name="ul290995117818"></a><a name="ul290995117818"></a><ul id="ul290995117818"><li>Specifies information about the EIP to be removed from the bandwidth. For details, see <a href="#table30936422">Table 4</a>.</li><li>The bandwidth, whose type is <strong id="b239618448438"><a name="b239618448438"></a><a name="b239618448438"></a>WHOLE</strong>, can be used by multiple EIPs. The number of EIPs varies depending on the tenant quota. By default, a shared bandwidth can be used by up to 20 EIPs.</li></ul>
    </td>
    </tr>
    <tr id="row193703372412"><td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.2.5.1.1 "><p id="p183711037154117"><a name="p183711037154117"></a><a name="p183711037154117"></a>charge_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.2.5.1.2 "><p id="p17371237114118"><a name="p17371237114118"></a><a name="p17371237114118"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.2.5.1.3 "><p id="p15371143714413"><a name="p15371143714413"></a><a name="p15371143714413"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.830000000000005%" headers="mcps1.2.5.1.4 "><p id="p877125719190"><a name="p877125719190"></a><a name="p877125719190"></a>After an EIP is removed from a shared bandwidth, a dedicated bandwidth will be allocated to the EIP, and you will be billed for the dedicated bandwidth.</p>
    <p id="p29217211425"><a name="p29217211425"></a><a name="p29217211425"></a>Specifies whether the dedicated bandwidth used by the EIP that has been removed from a shared bandwidth is billed by traffic or by bandwidth size.</p>
    <p id="p179232117423"><a name="p179232117423"></a><a name="p179232117423"></a>The value can be <strong id="b84235270618043"><a name="b84235270618043"></a><a name="b84235270618043"></a>bandwidth</strong> or <strong id="b84235270618050"><a name="b84235270618050"></a><a name="b84235270618050"></a>traffic</strong>.</p>
    </td>
    </tr>
    <tr id="row1125210414413"><td class="cellrowborder" valign="top" width="13.350000000000001%" headers="mcps1.2.5.1.1 "><p id="p1425214412410"><a name="p1425214412410"></a><a name="p1425214412410"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.2.5.1.2 "><p id="p1525210418416"><a name="p1525210418416"></a><a name="p1525210418416"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.91%" headers="mcps1.2.5.1.3 "><p id="p7252164114118"><a name="p7252164114118"></a><a name="p7252164114118"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.830000000000005%" headers="mcps1.2.5.1.4 "><p id="p42481825142019"><a name="p42481825142019"></a><a name="p42481825142019"></a>After an EIP is removed from a shared bandwidth, a dedicated bandwidth will be allocated to the EIP, and you will be billed for the dedicated bandwidth.</p>
    <p id="p16249725152011"><a name="p16249725152011"></a><a name="p16249725152011"></a>Specifies the size (Mbit/s) of the dedicated bandwidth used by the EIP that has been removed from a shared bandwidth.</p>
    <p id="p721494415220"><a name="p721494415220"></a><a name="p721494415220"></a>The value ranges from 1 Mbit/s to 2000 Mbit/s by default. (The specific range may vary depending on the configuration in each region. You can see the available bandwidth range on the management console.)</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **publicip\_info**  object

    <a name="table30936422"></a>
    <table><thead align="left"><tr id="row17161430"><th class="cellrowborder" valign="top" width="13.3%" id="mcps1.2.5.1.1"><p id="p47898561"><a name="p47898561"></a><a name="p47898561"></a><strong id="b1889898962"><a name="b1889898962"></a><a name="b1889898962"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.02%" id="mcps1.2.5.1.2"><p id="p157089251981"><a name="p157089251981"></a><a name="p157089251981"></a><strong id="b1822644524"><a name="b1822644524"></a><a name="b1822644524"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.96%" id="mcps1.2.5.1.3"><p id="p2828296517154"><a name="p2828296517154"></a><a name="p2828296517154"></a><strong id="b2109497716"><a name="b2109497716"></a><a name="b2109497716"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.72%" id="mcps1.2.5.1.4"><p id="p58761073"><a name="p58761073"></a><a name="p58761073"></a><strong id="b274459662"><a name="b274459662"></a><a name="b274459662"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62026502"><td class="cellrowborder" valign="top" width="13.3%" headers="mcps1.2.5.1.1 "><p id="p58090788"><a name="p58090788"></a><a name="p58090788"></a>publicip_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.02%" headers="mcps1.2.5.1.2 "><p id="p10708102514810"><a name="p10708102514810"></a><a name="p10708102514810"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.96%" headers="mcps1.2.5.1.3 "><p id="p921881117154"><a name="p921881117154"></a><a name="p921881117154"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.72%" headers="mcps1.2.5.1.4 "><p id="p476380"><a name="p476380"></a><a name="p476380"></a>Specifies the ID of the EIP that uses the bandwidth.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{Endpoint}/v2.0/{project_id}/bandwidths/{bandwidth_id}/remove
    
    {
        "bandwidth": {
            "publicip_info": [
                {
                    "publicip_id": "d91b0028-6f6b-4478-808a-297b75b6812a"
     
                },
                {
                    "publicip_id": "1d184b2c-4ec9-49b5-a3f9-27600a76ba3f"
                }
            ],
            "charge_mode": "traffic",
            "size": 22
        }
    }
    ```


## Response Message<a name="section8066134"></a>

-   Response parameter

    None

-   Example response

    None


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

