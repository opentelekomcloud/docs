# Removing a Firewall Rule<a name="vpc_firewall_0012"></a>

## Function<a name="section9946367132633"></a>

This API is used to remove a firewall rule from a firewall policy.

## URI<a name="section17986671132633"></a>

PUT /v2.0/fwaas/firewall\_policies/\{firewall\_policy\_id\}/remove\_rule

## Request Message<a name="section27028167132633"></a>

**Table  1**  Request parameter

<a name="table48893916132633"></a>
<table><thead align="left"><tr id="row19661564132633"><th class="cellrowborder" valign="top" width="23.47%" id="mcps1.2.5.1.1"><p id="p4257277132633"><a name="p4257277132633"></a><a name="p4257277132633"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.149999999999999%" id="mcps1.2.5.1.2"><p id="p2994165132633"><a name="p2994165132633"></a><a name="p2994165132633"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="19.52%" id="mcps1.2.5.1.3"><p id="p47550467132633"><a name="p47550467132633"></a><a name="p47550467132633"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42.86%" id="mcps1.2.5.1.4"><p id="p38031689132633"><a name="p38031689132633"></a><a name="p38031689132633"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row26905318132633"><td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.5.1.1 "><p id="p23736314132633"><a name="p23736314132633"></a><a name="p23736314132633"></a>firewall_rule_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.149999999999999%" headers="mcps1.2.5.1.2 "><p id="p25366437132633"><a name="p25366437132633"></a><a name="p25366437132633"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="19.52%" headers="mcps1.2.5.1.3 "><p id="p36656390132633"><a name="p36656390132633"></a><a name="p36656390132633"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.86%" headers="mcps1.2.5.1.4 "><p id="p48236351132633"><a name="p48236351132633"></a><a name="p48236351132633"></a>Specifies the firewall rule ID, which uniquely identifies the firewall rule.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="section14889742132633"></a>

**Table  2**  Response parameter

<a name="table7711269132633"></a>
<table><thead align="left"><tr id="row40961108132633"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.2.4.1.1"><p id="p53016887132633"><a name="p53016887132633"></a><a name="p53016887132633"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.61%" id="mcps1.2.4.1.2"><p id="p45522129132633"><a name="p45522129132633"></a><a name="p45522129132633"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.22%" id="mcps1.2.4.1.3"><p id="p31582377132633"><a name="p31582377132633"></a><a name="p31582377132633"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18215720132633"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p64319710132633"><a name="p64319710132633"></a><a name="p64319710132633"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="p20101354132633"><a name="p20101354132633"></a><a name="p20101354132633"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p41635977132633"><a name="p41635977132633"></a><a name="p41635977132633"></a>Provides supplementary information about the firewall policy.</p>
</td>
</tr>
<tr id="row7244977132633"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p35103306132633"><a name="p35103306132633"></a><a name="p35103306132633"></a>audited</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="p14021835132633"><a name="p14021835132633"></a><a name="p14021835132633"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p34631936132633"><a name="p34631936132633"></a><a name="p34631936132633"></a>Each time the firewall policy or the associated firewall rules are changed, this attribute will be set to <strong id="b8423527061137"><a name="b8423527061137"></a><a name="b8423527061137"></a>False</strong>.</p>
</td>
</tr>
<tr id="row21094728132633"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p50715789132633"><a name="p50715789132633"></a><a name="p50715789132633"></a>firewall_rules</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="p56483400132633"><a name="p56483400132633"></a><a name="p56483400132633"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p3804581132633"><a name="p3804581132633"></a><a name="p3804581132633"></a>Specifies the ID list of the firewall rules associated with the current firewall policy.</p>
</td>
</tr>
<tr id="row27264529132633"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p47093833132633"><a name="p47093833132633"></a><a name="p47093833132633"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="p45736328132633"><a name="p45736328132633"></a><a name="p45736328132633"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p46737820132633"><a name="p46737820132633"></a><a name="p46737820132633"></a>Specifies the firewall policy ID.</p>
</td>
</tr>
<tr id="row46882287132633"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p28861411132633"><a name="p28861411132633"></a><a name="p28861411132633"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="p36587630132633"><a name="p36587630132633"></a><a name="p36587630132633"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p14824904132633"><a name="p14824904132633"></a><a name="p14824904132633"></a>Specifies the firewall policy name.</p>
</td>
</tr>
<tr id="row64601479132633"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p61245310132633"><a name="p61245310132633"></a><a name="p61245310132633"></a>public</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="p21782173132633"><a name="p21782173132633"></a><a name="p21782173132633"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p9188558132633"><a name="p9188558132633"></a><a name="p9188558132633"></a>If this attribute is set to <strong id="b52671116122119"><a name="b52671116122119"></a><a name="b52671116122119"></a>True</strong>, the firewall policy is visible to tenants other than its owner. The firewall policy is not visible to other tenants by default.</p>
</td>
</tr>
<tr id="row31674173132633"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p49506560132633"><a name="p49506560132633"></a><a name="p49506560132633"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.2.4.1.2 "><p id="p50877818132633"><a name="p50877818132633"></a><a name="p50877818132633"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section48445237132633"></a>

Example request

```
PUT https://{Endpoint}/v2.0/fwaas/firewall_policies/afc52ce9-5305-4ec9-9feb-44feb8330341/remove_rule 

{
    "firewall_rule_id": "0f82b221-8cd6-44bd-9dfc-0e118fa7b6b1"
}
```

Example response

```
{
    "description": "", 
    "firewall_rules": [
        "b8243448-cb3c-496e-851c-dadade4c161b"
    ], 
    "tenant_id": "23c8a121505047b6869edf39f3062712", 
    "public": false, 
    "id": "afc52ce9-5305-4ec9-9feb-44feb8330341", 
    "audited": false, 
    "name": "test-policy",
    "project_id": "23c8a121505047b6869edf39f3062712"
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).

