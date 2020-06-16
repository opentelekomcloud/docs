# Default Users of Clusters with Kerberos Authentication Enabled<a name="EN-US_TOPIC_0221415053"></a>

## User Classification<a name="en-us_topic_0173178308_s6938c8b3b12d4493b56cb27c41fb2313"></a>

The MRS cluster provides the following three types of users. Users are required to periodically change their passwords. It is not recommended to use the default passwords.

<a name="en-us_topic_0173178308_te04570f84a8c4401a30e67359a9f6ef6"></a>
<table><thead align="left"><tr id="en-us_topic_0173178308_en-us_topic_0039905375_row1711617395159"><th class="cellrowborder" valign="top" width="21.5%" id="mcps1.1.3.1.1"><p id="en-us_topic_0173178308_acd42a1f7bb434508bc9c100b4a0f2049"><a name="en-us_topic_0173178308_acd42a1f7bb434508bc9c100b4a0f2049"></a><a name="en-us_topic_0173178308_acd42a1f7bb434508bc9c100b4a0f2049"></a>User Type</p>
</th>
<th class="cellrowborder" valign="top" width="78.5%" id="mcps1.1.3.1.2"><p id="en-us_topic_0173178308_a73f9735c2df340b2b3849dcad936de40"><a name="en-us_topic_0173178308_a73f9735c2df340b2b3849dcad936de40"></a><a name="en-us_topic_0173178308_a73f9735c2df340b2b3849dcad936de40"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0173178308_en-us_topic_0039905375_row2920896895159"><td class="cellrowborder" valign="top" width="21.5%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_en-us_topic_0039905375_p337902391436"><a name="en-us_topic_0173178308_en-us_topic_0039905375_p337902391436"></a><a name="en-us_topic_0173178308_en-us_topic_0039905375_p337902391436"></a>System user</p>
</td>
<td class="cellrowborder" valign="top" width="78.5%" headers="mcps1.1.3.1.2 "><a name="en-us_topic_0173178308_ub0050ca23d18471cb448f799f1ba6bc7"></a><a name="en-us_topic_0173178308_ub0050ca23d18471cb448f799f1ba6bc7"></a><ul id="en-us_topic_0173178308_ub0050ca23d18471cb448f799f1ba6bc7"><li>A user created on MRS Manager for MRS cluster O&amp;M and service scenarios. There are two types of users:<a name="en-us_topic_0173178308_ubb35dcd0d22c4433aab07175bfa9f39d"></a><a name="en-us_topic_0173178308_ubb35dcd0d22c4433aab07175bfa9f39d"></a><ul id="en-us_topic_0173178308_ubb35dcd0d22c4433aab07175bfa9f39d"><li><span class="parmname" id="en-us_topic_0173178308_en-us_topic_0039905375_parmname15793536111923"><a name="en-us_topic_0173178308_en-us_topic_0039905375_parmname15793536111923"></a><a name="en-us_topic_0173178308_en-us_topic_0039905375_parmname15793536111923"></a><b>Human-machine</b></span> user: used for MRS Manager O&amp;M scenarios and component client operation scenarios.</li><li><span class="parmname" id="en-us_topic_0173178308_en-us_topic_0039905375_parmname777481111955"><a name="en-us_topic_0173178308_en-us_topic_0039905375_parmname777481111955"></a><a name="en-us_topic_0173178308_en-us_topic_0039905375_parmname777481111955"></a><b>Machine-machine</b></span> user: used for MRS cluster application development scenarios.</li></ul>
</li><li>A user used to run OMS system processes.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row3350078495159"><td class="cellrowborder" valign="top" width="21.5%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_a4af0f57c3b5448c3b8374321986d0a37"><a name="en-us_topic_0173178308_a4af0f57c3b5448c3b8374321986d0a37"></a><a name="en-us_topic_0173178308_a4af0f57c3b5448c3b8374321986d0a37"></a>Internal system user</p>
</td>
<td class="cellrowborder" valign="top" width="78.5%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_a516e3292d2984c70a638aa1dc13383c3"><a name="en-us_topic_0173178308_a516e3292d2984c70a638aa1dc13383c3"></a><a name="en-us_topic_0173178308_a516e3292d2984c70a638aa1dc13383c3"></a>An internal user provided by the MRS cluster and used to implement communication between processes, save user group information, and associate user rights.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row2029769795159"><td class="cellrowborder" valign="top" width="21.5%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_adf39dd76e0604fe7a64368a4457e4c15"><a name="en-us_topic_0173178308_adf39dd76e0604fe7a64368a4457e4c15"></a><a name="en-us_topic_0173178308_adf39dd76e0604fe7a64368a4457e4c15"></a>Database user</p>
</td>
<td class="cellrowborder" valign="top" width="78.5%" headers="mcps1.1.3.1.2 "><a name="en-us_topic_0173178308_u858bd206e90145b3851384ba2c0cacdb"></a><a name="en-us_topic_0173178308_u858bd206e90145b3851384ba2c0cacdb"></a><ul id="en-us_topic_0173178308_u858bd206e90145b3851384ba2c0cacdb"><li>A user used to manage the OMS database and access data.</li><li>A user used to run the database of service components (Hive, Hue, <span id="en-us_topic_0173178308_ph9449175413245"><a name="en-us_topic_0173178308_ph9449175413245"></a><a name="en-us_topic_0173178308_ph9449175413245"></a>Loader</span> and DBService).</li></ul>
</td>
</tr>
</tbody>
</table>

## System Users<a name="en-us_topic_0173178308_sab2bd13717334d708e5478e08ed5e616"></a>

>![](/images/icon-note.gif) **NOTE:**   
>-   User  **ldap**  of the OS is required in the MRS cluster. Do not delete the account. Otherwise, the cluster may not work properly. Password management policies are maintained by the users.  
>-   Reset the password when you change the passwords of user  **ommdba** and user **omm**  for the first time. Change the passwords regularly after you have retrieved them.  

