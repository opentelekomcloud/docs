# Default Users of Clusters with Kerberos Authentication Enabled<a name="EN-US_TOPIC_0125376024"></a>

## User Classification<a name="s28eada6a9f604dd1af2bbec84b12b3f3"></a>

The MRS cluster provides the following three types of users. Users are required to periodically change the passwords. It is not recommended to use the default passwords.

<a name="t0709d56bb1f7453895b70b34aaf67357"></a>
<table><thead align="left"><tr id="rabbef91c0c934dd89cda5aeaf54b6712"><th class="cellrowborder" valign="top" width="21.5%" id="mcps1.1.3.1.1"><p id="a77da5cbcae564ed19c62248607f1ac18"><a name="a77da5cbcae564ed19c62248607f1ac18"></a><a name="a77da5cbcae564ed19c62248607f1ac18"></a>User Type</p>
</th>
<th class="cellrowborder" valign="top" width="78.5%" id="mcps1.1.3.1.2"><p id="a6f089092db5d479b83b4fe48b835f543"><a name="a6f089092db5d479b83b4fe48b835f543"></a><a name="a6f089092db5d479b83b4fe48b835f543"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r96f872e9615741b1a0883e9423dfa44c"><td class="cellrowborder" valign="top" width="21.5%" headers="mcps1.1.3.1.1 "><p id="a11a92169e3cb41b5b3b1b04fd9565f91"><a name="a11a92169e3cb41b5b3b1b04fd9565f91"></a><a name="a11a92169e3cb41b5b3b1b04fd9565f91"></a>System user</p>
</td>
<td class="cellrowborder" valign="top" width="78.5%" headers="mcps1.1.3.1.2 "><a name="u2a52013bb9644f75a1a183b2359f9a7c"></a><a name="u2a52013bb9644f75a1a183b2359f9a7c"></a><ul id="u2a52013bb9644f75a1a183b2359f9a7c"><li>A user created on MRS Manager for MRS cluster O&amp;M and service scenarios. There are two types of users:<a name="ufe9e24505dea4b10b1efe26932da1ba1"></a><a name="ufe9e24505dea4b10b1efe26932da1ba1"></a><ul id="ufe9e24505dea4b10b1efe26932da1ba1"><li><span class="parmname" id="p7bd512df888c4c1b9002328126a12da7"><a name="p7bd512df888c4c1b9002328126a12da7"></a><a name="p7bd512df888c4c1b9002328126a12da7"></a><b>Human-machine</b></span> user: used for MRS Manager O&amp;M scenarios and component client operation scenarios.</li><li><span class="parmname" id="pbcf441b5c1dd4e84b6bcde8896fdaf44"><a name="pbcf441b5c1dd4e84b6bcde8896fdaf44"></a><a name="pbcf441b5c1dd4e84b6bcde8896fdaf44"></a><b>Machine-machine</b></span> user: used for MRS cluster application development scenarios.</li></ul>
</li><li>A user used to run OMS system processes.</li></ul>
</td>
</tr>
<tr id="r6545b9a5985743d0af42fcb000526633"><td class="cellrowborder" valign="top" width="21.5%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0039905375_p669873595159"><a name="en-us_topic_0039905375_p669873595159"></a><a name="en-us_topic_0039905375_p669873595159"></a>Internal system user</p>
</td>
<td class="cellrowborder" valign="top" width="78.5%" headers="mcps1.1.3.1.2 "><p id="aff71df1c30d64adcb3e744ca25009e75"><a name="aff71df1c30d64adcb3e744ca25009e75"></a><a name="aff71df1c30d64adcb3e744ca25009e75"></a>An internal user provided by the MRS cluster and used to implement communication between processes, save user group information, and associate user rights.</p>
</td>
</tr>
<tr id="rd90ee76aaced40e291bb068e6d26c48a"><td class="cellrowborder" valign="top" width="21.5%" headers="mcps1.1.3.1.1 "><p id="a9e089c35280b428891b7555bc657a935"><a name="a9e089c35280b428891b7555bc657a935"></a><a name="a9e089c35280b428891b7555bc657a935"></a>Database user</p>
</td>
<td class="cellrowborder" valign="top" width="78.5%" headers="mcps1.1.3.1.2 "><a name="uabf79103e3a6476bb47b45fd710182ca"></a><a name="uabf79103e3a6476bb47b45fd710182ca"></a><ul id="uabf79103e3a6476bb47b45fd710182ca"><li>A user used to manage the OMS database and access data.</li><li>A user used to run the database of service components (Hive, Hue, <span id="ph4142653895350"><a name="ph4142653895350"></a><a name="ph4142653895350"></a>Loader</span> and DBService).</li></ul>
</td>
</tr>
</tbody>
</table>

## System Users<a name="sfa631598904a493e8d7bbe99548b6d56"></a>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   User  **ldap**  of the OS is required in the MRS cluster. Do not delete the account. Otherwise, the cluster may not work properly. Password management policies are maintained by the users.  
>-   Reset the password when you change the passwords of user  **ommdba** and user **omm**  for the first time. Change the passwords regularly after you have retrieved them.  

<a name="t9272fc94f92e4dd4b3c783d7d3cfc25a"></a>
<table><thead align="left"><tr id="r612fa79b111b41159011267625423f08"><th class="cellrowborder" valign="top" width="21.0978902109789%" id="mcps1.1.5.1.1"><p id="a6ae0377d6f294af8b3f71be8e8f9e10b"><a name="a6ae0377d6f294af8b3f71be8e8f9e10b"></a><a name="a6ae0377d6f294af8b3f71be8e8f9e10b"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="21.0978902109789%" id="mcps1.1.5.1.2"><p id="a52d98fa2f5ac4cd0a9751611a8ab8033"><a name="a52d98fa2f5ac4cd0a9751611a8ab8033"></a><a name="a52d98fa2f5ac4cd0a9751611a8ab8033"></a>Username</p>
</th>
<th class="cellrowborder" valign="top" width="20.88791120887911%" id="mcps1.1.5.1.3"><p id="a683e8728d2e643bda45e2d36b3d89080"><a name="a683e8728d2e643bda45e2d36b3d89080"></a><a name="a683e8728d2e643bda45e2d36b3d89080"></a>Initial Password</p>
</th>
<th class="cellrowborder" valign="top" width="36.91630836916308%" id="mcps1.1.5.1.4"><p id="a920cb534b5fd4607beaa5aa372db4a18"><a name="a920cb534b5fd4607beaa5aa372db4a18"></a><a name="a920cb534b5fd4607beaa5aa372db4a18"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rfe52cdd38f8646be86695c971caa3dd2"><td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.1.5.1.1 "><p id="a6cdb6e9a8c834811add33f69629c639e"><a name="a6cdb6e9a8c834811add33f69629c639e"></a><a name="a6cdb6e9a8c834811add33f69629c639e"></a>MRS cluster system user</p>
</td>
<td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.1.5.1.2 "><p id="ad8ed627af7e146828c2ed1d19b18e0a4"><a name="ad8ed627af7e146828c2ed1d19b18e0a4"></a><a name="ad8ed627af7e146828c2ed1d19b18e0a4"></a>admin</p>
</td>
<td class="cellrowborder" valign="top" width="20.88791120887911%" headers="mcps1.1.5.1.3 "><p id="a3b1601d9f92b493194e49f9c4bed7135"><a name="a3b1601d9f92b493194e49f9c4bed7135"></a><a name="a3b1601d9f92b493194e49f9c4bed7135"></a>Specified by the user when the cluster is created</p>
</td>
<td class="cellrowborder" valign="top" width="36.91630836916308%" headers="mcps1.1.5.1.4 "><p id="a69c6a44a2ba04c1a97b0ad4dcdb2111f"><a name="a69c6a44a2ba04c1a97b0ad4dcdb2111f"></a><a name="a69c6a44a2ba04c1a97b0ad4dcdb2111f"></a>Administrator of MRS Manager.</p>
<p id="p3549338891651"><a name="p3549338891651"></a><a name="p3549338891651"></a>This user also has the following rights:</p>
<a name="ul367366739176"></a><a name="ul367366739176"></a><ul id="ul367366739176"><li>Common HDFS and ZooKeeper user rights.</li><li>Rights to submit and query MapReduce and Yarn tasks, to manage Yarn queues, and to access Yarn WebUI.</li><li>Rights to submit, query, activate, deactivate, reassign, delete topologies, and operate all topologies of the Storm service.</li><li>Rights to create, delete, authenticate, reassign, consume, write, and query topics of the Kafka service.</li></ul>
</td>
</tr>
<tr id="r2be7ede13b6c4230af70174947460aaa"><td class="cellrowborder" rowspan="2" valign="top" width="21.0978902109789%" headers="mcps1.1.5.1.1 "><p id="ab5d43fe1a65a4b48bd965c3bc7623389"><a name="ab5d43fe1a65a4b48bd965c3bc7623389"></a><a name="ab5d43fe1a65a4b48bd965c3bc7623389"></a>MRS cluster node OS user</p>
</td>
<td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.1.5.1.2 "><p id="ac5acf6c1f3994a03ad0a5785d1783a84"><a name="ac5acf6c1f3994a03ad0a5785d1783a84"></a><a name="ac5acf6c1f3994a03ad0a5785d1783a84"></a>ommdba</p>
</td>
<td class="cellrowborder" valign="top" width="20.88791120887911%" headers="mcps1.1.5.1.3 "><p id="p33471650121319"><a name="p33471650121319"></a><a name="p33471650121319"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" width="36.91630836916308%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0039905375_p861164095430"><a name="en-us_topic_0039905375_p861164095430"></a><a name="en-us_topic_0039905375_p861164095430"></a>User who creates the MRS cluster system database. This user is an OS user generated on the management nodes and does not require a unified password.</p>
</td>
</tr>
<tr id="r904f76cfdb8f4fec904044407354c62d"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="aa18517c8868c4269abb4bc61a875064a"><a name="aa18517c8868c4269abb4bc61a875064a"></a><a name="aa18517c8868c4269abb4bc61a875064a"></a>omm</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p7414134741318"><a name="p7414134741318"></a><a name="p7414134741318"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="a4a9e815a5b0d47b1809d25c8a4bdb492"><a name="a4a9e815a5b0d47b1809d25c8a4bdb492"></a><a name="a4a9e815a5b0d47b1809d25c8a4bdb492"></a>Internal running user of the MRS cluster system. This user is an OS user generated on all nodes and does not require a unified password.</p>
</td>
</tr>
<tr id="re1f2103c99cc4632afd67fd8ce21ac37"><td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.1.5.1.1 "><p id="abb3211fe7c3b49d9a51814f7ea620120"><a name="abb3211fe7c3b49d9a51814f7ea620120"></a><a name="abb3211fe7c3b49d9a51814f7ea620120"></a>User for running MRS cluster jobs</p>
</td>
<td class="cellrowborder" valign="top" width="21.0978902109789%" headers="mcps1.1.5.1.2 "><p id="a91083b832b3043c2a02fe818347ae340"><a name="a91083b832b3043c2a02fe818347ae340"></a><a name="a91083b832b3043c2a02fe818347ae340"></a>yarn_user</p>
</td>
<td class="cellrowborder" valign="top" width="20.88791120887911%" headers="mcps1.1.5.1.3 "><p id="a9b11adb1201842f18ba64172e2a16037"><a name="a9b11adb1201842f18ba64172e2a16037"></a><a name="a9b11adb1201842f18ba64172e2a16037"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" width="36.91630836916308%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0039905375_p718400112155"><a name="en-us_topic_0039905375_p718400112155"></a><a name="en-us_topic_0039905375_p718400112155"></a>Internal user used to run the MRS cluster jobs. This user is generated on Core nodes.</p>
</td>
</tr>
</tbody>
</table>

