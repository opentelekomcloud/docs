# Is the BMS Host Name with Suffix novalocal Normal?<a name="EN-US_TOPIC_0166937671"></a>

## Symptom<a name="section10979141164416"></a>

Host names of some BMSs have suffix  **.novalocal**.

For example, the host name is set to  **abc**  during BMS creation.  [Table 1](#table168595206502)  lists the host names \(obtained by running the  **hostname**  command\) of BMSs created using different images and those displayed after the BMSs are restarted.

**Table  1**  Hostnames of BMSs created from different images

<a name="table168595206502"></a>
<table><thead align="left"><tr id="row1886017204502"><th class="cellrowborder" valign="top" width="30.693069306930692%" id="mcps1.2.4.1.1"><p id="p78601120205016"><a name="p78601120205016"></a><a name="p78601120205016"></a>Image</p>
</th>
<th class="cellrowborder" valign="top" width="29.7029702970297%" id="mcps1.2.4.1.2"><p id="p1386072045010"><a name="p1386072045010"></a><a name="p1386072045010"></a>Host Name Before BMS Restart</p>
</th>
<th class="cellrowborder" valign="top" width="39.603960396039604%" id="mcps1.2.4.1.3"><p id="p13931651105213"><a name="p13931651105213"></a><a name="p13931651105213"></a>Host Name After BMS Restart</p>
</th>
</tr>
</thead>
<tbody><tr id="row5860162011509"><td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.4.1.1 "><p id="p386012085016"><a name="p386012085016"></a><a name="p386012085016"></a>CentOS 6.8</p>
</td>
<td class="cellrowborder" valign="top" width="29.7029702970297%" headers="mcps1.2.4.1.2 "><p id="p486042016501"><a name="p486042016501"></a><a name="p486042016501"></a>abc</p>
</td>
<td class="cellrowborder" valign="top" width="39.603960396039604%" headers="mcps1.2.4.1.3 "><p id="p4932551195211"><a name="p4932551195211"></a><a name="p4932551195211"></a>abc.novalocal</p>
</td>
</tr>
<tr id="row11860820185019"><td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.4.1.1 "><p id="p286062015501"><a name="p286062015501"></a><a name="p286062015501"></a>CentOS 7.3</p>
</td>
<td class="cellrowborder" valign="top" width="29.7029702970297%" headers="mcps1.2.4.1.2 "><p id="p10860162011508"><a name="p10860162011508"></a><a name="p10860162011508"></a>abc.novalocal</p>
</td>
<td class="cellrowborder" valign="top" width="39.603960396039604%" headers="mcps1.2.4.1.3 "><p id="p29321951115218"><a name="p29321951115218"></a><a name="p29321951115218"></a>abc.novalocal</p>
</td>
</tr>
<tr id="row1086082045017"><td class="cellrowborder" valign="top" width="30.693069306930692%" headers="mcps1.2.4.1.1 "><p id="p98600203505"><a name="p98600203505"></a><a name="p98600203505"></a>Ubuntu 16</p>
</td>
<td class="cellrowborder" valign="top" width="29.7029702970297%" headers="mcps1.2.4.1.2 "><p id="p17860172016504"><a name="p17860172016504"></a><a name="p17860172016504"></a>abc</p>
</td>
<td class="cellrowborder" valign="top" width="39.603960396039604%" headers="mcps1.2.4.1.3 "><p id="p7932751125212"><a name="p7932751125212"></a><a name="p7932751125212"></a>abc</p>
</td>
</tr>
</tbody>
</table>

Host names of BMSs created from some types of images have suffix  **.novalocal**, while others do not.

## Troubleshooting<a name="section152294541871"></a>

This is a normal phenomenon.

The static host name of a Linux BMS is user-defined and injected using Cloud-Init during the BMS creation. According to the test results, Cloud-Init adapts to OSs differently. As a result, hostnames of some ECSs have suffix  **.novalocal**, while others do not.

If you want to ensure that all host names do not have suffix  **.novalocal**, you can change the hostname. For details, see  [Changing the Name of a BMS](changing-the-name-of-a-bms.md)

