# Modifying an Instance<a name="EN-US_TOPIC_0128036897"></a>

## Function<a name="section16640184612281"></a>

This API is used to modify the instance information, including the instance name, description, maintenance window, and security group.

## URI<a name="section1333816281512"></a>

PUT /v1.0/\{project\_id\}/instances/\{instance\_id\}

**Table  1**  Parameter description

<a name="table434018282110"></a>
<table><thead align="left"><tr id="row46806283114"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p1368010288120"><a name="p1368010288120"></a><a name="p1368010288120"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p86803283111"><a name="p86803283111"></a><a name="p86803283111"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p1568018281318"><a name="p1568018281318"></a><a name="p1568018281318"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p166801828014"><a name="p166801828014"></a><a name="p166801828014"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row186802285111"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1268012813116"><a name="p1268012813116"></a><a name="p1268012813116"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p86812281319"><a name="p86812281319"></a><a name="p86812281319"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1768110283116"><a name="p1768110283116"></a><a name="p1768110283116"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p20681182818117"><a name="p20681182818117"></a><a name="p20681182818117"></a>Indicates the ID of a project.</p>
</td>
</tr>
<tr id="row968112281014"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p868112281017"><a name="p868112281017"></a><a name="p868112281017"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p9681328010"><a name="p9681328010"></a><a name="p9681328010"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p4681192819115"><a name="p4681192819115"></a><a name="p4681192819115"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p96811287114"><a name="p96811287114"></a><a name="p96811287114"></a>Indicates the instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section1535592810114"></a>

**Request parameters**

