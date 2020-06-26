# Using HBase from Scratch<a name="EN-US_TOPIC_0125375348"></a>

HBase is a scalable column-based distributed storage system. It features high reliability and high performance.

You can update the client on a Master node in the  **mrs\_20160907**  cluster. The client can be used to create a table, data can be inserted to, read, and deleted from the table, and the table can be modified and deleted.

## Background<a name="s6e8a8cc92729434eafb64c57d3082ef0"></a>

After an MRS cluster has been successfully created, the original client is by default stored in the  **/opt/client**  directory on all nodes in the cluster. Before using the client, download the client file, update the client, and locate the active management node of MRS Manager.

For example, if a user develops an application to manage information about users who use service A in an enterprise, the operation processes of service A using the HBase client are as follows:

-   Create a user information table.
-   Add diplomas and titles of users to the table.
-   Query usernames and addresses by user ID.
-   Query information by username.
-   Deregister users and delete user data.
-   Delete the user information table after service A ends.

**Table  1**  User information

<a name="en-us_topic_0037446806_table27353390"></a>
<table><thead align="left"><tr id="en-us_topic_0037446806_row32789387"><th class="cellrowborder" valign="top" width="19.998000199980005%" id="mcps1.2.6.1.1"><p id="en-us_topic_0037446806_p38694667"><a name="en-us_topic_0037446806_p38694667"></a><a name="en-us_topic_0037446806_p38694667"></a><strong id="en-us_topic_0037446806_b682418185047"><a name="en-us_topic_0037446806_b682418185047"></a><a name="en-us_topic_0037446806_b682418185047"></a>ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.678432156784321%" id="mcps1.2.6.1.2"><p id="en-us_topic_0037446806_p22689808"><a name="en-us_topic_0037446806_p22689808"></a><a name="en-us_topic_0037446806_p22689808"></a><strong id="aa1f6a8bb4c0c4b02a43d11ecd84e321d"><a name="aa1f6a8bb4c0c4b02a43d11ecd84e321d"></a><a name="aa1f6a8bb4c0c4b02a43d11ecd84e321d"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.558244175582445%" id="mcps1.2.6.1.3"><p id="en-us_topic_0037446806_p32089967"><a name="en-us_topic_0037446806_p32089967"></a><a name="en-us_topic_0037446806_p32089967"></a><strong id="a56b3c0ab560b4a1fa37d07fd8ae3b38b"><a name="a56b3c0ab560b4a1fa37d07fd8ae3b38b"></a><a name="a56b3c0ab560b4a1fa37d07fd8ae3b38b"></a>Gender</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.2984701529847%" id="mcps1.2.6.1.4"><p id="en-us_topic_0037446806_p39701876"><a name="en-us_topic_0037446806_p39701876"></a><a name="en-us_topic_0037446806_p39701876"></a><strong id="a3bbfc04c5bdf4583ad6b108efeb8df4f"><a name="a3bbfc04c5bdf4583ad6b108efeb8df4f"></a><a name="a3bbfc04c5bdf4583ad6b108efeb8df4f"></a>Age</strong></p>
</th>
<th class="cellrowborder" valign="top" width="31.46685331466853%" id="mcps1.2.6.1.5"><p id="en-us_topic_0037446806_p18747312"><a name="en-us_topic_0037446806_p18747312"></a><a name="en-us_topic_0037446806_p18747312"></a><strong id="ac64afdd0bc00404984593c9180d9e96a"><a name="ac64afdd0bc00404984593c9180d9e96a"></a><a name="ac64afdd0bc00404984593c9180d9e96a"></a>Address</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0037446806_row43691456"><td class="cellrowborder" valign="top" width="19.998000199980005%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0037446806_p49347015"><a name="en-us_topic_0037446806_p49347015"></a><a name="en-us_topic_0037446806_p49347015"></a>12005000201</p>
</td>
<td class="cellrowborder" valign="top" width="15.678432156784321%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0037446806_p37685299"><a name="en-us_topic_0037446806_p37685299"></a><a name="en-us_topic_0037446806_p37685299"></a>A</p>
</td>
<td class="cellrowborder" valign="top" width="17.558244175582445%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0037446806_p32610412"><a name="en-us_topic_0037446806_p32610412"></a><a name="en-us_topic_0037446806_p32610412"></a>Male</p>
</td>
<td class="cellrowborder" valign="top" width="15.2984701529847%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0037446806_p24197721"><a name="en-us_topic_0037446806_p24197721"></a><a name="en-us_topic_0037446806_p24197721"></a>19</p>
</td>
<td class="cellrowborder" valign="top" width="31.46685331466853%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0037446806_p13858403"><a name="en-us_topic_0037446806_p13858403"></a><a name="en-us_topic_0037446806_p13858403"></a>City A</p>
</td>
</tr>
<tr id="en-us_topic_0037446806_row57616766"><td class="cellrowborder" valign="top" width="19.998000199980005%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0037446806_p36446461"><a name="en-us_topic_0037446806_p36446461"></a><a name="en-us_topic_0037446806_p36446461"></a>12005000202</p>
</td>
<td class="cellrowborder" valign="top" width="15.678432156784321%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0037446806_p66482253"><a name="en-us_topic_0037446806_p66482253"></a><a name="en-us_topic_0037446806_p66482253"></a>B</p>
</td>
<td class="cellrowborder" valign="top" width="17.558244175582445%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0037446806_p16353430"><a name="en-us_topic_0037446806_p16353430"></a><a name="en-us_topic_0037446806_p16353430"></a>Female</p>
</td>
<td class="cellrowborder" valign="top" width="15.2984701529847%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0037446806_p49559423"><a name="en-us_topic_0037446806_p49559423"></a><a name="en-us_topic_0037446806_p49559423"></a>23</p>
</td>
<td class="cellrowborder" valign="top" width="31.46685331466853%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0037446806_p54890288"><a name="en-us_topic_0037446806_p54890288"></a><a name="en-us_topic_0037446806_p54890288"></a>City B</p>
</td>
</tr>
<tr id="en-us_topic_0037446806_row24250547"><td class="cellrowborder" valign="top" width="19.998000199980005%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0037446806_p18137316"><a name="en-us_topic_0037446806_p18137316"></a><a name="en-us_topic_0037446806_p18137316"></a>12005000203</p>
</td>
<td class="cellrowborder" valign="top" width="15.678432156784321%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0037446806_p59836530"><a name="en-us_topic_0037446806_p59836530"></a><a name="en-us_topic_0037446806_p59836530"></a>C</p>
</td>
<td class="cellrowborder" valign="top" width="17.558244175582445%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0037446806_p14920772"><a name="en-us_topic_0037446806_p14920772"></a><a name="en-us_topic_0037446806_p14920772"></a>Male</p>
</td>
<td class="cellrowborder" valign="top" width="15.2984701529847%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0037446806_p623043"><a name="en-us_topic_0037446806_p623043"></a><a name="en-us_topic_0037446806_p623043"></a>26</p>
</td>
<td class="cellrowborder" valign="top" width="31.46685331466853%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0037446806_p50466518"><a name="en-us_topic_0037446806_p50466518"></a><a name="en-us_topic_0037446806_p50466518"></a>City C</p>
</td>
</tr>
<tr id="en-us_topic_0037446806_row51545483"><td class="cellrowborder" valign="top" width="19.998000199980005%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0037446806_p14434584"><a name="en-us_topic_0037446806_p14434584"></a><a name="en-us_topic_0037446806_p14434584"></a>12005000204</p>
</td>
<td class="cellrowborder" valign="top" width="15.678432156784321%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0037446806_p28350637"><a name="en-us_topic_0037446806_p28350637"></a><a name="en-us_topic_0037446806_p28350637"></a>D</p>
</td>
<td class="cellrowborder" valign="top" width="17.558244175582445%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0037446806_p14700275"><a name="en-us_topic_0037446806_p14700275"></a><a name="en-us_topic_0037446806_p14700275"></a>Male</p>
</td>
<td class="cellrowborder" valign="top" width="15.2984701529847%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0037446806_p49871633"><a name="en-us_topic_0037446806_p49871633"></a><a name="en-us_topic_0037446806_p49871633"></a>18</p>
</td>
<td class="cellrowborder" valign="top" width="31.46685331466853%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0037446806_p13070512"><a name="en-us_topic_0037446806_p13070512"></a><a name="en-us_topic_0037446806_p13070512"></a>City D</p>
</td>
</tr>
<tr id="en-us_topic_0037446806_row50525752"><td class="cellrowborder" valign="top" width="19.998000199980005%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0037446806_p66054074"><a name="en-us_topic_0037446806_p66054074"></a><a name="en-us_topic_0037446806_p66054074"></a>12005000205</p>
</td>
<td class="cellrowborder" valign="top" width="15.678432156784321%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0037446806_p48779793"><a name="en-us_topic_0037446806_p48779793"></a><a name="en-us_topic_0037446806_p48779793"></a>E</p>
</td>
<td class="cellrowborder" valign="top" width="17.558244175582445%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0037446806_p58849189"><a name="en-us_topic_0037446806_p58849189"></a><a name="en-us_topic_0037446806_p58849189"></a>Female</p>
</td>
<td class="cellrowborder" valign="top" width="15.2984701529847%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0037446806_p2055005"><a name="en-us_topic_0037446806_p2055005"></a><a name="en-us_topic_0037446806_p2055005"></a>21</p>
</td>
<td class="cellrowborder" valign="top" width="31.46685331466853%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0037446806_p32237730"><a name="en-us_topic_0037446806_p32237730"></a><a name="en-us_topic_0037446806_p32237730"></a>City E</p>
</td>
</tr>
<tr id="en-us_topic_0037446806_row21704116"><td class="cellrowborder" valign="top" width="19.998000199980005%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0037446806_p13202999"><a name="en-us_topic_0037446806_p13202999"></a><a name="en-us_topic_0037446806_p13202999"></a>12005000206</p>
</td>
<td class="cellrowborder" valign="top" width="15.678432156784321%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0037446806_p62809978"><a name="en-us_topic_0037446806_p62809978"></a><a name="en-us_topic_0037446806_p62809978"></a>F</p>
</td>
<td class="cellrowborder" valign="top" width="17.558244175582445%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0037446806_p54443429"><a name="en-us_topic_0037446806_p54443429"></a><a name="en-us_topic_0037446806_p54443429"></a>Male</p>
</td>
<td class="cellrowborder" valign="top" width="15.2984701529847%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0037446806_p47841633"><a name="en-us_topic_0037446806_p47841633"></a><a name="en-us_topic_0037446806_p47841633"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="31.46685331466853%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0037446806_p49967061"><a name="en-us_topic_0037446806_p49967061"></a><a name="en-us_topic_0037446806_p49967061"></a>City F</p>
</td>
</tr>
<tr id="en-us_topic_0037446806_row47050372"><td class="cellrowborder" valign="top" width="19.998000199980005%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0037446806_p52983808"><a name="en-us_topic_0037446806_p52983808"></a><a name="en-us_topic_0037446806_p52983808"></a>12005000207</p>
</td>
<td class="cellrowborder" valign="top" width="15.678432156784321%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0037446806_p63830089"><a name="en-us_topic_0037446806_p63830089"></a><a name="en-us_topic_0037446806_p63830089"></a>G</p>
</td>
<td class="cellrowborder" valign="top" width="17.558244175582445%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0037446806_p2854726"><a name="en-us_topic_0037446806_p2854726"></a><a name="en-us_topic_0037446806_p2854726"></a>Female</p>
</td>
<td class="cellrowborder" valign="top" width="15.2984701529847%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0037446806_p29906272"><a name="en-us_topic_0037446806_p29906272"></a><a name="en-us_topic_0037446806_p29906272"></a>29</p>
</td>
<td class="cellrowborder" valign="top" width="31.46685331466853%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0037446806_p6488958"><a name="en-us_topic_0037446806_p6488958"></a><a name="en-us_topic_0037446806_p6488958"></a>City G</p>
</td>
</tr>
<tr id="en-us_topic_0037446806_row58400626"><td class="cellrowborder" valign="top" width="19.998000199980005%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0037446806_p32830290"><a name="en-us_topic_0037446806_p32830290"></a><a name="en-us_topic_0037446806_p32830290"></a>12005000208</p>
</td>
<td class="cellrowborder" valign="top" width="15.678432156784321%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0037446806_p42007851"><a name="en-us_topic_0037446806_p42007851"></a><a name="en-us_topic_0037446806_p42007851"></a>H</p>
</td>
<td class="cellrowborder" valign="top" width="17.558244175582445%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0037446806_p47192740"><a name="en-us_topic_0037446806_p47192740"></a><a name="en-us_topic_0037446806_p47192740"></a>Female</p>
</td>
<td class="cellrowborder" valign="top" width="15.2984701529847%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0037446806_p64515557"><a name="en-us_topic_0037446806_p64515557"></a><a name="en-us_topic_0037446806_p64515557"></a>30</p>
</td>
<td class="cellrowborder" valign="top" width="31.46685331466853%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0037446806_p58377623"><a name="en-us_topic_0037446806_p58377623"></a><a name="en-us_topic_0037446806_p58377623"></a>City H</p>
</td>
</tr>
<tr id="en-us_topic_0037446806_row55636561"><td class="cellrowborder" valign="top" width="19.998000199980005%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0037446806_p10267631"><a name="en-us_topic_0037446806_p10267631"></a><a name="en-us_topic_0037446806_p10267631"></a>12005000209</p>
</td>
<td class="cellrowborder" valign="top" width="15.678432156784321%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0037446806_p26371793"><a name="en-us_topic_0037446806_p26371793"></a><a name="en-us_topic_0037446806_p26371793"></a>I</p>
</td>
<td class="cellrowborder" valign="top" width="17.558244175582445%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0037446806_p55740512"><a name="en-us_topic_0037446806_p55740512"></a><a name="en-us_topic_0037446806_p55740512"></a>Male</p>
</td>
<td class="cellrowborder" valign="top" width="15.2984701529847%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0037446806_p18687619"><a name="en-us_topic_0037446806_p18687619"></a><a name="en-us_topic_0037446806_p18687619"></a>26</p>
</td>
<td class="cellrowborder" valign="top" width="31.46685331466853%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0037446806_p37302179"><a name="en-us_topic_0037446806_p37302179"></a><a name="en-us_topic_0037446806_p37302179"></a>City I</p>
</td>
</tr>
<tr id="en-us_topic_0037446806_row175293"><td class="cellrowborder" valign="top" width="19.998000199980005%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0037446806_p14198754"><a name="en-us_topic_0037446806_p14198754"></a><a name="en-us_topic_0037446806_p14198754"></a>12005000210</p>
</td>
<td class="cellrowborder" valign="top" width="15.678432156784321%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0037446806_p9248440"><a name="en-us_topic_0037446806_p9248440"></a><a name="en-us_topic_0037446806_p9248440"></a>J</p>
</td>
<td class="cellrowborder" valign="top" width="17.558244175582445%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0037446806_p10926182"><a name="en-us_topic_0037446806_p10926182"></a><a name="en-us_topic_0037446806_p10926182"></a>Male</p>
</td>
<td class="cellrowborder" valign="top" width="15.2984701529847%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0037446806_p12605589"><a name="en-us_topic_0037446806_p12605589"></a><a name="en-us_topic_0037446806_p12605589"></a>25</p>
</td>
<td class="cellrowborder" valign="top" width="31.46685331466853%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0037446806_p14419821"><a name="en-us_topic_0037446806_p14419821"></a><a name="en-us_topic_0037446806_p14419821"></a>City J</p>
</td>
</tr>
</tbody>
</table>

