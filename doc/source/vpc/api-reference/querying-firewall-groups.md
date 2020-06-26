# Querying Firewall Groups<a name="vpc_firewall_0013"></a>

## Function<a name="section11380465132652"></a>

This API is used to query all firewall groups accessible to the tenant submitting the request. 

## URI<a name="section38164372132652"></a>

GET /v2.0/fwaas/firewall\_groups

Example of querying groups by page

```
GET https://{Endpoint}/v2.0/fwaas/firewall_groups?limit=2&marker=cd600d47-0045-483f-87a1-5041ae2f513b&page_reverse=False
```

[Table 1](#table2285151162120)  describes the parameters.

**Table  1**  Parameter description

<a name="table2285151162120"></a>
<table><thead align="left"><tr id="row439021115215"><th class="cellrowborder" valign="top" width="19.971997199719972%" id="mcps1.2.5.1.1"><p id="p19390141117210"><a name="p19390141117210"></a><a name="p19390141117210"></a><strong id="b695592912918"><a name="b695592912918"></a><a name="b695592912918"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.39163916391639%" id="mcps1.2.5.1.2"><p id="p163901911102116"><a name="p163901911102116"></a><a name="p163901911102116"></a><strong id="b07529302292"><a name="b07529302292"></a><a name="b07529302292"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.851985198519852%" id="mcps1.2.5.1.3"><p id="p15390171102117"><a name="p15390171102117"></a><a name="p15390171102117"></a><strong id="b18641133162912"><a name="b18641133162912"></a><a name="b18641133162912"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43.784378437843785%" id="mcps1.2.5.1.4"><p id="p339051116218"><a name="p339051116218"></a><a name="p339051116218"></a><strong id="b8501532202919"><a name="b8501532202919"></a><a name="b8501532202919"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1739012116211"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p1139011142114"><a name="p1139011142114"></a><a name="p1139011142114"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.5.1.2 "><p id="p0390511162114"><a name="p0390511162114"></a><a name="p0390511162114"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.851985198519852%" headers="mcps1.2.5.1.3 "><p id="p83901011172115"><a name="p83901011172115"></a><a name="p83901011172115"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.784378437843785%" headers="mcps1.2.5.1.4 "><p id="p23908114217"><a name="p23908114217"></a><a name="p23908114217"></a>Specifies that the ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row83901711182112"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p2390911172112"><a name="p2390911172112"></a><a name="p2390911172112"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.5.1.2 "><p id="p539041162115"><a name="p539041162115"></a><a name="p539041162115"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.851985198519852%" headers="mcps1.2.5.1.3 "><p id="p3390141110213"><a name="p3390141110213"></a><a name="p3390141110213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.784378437843785%" headers="mcps1.2.5.1.4 "><p id="p133901211162112"><a name="p133901211162112"></a><a name="p133901211162112"></a>Specifies that the name is used as the filtering condition.</p>
</td>
</tr>
<tr id="row03901117211"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p139013118211"><a name="p139013118211"></a><a name="p139013118211"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.5.1.2 "><p id="p163901211192116"><a name="p163901211192116"></a><a name="p163901211192116"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.851985198519852%" headers="mcps1.2.5.1.3 "><p id="p4391101182113"><a name="p4391101182113"></a><a name="p4391101182113"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.784378437843785%" headers="mcps1.2.5.1.4 "><p id="p14391161112114"><a name="p14391161112114"></a><a name="p14391161112114"></a>Specifies that the description is used as the filtering condition.</p>
</td>
</tr>
<tr id="row2391191118211"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p43911911112110"><a name="p43911911112110"></a><a name="p43911911112110"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.5.1.2 "><p id="p163911311132119"><a name="p163911311132119"></a><a name="p163911311132119"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.851985198519852%" headers="mcps1.2.5.1.3 "><p id="p11391181115216"><a name="p11391181115216"></a><a name="p11391181115216"></a>Booleab</p>
</td>
<td class="cellrowborder" valign="top" width="43.784378437843785%" headers="mcps1.2.5.1.4 "><p id="p2715182372114"><a name="p2715182372114"></a><a name="p2715182372114"></a>Specifies that the admin state is used as the filtering condition.</p>
<p id="p1339181115217"><a name="p1339181115217"></a><a name="p1339181115217"></a>The value can be <strong id="b18839125492916"><a name="b18839125492916"></a><a name="b18839125492916"></a>true</strong> or <strong id="b68391654152910"><a name="b68391654152910"></a><a name="b68391654152910"></a>false</strong>.</p>
</td>
</tr>
<tr id="row83911211112115"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p16391181172119"><a name="p16391181172119"></a><a name="p16391181172119"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.5.1.2 "><p id="p439151115210"><a name="p439151115210"></a><a name="p439151115210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.851985198519852%" headers="mcps1.2.5.1.3 "><p id="p7391171114213"><a name="p7391171114213"></a><a name="p7391171114213"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.784378437843785%" headers="mcps1.2.5.1.4 "><p id="p143911111142114"><a name="p143911111142114"></a><a name="p143911111142114"></a>Specifies that the project ID is used as the filtering condition.</p>
</td>
</tr>
<tr id="row1239110118217"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p20391111142113"><a name="p20391111142113"></a><a name="p20391111142113"></a>marker</p>
</td>
<td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.5.1.2 "><p id="p2391161142119"><a name="p2391161142119"></a><a name="p2391161142119"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.851985198519852%" headers="mcps1.2.5.1.3 "><p id="p83911911142119"><a name="p83911911142119"></a><a name="p83911911142119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.784378437843785%" headers="mcps1.2.5.1.4 "><p id="p639191113214"><a name="p639191113214"></a><a name="p639191113214"></a>Specifies the start resource ID of pagination query. If the parameter is left blank, only resources on the first page are queried.</p>
</td>
</tr>
<tr id="row039113115215"><td class="cellrowborder" valign="top" width="19.971997199719972%" headers="mcps1.2.5.1.1 "><p id="p43911611132116"><a name="p43911611132116"></a><a name="p43911611132116"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="16.39163916391639%" headers="mcps1.2.5.1.2 "><p id="p163911811172115"><a name="p163911811172115"></a><a name="p163911811172115"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.851985198519852%" headers="mcps1.2.5.1.3 "><p id="p1039131162116"><a name="p1039131162116"></a><a name="p1039131162116"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="43.784378437843785%" headers="mcps1.2.5.1.4 "><p id="p6190327172119"><a name="p6190327172119"></a><a name="p6190327172119"></a>Specifies the number of records on each page.</p>
<p id="p193911011122112"><a name="p193911011122112"></a><a name="p193911011122112"></a>The value ranges from 0 to intmax.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section30244758132652"></a>

None

## Response Message<a name="section48852885132652"></a>

**Table  2**  Response parameter

<a name="table25605667132652"></a>
<table><thead align="left"><tr id="row26621002132652"><th class="cellrowborder" valign="top" width="23.330000000000002%" id="mcps1.2.4.1.1"><p id="p17188156132652"><a name="p17188156132652"></a><a name="p17188156132652"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.78%" id="mcps1.2.4.1.2"><p id="p29579284132652"><a name="p29579284132652"></a><a name="p29579284132652"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.89%" id="mcps1.2.4.1.3"><p id="p37495801132652"><a name="p37495801132652"></a><a name="p37495801132652"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row29258567132652"><td class="cellrowborder" valign="top" width="23.330000000000002%" headers="mcps1.2.4.1.1 "><p id="p7598331132652"><a name="p7598331132652"></a><a name="p7598331132652"></a>firewall_groups</p>
</td>
<td class="cellrowborder" valign="top" width="17.78%" headers="mcps1.2.4.1.2 "><p id="p50785846132652"><a name="p50785846132652"></a><a name="p50785846132652"></a>Array of <a href="#table31629250121127">Firewall Group</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="58.89%" headers="mcps1.2.4.1.3 "><p id="p48871362132652"><a name="p48871362132652"></a><a name="p48871362132652"></a>Specifies the firewall group list. For details, see <a href="#table31629250121127">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **Firewall Group**  objects

<a name="table31629250121127"></a>
<table><thead align="left"><tr id="row45711693121127"><th class="cellrowborder" valign="top" width="35.3%" id="mcps1.2.4.1.1"><p id="p46819705121127"><a name="p46819705121127"></a><a name="p46819705121127"></a><strong id="b17109172373511"><a name="b17109172373511"></a><a name="b17109172373511"></a>Attribute</strong></p>
</th>
<th class="cellrowborder" valign="top" width="21.57%" id="mcps1.2.4.1.2"><p id="p35064605121127"><a name="p35064605121127"></a><a name="p35064605121127"></a><strong id="b550819342379"><a name="b550819342379"></a><a name="b550819342379"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="43.13%" id="mcps1.2.4.1.3"><p id="p11952850121127"><a name="p11952850121127"></a><a name="p11952850121127"></a><strong id="b335614354371"><a name="b335614354371"></a><a name="b335614354371"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row20395689121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p50168503121127"><a name="p50168503121127"></a><a name="p50168503121127"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p47513116121127"><a name="p47513116121127"></a><a name="p47513116121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p62072725121127"><a name="p62072725121127"></a><a name="p62072725121127"></a>Specifies the UUID of the firewall group. </p>
</td>
</tr>
<tr id="row34896104121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p52608071121127"><a name="p52608071121127"></a><a name="p52608071121127"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p59846605121127"><a name="p59846605121127"></a><a name="p59846605121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p28604909121127"><a name="p28604909121127"></a><a name="p28604909121127"></a>Specifies the name of the firewall group.</p>
</td>
</tr>
<tr id="row11129246121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p39887063121127"><a name="p39887063121127"></a><a name="p39887063121127"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p28745735121127"><a name="p28745735121127"></a><a name="p28745735121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p35639020121127"><a name="p35639020121127"></a><a name="p35639020121127"></a>Provides supplementary information about the firewall group.</p>
</td>
</tr>
<tr id="row677472121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p60717947121127"><a name="p60717947121127"></a><a name="p60717947121127"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p65871708121127"><a name="p65871708121127"></a><a name="p65871708121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row38137474121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p35500294121127"><a name="p35500294121127"></a><a name="p35500294121127"></a>ingress_firewall_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p49995809121127"><a name="p49995809121127"></a><a name="p49995809121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p56499442121127"><a name="p56499442121127"></a><a name="p56499442121127"></a>Specifies the firewall policy for inbound traffic.</p>
</td>
</tr>
<tr id="row9094936121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p34911245121127"><a name="p34911245121127"></a><a name="p34911245121127"></a>egress_firewall_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p44624490121127"><a name="p44624490121127"></a><a name="p44624490121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p37100641121127"><a name="p37100641121127"></a><a name="p37100641121127"></a>Specifies the firewall policy for outbound traffic.</p>
</td>
</tr>
<tr id="row31622902121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p65911012121127"><a name="p65911012121127"></a><a name="p65911012121127"></a>ports</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p5459978121127"><a name="p5459978121127"></a><a name="p5459978121127"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p61002567121127"><a name="p61002567121127"></a><a name="p61002567121127"></a>Specifies the list of ports bound with the firewall group.</p>
</td>
</tr>
<tr id="row48186031121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p33368479121127"><a name="p33368479121127"></a><a name="p33368479121127"></a>public</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p7938198121127"><a name="p7938198121127"></a><a name="p7938198121127"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p56166201121127"><a name="p56166201121127"></a><a name="p56166201121127"></a>Specifies whether the firewall policy can be shared by different tenants.</p>
</td>
</tr>
<tr id="row60912436121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p66273781121127"><a name="p66273781121127"></a><a name="p66273781121127"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p7141533121127"><a name="p7141533121127"></a><a name="p7141533121127"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p6468335121127"><a name="p6468335121127"></a><a name="p6468335121127"></a>Specifies the status of the firewall policy.</p>
</td>
</tr>
<tr id="row59833296121127"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p44051842121127"><a name="p44051842121127"></a><a name="p44051842121127"></a>admin_state_up</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p58587899121127"><a name="p58587899121127"></a><a name="p58587899121127"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p3428646121127"><a name="p3428646121127"></a><a name="p3428646121127"></a>Specifies whether the firewall is controlled by the administrator.</p>
</td>
</tr>
<tr id="row7228115213486"><td class="cellrowborder" valign="top" width="35.3%" headers="mcps1.2.4.1.1 "><p id="p53071912134918"><a name="p53071912134918"></a><a name="p53071912134918"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.57%" headers="mcps1.2.4.1.2 "><p id="p1731011220498"><a name="p1731011220498"></a><a name="p1731011220498"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.13%" headers="mcps1.2.4.1.3 "><p id="p2078552513296"><a name="p2078552513296"></a><a name="p2078552513296"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section19537091132652"></a>

Example request

```
GET https://{Endpoint}/v2.0/fwaas/firewall_groups
```

Example response

```
{
    "firewall_groups": [
        {
            "status": "INACTIVE", 
            "public": false, 
            "egress_firewall_policy_id": null, 
            "name": "", 
            "admin_state_up": true, 
            "ports": [ ], 
            "tenant_id": "23c8a121505047b6869edf39f3062712", 
            "id": "cd600d47-0045-483f-87a1-5041ae2f513b", 
            "ingress_firewall_policy_id": null, 
            "description": "",
            "project_id": "23c8a121505047b6869edf39f3062712"
        }, 
        {
            "status": "INACTIVE", 
            "public": false, 
            "egress_firewall_policy_id": "d939df29-fe76-4089-90c3-3778e4d53141", 
            "name": "fwg-1475475043", 
            "admin_state_up": true, 
            "ports": [ ], 
            "tenant_id": "0af57070695044ea9a70f04779e6aa1f", 
            "id": "ca971b45-70ce-4879-9734-b6cac1d00845", 
            "ingress_firewall_policy_id": "d939df29-fe76-4089-90c3-3778e4d53141", 
            "description": "",
            "project_id": "0af57070695044ea9a70f04779e6aa1f"
        }
    ]
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