[Table 2](#table1535615281916)  describes the parameters.

**Table  2**  Parameter description

<a name="table1535615281916"></a>
<table><thead align="left"><tr id="row368114281213"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.5.1.1"><p id="p968142814110"><a name="p968142814110"></a><a name="p968142814110"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.2"><p id="p268117281614"><a name="p268117281614"></a><a name="p268117281614"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="9%" id="mcps1.2.5.1.3"><p id="p56811628914"><a name="p56811628914"></a><a name="p56811628914"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.2.5.1.4"><p id="p66814283115"><a name="p66814283115"></a><a name="p66814283115"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row76815281815"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p186821628616"><a name="p186821628616"></a><a name="p186821628616"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p96821328215"><a name="p96821328215"></a><a name="p96821328215"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.5.1.3 "><p id="p1668214286117"><a name="p1668214286117"></a><a name="p1668214286117"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p968210281411"><a name="p968210281411"></a><a name="p968210281411"></a>Indicates the instance name.</p>
<p id="p1968211281517"><a name="p1968211281517"></a><a name="p1968211281517"></a>An instance name is a string of 4 to 64 characters that contain letters, digits, underscores (_), and hyphens (-).</p>
</td>
</tr>
<tr id="row19682728211"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p168262813117"><a name="p168262813117"></a><a name="p168262813117"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p106825281913"><a name="p106825281913"></a><a name="p106825281913"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.5.1.3 "><p id="p36828281414"><a name="p36828281414"></a><a name="p36828281414"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p76821928819"><a name="p76821928819"></a><a name="p76821928819"></a>Indicates the description of an instance.</p>
<p id="p1368213286119"><a name="p1368213286119"></a><a name="p1368213286119"></a>The description must be a character string containing not more than 1,024 characters.</p>
<div class="note" id="note23701428716"><a name="note23701428716"></a><a name="note23701428716"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p26821628212"><a name="p26821628212"></a><a name="p26821628212"></a>The backslash (\) and quotation mark (") are special characters for JSON packets. When using these characters in a parameter value, add the escape character (\) before these characters, for example, <strong id="b143981532181916"><a name="b143981532181916"></a><a name="b143981532181916"></a>\\</strong> and <strong id="b6398153221915"><a name="b6398153221915"></a><a name="b6398153221915"></a>\"</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row2682152819119"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p86829282112"><a name="p86829282112"></a><a name="p86829282112"></a>maintain_begin</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p468211281014"><a name="p468211281014"></a><a name="p468211281014"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.5.1.3 "><p id="p18682142817111"><a name="p18682142817111"></a><a name="p18682142817111"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p332017212255"><a name="p332017212255"></a><a name="p332017212255"></a>Indicates the time at which a maintenance time window starts. Format: <em id="i208181850963"><a name="i208181850963"></a><a name="i208181850963"></a>HH:mm</em>.</p>
<a name="ul1232022112510"></a><a name="ul1232022112510"></a><ul id="ul1232022112510"><li>The start time and end time of the maintenance time window must indicate the specified time segment. For details about how to query the time segments of supported maintenance time windows, see <a href="querying-maintenance-time-windows.md">Querying Maintenance Time Windows</a>.</li><li>The start time must be set to 22:00, 02:00, 06:00, 10:00, 14:00, or 18:00.</li><li>Parameters <strong id="b5257195412191"><a name="b5257195412191"></a><a name="b5257195412191"></a>maintain_begin</strong> and <strong id="b32571254121912"><a name="b32571254121912"></a><a name="b32571254121912"></a>maintain_end</strong> must be set in pairs. If parameter <strong id="b1257185411195"><a name="b1257185411195"></a><a name="b1257185411195"></a>maintain_begin</strong> is left blank, parameter <strong id="b1625765451915"><a name="b1625765451915"></a><a name="b1625765451915"></a>maintain_end</strong> is also left blank. In this case, the system automatically set the start time to 02:00.</li></ul>
</td>
</tr>
<tr id="row196828281817"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p46833281516"><a name="p46833281516"></a><a name="p46833281516"></a>maintain_end</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p2068392819113"><a name="p2068392819113"></a><a name="p2068392819113"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.5.1.3 "><p id="p1368317281511"><a name="p1368317281511"></a><a name="p1368317281511"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p2320424257"><a name="p2320424257"></a><a name="p2320424257"></a>Indicates the time at which a maintenance time window ends. Format: <em id="i891014221882"><a name="i891014221882"></a><a name="i891014221882"></a>HH:mm</em>.</p>
<a name="ul1432013292512"></a><a name="ul1432013292512"></a><ul id="ul1432013292512"><li>The start time and end time of the maintenance time window must indicate the specified time segment. For details about how to query the time segments of supported maintenance time windows, see <a href="querying-maintenance-time-windows.md">Querying Maintenance Time Windows</a>.</li><li>The end time is four hours later than the start time. For example, if the start time is 22:00, the end time is 02:00.</li><li>Parameters <strong id="b3691185833412"><a name="b3691185833412"></a><a name="b3691185833412"></a>maintain_begin</strong> and <strong id="b15691155814348"><a name="b15691155814348"></a><a name="b15691155814348"></a>maintain_end</strong> must be set in pairs. If parameter <strong id="b10691145817346"><a name="b10691145817346"></a><a name="b10691145817346"></a>maintain_end</strong> is left blank, parameter <strong id="b14691358153413"><a name="b14691358153413"></a><a name="b14691358153413"></a>maintain_start</strong> is also left blank. In this case, the system automatically set the end time to 06:00.</li></ul>
</td>
</tr>
<tr id="row768311286112"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p2683128811"><a name="p2683128811"></a><a name="p2683128811"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.2 "><p id="p2683122812114"><a name="p2683122812114"></a><a name="p2683122812114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.5.1.3 "><p id="p136831528418"><a name="p136831528418"></a><a name="p136831528418"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p168316286116"><a name="p168316286116"></a><a name="p168316286116"></a>Indicates the security group ID.</p>
</td>
</tr>
</tbody>
</table>

**Example request**

Example 1:

```
{  
    "name": "dms002",  
    "description": "instance description"  
} 
```

Example 2:

```
{ 
     "name": "dms002",   
     "description": "instance description", 
     "maintain_begin":"02:00", 
     "maintain_end":"06:00" 
}
```

## Response<a name="section243616287110"></a>

**Response parameters**

None.

**Example response**

None.

## Status Code<a name="section643822820115"></a>

[Table 3](#table044092812115)  describes the status code of successful operations. For details about other status codes, see  [Status Code](status-code.md).

**Table  3**  Status code

<a name="table044092812115"></a>
<table><thead align="left"><tr id="row1368415282114"><th class="cellrowborder" valign="top" width="15.15%" id="mcps1.2.3.1.1"><p id="p16849281913"><a name="p16849281913"></a><a name="p16849281913"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.85000000000001%" id="mcps1.2.3.1.2"><p id="p5684152812113"><a name="p5684152812113"></a><a name="p5684152812113"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16842281518"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.3.1.1 "><p id="p1468410281117"><a name="p1468410281117"></a><a name="p1468410281117"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="84.85000000000001%" headers="mcps1.2.3.1.2 "><p id="p1868410286115"><a name="p1868410286115"></a><a name="p1868410286115"></a>The instance is modified successfully.</p>
</td>
</tr>
</tbody>
</table>