## Internal System Users<a name="s1a6db0a323c3460498db4849d609f7d0"></a>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Do not delete the following internal system users. Otherwise, the cluster or services may not work properly.  

<a name="te42beb7fa54d4fe4aeba84a2d35e44e1"></a>
<table><thead align="left"><tr id="rbf898ad841dd4631b9d69a62a333552b"><th class="cellrowborder" valign="top" width="20.47%" id="mcps1.1.5.1.1"><p id="a9c382e8b7c8442e091f1f5ad3c78aeae"><a name="a9c382e8b7c8442e091f1f5ad3c78aeae"></a><a name="a9c382e8b7c8442e091f1f5ad3c78aeae"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25.729999999999997%" id="mcps1.1.5.1.2"><p id="a56df1a04db684779bb99de7d07db5ee3"><a name="a56df1a04db684779bb99de7d07db5ee3"></a><a name="a56df1a04db684779bb99de7d07db5ee3"></a>Default User</p>
</th>
<th class="cellrowborder" valign="top" width="14.580000000000002%" id="mcps1.1.5.1.3"><p id="ae28bfc9d57124a53a9e6aa1225cdbb8c"><a name="ae28bfc9d57124a53a9e6aa1225cdbb8c"></a><a name="ae28bfc9d57124a53a9e6aa1225cdbb8c"></a>Initial Password</p>
</th>
<th class="cellrowborder" valign="top" width="39.22%" id="mcps1.1.5.1.4"><p id="a408992729fbb4d65ada485c78a7271ad"><a name="a408992729fbb4d65ada485c78a7271ad"></a><a name="a408992729fbb4d65ada485c78a7271ad"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="red6fda20f779453081cf33438b31c565"><td class="cellrowborder" valign="top" width="20.47%" headers="mcps1.1.5.1.1 "><p id="a85973a313f6a4c8f9a0beb5118110aa5"><a name="a85973a313f6a4c8f9a0beb5118110aa5"></a><a name="a85973a313f6a4c8f9a0beb5118110aa5"></a>Kerberos administrator</p>
</td>
<td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.1.5.1.2 "><p id="a46f5c1847c5a45c0af4073b893fb8a5a"><a name="a46f5c1847c5a45c0af4073b893fb8a5a"></a><a name="a46f5c1847c5a45c0af4073b893fb8a5a"></a>kadmin/admin</p>
</td>
<td class="cellrowborder" valign="top" width="14.580000000000002%" headers="mcps1.1.5.1.3 "><p id="acee158c67d334ffc875e0ad3d6e72aea"><a name="acee158c67d334ffc875e0ad3d6e72aea"></a><a name="acee158c67d334ffc875e0ad3d6e72aea"></a>Admin@123</p>
</td>
<td class="cellrowborder" valign="top" width="39.22%" headers="mcps1.1.5.1.4 "><p id="a66957dc36f90434f8b260630c133b772"><a name="a66957dc36f90434f8b260630c133b772"></a><a name="a66957dc36f90434f8b260630c133b772"></a>Account that is used to add, delete, modify, and query users on Kerberos.</p>
</td>
</tr>
<tr id="r6446466527c442a69d7ac8a643000cfa"><td class="cellrowborder" valign="top" width="20.47%" headers="mcps1.1.5.1.1 "><p id="a61dd49a5025f4ba591b77a940edb2d56"><a name="a61dd49a5025f4ba591b77a940edb2d56"></a><a name="a61dd49a5025f4ba591b77a940edb2d56"></a>OMS Kerberos administrator</p>
</td>
<td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.1.5.1.2 "><p id="a6813d6524001440b942931c308aca7d8"><a name="a6813d6524001440b942931c308aca7d8"></a><a name="a6813d6524001440b942931c308aca7d8"></a>kadmin/admin</p>
</td>
<td class="cellrowborder" valign="top" width="14.580000000000002%" headers="mcps1.1.5.1.3 "><p id="a4677024d143b44c4ac415932309a3484"><a name="a4677024d143b44c4ac415932309a3484"></a><a name="a4677024d143b44c4ac415932309a3484"></a>Admin@123</p>
</td>
<td class="cellrowborder" valign="top" width="39.22%" headers="mcps1.1.5.1.4 "><p id="a29ef0de44d6a40dfbd20f13698bff995"><a name="a29ef0de44d6a40dfbd20f13698bff995"></a><a name="a29ef0de44d6a40dfbd20f13698bff995"></a>Account that is used to add, delete, modify, and query users on OMS Kerberos.</p>
</td>
</tr>
<tr id="r0789ed7168cc4888947405b81bc8a8cc"><td class="cellrowborder" valign="top" width="20.47%" headers="mcps1.1.5.1.1 "><p id="a7378dcea68dc4e15aa9232ecd9a52885"><a name="a7378dcea68dc4e15aa9232ecd9a52885"></a><a name="a7378dcea68dc4e15aa9232ecd9a52885"></a>LDAP administrator</p>
</td>
<td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.1.5.1.2 "><p id="aafc26cd8a36b465e85e47858e9c33ed8"><a name="aafc26cd8a36b465e85e47858e9c33ed8"></a><a name="aafc26cd8a36b465e85e47858e9c33ed8"></a>cn=root,dc=hadoop,dc=com</p>
</td>
<td class="cellrowborder" valign="top" width="14.580000000000002%" headers="mcps1.1.5.1.3 "><p id="a654ba9ce57e54d54a42230602801c46d"><a name="a654ba9ce57e54d54a42230602801c46d"></a><a name="a654ba9ce57e54d54a42230602801c46d"></a>LdapChangeMe@123</p>
</td>
<td class="cellrowborder" valign="top" width="39.22%" headers="mcps1.1.5.1.4 "><p id="af08505bb7f3a420fb6ca561f85bbaef8"><a name="af08505bb7f3a420fb6ca561f85bbaef8"></a><a name="af08505bb7f3a420fb6ca561f85bbaef8"></a>Account that is used to add, delete, modify, and query the user information on LDAP.</p>
</td>
</tr>
<tr id="r7b1467412de8459eb7e0b4b0b26ccea3"><td class="cellrowborder" valign="top" width="20.47%" headers="mcps1.1.5.1.1 "><p id="ae7ff450c01db4f6d9e184597c00e2965"><a name="ae7ff450c01db4f6d9e184597c00e2965"></a><a name="ae7ff450c01db4f6d9e184597c00e2965"></a>OMS LDAP administrator</p>
</td>
<td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.1.5.1.2 "><p id="a8037da561dfe486394e42ba517e628ce"><a name="a8037da561dfe486394e42ba517e628ce"></a><a name="a8037da561dfe486394e42ba517e628ce"></a>cn=root,dc=hadoop,dc=com</p>
</td>
<td class="cellrowborder" valign="top" width="14.580000000000002%" headers="mcps1.1.5.1.3 "><p id="a454eb003f619409b8c70325cc566d044"><a name="a454eb003f619409b8c70325cc566d044"></a><a name="a454eb003f619409b8c70325cc566d044"></a>LdapChangeMe@123</p>
</td>
<td class="cellrowborder" valign="top" width="39.22%" headers="mcps1.1.5.1.4 "><p id="a86beaee1e8014c5081150f20bafa6e78"><a name="a86beaee1e8014c5081150f20bafa6e78"></a><a name="a86beaee1e8014c5081150f20bafa6e78"></a>Account that is used to add, delete, modify, and query the user information on OMS LDAP.</p>
</td>
</tr>
<tr id="row52698596154811"><td class="cellrowborder" valign="top" width="20.47%" headers="mcps1.1.5.1.1 "><p id="p40727896154811"><a name="p40727896154811"></a><a name="p40727896154811"></a>LDAP user</p>
</td>
<td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.1.5.1.2 "><p id="p10625243154811"><a name="p10625243154811"></a><a name="p10625243154811"></a>cn=pg_search_dn,ou=Users,dc=hadoop,dc=com</p>
</td>
<td class="cellrowborder" valign="top" width="14.580000000000002%" headers="mcps1.1.5.1.3 "><p id="p55338392154811"><a name="p55338392154811"></a><a name="p55338392154811"></a>pg_search_dn@123</p>
</td>
<td class="cellrowborder" valign="top" width="39.22%" headers="mcps1.1.5.1.4 "><p id="p53224757154811"><a name="p53224757154811"></a><a name="p53224757154811"></a>User that is used to query information about users and user groups on LDAP.</p>
</td>
</tr>
<tr id="row4084686154811"><td class="cellrowborder" valign="top" width="20.47%" headers="mcps1.1.5.1.1 "><p id="p62424135154811"><a name="p62424135154811"></a><a name="p62424135154811"></a>OMS LDAP user</p>
</td>
<td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.1.5.1.2 "><p id="p23190173154811"><a name="p23190173154811"></a><a name="p23190173154811"></a>cn=pg_search_dn,ou=Users,dc=hadoop,dc=com</p>
</td>
<td class="cellrowborder" valign="top" width="14.580000000000002%" headers="mcps1.1.5.1.3 "><p id="p66464695154811"><a name="p66464695154811"></a><a name="p66464695154811"></a>pg_search_dn@123</p>
</td>
<td class="cellrowborder" valign="top" width="39.22%" headers="mcps1.1.5.1.4 "><p id="p14931197154811"><a name="p14931197154811"></a><a name="p14931197154811"></a>User that is used to query information about users and user groups on OMS LDAP.</p>
</td>
</tr>
<tr id="row98931555131414"><td class="cellrowborder" rowspan="2" valign="top" width="20.47%" headers="mcps1.1.5.1.1 "><p id="p13243516155"><a name="p13243516155"></a><a name="p13243516155"></a>LDAP administrator account</p>
</td>
<td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.1.5.1.2 "><p id="p2089315541419"><a name="p2089315541419"></a><a name="p2089315541419"></a>cn=krbkdc,ou=Users,dc=hadoop,dc=com</p>
</td>
<td class="cellrowborder" valign="top" width="14.580000000000002%" headers="mcps1.1.5.1.3 "><p id="p138931755101410"><a name="p138931755101410"></a><a name="p138931755101410"></a>LdapChangeMe@123</p>
</td>
<td class="cellrowborder" valign="top" width="39.22%" headers="mcps1.1.5.1.4 "><p id="p14893185517145"><a name="p14893185517145"></a><a name="p14893185517145"></a>Account that is used to query Kerberos component authentication account information.</p>
</td>
</tr>
<tr id="row215342471512"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p2154122420155"><a name="p2154122420155"></a><a name="p2154122420155"></a>cn=krbadmin,ou=Users,dc=hadoop,dc=com</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p315410248154"><a name="p315410248154"></a><a name="p315410248154"></a>LdapChangeMe@123</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p915413243159"><a name="p915413243159"></a><a name="p915413243159"></a>Account that is used to add, delete, or query Kerberos component authentication account information.</p>
</td>
</tr>
<tr id="r44fe146ebc1743d59eb877de26514d7c"><td class="cellrowborder" valign="top" width="20.47%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0039905375_p217528112845"><a name="en-us_topic_0039905375_p217528112845"></a><a name="en-us_topic_0039905375_p217528112845"></a>User for querying the MRS cluster</p>
</td>
<td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.1.5.1.2 "><p id="a3bab0559fefa4d4094e566cb634703d5"><a name="a3bab0559fefa4d4094e566cb634703d5"></a><a name="a3bab0559fefa4d4094e566cb634703d5"></a>executor</p>
</td>
<td class="cellrowborder" valign="top" width="14.580000000000002%" headers="mcps1.1.5.1.3 "><p id="a4d9068b06cb14a6c8918dc32c120817c"><a name="a4d9068b06cb14a6c8918dc32c120817c"></a><a name="a4d9068b06cb14a6c8918dc32c120817c"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" width="39.22%" headers="mcps1.1.5.1.4 "><p id="a5381e331a41845e3a2db9d36edc4e632"><a name="a5381e331a41845e3a2db9d36edc4e632"></a><a name="a5381e331a41845e3a2db9d36edc4e632"></a>User that is used to query clusters with Kerberos authentication enabled on the MRS management console.</p>
</td>
</tr>
<tr id="rbd52f8740f754627aa5120cd113f7c3b"><td class="cellrowborder" rowspan="29" valign="top" width="20.47%" headers="mcps1.1.5.1.1 "><p id="a6b1861956b614b7abce0638b7168a2da"><a name="a6b1861956b614b7abce0638b7168a2da"></a><a name="a6b1861956b614b7abce0638b7168a2da"></a>Component running user</p>
</td>
<td class="cellrowborder" valign="top" width="25.729999999999997%" headers="mcps1.1.5.1.2 "><p id="ae6f8ce9b35f44e14bc13f6e493bf8c2f"><a name="ae6f8ce9b35f44e14bc13f6e493bf8c2f"></a><a name="ae6f8ce9b35f44e14bc13f6e493bf8c2f"></a>hdfs</p>
</td>
<td class="cellrowborder" valign="top" width="14.580000000000002%" headers="mcps1.1.5.1.3 "><p id="abab8f70417904354ae3553cc75a4e8bc"><a name="abab8f70417904354ae3553cc75a4e8bc"></a><a name="abab8f70417904354ae3553cc75a4e8bc"></a>Hdfs@123</p>
</td>
<td class="cellrowborder" valign="top" width="39.22%" headers="mcps1.1.5.1.4 "><p id="adab5d2371c174e4ab68bbf0737afed10"><a name="adab5d2371c174e4ab68bbf0737afed10"></a><a name="adab5d2371c174e4ab68bbf0737afed10"></a>HDFS system administrator who has the following permission:</p>
<a name="ob0b47ccbe4dd4b2f8b209864af6c17b4"></a><a name="ob0b47ccbe4dd4b2f8b209864af6c17b4"></a><ol id="ob0b47ccbe4dd4b2f8b209864af6c17b4"><li>File system operation permission:<a name="ua2c969d05ac144119ba398aa59d02edc"></a><a name="ua2c969d05ac144119ba398aa59d02edc"></a><ul id="ua2c969d05ac144119ba398aa59d02edc"><li>Views, modifies, and creates files.</li><li>Views and creates directories.</li><li>Views and modifies the groups where files belong.</li><li>Views and sets disk quotas of users</li></ul>
</li></ol>
<a name="o2028454f95964de0a29d3ca2bd29fcb6"></a><a name="o2028454f95964de0a29d3ca2bd29fcb6"></a><ol id="o2028454f95964de0a29d3ca2bd29fcb6"><li>HDFS management operation permission:<a name="ua69a5726bafb45609688d1d190cf2a8e"></a><a name="ua69a5726bafb45609688d1d190cf2a8e"></a><ul id="ua69a5726bafb45609688d1d190cf2a8e"><li>Views the WebUI status.</li><li>Views and sets the active and standby HDFS status.</li><li>Enters and exits HDFS in security mode.</li><li>Checks HDFS.</li></ul>
</li></ol>
</td>
</tr>
<tr id="r9e56bcece932436a934790ce274a7fac"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="aa7034d596a3a4b85b24a3343043db53e"><a name="aa7034d596a3a4b85b24a3343043db53e"></a><a name="aa7034d596a3a4b85b24a3343043db53e"></a>hbase</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="a8090bc36041a4eaf91385b971a1afd53"><a name="a8090bc36041a4eaf91385b971a1afd53"></a><a name="a8090bc36041a4eaf91385b971a1afd53"></a>Hbase@123</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="acad723fb9f8041958a888909b0720d05"><a name="acad723fb9f8041958a888909b0720d05"></a><a name="acad723fb9f8041958a888909b0720d05"></a>HBase system administrator who has the following permission:</p>
<a name="u0174290cb4964017883fe4d8bcb8fd4f"></a><a name="u0174290cb4964017883fe4d8bcb8fd4f"></a><ul id="u0174290cb4964017883fe4d8bcb8fd4f"><li>Cluster management permission: Enables and disables tables, and triggers MajorCompact and Access Control List (ACL).</li><li>Grants and reclaims permission, and shuts down the cluster.</li><li>Table management permission: Creates, modifies, and deletes tables.</li><li>Data management permission: Reads and writes table-, column family-, and column-level data.</li><li>Accesses the HBase WebUI.</li></ul>
</td>
</tr>
<tr id="rf0a089a2264b4ddf8eaa35b67787d442"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="ae0630d3734d54d25a33820eeb8730663"><a name="ae0630d3734d54d25a33820eeb8730663"></a><a name="ae0630d3734d54d25a33820eeb8730663"></a>mapred</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="a5a05cdf8febe4b3c9d43420c76ba6fe3"><a name="a5a05cdf8febe4b3c9d43420c76ba6fe3"></a><a name="a5a05cdf8febe4b3c9d43420c76ba6fe3"></a>Mapred@123</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="a99d3920ddc9b40c98dee1276570f0d59"><a name="a99d3920ddc9b40c98dee1276570f0d59"></a><a name="a99d3920ddc9b40c98dee1276570f0d59"></a>MapReduce system administrator who has the following permission:</p>
<a name="u48def32f3a614885957762582b7c84e1"></a><a name="u48def32f3a614885957762582b7c84e1"></a><ul id="u48def32f3a614885957762582b7c84e1"><li>Submits, stops, and views MapReduce tasks.</li><li>Modifies the Yarn configuration parameters.</li><li>Accesses the Yarn and MapReduce WebUI.</li></ul>
</td>
</tr>
<tr id="r5f6ba07f2e3f4c41856d0ad54732f313"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="afc2bec6823284fe3aeea6df27ddbe1fe"><a name="afc2bec6823284fe3aeea6df27ddbe1fe"></a><a name="afc2bec6823284fe3aeea6df27ddbe1fe"></a>spark</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="a6e3a2ee65ba34cf290fcc1cad056c197"><a name="a6e3a2ee65ba34cf290fcc1cad056c197"></a><a name="a6e3a2ee65ba34cf290fcc1cad056c197"></a>Spark@123</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="a4aedb73d5b3c465b938c5280f04f7223"><a name="a4aedb73d5b3c465b938c5280f04f7223"></a><a name="a4aedb73d5b3c465b938c5280f04f7223"></a>Spark system administrator who has the following permission:</p>
<a name="u91ff2e2a92e34888a0d969ba24967754"></a><a name="u91ff2e2a92e34888a0d969ba24967754"></a><ul id="u91ff2e2a92e34888a0d969ba24967754"><li>Accesses the Spark WebUI.</li><li>Submits Spark tasks.</li></ul>
</td>
</tr>
<tr id="r6003940d73c64d0e8b3e88e543915cc0"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0039905375_p772789692452"><a name="en-us_topic_0039905375_p772789692452"></a><a name="en-us_topic_0039905375_p772789692452"></a>oms/manager</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="a3f51bf4e40c74f149e9bb91641564fdd"><a name="a3f51bf4e40c74f149e9bb91641564fdd"></a><a name="a3f51bf4e40c74f149e9bb91641564fdd"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0039905375_p475841792452"><a name="en-us_topic_0039905375_p475841792452"></a><a name="en-us_topic_0039905375_p475841792452"></a>Controller and NodeAgent authentication user who has the permission of <strong id="a6179b962219c4e50b6ec2cfd73b3916f"><a name="a6179b962219c4e50b6ec2cfd73b3916f"></a><a name="a6179b962219c4e50b6ec2cfd73b3916f"></a>supergroup</strong></p>
</td>
</tr>
<tr id="rad962e280bf9409a8bf218d0d2ca1f2d"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="a37f463de33ed4f9193a54d328d950121"><a name="a37f463de33ed4f9193a54d328d950121"></a><a name="a37f463de33ed4f9193a54d328d950121"></a>backup/manager</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="aba307a8fd1a94a7792140f06bae2277a"><a name="aba307a8fd1a94a7792140f06bae2277a"></a><a name="aba307a8fd1a94a7792140f06bae2277a"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0039905375_p387575093512"><a name="en-us_topic_0039905375_p387575093512"></a><a name="en-us_topic_0039905375_p387575093512"></a>User who runs backup and recovery tasks and has the permission of <strong id="aa4bfe002674b4b649e5064ff783c54f3"><a name="aa4bfe002674b4b649e5064ff783c54f3"></a><a name="aa4bfe002674b4b649e5064ff783c54f3"></a>supergroup</strong></p>
</td>
</tr>
<tr id="rc20bc2537dd5415f985ba0ed6e56b0f3"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0039905375_p325794593512"><a name="en-us_topic_0039905375_p325794593512"></a><a name="en-us_topic_0039905375_p325794593512"></a>hdfs/hadoop.hadoop.com</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="a067ecf4237fa435f90978a193ead14ca"><a name="a067ecf4237fa435f90978a193ead14ca"></a><a name="a067ecf4237fa435f90978a193ead14ca"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="a7ada639f1a964d039bc3e3f86851f898"><a name="a7ada639f1a964d039bc3e3f86851f898"></a><a name="a7ada639f1a964d039bc3e3f86851f898"></a>HDFS system startup user who has the following permission:</p>
<a name="oa58f1072108847dbbe79ec3af02dfafd"></a><a name="oa58f1072108847dbbe79ec3af02dfafd"></a><ol id="oa58f1072108847dbbe79ec3af02dfafd"><li>File system operation permission:<a name="u9b1ca89767f84408a657e52bda628739"></a><a name="u9b1ca89767f84408a657e52bda628739"></a><ul id="u9b1ca89767f84408a657e52bda628739"><li>Views, modifies, and creates files.</li><li>Views and creates directories.</li><li>Views and modifies the groups where files belong.</li><li>Views and sets disk quotas of users.</li></ul>
</li></ol>
<a name="o7da3b78d745a47a49b48299ae9eb7e93"></a><a name="o7da3b78d745a47a49b48299ae9eb7e93"></a><ol id="o7da3b78d745a47a49b48299ae9eb7e93"><li>HDFS management operation permission:<a name="u5d3440ddb70649f3b54a7b2b531880a4"></a><a name="u5d3440ddb70649f3b54a7b2b531880a4"></a><ul id="u5d3440ddb70649f3b54a7b2b531880a4"><li>Views the WebUI status.</li><li>Views and sets the active and standby HDFS status.</li><li>Enters and exits HDFS in security mode.</li><li>Checks HDFS.</li></ul>
</li></ol>
</td>
</tr>
<tr id="rdd2fa180e5914c4294ba001b9955fa2c"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="a72a41b8b335c4a6da0b41d263d83c92b"><a name="a72a41b8b335c4a6da0b41d263d83c92b"></a><a name="a72a41b8b335c4a6da0b41d263d83c92b"></a>mapred/hadoop.hadoop.com</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="a8c531e247c85485fb9e6f6a264ad1d66"><a name="a8c531e247c85485fb9e6f6a264ad1d66"></a><a name="a8c531e247c85485fb9e6f6a264ad1d66"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="a464a61136df04c2799c0153abc9df9f4"><a name="a464a61136df04c2799c0153abc9df9f4"></a><a name="a464a61136df04c2799c0153abc9df9f4"></a>MapReduce system startup user who has the following permission:</p>
<a name="ubc4ee8cc08e1485186d2c019e342c81b"></a><a name="ubc4ee8cc08e1485186d2c019e342c81b"></a><ul id="ubc4ee8cc08e1485186d2c019e342c81b"><li>Submits, stops, and views MapReduce tasks.</li><li>Modifies the Yarn configuration parameters.</li></ul>
</td>
</tr>
<tr id="rb42b3a0329e14c75b1fa4d0d2bbc06fa"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="afd42c432a3754e3980829a5122fcab56"><a name="afd42c432a3754e3980829a5122fcab56"></a><a name="afd42c432a3754e3980829a5122fcab56"></a>mr_zk/hadoop.hadoop.com</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="a3cd62cf3cccb4da891b62e4072a023f4"><a name="a3cd62cf3cccb4da891b62e4072a023f4"></a><a name="a3cd62cf3cccb4da891b62e4072a023f4"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0039905375_p798294693512"><a name="en-us_topic_0039905375_p798294693512"></a><a name="en-us_topic_0039905375_p798294693512"></a>User used for MapReduce to access ZooKeeper</p>
</td>
</tr>
<tr id="r9112207c8e5c4c2a83c95183d9faa964"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="aee7305bd33054c85b6ef9884d93473fd"><a name="aee7305bd33054c85b6ef9884d93473fd"></a><a name="aee7305bd33054c85b6ef9884d93473fd"></a>hbase/hadoop.hadoop.com</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="ac2c58c18f5f147a8813a1e3df8df1c78"><a name="ac2c58c18f5f147a8813a1e3df8df1c78"></a><a name="ac2c58c18f5f147a8813a1e3df8df1c78"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0039905375_p381898593544"><a name="en-us_topic_0039905375_p381898593544"></a><a name="en-us_topic_0039905375_p381898593544"></a>User used for the authentication between internal components during the HBase system startup</p>
</td>
</tr>
<tr id="ra8e49db2684842758415e59b39909815"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0039905375_p185469193544"><a name="en-us_topic_0039905375_p185469193544"></a><a name="en-us_topic_0039905375_p185469193544"></a>hbase/zkclient.hadoop.com</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="ab689935452c440818a6f3a157c222919"><a name="ab689935452c440818a6f3a157c222919"></a><a name="ab689935452c440818a6f3a157c222919"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="a1ac0a20ec5034c87aea9916f49f5d033"><a name="a1ac0a20ec5034c87aea9916f49f5d033"></a><a name="a1ac0a20ec5034c87aea9916f49f5d033"></a>User used for HBase to perform ZooKeeper authentication in a cluster in security mode</p>
</td>
</tr>
<tr id="r67510b818766461dbfb4d4634799b9ed"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="a454e41f7f7c04d75955f589b559131a1"><a name="a454e41f7f7c04d75955f589b559131a1"></a><a name="a454e41f7f7c04d75955f589b559131a1"></a>thrift/hadoop.hadoop.com</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="a2ac133a4c41543bf80c22c57e1dc749c"><a name="a2ac133a4c41543bf80c22c57e1dc749c"></a><a name="a2ac133a4c41543bf80c22c57e1dc749c"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="afcc446791cd443bea12cc63f871d0495"><a name="afcc446791cd443bea12cc63f871d0495"></a><a name="afcc446791cd443bea12cc63f871d0495"></a>ThriftServer system startup user</p>
</td>
</tr>
<tr id="rf349690b1f4c4c4ba172de6b4e8a64a5"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="a8467db39e63e4ac681823a3c9bd94a52"><a name="a8467db39e63e4ac681823a3c9bd94a52"></a><a name="a8467db39e63e4ac681823a3c9bd94a52"></a>thrift/<i><span class="varname" id="v695b554c437c4153b0e524bde3d90038"><a name="v695b554c437c4153b0e524bde3d90038"></a><a name="v695b554c437c4153b0e524bde3d90038"></a>&lt;hostname&gt;</span></i></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0039905375_p154824593544"><a name="en-us_topic_0039905375_p154824593544"></a><a name="en-us_topic_0039905375_p154824593544"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="ac730ad75023547e2be514cf72c63fc95"><a name="ac730ad75023547e2be514cf72c63fc95"></a><a name="ac730ad75023547e2be514cf72c63fc95"></a>User used for the ThriftServer system to access HBase. This user has the permission to read, write, execute, create, and manage all HBase NameSpaces and tables. <i><span class="varname" id="v40816d31f13d46739524b3adcc6ab1c3"><a name="v40816d31f13d46739524b3adcc6ab1c3"></a><a name="v40816d31f13d46739524b3adcc6ab1c3"></a>&lt;hostname&gt;</span></i> specifies the host name of the node where ThriftServer is installed.</p>
</td>
</tr>
<tr id="r9631b9ccff5e41768314c351518c187d"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0039905375_p337919093544"><a name="en-us_topic_0039905375_p337919093544"></a><a name="en-us_topic_0039905375_p337919093544"></a>hive/hadoop.hadoop.com</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="a6ed1bca746ea4790893f616c8fea338c"><a name="a6ed1bca746ea4790893f616c8fea338c"></a><a name="a6ed1bca746ea4790893f616c8fea338c"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="acae9136c20fb47f083d3f41da74fd2db"><a name="acae9136c20fb47f083d3f41da74fd2db"></a><a name="acae9136c20fb47f083d3f41da74fd2db"></a>User used for the authentication between internal components during the Hive system startup. The user has the following permission:</p>
<a name="oeb5af44004cd44149fd8f6c84bdd904d"></a><a name="oeb5af44004cd44149fd8f6c84bdd904d"></a><ol id="oeb5af44004cd44149fd8f6c84bdd904d"><li>Hive administrator permission:<a name="ubbdc487facee4c6ea119af23e401eac6"></a><a name="ubbdc487facee4c6ea119af23e401eac6"></a><ul id="ubbdc487facee4c6ea119af23e401eac6"><li>Creates, deletes, and modifies databases.</li><li>Creates, queries, modifies, and deletes tables.</li><li>Queries, inserts, and loads data.</li></ul>
</li><li>HDFS file operation permission:<a name="u87fe7fad9eca4b7bb87e49d4222db205"></a><a name="u87fe7fad9eca4b7bb87e49d4222db205"></a><ul id="u87fe7fad9eca4b7bb87e49d4222db205"><li>Views, modifies, and creates files.</li><li>Views and creates directories.</li><li>Views and modifies the groups where files belong.</li></ul>
</li><li>Submits and stops MapReduce jobs.</li></ol>
</td>
</tr>
<tr id="r967484862fc64f73aecc7ed573c5c8b8"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="aead8f0fe055045738831680c176f3cde"><a name="aead8f0fe055045738831680c176f3cde"></a><a name="aead8f0fe055045738831680c176f3cde"></a>spark/hadoop.hadoop.com</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="a1453ca8dac2f41c09f3c31399c1f4f40"><a name="a1453ca8dac2f41c09f3c31399c1f4f40"></a><a name="a1453ca8dac2f41c09f3c31399c1f4f40"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0039905375_p248978693544"><a name="en-us_topic_0039905375_p248978693544"></a><a name="en-us_topic_0039905375_p248978693544"></a>Spark system startup user</p>
</td>
</tr>
<tr id="rc9ad6a3ada5f4bd1a9db0d297de39a24"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="aec2690381750432b95956927512b8d32"><a name="aec2690381750432b95956927512b8d32"></a><a name="aec2690381750432b95956927512b8d32"></a>spark_zk/hadoop.hadoop.com</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="ad8f8603299cb4600b4e638905a21e265"><a name="ad8f8603299cb4600b4e638905a21e265"></a><a name="ad8f8603299cb4600b4e638905a21e265"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="aa92001b8036a4f30b49d4fe21e02f3d7"><a name="aa92001b8036a4f30b49d4fe21e02f3d7"></a><a name="aa92001b8036a4f30b49d4fe21e02f3d7"></a>User used for Spark to access ZooKeeper</p>
</td>
</tr>
<tr id="r3b5cefe32d4844e8a652eb4fe2d9a815"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="a65c4753a6cf5415986159dec2fe0379b"><a name="a65c4753a6cf5415986159dec2fe0379b"></a><a name="a65c4753a6cf5415986159dec2fe0379b"></a>zookeeper/hadoop.hadoop.com</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="a9a2ec9437014444380f7428276e23798"><a name="a9a2ec9437014444380f7428276e23798"></a><a name="a9a2ec9437014444380f7428276e23798"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0039905375_p752336993641"><a name="en-us_topic_0039905375_p752336993641"></a><a name="en-us_topic_0039905375_p752336993641"></a>ZooKeeper system startup user</p>
</td>
</tr>
<tr id="ra2aba08e875a4b228383f9b3af490813"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="a93b5894a76c44ed7907c386a79ed6637"><a name="a93b5894a76c44ed7907c386a79ed6637"></a><a name="a93b5894a76c44ed7907c386a79ed6637"></a>zkcli/hadoop.hadoop.com</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="a1b39365849fa4431aff4683648b7820f"><a name="a1b39365849fa4431aff4683648b7820f"></a><a name="a1b39365849fa4431aff4683648b7820f"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="a50c127ef53ba4390a1039b0cd465f2dc"><a name="a50c127ef53ba4390a1039b0cd465f2dc"></a><a name="a50c127ef53ba4390a1039b0cd465f2dc"></a>ZooKeeper server login user</p>
</td>
</tr>
<tr id="r160a006e21e648e8afdab5d3b78d67f1"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="a178f6efbcded4964b897014519e351e3"><a name="a178f6efbcded4964b897014519e351e3"></a><a name="a178f6efbcded4964b897014519e351e3"></a>kafka/hadoop.hadoop.com</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0039905375_p629863094333"><a name="en-us_topic_0039905375_p629863094333"></a><a name="en-us_topic_0039905375_p629863094333"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="aa7d6c83784384c6882acffdf3d477372"><a name="aa7d6c83784384c6882acffdf3d477372"></a><a name="aa7d6c83784384c6882acffdf3d477372"></a>User used for security authentication for Kafka.</p>
</td>
</tr>
<tr id="r79cf7ef9ea364452b8e37f6dc8d7fbc9"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="a01a33de0c9e8407a85b8a701124a205c"><a name="a01a33de0c9e8407a85b8a701124a205c"></a><a name="a01a33de0c9e8407a85b8a701124a205c"></a>storm/hadoop.hadoop.com</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="aedf96e81ed8d42139b59887feea142ef"><a name="aedf96e81ed8d42139b59887feea142ef"></a><a name="aedf96e81ed8d42139b59887feea142ef"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="ada8a983c530a4c7abcc1bca92ef40f6e"><a name="ada8a983c530a4c7abcc1bca92ef40f6e"></a><a name="ada8a983c530a4c7abcc1bca92ef40f6e"></a>Storm system startup user.</p>
</td>
</tr>
<tr id="r9f856fcfd1ab4d2b9a1b7963b03baff4"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="a1b7caa7bcc9e4d698053fc8ee4ae6f01"><a name="a1b7caa7bcc9e4d698053fc8ee4ae6f01"></a><a name="a1b7caa7bcc9e4d698053fc8ee4ae6f01"></a>storm_zk/hadoop.hadoop.com</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="ab0bb46c3ec414c9594c713f79cd498ad"><a name="ab0bb46c3ec414c9594c713f79cd498ad"></a><a name="ab0bb46c3ec414c9594c713f79cd498ad"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="a6726797604eb424584d52051f9287be3"><a name="a6726797604eb424584d52051f9287be3"></a><a name="a6726797604eb424584d52051f9287be3"></a>User for the Worker process to access ZooKeeper.</p>
</td>
</tr>
<tr id="row2305167092212"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p5524595192212"><a name="p5524595192212"></a><a name="p5524595192212"></a><span id="ph2198713592237"><a name="ph2198713592237"></a><a name="ph2198713592237"></a>loader/hadoop.hadoop.com</span></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p4573700892212"><a name="p4573700892212"></a><a name="p4573700892212"></a><span id="ph1758864992247"><a name="ph1758864992247"></a><a name="ph1758864992247"></a>Randomly generated by the system</span></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p1371016292212"><a name="p1371016292212"></a><a name="p1371016292212"></a><span id="ph6653344892256"><a name="ph6653344892256"></a><a name="ph6653344892256"></a>User for Loader system startup and Kerberos authentication.</span></p>
</td>
</tr>
<tr id="row61208173184010"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p14002647184010"><a name="p14002647184010"></a><a name="p14002647184010"></a><span id="ph15187733184030"><a name="ph15187733184030"></a><a name="ph15187733184030"></a>HTTP/&lt;hostname&gt;</span></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p60472661184010"><a name="p60472661184010"></a><a name="p60472661184010"></a><span id="ph15311528184036"><a name="ph15311528184036"></a><a name="ph15311528184036"></a>Randomly generated by the system</span></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p66447383184010"><a name="p66447383184010"></a><a name="p66447383184010"></a><span id="ph35684309184041"><a name="ph35684309184041"></a><a name="ph35684309184041"></a>Used to connect to the HTTP interface of each component. &lt;hostname&gt; indicates the name of the node in the cluster.</span></p>
</td>
</tr>
<tr id="row275740992216"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p2202360192216"><a name="p2202360192216"></a><a name="p2202360192216"></a><span id="ph4076392692310"><a name="ph4076392692310"></a><a name="ph4076392692310"></a>flume</span></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p3908127492216"><a name="p3908127492216"></a><a name="p3908127492216"></a><span id="ph1801033992321"><a name="ph1801033992321"></a><a name="ph1801033992321"></a>Randomly generated by the system</span></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p1146659592216"><a name="p1146659592216"></a><a name="p1146659592216"></a><span id="ph3205224892331"><a name="ph3205224892331"></a><a name="ph3205224892331"></a>User for Flume system startup and HDFS and Hive access. The user has read and write permission of the HDFS directory /flume.</span></p>
</td>
</tr>
<tr id="rc9a1f3fe49344f47baa068c63c8a938f"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="a51608ca36bed4dfbb3ed7f8712c7056c"><a name="a51608ca36bed4dfbb3ed7f8712c7056c"></a><a name="a51608ca36bed4dfbb3ed7f8712c7056c"></a>check_ker_M</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="a86ddc87ae8e240998e06dcaf4662a03d"><a name="a86ddc87ae8e240998e06dcaf4662a03d"></a><a name="a86ddc87ae8e240998e06dcaf4662a03d"></a>Randomly generated by the system</p>
</td>
<td class="cellrowborder" rowspan="5" valign="top" headers="mcps1.1.5.1.3 "><p id="a7649b229f5094bb6bae88cd2dd5a6059"><a name="a7649b229f5094bb6bae88cd2dd5a6059"></a><a name="a7649b229f5094bb6bae88cd2dd5a6059"></a>Kerberos internal functional user. This user cannot be deleted, and its password cannot be changed. This internal account cannot be used on the nodes where Kerberos service is not installed.</p>
</td>
</tr>
<tr id="rdc00bf8b22864a198f7a9bc64a13e8ba"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="af330c4b5b05d4932988422f0298e495a"><a name="af330c4b5b05d4932988422f0298e495a"></a><a name="af330c4b5b05d4932988422f0298e495a"></a>K/M</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="a20fa0b8f8269419d9e6808d98f5b1486"><a name="a20fa0b8f8269419d9e6808d98f5b1486"></a><a name="a20fa0b8f8269419d9e6808d98f5b1486"></a>Randomly generated by the system</p>
</td>
</tr>
<tr id="rc74a3d9e8e2f497f8821c372298038a1"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="a53523362985b4704a0de04397c0f1c52"><a name="a53523362985b4704a0de04397c0f1c52"></a><a name="a53523362985b4704a0de04397c0f1c52"></a>kadmin/changepw</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="ab4e0365e74a74993a68a093443fdbfb0"><a name="ab4e0365e74a74993a68a093443fdbfb0"></a><a name="ab4e0365e74a74993a68a093443fdbfb0"></a>Randomly generated by the system</p>
</td>
</tr>
<tr id="r54986a2dca144fbba9fe07ce95957d40"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="a0e5200c61ef74916a73762ac3a91c302"><a name="a0e5200c61ef74916a73762ac3a91c302"></a><a name="a0e5200c61ef74916a73762ac3a91c302"></a>kadmin/history</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="a6514afb23492451d866bd5ebb5b68438"><a name="a6514afb23492451d866bd5ebb5b68438"></a><a name="a6514afb23492451d866bd5ebb5b68438"></a>Randomly generated by the system</p>
</td>
</tr>
<tr id="r010b7248d35b416391763b3180f3570b"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="a619035fbd4344a1aa2e616ed61e559d8"><a name="a619035fbd4344a1aa2e616ed61e559d8"></a><a name="a619035fbd4344a1aa2e616ed61e559d8"></a>krbtgt/HADOOP.COM</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="aef758d2b15634783a81a3a4bb9fa095f"><a name="aef758d2b15634783a81a3a4bb9fa095f"></a><a name="aef758d2b15634783a81a3a4bb9fa095f"></a>Randomly generated by the system</p>
</td>
</tr>
</tbody>
</table>