<a name="en-us_topic_0173178308_t6b8aac53ebdc49efaacdbccaaa559ab1"></a>
<table><thead align="left"><tr id="en-us_topic_0173178308_en-us_topic_0039905375_row4683794795430"><th class="cellrowborder" valign="top" width="21.0978902109789%" id="mcps1.1.5.1.1"><p id="en-us_topic_0173178308_en-us_topic_0039905375_p602860391613"><a name="en-us_topic_0173178308_en-us_topic_0039905375_p602860391613"></a><a name="en-us_topic_0173178308_en-us_topic_0039905375_p602860391613"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="21.0978902109789%" id="mcps1.1.5.1.2"><p id="en-us_topic_0173178308_acf9704788cec41d597b2465e4ee1d962"><a name="en-us_topic_0173178308_acf9704788cec41d597b2465e4ee1d962"></a><a name="en-us_topic_0173178308_acf9704788cec41d597b2465e4ee1d962"></a>Username</p>
</th>
<th class="cellrowborder" valign="top" width="20.88791120887911%" id="mcps1.1.5.1.3"><p id="en-us_topic_0173178308_acb498f43480549f3acfcb7877d910ead"><a name="en-us_topic_0173178308_acb498f43480549f3acfcb7877d910ead"></a><a name="en-us_topic_0173178308_acb498f43480549f3acfcb7877d910ead"></a>Initial Password</p>
</th>
<th class="cellrowborder" valign="top" width="36.91630836916308%" id="mcps1.1.5.1.4"><p id="en-us_topic_0173178308_a3255af176f334fc0a4eeba52971ae5c6"><a name="en-us_topic_0173178308_a3255af176f334fc0a4eeba52971ae5c6"></a><a name="en-us_topic_0173178308_a3255af176f334fc0a4eeba52971ae5c6"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0173178308_en-us_topic_0039905375_row67033319112132"><td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0173178308_aebf20281e7f141e8a6e9b241bd837e14"><a name="en-us_topic_0173178308_aebf20281e7f141e8a6e9b241bd837e14"></a><a name="en-us_topic_0173178308_aebf20281e7f141e8a6e9b241bd837e14"></a>MRS cluster system user</p>
</td>
<td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0173178308_af3894562851b4654b850205d85e99843"><a name="en-us_topic_0173178308_af3894562851b4654b850205d85e99843"></a><a name="en-us_topic_0173178308_af3894562851b4654b850205d85e99843"></a>admin</p>
</td>
<td class="cellrowborder" valign="top" width="20.88791120887911%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0173178308_a0aef5a6c9b1a4904813222a438e79a84"><a name="en-us_topic_0173178308_a0aef5a6c9b1a4904813222a438e79a84"></a><a name="en-us_topic_0173178308_a0aef5a6c9b1a4904813222a438e79a84"></a>Specified by the user when the cluster is created</p>
</td>
<td class="cellrowborder" valign="top" width="36.91630836916308%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0173178308_acdb5db3097f5437d91aa2b56029c5646"><a name="en-us_topic_0173178308_acdb5db3097f5437d91aa2b56029c5646"></a><a name="en-us_topic_0173178308_acdb5db3097f5437d91aa2b56029c5646"></a>Administrator of MRS Manager.</p>
<p id="en-us_topic_0173178308_p2240466591526"><a name="en-us_topic_0173178308_p2240466591526"></a><a name="en-us_topic_0173178308_p2240466591526"></a>This user also has the following rights:</p>
<a name="en-us_topic_0173178308_ul77702491530"></a><a name="en-us_topic_0173178308_ul77702491530"></a><ul id="en-us_topic_0173178308_ul77702491530"><li>Common HDFS and ZooKeeper user rights.</li><li>Rights to submit and query MapReduce and Yarn tasks, to manage Yarn queues, and to access the Yarn web UI.</li><li>Rights to submit, query, activate, deactivate, reassign, delete topologies, and operate all topologies of the Storm service.</li><li>Rights to create, delete, authenticate, reassign, consume, write, and query topics of the Kafka service.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row4237456195430"><td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0173178308_ab1bf70004a404b60a7ed9294b2909244"><a name="en-us_topic_0173178308_ab1bf70004a404b60a7ed9294b2909244"></a><a name="en-us_topic_0173178308_ab1bf70004a404b60a7ed9294b2909244"></a>MRS cluster node OS user</p>
</td>
<td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0173178308_p10684945121110"><a name="en-us_topic_0173178308_p10684945121110"></a><a name="en-us_topic_0173178308_p10684945121110"></a>omm</p>
</td>
<td class="cellrowborder" valign="top" width="20.88791120887911%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0173178308_p068494517111"><a name="en-us_topic_0173178308_p068494517111"></a><a name="en-us_topic_0173178308_p068494517111"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" width="36.91630836916308%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0173178308_p8684945131112"><a name="en-us_topic_0173178308_p8684945131112"></a><a name="en-us_topic_0173178308_p8684945131112"></a>Internal running user of the MRS cluster system. This user is an OS user generated on all nodes and does not require a unified password.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row6856757104728"><td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0173178308_p1190851873618"><a name="en-us_topic_0173178308_p1190851873618"></a><a name="en-us_topic_0173178308_p1190851873618"></a>MRS cluster node OS user</p>
</td>
<td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0173178308_p11908518153613"><a name="en-us_topic_0173178308_p11908518153613"></a><a name="en-us_topic_0173178308_p11908518153613"></a>root</p>
</td>
<td class="cellrowborder" valign="top" width="20.88791120887911%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0173178308_p290881820369"><a name="en-us_topic_0173178308_p290881820369"></a><a name="en-us_topic_0173178308_p290881820369"></a>Password set by the user</p>
</td>
<td class="cellrowborder" valign="top" width="36.91630836916308%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0173178308_p390861893616"><a name="en-us_topic_0173178308_p390861893616"></a><a name="en-us_topic_0173178308_p390861893616"></a>User used to log in to a node in the MRS cluster. This user is an OS user generated on all nodes.</p>
</td>
</tr>
</tbody>
</table>

