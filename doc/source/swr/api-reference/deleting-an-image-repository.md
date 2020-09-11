# Deleting an Image Repository<a name="EN-US_TOPIC_0198655158"></a>

## Function<a name="section14905762191056"></a>

Delete an image repository in an organization.

## URI<a name="section10482810165331"></a>

DELETE /v2/manage/namespaces/\{_namespace_\}/repos/\{_repository_\}

For details about parameters, see  [Table 1](#table184146147323).

**Table  1**  Parameter description

<a name="table184146147323"></a>
<table><thead align="left"><tr id="row1415114163212"><th class="cellrowborder" valign="top" width="18.831883188318834%" id="mcps1.2.5.1.1"><p id="p9415114193219"><a name="p9415114193219"></a><a name="p9415114193219"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.64246424642464%" id="mcps1.2.5.1.2"><p id="p15022419437"><a name="p15022419437"></a><a name="p15022419437"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="22.63226322632263%" id="mcps1.2.5.1.3"><p id="p1450315424313"><a name="p1450315424313"></a><a name="p1450315424313"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.89338933893389%" id="mcps1.2.5.1.4"><p id="p841591415328"><a name="p841591415328"></a><a name="p841591415328"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row941641411326"><td class="cellrowborder" valign="top" width="18.831883188318834%" headers="mcps1.2.5.1.1 "><p id="p8416314113213"><a name="p8416314113213"></a><a name="p8416314113213"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="24.64246424642464%" headers="mcps1.2.5.1.2 "><p id="p105058419438"><a name="p105058419438"></a><a name="p105058419438"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="22.63226322632263%" headers="mcps1.2.5.1.3 "><p id="p10507114164313"><a name="p10507114164313"></a><a name="p10507114164313"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.89338933893389%" headers="mcps1.2.5.1.4 "><p id="p18734369112"><a name="p18734369112"></a><a name="p18734369112"></a>Organization name.</p>
</td>
</tr>
<tr id="row7417171415327"><td class="cellrowborder" valign="top" width="18.831883188318834%" headers="mcps1.2.5.1.1 "><p id="p84177144326"><a name="p84177144326"></a><a name="p84177144326"></a>repository</p>
</td>
<td class="cellrowborder" valign="top" width="24.64246424642464%" headers="mcps1.2.5.1.2 "><p id="p13259041124313"><a name="p13259041124313"></a><a name="p13259041124313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="22.63226322632263%" headers="mcps1.2.5.1.3 "><p id="p142591841114317"><a name="p142591841114317"></a><a name="p142591841114317"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.89338933893389%" headers="mcps1.2.5.1.4 "><p id="p181285313257"><a name="p181285313257"></a><a name="p181285313257"></a>Image repository name.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section3270966102931"></a>

N/A

## Response<a name="section46271297104114"></a>

N/A

## Status Code<a name="section5365169104253"></a>

For details about status code, see  [Table 2](#table83715129124).

**Table  2**  Status code

<a name="table83715129124"></a>
<table><thead align="left"><tr id="row0371712141214"><th class="cellrowborder" valign="top" width="22.98%" id="mcps1.2.3.1.1"><p id="p3371112171215"><a name="p3371112171215"></a><a name="p3371112171215"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="77.02%" id="mcps1.2.3.1.2"><p id="p13781210124"><a name="p13781210124"></a><a name="p13781210124"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row103819129123"><td class="cellrowborder" valign="top" width="22.98%" headers="mcps1.2.3.1.1 "><p id="p1238912101213"><a name="p1238912101213"></a><a name="p1238912101213"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="77.02%" headers="mcps1.2.3.1.2 "><p id="p73871261219"><a name="p73871261219"></a><a name="p73871261219"></a>The brief information about the image repository is successfully deleted.</p>
</td>
</tr>
<tr id="row1338151211120"><td class="cellrowborder" valign="top" width="22.98%" headers="mcps1.2.3.1.1 "><p id="p23851210121"><a name="p23851210121"></a><a name="p23851210121"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="77.02%" headers="mcps1.2.3.1.2 "><p id="p1238161271215"><a name="p1238161271215"></a><a name="p1238161271215"></a>Request error. Error information is returned.</p>
</td>
</tr>
<tr id="row738171215127"><td class="cellrowborder" valign="top" width="22.98%" headers="mcps1.2.3.1.1 "><p id="p43881201211"><a name="p43881201211"></a><a name="p43881201211"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="77.02%" headers="mcps1.2.3.1.2 "><p id="p4381212121219"><a name="p4381212121219"></a><a name="p4381212121219"></a>The repository does not exist.</p>
</td>
</tr>
<tr id="row1162431422920"><td class="cellrowborder" valign="top" width="22.98%" headers="mcps1.2.3.1.1 "><p id="p14625141492918"><a name="p14625141492918"></a><a name="p14625141492918"></a>406</p>
</td>
<td class="cellrowborder" valign="top" width="77.02%" headers="mcps1.2.3.1.2 "><p id="p145322112919"><a name="p145322112919"></a><a name="p145322112919"></a>The repository cannot be deleted because it contains images.</p>
</td>
</tr>
<tr id="row13381712111212"><td class="cellrowborder" valign="top" width="22.98%" headers="mcps1.2.3.1.1 "><p id="p33819120123"><a name="p33819120123"></a><a name="p33819120123"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="77.02%" headers="mcps1.2.3.1.2 "><p id="p638101219128"><a name="p638101219128"></a><a name="p638101219128"></a>Internal error. Error information is returned.</p>
</td>
</tr>
</tbody>
</table>