## User Group Information<a name="s6e221a0adafd49bb97f0810c138ec055"></a>

<a name="tb35bcee351694e1bb73789c1253d6811"></a>
<table><thead align="left"><tr id="r987709d0748e4e5f83f89d7f6ed1e27f"><th class="cellrowborder" valign="top" width="35%" id="mcps1.1.3.1.1"><p id="a4340ece9f53047d18fb7e328de81cf95"><a name="a4340ece9f53047d18fb7e328de81cf95"></a><a name="a4340ece9f53047d18fb7e328de81cf95"></a>Default User Group</p>
</th>
<th class="cellrowborder" valign="top" width="65%" id="mcps1.1.3.1.2"><p id="en-us_topic_0039905375_p96478795542"><a name="en-us_topic_0039905375_p96478795542"></a><a name="en-us_topic_0039905375_p96478795542"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rfcd21c0629c24fd7934437cacc355527"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0039905375_p917078395542"><a name="en-us_topic_0039905375_p917078395542"></a><a name="en-us_topic_0039905375_p917078395542"></a>hadoop</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="a61202b63051e4931b81b9818eb1507d1"><a name="a61202b63051e4931b81b9818eb1507d1"></a><a name="a61202b63051e4931b81b9818eb1507d1"></a>Users added to this user group have the permission to submit tasks to all Yarn queues.</p>
</td>
</tr>
<tr id="r9fa767ba318a4546b03a6632fc439d8e"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="a93b7d82f5d7046f9b0f118abb5f22181"><a name="a93b7d82f5d7046f9b0f118abb5f22181"></a><a name="a93b7d82f5d7046f9b0f118abb5f22181"></a>hbase</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="ac46ebbe1a0a94e77aba5683eb7893629"><a name="ac46ebbe1a0a94e77aba5683eb7893629"></a><a name="ac46ebbe1a0a94e77aba5683eb7893629"></a>Common user group. Users added to this user group will not have any additional rights.</p>
</td>
</tr>
<tr id="r7fb1820cd4264c908714562f9a6bdf31"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="a206690dae1354d0199e8997a6f0d5825"><a name="a206690dae1354d0199e8997a6f0d5825"></a><a name="a206690dae1354d0199e8997a6f0d5825"></a>hive</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="a5b9440fce176408e9297e489c7ca7082"><a name="a5b9440fce176408e9297e489c7ca7082"></a><a name="a5b9440fce176408e9297e489c7ca7082"></a>Users added to this user group can use Hive.</p>
</td>
</tr>
<tr id="r198198524e424e79bbf9c59b2bf375a5"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0039905375_p794038695542"><a name="en-us_topic_0039905375_p794038695542"></a><a name="en-us_topic_0039905375_p794038695542"></a>spark</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="ae3e8786e3de4469ba9551f74fe74ccd1"><a name="ae3e8786e3de4469ba9551f74fe74ccd1"></a><a name="ae3e8786e3de4469ba9551f74fe74ccd1"></a>Common user group. Users added to this user group will not have any additional rights.</p>
</td>
</tr>
<tr id="r91420ca146f04d4eba22a5a93a85c28c"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="ad3f10d002ee048219e13d0adce087374"><a name="ad3f10d002ee048219e13d0adce087374"></a><a name="ad3f10d002ee048219e13d0adce087374"></a>supergroup</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="a8a71fd0b92a5410d91f2e8e732570f5a"><a name="a8a71fd0b92a5410d91f2e8e732570f5a"></a><a name="a8a71fd0b92a5410d91f2e8e732570f5a"></a>Users added to this user group can have the administrator rights of HBase, HDFS, and Yarn and can use Hive.</p>
</td>
</tr>
<tr id="r20559f798db344168e829fd22bd75b8d"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="aa41728e2d3954d40953469697a38f18a"><a name="aa41728e2d3954d40953469697a38f18a"></a><a name="aa41728e2d3954d40953469697a38f18a"></a>check_sec_ldap</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="a295e4ace95d64d43b4e334a2940f99c6"><a name="a295e4ace95d64d43b4e334a2940f99c6"></a><a name="a295e4ace95d64d43b4e334a2940f99c6"></a>Used to test whether the active LDAP works properly. This user group is generated randomly in a test and automatically deleted after the test is complete. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="rb68b46311fd8429a81c55170b3bacf6c"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="ad84bebbee05b41d697e3967c711cafa9"><a name="ad84bebbee05b41d697e3967c711cafa9"></a><a name="ad84bebbee05b41d697e3967c711cafa9"></a>Manager_tenant_187</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0039905375_p311491895542"><a name="en-us_topic_0039905375_p311491895542"></a><a name="en-us_topic_0039905375_p311491895542"></a>Tenant system user group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="reb9bdd4a8c39450697af24c64dc5d857"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="a2f05fbcb9bee416fb7689f557a0ed71f"><a name="a2f05fbcb9bee416fb7689f557a0ed71f"></a><a name="a2f05fbcb9bee416fb7689f557a0ed71f"></a>System_administrator_186</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0039905375_p642151095542"><a name="en-us_topic_0039905375_p642151095542"></a><a name="en-us_topic_0039905375_p642151095542"></a>MRS cluster system administrator group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="r3fff0490ad034bde8cd3cec4364d35f0"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="abb83dfcde4b44780bf86fd7ecda22bae"><a name="abb83dfcde4b44780bf86fd7ecda22bae"></a><a name="abb83dfcde4b44780bf86fd7ecda22bae"></a>Manager_viewer_183</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="a29d687923ae24eda9d8163e7465a31d2"><a name="a29d687923ae24eda9d8163e7465a31d2"></a><a name="a29d687923ae24eda9d8163e7465a31d2"></a>MRS Manager system viewer group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="r3f63832d9d854c7c89a4605769a24cb3"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="aa4ba3ccb1cfa49e78c8ec7a1ec68d834"><a name="aa4ba3ccb1cfa49e78c8ec7a1ec68d834"></a><a name="aa4ba3ccb1cfa49e78c8ec7a1ec68d834"></a>Manager_operator_182</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0039905375_p26828595542"><a name="en-us_topic_0039905375_p26828595542"></a><a name="en-us_topic_0039905375_p26828595542"></a>MRS Manager system operator group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="r212ef45a17444d9a9147a844bcd85c66"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="ade940c17817643128152de3c9bd7ecea"><a name="ade940c17817643128152de3c9bd7ecea"></a><a name="ade940c17817643128152de3c9bd7ecea"></a>Manager_auditor_181</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="ac43a1317832347b586109d5694ff8a47"><a name="ac43a1317832347b586109d5694ff8a47"></a><a name="ac43a1317832347b586109d5694ff8a47"></a>MRS Manager system auditor group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="r3cfb6364a293426da53ed1f54aaf9924"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="a9df2ea47e161420d9a39d94322c451b2"><a name="a9df2ea47e161420d9a39d94322c451b2"></a><a name="a9df2ea47e161420d9a39d94322c451b2"></a>Manager_administrator_180</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="a053c274af45643f784399088b26d708a"><a name="a053c274af45643f784399088b26d708a"></a><a name="a053c274af45643f784399088b26d708a"></a>MRS Manager system administrator group. This is an internal system user group used only between components.</p>
</td>
</tr>
<tr id="r2507018770d3411aa486099ced6ddb45"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="a06425244781e42c09c9d6f197ea384eb"><a name="a06425244781e42c09c9d6f197ea384eb"></a><a name="a06425244781e42c09c9d6f197ea384eb"></a>compcommon</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="a96f208a451704fd2945f0aa706be1752"><a name="a96f208a451704fd2945f0aa706be1752"></a><a name="a96f208a451704fd2945f0aa706be1752"></a>MRS cluster internal group for accessing public cluster resources. All system users and system running users are added to this user group by default.</p>
</td>
</tr>
<tr id="r16b3dfae7356454696034db4a38c7ffd"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="a31b277cf57294914ab9202de1bd0b97e"><a name="a31b277cf57294914ab9202de1bd0b97e"></a><a name="a31b277cf57294914ab9202de1bd0b97e"></a>default_1000</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="a7f79520d0de04c81a587f1f1e470b959"><a name="a7f79520d0de04c81a587f1f1e470b959"></a><a name="a7f79520d0de04c81a587f1f1e470b959"></a>This group is created for tenants. Internal system user group, which is used only between components.</p>
</td>
</tr>
<tr id="rf70848a179a44a418458378f8b08c493"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0039905375_p862777094559"><a name="en-us_topic_0039905375_p862777094559"></a><a name="en-us_topic_0039905375_p862777094559"></a>kafka</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="a88df1be7d50944e780c2902833d30806"><a name="a88df1be7d50944e780c2902833d30806"></a><a name="a88df1be7d50944e780c2902833d30806"></a>Kafka common user group. A user added to this user group can access a topic only when a user in the kafkaadmin group grants the read and write permission of the topic to the user.</p>
</td>
</tr>
<tr id="rf5bbb35f34a14d3399bfa17c9dcadb4a"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="aacd9ca926bc842aa9420edde5a423b38"><a name="aacd9ca926bc842aa9420edde5a423b38"></a><a name="aacd9ca926bc842aa9420edde5a423b38"></a>kafkasuperuser</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="a4339322f870045b7bd8958cafbcea59c"><a name="a4339322f870045b7bd8958cafbcea59c"></a><a name="a4339322f870045b7bd8958cafbcea59c"></a>Users added to this user group have the read and write permission of all topics.</p>
</td>
</tr>
<tr id="re454f3833e4342a69721a15a0c91cb24"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="a7efa7a7555944d46ad793ea0e2fae089"><a name="a7efa7a7555944d46ad793ea0e2fae089"></a><a name="a7efa7a7555944d46ad793ea0e2fae089"></a>kafkaadmin</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="ab60594879e784d57ac8180205d426a1f"><a name="ab60594879e784d57ac8180205d426a1f"></a><a name="ab60594879e784d57ac8180205d426a1f"></a>Kafka administrator group. Users added to this user group have the rights to create, delete, authorize, read, and write all topics.</p>
</td>
</tr>
<tr id="ra6162d6bbdda412c9294155e644228fd"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="a9a62f457eb5d42fd851a0c1a898862c7"><a name="a9a62f457eb5d42fd851a0c1a898862c7"></a><a name="a9a62f457eb5d42fd851a0c1a898862c7"></a>storm</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="ae5f73cf2617545e08cd471b091d68759"><a name="ae5f73cf2617545e08cd471b091d68759"></a><a name="ae5f73cf2617545e08cd471b091d68759"></a>Users added to this user group can submit topologies and manage their own topologies.</p>
</td>
</tr>
<tr id="r4ab1a56b07af462b92f94cea900230b2"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.1.3.1.1 "><p id="a1604dda7c0644344a90fd2fb3230f381"><a name="a1604dda7c0644344a90fd2fb3230f381"></a><a name="a1604dda7c0644344a90fd2fb3230f381"></a>stormadmin</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.3.1.2 "><p id="a8424f2bae5df4c6691e1b720c5f1afe5"><a name="a8424f2bae5df4c6691e1b720c5f1afe5"></a><a name="a8424f2bae5df4c6691e1b720c5f1afe5"></a>Users added to this user group can have the storm administrator rights and can submit topologies and manage all topologies.</p>
</td>
</tr>
</tbody>
</table>

