# Creating a Cluster<a name="EN-US_TOPIC_0125375856"></a>

## Procedure<a name="s561ee4f7ae984b82b1b3d1edf1609be0"></a>

1.  Log in to the MRS management console.
2.  Click  ![](figures/dt_mrs_project_region_image01.png) in the upper-left corner on the management console and select **Region** and **Project**.
3.  Click  **Create Cluster** and open the **Create Cluster**  page.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Note the usage of quotas when you create a cluster. If the resource quotas are insufficient, apply for new quotas based on the prompted information and create new clusters.  

4.  [Table 1](#table1226616581314), [Table 2](#table57941243154250), [Table 3](#table19676791228), [Table 4](#table2774903118058), [Table 5](#table56762022141941), and [Table 6](#table18305573153324)  describe the basic configuration information, node configuration information, login information, component information and job configuration information for a cluster, respectively.

    **Table  1**  Basic cluster configuration information

    <a name="table1226616581314"></a>
    <table><thead align="left"><tr id="row82667581019"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p42668581716"><a name="p42668581716"></a><a name="p42668581716"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p0268105810113"><a name="p0268105810113"></a><a name="p0268105810113"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row32781258414"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p11278858514"><a name="p11278858514"></a><a name="p11278858514"></a>Region</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p02793581316"><a name="p02793581316"></a><a name="p02793581316"></a>To change the region, click <a name="image1827911581316"></a><a name="image1827911581316"></a><span><img id="image1827911581316" src="figures/dt_mrs_project_region_image01.png"></span> in the upper left corner to select one.</p>
    </td>
    </tr>
    <tr id="row1828019581517"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p11280658315"><a name="p11280658315"></a><a name="p11280658315"></a>AZ</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p122801758218"><a name="p122801758218"></a><a name="p122801758218"></a>An availability zone (AZ) is a physical area that uses independent power and network resources. In this way, applications are interconnected using internal networks but are physically isolated. As a result, application availability is improved. It is recommended that you create clusters under different AZs.</p>
    <p id="p22801658319"><a name="p22801658319"></a><a name="p22801658319"></a>MRS enables an AZ to be randomly selected to prevent excessive VMs to be created in the specified default AZ and avoid uneven resource occupation among AZs. MRS also enables a tenant's all VMs to be created in one AZ as much as possible.</p>
    <p id="p1928017581119"><a name="p1928017581119"></a><a name="p1928017581119"></a>If your VMs must be located in different AZs, specify AZs when creating VMs. In a multi-user and multi-AZ scenario, each user tries to obtain a default AZ that is different from other users' default AZs.</p>
    <p id="p9280185815112"><a name="p9280185815112"></a><a name="p9280185815112"></a>Select an AZ of the region in the cluster. Currently, only the <span class="parmvalue" id="parmvalue528025815110"><a name="parmvalue528025815110"></a><a name="parmvalue528025815110"></a><b>eu-de</b></span> region is supported.</p>
    </td>
    </tr>
    <tr id="row1528275810119"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p122821558314"><a name="p122821558314"></a><a name="p122821558314"></a>Cluster Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p5282358519"><a name="p5282358519"></a><a name="p5282358519"></a>Cluster name, which is globally unique.</p>
    <p id="p1428205812110"><a name="p1428205812110"></a><a name="p1428205812110"></a>A cluster name can contain only 1 to 64 characters, including letters, digits, hyphens (-), or underscores (_).</p>
    <p id="p12282958913"><a name="p12282958913"></a><a name="p12282958913"></a>The default name is <strong id="b32829581016"><a name="b32829581016"></a><a name="b32829581016"></a>mrs_xxxx</strong>, where&nbsp;<strong id="b122821458611"><a name="b122821458611"></a><a name="b122821458611"></a>xxxx</strong> is a random combination of four letters and numbers.</p>
    </td>
    </tr>
    <tr id="row728315819118"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1928325812111"><a name="p1928325812111"></a><a name="p1928325812111"></a>Cluster Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p18377143111717"><a name="p18377143111717"></a><a name="p18377143111717"></a>Currently, MRS 1.6.3, MRS 1.7.2 , MRS 1.9.2 and MRS 2.1.0 are supported.</p>
    <p id="p8284258219"><a name="p8284258219"></a><a name="p8284258219"></a>The latest version of MRS is used by default.</p>
    </td>
    </tr>
    <tr id="row15285175818112"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p428515581813"><a name="p428515581813"></a><a name="p428515581813"></a>Kerberos Authentication</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p4286958519"><a name="p4286958519"></a><a name="p4286958519"></a>Indicates whether to enable Kerberos authentication when logging in to MRS Manager. Possible values are as follows:</p>
    <a name="ul14288158116"></a><a name="ul14288158116"></a><ul id="ul14288158116"><li><a name="image42892588112"></a><a name="image42892588112"></a><span><img id="image42892588112" src="figures/icon_mrs_disable_dt.png"></span><p id="p3289125820118"><a name="p3289125820118"></a><a name="p3289125820118"></a>If Kerberos authentication is disabled, you can use all functions of an MRS cluster. You are advised to disable Kerberos authentication in single-user scenarios. For clusters with Kerberos authentication disabled, you can directly access the MRS cluster management page and components without security authentication. If Kerberos authentication is disabled, you can follow instructions in <a href="security-configuration-suggestions-for-clusters-with-kerberos-authentication-disabled.md">Security Configuration Suggestions for Clusters with Kerberos Authentication Disabled</a> to perform security configuration.</p>
    </li><li><a name="image19289125820112"></a><a name="image19289125820112"></a><span><img id="image19289125820112" src="figures/dt_enable.png"></span><p id="p62892583115"><a name="p62892583115"></a><a name="p62892583115"></a>If Kerberos authentication is enabled, common users cannot use the file management and job management functions of an MRS cluster and cannot view cluster resource usage or the job records for Hadoop and Spark. To use more cluster functions, the users must contact the MRS Manager administrator to assign more permissions. You are advised to enable Kerberos authentication in multi-user scenarios.</p>
    </li></ul>
    <p id="p1328918580112"><a name="p1328918580112"></a><a name="p1328918580112"></a>You can click <a name="image52891581716"></a><a name="image52891581716"></a><span><img id="image52891581716" src="figures/dt_enable.png"></span>&nbsp;or&nbsp;<a name="image5290858218"></a><a name="image5290858218"></a><span><img id="image5290858218" src="figures/icon_mrs_disable_dt.png"></span> to disable or enable Kerberos authentication, respectively.</p>
    <p id="p1629018581917"><a name="p1629018581917"></a><a name="p1629018581917"></a>After creating MRS clusters with Kerberos authentication enabled, users can manage running clusters on MRS Manager. The users must prepare a working environment on the public cloud platform for accessing MRS Manager. For details, see <a href="accessing-mrs-manager-supporting-kerberos-authentication.md">Accessing MRS Manager Supporting Kerberos Authentication</a><em id="i1729085810118"><a name="i1729085810118"></a><a name="i1729085810118"></a>.</em></p>
    <div class="note" id="note5290105820112"><a name="note5290105820112"></a><a name="note5290105820112"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p11290195820119"><a name="p11290195820119"></a><a name="p11290195820119"></a>The <span class="parmname" id="parmname192903586112"><a name="parmname192903586112"></a><a name="parmname192903586112"></a><b>Kerberos Authentication</b></span>,&nbsp;<span class="parmname" id="parmname1629013581014"><a name="parmname1629013581014"></a><a name="parmname1629013581014"></a><b>Username</b></span>,&nbsp;<span class="parmname" id="parmname22908580114"><a name="parmname22908580114"></a><a name="parmname22908580114"></a><b>Password</b></span>, and&nbsp;<span class="parmname" id="parmname122907588114"><a name="parmname122907588114"></a><a name="parmname122907588114"></a><b>Confirm Password</b></span> parameters are displayed only after the user obtains the permission for MRS in security mode.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row5290958513"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1529018586120"><a name="p1529018586120"></a><a name="p1529018586120"></a>Username</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1629075812117"><a name="p1629075812117"></a><a name="p1629075812117"></a>Indicates the username for the administrator of MRS Manager. <strong id="b15290658215"><a name="b15290658215"></a><a name="b15290658215"></a>admin</strong> is used by default.</p>
    <p id="p102900581815"><a name="p102900581815"></a><a name="p102900581815"></a>For clusters whose versions are earlier than MRS 1.9.2, this parameter needs to be configured only when <span class="parmname" id="parmname62927582112"><a name="parmname62927582112"></a><a name="parmname62927582112"></a><b>Kerberos Authentication</b></span>&nbsp;is set to "<span class="parmvalue" id="parmvalue129220581318"><a name="parmvalue129220581318"></a><a name="parmvalue129220581318"></a><b>Enable</b></span>":&nbsp;<a name="image202922587118"></a><a name="image202922587118"></a><span><img id="image202922587118" src="figures/dt_enable.png"></span>.</p>
    </td>
    </tr>
    <tr id="row1295185815112"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p42958581120"><a name="p42958581120"></a><a name="p42958581120"></a>Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1629713581411"><a name="p1629713581411"></a><a name="p1629713581411"></a><span>Indicates the password of the MRS Manager administrator.</span></p>
    <a name="ul12975581711"></a><a name="ul12975581711"></a><ul id="ul12975581711"><li>Must contain 8 to 32 characters.</li><li>Must contain at least three types of the following:<a name="ul152997581516"></a><a name="ul152997581516"></a><ul id="ul152997581516"><li>Lowercase letters</li><li>Uppercase letters</li><li>Digits</li><li>Special characters of `~!@#$%^&amp;*()-_=+\|[{}];:'",&lt;.&gt;/?</li><li>Spaces</li></ul>
    </li><li>Must be different from the username.</li><li>Must be different from the username written in reverse order.</li></ul>
    <p id="p1930412581912"><a name="p1930412581912"></a><a name="p1930412581912"></a>Password strength: The colorbar in red, orange, and green indicates weak, medium, and strong password, respectively.</p>
    <p id="p1530485814113"><a name="p1530485814113"></a><a name="p1530485814113"></a>For clusters whose versions are earlier than MRS 1.9.2, this parameter needs to be configured only when <span class="parmname" id="parmname113042588119"><a name="parmname113042588119"></a><a name="parmname113042588119"></a><b>Kerberos Authentication</b></span>&nbsp;is set to "<span class="parmvalue" id="parmvalue113041558015"><a name="parmvalue113041558015"></a><a name="parmvalue113041558015"></a><b>Enable</b></span>":&nbsp;<a name="image9304175812115"></a><a name="image9304175812115"></a><span><img id="image9304175812115" src="figures/dt_enable.png"></span>.</p>
    </td>
    </tr>
    <tr id="row17305125812120"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p730510581119"><a name="p730510581119"></a><a name="p730510581119"></a>Confirm Password</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p93056589120"><a name="p93056589120"></a><a name="p93056589120"></a>Enter the user password again.</p>
    <p id="p163053583117"><a name="p163053583117"></a><a name="p163053583117"></a>For clusters whose versions are earlier than MRS 1.9.2, this parameter needs to be configured only when <span class="parmname" id="parmname12305145817111"><a name="parmname12305145817111"></a><a name="parmname12305145817111"></a><b>Kerberos Authentication</b></span>&nbsp;is set to "<span class="parmvalue" id="parmvalue113051058117"><a name="parmvalue113051058117"></a><a name="parmvalue113051058117"></a><b>Enable</b></span>":&nbsp;<a name="image173057581120"></a><a name="image173057581120"></a><span><img id="image173057581120" src="figures/dt_enable.png"></span>.</p>
    </td>
    </tr>
    <tr id="row1430613581417"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p18306958713"><a name="p18306958713"></a><a name="p18306958713"></a>Cluster Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><div class="p" id="p1646587610513"><a name="p1646587610513"></a><a name="p1646587610513"></a>Provides three types of clusters:<a name="ul5866754210513"></a><a name="ul5866754210513"></a><ul id="ul5866754210513"><li>Analysis cluster: is used for offline data analysis and provides Hadoop components.</li><li>Streaming cluster: is used for streaming tasks and provides stream processing components.</li><li>Hybrid cluster: is used for both offline data analysis and streaming processing and provides Hadoop components and streaming processing components. You are advised to use a hybrid cluster to perform offline data analysis and streaming processing tasks at the same time. (MRS 1.9.2 or later supports hybrid clusters.)</li></ul>
    </div>
    <div class="note" id="note1730795818117"><a name="note1730795818117"></a><a name="note1730795818117"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p530710587118"><a name="p530710587118"></a><a name="p530710587118"></a>MRS streaming clusters do not support <span class="parmname" id="parmname118351333195019"><a name="parmname118351333195019"></a><a name="parmname118351333195019"></a><b>Jobs</b></span>&nbsp;or&nbsp;<span class="parmname" id="parmname96136138476"><a name="parmname96136138476"></a><a name="parmname96136138476"></a><b>Files</b></span>. If the cluster type is&nbsp;<strong id="b730725816117"><a name="b730725816117"></a><a name="b730725816117"></a>Streaming Cluster</strong>, the&nbsp;<span class="uicontrol" id="uicontrol630710587116"><a name="uicontrol630710587116"></a><a name="uicontrol630710587116"></a><b>Create Job</b></span> area is not displayed on the cluster creation page.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row113094582118"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p1530911584110"><a name="p1530911584110"></a><a name="p1530911584110"></a>Component</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p530128172211"><a name="p530128172211"></a><a name="p530128172211"></a>The MRS components are as follows:</p>
    <div class="p" id="p17754193712915"><a name="p17754193712915"></a><a name="p17754193712915"></a>Components of an analysis cluster:<a name="ul107601137694"></a><a name="ul107601137694"></a><ul id="ul107601137694"><li>Presto: open source and distributed SQL query engine</li><li>Hadoop: distributed system architecture</li><li>Spark: in-memory distributed computing framework</li><li>Hive: data warehouse framework built on Hadoop</li><li>OpenTSDB: a distributed, scalable time series database that can store and serve massive amounts of time series data without losing granularity (supported in MRS 1.9.2)</li><li>HBase: distributed column-oriented database</li><li>Tez: provides a distributed computing framework of directed acyclic graphs (DAGs). (supported in MRS 2.1.0 or later)</li><li>Hue: provides the Hadoop UI capability, which enables users to analyze and process Hadoop cluster data on browsers</li><li>Loader: a tool based on source Sqoop 1.99.7, designed for efficiently transferring bulk data between Apache Hadoop and structured datastores such as relational databases<p id="p148558372910"><a name="p148558372910"></a><a name="p148558372910"></a>Hadoop is mandatory, and Spark and Hive must be used together. Select components based on service requirements.</p>
    </li><li>Flink: a distributed big data processing engine that can perform stateful computations over both finite and infinite data streams (supported in MRS 1.9.2 or later)</li><li>Alluxio: Alluxio is a memory speed virtual distributed storage system (supported in MRS 1.9.2)</li><li>Ranger: Apache Ranger is a framework to enable, monitor and manage comprehensive data security across the Hadoop platform (supported in MRS 1.9.2)</li></ul>
    </div>
    <div class="p" id="p128580371792"><a name="p128580371792"></a><a name="p128580371792"></a>Components of a streaming cluster:<a name="ul1586213370918"></a><a name="ul1586213370918"></a><ul id="ul1586213370918"><li>Kafka: distributed messaging system</li><li>KafkaManager: Kafka cluster monitoring management tool (supported in MRS 1.9.2)</li><li>Storm: distributed real-time computing system</li><li>Flume: distributed, reliable, and available service for efficiently collecting, aggregating, and moving large amounts of log data</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row133219583113"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p93324581516"><a name="p93324581516"></a><a name="p93324581516"></a>VPC</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p143321758315"><a name="p143321758315"></a><a name="p143321758315"></a>A VPC is a secure, isolated, and logical network environment.</p>
    <p id="p143321458416"><a name="p143321458416"></a><a name="p143321458416"></a>Select the VPC for which you want to create a cluster and click <span class="uicontrol" id="uicontrol133322581910"><a name="uicontrol133322581910"></a><a name="uicontrol133322581910"></a><b>View VPC</b></span> to view the name and ID of the VPC. If no VPC is available, create one.</p>
    </td>
    </tr>
    <tr id="row93321958911"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p6332105818111"><a name="p6332105818111"></a><a name="p6332105818111"></a>Subnet</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p9333175813111"><a name="p9333175813111"></a><a name="p9333175813111"></a>A subnet provides dedicated network resources that are isolated from other networks, improving network security.</p>
    <p id="p133316581718"><a name="p133316581718"></a><a name="p133316581718"></a>Select the subnet for which you want to create a cluster to enter the VPC and view the name and ID of the subnet.</p>
    <p id="p533317581219"><a name="p533317581219"></a><a name="p533317581219"></a>If no subnet is created under the VPC, click <span class="uicontrol" id="uicontrol133331158210"><a name="uicontrol133331158210"></a><a name="uicontrol133331158210"></a><b>Create Subnet</b></span> to create one.</p>
    <div class="warning" id="note1233314588110"><a name="note1233314588110"></a><a name="note1233314588110"></a><span class="warningtitle"> WARNING: </span><div class="warningbody"><p id="p833355816112"><a name="p833355816112"></a><a name="p833355816112"></a>Do not associate the subnet with the network ACL.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row93338581715"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p233310588110"><a name="p233310588110"></a><a name="p233310588110"></a>Security Group</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1833310581119"><a name="p1833310581119"></a><a name="p1833310581119"></a>A security group is a set of ECS access rules. It provides access policies for ECSs that have the same security protection requirements and are mutually trusted in a VPC.</p>
    <p id="p23337581313"><a name="p23337581313"></a><a name="p23337581313"></a>When you create an MRS cluster, you can select <strong id="b333320583115"><a name="b333320583115"></a><a name="b333320583115"></a>Auto Create</strong>&nbsp;from the drop-down list of&nbsp;<strong id="b1333375817119"><a name="b1333375817119"></a><a name="b1333375817119"></a>Security Group</strong> to create a security group or select an existing security group.</p>
    </td>
    </tr>
    <tr id="row65108317237"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p12467163110352"><a name="p12467163110352"></a><a name="p12467163110352"></a>EIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p21911274314"><a name="p21911274314"></a><a name="p21911274314"></a>After binding an EIP to an MRS cluster, you can use the EIP to access the <strong id="b11862121892415"><a name="b11862121892415"></a><a name="b11862121892415"></a>MRS Manager</strong> page of the cluster.</p>
    <p id="p19997852143711"><a name="p19997852143711"></a><a name="p19997852143711"></a>When creating a cluster, you can select an available EIP from the drop-down list and bind it. If no EIP is available in the drop-down list, click <strong id="b9811515325"><a name="b9811515325"></a><a name="b9811515325"></a>Manage EIP</strong> to access the <strong id="b1978710233202"><a name="b1978710233202"></a><a name="b1978710233202"></a>EIPs</strong> page to create one.</p>
    <div class="note" id="note69611412419"><a name="note69611412419"></a><a name="note69611412419"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul1531291915418"></a><a name="ul1531291915418"></a><ul id="ul1531291915418"><li>This parameter is valid only in MRS 1.9.2 or later.</li><li>The EIP must be in the same region as the cluster.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row103342589115"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p19334195817110"><a name="p19334195817110"></a><a name="p19334195817110"></a>Cluster HA</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p2335358017"><a name="p2335358017"></a><a name="p2335358017"></a>Cluster HA specifies whether to enable high availability for a cluster. This parameter is enabled by default.</p>
    <p id="p6335658217"><a name="p6335658217"></a><a name="p6335658217"></a>If you enable this option, the management processes of all components will be deployed on both Master nodes to achieve hot standby and prevent single-node failure, improving reliability. If you disable this option, they will be deployed on only one Master node. As a result, if a process of a component becomes abnormal, the component will fail to provide services.</p>
    <a name="ul1335145816120"></a><a name="ul1335145816120"></a><ul id="ul1335145816120"><li><a name="image195037171120"></a><a name="image195037171120"></a><span><img id="image195037171120" src="figures/icon_mrs_disable_dt.png"></span>: Disabled. When&nbsp;<strong id="b183359581110"><a name="b183359581110"></a><a name="b183359581110"></a>Cluster HA</strong> is disabled, there is only one Master node and the number of Core nodes is three by default. However, you can decrease the number of Core nodes to 1.</li><li><a name="image6808826151111"></a><a name="image6808826151111"></a><span><img id="image6808826151111" src="figures/dt_enable.png"></span>: Enabled. When&nbsp;<strong id="b433619581712"><a name="b433619581712"></a><a name="b433619581712"></a>Cluster HA</strong> is enabled, there are two Master nodes and the number of Core nodes is three by default. However, you can decrease the number of Core nodes to 1.</li></ul>
    <p id="p143363581915"><a name="p143363581915"></a><a name="p143363581915"></a>You can click <a name="image45718336114"></a><a name="image45718336114"></a><span><img id="image45718336114" src="figures/dt_enable.png"></span>&nbsp;or&nbsp;<a name="image8800165141216"></a><a name="image8800165141216"></a><span><img id="image8800165141216" src="figures/icon_mrs_disable_dt.png"></span>: to disable or enable high availability, respectively.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Cluster node information

    <a name="table57941243154250"></a>
    <table><thead align="left"><tr id="row53863880154250"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p898179154250"><a name="p898179154250"></a><a name="p898179154250"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p5643687154250"><a name="p5643687154250"></a><a name="p5643687154250"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row40491593154250"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p58593568154250"><a name="p58593568154250"></a><a name="p58593568154250"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p48458588154250"><a name="p48458588154250"></a><a name="p48458588154250"></a>MRS provides three types of nodes:</p>
    <a name="ul33474116154250"></a><a name="ul33474116154250"></a><ul id="ul33474116154250"><li>Master: A Master node in an MRS cluster manages the cluster, assigns cluster executable files to Core nodes, traces the execution status of each job, and monitors the DataNode running status.</li><li>Core: A Core node in a cluster processes data and stores process data in HDFS.</li><li>Task: A Task node in a cluster is used for computing and does not store persistent data. Yarn and Storm are mainly installed on Task nodes. Task nodes are optional, and the number of Task nodes can be zero. (Task nodes are supported by MRS 1.6.3 or later.)<div class="p" id="p61082084103720"><a name="p61082084103720"></a><a name="p61082084103720"></a>When the number of clusters does not change much but the clusters' service processing capabilities need to be remarkably and temporarily improved, add Task nodes to address the following situations:<a name="ul12867850103720"></a><a name="ul12867850103720"></a><ul id="ul12867850103720"><li>The volume of temporary services is increased, for example, report processing at the end of the year.</li><li>Long-term tasks must be completed in a short time, for example, some urgent analysis tasks.</li></ul>
    </div>
    </li></ul>
    </td>
    </tr>
    <tr id="row54971833919"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p104971055191015"><a name="p104971055191015"></a><a name="p104971055191015"></a>Disk LVM</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p11167121719559"><a name="p11167121719559"></a><a name="p11167121719559"></a>This parameter is valid in the <strong id="b1777311306207"><a name="b1777311306207"></a><a name="b1777311306207"></a>Operation</strong> column of a streaming Core node only when the streaming Core node is created. Click this parameter to enable or disable the disk LVM function. The function status is displayed in the parentheses next to this parameter.</p>
    <p id="p3167131714551"><a name="p3167131714551"></a><a name="p3167131714551"></a>If LVM is enabled, all disks on a node are mounted as logical volumes. This delivers more proper disk planning to avoid data skew, thereby improving system stability.</p>
    </td>
    </tr>
    <tr id="row22792633193015"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p55868319193051"><a name="p55868319193051"></a><a name="p55868319193051"></a>(Optional) Configure Task Node</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p29040004193051"><a name="p29040004193051"></a><a name="p29040004193051"></a>Click <strong id="b765343613144"><a name="b765343613144"></a><a name="b765343613144"></a>Configure Task Node</strong> to configure the information about the Task node.</p>
    <p id="p12749861697"><a name="p12749861697"></a><a name="p12749861697"></a>Click <strong id="b1697617321281"><a name="b1697617321281"></a><a name="b1697617321281"></a>Auto Scaling</strong> in the <strong id="b84542389202"><a name="b84542389202"></a><a name="b84542389202"></a>Operation</strong> column of the Task node. On the <strong id="b226598849"><a name="b226598849"></a><a name="b226598849"></a>Auto Scaling</strong> page that is displayed, configure auto scaling rules. For details, see <a href="using-auto-scaling-in-a-cluster.md">Using Auto Scaling in a Cluster</a>.</p>
    <p id="p1010745745320"><a name="p1010745745320"></a><a name="p1010745745320"></a>Note:The <strong id="b14848121110189"><a name="b14848121110189"></a><a name="b14848121110189"></a>Auto Scaling</strong> parameter in the <strong id="b168491311201811"><a name="b168491311201811"></a><a name="b168491311201811"></a>Operation</strong> column of the Task node is used to configure an auto scaling rule. The content in the parentheses next to this parameter indicates the default node range when the auto scaling is enabled or is <strong id="b2849131119186"><a name="b2849131119186"></a><a name="b2849131119186"></a>Disabled</strong> when auto scaling is disabled.</p>
    </td>
    </tr>
    <tr id="row42113058154250"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p55714556154250"><a name="p55714556154250"></a><a name="p55714556154250"></a>Instance Specifications</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p12877360171321"><a name="p12877360171321"></a><a name="p12877360171321"></a>Instance specifications of a node. MRS supports host specifications determined by CPU, memory, and disk space.</p>
    <p id="p67151923143810"><a name="p67151923143810"></a><a name="p67151923143810"></a>MRS supports instance specifications detailed in <a href="ecs-specifications-used-by-mrs.md">ECS Specifications Used by MRS</a>.</p>
    <div class="note" id="note19219612154250"><a name="note19219612154250"></a><a name="note19219612154250"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul2523572017029"></a><a name="ul2523572017029"></a><ul id="ul2523572017029"><li>More advanced instance specifications allow better data processing.</li><li>If the specifications of Core nodes are d1.xlarge, d1.2xlarge, d1.4xlarge,&nbsp;or d1.8xlarge,&nbsp;<span class="parmname" id="parmname5771424293824"><a name="parmname5771424293824"></a><a name="parmname5771424293824"></a><b>Data Disk</b></span> is not displayed. This is because data disks are configured by default for these specifications. Other specifications do not have data disks. Users must manually add data disks if they are required.</li><li>If you select HDDs for Core nodes, there is no charging information for data disks. The fees are charged with ECSs.</li><li>If you select HDDs for Core nodes, the system disks (40 GB) of Master nodes and Core nodes, as well as the data disks (200 GB) of Master nodes, are SATA disks.</li><li>If you select non-HDD disks for Core nodes, the disk types of Master and Core nodes are determined by <strong id="b42177151233124"><a name="b42177151233124"></a><a name="b42177151233124"></a>Data Disk</strong>.</li><li>If <strong id="b96731537121614"><a name="b96731537121614"></a><a name="b96731537121614"></a>Sold Out</strong> appears next to an instance specification of a node, the node of this specification cannot be purchased. You can only purchase nodes of other specifications.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row21441724152911"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p3193172516291"><a name="p3193172516291"></a><a name="p3193172516291"></a>Instance&nbsp;Count</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p10193132562915"><a name="p10193132562915"></a><a name="p10193132562915"></a>Number of Master, Core, and Task nodes</p>
    <p id="p1450560795651"><a name="p1450560795651"></a><a name="p1450560795651"></a>For Master nodes:</p>
    <a name="ul7193825182917"></a><a name="ul7193825182917"></a><ul id="ul7193825182917"><li>If <strong id="b719362518294"><a name="b719362518294"></a><a name="b719362518294"></a>Cluster HA</strong> is enabled, the number of Master nodes is fixed to 2.</li><li>If <strong id="b17193925202910"><a name="b17193925202910"></a><a name="b17193925202910"></a>Cluster HA</strong> is disabled, the number of Master nodes is fixed to 1.</li></ul>
    <p id="p15193825142919"><a name="p15193825142919"></a><a name="p15193825142919"></a>The minimum number of Core nodes is 1 and the total number of Core and Task nodes cannot exceed 500.</p>
    <div class="note" id="note1619322552916"><a name="note1619322552916"></a><a name="note1619322552916"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul1619342513295"></a><a name="ul1619342513295"></a><ul id="ul1619342513295"><li>If more than 500 Core nodes and Task nodes are required, contact technical support engineers or invoke a background interface to modify the database.</li><li>A small number of nodes may cause clusters to run slowly while a large number of nodes may be unnecessarily costly. Set an appropriate value based on data to be processed.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row15933174992916"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0013363945_p49968442154250"><a name="en-us_topic_0013363945_p49968442154250"></a><a name="en-us_topic_0013363945_p49968442154250"></a>Data Disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0013363945_p24824775171417"><a name="en-us_topic_0013363945_p24824775171417"></a><a name="en-us_topic_0013363945_p24824775171417"></a>Disk space of Core nodes</p>
    <p id="en-us_topic_0013363945_p20912033154250"><a name="en-us_topic_0013363945_p20912033154250"></a><a name="en-us_topic_0013363945_p20912033154250"></a>Users can add disks to increase storage capacity when creating a cluster. There are two different configurations for storage and computing:</p>
    <a name="en-us_topic_0013363945_ul53990569154250"></a><a name="en-us_topic_0013363945_ul53990569154250"></a><ul id="en-us_topic_0013363945_ul53990569154250"><li>Data storage and computing are performed separately<p id="en-us_topic_0013363945_p9688203171457"><a name="en-us_topic_0013363945_p9688203171457"></a><a name="en-us_topic_0013363945_p9688203171457"></a>Data is stored in OBS, which features low cost and unlimited storage capacity. The clusters can be terminated at any time in OBS. The computing performance is determined by OBS access performance and is lower than that of HDFS. This configuration is recommended if data computing is infrequent.</p>
    </li><li>Data storage and computing are performed together<p id="en-us_topic_0013363945_p14436333171558"><a name="en-us_topic_0013363945_p14436333171558"></a><a name="en-us_topic_0013363945_p14436333171558"></a>Data is stored in HDFS, which features high cost, high computing performance, and limited storage capacity. Before terminating clusters, you must export and store the data. This configuration is recommended if data computing is frequent.</p>
    </li></ul>
    <p id="en-us_topic_0013363945_p33330714154250"><a name="en-us_topic_0013363945_p33330714154250"></a><a name="en-us_topic_0013363945_p33330714154250"></a>The following disk types are supported:</p>
    <a name="en-us_topic_0013363945_ul31540977154250"></a><a name="en-us_topic_0013363945_ul31540977154250"></a><ul id="en-us_topic_0013363945_ul31540977154250"><li>SATA: Common I/O</li><li>SAS: High I/O</li><li>SSD: Ultra-high I/O</li></ul>
    <p id="en-us_topic_0013363945_p43726395154250"><a name="en-us_topic_0013363945_p43726395154250"></a><a name="en-us_topic_0013363945_p43726395154250"></a>The disk sizes range from 100 GB to 32,000 GB, with 10 GB added each time, for example, 100 GB, 110 GB.</p>
    <div class="note" id="en-us_topic_0013363945_note57993243154250"><a name="en-us_topic_0013363945_note57993243154250"></a><a name="en-us_topic_0013363945_note57993243154250"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0013363945_ul506357631766"></a><a name="en-us_topic_0013363945_ul506357631766"></a><ul id="en-us_topic_0013363945_ul506357631766"><li>More nodes in a cluster require higher disk capacity of Master nodes. To ensure stable cluster running, set the disk capacity of the Master node to over 600 GB if the number of nodes is 300 and increase it to over 1 TB if the number of nodes reaches 500.</li><li>The Master node increases data disk storage space for MRS Manager. The disk type must be the same as the data disk type of Core nodes. The default disk space is 200 GB and cannot be changed.</li><li>If the specifications of Core nodes are d1.xlarge, d1.2xlarge, d1.4xlarge,&nbsp;or d1.8xlarge,&nbsp;<span class="parmname" id="parmname136124132115"><a name="parmname136124132115"></a><a name="parmname136124132115"></a><b>Data Disk</b></span> is not displayed. This applies to MRS 1.6.0 or earlier.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row17140232163017"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p195052356303"><a name="p195052356303"></a><a name="p195052356303"></a>Operation</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p1550518359305"><a name="p1550518359305"></a><a name="p1550518359305"></a>Only after you click <span class="uicontrol" id="uicontrol125057359302"><a name="uicontrol125057359302"></a><a name="uicontrol125057359302"></a><b>Configure Task Node</b></span>, Task nodes can be configured.</p>
    <p id="p195055352308"><a name="p195055352308"></a><a name="p195055352308"></a>If you do not need to configure a Task node, click <span class="parmname" id="parmname85059352305"><a name="parmname85059352305"></a><a name="parmname85059352305"></a><b>Delete</b></span> in the row of the Task node.</p>
    </td>
    </tr>
    <tr id="row4056436416658"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p2953495916658"><a name="p2953495916658"></a><a name="p2953495916658"></a>Auto Scaling</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p3069870716513"><a name="p3069870716513"></a><a name="p3069870716513"></a>After you have added a Task node, if you have not enabled the Auto Scaling function, <strong id="b15759087486"><a name="b15759087486"></a><a name="b15759087486"></a>Disabled</strong>&nbsp;is displayed in the&nbsp;<strong id="b17759383481"><a name="b17759383481"></a><a name="b17759383481"></a>Auto Scaling</strong>&nbsp;column. If you have enabled the Auto Scaling function,&nbsp;<strong id="b1675978194815"><a name="b1675978194815"></a><a name="b1675978194815"></a>Minimum</strong>&nbsp;<em id="i123641651142011"><a name="i123641651142011"></a><a name="i123641651142011"></a>xxx</em> and&nbsp;<strong id="b1375928184817"><a name="b1375928184817"></a><a name="b1375928184817"></a>Maximum</strong>&nbsp;<em id="i575913810482"><a name="i575913810482"></a><a name="i575913810482"></a>xxx</em>&nbsp;are displayed in the&nbsp;<strong id="b37599884817"><a name="b37599884817"></a><a name="b37599884817"></a>Auto Scaling</strong>&nbsp;column.&nbsp;<em id="i137597814814"><a name="i137597814814"></a><a name="i137597814814"></a>xxx</em>&nbsp;indicates the number of nodes. Click&nbsp;<a name="image1482736018325"></a><a name="image1482736018325"></a><span><img id="image1482736018325" src="figures/wwx437827-中软基础平台部-datasight-image-3410f4e5-0ef3-4377-8a08-65cd7bcb25d4.png"></span>&nbsp;. On the&nbsp;<strong id="b57591585486"><a name="b57591585486"></a><a name="b57591585486"></a>Auto Scaling</strong>&nbsp;page that is displayed, you can determine whether to enable or disable the Auto Scaling function and configure the auto scaling rule. For details, see&nbsp;<a href="using-auto-scaling-in-a-cluster.md">Using Auto Scaling in a Cluster</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Login information

    <a name="table19676791228"></a>
    <table><thead align="left"><tr id="row193501445183113"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p9350104513114"><a name="p9350104513114"></a><a name="p9350104513114"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p4350134512318"><a name="p4350134512318"></a><a name="p4350134512318"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1235013452315"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p193501445183113"><a name="p193501445183113"></a><a name="p193501445183113"></a>Login Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><a name="ul1355102835514"></a><a name="ul1355102835514"></a><ul id="ul1355102835514"><li>Key Pair<p id="p23505451315"><a name="p23505451315"></a><a name="p23505451315"></a>Keys are used to log in to Master1 of the cluster.</p>
    <p id="p1235094503112"><a name="p1235094503112"></a><a name="p1235094503112"></a>A key pair, also called an SSH key, consists of a public key and a private key. You can create an SSH key and download the private key for authenticating remote login. For security, a private key can only be downloaded once. Keep it secure.</p>
    <p id="p193501845153118"><a name="p193501845153118"></a><a name="p193501845153118"></a>Select the key pair, for example <i><span class="varname" id="varname5351174513112"><a name="varname5351174513112"></a><a name="varname5351174513112"></a>SSHkey-bba1.pem</span></i>, from the drop-down list. If you have obtained the private key file, select&nbsp;<strong id="b335114519314"><a name="b335114519314"></a><a name="b335114519314"></a>I acknowledge that I have obtained private key file</strong>&nbsp;<i><span class="varname" id="varname2351204583115"><a name="varname2351204583115"></a><a name="varname2351204583115"></a>SSHkey-bba1.pem</span></i> <strong id="b6795818214"><a name="b6795818214"></a><a name="b6795818214"></a>and that without this file I will not be able to log in to my ECS</strong>. If no key pair is created, click&nbsp;<span class="uicontrol" id="uicontrol2351154518319"><a name="uicontrol2351154518319"></a><a name="uicontrol2351154518319"></a><b>View Key Pair</b></span>&nbsp;to create or import keys. Then obtain the private key file.</p>
    <p id="p13511454317"><a name="p13511454317"></a><a name="p13511454317"></a>Configure an SSH key using either of the following two methods:</p>
    <a name="ol6375132119385"></a><a name="ol6375132119385"></a><ol id="ol6375132119385"><li><span>Create an SSH key</span><p id="p03511345113112"><a name="p03511345113112"></a><a name="p03511345113112"></a><span>After you create an SSH key, a public key and a private key are generated. The public key is stored in the system, and the private key is stored in the local ECS.</span>&nbsp;<span>When you log in to an ECS, the public and private keys are used for authentication.</span></p>
    </li><li><span>Import an SSH key</span><p id="p133511458314"><a name="p133511458314"></a><a name="p133511458314"></a><span>If you have obtained the public and private keys, import the public key into the system. When you log in to an ECS, the public and private keys are used for authentication.</span></p>
    </li></ol>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Log management information

    <a name="table2774903118058"></a>
    <table><thead align="left"><tr id="row132203418058"><th class="cellrowborder" valign="top" width="19.919999999999998%" id="mcps1.2.3.1.1"><p id="p4987022318110"><a name="p4987022318110"></a><a name="p4987022318110"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="80.08%" id="mcps1.2.3.1.2"><p id="p1295627218110"><a name="p1295627218110"></a><a name="p1295627218110"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2083152318058"><td class="cellrowborder" valign="top" width="19.919999999999998%" headers="mcps1.2.3.1.1 "><p id="p963176918058"><a name="p963176918058"></a><a name="p963176918058"></a>Logging</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.08%" headers="mcps1.2.3.1.2 "><p id="p4197582418058"><a name="p4197582418058"></a><a name="p4197582418058"></a>Indicates whether the tenant has enabled the log collection function.</p>
    <a name="ul6645300618641"></a><a name="ul6645300618641"></a><ul id="ul6645300618641"><li><a name="image36391075105013"></a><a name="image36391075105013"></a><span><img id="image36391075105013" src="figures/dt_enable.png"></span>: Enabled</li><li><a name="image37558765105243"></a><a name="image37558765105243"></a><span><img id="image37558765105243" src="figures/icon_mrs_disable_dt.png"></span>: Disabled</li></ul>
    <p id="p11522259162257"><a name="p11522259162257"></a><a name="p11522259162257"></a>You can click <a name="image57968561162554"></a><a name="image57968561162554"></a><span><img id="image57968561162554" src="figures/dt_enable.png"></span>&nbsp;or&nbsp;<a name="image5737583816318"></a><a name="image5737583816318"></a><span><img id="image5737583816318" src="figures/icon_mrs_disable_dt.png"></span> to disable or enable the log collection function, respectively.</p>
    </td>
    </tr>
    <tr id="row4223809918058"><td class="cellrowborder" valign="top" width="19.919999999999998%" headers="mcps1.2.3.1.1 "><p id="p6584286218058"><a name="p6584286218058"></a><a name="p6584286218058"></a>OBS Bucket</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.08%" headers="mcps1.2.3.1.2 "><p id="p50507154172426"><a name="p50507154172426"></a><a name="p50507154172426"></a>Indicates the log save path, for example, s3a://mrs_log_0adca19f25834f3597602094bec12990_eu-xx.</p>
    <p id="p4170861015404"><a name="p4170861015404"></a><a name="p4170861015404"></a>If an MRS cluster supporting log records fails to be created, you can use OBS to download related logs for troubleshooting.</p>
    <p id="p5874739716142"><a name="p5874739716142"></a><a name="p5874739716142"></a>Procedure:</p>
    <a name="ol6676817416257"></a><a name="ol6676817416257"></a><ol id="ol6676817416257"><li>Log in to the OBS management console.</li><li>Select the <span class="filepath" id="filepath640791541211"><a name="filepath640791541211"></a><a name="filepath640791541211"></a><b>mrs-log-&lt;tenant_id&gt;-&lt;region_id&gt;</b></span>&nbsp;bucket from the bucket list and go to the&nbsp;<span class="filepath" id="filepath13920245139"><a name="filepath13920245139"></a><a name="filepath13920245139"></a><b>/&lt;cluster_id&gt;/install_log</b></span>&nbsp;folder to download the&nbsp;<span class="filepath" id="filepath1073922311312"><a name="filepath1073922311312"></a><a name="filepath1073922311312"></a><b>YYYYMMDDHHMMSS.tar.gz</b></span>&nbsp;log, for example,&nbsp;/mrs_log_0adca19f25834f3597602094bec12990_eu-xx/65d0a20f-bcb7-4da3-81d3-71fef12d993d/20170818091516.tar.gz.</li></ol>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Component information

    <a name="table56762022141941"></a>
    <table><thead align="left"><tr id="row30114881141941"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p465067142437"><a name="p465067142437"></a><a name="p465067142437"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p44715211142034"><a name="p44715211142034"></a><a name="p44715211142034"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16983795103139"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p18636427103139"><a name="p18636427103139"></a><a name="p18636427103139"></a>Price Calculator</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p33155625103139"><a name="p33155625103139"></a><a name="p33155625103139"></a>Calculates the price for MRS configurations before they are ordered by the user.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  Job configuration information

    <a name="table18305573153324"></a>
    <table><thead align="left"><tr id="row29977293153324"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p2263811815359"><a name="p2263811815359"></a><a name="p2263811815359"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p2174827615359"><a name="p2174827615359"></a><a name="p2174827615359"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row28596456145742"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p42224797145742"><a name="p42224797145742"></a><a name="p42224797145742"></a>Configure</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p65953043111928"><a name="p65953043111928"></a><a name="p65953043111928"></a>After you click <span class="uicontrol" id="uicontrol15476737125217"><a name="uicontrol15476737125217"></a><a name="uicontrol15476737125217"></a><b>Configure</b></span>, the page for adding a tag or a bootstrap action is displayed.</p>
    <a name="ul265673984011"></a><a name="ul265673984011"></a><ul id="ul265673984011"><li>For details about how to add a tag, see <a href="managing-cluster-tags.md">Managing Cluster Tags</a>.</li><li>For details about how to add a bootstrap action, see <a href="bootstrap-actions.md">Bootstrap Actions</a>.</li></ul>
    </td>
    </tr>
    <tr id="row55480853145742"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p59445743145742"><a name="p59445743145742"></a><a name="p59445743145742"></a>Skip</p>
    </td>
    <td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p25228293145742"><a name="p25228293145742"></a><a name="p25228293145742"></a>You can add job configuration information later.</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **Create now**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >For details about the pricing, click  **Price Calculator**.  

6.  Confirm cluster specifications, and click  **Submit**  to submit a cluster creation task.
7.  Click  **Back to Cluster List**  to view the cluster status.

    For details about cluster status during cluster creation, see the  **Status**  parameter description in [Table 1](cluster-list.md#table3950169215120).

    Cluster creation takes some time. While the cluster is being created, its status is  **Starting**. After the cluster is created successfully, the cluster status becomes **Running**.

    Users can create a maximum of 10 clusters at a time and manage a maximum of 100 clusters on the MRS management console.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The name of a new cluster can be the same as that of a failed or terminated cluster.  


## Failed to Create a Cluster<a name="section50739391101333"></a>

If the cluster fails to be created, the failed task automatically switches to the  **Manage Failed Task**  page. You can click ![](figures/icon_mrs_critical.jpg) displayed in  [Figure 1](#fig5096054410932)  to access the **Manage Failed Task**  page and move the cursor over ![](figures/icon_mrs_critical.jpg) in the **Task Status**  column shown in  [Figure 2](#fig42978229101022)  to view the causes. For details about how to delete the failed task, see [Deleting a Failed Task](deleting-a-failed-task.md).

**Figure  1**  Managing failed tasks<a name="fig5096054410932"></a>  
![](figures/managing-failed-tasks.png "managing-failed-tasks")

**Figure  2**  Causes<a name="fig42978229101022"></a>  
![](figures/causes.png "causes")

[Table 7](#table41545811153550)  provides error codes about cluster creation failure.

**Table  7**  Error codes

<a name="table41545811153550"></a>
<table><thead align="left"><tr id="row63176370153550"><th class="cellrowborder" valign="top" width="19.919999999999998%" id="mcps1.2.3.1.1"><p id="p6886964153616"><a name="p6886964153616"></a><a name="p6886964153616"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="80.08%" id="mcps1.2.3.1.2"><p id="p27213325153628"><a name="p27213325153628"></a><a name="p27213325153628"></a>Message</p>
</th>
</tr>
</thead>
<tbody><tr id="row15807820153550"><td class="cellrowborder" valign="top" width="19.919999999999998%" headers="mcps1.2.3.1.1 "><p id="p21105754153616"><a name="p21105754153616"></a><a name="p21105754153616"></a>MRS.101</p>
</td>
<td class="cellrowborder" valign="top" width="80.08%" headers="mcps1.2.3.1.2 "><p id="p37050788153628"><a name="p37050788153628"></a><a name="p37050788153628"></a>Insufficient quota to meet your request. Contact customer service to increase the quota.</p>
</td>
</tr>
<tr id="row18828355153550"><td class="cellrowborder" valign="top" width="19.919999999999998%" headers="mcps1.2.3.1.1 "><p id="p18165449153616"><a name="p18165449153616"></a><a name="p18165449153616"></a>MRS.102</p>
</td>
<td class="cellrowborder" valign="top" width="80.08%" headers="mcps1.2.3.1.2 "><p id="p32261398153628"><a name="p32261398153628"></a><a name="p32261398153628"></a>The token cannot be null or invalid. Try again later or contact customer service.</p>
</td>
</tr>
<tr id="row2992003153550"><td class="cellrowborder" valign="top" width="19.919999999999998%" headers="mcps1.2.3.1.1 "><p id="p22166330153616"><a name="p22166330153616"></a><a name="p22166330153616"></a>MRS.103</p>
</td>
<td class="cellrowborder" valign="top" width="80.08%" headers="mcps1.2.3.1.2 "><p id="p30457324153628"><a name="p30457324153628"></a><a name="p30457324153628"></a>Invalid request. Try again later or contact customer service.</p>
</td>
</tr>
<tr id="row44281970153550"><td class="cellrowborder" valign="top" width="19.919999999999998%" headers="mcps1.2.3.1.1 "><p id="p53127826153616"><a name="p53127826153616"></a><a name="p53127826153616"></a>MRS.104</p>
</td>
<td class="cellrowborder" valign="top" width="80.08%" headers="mcps1.2.3.1.2 "><p id="p57464328153628"><a name="p57464328153628"></a><a name="p57464328153628"></a>Insufficient resources. Try again later or contact customer service.</p>
</td>
</tr>
<tr id="row43432126153550"><td class="cellrowborder" valign="top" width="19.919999999999998%" headers="mcps1.2.3.1.1 "><p id="p8371003153616"><a name="p8371003153616"></a><a name="p8371003153616"></a>MRS.105</p>
</td>
<td class="cellrowborder" valign="top" width="80.08%" headers="mcps1.2.3.1.2 "><p id="p15563988153628"><a name="p15563988153628"></a><a name="p15563988153628"></a>Insufficient IP addresses in the existing subnet. Try again later or contact customer service.</p>
</td>
</tr>
<tr id="row58399131153550"><td class="cellrowborder" valign="top" width="19.919999999999998%" headers="mcps1.2.3.1.1 "><p id="p62663656153616"><a name="p62663656153616"></a><a name="p62663656153616"></a>MRS.201</p>
</td>
<td class="cellrowborder" valign="top" width="80.08%" headers="mcps1.2.3.1.2 "><p id="p4749829153628"><a name="p4749829153628"></a><a name="p4749829153628"></a>Failed due to an ECS error. Try again later or contact customer service.</p>
</td>
</tr>
<tr id="row21320966153550"><td class="cellrowborder" valign="top" width="19.919999999999998%" headers="mcps1.2.3.1.1 "><p id="p47777876153616"><a name="p47777876153616"></a><a name="p47777876153616"></a>MRS.202</p>
</td>
<td class="cellrowborder" valign="top" width="80.08%" headers="mcps1.2.3.1.2 "><p id="p40073813153628"><a name="p40073813153628"></a><a name="p40073813153628"></a>Failed due to an IAM error. Try again later or contact customer service.</p>
</td>
</tr>
<tr id="row6411866515369"><td class="cellrowborder" valign="top" width="19.919999999999998%" headers="mcps1.2.3.1.1 "><p id="p571394153616"><a name="p571394153616"></a><a name="p571394153616"></a>MRS.203</p>
</td>
<td class="cellrowborder" valign="top" width="80.08%" headers="mcps1.2.3.1.2 "><p id="p21454407153628"><a name="p21454407153628"></a><a name="p21454407153628"></a>Failed due to a VPC error. Try again later or contact customer service.</p>
</td>
</tr>
<tr id="row2150128815369"><td class="cellrowborder" valign="top" width="19.919999999999998%" headers="mcps1.2.3.1.1 "><p id="p13893373153616"><a name="p13893373153616"></a><a name="p13893373153616"></a>MRS.300</p>
</td>
<td class="cellrowborder" valign="top" width="80.08%" headers="mcps1.2.3.1.2 "><p id="p3898087153628"><a name="p3898087153628"></a><a name="p3898087153628"></a>MRS system error. Try again later or contact customer service.</p>
</td>
</tr>
</tbody>
</table>