## Procedure<a name="sa2e3c55dc02b463c8f36a5e01d263e0e"></a>

1.  Download the client file or the client configuration file.
    1.  Log in to the MRS management console. In the navigation tree on the left, choose  **Clusters \> Active Clusters** and click the cluster named **mrs\_20160907**. The **mrs\_20160907** cluster was created in section [Creating a Cluster](creating-a-cluster_quick-start.md).
    2.  In the  **Cluster List \> mrs\_20160907** area, click **View**  to open MRS Manager.
    3.  Click  **Service**, and click **Download Client**.

        Set  **Client Type** to **All client files** or **Only configuration files**, set **Download Path** to **Server**, and click **OK** to generate the client file or the client configuration file. The generated file is saved in the **/tmp/MRS-client**  directory on the active management node by default. You can modify the file save path as required.

2.  Log in to the active management node.
    1.  In the  **Cluster List \> mrs\_20160907**Choose  **Clusters \> Active Clusters**  and click the cluster named  **mrs\_20160907**. In the  **Cluster List \> mrs\_20160907**  area to view the  **Active Master Node IP Address**  parameter.  **Active Master Node IP Address**  is the IP address of the active Master node in a cluster, which is also the IP address of the active management node of MRS Manager.

        The active and standby management nodes of MRS Manager are installed on Master nodes by default. Because Master1 and Master2 are switched over in active and standby mode, Master1 is not always the active management node of MRS Manager.

    2.  Log in to the Master1 node using a  password as user **linux**. For details, see [Logging In to an ECS Using VNC](logging-in-to-an-ecs-using-vnc.md) in the _User Guide_.

        The Master node supports Cloud-init. The preset username for Cloud-init is  **linux**. The password is randomly generated and is displayed on the VNC login page by default. If you have changed the password, log in to the node using the new password. See "How Do I Log In to an ECS Once All Images Support Cloud-Init?" in the _Elastic Cloud Server User Guide_ \(**FAQs \> Login FAQs \> How Do I Log In to an ECS Once All Images Support Cloud-Init?**\).

    3.  Log in to the active management node as user **root**.