<a name="t3bcc98288aa14a72b5c077633bd640e0"></a>
<table><thead align="left"><tr id="r19d0a40ecee74498972725b7db32290c"><th class="cellrowborder" valign="top" width="35.449999999999996%" id="mcps1.1.3.1.1"><p id="af405fdce89414942a84d074e78d24824"><a name="af405fdce89414942a84d074e78d24824"></a><a name="af405fdce89414942a84d074e78d24824"></a>OS User Group</p>
</th>
<th class="cellrowborder" valign="top" width="64.55%" id="mcps1.1.3.1.2"><p id="aa86bfa20ab97450f91b12e2ab8cb674f"><a name="aa86bfa20ab97450f91b12e2ab8cb674f"></a><a name="aa86bfa20ab97450f91b12e2ab8cb674f"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r9da91b7c6cf34dd286dfdf54c8b82405"><td class="cellrowborder" valign="top" width="35.449999999999996%" headers="mcps1.1.3.1.1 "><p id="a4f0fa290da864bbe9ffd7825ee70910f"><a name="a4f0fa290da864bbe9ffd7825ee70910f"></a><a name="a4f0fa290da864bbe9ffd7825ee70910f"></a>wheel</p>
</td>
<td class="cellrowborder" valign="top" width="64.55%" headers="mcps1.1.3.1.2 "><p id="af42256d2e85d4b7182c48cf5b1f08d14"><a name="af42256d2e85d4b7182c48cf5b1f08d14"></a><a name="af42256d2e85d4b7182c48cf5b1f08d14"></a>Primary group of MRS internal running user <strong id="a7da972087e6e417cb9b1f6263be541f5"><a name="a7da972087e6e417cb9b1f6263be541f5"></a><a name="a7da972087e6e417cb9b1f6263be541f5"></a>omm</strong></p>
</td>
</tr>
<tr id="en-us_topic_0039905375_row7450595611"><td class="cellrowborder" valign="top" width="35.449999999999996%" headers="mcps1.1.3.1.1 "><p id="a5a814b7132cc4f6fa1b2cd80041b2f3f"><a name="a5a814b7132cc4f6fa1b2cd80041b2f3f"></a><a name="a5a814b7132cc4f6fa1b2cd80041b2f3f"></a>ficommon</p>
</td>
<td class="cellrowborder" valign="top" width="64.55%" headers="mcps1.1.3.1.2 "><p id="ab79e1b8ad84c480e91ad15d70baada66"><a name="ab79e1b8ad84c480e91ad15d70baada66"></a><a name="ab79e1b8ad84c480e91ad15d70baada66"></a>MRS cluster common group that corresponds to <strong id="en-us_topic_0039905375_b730495895611"><a name="en-us_topic_0039905375_b730495895611"></a><a name="en-us_topic_0039905375_b730495895611"></a>compcommon</strong> for accessing public cluster resource files stored in the OS</p>
</td>
</tr>
</tbody>
</table>

