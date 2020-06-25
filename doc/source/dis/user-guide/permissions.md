# Permissions<a name="dis_01_0005"></a>

You need an account on the management console to create, query, and delete DIS streams, and need an Access Key ID/Secret Access Key \(AK/SK\) file to push, pull, and dump data.

For details about how to perform operations on IAM, see  _IAM User Guide_.

For details about DIS permissions, see  [Table 1](#table55585464113541)  and  [Permissions](https://docs.otc.t-systems.com/en-us/permissions/index.html).

**Table  1**  Permission list

<a name="table55585464113541"></a>
<table><thead align="left"><tr id="row45371081113541"><th class="cellrowborder" valign="top" width="13.048695130486951%" id="mcps1.2.6.1.1"><p id="p13899358113555"><a name="p13899358113555"></a><a name="p13899358113555"></a>Node Name</p>
</th>
<th class="cellrowborder" valign="top" width="11.918808119188082%" id="mcps1.2.6.1.2"><p id="p52106194113555"><a name="p52106194113555"></a><a name="p52106194113555"></a>Permission Name</p>
</th>
<th class="cellrowborder" valign="top" width="13.048695130486951%" id="mcps1.2.6.1.3"><p id="p59852179113555"><a name="p59852179113555"></a><a name="p59852179113555"></a>Managed Cloud Resource</p>
</th>
<th class="cellrowborder" valign="top" width="17.738226177382263%" id="mcps1.2.6.1.4"><p id="p16188296113555"><a name="p16188296113555"></a><a name="p16188296113555"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="44.24557544245575%" id="mcps1.2.6.1.5"><p id="p36183577113555"><a name="p36183577113555"></a><a name="p36183577113555"></a>How to Assign Permissions</p>
</th>
</tr>
</thead>
<tbody><tr id="row37379105113541"><td class="cellrowborder" valign="top" width="13.048695130486951%" headers="mcps1.2.6.1.1 "><p id="p36402482113555"><a name="p36402482113555"></a><a name="p36402482113555"></a>Base</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.6.1.2 "><p id="p33286409113555"><a name="p33286409113555"></a><a name="p33286409113555"></a>Tenant Administrator</p>
</td>
<td class="cellrowborder" valign="top" width="13.048695130486951%" headers="mcps1.2.6.1.3 "><p id="p11844610113555"><a name="p11844610113555"></a><a name="p11844610113555"></a>All services</p>
</td>
<td class="cellrowborder" valign="top" width="17.738226177382263%" headers="mcps1.2.6.1.4 "><p id="p19889388113555"><a name="p19889388113555"></a><a name="p19889388113555"></a>Users have permission to operate all cloud resources owned by an enterprise.</p>
</td>
<td class="cellrowborder" valign="top" width="44.24557544245575%" headers="mcps1.2.6.1.5 "><p id="p427759113555"><a name="p427759113555"></a><a name="p427759113555"></a>Permission parameter settings:</p>
<p id="p3849833113555"><a name="p3849833113555"></a><a name="p3849833113555"></a><strong id="b2350590232224"><a name="b2350590232224"></a><a name="b2350590232224"></a>Region</strong>: set to the region to which your cloud resources belong. <strong id="b17214290292717"><a name="b17214290292717"></a><a name="b17214290292717"></a>Project</strong>: set to the project to which your cloud resources belong. <strong id="b174057153592721"><a name="b174057153592721"></a><a name="b174057153592721"></a>Policy</strong>: set to <strong id="b206618248692721"><a name="b206618248692721"></a><a name="b206618248692721"></a>Tenant Administrator</strong>.</p>
</td>
</tr>
<tr id="row28310851113541"><td class="cellrowborder" valign="top" width="13.048695130486951%" headers="mcps1.2.6.1.1 "><p id="p55064925113555"><a name="p55064925113555"></a><a name="p55064925113555"></a>DIS</p>
</td>
<td class="cellrowborder" valign="top" width="11.918808119188082%" headers="mcps1.2.6.1.2 "><p id="p31073945113555"><a name="p31073945113555"></a><a name="p31073945113555"></a>DIS Administrator</p>
</td>
<td class="cellrowborder" valign="top" width="13.048695130486951%" headers="mcps1.2.6.1.3 "><p id="p37219068113555"><a name="p37219068113555"></a><a name="p37219068113555"></a>DIS</p>
</td>
<td class="cellrowborder" valign="top" width="17.738226177382263%" headers="mcps1.2.6.1.4 "><p id="p61954552113555"><a name="p61954552113555"></a><a name="p61954552113555"></a>Users have permissions to perform the following operations:</p>
<a name="ul20720064113555"></a><a name="ul20720064113555"></a><ul id="ul20720064113555"><li>Create, delete, modify, and query DIS streams</li><li>Create, delete, modify, and query dump tasks</li><li>Upload and download data through a stream</li><li>Query stream monitoring metrics</li></ul>
</td>
<td class="cellrowborder" valign="top" width="44.24557544245575%" headers="mcps1.2.6.1.5 "><p id="p43730058113555"><a name="p43730058113555"></a><a name="p43730058113555"></a>Permission parameter settings:</p>
<a name="ul64599346103556"></a><a name="ul64599346103556"></a><ul id="ul64599346103556"><li><strong id="b3739007810361"><a name="b3739007810361"></a><a name="b3739007810361"></a>Region</strong>: set to the region to which DIS streams belong.</li><li><strong id="b656707310363"><a name="b656707310363"></a><a name="b656707310363"></a>Project</strong>: set to the project to which DIS streams belong.</li><li><strong id="b6597054103556"><a name="b6597054103556"></a><a name="b6597054103556"></a>Policy</strong>: set to <strong id="b59373488103556"><a name="b59373488103556"></a><a name="b59373488103556"></a>DIS Administrator</strong>.</li></ul>
<div class="p" id="p47101587113831"><a name="p47101587113831"></a><a name="p47101587113831"></a>Assign different permissions based on the destination to which data of DIS streams will be dumped.<a name="ul21261106113831"></a><a name="ul21261106113831"></a><ul id="ul21261106113831"><li class="textintable">To create DIS streams capable of dumping data to OBS and ensure that the users have permissions to use both DIS and OBS. </li><li class="textintable">Parameter settings required for using OBS:<p id="p4825762103940"><a name="p4825762103940"></a><a name="p4825762103940"></a><strong id="b53552933103940"><a name="b53552933103940"></a><a name="b53552933103940"></a>Region</strong>: set to <strong id="b12214356103940"><a name="b12214356103940"></a><a name="b12214356103940"></a>Global service</strong>.</p>
<p id="p66027931103943"><a name="p66027931103943"></a><a name="p66027931103943"></a><strong id="b21538696103943"><a name="b21538696103943"></a><a name="b21538696103943"></a>Project</strong>: set to <strong id="b59630539103943"><a name="b59630539103943"></a><a name="b59630539103943"></a>OBS</strong>.</p>
<p id="p44428001113831"><a name="p44428001113831"></a><a name="p44428001113831"></a><strong id="b16209065149406"><a name="b16209065149406"></a><a name="b16209065149406"></a>Policy</strong>: set to <strong id="b13673228949406"><a name="b13673228949406"></a><a name="b13673228949406"></a>Tenant Administrator</strong>.</p>
</li></ul>
</div>
</td>
</tr>
</tbody>
</table>

