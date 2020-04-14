# Related Services<a name="EN-US_TOPIC_0030713148"></a>

**Table  1**  Related services

<a name="table65381329371"></a>
<table><thead align="left"><tr id="row653913291718"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p12539142918719"><a name="p12539142918719"></a><a name="p12539142918719"></a>Service</p>
</th>
<th class="cellrowborder" valign="top" width="27.622762276227625%" id="mcps1.2.4.1.2"><p id="p4539142911713"><a name="p4539142911713"></a><a name="p4539142911713"></a>Relationship with IMS</p>
</th>
<th class="cellrowborder" valign="top" width="39.043904390439046%" id="mcps1.2.4.1.3"><p id="p35394291571"><a name="p35394291571"></a><a name="p35394291571"></a>Related Operation</p>
</th>
</tr>
</thead>
<tbody><tr id="row7539529579"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p19729155215716"><a name="p19729155215716"></a><a name="p19729155215716"></a>Elastic Cloud Server (ECS)</p>
</td>
<td class="cellrowborder" valign="top" width="27.622762276227625%" headers="mcps1.2.4.1.2 "><p id="p1653918291871"><a name="p1653918291871"></a><a name="p1653918291871"></a>You can use an image to create ECSs or use an ECS to create an image.</p>
</td>
<td class="cellrowborder" valign="top" width="39.043904390439046%" headers="mcps1.2.4.1.3 "><a name="ul1467672315181"></a><a name="ul1467672315181"></a><ul id="ul1467672315181"><li><a href="creating-an-ecs-from-an-image.md">Creating an ECS from an Image</a></li><li><a href="creating-a-system-disk-image-from-a-windows-ecs.md">Creating a System Disk Image from a Windows ECS</a></li><li><a href="creating-a-system-disk-image-from-a-linux-ecs.md">Creating a System Disk Image from a Linux ECS</a></li></ul>
</td>
</tr>
<tr id="row145391829173"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p253914291711"><a name="p253914291711"></a><a name="p253914291711"></a>Bare Metal Server (BMS)</p>
</td>
<td class="cellrowborder" valign="top" width="27.622762276227625%" headers="mcps1.2.4.1.2 "><p id="p65391291713"><a name="p65391291713"></a><a name="p65391291713"></a>You can use an image to create BMSs or use a BMS to create an image.</p>
</td>
<td class="cellrowborder" valign="top" width="39.043904390439046%" headers="mcps1.2.4.1.3 "><p id="p63138221375"><a name="p63138221375"></a><a name="p63138221375"></a><a href="creating-a-bms-system-disk-image.md">Creating a BMS System Disk Image</a></p>
</td>
</tr>
<tr id="row153962917716"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4539329670"><a name="p4539329670"></a><a name="p4539329670"></a>Object Storage Service (OBS)</p>
</td>
<td class="cellrowborder" valign="top" width="27.622762276227625%" headers="mcps1.2.4.1.2 "><p id="p953916298719"><a name="p953916298719"></a><a name="p953916298719"></a>Images are stored in OBS buckets. External image files to be uploaded to the system are stored in OBS buckets, and private images are exported to OBS buckets.</p>
</td>
<td class="cellrowborder" valign="top" width="39.043904390439046%" headers="mcps1.2.4.1.3 "><p id="p187585810914"><a name="p187585810914"></a><a name="p187585810914"></a><a href="exporting-images.md">Exporting Images</a></p>
</td>
</tr>
<tr id="row654012911714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15401829778"><a name="p15401829778"></a><a name="p15401829778"></a>Key Management Service (KMS)</p>
</td>
<td class="cellrowborder" valign="top" width="27.622762276227625%" headers="mcps1.2.4.1.2 "><p id="p105403291678"><a name="p105403291678"></a><a name="p105403291678"></a>KMS provides the keys used for encrypting images.</p>
</td>
<td class="cellrowborder" valign="top" width="39.043904390439046%" headers="mcps1.2.4.1.3 "><p id="p1966042925812"><a name="p1966042925812"></a><a name="p1966042925812"></a><a href="encrypting-images.md">Encrypting Images</a></p>
</td>
</tr>
<tr id="row95401929073"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p19540152914719"><a name="p19540152914719"></a><a name="p19540152914719"></a>Elastic Volume Service (EVS)</p>
</td>
<td class="cellrowborder" valign="top" width="27.622762276227625%" headers="mcps1.2.4.1.2 "><p id="p354014299718"><a name="p354014299718"></a><a name="p354014299718"></a>You can create a data disk image using a data disk of an ECS. The created data disk image can be used to create other EVS disks.</p>
</td>
<td class="cellrowborder" valign="top" width="39.043904390439046%" headers="mcps1.2.4.1.3 "><p id="p164863139411"><a name="p164863139411"></a><a name="p164863139411"></a><a href="creating-a-data-disk-image-from-an-ecs-data-disk.md">Creating a Data Disk Image from an ECS Data Disk</a></p>
</td>
</tr>
<tr id="row1654042918715"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p15407291473"><a name="p15407291473"></a><a name="p15407291473"></a>Cloud Server Backup Service (CSBS)</p>
</td>
<td class="cellrowborder" valign="top" width="27.622762276227625%" headers="mcps1.2.4.1.2 "><p id="p354092910718"><a name="p354092910718"></a><a name="p354092910718"></a>You can use a CSBS backup to create a full-ECS image.</p>
</td>
<td class="cellrowborder" valign="top" width="39.043904390439046%" headers="mcps1.2.4.1.3 "><p id="p3832210185113"><a name="p3832210185113"></a><a name="p3832210185113"></a><a href="creating-a-full-ecs-image-from-a-csbs-backup.md">Creating a Full-ECS Image from a CSBS Backup</a></p>
</td>
</tr>
<tr id="row18846924141820"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p98461248185"><a name="p98461248185"></a><a name="p98461248185"></a>Tag Management Service (TMS)</p>
</td>
<td class="cellrowborder" valign="top" width="27.622762276227625%" headers="mcps1.2.4.1.2 "><p id="p11846424171817"><a name="p11846424171817"></a><a name="p11846424171817"></a>You can add tags to images for convenient classification and search.</p>
</td>
<td class="cellrowborder" valign="top" width="39.043904390439046%" headers="mcps1.2.4.1.3 "><p id="p128461524101819"><a name="p128461524101819"></a><a name="p128461524101819"></a><a href="tagging-an-image.md">Tagging an Image</a></p>
</td>
</tr>
<tr id="row91551216191416"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1615631616149"><a name="p1615631616149"></a><a name="p1615631616149"></a>Cloud Trace Service (CTS)</p>
</td>
<td class="cellrowborder" valign="top" width="27.622762276227625%" headers="mcps1.2.4.1.2 "><p id="p315612168143"><a name="p315612168143"></a><a name="p315612168143"></a>CTS records IMS operations for query, auditing, or backtrack.</p>
</td>
<td class="cellrowborder" valign="top" width="39.043904390439046%" headers="mcps1.2.4.1.3 "><p id="p14440175119411"><a name="p14440175119411"></a><a name="p14440175119411"></a><a href="auditing-key-operations.md">Auditing Key Operations</a></p>
</td>
</tr>
</tbody>
</table>