## Internal System Users<a name="en-us_topic_0173178308_s7014b4bc5b1f49d1aaa0ba7dfc3e4e8b"></a>

>![](/images/icon-note.gif) **NOTE:**   
>Do not delete the following internal system users. Otherwise, the cluster or services may not work properly.  

<a name="en-us_topic_0173178308_t7c6eb02b0e9a47bf8c2beef04898f21c"></a>
<table><thead align="left"><tr id="en-us_topic_0173178308_en-us_topic_0039905375_row5525661591813"><th class="cellrowborder" valign="top" width="20.47%" id="mcps1.1.5.1.1"><p id="en-us_topic_0173178308_a86ef5120d8a4405e9256272dadfecd0f"><a name="en-us_topic_0173178308_a86ef5120d8a4405e9256272dadfecd0f"></a><a name="en-us_topic_0173178308_a86ef5120d8a4405e9256272dadfecd0f"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25.729999999999997%" id="mcps1.1.5.1.2"><p id="en-us_topic_0173178308_a1a3b31f329cc41c89d5baa4d2a9087e2"><a name="en-us_topic_0173178308_a1a3b31f329cc41c89d5baa4d2a9087e2"></a><a name="en-us_topic_0173178308_a1a3b31f329cc41c89d5baa4d2a9087e2"></a>Default User</p>
</th>
<th class="cellrowborder" valign="top" width="14.580000000000002%" id="mcps1.1.5.1.3"><p id="en-us_topic_0173178308_a775ea3b21c2d460a8877d30a8861b132"><a name="en-us_topic_0173178308_a775ea3b21c2d460a8877d30a8861b132"></a><a name="en-us_topic_0173178308_a775ea3b21c2d460a8877d30a8861b132"></a>Initial Password</p>
</th>
<th class="cellrowborder" valign="top" width="39.22%" id="mcps1.1.5.1.4"><p id="en-us_topic_0173178308_ac9a80b80fc7949d289ca25cbc3e44fe4"><a name="en-us_topic_0173178308_ac9a80b80fc7949d289ca25cbc3e44fe4"></a><a name="en-us_topic_0173178308_ac9a80b80fc7949d289ca25cbc3e44fe4"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0173178308_en-us_topic_0039905375_row4296949792445"><td class="cellrowborder" rowspan="4" valign="top" width="20.47%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0173178308_a09e79d22f72a42f8a2e16c4f839495c0"><a name="en-us_topic_0173178308_a09e79d22f72a42f8a2e16c4f839495c0"></a><a name="en-us_topic_0173178308_a09e79d22f72a42f8a2e16c4f839495c0"></a>Component running user</p>
</td>
<td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0173178308_a3ca0a44fd3094cfd9e7fa5e86feb687f"><a name="en-us_topic_0173178308_a3ca0a44fd3094cfd9e7fa5e86feb687f"></a><a name="en-us_topic_0173178308_a3ca0a44fd3094cfd9e7fa5e86feb687f"></a>hdfs</p>
</td>
<td class="cellrowborder" valign="top" width="14.580000000000002%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0173178308_abc2adb66b75b4ea2826036644fe86a81"><a name="en-us_topic_0173178308_abc2adb66b75b4ea2826036644fe86a81"></a><a name="en-us_topic_0173178308_abc2adb66b75b4ea2826036644fe86a81"></a>Hdfs@123</p>
</td>
<td class="cellrowborder" valign="top" width="39.22%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0173178308_abd7b74694f87487bb9e5f3eb750e2cc1"><a name="en-us_topic_0173178308_abd7b74694f87487bb9e5f3eb750e2cc1"></a><a name="en-us_topic_0173178308_abd7b74694f87487bb9e5f3eb750e2cc1"></a>HDFS system administrator who has the following permission:</p>
<a name="en-us_topic_0173178308_en-us_topic_0039905375_ol6185503710221"></a><a name="en-us_topic_0173178308_en-us_topic_0039905375_ol6185503710221"></a><ol id="en-us_topic_0173178308_en-us_topic_0039905375_ol6185503710221"><li>File system operation permission:<a name="en-us_topic_0173178308_u46279b3930304aa1a6200485750f4fc2"></a><a name="en-us_topic_0173178308_u46279b3930304aa1a6200485750f4fc2"></a><ul id="en-us_topic_0173178308_u46279b3930304aa1a6200485750f4fc2"><li>Views, modifies, and creates files.</li><li>Views and creates directories.</li><li>Views and modifies the groups where files belong.</li><li>Views and sets disk quotas of users</li></ul>
</li></ol>
<a name="en-us_topic_0173178308_en-us_topic_0039905375_ol4340515210230"></a><a name="en-us_topic_0173178308_en-us_topic_0039905375_ol4340515210230"></a><ol id="en-us_topic_0173178308_en-us_topic_0039905375_ol4340515210230"><li>HDFS management operation permission:<a name="en-us_topic_0173178308_u6c8113c615bc4eecb120e777123b9465"></a><a name="en-us_topic_0173178308_u6c8113c615bc4eecb120e777123b9465"></a><ul id="en-us_topic_0173178308_u6c8113c615bc4eecb120e777123b9465"><li>Views the web UI status.</li><li>Views and sets the active and standby HDFS status.</li><li>Enters and exits HDFS in security mode.</li><li>Checks HDFS.</li></ul>
</li></ol>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row787279192452"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0173178308_aa8791baf97e449bcab3cce09f17406ab"><a name="en-us_topic_0173178308_aa8791baf97e449bcab3cce09f17406ab"></a><a name="en-us_topic_0173178308_aa8791baf97e449bcab3cce09f17406ab"></a>hbase</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0173178308_a712c0d0dfb284096be1a944ef8183d03"><a name="en-us_topic_0173178308_a712c0d0dfb284096be1a944ef8183d03"></a><a name="en-us_topic_0173178308_a712c0d0dfb284096be1a944ef8183d03"></a>Hbase@123</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0173178308_a48226f3ff818428eab07b2c05c723b90"><a name="en-us_topic_0173178308_a48226f3ff818428eab07b2c05c723b90"></a><a name="en-us_topic_0173178308_a48226f3ff818428eab07b2c05c723b90"></a>HBase system administrator who has the following permission:</p>
<a name="en-us_topic_0173178308_ud1d77e5225744d7290262fa790d3f191"></a><a name="en-us_topic_0173178308_ud1d77e5225744d7290262fa790d3f191"></a><ul id="en-us_topic_0173178308_ud1d77e5225744d7290262fa790d3f191"><li>Cluster management permission: Enables and disables tables, and triggers MajorCompact and Access Control List (ACL).</li><li>Grants and reclaims permission, and shuts down the cluster.</li><li>Table management permission: Creates, modifies, and deletes tables.</li><li>Data management permission: Reads and writes table-, column family-, and column-level data.</li><li>Accesses the HBase web UI.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row1720200792452"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0173178308_a80f1f3b9b14a4983ab75bffb7bd041e2"><a name="en-us_topic_0173178308_a80f1f3b9b14a4983ab75bffb7bd041e2"></a><a name="en-us_topic_0173178308_a80f1f3b9b14a4983ab75bffb7bd041e2"></a>mapred</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0173178308_a6e3f65103daa460f9f38e0110172df42"><a name="en-us_topic_0173178308_a6e3f65103daa460f9f38e0110172df42"></a><a name="en-us_topic_0173178308_a6e3f65103daa460f9f38e0110172df42"></a>Mapred@123</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0173178308_aef97b376d6654246bb03fb5f569d3b00"><a name="en-us_topic_0173178308_aef97b376d6654246bb03fb5f569d3b00"></a><a name="en-us_topic_0173178308_aef97b376d6654246bb03fb5f569d3b00"></a>MapReduce system administrator who has the following permission:</p>
<a name="en-us_topic_0173178308_ufb9017f24be64ef5b60f0e9e909db2c1"></a><a name="en-us_topic_0173178308_ufb9017f24be64ef5b60f0e9e909db2c1"></a><ul id="en-us_topic_0173178308_ufb9017f24be64ef5b60f0e9e909db2c1"><li>Submits, stops, and views MapReduce tasks.</li><li>Modifies the Yarn configuration parameters.</li><li>Accesses the Yarn and MapReduce web UIs.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row4184534392452"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0173178308_a6adaae55d083493abb17382b33a32a39"><a name="en-us_topic_0173178308_a6adaae55d083493abb17382b33a32a39"></a><a name="en-us_topic_0173178308_a6adaae55d083493abb17382b33a32a39"></a>spark</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0173178308_a949806e96af84e31af4f35172bd2d52f"><a name="en-us_topic_0173178308_a949806e96af84e31af4f35172bd2d52f"></a><a name="en-us_topic_0173178308_a949806e96af84e31af4f35172bd2d52f"></a>Spark@123</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0173178308_a60bae9783a194e7ab6102c49521576fd"><a name="en-us_topic_0173178308_a60bae9783a194e7ab6102c49521576fd"></a><a name="en-us_topic_0173178308_a60bae9783a194e7ab6102c49521576fd"></a>Spark system administrator who has the following permission:</p>
<a name="en-us_topic_0173178308_u0c233dae119d4b428a85424b1496dc6e"></a><a name="en-us_topic_0173178308_u0c233dae119d4b428a85424b1496dc6e"></a><ul id="en-us_topic_0173178308_u0c233dae119d4b428a85424b1496dc6e"><li>Accesses the Spark web UI.</li><li>Submits Spark tasks.</li></ul>
</td>
</tr>
</tbody>
</table>

