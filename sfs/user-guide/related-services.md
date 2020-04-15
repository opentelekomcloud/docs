# Related Services<a name="sfs_01_0007"></a>

[Table 1](#table128311585308)  shows the relationship between SFS and other cloud services.

**Table  1**  Related services

<a name="table128311585308"></a>
<table><thead align="left"><tr id="row1283138113020"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p78323843011"><a name="p78323843011"></a><a name="p78323843011"></a>Function</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1583208183018"><a name="p1583208183018"></a><a name="p1583208183018"></a>Related Service</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p1183298143014"><a name="p1183298143014"></a><a name="p1183298143014"></a>Reference</p>
</th>
</tr>
</thead>
<tbody><tr id="row88321285307"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p13832178183011"><a name="p13832178183011"></a><a name="p13832178183011"></a>A file system and the associated ECSs must belong to the same project. File systems are mounted to shared paths for data sharing.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1783219820302"><a name="p1783219820302"></a><a name="p1783219820302"></a>Elastic Cloud Server (ECS)</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p119861917519"><a name="p119861917519"></a><a name="p119861917519"></a><a href="mounting-an-nfs-file-system-to-ecss-(linux).md">Mounting an NFS File System to ECSs (Linux)</a></p>
<p id="p12439185014525"><a name="p12439185014525"></a><a name="p12439185014525"></a><a href="mounting-an-nfs-file-system-to-ecss-(windows-2012).md">Mounting an NFS File System to ECSs (Windows 2012)</a></p>
</td>
</tr>
<tr id="row0832484307"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1520012484238"><a name="p1520012484238"></a><a name="p1520012484238"></a>VPC provisions an isolated virtual network environment defined and managed by yourself, improving the security of cloud resources and simplifying network deployment.</p>
<p id="p840082141914"><a name="p840082141914"></a><a name="p840082141914"></a>An ECS cannot access file systems in a different VPC. Before using SFS, assign the file system and the associated ECSs to the same VPC.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p148328863017"><a name="p148328863017"></a><a name="p148328863017"></a>Virtual Private Cloud (VPC)</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p342011405498"><a name="p342011405498"></a><a name="p342011405498"></a><a href="step-1-create-a-file-system.md">Creating a File System</a></p>
</td>
</tr>
<tr id="row1083218813306"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1483212863019"><a name="p1483212863019"></a><a name="p1483212863019"></a>IAM is an enterprise-level self-help cloud resource management system. It provides user identity management and access control functions. When an enterprise needs to provide SFS for multiple users within the enterprise, the enterprise administrator can use IAM to create users and control these users' permissions on enterprise resources.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p108323810306"><a name="p108323810306"></a><a name="p108323810306"></a>Identity and Access Management (IAM)</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1683212816304"><a name="p1683212816304"></a><a name="p1683212816304"></a><a href="accessing-sfs.md#section9612155718233">User Permission</a></p>
</td>
</tr>
<tr id="row136795523343"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p176809522349"><a name="p176809522349"></a><a name="p176809522349"></a>The encryption feature relies on KMS, which improves the data security of your file systems.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p109717561126"><a name="p109717561126"></a><a name="p109717561126"></a>Key Management Service (KMS)</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p145621347194815"><a name="p145621347194815"></a><a name="p145621347194815"></a><a href="encryption.md">Encryption</a></p>
</td>
</tr>
<tr id="row18433410123617"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1343314109360"><a name="p1343314109360"></a><a name="p1343314109360"></a>Once you have subscribed to SFS, you can monitor its performance, such as the read bandwidth, write bandwidth, and read write bandwidth on Cloud Eye, which does not require any plug-ins.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1143341015367"><a name="p1143341015367"></a><a name="p1143341015367"></a>Cloud Eye</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1714414410489"><a name="p1714414410489"></a><a name="p1714414410489"></a><a href="monitoring.md">Monitoring</a></p>
</td>
</tr>
<tr id="row20343193813812"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p434319386385"><a name="p434319386385"></a><a name="p434319386385"></a>Cloud Trace Service (CTS) allows you to collect, store, and query cloud resource operation records and use these records for security analysis, compliance auditing, resource tracking, and fault locating. With CTS, you can record operations associated with SFS for later query, audit, and backtrack operations.</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p734383813389"><a name="p734383813389"></a><a name="p734383813389"></a>Cloud Trace Service (CTS)</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p9147101334614"><a name="p9147101334614"></a><a name="p9147101334614"></a><a href="auditing.md">Auditing</a></p>
</td>
</tr>
</tbody>
</table>

