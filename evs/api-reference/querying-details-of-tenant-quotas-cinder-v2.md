# Querying Details of Tenant Quotas<a name="evs_04_2073"></a>

## Function<a name="section9502070"></a>

This API is used to query the details of tenant quotas.

## URI<a name="section18409771"></a>

-   URI format

    GET /v2/\{project\_id\}/os-quota-sets/\{project\_id\}?usage=True

-   Parameter description

    <a name="table117163"></a>
    <table><thead align="left"><tr id="row55762700"><th class="cellrowborder" valign="top" width="33.33%" id="mcps1.1.4.1.1"><p id="p20484818"><a name="p20484818"></a><a name="p20484818"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.3%" id="mcps1.1.4.1.2"><p id="p48657561"><a name="p48657561"></a><a name="p48657561"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.370000000000005%" id="mcps1.1.4.1.3"><p id="p48948360"><a name="p48948360"></a><a name="p48948360"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5394248"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.1.4.1.1 "><p id="p34280961"><a name="p34280961"></a><a name="p34280961"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.1.4.1.2 "><p id="p25294426"><a name="p25294426"></a><a name="p25294426"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.370000000000005%" headers="mcps1.1.4.1.3 "><p id="p35582587"><a name="p35582587"></a><a name="p35582587"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section31470215"></a>

-   Example request

    ```
    GET https://{endpoint}/v2/{project_id}/os-quota-sets/{project_id}?usage=True
    ```


## Response<a name="section14796483"></a>

