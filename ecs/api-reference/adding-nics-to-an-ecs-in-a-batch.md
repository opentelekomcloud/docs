# Adding NICs to an ECS in a Batch<a name="EN-US_TOPIC_0020212663"></a>

## Function<a name="section36695198"></a>

This API is used to add one or multiple NICs to an ECS.

## URI<a name="section61821327"></a>

POST /v1/\{project\_id\}/cloudservers/\{server\_id\}/nics

[Table 1](#table54800025)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table54800025"></a>
<table><thead align="left"><tr id="row14870565"><th class="cellrowborder" valign="top" width="16.6%" id="mcps1.2.4.1.1"><p id="p63665103"><a name="p63665103"></a><a name="p63665103"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.16%" id="mcps1.2.4.1.2"><p id="p56599738"><a name="p56599738"></a><a name="p56599738"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.24%" id="mcps1.2.4.1.3"><p id="p21176078"><a name="p21176078"></a><a name="p21176078"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row37540721"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p20899598"><a name="p20899598"></a><a name="p20899598"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p15145867"><a name="p15145867"></a><a name="p15145867"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.24%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row35483542"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p55594619"><a name="p55594619"></a><a name="p55594619"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p6870268"><a name="p6870268"></a><a name="p6870268"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.24%" headers="mcps1.2.4.1.3 "><p id="p19620867"><a name="p19620867"></a><a name="p19620867"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section19521038"></a>

[Table 2](#table23831236)  describes the request parameters.

**Table  2**  Request parameters

<a name="table23831236"></a>
<table><thead align="left"><tr id="row62644428"><th class="cellrowborder" valign="top" width="16.54%" id="mcps1.2.5.1.1"><p id="p41033878"><a name="p41033878"></a><a name="p41033878"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.2"><p id="p35409804"><a name="p35409804"></a><a name="p35409804"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.71%" id="mcps1.2.5.1.3"><p id="p49621912"><a name="p49621912"></a><a name="p49621912"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.459999999999994%" id="mcps1.2.5.1.4"><p id="p59951903"><a name="p59951903"></a><a name="p59951903"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row24265995"><td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.5.1.1 "><p id="p19388612"><a name="p19388612"></a><a name="p19388612"></a>nics</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p26973745"><a name="p26973745"></a><a name="p26973745"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.71%" headers="mcps1.2.5.1.3 "><p id="p37389755"><a name="p37389755"></a><a name="p37389755"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="52.459999999999994%" headers="mcps1.2.5.1.4 "><p id="p10932885"><a name="p10932885"></a><a name="p10932885"></a>Specifies the NICs to be added. For details, see <a href="#table58396974">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **nics**  field description

<a name="table58396974"></a>
<table><thead align="left"><tr id="row66803900"><th class="cellrowborder" valign="top" width="16.61833816618338%" id="mcps1.2.5.1.1"><p id="p1423511508114"><a name="p1423511508114"></a><a name="p1423511508114"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.308269173082692%" id="mcps1.2.5.1.2"><p id="p142352508112"><a name="p142352508112"></a><a name="p142352508112"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.618638136186382%" id="mcps1.2.5.1.3"><p id="p12235450218"><a name="p12235450218"></a><a name="p12235450218"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.45475452454754%" id="mcps1.2.5.1.4"><p id="p10235165010113"><a name="p10235165010113"></a><a name="p10235165010113"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19299134"><td class="cellrowborder" valign="top" width="16.61833816618338%" headers="mcps1.2.5.1.1 "><p id="p19726002"><a name="p19726002"></a><a name="p19726002"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.308269173082692%" headers="mcps1.2.5.1.2 "><p id="p54302323"><a name="p54302323"></a><a name="p54302323"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.618638136186382%" headers="mcps1.2.5.1.3 "><p id="p36412008"><a name="p36412008"></a><a name="p36412008"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.45475452454754%" headers="mcps1.2.5.1.4 "><p id="p52170790174229"><a name="p52170790174229"></a><a name="p52170790174229"></a>Specifies the information about the NICs to be added to an ECS.</p>
<p id="p43287089174217"><a name="p43287089174217"></a><a name="p43287089174217"></a>The value must be the ID of a created network in UUID format.</p>
</td>
</tr>
<tr id="row58738960"><td class="cellrowborder" valign="top" width="16.61833816618338%" headers="mcps1.2.5.1.1 "><p id="p60235282"><a name="p60235282"></a><a name="p60235282"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="17.308269173082692%" headers="mcps1.2.5.1.2 "><p id="p47219689"><a name="p47219689"></a><a name="p47219689"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.618638136186382%" headers="mcps1.2.5.1.3 "><p id="p66698493"><a name="p66698493"></a><a name="p66698493"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="52.45475452454754%" headers="mcps1.2.5.1.4 "><p id="p36384226"><a name="p36384226"></a><a name="p36384226"></a>Specifies the security groups for NICs. For details, see <a href="#table16100147">Table 4</a>.</p>
</td>
</tr>
<tr id="row29643385104818"><td class="cellrowborder" valign="top" width="16.61833816618338%" headers="mcps1.2.5.1.1 "><p id="p65463874104818"><a name="p65463874104818"></a><a name="p65463874104818"></a>ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="17.308269173082692%" headers="mcps1.2.5.1.2 "><p id="p973617104818"><a name="p973617104818"></a><a name="p973617104818"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.618638136186382%" headers="mcps1.2.5.1.3 "><p id="p11754185104818"><a name="p11754185104818"></a><a name="p11754185104818"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.45475452454754%" headers="mcps1.2.5.1.4 "><p id="p12564913104818"><a name="p12564913104818"></a><a name="p12564913104818"></a>Specifies the IP address. If this parameter is unavailable, the IP address is automatically assigned.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **security\_groups**  field description

<a name="table16100147"></a>
<table><thead align="left"><tr id="row24331897"><th class="cellrowborder" valign="top" width="16.54%" id="mcps1.2.5.1.1"><p id="p93384531019"><a name="p93384531019"></a><a name="p93384531019"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.2"><p id="p16355135315116"><a name="p16355135315116"></a><a name="p16355135315116"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.719999999999999%" id="mcps1.2.5.1.3"><p id="p16355953418"><a name="p16355953418"></a><a name="p16355953418"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.449999999999996%" id="mcps1.2.5.1.4"><p id="p103559531511"><a name="p103559531511"></a><a name="p103559531511"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8500244"><td class="cellrowborder" valign="top" width="16.54%" headers="mcps1.2.5.1.1 "><p id="p17431163"><a name="p17431163"></a><a name="p17431163"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.2 "><p id="p2638090"><a name="p2638090"></a><a name="p2638090"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.719999999999999%" headers="mcps1.2.5.1.3 "><p id="p12358762"><a name="p12358762"></a><a name="p12358762"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.449999999999996%" headers="mcps1.2.5.1.4 "><p id="p16950236"><a name="p16950236"></a><a name="p16950236"></a>Specifies the ID of the security group.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section41471619"></a>

See  [Responses \(Task\)](responses-(task).md).

## Example Request<a name="section1912511011213"></a>

```
POST https://{endpoint}/v1/{project_id}/cloudservers/{server_id}/nics
```

```
{
    "nics": [
        {
            "subnet_id": "d32019d3-bc6e-4319-9c1d-6722fc136a23", 
            "security_groups": [
                {
                    "id": "f0ac4394-7e4a-4409-9701-ba8be283dbc3"
                }
            ]
        }
    ]
}
```

## Example Response<a name="section120154513611"></a>

None

## Returned Values<a name="en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section23611955"></a>

See  [Error Code Description](error-code-description.md).

