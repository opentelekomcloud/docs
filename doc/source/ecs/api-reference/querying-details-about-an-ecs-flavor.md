# Querying Details About an ECS Flavor<a name="EN-US_TOPIC_0020212659"></a>

## Function<a name="section64833508"></a>

This API is used to query the details about an ECS flavor based on the flavor ID.

## URI<a name="section46630661"></a>

GET /v2/\{project\_id\}/flavors/\{flavors\_id\}

GET /v2.1/\{project\_id\}/flavors/\{flavors\_id\}

[Table 1](#table47154420)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table47154420"></a>
<table><thead align="left"><tr id="row324668"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.16%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.86%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17004965"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p35224963"><a name="p35224963"></a><a name="p35224963"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p34649765"><a name="p34649765"></a><a name="p34649765"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.86%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row26746391"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p18974100"><a name="p18974100"></a><a name="p18974100"></a>flavors_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p60507121"><a name="p60507121"></a><a name="p60507121"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.86%" headers="mcps1.2.4.1.3 "><p id="p2129750"><a name="p2129750"></a><a name="p2129750"></a>Specifies the flavor ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section17022773"></a>

None

## Response<a name="section18987236"></a>

[Table 2](#table61695723)  describes the response parameters.

**Table  2**  Response parameters

<a name="table61695723"></a>
<table><thead align="left"><tr id="row52977523"><th class="cellrowborder" valign="top" width="16.85%" id="mcps1.2.4.1.1"><p id="p110452114597"><a name="p110452114597"></a><a name="p110452114597"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.29%" id="mcps1.2.4.1.2"><p id="p71044217595"><a name="p71044217595"></a><a name="p71044217595"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.86%" id="mcps1.2.4.1.3"><p id="p15104102175910"><a name="p15104102175910"></a><a name="p15104102175910"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2794650"><td class="cellrowborder" valign="top" width="16.85%" headers="mcps1.2.4.1.1 "><p id="p25040094"><a name="p25040094"></a><a name="p25040094"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.2.4.1.2 "><p id="p5563313"><a name="p5563313"></a><a name="p5563313"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="66.86%" headers="mcps1.2.4.1.3 "><p id="p29123463"><a name="p29123463"></a><a name="p29123463"></a>Specifies ECS flavors. For details, see <a href="#table20109663">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **flavor**  field description

<a name="table20109663"></a>
<table><thead align="left"><tr id="row50842877"><th class="cellrowborder" valign="top" width="16.86%" id="mcps1.2.4.1.1"><p id="p1011213912218"><a name="p1011213912218"></a><a name="p1011213912218"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.2%" id="mcps1.2.4.1.2"><p id="p111215914215"><a name="p111215914215"></a><a name="p111215914215"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.94%" id="mcps1.2.4.1.3"><p id="p121121091925"><a name="p121121091925"></a><a name="p121121091925"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row37029065"><td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.2.4.1.1 "><p id="p46564252"><a name="p46564252"></a><a name="p46564252"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="p28514710"><a name="p28514710"></a><a name="p28514710"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.94%" headers="mcps1.2.4.1.3 "><p id="p50584809"><a name="p50584809"></a><a name="p50584809"></a>Specifies the ECS flavor ID.</p>
</td>
</tr>
<tr id="row52610097"><td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.2.4.1.1 "><p id="p33559471"><a name="p33559471"></a><a name="p33559471"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="p66621782"><a name="p66621782"></a><a name="p66621782"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.94%" headers="mcps1.2.4.1.3 "><p id="p47570623"><a name="p47570623"></a><a name="p47570623"></a>Specifies the name of the ECS flavor.</p>
</td>
</tr>
<tr id="row12413842183117"><td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.2.4.1.1 "><p id="p184132423315"><a name="p184132423315"></a><a name="p184132423315"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="p11413142153116"><a name="p11413142153116"></a><a name="p11413142153116"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.94%" headers="mcps1.2.4.1.3 "><p id="p1941384233119"><a name="p1941384233119"></a><a name="p1941384233119"></a>Specifies details about an ECS flavor.</p>
<p id="p210419138321"><a name="p210419138321"></a><a name="p210419138321"></a>This field is supported in microversions later than 2.55.</p>
</td>
</tr>
<tr id="row25482430"><td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.2.4.1.1 "><p id="p50810959"><a name="p50810959"></a><a name="p50810959"></a>vcpus</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="p40977906"><a name="p40977906"></a><a name="p40977906"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.94%" headers="mcps1.2.4.1.3 "><p id="p9449599"><a name="p9449599"></a><a name="p9449599"></a>Specifies the number of vCPUs in the ECS flavor.</p>
</td>
</tr>
<tr id="row2289826710437"><td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.2.4.1.1 "><p id="p6260494310453"><a name="p6260494310453"></a><a name="p6260494310453"></a>ram</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="p3783561810453"><a name="p3783561810453"></a><a name="p3783561810453"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.94%" headers="mcps1.2.4.1.3 "><p id="p42285210453"><a name="p42285210453"></a><a name="p42285210453"></a>Specifies the memory size (MB) in the ECS flavor.</p>
</td>
</tr>
<tr id="row17937528"><td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.2.4.1.1 "><p id="p43653635"><a name="p43653635"></a><a name="p43653635"></a>disk</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="p57980147"><a name="p57980147"></a><a name="p57980147"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.94%" headers="mcps1.2.4.1.3 "><p id="p56052334"><a name="p56052334"></a><a name="p56052334"></a>Specifies the system disk size in the ECS flavor.</p>
<p id="p34708966"><a name="p34708966"></a><a name="p34708966"></a>This parameter has not been used. Its default value is <strong id="b84235270611135"><a name="b84235270611135"></a><a name="b84235270611135"></a>0</strong>.</p>
</td>
</tr>
<tr id="row43945239"><td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.2.4.1.1 "><p id="p2794612"><a name="p2794612"></a><a name="p2794612"></a>swap</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="p14734188"><a name="p14734188"></a><a name="p14734188"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.94%" headers="mcps1.2.4.1.3 "><p id="p1699362755013"><a name="p1699362755013"></a><a name="p1699362755013"></a>Specifies the swap partition size required by the ECS flavor.</p>
<p id="p4563766173425"><a name="p4563766173425"></a><a name="p4563766173425"></a>This parameter has not been used. Its default value is <strong id="b84235270611135_1"><a name="b84235270611135_1"></a><a name="b84235270611135_1"></a>""</strong>.</p>
</td>
</tr>
<tr id="row34246806"><td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.2.4.1.1 "><p id="p22527890"><a name="p22527890"></a><a name="p22527890"></a>OS-FLV-EXT-DATA:ephemeral</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="p31767774"><a name="p31767774"></a><a name="p31767774"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="66.94%" headers="mcps1.2.4.1.3 "><p id="p16591226713"><a name="p16591226713"></a><a name="p16591226713"></a>Specifies the temporary disk size. This is an extended attribute.</p>
<p id="p1140814148017"><a name="p1140814148017"></a><a name="p1140814148017"></a>This parameter has not been used. Its default value is <strong id="b84235270611135_2"><a name="b84235270611135_2"></a><a name="b84235270611135_2"></a>0</strong>.</p>
</td>
</tr>
<tr id="row55347837"><td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.2.4.1.1 "><p id="p53989823"><a name="p53989823"></a><a name="p53989823"></a>OS-FLV-DISABLED:disabled</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="p26649649"><a name="p26649649"></a><a name="p26649649"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="66.94%" headers="mcps1.2.4.1.3 "><p id="p32761310192019"><a name="p32761310192019"></a><a name="p32761310192019"></a>Specifies whether the ECS flavor has been disabled. This is an extended attribute.</p>
<p id="p182115151112"><a name="p182115151112"></a><a name="p182115151112"></a>This parameter has not been used. Its default value is <strong id="b84235270611135_3"><a name="b84235270611135_3"></a><a name="b84235270611135_3"></a>false</strong>.</p>
</td>
</tr>
<tr id="row29760277"><td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.2.4.1.1 "><p id="p61772230"><a name="p61772230"></a><a name="p61772230"></a>rxtx_factor</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="p17171756"><a name="p17171756"></a><a name="p17171756"></a>Float</p>
</td>
<td class="cellrowborder" valign="top" width="66.94%" headers="mcps1.2.4.1.3 "><p id="p16772171313154"><a name="p16772171313154"></a><a name="p16772171313154"></a>Specifies the ratio of the available network bandwidth to the network hardware bandwidth of the ECS.</p>
<p id="p3711880173425"><a name="p3711880173425"></a><a name="p3711880173425"></a>This parameter has not been used. Its default value is <strong id="b84235270611135_4"><a name="b84235270611135_4"></a><a name="b84235270611135_4"></a>1.0</strong>.</p>
</td>
</tr>
<tr id="row5115727"><td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.2.4.1.1 "><p id="p11720763"><a name="p11720763"></a><a name="p11720763"></a>os-flavor-access:is_public</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="p60282721"><a name="p60282721"></a><a name="p60282721"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="66.94%" headers="mcps1.2.4.1.3 "><p id="p8894218182818"><a name="p8894218182818"></a><a name="p8894218182818"></a>Specifies whether a flavor is available to all tenants. This is an extended attribute.</p>
<a name="ul1474014143815"></a><a name="ul1474014143815"></a><ul id="ul1474014143815"><li><strong id="b84235270620200"><a name="b84235270620200"></a><a name="b84235270620200"></a>true</strong>: indicates that a flavor is available to all tenants.</li><li><strong id="b84235270620200_1"><a name="b84235270620200_1"></a><a name="b84235270620200_1"></a>false</strong>: indicates that a flavor is available only to certain tenants.</li></ul>
<p id="p35038271466"><a name="p35038271466"></a><a name="p35038271466"></a>Default value: <strong id="b842352706115252"><a name="b842352706115252"></a><a name="b842352706115252"></a>true</strong></p>
</td>
</tr>
<tr id="row57014372193259"><td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.2.4.1.1 "><p id="p1587802219356"><a name="p1587802219356"></a><a name="p1587802219356"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="16.2%" headers="mcps1.2.4.1.2 "><p id="p1105141919356"><a name="p1105141919356"></a><a name="p1105141919356"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="66.94%" headers="mcps1.2.4.1.3 "><p id="p342100019356"><a name="p342100019356"></a><a name="p342100019356"></a>Specifies shortcut links for ECS flavors. For details, see <a href="#table35514108193545">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **links**  field description

<a name="table35514108193545"></a>
<table><thead align="left"><tr id="row23367815193545"><th class="cellrowborder" valign="top" width="17.05%" id="mcps1.2.4.1.1"><p id="p98047153213"><a name="p98047153213"></a><a name="p98047153213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.29%" id="mcps1.2.4.1.2"><p id="p188041415328"><a name="p188041415328"></a><a name="p188041415328"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.66%" id="mcps1.2.4.1.3"><p id="p17804181511210"><a name="p17804181511210"></a><a name="p17804181511210"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row37879124193545"><td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.2.4.1.1 "><p id="p48310227193545"><a name="p48310227193545"></a><a name="p48310227193545"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.2.4.1.2 "><p id="p20814310193545"><a name="p20814310193545"></a><a name="p20814310193545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.66%" headers="mcps1.2.4.1.3 "><p id="p8237558193545"><a name="p8237558193545"></a><a name="p8237558193545"></a>Specifies the shortcut link marker name.</p>
</td>
</tr>
<tr id="row7029160193545"><td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.2.4.1.1 "><p id="p32491069193545"><a name="p32491069193545"></a><a name="p32491069193545"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="16.29%" headers="mcps1.2.4.1.2 "><p id="p14530947193545"><a name="p14530947193545"></a><a name="p14530947193545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.66%" headers="mcps1.2.4.1.3 "><p id="p36156065193545"><a name="p36156065193545"></a><a name="p36156065193545"></a>Provides the corresponding shortcut link.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section17318173018714"></a>

```
GET https://{endpoint}/v2/743b4c0428d94531b9f2add666642e6b/flavors/c3.2xlarge.2
GET https://{endpoint}/v2.1/743b4c0428d94531b9f2add666642e6b/flavors/c3.2xlarge.2
```

## Example Response<a name="section17459730163216"></a>

```
{
    "flavor": {
        "name": "c3.2xlarge.2",
        "links": [
            {
                "href": "https://compute.region.xxx.com/v2.1/743b4c0428d94531b9f2add666642e6b/flavors/c3.2xlarge.2",
                "rel": "self"
            },
            {
                "href": "https://compute.region.xxx.com/743b4c0428d94531b9f2add666642e6b/flavors/c3.2xlarge.2",
                "rel": "bookmark"
            }
        ],
        "ram": 16384,
        "OS-FLV-DISABLED:disabled": false,
        "vcpus": 8,
        "swap": "",
        "os-flavor-access:is_public": true,
        "rxtx_factor": 1,
        "OS-FLV-EXT-DATA:ephemeral": 0,
        "disk": 0,
        "id": "c3.2xlarge.2"
    }
                }
```

## Returned Values<a name="section36667404"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