-   Parameter description

    <a name="table13993131410556"></a>
    <table><thead align="left"><tr id="row799321420553"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="p099351495511"><a name="p099351495511"></a><a name="p099351495511"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.62%" id="mcps1.1.4.1.2"><p id="p5993141425516"><a name="p5993141425516"></a><a name="p5993141425516"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p17993414135514"><a name="p17993414135514"></a><a name="p17993414135514"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row209931814185513"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p119941014125514"><a name="p119941014125514"></a><a name="p119941014125514"></a>quota_set</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p14994514165520"><a name="p14994514165520"></a><a name="p14994514165520"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p1099416145558"><a name="p1099416145558"></a><a name="p1099416145558"></a>Specifies the queried quota information. For details, see <a href="#li4741865201620">Parameters in the quota_set field</a>.</p>
    </td>
    </tr>
    <tr id="row3451722569"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li4741865201620"></a>Parameters in the  **quota\_set**  field

    <a name="table42676787201620"></a>
    <table><thead align="left"><tr id="row15715964201620"><th class="cellrowborder" valign="top" width="20.24%" id="mcps1.1.4.1.1"><p id="p65033611201620"><a name="p65033611201620"></a><a name="p65033611201620"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.62%" id="mcps1.1.4.1.2"><p id="p5090379315311"><a name="p5090379315311"></a><a name="p5090379315311"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p1989612244512"><a name="p1989612244512"></a><a name="p1989612244512"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60124619201620"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p38255980201620"><a name="p38255980201620"></a><a name="p38255980201620"></a>volumes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p2956653915311"><a name="p2956653915311"></a><a name="p2956653915311"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p10336815201620"><a name="p10336815201620"></a><a name="p10336815201620"></a>Specifies the number of disks. This parameter is made up of key-value pairs which include <strong id="b617164102112"><a name="b617164102112"></a><a name="b617164102112"></a>reserved</strong>, <strong id="b19590835125916"><a name="b19590835125916"></a><a name="b19590835125916"></a>allocated</strong>, <strong id="b12172447219"><a name="b12172447219"></a><a name="b12172447219"></a>limit</strong>, and <strong id="b1117220414217"><a name="b1117220414217"></a><a name="b1117220414217"></a>in_use</strong>.</p>
    </td>
    </tr>
    <tr id="row25922478201620"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p19345972201620"><a name="p19345972201620"></a><a name="p19345972201620"></a>snapshots</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p4607944115311"><a name="p4607944115311"></a><a name="p4607944115311"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p26061300201620"><a name="p26061300201620"></a><a name="p26061300201620"></a>Specifies the number of snapshots. This parameter is made up of key-value pairs which include <strong id="b35972435596"><a name="b35972435596"></a><a name="b35972435596"></a>reserved</strong>, <strong id="b4263114915920"><a name="b4263114915920"></a><a name="b4263114915920"></a>allocated</strong>, <strong id="b1059817439595"><a name="b1059817439595"></a><a name="b1059817439595"></a>limit</strong>, and <strong id="b19599104305915"><a name="b19599104305915"></a><a name="b19599104305915"></a>in_use</strong>.</p>
    </td>
    </tr>
    <tr id="row33225116201620"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p6879872201620"><a name="p6879872201620"></a><a name="p6879872201620"></a>gigabytes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p4144727715311"><a name="p4144727715311"></a><a name="p4144727715311"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p41689235201620"><a name="p41689235201620"></a><a name="p41689235201620"></a>Specifies the total size (GB) of disks and snapshots allowed by the quota. This parameter is made up of key-value pairs which include <strong id="b63503695111621"><a name="b63503695111621"></a><a name="b63503695111621"></a>reserved</strong>, <strong id="b10649155513591"><a name="b10649155513591"></a><a name="b10649155513591"></a>allocated</strong>, <strong id="b34662348111621"><a name="b34662348111621"></a><a name="b34662348111621"></a>limit</strong>, and <strong id="b43525681111621"><a name="b43525681111621"></a><a name="b43525681111621"></a>in_use</strong>.</p>
    </td>
    </tr>
    <tr id="row39658796201620"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p58245913201620"><a name="p58245913201620"></a><a name="p58245913201620"></a>volume_{volume_type}</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p178624415311"><a name="p178624415311"></a><a name="p178624415311"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p33568305201620"><a name="p33568305201620"></a><a name="p33568305201620"></a>Specifies the number of disks reserved for a specified volume type. For example, the parameter name may be <strong id="b122905187496"><a name="b122905187496"></a><a name="b122905187496"></a>volume_SATA</strong> or <strong id="b13432152018497"><a name="b13432152018497"></a><a name="b13432152018497"></a>volume_SSD</strong>. The parameter value is made up of key-value pairs which include <strong id="b163691642132114"><a name="b163691642132114"></a><a name="b163691642132114"></a>reserved</strong>, <strong id="b1474005655415"><a name="b1474005655415"></a><a name="b1474005655415"></a>allocated</strong>, <strong id="b33704428213"><a name="b33704428213"></a><a name="b33704428213"></a>limit</strong>, and <strong id="b1537194211217"><a name="b1537194211217"></a><a name="b1537194211217"></a>in_use</strong>.</p>
    </td>
    </tr>
    <tr id="row33679293201620"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p6988929729"><a name="p6988929729"></a><a name="p6988929729"></a>snapshots_{volume_type}</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p1046809615311"><a name="p1046809615311"></a><a name="p1046809615311"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p19567167201620"><a name="p19567167201620"></a><a name="p19567167201620"></a>Specifies the number of snapshots reserved for a specified volume type. For example, the parameter name may be <strong id="b12800148115615"><a name="b12800148115615"></a><a name="b12800148115615"></a>snapshots_SATA</strong> or <strong id="b1751115495515"><a name="b1751115495515"></a><a name="b1751115495515"></a>snapshots_SSD</strong>. The parameter value is made up of key-value pairs which include <strong id="b6891233155412"><a name="b6891233155412"></a><a name="b6891233155412"></a>reserved</strong>, <strong id="b1995483115613"><a name="b1995483115613"></a><a name="b1995483115613"></a>allocated</strong>, <strong id="b1489273312547"><a name="b1489273312547"></a><a name="b1489273312547"></a>limit</strong>, and <strong id="b989373319543"><a name="b989373319543"></a><a name="b989373319543"></a>in_use</strong>.</p>
    </td>
    </tr>
    <tr id="row41886775201620"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p932213524218"><a name="p932213524218"></a><a name="p932213524218"></a>gigabytes_{volume_type}</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p4260948115311"><a name="p4260948115311"></a><a name="p4260948115311"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p3943730201620"><a name="p3943730201620"></a><a name="p3943730201620"></a>Specifies the capacity (GB) reserved for a specified volume type. For example, the parameter name may be <strong id="b1835061125712"><a name="b1835061125712"></a><a name="b1835061125712"></a>gigabytes_SATA</strong> or <strong id="b103501111185713"><a name="b103501111185713"></a><a name="b103501111185713"></a>gigabytes_SSD</strong>. The parameter value is made up of key-value pairs which include <strong id="b24105662111621"><a name="b24105662111621"></a><a name="b24105662111621"></a>reserved</strong>, <strong id="b12179154914574"><a name="b12179154914574"></a><a name="b12179154914574"></a>allocated</strong>, <strong id="b15624373111621"><a name="b15624373111621"></a><a name="b15624373111621"></a>limit</strong>, and <strong id="b6401629111621"><a name="b6401629111621"></a><a name="b6401629111621"></a>in_use</strong>.</p>
    </td>
    </tr>
    <tr id="row35493575201620"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p56407339201620"><a name="p56407339201620"></a><a name="p56407339201620"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p2881594215311"><a name="p2881594215311"></a><a name="p2881594215311"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p50275403201620"><a name="p50275403201620"></a><a name="p50275403201620"></a>Specifies the tenant ID. <span id="text19941457165313"><a name="text19941457165313"></a><a name="text19941457165313"></a>The tenant ID is actually the project ID.</span></p>
    </td>
    </tr>
    <tr id="row49825446201620"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p9329306201620"><a name="p9329306201620"></a><a name="p9329306201620"></a>backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p5238998415311"><a name="p5238998415311"></a><a name="p5238998415311"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p6295376201620"><a name="p6295376201620"></a><a name="p6295376201620"></a>Specifies the number of backups. This parameter is made up of key-value pairs which include <strong id="b789155785917"><a name="b789155785917"></a><a name="b789155785917"></a>reserved</strong>, <strong id="b191662018011"><a name="b191662018011"></a><a name="b191662018011"></a>allocated</strong>, <strong id="b49005711595"><a name="b49005711595"></a><a name="b49005711595"></a>limit</strong>, and <strong id="b13916577592"><a name="b13916577592"></a><a name="b13916577592"></a>in_use</strong>.</p>
    </td>
    </tr>
    <tr id="row56658385201620"><td class="cellrowborder" valign="top" width="20.24%" headers="mcps1.1.4.1.1 "><p id="p25926512201620"><a name="p25926512201620"></a><a name="p25926512201620"></a>backup_gigabytes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.62%" headers="mcps1.1.4.1.2 "><p id="p1573030215311"><a name="p1573030215311"></a><a name="p1573030215311"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p49989712201620"><a name="p49989712201620"></a><a name="p49989712201620"></a>Specifies the backup size, in GB. This parameter is made up of key-value pairs which include <strong id="b19174527017"><a name="b19174527017"></a><a name="b19174527017"></a>reserved</strong>, <strong id="b958723305"><a name="b958723305"></a><a name="b958723305"></a>allocated</strong>, <strong id="b6175152906"><a name="b6175152906"></a><a name="b6175152906"></a>limit</strong>, and <strong id="b7176422013"><a name="b7176422013"></a><a name="b7176422013"></a>in_use</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the  **limit**  value returned in the response is  **-1**, no quota limit has been set.  