## User Group Information<a name="en-us_topic_0173178308_s7e903a7017034fb28fc5ce90846c9111"></a>

<a name="en-us_topic_0173178308_t2b63afe6ad6d4687b5cbcd106db57a53"></a>
<table><thead align="left"><tr id="en-us_topic_0173178308_en-us_topic_0039905375_row2146537095542"><th class="cellrowborder" valign="top" width="35%" id="mcps1.1.3.1.1"><p id="en-us_topic_0173178308_afb8b3a42df9d46f4ac70366e65a8099b"><a name="en-us_topic_0173178308_afb8b3a42df9d46f4ac70366e65a8099b"></a><a name="en-us_topic_0173178308_afb8b3a42df9d46f4ac70366e65a8099b"></a>Default User Group</p>
</th>
<th class="cellrowborder" valign="top" width="65%" id="mcps1.1.3.1.2"><p id="en-us_topic_0173178308_a4188a9c106b843d6b480c4e0e3ec9e7d"><a name="en-us_topic_0173178308_a4188a9c106b843d6b480c4e0e3ec9e7d"></a><a name="en-us_topic_0173178308_a4188a9c106b843d6b480c4e0e3ec9e7d"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0173178308_en-us_topic_0039905375_row2173685595542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_a7feff961662e4ff4989046eeef9d9ed7"><a name="en-us_topic_0173178308_a7feff961662e4ff4989046eeef9d9ed7"></a><a name="en-us_topic_0173178308_a7feff961662e4ff4989046eeef9d9ed7"></a>hadoop</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_adabbf87da93044249cf2b5b7261265b9"><a name="en-us_topic_0173178308_adabbf87da93044249cf2b5b7261265b9"></a><a name="en-us_topic_0173178308_adabbf87da93044249cf2b5b7261265b9"></a>Users added to this user group have the permission to submit tasks to all Yarn queues.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row1645580095542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_a84235225147c476182e5e1a812d8d6d7"><a name="en-us_topic_0173178308_a84235225147c476182e5e1a812d8d6d7"></a><a name="en-us_topic_0173178308_a84235225147c476182e5e1a812d8d6d7"></a>hbase</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_a43a9611866f64cf9869ddc7666481179"><a name="en-us_topic_0173178308_a43a9611866f64cf9869ddc7666481179"></a><a name="en-us_topic_0173178308_a43a9611866f64cf9869ddc7666481179"></a>Common user group. Users added to this user group will not have any additional rights.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row3291757595542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_a5b44543ef01e408fb9524e98d7e71fca"><a name="en-us_topic_0173178308_a5b44543ef01e408fb9524e98d7e71fca"></a><a name="en-us_topic_0173178308_a5b44543ef01e408fb9524e98d7e71fca"></a>hive</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_aa8b6b17fcf524472a9e2ff43f3386191"><a name="en-us_topic_0173178308_aa8b6b17fcf524472a9e2ff43f3386191"></a><a name="en-us_topic_0173178308_aa8b6b17fcf524472a9e2ff43f3386191"></a>Users added to this user group can use Hive.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row4709299695542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_a940844d173984a988e3f0d2a4b866081"><a name="en-us_topic_0173178308_a940844d173984a988e3f0d2a4b866081"></a><a name="en-us_topic_0173178308_a940844d173984a988e3f0d2a4b866081"></a>spark</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_a9d3cff5becbb4e2b82c43c5100c3e62b"><a name="en-us_topic_0173178308_a9d3cff5becbb4e2b82c43c5100c3e62b"></a><a name="en-us_topic_0173178308_a9d3cff5becbb4e2b82c43c5100c3e62b"></a>Common user group. Users added to this user group will not have any additional rights.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row4974878695542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_a15ca38ced204424b9d952ea0ffa355c4"><a name="en-us_topic_0173178308_a15ca38ced204424b9d952ea0ffa355c4"></a><a name="en-us_topic_0173178308_a15ca38ced204424b9d952ea0ffa355c4"></a>supergroup</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_en-us_topic_0039905375_p484018194426"><a name="en-us_topic_0173178308_en-us_topic_0039905375_p484018194426"></a><a name="en-us_topic_0173178308_en-us_topic_0039905375_p484018194426"></a>Users added to this user group can have the administrator rights of HBase, HDFS, and Yarn and can use Hive.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row4187683195542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_a939aa842190f4015a9f42db701576a75"><a name="en-us_topic_0173178308_a939aa842190f4015a9f42db701576a75"></a><a name="en-us_topic_0173178308_a939aa842190f4015a9f42db701576a75"></a>check_sec_ldap</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_a69f3a09d45d840d89c8d43068d542d69"><a name="en-us_topic_0173178308_a69f3a09d45d840d89c8d43068d542d69"></a><a name="en-us_topic_0173178308_a69f3a09d45d840d89c8d43068d542d69"></a>Used to test whether the active LDAP works properly. This user group is generated randomly in a test and automatically deleted after the test is complete. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row6202335295542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_a27573a850cf64afdabaca4d01d97705a"><a name="en-us_topic_0173178308_a27573a850cf64afdabaca4d01d97705a"></a><a name="en-us_topic_0173178308_a27573a850cf64afdabaca4d01d97705a"></a>Manager_tenant</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_a1a87b6544fd440db8129b6bea7fe8870"><a name="en-us_topic_0173178308_a1a87b6544fd440db8129b6bea7fe8870"></a><a name="en-us_topic_0173178308_a1a87b6544fd440db8129b6bea7fe8870"></a>Tenant system user group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row5098181595542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_a6b9ce7f67dcf401dae2f456c8ab4ce0d"><a name="en-us_topic_0173178308_a6b9ce7f67dcf401dae2f456c8ab4ce0d"></a><a name="en-us_topic_0173178308_a6b9ce7f67dcf401dae2f456c8ab4ce0d"></a>System_administrator</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_a2e05f9bef0e64d9a8ded665d82f800b1"><a name="en-us_topic_0173178308_a2e05f9bef0e64d9a8ded665d82f800b1"></a><a name="en-us_topic_0173178308_a2e05f9bef0e64d9a8ded665d82f800b1"></a>MRS cluster system administrator group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row5038033795542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_en-us_topic_0039905375_p330046794426"><a name="en-us_topic_0173178308_en-us_topic_0039905375_p330046794426"></a><a name="en-us_topic_0173178308_en-us_topic_0039905375_p330046794426"></a>Manager_viewer</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_a92b846c06539489e9d5c02a8660cae75"><a name="en-us_topic_0173178308_a92b846c06539489e9d5c02a8660cae75"></a><a name="en-us_topic_0173178308_a92b846c06539489e9d5c02a8660cae75"></a>MRS Manager system viewer group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row1988690795542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_a882453dde6404e2aa7b7204c2d6d22ec"><a name="en-us_topic_0173178308_a882453dde6404e2aa7b7204c2d6d22ec"></a><a name="en-us_topic_0173178308_a882453dde6404e2aa7b7204c2d6d22ec"></a>Manager_operator</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_a6d816c93930f42b6a5ff51de06e705e3"><a name="en-us_topic_0173178308_a6d816c93930f42b6a5ff51de06e705e3"></a><a name="en-us_topic_0173178308_a6d816c93930f42b6a5ff51de06e705e3"></a>MRS Manager system operator group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row2173111295542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_a65a50708a57848f48a50365be49a4a68"><a name="en-us_topic_0173178308_a65a50708a57848f48a50365be49a4a68"></a><a name="en-us_topic_0173178308_a65a50708a57848f48a50365be49a4a68"></a>Manager_auditor</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_ab1e5ffa592e94d5db2e5fdb5c07ba24d"><a name="en-us_topic_0173178308_ab1e5ffa592e94d5db2e5fdb5c07ba24d"></a><a name="en-us_topic_0173178308_ab1e5ffa592e94d5db2e5fdb5c07ba24d"></a>MRS Manager system auditor group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row881498995542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_abd8593eb855744a09df892c87cecc5aa"><a name="en-us_topic_0173178308_abd8593eb855744a09df892c87cecc5aa"></a><a name="en-us_topic_0173178308_abd8593eb855744a09df892c87cecc5aa"></a>Manager_administrator</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_a05348c51b79943fd852cf4a898f55be7"><a name="en-us_topic_0173178308_a05348c51b79943fd852cf4a898f55be7"></a><a name="en-us_topic_0173178308_a05348c51b79943fd852cf4a898f55be7"></a>MRS Manager system administrator group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row4400159695542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_a1cf1bfb8f82a42e98073c8ffbc3bc71f"><a name="en-us_topic_0173178308_a1cf1bfb8f82a42e98073c8ffbc3bc71f"></a><a name="en-us_topic_0173178308_a1cf1bfb8f82a42e98073c8ffbc3bc71f"></a>compcommon</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_ad6654265ef634bdfa1f59be322789ceb"><a name="en-us_topic_0173178308_ad6654265ef634bdfa1f59be322789ceb"></a><a name="en-us_topic_0173178308_ad6654265ef634bdfa1f59be322789ceb"></a>MRS cluster internal group for accessing public cluster resources. All system users and system running users are added to this user group by default.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row2075655595542"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_ae834a92432b4495e87ed8afe26382e62"><a name="en-us_topic_0173178308_ae834a92432b4495e87ed8afe26382e62"></a><a name="en-us_topic_0173178308_ae834a92432b4495e87ed8afe26382e62"></a>default_1000</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_a73209d5b31884b1a9a504293113d5d1d"><a name="en-us_topic_0173178308_a73209d5b31884b1a9a504293113d5d1d"></a><a name="en-us_topic_0173178308_a73209d5b31884b1a9a504293113d5d1d"></a>This group is created for tenants. Internal system user group, which is used only between components.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row202066799457"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_a928e9974dc2a468aa78038d3bd00cbac"><a name="en-us_topic_0173178308_a928e9974dc2a468aa78038d3bd00cbac"></a><a name="en-us_topic_0173178308_a928e9974dc2a468aa78038d3bd00cbac"></a>kafka</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_a3f6961143de94d7a97afb2a40490b93f"><a name="en-us_topic_0173178308_a3f6961143de94d7a97afb2a40490b93f"></a><a name="en-us_topic_0173178308_a3f6961143de94d7a97afb2a40490b93f"></a>Kafka common user group. A user added to this user group can access a topic only when a user in the kafkaadmin group grants the read and write permission of the topic to the user.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row6569852694530"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_afc83cb0962234871a1d189d4e6e95177"><a name="en-us_topic_0173178308_afc83cb0962234871a1d189d4e6e95177"></a><a name="en-us_topic_0173178308_afc83cb0962234871a1d189d4e6e95177"></a>kafkasuperuser</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_a6bdad5adf8514b9cb7eac7d5ba76da09"><a name="en-us_topic_0173178308_a6bdad5adf8514b9cb7eac7d5ba76da09"></a><a name="en-us_topic_0173178308_a6bdad5adf8514b9cb7eac7d5ba76da09"></a>Users added to this user group have the read and write permission of all topics.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row6261757794534"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_afa32625786b84845b61e362d8b9db361"><a name="en-us_topic_0173178308_afa32625786b84845b61e362d8b9db361"></a><a name="en-us_topic_0173178308_afa32625786b84845b61e362d8b9db361"></a>kafkaadmin</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_a0ef55c8643954d3bbd0407b9b0a75f3c"><a name="en-us_topic_0173178308_a0ef55c8643954d3bbd0407b9b0a75f3c"></a><a name="en-us_topic_0173178308_a0ef55c8643954d3bbd0407b9b0a75f3c"></a>Kafka administrator group. Users added to this user group have the rights to create, delete, authorize, read, and write all topics.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row543859494539"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_ab2954e7055fb4f6c83872a53c9116780"><a name="en-us_topic_0173178308_ab2954e7055fb4f6c83872a53c9116780"></a><a name="en-us_topic_0173178308_ab2954e7055fb4f6c83872a53c9116780"></a>storm</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_ac49a11ddf7aa4630a74916753b22cc9a"><a name="en-us_topic_0173178308_ac49a11ddf7aa4630a74916753b22cc9a"></a><a name="en-us_topic_0173178308_ac49a11ddf7aa4630a74916753b22cc9a"></a>Users added to this user group can submit topologies and manage their own topologies.</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row1054132094543"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_a5bd373bf0eaa43beaefc7e6ec628b09d"><a name="en-us_topic_0173178308_a5bd373bf0eaa43beaefc7e6ec628b09d"></a><a name="en-us_topic_0173178308_a5bd373bf0eaa43beaefc7e6ec628b09d"></a>stormadmin</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_a173acadcc8f84d5291f5501df94fb3e1"><a name="en-us_topic_0173178308_a173acadcc8f84d5291f5501df94fb3e1"></a><a name="en-us_topic_0173178308_a173acadcc8f84d5291f5501df94fb3e1"></a>Users added to this user group can have the storm administrator rights and can submit topologies and manage all topologies.</p>
</td>
</tr>
</tbody>
</table>

