# Querying the Quota of a Tenant<a name="EN-US_TOPIC_0237964376"></a>

## Function<a name="section6252848"></a>

This API is used to query the resource quota of a tenant.

## URI<a name="section56275633"></a>

-   URI format:

    GET /v1.0/\{project\_id\}/quota

-   Parameter description:

    [Table 1](#table5250475)  describes the parameter of this API.


**Table  1**  Parameter description

<a name="table5250475"></a>
<table><thead align="left"><tr id="row56570155"><th class="cellrowborder" valign="top" width="16.3265306122449%" id="mcps1.2.5.1.1"><p id="p18779882"><a name="p18779882"></a><a name="p18779882"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="23.46938775510204%" id="mcps1.2.5.1.2"><p id="p44775506"><a name="p44775506"></a><a name="p44775506"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="26.53061224489796%" id="mcps1.2.5.1.3"><p id="p2937354"><a name="p2937354"></a><a name="p2937354"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="33.6734693877551%" id="mcps1.2.5.1.4"><p id="p36599098"><a name="p36599098"></a><a name="p36599098"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11736971"><td class="cellrowborder" valign="top" width="16.3265306122449%" headers="mcps1.2.5.1.1 "><p id="p11170596"><a name="p11170596"></a><a name="p11170596"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.46938775510204%" headers="mcps1.2.5.1.2 "><p id="p32403118"><a name="p32403118"></a><a name="p32403118"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="26.53061224489796%" headers="mcps1.2.5.1.3 "><p id="p7406929"><a name="p7406929"></a><a name="p7406929"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.6734693877551%" headers="mcps1.2.5.1.4 "><p id="p63090356"><a name="p63090356"></a><a name="p63090356"></a>Project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section36718649"></a>

None.

## Response<a name="section62032385"></a>

-   Status code:

    If status code "200 OK" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    [Table 2](#table52426669)  describes the response parameter.


**Table  2**  Parameters description

<a name="table52426669"></a>
<table><thead align="left"><tr id="row54210611"><th class="cellrowborder" valign="top" width="19.19191919191919%" id="mcps1.2.5.1.1"><p id="p28983346"><a name="p28983346"></a><a name="p28983346"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="30.303030303030305%" id="mcps1.2.5.1.2"><p id="p65949678"><a name="p65949678"></a><a name="p65949678"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.5.1.3"><p id="p40323662"><a name="p40323662"></a><a name="p40323662"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.5.1.4"><p id="p44991162"><a name="p44991162"></a><a name="p44991162"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20405531"><td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.2.5.1.1 "><p id="p42235353"><a name="p42235353"></a><a name="p42235353"></a>quotas</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.5.1.2 "><p id="p65620443"><a name="p65620443"></a><a name="p65620443"></a>Array.</p>
<p id="p53713082"><a name="p53713082"></a><a name="p53713082"></a>For details, see <a href="#ref478580623">Table 3</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.3 "><p id="p32369101"><a name="p32369101"></a><a name="p32369101"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.4 "><p id="p4651533"><a name="p4651533"></a><a name="p4651533"></a>List of resource quotas.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Parameter description of the quotas array

<a name="ref478580623"></a>
<table><thead align="left"><tr id="row64690895"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p5471175"><a name="p5471175"></a><a name="p5471175"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p40512015"><a name="p40512015"></a><a name="p40512015"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p60247759"><a name="p60247759"></a><a name="p60247759"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p48230320"><a name="p48230320"></a><a name="p48230320"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14341849"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p20839155"><a name="p20839155"></a><a name="p20839155"></a>resources</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p10250022"><a name="p10250022"></a><a name="p10250022"></a>Array.</p>
<p id="p25141336"><a name="p25141336"></a><a name="p25141336"></a>For details, see <a href="#ref478580726">Table 4</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p7314164"><a name="p7314164"></a><a name="p7314164"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p55576416"><a name="p55576416"></a><a name="p55576416"></a>Resource details.</p>
</td>
</tr>
<tr id="row30425700"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p48562603"><a name="p48562603"></a><a name="p48562603"></a>resource_user</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p41256791"><a name="p41256791"></a><a name="p41256791"></a>JSON string.</p>
<p id="p35766807"><a name="p35766807"></a><a name="p35766807"></a>For details, see <a href="#ref478580644">Table 5</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p35763197"><a name="p35763197"></a><a name="p35763197"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p11137863"><a name="p11137863"></a><a name="p11137863"></a>Information about a resource tenant.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Parameter description of the resources array

<a name="ref478580726"></a>
<table><thead align="left"><tr id="row23002923"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.1"><p id="p51297435"><a name="p51297435"></a><a name="p51297435"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p61451543"><a name="p61451543"></a><a name="p61451543"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.2.4.1.3"><p id="p11519112"><a name="p11519112"></a><a name="p11519112"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row60632918"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p12319336"><a name="p12319336"></a><a name="p12319336"></a>quota</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p58342183"><a name="p58342183"></a><a name="p58342183"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="p28096378"><a name="p28096378"></a><a name="p28096378"></a>Maximum number of resource items.</p>
</td>
</tr>
<tr id="row51540815"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p14056476"><a name="p14056476"></a><a name="p14056476"></a>used</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p64832753"><a name="p64832753"></a><a name="p64832753"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="p16961655"><a name="p16961655"></a><a name="p16961655"></a>Number of used resource items.</p>
</td>
</tr>
<tr id="row18437172"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p17015941"><a name="p17015941"></a><a name="p17015941"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p36114012"><a name="p36114012"></a><a name="p36114012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="p39553822"><a name="p39553822"></a><a name="p39553822"></a>Resource type.</p>
<p id="p20440084"><a name="p20440084"></a><a name="p20440084"></a>Options: instance and RAM.</p>
</td>
</tr>
<tr id="row49743029"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p2653577"><a name="p2653577"></a><a name="p2653577"></a>unit</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p13613185"><a name="p13613185"></a><a name="p13613185"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="p28926214"><a name="p28926214"></a><a name="p28926214"></a>Resource unit.</p>
<p id="p59009336"><a name="p59009336"></a><a name="p59009336"></a>If <strong id="b61321983"><a name="b61321983"></a><a name="b61321983"></a>type</strong> is set to <strong id="b15026939"><a name="b15026939"></a><a name="b15026939"></a>instance</strong>, a non-null value id returned for this parameter.</p>
</td>
</tr>
<tr id="row1024725"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p15893871"><a name="p15893871"></a><a name="p15893871"></a>max</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p12335157"><a name="p12335157"></a><a name="p12335157"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="p59623697"><a name="p59623697"></a><a name="p59623697"></a>Maximum limit of the quota.</p>
</td>
</tr>
<tr id="row66851225"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p46240174"><a name="p46240174"></a><a name="p46240174"></a>min</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p54466636"><a name="p54466636"></a><a name="p54466636"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.2.4.1.3 "><p id="p49721370"><a name="p49721370"></a><a name="p49721370"></a>Minimum limit o the quota.</p>
</td>
</tr>
</tbody>
</table>

**Table  5**  Parameter description of the resource\_user JSON string

<a name="ref478580644"></a>
<table><thead align="left"><tr id="row22881750"><th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.4.1.1"><p id="p41482479"><a name="p41482479"></a><a name="p41482479"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.4.1.2"><p id="p4637608"><a name="p4637608"></a><a name="p4637608"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="63.63636363636363%" id="mcps1.2.4.1.3"><p id="p40101929"><a name="p40101929"></a><a name="p40101929"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row27030811"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="p42012069"><a name="p42012069"></a><a name="p42012069"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.4.1.2 "><p id="p47534448"><a name="p47534448"></a><a name="p47534448"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.63636363636363%" headers="mcps1.2.4.1.3 "><p id="p25085092"><a name="p25085092"></a><a name="p25085092"></a>Resource tenant ID.</p>
</td>
</tr>
<tr id="row24439236"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="p33421095"><a name="p33421095"></a><a name="p33421095"></a>tenant_name</p>
</td>
<td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.4.1.2 "><p id="p22754183"><a name="p22754183"></a><a name="p22754183"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="63.63636363636363%" headers="mcps1.2.4.1.3 "><p id="p31149515"><a name="p31149515"></a><a name="p31149515"></a>Resource tenant name.</p>
</td>
</tr>
</tbody>
</table>

-   Example response:

    ```
    { 
     "quotas": { 
            "resources": [{ 
                "quota": 160, 
                "used": 3, 
                "type": "instance", 
                "min": 0, 
                "max": 2147483647, 
                "unit": null 
            }, 
            { 
                "quota": 64000, 
                "used": 12, 
                "type": "ram", 
                "min": 1, 
                "max": 1048576, 
                "unit": "GB" 
            }], 
            "resource_user": { 
                "tenant_id": "4d879867f4324c4297328c567196f2fb", 
                "tenant_name": "op_svc_dcs_34" 
      } 
     } 
    }
    ```


