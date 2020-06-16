# Using Hive from Scratch<a name="EN-US_TOPIC_0229290114"></a>

Hive is a data warehouse framework built on Hadoop. It maps structured data files to a database table and provides SQL-like functions to analyze and process data. It also allows you to quickly implements simple MapReduce statistics using SQL-like statements without the need of developing a specific MapReduce application. Therefore, it is suitable for statistics and analysis of data warehouses.

## **Background**<a name="section316983143915"></a>

After an MRS cluster is successfully created, the original client is stored in the  **/opt/client**  directory on all nodes in the cluster by default. Before using the client, download and update the client configuration file, and ensure that the active management node of MRS Manager is available.

Suppose a user develops an application to manage users who use service A in an enterprise. The procedure of operating service A on the Hive client is as follows:

**Operations on common tables**:

-   Create the  **user\_info**  table.
-   Add users' educational backgrounds and titles to the table.
-   Query user names and addresses by user ID.
-   Delete the user information table after service A ends.

**Table  1**  User information

<a name="en-us_topic_0037446806_table27353390"></a>
<table><thead align="left"><tr id="en-us_topic_0037446806_row32789387"><th class="cellrowborder" valign="top" width="19.998000199980005%" id="mcps1.2.6.1.1"><p id="en-us_topic_0037446806_p38694667"><a name="en-us_topic_0037446806_p38694667"></a><a name="en-us_topic_0037446806_p38694667"></a><strong id="en-us_topic_0037446806_b12707688"><a name="en-us_topic_0037446806_b12707688"></a><a name="en-us_topic_0037446806_b12707688"></a>ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.678432156784321%" id="mcps1.2.6.1.2"><p id="en-us_topic_0037446806_p22689808"><a name="en-us_topic_0037446806_p22689808"></a><a name="en-us_topic_0037446806_p22689808"></a><strong id="b8423527069446"><a name="b8423527069446"></a><a name="b8423527069446"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.558244175582445%" id="mcps1.2.6.1.3"><p id="en-us_topic_0037446806_p32089967"><a name="en-us_topic_0037446806_p32089967"></a><a name="en-us_topic_0037446806_p32089967"></a><strong id="b8423527069443"><a name="b8423527069443"></a><a name="b8423527069443"></a>Gender</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15.2984701529847%" id="mcps1.2.6.1.4"><p id="en-us_topic_0037446806_p39701876"><a name="en-us_topic_0037446806_p39701876"></a><a name="en-us_topic_0037446806_p39701876"></a><strong id="b84235270694413"><a name="b84235270694413"></a><a name="b84235270694413"></a>Age</strong></p>
</th>
<th class="cellrowborder" valign="top" width="31.46685331466853%" id="mcps1.2.6.1.5"><p id="en-us_topic_0037446806_p18747312"><a name="en-us_topic_0037446806_p18747312"></a><a name="en-us_topic_0037446806_p18747312"></a><strong id="b84235270694420"><a name="b84235270694420"></a><a name="b84235270694420"></a>Address</strong></p>
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
<tr id="en-us_topic_0037446806_row175293"><td class="cellrowborder" valign="top" width="19.998000199980005%" headers="mcps1.2.6.1.1 "><p id="p20275141018126"><a name="p20275141018126"></a><a name="p20275141018126"></a>12005000210</p>
</td>
<td class="cellrowborder" valign="top" width="15.678432156784321%" headers="mcps1.2.6.1.2 "><p id="p7273191071210"><a name="p7273191071210"></a><a name="p7273191071210"></a>J</p>
</td>
<td class="cellrowborder" valign="top" width="17.558244175582445%" headers="mcps1.2.6.1.3 "><p id="p12194165416015"><a name="p12194165416015"></a><a name="p12194165416015"></a>Female</p>
</td>
<td class="cellrowborder" valign="top" width="15.2984701529847%" headers="mcps1.2.6.1.4 "><p id="p127221061217"><a name="p127221061217"></a><a name="p127221061217"></a>25</p>
</td>
<td class="cellrowborder" valign="top" width="31.46685331466853%" headers="mcps1.2.6.1.5 "><p id="p2270910101219"><a name="p2270910101219"></a><a name="p2270910101219"></a>City J</p>
</td>
</tr>
</tbody>
</table>

## Procedure<a name="section16880721113918"></a>

1.  <a name="l6b58a848ef0f4fe6a361d4ef0ac39fb8"></a>Download the client configuration file.
    1.  Log in to the MRS management console. In the navigation tree on the left, choose  **Clusters**  \>  **Active Clusters**  and click the cluster named  **mrs\_20180707**. The  **mrs\_20180707**  cluster was created in  [Creating a Cluster](creating-a-cluster.md).
    2.  Click  **Services**.
    3.  Click  **Services**, and click  **Download Client**.

        Set  **Client Type**  to  **Only configuration files**, and click  **OK**  to generate the client configuration file. The generated file is saved in the  **/tmp/MRS-client**  directory on the active management node by default. You can customize the file path.

