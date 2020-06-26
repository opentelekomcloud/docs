# Function Description<a name="obs_03_0402"></a>

[Table 1](#tcd411e26f9974e8b8a6642bdc4534bc4)  describes the functions of OBS Browser:

**Table  1**  Function description

<a name="tcd411e26f9974e8b8a6642bdc4534bc4"></a>
<table><thead align="left"><tr id="r66c9ad2e76e6438687cf97d397e6876c"><th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.3.1.1"><p id="acbf8e31d8da346a9a8367f65b532cc3e"><a name="acbf8e31d8da346a9a8367f65b532cc3e"></a><a name="acbf8e31d8da346a9a8367f65b532cc3e"></a>Function</p>
</th>
<th class="cellrowborder" valign="top" width="65.98%" id="mcps1.2.3.1.2"><p id="a62baac5347f949409bb2dc1f2fc27e4b"><a name="a62baac5347f949409bb2dc1f2fc27e4b"></a><a name="a62baac5347f949409bb2dc1f2fc27e4b"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rd3cf6282803e42aa8cf96a6fc8b08156"><td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.3.1.1 "><p id="a8666b8f9d4b9404a9f2388771b0b0ff8"><a name="a8666b8f9d4b9404a9f2388771b0b0ff8"></a><a name="a8666b8f9d4b9404a9f2388771b0b0ff8"></a><a href="managing-buckets-1.md">Bucket management</a></p>
</td>
<td class="cellrowborder" valign="top" width="65.98%" headers="mcps1.2.3.1.2 "><p id="a146050e666dd438eb14d8e715a6ce5f5"><a name="a146050e666dd438eb14d8e715a6ce5f5"></a><a name="a146050e666dd438eb14d8e715a6ce5f5"></a>Creates and deletes buckets of different storage classes in specific regions (service areas) and changes bucket storage classes.</p>
</td>
</tr>
<tr id="r5acb8ca9c46d4b32ba19ef46dcd6ff51"><td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.3.1.1 "><p id="a3109dfef548d4aac84df9b78768992e5"><a name="a3109dfef548d4aac84df9b78768992e5"></a><a name="a3109dfef548d4aac84df9b78768992e5"></a><a href="managing-objects-3.md">Object management</a></p>
</td>
<td class="cellrowborder" valign="top" width="65.98%" headers="mcps1.2.3.1.2 "><p id="p68131665411"><a name="p68131665411"></a><a name="p68131665411"></a>Manages objects by uploading (including multipart uploading), downloading, deleting, changing storage classes, restoring Cold objects, and sharing objects through URLs.</p>
<p id="p393263819495"><a name="p393263819495"></a><a name="p393263819495"></a>Supports batch upload and download objects, as well as multipart upload.</p>
</td>
</tr>
<tr id="row16682104155516"><td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.3.1.1 "><p id="a86172af891254492b49e41476b7159d0"><a name="a86172af891254492b49e41476b7159d0"></a><a name="a86172af891254492b49e41476b7159d0"></a><a href="managing-fragments.md">Fragment management</a></p>
</td>
<td class="cellrowborder" valign="top" width="65.98%" headers="mcps1.2.3.1.2 "><p id="aa910245d94ad42d986dbf12f8b8e316c"><a name="aa910245d94ad42d986dbf12f8b8e316c"></a><a name="aa910245d94ad42d986dbf12f8b8e316c"></a>Enables you to clear fragments that have been generated.</p>
</td>
</tr>
<tr id="row2267193116251"><td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.3.1.1 "><p id="p1426815317251"><a name="p1426815317251"></a><a name="p1426815317251"></a><a href="permission-control-6.md">Permission control</a></p>
</td>
<td class="cellrowborder" valign="top" width="65.98%" headers="mcps1.2.3.1.2 "><p id="p8060118"><a name="p8060118"></a><a name="p8060118"></a>OBS Browser supports permission control based on bucket policies, bucket ACLs, and object ACLs.</p>
</td>
</tr>
<tr id="row6360153417109"><td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.3.1.1 "><p id="a25b870810ad54bf4bb1d4a01e1e9d38d"><a name="a25b870810ad54bf4bb1d4a01e1e9d38d"></a><a name="a25b870810ad54bf4bb1d4a01e1e9d38d"></a><a href="server-side-encryption-5.md">Server-side encryption</a></p>
</td>
<td class="cellrowborder" valign="top" width="65.98%" headers="mcps1.2.3.1.2 "><p id="a8b007e7b1f444c1589b62823423e6a83"><a name="a8b007e7b1f444c1589b62823423e6a83"></a><a name="a8b007e7b1f444c1589b62823423e6a83"></a>OBS allows user to encrypt objects using server-side encryption so that the objects can be securely stored in OBS.</p>
</td>
</tr>
<tr id="row1253716179589"><td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.3.1.1 "><p id="p1236010446488"><a name="p1236010446488"></a><a name="p1236010446488"></a><a href="cors-(browser).md">CORS</a></p>
</td>
<td class="cellrowborder" valign="top" width="65.98%" headers="mcps1.2.3.1.2 "><p id="p536013440486"><a name="p536013440486"></a><a name="p536013440486"></a>CORS is a browser-standard mechanism provided by the World Wide Web Consortium (W3C). It defines the interaction methods between client-side web applications in one origin and resources in another origin. For general web page requests, website scripts and contents in one origin cannot interact with those in another origin because of Same Origin Policies (SOPs).</p>
</td>
</tr>
<tr id="r35b174339a5440b3a6a12b36b0c2f21b"><td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.3.1.1 "><p id="a778cb45d735440069f1142715356722d"><a name="a778cb45d735440069f1142715356722d"></a><a name="a778cb45d735440069f1142715356722d"></a><a href="logging-8.md">Logging</a></p>
</td>
<td class="cellrowborder" valign="top" width="65.98%" headers="mcps1.2.3.1.2 "><p id="afbb33abb025a439b97a83af110ac2deb"><a name="afbb33abb025a439b97a83af110ac2deb"></a><a name="afbb33abb025a439b97a83af110ac2deb"></a>Records bucket access requests in logs for request analysis and log audit.</p>
</td>
</tr>
<tr id="rf5655e2bb78448d19404250f8c5728be"><td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.3.1.1 "><p id="a9ee0fc1553da440bb67d615fe5b2dd7d"><a name="a9ee0fc1553da440bb67d615fe5b2dd7d"></a><a name="a9ee0fc1553da440bb67d615fe5b2dd7d"></a><a href="lifecycle-management-7.md">Lifecycle management</a></p>
</td>
<td class="cellrowborder" valign="top" width="65.98%" headers="mcps1.2.3.1.2 "><p id="a37d863511cf54a2cad8ce931f95f278e"><a name="a37d863511cf54a2cad8ce931f95f278e"></a><a name="a37d863511cf54a2cad8ce931f95f278e"></a>Supports the ability to set lifecycle rules for buckets to automatically delete expired objects.</p>
</td>
</tr>
<tr id="r5b134c229f6e4057b1f0c76bf0bd18c6"><td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.3.1.1 "><p id="a42169f33633548c888286b6b201b3572"><a name="a42169f33633548c888286b6b201b3572"></a><a name="a42169f33633548c888286b6b201b3572"></a><a href="external-buckets.md">External bucket adding</a></p>
</td>
<td class="cellrowborder" valign="top" width="65.98%" headers="mcps1.2.3.1.2 "><p id="aff7f44174f2646349df8463530160f37"><a name="aff7f44174f2646349df8463530160f37"></a><a name="aff7f44174f2646349df8463530160f37"></a>Allows you to manage data shared by other OBS users.</p>
</td>
</tr>
<tr id="r56bcaf0f197e4fce83e16238de410e63"><td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.3.1.1 "><p id="a84907a8a1a874fb38dd2fd9f42566f32"><a name="a84907a8a1a874fb38dd2fd9f42566f32"></a><a name="a84907a8a1a874fb38dd2fd9f42566f32"></a><a href="task-management.md">Task management</a></p>
</td>
<td class="cellrowborder" valign="top" width="65.98%" headers="mcps1.2.3.1.2 "><p id="p10995321165348"><a name="p10995321165348"></a><a name="p10995321165348"></a>Allows you to upload, download, delete, and restore tasks.</p>
</td>
</tr>
</tbody>
</table>

