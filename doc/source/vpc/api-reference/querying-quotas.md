# Querying Quotas<a name="vpc_quota_0001"></a>

## Function<a name="section52301286"></a>

This API is used to query network resource quotas of a tenant. The network resources include VPCs, subnets, security groups, security group rules, EIPs, and VPNs.

## URI<a name="section949529"></a>

GET /v1/\{project\_id\}/quotas

Example:

```
GET https://{Endpoint}/v1/{project_id}/quotas?type={type}
```

[Table 1](#table38014313)  describes the parameters.

**Table  1**  Parameter description

<a name="table38014313"></a>
<table><thead align="left"><tr id="row46663997"><th class="cellrowborder" valign="top" width="18.8%" id="mcps1.2.5.1.1"><p id="p21687383"><a name="p21687383"></a><a name="p21687383"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.2"><p id="p11847581"><a name="p11847581"></a><a name="p11847581"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.42%" id="mcps1.2.5.1.3"><p id="p18682156172640"><a name="p18682156172640"></a><a name="p18682156172640"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45.86%" id="mcps1.2.5.1.4"><p id="p20130041"><a name="p20130041"></a><a name="p20130041"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19920592"><td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.1 "><p id="p2955276"><a name="p2955276"></a><a name="p2955276"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="p38050837"><a name="p38050837"></a><a name="p38050837"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.3 "><p id="p36859696172640"><a name="p36859696172640"></a><a name="p36859696172640"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.86%" headers="mcps1.2.5.1.4 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row23099752"><td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.1 "><p id="p59140623"><a name="p59140623"></a><a name="p59140623"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="p25661150"><a name="p25661150"></a><a name="p25661150"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.3 "><p id="p32845400172640"><a name="p32845400172640"></a><a name="p32845400172640"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.86%" headers="mcps1.2.5.1.4 "><p id="p4851544151913"><a name="p4851544151913"></a><a name="p4851544151913"></a>Specifies the resource type.</p>
<p id="p48177051173921"><a name="p48177051173921"></a><a name="p48177051173921"></a>The value can be <strong id="b768214556573"><a name="b768214556573"></a><a name="b768214556573"></a>vpc</strong>, <strong id="b06831955185713"><a name="b06831955185713"></a><a name="b06831955185713"></a>subnet</strong>, <strong id="b16831955125717"><a name="b16831955125717"></a><a name="b16831955125717"></a>securityGroup</strong>, <strong id="b20684055125715"><a name="b20684055125715"></a><a name="b20684055125715"></a>securityGroupRule</strong>, <strong id="b3685155513571"><a name="b3685155513571"></a><a name="b3685155513571"></a>publicIp</strong>, <strong id="b1568555555719"><a name="b1568555555719"></a><a name="b1568555555719"></a>vpn</strong>, <strong id="b17687105513579"><a name="b17687105513579"></a><a name="b17687105513579"></a>vpngw</strong>, <strong id="b96871955115713"><a name="b96871955115713"></a><a name="b96871955115713"></a>physicalConnect</strong>, <strong id="b146871755115717"><a name="b146871755115717"></a><a name="b146871755115717"></a>virtualInterface</strong>, <strong id="b268925525714"><a name="b268925525714"></a><a name="b268925525714"></a>vpcPeer</strong>, <strong id="b16690135575710"><a name="b16690135575710"></a><a name="b16690135575710"></a>firewall</strong>, <strong id="b9690155155715"><a name="b9690155155715"></a><a name="b9690155155715"></a>shareBandwidth</strong>, <strong id="b969112557579"><a name="b969112557579"></a><a name="b969112557579"></a>shareBandwidthIP</strong>, <strong id="b4693115512570"><a name="b4693115512570"></a><a name="b4693115512570"></a>loadbalancer</strong>, or <strong id="b66931355205719"><a name="b66931355205719"></a><a name="b66931355205719"></a>listener</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section8545767"></a>

-   Request parameter

    ```
    None
    ```

-   Example request

    ```
    GET https://{Endpoint}/v1/{project_id}/quotas
    ```


## Response Message<a name="section9803039"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table66351430155536"></a>
    <table><thead align="left"><tr id="row25019730155536"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p13332267155536"><a name="p13332267155536"></a><a name="p13332267155536"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="p30154725155536"><a name="p30154725155536"></a><a name="p30154725155536"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="p26613655155536"><a name="p26613655155536"></a><a name="p26613655155536"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8222433155536"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p62037356155536"><a name="p62037356155536"></a><a name="p62037356155536"></a>quotas</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p11836771155536"><a name="p11836771155536"></a><a name="p11836771155536"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="p39072163155536"><a name="p39072163155536"></a><a name="p39072163155536"></a>Specifies the quota object. For details, see <a href="#table11308015155544">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **quotas**  field

    <a name="table11308015155544"></a>
    <table><thead align="left"><tr id="row37694756155544"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="p33376361155544"><a name="p33376361155544"></a><a name="p33376361155544"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.509999999999998%" id="mcps1.2.4.1.2"><p id="p6082737155544"><a name="p6082737155544"></a><a name="p6082737155544"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.15%" id="mcps1.2.4.1.3"><p id="p22939651155544"><a name="p22939651155544"></a><a name="p22939651155544"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46172458155544"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="p48981646155544"><a name="p48981646155544"></a><a name="p48981646155544"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p51341867155544"><a name="p51341867155544"></a><a name="p51341867155544"></a>Array of <a href="#table8208684">resource</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.15%" headers="mcps1.2.4.1.3 "><p id="p48584024155544"><a name="p48584024155544"></a><a name="p48584024155544"></a>Specifies the resource objects. For details, see <a href="#table8208684">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Description of the  **resource**  field

    <a name="table8208684"></a>
    <table><thead align="left"><tr id="row19762867"><th class="cellrowborder" valign="top" width="15.959999999999999%" id="mcps1.2.4.1.1"><p id="p57288388"><a name="p57288388"></a><a name="p57288388"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.1%" id="mcps1.2.4.1.2"><p id="p3523125172732"><a name="p3523125172732"></a><a name="p3523125172732"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.94%" id="mcps1.2.4.1.3"><p id="p59475690"><a name="p59475690"></a><a name="p59475690"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52801617"><td class="cellrowborder" valign="top" width="15.959999999999999%" headers="mcps1.2.4.1.1 "><p id="p49072547"><a name="p49072547"></a><a name="p49072547"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.1%" headers="mcps1.2.4.1.2 "><p id="p16937702172732"><a name="p16937702172732"></a><a name="p16937702172732"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.2.4.1.3 "><a name="ul15534105019216"></a><a name="ul15534105019216"></a><ul id="ul15534105019216"><li>Specifies the resource type.</li><li>The value can be <strong id="b115144375818"><a name="b115144375818"></a><a name="b115144375818"></a>vpc</strong>, <strong id="b25204305819"><a name="b25204305819"></a><a name="b25204305819"></a>subnet</strong>, <strong id="b1854104318581"><a name="b1854104318581"></a><a name="b1854104318581"></a>securityGroup</strong>, <strong id="b1354164313586"><a name="b1354164313586"></a><a name="b1354164313586"></a>securityGroupRule</strong>, <strong id="b9558433585"><a name="b9558433585"></a><a name="b9558433585"></a>publicIp</strong>, <strong id="b195524355816"><a name="b195524355816"></a><a name="b195524355816"></a>vpn</strong>, <strong id="b84235270619199"><a name="b84235270619199"></a><a name="b84235270619199"></a>vpngw</strong>, <strong id="b547665931192357"><a name="b547665931192357"></a><a name="b547665931192357"></a>physicalConnect</strong>, <strong id="b463516335192357"><a name="b463516335192357"></a><a name="b463516335192357"></a>virtualInterface</strong>, <strong id="b1389639160191741"><a name="b1389639160191741"></a><a name="b1389639160191741"></a>vpcPeer</strong>, <strong id="b328973019191741"><a name="b328973019191741"></a><a name="b328973019191741"></a>firewall</strong>, <strong id="b171092584191741"><a name="b171092584191741"></a><a name="b171092584191741"></a>shareBandwidth</strong>, or <strong id="b1584642343191741"><a name="b1584642343191741"></a><a name="b1584642343191741"></a>shareBandwidthIP</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row49017803"><td class="cellrowborder" valign="top" width="15.959999999999999%" headers="mcps1.2.4.1.1 "><p id="p11019092"><a name="p11019092"></a><a name="p11019092"></a>used</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.1%" headers="mcps1.2.4.1.2 "><p id="p29776587172732"><a name="p29776587172732"></a><a name="p29776587172732"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.2.4.1.3 "><a name="ul255215419218"></a><a name="ul255215419218"></a><ul id="ul255215419218"><li>Specifies the number of created network resources.</li><li>The value ranges from <strong id="b1407708997192551"><a name="b1407708997192551"></a><a name="b1407708997192551"></a>0</strong> to the value of <strong id="b637466560192551"><a name="b637466560192551"></a><a name="b637466560192551"></a>quota</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row13742502"><td class="cellrowborder" valign="top" width="15.959999999999999%" headers="mcps1.2.4.1.1 "><p id="p39400845"><a name="p39400845"></a><a name="p39400845"></a>quota</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.1%" headers="mcps1.2.4.1.2 "><p id="p63093324172732"><a name="p63093324172732"></a><a name="p63093324172732"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.2.4.1.3 "><a name="ul399282316224"></a><a name="ul399282316224"></a><ul id="ul399282316224"><li>Specifies the maximum quota values for the resources.</li><li>The value ranges from the default quota value to the maximum quota value.</li><li>The default resource quota values can be changed. You must configure the quota values in the underlying system in advance. The default quota values of network resources are as follows:<p id="p38368340193625"><a name="p38368340193625"></a><a name="p38368340193625"></a>VPC: <strong id="b12897103314391"><a name="b12897103314391"></a><a name="b12897103314391"></a>5</strong></p>
    <p id="p38028380193629"><a name="p38028380193629"></a><a name="p38028380193629"></a>Subnet: <strong id="b23012464194454"><a name="b23012464194454"></a><a name="b23012464194454"></a>100</strong></p>
    <p id="p47717668193633"><a name="p47717668193633"></a><a name="p47717668193633"></a>Security group: <strong id="b58878568194459"><a name="b58878568194459"></a><a name="b58878568194459"></a>100</strong></p>
    <p id="p5328104193636"><a name="p5328104193636"></a><a name="p5328104193636"></a>Security group rule: <strong id="b1291945119453"><a name="b1291945119453"></a><a name="b1291945119453"></a>5000</strong></p>
    <p id="p43080847193649"><a name="p43080847193649"></a><a name="p43080847193649"></a>EIP: <strong id="b1042585419457"><a name="b1042585419457"></a><a name="b1042585419457"></a>10</strong></p>
    <p id="p3568935193652"><a name="p3568935193652"></a><a name="p3568935193652"></a>VPN: <strong id="b16518479194510"><a name="b16518479194510"></a><a name="b16518479194510"></a>5</strong></p>
    <p id="p44080164193657"><a name="p44080164193657"></a><a name="p44080164193657"></a>VPN gateway: <strong id="b40390867194513"><a name="b40390867194513"></a><a name="b40390867194513"></a>2</strong></p>
    <p id="p5934768819371"><a name="p5934768819371"></a><a name="p5934768819371"></a>Direct Connect connection: <strong id="b13647868194520"><a name="b13647868194520"></a><a name="b13647868194520"></a>10</strong></p>
    <p id="p1480511319377"><a name="p1480511319377"></a><a name="p1480511319377"></a>Virtual interface: <strong id="b35477743194525"><a name="b35477743194525"></a><a name="b35477743194525"></a>50</strong></p>
    <p id="p47498695193731"><a name="p47498695193731"></a><a name="p47498695193731"></a>VPC peering connection: <strong id="b46078690194528"><a name="b46078690194528"></a><a name="b46078690194528"></a>50</strong></p>
    <p id="p37182716193735"><a name="p37182716193735"></a><a name="p37182716193735"></a>Firewall: <strong id="b29028585194533"><a name="b29028585194533"></a><a name="b29028585194533"></a>200</strong></p>
    <p id="p54331441193739"><a name="p54331441193739"></a><a name="p54331441193739"></a>Shared bandwidth: <strong id="b9281383194535"><a name="b9281383194535"></a><a name="b9281383194535"></a>5</strong></p>
    <p id="p34080811193622"><a name="p34080811193622"></a><a name="p34080811193622"></a>IP address with shared bandwidth: <strong id="b6950173194539"><a name="b6950173194539"></a><a name="b6950173194539"></a>20</strong></p>
    <p id="p17633487113"><a name="p17633487113"></a><a name="p17633487113"></a></p>
    </li></ul>
    </td>
    </tr>
    <tr id="row4925573392829"><td class="cellrowborder" valign="top" width="15.959999999999999%" headers="mcps1.2.4.1.1 "><p id="p576726292829"><a name="p576726292829"></a><a name="p576726292829"></a>min</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.1%" headers="mcps1.2.4.1.2 "><p id="p3758450892829"><a name="p3758450892829"></a><a name="p3758450892829"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.2.4.1.3 "><p id="p6018282892829"><a name="p6018282892829"></a><a name="p6018282892829"></a>Specifies the minimum quota value allowed.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "quotas": {
            "resources": [
                {
                    "type": "vpc",
                    "used": 4,
                    "quota": 150,
                    "min": 0
                },
                {
                    "type": "subnet",
                    "used": 5,
                    "quota": 400,
                    "min": 0
                },
                {
                    "type": "securityGroup",
                    "used": 1,
                    "quota": 100,
                    "min": 0
                },
                {
                    "type": "securityGroupRule",
                    "used": 6,
                    "quota": 5000,
                    "min": 0
                },
                {
                    "type": "publicIp",
                    "used": 2,
                    "quota": 10,
                    "min": 0
                },
                {
                    "type": "vpn",
                    "used": 0,
                    "quota": 5,
                    "min": 0
                },
                {
                    "type": "vpngw",
                    "used": 0,
                    "quota": 2,
                    "min": 0
                },
                {
                    "type": "vpcPeer",
                    "used": 0,
                    "quota": 50,
                    "min": 0
                },
                {
                    "type":"physicalConnect",
                    "used":0,
                    "quota":10,
                    "min":0
                },
                {
                    "type":"virtualInterface",
                    "used":0,
                    "quota":50,
                    "min":0
                },
                {
                    "type": "firewall",
                    "used": 0,
                    "quota": 200,
                    "min": 0
                },
                {
                    "type": "shareBandwidth",
                    "used": 0,
                    "quota": 5,
                    "min": 0
                },
                {
                    "type": "shareBandwidthIP",
                    "used": 0,
                    "quota": 20,
                    "min": 0
                },
                {
                    "type": "loadbalancer",
                    "used": 0,
                    "quota": 10,
                    "min": 0
                },
                {
                    "type": "listener",
                    "used": 0,
                    "quota": 10,
                    "min": 0
                }
            ]
        }
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

