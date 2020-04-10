# Common Image Formats<a name="EN-US_TOPIC_0089615820"></a>

IMS supports multiple image formats, and the system uses the ZVHD format by default.

[Table 1](#table44616390201811)  lists the common  image formats.

**Table  1**  Common image formats

<a name="table44616390201811"></a>
<table><thead align="left"><tr id="row7416711201811"><th class="cellrowborder" valign="top" width="19.61%" id="mcps1.2.4.1.1"><p id="p3513732420214"><a name="p3513732420214"></a><a name="p3513732420214"></a>Image Format</p>
</th>
<th class="cellrowborder" valign="top" width="47.06%" id="mcps1.2.4.1.2"><p id="p2755096220214"><a name="p2755096220214"></a><a name="p2755096220214"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.3"><p id="p1703544920214"><a name="p1703544920214"></a><a name="p1703544920214"></a>Remarks</p>
</th>
</tr>
</thead>
<tbody><tr id="row4661818201811"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.4.1.1 "><p id="p370276720214"><a name="p370276720214"></a><a name="p370276720214"></a>ZVHD</p>
</td>
<td class="cellrowborder" valign="top" width="47.06%" headers="mcps1.2.4.1.2 "><p id="p3148868620214"><a name="p3148868620214"></a><a name="p3148868620214"></a>This is a self-developed format. It uses the ZLIB compression algorithm and supports sequential read and write.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p44676220214"><a name="p44676220214"></a><a name="p44676220214"></a>A universal format supported by IaaS OpenStack A format supported for imported and exported images</p>
</td>
</tr>
<tr id="row10287614201811"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.4.1.1 "><p id="p5725404320214"><a name="p5725404320214"></a><a name="p5725404320214"></a>ZVHD2</p>
</td>
<td class="cellrowborder" valign="top" width="47.06%" headers="mcps1.2.4.1.2 "><p id="p706590120214"><a name="p706590120214"></a><a name="p706590120214"></a>This is a self-developed format. It uses the ZSTD algorithm and supports lazy loading.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p3546709520214"><a name="p3546709520214"></a><a name="p3546709520214"></a>A format for the lazy loading feature A format supported for imported images</p>
</td>
</tr>
<tr id="row49765378201811"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.4.1.1 "><p id="p1860015120214"><a name="p1860015120214"></a><a name="p1860015120214"></a>QCOW2</p>
</td>
<td class="cellrowborder" valign="top" width="47.06%" headers="mcps1.2.4.1.2 "><p id="p3021728620214"><a name="p3021728620214"></a><a name="p3021728620214"></a>This is a disk image supported by the QEMU simulator. It is a file that indicates a block device disk of a fixed size. Compared with the RAW format, the QCOW2 format has the following features:</p>
<a name="ul2482301310111"></a><a name="ul2482301310111"></a><ul id="ul2482301310111"><li>Supports a lower disk usage.</li><li>Supports Copy-On-Write (CoW). The image file only reflects the changes of disks.</li><li>Supports snapshots.</li><li>Supports zlib compression and encryption by following Advanced Encryption Standard (AES).</li></ul>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p1043906420214"><a name="p1043906420214"></a><a name="p1043906420214"></a>A format supported for imported and exported images</p>
</td>
</tr>
<tr id="row46398011201811"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.4.1.1 "><p id="p2677651520214"><a name="p2677651520214"></a><a name="p2677651520214"></a>VMDK</p>
</td>
<td class="cellrowborder" valign="top" width="47.06%" headers="mcps1.2.4.1.2 "><p id="p2141408420214"><a name="p2141408420214"></a><a name="p2141408420214"></a>VMDK is a virtual disk format created by VMware. A VMDK file represents a physical disk drive of the virtual machine file system (VMFS) on an <span id="text2436711173311"><a name="text2436711173311"></a><a name="text2436711173311"></a></span><span id="text178801512163319"><a name="text178801512163319"></a><a name="text178801512163319"></a>ECS</span>.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p5681927520214"><a name="p5681927520214"></a><a name="p5681927520214"></a>A format supported for imported and exported images</p>
</td>
</tr>
<tr id="row30482282201811"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.4.1.1 "><p id="p1508241120214"><a name="p1508241120214"></a><a name="p1508241120214"></a>VHD</p>
</td>
<td class="cellrowborder" valign="top" width="47.06%" headers="mcps1.2.4.1.2 "><p id="p1371575520214"><a name="p1371575520214"></a><a name="p1371575520214"></a>VHD is a virtual disk file format provided by Microsoft. A VHD file is a compressed file stored in the file system of the host machine. It mainly contains a file system required for starting ECSs.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p3723438020214"><a name="p3723438020214"></a><a name="p3723438020214"></a>A format supported for imported and exported images</p>
</td>
</tr>
<tr id="row60908757201811"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.4.1.1 "><p id="p3188234120214"><a name="p3188234120214"></a><a name="p3188234120214"></a>VHDX</p>
</td>
<td class="cellrowborder" valign="top" width="47.06%" headers="mcps1.2.4.1.2 "><p id="p3233281420214"><a name="p3233281420214"></a><a name="p3233281420214"></a>VHDX is a new VHD format introduced into Hyper-V of Windows Server 2012 by Microsoft. Compared with the VHD format, VHDX has a larger storage capacity. It provides protection against data damage during power supply failures and optimizes the disk structure alignment mode to prevent performance degradation of new physical disks in a large sector.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p171227620214"><a name="p171227620214"></a><a name="p171227620214"></a>A format supported for imported images</p>
</td>
</tr>
<tr id="row19913227201811"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.4.1.1 "><p id="p4028974420214"><a name="p4028974420214"></a><a name="p4028974420214"></a>RAW</p>
</td>
<td class="cellrowborder" valign="top" width="47.06%" headers="mcps1.2.4.1.2 "><p id="p4224383620214"><a name="p4224383620214"></a><a name="p4224383620214"></a>A RAW file can be directly read and written by ECSs. This format does not support dynamic space expansion and has the best I/O performance.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p6630755220214"><a name="p6630755220214"></a><a name="p6630755220214"></a>A format supported for imported images</p>
</td>
</tr>
<tr id="row18432362201821"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.4.1.1 "><p id="p1982395520214"><a name="p1982395520214"></a><a name="p1982395520214"></a>QCOW</p>
</td>
<td class="cellrowborder" valign="top" width="47.06%" headers="mcps1.2.4.1.2 "><p id="p6223655620214"><a name="p6223655620214"></a><a name="p6223655620214"></a>QCOW manages the space allocation of an image through the secondary index table. The secondary index uses the memory cache technology and needs the query operation, which results in performance loss. The performance of QCOW is inferior to that of QCOW2, and the read and write performance is inferior to that of RAW.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p799628120214"><a name="p799628120214"></a><a name="p799628120214"></a>A format supported for imported images</p>
</td>
</tr>
<tr id="row56057847201821"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.4.1.1 "><p id="p5792707020214"><a name="p5792707020214"></a><a name="p5792707020214"></a>VDI</p>
</td>
<td class="cellrowborder" valign="top" width="47.06%" headers="mcps1.2.4.1.2 "><p id="p6158108520214"><a name="p6158108520214"></a><a name="p6158108520214"></a>VDI is the disk image file format used by the Virtual BOX virtualization software of SUN. It supports snapshots.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p2201201320214"><a name="p2201201320214"></a><a name="p2201201320214"></a>A format supported for imported images</p>
</td>
</tr>
<tr id="row48240807201821"><td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.4.1.1 "><p id="p773949520214"><a name="p773949520214"></a><a name="p773949520214"></a>QED</p>
</td>
<td class="cellrowborder" valign="top" width="47.06%" headers="mcps1.2.4.1.2 "><p id="p2291931920214"><a name="p2291931920214"></a><a name="p2291931920214"></a>The QED format is an evolved version of the QCOW2 format. Its storage location query mode and data block size are the same as those of the QCOW2 format. However, QED implements Copy-On-Write (CoW) in a different way as it uses a dirty flag to replace the reference count table of QCOW2.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.3 "><p id="p4452552320214"><a name="p4452552320214"></a><a name="p4452552320214"></a>A format supported for imported images</p>
</td>
</tr>
</tbody>
</table>