-   <a name="li0419202382514"></a>Parameters in the  **error**  field

    <a name="evs_04_2013_table15441099103019"></a>
    <table><thead align="left"><tr id="evs_04_2013_row54094047103019"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="evs_04_2013_p19541716103019"><a name="evs_04_2013_p19541716103019"></a><a name="evs_04_2013_p19541716103019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="evs_04_2013_p39375186103019"><a name="evs_04_2013_p39375186103019"></a><a name="evs_04_2013_p39375186103019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2013_p38578950103019"><a name="evs_04_2013_p38578950103019"></a><a name="evs_04_2013_p38578950103019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2013_row59401790103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p46815658103019"><a name="evs_04_2013_p46815658103019"></a><a name="evs_04_2013_p46815658103019"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p33971979103019"><a name="evs_04_2013_p33971979103019"></a><a name="evs_04_2013_p33971979103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p21623243103019"><a name="evs_04_2013_p21623243103019"></a><a name="evs_04_2013_p21623243103019"></a>Specifies the error message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="evs_04_2013_row60391466103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p59870541103019"><a name="evs_04_2013_p59870541103019"></a><a name="evs_04_2013_p59870541103019"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p17675690103019"><a name="evs_04_2013_p17675690103019"></a><a name="evs_04_2013_p17675690103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p6087468103019"><a name="evs_04_2013_p6087468103019"></a><a name="evs_04_2013_p6087468103019"></a>Specifies the error code returned when an error occurs.</p>
    <p id="evs_04_2013_p54787218103019"><a name="evs_04_2013_p54787218103019"></a><a name="evs_04_2013_p54787218103019"></a>For details about the error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "quota_set": {
            "gigabytes_SAS": {
                "reserved": 0, 
                "allocated":0,
                "limit": -1, 
                "in_use": 21
            }, 
            "volumes_SATA": {
                "reserved": 0, 
                "allocated":0,
                "limit": -1, 
                "in_use": 8
            }, 
            "gigabytes": {
                "reserved": 0, 
                "allocated":0,
                "limit": 42790, 
                "in_use": 2792
            }, 
            "backup_gigabytes": {
                "reserved": 0,
                "allocated":0, 
                "limit": 5120, 
                "in_use": 51
            }, 
            "snapshots_SAS": {
                "reserved": 0, 
                "allocated":0,
                "limit": -1, 
                "in_use": 0
            }, 
            "volumes_SSD": {
                "reserved": 0, 
                "allocated":0,
                "limit": -1, 
                "in_use": 28
            }, 
            "snapshots": {
                "reserved": 0, 
                "allocated":0,
                "limit": 10, 
                "in_use": 6
            }, 
            "id": "cd631140887d4b6e9c786b67a6dd4c02", 
            "volumes_SAS": {
                "reserved": 0, 
                "allocated":0,
                "limit": -1, 
                "in_use": 2
            }, 
            "snapshots_SSD": {
                "reserved": 0, 
                "allocated":0,
                "limit": -1, 
                "in_use": 0
            }, 
            "volumes": {
                "reserved": 0, 
                "allocated":0,
                "limit": -1, 
                "in_use": 108
            }, 
            "gigabytes_SATA": {
                "reserved": 0, 
                "allocated":0,
                "limit": -1, 
                "in_use": 168
            }, 
            "backups": {
                "reserved": 0, 
                "allocated":0,
                "limit": 100, 
                "in_use": 10
            }, 
            "gigabytes_SSD": {
                "reserved": 0, 
                "allocated":0,
                "limit": -1, 
                "in_use": 1085
            }, 
            "snapshots_SATA": {
                "reserved": 0, 
                "allocated":0,
                "limit": -1, 
                "in_use": 0
            }
        }
    }
    ```

    or

    ```
    {
        "error": {
            "message": "XXXX", 
            "code": "XXX"
        }
    }
    ```

    In the preceding example,  **error**  indicates a general error, for example,  **badrequest**  or  **itemNotFound**. An example is provided as follows:

    ```
    {
        "badrequest": {
            "message": "XXXX", 
            "code": "XXX"
        }
    }
    ```


## Status Codes<a name="section66059488"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).