2.  Log in to the active management node of MRS Manager.
    1.  In the MRS management console, choose  **Clusters**  \>  **Active Clusters**  and click the cluster name. Select  **Nodes**  to view the  **Node**  parameter. The node that contains  **master1**  in its name is the Master1 node. The node that contains  **master2**  in its name is the Master2 node.

        The active and standby management nodes of MRS Manager are installed on Master nodes by default. Because Master1 and Master2 are switched over in active and standby mode, Master1 is not always the active management node of MRS Manager. Run a command in Master1 to check whether Master1 is the active management node of MRS Manager. For details about the command, see  [2.d](#le8e7045cece741e8b6209b929a50ff22).

    2.  For clusters whose versions are earlier than MRS 1.9.2, log in to the Master1 node using a password as user  **linux**. For clusters whose versions are MRS 1.9.2 or later, log in to the Master1 node using a password as user  **root**. For details, see  [Logging In to an ECS Using VNC](logging-in-to-an-ecs-using-vnc.md)  in the  _User Guide_.
    3.  Run the following command to switch to user  **omm**:

        **sudo su - root**

        **su - omm**

    4.  <a name="le8e7045cece741e8b6209b929a50ff22"></a>Run the following command to check the active management node of MRS Manager:

        **sh $\{BIGDATA\_HOME\}/om-0.0.1/sbin/status-oms.sh**

        In the command output, the node whose  **HAActive**  is  **active**  is the active management node, and the node whose  **HAActive**  is  **standby**  is the standby management node. In the following example,  **mgtomsdat-sh-3-01-1**  is the active management node, and  **mgtomsdat-sh-3-01-2**  is the standby management node.

        ```
        Ha mode
        double
        NodeName              HostName                      HAVersion          StartTime                HAActive             HAAllResOK           HARunPhase 
        192-168-0-30          mgtomsdat-sh-3-01-1           V100R001C01        2014-11-18 23:43:02      active               normal               Actived    
        192-168-0-24          mgtomsdat-sh-3-01-2           V100R001C01        2014-11-21 07:14:02      standby              normal               Deactived
        ```

    5.  Log in to the active management node as user  **root**, for example, node  **192-168-0-30**.

3.  Run the following command to go to the client installation directory:

    After an MRS cluster is successfully created, the client is installed in the  **/opt/client**  directory by default.

    cd /opt/client

4.  <a name="li15639738131312"></a>Run the following command to update the client configuration for the active management node:

    Switch to user  **omm**.

    **sudo su - omm**

    **sh refreshConfig.sh /opt/client** _Full path of the client configuration file package_

    For example, run the following command:

    **sh refreshConfig.sh /opt/client /tmp/MRS-client/MRS\_Services\_Client.tar**

    If the following information is displayed, the configuration is updated successfully.

    ```
     ReFresh components client config is complete.
     Succeed to refresh components client config.
    ```

    >![](/images/icon-note.gif) **NOTE:**   
    >You can also refer to method 2 in  [Updating the Client](updating-the-client.md)  to perform operations in  [1](#l6b58a848ef0f4fe6a361d4ef0ac39fb8)  to  [4](#li15639738131312).  

5.  Use the client on a Master node.
    1.  On the active management node where the client is updated, for example, node  **192-168-0-30**, run the following command to go to the client directory.

        **cd /opt/client**

    2.  Run the following command to configure environment variables:

        **source bigdata\_env**

    3.  If Kerberos authentication has been enabled for the current cluster, run the following command to authenticate the current user. The current user must have a permission to create Hive tables. For details about how to configure a role with the corresponding permission, see  [Creating a Role](creating-a-role.md). For details about how to bind a role to a user, see  [Creating a User](creating-a-user.md). If the Kerberos authentication is disabled for the current cluster, skip this step.

        **kinit** **_MRS cluster user_**

        For example,  **kinit hiveuser**.

    4.  Run the client command of the Hive component directly.

        **beeline**

6.  Run the Hive client command to implement service A.

    **Operations on internal tables**:

    1.  Create the  **user\_info**  user information table according to  [Table 1](#en-us_topic_0037446806_table27353390)  and add data to it.

        ```
        create table user_info(id string,name string,gender string,age int,addr string);
        insert into table user_info(id,name,gender,age,addr) values("12005000201", "A", "Male", "19", "City A");
        ... (Other statements are the same.)
        ```

    2.  Add users' educational backgrounds and titles to the  **user\_info**  table.

        For example, to add educational background and title information about user 12005000201, run the following command:

        ```
        alter table user_info add columns(education string,technical string);
        ```

    3.  Query user names and addresses by user ID.

        For example, to query the name and address of user 12005000201, run the following command:

        ```
        select name,addr from user_info where id='12005000201';
        ```

    4.  Run the following command to delete the user information table.

        ```
        drop table user_info;
        ```

    **Operations on external partition tables**:

    Create an external partition table and import data.

    1.  Create a path for storing external table data.

        ```
        hdfs dfs -mkdir /hive/user_info
        ```

    2.  Create a table.

        ```
        create external table user_info(id string,name string,gender string,age int,addr string) partitioned by(year string) row format delimited fields terminated by ' ' lines terminated by '\n' stored as textfile location '/hive/user_info';
        ```

        >![](/images/icon-note.gif) **NOTE:**   
        >**fields terminated**  indicates delimiters, for example, spaces.  
        >**lines terminated**  indicates line breaks, for example,  **\\n**.  
        >**/hive/user\_info**  indicates the path of the data file.  

    3.  Import data.
        1.  Execute the insert statement to insert data.

            ```
            insert into user_info partition(year="2018") values ("12005000201", "A", "Male", "19", "City A");
            ```

        2.  Run the  **load data**  command to import file data.
            1.  Create a file based on the data in  [Table 1](#en-us_topic_0037446806_table27353390). For example, the file name is  **txt.log**. Fields are separated by space, and the line feed characters are used as the line breaks.
            2.  Upload the file to HDFS.

                ```
                hdfs dfs -put txt.log /tmp
                ```

            3.  Load data to the table.

                ```
                load data inpath '/tmp/txt.log' into table user_info partition (year='2011');
                ```


    4.  Query the imported data.

        ```
        select * from user_info;
        ```

    5.  Delete the user information table.

        ```
        drop table user_info;
        ```

7.  Delete the cluster.

    For details, see  [Terminating a Cluster](terminating-a-cluster.md)  in the  _User Guide_.