<a name="en-us_topic_0173178308_tb626363ed65e402db25e807c2d3b9bf8"></a>
<table><thead align="left"><tr id="en-us_topic_0173178308_en-us_topic_0039905375_row6615973595611"><th class="cellrowborder" valign="top" width="35.449999999999996%" id="mcps1.1.3.1.1"><p id="en-us_topic_0173178308_en-us_topic_0039905375_p108162799453"><a name="en-us_topic_0173178308_en-us_topic_0039905375_p108162799453"></a><a name="en-us_topic_0173178308_en-us_topic_0039905375_p108162799453"></a>OS User Group</p>
</th>
<th class="cellrowborder" valign="top" width="64.55%" id="mcps1.1.3.1.2"><p id="en-us_topic_0173178308_en-us_topic_0039905375_p315392209453"><a name="en-us_topic_0173178308_en-us_topic_0039905375_p315392209453"></a><a name="en-us_topic_0173178308_en-us_topic_0039905375_p315392209453"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0173178308_en-us_topic_0039905375_row4637249295611"><td class="cellrowborder" valign="top" width="35.449999999999996%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_en-us_topic_0039905375_p412556129453"><a name="en-us_topic_0173178308_en-us_topic_0039905375_p412556129453"></a><a name="en-us_topic_0173178308_en-us_topic_0039905375_p412556129453"></a>wheel</p>
</td>
<td class="cellrowborder" valign="top" width="64.55%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_en-us_topic_0039905375_p280260249453"><a name="en-us_topic_0173178308_en-us_topic_0039905375_p280260249453"></a><a name="en-us_topic_0173178308_en-us_topic_0039905375_p280260249453"></a>Primary group of MRS internal running user <strong id="en-us_topic_0173178308_en-us_topic_0039905375_b1376962105451"><a name="en-us_topic_0173178308_en-us_topic_0039905375_b1376962105451"></a><a name="en-us_topic_0173178308_en-us_topic_0039905375_b1376962105451"></a>omm</strong></p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row7450595611"><td class="cellrowborder" valign="top" width="35.449999999999996%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0173178308_en-us_topic_0039905375_p371687299453"><a name="en-us_topic_0173178308_en-us_topic_0039905375_p371687299453"></a><a name="en-us_topic_0173178308_en-us_topic_0039905375_p371687299453"></a>ficommon</p>
</td>
<td class="cellrowborder" valign="top" width="64.55%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0173178308_en-us_topic_0039905375_p575311339453"><a name="en-us_topic_0173178308_en-us_topic_0039905375_p575311339453"></a><a name="en-us_topic_0173178308_en-us_topic_0039905375_p575311339453"></a>MRS cluster common group that corresponds to <strong id="en-us_topic_0173178308_en-us_topic_0039905375_b730495895611"><a name="en-us_topic_0173178308_en-us_topic_0039905375_b730495895611"></a><a name="en-us_topic_0173178308_en-us_topic_0039905375_b730495895611"></a>compcommon</strong> for accessing public cluster resource files stored in the OS</p>
</td>
</tr>
</tbody>
</table>

