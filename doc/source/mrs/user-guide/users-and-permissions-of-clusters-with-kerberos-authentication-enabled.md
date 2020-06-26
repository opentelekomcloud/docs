# Users and Permissions of Clusters with Kerberos Authentication Enabled<a name="EN-US_TOPIC_0125375243"></a>

## Overview<a name="sa36aca3d54454f3686f2d28e3ae242b6"></a>

-   **MRS Cluster Users**

    Indicate the security accounts of MRS Manager, including usernames and passwords. These accounts are used to access resources in MRS clusters. Each MRS cluster in which Kerberos authentication is enabled can have multiple users.

-   **MRS Cluster Roles**

    Before using resources in an MRS cluster, users must obtain the access permission. The access permission is defined by MRS cluster objects. A cluster role is a set of one or more permissions. For example, the permission to access a directory in HDFS needs to be configured in the specified directory and saved in a role.


MRS Manager provides the user permission management function for MRS clusters, facilitating permission and user management.

-   Permission management: adopts the role-based access control \(RBAC\) mode. In this mode, permissions are granted by role, forming a permission set. After one or more roles are allocated to a user, the user can obtain the permissions of the roles.
-   User management: uses MRS Manager to uniformly manage users, adopts the Kerberos protocol for user identity verification, and employs Lightweight Directory Access Protocol \(LDAP\) to store user information.

## Permission Management<a name="sd6bc42ee06e6423e8fd2733da22b3739"></a>

Permissions provided by MRS clusters include the O&M permissions of MRS Manager and components \(such as HDFS, HBase, Hive, and Yarn\). In actual application, permissions must be assigned to each user based on service scenarios. To facilitate permission management, MRS Manager introduces the role function to allow administrators to select and assign specified permissions. Permissions are centrally viewed and managed in permission sets, enhancing user experience.

A role is a logical entity that contains one or more permissions. Permissions are assigned to roles, and users can be granted the permissions by obtaining the roles.

A role can have multiple permissions, and a user can be bound to multiple roles.

-   Role 1: is assigned operation permissions A and B. After role 1 is allocated to users a and b, users a and b can obtain operation permissions A and B.
-   Role 2: is assigned operation permission C. After role 2 is allocated to users c and d, users c and d can obtain operation permission C.
-   Role 3: is assigned operation permissions D and F. After role 3 is allocated to user a, user a can obtain operation permissions D and F.

For example, if an MRS user is bound to the administrator role, the user is an administrator of the MRS cluster.

