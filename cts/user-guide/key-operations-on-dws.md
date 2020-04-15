# Key Operations on DWS<a name="en-us_topic_0100498013"></a>

Data Warehouse Service \(DWS\) is an online data processing database based on the public cloud infrastructure and platform and helps you mine and analyze massive data.

With CTS, you can record operations associated with DWS for later query, audit, and backtrack operations.

**Table  1**  DWS operations that can be recorded by CTS

<a name="table2699372817247"></a>
<table><thead align="left"><tr id="r94b2224cbb874ab2b152420a0b99dee7"><th class="cellrowborder" valign="top" width="25.979999999999997%" id="mcps1.2.4.1.1"><p id="af01beb31c55145688ea6b56e46087b4c"><a name="af01beb31c55145688ea6b56e46087b4c"></a><a name="af01beb31c55145688ea6b56e46087b4c"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="31.78%" id="mcps1.2.4.1.2"><p id="a62371c2215174704afd82be218684600"><a name="a62371c2215174704afd82be218684600"></a><a name="a62371c2215174704afd82be218684600"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.24%" id="mcps1.2.4.1.3"><p id="a1dd017279f50480e92eed61a66a566e7"><a name="a1dd017279f50480e92eed61a66a566e7"></a><a name="a1dd017279f50480e92eed61a66a566e7"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r82303cceb3ae499ab6ca5030177ed952"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240321_p584824081742"><a name="en-us_topic_0100240321_p584824081742"></a><a name="en-us_topic_0100240321_p584824081742"></a>Creating/Restoring a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="a0bd03ee53f6e4bfbad34355634541cae"><a name="a0bd03ee53f6e4bfbad34355634541cae"></a><a name="a0bd03ee53f6e4bfbad34355634541cae"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="a5f6ce4e4a0ed468e902640b0dc566ee0"><a name="a5f6ce4e4a0ed468e902640b0dc566ee0"></a><a name="a5f6ce4e4a0ed468e902640b0dc566ee0"></a>createCluster</p>
</td>
</tr>
<tr id="r1ae67a11201b454ba4fd952b99c66f82"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240321_p195474191742"><a name="en-us_topic_0100240321_p195474191742"></a><a name="en-us_topic_0100240321_p195474191742"></a>Deleting a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="ac4cdb0005b8546038a64741ae435c446"><a name="ac4cdb0005b8546038a64741ae435c446"></a><a name="ac4cdb0005b8546038a64741ae435c446"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="a3b89f318558241799af5648438c5ecb1"><a name="a3b89f318558241799af5648438c5ecb1"></a><a name="a3b89f318558241799af5648438c5ecb1"></a>deleteCluster</p>
</td>
</tr>
<tr id="rf41f5f62f4b849978630faae90caf2d9"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240321_p229899451742"><a name="en-us_topic_0100240321_p229899451742"></a><a name="en-us_topic_0100240321_p229899451742"></a>Expanding cluster capacity</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="a4236732cb0e04bfbbcdb180bc03e5121"><a name="a4236732cb0e04bfbbcdb180bc03e5121"></a><a name="a4236732cb0e04bfbbcdb180bc03e5121"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="aed33e321ca054a0aaa21614427dc334c"><a name="aed33e321ca054a0aaa21614427dc334c"></a><a name="aed33e321ca054a0aaa21614427dc334c"></a>growCluster</p>
</td>
</tr>
<tr id="r0d7937fdbb514297968410a3ac60c87d"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240321_p495628271742"><a name="en-us_topic_0100240321_p495628271742"></a><a name="en-us_topic_0100240321_p495628271742"></a>Restarting a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="a0c3ab4fc804941dd9b819bdf5b9917fb"><a name="a0c3ab4fc804941dd9b819bdf5b9917fb"></a><a name="a0c3ab4fc804941dd9b819bdf5b9917fb"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="a2b75ad4beabb4a119fcfd49e1ef5b929"><a name="a2b75ad4beabb4a119fcfd49e1ef5b929"></a><a name="a2b75ad4beabb4a119fcfd49e1ef5b929"></a>rebootCluster</p>
</td>
</tr>
<tr id="r350a3a8e23a645668a02230a828a46d0"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240321_p267323251742"><a name="en-us_topic_0100240321_p267323251742"></a><a name="en-us_topic_0100240321_p267323251742"></a>Creating a snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240321_p205290217417"><a name="en-us_topic_0100240321_p205290217417"></a><a name="en-us_topic_0100240321_p205290217417"></a>backup</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="a221b491a9a12412e9391cb52182877bf"><a name="a221b491a9a12412e9391cb52182877bf"></a><a name="a221b491a9a12412e9391cb52182877bf"></a>createBackup</p>
</td>
</tr>
<tr id="r0c932cbe4118453881a780f7a5a02a84"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240321_p262949471742"><a name="en-us_topic_0100240321_p262949471742"></a><a name="en-us_topic_0100240321_p262949471742"></a>Deleting a snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="a46fa36fc507f4e15bb30cd2a13887948"><a name="a46fa36fc507f4e15bb30cd2a13887948"></a><a name="a46fa36fc507f4e15bb30cd2a13887948"></a>backup</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="a50d42deec95c4442a6f81ac9c318be7a"><a name="a50d42deec95c4442a6f81ac9c318be7a"></a><a name="a50d42deec95c4442a6f81ac9c318be7a"></a>deleteBackup</p>
</td>
</tr>
<tr id="r1063b0bdafb9421eb31aaee0b796ccf5"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240321_p429903751742"><a name="en-us_topic_0100240321_p429903751742"></a><a name="en-us_topic_0100240321_p429903751742"></a>Setting security parameters</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240321_p764854317417"><a name="en-us_topic_0100240321_p764854317417"></a><a name="en-us_topic_0100240321_p764854317417"></a>configurations</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="a9bf99c0ca6d24d47a3c7bc8ef55865ec"><a name="a9bf99c0ca6d24d47a3c7bc8ef55865ec"></a><a name="a9bf99c0ca6d24d47a3c7bc8ef55865ec"></a>updateConfigurations</p>
</td>
</tr>
<tr id="r7c6d992c6ded4dcbaacb6bfdb8125f7e"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240321_p1438991742"><a name="en-us_topic_0100240321_p1438991742"></a><a name="en-us_topic_0100240321_p1438991742"></a>Creating an MRS data source</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240321_p575251217417"><a name="en-us_topic_0100240321_p575251217417"></a><a name="en-us_topic_0100240321_p575251217417"></a>dataSource</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="a5977318a17754b7eb318bf5e2510e98a"><a name="a5977318a17754b7eb318bf5e2510e98a"></a><a name="a5977318a17754b7eb318bf5e2510e98a"></a>createExtDataSource</p>
</td>
</tr>
<tr id="r1a68c4c6d2934d938fbfd0608460f32f"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240321_p414232791742"><a name="en-us_topic_0100240321_p414232791742"></a><a name="en-us_topic_0100240321_p414232791742"></a>Deleting an MRS data source</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="a5f9e4b4e08684548b6b64da3a12e9a52"><a name="a5f9e4b4e08684548b6b64da3a12e9a52"></a><a name="a5f9e4b4e08684548b6b64da3a12e9a52"></a>dataSource</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240321_p79345617428"><a name="en-us_topic_0100240321_p79345617428"></a><a name="en-us_topic_0100240321_p79345617428"></a>deleteExtDataSource</p>
</td>
</tr>
<tr id="r801b61bf8ce34a519633412b57924335"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240321_p193645421742"><a name="en-us_topic_0100240321_p193645421742"></a><a name="en-us_topic_0100240321_p193645421742"></a>Updating an MRS data source</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="a9e6ed60dcb564395a2725fa32fca5f75"><a name="a9e6ed60dcb564395a2725fa32fca5f75"></a><a name="a9e6ed60dcb564395a2725fa32fca5f75"></a>dataSource</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="a41f24fef3b274c65855bc9752f1e3244"><a name="a41f24fef3b274c65855bc9752f1e3244"></a><a name="a41f24fef3b274c65855bc9752f1e3244"></a>updateExtDataSource</p>
</td>
</tr>
</tbody>
</table>