3.  Run the following command to go to the client directory:

    After an MRS cluster is successfully created, the client is installed in the /**opt/client**  directory by default.

    **cd /opt/client**

4.  Run the following command to update the client configuration for the active management node.

    Switch to user  **omm**.

    **sudo su - omm**

    **sh refreshConfig.sh /opt/client** _Full path of the client configuration file package_

    For example, run the following command:

    **sh refreshConfig.sh /opt/client /tmp/MRS-Client/MRS\_Services\_Client.tar**

    If the following information is displayed, the configuration is updated successfully.

    ```
    ReFresh components client config is complete.
    Succeed to refresh components client config.
    ```

5.  Use the client on a Master node.
    1.  On the active management node where the client is updated, for example,  **node-master2-LJXDj**, run the following command to go to the client directory.

        **cd /opt/client**

    2.  Run the following command to configure environment variables.

        **source bigdata\_env**

    3.  If the Kerberos authentication is enabled for the current cluster, run the following command to authenticate users. If the Kerberos authentication is disabled for the current cluster, skip this step.

        **kinit** **_MRS cluster user_**

        For example,  **kinit admin**.

    4.  Run an HBase component client command directly.

        **hbase shell**

6.  Run commands on the HBase client to implement service A.
    1.  Create a user information table according to  [Table 1](#en-us_topic_0037446806_table27353390)  and add data to it.

        **create** '_user\_info_',\{**NAME**  =\> 'i'\}

        For example, to add data of user 12005000201, run the following commands in sequence:

        **put** '_user\_info_','_12005000201_','_**i:name**_','_A_'

        **put** '_user\_info_','_12005000201_','_**i:gender**_','_Male_'

        **put** '_user\_info_','_12005000201_','_**i:age**_','_19_'

        **put** '_user\_info_','_12005000201_','_**i:address**_','_City A_'

    2.  Add degree and title information about the user to the table.

        For example, to add degree and title information about user 12005000201, run the following commands:

        **put** '_user\_info_','_12005000201_','**i:degree**','_master_'

        **put** '_user\_info_','_12005000201_','**i:pose**','_manager_'

    3.  Query usernames and addresses by user ID.

        For example, to query the username and address of user 12005000201, run the following command:

        **scan**'_user\_info_',\{**STARTROW**=\>'_12005000201_',**STOPROW**=\>'_12005000201_',**COLUMNS**=\>\['**i:name**','**i:address**'\]\}

    4.  Query information by username.

        For example, to query information about user A, run the following command:

        **scan**'_user\_info_',\{**FILTER**=\>"SingleColumnValueFilter\('i','name',=,'binary:_A_'\)"\}

    5.  Delete user data from the user information table.

        All user data needs to be deleted. For example, to delete data of user 12005000201, run the following command:

        **delete**'_user\_info_','_12005000201_','i'

    6.  Run the following command to delete the user information table.

        **disable**'_user\_info_';**drop** '_user\_info_'

7.  Terminate a cluster.

    For details, see  [Terminating a Cluster](terminating-a-cluster.md) in the _User Guide_.


