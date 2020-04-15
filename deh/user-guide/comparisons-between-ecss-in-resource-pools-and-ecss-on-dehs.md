# Comparisons Between ECSs in Resource Pools and ECSs on DeHs<a name="EN-US_TOPIC_0071443414"></a>

ECSs in resource pools and ECSs on DeHs have almost the same functions except those listed in  [Table 1](#table4650133512557).

**Table  1**  Comparisons between ECSs in resource pools and ECSs on DeHs

<a name="table4650133512557"></a>
<table><thead align="left"><tr id="row46501535105511"><th class="cellrowborder" valign="top" width="21.04210421042104%" id="mcps1.2.4.1.1"><p id="p1765083520559"><a name="p1765083520559"></a><a name="p1765083520559"></a>Item</p>
</th>
<th class="cellrowborder" valign="top" width="35.3035303530353%" id="mcps1.2.4.1.2"><p id="p16501835145513"><a name="p16501835145513"></a><a name="p16501835145513"></a>Resource Pool ECS</p>
</th>
<th class="cellrowborder" valign="top" width="43.65436543654365%" id="mcps1.2.4.1.3"><p id="p1465083517559"><a name="p1465083517559"></a><a name="p1465083517559"></a>DeH ECS</p>
</th>
</tr>
</thead>
<tbody><tr id="row0650635115513"><td class="cellrowborder" valign="top" width="21.04210421042104%" headers="mcps1.2.4.1.1 "><p id="p865012355559"><a name="p865012355559"></a><a name="p865012355559"></a>ECS flavors</p>
</td>
<td class="cellrowborder" valign="top" width="35.3035303530353%" headers="mcps1.2.4.1.2 "><p id="p117197585445"><a name="p117197585445"></a><a name="p117197585445"></a>Multiple ECS types are supported. For details, see the <em id="i84235269717538"><a name="i84235269717538"></a><a name="i84235269717538"></a>Elastic Cloud Server User Guide</em>.</p>
</td>
<td class="cellrowborder" valign="top" width="43.65436543654365%" headers="mcps1.2.4.1.3 "><p id="p8650335165515"><a name="p8650335165515"></a><a name="p8650335165515"></a>Only the ECS flavors supported by DeH flavors can be placed on the DeHs.</p>
</td>
</tr>
<tr id="row16189604712"><td class="cellrowborder" valign="top" width="21.04210421042104%" headers="mcps1.2.4.1.1 "><p id="p51891001375"><a name="p51891001375"></a><a name="p51891001375"></a>Auto recovery</p>
</td>
<td class="cellrowborder" valign="top" width="35.3035303530353%" headers="mcps1.2.4.1.2 "><p id="p41891701773"><a name="p41891701773"></a><a name="p41891701773"></a>Supported</p>
<div class="note" id="note1496975431413"><a name="note1496975431413"></a><a name="note1496975431413"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p199707548144"><a name="p199707548144"></a><a name="p199707548144"></a>The ECS supports powerful automatic failover. If the physical server accommodating the ECS becomes faulty, the ECS can be automatically migrated to a properly running physical server, ensuring service continuity and stability.</p>
</div></div>
</td>
<td class="cellrowborder" valign="top" width="43.65436543654365%" headers="mcps1.2.4.1.3 "><p id="p1518920011713"><a name="p1518920011713"></a><a name="p1518920011713"></a>Not supported</p>
<div class="note" id="note198341832141120"><a name="note198341832141120"></a><a name="note198341832141120"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p19835133271119"><a name="p19835133271119"></a><a name="p19835133271119"></a>An ECS deployed on a DeH is bound to the DeH and cannot be migrated to another DeH if the homing DeH becomes faulty. In this case, the O&amp;M personnel will select another DeH and update the firmware to run the affected ECS.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