[Table 1](#tc121417c5da94a81b975ea77169ea15d)  lists the roles that are created by default on MRS Manager.

**Table  1**  Default roles and description

<a name="tc121417c5da94a81b975ea77169ea15d"></a>
<table><thead align="left"><tr id="r40e3edbc38fb44a99a3a22262f4cce37"><th class="cellrowborder" valign="top" width="30.5%" id="mcps1.2.3.1.1"><p id="ad1eed100f0294495b38ebe2fefb5c9ea"><a name="ad1eed100f0294495b38ebe2fefb5c9ea"></a><a name="ad1eed100f0294495b38ebe2fefb5c9ea"></a><strong id="aa7c0459613de4d2cb7372d6eaf444dc3"><a name="aa7c0459613de4d2cb7372d6eaf444dc3"></a><a name="aa7c0459613de4d2cb7372d6eaf444dc3"></a>Default Role</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69.5%" id="mcps1.2.3.1.2"><p id="a3921fdcde552491bb8b9dde75cdf14e8"><a name="a3921fdcde552491bb8b9dde75cdf14e8"></a><a name="a3921fdcde552491bb8b9dde75cdf14e8"></a><strong id="af1c116b635674194aebd017c48249fe7"><a name="af1c116b635674194aebd017c48249fe7"></a><a name="af1c116b635674194aebd017c48249fe7"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r305bf7d18aff4f0a872319c88c657d26"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="a2af8ff8bb0664818ba65c27db37f7167"><a name="a2af8ff8bb0664818ba65c27db37f7167"></a><a name="a2af8ff8bb0664818ba65c27db37f7167"></a>default</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="a3521c0ef5f624c3e8084880110a4ce8b"><a name="a3521c0ef5f624c3e8084880110a4ce8b"></a><a name="a3521c0ef5f624c3e8084880110a4ce8b"></a>Tenant role</p>
</td>
</tr>
<tr id="r338b59bcee9b4c8f854ec8bf7be84c4a"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="a36d824ece24c4bd0ab685543b99cb37b"><a name="a36d824ece24c4bd0ab685543b99cb37b"></a><a name="a36d824ece24c4bd0ab685543b99cb37b"></a>Manager_administrator</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="a9a4d4cd7864a4cf6bf84dac2972b13d6"><a name="a9a4d4cd7864a4cf6bf84dac2972b13d6"></a><a name="a9a4d4cd7864a4cf6bf84dac2972b13d6"></a>Manager administrator: This role has the permission to manage MRS Manager.</p>
</td>
</tr>
<tr id="r36c91feadf73407aae24199fb99093cd"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="afded5c4d7f80456bbbab46431b993d5e"><a name="afded5c4d7f80456bbbab46431b993d5e"></a><a name="afded5c4d7f80456bbbab46431b993d5e"></a>Manager_auditor</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="ab11da40c720d45a79004036c2e76f7e1"><a name="ab11da40c720d45a79004036c2e76f7e1"></a><a name="ab11da40c720d45a79004036c2e76f7e1"></a>Manager auditor: This role has the permission to view and manage auditing information.</p>
</td>
</tr>
<tr id="r519303d415dc454dbdff26e63b245f2e"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="a18de7f52041b4560a00e15a1a948474f"><a name="a18de7f52041b4560a00e15a1a948474f"></a><a name="a18de7f52041b4560a00e15a1a948474f"></a>Manager_operator</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="af17664084d69437d829b2608636cf506"><a name="af17664084d69437d829b2608636cf506"></a><a name="af17664084d69437d829b2608636cf506"></a>Manager operator: This role has all permissions except tenant, configuration, and cluster management permissions.</p>
</td>
</tr>
<tr id="rb52748e95cbb47cba9258687a93d2a9b"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="a3c177d7631cf4c7d8b3a863bb4212dde"><a name="a3c177d7631cf4c7d8b3a863bb4212dde"></a><a name="a3c177d7631cf4c7d8b3a863bb4212dde"></a>Manager_viewer</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="a176f5bb20c5342ba8fb1bd87c8bae24f"><a name="a176f5bb20c5342ba8fb1bd87c8bae24f"></a><a name="a176f5bb20c5342ba8fb1bd87c8bae24f"></a>Manager viewer: This role has the permission to view the information about systems, services, hosts, alarms, and auditing logs.</p>
</td>
</tr>
<tr id="r9b6b734de8b84892b492db9f710790d3"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="a212bc8fc836d4a40afebe1394af807a2"><a name="a212bc8fc836d4a40afebe1394af807a2"></a><a name="a212bc8fc836d4a40afebe1394af807a2"></a>System_administrator</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="ae49b9ae71c6843148afb4e525de76bec"><a name="ae49b9ae71c6843148afb4e525de76bec"></a><a name="ae49b9ae71c6843148afb4e525de76bec"></a>System administrator: This role has the permissions of Manager administrators and all service administrators.</p>
</td>
</tr>
<tr id="r9c11a011c6a249e6960864001ee14991"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="a945bc861b2f34448b83b065fd8bc171e"><a name="a945bc861b2f34448b83b065fd8bc171e"></a><a name="a945bc861b2f34448b83b065fd8bc171e"></a>Manager_tenant</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="a28dbf5cc7d34448a9023a4d0ab737662"><a name="a28dbf5cc7d34448a9023a4d0ab737662"></a><a name="a28dbf5cc7d34448a9023a4d0ab737662"></a>Manager tenant viewer: This role has the permission to view information on the <strong id="a66e5b5d08f7644629223dda14ed125df"><a name="a66e5b5d08f7644629223dda14ed125df"></a><a name="a66e5b5d08f7644629223dda14ed125df"></a>Tenant</strong> page on MRS Manager.</p>
</td>
</tr>
</tbody>
</table>

When creating a role on MRS Manager, you can perform permission management for MRS Manager and components, as described in  [Table 2](#t81178f9b25444c3e98bb7fa302660921).

**Table  2**  Manager and component permission management

<a name="t81178f9b25444c3e98bb7fa302660921"></a>
<table><thead align="left"><tr id="rdf3a92636d7d4a5cab37f8a16bc1f818"><th class="cellrowborder" valign="top" width="30.5%" id="mcps1.2.3.1.1"><p id="a0cf8fe4221a7429baf3d928e80c77421"><a name="a0cf8fe4221a7429baf3d928e80c77421"></a><a name="a0cf8fe4221a7429baf3d928e80c77421"></a><strong id="abf4b0907bf4e4192af3fdd490e54394c"><a name="abf4b0907bf4e4192af3fdd490e54394c"></a><a name="abf4b0907bf4e4192af3fdd490e54394c"></a>Permission</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69.5%" id="mcps1.2.3.1.2"><p id="ac8d49fe08c7d4d5c95e1393be3488153"><a name="ac8d49fe08c7d4d5c95e1393be3488153"></a><a name="ac8d49fe08c7d4d5c95e1393be3488153"></a><strong id="a045e4cb6aa8d46ec91bdb3044923ecb0"><a name="a045e4cb6aa8d46ec91bdb3044923ecb0"></a><a name="a045e4cb6aa8d46ec91bdb3044923ecb0"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rb73dbbcf9efb47d2a8c168e5e9f21fa5"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="a32cc04fec99643bc8f5f2f9e7ea2b95c"><a name="a32cc04fec99643bc8f5f2f9e7ea2b95c"></a><a name="a32cc04fec99643bc8f5f2f9e7ea2b95c"></a>Manager</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="a505fc81dadfe46fab2ea81aaea769bee"><a name="a505fc81dadfe46fab2ea81aaea769bee"></a><a name="a505fc81dadfe46fab2ea81aaea769bee"></a>Manager access and login permission.</p>
</td>
</tr>
<tr id="r6b6ceea05cb74fcca873ca13b6d8c09e"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="a76f8225cce8c41e9b1b7b54fbeabf79f"><a name="a76f8225cce8c41e9b1b7b54fbeabf79f"></a><a name="a76f8225cce8c41e9b1b7b54fbeabf79f"></a>HBase</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="aca695083fd2146d0b0bc7ab4ec1aa9cb"><a name="aca695083fd2146d0b0bc7ab4ec1aa9cb"></a><a name="aca695083fd2146d0b0bc7ab4ec1aa9cb"></a>HBase administrator permission and permission for accessing HBase tables and column families.</p>
</td>
</tr>
<tr id="r9692274f73c243629141d7389166f57a"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="a89b2cbba8a9341eea9007c9cf00120e7"><a name="a89b2cbba8a9341eea9007c9cf00120e7"></a><a name="a89b2cbba8a9341eea9007c9cf00120e7"></a>HDFS</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="adde34c247d3e4c6b8c495cd040fa6128"><a name="adde34c247d3e4c6b8c495cd040fa6128"></a><a name="adde34c247d3e4c6b8c495cd040fa6128"></a>HDFS directory and file permission.</p>
</td>
</tr>
<tr id="rfc3874c1e76e4ee5a350d1c90abcdcb0"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="a4fe9bf943120445383ba394d70b7ff17"><a name="a4fe9bf943120445383ba394d70b7ff17"></a><a name="a4fe9bf943120445383ba394d70b7ff17"></a>Hive</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><a name="ub9a0f1f4cb2149beaaa72a1ab45bf88b"></a><a name="ub9a0f1f4cb2149beaaa72a1ab45bf88b"></a><ul id="ub9a0f1f4cb2149beaaa72a1ab45bf88b"><li>Hive Admin Privilege<p id="aa88c2418783649c8a74276a686a20fdc"><a name="aa88c2418783649c8a74276a686a20fdc"></a><a name="aa88c2418783649c8a74276a686a20fdc"></a>Hive administrator permission.</p>
</li><li>Hive Read Write Privileges<p id="ae00e21a3a2a5409e87357f3ed89d9876"><a name="ae00e21a3a2a5409e87357f3ed89d9876"></a><a name="ae00e21a3a2a5409e87357f3ed89d9876"></a>Hive data table management permission, which is the operation permission to set and manage the data of created tables.</p>
</li></ul>
</td>
</tr>
<tr id="row4119556110131"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="p4850617310131"><a name="p4850617310131"></a><a name="p4850617310131"></a>Hue</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="p3668594110131"><a name="p3668594110131"></a><a name="p3668594110131"></a>Storage policy administrator rights.</p>
</td>
</tr>
<tr id="rc983f0bb7551459da96588bde155d746"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="a73229bf7edb041c6a0c96aacaa1e0e38"><a name="a73229bf7edb041c6a0c96aacaa1e0e38"></a><a name="a73229bf7edb041c6a0c96aacaa1e0e38"></a>Yarn</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><a name="u24c48e69f3f24fbc8aa3c24fa27a9001"></a><a name="u24c48e69f3f24fbc8aa3c24fa27a9001"></a><ul id="u24c48e69f3f24fbc8aa3c24fa27a9001"><li>Cluster Admin Operations<p id="a80084d4be42549e9b3cc0af355d45b46"><a name="a80084d4be42549e9b3cc0af355d45b46"></a><a name="a80084d4be42549e9b3cc0af355d45b46"></a>Yarn administrator permission.</p>
</li><li>Scheduler Queue<p id="a45b5908a6ce24a69b312ef0ab47de743"><a name="a45b5908a6ce24a69b312ef0ab47de743"></a><a name="a45b5908a6ce24a69b312ef0ab47de743"></a>Queue resource management permission.</p>
</li></ul>
</td>
</tr>
</tbody>
</table>

## User Management<a name="s462cd81bcbb34a379cb955061aa19f38"></a>

MRS clusters that support Kerberos authentication use the Kerberos protocol and LDAP for user management.

-   Kerberos verifies the identity of a user when the user logs in to MRS Manager or uses a component client. Identity verification is not required for clusters with Kerberos authentication disabled.
-   LDAP is used to store user information, including user records, user group information, and permission information.

MRS clusters can automatically update Kerberos and LDAP user data when users are created or modified on MRS Manager. They can also automatically perform user identity verification and authentication and obtain user information when a user logs in to MRS Manager or uses a component client. This ensures the security of user management and simplifies the user management tasks. MRS Manager also provides the user group function for managing one or more users by type:

-   A user group is a set of users. Users in the system can exist independently or in a user group.
-   After a user is added to a user group to which roles are allocated, the role permission of the user group is assigned to the user.

The following table lists the user groups that are created by default on MRS Manager.

**Table  3**  Default user groups and description

<a name="td1e47dda51814bc4b505b8064f957f21"></a>
<table><thead align="left"><tr id="rae0ed8f43be8418696b5bb087758a799"><th class="cellrowborder" valign="top" width="30.5%" id="mcps1.2.3.1.1"><p id="en-us_topic_0043021163_p486451514739"><a name="en-us_topic_0043021163_p486451514739"></a><a name="en-us_topic_0043021163_p486451514739"></a><strong id="a13f5d2f19db44f2a9eadfdc378b4ac76"><a name="a13f5d2f19db44f2a9eadfdc378b4ac76"></a><a name="a13f5d2f19db44f2a9eadfdc378b4ac76"></a>User Group</strong></p>
</th>
<th class="cellrowborder" valign="top" width="69.5%" id="mcps1.2.3.1.2"><p id="a813c653dd9bb4e85bbb38b863c7e0f9f"><a name="a813c653dd9bb4e85bbb38b863c7e0f9f"></a><a name="a813c653dd9bb4e85bbb38b863c7e0f9f"></a><strong id="a873a58a3281a4b16ae0ec2b450c5a8d5"><a name="a873a58a3281a4b16ae0ec2b450c5a8d5"></a><a name="a873a58a3281a4b16ae0ec2b450c5a8d5"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rbe10b1bf56194fe89815d043a9e3a6a9"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="a657a9b0a9a26489fb253094c371df45d"><a name="a657a9b0a9a26489fb253094c371df45d"></a><a name="a657a9b0a9a26489fb253094c371df45d"></a>hadoop</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="acd3302b815d94a1faa8a65e3ba597b65"><a name="acd3302b815d94a1faa8a65e3ba597b65"></a><a name="acd3302b815d94a1faa8a65e3ba597b65"></a>Users added to this user group have the permission to submit tasks to all Yarn queues.</p>
</td>
</tr>
<tr id="r4927b63a08b14bf9952366194fb013b0"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="ab6a07510cf8b4903be42b2b850e6894f"><a name="ab6a07510cf8b4903be42b2b850e6894f"></a><a name="ab6a07510cf8b4903be42b2b850e6894f"></a>hbase</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="ad795adb1c5fc42148012b399bc4088c3"><a name="ad795adb1c5fc42148012b399bc4088c3"></a><a name="ad795adb1c5fc42148012b399bc4088c3"></a>Common user group. Users added to this user group will not have any additional permission.</p>
</td>
</tr>
<tr id="r6461ffd4645a4545af02ba95094a9437"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="a43277e28da2844b19305d85b292359f4"><a name="a43277e28da2844b19305d85b292359f4"></a><a name="a43277e28da2844b19305d85b292359f4"></a>hive</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="a60e7f5af29634defa7d52888e93bb154"><a name="a60e7f5af29634defa7d52888e93bb154"></a><a name="a60e7f5af29634defa7d52888e93bb154"></a>Users added to this user group can use Hive.</p>
</td>
</tr>
<tr id="ra40c83a7583c45819b26e6a8925f9b6f"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="a1c72f98c750c47ea8931258b74b534da"><a name="a1c72f98c750c47ea8931258b74b534da"></a><a name="a1c72f98c750c47ea8931258b74b534da"></a>supergroup</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="a1e2eb15c35924f46bb0be57d9fdcfa50"><a name="a1e2eb15c35924f46bb0be57d9fdcfa50"></a><a name="a1e2eb15c35924f46bb0be57d9fdcfa50"></a>Users added to this user group can have the administrator rights of HBase, HDFS, and Yarn and can use Hive.</p>
</td>
</tr>
<tr id="row7578323172849"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="p17019925172858"><a name="p17019925172858"></a><a name="p17019925172858"></a>flume</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="p36436694172858"><a name="p36436694172858"></a><a name="p36436694172858"></a>Common user group. Users added to this user group will not have any additional permission.</p>
</td>
</tr>
<tr id="row37145758173141"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="p63540992173141"><a name="p63540992173141"></a><a name="p63540992173141"></a>kafka</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="p51781796173141"><a name="p51781796173141"></a><a name="p51781796173141"></a>Kafka common user group. A user added to this user group can access a topic only when a user in the kafkaadmin group grants the read and write permission of the topic to the user.</p>
</td>
</tr>
<tr id="row31247039173152"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="p720478173152"><a name="p720478173152"></a><a name="p720478173152"></a>kafkasuperuser</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="p47646035173152"><a name="p47646035173152"></a><a name="p47646035173152"></a>Users added to this user group have the read and write permission of all topics.</p>
</td>
</tr>
<tr id="row31149839173546"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="p7078932173546"><a name="p7078932173546"></a><a name="p7078932173546"></a>kafkaadmin</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="p62256711173546"><a name="p62256711173546"></a><a name="p62256711173546"></a>Kafka administrator group. Users added to this user group have the rights to create, delete, authorize, read, and write all topics.</p>
</td>
</tr>
<tr id="row2140564173157"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="p62784240173157"><a name="p62784240173157"></a><a name="p62784240173157"></a>storm</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="p48573834173157"><a name="p48573834173157"></a><a name="p48573834173157"></a>Users added to this user group can submit topologies and manage their own topologies.</p>
</td>
</tr>
<tr id="row6162116117321"><td class="cellrowborder" valign="top" width="30.5%" headers="mcps1.2.3.1.1 "><p id="p5984692417321"><a name="p5984692417321"></a><a name="p5984692417321"></a>stormadmin</p>
</td>
<td class="cellrowborder" valign="top" width="69.5%" headers="mcps1.2.3.1.2 "><p id="p2469056417321"><a name="p2469056417321"></a><a name="p2469056417321"></a>Users added to this user group can have the storm administrator rights and can submit topologies and manage all topologies.</p>
</td>
</tr>
</tbody>
</table>

User  **admin**  is created by default for MRS clusters with Kerberos authentication enabled and is used by administrators to maintain the clusters.

## Process Overview<a name="sb5a80785e75346a698d7a44713e2b022"></a>

In practice, administrators must understand the service scenarios of MRS clusters and plan user permissions. Then, create roles and assign permissions to the roles on MRS Manager to meet service requirements. Administrators can create user groups on MRS Manager to manage users in one or more service scenarios of the same type.

>![](/images/icon-note.gif) **NOTE:**   
>If a role has the permission of HDFS, HBase, Hive, or Yarn, the role can use the corresponding functions of the component. To use MRS Manager, the corresponding Manager permission must be added to the role.  

**Figure  1**  Process of creating a user<a name="f7b8609bd89e04d7595615c3dbc17bb29"></a>  
![](figures/process-of-creating-a-user.jpg "process-of-creating-a-user")

