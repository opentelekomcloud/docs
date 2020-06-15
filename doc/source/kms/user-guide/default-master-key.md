# Default Master Key<a name="kms_01_0006"></a>

A Default Master Key is automatically created by another cloud service using KMS, such as Object Storage Service \(OBS\). The alias of a Default Master Key ends with  **/default**.

You can use the management console to query the status of Default Master Keys, but cannot disable or schedule the deletion of Default Master Keys.

**Table  1**  Default Master Keys

<a name="table2077517211519"></a>
<table><thead align="left"><tr id="row1777602185116"><th class="cellrowborder" valign="top" width="26.5%" id="mcps1.2.3.1.1"><p id="p477711285114"><a name="p477711285114"></a><a name="p477711285114"></a><strong id="b842352706114440_1"><a name="b842352706114440_1"></a><a name="b842352706114440_1"></a>Alias</strong></p>
</th>
<th class="cellrowborder" valign="top" width="73.5%" id="mcps1.2.3.1.2"><p id="p1177916225117"><a name="p1177916225117"></a><a name="p1177916225117"></a><strong id="b842352706114445_1"><a name="b842352706114445_1"></a><a name="b842352706114445_1"></a>Cloud Service</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row977911275118"><td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.3.1.1 "><p id="p1577914215512"><a name="p1577914215512"></a><a name="p1577914215512"></a>obs/default</p>
</td>
<td class="cellrowborder" valign="top" width="73.5%" headers="mcps1.2.3.1.2 "><p id="p378020265119"><a name="p378020265119"></a><a name="p378020265119"></a>OBS</p>
</td>
</tr>
<tr id="row10780428512"><td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.3.1.1 "><p id="p1978220265110"><a name="p1978220265110"></a><a name="p1978220265110"></a>evs/default</p>
</td>
<td class="cellrowborder" valign="top" width="73.5%" headers="mcps1.2.3.1.2 "><p id="p17782182175119"><a name="p17782182175119"></a><a name="p17782182175119"></a>Elastic Volume Service (EVS)</p>
</td>
</tr>
<tr id="row47822245114"><td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.3.1.1 "><p id="p478211205110"><a name="p478211205110"></a><a name="p478211205110"></a>ims/default</p>
</td>
<td class="cellrowborder" valign="top" width="73.5%" headers="mcps1.2.3.1.2 "><p id="p147846275115"><a name="p147846275115"></a><a name="p147846275115"></a>Image Management Service (IMS)</p>
</td>
</tr>
<tr id="row14776143811518"><td class="cellrowborder" valign="top" width="26.5%" headers="mcps1.2.3.1.1 "><p id="p167779380511"><a name="p167779380511"></a><a name="p167779380511"></a>sfs/default</p>
</td>
<td class="cellrowborder" valign="top" width="73.5%" headers="mcps1.2.3.1.2 "><p id="p167771638195110"><a name="p167771638195110"></a><a name="p167771638195110"></a>Scalable File Service (SFS)</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>A Default Master Key is automatically created when a user employs the KMS encryption function for the first time in another cloud service.  

