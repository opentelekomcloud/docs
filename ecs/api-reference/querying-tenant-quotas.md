# Querying Tenant Quotas<a name="EN-US_TOPIC_0020212674"></a>

## Function<a name="section7764884"></a>

This API is used to query the quotas of all resources for a specified tenant, including used quotas.

## URI<a name="section2775100"></a>

GET /v1/\{project\_id\}/cloudservers/limits

[Table 1](#table23262209)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table23262209"></a>
<table><thead align="left"><tr id="row32406826"><th class="cellrowborder" valign="top" width="16.61%" id="mcps1.2.4.1.1"><p id="p7707213"><a name="p7707213"></a><a name="p7707213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.54%" id="mcps1.2.4.1.2"><p id="p20304554"><a name="p20304554"></a><a name="p20304554"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.85%" id="mcps1.2.4.1.3"><p id="p34056167"><a name="p34056167"></a><a name="p34056167"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row7086124"><td class="cellrowborder" valign="top" width="16.61%" headers="mcps1.2.4.1.1 "><p id="p37105186"><a name="p37105186"></a><a name="p37105186"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.54%" headers="mcps1.2.4.1.2 "><p id="p52730096"><a name="p52730096"></a><a name="p52730096"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.85%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section24975902"></a>

None

## Response<a name="section23456533"></a>

[Table 2](#table6147620)  describes the response parameters.

**Table  2**  Response parameters

<a name="table6147620"></a>
<table><thead align="left"><tr id="row63161481"><th class="cellrowborder" valign="top" width="16.85%" id="mcps1.2.4.1.1"><p id="p15806308"><a name="p15806308"></a><a name="p15806308"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.23%" id="mcps1.2.4.1.2"><p id="p21995508"><a name="p21995508"></a><a name="p21995508"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.92%" id="mcps1.2.4.1.3"><p id="p36805753"><a name="p36805753"></a><a name="p36805753"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row28476039"><td class="cellrowborder" valign="top" width="16.85%" headers="mcps1.2.4.1.1 "><p id="p24857797"><a name="p24857797"></a><a name="p24857797"></a>absolute</p>
</td>
<td class="cellrowborder" valign="top" width="17.23%" headers="mcps1.2.4.1.2 "><p id="p17467122"><a name="p17467122"></a><a name="p17467122"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="65.92%" headers="mcps1.2.4.1.3 "><p id="p49956928"><a name="p49956928"></a><a name="p49956928"></a>Specifies tenant quotas. For details, see <a href="#table7714075">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **absolute**  field description

<a name="table7714075"></a>
<table><thead align="left"><tr id="row63715136"><th class="cellrowborder" valign="top" width="19.470000000000002%" id="mcps1.2.4.1.1"><p id="p1243814208352"><a name="p1243814208352"></a><a name="p1243814208352"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.56%" id="mcps1.2.4.1.2"><p id="p943862010355"><a name="p943862010355"></a><a name="p943862010355"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.97%" id="mcps1.2.4.1.3"><p id="p1443832011351"><a name="p1443832011351"></a><a name="p1443832011351"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row42383756"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p10532193"><a name="p10532193"></a><a name="p10532193"></a>maxTotalInstances</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p46701637"><a name="p46701637"></a><a name="p46701637"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p21300044"><a name="p21300044"></a><a name="p21300044"></a>Specifies the maximum number of ECSs you can use.</p>
</td>
</tr>
<tr id="row57482668"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p25584516"><a name="p25584516"></a><a name="p25584516"></a>maxTotalCores</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p20741957"><a name="p20741957"></a><a name="p20741957"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p21392630"><a name="p21392630"></a><a name="p21392630"></a>Specifies the maximum number of CPU cores you can use.</p>
</td>
</tr>
<tr id="row58315944"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p25971051"><a name="p25971051"></a><a name="p25971051"></a>maxTotalRAMSize</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p6661465"><a name="p6661465"></a><a name="p6661465"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p24370177"><a name="p24370177"></a><a name="p24370177"></a>Specifies the maximum memory space (MB) you can use.</p>
</td>
</tr>
<tr id="row18005001"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p49119006"><a name="p49119006"></a><a name="p49119006"></a>maxTotalKeypairs</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p13038474"><a name="p13038474"></a><a name="p13038474"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p42697780"><a name="p42697780"></a><a name="p42697780"></a>Specifies the maximum number of SSH key pairs you can use.</p>
</td>
</tr>
<tr id="row48735703"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p55277862"><a name="p55277862"></a><a name="p55277862"></a>maxServerMeta</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p21756767"><a name="p21756767"></a><a name="p21756767"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p22991320"><a name="p22991320"></a><a name="p22991320"></a>Specifies the maximum length of the metadata you can use.</p>
</td>
</tr>
<tr id="row5595289"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p50565259"><a name="p50565259"></a><a name="p50565259"></a>maxPersonality</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p39551712"><a name="p39551712"></a><a name="p39551712"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p43495860"><a name="p43495860"></a><a name="p43495860"></a>Specifies the maximum number of files that can be injected.</p>
</td>
</tr>
<tr id="row55918423"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p33098452"><a name="p33098452"></a><a name="p33098452"></a>maxPersonalitySize</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p61770902"><a name="p61770902"></a><a name="p61770902"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p940305"><a name="p940305"></a><a name="p940305"></a>Specifies the maximum size (byte) of the file to be injected.</p>
</td>
</tr>
<tr id="row56010681154433"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p34334083154433"><a name="p34334083154433"></a><a name="p34334083154433"></a>maxServerGroups</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p29597354154433"><a name="p29597354154433"></a><a name="p29597354154433"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p48575502154433"><a name="p48575502154433"></a><a name="p48575502154433"></a>Specifies the maximum number of server groups.</p>
</td>
</tr>
<tr id="row6104724715477"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p4587998315477"><a name="p4587998315477"></a><a name="p4587998315477"></a>maxServerGroupMembers</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p2529112315477"><a name="p2529112315477"></a><a name="p2529112315477"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p3531507615477"><a name="p3531507615477"></a><a name="p3531507615477"></a>Specifies the maximum number of ECSs in an ECS group.</p>
</td>
</tr>
<tr id="row3499539015481"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p1605434815481"><a name="p1605434815481"></a><a name="p1605434815481"></a>totalServerGroupsUsed</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p2533385115481"><a name="p2533385115481"></a><a name="p2533385115481"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p3877608315481"><a name="p3877608315481"></a><a name="p3877608315481"></a>Specifies the number of used server groups.</p>
</td>
</tr>
<tr id="row8462746"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p14393865"><a name="p14393865"></a><a name="p14393865"></a>maxSecurityGroups</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p15982473"><a name="p15982473"></a><a name="p15982473"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p41389494"><a name="p41389494"></a><a name="p41389494"></a>Specifies the maximum number of security groups you can use.</p>
<div class="note" id="note8411879113615"><a name="note8411879113615"></a><a name="note8411879113615"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p8598055113615"><a name="p8598055113615"></a><a name="p8598055113615"></a>The quota complies with the VPC quota limit.</p>
</div></div>
</td>
</tr>
<tr id="row36961130"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p41061555"><a name="p41061555"></a><a name="p41061555"></a>maxSecurityGroupRules</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p29888320"><a name="p29888320"></a><a name="p29888320"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p45313516"><a name="p45313516"></a><a name="p45313516"></a>Specifies the maximum number of security group rules that you can configure in a security group.</p>
<div class="note" id="note32309229113621"><a name="note32309229113621"></a><a name="note32309229113621"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p22347611113621"><a name="p22347611113621"></a><a name="p22347611113621"></a>The quota complies with the VPC quota limit.</p>
</div></div>
</td>
</tr>
<tr id="row5168462"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p15992282"><a name="p15992282"></a><a name="p15992282"></a>maxTotalFloatingIps</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p34210755"><a name="p34210755"></a><a name="p34210755"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p42252410"><a name="p42252410"></a><a name="p42252410"></a>Specifies the maximum number of floating IP addresses you can use.</p>
</td>
</tr>
<tr id="row44727375"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p66147589"><a name="p66147589"></a><a name="p66147589"></a>maxImageMeta</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p1311131"><a name="p1311131"></a><a name="p1311131"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p16290985"><a name="p16290985"></a><a name="p16290985"></a>Specifies the maximum length of the image metadata.</p>
</td>
</tr>
<tr id="row12401140"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p64968253"><a name="p64968253"></a><a name="p64968253"></a>totalInstancesUsed</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p48312784"><a name="p48312784"></a><a name="p48312784"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p54975040"><a name="p54975040"></a><a name="p54975040"></a>Specifies the number of used ECSs.</p>
</td>
</tr>
<tr id="row25013317"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p12812809"><a name="p12812809"></a><a name="p12812809"></a>totalCoresUsed</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p44542441"><a name="p44542441"></a><a name="p44542441"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p57858440"><a name="p57858440"></a><a name="p57858440"></a>Specifies the number of the used CPU cores.</p>
</td>
</tr>
<tr id="row50963915"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p34436465"><a name="p34436465"></a><a name="p34436465"></a>totalRAMUsed</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p49214446"><a name="p49214446"></a><a name="p49214446"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p41198408"><a name="p41198408"></a><a name="p41198408"></a>Specifies the used memory size (MB).</p>
</td>
</tr>
<tr id="row35241358"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p35977726"><a name="p35977726"></a><a name="p35977726"></a>totalSecurityGroupsUsed</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p27989608"><a name="p27989608"></a><a name="p27989608"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p3330249"><a name="p3330249"></a><a name="p3330249"></a>Specifies the number of used security groups.</p>
</td>
</tr>
<tr id="row29972245"><td class="cellrowborder" valign="top" width="19.470000000000002%" headers="mcps1.2.4.1.1 "><p id="p11832760"><a name="p11832760"></a><a name="p11832760"></a>totalFloatingIpsUsed</p>
</td>
<td class="cellrowborder" valign="top" width="14.56%" headers="mcps1.2.4.1.2 "><p id="p56892511"><a name="p56892511"></a><a name="p56892511"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="65.97%" headers="mcps1.2.4.1.3 "><p id="p1362898"><a name="p1362898"></a><a name="p1362898"></a>Specifies the number of used floating IP addresses.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section59014260171"></a>

```
GET https://{endpoint}/v1/{project_id}/cloudservers/limits
```

## Example Response<a name="section15363155313399"></a>

Example response

```
{
    "absolute": {
        "maxServerMeta": 128, 
        "maxPersonality": 5, 
        "maxImageMeta": 128, 
        "maxPersonalitySize": 10240, 
        "maxSecurityGroupRules": 20, 
        "maxTotalKeypairs": -1, 
        "totalRAMUsed": 75776, 
        "totalInstancesUsed": 21, 
        "maxSecurityGroups": 10, 
        "totalFloatingIpsUsed": 0, 
        "maxTotalCores": 20480, 
        "totalSecurityGroupsUsed": 1, 
        "maxTotalFloatingIps": 10, 
        "maxTotalInstances": 2048, 
        "totalCoresUsed": 40, 
        "maxTotalRAMSize": 25165824,
        "maxServerGroups": 10,
        "maxServerGroupMembers": 16,
        "totalServerGroupsUsed": 2
    }
}
```

## Returned Values<a name="section9782209"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).