## Database Users<a name="en-us_topic_0173178308_s440b3ede47f644ba9487dfcb0c33946a"></a>

MRS cluster system database users contain OMS database users and DBService database users.

>![](/images/icon-note.gif) **NOTE:**   
>Do not delete the following database users. Otherwise, the cluster or services may not work properly.  

<a name="en-us_topic_0173178308_td88a77ed35f74ba58ec71944adb700ec"></a>
<table><thead align="left"><tr id="en-us_topic_0173178308_en-us_topic_0039905375_row1142646795648"><th class="cellrowborder" valign="top" width="21.11788821117888%" id="mcps1.1.5.1.1"><p id="en-us_topic_0173178308_a8fea2203ff3c4e87b2ce27e3bc8ab10a"><a name="en-us_topic_0173178308_a8fea2203ff3c4e87b2ce27e3bc8ab10a"></a><a name="en-us_topic_0173178308_a8fea2203ff3c4e87b2ce27e3bc8ab10a"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="21.11788821117888%" id="mcps1.1.5.1.2"><p id="en-us_topic_0173178308_a71838f8eb417474fb9da0c87da81a82e"><a name="en-us_topic_0173178308_a71838f8eb417474fb9da0c87da81a82e"></a><a name="en-us_topic_0173178308_a71838f8eb417474fb9da0c87da81a82e"></a>Default User</p>
</th>
<th class="cellrowborder" valign="top" width="20.727927207279272%" id="mcps1.1.5.1.3"><p id="en-us_topic_0173178308_a6b8c0dccb89a4f1995c8bdfa97c090ac"><a name="en-us_topic_0173178308_a6b8c0dccb89a4f1995c8bdfa97c090ac"></a><a name="en-us_topic_0173178308_a6b8c0dccb89a4f1995c8bdfa97c090ac"></a>Initial Password</p>
</th>
<th class="cellrowborder" valign="top" width="37.03629637036296%" id="mcps1.1.5.1.4"><p id="en-us_topic_0173178308_aa32827fce9f94389921e7944c8544486"><a name="en-us_topic_0173178308_aa32827fce9f94389921e7944c8544486"></a><a name="en-us_topic_0173178308_aa32827fce9f94389921e7944c8544486"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0173178308_en-us_topic_0039905375_row6356712795648"><td class="cellrowborder" rowspan="2" valign="top" width="21.11788821117888%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0173178308_a77b1dfce79f545efa4af627a3993b302"><a name="en-us_topic_0173178308_a77b1dfce79f545efa4af627a3993b302"></a><a name="en-us_topic_0173178308_a77b1dfce79f545efa4af627a3993b302"></a>OMS database</p>
</td>
<td class="cellrowborder" valign="top" width="21.11788821117888%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0173178308_a564f46a9a8a046fbb03cc124434167e0"><a name="en-us_topic_0173178308_a564f46a9a8a046fbb03cc124434167e0"></a><a name="en-us_topic_0173178308_a564f46a9a8a046fbb03cc124434167e0"></a>ommdba</p>
</td>
<td class="cellrowborder" valign="top" width="20.727927207279272%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0173178308_ab2447cdd41e9428ca1ff5211e734d283"><a name="en-us_topic_0173178308_ab2447cdd41e9428ca1ff5211e734d283"></a><a name="en-us_topic_0173178308_ab2447cdd41e9428ca1ff5211e734d283"></a>dbChangeMe@123456</p>
</td>
<td class="cellrowborder" valign="top" width="37.03629637036296%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0173178308_a02523534bc8b46e4a480b3a205b58d7e"><a name="en-us_topic_0173178308_a02523534bc8b46e4a480b3a205b58d7e"></a><a name="en-us_topic_0173178308_a02523534bc8b46e4a480b3a205b58d7e"></a>OMS database administrator who performs maintenance operations, such as creating, starting, and stopping applications</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row2363231995648"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0173178308_aeb04d10838f541a0bf0061611d757d63"><a name="en-us_topic_0173178308_aeb04d10838f541a0bf0061611d757d63"></a><a name="en-us_topic_0173178308_aeb04d10838f541a0bf0061611d757d63"></a>omm</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0173178308_a678c5db3f5b5455889c1b6d94901aecb"><a name="en-us_topic_0173178308_a678c5db3f5b5455889c1b6d94901aecb"></a><a name="en-us_topic_0173178308_a678c5db3f5b5455889c1b6d94901aecb"></a>ChangeMe@123456</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0173178308_a7536eb415f6e4cc7ade6fefa85c59ee0"><a name="en-us_topic_0173178308_a7536eb415f6e4cc7ade6fefa85c59ee0"></a><a name="en-us_topic_0173178308_a7536eb415f6e4cc7ade6fefa85c59ee0"></a>User used for accessing OMS database data</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row3844649595648"><td class="cellrowborder" rowspan="4" valign="top" width="21.11788821117888%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0173178308_a5bf21fd8ad014379acc952eccbc04415"><a name="en-us_topic_0173178308_a5bf21fd8ad014379acc952eccbc04415"></a><a name="en-us_topic_0173178308_a5bf21fd8ad014379acc952eccbc04415"></a>DBService database</p>
</td>
<td class="cellrowborder" valign="top" width="21.11788821117888%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0173178308_ab65e71a4a6b74a3dac40b77f86ff8eae"><a name="en-us_topic_0173178308_ab65e71a4a6b74a3dac40b77f86ff8eae"></a><a name="en-us_topic_0173178308_ab65e71a4a6b74a3dac40b77f86ff8eae"></a>omm</p>
</td>
<td class="cellrowborder" valign="top" width="20.727927207279272%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0173178308_a63c64a4581724f9da63cdfd02f6ad012"><a name="en-us_topic_0173178308_a63c64a4581724f9da63cdfd02f6ad012"></a><a name="en-us_topic_0173178308_a63c64a4581724f9da63cdfd02f6ad012"></a>dbserverAdmin@123</p>
</td>
<td class="cellrowborder" valign="top" width="37.03629637036296%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0173178308_a16fba29a1a7845e593a1494f1a87e7f0"><a name="en-us_topic_0173178308_a16fba29a1a7845e593a1494f1a87e7f0"></a><a name="en-us_topic_0173178308_a16fba29a1a7845e593a1494f1a87e7f0"></a>Administrator of the GaussDB database in the DBService component</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row5016024095648"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0173178308_ac30260ef088f4c93a77a40e105ebb921"><a name="en-us_topic_0173178308_ac30260ef088f4c93a77a40e105ebb921"></a><a name="en-us_topic_0173178308_ac30260ef088f4c93a77a40e105ebb921"></a>hive</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0173178308_en-us_topic_0039905375_p103531994551"><a name="en-us_topic_0173178308_en-us_topic_0039905375_p103531994551"></a><a name="en-us_topic_0173178308_en-us_topic_0039905375_p103531994551"></a>HiveUser@</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0173178308_abe48921bebd24b6aa26eb47bc8e48639"><a name="en-us_topic_0173178308_abe48921bebd24b6aa26eb47bc8e48639"></a><a name="en-us_topic_0173178308_abe48921bebd24b6aa26eb47bc8e48639"></a>User used for Hive to connect to the DBService database</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_en-us_topic_0039905375_row461324311248"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0173178308_ae00c4991cebc4fa8a8d633302f4e4c16"><a name="en-us_topic_0173178308_ae00c4991cebc4fa8a8d633302f4e4c16"></a><a name="en-us_topic_0173178308_ae00c4991cebc4fa8a8d633302f4e4c16"></a>hue</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0173178308_a7c77ef536cfb44408633d65ba0a65859"><a name="en-us_topic_0173178308_a7c77ef536cfb44408633d65ba0a65859"></a><a name="en-us_topic_0173178308_a7c77ef536cfb44408633d65ba0a65859"></a>HueUser@123</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0173178308_af2032b5030dd4fbeab1821a8b743e153"><a name="en-us_topic_0173178308_af2032b5030dd4fbeab1821a8b743e153"></a><a name="en-us_topic_0173178308_af2032b5030dd4fbeab1821a8b743e153"></a>User used for Hue to connect to the DBService database</p>
</td>
</tr>
<tr id="en-us_topic_0173178308_row27618982141417"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0173178308_p35509001105120"><a name="en-us_topic_0173178308_p35509001105120"></a><a name="en-us_topic_0173178308_p35509001105120"></a><span id="en-us_topic_0173178308_ph52726925141441"><a name="en-us_topic_0173178308_ph52726925141441"></a><a name="en-us_topic_0173178308_ph52726925141441"></a>sqoop</span></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0173178308_p57656838105120"><a name="en-us_topic_0173178308_p57656838105120"></a><a name="en-us_topic_0173178308_p57656838105120"></a><span id="en-us_topic_0173178308_ph40047445141447"><a name="en-us_topic_0173178308_ph40047445141447"></a><a name="en-us_topic_0173178308_ph40047445141447"></a>SqoopUser@</span></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0173178308_p39692320105120"><a name="en-us_topic_0173178308_p39692320105120"></a><a name="en-us_topic_0173178308_p39692320105120"></a><span id="en-us_topic_0173178308_ph12287639101749"><a name="en-us_topic_0173178308_ph12287639101749"></a><a name="en-us_topic_0173178308_ph12287639101749"></a>User for Loader to connect to the DBService database</span></p>
</td>
</tr>
</tbody>
</table>