## Database Users<a name="seb9c44d5a0794b0f83adc3882e859eab"></a>

MRS cluster system database users contain OMS database users and DBService database users.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Do not delete the following database users. Otherwise, the cluster or services may not work properly.  

<a name="t73521059ee584b4f921e2e8910568d40"></a>
<table><thead align="left"><tr id="ra4a910d43f8a4c00bb16b8ccf861beef"><th class="cellrowborder" valign="top" width="21.11788821117888%" id="mcps1.1.5.1.1"><p id="en-us_topic_0039905375_p845453895648"><a name="en-us_topic_0039905375_p845453895648"></a><a name="en-us_topic_0039905375_p845453895648"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="21.11788821117888%" id="mcps1.1.5.1.2"><p id="a04f4805bf83a417f8e52802b06147539"><a name="a04f4805bf83a417f8e52802b06147539"></a><a name="a04f4805bf83a417f8e52802b06147539"></a>Default User</p>
</th>
<th class="cellrowborder" valign="top" width="20.727927207279272%" id="mcps1.1.5.1.3"><p id="en-us_topic_0039905375_p532192795648"><a name="en-us_topic_0039905375_p532192795648"></a><a name="en-us_topic_0039905375_p532192795648"></a>Initial Password</p>
</th>
<th class="cellrowborder" valign="top" width="37.03629637036296%" id="mcps1.1.5.1.4"><p id="a362119c87ae24116bbcb228ed3ab5efb"><a name="a362119c87ae24116bbcb228ed3ab5efb"></a><a name="a362119c87ae24116bbcb228ed3ab5efb"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rff164d8a88a742a4988cfa1ff3de817a"><td class="cellrowborder" rowspan="2" valign="top" width="21.11788821117888%" headers="mcps1.1.5.1.1 "><p id="a894a853295c3497ab84993ad4eca2748"><a name="a894a853295c3497ab84993ad4eca2748"></a><a name="a894a853295c3497ab84993ad4eca2748"></a>OMS database</p>
</td>
<td class="cellrowborder" valign="top" width="21.11788821117888%" headers="mcps1.1.5.1.2 "><p id="a7f8840b682e947d19df9ba46a80dc9f3"><a name="a7f8840b682e947d19df9ba46a80dc9f3"></a><a name="a7f8840b682e947d19df9ba46a80dc9f3"></a>ommdba</p>
</td>
<td class="cellrowborder" valign="top" width="20.727927207279272%" headers="mcps1.1.5.1.3 "><p id="aa515fd48bb3f4817b1661a27ca43d360"><a name="aa515fd48bb3f4817b1661a27ca43d360"></a><a name="aa515fd48bb3f4817b1661a27ca43d360"></a>dbChangeMe@123456</p>
</td>
<td class="cellrowborder" valign="top" width="37.03629637036296%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0039905375_p793760895648"><a name="en-us_topic_0039905375_p793760895648"></a><a name="en-us_topic_0039905375_p793760895648"></a>OMS database administrator who performs maintenance operations, such as creating, starting, and stopping applications</p>
</td>
</tr>
<tr id="r2a53dfd12c96483781008b7e781f648e"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="a791b8128cc4f4623aceef99cab9d3e17"><a name="a791b8128cc4f4623aceef99cab9d3e17"></a><a name="a791b8128cc4f4623aceef99cab9d3e17"></a>omm</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="a5449d726ead848f48763e77f272fc759"><a name="a5449d726ead848f48763e77f272fc759"></a><a name="a5449d726ead848f48763e77f272fc759"></a>ChangeMe@123456</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="a9b2bd9f62e1a4e7b909189f9e0831266"><a name="a9b2bd9f62e1a4e7b909189f9e0831266"></a><a name="a9b2bd9f62e1a4e7b909189f9e0831266"></a>User used for accessing OMS database data</p>
</td>
</tr>
<tr id="ra56556bbd4e54e48a9697fd234769ff5"><td class="cellrowborder" rowspan="4" valign="top" width="21.11788821117888%" headers="mcps1.1.5.1.1 "><p id="a57f9fe322de840328b395866eb0f0290"><a name="a57f9fe322de840328b395866eb0f0290"></a><a name="a57f9fe322de840328b395866eb0f0290"></a>DBService database</p>
</td>
<td class="cellrowborder" valign="top" width="21.11788821117888%" headers="mcps1.1.5.1.2 "><p id="aec08440729fe4a72b65dc09ed6f7fccd"><a name="aec08440729fe4a72b65dc09ed6f7fccd"></a><a name="aec08440729fe4a72b65dc09ed6f7fccd"></a>omm</p>
</td>
<td class="cellrowborder" valign="top" width="20.727927207279272%" headers="mcps1.1.5.1.3 "><p id="aaab30603db914d0fb35c5e53ce54f814"><a name="aaab30603db914d0fb35c5e53ce54f814"></a><a name="aaab30603db914d0fb35c5e53ce54f814"></a>dbserverAdmin@123</p>
</td>
<td class="cellrowborder" valign="top" width="37.03629637036296%" headers="mcps1.1.5.1.4 "><p id="aabef8f75b808428b9494926b692c8ccc"><a name="aabef8f75b808428b9494926b692c8ccc"></a><a name="aabef8f75b808428b9494926b692c8ccc"></a>Administrator of the GaussDB database in the DBService component</p>
</td>
</tr>
<tr id="ref87fbd680bf4c4784c749230cb91993"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="abfd42fde288f4e13aebfad0f1cfd55b1"><a name="abfd42fde288f4e13aebfad0f1cfd55b1"></a><a name="abfd42fde288f4e13aebfad0f1cfd55b1"></a>hive</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="aa80f530061b844c18916def9b6b1421a"><a name="aa80f530061b844c18916def9b6b1421a"></a><a name="aa80f530061b844c18916def9b6b1421a"></a>HiveUser@</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="a3a988c0eb9154fd590b8c002a29720b0"><a name="a3a988c0eb9154fd590b8c002a29720b0"></a><a name="a3a988c0eb9154fd590b8c002a29720b0"></a>User used for Hive to connect to the DBService database</p>
</td>
</tr>
<tr id="r5c2d8074b5bd46978a1afac836b54d5f"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0039905375_p139192711248"><a name="en-us_topic_0039905375_p139192711248"></a><a name="en-us_topic_0039905375_p139192711248"></a>hue</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="ac0c8f4d57907488999db7e61d0ac787f"><a name="ac0c8f4d57907488999db7e61d0ac787f"></a><a name="ac0c8f4d57907488999db7e61d0ac787f"></a>HueUser@123</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0039905375_p562858011248"><a name="en-us_topic_0039905375_p562858011248"></a><a name="en-us_topic_0039905375_p562858011248"></a>User used for Hue to connect to the DBService database</p>
</td>
</tr>
<tr id="row27618982141417"><td class="cellrowborder" valign="top" headers="mcps1.1.5.1.1 "><p id="p14208217141417"><a name="p14208217141417"></a><a name="p14208217141417"></a><span id="ph52726925141441"><a name="ph52726925141441"></a><a name="ph52726925141441"></a>sqoop</span></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.2 "><p id="p10014915141417"><a name="p10014915141417"></a><a name="p10014915141417"></a><span id="ph40047445141447"><a name="ph40047445141447"></a><a name="ph40047445141447"></a>SqoopUser@</span></p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.5.1.3 "><p id="p5901806141417"><a name="p5901806141417"></a><a name="p5901806141417"></a><span id="ph12287639101749"><a name="ph12287639101749"></a><a name="ph12287639101749"></a>User for Loader to connect to the DBService database</span></p>
</td>
</tr>
</tbody>
</table>

